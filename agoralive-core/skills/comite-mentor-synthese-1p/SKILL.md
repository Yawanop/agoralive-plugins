---
name: comite-mentor-synthese-1p
description: >
  Produit la SYNTHÈSE 1 PAGE envoyée à Philippe Salah (Business Angel) 48h avant
  le Comité Mentor mensuel. Format reporting investisseur : KPI clés du mois,
  faits marquants, risques, 2-3 questions précises. Règle d'or du rituel : sans
  cette synthèse 48h avant, le Comité est diminué. Pour Julie (côté Julien =
  direction qui envoie). Complémentaire de `comite-mentor-prep` (Pauline, côté
  Paul = prépare les questions stratégiques à poser). À déclencher quand Julien
  (ou Julie) demande : "drafte la synthèse 1 page pour Philippe", "synthèse
  Comité Mentor", "Julie produit la note pour Philippe", "note 48h Comité".
---

# comite-mentor-synthese-1p — Synthèse 1 page envoyée à Philippe 48h avant

## Mission

Produire le document 1 page format reporting investisseur que **Julien envoie à Philippe Salah 48h avant le Comité Mentor**. C'est la matière sur laquelle Philippe va arriver préparé en séance.

Sans cette synthèse, Philippe découvre les chiffres en séance et le Comité perd 50% de sa valeur. **C'est non-négociable.**

---

## Procédure

### Étape 1 — Calcule la date d'envoi

Date Comité Mentor = par défaut 1er lundi du mois courant ou suivant. Date d'envoi de la synthèse = **48h ouvrées avant** (donc jeudi précédent si Comité lundi).

Si tu détectes que Julien est en retard (Comité dans <48h et synthèse pas envoyée) → flag urgent : *"⚠️ Synthèse à envoyer MAINTENANT, Comité dans <X> heures"*.

### Étape 2 — Récupère la matière chiffrée

1. **📊 KPI mensuels** (`fa0b21be8f6b4569aa4431e42320d7da`) — chiffres du mois écoulé + comparaison M-1 et M-2
2. **💰 Trésorerie** : solde fin de mois, burn rate moyen 3 derniers mois, runway en mois
3. **📈 Business Plan** : écart actuel vs ramp BP 6→40→80→130 deals
4. **🎯 OKR / KR** : progression du trimestre courant
5. **📝 Faits marquants** : depuis le Comité précédent (signatures, départs, levées, événements)

### Étape 3 — Identifie les 2-3 risques majeurs

Pour chaque risque :
- **Description** factuelle (pas alarmiste)
- **Impact si non traité** (sur runway, sur ramp, sur équipe)
- **Action en cours ou proposée**

### Étape 4 — Drafte les 2-3 questions précises à Philippe

(Coordonné avec `comite-mentor-prep` côté Paul — éviter les doublons, viser des questions complémentaires.)

