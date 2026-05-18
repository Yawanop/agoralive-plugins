# Changelog — agoralive-plugins

Format basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/).
Versioning sémantique : MAJOR.MINOR.PATCH.

---

## [0.3.0] — 2026-05-18

### Added (Sprint 4 — Industrialisation Jumeaux — spec phase)

- **5 scheduled tasks daily** (lun-ven 7h) déclarées côté Cowork pour les 5 watch quotidiens : `cockpit-philippe-watch` (Paul/Pauline), `cessions-watch` et `contrats-watch` (Olivier/Olivia), `pipeline-sponsors-watch` (Éloïse/Éloi), `prospects-congres-watch` (Michel/Michelle). Premier passage automatique le 19/05/2026. Stockées dans `~/Documents/Claude/Scheduled/` côté machine de chaque membre — pas embarquées dans le plugin (chaque jumeau cible son cockpit Notion).
- **4 PRDs Chaînes inter-jumeaux** rédigées dans Notion (hub : [🤖 Industrialisation Jumeaux v0.3](https://www.notion.so/3646979fbcd1814281dce1d1d0178f67)) :
  - **Chaîne A — PRD → Sprint** (Pauline → Philippine) : `prd-pauline` complétée trigger `bug-triage-cto` automatique côté CTO.
  - **Chaîne C — KPI → Comité Mentor** (Pauline → Julie → Philippine BA) : `kpi-mensuel-update` → `comite-mentor-synthese-1p` → `prep-comite-mentor-ba` + `analyse-runway` → `comite-mentor-prep`, séquence J-3/J-2/J-1 automatique. **Priorité #1 — live cible Comité Mentor de juin 2026**.
  - **Chaîne D — Onboarding cascade** (Julie → Olivia + Éloi + Michelle) : `onboarding-client` propage automatiquement vers cessions (Olivia), brief commercial (Éloi), prospects société savante (Michelle si dentaire).
  - **Chaîne E — Pipeline daily → hebdo → BP** (Éloi → Julie) : changements statut majeur dans base Sponsors → ping cockpit Julien + suggestion `bp-alignment-pipeline` si écart > 10%.
- **Fiche décision Paul+Julien** ([📝 Inter-jumeaux : auto-ping vs humain pivot](https://www.notion.so/3646979fbcd18139a4b9d45c113f60f7)) — arbitrage Option A (statu quo strict) vs Option B (auto-ping autorisé sur chaînes nommées uniquement) vs Option C (auto-ping généralisé). **Reco Pauline : Option B**. À trancher au sync binôme du 25/05/2026.

### Notes

- **Aucun skill métier modifié dans cette version**. v0.3.0 = release "spec phase" — les PRDs sont rédigées, l'orchestrateur (webhooks Notion + polling jumeaux) reste à implémenter par Philippe post-décision Paul+Julien.
- **Hors périmètre par décision Paul du 18/05/2026** : Chaîne B (auto-trigger `officiel-article-v3` → Trinôme Comm) — le skill `officiel-article-v3` reste tel quel. Pas de modif prévue.
- **Audit complet de l'architecture v0.2.x** réalisé le 18/05/2026 par Pauline (jumelle de Paul) : 6 jumeaux passés en revue (forces, manques, ponts inter-jumeaux), 5 chaînes transverses identifiées dont 4 retenues, 5 automatisations daily mises en place.
- **Roadmap impl. (si Option B retenue)** : Chaîne C → 1er juin 2026 · Chaîne A → 15 juin 2026 · Chaînes D + E → 30 juin 2026.

### Documented

- Hub initiative Notion : [🤖 Industrialisation Jumeaux v0.3](https://www.notion.so/3646979fbcd1814281dce1d1d0178f67) (parent des 5 documents v0.3.0).
- Section dédiée ajoutée à la [🗺️ Roadmap Organisation AgoraLive](https://www.notion.so/3606979fbcd181d38416c267df9943bf) — "🤖 Industrialisation Jumeaux & Automatisations" avec 7 missions trackées.

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
