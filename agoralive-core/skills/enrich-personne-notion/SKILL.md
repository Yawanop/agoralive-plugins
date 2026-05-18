---
name: enrich-personne-notion
description: >
  Enrichit une fiche Personne (contact pro B2B) dans la base 👤 Personnes Notion
  AgoraLive à partir de sources open source GRATUITES : recherche Google ciblée
  (LinkedIn public, site corporate), inférence de pattern email pro
  (prenom.nom@boite.com et variantes) avec validation SMTP/MX quand possible.
  Fournit un score de confiance HIGH/MEDIUM/LOW par champ et trace chaque source.
  À déclencher quand Paul, Éloïse, Julien (ou leurs jumeaux) demandent :
  "enrichis ce contact", "trouve le mail de [prénom] chez [boite]",
  "complète la fiche personne", "Éloi enrichis [nom]",
  "trouve-moi le téléphone de X", "qui contacter chez Y",
  "mail pro de [nom]". S'invoque aussi en batch sur les personnes liées à
  une société qu'on vient d'enrichir. Skill mutualisé.
---

# enrich-personne-notion — Enrichissement contact pro open source

## Mission

Compléter une fiche Personne (contact B2B prospection) avec mail pro, téléphone direct si trouvable, profil LinkedIn, poste actuel, **sans utiliser d'API payante** en v1.

L'approche est **plus heuristique** que pour les sociétés : les contacts personnels sont moins exposés publiquement, donc on combine plusieurs signaux et on **score la confiance**. Mieux vaut un champ vide qu'un faux mail.

---

## Pré-requis

1. Base 👤 Personnes Notion : `9d8d3c6b370d4c808502c0d6cd4c1e36`
2. La fiche cible doit avoir AU MINIMUM : prénom + nom + une référence société (relation vers Organisations, ou champ texte société).
3. Outil bash disponible pour les commandes DNS / SMTP de validation (`dig`, `host`).
4. (Optionnel) Token Hunter.io gratuit dans `~/Desktop/claude-hunter.txt` — 25 requêtes/mois gratuites, donne le **pattern email** d'un domaine.

---

## Procédure (7 étapes)

### Étape 1 — Identifier la cible + récupérer le contexte

1. Lire la fiche Notion : prénom, nom, société (relation), poste si déjà rempli.
2. Si société liée → récupérer son **domaine web** (champ Site de la fiche Organisation). Si pas de domaine → lancer en parallèle `enrich-societe-notion` pour le récupérer, puis revenir.
3. Vérifier les champs DÉJÀ remplis pour ne pas écraser des infos validées humainement.

### Étape 2 — Recherche LinkedIn publique

```
Google: "Prénom Nom" "<Société>" site:linkedin.com/in
```

Prendre le 1er résultat fiable. Extraire :
- URL profil LinkedIn (toujours `linkedin.com/in/<slug>`)
- Poste actuel affiché publiquement (snippet Google)
- Ancienneté approximative dans la boîte si visible

**Important** : on ne se logue PAS sur LinkedIn, on ne fait PAS de scraping authentifié. On utilise uniquement les résultats publics indexés par Google. C'est conforme aux CGU LinkedIn.

### Étape 3 — Inférer le pattern email de la société

Sources possibles, dans cet ordre :

1. **Hunter.io free tier** (si token dispo) :
   ```bash
   TOKEN=$(cat ~/Desktop/claude-hunter.txt)
   curl -s "https://api.hunter.io/v2/domain-search?domain=<DOMAIN>&api_key=$TOKEN" | jq .pattern
   ```
   Donne par exemple `{first}.{last}` ou `{f}{last}`.

2. **Recherche Google d'emails publics** : `"@<domain>" -site:<domain>` → repère un format dans les résultats (souvent mentions presse, papers académiques, signatures de mails leakés).

3. **Fallback heuristique** : si rien trouvé, générer les 5 patterns les plus courants :
   - `prenom.nom@<domain>`
   - `p.nom@<domain>`
   - `prenom@<domain>`
   - `nom@<domain>`
   - `prenom-nom@<domain>`

### Étape 4 — Construire les emails candidats + valider

Pour chaque pattern probable, construire l'email du contact ciblé. Exemple :
- Pattern Hunter : `{first}.{last}` → `eloise.dupont@henry-schein.fr`
- Fallback : 5 variantes listées plus haut

**Validation MX** (vérifie que le domaine peut recevoir des mails) :
```bash
dig MX <domain> +short
```
Si pas de MX → email forcément invalide, drop.

**Validation SMTP** (optionnel, à activer prudemment) :
```bash
# Ouvrir un socket SMTP et faire MAIL FROM + RCPT TO sans envoyer
# ⚠️ Beaucoup de serveurs détectent et bannissent les IPs qui font ça en masse
# → ne JAMAIS valider plus de 5 mails/heure sur le même domaine
```

**En v1, on se contente du MX + du pattern le plus probable** sans tester SMTP réellement. Le score de confiance reflète l'incertitude.

