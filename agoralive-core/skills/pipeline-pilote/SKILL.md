---
name: pipeline-pilote
description: >
  Vue de pilotage du pipeline congrès + sponsors pour Julie (Julien) — angle DG.
  Différent de pipeline-sponsors-watch (qui est l'angle commercial daily d'Éloïse).
  Ici : vue agrégée (CA pipeline pondéré, deals chauds, vélocité, deals qui dérivent,
  alertes), comparée au ramp BP, avec recommandations stratégiques. À déclencher
  quand Julien (ou Julie) demande : "où en est le pipeline", "Julie pipeline",
  "vue commerciale", "qu'est-ce qui chauffe côté commercial".
---

# pipeline-pilote — Vue de pilotage pipeline pour Julien (DG)

## Mission

Donner à Julien (en tant que DG + co-pilote Squad Finance) une **vue stratégique** du pipeline commercial — pas opérationnelle. Pour décider, pas pour appeler.

---

## Procédure

### Étape 1 — Agrège le pipeline complet

Depuis hub Commercial + base Sponsors :
- **Deals chauds** : statut "En négociation" ou "Proposition envoyée" avec activité <14j
- **Deals qui dérivent** : >30j sans contact, ou repoussés plusieurs fois
- **Deals signés ce mois**
- **Deals perdus ce mois** (et raisons si renseignées)

### Étape 2 — Calcule les métriques de pilotage

- **CA pipeline pondéré** : Σ(montant × probabilité)
- **CA confirmé YTD**
- **Cycle de vente moyen** : durée moyenne entre 1er contact et signature
- **Taux de conversion** : signés / opportunités créées
- **Vélocité** : nouveaux deals créés / nouveaux deals signés ce mois

### Étape 3 — Compare au ramp BP

Référence rapide :
- Cible 2026 : 6 deals, ARPU 11 k€, conversion 95% an 3
- Trajectoire trimestrielle attendue (sera ~1-2 deals/trimestre en 2026)

### Étape 4 — Identifie les signaux

🟢 **Bons signaux** :
- Pipeline pondéré > 3× CA confirmé YTD
- Cycle de vente qui raccourcit
- Conversion qui s'améliore
- Nouveaux deals créés > deals signés (= top of funnel sain)

🟠 **Signaux d'alerte** :
- Pipeline stagnant
- Beaucoup de deals qui dérivent (>5)
- Cycle de vente qui s'allonge
- Conversion en baisse

🔴 **Signaux critiques** :
- Aucun deal chaud
- Aucune signature ce mois ET pipeline vide
- Top deals perdus à la chaîne

### Étape 5 — Restitue le brief stratégique

```
📊 Pipeline pilote — <date>

💰 Métriques clés
• CA confirmé YTD : <X k€> (cible <Y k€>)
• CA pipeline pondéré : <X k€>
• Deals signés mois : <X>
• Cycle vente moyen : <X jours>
• Conversion : <X%>

📈 Vs ramp BP
• Cible deals 2026 : 6 / Réel YTD : <Y>
• Tendance : 🟢 / 🟠 / 🔴

🔥 Top deals chauds (en négo, à pousser)
• <Sponsor 1 — montant — statut — prochain step>
• <Sponsor 2>

⚠️ Deals qui dérivent (>30j sans contact)
• <Sponsor — depuis quand — pourquoi>

🚨 Signaux d'alerte
• <Signal — interprétation>

💡 Recommandations stratégiques
• <Action 1 — pour Éloïse / Michel / sync Paul-Julien>

👉 À porter au prochain sync Paul-Julien ? <Oui/Non — quoi>
```

---

## Anti-patterns

- ❌ **Ne fais pas le travail d'Éloi** — `pipeline-sponsors-watch` est daily commercial, celui-ci est hebdo/mensuel stratégique.
- ❌ **Ne dramatise pas un mauvais mois isolé** — regarde la tendance 3 mois.
- ❌ **N'oublie pas le ramp BP** — un pipeline qui va bien dans l'absolu mais mauvais vs BP, c'est mauvais.
- ❌ **Ne tranche pas seul une action stratégique** — Paul + Julien décident en sync.

## Identifiants Notion utiles

- 💼 Hub Commercial : `35e6979fbcd181c3b6bed19cc2fbb275`
- 📈 Business Plan : `35e6979fbcd181f2b785dd872ba12722`
- 📊 Pricer Sponsors : `3616979fbcd181e1b1b1c6a7f0335011`
- 🐺 Cockpit Julien : `3616979fbcd181b8bb90f8ab0985ef39`
- 💰 Squad Finance : `3626979fbcd18164b631d9a3a5771a3f`
