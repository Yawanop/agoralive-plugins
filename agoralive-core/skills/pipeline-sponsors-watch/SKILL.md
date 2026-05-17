---
name: pipeline-sponsors-watch
description: >
  Brief daily du pipeline sponsors pour Éloïse (Directrice Commerciale). Ouvre le
  hub Commercial Notion, identifie les deals chauds à pousser aujourd'hui, les
  relances en retard, les sponsors en attente de validation trinôme Comm, et
  restitue un brief court actionnable avec une recommandation de "qui appeler en
  premier". À déclencher quand Éloïse (ou son jumeau Éloi) demande : "qui je
  rappelle aujourd'hui", "pipeline du jour", "mes deals chauds", "Éloi pipeline",
  "qu'est-ce qui chauffe côté commercial". Skill mutualisable : Julien (DG) ou
  Paul peuvent l'invoquer pour suivi pipeline.
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

- Pour drafter un mail de relance, route vers `mail-commercial-eloise` avec la voix d'Éloïse.
- Pour préparer un call sponsor en détail, route vers `prep-meeting-eloise`.
- Si une validation trinôme est nécessaire, route vers `trinome-comm-coord`.
- Ce skill ne **modifie rien** dans Notion — il lit et restitue.

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
