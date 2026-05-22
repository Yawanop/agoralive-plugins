# Mode Livret de congrès

Compile plusieurs articles en un document relié, imprimable, destiné à être
distribué sur un stand de congrès.

## Principe

Un livret = N articles + une enveloppe éditoriale (couverture, sommaire,
pagination continue). Chaque article est d'abord produit individuellement
(mode Conférence ou Sponsorisé) ; le livret les assemble.

## Composition

1. **Page de couverture** — nom et logo du congrès, millésime ou dates, titre
   du recueil, lockup AgoraLive (et sponsors si le recueil est sponsorisé).
2. **Sommaire** — titre de chaque article + numéro de page.
3. **Articles** — chacun démarre en belle page (page de droite, recto).
4. **4e de couverture** — colophon : éditeur, date, mentions légales,
   directeur de publication.

## Pagination et titres courants

- **Pagination continue** sur tout le livret. Le gabarit print accepte un
  numéro de première page paramétrable (même logique que `officiel-article-v3`).
- **Titre courant** en en-tête de chaque page : nom du congrès et/ou titre de
  l'article.
- La numérotation fiable est posée à l'export par le moteur de rendu
  (`export_pdf.py` / `build_livret.py`), pas par le CSS `@page` — les
  navigateurs ne rendent pas le contenu des marges `@page`.

## Réglages de production imprimeur

- **Fond perdu** 3-5 mm + traits de coupe si une couleur ou une image touche le
  bord de page.
- **Marge de reliure (gouttière)** — marge intérieure élargie ; marges en
  miroir recto/verso (`@page :left` / `:right`).
- **Recto/verso** — document pensé en double page.
- **CMJN** — convertir la charte en CMJN pour l'imprimeur (champ `colors_cmyk`
  du profil de marque) ; contrôler le rendu du teal, qui peut virer.
- **Export PDF/X** — PDF/X-1a ou X-4, polices embarquées, profil colorimétrique
  inclus.
- **Format** — A4 ou A5 selon le congrès, à fixer au démarrage.

## Atout

Tout le contenu graphique des articles est vectoriel (logos et schémas en SVG) :
aucun problème de résolution à 300 dpi, c'est prêt pour l'impression. Seules
d'éventuelles photos ajoutées doivent être fournies en 300 dpi.

## Assemblage

`scripts/build_livret.py` prend la liste des articles (HTML print déjà rendus)
et le profil du congrès, puis produit le livret complet : couverture, sommaire,
articles paginés en continu. `export_pdf.py` génère le PDF/X final.
