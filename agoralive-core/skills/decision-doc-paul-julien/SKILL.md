---
name: decision-doc-paul-julien
description: >
  Structure une décision Paul+Julien (binôme Direction) en fiche standardisée :
  contexte, options envisagées (A/B/C), critères de choix, recommandation,
  décision finale, owners, deadlines, diffusion vers sous-sections. Archive
  dans Notion avec timestamp + lien Journal de bord. Skill mutualisé Pauline +
  Julie. À déclencher quand Paul (ou Pauline) ou Julien (ou Julie) demande :
  "documente cette décision", "on doit trancher X", "fiche décision pour Y",
  "Pauline structure la décision", "decision-doc".
---

# decision-doc-paul-julien — Documentation décisions Paul + Julien

## Mission

Chaque fois que Paul + Julien tranchent une décision structurante (allocation, recrutement, pricing, contrat, pivot), produire une **fiche décision standardisée** archivée dans Notion. Sans ce reflexe, les décisions s'évaporent ou se contredisent.

---

## Paramètres d'invocation

1. **`sujet`** : titre court de la décision
2. **`contexte`** : 2-3 phrases qui posent le problème
3. **`options`** : 2-4 options envisagées
4. **`urgence`** : `urgent` (deadline <48h) · `normal` (semaine) · `reflexion` (mensuel)

Si manque → pose les questions de cadrage (pas d'invention).

---

## Procédure

### Étape 1 — Cadre la décision

Pour qu'une fiche décision tienne, il faut clarifier :

- **Le problème** : qu'est-ce qui force à décider maintenant ?
- **Les options** : 2-4 alternatives concrètes (pas "faire / pas faire", trop binaire)
- **Les critères** : sur quoi on évalue chaque option (coût, runway, risque, complexité, alignement BP)
- **Les implications** : que se passe-t-il si on choisit A vs B vs C ?

### Étape 2 — Tableau des options

Pour chaque option :

```
Option <Lettre> : <Titre court>
• Description : <2 phrases>
• Coût / effort : <€ ou jours dev>
• Risque : <faible/moyen/élevé + raison>
• Bénéfice : <quoi concrètement>
• Réversibilité : <facile à annuler ou non>
```

### Étape 3 — Recommandation

Propose ta lecture (Pauline ou Julie), basée sur les critères. Format :

```
🎯 Recommandation : Option <X>
Justification : <pourquoi> 
Risque résiduel : <ce qui reste à surveiller>
Conditions de validation : <ce qui doit être vérifié en parallèle>
```

### Étape 4 — Décision finale (à remplir par Paul + Julien)

Laisse explicite l'espace pour la **vraie** décision :

```
✅ Décision actée : Option <_> 
Date : <_>
Décideurs : 🦊 Paul + 🐺 Julien
Sync préalable avec Philippe (si structurante) : ✅ / n/a
```

### Étape 5 — Diffusion + suivi

Liste les sous-sections à mettre à jour avec cette décision :

```
📤 Diffusion (sous 48h, règle d'or) :
• <Sous-section 1> : <quoi y mettre>
• <Sous-section 2> : <quoi y mettre>
...

📅 Suivi :
• Owner : <nom>
• Deadline première revue : <date>
• KPI à surveiller : <quoi>
```

### Étape 6 — Restitue la fiche complète + archive

Format final :

```
📋 Décision : <Sujet>
Date : <date>
Urgence : <urgent/normal/reflexion>

🎯 Contexte
<2-3 phrases>

📊 Options
Option A : <…>
Option B : <…>
Option C : <…>

🎯 Recommandation (Pauline ou Julie)
<…>

✅ Décision actée par Paul + Julien
[à remplir]

📤 Diffusion sous 48h
[liste]

📅 Suivi
[owner + deadline + KPI]
```

Si Paul/Julien valide → archive dans :
- 📅 Journal de bord (`39e76afc61e247ff8f5c320a14f4c74d`) — comme entrée datée
- 🧭 Direction (`35e6979fbcd181cbbb32eec0b388dd15`) — comme commentaire si la décision impacte le pilotage
- Sous-section concernée selon la nature (Légal, Finance, Commercial, etc.)

---

## Anti-patterns

- ❌ **Ne propose pas une seule option** — au minimum 2, idéalement 3.
- ❌ **Ne décide pas à la place de Paul + Julien** — tu prépares la fiche, ils tranchent.
- ❌ **Ne saute pas la diffusion** — sans diffusion 48h, la décision n'existe pas pour le reste de l'équipe.
- ❌ **N'archive pas dans 5 endroits** — vise les 1-2 sous-sections vraiment concernées.
- ❌ **Ne mélange pas avec un brief d'arbitrage** — `arbitrage-tri` priorise, ce skill structure une décision tranchée.

---

## Cas particuliers

### Décision structurante (allocation budget, recrutement clé, pivot pricing, financement)
→ Vérifie qu'un sync avec Philippe (mentor BA) a eu lieu en amont. Si pas → flag pour reporter à Comité Mentor ou pour sync ad hoc.

### Décision urgente (deadline <48h)
→ Ne pas saboter la qualité par l'urgence. Si l'analyse est incomplète, dis-le et propose un "decision sprint" 30 min.

### Décision difficile à trancher entre 2 options proches
→ Propose explicitement un test A/B ou une décision réversible avec checkpoint.

### Décision qui touche une partie tierce (sponsor, candidat, partenaire)
→ Liste explicitement les communications nécessaires post-décision (qui prévient qui, quand).

---

## Identifiants Notion utiles

- 📅 Journal de bord : `39e76afc61e247ff8f5c320a14f4c74d`
- 🧭 Direction : `35e6979fbcd181cbbb32eec0b388dd15`
- 🧠 Comité Mentor Philippe Salah : `35e6979fbcd181569dc6c3cc418d6774`
- 💡 BP Lab : `24dc5471875c4821acce30c9e193b7c7`
- 🦊 Cockpit Paul : `3616979fbcd18186bf48cb87faa13af3`
- 🐺 Cockpit Julien : `3616979fbcd181b8bb90f8ab0985ef39`
