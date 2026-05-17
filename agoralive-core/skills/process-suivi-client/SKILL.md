---
name: process-suivi-client
description: >
  Drafte ou met à jour le process de suivi client AgoraLive — mission 🔴 actuelle
  co-portée par Julien et Éloïse. Mutualisé Julie + Éloi. Décompose les 4 phases
  (entretien préparatoire, suivi pendant congrès, feedback client, next step) en
  étapes concrètes, identifie les informations à recueillir à chaque phase, et
  propose un template Notion exploitable par toute l'équipe terrain.
  À déclencher quand Julien, Éloïse, Julie ou Éloi demande : "process suivi
  client", "drafte le suivi client", "fais le process", "comment on suit nos
  clients", "kit accompagnement".
---

# process-suivi-client — Process de suivi client AgoraLive

## Mission

Mission 🔴 actuelle de Julien + Éloïse : définir le process complet de suivi d'un client AgoraLive (organisateur de congrès), de la signature à la post-livraison. Sans process clair, l'expérience client varie selon qui s'en occupe.

---

## Procédure

### Étape 1 — Cadre les 4 phases du suivi

Le suivi client AgoraLive se décompose en 4 phases temporelles :

```
[Signature] → Phase 1 : Entretien préparatoire
            → Phase 2 : Suivi pendant le congrès
            → Phase 3 : Feedback post-congrès
            → Phase 4 : Next step (renouvellement / extension)
```

### Étape 2 — Détaille chaque phase

#### Phase 1 — Entretien préparatoire (J-30 à J-7 avant congrès)

**Objectif** : connaître le congrès, ses spécificités, les attentes du client, valider les pré-requis techniques.

**Owner principal** : Julien (ou délégué)

**Informations à recueillir** :
- Date(s) + lieu(x) précis du congrès
- Programme détaillé (sessions, salles, intervenants confirmés)
- Liste des intervenants à capter (avec cessions de droits à faire signer)
- Pré-requis techniques (wifi salle, prises, taille salles, retour son scène)
- Personne de contact terrain pendant le congrès (numéro, dispo)
- Sponsors associés (validation pricing avec Éloïse, conformité avec Olivier)
- Attentes spécifiques (qualité audio, articles publiés sous délai X, etc.)

**Livrables** :
- Fiche Congrès dans Notion complétée
- Liste cessions à signer envoyée à Olivier (`triage-contrat-agoralive` ou `cessions-watch`)
- Brief équipe terrain (intérimaires ou salariés AgoraLive)

#### Phase 2 — Suivi pendant le congrès (J0 à J+durée)

**Objectif** : être présent, réactif, anticiper les pépins, capturer la valeur en direct.

**Owner principal** : équipe terrain + Julien (relai)

**Actions** :
- Vérification matériel J-1 (test enregistrement, batteries, cartes SD)
- Présence physique sur place (au moins jour 1)
- Point quotidien client en fin de journée (5 min)
- Note des moments forts (citations, ambiance, panels remarqués) — utile pour articles
- Gestion incidents (intervenant absent, salle changée, technique en panne)

**Livrables** :
- Photos pour reportage (style `retour-experience-sfodf`)
- Audio enregistré (à transférer vers `notion-document-router` pour archivage Drive)
- Note de fin de jour (3 lignes) dans le Journal de bord

#### Phase 3 — Feedback post-congrès (J+1 à J+15)

**Objectif** : valider la satisfaction client, capturer les enseignements, démarrer la production éditoriale.

**Owner principal** : Éloïse (côté client) + équipe édito (côté production)

**Actions** :
- Mail de remerciement à J+1 (`mail-rediger` voix eloise)
- Call de debrief à J+7 (30 min) — `prep-meeting` côté Julien ou Éloïse
- Questionnaire satisfaction (NPS, points forts, points faibles)
- Récupération matériel (intérimaires ou retour Paris)
- Démarrage chaîne éditoriale (transcription → article → numéro)

**Informations à recueillir** :
- NPS (note 0-10) + commentaire
- Ce qui a marché
- Ce qui n'a pas marché
- Sponsors satisfaits ? (à valider avec Éloïse)
- Volonté de renouveler ?

**Livrables** :
- Fiche feedback dans Notion (lien Congrès)
- Articles SFODF en production (`officiel-article-v3`)
- Numéro du journal en montage

#### Phase 4 — Next step (J+30 à J+90)

**Objectif** : convertir la satisfaction en renouvellement ou en extension (autres congrès du même client).

**Owner principal** : Éloïse (commercial) + Michel (pertinence métier)

**Actions** :
- Présentation du numéro fini au client (J+60 environ)
- Proposition renouvellement année suivante
- Proposition extension à d'autres congrès du même client/société savante
- Demande de mise en relation avec d'autres présidents de société savante (`nouveau-president-contact` via Michel)
- Témoignage client si NPS ≥ 9 (pour site web "ils nous font confiance")

**Livrables** :
- Proposition commerciale renouvellement (`agoralib-pricing`)
- Témoignage écrit (pour site web)
- Référence ajoutée au pitch deck

### Étape 3 — Templates Notion à créer

Pour chaque phase, proposer un **template Notion** réutilisable :

1. **Template Fiche Congrès** (Phase 1) — base Congrès `c7ffc0cf7a3b427dab83c02f4fa4a03f`
2. **Template Brief Équipe Terrain** (Phase 1) — sous-page de la fiche Congrès
3. **Template Journal de bord congrès** (Phase 2) — entrées datées
4. **Template Feedback client** (Phase 3) — base à créer ou champ étendu Congrès
5. **Template Proposition Renouvellement** (Phase 4) — sous-page Commercial

### Étape 4 — Restitue le process complet

```
📋 Process Suivi Client AgoraLive — v1
Owners : Julien (Phase 1+2) · Éloïse (Phase 3+4)

[Détail des 4 phases ci-dessus avec timeline, owners, informations à recueillir, livrables]

🎯 Templates Notion proposés : <liste>

📤 Diffusion :
• Hub Commercial (process officiel)
• Cockpit Julien + Éloïse (rituels)
• Base Congrès (template fiche)
• Équipe terrain (brief)

📅 Prochaine revue : <date> — ajustement après 3-5 congrès traités
```

---

## Anti-patterns

- ❌ **Ne fais pas un process de 50 pages** — vise 1 page A4 de process exploitable + des templates.
- ❌ **N'oublie pas la Phase 4** — c'est là où se gagne la LTV.
- ❌ **Ne sépare pas process commercial et process production** — c'est UN flux client unique.
- ❌ **Ne fais pas le process solo** — Julien + Éloïse co-portent.
- ❌ **Ne crée pas 10 templates** — 5 max, sinon ça devient ingérable.

---

## Identifiants Notion utiles

- 💼 Hub Commercial : `35e6979fbcd181c3b6bed19cc2fbb275`
- 🏛️ Base Congrès : `c7ffc0cf7a3b427dab83c02f4fa4a03f`
- 👤 Base Personnes : `9d8d3c6b370d4c808502c0d6cd4c1e36`
- 📅 Journal de bord : `39e76afc61e247ff8f5c320a14f4c74d`
- 🎬 Production : `35e6979fbcd1813990f6eec9e3d69723`
- 📰 Édito : `35e6979fbcd18154b707ce1c829317f0`
- 🗺️ Roadmap Organisation : `3606979fbcd181d38416c267df9943bf`
- 🐺 Cockpit Julien : `3616979fbcd181b8bb90f8ab0985ef39`
- 🦋 Cockpit Éloïse : `3616979fbcd181098eede7282c11e504`
