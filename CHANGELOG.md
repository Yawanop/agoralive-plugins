# Changelog — agoralive-plugins

Format basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/).
Versioning sémantique : MAJOR.MINOR.PATCH.

---

## [0.2.0] — 2026-05-17

### Changed (refactor majeur)

- **6 jumeaux refondus** : les routing tables sont désormais consolidées (un seul tableau "skills opérationnels" au lieu des sections A/B/C/D séparant existants et "à construire"). Chaque jumeau invoque directement les vrais skills au lieu de bricoler à la main.
- **Exemples typiques ajoutés** à chaque jumeau (Pauline, Julie, Philippine, Éloi, Michelle, Olivia) — facilite le déclenchement par le modèle.
- **Anti-patterns nettoyés** : suppression de la consigne "pour les skills à construire, fais à la main" qui n'a plus de sens.

### Notes

- Aucun skill métier modifié dans cette version. Pas de changement de comportement pour les usages métier — seul le routage par les jumeaux est nettoyé.
- Si tu as ouvert une session avant cette version, fais `/reload-plugins` pour bénéficier des nouvelles routing tables.

---

## [0.1.0] — 2026-05-17

### Added (release initiale)

- **6 jumeaux personnels** (1 par membre de l'équipe, déclenchement par prénom) :
  - `agent-pauline` (Paul, CEO & PO) 🦊
  - `agent-julie` (Julien, DG & PM) 🐺
  - `agent-philippine` (Philippe, CTO + Mentor BA) 🦁
  - `agent-eloi` (Éloïse, Directrice Commerciale) 🦋
  - `agent-michelle` (Michel, Dir Scientifique & Commercial Dentaire) 🐘
  - `agent-olivia` (Olivier, Directeur Juridique & Compliance) 🦉

- **1 skill universel** :
  - `notion-document-router` — upload Drive automatique + fiche maître Notion + propagation aux bases dérivées

- **5 skills daily watch** :
  - `cockpit-philippe-watch` (Pauline → état sprint angle PO)
  - `cessions-watch` (Olivia → cessions en attente signature)
  - `contrats-watch` (Olivia → contrats à triager)
  - `pipeline-sponsors-watch` (Éloi → deals chauds, relances en retard)
  - `prospects-congres-watch` (Michelle → congrès dentaires à relancer)

- **2 skills paramétrés multi-voix** :
  - `mail-rediger` — drafte mail dans la voix de l'humain (6 voix)
  - `prep-reunion` — brief 1 page pré-réunion (7 humains)

- **2 skills sync & arbitrage** :
  - `sync-binome-prep` — prep sync hebdo Paul + Julien
  - `arbitrage-tri` — triage inbox arbitrages

- **5 skills Kit Philippine (CTO + BA)** :
  - `sprint-status-philippe`, `bug-triage-cto`, `commit-message-helper`, `prep-sprint-planning`, `prep-comite-mentor-ba`

- **3 skills communication coord & PRD** :
  - `trinome-comm-coord`, `point-paul-hebdo`, `prd-pauline`

- **2 skills Comité Mentor** :
  - `comite-mentor-prep` (Pauline → questions stratégiques Paul)
  - `comite-mentor-synthese-1p` (Julie → synthèse 1 page envoyée à Philippe 48h avant)

- **2 skills gardiens validation** :
  - `validation-message-sponsor` (Michelle → pertinence métier dentaire)
  - `validation-legale-message` (Olivia → RGPD + santé publique + droits + RC pro)

- **1 skill escalation** :
  - `escalation-paul-check` (Olivia → vérification critères avant signature)

- **3 skills mutualisés universels** :
  - `recrutement-screener`, `roadmap-orga-update`, `decision-doc-paul-julien`

- **4 skills missions 🔴 actuelles** :
  - `compta-setup-phase2`, `etude-4p`, `process-suivi-client`, `identite-agoralive`

- **3 skills cycle mensuel** :
  - `echeances-legales-mensuel`, `note-mensuelle-paul`, `kpi-mensuel-update`

- **2 skills Philippine BA finale** :
  - `bp-challenge-philippe`, `analyse-runway`

- **4 skills Julie complétion** :
  - `bp-alignment-pipeline`, `pipeline-pilote`, `onboarding-client`, `mail-signature-design`

- **4 skills Éloi complétion** :
  - `linkedin-pro-agoralive-setup`, `package-salaries-design`, `pitch-sponsor-iterator`, `analyse-conversion-sponsor`

- **2 skills Michelle complétion** :
  - `approche-congres-strategie`, `nouveau-president-contact`

- **2 skills Olivia audits** :
  - `audit-rgpd`, `audit-code-sante-publique`

- **2 skills Pauline complétion** :
  - `pitch-deck-iterator`, `okr-trimestre-review`

- **Page Notion** : `🚀 Bienvenue chez AgoraLive` (onboarding 60 secondes pour chaque membre)
- **Home Notion AgoraLive** : refonte (section AVANT TOUT remplacée par la nouvelle section jumeaux + callouts équipe enrichis)

**TOTAL : 55 skills**

---

## Conventions de versioning

- **MAJOR (X.0.0)** — changement breaking (suppression de skill, renommage, changement architecture plugin)
- **MINOR (0.X.0)** — ajout de nouveaux skills ou refactor majeur sans breaking
- **PATCH (0.0.X)** — bugfix, ajustements descriptifs, corrections triggers

## À venir (roadmap)

- Skills additionnels identifiés (à valider) :
  - `inbox-mail-triage` (tri mails entrants)
  - `calendar-conflict-detector` (détection conflits agenda)
  - `nps-tracker` (suivi NPS dans la durée)
  - `newsletter-content` (production newsletter mensuelle)
  - `concurrence-veille-update` (brief mensuel veille)
  - `notion-orphans-clean` (hygiène bases Notion)
- Améliorations qualité :
  - Validation Notion IDs (script automatique)
  - Documentation `Comment contribuer` dans le plugin
  - Tests / exemples de cas-types par skill
