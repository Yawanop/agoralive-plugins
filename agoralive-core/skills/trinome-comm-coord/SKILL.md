---
name: trinome-comm-coord
description: >
  Coordonne les validations du Trinôme Comm (Éloïse forme + Michel pertinence
  métier + Olivier compliance) pour tout sujet sortant qui touche au commercial
  ou à la communication AgoraLive (post LinkedIn, message sponsor, brochure,
  pitch, page web, mail externe). Identifie qui doit valider quoi, drafte le
  ping de validation adapté à chacun, et track le statut des validations en
  attente. Mutualisé entre Éloi (Éloïse), Michelle (Michel) et Olivia (Olivier).
  À déclencher quand un membre du trinôme demande : "valide ce post avec le
  trinôme", "ping Michel/Olivier sur X", "qui valide ce message",
  "trinome-comm-coord", "Éloi coordonne le trinôme sur Y".
---

# trinome-comm-coord — Coordination Trinôme Comm

## Mission

Donner au membre du Trinôme Comm qui sollicite (Éloïse, Michel ou Olivier) un workflow clair pour faire passer un sujet par les trois filtres avant publication ou envoi.

---

## Le Trinôme Comm — qui valide quoi

| Membre | Filtre | Exemples de sujets à valider |
|---|---|---|
| 🦋 **Éloïse** (Dir Commercial) | **Forme + impact commercial** | Ton, calls-to-action, branding, structure narrative |
| 🐘 **Michel** (Dir Scientifique & Commercial Dentaire) | **Pertinence métier dentaire** | Cohérence avec codes du milieu académique, vocabulaire correct, autorité maintenue |
| 🦉 **Olivier** (Dir Juridique) | **Légalité pure** | RGPD, code santé publique, mentions obligatoires, droits, allégations |

Les trois validations sont **séquentielles ou parallèles** selon le sujet, jamais redondantes.

---

## Procédure

### Étape 1 — Identifie le sujet à valider

Récupère :
- Le contenu (post, mail, brochure, pitch, etc.)
- Le canal de publication (LinkedIn, mail, site web, support imprimé)
- Le contexte (sponsor, congrès, événement, nouveau prospect)

### Étape 2 — Identifie qui doit valider

Selon le sujet, coche les validateurs nécessaires :

- **Toujours Éloïse** si le sujet est commercial ou communication marketing (sauf si elle est l'initiatrice)
- **Michel** si le sujet touche au milieu dentaire (mention spécialité, ton académique, contact société savante, communication scientifique)
- **Olivier** si le sujet mentionne : sponsor (clause RC pro), dispositif médical, données utilisateur, comparaison, allégation, droit à l'image, citation

Cas typiques :

| Type sujet | Éloïse | Michel | Olivier |
|---|---|---|---|
| Post LinkedIn tech sans dentaire | ✅ | ⚪ | ⚪ |
| Post LinkedIn parlant d'orthodontie | ✅ | ✅ | ⚪ |
| Message sponsor avec mention dispositif médical | ✅ | ✅ | ✅ |
| Brochure pour société savante | ✅ | ✅ | ⚪ |
| Newsletter aux congrès clients | ✅ | ⚪ | ⚪ |
| Site web — page services | ✅ | ⚪ | ✅ |
| Mail froid à un président société savante | ⚪ | ✅ | ⚪ |
| Contrat de cession | ⚪ | ⚪ | ✅ |

### Étape 3 — Drafte le ping de validation pour chacun

Pour chaque validateur identifié, drafte un ping court (en commentaire Notion ou en message direct) avec :
- **Le contenu à valider** (lien ou inline)
- **Le filtre attendu** (rappel court du rôle de validation)
- **La deadline** (par défaut : 48h ouvrées)
- **Le canal de retour** (commentaire Notion sur la fiche source, ou réponse directe)

Format :
```
@<Validateur>,

Sujet : <description sujet en 1 ligne>
Lien : <URL Notion ou Drive>
Filtre attendu : <son rôle de validation>
Deadline : <date>

Si OK → valide en commentaire "✅ OK + ton nom".
Si ajustement → propose une reformulation directement.
Si bloquant → on en discute en réunion trinôme ou via Slack.

Merci.
— <Initiateur>
```

### Étape 4 — Track le statut

Maintenir un état clair :
- Validateur attendu
- Statut : ⏳ En attente · ✅ Validé · 🔄 Ajustement demandé · ❌ Bloqué
- Date de relance si validation > 48h

Si une validation traîne > 5 jours → suggère une relance ou une escalade.

### Étape 5 — Restitue le récap

```
🤝 Trinôme Comm — coordination "<titre sujet>"

Validateurs requis : <liste>

Pings à envoyer :
• @Éloïse — <drafté ci-dessus> — deadline <date>
• @Michel — <drafté ci-dessus> — deadline <date>
• @Olivier — <drafté ci-dessus> — deadline <date>

État actuel :
• Éloïse : ⏳ En attente / ✅ Validé / 🔄 Ajustement
• Michel : ⏳ / …
• Olivier : ⏳ / …

👉 Prochaine action : <ex : envoyer les pings maintenant + relance à J+3 si silence>
```

---

## Anti-patterns

- ❌ **Ne sur-sollicite pas le trinôme** — si Michel n'a pas à intervenir sur un post tech pur, ne le ping pas.
- ❌ **N'inverse pas les rôles** — Michel ne valide pas la légalité, Olivier ne valide pas la pertinence métier.
- ❌ **Ne lance pas la publication sans toutes les validations** — sauf cas explicite d'urgence avec accord initiateur.
- ❌ **Ne fais pas la validation toi-même** — tu coordonnes, tu ne valides pas. Chacun valide son filtre.
- ❌ **Ne court-circuite pas Éloïse** — sauf si elle est l'initiatrice, elle valide systématiquement la forme.

---

## Cas particuliers

### Validation urgente (< 24h)
→ Drafte les pings avec un flag explicite ⚡ URGENT et la justification de l'urgence. Propose un fallback : "Si pas de retour à H+12, on publie avec disclaimer".

### Désaccord entre validateurs
→ Suggère un sync rapide trinôme (15-30 min) plutôt qu'un ping-pong asynchrone.

### Sujet récurrent (post LinkedIn hebdo type)
→ Suggère de **prévalider un template** une fois pour toutes, ensuite seules les variantes spécifiques nécessitent le trinôme.

### Sujet hors trinôme (technique pure, RH interne)
→ Flag : *"Pas pour le trinôme Comm. Sujet à router vers Philippe (tech) ou Paul+Julien (RH/strat)."*.

---

## Identifiants Notion utiles

- 🤝 Trinôme Comm — Stratégie 2026 : `35e6979fbcd18196834ad273a7807d80`
- 🦋 Cockpit Éloïse : `3616979fbcd181098eede7282c11e504`
- 🐘 Cockpit Michel : `3616979fbcd181e39437fe6a77477720`
- 🦉 Cockpit Olivier : `3616979fbcd181c0b10ff2b25011ba1d`
- 💼 Hub Commercial : `35e6979fbcd181c3b6bed19cc2fbb275`
- 📣 Calendrier éditorial : `738d418367fe47b780e26b3c43133357`
