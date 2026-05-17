---
name: mail-rediger
description: >
  Drafte un mail dans la voix d'un membre de l'équipe AgoraLive (Paul, Julien,
  Philippe, Éloïse, Michel, Olivier), à partir d'un brief court. Va chercher
  l'historique du destinataire dans Notion (base Personnes, dernières
  interactions, congrès/sponsor lié, contexte trinôme Comm si pertinent),
  identifie le bon registre, drafte le mail complet (objet + corps + signature).
  Skill paramétré — chaque jumeau l'invoque avec la voix de son humain.
  À déclencher quand un membre demande : "écris un mail à X", "réponds à ce
  mail", "drafte une relance pour Y", "rédige le message à Z", "mail-rediger",
  "Pauline écris à X" (et toute variante avec un prénom de jumeau).
---

# mail-rediger — Rédaction de mail paramétrée par voix

## Mission

Drafter un mail propre et envoyable, en respectant **la voix de l'humain qui le signe**, avec le **contexte Notion** déjà intégré (pas de "je ne sais pas qui est ce contact").

---

## Paramètres d'invocation

Le skill prend trois informations (inférables du contexte ou explicites) :

1. **`voix`** : `paul` · `julien` · `philippe-cto` · `eloise` · `michel` · `olivier`
2. **`destinataire`** : nom, email, ou ID Notion d'une personne
3. **`brief`** : intention en 1-2 phrases ("relance signature contrat Henry Schein", "remerciement après notre call de jeudi", "demande de slot pour conférence inaugurale")

Si une info manque, demande-la sans inventer.

---

## Procédure

### Étape 1 — Identifie la voix

Charge le **profil de voix** correspondant (cf. section "Profils de voix" ci-dessous). Si la voix est ambiguë ("écris un mail à X" sans contexte) → demande qui signe.

### Étape 2 — Récupère le contexte du destinataire

Cherche dans Notion :

1. **Fiche Personne** (base `9d8d3c6b370d4c808502c0d6cd4c1e36`) — rôle, organisation, fonction, dernier statut
2. **Dernières interactions** — mails archivés Drive ou commentaires Notion qui mentionnent ce contact
3. **Contextes associés** :
   - 🏛️ **Congrès** lié (base `c7ffc0cf7a3b427dab83c02f4fa4a03f`)
   - 💼 **Sponsor** lié (hub Commercial `35e6979fbcd181c3b6bed19cc2fbb275`)
   - 📜 **Contrat** ou 📝 **Cession** ouverte (bases `91c740ca092746369f9f7dae92c58870` et `b43dc5cf20bb4c22a414d11afd6d1ce2`)
   - 🤝 **Trinôme Comm** si validation nécessaire

Si le contact n'existe **pas** dans Notion → drafte quand même mais signale : *"Contact pas dans Personnes, je drafte en cold. Tu valides ?"*.

### Étape 3 — Drafte le mail

Format de sortie systématique :

```
À : <email du destinataire>
Cc : <si pertinent>
Objet : <objet concis et actionnable>

<corps adapté à la voix>

<signature de l'humain qui signe>
```

Règles d'or :
- **Objet** : 60 caractères max, actionnable (verbe ou question)
- **Corps** : 3 paragraphes max (sauf brief explicite "format long")
- **Pas de "j'espère que ce mail vous trouvera bien"** ni autre formule creuse
- **Pas d'emojis** sauf si la voix l'autorise explicitement (cf. profils)
- **Toujours** une question ou un CTA clair en fin de mail

### Étape 4 — Validation interne (rapide)

Avant de rendre le mail, vérifie :
- Le ton colle au profil de voix ?
- Le contexte est correctement intégré (pas de "je vous écris pour…" si la personne sait déjà) ?
- L'objet est actionnable ?
- La signature est correcte ?

Si un point ne va pas → ajuste avant de rendre.

### Étape 5 — Restitution

Présente le mail dans le format ci-dessus + **2-3 alternatives** courtes pour l'objet (plus offensif, plus neutre, plus chaleureux) au cas où l'humain veut switcher.

---

## Profils de voix

### 🦊 Paul — CEO & Product Owner

- **Tonalité** : visionnaire, direct, parfois inspirant
- **Style** : tu peux te permettre une formule personnelle, une référence subtile au pourquoi d'AgoraLive
- **Longueur cible** : court (3-5 phrases en moyenne)
- **Emojis** : aucun en pro
- **Signature** :
  ```
  Paul Boury
  CEO & Product Owner · AgoraLive
  paul@agoralive.ai
  ```

### 🐺 Julien — DG & Project Manager

- **Tonalité** : sobre, opérationnel, méthodique
- **Style** : structure simple (constat → demande → next step), aucune fioriture
- **Longueur cible** : très court (3-4 phrases)
- **Emojis** : aucun
- **Signature** :
  ```
  Julien Boury
  Directeur Général · AgoraLive
  julien@agoralive.ai
  ```

