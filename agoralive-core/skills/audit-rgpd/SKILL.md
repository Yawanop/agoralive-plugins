---
name: audit-rgpd
description: >
  Audit ad hoc de la conformité RGPD d'un workflow, d'une page, d'un formulaire,
  d'une intégration tierce, ou d'une nouvelle fonctionnalité AgoraLive. Vérifie
  flux de données personnelles, base légale, durée de conservation, droits
  utilisateurs, transferts hors UE, cookies/tracking. Pour Olivia (Olivier).
  À déclencher quand : "audit RGPD", "vérifie la conformité RGPD de X",
  "Olivia RGPD check", "ce workflow est-il conforme".
---

# audit-rgpd — Audit RGPD ad hoc

## Mission

Vérifier qu'un workflow / une page / une intégration AgoraLive est conforme RGPD avant déploiement ou publication.

---

## Procédure

### Étape 1 — Cadre le périmètre de l'audit

Demande à Olivier :
- Quel objet à auditer ? (workflow concret, page web, intégration, formulaire, app feature)
- Quel statut ? (idée, draft, en production déjà)

### Étape 2 — Vérifie les 8 points RGPD critiques

#### 1. Collecte de données personnelles
- Quelles données sont collectées ?
- Sont-elles strictement nécessaires (principe de minimisation) ?

#### 2. Base légale
Pour chaque finalité de traitement :
- Consentement (cocher case, signature, opt-in actif) ?
- Exécution contrat (sponsor signé, prestation) ?
- Intérêt légitime (à documenter) ?
- Obligation légale ?
→ Une finalité = une base légale. Pas de cumul flou.

#### 3. Information utilisateur
- Mention d'information présente (qui collecte, finalité, durée, droits) ?
- Politique de confidentialité accessible et à jour ?

#### 4. Durée de conservation
- Pour chaque catégorie de données, durée définie ?
- Mécanisme de purge automatique en place ?

#### 5. Droits utilisateurs (RGPD art. 15-22)
- Droit d'accès (mécanisme de réponse < 1 mois) ?
- Droit de rectification ?
- Droit d'effacement (sauf obligations légales contraires) ?
- Droit à la portabilité ?
- Droit d'opposition ?

#### 6. Sous-traitants et transferts
- Liste des prestataires qui accèdent aux données (Notion, Drive, etc.) ?
- DPA (Data Processing Agreement) signé avec chacun ?
- Transferts hors UE (USA, etc.) ? Si oui, mécanisme légal (clauses contractuelles types) ?

#### 7. Sécurité
- Chiffrement au repos (cloud) ?
- Chiffrement en transit (HTTPS) ?
- Accès limité (principe du moindre privilège) ?
- Sauvegarde + plan de récupération ?

#### 8. Cookies & tracking
Pour les pages web :
- Bandeau cookies conforme (refus aussi facile qu'accepter) ?
- Pas de cookie non-essentiel avant consentement ?
- Distinction cookies essentiels / statistiques / marketing ?

### Étape 3 — Liste les non-conformités

Pour chaque point, marque ✅ Conforme / ⚠️ À ajuster / ❌ Non-conforme.

### Étape 4 — Évalue le risque

- 🟢 **Faible** : non-conformités mineures, faciles à corriger
- 🟠 **Moyen** : non-conformités structurelles, à corriger avant déploiement large
- 🔴 **Élevé** : risque CNIL réel, à corriger AVANT toute mise en production

### Étape 5 — Propose un plan de mise en conformité

```
🦉 Audit RGPD — <objet audité>
Date : <date>

📊 Score conformité : <X/8 points OK>

✅ Points OK
• <Point 1>

⚠️ Points à ajuster
• <Point 2 — recommandation>

❌ Non-conformités à corriger
• <Point 3 — action prioritaire>

🎯 Niveau de risque : 🟢/🟠/🔴

📋 Plan de mise en conformité
1. <Action 1 — owner — deadline>
2. <Action 2 — …>

📤 Si risque 🔴 → escalation Paul + arrêt déploiement jusqu'à correction.
📤 Sinon → ajustements à intégrer dans le sprint en cours.
```

---

## Anti-patterns

- ❌ **Ne fais pas un audit superficiel** — un seul point manqué peut coûter cher (CNIL).
- ❌ **Ne valide pas RGPD sans connaître les sous-traitants** — c'est souvent là que ça pèche.
- ❌ **Ne sous-estime pas un risque cookies** — la CNIL est très active sur ce point.
- ❌ **Ne te substitue pas à un DPO** (Délégué à la Protection des Données) externe si le sujet est complexe.

## Identifiants Notion utiles

- 🦉 Cockpit Olivier : `3616979fbcd181c0b10ff2b25011ba1d`
- ⚖️ Légal & Finance : `35e6979fbcd18116a3e4e5638feaf5ec`
- 🛠️ Ops & Wiki Légal : `35e6979fbcd181e091e1eed92cc25f18`
