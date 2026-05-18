---
name: enrichir-contact
description: >
  Enrichit une fiche Notion AgoraLive (Personnes ou Organisations) avec son
  mail et son téléphone, et attribue un niveau de confiance à chacune des deux
  valeurs (✅ Confirmé / 🟡 Probable / 🔴 Inférence / ⚪ Non trouvé). Dispatcher
  2-en-1 : pour une Personne → pipeline Clay
  (find-and-enrich-list-of-contacts + Email + custom phone) + fallback web
  pattern ; pour une Organisation → pipeline web scrape ciblé du site officiel
  (homepage + /contact + footer) + fallback Clay company. Optionnel pour les
  Sponsors (deals) : recherche d'un contact commercial nommé via Clay
  find-and-enrich-contacts-at-company avec filtre titre (Sales / Partnerships
  / Business Development), puis enrichit la fiche Personne créée. Écrit
  directement dans les champs canoniques existants (Email pro / Email
  générique, Téléphone / Téléphone standard) + 4 métadonnées (Confiance mail,
  Confiance tel, Date enrichissement, Source enrichissement). Skill mutualisé
  tous jumeaux AgoraLive (Pauline, Julie, Éloi, Michelle, Olivia, Philippine).
  À déclencher quand un membre demande : "enrichis cette fiche", "trouve le
  mail et le tel de X", "Éloi enrichis Henry Schein", "Michelle complète la
  fiche du Pr Dupont", "Olivia enrichis ce sponsor", "Pauline enrichis ces 3
  personnes", "Julie complète les contacts du congrès Y",
  "enrichir-contact". Anti-triggers : (1) la fiche est déjà enrichie avec
  confiance ≥ 🟡 ET la date d'enrichissement date de moins de 90 jours → ne
  pas re-déclencher Clay (coûte des crédits, pas de valeur ajoutée) ;
  (2) recherche d'un contact commercial à TROUVER (pas à enrichir) chez une
  orga déjà connue → utiliser directement Clay
  find-and-enrich-contacts-at-company en mode standalone, pas ce skill ;
  (3) demande de mass enrichment > 50 fiches → escalader à Paul pour
  validation budget Clay avant de lancer.
---

# enrichir-contact

## Mission

Enrichir une fiche Notion AgoraLive (Personne ou Organisation) avec **email + téléphone + niveaux de confiance**, pour que l'équipe puisse contacter les prospects sans avoir à googler ou à payer un enrichissement à chaque fois.

Skill mutualisé entre tous les jumeaux. Chaque jumeau l'invoque pour son humain.

## Quand déclencher

- L'humain (ou son jumeau) demande explicitement : *"enrichis cette fiche"*, *"trouve-moi le mail et le tel de…"*, *"complète les contacts de…"*
- Une fiche vient d'être créée par `notion-document-router` avec Email/Tel vides et l'humain veut la compléter avant un envoi
- Travail en batch sur une base : *"enrichis les 12 nouveaux sponsors de la semaine"*

## Anti-triggers stricts

1. **Fiche déjà enrichie avec confiance ≥ 🟡 ET date d'enrichissement < 90 jours** → ne pas re-déclencher. Coûte des crédits Clay sans valeur ajoutée. Sortir avec un message *"Déjà enrichie il y a X jours, confiance actuelle Y — re-enrichir ? (oui/non)"*.
2. **Recherche d'un contact à trouver chez une orga déjà connue** (ex : *"trouve-moi un Sales chez Align Technology"*) → ce n'est pas un enrichissement, c'est une recherche de personne. Invoquer directement `find-and-enrich-contacts-at-company` en standalone.
3. **Demande de mass enrichment > 50 fiches** → escalader à Paul pour validation budget Clay avant de lancer.

## Inputs attendus

L'humain fournit (au moins l'un des deux) :
- **ID Notion** de la fiche à enrichir (Personne ou Organisation), OU
- **Nom de l'entité + base d'appartenance** (ex : *"Henry Schein, Organisations"* ou *"Pr Finn Geoghegan, Personnes, lié à EOS"*)

Si l'entité n'existe pas encore dans Notion → créer d'abord la fiche (déléguer à `notion-document-router` si applicable), puis enrichir.

## Pipeline — dispatcher selon le type

### Personne

