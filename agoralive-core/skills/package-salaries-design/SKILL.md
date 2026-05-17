---
name: package-salaries-design
description: >
  Aide à structurer le package salariés AgoraLive — mission 🔴 actuelle d'Éloïse
  (avec Olivier sur la dimension juridique/admin). Couvre : salaire, BSPCE,
  télétravail, mutuelle, tickets resto, téléphone pro, congés, conditions
  particulières (jeune startup). Mutualisé Éloi + Olivia. À déclencher quand :
  "package salariés", "définir conditions employés", "BSPCE", "Éloi package",
  "Olivia conditions salariés".
---

# package-salaries-design — Design package salariés AgoraLive

## Mission

Mission 🔴 actuelle d'Éloïse + Olivier : définir le package complet à proposer aux futurs salariés AgoraLive. Sans cadre clair, on improvise à chaque embauche et on crée des inégalités.

---

## Procédure

### Étape 1 — Liste les briques du package

| Brique | Owner | Détails à définir |
|---|---|---|
| 💰 Salaire | Éloïse + Paul | Grille par fonction + ancienneté |
| 📈 BSPCE | Olivier | % vesting, cliff, prix exercice |
| 🏠 Télétravail | Éloïse | Full / hybride / spécifications |
| 🏥 Mutuelle | Olivier | Niveau + prise en charge employeur (50-100%) |
| 🍱 Tickets resto | Olivier | Sodexo, Swile, Edenred — montant facial |
| 📱 Téléphone pro | Éloïse | Forfait + matériel ou compensation |
| 🏖️ Congés | Olivier | 25 jours légaux + RTT éventuels + jours flottants |
| 💻 Matériel | Éloïse | MacBook Pro / Air, écran 27", chaise |
| 📚 Formation | Éloïse | Budget annuel/salarié |
| 🚲 Mobilité | Olivier | Forfait mobilités durables (200-700€/an) |
| 🎉 Vie d'équipe | Éloïse | Séminaire annuel, événements |
| 👨‍👩‍👦 Famille | Olivier | Congé paternité étendu, jours enfants malades |
| 🌍 Sabbatique | Olivier | Conditions après X années |

### Étape 2 — Benchmark startup B2B 2-10 personnes

Pour calibrer, comparer à 3 références :
- Startup tech française early-stage (Pennylane, Spendesk early days)
- Édition / média spécialisé (Mediapart, Le Tigre)
- Agence éditoriale dentaire (s'il y en a)

### Étape 3 — Définit 2 niveaux de package

#### Package Standard (CDI fondateur des prochains)

```
Salaire : grille marché + 10-20% (startup early, on attire avec BSPCE)
BSPCE : 0.5-2% selon ancienneté et rôle
Télétravail : Hybride 2j/sem présentiel (Reims ou Paris)
Mutuelle : niveau Tier 2 (Alan ou Henner), 60% employeur
Tickets resto : Swile, 10€/jour facial, 50% employeur
Téléphone : MacBook fourni + iPhone d'occasion ou compensation 50€/mois
Congés : 25 jours + 1 jour anniv + 2 jours flottants
Matériel : MacBook Pro 14", écran 27", chaise ergo (à 1500€ max)
Formation : 1000€/an/personne
Mobilité : forfait 400€/an
Vie d'équipe : 2 séminaires/an + Noël
Famille : congé paternité 28j (légal+) + 3 jours enfant malade/an
Sabbatique : non au démarrage, à revoir à 5 ans
```

#### Package Senior / Stratégique (rôles clés type Head of Sales, Lead Dev)

Mêmes briques + :
- BSPCE plus généreux (1-3%)
- Mutuelle Tier 3
- Tickets resto à 12€
- Formation 2000€/an
- Sabbatique au bout de 3 ans

### Étape 4 — Identifie les points d'arbitrage Paul + Julien

Certaines décisions structurantes :
- Pourcentage BSPCE pool total (5-15% du capital)
- Quel % employeur sur mutuelle (50, 60 ou 100%)
- Politique télétravail (priorité résultat vs présentiel)
- Niveau séminaires (frugal ou ambitieux)

→ Déclencher `decision-doc-paul-julien` sur ces points.

### Étape 5 — Drafte un document "Package AgoraLive v1"

À pousser dans Notion :
- Page sous-section "RH & Équipe"
- Public au workspace mais avec note de confidentialité (négociations)
- Versionné (v1, v2, etc.)

### Étape 6 — Restitue le récap

```
📦 Package salariés AgoraLive — v1

Owners : Éloïse (vie quotidienne) + Olivier (juridique/admin)

✅ Briques définies : <N/13>
⏳ Briques à arbitrer Paul + Julien : <liste>
📅 Validation finale prévue : <date>

🎯 Coût estimé / salarié / an
• Salaire moyen : <X €>
• Cotisations sociales : <Y €>
• Avantages (mutuelle, tickets, formation, matériel) : <Z €>
• TOTAL : <T €>

📤 Diffusion :
• Hub Stratégie & équipe — pour visibilité Paul + Julien
• Cockpits Éloïse + Olivier — pour suivi
• BP — pour intégration coûts dans Squad Finance
```

---

## Anti-patterns

- ❌ **Ne sous-paye pas** par fausse économie — on perd le candidat ou il part dans 6 mois.
- ❌ **Ne sur-paye pas** non plus — on grille le runway et on crée des inéquités internes.
- ❌ **Ne décide pas seul du BSPCE pool** — c'est Paul + Julien (dilution).
- ❌ **N'oublie pas la dimension affichage** — un package attractif se présente bien, pas juste un PDF froid.
- ❌ **Ne fais pas un package figé** — review annuelle obligatoire (inflation, marché, situation entreprise).

## Identifiants Notion utiles

- 🗺️ Roadmap Organisation : `3606979fbcd181d38416c267df9943bf`
- 🦋 Cockpit Éloïse : `3616979fbcd181098eede7282c11e504`
- 🦉 Cockpit Olivier : `3616979fbcd181c0b10ff2b25011ba1d`
- 🧭 Stratégie & équipe (sous-section RH) : `35e6979fbcd181cbbb32eec0b388dd15`
- 💰 Squad Finance : `3626979fbcd18164b631d9a3a5771a3f`
- 📈 Business Plan : `35e6979fbcd181f2b785dd872ba12722`
