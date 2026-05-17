---
name: contrats-watch
description: >
  Brief daily des contrats à traiter pour Olivier (Directeur Juridique). Ouvre la
  base Contrats Notion, filtre les items au statut "À traiter", priorise par
  urgence + montant, flag ceux qui pourraient passer les critères d'escalation à
  Paul (montant > 10k€ HT, juridiction étrangère, cession PI hors standard).
  Restitue un brief court actionnable. À déclencher quand Olivier (ou sa jumelle
  Olivia) demande : "mes contrats à traiter", "quoi de neuf juridique", "nouveau
  contrat", "contrats à viser", "Olivia mes contrats". Skill mutualisable : Paul
  peut l'invoquer pour visibilité escalations.
---

# contrats-watch — Brief daily des contrats pour Olivier

## Mission

Donner à Olivier (ou à sa jumelle Olivia) une vue claire des contrats **à traiter** ce matin, hiérarchisés par urgence + montant + risque d'escalation à Paul.

---

## Procédure

### Étape 1 — Ouvre la base Contrats

```
notion-fetch sur collection://91c740ca092746369f9f7dae92c58870
```

Récupère les data sources et identifie la vue "À traiter" (ou applique le filtre manuel : statut = `📥 À traiter` OU `🔄 En triage`).

### Étape 2 — Priorise par urgence + montant + risque escalation

Pour chaque contrat à traiter, évalue :

1. **Urgence** : deadline de signature, échéance de prestation, partie tierce qui attend
2. **Montant** : > 10 k€ HT one-shot ou > 2 k€/mois récurrent → flag escalation Paul
3. **Risque escalation** : juridiction étrangère, clause d'arbitrage, cession PI hors standard AgoraLive, demande CNIL/avocat externe → flag escalation Paul
4. **Type** : sponsoring, cession, prestation, partenariat — chacun a un workflow propre

### Étape 3 — Brief formaté

```
🦉 Contrats à traiter :
• Total : <nombre> dont <nombre> en escalation potentielle Paul

🚨 À escalader Paul :
  - <Titre contrat> — <raison escalation (montant/juridiction/PI)>

📋 Triage standard :
  - <Titre contrat> — <type> — <urgence>
  - <…>

👉 Recommandation : <ex : commencer par le contrat XYZ (deadline demain) avant le triage en cascade>
```

Si rien à traiter : *"Contrats à jour, pas de triage en attente."*

---

## Notes d'usage

- Pour vraiment **viser** un contrat (verdict GREEN/YELLOW/RED + fiche Notion), route vers `triage-contrat-agoralive`.
- Pour vérifier formellement les critères d'escalation Paul, utilise `escalation-paul-check`.
- Ce skill ne **modifie rien** dans Notion — il lit et priorise.

## Cas particuliers

### Aucun contrat à traiter
→ Dis-le : *"Rien à triager côté contrats. Bon moment pour avancer sur Phase 2 Compta ou autre chantier."*

### Beaucoup de contrats en escalation potentielle (>3)
→ Flag pour batch : *"⚠️ 4 contrats en escalation potentielle. Suggère un sync 30 min avec Paul pour les trancher en bloc."*

### Contrat très urgent (deadline <48h)
→ Flag visible en tête de brief : *"🔥 URGENT : contrat SFCD à signer avant vendredi 18h. Triage prioritaire."*

### Contrat sponsor de fabricant de dispositif médical
→ Note de vigilance : *"Sponsor dispositif médical → vérifier cohérence métier (ping Michel via `trinome-comm-coord`) AVANT triage légal."*

## Critères d'escalation à Paul (à graver)

- Verdict 🔴 RED en triage
- Juridiction étrangère ou clause arbitrale
- Montant > 10 k€ HT ou récurrent > 2 k€/mois
- Cession de PI au-delà du standard AgoraLive
- Demande CNIL, avocat externe, autorité (URSSAF, fisc)
- Modification clause de responsabilité / garantie non couverte par la RC pro

## Identifiants Notion utiles

- 📜 Base Contrats : `91c740ca092746369f9f7dae92c58870`
- 🦉 Cockpit Olivier : `3616979fbcd181c0b10ff2b25011ba1d`
- ⚖️ Légal & Finance : `35e6979fbcd18116a3e4e5638feaf5ec`
- 👤 Base Personnes : `9d8d3c6b370d4c808502c0d6cd4c1e36`
- 🏛️ Base Congrès : `c7ffc0cf7a3b427dab83c02f4fa4a03f`
