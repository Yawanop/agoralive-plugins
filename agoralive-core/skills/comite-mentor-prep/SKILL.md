---
name: comite-mentor-prep
description: >
  Prépare Paul (CEO) pour le Comité Mentor mensuel 45 min avec Philippe Salah
  (Business Angel) et Julien. Côté Paul = production des 2-3 questions
  stratégiques précises à poser à Philippe pendant le bloc "arbitrages + sujet
  stratégique" du Comité. Lit le tableau de bord (KPI, trésorerie, runway),
  identifie les hypothèses BP en attente, les arbitrages en cours, les risques,
  et drafte les questions à fort levier. Complémentaire de `comite-mentor-synthese-1p`
  (Julie, côté direction → envoie la synthèse à Philippe 48h avant). Pour Pauline.
  À déclencher quand Paul (ou Pauline) demande : "prépare le Comité Mentor",
  "j'ai Comité Mentor mardi prépare-moi", "Pauline prépa Comité", "questions
  pour Philippe Salah".
---

# comite-mentor-prep — Prep Paul pour Comité Mentor mensuel

## Mission

Donner à Paul (CEO) **les 2-3 questions stratégiques précises** à poser à Philippe Salah (Business Angel) pendant le Comité Mentor mensuel. Pas une note d'intention vague — des questions affûtées qui transforment l'heure passée avec Philippe en levier d'arbitrage.

Le rituel est **sacralisé** (45 min, slot fixe, jamais sauté). Sans prep solide, c'est 45 min perdues.

---

## Procédure

### Étape 1 — Lit le tableau de bord du mois

Récupère :

1. **📊 KPI mensuels** (`fa0b21be8f6b4569aa4431e42320d7da`) : tendance CA pipeline, CA confirmé, trésorerie, runway, conversion sponsor, NPS, articles publiés
2. **📈 Business Plan** (`35e6979fbcd181f2b785dd872ba12722`) : écart actuel vs ramp 6→40→80→130 deals
3. **💰 Trésorerie & runway** : burn rate moyen, mois de visibilité restants
4. **🎯 OKR / KR du trimestre** : progression vs cible

### Étape 2 — Identifie les zones de tension stratégique

Trois familles à examiner :

1. **Écarts vs BP** — où la réalité dévie significativement (> 20%) de l'hypothèse
2. **Décisions en attente** — qu'est-ce que Paul + Julien hésitent à trancher seuls (allocation budget, recrutement clé, pivot pricing) ?
3. **Risques émergents** — qu'est-ce qui pourrait dérailler le BP dans les 3-6 mois si rien n'est fait ?

### Étape 3 — Identifie les hypothèses BP à challenger

Ouvre **BP Lab** (`24dc5471875c4821acce30c9e193b7c7`). Liste :
- Hypothèses au statut `📥 Soumis` ou `🔄 En débat` qui n'ont pas été tranchées
- Hypothèses qui méritent une re-validation après évolution terrain
- Nouvelles hypothèses à soumettre suite au tableau de bord

### Étape 4 — Drafte 2-3 questions stratégiques

Une bonne question Comité Mentor est :
- **Spécifique** : pas "ça avance ?" mais "On a converti 22% des sponsors approchés vs 35% au BP. Tu vois quoi comme cause ?"
- **Provocante** : challenge un présupposé que Paul + Julien tiennent pour acquis
- **Décisionnelle** : appelle une réponse Philippe qui débloque une décision Paul + Julien

Format pour chaque question :
```
Question <N> : <formulation précise>
  
  Contexte (à exposer à Philippe en 2 phrases avant la question) :
  <le chiffre, la tendance ou l'hypothèse qui motive la question>
  
  Réponse attendue (type) :
  <ex : un go/no-go sur recrutement, un avis sur réallocation budget, une lecture du risque>
```

### Étape 5 — Identifie le "sujet stratégique du mois"

Le Comité a un bloc 7 min "Stratégie & vision". Propose **un seul** sujet de fond :
- Positionnement marché (concurrents, différenciation)
- Levée de fonds (timing, montant, dilution)
- Expansion (nouveau segment, nouveau pays, nouveau produit)
- Pivot pricing
- Décision de leadership / recrutement clé

