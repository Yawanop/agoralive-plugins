---
name: escalation-paul-check
description: >
  Vérifie SYSTÉMATIQUEMENT si un contrat, une décision ou un message qu'Olivier
  s'apprête à valider/signer passe les critères d'escalation à Paul. Six critères
  durs : verdict 🔴 RED au triage, juridiction étrangère ou clause arbitrale,
  montant > 10 k€ HT ou récurrent > 2 k€/mois, cession PI au-delà du standard,
  demande CNIL/avocat externe/autorité (URSSAF, fisc, ARS), modification clause
  responsabilité non couverte par la RC pro. Si un critère est touché → ne pas
  agir sans Paul. Pour Olivia. À déclencher quand Olivier (ou Olivia) doit
  vérifier avant signature : "escalation-paul-check", "ce contrat doit-il aller
  à Paul", "Olivia check si je peux signer", "vérifie escalation".
---

# escalation-paul-check — Vérification critères escalation Paul (Olivier)

## Mission

Garantir qu'**Olivier ne signe jamais seul** un contrat ou une décision qui passe les critères d'escalation. Six critères durs, simples à vérifier — mais facilement oubliés sous pression.

Ce skill est le filet de sécurité d'Olivier. Il s'invoque automatiquement avant chaque signature ou décision juridique structurante.

---

## Les 6 critères d'escalation à Paul (à graver)

| # | Critère | Pourquoi |
|---|---|---|
| 1 | **Verdict 🔴 RED** dans un triage contrat | Risque grave identifié — décision conjointe Paul + Olivier obligatoire |
| 2 | **Juridiction étrangère** ou **clause arbitrale** | Litige potentiel sortant du droit français — Paul doit valider |
| 3 | **Montant > 10 k€ HT** one-shot OU **récurrent > 2 k€/mois** | Engagement financier matériel — Paul décide |
| 4 | **Cession de PI** au-delà du standard AgoraLive | Cession irrévocable de capital immatériel — Paul valide |
| 5 | Demande **CNIL**, **avocat externe**, ou **autorité** (URSSAF, fisc, ARS) | Sujet hors zone confort opé — Paul gère |
| 6 | Modification **clause de responsabilité** ou **garantie** non couverte par la RC pro | Exposition non assurée — Paul tranche |

---

## Procédure

### Étape 1 — Récupère l'objet à checker

Type d'objet :
- Contrat (sponsoring, cession, prestation, partenariat)
- Décision (réponse à un sponsor, validation d'un devis, signature d'un mail engageant)
- Message structurant (réponse à autorité, communication officielle)

### Étape 2 — Évalue chacun des 6 critères

Pour chaque critère, marque :
- ✅ **Pas touché** — passe au suivant
- ⚠️ **Touché — escalation nécessaire**
- ❓ **Ambigu — vérifier avec Olivier en lecture**

#### Détail des vérifications

**Critère 1 — Verdict RED**
- A-t-il été passé par `triage-contrat-agoralive` ?
- Quel est le verdict (GREEN / YELLOW / RED) ?
- Si RED → ⚠️ escalation

**Critère 2 — Juridiction / arbitrage**
- Cherche dans le contrat les mots : "tribunal", "compétence", "arbitrage", "droit applicable", "Cour", "London", "New York", "International Chamber"
- Si droit non français OU clause arbitrale → ⚠️

**Critère 3 — Montant**
- Total HT du contrat ou de la prestation
- Récurrence (mensuelle, annuelle)
- Si > 10 000 € HT one-shot OU récurrent > 2 000 €/mois (= 24 000 €/an) → ⚠️

**Critère 4 — Cession PI**
- Cherche : "cession", "transfert", "droit moral", "propriété intellectuelle", "œuvre", "marque", "brevet"
- Le contrat cède-t-il à un tiers de la PI AgoraLive (au-delà du standard captation/édition) ?
- Si oui → ⚠️

**Critère 5 — Autorité externe**
- Cherche : "CNIL", "avocat", "URSSAF", "fisc", "DGCCRF", "ARS", "ANSM", "mise en demeure", "saisine"
- Si l'objet implique une autorité ou un avocat externe → ⚠️

**Critère 6 — Clause responsabilité hors RC pro**
- Cherche : "responsabilité illimitée", "indemnisation", "préjudice", "perte de chiffre d'affaires", "frais juridiques", "garantie totale"
- Compare à la couverture RC pro AgoraLive (à vérifier dans `35e6979fbcd18116a3e4e5638feaf5ec`)
- Si clause au-delà de la couverture → ⚠️

