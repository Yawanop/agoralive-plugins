---
name: notion-document-router
description: |
  Pipeline d'alimentation à source de vérité unique pour les bases Notion AgoraLive + archivage Drive.
  L'utilisateur dépose un document (PDF, audio, image, transcription, brief, contrat, dictée bug…) — le skill
  (1) upload le fichier sur Google Drive dans l'arborescence officielle AgoraLive, (2) crée une fiche dans la
  base maître `📥 Documents Source` Notion avec le lien Drive, (3) classifie le type, (4) crée/met à jour
  les fiches dérivées dans les bases spécialisées concernées, liées à la maître par relations. Garantit
  idempotence, anti-doublon Notion ET Drive, traçabilité bout-en-bout. Triggers : "route ce document",
  "alimente les bases", "traite ce fichier", "classe ce contrat/cession/bug/article", "fais la fiche
  maître", "propage dans Notion", "pousse dans les bases", "upload sur Drive", "Documents Source", "📥",
  ou dépôt d'un fichier sans instruction. Aussi "traite la dernière ligne de Documents Source",
  "Notion routing". Anti-triggers : un seul type demandé explicitement avec skill dédié existant
  (`po-bug-agoralive`, `triage-contrat-agoralive`, `officiel-article-v3`) — déléguer.
---

# notion-document-router — Skill d'alimentation unifiée Notion + Drive

## Mission
Garantir qu'**un document = un fichier Drive archivé + une fiche source Notion + N fiches dérivées liées**, jamais de duplication, toujours rejouable.

---

## 1. Pré-requis (one-shot)

Avant la première exécution, vérifier que :

1. La base maître `📥 Documents Source` existe dans Notion. Si non → la créer (schéma minimal ci-dessous).
2. Le dossier racine Drive `AgoraLive — Documents Source` existe. Si non → le créer (à la racine du Drive partagé AgoraLive).
3. Les sous-dossiers par type existent dans le dossier racine : `Contrats/`, `Cessions/`, `Bugs/`, `Articles/`, `CV/`, `Devis/`, `Comptes-rendus/`, `Briefs/`, `Autres/`. Créer ceux manquants à la demande.

**Schéma minimal `📥 Documents Source`** : `📄 Titre`, `🔗 URL fichier Drive`, `📦 Type détecté` (select), `🚦 Statut routage` (select), `🎯 Bases cibles` (multi-select), `🧠 Confiance IA` (number), `📝 Résumé extrait` (text), `👤 Déposé par` (people), `🤖 Logs` (text), relations vers chaque base dérivée.

---

## 2. Procédure complète (7 étapes)

### Étape A — Lecture du document

1. Si l'utilisateur a uploadé un fichier dans Cowork → lire le contenu (Read pour texte/PDF/image, transcription pour audio).
2. Si l'utilisateur dit "traite la dernière ligne de Documents Source" → `notion-query-database-view` sur la base maître, filtrer `🚦 Statut routage = 📥 À traiter`, prendre la plus récente.
3. Si l'utilisateur fournit un lien Drive sans fichier local → télécharger via `download_file_content` Drive MCP, puis lire.

### Étape B — Classification

1. Identifier le **type** via signaux textuels/structurels (titre, structure, mots-clés). Types possibles : `Contrat`, `Cession`, `Bug`, `Article`, `CV`, `Devis`, `Compte-rendu`, `Brief`, `Autre`.
2. Calculer un **score de confiance 0-100** :
   - 90-100 : signaux multiples convergents (ex : titre "Contrat" + "Article 1" + signatures)
   - 70-89 : signaux clairs mais partiels
   - <70 : ambigu → ne **pas** router, juste créer fiche maître en `🔄 En classification` et arrêter
3. Identifier les **bases cibles** (1 à N) et les **entités nommées** (personnes, orgas, congrès, routes).

### Étape C — Anti-doublon Drive (lookup avant upload)

