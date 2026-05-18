---
name: prospection-auto-hebdo
description: >
  Orchestrateur de prospection automatique hebdomadaire AgoraLive. Tourne tous
  les lundis matin (via scheduled task) et exécute trois flux : (1) scan des
  programmes officiels des congrès dentaires à venir 1-12 mois pour détecter
  les listes d'exposants nouvellement publiées, (2) veille RSS dentaire via
  Miniflux (Dental Tribune, Les Échos santé, Maddyness medtech, etc.) pour
  capter les sociétés "tendance" (levées, lancements, fusions),
  (3) enrichissement automatique des nouvelles sociétés détectées via
  `enrich-societe-notion` (API gouv recherche-entreprises ou fallback
  WebSearch). Sortie : brief Pauline du lundi matin listant les 5-15 nouveaux
  prospects qualifiés, en statut 🟡 Prospect dans le Hub Commercial, prêts
  pour Éloïse — AUCUN outbound automatique, validation humaine obligatoire.
  À déclencher quand Paul, Éloïse, Julien (ou jumeaux) demandent : "lance la
  prospection auto", "prospection hebdo", "Pauline prospection automatique",
  "scan les nouveaux prospects de la semaine", "brief prospection lundi",
  ou via la scheduled task `prospection-hebdo-lundi-8h`.
---

# prospection-auto-hebdo — Orchestrateur de prospection sortante hebdomadaire

## Mission

Maintenir un flux régulier de **5 à 15 nouveaux prospects qualifiés par semaine** dans le Hub Commercial AgoraLive, **sans intervention humaine** sur la phase de détection-enrichissement. Validation humaine d'Éloïse obligatoire AVANT tout outbound.

Le skill agit comme un chef d'orchestre — il appelle `enrich-societe-notion`, `enrich-personne-notion` et `find-prospects-congres` selon les sources, et consolide en un brief Pauline du lundi matin.

---

## Pré-requis

1. Base Congrès Notion : `c7ffc0cf7a3b427dab83c02f4fa4a03f`
2. Base Organisations : `06d3fc453c564f7eb6d9b862529d209a`
3. Hub Commercial : `35e6979fbcd181c3b6bed19cc2fbb275`
4. Skills appelés : `enrich-societe-notion`, `enrich-personne-notion`, `find-prospects-congres`, optionnellement `veille` pour la partie RSS
5. (Optionnel) Miniflux configuré pour la veille RSS dentaire (cf. skill `veille`)
6. Validation RGPD préalable : `audit-rgpd` invoqué par Olivia au moins une fois sur la chaîne complète

---

## Procédure (6 étapes)

### Étape 1 — Identifier les congrès à scanner cette semaine

