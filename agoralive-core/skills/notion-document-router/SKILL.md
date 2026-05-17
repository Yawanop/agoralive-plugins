---
name: notion-document-router
description: |
  Pipeline d'alimentation à source de vérité unique pour les bases Notion AgoraLive + archivage automatique Drive miroir via Apps Script "AgoraLive Drive Mover".

  L'utilisateur dépose un document selon l'un des trois modes :
  - Mode A — drag-drop natif dans 📥 INBOX du Shared Drive (async, batch, rapide)
  - Mode B — upload direct dans le chat Cowork (interactif, synchrone)
  - Mode C — note vocale Notion AI (texte déjà transcrit) accessible depuis 🎙️ Inbox Vocale (multi-distribution multi-cockpits)

  Le skill (1) lit le contenu texte, (2) crée une fiche dans la base maître `📥 Documents Source`, (3) classifie le type + identifie les bases dérivées concernées (potentiellement plusieurs pour une note vocale), (4) crée les fiches dérivées liées, (5) remplit le champ `📁 Drive cible (folder ID)` selon la table de mapping pour que l'Apps Script déplace le fichier automatiquement dans les 5 minutes suivantes.

  Triggers : "route ce document", "alimente les bases", "traite ce fichier", "classe ce contrat/cession/bug/article", "fais la fiche maître", "propage dans Notion", "pousse dans les bases", "Documents Source", "📥", "route mes vocales", "traite mes notes Notion AI", "traite l'inbox", "vide l'inbox", ou dépôt d'un fichier sans instruction. Aussi "traite la dernière ligne de Documents Source", "Notion routing".

  Anti-triggers : un seul type demandé explicitement avec skill dédié existant (`po-bug-agoralive`, `triage-contrat-agoralive`, `officiel-article-v3`) — déléguer.
---

# notion-document-router v2 — Routing unifié Notion + Drive miroir

## Mission

Garantir qu'**un document = un fichier Drive archivé dans le bon dossier miroir + une fiche source Notion + N fiches dérivées liées**, sans duplication, toujours rejouable, qui fonctionne pour **toute l'équipe AgoraLive** sans setup individuel — Pauline, Julie, Éloi, Michelle, Olivia, Philippine se partagent ce même skill.

## Architecture en 3 couches

```
[INGESTION]                  [CLASSIFICATION]              [ARCHIVAGE DRIVE]
─────────────                ───────────────                ──────────────────
A. 📥 INBOX (Drive)  ─┐
B. Upload Cowork     ─┼─►  notion-document-router    ─►   Apps Script
C. 🎙️ Inbox Vocale  ─┘     (ce skill, ici)                  AgoraLive Drive Mover
                              │                                trigger 5 min
                              ▼                                (paul@agoralive.ai)
                       Notion: maître +
                       N fiches dérivées +
                       📁 Drive cible (folder ID)
```

Le skill ne touche **pas directement** au Drive pour les moves. Il prépare la fiche Notion avec le bon `📁 Drive cible (folder ID)`, et l'Apps Script ferme la boucle de manière asynchrone (trigger temporel 5 min).

## Pré-requis (déjà en place côté infra)

1. Base maître `📥 Documents Source` Notion — ID `db0066ca76eb4eeb9a0741ba22377326`
2. Dossier `📥 INBOX` à la racine du Shared Drive AgoraLive — ID `1apPjlKOsdYT44dYHSnBT7yi2QA5Lbemq`
3. Dossier `🎙️ Inbox Vocale` à la racine — ID `15MOnSU3XtDUO0VruR7n5HTBdvN7Q5d4y`
4. Apps Script "AgoraLive Drive Mover" déployé avec trigger temporel 5 min sur `routePendingMoves`
5. Notion Connection "AgoraLive Drive Mover" partagée avec la base maître
6. Champ `📁 Drive cible (folder ID)` (rich_text) sur la base maître

Aucun setup côté utilisateur final. Tout est partagé via l'org Workspace AgoraLive.

## Procédure complète (7 étapes)

### Étape A — Détection de la source

Trois modes possibles, à détecter selon le contexte d'invocation :

**Mode B (Upload chat Cowork — synchrone)** — déclenché si l'utilisateur a joint un fichier au message courant :
1. Lire le contenu via `Read` tool (texte/PDF/image/docx)
2. Upload du fichier dans `📥 INBOX` via `create_file` Drive MCP avec `parentId = 1apPjlKOsdYT44dYHSnBT7yi2QA5Lbemq`
3. Continuer en Étape B avec le file_id Drive retourné

