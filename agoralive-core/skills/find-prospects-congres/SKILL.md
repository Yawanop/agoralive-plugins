---
name: find-prospects-congres
description: >
  Génère automatiquement une liste de prospects sponsors AgoraLive à partir
  du programme officiel d'un congrès dentaire (PDF, page web officielle, ou
  liste d'exposants). Extrait la liste des sponsors/exposants historiques,
  enrichit chaque société via `enrich-societe-notion` (API gouv `recherche-entreprises` + open source),
  identifie un contact commercial via `enrich-personne-notion`, génère un
  argument de matching "pourquoi AgoraLive intéresse cette boîte", et crée
  les fiches dans Notion (Hub Commercial + Organisations + Personnes).
  S'appuie sur l'API publique GRATUITE `recherche-entreprises.api.gouv.fr`
  (sans token) pour les données légales. POC : ADF 2024. À déclencher quand
  Éloïse, Paul, Julien (ou leurs jumeaux) demandent : "trouve les sponsors
  de [congrès]", "liste exposants ADF 2024", "génère prospects depuis
  [programme]", "Éloi prospects SFODF", "scan ce programme et fais-moi les
  fiches", "boote la base prospects sponsors depuis [congrès]". Skill
  principal de prospection sortante.
---

# find-prospects-congres — Prospection sortante depuis programmes de congrès

## Mission

Transformer un programme officiel de congrès dentaire en **liste de prospects sponsors qualifiés** dans Notion, avec :
- Fiche Société Notion enrichie (API gouv `recherche-entreprises` + web)
- Fiche Personne Notion (contact commercial pertinent identifié)
- Argument de matching pré-rédigé ("pourquoi cette boîte sponsorise des congrès, et pourquoi AgoraLive lui apporte de la valeur")
- Statut commercial initialisé dans le Hub Commercial

C'est le **bootstrap commercial** : à partir d'un programme PDF, sortir 20-50 prospects qualifiés et prêts à être travaillés par Éloïse.

---

## Pré-requis

1. Programme officiel du congrès :
   - **PDF** uploadé dans Cowork, OU
   - **URL** d'une page web officielle (site du congrès, liste des exposants), OU
   - **Texte brut** collé par l'utilisateur ("voici la liste des exposants")
