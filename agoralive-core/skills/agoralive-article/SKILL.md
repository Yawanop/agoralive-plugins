---
name: agoralive-article
description: >-
  Moteur éditorial d'AgoraLive — transforme une transcription de conférence ou
  un brief de sujet en article scientifique fini, en HTML web interactif ET en
  PDF imprimable, et compile plusieurs articles en livret de congrès. Deux
  modes : article de conférence (depuis la transcription audio) et article
  sponsorisé (revue de la littérature avec vérification PubMed). Gère la charte
  par congrès et par sponsor. À utiliser dès que l'équipe AgoraLive mentionne :
  créer ou générer un article, article de conférence, article sponsorisé,
  transformer une transcription en article, revue de littérature pour un
  sponsor, article web AgoraLive, version PDF d'un article, livret de congrès —
  ou dépose une transcription de conférence. Anti-triggers : article SFODF
  imprimé paginé (officiel-article-v3), poster (poster-builder), Word de
  révision (prepa-medicale, lecture-to-course).
---

# AgoraLive Article — Moteur éditorial web + PDF + livret

Ce skill produit les articles scientifiques éditoriaux d'AgoraLive. Il part
d'une matière brute (transcription de conférence ou sujet à traiter) et livre
un article fini dans deux formats, plus la possibilité de relier plusieurs
articles en livret de congrès.

C'est le moteur de production de contenu d'AgoraLive — l'éditeur qui publie,
le congrès ou le sponsor qui apporte la charte. Il ne faut jamais inventer de
données scientifiques ni de références : la fidélité à la source (transcription
ou littérature vérifiée) est la règle absolue.

## Quand utiliser ce skill

- Transformer la transcription texte d'une conférence en article web + PDF.
- Produire un article sponsorisé sous forme de revue de la littérature.
- Décliner un article existant dans l'autre format (web ↔ PDF).
- Compiler plusieurs articles en livret de congrès imprimable.

Ne pas utiliser pour : un article SFODF au gabarit imprimé strict 6 pages
(`officiel-article-v3`), un poster (`poster-builder`), un Word de révision
(`prepa-medicale`, `lecture-to-course`).

## Les deux modes de création

### Mode Conférence
Entrée : la **transcription texte** issue du pipeline audio d'AgoraLive, plus
l'identité du **congrès** (nom, logo, charte) et les métadonnées (titre de la
conférence, conférencier·s). Le skill structure le brut en article éditorial
fidèle au propos tenu — il ne complète pas, n'invente pas, ne corrige pas le
fond scientifique du conférencier. Charte appliquée = celle du congrès.
Procédure détaillée : voir `references/mode-conference.md`.

### Mode Sponsorisé
Entrée : un **sujet ou un brief**, plus l'identité du **sponsor**. Le skill
mène une revue de la littérature : recherche PubMed, sélection des études,
**vérification de chaque PMID** (voir garde-fous). Il rédige une « revue de la
littérature » au ton scientifique mais favorable au produit du sponsor. La
section critique « Limites de la preuve » est remplacée par un encadré court
et positif « Bien interpréter ces résultats » (orienté conditions de réussite).
La déclaration de sponsoring est obligatoire (bandeau en tête + encadré dédié).
Charte appliquée = celle du sponsor.
Procédure détaillée : voir `references/mode-sponsorise.md`.

## Les deux formats de sortie

Chaque article existe dans deux formats, à partir du même contenu éditorial :

- **HTML web** — mise en page 3 colonnes interactive : barre supérieure,
  sommaire latéral, contenu, rail de suggestions + glossaire, barre de
  progression, onde ambiante sur les cartes, apparition au défilement.
  Responsive (ordinateur 3 colonnes / tablette 2 colonnes / téléphone 1
  colonne). Gabarit : `assets/template-web.html`.
- **PDF imprimable** — édition pour le papier : page de titre, aucune barre
  latérale, aucune animation, QCM et glossaire absents (web uniquement),
  césure et veuves/orphelines maîtrisées, `print-color-adjust: exact`.
  Plusieurs mises en page dans la bibliothèque `assets/print-templates/`
  (classique mono-colonne ou revue 2 colonnes — voir son README).
  Export via `scripts/export_pdf.py` (rendu navigateur, type Playwright).

Les deux gabarits sont la généralisation des designs de référence validés avec
Paul sur l'article DentalMonitoring (web v11, PDF v2).

## Le mode Livret de congrès

Un livret relie **plusieurs articles** en un document imprimable unique :
page de couverture (nom + logo du congrès, millésime), 4e de couverture,
sommaire avec numéros de page, **pagination continue**, titres courants, et
réglages de production : fond perdu 3-5 mm, marge de reliure (gouttière) en
miroir recto/verso, démarrage de chaque article en belle page, conversion
CMJN de la charte, export PDF/X polices embarquées.
Gabarit : `assets/template-livret.html` ; assemblage via
`scripts/build_livret.py`. Procédure : voir `references/mode-livret.md`.

## Le système de charte (marques)

Toute la couleur d'un article transite par des variables CSS `--brand-*`.
Un **profil de marque** décrit une identité (congrès ou sponsor) : nom, logo,
couleurs (`accent`, `accent-soft`, `accent-bright`, `tint`), équivalents CMJN
pour l'impression. Les profils vivent dans `assets/brands/*.json`
(schéma : `assets/brands/_schema.json`).

