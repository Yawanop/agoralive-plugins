---
name: recrutement-screener
description: >
  Pré-qualifie un candidat à partir d'un CV (PDF, lien LinkedIn, texte) ou d'une
  fiche existante dans la base Recrutement Notion. Évalue le matching avec le
  poste visé, drafte 5 questions d'entretien ciblées sur les compétences clés,
  flag les zones d'ombre à creuser, et crée/met à jour la fiche Notion.
  Skill mutualisé entre tous les jumeaux. À déclencher quand un membre demande :
  "screen ce candidat", "pré-qualifie ce CV", "Pauline analyse ce candidat",
  "Julie screen ce dev", "Olivia ce profil juridique", "Michelle ce profil dentaire".
---

# recrutement-screener — Pré-qualification candidat

## Mission

Donner à n'importe quel membre de l'équipe AgoraLive une **pré-qualification structurée d'un candidat**, prête à servir de base pour un entretien ou pour décider d'aller plus loin.

---

## Paramètres d'invocation

1. **`cv`** : PDF, lien LinkedIn, ou texte brut du CV
2. **`poste_vise`** : intitulé du poste + critères clés (ou ID fiche poste dans Recrutement Notion)
3. **`reviewer`** : qui va recevoir le brief (Paul, Julien, Philippe, Éloïse, Michel, Olivier)

Si la fiche poste n'existe pas → propose de la créer d'abord.

---

## Procédure

### Étape 1 — Lit le CV

Si PDF → utilise les outils Read pour extraire le texte.
Si lien LinkedIn → flag que tu ne peux pas accéder directement, demande à l'humain de copier-coller le profil.
Si texte brut → traite directement.

### Étape 2 — Compare au poste visé

Identifie les **5-7 critères clés** du poste (compétences techniques, expérience, soft skills, localisation, dispo, salaire attendu). Pour chacun :
- ✅ **Match clair** — preuve dans le CV
- 🟡 **Match partiel** — proche mais incomplet
- ❌ **Pas matché** — manque
- ❓ **Impossible à évaluer** — pas mentionné dans le CV

### Étape 3 — Identifie les zones d'ombre

3-5 questions auxquelles le CV ne répond pas, qu'il faut creuser en entretien :
- Trous chronologiques
- Compétences clés non démontrées
- Motivation pour AgoraLive
- Compatibilité culturelle (équipe petite, multi-casquette, parfois chaotique)

### Étape 4 — Drafte 5 questions d'entretien

Format pour chaque question :
```
Q<N> : <Question>
  Pourquoi : <ce que tu cherches à valider>
  Mauvaise réponse type : <signal d'alerte>
  Bonne réponse type : <signal positif>
```

Les 5 questions doivent couvrir : 1 technique, 1 expérience concrète (STAR), 1 motivation, 1 collaboration, 1 ouverte.

### Étape 5 — Restitue le brief

```
🎯 Pré-qualification : <Nom candidat>
Poste visé : <Intitulé>
Reviewer : <nom>

📋 Matching critères :
| Critère | Statut | Note |
|---|---|---|
| <Crit 1> | ✅ / 🟡 / ❌ / ❓ | <preuve ou manque> |
...

📊 Score global : <X/N critères matchés>
🎯 Verdict : 🟢 GO entretien · 🟡 OK avec réserves · 🔴 PASS (pas le profil)

❓ Zones d'ombre à creuser
• <Zone 1>
• <Zone 2>

🎤 Questions d'entretien suggérées
Q1 : <…>
Q2 : <…>
Q3 : <…>
Q4 : <…>
Q5 : <…>

👉 Recommandation : <ex : Vaut un premier call de 30 min — profil intéressant côté tech mais à creuser sur motivation>
```

### Étape 6 — Crée/met à jour la fiche Notion

Si Paul/Julien valide → crée fiche dans la base Recrutement (`e2029ad3f7894828a174e34156e831bc`) avec :
- Nom, Poste visé, Statut (`📥 Sourcé` ou `🔄 Pré-qualifié`)
- Lien vers fiche Personne (créer si nouveau)
- Brief de pré-qualif en commentaire
- Questions entretien en sous-page ou commentaire

---

## Adaptations selon le reviewer

- **Reviewer dev/tech (Philippe)** : `recrutement-tech-screener` plus poussé — focus stack, expérience produit, GitHub
- **Reviewer juridique (Olivier)** : focus barreau, spécialité, références cabinets
- **Reviewer dentaire (Michel)** : focus diplôme dentaire, spécialité, sociétés savantes
- **Reviewer commercial (Éloïse)** : focus expérience B2B, métriques (closing rate, cycle de vente), ARPU traités

---

## Anti-patterns

- ❌ **Ne juge pas l'humain sur le ton/style du CV** — focus compétences et matching.
- ❌ **N'invente pas de critères qui ne sont pas dans la fiche poste** — si la fiche manque, demande à l'humain de la clarifier.
- ❌ **Ne fais pas de discrimination** — pas de questions illégales (âge, situation familiale, religion, etc.).
- ❌ **Ne valide pas seul un GO entretien** — propose, le reviewer tranche.
- ❌ **Ne crée pas la fiche Personne** sans vérifier qu'elle n'existe pas déjà (anti-doublon).

---

## Identifiants Notion utiles

- 👔 Recrutement : `e2029ad3f7894828a174e34156e831bc`
- 👤 Personnes : `9d8d3c6b370d4c808502c0d6cd4c1e36`
- 🧭 Stratégie & équipe (Direction RH) : `35e6979fbcd181cbbb32eec0b388dd15`
