---
name: roadmap-orga-update
description: >
  Met à jour la Roadmap Organisation Notion (`3606979fbcd181d38416c267df9943bf`)
  qui pilote les missions opérationnelles (Organisation, RH, Marketing,
  Communication, Commercial, IT). Trois opérations : (1) marquer une mission
  comme terminée, (2) ajouter une nouvelle mission avec owner + priorité, (3)
  re-prioriser une mission existante. Skill mutualisé tous jumeaux. À déclencher
  quand un membre dit : "j'ai fini la mission X", "ajoute une mission de
  Roadmap orga", "Pauline marque comme fait", "re-prioriser X en 🔴",
  "update roadmap orga".
---

# roadmap-orga-update — Mise à jour Roadmap Organisation

## Mission

Donner à n'importe quel jumeau le réflexe de **maintenir la Roadmap Organisation à jour** — pour qu'elle reflète l'état réel des chantiers et serve vraiment de pilotage mensuel pour Paul + Julien.

---

## Paramètres d'invocation

1. **`operation`** : `marquer_fait` · `ajouter_mission` · `reprioriser` · `mettre_a_jour_owner`
2. **`mission`** : identifier la mission (texte exact ou description partielle)
3. **`section`** : 🏢 Organisation générale · 👥 RH · 📣 Marketing · 📢 Communication · 💼 Commercial · 💻 IT

Si manque → demande clarification (pas d'invention).

---

## Procédure

### Étape 1 — Ouvre la Roadmap Organisation

```
notion-fetch sur https://www.notion.so/3606979fbcd181d38416c267df9943bf
```

Identifie le tableau de la section concernée.

### Étape 2 — Effectue l'opération

#### Cas A — `marquer_fait`

1. Localise la mission par titre (fuzzy match si nécessaire)
2. Si trouvée → met à jour la colonne Statut : ajouter `✅ Fait`
3. Si plusieurs matches → demande à l'humain laquelle

#### Cas B — `ajouter_mission`

1. Demande à l'humain (si pas déjà fourni) :
   - Titre actionnable
   - Priorité : 🔴 1 (urgent/structurant) · 🟠 2 (important) · 🟢 3 (nice-to-have)
   - Owner (un nom ou "Tout le monde")
   - Section concernée
2. Crée la ligne dans le tableau Notion

#### Cas C — `reprioriser`

1. Localise la mission
2. Demande la nouvelle priorité
3. Update

#### Cas D — `mettre_a_jour_owner`

1. Localise la mission
2. Demande le nouvel owner
3. Update

### Étape 3 — Confirme + propose suite

```
✅ Roadmap orga mise à jour :
• <Action effectuée>
• Section : <section>
• Mission : <titre>
• Owner : <nom>
• Priorité : <🔴/🟠/🟢>

👉 Note : la prochaine revue mensuelle est avec Paul + Julien (review owner page).
```

Si l'opération concerne plusieurs missions liées → suggère de toutes les traiter ensemble.

---

## Synthèse rapide (rappel utile)

À jour au 15 mai 2026 :

| Section | P1 🔴 | P2 🟠 | P3 🟢 | Total |
|---|---|---|---|---|
| Organisation générale | 3 (dont 1 fait) | 5 | 0 | 8 |
| RH (incl. réunions & juridique) | 8 | 1 | 4 | 13 |
| Marketing (incl. réunion) | 2 | 1 | 1 | 4 |
| Communication | 0 | 6 | 5 | 11 |
| Commercial | 1 | 1 | 3 | 5 |
| IT | 1 | 3 | 0 | 4 |

---

## Anti-patterns

- ❌ **Ne supprime jamais une mission** — utilise `✅ Fait`. La trace reste utile pour la revue mensuelle.
- ❌ **N'ajoute pas une mission sans priorité** — le pilotage repose sur la priorisation.
- ❌ **N'ajoute pas une mission sans owner** — "Personne" ou "À définir" est mieux que rien, mais pousse à attribuer.
- ❌ **Ne re-priorise pas sans justification** — note brève en commentaire de la ligne.
- ❌ **Ne crée pas de section nouvelle** — utilise une des 6 existantes.

---

## Identifiants Notion utiles

- 🗺️ Roadmap Organisation : `3606979fbcd181d38416c267df9943bf`
- 🧭 Stratégie & équipe (parent) : `35e6979fbcd181cbbb32eec0b388dd15`
