# Bibliothèque de composants éditoriaux

Briques de mise en page communes aux deux modes. Sauf mention contraire, un
composant existe dans les deux formats (web + PDF). Le YAML porte le texte ;
le gabarit porte la forme.

## Structure d'ouverture

- **Bandeau marque** — en tête de contenu : logo de la marque + une phrase de
  contexte. En mode sponsorisé, mention « Contenu sponsorisé par X » obligatoire.
- **Hero** — accroche (eyebrow), titre h1, filet d'accent, chapô (auteur /
  éditeur / mention sponsor), méta de lecture (durée, public visé). Pas
  d'indicateur de « niveau ».
- **Objectifs de lecture** — encadré à liste numérotée, 4 à 6 objectifs.
- **À retenir** — encadré, 4 à 6 points clés en puces fléchées ; fond blanc,
  onde ambiante active.

## Corps

- **Sections h2/h3** — h2 avec filet d'accent court ; prose en paragraphes
  pleins. Jamais de listes télégraphiques dans le corps rédactionnel.
- **Termes de glossaire** (web) — `span` ouvrant une définition en bulle au
  survol/clic, + glossaire récapitulatif dans le rail droit. Absents du PDF.
- **« Saviez-vous ? »** — encadré teinté : un fait marquant sourcé, avec sa
  référence PubMed (PMID). 1 à 3 par article.
- **Cartes comparatives** — deux cartes côte à côte (avant/après,
  amélioré/inchangé…) ; carte mise en avant = bordure d'accent. Fond blanc,
  onde ambiante active.
- **Scénario d'usage** — encadré : contexte, observation, décision, appui
  littérature, puis « ce qu'il faut en tirer ».
- **Schéma SVG** — diagramme vectoriel (workflow, boucle de suivi…) + légende.

## Auto-évaluation et clôture

- **QCM** (web uniquement) — questions à choix multiple interactives. Retiré du
  PDF (décision Paul).
- **Encadré sponsor** — « À propos de ce contenu sponsorisé » : nature du
  contenu, méthode (revue de littérature, sources PubMed). Mode sponsorisé.
- **Bien interpréter ces résultats** — mode sponsorisé : encadré court et
  positif, orienté conditions de réussite. Remplace toute section « Limites ».
- **Références** — liste numérotée au format Vancouver, chaque entrée avec son
  PMID en lien PubMed. Chaque référence doit être citée dans le corps.

## Effets web (format HTML uniquement)

- **Onde ambiante** — halos de couleur de charte dérivant en continu derrière
  les cartes blanches (À retenir, QCM, cartes comparatives). Composée sur GPU
  (transform/opacity/translate). Réglages de référence validés :
  intensité 0.29, cycle 6 s, ampleur 67 %, flou 41 px, réactivité curseur 50 %.
- **Apparition au défilement** — sections et encadrés montent en fondu à
  l'entrée dans l'écran (une fois).
- **Profondeur au survol et au toucher** — pastille teintée sur les citations,
  ombre teal sur les cartes, glissé doux sur les liens du plan, badge des
  références qui se remplit.
- Tous ces effets sont désactivés sous `prefers-reduced-motion` et absents du
  PDF.

## Calibrage

Le détail des tailles, marges et budgets typographiques est porté par les
gabarits (`assets/template-*.html.jinja`). Ne pas redéfinir ces valeurs dans le
contenu : le YAML reste strictement éditorial.