1. Fetch fiche Notion Personne → récupérer `Nom complet` + `Organisation rattachée` (relation)
2. Fetch fiche Organisation rattachée → récupérer `Site web` ou `Domaine`
3. Appel `mcp__clay__find-and-enrich-list-of-contacts` avec :
   - `contactName: "<Nom complet>"`
   - `companyIdentifier: "<domaine>"`
   - `dataPoints: { contactDataPoints: [{ type: "Email" }] }`
4. Si Clay ne renvoie pas le mail :
   - Web search pattern entreprise : `"first.last@<domaine>"` ou via RocketReach
   - Si pattern confirmé → appliquer au nom (`firstname.lastname@domaine`)
5. Téléphone : Clay ne le sort pas en natif → custom data point Clay (*"Find direct phone number"*) OU fallback web sur site officiel orga (réception)
6. Calculer confiance (voir règles ci-dessous)
7. Mettre à jour la fiche Notion Personne

### Organisation

1. Fetch fiche Notion → récupérer `Nom` + `Site web`
2. Si pas de site web → web search pour le trouver, mettre à jour la fiche
3. **Web scrape ciblé** du site officiel :
   - Homepage
   - `/contact` ou `/contact-us`
   - `/about` ou `/about-us`
   - Footer (souvent où le mail générique + tel standard sont publiés)
4. Extraire : mail générique (`contact@`, `info@`, `hello@`, `partnerships@`, `sponsoring@`) + tel standard
5. Si rien trouvé → fallback Clay `find-and-enrich-company` avec custom data points (*"Find main contact email"* + *"Find main phone number"*)
6. Calculer confiance
7. Mettre à jour la fiche Notion

### Option Sponsor — recherche contact commercial nommé

La base **Sponsors** chez AgoraLive est une base de DEALS (un sponsor × un congrès × un montant), pas d'organisations. Les sponsors-orgas vivent dans **Organisations** avec `Type = Sponsor`.

Si l'humain demande *"enrichis Henry Schein ET trouve-moi le bon commercial"*, ajouter une étape après l'enrichissement de l'Organisation :

8. Appel `mcp__clay__find-and-enrich-contacts-at-company` avec :
   - `companyIdentifier: "<domaine>"`
   - `contactFilters: { job_title_keywords: ["Sales", "Partnerships", "Business Development", "Account Executive", "Key Account"] }`
   - `dataPoints: { contactDataPoints: [{ type: "Email" }] }`
9. Créer/mettre à jour une fiche Personne pour chaque contact retourné (max 3), liée à l'Organisation
10. Enrichir chaque fiche Personne créée (récursif sur le pipeline Personne ci-dessus)

## Règles de confiance

Appliquer la même grille aux deux variables (mail et tel) indépendamment :

