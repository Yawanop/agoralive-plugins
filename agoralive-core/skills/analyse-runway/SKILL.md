---
name: analyse-runway
description: >
  Calcule et analyse le runway d'AgoraLive — trésorerie actuelle, burn rate
  moyen 3 mois, mois de visibilité restants. Identifie les seuils d'alerte (12,
  6, 3 mois), simule l'impact d'événements anticipés (recrutement clé, signature
  gros sponsor, levée), et propose des actions correctives si runway critique.
  Pour Philippine (Philippe BA) — mais utilisable par Paul, Julien, Olivier.
  À déclencher quand : "analyse runway", "où on en est en trésorerie",
  "Philippine calcule le burn", "runway", "combien de mois de visibilité".
---

# analyse-runway — Analyse runway AgoraLive

## Mission

Donner une lecture claire du runway, métrique-pivot du pilotage AgoraLive. Si on ignore son runway, on pilote à l'aveugle.

---

## Procédure

### Étape 1 — Récupère trésorerie + burn rate

Depuis Notion KPI mensuels (`fa0b21be8f6b4569aa4431e42320d7da`) :
- **Trésorerie fin de mois dernier** (valeur la plus récente disponible)
- **Burn rate des 3 derniers mois** (dépenses moyennes mensuelles)

Si ces valeurs ne sont pas dans Notion → demande à Olivier (côté trésorerie) et calcule depuis les factures Drive si possible.

### Étape 2 — Calcule le runway

```
Runway (mois) = Trésorerie actuelle / Burn rate mensuel
```

Niveau d'alerte :
- 🟢 **Sain** : > 12 mois
- 🟡 **À surveiller** : 6-12 mois
- 🟠 **Tension** : 3-6 mois — actions correctives nécessaires
- 🔴 **Critique** : < 3 mois — décision urgente Paul + Julien + Philippe

### Étape 3 — Identifie les événements anticipés

Recense ce qui va changer le runway dans les 6 prochains mois :

**Côté ENTRÉES** :
- Signatures sponsors attendues (pipeline pondéré)
- CA confirmé en attente d'encaissement
- Apports CCA (cf. hypothèse 100 k€ associés)
- Subventions / aides

**Côté SORTIES** :
- Recrutements prévus (cf. mission 🔴 RH Phase 2)
- Investissements matériel (enregistrement, etc.)
- Coûts récurrents qui démarrent (compta, paie, mutuelle dès 30 juin)
- Frais exceptionnels (déménagement, événement)

### Étape 4 — Simule l'impact sur runway

Pour chaque événement anticipé :

```
<Événement> → impact runway = <+/- X mois>
```

Restitue la **trajectoire 6 mois** :

```
M+1 : Trésorerie = <X k€> · Burn = <Y> · Runway = <Z>
M+2 : <…>
M+3 : <…>
M+6 : <…>
```

### Étape 5 — Restitue avec recommandations

```
📊 Analyse runway — <date>

💰 État actuel
• Trésorerie : <X k€>
• Burn rate moyen 3M : <Y k€/mois>
• Runway : <Z mois>
• Niveau d'alerte : 🟢/🟡/🟠/🔴

📅 Trajectoire 6 mois (avec événements anticipés)
M+1 : <Z mois>
M+3 : <Z mois>
M+6 : <Z mois>

🎯 Événements modélisés
• <+événement entrée> → +<X mois>
• <-événement sortie> → -<Y mois>

⚠️ Risques
• <Risque 1 : ex retard signature Henry Schein recule runway critique en M+4>

💡 Recommandations
• <ex : sécuriser CCA 100 k€ avant T2 pour éviter zone rouge M+5>
• <ex : reporter recrutement Head of Sales de 2 mois si pas de signature majeure d'ici M+2>

🎯 Si niveau alerte 🟠 ou 🔴 : déclencher decision-doc-paul-julien sur les actions correctives.
```

---

## Anti-patterns

- ❌ **N'invente pas la trésorerie** — si tu n'as pas la valeur, demande à Olivier.
- ❌ **Ne sur-pondère pas le pipeline** — les sponsors pondérés à 50% sont à 50%, pas à 100%.
- ❌ **N'oublie pas les coûts récurrents nouveaux** (paie, mutuelle, compta dès 30 juin 2026).
- ❌ **Ne dramatise pas sans données** — un seuil 🔴 doit être documenté.

## Identifiants Notion utiles

- 📊 KPI mensuels : `fa0b21be8f6b4569aa4431e42320d7da`
- 📈 Business Plan : `35e6979fbcd181f2b785dd872ba12722`
- 💰 Squad Finance : `3626979fbcd18164b631d9a3a5771a3f`
- ⚖️ Légal & Finance : `35e6979fbcd18116a3e4e5638feaf5ec`
- 🧠 Comité Mentor : `35e6979fbcd181569dc6c3cc418d6774`
