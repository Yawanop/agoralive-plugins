---
name: bp-alignment-pipeline
description: >
  Aligne le pipeline commercial réel (depuis hub Commercial + Sponsors) avec le
  ramp BP (6 → 40 → 80 → 130 deals/an sur 4 ans). Détecte les écarts par
  trimestre, identifie les hypothèses BP à challenger si dérive, propose des
  actions correctives. Pour Julie (Julien, co-pilote Squad Finance avec Paul).
  À déclencher quand : "aligne pipeline et BP", "où on en est vs ramp",
  "Julie BP alignment", "écart pipeline".
---

# bp-alignment-pipeline — Alignement pipeline réel vs ramp BP

## Mission

Garantir que Julien a une lecture claire de l'écart entre pipeline commercial réel et hypothèses BP — pour anticiper les arbitrages avant qu'il soit trop tard.

---

## Procédure

### Étape 1 — Récupère le ramp BP

Depuis Business Plan (`35e6979fbcd181f2b785dd872ba12722`) :
- Cible deals signés / an : 2026 = 6, 2027 = 40, 2028 = 80, 2029 = 130
- ARPU moyen visé : 11 000 € (hypothèse 🔴 P1 BP Lab)
- Cible CA confirmé / an : 2026 = 66 k€, 2027 = 453 k€, 2028 = 934 k€, 2029 = 1 562 k€

### Étape 2 — Récupère le pipeline réel

Depuis hub Commercial (`35e6979fbcd181c3b6bed19cc2fbb275`) + base Sponsors :
- Deals signés YTD (year to date)
- Deals en négociation (pondérer par probabilité)
- Deals perdus
- ARPU moyen réel des deals signés

### Étape 3 — Calcule les écarts

| Métrique | Cible BP YTD | Réel YTD | Écart |
|---|---|---|---|
| Deals signés | <X> | <Y> | <%>  |
| CA confirmé | <X k€> | <Y k€> | <%> |
| ARPU moyen | 11 000 € | <Y €> | <%> |
| Conversion sponsor | <%> | <%> | <%> |

### Étape 4 — Interprète + flag

Pour chaque écart > 20% :
- Cause hypothétique (cycle de vente plus long ? cible mal choisie ? pricing mal calibré ?)
- Hypothèse BP à reviser (ramp ? ARPU ? conversion ?)
- Action corrective possible

### Étape 5 — Restitue avec recommandations

```
📊 Alignement pipeline / BP — <date>

📈 Cible BP 2026 : 6 deals · 66 k€ CA confirmé · ARPU 11 k€

📊 État réel YTD (au <date>)
• Deals signés : <Y> (cible YTD : <X>) — <écart %>
• CA confirmé : <Y k€> (cible YTD : <X k€>) — <écart %>
• ARPU moyen réel : <Y €> (cible : 11 k€) — <écart %>
• Pipeline pondéré actuel : <Z k€>

🚨 Écarts notables
• <écart 1> — interprétation
• <écart 2> — interprétation

💡 Hypothèses BP à challenger
• <Hypothèse 1> — pourquoi
• <Hypothèse 2> — pourquoi

🎯 Actions correctives proposées
• <Action 1 — owner — deadline>
• <Action 2>

👉 Recommandation : <ex : à remonter au prochain Comité Mentor, ou à trancher dans le sync Paul-Julien>
```

### Étape 6 — Diffusion

Si l'écart est significatif → propose un suivi :
- Si touche stratégique : `decision-doc-paul-julien` pour cadrer la décision
- Si touche hypothèses BP : `bp-challenge-philippe` pour challenger en Comité Mentor
- Si touche commercial opérationnel : update `pipeline-pilote` et brief Éloïse

---

## Anti-patterns

- ❌ **Ne mélange pas pipeline et CA confirmé** — l'un est probable, l'autre est certain.
- ❌ **Ne dramatise pas un écart de 10%** — la variance normale d'une startup tôt est élevée.
- ❌ **Ne remets pas en cause le BP à chaque écart** — distinguer dérive ponctuelle vs systémique.
- ❌ **Ne fais pas de proj annuelle à partir de 2 mois** — extrapole intelligemment.

## Identifiants Notion utiles

- 📈 Business Plan : `35e6979fbcd181f2b785dd872ba12722`
- 💼 Hub Commercial : `35e6979fbcd181c3b6bed19cc2fbb275`
- 💡 BP Lab : `24dc5471875c4821acce30c9e193b7c7`
- 💰 Squad Finance : `3626979fbcd18164b631d9a3a5771a3f`
- 📊 KPI mensuels : `fa0b21be8f6b4569aa4431e42320d7da`
- 🐺 Cockpit Julien : `3616979fbcd181b8bb90f8ab0985ef39`
