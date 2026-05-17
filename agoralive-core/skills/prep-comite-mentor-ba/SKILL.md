---
name: prep-comite-mentor-ba
description: >
  Prépare Philippe (en mode Mentor Business Angel) pour le Comité Mentor mensuel
  45 min avec Paul & Julien. Bascule sur son cockpit BA, lit KPI/OKR/trésorerie/
  runway, identifie les hypothèses BP en attente de challenge, et propose 3-4
  questions stratégiques précises à poser pendant le Comité. Sort une note de
  prep 1 page côté mentor. À déclencher quand Philippe (ou Philippine) demande :
  "prépare le Comité Mentor", "j'ai besoin de la prep côté BA", "Philippine
  passe en mode BA", "Comité du mois prochain prépare-moi".
---

# prep-comite-mentor-ba — Prep Comité Mentor côté Philippe (BA)

## Mission

Donner à Philippe (en mode Mentor BA) une **note de prep 1 page** avant le Comité Mentor mensuel — pour qu'il arrive avec ses challenges déjà identifiés et ses 3-4 questions stratégiques affûtées.

C'est le miroir de `comite-mentor-synthese-1p` qui sera invoqué par Julie (côté direction Paul+Julien envoie la synthèse à Philippe 48h avant). Ici, Philippine prépare la réception de Philippe.

---

## Procédure

### Étape 1 — Bascule sur le cockpit BA

```
notion-fetch sur https://www.notion.so/3616979fbcd18101bed6db9fefb3dcbb
```

(Pas le cockpit CTO — c'est l'angle BA qu'on prépare.)

### Étape 2 — Récupère la matière stratégique

1. **📊 KPI mensuels** (`fa0b21be8f6b4569aa4431e42320d7da`) : tendance des 3 derniers mois sur CA pipeline, CA confirmé, conversion sponsor, NPS, articles publiés, trésorerie
2. **🎯 OKR + Key Results** (`88627a768f894c07a2a7ee5a7044c1cd` et `4bbcafe6f62147d9a705b27f0ddcd130`) : progression du trimestre courant
3. **📈 Business Plan** (`35e6979fbcd181f2b785dd872ba12722`) : ramp 6→40→80→130 deals, hypothèses ARPU, runway
4. **💡 BP Lab — Hypothèses ouvertes** (`24dc5471875c4821acce30c9e193b7c7`) : hypothèses en attente de challenge (statut "Soumis" ou "En débat")
5. **🧠 Synthèse 1 page reçue 48h avant** : si Julie a déjà envoyé, lit-la pour aligner les questions

### Étape 3 — Identifie 3-4 challenges prioritaires

Pour chaque sujet, évalue :

- **Écart vs BP** : pipeline réel vs ramp ? CA confirmé vs cible ?
- **Hypothèse risquée** : laquelle peut faire dérailler le BP si elle s'effondre ?
- **Décision en attente** : Paul + Julien sont sur quoi qu'il faut débloquer ?
- **Sujet à fond du mois** : c'est quoi le sujet stratégique de ce comité (positionnement, levée, expansion, exit) ?

### Étape 4 — Drafte 3-4 questions précises

Une bonne question Mentor BA est :
- **Spécifique** : pas "comment va le commercial" mais "pourquoi la conversion sponsor est passée de 35% à 22% ce trimestre"
- **Provocante** : challenge un présupposé, pas un constat
- **Décisionnelle** : appelle une réponse Paul + Julien actionnable

Formate :
```
Question 1 : <question précise>
  Pourquoi : <ce que tu cherches à savoir / faire bouger>
  Réponse attendue : <type de réponse qui te suffit pour avancer>

Question 2 : <…>

Question 3 : <…>
```

### Étape 5 — Restitue la note 1 page

```
🧠 Prep Comité Mentor — <date> · 45 min · Mode BA

📊 Lecture du mois (chiffres clés)
• Trésorerie : <X k€> · Runway : <Y mois>
• CA confirmé : <X k€> · CA pipeline pondéré : <Y k€>
• Burn rate : <X k€/mois>
• Tendance significative : <ex : conversion sponsor en baisse>

🚨 Écarts notables vs BP
• <Écart 1> — interprétation possible
• <Écart 2>

💡 Hypothèses ouvertes à challenger
• <Hypothèse 1> — pourquoi elle mérite débat ce mois
• <Hypothèse 2>

🎯 Tes 3-4 questions stratégiques (à poser pendant les 25 min "arbitrages + sujet stratégique")
1. <Question>
2. <Question>
3. <Question>
(4. <Question si pertinent>)

🧭 Sujet stratégique du mois (proposé)
• <ex : Pivot pricing ou maintien grille ?>
```

---

## Anti-patterns

- ❌ **Ne décide pas à la place de Paul + Julien** — tu prépares les challenges, ils tranchent.
- ❌ **Ne pose pas de questions creuses** — "comment va le moral" ne sert à rien. Toujours spécifique + provocant + décisionnel.
- ❌ **Ne te mélange pas avec l'angle CTO** — pour le sprint, c'est `prep-sprint-planning`. Ici on est sur le BP, pas sur les bugs.
- ❌ **Ne survole pas les hypothèses BP** — c'est ton **vrai** terrain de mentor, c'est là qu'on attend ta valeur ajoutée.
- ❌ **N'oublie pas le runway** — c'est la métrique-pivot du mentor BA. Toujours en première section.

---

## Identifiants Notion utiles

- 🧠 Cockpit Philippe BA : `3616979fbcd18101bed6db9fefb3dcbb`
- 📊 KPI mensuels : `fa0b21be8f6b4569aa4431e42320d7da`
- 🎯 OKR : `88627a768f894c07a2a7ee5a7044c1cd`
- 🔑 Key Results : `4bbcafe6f62147d9a705b27f0ddcd130`
- 📈 Business Plan : `35e6979fbcd181f2b785dd872ba12722`
- 💡 BP Lab : `24dc5471875c4821acce30c9e193b7c7`
- 🧠 Comité Mentor Philippe Salah : `35e6979fbcd181569dc6c3cc418d6774`
- 💰 Squad Finance : `3626979fbcd18164b631d9a3a5771a3f`
