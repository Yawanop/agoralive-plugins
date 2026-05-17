---
name: commit-message-helper
description: >
  Génère un message de commit Git conforme à la convention AgoraLive (BUG-N dans
  le message + verbe d'action + description courte). Sait gérer multi-IDs, les
  marqueurs spéciaux (WIP, wontfix, fixes/closes), et adapte selon la cible
  (push main vs PR vs branche). Pour Philippe (CTO). À déclencher quand Philippe
  (ou Philippine) demande : "drafte mon commit", "format BUG-N pour ce fix",
  "Philippine aide-moi à écrire le commit", "j'ai fixé BUG-42, formule le
  commit", "commit message".
---

# commit-message-helper — Génération message de commit conforme

## Mission

Aider Philippe à écrire des commits conformes à la convention AgoraLive — celle qui déclenche le **sync auto GitHub → Notion** sur les fiches Bug.

---

## Convention AgoraLive (à respecter)

### Format de base

```
<type>(<scope optionnel>): BUG-<id> <description courte>
```

Exemples valides :

```
fix(admin): BUG-42 le bouton Enregistrer persiste l'email avec un point
feat: BUG-7 ajout du toggle 2FA sur /settings
refactor(users): BUG-12, BUG-15 nettoyage du module
chore: BUG-3 bump dependencies
Fixes BUG-3 — closes BUG-4
```

### Multi-IDs

Plusieurs IDs autorisés dans le même commit, séparés par espace ou virgule :
```
BUG-12, BUG-15
BUG-12 et BUG-15
fix BUG-12 BUG-15
```

### Casse insensible et variantes

Acceptés : `BUG-42`, `bug-42`, `BUG_42`, `BUG42`, `bug 42`.

### Marqueurs spéciaux

| Marqueur | Effet sur statut Notion |
|---|---|
| `WIP BUG-42` ou `[draft] BUG-42` | `🔧 En cours` (même sur push main) |
| `wontfix BUG-99: hors scope V1` | `❌ Won't fix` (le message sert de justif) |
| `Fixes BUG-3 — closes BUG-4` | Les deux passent à `👀 À retester` |

---

## Paramètres d'invocation

1. **`description`** : ce qu'a fait le commit (en 1-2 phrases)
2. **`bug_ids`** : un ou plusieurs IDs (ex : "BUG-42" ou "BUG-12, BUG-15")
3. **`type`** : optionnel — `fix`, `feat`, `refactor`, `chore`, `docs`, `test`, `style`. À deviner si Philippe ne précise pas.
4. **`scope`** : optionnel — module touché (`admin`, `users`, `auth`, etc.)
5. **`cible`** : optionnel — `main` (par défaut) · `pr` · `branch` · `wip`

---

## Procédure

### Étape 1 — Vérifie que les BUG-IDs existent

Cherche chaque ID dans la base Bugs (`4dc80e0b2bf04fe696e18a3f8510b117`). Si un ID est introuvable → flag : *"BUG-X introuvable dans Notion. Tu veux que je le crée ou tu corriges l'ID ?"*. Sinon le sync ne fera rien et tu auras le bug "in the void".

### Étape 2 — Identifie le type (si pas fourni)

Devine selon la description :
- "fix", "corrige", "résout" → `fix`
- "ajoute", "implémente", "crée" → `feat`
- "refacto", "réorganise", "simplifie" → `refactor`
- "doc", "readme", "explique" → `docs`
- "test", "spec" → `test`
- "bump", "deps", "lint", "config" → `chore`

Si vraiment ambigu → propose les 2 plus probables.

### Étape 3 — Drafte le message

```
<type>(<scope>): BUG-<id> <description en max 60 caractères>
```

Si description trop longue → propose une version courte (ligne 1) + corps optionnel (lignes suivantes).

### Étape 4 — Adapte selon la cible

- **`cible: main`** (défaut) : commit "propre" qui déclenche le sync → bug passe à `👀 À retester`
- **`cible: pr`** : commit "fix en PR" → le sync passe à `🔧 En cours` (puisque pas mergé)
- **`cible: branch`** : pareil que PR
- **`cible: wip`** : préfixe `WIP` ajouté → `🔧 En cours` même sur push main

### Étape 5 — Restitue + alternatives

```
✍️ Commit suggéré :
   fix(admin): BUG-42 corrige persistance email avec point final

📝 Alternatives :
   • Court : fix: BUG-42 fix email persistence
   • Long :  fix(admin): BUG-42 corrige persistance email avec point final
            
            La validation regex acceptait un point en fin d'adresse,
            qui faisait échouer la sauvegarde silencieuse.

📌 Convention rappel : `git commit -m "<message>"`. Push sur main → bug passe à 👀 À retester.
```

---

## Anti-patterns

- ❌ **Ne génère pas un commit sans BUG-ID** si Philippe en mentionne un — la convention l'exige pour déclencher le sync.
- ❌ **Ne génère pas un commit avec un BUG-ID inexistant** dans Notion — flag avant.
- ❌ **Ne dépasse pas 72 caractères** sur la ligne 1 (convention Git).
- ❌ **N'utilise pas de marqueur spécial** (WIP, wontfix) sans confirmation de Philippe — c'est sa décision pas la tienne.
- ❌ **Ne propose pas plusieurs IDs dans un seul commit** si ce n'est pas explicitement demandé.

---

## Identifiants Notion utiles

- 🐛 Base Bugs : `4dc80e0b2bf04fe696e18a3f8510b117`
- 🦁 Cockpit Philippe CTO (où le workflow GitHub→Notion est documenté) : `3606979fbcd1811c9609e3c85ed9fada`
