# Changelog — agoralive-plugins

Format basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/).
Versioning sémantique : MAJOR.MINOR.PATCH.

---

## [0.6.0] — 2026-05-22

### Added

- **Nouveau skill `agoralive-article`** — moteur éditorial AgoraLive : transforme une transcription de conférence ou un brief de sujet en article scientifique fini, en HTML web interactif ET en PDF imprimable, et compile plusieurs articles en livret de congrès. Deux modes de création — article de conférence (depuis la transcription audio) et article sponsorisé (revue de la littérature avec vérification PubMed des PMID, zéro référence inventée). Charte graphique pilotée par profil de marque (congrès ou sponsor), architecture prête pour une récupération auto depuis agoralive.ai. Bibliothèque de gabarits PDF (mono-colonne classique, revue 2 colonnes). Système d'audit intégré : contrôles déterministes (intégrité citations/références, autonomie, PMID) via `audit_article.py` + audit guidé fond + forme. Scripts : `build_article.py`, `export_pdf.py`, `pubmed_verify.py`, `build_livret.py`, `audit_article.py`. Disponible sous `agoralive-core:agoralive-article` chez tous les jumeaux.

### Notes

- **Évolution AgoraLive de `scientific-writing`** — `agoralive-article` est orienté production éditoriale (web + PDF + livret) plutôt que manuscrit académique. `scientific-writing` est conservé en parallèle pour les rédactions académiques classiques (IMRAD, soumissions journal) — les deux skills coexistent.
- Issu d'un travail d'itération sur l'article de référence DentalMonitoring : design web validé, édition PDF, onde ambiante, audit qualité.

---

## [0.5.0] — 2026-05-21

### Added

- **Skill générique `scientific-writing`** ajouté au plugin — manuscrits scientifiques en IMRAD (Introduction, Methods, Results, Discussion), citations APA/AMA/Vancouver, intégration figures/tables, conformité aux reporting guidelines (CONSORT, STROBE, PRISMA). Processus en deux étapes : (1) outline par section avec key points via `research-lookup`, (2) conversion en prose. Pour articles de recherche, soumissions journal, rédaction académique. Disponible sous `agoralive-core:scientific-writing` chez tous les jumeaux.

### Notes

- **Pas un skill métier AgoraLive** — skill générique d'écriture scientifique, utile à Michel (Dir Scientifique) pour rédactions SFODF et publications, mais aussi mutualisable pour tout contenu académique de l'équipe.

---

## [0.4.2] — 2026-05-19

### Added

