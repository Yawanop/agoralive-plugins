---
name: arbitrage-tri
description: >
  Trie les arbitrages reçus dans l'inbox d'un dirigeant AgoraLive (Paul, Julien),
  en hiérarchisant et en proposant pour chaque item une recommandation d'action :
  réponds toi-même / escalade au binôme / attends le prochain Comité / délègue.
  Skill paramétré et mutualisé entre Pauline et Julie. À déclencher quand le
  dirigeant (ou son jumeau) demande : "trie mon inbox d'arbitrages", "mes
  arbitrages en attente", "qu'est-ce qui attend ma décision", "Pauline mes
  arbitrages", "Julie tri mes arbitrages", "j'ai 5 arbitrages, aide-moi à
  prioriser".
---

# arbitrage-tri — Triage des arbitrages d'un dirigeant

## Mission

Quand Paul ou Julien reçoivent une série d'arbitrages (de l'équipe, de prestataires, de partenaires), les ranger, hiérarchiser, et **proposer une route claire** pour chacun — sans décider à leur place.

---

## Paramètres d'invocation

1. **`humain`** : `paul` · `julien` — le dirigeant qui demande le tri
2. **`portee`** : par défaut "tout ce qui est en attente". Peut être restreint ("seulement cette semaine", "seulement les sujets compliance").

Si manque → suppose le dirigeant qui invoque + portée par défaut "tout en attente".

---

## Procédure

### Étape 1 — Identifie les arbitrages en attente

Va chercher dans :

1. **📨 Pings & questions** (data source `03837509-4c7e-4a3a-a63c-fe8c7f6ad43e`) — filtre tag humain + type "arbitrage" ou "décision attendue"
2. **✅ Mes tâches** (data source `f4f01b9a-a57e-41f4-9947-9c2258080d20`) — filtre owner humain + statut "à arbitrer"
3. **Commentaires Notion** dans les hubs (Direction, Légal, Commercial, RH) qui mentionnent l'humain comme arbitre

Restitue la liste brute avant de trier — pour que l'humain valide le périmètre.

### Étape 2 — Classifie chaque arbitrage

Pour chaque item, identifie :

1. **Sujet** : RH, Commercial, Compliance/légal, Produit, Finance, Opé
2. **Demandeur** : qui demande (membre de l'équipe, prestataire, partenaire)
3. **Urgence** : a-t-il une deadline ? Bloque-t-il un autre workflow ?
4. **Complexité décisionnelle** :
   - 🟢 **Simple** : information suffisante, peut être tranché solo
   - 🟠 **Modéré** : mérite un input court du binôme ou d'un expert (Olivier sur compliance, Philippe sur tech)
   - 🔴 **Structurant** : doit attendre le binôme Paul+Julien ensemble, ou le Comité Mentor

### Étape 3 — Propose une route par item

Quatre routes possibles, à choisir :

- ✅ **Réponds toi-même** (sujet simple, info suffisante, deadline proche)
- 🤝 **Sync rapide avec binôme** (Paul ou Julien — selon qui invoque)
- 🧠 **Garde pour Comité Mentor** (sujet structurant, pas urgent, mérite un avis Philippe BA)
- 👉 **Délègue / repasse la main** (en vrai c'est pas ton scope — c'est Olivier sur compliance, Éloïse sur commercial, etc.)

### Étape 4 — Restitue le tri formaté

```
⚖️ Inbox arbitrages — <date> · <N items au total>

🔴 Structurants (Comité Mentor ou binôme)
• <Sujet 1> — <demandeur> — <pourquoi structurant> → route : 🧠 / 🤝
• <Sujet 2> — …

🟠 Modérés (sync avec X)
• <Sujet 3> — <demandeur> — <input nécessaire de X> → route : 🤝 ou 👉

🟢 Simples (réponds toi-même)
• <Sujet 4> — <demandeur> — <reco rapide> → route : ✅
• <Sujet 5> — …

⏰ Avec deadline
• <Sujet 6> — <échéance> — <route>

👉 Recommandation d'ordre :
1. Traite d'abord les ⏰ avec deadline
2. Puis les 🟢 simples (gain rapide, libère l'inbox)
3. Puis prends 30 min pour les 🟠 modérés
4. Les 🔴 structurants → liste pour le prochain sync binôme
```

### Étape 5 — Adapte le ton à l'humain

- **`humain: paul`** (invoqué par Pauline) : direct, légèrement challengeur ("Paul, t'as 8 arbitrages, on en clôture 5 aujourd'hui ?")
- **`humain: julien`** (invoqué par Julie) : méthodique, structurant ("Julien, voilà la pile rangée. On déroule dans l'ordre ?")

---

## Anti-patterns

- ❌ **Ne tranche pas à la place du dirigeant.** Tu proposes une route, lui décide.
- ❌ **N'invente pas d'urgence** — si rien n'indique une deadline, ne marque pas ⏰.
- ❌ **Ne sur-classe pas en 🔴 structurant** — réserve cette catégorie aux vrais sujets stratégiques (financement, recrutement clé, pivot pricing, scénarios BP). Sinon tout devient "structurant" et plus rien ne l'est.
- ❌ **Ne mélange pas les inboxes Paul et Julien** — chaque humain a la sienne, même si beaucoup d'items se recoupent.
- ❌ **Ne laisse pas un item "sans route"** — chaque item doit avoir une recommandation, même "à clarifier avec le demandeur".

---

## Cas particuliers

### Aucun arbitrage en attente
→ Dis-le franchement : *"Inbox arbitrages vide. Bon moment pour avancer sur autre chose."*

### Beaucoup d'arbitrages d'un seul demandeur
→ Signale-le : *"⚠️ 4 arbitrages d'Éloïse ce mois — possible signal d'un workflow à clarifier."*

### Arbitrage qui dépasse les critères d'escalation Paul
→ Si Julie traite et qu'un item passe les critères (montant >10k€, juridiction étrangère, etc.), route impérativement vers `escalation-paul-check` ou flag à Paul.

### Arbitrage déjà tranché mais oublié (statut pas mis à jour)
→ Signale et propose de mettre à jour le statut Notion pour fermer l'item.

### Sujet en boucle (arbitrage déjà tranché 2 fois, qui revient)
→ Flag explicitement : *"⚠️ Sujet revient — soit la décision n'a pas été diffusée, soit elle n'est pas tenue. À investiguer avant de re-trancher."*

---

## Identifiants Notion utiles

- 🦊 Cockpit Paul : `3616979fbcd18186bf48cb87faa13af3`
- 🐺 Cockpit Julien : `3616979fbcd181b8bb90f8ab0985ef39`
- 📨 Pings & questions : data source `03837509-4c7e-4a3a-a63c-fe8c7f6ad43e`
- ✅ Mes tâches : data source `f4f01b9a-a57e-41f4-9947-9c2258080d20`
- 🧠 Comité Mentor Philippe Salah : `35e6979fbcd181569dc6c3cc418d6774`
- ⚖️ Légal & Finance (escalations) : `35e6979fbcd18116a3e4e5638feaf5ec`
- 🧭 Direction : `35e6979fbcd181cbbb32eec0b388dd15`