### Étape 5 — Téléphone (optionnel, faible probabilité)

Sources gratuites :
1. **Signatures de mail publiques** : Google `"<Prénom Nom>" "+33" OR "01" OR "06" "<société>"`
2. **Pages "Contact" du site** corporate : récupérer le standard, **pas un direct** (suffisant pour démarrage commercial).
3. **Programmes de congrès dentaires** : les conférenciers laissent souvent un numéro pro.

**Ne jamais inventer un numéro.** Si rien trouvé → champ vide.

### Étape 6 — Score de confiance par champ

| Champ | HIGH | MEDIUM | LOW |
|---|---|---|---|
| LinkedIn | Profil unique trouvé | Plusieurs candidats, choisi le + probable | Inférence par nom seul |
| Email pro | Hunter pattern + MX valide | Heuristique + MX valide | Heuristique sans validation |
| Téléphone | Signature mail publique | Page contact société (standard) | Aucun → vide |
| Poste | LinkedIn snippet récent | Mention presse récente | Inféré par titre interne |

### Étape 7 — Écriture Notion + récap

`notion-update-page` avec :
- Champs enrichis remplis
- `📝 Notes enrichissement` : pour chaque champ, ligne au format :
  ```
  [2026-05-18] Email ← Hunter pattern + MX validé (confiance HIGH)
  [2026-05-18] LinkedIn ← Google search publique (confiance HIGH)
  [2026-05-18] Téléphone ← Non trouvé en open source
  ```
- `🚦 Statut enrichissement` : `✅ Enrichi` ou `⚠️ Partiel` ou `❌ Échec`

Récap chat :

```
✅ Contact enrichi : <Prénom Nom>
🏢 <Société> — <Poste>
📧 <email> [HIGH/MEDIUM/LOW]
📞 <tel ou "non trouvé">
🔗 <URL LinkedIn>

🧠 Sources : <liste>
📥 Fiche Notion : <URL>

⚠️ À VALIDER AVANT 1er CONTACT : l'email à confiance MEDIUM ou LOW n'a PAS été vérifié SMTP. Test en envoyant un mail court d'abord (bounce = mauvais pattern).
```

---

## Cas particuliers

### Personne avec nom très commun (Jean Martin)
La probabilité de mismatch LinkedIn est forte. Demander à Paul la ville ou le poste précis pour disambigüer avant d'écrire en Notion.

### Personne d'une PME / cabinet libéral
Souvent pas de Hunter pattern, pas de LinkedIn. Tomber sur la page Contact du site + numéro de standard. Confiance LOW assumée.

### Société multinationale (Dentsply, Straumann…)
Pattern email souvent uniforme dans toute l'organisation → HIGH si Hunter le confirme.

### Domaine email d'une filiale (henryschein.fr vs henryschein.com)
Tester les deux. Privilégier `.fr` si la personne est en France (poste sur LinkedIn).

### Personne en transition (vient d'arriver / vient de partir)
LinkedIn indique souvent "Started X" ou "Open to work". Flagger dans Notes : `⚠️ Possible transition, à valider`.

### Contact dentiste / praticien individuel
Source spécifique : annuaire de l'Ordre National des Chirurgiens-Dentistes (public, mais accès via leur portail). Pour les universitaires : pages des facultés de chirurgie dentaire.

---

## Compliance RGPD (à valider avec Olivia)

- **Base légale** : intérêt légitime, prospection B2B.
- **Mention obligatoire dans le 1er email** : "vous pouvez vous opposer au traitement de vos données (lien de désinscription / mail dédié)".
- **Sources documentées** : champ Notes enrichissement = preuve du caractère public des données.
- **Pas de scraping authentifié** : on ne se logue jamais sur LinkedIn pour récupérer des données.
- **Pas de tracking caché** : pas de pixel espion dans les premiers mails.
- **Droit d'effacement** : si la personne demande retrait → suppression de la fiche Notion + log.

Avant industrialisation : invoquer `audit-rgpd` sur ce pipeline, et faire valider par Olivia la formulation de la mention "vous pouvez vous opposer" pour les mails de 1er contact (à coordonner avec `validation-legale-message`).

---

## Identifiants Notion utiles

- 👤 Base Personnes : `9d8d3c6b370d4c808502c0d6cd4c1e36`
- 🏛️ Base Organisations : `06d3fc453c564f7eb6d9b862529d209a`
- 💼 Hub Commercial : `35e6979fbcd181c3b6bed19cc2fbb275`

## Skills liés

- `enrich-societe-notion` — à lancer AVANT pour avoir le domaine web qui sert au pattern email
- `find-prospects-congres` — bootstrappe une vague de personnes à enrichir
- `mail-rediger` — pour drafter le 1er contact une fois enrichi (avec la mention RGPD obligatoire)
- `validation-legale-message` (Olivia) — valide le 1er mail avant envoi
- `audit-rgpd` — valide la conformité du pipeline d'enrichissement
