---
name: sprint-status-philippe
description: >
  Brief daily du sprint pour PHILIPPE (CTO), ANGLE DEV — ce qu'il doit prendre
  maintenant, ce qu'il a livré, sa charge vs capacité, FRs à clarifier. À
  déclencher UNIQUEMENT quand Philippe (ou Philippine) demande : "brief le sprint
  pour moi", "qu'est-ce que JE dois prendre", "Philippine quoi de neuf côté
  sprint", "Philippine sprint-moi", "ma file dev". DIFFÉRENT de
  cockpit-philippe-watch (angle PO Paul, ce que PAUL doit retester / valider) :
  si Paul ou Pauline demande "où en est Philippe", invoquer cockpit-philippe-watch
  à la place. Anti-trigger : tout prompt qui vient de Paul/Pauline.
---

# sprint-status-philippe — Brief sprint pour Philippe (CTO)

## Mission

Donner à Philippe (ou à Philippine) une vue **opérationnelle dev** de son sprint : quelle carte prendre maintenant, qu'est-ce qui attend, où il en est de sa capacité.

C'est le pendant CTO du skill `cockpit-philippe-watch` (qui donne l'angle PO Paul sur le même sprint).

---

## Procédure

### Étape 1 — Ouvre le Cockpit Philippe CTO

```
notion-fetch sur https://www.notion.so/3606979fbcd1811c9609e3c85ed9fada
```

### Étape 2 — Récupère les 4 segments dev

1. **🎯 Prochaine carte à prendre** : vue Sprint par priorité (`3606979fbcd181e3b271ebfa88ba9a42`), trier P0 → P3 puis par sévérité, prendre la première qui n'est pas déjà en `🔧 En cours`
2. **🔧 Ses bugs en cours actuellement** : statut `🔧 En cours`, assigné à Philippe — combien + effort cumulé estimé
3. **🧪 Ses livrés en attente retest Paul** : statut `👀 À retester` — combien et depuis combien de temps
4. **❓ FRs à clarifier** : bugs orphelins (sans FR) où Philippe est assigné, ou bugs avec commentaire `❓ Question Paul`

### Étape 3 — Brief formaté CTO

```
🦁 Yo Philippe. État sprint :
🎯 Prochaine carte : <Titre bug + ID + sévérité + route impactée>
🔧 Tu as en cours : <nombre> bug(s), effort estimé <total XS/S/M/L/XL>
🧪 Livrés en attente retest Paul : <nombre> (le + ancien : <Nj>)
❓ Questions ouvertes pour Paul : <nombre>

👉 Action : <ex : Tu attaques BUG-42 (P0, S, route /soumettre) — celui-là débloque le sprint>
```

Si la prochaine carte est P0/P1 → marqueur ⚠️ pour visibilité.
Si la file en cours est saturée (>3 bugs M+) → propose un focus : *"Tu as 4 trucs M+ en cours, tu fermes celui-ci avant d'en prendre un nouveau ?"*.
Si rien à prendre (sprint vide) → propose : *"Sprint au calme. Bon moment pour reviewer une PRD ou avancer sur dette technique."*

### Étape 4 — Suggestions de routage

- Pour le bug à prendre → propose `bug-triage-cto` si pas encore diagnostiqué
- Pour fermer un bug → rappelle convention `commit-message-helper` (BUG-N dans le commit)
- Pour les FRs à clarifier → suggère un sync rapide avec Paul (ou ping via mail-rediger voix philippe-cto)

---

## Anti-patterns

- ❌ **Ne fais pas le boulot de Paul** (pas de retest, pas de priorisation produit) — tu donnes l'angle CTO uniquement.
- ❌ **N'invente pas de bugs** — si la base est vide, dis-le.
- ❌ **Ne pousse pas Philippe à prendre une carte qui dépend d'une clarification produit** — flag plutôt que d'ignorer.
- ❌ **Ne mélange pas avec l'angle BA** — pour les KPI/OKR/BP, utilise `prep-comite-mentor-ba`.

---

## Identifiants Notion utiles

- 🦁 Cockpit Philippe CTO : `3606979fbcd1811c9609e3c85ed9fada`
- 🎯 Vue Sprint par priorité : `3606979fbcd181e3b271ebfa88ba9a42`
- 📊 Vue État des bugs : `3606979fbcd181dd867bcce3a6be26b5`
- 🐛 Base Bugs : `4dc80e0b2bf04fe696e18a3f8510b117`
- 🗺️ Base Routes : `42c3546d6b5345d2bc0a89bce5560eea`
- 📋 Base Requirements : `5911b1baad614679aeed2b43a6595811`