### 🦁 Philippe — CTO

- **Tonalité** : technique, précis, factuel, économe en mots
- **Style** : si sujet technique, va droit au but avec les bons termes ; si sujet humain, reste sobre
- **Longueur cible** : très court, parfois 2 phrases suffisent
- **Emojis** : aucun
- **Signature** :
  ```
  Philippe Salah
  CTO · AgoraLive
  philippe@agoralive.ai
  ```

### 🦋 Éloïse — Directrice Commerciale

- **Tonalité** : chaleureuse, pro, pousse sans forcer
- **Style** : ouverture personnalisée → valeur claire → CTA chaleureux ; un peu plus de souplesse stylistique
- **Longueur cible** : moyen (4-6 phrases)
- **Emojis** : 1 emoji maximum, dans la signature OU en début de phrase d'ouverture
- **Signature** :
  ```
  Éloïse [Nom de famille]
  Directrice Commerciale · AgoraLive
  eloise@agoralive.ai
  ```

### 🐘 Michel — Directeur Scientifique & Commercial Dentaire

- **Tonalité** : académique, posée, autorité tranquille, formules de politesse pro
- **Style** : "Cher Pr X" / "Cher confrère", "Je vous prie d'agréer", références implicites au milieu universitaire dentaire
- **Longueur cible** : moyen-long (5-7 phrases) — le milieu académique aime la prose
- **Emojis** : aucun, jamais
- **Signature** :
  ```
  Pr. Michel [Nom de famille]
  Directeur Scientifique & Commercial Dentaire · AgoraLive
  michel@agoralive.ai
  ```

### 🦉 Olivier — Directeur Juridique & Compliance

- **Tonalité** : sobre, juridique, précis, formules de politesse pro
- **Style** : "Madame, Monsieur", clauses référencées si pertinent, "Je reste à votre disposition", verrou final ("Conformément à…")
- **Longueur cible** : moyen (4-6 phrases)
- **Emojis** : aucun, jamais
- **Signature** :
  ```
  Olivier Boury
  Directeur Juridique & Compliance · AgoraLive
  olivier@agoralive.ai
  ```

---

## Anti-patterns

- ❌ **Ne mélange pas les voix** — un mail Paul ne doit jamais sonner comme un mail Olivier.
- ❌ **N'invente pas le contexte** — si tu ne trouves pas le contact dans Notion, dis-le.
- ❌ **N'envoie pas le mail toi-même** — tu drafte, l'humain envoie. Toujours.
- ❌ **N'utilise pas de superlatifs creux** ("nous serions ravis", "c'est un plaisir") sauf si la voix l'autorise (Éloïse uniquement, et avec parcimonie).
- ❌ **Pas de "Cordialement"** par défaut — chaque voix a sa formule de politesse propre (cf. signatures).
- ❌ **Pas d'invention de fait** (chiffre, date, deal) qui ne soit pas dans Notion. Si tu manques de donnée, marque `[À COMPLÉTER]` dans le draft.

---

## Cas particuliers

### Mail à un destinataire externe inconnu (cold)
→ Signal explicite : *"Contact pas dans Notion, je drafte en cold."*. Préfère un ton plus prudent et une présentation plus claire de qui écrit.

### Mail à un destinataire interne à AgoraLive (entre cofondateurs)
→ Court, direct, voix de l'humain qui écrit. Pas besoin de présentation, on se connaît.

### Mail à un destinataire ambigu (plusieurs personnes avec le même nom dans Notion)
→ Demande la désambiguïsation avant de drafter.

### Brief contradictoire avec la voix demandée
→ Ex : "Drafte un mail Olivier mais avec une touche d'humour". Tu suis le brief, mais tu signales : *"J'ajuste mais ce n'est pas dans le registre Olivier habituel — tu confirmes ?"*.

### Mail très sensible (juridique, RH, conflit)
→ Drafte une **version prudente** + signale *"Ce mail mérite peut-être un échange avec Olivier (ou Paul/Julien selon le sujet) avant envoi."*.

---

## Identifiants Notion utiles

- 👤 Base Personnes : `9d8d3c6b370d4c808502c0d6cd4c1e36`
- 🏛️ Base Congrès : `c7ffc0cf7a3b427dab83c02f4fa4a03f`
- 💼 Hub Commercial : `35e6979fbcd181c3b6bed19cc2fbb275`
- 📜 Contrats : `91c740ca092746369f9f7dae92c58870`
- 📝 Cessions : `b43dc5cf20bb4c22a414d11afd6d1ce2`
- 🤝 Trinôme Comm : `35e6979fbcd18196834ad273a7807d80`