### Étape 6 — Restitue la note prep côté Paul

Format imposé :

```
🦊 Prep Comité Mentor — <date> · 45 min

📊 Ma lecture du mois (résumé interne, à NE PAS exposer en Comité comme tel)
• Trésorerie : <X k€> · Runway : <Y mois>
• CA confirmé : <X k€> vs cible <Y k€> = <écart>
• Pipeline pondéré : <X k€>
• Faits marquants : <2-3 points>

🎯 Mes 2-3 questions pour Philippe (à poser pendant les 25 min arbitrage+sujet stratégique)

Q1 : <Question précise>
  Contexte : <2 phrases>
  Réponse attendue : <type>

Q2 : <Question précise>
  Contexte : <2 phrases>
  Réponse attendue : <type>

Q3 (si pertinent) : <Question précise>

💡 Hypothèses BP à challenger ce comité
• <Hypothèse 1 — pourquoi maintenant>
• <Hypothèse 2>

🧭 Sujet stratégique proposé pour les 7 min "Vision"
• <Titre> — <Position Paul+Julien actuelle> — <Ce que tu veux entendre de Philippe>

⏱️ Reminder agenda type
• 0-5 min : lecture commune tableau de bord
• 5-15 min : hypothèses challengées (Q1, Q2)
• 15-25 min : arbitrages en cours (Q3 + décisions à trancher)
• 25-35 min : risques & alertes
• 35-42 min : sujet stratégique du mois
• 42-45 min : CR validé en séance
```

---

## Anti-patterns

- ❌ **Ne pose pas de questions creuses** ("comment ça va ?") — perte de temps Philippe.
- ❌ **N'oublie pas le runway** — c'est la métrique-pivot du mentor BA, toujours en lecture du mois.
- ❌ **Ne propose pas plus de 3 questions** — l'attention de Philippe est limitée, mieux vaut 3 bonnes que 6 moyennes.
- ❌ **Ne décide pas à la place de Paul + Julien** — tu prépares les questions, ils tranchent avec Philippe en séance.
- ❌ **Ne mélange pas avec le côté Julie** (`comite-mentor-synthese-1p`) — ici on prépare les questions de Paul, pas la synthèse 1 page envoyée 48h avant.
- ❌ **N'oublie pas le CR validé EN SÉANCE** — c'est la règle d'or du rituel. Si Pauline propose à Paul de "valider le CR plus tard", elle viole la règle.

---

## Cas particuliers

### Premier Comité Mentor (pas d'historique)
→ Questions plus structurelles : "Sur quelle métrique tu mesurerais la santé d'AgoraLive ?", "Quelle hypothèse du BP tu trouves la plus risquée ?"

### Comité après un évènement majeur (signature gros sponsor, perte client clé, recrutement clé)
→ La Q1 doit explicitement remonter l'évènement : "On a signé Henry Schein à 18k€, ça change quoi à ton avis sur le ramp ?"

### Paul a déjà tranché mentalement une décision
→ Drafte une question contradictoire : *"Pose-la comme si tu n'avais pas décidé — Philippe te sert à challenger, pas à valider."*. Sinon le Comité ne sert à rien.

### Mois où tout va bien (rare)
→ Pas de fausse question. Propose plutôt un sujet stratégique à fond : "Bon mois — utilisons les 45 min pour réfléchir levée fonds ou expansion".

---

## Identifiants Notion utiles

- 🧠 Comité Mentor Philippe Salah : `35e6979fbcd181569dc6c3cc418d6774`
- 📊 KPI mensuels : `fa0b21be8f6b4569aa4431e42320d7da`
- 📈 Business Plan : `35e6979fbcd181f2b785dd872ba12722`
- 💡 BP Lab : `24dc5471875c4821acce30c9e193b7c7`
- 🎯 OKR : `88627a768f894c07a2a7ee5a7044c1cd`
- 🔑 Key Results : `4bbcafe6f62147d9a705b27f0ddcd130`
- 💰 Squad Finance : `3626979fbcd18164b631d9a3a5771a3f`
- 🦊 Cockpit Paul : `3616979fbcd18186bf48cb87faa13af3`