| Niveau | Conditions |
|---|---|
| ✅ **Confirmé** | Valeur publiée en clair sur site officiel (footer, page contact, masthead) OU retournée par Clay avec source vérifiée OU saisie manuelle par l'humain |
| 🟡 **Probable** | Pattern entreprise confirmé (`first.last@`) appliqué à un nom OU Clay sans vérification croisée OU déduite par règle métier (ex : `EOSpartnerships@` est le pattern documenté pour les contacts sponsoring TFI Lodestar) |
| 🔴 **Inférence** | Guess sur convention sans confirmation (ex : tester `info@domaine` parce que c'est commun) |
| ⚪ **Non trouvé** | Pas de résultat exploitable |

**Règle de sécurité** : si confiance mail < 🟡 → **flagger dans la sortie chat** : *"Mail incertain, à valider avant envoi"*. Idem tel.

## Champs Notion à écrire

**Périmètre** : seulement les bases **Personnes** et **Organisations**. La base **Sponsors** (deals) n'est pas touchée — ses mails/tels sont sur les Personnes et Organisations liées.

### Pas de champ "Email enrichi" séparé

Le skill **écrit directement dans les champs canoniques existants** (`Email pro` + `Téléphone` sur Personnes ; `Email générique` + `Téléphone standard` sur Organisations). Pas de duplication. Les 4 champs de métadonnées ci-dessous indiquent la source et la confiance.

### Champs sur **Personnes** (data source `3c8396be-e935-4d83-8baa-28b3b8d497d1`)

Existant — alimentés par le skill :
- `Email pro` (email)
- `Téléphone` (phone_number)

Ajoutés pour le skill :
- `Confiance mail` (select : ✅ Confirmé / 🟡 Probable / 🔴 Inférence / ⚪ Non trouvé)
- `Confiance tel` (select : idem)
- `Date enrichissement` (date)
- `Source enrichissement` (multi-select : Clay / Web / Manuel / RocketReach / Site officiel)

### Champs sur **Organisations** (data source `f829e976-27cc-4fb8-97a9-ecba4c8444a7`)

Existant — alimentés par le skill :
- `Email générique` (email)
- `Téléphone standard` (phone_number)

Ajoutés pour le skill :
- `Confiance mail` (select)
- `Confiance tel` (select)
- `Date enrichissement` (date)
- `Source enrichissement` (multi-select)

### Règle de sécurité

⚠️ Ne JAMAIS écraser un mail/tel déjà saisi manuellement si `Confiance mail/tel = ✅ Confirmé` ET `Source enrichissement` contient `Manuel`. La saisie humaine vérifiée est sacrée.

## Output chat

Récap court structuré :

```
🔍 Enrichissement [Nom entité] — base [Personnes / Organisations]

Mail : <valeur> — <confiance> — <source>
Tel  : <valeur> — <confiance> — <source>

[Si confiance < 🟡 sur l'un des deux]
⚠️ À valider avant envoi à froid

✅ Fiche Notion mise à jour : <lien Notion>
```

Si batch (> 1 fiche) :
- Tableau Markdown avec une ligne par fiche
- Compte final : *"X/Y enrichies avec confiance ≥ 🟡, Z à valider manuellement"*

## Limites connues (à dire à l'humain si pertinent)

- **Clay couvre mal** : cabinets médicaux européens < 10 personnes, académiques niches, ONG, startups très early. Sur ces cas, le skill bascule automatiquement sur web scrape.
- **Tels persos européens : rares** parce que RGPD. On obtient surtout des tels standards d'orga, pas des portables directs.
- **Coût Clay** : chaque enrichissement Personne consomme des crédits. Budget mensuel à surveiller (voir avec Olivia côté admin abonnement).
- **Pas de re-enrichissement automatique** : la fiche se périme à 90 jours, mais le skill ne ré-enrichit qu'à la demande explicite (anti-trigger 1).

## Exemples d'invocation

```
[Pauline → Paul]
Paul : "Pauline enrichis Henry Schein"
→ Dispatcher détecte : base Organisations → pipeline web scrape officiel
→ Trouve contact@henryschein.fr, ✅ Confirmé + tel +33 ... ✅ Confirmé
→ Met à jour fiche Notion Organisation Henry Schein

[Éloi → Éloïse]
Éloïse : "Éloi trouve-moi les 3 commerciaux d'Align Technology + leurs mails"
→ Détecte : "trouve" + "commerciaux" = Option Sponsor recherche contact
→ Clay find-and-enrich-contacts-at-company avec filtre Sales/Partnerships
→ Crée 3 fiches Personne liées à Align Technology
→ Enrichit chacune
→ Récap chat avec 3 mails + 3 confiances

[Michelle → Michel]
Michel : "Michelle complète la fiche du Pr Finn Geoghegan"
→ Dispatcher détecte : base Personnes → pipeline Clay + fallback web
→ Clay rate (cabinet trop petit)
→ Bascule sur web scrape sop.ie : trouve format first.last@ + reception@
→ Applique finn.geoghegan@sop.ie 🟡 Probable
→ Flag : "Mail incertain, à valider avant envoi"
```

## Pré-requis avant 1er run

- [x] Connecteur Clay authentifié (`mcp__plugin_sales_clay__*`)
- [x] Connecteur Notion authentifié (`mcp__notion-*`)
- [x] Les 4 champs Notion créés sur les 2 bases (Personnes, Organisations) — fait au 19/05/2026
- [ ] Budget Clay validé par Paul (alerte si > 50 enrichissements/mois)

## Évolutions futures

- **V2** : hook dans `notion-document-router` pour enrichir automatiquement toute nouvelle fiche Personne/Organisation créée par le router avec Email/Tel vides
- **V3** : ajouter un cron mensuel qui re-checke les fiches dont la confiance est 🔴 ou ⚪ depuis > 30 jours pour voir si une source publique est apparue entre-temps
- **V4** : intégrer la validation RGPD côté Olivia (`audit-rgpd`) — avant d'écrire un tel perso européen dans Notion, vérifier base légale
