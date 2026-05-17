---
name: note-mensuelle-paul
description: >
  Drafte la note mensuelle d'Olivier à Paul (5 lignes en commentaire de la page
  Direction Notion), couvrant l'état conformité, les contrats du mois, les
  alertes et les demandes d'arbitrage. Plus complète que `point-paul-hebdo`
  (3 lignes hebdo). Pour Olivia. À déclencher quand Olivier (ou Olivia) demande :
  "drafte ma note mensuelle Paul", "note mensuelle juridique", "Olivia mon
  reporting mensuel", "fais la note du mois pour Paul".
---

# note-mensuelle-paul — Note mensuelle Olivier → Paul

## Mission

Le 1er de chaque mois (rituel 30 min), Olivier poste un résumé 5 lignes en commentaire de la page Direction Notion (`35e6979fbcd181cbbb32eec0b388dd15`) pour que Paul ait une vue agrégée de l'état juridique/admin du mois écoulé.

Plus dense que le point hebdo (3 lignes), moins dense qu'un Comité Mentor.

---

## Procédure

### Étape 1 — Agrège les sujets du mois écoulé

Récupère depuis Notion :

1. **📜 Contrats** : signés ce mois, en cours, en retard signature, en escalation
2. **📝 Cessions** : signées, en attente, en retard
3. **🚨 Escalations** : items envoyés à Paul ce mois (tranchés ou non)
4. **📅 Échéances** : ce qui a été traité ce mois (TVA, IS, etc.) + à venir 30 jours
5. **🔴 Chantier Phase 2 Compta** : progression du mois (deadline 30 juin 2026)
6. **🎯 Autres chantiers actifs** : compliance LinkedIn, RC pro renouvellement, fiches de paie, etc.
7. **🚧 Blocages identifiés** : ce qui attend une décision Paul ou un input externe

### Étape 2 — Synthétise en 5 lignes (max)

Format imposé :

```
🦉 Note mensuelle juridique — <Mois Année>
1. <Contrats/Cessions/Signatures du mois — 1 ligne>
2. <Phase 2 Compta — progression — 1 ligne>
3. <Échéances traitées + à venir — 1 ligne>
4. <Escalations en attente Paul — 1 ligne>
5. <Risque émergent ou recommandation — 1 ligne>
```

Chaque ligne doit être **actionnable ou informative** — pas de remplissage.

Exemples bien écrits :

```
🦉 Note mensuelle juridique — Mai 2026
1. Signé : SFODF 2027 (18 k€), AOFR Q4 (8 k€). En attente : 3 cessions Surlemont (>7j).
2. Phase 2 Compta : cabinet sélectionné (KPMG), souscription mardi prochain. Reste paie + mutuelle.
3. TVA T1 payée. À venir : URSSAF mensuelle 15 mai, RC pro renouvellement 1er juin.
4. 🚨 Escalation Henry Schein toujours ouverte depuis 3 sem — bloque la signature.
5. ⚠️ Recommandation : sync Paul + Olivier 30 min cette semaine pour trancher Henry Schein.
```

```
🦉 Note mensuelle juridique — Juin 2026
1. Aucune nouvelle signature ce mois, 2 contrats en négociation (SFCD, Adfecto).
2. Phase 2 Compta : ✅ DEADLINE TENUE. Compta + paie + mutuelle souscrites et actives.
3. CFE déclarée. Pas d'autre échéance imminente.
4. 0 escalation en attente — RAS.
5. Bilan : mois calme côté légal, juillet sera plus chargé (renouvellements été + recrutement).
```

### Étape 3 — Poste le commentaire

Si Olivier valide → utilise `notion-update-page` pour poster en commentaire de la page Direction.

Sinon → restitue pour qu'il copie-colle lui-même.

### Étape 4 — Trace l'envoi

Note dans le cockpit Olivier que la note du mois <X> a été envoyée à Paul. Permet d'avoir l'historique.

---

## Anti-patterns

- ❌ **Ne dépasse pas 5 lignes** — c'est la règle. Si trop de matière, c'est un sujet de Comité Mentor.
- ❌ **N'utilise pas de jargon juridique opaque** — Paul lit en 30 secondes, pas en 5 minutes.
- ❌ **Ne fais pas que de la statistique sèche** — chaque ligne doit dire quelque chose d'actionnable.
- ❌ **Ne réduis pas si plusieurs sujets brûlants** — propose à Olivier d'ajouter une 6e ligne ou de prévoir un sync, mais ne perds pas l'info.
- ❌ **Ne confonds pas avec `point-paul-hebdo`** — hebdo = 3 lignes courantes, mensuel = 5 lignes bilan.

---

## Cas particuliers

### Mois où la Phase 2 Compta dérape
→ Ligne 2 doit être explicite : *"⚠️ Phase 2 Compta en retard — cabinet pas encore décidé. À débloquer cette semaine."*

### Mois où une escalation a abouti (Paul a tranché)
→ Ligne 4 le note explicitement : *"Henry Schein tranché ✅ — clause arbitrage acceptée avec ajustement."*

### Mois après le 30 juin 2026 (deadline Phase 2 atteinte)
→ La ligne 2 bascule de chantier à exploitation : *"Compta + paie + mutuelle opérationnelles. Mois 1 de compta classique."*

---

## Identifiants Notion utiles

- 🧭 Direction (où poster) : `35e6979fbcd181cbbb32eec0b388dd15`
- 🦉 Cockpit Olivier : `3616979fbcd181c0b10ff2b25011ba1d`
- 📜 Contrats : `91c740ca092746369f9f7dae92c58870`
- 📝 Cessions : `b43dc5cf20bb4c22a414d11afd6d1ce2`
- ⚖️ Légal & Finance : `35e6979fbcd18116a3e4e5638feaf5ec`
- 🗺️ Roadmap Organisation (suivi Phase 2 Compta) : `3606979fbcd181d38416c267df9943bf`