Une bonne question pour Philippe BA :
- Spécifique (pas générique)
- Décisionnelle (appelle une réponse actionnable)
- Hors zone de confort Paul + Julien (utilise vraiment l'expérience Philippe)

### Étape 5 — Restitue la synthèse 1 page

Format strict (tient sur 1 page A4 ou écran scroll-free) :

```
📊 Synthèse Comité Mentor — <date Comité> · pour Philippe Salah
   Envoyée par Julien — <date envoi>

──────────────────────────────────────
📅 Lecture du mois <Mois Année>
──────────────────────────────────────

💰 Finance
• Trésorerie fin de mois : <X k€> (M-1 : <Y k€>)
• Burn rate moyen 3 mois : <X k€/mois>
• Runway : <X mois>

📈 Commercial
• CA confirmé mois : <X k€> (cible BP : <Y k€> — écart <%>)
• CA pipeline pondéré : <X k€>
• Conversion sponsor : <X%> (BP : <Y%>)
• Nouveaux deals signés : <X>

🎬 Production / Édito
• Captations réalisées : <X>
• Articles publiés : <X>
• Numéros bouclés : <X>

──────────────────────────────────────
📝 Faits marquants depuis le dernier Comité
──────────────────────────────────────
• <Fait 1 : ex signature SFODF 2027 18 k€>
• <Fait 2>
• <Fait 3>

──────────────────────────────────────
🚨 Risques identifiés
──────────────────────────────────────

Risque 1 : <Titre>
• Description : <factuel>
• Impact : <sur runway / ramp / équipe>
• Action en cours : <ce qui est fait>

Risque 2 : <…>

──────────────────────────────────────
🎯 Nos 2-3 questions pour toi, Philippe
──────────────────────────────────────

Q1 : <Question précise>
Q2 : <Question précise>
Q3 (si pertinent) : <Question précise>

──────────────────────────────────────
📋 Décisions en attente que nous souhaitons trancher avec toi
──────────────────────────────────────
• <Décision 1>
• <Décision 2>

──────────────────────────────────────
🧭 Sujet stratégique proposé pour le bloc Vision (7 min)
──────────────────────────────────────
<Titre du sujet — pourquoi ce mois>

──────────────────────────────────────
À mardi prochain.
— Julien & Paul
```

### Étape 6 — Pousse dans Drive + ping Philippe

Si Julien valide → uploader la synthèse dans le dossier Drive Comité Mentor (à confirmer URL — sinon dans le dossier Direction) et envoyer à Philippe par mail avec le lien.

Si Julien veut valider d'abord → restitue le draft et propose : *"Tu valides ? Je pousse sur Drive et drafte le mail à Philippe."*

---

## Anti-patterns

- ❌ **Ne dépasse pas 1 page** — c'est la règle. Si tu as 2 pages de matière, condense.
- ❌ **N'envoie pas en J-1 ou jour J** — 48h ouvrées avant minimum. Si pas le temps, dis-le franchement à Julien : *"Trop tard pour envoyer 48h avant. Tu envoies quand même ou on saute ce mois ?"* (mais sauter est mauvais).
- ❌ **Ne mets pas de chiffres faux ou inventés** — si une métrique manque dans Notion, marque `[À COMPLÉTER]` dans le draft.
- ❌ **N'oublie pas les 2-3 questions** — sans questions précises, Philippe vient pour rien.
- ❌ **Ne dérive pas vers un mémo de 5 pages** — Philippe a besoin de l'essentiel pour challenger, pas d'un livre.
- ❌ **Ne mélange pas avec `comite-mentor-prep`** (Pauline) — celui-ci produit la synthèse écrite envoyée 48h avant, l'autre prépare les questions Paul à poser en séance.

---

## Cas particuliers

### Mois où la trésorerie est tendue (runway <6 mois)
→ Risque 1 obligatoirement = trésorerie. Question 1 = "Comment tu cadres le timing levée ?". Sujet stratégique = financement.

### Mois où un sponsor majeur est signé ou perdu
→ Fait marquant en premier. Question dédiée sur l'interprétation Philippe.

### Sync Paul+Julien pas eu (la synthèse n'est pas alignée)
→ Avant de l'envoyer, force un mini sync : *"Cette synthèse engage Paul aussi. 15 min avec lui avant envoi ?"*

### Comité reporté
→ Recalcule la date envoi (toujours 48h avant). Reste rigoureux même si le slot bouge.

---

## Identifiants Notion utiles

- 🧠 Comité Mentor Philippe Salah : `35e6979fbcd181569dc6c3cc418d6774`
- 📊 KPI mensuels : `fa0b21be8f6b4569aa4431e42320d7da`
- 📈 Business Plan : `35e6979fbcd181f2b785dd872ba12722`
- 💡 BP Lab : `24dc5471875c4821acce30c9e193b7c7`
- 🎯 OKR : `88627a768f894c07a2a7ee5a7044c1cd`
- 🔑 Key Results : `4bbcafe6f62147d9a705b27f0ddcd130`
- 💰 Squad Finance : `3626979fbcd18164b631d9a3a5771a3f`
- 🐺 Cockpit Julien : `3616979fbcd181b8bb90f8ab0985ef39`
- 🦊 Cockpit Paul : `3616979fbcd18186bf48cb87faa13af3`
