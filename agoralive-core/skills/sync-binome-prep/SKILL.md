---
name: sync-binome-prep
description: >
  Prépare le sync hebdo lundi 1h du binôme Direction Paul + Julien. Skill mutualisé,
  invoqué soit par Pauline (côté Paul) soit par Julie (côté Julien), avec une vue
  symétrique de la matière. Agrège depuis Notion : pipeline congrès + sponsors chauds,
  décisions à trancher cette semaine, alertes Cockpit Philippe, état Comité Mentor
  (s'il y en a un ce mois-ci), arbitrages en cours, blocages. Sort une slide de
  5 lignes prête à dérouler en 60 min. À déclencher quand Paul (ou Pauline) ou
  Julien (ou Julie) demande : "prépare mon lundi", "sync Paul-Julien", "prep
  binôme", "Pauline prépare mon lundi", "Julie prépare mon lundi avec Paul",
  "agenda binôme direction".
---

# sync-binome-prep — Prep sync hebdo Paul + Julien

## Mission

Donner aux deux co-fondateurs (Paul et Julien) une **matière commune** pour leur sync hebdo du lundi 1h, en pré-rangée et hiérarchisée. Le binôme arrive aligné, pas en mode "qu'est-ce qu'on disait déjà ?".

---

## Paramètres d'invocation

1. **`cote`** : `paul` · `julien` — côté du binôme depuis lequel le sync est préparé. La structure du brief est identique mais le **point de vue narratif** s'adapte (Pauline dira "tu as 3 décisions", Julie dira "Paul a 3 décisions à débloquer pour toi").
2. **`date_sync`** : par défaut le **prochain lundi**. Sinon date explicite.

Si manque → suppose paul + prochain lundi.

---

## Procédure

### Étape 1 — Identifie la date du sync et le périmètre temporel

- Date du sync = prochain lundi (ou date donnée)
- Période couverte = **depuis le dernier sync** (lundi précédent — ou semaine entière si pas de trace)

### Étape 2 — Agrège les 6 segments

Récupère, dans cet ordre exact :

1. **💼 Pipeline congrès + sponsors chauds** (hub Commercial `35e6979fbcd181c3b6bed19cc2fbb275`) — deals qui ont bougé cette semaine + relances en retard
2. **🎯 Décisions à trancher cette semaine** — items des cockpits Paul et Julien marqués "à décider" ou avec un statut "En arbitrage"
3. **🦁 Alertes Cockpit Philippe** (CTO `3606979fbcd1811c9609e3c85ed9fada`) — bugs P0, FRs bloqués, sprint à risque
4. **🧠 État Comité Mentor Philippe Salah** (`35e6979fbcd181569dc6c3cc418d6774`) — y a-t-il un Comité ce mois ? Quand ? Quelle synthèse 1 page à envoyer 48h avant ?
5. **⚖️ Arbitrages en attente** — items de l'inbox Paul et Julien marqués "à arbitrer"
6. **🚨 Blocages identifiés** — items signalés bloquants par l'équipe (RH, commercial, légal)

### Étape 3 — Restitue la slide de 5 lignes

Format imposé (pas de variation) :

```
📅 Sync binôme Paul + Julien — lundi <date> · 1h

1️⃣ Pipeline
<2 lignes max — deals chauds + relances en retard + alertes>

2️⃣ Décisions de la semaine
• <Décision 1 — contexte minimal>
• <Décision 2>
• <Décision 3>

3️⃣ Alertes & blocages
<2 lignes max — Cockpit Philippe + RH/commercial/légal>

4️⃣ Comité Mentor
<1 ligne — date prochain Comité + état de la prep synthèse 1 page>

5️⃣ Arbitrages en attente
• <Item — qui attend quoi>

⏱️ Suggestion de cadrage 60 min :
• 15 min pipeline & décisions
• 15 min alertes & blocages
• 20 min Comité Mentor (prep ou debrief selon timing)
• 10 min arbitrages & wrap
```

Si une section est vide → écrire *"Rien à signaler"* plutôt qu'inventer.

### Étape 4 — Adapte le point de vue narratif

Selon le paramètre `cote` :

- **`cote: paul`** (invoqué par Pauline) : ton direct, perspective Paul ("tu as à trancher", "Julien attend que…")
- **`cote: julien`** (invoqué par Julie) : ton méthodique, perspective Julien ("Paul attend ton input sur", "ce que tu dois préparer pour…")

Le **contenu** est identique. Seule la narration change.

---

## Anti-patterns

- ❌ **Ne fais pas une slide de 30 lignes** — l'idée c'est 5 sections, pas 30 items.
- ❌ **N'invente pas de décisions** qui ne sont pas dans Notion.
- ❌ **Ne fais pas de recommandation politique** type "tu devrais lâcher du lest sur X" — tu prépares la matière, le binôme décide.
- ❌ **Ne dupliques pas le cockpit perso** — c'est un brief **commun aux deux**, donc seules les choses qui méritent un sync à 2 voix.
- ❌ **N'oublie pas le Comité Mentor** — c'est leur rituel sacralisé. Si y a un Comité ce mois, c'est en section 4 obligatoire.

---

## Cas particuliers

### Le binôme a sauté le sync de la semaine précédente
→ Élargis la période à 2 semaines. Signale en ouverture : *"⚠️ 2 semaines de couverture vu le sync sauté"*.

### Comité Mentor cette semaine ou la suivante
→ Section 4 devient prioritaire. Liste explicitement : Hypothèses BP à challenger (depuis `24dc5471875c4821acce30c9e193b7c7`), questions stratégiques à poser, état de la synthèse 1 page.

### Pipeline complètement vide (cas anormal)
→ Pas de "rien à signaler" qui sonne faux. Écris : *"⚠️ Pipeline vide cette semaine — à investiguer avec Éloïse"*.

### Beaucoup d'arbitrages en attente (>5)
→ Tu peux suggérer de bouger le timing : "Vu 7 arbitrages en attente, le 60 min va être court. Proposer 90 min ?"

---

## Identifiants Notion utiles

- 🦊 Cockpit Paul : `3616979fbcd18186bf48cb87faa13af3`
- 🐺 Cockpit Julien : `3616979fbcd181b8bb90f8ab0985ef39`
- 🦁 Cockpit Philippe CTO : `3606979fbcd1811c9609e3c85ed9fada`
- 💼 Hub Commercial : `35e6979fbcd181c3b6bed19cc2fbb275`
- 🧠 Comité Mentor Philippe Salah : `35e6979fbcd181569dc6c3cc418d6774`
- 💡 BP Lab (hypothèses) : `24dc5471875c4821acce30c9e193b7c7`
- 💰 Squad Finance : `3626979fbcd18164b631d9a3a5771a3f`
- 🧭 Direction : `35e6979fbcd181cbbb32eec0b388dd15`
- 📅 Journal de bord : `39e76afc61e247ff8f5c320a14f4c74d`