`notion-query-database-view` sur la base Congrès avec filtre :
- Date congrès comprise entre J+30 et J+365 (cible la fenêtre où les programmes sont publiés mais le congrès pas encore passé)
- `Date dernier scan prospects` vide OU antérieure à J-7 (évite de rescanner ce qu'on a vu la semaine dernière)
- Statut ≠ Annulé, ≠ Pas pour nous

Sortie : liste de 5-30 congrès cibles selon la saison (forte densité en septembre-novembre et février-avril, creux en juillet-août).

### Étape 2 — Scanner les programmes pour détecter exposants

Pour chaque congrès :

1. Si `URL programme officiel` est rempli dans la fiche Notion → `WebFetch` ou `mcp__workspace__web_fetch`.
2. Sinon → `WebSearch` ciblé : `"programme officiel <NOM_CONGRÈS> <ANNÉE>"` et `"<NOM_CONGRÈS> exposants partenaires sponsors"`.
3. Détecter dans la page : présence des mots-clés "Sponsors", "Exposants", "Partenaires", "Avec le soutien de".
4. Extraire la liste brute des sociétés (cf. procédure de `find-prospects-congres` étape 2).
5. Si la page est JS-only et que WebFetch renvoie vide → escalader à `mcp__Claude_in_Chrome__navigate` + `get_page_text`.

**Anti-bruit** : si la même liste a déjà été parsée la semaine dernière (hash du contenu identique) → skip.

### Étape 3 — Filtre dédoublonnage Notion

Pour chaque société extraite :
1. `notion-search` dans Organisations + Hub Commercial.
2. Si déjà en base → ajouter une relation "Sponsorings historiques" vers le congrès courant (pas de doublon).
3. Si nouvelle → marquer comme candidat pour enrichissement.

### Étape 4 — Enrichissement des nouveaux candidats

Pour chaque société candidate, invoquer la procédure de `enrich-societe-notion` :
- API recherche-entreprises.api.gouv.fr (si proxy l'autorise) ou fallback WebSearch sur societe.com / annuaire-entreprises.data.gouv.fr / pappers.fr.
- Création fiche Organisations avec champs SIREN, dirigeants, adresse, NAF, effectif, CA si dispo, site, LinkedIn corporate.
- Ligne dans Hub Commercial : `🚦 Statut commercial = 🔍 À qualifier`, `🥇 Tier historique` selon le programme, `📝 Notes` avec argument matching pré-rédigé.

**Plafond hebdo dur** : 15 nouveaux prospects créés max par exécution. Au-delà → garder dans une "watchlist" pour la semaine suivante (évite de noyer Éloïse).

### Étape 5 — Veille RSS dentaire (optionnel)

Si Miniflux est configuré :
1. Lire les flux dentaires non lus via API Miniflux (cf. skill `veille`).
2. Pour chaque article, extraire les **noms d'entreprises mentionnés** (via inférence sur le titre + 1ère phrase, pas besoin de NER complexe).
3. Filtrer les noms : ne garder que ceux qui ressemblent à des fabricants/distributeurs dentaires (heuristique : présence de mots-clés "dentaire", "ortho", "implant", "DM", "medtech" dans le contexte).
4. Pour chaque société pertinente non en base → invoquer `enrich-societe-notion` + créer la fiche en `🟡 Prospect` avec `Origine du contact = LinkedIn` ou `Autre` (préciser presse + date article).
5. Marquer les articles comme lus dans Miniflux.

**Plafond RSS** : 5 nouvelles sociétés max via cette voie (pour ne pas noyer Éloïse non plus).

### Étape 6 — Mettre à jour les métadonnées + brief Pauline

1. Pour chaque congrès scanné → `notion-update-page` sur la fiche Congrès : `Date dernier scan prospects = aujourd'hui`.
2. Produire le brief dans Cowork (Pauline le verra le lundi matin) :

```
🐺 Brief prospection auto — Lundi <DATE>

📊 Cette semaine :
• <N_CONG> congrès scannés (programmes publiés détectés sur <X>)
• <N_NEW> nouveaux prospects créés (Hub Commercial → filtre "Créé cette semaine")
• <N_LINK> sponsorings historiques rattachés à des fiches existantes
• <N_RSS> prospects identifiés via veille RSS

🥇 TOP 5 priorité Éloïse :
1. <Société> — Tier <T> — Source : <Congrès ou Presse> — Contact identifié : <Personne/email/confiance>
   Argument matching : <1 phrase>
   👉 Action recommandée : <recommandation contextualisée>
2. ...
5. ...

🔜 Watchlist semaine prochaine (capacité dépassée) :
• <N> autres prospects en attente

⚠️ Compliance : aucun outbound déclenché automatiquement. Avant 1er contact :
1. Éloïse valide la TOP 5 (drop ou garde)
2. `mail-rediger` voix=eloise pour drafter le 1er message (mention RGPD obligatoire)
3. `validation-legale-message` Olivia avant envoi

📥 Vues Notion :
• Nouveaux prospects de la semaine : <URL filtre>
• Watchlist : <URL filtre>
• Logs scan : <URL page debug>
```

---

## Cas particuliers

### Période juillet-août (silence académique)
Si la fenêtre courante est entre le 15 juillet et le 25 août → ne scanne PAS les programmes (les congrès ne publient pas l'été et les exposants ne répondent pas). Brief allégé : "Période estivale — pas de scan. Relance prévue à partir du 26/08."

### Aucun nouveau programme détecté cette semaine
Brief court : "Pas de nouveaux programmes cette semaine. <N> prospects RSS détectés (si applicable). Bonne semaine."

### Quota proxy / API dépassé
Si l'API gouv ou WebSearch sature → finir ce qui a été commencé, marquer les congrès non traités avec `🚦 À rescanner`, et l'inclure dans le brief : "<N> congrès non scannés (cap technique atteint) — rescan automatique semaine prochaine."

### Société candidate sans SIREN trouvable (auto-entrepreneur, asso, marque commerciale d'un groupe)
Créer quand même la fiche en `🟡 Prospect` mais avec `🆔 SIREN non trouvé` et flag `À qualifier manuellement` pour qu'Éloïse décide.

### Détection d'un duplicat probable (nom similaire à une fiche existante mais SIREN différent)
Ne pas créer en automatique. Lister dans le brief sous "🤔 Doublons probables à arbitrer humainement".

### Volumétrie qui explose (>50 nouveaux candidats détectés)
Ne créer que les 15 premiers + 5 RSS = 20 max. Mettre les autres dans la watchlist. Alerter dans le brief.

---

## Création de la scheduled task

Une fois ce skill installé, créer la scheduled task qui le déclenche :

**Via Cowork — invoquer le skill `schedule`** avec :
- `taskName` : `prospection-hebdo-lundi-8h`
- `cronExpression` : `0 8 * * 1` (tous les lundis à 8h, heure locale Paul)
- `prompt` : self-contained, du type :
  > Lance le skill `prospection-auto-hebdo` pour la semaine en cours.
  > Scanne les congrès dentaires à venir, fais la veille RSS si configurée,
  > crée les nouvelles fiches prospect dans le Hub Commercial AgoraLive
  > et produit le brief Pauline complet. Volumétrie max : 15 prospects
  > congrès + 5 RSS. Aucun outbound automatique — uniquement détection
  > et enrichissement. Compliance RGPD : déjà validée par Olivia via
  > audit-rgpd (référence ticket Notion à compléter).

La tâche tourne en autonomie. Paul/Éloïse voient le brief en ouvrant Cowork le lundi matin.

---

## Compliance RGPD (validation Olivia obligatoire avant 1ère exécution)

- **Validation préalable** : invoquer `audit-rgpd` sur le pipeline complet (les 3 skills appelés + cette orchestration). Olivia donne son go.
- **Aucun outbound automatique** : le skill crée des fiches en `🟡 Prospect` mais n'envoie AUCUN message. La validation humaine d'Éloïse + Olivia reste obligatoire pour le 1er contact.
- **Volumétrie maîtrisée** : 15+5 max/semaine = ~80 prospects/mois. Sous le seuil 100/mois souvent recommandé en B2B intérêt légitime.
- **Traçabilité** : chaque fiche créée porte ses sources et la date dans `📝 Notes enrichissement`.
- **Effacement** : process formel à invoquer si une personne s'oppose (suppression fiche + log).

---

## Identifiants Notion utiles

- 🏛️ Base Congrès : `c7ffc0cf7a3b427dab83c02f4fa4a03f`
- 🏛️ Base Organisations : `06d3fc453c564f7eb6d9b862529d209a`
- 💼 Hub Commercial : `35e6979fbcd181c3b6bed19cc2fbb275`
- 👤 Base Personnes : `9d8d3c6b370d4c808502c0d6cd4c1e36`
- 🦊 Cockpit Paul : `3616979fbcd18186bf48cb87faa13af3` (pour le brief Pauline)
- 🦋 Cockpit Éloïse : `3616979fbcd181098eede7282c11e504`

## Skills appelés

- `enrich-societe-notion` — enrichissement légal + web pour chaque nouvelle société
- `enrich-personne-notion` — identification d'un contact commercial sur les TOP 5
- `find-prospects-congres` — extraction de la liste exposants depuis un programme
- `veille` — (optionnel) lecture des flux RSS dentaires
- `audit-rgpd` — validation Olivia préalable (à invoquer 1 fois puis périodiquement)

## Skills enchaînés en aval (manuels)

- `pipeline-sponsors-watch` (Éloi) — pour suivre les prospects créés
- `mail-rediger` voix=eloise — pour drafter le 1er contact validé
- `validation-legale-message` (Olivia) — pour valider la formulation RGPD du 1er mail
- `analyse-conversion-sponsor` (Éloi) — pour mesurer le taux de transformation du flux auto
