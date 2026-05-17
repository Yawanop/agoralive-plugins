---
name: compta-setup-phase2
description: >
  Aide Olivier à structurer la Phase 2 Compta — mission 🔴 critique avec
  deadline 30 juin 2026 (souscription cabinet compta + plateforme paie + mutuelle).
  Décompose le chantier en sous-tâches concrètes, propose un ordre d'attaque,
  identifie les prérequis, drafte les comparatifs cabinet/plateforme, et trace
  l'avancement dans la Roadmap Organisation. Pour Olivia. À déclencher quand
  Olivier (ou Olivia) demande : "Phase 2 Compta", "où on en est compta", "souscrire
  cabinet compta", "monter la paie", "Olivia compta", "deadline 30 juin compta".
---

# compta-setup-phase2 — Pilotage chantier compta + paie + mutuelle

## Mission

Mission 🔴 critique d'Olivier avec **deadline 30 juin 2026** : structurer la compta + paie + mutuelle AgoraLive. Décomposer le chantier, prioriser, dépanner les blocages.

Sans ce skill, Olivier risque de manquer la deadline ou de souscrire dans l'urgence à une mauvaise solution.

---

## Procédure

### Étape 1 — Évalue l'état actuel

Ouvre la mission dans la Roadmap Organisation (`3606979fbcd181d38416c267df9943bf` → section RH opérationnel) :
- Cabinet compta : sélectionné ? souscrit ? actif ?
- Plateforme paie : sélectionnée ? souscrite ? première paie générée ?
- Mutuelle : sélectionnée ? souscrite ? salariés affiliés ?

Calcule le temps restant : `30 juin 2026 - aujourd'hui = X jours`.

### Étape 2 — Décompose les 3 sous-chantiers

#### Sous-chantier 1 — Cabinet comptable (~3-6 semaines)

Étapes :
1. **Cahier des charges** : volumes (transactions/mois), spécificités (TVA intracom, sponsors étrangers, BP scaling), services attendus (compta complète vs assistance), budget cible
2. **Sourcing 3 cabinets** : Pennylane Comptable / Dougs / cabinet local Reims-Paris / cabinet expert tech (KPMG Avocats, EY etc.)
3. **Devis comparés** : 3 cabinets, grille d'évaluation (prix, réactivité, spécialité tech/SaaS, références clients similaires)
4. **Décision Paul + Olivier** (sync rapide ou async via `decision-doc-paul-julien`)
5. **Signature contrat** + envoi pièces (K-bis, statuts, RIB, bilan d'ouverture)
6. **Onboarding** : transfert factures Drive, plan comptable, déclarations en cours

#### Sous-chantier 2 — Plateforme paie (~2-3 semaines)

Étapes :
1. **Cahier des charges** : nb salariés prévus (3 fin 2026 ? 5 fin 2027 ?), BSPCE, télétravail, multi-pays éventuel
2. **Sourcing 3 plateformes** : PayFit / Lucca / Silae / Combo (selon profil tech-friendly)
3. **Devis comparés** : grille (prix/salarié, fonctionnalités BSPCE, intégration compta, UX)
4. **Décision Paul + Olivier**
5. **Souscription** + configuration paramètres (conventions collectives, brut/net standards)
6. **Test sur paie blanche** avant première vraie paie

#### Sous-chantier 3 — Mutuelle (~2 semaines)

Étapes :
1. **Cahier des charges** : niveau de garanties (hospi, dentaire ★, optique, médecines douces), pris en charge employeur (50% minimum, 100% souvent attractif), couverture famille
2. **Sourcing 3 mutuelles** : Alan / Henner / classique (AXA, Generali)
3. **Devis comparés** : grille (prix/salarié, niveau garanties dentaire — critique vu notre univers, UX, app mobile)
4. **Décision Paul + Olivier**
5. **Souscription** + collecte affiliations salariés
6. **Communication équipe** : présenter le contrat, comment ça marche

### Étape 3 — Identifie les blocages

Pour chaque sous-chantier, flag ce qui peut bloquer :
- Décision Paul + Julien en attente
- Pièces administratives manquantes (K-bis récent, RIB, statuts à jour)
- Validation budget BP (compta = ~250-500€/mois, paie = ~30-50€/salarié/mois, mutuelle = ~50-100€/salarié/mois)
- Coordination avec Julien (RH co-owner) sur le timing recrutements

### Étape 4 — Propose un ordre d'attaque

Ordre recommandé (parallélisable en partie) :

```
J → J+7  : Cahiers des charges des 3 sous-chantiers (Olivier solo)
J+7 → J+21 : Sourcing 3 prestataires de chaque (3 x 3 = 9 contacts)
J+21 → J+28 : Devis reçus + grilles comparées
J+28 → J+35 : Décisions Paul + Olivier
J+35 → J+50 : Souscriptions + onboardings
J+50 → J+60 : Tests (paie blanche, première transaction compta, première carte mutuelle)
```

Si la deadline est dans <60 jours → propose des raccourcis (skip étape sourcing complet, prendre recos confiance comme Alan + Pennylane).

### Étape 5 — Trace l'avancement

Met à jour la Roadmap Organisation à chaque étape franchie (via `roadmap-orga-update`). Si une étape est en retard → flag pour Paul (point hebdo via `point-paul-hebdo`).

### Étape 6 — Restitue le brief d'état

```
🦉 Phase 2 Compta — état au <date>
Deadline : 30 juin 2026 (J-<X>)

📊 Avancement par sous-chantier :
1. Cabinet compta : <étape actuelle> / 6
2. Plateforme paie : <étape actuelle> / 6
3. Mutuelle : <étape actuelle> / 6

🚧 Blocages actifs :
• <blocage 1>
• <blocage 2>

🎯 Prochaine action prioritaire :
<action concrète + qui fait + quand>

📅 Statut global : 🟢 dans les temps · 🟠 sous tension · 🔴 critique
```

---

## Anti-patterns

- ❌ **Ne souscris pas sans avoir comparé** — sauf si la deadline force vraiment.
- ❌ **Ne mélange pas les 3 sous-chantiers** — chacun a son propre cahier des charges, prestataires, timing.
- ❌ **Ne décide pas seule** — Paul + Olivier signent ensemble (engagement financier récurrent + RH).
- ❌ **N'oublie pas le BP** — chaque souscription engage budget récurrent à valider contre le BP.
- ❌ **Ne perds pas la traçabilité** — chaque devis, contrat, signature doit être dans Drive Légal & Finance + lié dans Notion.

---

## Identifiants Notion utiles

- 🗺️ Roadmap Organisation : `3606979fbcd181d38416c267df9943bf`
- 🦉 Cockpit Olivier : `3616979fbcd181c0b10ff2b25011ba1d`
- ⚖️ Légal & Finance : `35e6979fbcd18116a3e4e5638feaf5ec`
- 📜 Contrats : `91c740ca092746369f9f7dae92c58870`
- 💰 Squad Finance (validation BP) : `3626979fbcd18164b631d9a3a5771a3f`
- 🧭 Direction (escalation Paul) : `35e6979fbcd181cbbb32eec0b388dd15`
