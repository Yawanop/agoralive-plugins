---
name: enrich-societe-notion
description: >
  Enrichit automatiquement une fiche Société/Organisation Notion AgoraLive
  (base 🏛️ Organisations ou Hub Commercial) à partir de l'API publique
  française GRATUITE et SANS TOKEN `recherche-entreprises.api.gouv.fr`
  (DINUM, alimentée INSEE/INPI) : SIREN, SIRET, dirigeants, NAF, effectif,
  adresse siège, date création, forme juridique. Complété par recherche web
  open source pour le site officiel, la page LinkedIn corporate et les
  sponsorings historiques. Écrit en retour dans la fiche Notion avec
  traçabilité de la source et de la date.
  À déclencher quand Paul, Éloïse, Julien (ou leurs jumeaux) demandent :
  "enrichis cette société", "complète la fiche [boite]", "trouve-moi les infos
  légales de X", "Pauline enrichis cette orga", "Éloi complète ce sponsor",
  "données INSEE/INPI de [société]", "fiche société à compléter",
  "qui dirige X", "SIREN de Y", "effectif et CA de Z". S'invoque aussi en
  batch : "enrichis toutes les sociétés vides de la base". Skill mutualisé.
---

# enrich-societe-notion — Enrichissement société via API gouv + open source

## Mission

À partir d'une fiche Société existante dans Notion (même partiellement remplie : juste un nom de boîte suffit), compléter automatiquement toutes les informations légales et commerciales disponibles publiquement, **avec traçabilité de la source**.

Source primaire : **API publique `recherche-entreprises.api.gouv.fr`** (DINUM — données officielles INSEE/INPI, **GRATUITE, sans token, sans inscription**). Source secondaire : recherche web pour le site officiel, la page LinkedIn corporate et les sponsorings historiques.

---

## Pré-requis

1. **Aucun token requis** — l'API gouv est en accès libre. Aucun fichier secret à gérer.
2. Connexion internet sortante vers `https://recherche-entreprises.api.gouv.fr`.
3. Base 🏛️ Organisations Notion : `06d3fc453c564f7eb6d9b862529d209a`
4. Hub Commercial : `35e6979fbcd181c3b6bed19cc2fbb275` (pour les sociétés sponsors)

---

## Procédure (6 étapes)

### Étape 1 — Identifier la cible

Trois patterns d'entrée :

1. **URL Notion d'une fiche** fournie par l'utilisateur → `notion-fetch` pour lire les champs déjà remplis.
2. **Nom de société libre** ("enrichis Henry Schein") → `notion-search` dans la base Organisations + Hub Commercial. Si plusieurs matchs → demander à Paul de choisir. Si aucun → demander confirmation pour **créer** la fiche.
3. **Mode batch** ("enrichis toutes les sociétés vides") → `notion-query-database-view` sur la base Organisations, filtre sur les fiches où SIREN OU CA OU Dirigeants sont vides. Itère.

À cette étape, on a : nom de la société + ville/pays (si dispo) + ID de la fiche Notion existante (ou flag "à créer").

### Étape 2 — Requête API recherche-entreprises.api.gouv.fr

L'API est en accès libre, pas d'auth :

```bash
# Recherche par nom (renvoie une liste de matchs triée par pertinence)
curl -s "https://recherche-entreprises.api.gouv.fr/search?q=<NOM_URL_ENCODED>&page=1&per_page=5" | jq .

# Recherche par SIREN direct (si on l'a déjà)
curl -s "https://recherche-entreprises.api.gouv.fr/search?q=<SIREN>" | jq .

# Filtre géographique optionnel (utile si plusieurs sociétés au même nom)
curl -s "https://recherche-entreprises.api.gouv.fr/search?q=<NOM>&code_postal=<CP>" | jq .
```

L'API supporte aussi les filtres par section NAF (`section_activite_principale`), tranche d'effectif (`tranche_effectif_salarie`), et nature juridique. Documentation complète : https://recherche-entreprises.api.gouv.fr/docs

### Étape 3 — Parser la réponse API gouv

Les résultats sont dans `results[]`. Pour chaque match, champs à extraire :