Aujourd'hui les profils sont **renseignés manuellement**. L'architecture est
prête pour une récupération automatique depuis **agoralive.ai** : chaque profil
porte un champ `source` (`manuel` aujourd'hui, `agoralive.ai` demain) — quand
la récupération auto sera branchée, seul le mode de remplissage changera, pas
le reste de la chaîne.
Détail : voir `references/charte-marques.md`.

## Workflow

1. **Identifier le mode** (Conférence ou Sponsorisé) et rassembler les entrées
   manquantes en une seule question groupée.
2. **Charger ou créer le profil de marque** (congrès ou sponsor) depuis
   `assets/brands/`. Si le profil n'existe pas, le créer avec l'utilisateur.
3. **Réunir la matière** :
   - Conférence → lire la transcription, en extraire la structure réelle.
   - Sponsorisé → revue PubMed, vérifier les PMID avec
     `scripts/pubmed_verify.py`.
4. **Rédiger l'article** en prose éditoriale (jamais en listes télégraphiques),
   en mobilisant la bibliothèque de composants. Caler la déontologie (mode
   sponsorisé : déclaration + ton + dispositif médical).
5. **Mettre en forme** : partir du gabarit de référence
   `assets/template-web.html`, conserver sa structure, son CSS et son
   JavaScript, et y couler le contenu rédigé en adaptant chaque composant.
6. **Finaliser et rendre** : `scripts/build_article.py` applique le profil de
   marque et vérifie l'autonomie du fichier. Pour le PDF, choisir une mise en
   page dans `assets/print-templates/` puis lancer `scripts/export_pdf.py`.
7. **Auditer** : lancer `scripts/audit_article.py` (contrôles déterministes)
   puis l'audit guidé fond + forme de `references/audit-article.md` (note /50).
   Corriger toute alerte avant livraison.
8. **Livrer** le HTML web et le PDF.
9. **Livret** (si demandé) : produire chaque article, puis
   `scripts/build_livret.py` pour la compilation.

## Bibliothèque de composants éditoriaux

Briques disponibles, communes aux deux modes : bandeau sponsor/congrès, hero
(accroche, titre, chapô, méta de lecture), « Objectifs de lecture », « À
retenir », sections h2/h3, termes de glossaire (web), encadrés « Saviez-vous ? »
sourcés PubMed, cartes comparatives, scénarios d'usage, schémas SVG, QCM
d'auto-évaluation (web uniquement), encadré sponsor, références numérotées avec
liens PubMed, onde ambiante sur les cartes (web uniquement).
Catalogue, calibrage et règles d'emploi : voir
`references/composants-editoriaux.md`.

## Garde-fous

- **Jamais de PMID inventé.** En mode sponsorisé, chaque référence doit être
  vérifiée via `scripts/pubmed_verify.py`. Si PubMed ne renvoie rien de
  pertinent, demander un autre angle — ne jamais fabriquer une référence
  plausible. C'est l'erreur la plus grave possible pour une revue de littérature.
- **Fidélité à la source.** Mode Conférence : ne pas inventer de données ni
  réécrire le fond du conférencier. Mode Sponsorisé : rapporter les études
  telles que publiées, y compris leurs nuances factuelles (ex. durée de
  traitement non raccourcie).
- **Dispositif médical.** Si le sponsor est un dispositif médical, la
  communication est encadrée (Code de la santé publique). Recommander
  systématiquement une validation par Olivier (validation légale) avant
  publication.
- **Déclaration de sponsoring** toujours visible : bandeau en tête + encadré
  « À propos de ce contenu sponsorisé ».
- **Prose, jamais de listes télégraphiques** dans le corps rédactionnel.
- **Accessibilité** : `prefers-reduced-motion` respecté, contrastes conformes
  AA, navigation clavier.

## Structure du skill

```
agoralive-article/
├── SKILL.md                          ← ce fichier
├── references/
│   ├── mode-conference.md            ← structurer depuis une transcription
│   ├── mode-sponsorise.md            ← revue de littérature + PubMed
│   ├── composants-editoriaux.md      ← catalogue des briques + calibrage
│   ├── audit-article.md              ← contrôle qualité fond + forme
│   ├── mode-livret.md                ← compilation livret de congrès
│   └── charte-marques.md             ← système de marque + schéma JSON
├── assets/
│   ├── template-web.html       ← gabarit HTML web (design v11)
│   ├── template-livret.html    ← gabarit livret de congrès
│   ├── print-templates/        ← bibliothèque de gabarits PDF
│   │   ├── README.md           ← catalogue + guide des réglages
│   │   ├── classique.html      ← PDF mono-colonne A4 (défaut)
│   │   └── revue-2col.html     ← PDF deux colonnes
│   ├── logo-agoralive.svg            ← logo éditeur
│   └── brands/
│       ├── _schema.json              ← schéma d'un profil de marque
│       ├── sponsor-dentalmonitoring.json
│       └── congres-sfodf.json
├── scripts/
│   ├── build_article.py              ← applique la marque + vérifie l'autonomie
│   ├── export_pdf.py                 ← HTML print → PDF A4 (Playwright)
│   ├── pubmed_verify.py              ← vérification des PMID
│   ├── audit_article.py              ← contrôles déterministes d'un article
│   └── build_livret.py               ← compilation multi-articles en livret
└── examples/
    └── README.md                     ← renvoie vers les gabarits-exemples
```

## Références

Charger le fichier de référence pertinent au moment voulu :

- `references/mode-conference.md` — au démarrage d'un article de conférence.
- `references/mode-sponsorise.md` — au démarrage d'un article sponsorisé.
- `references/composants-editoriaux.md` — pendant la rédaction.
- `references/audit-article.md` — avant chaque livraison.
- `references/mode-livret.md` — pour une compilation en livret.
- `references/charte-marques.md` — pour créer ou charger un profil de marque.
