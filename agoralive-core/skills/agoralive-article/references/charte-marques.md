# Système de charte — marques AgoraLive

Chaque article « porte » une marque. AgoraLive est l'éditeur (constant, présent
sur tous les articles). La marque variable est :

- le **congrès** en mode Conférence ;
- le **sponsor** en mode Sponsorisé.

Toute la couleur d'un article transite par des variables CSS `--brand-*` dans
les gabarits. Changer de marque = charger un autre profil, rien d'autre.

## Profil de marque

Un profil est un fichier JSON dans `assets/brands/`. Schéma de référence :
`assets/brands/_schema.json`.

| Champ | Rôle |
|---|---|
| `id` | identifiant fichier, ex. `sponsor-dentalmonitoring` |
| `type` | `congres` ou `sponsor` |
| `name` | nom affiché, ex. « DentalMonitoring » |
| `logo` | logo en data-URI (SVG inline encodé base64) ou chemin |
| `colors.accent` | teal foncé — titres, texte de marque |
| `colors.accent_soft` | couleur de marque principale |
| `colors.accent_bright` | variante claire — survols, onde ambiante |
| `colors.tint` | fond teinté très clair (encadrés) |
| `colors.tint_deep` | bordures teintées |
| `colors_cmyk` | équivalents CMJN pour l'impression (clé = nom de couleur) |
| `source` | `manuel` aujourd'hui ; `agoralive.ai` à terme |
| `date_maj` | date de dernière mise à jour |

## Correspondance avec les variables CSS

`build_article.py` injecte les couleurs du profil dans le bloc `:root` du
gabarit :

```
--brand-accent        ← colors.accent
--brand-accent-soft   ← colors.accent_soft
--brand-accent-bright ← colors.accent_bright
--brand-tint          ← colors.tint
--brand-tint-deep     ← colors.tint_deep
```

Les neutres éditoriaux (fonds papier, encres, règles) sont fixes — propres à
AgoraLive — et ne dépendent jamais de la marque.

## Créer un profil

1. Récupérer le logo de la marque, idéalement en SVG vectoriel (sinon PNG haute
   résolution) ; l'encoder en data-URI.
2. Relever les couleurs de la charte. Si une seule couleur est connue, dériver
   `accent` (assombrie ~12 %), `accent_bright` (éclaircie ~12 %), puis `tint` et
   `tint_deep` (versions très désaturées et claires).
3. Pour l'impression, renseigner `colors_cmyk` : une couleur écran RVB peut
   virer en CMJN — demander l'équivalent CMJN ou Pantone officiel à la marque.
4. Enregistrer dans `assets/brands/<type>-<nom>.json` avec `source: "manuel"`.

## Demain — récupération depuis agoralive.ai

L'architecture est prête : le champ `source` distingue déjà l'origine du profil.
Quand la récupération automatique sera branchée, un profil pourra être rempli
depuis la fiche du congrès ou du sponsor sur agoralive.ai (logo + couleurs),
avec `source: "agoralive.ai"`. Le reste de la chaîne — variables CSS, rendu —
ne change pas.
