---
name: prospects-congres-watch
description: >
  Brief daily des prospects congrès pour Michel (Directeur Scientifique &
  Commercial Dentaire). Ouvre la base Congrès Notion, filtre les congrès avec une
  "Prochaine action" en retard, segmente par spécialité dentaire (Orthodontie /
  ODF / Dentaire généraliste / Chirurgie), et restitue un brief court actionnable
  respectant les codes du milieu académique dentaire. À déclencher quand Michel
  (ou sa jumelle Michelle) demande : "quels congrès aujourd'hui", "mes relances
  en retard", "Michelle quels prospects", "mes contacts à rappeler côté congrès".
  Skill mutualisable : Éloïse ou Julien peuvent l'invoquer pour suivi.
---

# prospects-congres-watch — Brief daily congrès pour Michel

## Mission

Donner à Michel (ou à sa jumelle Michelle) une vue actionnable des prospects congrès dentaires avec une **Prochaine action en retard**, en respectant son réflexe métier : segmenter par **spécialité dentaire**.

---

## Procédure

### Étape 1 — Ouvre la base Congrès

```
notion-fetch sur collection://c7ffc0cf7a3b427dab83c02f4fa4a03f
```

Identifie les data sources et localise la propriété "Prochaine action" (date) + "Spécialité" (select).

### Étape 2 — Filtre + segmente

1. **Filtre** : Prochaine action ≤ aujourd'hui (en retard ou prévue aujourd'hui), statut ≠ Signé/Perdu/Pas pour nous
2. **Segmente par spécialité** :
   - 🦷 **Orthodontie / ODF** (SFODF, AOFR, etc.)
   - 🦷 **Dentaire généraliste** (ADF, SOP, etc.)
   - 🦷 **Chirurgie orale** (SFCO, etc.)
   - 🦷 **Autres spécialités** (parodonto, implanto, prothèse, etc.)
3. Pour chaque congrès : identifie l'âge du retard et le contact principal (président société savante, comité scientifique)

### Étape 3 — Brief formaté posé

```
🐘 Point congrès du jour :

Orthodontie / ODF :
• <Congrès> — Prochaine action : <action> — Contact : <nom président> — retard <Nj>

Dentaire généraliste :
• <Congrès> — <…>

Chirurgie :
• <Congrès> — <…>

👉 Recommandation : <ex : rappeler le Pr Y (SFCO) — relation chaude, dernier échange il y a 12j, le bon moment pour proposer le partenariat Deauville 2027>
```

Si rien en retard, propose proactif : *"Pas de retard. Bon moment pour préparer la cible des congrès Q3 — on identifie 3 cibles ODF ?"*.

---

## Notes d'usage

- Pour drafter un mail à un président de société savante, utilise `mail-rediger` voix=michel.
- Pour un premier contact avec un nouveau président, route vers `nouveau-president-contact`.
- Pour préparer un call avec un président, utilise `prep-reunion` humain=michel.
- Ce skill ne **modifie rien** dans Notion — il lit et priorise.

## Cas particuliers

### Période juillet-août (silence académique)
→ Ne pas pousser à relancer : *"Période estivale = silence académique. Les relances seront mal perçues. Retour des relances en septembre."*

### Congrès qui n'a jamais été en contact (cold)
→ Suggère stratégie d'approche : *"Pas d'historique avec ce congrès. Avant relance, on cadre l'approche via `approche-congres-strategie` ?"*

### Plusieurs congrès même société savante (SFODF par exemple)
→ Suggère batch : *"3 congrès SFODF à relancer — possible de packager une approche commune avec le président général de la SFODF ?"*

### Congrès dont la "Prochaine action" est mal renseignée
→ Flag pour clarif : *"Action floue sur <congrès> — clarifier avant relance (qui contacter ? sur quel angle ?)."*

## Codes du milieu dentaire (à respecter)

- **Le rythme** : académique français = lent. Une relance tous les 10-14 jours, pas tous les 3 jours.
- **Le ton** : sobre, érudit, jamais "tech bro". Préférer "votre conférence inaugurale" à "votre talk".
- **L'autorité** : Michel a une légitimité Pr des universités. Il faut la maintenir, pas la diluer.
- **Saisonnalité** : éviter juillet/août (rentrée académique en septembre), pic congrès au printemps et automne.

## Identifiants Notion utiles

- 🏛️ Base Congrès : `c7ffc0cf7a3b427dab83c02f4fa4a03f`
- 🐘 Cockpit Michel : `3616979fbcd181e39437fe6a77477720`
- 👤 Base Personnes : `9d8d3c6b370d4c808502c0d6cd4c1e36`
- 💼 Hub Commercial : `35e6979fbcd181c3b6bed19cc2fbb275`
- 🤝 Trinôme Comm : `35e6979fbcd18196834ad273a7807d80`
- 🎬 Chaîne éditoriale : `35e6979fbcd1813990f6eec9e3d69723`