**Mode A (Scan INBOX — async batch)** — déclenché par "route mon dernier doc", "traite l'inbox", "vide l'inbox" :
1. Lister les fichiers de `📥 INBOX` via `search_files` Drive MCP (`parentId = '1apPjlKOsdYT44dYHSnBT7yi2QA5Lbemq'`)
2. Pour chaque fichier non encore référencé dans la base maître (cf. anti-doublon étape D), traiter un par un
3. Lire le contenu via `read_file_content` Drive MCP

**Mode C (Scan Inbox Vocale — async)** — déclenché par "route mes vocales", "traite mes notes Notion AI" :
1. Lister les fichiers/pages texte dans `🎙️ Inbox Vocale` via `search_files` (`parentId = '15MOnSU3XtDUO0VruR7n5HTBdvN7Q5d4y'`)
2. Pour chaque note non encore référencée, lire le contenu via `read_file_content`
3. Les notes vocales sont **déjà du texte** (transcription Notion AI faite côté Notion mobile/desktop), aucune étape de transcription Whisper à effectuer

### Étape B — Classification

1. Identifier le **type** parmi : `📜 Contrat`, `📝 Cession`, `🐛 Bug`, `✍️ Article`, `👔 CV`, `💰 Devis sponsor`, `📅 Compte-rendu`, `📄 PDF brut`, `🎙️ Audio` (= note vocale issue de Notion AI), `🖼️ Image`, `📝 Transcription`, `🧾 Brief`, `❓ Autre`

2. Calculer un **score de confiance 0-100** :
   - 90-100 : signaux multiples convergents (ex : titre "Contrat" + clauses + signatures + montant)
   - 70-89 : signaux clairs mais partiels
   - <70 : ambigu → créer fiche maître en statut `🔄 En classification`, **ne pas propager** aux bases dérivées, ne pas remplir `📁 Drive cible`, attendre validation manuelle

3. Identifier les **bases dérivées cibles** (1 à N). Pour les notes vocales (mode C), souvent multiple : une dictée libre peut toucher `🐛 Bugs` + `📅 Compte-rendu` + `👤 Personnes` + `🏛️ Congrès` en même temps. Découper le contenu par sujet et alimenter chaque base concernée.

4. Identifier les **entités nommées** : personnes (auteurs, intervenants, contacts), organisations, congrès, routes (pour les bugs), conférences. Stocker leurs identifiants pour les relations en étape F.

### Étape C — Table de mapping Type → Drive folder ID

| Type détecté Notion | Sous-dossier Drive | Folder ID | Statut |
|---|---|---|---|
| ✍️ Article | `Articles/` | `1rF44X2PSSdxklEtYqfuh89X_dYwWpsgz` | ✅ Existant |
| 📜 Contrat | `Contrats/` (ACL à restreindre Olivier+Paul+Julien) | `1gahtS4XqTgUZXGAky7hlzw2br9Y2AGAI` | ✅ Existant |
| 📝 Cession | `Cessions/` (ACL à restreindre Olivier+Paul+Julien) | `1_BklMOmWZSUrHqnEwbMUzwT6JdIz4EwA` | ✅ Existant |
| 🐛 Bug | `Bugs/` | `1lEsgCm8bMNFOQsF94NS9mwU9zalzy5s-` | ✅ Existant |
| 👔 CV | `CV/` (ACL à restreindre RH) | `1gXePj6uqX2hpbqS_--LD5VXdulOXsENs` | ✅ Existant |
| 💰 Devis sponsor | `Devis/` | `1fwimmJR5tN4OOwXMRPJnUHvNjDArOTmI` | ✅ Existant |
| 📅 Compte-rendu | `Comptes-rendus/` | `1WSUuBqVBNhuJfYolhGVvyTbee8jVjEbO` | ✅ Existant |
| 🧾 Brief | `Briefs/` | `1TN4yhN0o8JZCZvdIqoak_sp1qmJCJdT0` | ✅ Existant |
| 🎙️ Audio | `🎙️ Inbox Vocale` (reste sur place — no-op Apps Script) | `15MOnSU3XtDUO0VruR7n5HTBdvN7Q5d4y` | ✅ Existant |
| 🖼️ Image | `Images/` | `1y0LoRLCfrY-h6800xoSJaXpEEFcFfOFU` | ✅ Existant |
| 📝 Transcription | `Transcriptions/` | `1lZSmvne9LqoWuLNUv64cqIrthNS0ybp-` | ✅ Existant |
| 📄 PDF brut | `PDF/` | `1ILENg2HYP9TeG-wkNylQKcsXC0Z-PZ79` | ✅ Existant |
| ❓ Autre | `Autres/` | `1r828U69SWfKX03BdLgP9s7tmj8BTZ5RI` | ✅ Existant |

### Étape D — Anti-doublon Notion (lookup avant création)

