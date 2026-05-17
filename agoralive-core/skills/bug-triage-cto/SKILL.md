---
name: bug-triage-cto
description: >
  Diagnostic initial d'un nouveau bug par Philippe (CTO). À partir de la fiche
  Notion du bug (ou de sa description), identifie la route impactée, propose une
  hypothèse de cause, estime l'effort dev (XS/S/M/L/XL), suggère la priorité
  (P0/P1/P2/P3), et drafte un commentaire de prise en charge ("🚧 En cours + ETA").
  À déclencher quand Philippe (ou Philippine) demande : "diagnostic ce bug",
  "estime l'effort de BUG-X", "Philippine triage ce bug", "qu'est-ce qui se passe
  sur cette route", "BUG-X je le prends, fais-moi le triage".
---

# bug-triage-cto — Diagnostic initial d'un nouveau bug

## Mission

Quand un nouveau bug arrive (ou quand Philippe veut comprendre un bug existant), donner un **diagnostic initial structuré** pour qu'il sache : où regarder, combien ça va lui coûter, à quelle priorité le ranger.

---

## Paramètres d'invocation

1. **`bug_id`** ou **`description`** : identifiant du bug (ex : BUG-42) ou description si pas encore créé dans Notion
2. **`route_suspectée`** : optionnel, si Philippe a déjà une intuition

Si juste un texte de bug brut → propose d'abord de créer la fiche via `notion-document-router` ou `po-bug-agoralive`.

---

## Procédure

### Étape 1 — Récupère la fiche bug

```
notion-fetch sur la base Bugs (4dc80e0b2bf04fe696e18a3f8510b117), cherche le bug
```

Si trouvé, lit : titre, description, captures éventuelles, reproductibilité, route impactée (si déjà liée), sévérité (si déjà mise).

### Étape 2 — Identifie la route impactée

Si pas encore liée à une route :
1. Cherche dans la description les mots-clés d'URL (`/soumettre`, `/admin`, `/dashboard`, `/login`, etc.)
2. Cherche dans la base Routes (`42c3546d6b5345d2bc0a89bce5560eea`) celle qui matche
3. Si plusieurs candidates → demande à Philippe de désambiguïser
4. Si aucune → flag : *"Route non identifiée — Paul à clarifier"*

### Étape 3 — Propose une hypothèse de cause

Selon le pattern du bug, propose 2-3 hypothèses ordonnées par probabilité :

- **Backend (API)** : si erreur HTTP, données incorrectes, lenteur
- **Frontend (UI)** : si affichage cassé, état React/JS incohérent
- **Auth/permissions** : si bug d'accès, redirect, 401/403
- **Data/DB** : si bug sur le contenu, migration, requête
- **Intégration tierce** : si bug touche Notion, Drive, Stripe, etc.

Format :
```
Hypothèses de cause (par probabilité) :
1. <Cause la plus probable> — pourquoi tu le penses
2. <Alternative> — pourquoi possible aussi
3. <Long shot> — à investiguer si 1 et 2 échouent
```

### Étape 4 — Estime l'effort dev

Échelle AgoraLive :

| Niveau | Indication |
|---|---|
| **XS** | < 30 min — fix trivial, 1 ligne |
| **S** | 30 min - 2h — fix localisé, peu de tests |
| **M** | 2h - 1 jour — refacto léger, tests à ajouter |
| **L** | 1-3 jours — refacto plus large, impact multi-route |
| **XL** | > 3 jours — chantier structurel, sortir du sprint |

### Étape 5 — Suggère la priorité

Selon impact + reproductibilité :

| Priorité | Critère |
|---|---|
| **P0** | Bloque les utilisateurs sur un flow critique (login, captation, paiement) |
| **P1** | Bug visible sur un flow standard, contournement possible |
| **P2** | Bug mineur ou cas tordu, impact limité |
| **P3** | Esthétique, edge case rare, à voir avec PRD |

Si tu suggères P0 → flag explicitement : *"⚠️ Suggestion P0 — à valider rapidement avec Paul avant d'embarquer"*.

### Étape 6 — Drafte le commentaire de prise en charge

```
🚧 En cours
- Diagnostic initial : <hypothèse principale>
- Effort estimé : <XS/S/M/L/XL>
- Priorité suggérée : <P0/P1/P2/P3>
- ETA : <date selon effort + sprint en cours>
```

Si Philippe veut, il peut copier-coller ce commentaire dans la fiche bug Notion (ou tu peux le faire pour lui via `notion-update-page`).

---

## Anti-patterns

- ❌ **N'affirme pas une cause** sans investiguer — toujours présenter comme "hypothèse".
- ❌ **N'estime pas un XL sans alerter** — un XL doit sortir du sprint et passer en discussion produit.
- ❌ **Ne saute pas la route** — un bug sans route identifiée doit être flag (souvent = spec manquante).
- ❌ **Ne range pas en P0 par défaut** — réserve P0 aux vrais flows critiques utilisateur.
- ❌ **Ne décide pas seul de la priorité finale** — propose, Philippe + Paul valident.

---

## Identifiants Notion utiles

- 🐛 Base Bugs : `4dc80e0b2bf04fe696e18a3f8510b117`
- 🗺️ Base Routes : `42c3546d6b5345d2bc0a89bce5560eea`
- 📋 Base Requirements : `5911b1baad614679aeed2b43a6595811`
- 🦁 Cockpit Philippe CTO : `3606979fbcd1811c9609e3c85ed9fada`