| Champ Notion | Source API gouv | Format |
|---|---|---|
| 🆔 SIREN | `siren` | 9 chiffres |
| 🆔 SIRET siège | `siege.siret` | 14 chiffres |
| 🏷️ Dénomination officielle | `nom_complet` ou `nom_raison_sociale` | string |
| 📅 Date création | `date_creation` | YYYY-MM-DD |
| 👤 Dirigeants | `dirigeants[]` (`nom`, `prenoms`, `qualite`, `type_dirigeant`) | liste |
| 🏠 Siège social | `siege.adresse` (composé `numero_voie + type_voie + libelle_voie + code_postal + libelle_commune`) | adresse |
| 👥 Effectif | `tranche_effectif_salarie` (code INSEE 00 à 53) + `annee_tranche_effectif_salarie` | string |
| 💼 NAF / APE | `activite_principale` + `section_activite_principale` | string |
| 🏢 Forme juridique | `nature_juridique` (code) — mapper via table INSEE | string |
| 📊 État administratif | `etat_administratif` (`A` = actif, `C` = cessé) | A/C |
| 📊 CA dernier exercice | `finances.<année>.chiffre_affaires` (si dispo, souvent vide hors sociétés cotées) | EUR |
| 💰 Capital social | `complements.capital_social` | EUR |

**Limites vs Pappers** : pas de K-bis téléchargeable, comptes annuels souvent vides pour SAS/SARL non cotées, pas de bénéficiaires effectifs détaillés. Pour 99% des besoins prospection sponsor, c'est largement suffisant. Si on a besoin du CA précis d'une cible Tier 1 → demander à Olivier de checker manuellement sur Infogreffe (5€ par bilan) ou bascule v2 sur Pappers payant.

### Étape 4 — Compléments open source (web)

Pour combler les champs **non couverts par l'API gouv** (site web, LinkedIn corporate, sponsorings historiques, etc.) :

1. **Site web officiel** : Google `"<NOM>" site officiel` → prendre le 1er résultat fiable (homepage du domaine matchant la dénomination).
2. **Page LinkedIn entreprise** : Google `"<NOM>" site:linkedin.com/company` → URL LinkedIn corporate.
3. **Sponsoring historique dentaire** (si Hub Commercial) : Google `"<NOM>" sponsor (ADF OR SFODF OR IFRO OR IDS) -site:linkedin.com` → identifier 2-3 congrès où la boîte a déjà sponsorisé.
4. **Activité dentaire** (qualification de pertinence pour AgoraLive) : vérifier si le code NAF / l'activité décrite touche au dentaire / médical / pharma / fabrication de DM. Sortir un flag `🦷 Pertinence dentaire : OUI/NON/PARTIELLE` + 1 phrase de justification.

### Étape 5 — Écriture dans Notion

`notion-update-page` sur la fiche existante (ou `notion-create-pages` si Étape 1 a créé la fiche).

**Règle critique** : pour chaque champ enrichi, ajouter dans le champ `📝 Notes enrichissement` une ligne :
```
[2026-05-18] SIREN + dirigeants ← recherche-entreprises.api.gouv.fr (réf. SIREN 123456789)
[2026-05-18] Site web ← Google search "<query>"
[2026-05-18] Sponsoring historique ← Programme ADF 2023 (PDF adf.asso.fr/programme-2023.pdf)
```

Cette traçabilité est **non négociable** : c'est la condition pour qu'Olivia valide RGPD-wise (article 13 RGPD : source des données collectées). L'API gouv étant un service public officiel, la légitimité de la source est encore plus solide que Pappers (republier).

### Étape 6 — Récap chat

```
✅ Société enrichie : <Dénomination> (SIREN <siren>)
📍 <Adresse siège>
👥 Effectif : <tranche> | 💰 CA : <CA>€ | 📅 Créée en <année>
👤 Dirigeants : <Liste 1-3 noms + qualité>
🦷 Pertinence dentaire : <OUI/NON/PARTIELLE> — <justification>
🔗 Site : <URL> | LinkedIn : <URL>
🎯 Sponsoring historique : <2-3 congrès> (si applicable)

📊 Sources : recherche-entreprises.api.gouv.fr (DINUM / INSEE-INPI) + recherche web ouverte
📥 Fiche Notion : <URL>
```