Avant de créer la fiche maître :
1. `notion-query-database-view` sur la base maître, filtrer `🔗 URL fichier` contenant le Drive file ID
2. Si une fiche existe déjà → réutiliser, ne pas dupliquer. Logger "déjà routé".

Pour chaque entité nommée à créer (`👤 Personnes`, `🏛️ Organisations`, `🏛️ Congrès`, `🗺️ Routes`) :
1. `notion-search` ciblé sur la base concernée
2. Si fuzzy match (nom exact ou email exact) → réutiliser l'ID existant
3. Sinon → créer la fiche

### Étape E — Création fiche maître

`notion-create-pages` dans `📥 Documents Source` (data_source_id `25697468-84b6-4016-97b2-14ce52461923`) avec :
- `📄 Titre` : titre actionnable extrait du document
- `🔗 URL fichier` : `https://drive.google.com/file/d/{file_id}/view`
- `📦 Type détecté` : selon classification étape B
- `🚦 Statut routage` : `✅ Routé` (ou `🔄 En classification` si confiance < 70)
- `🎯 Bases cibles` : multi-select avec les bases dérivées identifiées
- `🧠 Confiance IA` : score 0.0 à 1.0
- `📝 Résumé extrait` : 3 phrases max
- `🤖 Logs` : `[<ISO timestamp>] Mode <A|B|C>. Drive file ID: <id>. Classification: <type> (confiance N%). Signaux: <résumé>. Entités: <liste>.`
- `📁 Drive cible (folder ID)` : ID du dossier selon table mapping étape C

### Étape F — Propagation aux bases dérivées

Pour chaque base cible identifiée :
1. `notion-create-pages` dans la base dérivée avec les champs spécifiques (mapping ci-dessous) + relation `→ 📥 Documents Source` pointant vers la maître + `🔗 URL fichier` recopié pour accès rapide
2. Récupérer l'ID de la fiche dérivée
3. `notion-update-page` sur la maître pour remplir la relation `→ <base>` avec cet ID

**Mappings par base dérivée :**

- **📜 Contrats** (id `adaadf0e-327f-4bfc-bb1e-a19bdf655922`) → Partie 1, Partie 2, Date signature, Montant, Statut (Brouillon/En signature/Signé), 🔗 URL Drive, → 📥 Doc source
- **📝 Cessions** (id `9ab85bdd-3525-47e8-a471-e914da7278b2`) → Intervenant (rel Personnes), Conférence (rel), Date, Statut signature, 🔗 URL Drive, → 📥 Doc source
- **🐛 Bugs** (id `dd1b0215-2810-4e17-bbc6-0e30d52a321e`) → Titre actionnable, Route (rel), Sévérité (P0/P1/P2/P3), Statut (`📥 À traiter`), DoD, 🔗 URL Drive, → 📥 Doc source
- **✍️ Articles** (id `b6733212-5076-4fed-a165-2e513a663317`) → Titre, Auteur principal + Co-auteurs (rel Personnes), Conférence source (rel), Type (Synthèse/Tribune/...), Statut rédaction, 📎 Lien Drive, → 📥 Doc source
- **👔 Recrutement** (id `9658f18b-205a-4372-a36d-ff37f8d46b5b`) → Nom, Poste visé, Statut (`📥 Sourcé`), → 👤 Personnes (rel, créer si absent), 🔗 URL Drive, → 📥 Doc source
- **💰 Sponsors** (id `3abc2ce9-e44e-44e4-b3e5-b2ea2aced1a0`) → Congrès (rel), Montant, Tier, Statut négociation, 🔗 URL Drive, → 📥 Doc source
- **📅 Journal de bord** — pages ou base selon le cas — Date, Participants (rel Personnes), Décisions, Actions, 🔗 URL Drive, → 📥 Doc source

**Cas particulier mode C (notes vocales)** : une note vocale touche souvent N bases en même temps. Créer N fiches dérivées (une par sujet identifié), toutes liées à la même fiche maître via `→ 📥 Documents Source`. Sur chaque cockpit jumeau qui consulte une de ces bases, la note vocale apparaîtra naturellement via la relation.

### Étape G — Finalisation

1. Vérifier que la fiche maître a bien `🚦 Statut routage = ✅ Routé` ET `📁 Drive cible (folder ID)` rempli
2. **L'Apps Script "AgoraLive Drive Mover" prendra le relais dans les 5 minutes suivantes** — aucune action Drive à faire depuis Cowork
3. Pour mode C (notes vocales), `📁 Drive cible = 15MOnSU3XtDUO0VruR7n5HTBdvN7Q5d4y` (Inbox Vocale elle-même) → Apps Script détecte que le fichier est déjà dans le target folder → no-op silencieux, note reste sur place comme désiré

