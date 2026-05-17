---
name: audit-code-sante-publique
description: >
  Audit ad hoc de conformité au Code de la santé publique pour les contenus
  AgoraLive touchant aux dispositifs médicaux, allégations, communication
  comparative, déclarations CMA (Commission Marketing Approuvée). Pour Olivia
  (Olivier). À déclencher quand : "audit code santé publique", "vérifie la
  conformité publicitaire", "Olivia check CSP", "ce contenu mentionne un
  dispositif médical".
---

# audit-code-sante-publique — Audit code santé publique

## Mission

Vérifier qu'un contenu AgoraLive (publication, brochure, page web, mail sponsor) qui touche au médical/dentaire respecte le Code de la santé publique français — réglementation stricte qui peut entraîner des sanctions (avertissement ANSM, retrait, amende).

---

## Procédure

### Étape 1 — Identifie le périmètre

Demande à Olivier :
- Quel contenu à auditer ?
- Quel canal (LinkedIn, brochure, mail privé, page web public) ?
- Quelle audience (B2C grand public, B2B professionnels de santé, mixte) ?

**Note importante** : la réglementation diffère selon B2C (très strict) vs B2B professionnels (plus souple). À clarifier toujours.

### Étape 2 — Vérifie les 6 points critiques

#### 1. Mention de dispositifs médicaux
- Le contenu mentionne-t-il un dispositif médical (gouttière, scanner, soft 3D, etc.) ?
- Si oui : mention du marquage CE ?
- Mention du fabricant / distributeur ?
- Description neutre vs promotionnelle ?

#### 3. Allégations thérapeutiques
- Le contenu fait-il une promesse de résultat clinique ?
- Ex : "réduit de 30% le temps de traitement", "soigne les malocclusions"
- → **Interdit en B2C** sans validation CMA (Commission Marketing Approuvée) en amont
- → **Encadré en B2B** : doit être documenté scientifiquement

#### 3. Publicité comparative
- Le contenu compare-t-il un dispositif ou un service à un concurrent ?
- En santé : **strictement encadré**, souvent interdit en B2C, à l'audit en B2B
- Si oui : preuves scientifiques requises + mention du standard de comparaison

#### 4. Déclaration CMA (Commission Marketing Approuvée)
- Pour publicités auprès du public (B2C) de dispositifs médicaux : déclaration CMA obligatoire avant diffusion
- Numéro de déclaration mentionné dans le contenu ?

#### 5. Mentions obligatoires
- Pour dispositifs médicaux en B2C : "Ce dispositif est un dispositif médical réglementé qui porte, au titre de cette réglementation, le marquage CE. Lire attentivement les instructions figurant sur la notice."
- Pour B2B : variations selon dispositif

#### 6. Citation de praticien / intervenant
- Le contenu cite-t-il un praticien comme "expert" ou "ambassadeur" ?
- Si oui : conformité avec le code de déontologie médicale (transparence des liens d'intérêts)
- Cession de droits + déclaration des liens d'intérêts dans la pub (lien Sunshine Act FR)

### Étape 3 — Évalue le risque

- 🟢 **Faible** : contenu informatif neutre, B2B, conforme
- 🟠 **Moyen** : ajustements nécessaires (mentions à ajouter, allégations à atténuer)
- 🔴 **Élevé** : risque sanction ANSM réel (allégation thérapeutique grave en B2C, pub comparative non documentée)

### Étape 4 — Restitue avec recommandations

```
🦉 Audit Code Santé Publique — <objet>
Date : <date>
Canal : <…>
Audience : <B2C / B2B / mixte>

📋 Points évalués
1. Dispositif médical : ✅ / ⚠️ / ❌ — <note>
2. Allégations : ✅ / ⚠️ / ❌ — <note>
3. Publicité comparative : ✅ / ⚠️ / ❌ — <note>
4. Déclaration CMA : ✅ / ⚠️ / ❌ / n/a — <note>
5. Mentions obligatoires : ✅ / ⚠️ / ❌ — <note>
6. Citation praticien : ✅ / ⚠️ / ❌ / n/a — <note>

🎯 Niveau de risque : 🟢 / 🟠 / 🔴

✏️ Reformulations / ajouts suggérés
<exemple>
Original : "X réduit les délais de traitement de 30%"
Reformulé : "Selon l'étude Y publiée en 2024, l'usage de X a été associé à une réduction
moyenne de 30% des délais de traitement chez une cohorte de 200 patients."

Mentions à ajouter :
• <Mention 1>

📤 Si risque 🔴 → escalation Paul + arrêt publication.
📤 Si risque 🟠 → corrections appliquées avant publication.
📤 Si risque 🟢 → OK à publier.
```

---

## Anti-patterns

- ❌ **Ne valide pas une allégation thérapeutique** sans preuve documentée.
- ❌ **Ne sous-estime pas la dimension B2C vs B2B** — c'est la première chose à clarifier.
- ❌ **Ne valide pas une publicité comparative** sans avis d'un avocat spécialisé si doute.
- ❌ **Ne fais pas l'audit seul si le sujet est très technique** — pour un dispositif médical complexe, consulter un avocat spécialisé.

## Identifiants Notion utiles

- 🦉 Cockpit Olivier : `3616979fbcd181c0b10ff2b25011ba1d`
- ⚖️ Légal & Finance : `35e6979fbcd18116a3e4e5638feaf5ec`
- 🛠️ Ops & Wiki Légal : `35e6979fbcd181e091e1eed92cc25f18`
- 🐘 Cockpit Michel (pertinence métier en amont) : `3616979fbcd181e39437fe6a77477720`
