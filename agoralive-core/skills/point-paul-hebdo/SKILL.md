---
name: point-paul-hebdo
description: >
  Drafte le point hebdomadaire qu'Olivier (Directeur Juridique) laisse en
  commentaire de la page Direction Notion, pour que Paul ait en 3 lignes l'état
  juridique de la semaine : sujets chauds, escalations en cours, échéances à
  venir. Pour Olivia. À déclencher quand Olivier (ou Olivia) demande : "drafte
  mon point Paul de la semaine", "point Direction hebdo", "Olivia mon point
  hebdo", "fais-moi le point juridique pour Paul", "résume ma semaine pour Paul".
---

# point-paul-hebdo — Point hebdomadaire d'Olivier à Paul

## Mission

Drafter pour Olivier les **3 lignes hebdomadaires** qu'il laisse chaque lundi en commentaire de la page Direction Notion (`35e6979fbcd181cbbb32eec0b388dd15`) pour tenir Paul informé de l'état juridique sans rallonger leurs réunions.

---

## Procédure

### Étape 1 — Agrège les sujets de la semaine

Depuis les bases d'Olivier :

1. **📜 Contrats** (`91c740ca092746369f9f7dae92c58870`) : nouveaux contrats traités cette semaine, statuts qui ont bougé
2. **📝 Cessions** (`b43dc5cf20bb4c22a414d11afd6d1ce2`) : signatures obtenues, cessions en retard >7j
3. **🚨 Escalations en cours** : items où Olivier attend Paul
4. **📅 Échéances à venir** : contrats expirant <30j, échéances fiscales/sociales du mois
5. **🔴 Chantier Phase 2 Compta** : progression (deadline 30 juin 2026)

### Étape 2 — Identifie 3 lignes maximum

Sélectionne **les 3 sujets les plus actionnables** pour Paul cette semaine — pas plus. Olivier veut tenir Paul informé, pas l'écraser sous l'info.

Priorité de sélection :
1. Escalations (Paul doit décider quelque chose)
2. Risques émergents (signature qui dérape, contrat sensible)
3. Avancées du chantier compta Phase 2
4. Échéances dans les 14 jours qui méritent l'attention de Paul

### Étape 3 — Drafte le commentaire

Format imposé (3 lignes, pas plus) :

```
🦉 Point juridique S<semaine> :
• <Sujet 1 — état + action attendue de Paul si applicable>
• <Sujet 2>
• <Sujet 3>
```

Exemples bien écrits :

```
🦉 Point juridique S20 :
• Contrat SFODF 2027 signé ✅ — montant 18 k€
• 2 cessions Yves Surlemont en retard >7j — relance envoyée hier
• Phase 2 Compta : cabinet sélectionné (KPMG), souscription mardi prochain — RAS
```

```
🦉 Point juridique S21 :
• 🚨 Contrat Henry Schein → escalation Paul (juridiction US, clause arbitrage) — à acter cette semaine
• Cessions à jour, plus rien en retard
• Échéance TVA T1 lundi prochain — préparé, virement programmé
```

### Étape 4 — Poste le commentaire

Si Olivier valide → utilise `notion-update-page` pour poster le commentaire sur la page Direction (`35e6979fbcd181cbbb32eec0b388dd15`).

Sinon → restitue le draft pour qu'il le copie-colle lui-même.

---

## Anti-patterns

- ❌ **Ne dépasse pas 3 lignes** — c'est la règle. Si tu vois 5 sujets, choisis les 3 plus urgents et garde le reste pour la note mensuelle.
- ❌ **N'utilise pas de jargon juridique opaque** — Paul est CEO, pas juriste. Reste lisible.
- ❌ **N'invente pas une avancée** — si la Phase 2 Compta n'a pas bougé, dis-le ou omets-la.
- ❌ **Ne mélange pas avec la note mensuelle** — l'hebdo c'est 3 lignes, le mensuel c'est 5 lignes + plus de contexte.
- ❌ **Ne flag pas tout en escalation** — réserve l'escalation aux items qui passent vraiment les critères (>10k€, juridiction étrangère, etc.).

---

## Cas particuliers

### Semaine calme (rien à signaler)
→ Reste honnête : *"🦉 Point juridique S<X> : Semaine calme. Signatures à jour, pas d'escalation. Chantier Compta avance comme prévu."*

### Semaine très chargée (>5 sujets)
→ Suggère à Olivier d'ouvrir un sync avec Paul plutôt qu'un commentaire long. Le point hebdo reste 3 lignes.

### Une escalation déjà en cours non tranchée depuis 2 semaines
→ Re-flag explicitement : *"🚨 [SUITE] Escalation Henry Schein toujours en attente depuis S19 — bloque la signature"*. La répétition crée la pression.

---

## Identifiants Notion utiles

- 🧭 Direction (où poster le commentaire) : `35e6979fbcd181cbbb32eec0b388dd15`
- 🦉 Cockpit Olivier : `3616979fbcd181c0b10ff2b25011ba1d`
- 📜 Contrats : `91c740ca092746369f9f7dae92c58870`
- 📝 Cessions : `b43dc5cf20bb4c22a414d11afd6d1ce2`
- ⚖️ Légal & Finance : `35e6979fbcd18116a3e4e5638feaf5ec`