## Idempotence & rejouabilité

- **Niveau Drive** : pas d'upload multiple. Mode B upload une fois dans INBOX, le fichier garde son ID stable jusqu'au move Apps Script
- **Niveau fiche maître Notion** : anti-doublon via le champ `🔗 URL fichier` (étape D)
- **Niveau fiches dérivées** : avant create, vérifier qu'il n'existe pas déjà une fiche dans la base liée à la même maître via la relation `→ 📥 Documents Source`. Si oui → `notion-update-page` au lieu de `notion-create-pages`
- **Niveau Apps Script** : si le fichier n'est plus dans `📥 INBOX` (déjà déplacé), no-op silencieux. Le script peut tourner sur la même fiche plusieurs fois sans effet de bord

## Trigger Apps Script (info, ne pas appeler depuis ce skill)

L'Apps Script `AgoraLive Drive Mover` tourne toutes les 5 minutes sur le projet Google Apps Script de `paul@agoralive.ai` (`https://script.google.com/...`). Algorithme :

1. Query la base maître Notion pour les items avec `🚦 Statut routage = ✅ Routé` AND `📁 Drive cible (folder ID)` non vide
2. Pour chaque, extraire le Drive file ID depuis `🔗 URL fichier`
3. Vérifier que le fichier est encore dans `📥 INBOX` (sinon skip — déjà bougé)
4. `DriveApp.getFileById(fileId).moveTo(targetFolder)` selon `📁 Drive cible`
5. Logger le résultat

Les logs Apps Script sont consultables dans le journal d'exécution côté script.google.com.

## Récap chat (fin d'exécution)

Format obligatoire à rendre à l'utilisateur :

```
✅ Document routé : <Titre>
📁 Drive cible : <chemin lisible> (move planifié dans les 5 min par Apps Script)
📥 Fiche maître : <URL Notion>
🎯 Bases alimentées (<N>) :
  - 📜 Contrats — <URL Notion> (créé)
  - 👤 Personnes — <URL Notion> (créé) / <URL> (réutilisé)
  - 🏛️ Organisations — <URL Notion> (réutilisé)
🧠 Confiance : <score>% — <statut>
```

Si confiance < 70 :

```
⚠️ Classification incertaine (<score>%). Fiche maître créée en statut 🔄 En classification.
Aucune propagation aux bases dérivées. Aucun move Drive prévu.
Valide manuellement le type dans <URL maître> puis redemande "route à nouveau".
```

Si plusieurs fiches en mode C (note vocale multi-sujets) :

```
✅ Note vocale routée : <Titre / extrait>
📁 Drive : reste dans 🎙️ Inbox Vocale (multi-distribution Notion uniquement)
📥 Fiche maître : <URL>
🎯 Sujets identifiés et distribués (<N>) :
  - 🐛 Bug "page admin lente" → <URL>
  - 📅 Compte-rendu "call sponsoring SFODF" → <URL>
  - 👤 Personnes "Pierre M." → <URL>
🧠 Confiance distribution : <score>%
```

## Sécurité et permissions

- Contrats, cessions, CV : sous-dossiers Drive avec ACL restreints (configurer côté Drive Workspace, pas côté skill)
- Si l'utilisateur déposant n'a pas les droits Drive sur le dossier cible → l'Apps Script échouera silencieusement et loggera l'erreur dans son journal ; vérifier les Apps Script logs en cas de blocage récurrent
- Les notes vocales (`🎙️ Inbox Vocale`) sont visibles à toute l'équipe AgoraLive par défaut, attention au contenu sensible

## Setup nouveau membre AgoraLive

Pour qu'un nouvel humain (Julie, Éloi, Michelle, Olivia, Philippine, ou futur joiner) puisse utiliser ce flux :
1. Avoir un compte Workspace `@agoralive.ai` avec accès au Shared Drive AgoraLive
2. Avoir le plugin `agoralive-core` installé dans Cowork (`claude plugin install agoralive-core@agoralive-plugins`)
3. C'est tout. L'infrastructure (Apps Script, SA GCP, Notion integration, dossiers Drive) est mutualisée et déjà en place.

## Historique versions

- **v2** (2026-05-17) — Pivot architectural : 3 modes d'ingestion (INBOX/Cowork/Inbox Vocale), Apps Script externe pour les moves Drive, suppression du upload Cowork→Drive direct (trop lent), support natif des notes vocales Notion AI multi-distribution
- **v1** (2026-05) — Première version : upload Cowork→Drive direct, structure Drive `AgoraLive — Documents Source/<Type>/<Année>/`, sans Apps Script