### Étape 3 — Restitue le verdict

```
🦉 Vérification escalation Paul — <date>

Objet : <type + titre>

📋 Critères :
1. Verdict RED : ✅ / ⚠️ — <note>
2. Juridiction étrangère/arbitrage : ✅ / ⚠️ — <note>
3. Montant > 10k€ HT ou récurrent > 2k€/mois : ✅ / ⚠️ — <montant identifié>
4. Cession PI hors standard : ✅ / ⚠️ — <note>
5. Autorité / avocat externe : ✅ / ⚠️ — <note>
6. Clause responsabilité hors RC pro : ✅ / ⚠️ — <note>

🎯 Verdict :
```

Trois verdicts possibles :

**✅ Aucun critère touché — Olivier peut signer seul**
```
✅ Pas d'escalation nécessaire. Olivier peut acter.
```

**⚠️ Un ou plusieurs critères touchés — escalation Paul**
```
⚠️ ESCALATION PAUL REQUISE avant signature.

Critères touchés : <liste>

👉 Action recommandée :
1. Ne pas signer / valider / envoyer.
2. Drafter un mail à Paul via `mail-rediger` voix olivier expliquant :
   - L'objet
   - Le critère touché
   - La recommandation Olivier
   - La question précise à Paul
3. Attendre validation Paul avant action.

Optionnel : ouvrir une ligne dans Direction (`35e6979fbcd181cbbb32eec0b388dd15`) pour tracer.
```

**❓ Critère ambigu — Olivier doit confirmer en lecture**
```
❓ Vérification incomplète. À examiner par Olivier directement.

Points ambigus : <liste>
```

### Étape 4 — Trace l'escalation si nécessaire

Si escalation est lancée → ajoute une note dans la fiche Contrat / Décision Notion :
```
🚨 Escalation Paul — <date> — critères <X, Y> — en attente Paul
```

Une fois Paul a tranché → mettre à jour le statut Notion + clôturer l'escalation.

---

## Anti-patterns

- ❌ **Ne saute jamais un critère** — la liste est exhaustive, applique-la entière.
- ❌ **Ne minimise pas un critère touché** — même un seul critère = escalation, pas de "ça devrait passer".
- ❌ **Ne signe pas à la place d'Olivier ou de Paul** — tu vérifies, eux signent.
- ❌ **Ne fais pas semblant de "vérifier" sans lire** — si tu n'as pas accès au contenu, dis-le franchement : *"Je n'ai pas le détail du contrat, à examiner directement par Olivier."*
- ❌ **Ne lance pas une escalation sans drafter le mail à Paul** — Olivier n'aime pas faire l'intermédiaire à la main.
- ❌ **Ne dérive pas en analyse juridique de fond** — ce skill est un CHECK rapide (5 min), pas une review complète.

---

## Cas particuliers

### Contrat avec un sponsor connu (clauses standards déjà visées plusieurs fois)
→ Quand même appliquer les 6 critères, mais tu peux noter : *"Sponsor récurrent, clauses standards habituelles. Vérification rapide."*

### Décision urgente (deadline < 24h)
→ Si un critère est touché → l'urgence ne change rien. Escalation Paul immédiate via mail urgent ou appel direct.

### Olivier veut "passer outre" l'escalation pour gagner du temps
→ Rappelle fermement : *"Les critères sont des règles d'or. Paul + toi avez convenu de ne jamais signer sur ces critères sans son OK. Drafte le mail, ça prend 3 min."*

### Contrat juste sous le seuil (ex : 9 800 € HT)
→ Note explicite : *"Sous le seuil de 10k€, donc pas d'escalation obligatoire — mais à 200€ près, à toi de juger si tu veux un OK Paul informel."*

### Sujet qui touche plusieurs critères en cascade
→ Flag chaque critère séparément + escalation Paul groupée (un seul mail couvrant tous les points).

---

## Identifiants Notion utiles

- 🦉 Cockpit Olivier : `3616979fbcd181c0b10ff2b25011ba1d`
- ⚖️ Légal & Finance (RC pro à vérifier) : `35e6979fbcd18116a3e4e5638feaf5ec`
- 📜 Contrats : `91c740ca092746369f9f7dae92c58870`
- 📝 Cessions : `b43dc5cf20bb4c22a414d11afd6d1ce2`
- 🧭 Direction (tracer escalations) : `35e6979fbcd181cbbb32eec0b388dd15`
- 🦊 Cockpit Paul (destinataire escalation) : `3616979fbcd18186bf48cb87faa13af3`
