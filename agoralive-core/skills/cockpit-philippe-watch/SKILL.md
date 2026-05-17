---
name: cockpit-philippe-watch
description: >
  Brief daily du sprint Philippe (CTO) à destination de Paul (PO). Ouvre le Cockpit
  Philippe CTO Notion, identifie les bugs P0/P1 actifs, les bugs à retester par
  Paul (statut 👀 À retester), les FRs bloqués, les bugs orphelins (sans FR à
  associer), et restitue un brief court actionnable pour Paul. À déclencher quand
  Paul (ou sa jumelle Pauline) demande : "où en est Philippe", "fais le tour du
  sprint", "qu'est-ce qui chauffe côté dev", "brief sprint", "Philippe a livré
  quoi", "qu'est-ce que je dois retester", "Pauline regarde où en est le sprint".
  Skill mutualisable : Julien peut aussi l'invoquer via Julie pour sync sprint
  planning.
---

# cockpit-philippe-watch — Brief sprint pour Paul (PO)

## Mission

Donner à Paul (ou à son jumeau Pauline) une vue à 360° du sprint en cours de Philippe (CTO), focalisée sur **ce que Paul doit faire** : tri des bugs orphelins, validation des routes, retest des bugs livrés.

---

## Procédure

### Étape 1 — Ouvre le Cockpit Philippe CTO

```
notion-fetch sur https://www.notion.so/3606979fbcd1811c9609e3c85ed9fada
```

Ne pas ouvrir le Cockpit Philippe BA (ce n'est pas le bon angle pour un brief sprint).

### Étape 2 — Récupère les 4 segments

Depuis la base Bugs (`4dc80e0b2bf04fe696e18a3f8510b117`) et la base Routes (`42c3546d6b5345d2bc0a89bce5560eea`), récupère :

1. **🔥 Bugs P0/P1 actifs** : statut ≠ ✅ Résolu et ≠ ❌ Won't fix, sévérité P0 ou P1
2. **🧪 Bugs à retester par Paul** : statut `👀 À retester`
3. **🚧 FRs bloqués** : depuis la base Requirements (`5911b1baad614679aeed2b43a6595811`), ceux marqués bloqués
4. **🐛 Bugs orphelins (sans FR)** : bugs sans relation vers un Requirement — c'est une spec manquante à proposer à Paul, ou un hors-périmètre à reclasser

### Étape 3 — Brief formaté

```
🦁 Sprint Philippe — état :
• 🔥 P0/P1 actifs : <nombre> (top : <titre du plus chaud>)
• 🧪 À retester par toi : <nombre> bug(s) — <titres ou IDs>
• 🚧 FRs bloqués : <nombre> — <à clarifier avec Philippe>
• 🐛 Orphelins (sans FR) : <nombre> — à trier dans la base

👉 Recommandation : <l'action la plus urgente, ex : retester BUG-42 qui bloque le sprint>
```

Si les 4 segments sont vides, dis-le franchement : *"Sprint au vert, Philippe avance, rien ne t'attend."*

---

## Notes d'usage

- Ce skill ne **modifie rien** dans Notion — il lit et restitue.
- Pour traiter un bug en particulier (retest, validation, fermeture), bascule sur `po-bug-agoralive`.
- Pour la vue stratégique BA de Philippe (KPI, BP, runway), utilise le cockpit Mentor BA, pas celui-ci.

## Identifiants Notion utiles

- 🦁 Cockpit Philippe CTO : `3606979fbcd1811c9609e3c85ed9fada`
- 🐛 Base Bugs : `4dc80e0b2bf04fe696e18a3f8510b117`
- 🗺️ Base Routes : `42c3546d6b5345d2bc0a89bce5560eea`
- 📋 Base Requirements : `5911b1baad614679aeed2b43a6595811`
- 🎯 Vue Sprint par priorité : `3606979fbcd181e3b271ebfa88ba9a42`
- 📊 Vue État des bugs (kanban) : `3606979fbcd181dd867bcce3a6be26b5`
