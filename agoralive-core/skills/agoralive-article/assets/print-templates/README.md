# Bibliothèque de gabarits PDF

Deux mises en page pour l'export PDF d'un article AgoraLive. Choisir un gabarit
selon le besoin, puis l'adapter via le bloc RÉGLAGES en tête de son `<style>`.

## Gabarits proposés

| Gabarit | Mise en page | Pour quoi |
|---|---|---|
| `classique.html` | Mono-colonne A4, aérée | Défaut. Lecture confortable, tiré-à-part. |
| `revue-2col.html` | Deux colonnes A4 | Style revue scientifique, plus dense. |

Les deux partagent la même charte, les mêmes composants et le même contenu de
référence (l'article DentalMonitoring) — seule la mise en page change.

## Réglages — modifier facilement la mise en page

En tête du `<style>` de chaque gabarit, un bloc RÉGLAGES pointe les valeurs à
éditer :

- **Format & marges** — la règle `@page { size: A4; margin: ... }`. Passer
  `A4` à `A5` pour un format de poche ; ajuster `margin` pour les marges.
  Pour un aperçu écran fidèle, reporter la même valeur sur `.sheet { padding }`.
- **Taille du texte** — `body { font-size }`, en points. La réduire pour
  resserrer un article long.
- **Nombre de colonnes** — gabarit `revue-2col` : `.sheet { column-count }`,
  dans le bloc « Mise en page 2 colonnes » en fin de feuille de style.
  Mettre `2` pour deux colonnes, `1` pour revenir à une colonne.

## Mise en page 2 colonnes — principe

Dans `revue-2col.html`, le corps de texte coule en deux colonnes. Occupent
toute la largeur de la page (`column-span: all`) : le titre, les schémas, les
cartes comparatives, les scénarios, l'encadré sponsor — ainsi que les
**objectifs de lecture**, l'encadré **« À retenir »**, les encadrés
**« Saviez-vous ? »** et la **synthèse**. Conserver cette règle pour tout
nouvel élément large ajouté.

## Créer un nouveau gabarit

Copier le gabarit le plus proche, le renommer, ajuster le bloc RÉGLAGES.
Exemples faciles : un gabarit A5 de poche (changer `size: A4` en `A5`), ou une
version resserrée (réduire `body { font-size }` et les marges `@page`).

## Export

L'export PDF se fait avec `scripts/export_pdf.py` quel que soit le gabarit
choisi.
