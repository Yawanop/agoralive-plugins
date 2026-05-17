---
name: approche-congres-strategie
description: >
  Structure la stratégie d'approche d'un nouveau congrès dentaire (qui contacter
  en premier, par quel canal, avec quel message, à quelle saison, avec quel
  argument de valeur). Adaptée à la spécialité (Orthodontie / ODF / Dentaire
  généraliste / Chirurgie / Autres). Pour Michelle (Michel). À déclencher quand :
  "stratégie approche congrès", "comment on aborde X", "Michelle nouveau congrès",
  "plan d'attaque congrès dentaire".
---

# approche-congres-strategie — Stratégie d'approche d'un nouveau congrès

## Mission

Quand un nouveau congrès dentaire est identifié comme cible, Michelle aide Michel à structurer **la stratégie d'approche métier** — pas un cold call générique, mais une approche qui respecte les codes du milieu académique français.

---

## Procédure

### Étape 1 — Profile le congrès

Demande à Michel (ou cherche dans base Congrès `c7ffc0cf7a3b427dab83c02f4fa4a03f`) :
- **Nom du congrès** + société savante organisatrice (SFODF, AOFR, ADF, SFCO, etc.)
- **Spécialité** (ODF, dentaire généraliste, chirurgie orale, parodonto, etc.)
- **Périodicité** (annuel, biennal)
- **Taille** (200 participants ? 1000 ? plus ?)
- **Lieu + saison** (printemps ? automne ?)
- **Programme typique** (conférences plénières, ateliers, communications libres)
- **Historique sponsoring** (combien de sponsors, quel niveau de prix)

### Étape 2 — Identifie les bons interlocuteurs

Hiérarchie à respecter dans le milieu académique :
1. **Président de la société savante** (autorité ultime — Michel l'aborde directement)
2. **Comité scientifique du congrès** (validation programme)
3. **Comité d'organisation** (logistique, sponsors)
4. **Secrétaire général** (relai administratif)

Pour chaque interlocuteur :
- Nom + fonction
- Réseau Michel (déjà connu ? lien à activer ?)
- Profil (chercheur ? praticien ? institutionnel ?)

### Étape 3 — Cale le timing

Saisonnalité académique française :
- **Septembre-Octobre** : reprise, présentation programmes à venir
- **Novembre-Décembre** : bilan année, validation budgets
- **Janvier-Mars** : préparation congrès printemps
- **Avril-Juin** : congrès printemps + décisions automne
- **Juillet-Août** : silence académique (NE PAS contacter)

Selon la date du congrès cible → identifier la fenêtre optimale (typiquement 9-12 mois avant).

### Étape 4 — Adapte le message au profil

#### Si interlocuteur = Pr / Praticien

- Ton académique, érudit
- Référence à des numéros de journaux scientifiques de qualité
- Insistance sur la **pérennité éditoriale** (= ce qui les distingue d'un captationnaire classique)
- Pas de jargon "tech bro"

#### Si interlocuteur = Institutionnel (Secrétaire général, comité organisation)

- Ton pro, factuel
- Insistance sur la **valeur logistique** (libère leur équipe, simplifie la post-production)
- ROI sponsor (potentiel partenariat sponsors via AgoraLive)

### Étape 5 — Drafte le plan d'approche

```
📋 Plan d'approche : <Congrès>
Spécialité : <…>
Date cible : <…>
Fenêtre optimale contact : <mois>

👥 Interlocuteurs (par ordre)
1. <Nom + fonction + statut réseau Michel>
2. <Nom + fonction>
3. ...

📅 Timeline approche
• <Date> : Premier contact <Interlocuteur 1> via <canal>
• <Date+7j> : Suivi si pas de réponse
• <Date+14j> : Mail au Comité scientifique
• <Date+30j> : Si OK conceptuel → proposition formelle (`agoralib-pricing`)

🎯 Arguments-clés à passer (adaptés à la spécialité)
• <Argument 1 — pertinence pour cette société savante>
• <Argument 2>
• <Argument 3>

⚠️ Risques d'approche
• <Risque 1 : ex Pr X très réservé sur l'IA>
• <Risque 2>

📤 Coordination
• `nouveau-president-contact` pour le 1er email
• `mail-michel` pour les relances
• Trinôme Comm consulté si message public envisagé
```

### Étape 6 — Crée la fiche Congrès si pas déjà fait

Si le congrès n'est pas encore dans la base, crée la fiche avec `notion-document-router` ou directement via `notion-create-pages` dans la base Congrès.

---

## Anti-patterns

- ❌ **Ne contacte pas en juillet-août** — silence académique strict.
- ❌ **Ne saute pas la hiérarchie** — contacter directement un Pr sans avoir passé le Secrétaire général peut être perçu comme cavalier (à juger au cas par cas).
- ❌ **N'utilise pas le même message qu'un autre congrès** — chaque société savante a sa culture.
- ❌ **Ne pousse pas à closer en premier contact** — relation longue, plusieurs touches nécessaires.
- ❌ **Ne fais pas un mail générique** — toujours personnalisé (réseau Michel, citation d'un papier récent du président, etc.).

## Identifiants Notion utiles

- 🏛️ Base Congrès : `c7ffc0cf7a3b427dab83c02f4fa4a03f`
- 👤 Base Personnes : `9d8d3c6b370d4c808502c0d6cd4c1e36`
- 🐘 Cockpit Michel : `3616979fbcd181e39437fe6a77477720`
- 💼 Hub Commercial : `35e6979fbcd181c3b6bed19cc2fbb275`
- 🤝 Trinôme Comm : `35e6979fbcd18196834ad273a7807d80`
