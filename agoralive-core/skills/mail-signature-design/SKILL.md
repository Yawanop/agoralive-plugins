---
name: mail-signature-design
description: >
  Design une signature mail AgoraLive cohérente avec l'identité visuelle de la
  marque, à décliner par membre de l'équipe (nom, titre, contact, lien site,
  petits éléments graphiques). Mission 🟠 actuelle (Julien sur la Roadmap orga,
  Éloïse en input identité). Mutualisé Julie + Éloi. À déclencher quand :
  "design la signature mail", "drafte ma signature", "mail-signature-design",
  "Julie / Éloi signature mail équipe".
---

# mail-signature-design — Design signature mail AgoraLive

## Mission

Produire un design de signature mail cohérent avec l'identité AgoraLive (à finaliser via `identite-agoralive` si pas encore fait), décliné pour les 6 membres de l'équipe.

---

## Procédure

### Étape 1 — Récupère l'identité visuelle

Vérifie si le brand book v1 existe (cf. `identite-agoralive`). Si oui, récupère :
- Logo (URL ou fichier Drive)
- Palette de couleurs primaires
- Typographie principale

Si pas encore prêt → propose à Éloïse de finaliser l'identité d'abord, ou propose une signature minimaliste sans logo (juste texte + lien) en attendant.

### Étape 2 — Structure la signature type

Élements à inclure (dans cet ordre) :

1. **Nom complet** (gras, taille moyenne)
2. **Titre** (italique ou couleur secondaire, plus petit)
3. **Société : AgoraLive** (couleur primaire)
4. **Email professionnel** (lien mailto)
5. **Site web** : agoralive.ai (lien)
6. **Logo** (petit, à droite ou en-dessous)
7. (Optionnel) **Phrase clé** (en signature dérivée pour les mails marketing)

### Étape 3 — Propose 3 directions

Direction 1 — **Minimaliste pure**
```
[Nom]
[Titre] · AgoraLive
[email] · [site]
```

Direction 2 — **Avec logo**
```
[Logo 60px]   [Nom]
              [Titre]
              AgoraLive
              [email] · [site]
```

Direction 3 — **Avec bandeau coloré**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━
[Nom] · [Titre]
AgoraLive · [email] · [site]
━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Étape 4 — Décline pour chaque membre

| Membre | Nom complet | Titre | Email |
|---|---|---|---|
| Paul | Paul Boury | CEO & Product Owner | paul@agoralive.ai |
| Julien | Julien Boury | Directeur Général | julien@agoralive.ai |
| Philippe | Philippe Salah | CTO & Mentor | philippe@agoralive.ai |
| Éloïse | Éloïse [nom] | Directrice Commerciale | eloise@agoralive.ai |
| Michel | Pr. Michel [nom] | Directeur Scientifique | michel@agoralive.ai |
| Olivier | Olivier Boury | Directeur Juridique | olivier@agoralive.ai |

### Étape 5 — Produit le HTML + Markdown des signatures

Pour chaque direction validée, drafte :
- Le **HTML** (à coller dans Gmail, Outlook, Apple Mail)
- Le **Markdown** (pour les signatures Notion ou Slack)

### Étape 6 — Restitue + instructions de mise en place

```
✉️ Signatures mail AgoraLive — v1

Direction retenue : <#1, #2, #3>

📦 Pour chaque membre :
• Paul Boury — [voir HTML ci-dessous]
• Julien Boury — …
...

🔧 Instructions installation Gmail
1. Gmail → Settings → General → Signature
2. Coller le HTML
3. Save

🔧 Instructions installation Outlook
1. Outlook → File → Options → Mail → Signatures
2. Coller le HTML
3. Save

📤 Diffusion : envoyer le pack signatures à chaque membre individuellement avec instructions.
```

---

## Anti-patterns

- ❌ **Ne fais pas une signature avec image lourde** (>50 ko) — ça finit en spam.
- ❌ **Ne fais pas une signature qui s'affiche mal en mobile** — teste systématiquement sur Gmail mobile.
- ❌ **N'ajoute pas de réseaux sociaux** sans accord du membre (pas tout le monde veut son LinkedIn perso en signature).
- ❌ **Ne fais pas une signature non actualisable** — un nouveau membre doit pouvoir reprendre le template.

## Identifiants Notion utiles

- 🗺️ Roadmap Organisation (mission Julien) : `3606979fbcd181d38416c267df9943bf`
- 🦋 Cockpit Éloïse (input identité) : `3616979fbcd181098eede7282c11e504`
- 🐺 Cockpit Julien (owner mission) : `3616979fbcd181b8bb90f8ab0985ef39`