---

## Cas particuliers

### Société étrangère (pas de SIREN)
L'API gouv ne couvre que la France. Dégrader vers : recherche web pour adresse siège, dirigeants (LinkedIn), CA (rapport annuel public si coté). Flag `📍 Hors France` dans Notion. Mentionner à Olivia (escalation RGPD si transfert de données hors UE prévu).

### Plusieurs sociétés au même nom (groupes, filiales)
Lister les 2-3 matchs API gouv à Paul (utiliser le filtre `code_postal` pour disambigüer si une ville est connue) et lui demander laquelle est la cible. Ne **jamais** deviner — un mauvais SIREN = mauvaise négo sponsoring.

### Dirigeants non listés (sociétés récentes ou microSAS)
Certaines fiches INSEE n'ont pas tous les dirigeants à jour. Compléter via recherche web (page "Équipe" du site corporate, LinkedIn). Flag `👤 Dirigeants : complétés via web`.

### Mode batch — quotas API
L'API gouv est gracieuse mais pas illimitée. En pratique : pas de quota dur documenté, mais le DINUM demande un usage raisonnable. Bonne pratique : 1 req/seconde max, batch de 100 à la fois max, puis pause. Si on tape les limites → ajouter un `User-Agent: AgoraLive-Enrichment-Skill` dans le header pour la traçabilité.

### Société absente de l'API gouv (auto-entrepreneur ou très récente)
Faire la recherche web uniquement. Flagger `🆔 SIREN non trouvé` dans Notion. Auto-entrepreneur : pas de risque commercial sponsor (cible peu pertinente), souvent on peut drop.

### CA manquant (cas très fréquent pour SAS/SARL)
L'API gouv ne renvoie les comptes que pour les sociétés qui les déposent publiquement (cotées, certaines SA). Pour 80% des cibles sponsor B2B FR, le champ `finances` sera vide. Compléter par :
1. Recherche web "<Société> chiffre d'affaires 20XX" (souvent dans articles presse / Les Échos / Usine Nouvelle).
2. Effectif (toujours rempli) comme proxy de taille — règle empirique : CA ≈ effectif × 200k€ pour le dentaire fabricant, × 100k€ pour distribution.
3. Si cible Tier 1 où le CA précis est crucial → demander à Olivier un bilan Infogreffe (~5€).

---

## Compliance RGPD (à valider avec Olivia)

- **Base légale** : intérêt légitime (prospection B2B sur données légales publiques officielles INSEE/INPI).
- **Source publique officielle** : `recherche-entreprises.api.gouv.fr` est opérée par la DINUM (État français), alimentée par INSEE + INPI = données publiques par construction. Légitimité quasi-imbattable côté RGPD.
- **Pas de données sensibles** collectées (santé, opinions, etc.).
- **Pas de scraping illégal** : API officielle publique, accès libre documenté.
- **Traçabilité** : champ `📝 Notes enrichissement` documente chaque ajout.
- **Effacement** : si une société demande retrait → suppression de la fiche Notion + log dans le registre des traitements.

Avant industrialisation : invoquer `audit-rgpd` sur ce pipeline pour validation officielle Olivia.

---

## Identifiants Notion utiles

- 🏛️ Base Organisations : `06d3fc453c564f7eb6d9b862529d209a`
- 💼 Hub Commercial : `35e6979fbcd181c3b6bed19cc2fbb275`
- 👤 Base Personnes : `9d8d3c6b370d4c808502c0d6cd4c1e36`
- 🏛️ Base Congrès : `c7ffc0cf7a3b427dab83c02f4fa4a03f`

## Skills liés

- `enrich-personne-notion` — pour enrichir les contacts (dirigeants/commerciaux) une fois la société complétée
- `find-prospects-congres` — pour bootstrapper une liste de sociétés depuis un programme de congrès
- `audit-rgpd` — pour valider la conformité du pipeline avec Olivia
- `triage-contrat-agoralive` — pour la suite (quand on signe avec la société enrichie)
