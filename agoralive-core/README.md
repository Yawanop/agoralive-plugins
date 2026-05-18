# agoralive-core

Skills universels AgoraLive — installés par tous les membres de l'équipe.

**Version actuelle : 0.3.0** · cf. [CHANGELOG](../CHANGELOG.md)

---

## Architecture

Le plugin regroupe **6 jumeaux personnels** (1 par membre de l'équipe) + **49 skills métier opérationnels** que les jumeaux invoquent ou que les humains appellent directement.

### Jumeaux personnels (6)

Chaque membre de l'équipe AgoraLive a un **jumeau du genre opposé** qui sert de concierge Notion + routeur vers les skills métier. Chaque jumeau ne se déclenche **que quand son humain l'interpelle par son nom**.

| Humain | Jumeau | Rôle | Voix | Skills opérationnels |
|---|---|---|---|---|
| 🦊 Paul (CEO & PO) | **Pauline** | Concierge CEO/PO | Vive, challenge direct | 17 |
| 🐺 Julien (DG/PM) | **Julie** | Concierge DG/PM | Méthodique, structurée | 16 |
| 🦁 Philippe (CTO + Mentor BA) | **Philippine** | Bascule CTO ↔ BA | Techy (CTO) / posée (BA) | 12 |
| 🦋 Éloïse (Dir Commercial) | **Éloi** | Coach commercial | Énergique, motivant | 15 |
| 🐘 Michel (Dir Sci & Commercial Dentaire) | **Michelle** | Gardienne pertinence métier | Scientifique, posée | 11 |
| 🦉 Olivier (Dir Juridique) | **Olivia** | Filet sécurité légal | Prudente, rigoureuse | 19 |

### Skills métier (49)

Organisés par finalité :

- **1 universel** : `notion-document-router` (upload Drive + Notion + propagation bases dérivées)
- **5 daily watch** : `cockpit-philippe-watch`, `cessions-watch`, `contrats-watch`, `pipeline-sponsors-watch`, `prospects-congres-watch`
- **2 paramétrés multi-voix** : `mail-rediger` (6 voix), `prep-reunion` (7 humains)
- **2 sync & arbitrage** : `sync-binome-prep`, `arbitrage-tri`
- **5 Kit Philippine** : `sprint-status-philippe`, `bug-triage-cto`, `commit-message-helper`, `prep-sprint-planning`, `prep-comite-mentor-ba`
- **3 communication coord & PRD** : `trinome-comm-coord`, `point-paul-hebdo`, `prd-pauline`
- **2 Comité Mentor** : `comite-mentor-prep`, `comite-mentor-synthese-1p`
- **2 gardiens validation** : `validation-message-sponsor`, `validation-legale-message`
- **1 escalation** : `escalation-paul-check`
- **3 mutualisés universels** : `recrutement-screener`, `roadmap-orga-update`, `decision-doc-paul-julien`
- **4 missions 🔴 actuelles** : `compta-setup-phase2`, `etude-4p`, `process-suivi-client`, `identite-agoralive`
- **3 cycle mensuel** : `echeances-legales-mensuel`, `note-mensuelle-paul`, `kpi-mensuel-update`
- **2 Philippine BA** : `bp-challenge-philippe`, `analyse-runway`
- **4 Julie complétion** : `bp-alignment-pipeline`, `pipeline-pilote`, `onboarding-client`, `mail-signature-design`
- **4 Éloi complétion** : `linkedin-pro-agoralive-setup`, `package-salaries-design`, `pitch-sponsor-iterator`, `analyse-conversion-sponsor`
- **2 Michelle complétion** : `approche-congres-strategie`, `nouveau-president-contact`
- **2 Olivia audits** : `audit-rgpd`, `audit-code-sante-publique`
- **2 Pauline complétion** : `pitch-deck-iterator`, `okr-trimestre-review`

---

## 🔗 Chaînes inter-jumeaux (v0.3.0 — spec phase)

À partir de v0.3.0, l'architecture documente **4 chaînes transverses** où plusieurs jumeaux se synchronisent automatiquement sur un workflow déterministe. Ces chaînes restent en **spec phase** dans cette version (PRDs rédigées, orchestrateur non implémenté). Elles seront activées une à une après décision Paul+Julien (cf. fiche décision Notion).

| Chaîne | Jumeaux | Trigger | Live cible |
|---|---|---|---|
| **A — PRD → Sprint** | Pauline → Philippine | PRD complétée dans Notion | 15 juin 2026 |
| **C — KPI → Comité Mentor** | Pauline → Julie → Philippine BA → Pauline | 1er du mois 7h + cron J-3/J-2/J-1 | 1er juin 2026 |
| **D — Onboarding cascade** | Julie → Olivia + Éloi + Michelle | Fiche Congrès statut 🟢 Signé | 30 juin 2026 |
| **E — Pipeline daily → BP** | Éloi → Julie (+ Paul si seuil) | Changement statut deal majeur | 30 juin 2026 |

> 💡 **Chaîne B (officiel-article-v3 → Trinôme Comm)** : hors périmètre par décision Paul du 18/05/2026.

### 🤖 Automatisations daily (live depuis v0.3.0)

5 scheduled tasks Cowork tournent automatiquement **lun-ven à 7h** sur la machine de chaque membre :

| Scheduled task | Jumeau | Source |
|---|---|---|
| `cockpit-philippe-watch-daily` | Pauline (Paul) | `cockpit-philippe-watch` |
| `cessions-watch-daily` | Olivia (Olivier) | `cessions-watch` |
| `contrats-watch-daily` | Olivia (Olivier) | `contrats-watch` |
| `pipeline-sponsors-watch-daily` | Éloi (Éloïse) | `pipeline-sponsors-watch` |
| `prospects-congres-watch-daily` | Michelle (Michel) | `prospects-congres-watch` |

Stockées dans `~/Documents/Claude/Scheduled/` côté machine de chaque membre. Le plugin contient les skills source ; les scheduled tasks sont créées séparément par chaque humain via Cowork (cf. tutoriel à venir).

> 🔗 **Hub initiative complet** : [🤖 Industrialisation Jumeaux v0.3 — Notion](https://www.notion.so/3646979fbcd1814281dce1d1d0178f67)

---

## Installation

Cf. le [README parent](../README.md). Une fois `agoralive-core` installé, chaque membre adresse son jumeau par son prénom dans Cowork ou Claude Code.

---

## Architecture des skills (conventions)

### Structure obligatoire de chaque SKILL.md

```yaml
---
name: skill-name-kebab-case
description: >
  Description en 500-700 caractères avec 8-12 phrases-trigger naturelles.
  Mention claire de "À déclencher quand <humain> demande : '...', '...'".
  Si risque de confusion avec un autre skill : "Différent de X parce que Y".
  Anti-trigger explicite si applicable.
---

# Nom du skill — Description courte

## Mission
<2-3 phrases sur le pourquoi et pour qui>

## Procédure systématique (ou Procédure)
<Étapes claires, numérotées>

### Étape 1 — <Verbe>
### Étape 2 — <Verbe>
...

## Anti-patterns
- ❌ Liste de comportements à éviter

## Cas particuliers
### <Cas 1>
→ <comportement attendu>

## Exemples typiques (recommandé)
**"<prompt utilisateur>"**
→ <comportement attendu>

## Identifiants Notion utiles
<Liste des IDs avec un emoji et description courte>
```

### Conventions de naming

- **Kebab-case** : `skill-name-with-hyphens`
- **Jumeaux** : prefix `agent-` (ex : `agent-pauline`)
- **Skills paramétrés** : suffix selon paramètre (ex : `mail-rediger` qui prend `voix=paul`)
- **Skills personnels** : suffix `-<prenom>` (ex : `point-paul-hebdo`)
- **Skills universels** : pas de prefix (ex : `notion-document-router`)

### Conventions de description

- **Triggers explicites** : lister 6-10 phrases-trigger naturelles dans la description
- **Mentionner les jumeaux** qui invoquent ce skill
- **Anti-trigger** : si nécessaire, clarifier ce qui NE doit PAS déclencher le skill
- **Différenciation** : si proche d'un autre skill, dire "Différent de X parce que Y"

### Conventions des identifiants Notion

Listés en bas de chaque SKILL.md sous "## Identifiants Notion utiles". Avec emoji + description + UUID.

---

## Comment contribuer

### Ajouter un nouveau skill

1. **Identifier le besoin** : un jumeau bricole un workflow récurrent → c'est un candidat skill.
2. **Cloner SKILL_TEMPLATE.md** (dans ce dossier) et adapter.
3. **Ajouter le skill au routing table** du ou des jumeaux concernés.
4. **Update le CHANGELOG.md** (bump version selon impact).
5. **Update le README.md** (ajouter à la liste par finalité).
6. **Push** via `./push-agoralive-plugins.sh "Add new skill: <nom>"`.
7. **Annoncer à l'équipe** via Slack ou commentaire Notion.

### Modifier un skill existant

1. **Ouvrir le SKILL.md concerné**, modifier.
2. **Update CHANGELOG.md** (`PATCH` si bugfix, `MINOR` si refacto important).
3. **Tester en local** (invoquer le skill, vérifier comportement).
4. **Push**.
5. **Notifier les humains concernés** (le ou les jumeaux qui invoquent ce skill).

### Versioning

Cf. [CHANGELOG.md](../CHANGELOG.md). Format MAJOR.MINOR.PATCH :
- **MAJOR (X.0.0)** — changement breaking (suppression, renommage)
- **MINOR (0.X.0)** — ajout de skills ou refactor majeur
- **PATCH (0.0.X)** — bugfix, ajustements descriptifs

---

## Maintenance

**Owner** : Paul Boury — paulboury1@gmail.com

**Repo** : https://github.com/Yawanop/agoralive-plugins

**Issues / suggestions** : Slack #plugins-agoralive ou commentaire sur la fiche Notion correspondante.

---

## Roadmap

Cf. section "À venir" dans le [CHANGELOG.md](../CHANGELOG.md).
