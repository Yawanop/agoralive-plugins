---
name: prep-sprint-planning
description: >
  Prépare le sprint planning hebdo de Philippe (CTO) avec Paul & Julien (POs).
  Agrège depuis Notion : charge actuelle (bugs en cours + effort cumulé), bugs
  livrés en attente retest Paul, FRs à clarifier avec POs, bugs orphelins à
  reclasser, vélocité du sprint précédent. Propose une slide de planning prête
  à dérouler. À déclencher quand Philippe (ou Philippine) demande : "prépare le
  sprint planning", "qu'est-ce qu'on planifie cette semaine", "Philippine
  planning", "il faut prep le sprint avec Paul et Julien".
---

# prep-sprint-planning — Prep sprint planning Philippe + Paul + Julien

## Mission

Donner à Philippe une **matière claire** pour son sprint planning hebdo avec Paul & Julien, pour que la réunion serve à décider, pas à découvrir.

---

## Procédure

### Étape 1 — Ouvre le Cockpit Philippe CTO + sprint en cours

```
notion-fetch sur https://www.notion.so/3606979fbcd1811c9609e3c85ed9fada
notion-fetch sur le sprint en cours (3606979fbcd181e3b271ebfa88ba9a42)
```

### Étape 2 — Calcule la vélocité de la semaine passée

Depuis la base Bugs (`4dc80e0b2bf04fe696e18a3f8510b117`), récupère les bugs **livrés cette semaine** (statut `👀 À retester` ou `✅ Résolu`, avec date résolution dans les 7 derniers jours).

Somme l'effort estimé (XS=0.5, S=1, M=3, L=8, XL=20) → vélocité hebdo.

### Étape 3 — Calcule la charge restante du sprint

Bugs assignés à Philippe, statut `🔧 En cours` ou `📥 À traiter`, somme effort estimé restant.

### Étape 4 — Identifie les sujets de planning

Liste 4 catégories pour la réunion :

1. **🔧 À continuer** : bugs `🔧 En cours` non finis cette semaine
2. **🧪 À retester (côté Paul)** : bugs `👀 À retester` que Paul doit valider — combien et combien depuis quand
3. **❓ FRs à clarifier** : bugs orphelins ou commentaires `❓ Question Paul` — à débloquer en réunion
4. **🎯 À prendre** : bugs `📥 À traiter` non assignés, triés P0 → P3, pour décider lesquels embarquer

### Étape 5 — Restitue la slide planning

Format imposé :

```
🚀 Sprint Planning — semaine du <date>

📊 Vélocité semaine passée : <X points> (livrés : <N> bugs)
📊 Charge restante en cours : <Y points>
📊 Capacité disponible (estimée) : <Z points>

1️⃣ À continuer (déjà en cours)
• <Bug + effort restant>

2️⃣ À retester côté Paul (action de Paul)
• <Bug + jours depuis livraison>

3️⃣ FRs à clarifier avec Paul/Julien
• <Bug + question ouverte>

4️⃣ À embarquer cette semaine (à décider)
• <Bug — P? — effort estimé — pourquoi prio>
• <…>

⏱️ Suggestion de cadrage 30 min :
• 5 min vélocité + état
• 10 min retest + clarifications (Paul actionne)
• 15 min décision embarquement
```

### Étape 6 — Adapte la suggestion d'embarquement

Si la capacité disponible est < 50% de la vélocité passée → propose de **réduire les nouveaux embarquements** et flag : *"⚠️ Beaucoup de charge restante, attention à ne pas surcharger."*.

Si elle est saine → propose une sélection cohérente (priorité × effort) qui rentre dans la capacité.

---

## Anti-patterns

- ❌ **Ne décide pas seul de l'embarquement** — tu proposes, Paul + Julien (POs) tranchent.
- ❌ **N'ignore pas les FRs ouverts** — c'est souvent ça qui bloque le sprint si pas clarifié en réunion.
- ❌ **Ne sur-évalue pas la vélocité** — utilise les bugs **vraiment livrés**, pas ceux en cours.
- ❌ **Ne pousse pas à prendre les P3** si les P0/P1 ne sont pas couverts d'abord.

---

## Identifiants Notion utiles

- 🦁 Cockpit Philippe CTO : `3606979fbcd1811c9609e3c85ed9fada`
- 🎯 Vue Sprint par priorité : `3606979fbcd181e3b271ebfa88ba9a42`
- 🐛 Base Bugs : `4dc80e0b2bf04fe696e18a3f8510b117`
- 📋 Base Requirements : `5911b1baad614679aeed2b43a6595811`
- 🚀 Hub Produit & app : `35e6979fbcd18100b373fab843c12f9d`