2. Skills dépendants : `enrich-societe-notion` (utilise l'API gouv `recherche-entreprises.api.gouv.fr`, gratuite et sans token) + `enrich-personne-notion` (sources gratuites).
3. Aucun token / aucune inscription requise pour les sources légales FR.
4. Bases Notion :
   - 🏛️ Organisations : `06d3fc453c564f7eb6d9b862529d209a`
   - 👤 Personnes : `9d8d3c6b370d4c808502c0d6cd4c1e36`
   - 💼 Hub Commercial : `35e6979fbcd181c3b6bed19cc2fbb275`
   - 🏛️ Congrès : `c7ffc0cf7a3b427dab83c02f4fa4a03f` (pour le rattachement)

---

## Procédure (8 étapes)

### Étape 1 — Identifier le congrès cible

Demander à Paul/Éloïse :
1. **Quel congrès** (nom + édition + année) ?
2. **Source du programme** (PDF uploadé / URL / texte) ?
3. **Tier minimum recherché** (tous sponsors / Gold+Platinum only / etc.) — défaut : tous.

Vérifier que le congrès existe déjà dans la base Congrès Notion. Si oui → garder l'ID pour rattacher. Si non → proposer de créer la fiche Congrès (déléguer ponctuellement à `notion-document-router`).

### Étape 2 — Extraction de la liste brute

**Cas PDF** :
- Lire le PDF (skill `pdf` si tableaux complexes, sinon Read direct).
- Repérer les sections "Sponsors", "Exposants", "Partenaires", "Avec le soutien de".
- Extraire les **noms de sociétés**. Les logos sont indicatifs mais le texte près du logo donne souvent le nom exact.
- Si tiers visibles (Platinum, Gold, Silver, Bronze) → capturer aussi le tier.

**Cas URL** :
- WebFetch sur la page exposants.
- Si la page est en JavaScript (vide en HTML brut) → escalader à Claude in Chrome (`navigate` + `get_page_text`).
- Parser les noms de sociétés.

**Cas texte brut** :
- Splitter par lignes / virgules.

Sortir une **liste brute** : `[("Henry Schein France", "Platinum"), ("Dentsply Sirona", "Gold"), ...]`.

### Étape 3 — Dédoublonnage avant traitement

Avant d'enrichir, pour chaque société :
1. `notion-search` dans la base Organisations + Hub Commercial.
2. Si match existant → **ne pas recréer**, juste ajouter le rattachement à ce congrès dans l'historique sponsoring.
3. Si nouvelle → garder pour enrichissement.

### Étape 4 — Enrichissement Société (en boucle)

Pour chaque nouvelle société :
1. Invoquer la procédure de `enrich-societe-notion` (étapes 2-3 du skill : API gouv `recherche-entreprises` + web).
2. Récupérer SIREN, dirigeants, CA, effectif, site web, LinkedIn.
3. Créer la fiche Notion dans Organisations + ajouter une ligne dans Hub Commercial avec :
   - `🏢 Société` : relation vers fiche Organisations
   - `🏛️ Congrès source` : relation vers fiche Congrès
   - `🥇 Tier historique` : Platinum/Gold/Silver/Bronze (selon parsing étape 2)
   - `🚦 Statut commercial` : `🔍 À qualifier`
   - `📝 Notes` : "Identifié comme sponsor historique de <Congrès> via programme officiel <année>"

**Quotas API gouv** : pas de quota dur documenté, mais usage raisonnable demandé par la DINUM. Bonne pratique : 1 req/sec, batchs de 100 max puis pause de quelques secondes. Si le volume devient industriel (>5000 sociétés/mois) → envisager Pappers payant (~50€/mois) ou Sirene v3 INSEE (token gratuit à demander une fois).

### Étape 5 — Identifier le bon contact commercial

Pour chaque société enrichie, le bon contact n'est pas le PDG mais souvent :
- **Marketing Manager** / Directeur Marketing
- **Events Manager** / Directeur Événementiel
- **Sponsorship Manager**
- **KAM dentaire France** (pour les multinationales avec une équipe FR)

Stratégie :
1. Recherche Google : `"<Société>" (marketing OR events OR sponsorship OR partenariat) site:linkedin.com/in`
2. Prendre le 1-2 résultats les + récents (dernière mise à jour LinkedIn visible).
3. Si rien trouvé → fallback sur **un dirigeant identifié via l'API gouv** (qualité "Directeur Général", "Président", "Représentant légal"). Moins ciblé mais permet de démarrer.
4. Pour chaque contact identifié → invoquer la procédure `enrich-personne-notion` (recherche LinkedIn + pattern email + score de confiance).

Créer la fiche Personne dans la base Personnes + relation vers Société.

### Étape 6 — Générer l'argument de matching

Pour chaque société qualifiée comme prospect, **drafter une phrase courte** (2-3 lignes) répondant à : *"Pourquoi cette boîte sponsorise déjà des congrès ET pourquoi AgoraLive lui apporte un gain par rapport à un sponsoring classique ?"*.

Template :
```
<Société> sponsorise <X congrès dentaires> par an (tier <Y>).
Leur logique : <visibilité auprès des praticiens / formation continue / lancement DM>.
AgoraLive apporte : <captation + diffusion post-congrès qui démultiplie l'audience de leur sponsoring 10x+, valorisation de leurs intervenants experts, contenu réutilisable en marketing toute l'année>.
```

Stocker dans `📝 Argument matching` de la ligne Hub Commercial.

### Étape 7 — Hiérarchiser les prospects

Score à 4 critères (chaque /5) :
- **Pertinence dentaire** (NAF + activité confirmée) : 0-5
- **Capacité financière** (CA API gouv OU proxy effectif × ratio sectoriel > seuil) : 0-5
- **Sponsoring historique** (nombre de congrès trouvés en open source) : 0-5
- **Présence contact identifié** (HIGH confidence email/LinkedIn) : 0-5

Score total /20. Trier la liste. Top 10 = priorité d'Éloïse pour les premières prises de contact.

### Étape 8 — Récap chat + livrable

```
✅ Prospection congrès <NOM> <ANNÉE> terminée

📊 Bilan :
  - <N> sociétés extraites du programme
  - <X> déjà en base (rattachement historique ajouté)
  - <Y> nouvelles fiches créées
  - <Z> contacts personnes identifiés (HIGH confidence : <ZH>, MEDIUM : <ZM>, LOW : <ZL>)

🥇 TOP 10 prospects prioritaires (score /20) :
  1. <Société> — <score> — Contact : <Personne> (<email>) — 💰 CA <CAk€>
  2. ...
  10. ...

📥 Vues Notion :
  - Hub Commercial filtre "Statut = À qualifier + Congrès source = <NOM>" : <URL>
  - Top 10 prêt pour Éloïse : <URL>

🔜 Prochaines étapes recommandées :
  1. Éloïse trie le Top 10 (garde / drop / reformule) → 30 min
  2. `mail-rediger` voix=eloise pour drafter le 1er contact (mention RGPD obligatoire validée par Olivia)
  3. `pipeline-sponsors-watch` pour suivre les relances

⚠️ Compliance : pipeline d'enrichissement à faire valider par `audit-rgpd` (Olivia)
  avant le 1er envoi de mail prospection à plus de 50 personnes.
```

---

## Cas particuliers

### Programme PDF mal scanné / OCR
Si le PDF est un scan image (pas de texte sélectionnable), demander à Paul de relancer un OCR (skill `pdf` peut aider) ou de fournir une autre source.

### Congrès sans liste publique de sponsors (rare)
Tomber sur LinkedIn : recherche `"<Congrès> <année>" sponsor OR partner OR exposant` — souvent les sponsors postent eux-mêmes leur présence.

### Programme bilingue / international (IDS Cologne)
Garder les noms originaux pour le matching API gouv (qui inclut les filiales France des groupes internationaux comme "Dentsply Sirona France SAS").

### Société "fantôme" (existe sur programme mais absente de l'API gouv)
Possible auto-entrepreneur, association, ou société très récente. Créer la fiche minimale avec flag `🚦 À qualifier — données absentes`.

### Trop de prospects (>100) — congrès géant
Filtrer le programme dès l'étape 2 par tier minimum (ex : Gold+ seulement). 30-50 prospects qualifiés > 200 prospects brouillon.

### Conflit avec l'agenda Éloïse
Si Éloïse a déjà 20 deals chauds en cours (`pipeline-sponsors-watch`), batch d'un grand nombre de prospects la noie. Suggérer un découpage : 10 nouveaux prospects/semaine intégrés dans son flux.

---

## POC ADF 2024 (cas d'usage de référence)

Cible : programme ADF 2024 (le Salon ADF se tient chaque année à Paris Porte Maillot, ~50-80 exposants).

Étapes POC :
1. Paul/Éloïse fournit le PDF du programme officiel ADF 2024 OU l'URL https://www.adf.asso.fr (rubrique exposants 2024).
2. Skill extrait la liste → ~50 sociétés.
3. Enrichissement société via l'API gouv pour les ~50 sociétés (gratuit, sans quota dur, le batch passe sans problème en 5-10 min).
4. Identification contact commercial pour chacune (~50 recherches Google).
5. Génération matching argument pour chacune.
6. Sortie : Hub Commercial filtré avec ~50 lignes, Top 10 affiché à Éloïse.

Temps estimé : ~30-45 min pour la chaîne complète. Validation Olivia avant industrialisation.

---

## Compliance RGPD (validation Olivia obligatoire)

- **Base légale** : intérêt légitime (prospection B2B sur données publiques).
- **Sources** : programme officiel public (CGU congrès) + `recherche-entreprises.api.gouv.fr` (registre légal officiel) + Google indexed public data.
- **Mention obligatoire 1er contact** : à valider par Olivia + `validation-legale-message`.
- **Pas de scraping authentifié** : aucun login sur LinkedIn.
- **Pas de scraping massif** : usage raisonnable de l'API gouv (≤1 req/sec), pas de hammering des sites congrès, User-Agent identifiant AgoraLive pour traçabilité.
- **Effacement à la demande** : process à formaliser avant industrialisation.

**Avant 1er envoi mail prospection en masse** : invoquer `audit-rgpd` ET `validation-legale-message` pour qu'Olivia tamponne le pipeline complet.

---

## Identifiants Notion utiles

- 🏛️ Base Organisations : `06d3fc453c564f7eb6d9b862529d209a`
- 👤 Base Personnes : `9d8d3c6b370d4c808502c0d6cd4c1e36`
- 💼 Hub Commercial : `35e6979fbcd181c3b6bed19cc2fbb275`
- 🏛️ Base Congrès : `c7ffc0cf7a3b427dab83c02f4fa4a03f`

## Skills liés

- `enrich-societe-notion` — appelé pour chaque société extraite
- `enrich-personne-notion` — appelé pour chaque contact commercial identifié
- `notion-document-router` — pour créer la fiche Congrès si elle manque
- `mail-rediger` voix=eloise — pour drafter le 1er contact
- `validation-legale-message` (Olivia) — valide le 1er mail avant envoi
- `audit-rgpd` — valide le pipeline complet avant industrialisation
- `pipeline-sponsors-watch` (Éloi) — pour le suivi quotidien des prospects créés
- `analyse-conversion-sponsor` (Éloi) — pour mesurer la performance du pipeline source par source
