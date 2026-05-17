---
name: kpi-mensuel-update
description: >
  Met à jour la base KPI mensuels AgoraLive (`fa0b21be8f6b4569aa4431e42320d7da`)
  en début de chaque mois. Pour chaque métrique du tableau (CA pipeline, CA confirmé,
  conversion sponsor, trésorerie, articles publiés, audience LinkedIn, NPS, etc.),
  demande la valeur ou la calcule depuis les bases sources, et crée la ligne du
  mois. Pour Pauline (Paul, owner KPI direction). À déclencher au début du mois
  ou quand Paul (ou Pauline) demande : "update KPI du mois", "kpi-mensuel",
  "Pauline mets à jour les KPI", "stats du mois".
---

# kpi-mensuel-update — Mise à jour KPI mensuels AgoraLive

## Mission

Garantir que les KPI mensuels d'AgoraLive sont à jour pour servir au Comité Mentor, à la revue OKR, et au pilotage Paul + Julien.

---

## Procédure

### Étape 1 — Ouvre la base KPI mensuels

```
notion-fetch sur https://www.notion.so/fa0b21be8f6b4569aa4431e42320d7da
```

Identifie le schéma : Métrique, Mois, Valeur, Note, Source.

### Étape 2 — Liste les métriques à renseigner

Métriques standard à actualiser chaque mois :

#### 💰 Commercial
- **CA confirmé du mois** : depuis Sponsors signés ce mois
- **CA pipeline pondéré** : depuis Sponsors en cours × probabilité
- **Conversion sponsor** : signés / approchés ce mois
- **ARPU moyen** : CA confirmé / nb deals signés
- **Nb deals signés**
- **Nb leads qualifiés**

#### 🎬 Production / Édito
- **Captations réalisées**
- **Articles publiés**
- **Numéros bouclés**

#### 📣 Communication
- **Audience LinkedIn** (followers page entreprise)
- **Newsletter abonnés**
- **Posts publiés**
- **Engagement rate moyen**

#### 💼 Client
- **NPS moyen** (questionnaires reçus ce mois)
- **Clients renouvelés / total éligibles**
- **Clients perdus**

#### 🏦 Finance
- **Trésorerie fin de mois** (à demander à Olivier ou compta)
- **Burn rate moyen 3 mois**
- **Runway en mois** (trésorerie / burn)

### Étape 3 — Récupère ou calcule chaque valeur

Pour chaque métrique :

1. **Si valeur calculable depuis Notion** (CA, conversion, articles, etc.) → calcule
2. **Si valeur externe** (audience LinkedIn, trésorerie compta, etc.) → demande à l'humain owner (Éloïse pour LinkedIn, Olivier pour trésorerie, etc.)
3. **Si valeur manquante** → marque `[À COMPLÉTER — owner X]` et flag

### Étape 4 — Crée les lignes du mois

Pour chaque métrique, crée une nouvelle ligne dans la base KPI mensuels :
- Métrique : <nom>
- Mois : <YYYY-MM>
- Valeur : <chiffre>
- Note : <contexte si pertinent — pic exceptionnel, biais, etc.>
- Source : <calculé / saisi par X>

### Étape 5 — Restitue le résumé + écart vs mois précédent

```
📊 KPI mensuels — <Mois Année>

💰 Commercial
• CA confirmé : <X k€> (M-1 : <Y k€>) — <variation %>
• CA pipeline pondéré : <X k€>
• Conversion sponsor : <X%>

🎬 Production
• Captations : <X>
• Articles publiés : <X>
• Numéros : <X>

📣 Communication
• Followers LinkedIn : <X> (+<delta>)
• Newsletter : <X> abonnés

💼 Client
• NPS moyen : <X/10>

🏦 Finance
• Trésorerie : <X k€>
• Runway : <X mois>

🚨 Tendances notables
• <ex : CA en chute de 30% vs M-1, à investiguer>
• <ex : trésorerie sous le seuil 6 mois>

⚠️ Métriques non renseignées (à compléter)
• <Métrique 1 — owner X>
```

### Étape 6 — Flag pour Comité Mentor si pertinent

Si certains KPI méritent d'être remontés à Philippe BA → propose d'inclure dans le brief `comite-mentor-prep` du mois.

---

## Anti-patterns

- ❌ **N'invente pas une valeur** — si l'information manque, marque `[À COMPLÉTER]` et flag.
- ❌ **Ne mets pas à jour la base sans le brief de restitution** — la valeur de ce skill, c'est la lecture, pas la saisie.
- ❌ **N'oublie pas le runway** — c'est la métrique-pivot, toujours présente.
- ❌ **Ne loupe pas une métrique** — la cohérence dans le temps suppose qu'on ne saute pas de mois.
- ❌ **Ne fais pas d'analyse politique** — tu présentes les chiffres, Paul + Julien interprètent.

---

## Identifiants Notion utiles

- 📊 KPI mensuels : `fa0b21be8f6b4569aa4431e42320d7da`
- 🦊 Cockpit Paul : `3616979fbcd18186bf48cb87faa13af3`
- 🐺 Cockpit Julien : `3616979fbcd181b8bb90f8ab0985ef39`
- 💰 Squad Finance : `3626979fbcd18164b631d9a3a5771a3f`
- 🎯 OKR : `88627a768f894c07a2a7ee5a7044c1cd`
- 🧭 Direction : `35e6979fbcd181cbbb32eec0b388dd15`
- 🧠 Comité Mentor : `35e6979fbcd181569dc6c3cc418d6774`
