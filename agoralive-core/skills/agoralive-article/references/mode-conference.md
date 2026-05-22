# Mode Conférence — article depuis une transcription

Transforme la transcription texte d'une conférence (issue du pipeline audio
d'AgoraLive) en article éditorial web + PDF.

## Entrées

| Entrée | Obligatoire |
|---|---|
| Transcription texte (`.txt`, `.md`, ou texte brut) | oui |
| Identité du congrès (profil de marque, ou nom + logo + couleurs) | oui |
| Titre de la conférence | oui |
| Nom du ou des conférenciers | oui |

Si une entrée manque, la demander en une seule question groupée avant de
commencer.

## Principe directeur — fidélité

L'article restitue le propos réellement tenu. Ne pas inventer de données, ne pas
ajouter de résultats, ne pas corriger ni « améliorer » le fond scientifique du
conférencier. Le travail est éditorial : structurer, clarifier, mettre en
forme — pas réécrire la science.

## Étapes

1. **Lire toute la transcription.** Identifier le fil réel : thèse, arguments,
   exemples, données chiffrées citées, conclusion.
2. **Charger le profil du congrès** depuis `assets/brands/` (ou le créer —
   voir `charte-marques.md`).
3. **Construire le plan** : 4 à 8 sections h2 qui suivent la logique de la
   conférence. Une section = une idée distincte.
4. **Rédiger** en prose éditoriale, en mobilisant les composants
   (`composants-editoriaux.md`) : hero, objectifs, à retenir, sections,
   schéma si un mécanisme est décrit, scénario d'usage si un cas est exposé.
5. **Encadrés « Saviez-vous ? »** — facultatifs. S'ils ancrent un fait dans la
   littérature, vérifier le PMID avec `scripts/pubmed_verify.py`. Sinon s'en
   passer : ne jamais inventer une référence pour étoffer.
6. **Glossaire** — repérer les termes techniques susceptibles d'échapper à une
   partie du lectorat, les baliser, rédiger leurs définitions.
7. **Produire le YAML** source, référençant le profil du congrès.
8. **Rendre** web + PDF (`build_article.py` puis `export_pdf.py`).

## Charte

La charte appliquée est celle du **congrès**. AgoraLive reste l'éditeur (logo et
mention dans le hero et le pied de page).

## Ce que le mode Conférence ne fait pas

Pas de revue de littérature systématique — c'est le mode Sponsorisé. Pas de
déclaration de sponsoring, sauf si la conférence est elle-même sponsorisée : le
préciser alors explicitement, comme en mode Sponsorisé.
