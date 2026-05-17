# agoralive-core

Skills universels AgoraLive — installés par tous les membres de l'équipe.

## Skills inclus

### Jumeaux personnels (6 — 1 par membre de l'équipe)

Chaque membre de l'équipe AgoraLive a un **jumeau du genre opposé** qui sert de concierge Notion + routeur vers les skills métier. Chaque jumeau ne se déclenche **que quand son humain l'interpelle par son nom**.

| Humain | Jumeau | Rôle | Voix |
|---|---|---|---|
| 🦊 Paul (CEO & PO) | **Pauline** | Concierge CEO/PO, route bugs/PRDs/Comité Mentor | Vive, challenge direct |
| 🐺 Julien (DG/PM) | **Julie** | Concierge DG/PM, structure, range, pilote | Méthodique, opérationnelle |
| 🦁 Philippe (CTO + Mentor BA) | **Philippine** | Bascule entre cockpit CTO et cockpit BA selon contexte | Techy précise (CTO) / posée stratégique (BA) |
| 🦋 Éloïse (Dir Commercial) | **Éloi** | Coach commercial, pousse à clôturer | Énergique, motivant, action |
| 🐘 Michel (Dir Sci & Commercial Dentaire) | **Michelle** | Connaisseuse du milieu dentaire, gardienne pertinence métier | Scientifique, posée, autorité tranquille |
| 🦉 Olivier (Dir Juridique) | **Olivia** | Filet sécurité légal du quotidien, vérifie escalations | Prudente, rigoureuse, lawyer-like |

### Skills universels (utilisables par tous)

- `notion-document-router` — un document déposé → upload Drive automatique + fiche maître Notion + propagation aux bases dérivées (Contrats, Cessions, Bugs, Articles, CV, Devis, Comptes-rendus…). Idempotent, anti-doublon Notion **et** Drive.

## Installation

Cf. le README du repo parent. Une fois `agoralive-core` installé, chacun adresse son jumeau par son prénom dans Cowork ou Claude Code.

## Skills métier à venir

Chaque jumeau a une **routing table** qui liste les skills à construire (Tier 1 daily/hebdo, Tier 2 mensuel, Tier 3 ad hoc). Plusieurs sont **mutualisés** entre jumeaux (decision-doc-paul-julien, recrutement-screener, roadmap-orga-update, etc.). Ces skills viendront enrichir le plugin au fil des sprints.
