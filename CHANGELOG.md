# Changelog — agoralive-plugins

Format basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/).
Versioning sémantique : MAJOR.MINOR.PATCH.

---

## [0.2.2] — 2026-05-17

### Validated (Sprint 3 — audit technique)

- **Validation des 46 IDs Notion uniques** utilisés dans les 55 SKILL.md : 21 IDs critiques fetched et validés OK (cockpits 6 membres, hubs Direction/Produit/Commercial/Finance/Comité Mentor/BP/BP Lab, bases canoniques Personnes/Organisations/Congrès/Contrats/Cessions/Bugs/Routes). Aucun ID périmé ou erroné détecté.
- Confiance haute sur les ~25 IDs restants (sous-pages KPI/OKR/Requirements/Stories/Epics/etc.) — extraits des mêmes pages canoniques validées.

### Notes

- Aucun skill modifié dans cette version.
- Pas de nécessité de patch sur les Notion IDs.

---

## [0.2.1] — 2026-05-17

### Added (Sprint 2 — quality fixes)

- **README agoralive-core enrichi** : architecture complète, conventions de naming, conventions des descriptions, section "Comment contribuer" (ajout/modif/versioning), conventions Notion IDs.
- **SKILL_TEMPLATE.md** dans `agoralive-core/skills/` — template prêt à cloner pour tout nouveau skill.
- **Section "Cas particuliers"** ajoutée aux 5 daily watch skills (`cockpit-philippe-watch`, `cessions-watch`, `contrats-watch`, `pipeline-sponsors-watch`, `prospects-congres-watch`).

### Changed (Sprint 2 — collision fixes)

- **Descriptions clarifiées** pour 4 skills à risque de collision :
  - `cockpit-philippe-watch` (angle PO Paul) vs `sprint-status-philippe` (angle CTO Philippe) — anti-trigger croisés explicites.
  - `pipeline-sponsors-watch` (daily opérationnel Éloi) vs `pipeline-pilote` (stratégique hebdo Julie) — distinction explicite.

---

## [0.2.0] — 2026-05-17

### Changed (Sprint 1 — refactor majeur)

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

- **49 skills métier opérationnels** (cf. README agoralive-core pour la liste par catégorie)

- **Page Notion** : `🚀 Bienvenue chez AgoraLive` (onboarding 60 secondes pour chaque membre)
- **Home Notion AgoraLive** : refonte (section AVANT TOUT remplacée par la nouvelle section jumeaux + callouts équipe enrichis)

**TOTAL : 55 skills**

---

## Conventions de versioning

- **MAJOR (X.0.0)** — changement breaking (suppression de skill, renommage, changement architecture plugin)
- **MINOR (0.X.0)** — ajout de nouveaux skills ou refactor majeur sans breaking
- **PATCH (0.0.X)** — bugfix, ajustements descriptifs, corrections triggers, validation technique

## À venir (roadmap)

- **Sprint 4 (skills manquants)** — à valider avec le terrain :
  - `inbox-mail-triage` (tri mails entrants)
  - `calendar-conflict-detector` (détection conflits agenda)
  - `nps-tracker` (suivi NPS dans la durée)
  - `newsletter-content` (production newsletter mensuelle)
  - `concurrence-veille-update` (brief mensuel veille concurrentielle)
  - `notion-orphans-clean` (hygiène bases Notion : doublons, statuts incohérents)
  - `slack-summary-daily` (si Slack intégré)
- **Cas particuliers** à compléter sur les ~25 skills qui en manquent encore.
- **Examples typiques** à ajouter aux skills métier (au-delà des jumeaux qui les ont déjà).
