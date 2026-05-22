# Mode Sponsorisé — revue de la littérature pour un sponsor

Produit un article sponsorisé sous forme de revue de la littérature, à partir
d'un sujet, pour le compte d'un sponsor.

## Entrées

| Entrée | Obligatoire |
|---|---|
| Sujet ou brief de l'article | oui |
| Identité du sponsor (profil de marque, ou nom + logo + couleurs) | oui |
| Périmètre / angle souhaité | recommandé |

## Objectif éditorial

Un article **scientifique mais favorable au produit** du sponsor. La crédibilité
scientifique d'AgoraLive est exactement ce que le sponsor achète : un article
100 % laudateur, repérable en trois lignes par un lecteur expert, détruit cette
crédibilité — donc la valeur de l'inventaire sponsorisé. L'équilibre juste :
rapporter des études réelles, honnêtement, en laissant l'argumentaire favorable
émerger des faits eux-mêmes.

## Étapes

1. **Charger le profil du sponsor.**
2. **Revue de littérature PubMed** — rechercher les études pertinentes sur le
   sujet et le produit ; sélectionner les publications revues par les pairs.
3. **Vérifier chaque PMID** avec `scripts/pubmed_verify.py`. **Aucun PMID
   inventé.** Si PubMed ne renvoie rien de pertinent pour un point, changer
   d'angle ou retirer le point. C'est le garde-fou absolu de ce mode.
4. **Structurer** en revue de la littérature : hero, objectifs, à retenir,
   sections thématiques, encadrés « Saviez-vous ? » sourcés, cartes
   comparatives, scénarios d'usage, synthèse.
5. **Ton** — rapporter les résultats tels que publiés, nuances factuelles
   comprises. Ne pas masquer un résultat gênant ; le présenter avec mesure.
6. **« Bien interpréter ces résultats »** — remplacer toute section « Limites
   de la preuve » par cet encadré court et positif, orienté conditions de
   réussite : utilisé comme prévu, l'outil donne sa pleine mesure ; la
   recherche sur le sujet est un champ récent et en pleine expansion.
7. **Déclaration de sponsoring** — obligatoire et visible : bandeau « Contenu
   sponsorisé par X » en tête + encadré « À propos de ce contenu sponsorisé »
   en fin d'article.
8. **Produire le YAML**, rendre web + PDF.

## Garde-fou — dispositif médical

Si le sponsor est un dispositif médical, la communication est encadrée par le
Code de la santé publique (publicité trompeuse, allégations, comparatif). Avant
toute publication, recommander explicitement une **validation par Olivier**
(validation légale). Les chiffres issus d'études menées par le fabricant
lui-même doivent être présentés comme tels, sans les faire passer pour des
preuves pleinement indépendantes.

## Charte

La charte appliquée est celle du **sponsor**. AgoraLive reste l'éditeur.
