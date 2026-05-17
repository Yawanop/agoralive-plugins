---
name: analyse-conversion-sponsor
description: >
  Analyse les ratios de conversion sur la base Sponsors AgoraLive — taux de
  conversion par étape (lead → qualifié → proposition → signé), ARPU moyen,
  cycle de vente moyen, taux de churn et raisons. Pour Éloi (Éloïse). Sert au
  pilotage commercial + à challenger les hypothèses BP (cf. bp-alignment-pipeline
  pour la vue stratégique Julien). À déclencher quand : "analyse mes conversions",
  "ratios sponsor", "Éloi analyse les conversions", "taux de closing".
---

# analyse-conversion-sponsor — Analyse conversions commerciales

## Mission

Donner à Éloïse une lecture précise de la performance commerciale par étape du funnel, pour identifier où on perd des deals et où ajuster.

---

## Procédure

### Étape 1 — Définit les étapes du funnel

Le funnel standard AgoraLive :

```
🟢 Lead (contact identifié)
  ↓
🟡 Qualifié (intéressé, critères matchent)
  ↓
🟠 Proposition envoyée
  ↓
🔵 En négociation
  ↓
✅ Signé
```

(Adapter selon vrai schéma Notion de la base Sponsors.)

### Étape 2 — Calcule les conversions par étape

Pour la période analysée (mois, trimestre, année) :

| Étape | Volume | Taux conversion vs précédente |
|---|---|---|
| Leads | <X> | — |
| Qualifiés | <Y> | <Y/X %> |
| Propositions envoyées | <Z> | <Z/Y %> |
| Négociations actives | <W> | <W/Z %> |
| Signés | <S> | <S/W %> |

**Taux conversion global** : S / X = <X%>

### Étape 3 — Compare aux benchmarks BP

Hypothèses BP de référence :
- Conversion sponsor 95% en An 3 (hypothèse 🔴 P1 BP Lab)
- ARPU 11 k€ (hypothèse 🔴 P1 BP Lab)

Si écart > 20% → flag pour `bp-challenge-philippe` ou `bp-alignment-pipeline`.

### Étape 4 — Identifie les fuites du funnel

Pour chaque étape avec conversion faible :
- Cause hypothétique (mauvais lead initial ? proposition mal calibrée ? cycle trop long ?)
- Action corrective possible (changement pitch, changement targeting, etc.)

### Étape 5 — Analyse les deals perdus

Pour les deals au statut "Perdu" ce trimestre :
- Raison principale (filtrer par tag : prix, fit, timing, concurrence, pas de retour)
- Étape à laquelle ils ont décroché
- Pattern récurrent ?

### Étape 6 — Calcule métriques avancées

- **Cycle de vente moyen** : durée Lead → Signé (en jours)
- **ARPU moyen** : Σ montants signés / N deals signés
- **Cycle ARPU pondéré** : montant × probabilité dans le pipeline actuel
- **Churn rate** (si renouvellement) : clients perdus / clients éligibles renouvellement

### Étape 7 — Restitue avec recommandations

```
📊 Analyse conversion sponsor — <période>

📈 Funnel
| Étape | Volume | Taux conv |
|---|---|---|
| Leads | <X> | — |
| Qualifiés | <Y> | <%> |
| Propositions | <Z> | <%> |
| Négo | <W> | <%> |
| Signés | <S> | <%> |
| **Global** | — | **<X%>** |

📊 Métriques
• ARPU moyen : <X €> (BP cible : 11 k€)
• Cycle vente : <X jours>
• Pipeline pondéré actuel : <X k€>

🚨 Fuites identifiées
• <Étape — taux faible — cause hypothétique>

❌ Deals perdus ce trimestre : <N>
Raisons :
• <Raison 1 — N deals>
• <Raison 2 — N deals>

💡 Recommandations
• <Action 1 — pour Éloïse>
• <Action 2 — coordination avec Michel ou Trinôme Comm>

📤 À remonter à Julien (DG) : <Oui/Non — quoi>
```

---

## Anti-patterns

- ❌ **N'analyse pas une période trop courte** — sur 1 mois la variance est énorme. Mini 1 trimestre.
- ❌ **Ne confonds pas Lead et Qualifié** — assure-toi du schéma Notion.
- ❌ **Ne fais pas de conclusion politique** — tu donnes les chiffres, Éloïse + Julien interprètent.
- ❌ **N'ignore pas les deals perdus** — c'est la mine d'enseignement #1.

## Identifiants Notion utiles

- 💼 Hub Commercial : `35e6979fbcd181c3b6bed19cc2fbb275`
- 📊 Pricer Sponsors : `3616979fbcd181e1b1b1c6a7f0335011`
- 💡 BP Lab : `24dc5471875c4821acce30c9e193b7c7`
- 📈 Business Plan : `35e6979fbcd181f2b785dd872ba12722`
- 🦋 Cockpit Éloïse : `3616979fbcd181098eede7282c11e504`
