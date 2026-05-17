---
name: pitch-sponsor-iterator
description: >
  Itère sur le pitch sponsor d'AgoraLive — l'argumentaire utilisé par Éloïse
  pour convaincre un sponsor de financer un congrès. Affine les arguments-clés,
  prépare les objections types et leurs réponses, ajuste selon retour terrain
  (deals signés, perdus, raisons). Pour Éloi. À déclencher quand Éloïse demande :
  "itère le pitch sponsor", "améliore l'argumentaire", "Éloi pitch sponsor",
  "pitch deck commercial".
---

# pitch-sponsor-iterator — Itération du pitch sponsor

## Mission

Le pitch sponsor est l'arme commerciale d'Éloïse. À chaque deal perdu ou signé, il y a un enseignement. Éloi capitalise pour faire évoluer l'argumentaire.

---

## Procédure

### Étape 1 — Récupère le pitch actuel

Cherche dans Drive Pitch Deck ou hub Commercial le pitch sponsor en vigueur. Si plusieurs versions → identifier la dernière utilisée.

### Étape 2 — Analyse l'historique des deals

Depuis base Sponsors :
- Deals signés ce trimestre → quels arguments ont convaincu ? (vérifier les commentaires de closing)
- Deals perdus ce trimestre → quelles objections n'ont pas été levées ?

### Étape 3 — Structure les 5 arguments-clés du pitch

Un pitch sponsor AgoraLive bien construit a 5 arguments :

1. **🎯 Visibilité ciblée** : votre marque devant 200-500 dentistes/orthodontistes qualifiés (cible précise du congrès)
2. **📚 Pérennité éditoriale** : votre logo dans le numéro du journal qui circule pendant 12+ mois (vs sponsoring classique qui meurt avec le congrès)
3. **🤝 Légitimité scientifique** : sponsoriser l'éditorial = être perçu comme partenaire académique, pas commercial pur
4. **📊 Reporting concret** : audience, articles vus, citations — données mesurables après congrès
5. **💰 ROI vs alternatives** : comparé à un stand classique (5-10k€ sans pérennité), notre offre est compétitive

### Étape 4 — Affine selon retours terrain

Pour chaque argument, évalue :
- ✅ Argument qui ferme (mentionné dans deals signés)
- 🟡 Argument neutre (pas décisif)
- ❌ Argument qui ne porte pas (pas mentionné, ou contesté)

Renforce les ✅, requalifie ou supprime les ❌.

### Étape 5 — Prépare les objections types

Top 5 objections fréquentes + réponses préparées :

| Objection | Réponse type |
|---|---|
| "Trop cher vs notre budget sponsoring habituel" | "Comparons à un stand classique : 5-10k€ + frais transport + 2j de mobilisation. Notre offre c'est 12-25k€ tout inclus + 12 mois d'éditorial." |
| "Pas sûr que mon marketing valide" | "Je peux te préparer un one-pager spécifique pour ton équipe marketing — argumentaires + données ROI." |
| "On a déjà notre stratégie sponsoring 2026" | "Aucun souci. Pour 2027 on peut faire une convention cadre qui te donne accès à 3 congrès partenaires." |
| "Comment vous mesurez le ROI ?" | "Audience par article, citations en commission, demandes de devis générées dans le mois post-congrès. Reporting fourni à J+30." |
| "Vous n'êtes pas connus" | "Justement — c'est le moment d'être pionnier. Premier sponsor d'un congrès AgoraLive = positionnement long terme." |

### Étape 6 — Restitue le pitch v_next

```
📊 Pitch sponsor AgoraLive — v<X>
Mise à jour : <date>

🎯 5 arguments-clés (par ordre d'impact)
1. <Argument 1 — formulation>
2. <Argument 2>
3. <Argument 3>
4. <Argument 4>
5. <Argument 5>

⚠️ Top 5 objections + réponses préparées
1. <Objection> → <Réponse>
2. <…>
...

📈 Évolution depuis dernière version
• <Ajout 1 — pourquoi>
• <Suppression 1 — pourquoi>

🎯 À tester sur les 3 prochains deals : <ajustement spécifique>
```

---

## Anti-patterns

- ❌ **Ne fais pas un pitch de 20 slides** — 5-7 slides max, focus.
- ❌ **N'ajoute pas un argument sans preuve** — chaque argument doit pouvoir être étayé (chiffre, citation, retour client).
- ❌ **Ne mélange pas avec le pitch deck investisseur** — c'est un autre exercice (cf. `pitch-deck-iterator`).
- ❌ **Ne valide pas seul le pitch** — Éloïse + Michel (pertinence métier) + Olivier (légalité) doivent passer leur filtre.

## Identifiants Notion utiles

- 💼 Hub Commercial : `35e6979fbcd181c3b6bed19cc2fbb275`
- 📊 Pricer Sponsors : `3616979fbcd181e1b1b1c6a7f0335011`
- 🦋 Cockpit Éloïse : `3616979fbcd181098eede7282c11e504`
- 📁 Drive Pitch Deck : `https://drive.google.com/drive/folders/1skSuRFTMTaTiEKtyTEmEzb2vGen_lJUE`
- 🤝 Trinôme Comm : `35e6979fbcd18196834ad273a7807d80`
