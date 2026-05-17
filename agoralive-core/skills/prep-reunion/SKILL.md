---
name: prep-reunion
description: >
  Prépare un brief 1 page pour une réunion à venir d'un membre de l'équipe
  AgoraLive (Paul, Julien, Éloïse, Michel, Olivier, Philippe). À partir d'un
  événement (nom de réunion, date, participants ou lien Google Calendar), agrège
  le contexte Notion (qui est chaque participant, historique avec eux, congrès
  ou sponsor lié, contrats en cours, derniers échanges Drive), produit un brief
  structuré (contexte, agenda proposé, talking points, risques/sensibilités,
  next step attendu). Skill paramétré — chaque jumeau l'invoque avec son humain.
  À déclencher quand un membre demande : "prépare ma réunion avec X", "j'ai un
  call avec Y", "brief-moi pour le rdv de demain", "prep-reunion", "Pauline j'ai
  un call avec Henry Schein", "Éloi prépare mon call de 14h".
---

# prep-reunion — Brief 1 page pré-réunion paramétré

## Mission

Donner à n'importe quel membre de l'équipe AgoraLive un **brief 1 page exploitable** avant une réunion, pour qu'il arrive avec le bon contexte, les bons talking points et la bonne intention.

---

## Paramètres d'invocation

Le skill prend trois informations (inférables du contexte ou explicites) :

1. **`humain`** : `paul` · `julien` · `philippe-cto` · `philippe-ba` · `eloise` · `michel` · `olivier`
2. **`evenement`** : nom de la réunion, date, ou lien Google Calendar
3. **`participants`** : si pas dans l'événement, demander explicitement

Si une info manque, demande-la sans inventer.

---

## Procédure

### Étape 1 — Identifie l'événement

Si lien Google Calendar fourni → fetch l'événement (titre, participants, description).
Si juste un nom + date → reconstruis ce que tu peux depuis le contexte chat.
Si rien → demande à l'humain de préciser.

### Étape 2 — Identifie chaque participant

Pour chacun (hors l'humain lui-même) :

1. **Fiche Personne** dans `9d8d3c6b370d4c808502c0d6cd4c1e36` — rôle, organisation, fonction
2. **Historique** : dernier échange avec cet humain (mails Drive, commentaires Notion, mention dans un compte-rendu)
3. **Lien fort** : congrès lié, sponsor lié, contrat ouvert, candidat en recrutement

Si un participant est inconnu → drafter avec mention `[À CLARIFIER]`.

### Étape 3 — Identifie le contexte business

Selon les participants et le titre de l'événement :

- 🏛️ **Congrès** si réunion liée à un événement → base `c7ffc0cf7a3b427dab83c02f4fa4a03f`
- 💼 **Sponsor** si discussion deal → hub `35e6979fbcd181c3b6bed19cc2fbb275`
- 📜 **Contrat** en cours → base `91c740ca092746369f9f7dae92c58870`
- 👔 **Recrutement** si entretien candidat → base `e2029ad3f7894828a174e34156e831bc`
- 🧠 **Comité Mentor** si réunion avec Philippe Salah → page `35e6979fbcd181569dc6c3cc418d6774`

### Étape 4 — Restitue le brief 1 page

Format imposé (pas de variation) :

```
📋 Brief : <titre événement> — <date + heure>

👥 Participants
• <Nom 1> — <rôle / organisation> — <dernier contact : date + sujet>
• <Nom 2> — <…>

🎯 Contexte
<2-3 phrases qui posent : pourquoi cette réunion, où on en est, ce qui est en jeu>

📌 Talking points (à TOI)
1. <point 1 — formulation suggérée>
2. <point 2>
3. <point 3>

⚠️ Sensibilités / risques
• <ex : Henry Schein attend une réponse depuis 12 jours, possible tension>
• <ex : contrat de cession pas encore signé côté X, ne pas l'évoquer publiquement>

🎯 Next step attendu en sortie de réunion
<ce qu'on veut concrètement obtenir>

🔗 Documents utiles
• <lien Notion> · <lien Drive> · <lien fiche personne>
```

### Étape 5 — Adapte le ton au profil de l'humain

Le **format** est identique pour tous. Mais les **talking points** sont rédigés dans le registre de l'humain :

- **Paul** : direct, visionnaire — talking points = ce qu'il va défendre
- **Julien** : structuré, opérationnel — talking points = check-list à dérouler
- **Philippe CTO** : technique — talking points = positions techniques à tenir
- **Philippe BA** : stratégique — talking points = challenges à poser
- **Éloïse** : chaleureux + commercial — talking points = arguments de valeur à passer
- **Michel** : académique — talking points = sujets de fond à amener avec déférence
- **Olivier** : juridique — talking points = clauses à clarifier, points à acter

---

## Anti-patterns

- ❌ **Ne fais pas un brief de 3 pages** — tu te limites à 1 page, condensée et exploitable.
- ❌ **N'invente pas le contexte historique** — si tu ne trouves pas, marque `[À CLARIFIER]`.
- ❌ **Ne mélange pas les rôles des participants** — si tu n'es pas sûr, dis "Possiblement X chez Y" plutôt que d'affirmer.
- ❌ **Ne propose pas un next step que l'humain n'a pas demandé** — tu déduis du contexte, mais sans dérive.
- ❌ **Ne fais pas du business-plan** — c'est un brief pré-réunion, pas une stratégie globale.
- ❌ **N'oublie pas le "next step attendu"** — c'est la section qui transforme un brief passif en outil actif.

---

## Cas particuliers

### Réunion interne entre cofondateurs (sync hebdo, Comité Mentor)
→ Section "Participants" simplifiée (tout le monde se connaît). Focus sur agenda + sujets sensibles + décisions attendues.

### Premier rendez-vous avec un nouveau contact
→ Section "Sensibilités" plus développée : risques de cold introduction, ce qu'il faut absolument **ne pas** dire au premier rdv.

### Réunion avec un sponsor en attente de signature
→ Lier explicitement le contrat (sa version actuelle, points bloquants). Si le contrat est en escalation Paul, **flag impérativement**.

### Réunion Comité Mentor Philippe Salah
→ Section "Contexte" doit lister : KPI du mois, hypothèses BP à challenger, décisions en attente. Le brief sert à arriver structuré.

### Réunion d'entretien (candidat recrutement)
→ Section "Talking points" = 5-7 questions structurées sur les compétences clés. Lier la fiche `👔 Recrutement` du candidat.

### Réunion ad hoc dont tu n'as aucun contexte
→ Demande l'humain de préciser au moins : objectif + participants. Sans ça, brief = vide.

---

## Identifiants Notion utiles

- 👤 Base Personnes : `9d8d3c6b370d4c808502c0d6cd4c1e36`
- 🏛️ Base Congrès : `c7ffc0cf7a3b427dab83c02f4fa4a03f`
- 💼 Hub Commercial : `35e6979fbcd181c3b6bed19cc2fbb275`
- 📜 Contrats : `91c740ca092746369f9f7dae92c58870`
- 📝 Cessions : `b43dc5cf20bb4c22a414d11afd6d1ce2`
- 👔 Recrutement : `e2029ad3f7894828a174e34156e831bc`
- 🧠 Comité Mentor Philippe Salah : `35e6979fbcd181569dc6c3cc418d6774`
- 💰 Squad Finance : `3626979fbcd18164b631d9a3a5771a3f`
