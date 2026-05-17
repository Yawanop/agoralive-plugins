---
name: bp-challenge-philippe
description: >
  Ouvre BP Lab pour Philippe (en mode Mentor BA) et challenge une hypothèse
  spécifique du Business Plan. Sort l'historique des arguments pour/contre déjà
  votés, propose des angles d'attaque contra-intuitifs, identifie les variables
  les plus sensibles, et drafte une fiche d'hypothèse au format requis (Hypothèse +
  Variable + Valeur actuelle + Valeur proposée + Argumentaire). À déclencher
  quand Philippe (ou Philippine en mode BA) demande : "Philippine challenge
  l'hypothèse X", "ouvre BP Lab côté contre", "fais-moi le contradictoire sur Y".
---

# bp-challenge-philippe — Challenge BP côté Mentor BA

## Mission

Donner à Philippe (en mode Mentor BA) la matière contradictoire pour challenger efficacement une hypothèse du BP en Comité Mentor — c'est son vrai terrain de valeur ajoutée.

---

## Procédure

### Étape 1 — Identifie l'hypothèse à challenger

Demande à Philippe (ou déduis du contexte) :
- Quelle hypothèse précise ? (titre + variable concernée)
- Quel angle de challenge ? (trop optimiste / trop conservateur / mal sourcée / dépendance cachée)

### Étape 2 — Ouvre BP Lab + historique

```
notion-fetch sur https://www.notion.so/24dc5471875c4821acce30c9e193b7c7
```

Pour l'hypothèse ciblée, récupère :
- Statut actuel (Soumis / En débat / Validé / Rejeté)
- Arguments POUR déjà votés (colonne 👍)
- Arguments CONTRE déjà votés (colonne 👎)
- Commentaires associés

### Étape 3 — Identifie 3 angles de contradiction

Pour une hypothèse donnée, propose 3 contre-angles :

1. **Angle "empirique"** : qu'est-ce que le terrain dit déjà (ou ne dit pas encore) sur cette hypothèse ?
2. **Angle "sensibilité"** : que se passe-t-il si la valeur est ±20% / ±50% ? Le BP tient-il ?
3. **Angle "dépendance cachée"** : sur quelle autre hypothèse cette hypothèse repose-t-elle silencieusement ?

### Étape 4 — Drafte une simulation chiffrée

Si pertinent, propose 2-3 scénarios :

```
Scénario base : hypothèse à <X>
Scénario pessimiste : hypothèse à <0.7 × X> → impact runway = <Y mois en moins>
Scénario ambitieux : hypothèse à <1.3 × X> → impact runway = <Z mois en plus>
```

### Étape 5 — Restitue la fiche prête à soumettre

```
🧠 Challenge BP — <titre hypothèse>

Variable : <nom>
Valeur actuelle BP : <X>
Valeur proposée : <Y> (ou range)

📋 Argumentaire :
1. Angle empirique : <texte>
2. Angle sensibilité : <texte + simulation>
3. Angle dépendance : <texte>

🎯 Question à Paul + Julien : <question précise pour Comité Mentor>

📤 À soumettre dans BP Lab avec statut "📥 Soumis", priorité <P1/P2/P3>
```

---

## Anti-patterns

- ❌ **Ne challenge pas pour challenger** — vise une amélioration du BP, pas une opposition stylistique.
- ❌ **N'invente pas de chiffres** — base-toi sur le BP existant et les données terrain.
- ❌ **Ne décide pas à la place de Paul + Julien** — tu prépares le challenge, ils trancheront en Comité.
- ❌ **Ne duplique pas un argument déjà voté** — vérifie l'historique BP Lab d'abord.

## Identifiants Notion utiles

- 💡 BP Lab : `24dc5471875c4821acce30c9e193b7c7`
- 📈 Business Plan : `35e6979fbcd181f2b785dd872ba12722`
- 🧠 Cockpit Philippe BA : `3616979fbcd18101bed6db9fefb3dcbb`
- 🧠 Comité Mentor : `35e6979fbcd181569dc6c3cc418d6774`
