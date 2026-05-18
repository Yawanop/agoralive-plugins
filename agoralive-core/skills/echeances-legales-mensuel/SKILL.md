---
name: echeances-legales-mensuel
description: >
  Brief mensuel des échéances légales d'Olivier (TVA, IS, CFE, social, contrats
  arrivant à expiration <60 jours, pièces vitales à renouveler comme RC pro,
  K-bis, statuts). À déclencher le 1er du mois ou quand Olivier (ou Olivia)
  demande : "mes échéances du mois", "Olivia check les échéances", "quoi à
  surveiller en compliance ce mois", "deadline légales".
---

# echeances-legales-mensuel — Brief mensuel échéances Olivier

## Mission

Le 1er de chaque mois (rituel 30 min), Olivier passe en revue les échéances légales + administratives. Ce skill agrège tout pour qu'il n'oublie rien.

---

## Procédure

### Étape 1 — Liste les 4 familles d'échéances

#### 1. Échéances fiscales

| Échéance | Périodicité | Date type |
|---|---|---|
| TVA T1 | Trimestrielle | 20 avril |
| TVA T2 | Trimestrielle | 20 juillet |
| TVA T3 | Trimestrielle | 20 octobre |
| TVA T4 | Trimestrielle | 20 janvier |
| Acompte IS (si applicable) | Trimestrielle | 15 mars / 15 juin / 15 sept / 15 déc |
| Solde IS | Annuelle | 15 du 4e mois après clôture |
| CFE (Cotisation Foncière des Entreprises) | Annuelle | 15 décembre |
| CVAE (Cotisation sur la Valeur Ajoutée) | Annuelle | 15 mai (déclaration) + acomptes |

#### 2. Échéances sociales

| Échéance | Périodicité | Date type |
|---|---|---|
| Déclaration mensuelle URSSAF (DSN) | Mensuelle | 5 ou 15 du mois suivant |
| Acomptes / soldes RSI / SSI (si TNS) | Trimestrielle | 5 du 1er mois du trimestre |
| Bilan social annuel | Annuelle | 30 juin |

#### 3. Échéances contractuelles (depuis bases Notion)

Ouvre la base Contrats (`91c740ca092746369f9f7dae92c58870`) :
- Filtre : `Date fin / expiration` dans les **60 prochains jours**
- Inclut : contrats clients, sponsors, prestataires, baux, abonnements (RC pro, mutuelle, logiciels)

### 4. Pièces vitales à renouveler

| Pièce | Périodicité | Action |
|---|---|---|
| RC pro | Annuelle | Vérifier renouvellement, ajuster couverture si évolution activité |
| K-bis récent (<3 mois) | À la demande | Re-demander si plus vieux que 3 mois |
| Statuts à jour | À chaque modif capital ou gouvernance | Vérifier conformité |
| Mutuelle | Annuelle | Renouvellement + revue couverture |

### Étape 2 — Calcule les échéances dans les 60 prochains jours

Pour chaque échéance, vérifie : date < aujourd'hui + 60 jours.

Segmente par criticité :
- 🔴 **Urgent (<14 jours)** — à traiter cette semaine
- 🟠 **À surveiller (14-30 jours)** — préparer ce mois
- 🟢 **À planifier (30-60 jours)** — bloquer le créneau

### Étape 3 — Identifie les pièces manquantes

Vérifie si certaines pièces vitales sont absentes ou périmées :
- RC pro en cours ? (date dernier renouvellement)
- K-bis < 3 mois disponible ?
- Statuts conformes ?

### Étape 4 — Restitue le brief mensuel

```
🦉 Échéances légales — <Mois Année>

🔴 Urgent (<14j)
• <Échéance 1> — date — type — action
• <Échéance 2> — …

🟠 À surveiller (14-30j)
• <Échéance>

🟢 À planifier (30-60j)
• <Échéance>

📂 Pièces vitales
• RC pro : ✅ à jour / ⚠️ renouvellement <date> / ❌ manquante
• K-bis : ✅ <X mois> / ⚠️ > 3 mois — re-demander
• Statuts : ✅ / ⚠️ <commentaire>
• Mutuelle : ✅ / ⚠️

📜 Contrats expirant <60j
• <Contrat 1> — date fin — renouvellement à anticiper
• <Contrat 2> — …

🎯 Recommandation : <action prioritaire ce mois>
```

### Étape 5 — Mise à jour Notion + diffusion

Si Olivier valide :
- Ajoute les échéances comme notes dans `🎙️ Inbox Vocal` (data source `5fcf5b4e-c35f-4da9-9290-68e17a0c63de`) avec Type détecté = `Tâche`, Pour = `Olivier`, Statut = `À traiter`
- Met une note dans son cockpit pour visibilité
- Si une échéance touche le BP (paiement IS, etc.) → ping Julien via `mail-rediger` voix olivier

---

## Anti-patterns

- ❌ **Ne minimise pas une échéance fiscale** — un retard = pénalités automatiques.
- ❌ **N'oublie pas la RC pro** — sans RC pro à jour, certains contrats deviennent inopposables.
- ❌ **N'ajoute pas trop de "À planifier 60j"** — focus sur l'imminent.
- ❌ **Ne fais pas le travail à la place d'Olivier** — tu listes, il agit.
- ❌ **Ne mélange pas avec `note-mensuelle-paul`** — celui-ci est l'inventaire des échéances, l'autre est le résumé envoyé à Paul.

---

## Identifiants Notion utiles

- 🦉 Cockpit Olivier : `3616979fbcd181c0b10ff2b25011ba1d`
- 📜 Contrats : `91c740ca092746369f9f7dae92c58870`
- ⚖️ Légal & Finance : `35e6979fbcd18116a3e4e5638feaf5ec`
- 🛠️ Ops & Wiki Légal : `35e6979fbcd181e091e1eed92cc25f18`
- 💰 Squad Finance (alertes paiement à Julien) : `3626979fbcd18164b631d9a3a5771a3f`
