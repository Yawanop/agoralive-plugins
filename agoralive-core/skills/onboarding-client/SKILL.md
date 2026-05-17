---
name: onboarding-client
description: >
  Lance l'onboarding d'un nouveau client AgoraLive (organisateur de congrès)
  après signature. Crée la fiche Congrès dans Notion avec tous les champs initiaux,
  lance le process suivi client (Phase 1 entretien préparatoire), briefe l'équipe
  terrain, identifie les cessions à faire signer aux intervenants, planifie le
  kickoff. Pour Julie (Julien, owner onboarding clients). À déclencher quand :
  "nouveau client signé", "lance l'onboarding de X", "Julie onboarding",
  "kit démarrage client".
---

# onboarding-client — Lance l'onboarding d'un nouveau client

## Mission

Quand un client signe, lancer un onboarding propre, structuré, qui pose les bases du suivi client (cf. `process-suivi-client` Phase 1).

---

## Procédure

### Étape 1 — Récupère les infos initiales

Demande à Julien (ou déduis du contexte) :
- Nom du congrès / organisateur
- Date(s) + lieu du congrès
- Personne de contact principale (nom + email + téléphone)
- Montant signé
- Lien contrat signé (Drive ou Notion)

### Étape 2 — Crée la fiche Congrès dans Notion

```
notion-create-pages dans la base Congrès (c7ffc0cf7a3b427dab83c02f4fa4a03f)
```

Champs à remplir initialement :
- Titre : <Nom congrès — Année>
- Date(s)
- Lieu
- Personne de contact (relation → Personnes)
- Organisation (relation → Organisations)
- Statut : 🟢 Signé / Onboarding
- Spécialité (ODF, dentaire, chirurgie, etc.)
- Montant
- Owner interne (Julien par défaut, ou délégué)

### Étape 3 — Crée la sous-page Brief Équipe Terrain

Sous la fiche Congrès, crée une sous-page "Brief équipe terrain — <Nom congrès>" avec template :

```
# Brief équipe terrain — <Congrès>

📅 Quand : <dates>
📍 Où : <lieu + salles>

🎯 Mission
<rappel mission AgoraLive pour ce congrès>

👥 Équipe affectée
• <Nom + rôle>

📋 Checklist J-7
- [ ] Matériel testé
- [ ] Cessions intervenants signées (cf. liste ci-dessous)
- [ ] Accès salles confirmé
- [ ] Wifi/électricité vérifiés

📋 Pendant le congrès
- [ ] Point quotidien client (5 min fin de journée)
- [ ] Note des moments forts (citations, ambiance)
- [ ] Photos pour reportage
- [ ] Audio enregistré dans qualité requise

📋 J+1
- [ ] Transfert audio Drive
- [ ] Mail remerciement client (mail-rediger voix julien ou eloise)
- [ ] Note debrief dans Journal de bord
```

### Étape 4 — Identifie les cessions à faire signer

Pour chaque intervenant prévu (selon programme) :
- Vérifier dans base Personnes s'il a déjà signé une cession dans le passé
- Si non → créer une cession dans `b43dc5cf20bb4c22a414d11afd6d1ce2` avec statut `📝 À demander`
- Déléguer à Olivier (Olivia) pour le triage et envoi via `cessions-watch` + `mail-rediger` voix olivier

### Étape 5 — Planifie le kickoff (J-30)

Propose à Julien :
- Date kickoff (30 min avec client) — bloquer dans l'agenda
- Préparation via `prep-reunion` côté julien
- Agenda type :
  1. Tour de table
  2. Récap mission AgoraLive
  3. Programme du congrès (intervenants, salles, sessions)
  4. Pré-requis techniques
  5. Personne contact terrain
  6. Cessions à signer
  7. Calendrier production (article → numéro)

### Étape 6 — Restitue le récap onboarding

```
🐺 Onboarding lancé : <Nom congrès>

✅ Fiche Congrès créée : <URL Notion>
✅ Brief équipe terrain : <URL sous-page>
✅ Cessions identifiées : <N> à demander (relayé à Olivier)
📅 Kickoff client à planifier : <date suggérée>

👉 Prochaines actions :
1. Bloquer kickoff dans l'agenda
2. Olivier envoie les cessions
3. Constituer équipe terrain (salariés ou intérimaires ?)
```

---

## Anti-patterns

- ❌ **Ne saute pas l'identification des cessions** — l'oubli = problèmes légaux post-congrès.
- ❌ **N'attends pas pour briefer Olivier** — les cessions prennent du temps à signer (>7j en moyenne).
- ❌ **Ne sous-estime pas le kickoff** — c'est la base d'une bonne expérience client.
- ❌ **Ne crée pas la fiche Congrès sans relations** (Personnes + Organisations).

## Identifiants Notion utiles

- 🏛️ Base Congrès : `c7ffc0cf7a3b427dab83c02f4fa4a03f`
- 👤 Base Personnes : `9d8d3c6b370d4c808502c0d6cd4c1e36`
- 🏛️ Base Organisations : `06d3fc453c564f7eb6d9b862529d209a`
- 📜 Contrats : `91c740ca092746369f9f7dae92c58870`
- 📝 Cessions : `b43dc5cf20bb4c22a414d11afd6d1ce2`
- 💼 Hub Commercial : `35e6979fbcd181c3b6bed19cc2fbb275`
- 🎬 Production : `35e6979fbcd1813990f6eec9e3d69723`
- 🐺 Cockpit Julien : `3616979fbcd181b8bb90f8ab0985ef39`
- 🦉 Cockpit Olivier : `3616979fbcd181c0b10ff2b25011ba1d`
