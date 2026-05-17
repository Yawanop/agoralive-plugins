---
name: cessions-watch
description: >
  Brief daily des cessions de droits en attente de signature pour Olivier
  (Directeur Juridique). Ouvre la base Cessions de droits Notion, filtre les items
  en attente de signature, segmente par âge (récent / >7j / >14j), identifie les
  retards à relancer, et restitue un brief court actionnable. À déclencher quand
  Olivier (ou sa jumelle Olivia) demande : "mes cessions du jour", "qui doit
  signer", "où en est la signature de X", "cessions en attente", "Olivia mes
  cessions". Skill mutualisable : Paul ou Julien peut l'invoquer si besoin de
  visibilité sur les cessions sensibles (intervenants stars, congrès chauds).
---

# cessions-watch — Brief daily des cessions pour Olivier

## Mission

Donner à Olivier (ou à sa jumelle Olivia) une vue claire des cessions de droits **en attente de signature**, hiérarchisée par âge, pour qu'il puisse prioriser ses relances du matin.

---

## Procédure

### Étape 1 — Ouvre la base Cessions de droits

```
notion-fetch sur collection://b43dc5cf20bb4c22a414d11afd6d1ce2
```

Récupère les data sources et identifie la vue "En attente signature" (ou applique le filtre manuel : statut = `📨 Envoyé` OU `✍️ En signature`).

### Étape 2 — Segmente par âge

Pour chaque cession en attente, calcule le délai depuis l'envoi ou la création :

- 🟢 **Récent** : ≤ 7 jours — pas d'action urgente
- 🟠 **À surveiller** : 7-14 jours — première relance à envisager
- 🔴 **En retard** : > 14 jours — relance ferme nécessaire

### Étape 3 — Brief formaté

```
🦉 Cessions du jour :
• 🟢 Récentes (<7j) : <nombre>
• 🟠 À surveiller (7-14j) : <nombre> — <noms des intervenants>
• 🔴 En retard (>14j) : <nombre> — <noms> ⚠️ relance à pousser

👉 Recommandation : <ex : relancer Yves Surlemont (envoyé 18 mai, sans retour)>
```

Si tout est récent, dis-le : *"Cessions à jour, rien à relancer ce matin."*

---

## Notes d'usage

- Pour drafter le mail de relance, route vers `relance-signature` (skill à construire) ou utilise `mail-olivier` avec la voix juridique sobre.
- Si une cession dépasse les 30 jours sans signature → possiblement à escalader à Paul (l'intervenant pose problème, ou il faut renégocier).
- Ce skill ne **modifie rien** dans Notion — il lit et restitue.

## Identifiants Notion utiles

- 📝 Base Cessions de droits : `b43dc5cf20bb4c22a414d11afd6d1ce2`
- 🦉 Cockpit Olivier : `3616979fbcd181c0b10ff2b25011ba1d`
- 👤 Base Personnes : `9d8d3c6b370d4c808502c0d6cd4c1e36`