- **Routing `enrichir-contact` ajouté aux 6 jumeaux** (Pauline, Julie, Éloi, Michelle, Olivia, Philippine). Chaque agent voit désormais le skill dans sa description frontmatter, sa table de routing ("Si X dit / mentionne… | Tu invoques…"), et son tableau de présentation sur demande. Trigger phrase recommandée : *"Pauline enrichis [Nom]"* (substituer le jumeau approprié selon l'humain). Counts mis à jour : Pauline 17→18, Julie 16→17, Éloi 15→16, Michelle 11→12, Olivia 16→17, Philippine 12→13.

### Notes

- **Pas de modification du skill `enrichir-contact` lui-même** — uniquement l'ajout de routes côté jumeaux. Le pipeline était fonctionnel en 0.4.1, mais nécessitait de bypasser Pauline pour l'invoquer.
- **Catégorie d'affichage** : `👔 Transverse RH/ops` (cohérent avec `recrutement-screener` et `roadmap-orga-update`, autres skills mutualisés inter-jumeaux).

---

## [0.4.1] — 2026-05-19

### Added

- **Nouveau skill `enrichir-contact`** — pipeline d'enrichissement mail + téléphone + niveau de confiance pour les bases Personnes et Organisations Notion. Dispatcher 2-en-1 : pour une Personne → Clay `find-and-enrich-list-of-contacts` (Email natif) + fallback web pattern + RocketReach ; pour une Organisation → web scrape ciblé du site officiel (homepage + /contact + footer) + fallback Clay `find-and-enrich-company`. Écrit directement dans les champs canoniques `Email pro` / `Téléphone` (Personnes) et `Email générique` / `Téléphone standard` (Organisations) — pas de duplication. Quatre nouveaux champs de métadonnées par base : `Confiance mail`, `Confiance tel`, `Date enrichissement`, `Source enrichissement`. Anti-triggers : pas de re-enrichissement < 90 jours, pas de mass enrichment > 50 fiches sans validation Paul. Mutualisé tous jumeaux.
- **Option Sponsor** dans `enrichir-contact` — recherche d'un contact commercial nommé via Clay `find-and-enrich-contacts-at-company` avec filtre titre (Sales / Partnerships / Business Development), création de la Personne puis enrichissement récursif.
- **4 nouveaux champs Notion** poussés sur les bases Personnes (data source `3c8396be-e935-4d83-8baa-28b3b8d497d1`) et Organisations (`f829e976-27cc-4fb8-97a9-ecba4c8444a7`) : `Confiance mail` (select), `Confiance tel` (select), `Date enrichissement` (date), `Source enrichissement` (multi-select).

### Fixed

- **`agoralive-core/.claude-plugin/plugin.json`** était resté à `0.2.2` après la 0.4.0 (oubli au sprint 5). Aligné sur la version courante `0.4.1`.

### Notes

- **Pré-requis runtime** : connecteur Clay authentifié sur Cowork (`mcp__plugin_sales_clay__*`). Si non-authentifié, le skill flag et bascule sur fallback web uniquement.
- **Budget Clay à valider** par Paul si > 50 enrichissements/mois — alerte intégrée dans le skill.

---

## [0.4.0] — 2026-05-18

### Changed (Sprint 5 — Pivot canal unique de communication)

- **Inbox Vocal devient le canal unique de communication AgoraLive.** Les bases `📨 Pings & questions` et `✅ Mes tâches` ont été archivées sous `🗄️ Archive — bases obsolètes` côté Notion. Tous les pings, tâches, questions, décisions et infos transitent désormais par la base `🎙️ Inbox Vocal` (data source `5fcf5b4e-c35f-4da9-9290-68e17a0c63de`).
- **Propriété `Pour` (multi-select)** ajoutée à Inbox Vocal — pilote l'affichage par destinataire sur les cockpits. Options : Paul · Julien · Éloïse · Michel · Olivier · Philippe. Vide = broadcast à tout le monde.
- **Propriété `Statut` convertie de `status` à `select`** pour permettre le filtre DSL `!= "Traité"`. Les 3 options (À traiter / En cours / Traité) restent inchangées côté UX.
- **Refactor des 7 cockpits** (Paul, Julien, Éloïse, Michel, Olivier, Philippe CTO, Philippe BA) : remplacement des inline databases `Pings & questions` + `Mes tâches` par une vue gallery `🎙️ Mon inbox vocal` en tête, filtrée `(Pour CONTAINS owner OR Pour IS EMPTY) AND Statut != Traité`. Note marquée `Traité` disparaît automatiquement de tous les cockpits.
- **Auto-détection du destinataire** documentée dans `notion-document-router` — patterns `Pour <prénom>`, `Hey <prénom>`, `Demande à <prénom>`, etc. avec variations d'accent/casse et multi-destinataires.

### Patched (skills mis à jour)

- `notion-document-router` — nouvelle section "Routing addressé via la base Notion 🎙️ Inbox Vocal" + entrée v3 historique.
- `agent-pauline`, `agent-julie`, `agent-eloi`, `agent-michelle`, `agent-olivia`, `agent-philippine` — Étape 2 (récupération inbox cockpit) redirigée de Pings/Tâches vers Inbox Vocal.
- `arbitrage-tri` — Étape 1 réécrite pour lire depuis Inbox Vocal au lieu des deux bases archivées. Identifiants Notion mis à jour.
- `echeances-legales-mensuel` — création des tâches d'échéance dans Inbox Vocal (Type=Tâche, Pour=Olivier) au lieu de l'ancienne base Mes tâches.

### Notes

- **Aucune migration d'items en cours nécessaire** : audit du 18/05/2026 → 0 tâche ouverte, 1 ping résolu (à archiver tel quel).
- **Les bases archivées restent consultables en lecture** sous `🗄️ Archive — bases obsolètes` pour la traçabilité. Ne plus y créer de nouveaux items.
- **Skills opérationnels (`mail-rediger`, `prep-reunion`, watch quotidiens) non touchés** : ils ne créent pas de pings/tâches directement, donc pas de patch nécessaire dans ce sprint. À surveiller si un comportement émerge.
- **Bump version manifest** : `agoralive-core` passe de `0.2.2` à `0.4.0` (la 0.3.0 était une "spec phase" sans skill modifié).

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
