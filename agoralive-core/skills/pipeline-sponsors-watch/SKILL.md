---
name: pipeline-sponsors-watch
description: >
  Brief DAILY OPÉRATIONNEL du pipeline sponsors pour ÉLOÏSE (Directrice Commerciale).
  Ouvre le hub Commercial Notion, identifie les deals chauds à pousser AUJOURD'HUI,
  les relances en retard, les sponsors en attente de validation trinôme Comm.
  Recommandation "qui appeler en premier". À déclencher quand Éloïse (ou Éloi)
  demande : "qui je rappelle aujourd'hui", "pipeline du jour", "mes deals chauds",
  "Éloi pipeline", "Éloi qui je rappelle", "relances à pousser". DIFFÉRENT de
  pipeline-pilote (Julie, angle DG STRATÉGIQUE HEBDO/MENSUEL : CA pondéré, vélocité,
  alignement BP) : si Julien ou Julie demande la vue stratégique, invoquer
  pipeline-pilote à la place.
---

# pipeline-sponsors-watch — Brief daily commercial pour Éloïse

## Mission

Donner à Éloïse (ou à son jumeau Éloi) une vue actionnable du pipeline sponsors **aujourd'hui** : qui rappeler en priorité, quelles relances en retard, quels deals à pousser.

---

## Procédure

### Étape 1 — Ouvre le hub Commercial

```
notion-fetch sur https://www.notion.so/35e6979fbcd181c3b6bed19cc2fbb275
```

Identifie les bases liées (Sponsors, Congrès, Personnes contacts).

### Étape 2 — Récupère les 4 segments

1. **🔥 Deals chauds à pousser aujourd'hui** : statut "En négociation" ou "Proposition envoyée" avec date de prochain contact = aujourd'hui ou passée
2. **🟠 Relances en retard** : tout deal sans contact depuis > 7 jours et statut ≠ Signé/Perdu
3. **🟢 Nouveaux leads à qualifier** : statut "À qualifier" arrivés récemment
4. **⏸️ En attente validation trinôme Comm** : si une proposition sponsor nécessite OK Michel (pertinence métier) ou Olivier (légal)

### Étape 3 — Brief formaté énergique

```
🦋 Pipeline du jour :
• 🔥 À pousser MAINTENANT : <nombre> deals — top : <nom sponsor + statut + montant pondéré>
• 🟠 Relances en retard : <nombre> — <noms sponsors les plus chauds>
• 🟢 Nouveaux leads à qualifier : <nombre>
• ⏸️ En attente trinôme : <nombre> — <qui doit valider quoi>

👉 Top action : <ex : appeler Henry Schein (deal à 12 k€, proposition envoyée il y a 5 jours, pas de retour — le moment est mûr)>
```

Si tout est calme, propose une action proactive : *"Pipeline au calme — bon moment pour prospecter le congrès SFCD qui se prépare ?"*.

---

## Notes d'usage

- Pour drafter un mail de relance, utilise `mail-rediger` voix=eloise.
- Pour préparer un call sponsor en détail, utilise `prep-reunion` humain=eloise.
- Si une validation trinôme est nécessaire, route vers `trinome-comm-coord`.
- Ce skill ne **modifie rien** dans Notion — il lit et restitue.

## Cas particuliers

### Pipeline complètement vide (cas anormal)
→ Flag explicite : *"⚠️ Pipeline vide aujourd'hui. À investiguer rapidement avec Julien et Michel — pas un calme normal."*

### Beaucoup de deals chauds (>5 à pousser aujourd'hui)
→ Range par priorité : *"5 deals chauds — top 3 par valeur attendue : <liste>. Tu attaques par celui-ci en premier ?"*

### Sponsor en attente de validation trinôme depuis >5 jours
→ Flag : *"⚠️ Validation trinôme bloquée depuis 6j sur <sponsor>. Tu relances Michel ou Olivier ?"*

### Sponsor répété (deal perdu déjà, on retente)
→ Note de prudence : *"Sponsor déjà perdu en 2025. Vérifier raisons avant de re-pitcher — peut-être nouvel angle nécessaire."*

## Vocabulaire commercial (pour cohérence du brief)

- **Deal chaud** : statut "En négociation" ou "Proposition envoyée", retour récent positif
- **ARPU pondéré** : montant × probabilité de conversion (utile pour priorité)
- **Cycle de vente** : durée moyenne entre 1er contact et signature (sert à flagger les deals qui traînent)

## Identifiants Notion utiles

- 💼 Hub Commercial / Ventes & Comm : `35e6979fbcd181c3b6bed19cc2fbb275`
- 🦋 Cockpit Éloïse : `3616979fbcd181098eede7282c11e504`
- 📊 Pricer Sponsors : `3616979fbcd181e1b1b1c6a7f0335011`
- 🏛️ Base Congrès : `c7ffc0cf7a3b427dab83c02f4fa4a03f`
- 👤 Base Personnes : `9d8d3c6b370d4c808502c0d6cd4c1e36`
- 🤝 Trinôme Comm : `35e6979fbcd18196834ad273a7807d80`
- 🤖 Boîte à prompts commerciale : `f8a7d07ca0a64e4e8e6232dbfe4c8c72`