1. Construire le **chemin Drive cible** :
   ```
   AgoraLive — Documents Source/<TYPE>/<ANNÉE>/[<CONGRÈS si applicable>/]<nom_fichier>
   ```
   Exemple : `AgoraLive — Documents Source/Contrats/2026/SFODF/Cession_Yves_Surlemont.pdf`
2. **`search_files`** Drive MCP avec le nom du fichier dans le dossier cible.
3. Si un fichier au même nom existe **ET** que la taille/hash correspond → réutiliser le file ID existant, **ne pas re-uploader**.
4. Si nom identique mais contenu différent → ajouter suffixe `_v2`, `_v3`… au nom.

### Étape D — Upload Drive

1. Si le fichier vient d'un upload Cowork → le copier dans `/sessions/.../uploads/` accessible.
2. **`create_file`** Drive MCP avec :
   - `name` : nom propre (sans espace bizarre, garde l'extension d'origine)
   - `parent_id` : ID du sous-dossier cible (créer le sous-dossier d'année/congrès si manquant — voir note)
   - `content` : le fichier binaire
3. Récupérer le **`file_id`** et le **`webViewLink`** (lien Drive partageable).
4. Vérifier les permissions : le lien doit être accessible aux membres AgoraLive (par défaut le Drive partagé l'assure).

> **Note sur la création de dossier** : si la version actuelle du Drive MCP n'expose pas de `create_folder`, créer le sous-dossier manquant **manuellement** via une commande bash (gdrive CLI ou l'API REST). Si impossible, dégrader : uploader à la racine du dossier de type, et signaler à l'utilisateur "sous-dossier <X> à créer à la main".

### Étape E — Anti-doublon Notion (lookup avant création)

Pour chaque entité nommée à créer (`👤 Personnes`, `🏛️ Organisations`, `🏛️ Congrès`, `🗺️ Routes`) :
1. **`notion-search`** ciblé sur la base.
2. Si fuzzy match (nom exact ou email exact) → réutiliser l'ID existant.
3. Sinon → créer la fiche.

### Étape F — Création fiche maître + propagation

#### F.1 — Fiche maître

**`notion-create-pages`** dans `📥 Documents Source` avec :
- `📄 Titre` : titre actionnable extrait
- `🔗 URL fichier Drive` : `webViewLink` obtenu à l'étape D
- `📦 Type détecté` : selon taxonomie
- `🚦 Statut routage` : `🔄 En classification` (basculera à `✅ Routé` à la fin)
- `🎯 Bases cibles` : multi-select avec les bases ciblées
- `🧠 Confiance IA` : pourcentage
- `📝 Résumé extrait` : 3 phrases
- `👤 Déposé par` : utilisateur courant (Paul par défaut)
- `🤖 Logs` : timestamp + `Drive: <file_id>` + résultat classification

#### F.2 — Propagation aux bases dérivées

Pour chaque base cible identifiée :
1. **`notion-create-pages`** avec les champs spécifiques (cf. mapping ci-dessous) + la relation `→ 📥 Documents Source` pointant vers la maître + le `🔗 URL fichier Drive` recopié dans la fiche dérivée pour accès rapide.
2. Récupérer l'ID de la fiche dérivée.
3. **`notion-update-page`** sur la maître pour remplir la relation `→ <base>` avec cet ID.

### Étape G — Finalisation

1. **`notion-update-page`** sur la maître : `🚦 Statut routage` = `✅ Routé`, ajouter au champ `🤖 Logs` la liste des fiches créées (ID + base + URL).
2. Retour utilisateur : récap chat avec liens Notion vers la maître + toutes les dérivées + lien Drive.

---

## 3. Mappings champs (par base cible)

**Contrat → 📜 Contrats** : Partie 1, Partie 2, Date signature, Montant, Statut (Brouillon/En signature/Signé), 🔗 URL Drive, → 📥 Doc source
**Cession → 📝 Cessions** : Intervenant (relation Personnes), Conférence (relation), Date, Statut signature, 🔗 URL Drive, → 📥 Doc source
**Bug → 🐛 Bugs** : Titre actionnable, Route (relation), Sévérité (P0/P1/P2/P3), Statut (📥 À traiter), DoD, 🔗 URL Drive, → 📥 Doc source
**Article → ✍️ Articles** : Titre, Auteurs (relation Personnes), Conférence source (relation), Statut éditorial, 🔗 URL Drive, → 📥 Doc source
**CV → 👔 Recrutement** : Nom, Poste visé, Statut (📥 Sourcé), Date entretien, → 👤 Personnes (création), 🔗 URL Drive, → 📥 Doc source
**Devis Agoralib → 💰 Sponsors** : Congrès (relation), Montant, Tier, Statut négociation, 🔗 URL Drive, → 📥 Doc source
**Compte-rendu → 📅 Journal de bord** : Date, Participants (relation Personnes), Décisions, Actions, 🔗 URL Drive, → 📥 Doc source

---

## 4. Idempotence & rejouabilité

- **Niveau Drive** : avant upload, toujours `search_files` dans le dossier cible. Si même nom + même hash → réutiliser.
- **Niveau Notion fiche maître** : si une fiche maître existe déjà avec le même `🔗 URL fichier Drive` → ne pas en créer une nouvelle, mettre à jour celle qui existe.
- **Niveau fiches dérivées** : avant de créer une fiche dérivée, vérifier qu'il n'en existe pas déjà une liée à la même maître via la relation `→ 📥 Documents Source`. Si oui → `notion-update-page` au lieu de `notion-create-pages`.

---

## 5. Déclenchement depuis Notion

Trois patterns supportés :

1. **Push depuis Notion** : ligne créée dans `📥 Documents Source` avec lien Drive existant (pas de re-upload), statut `📥 À traiter`. Puis dans Cowork : *"Traite les nouveaux items de Documents Source"*.
2. **Drop direct Cowork** : fichier déposé dans Cowork chat → upload Drive + création maître + propagation.
3. **Scheduled task** : tâche planifiée (skill `schedule`) qui scanne `📥 Documents Source` toutes les 2h.

---

## 6. Récap chat (fin d'exécution)

Format obligatoire :

```
✅ Document routé : <Titre>
📁 Drive : <webViewLink>
📥 Fiche maître : <URL Notion>
🎯 Bases alimentées (<N>) :
  - 📜 Contrats — <URL>
  - 👤 Personnes — <URL> (créé) / <URL> (réutilisé)
  - 🏛️ Organisations — <URL> (réutilisé)
🧠 Confiance : <score>% — <statut>
```

Si confiance <70 :

```
⚠️ Classification incertaine (<score>%). Fichier uploadé sur Drive (<link>),
fiche maître créée en attente. AUCUNE propagation Notion aux bases dérivées.
Valide le type dans <URL maître> puis redemande "route à nouveau".
```

Si l'upload Drive échoue (permission, quota, MCP indispo) :

```
⚠️ Upload Drive échoué : <raison>. Fiche maître créée SANS lien Drive,
statut `🔄 En classification`. Re-uploade le fichier manuellement et
remplis le champ 🔗 URL fichier Drive, puis redemande "route à nouveau".
```

---

## 7. Sécurité et permissions

- Les contrats et cessions vont dans des sous-dossiers Drive **à accès restreint** (Olivier + Paul + Julien uniquement).
- Les CV vont dans un sous-dossier RH restreint.
- Les autres types (Bugs, Articles, Comptes-rendus, Briefs, Devis) sont accessibles à toute l'équipe AgoraLive.
- Si l'utilisateur déposant n'a pas les droits pour un type donné → uploader quand même (l'admin Drive valide), mais marquer la fiche maître `🚨 Vérif permissions à faire`.
