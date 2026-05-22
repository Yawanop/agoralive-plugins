# Audit d'un article AgoraLive

Tout article est audité avant livraison. L'audit a deux temps : des contrôles
déterministes automatiques, puis un audit guidé fond + forme.

## 1. Contrôles déterministes — `scripts/audit_article.py`

```
python scripts/audit_article.py article.html --mode sponsorise
```

Le script vérifie, sans rendu navigateur :

- **intégrité citations ↔ références** — aucun appel de citation orphelin,
  aucune référence morte ;
- **validité des ancres internes** (`#xxx`) ;
- **autonomie du fichier** — aucune ressource externe chargée hors polices ;
- **PMID présent** sur chaque référence ;
- **déclaration de sponsoring** (mode sponsorisé : bandeau + encadré).

Le script renvoie un rapport JSON ; chaque contrôle est `OK` ou `ALERTE`. Toute
ALERTE doit être corrigée avant de poursuivre.

## 2. Audit guidé — fond et forme

Adopter une posture d'auditeur exigeant : trouver les vrais problèmes — ceux
qu'un lecteur ou un relecteur remarquerait — et les corriger. Pas une liste
polie de suggestions.

### Axe contenu — note /25

- **Cohérence interne** — les chiffres concordent partout (à retenir, corps,
  synthèse) ; aucune affirmation contredite plus loin.
- **Structure** — enchaînement logique, sections distinctes, prose pleine
  (jamais de listes télégraphiques).
- **Rigueur** — chaque donnée chiffrée est rattachée à une référence.
- **Références** — réelles : recouper tout PMID douteux avec
  `scripts/pubmed_verify.py`. Format Vancouver cohérent.
- **Complétude** — mode sponsorisé : encadré « Bien interpréter ces résultats »
  présent ; ton favorable mais nuances factuelles non masquées.

### Axe design — note /25

- **Autonomie & liens** — fichier autoportant ; liens internes valides.
- **Contraste** — texte conforme WCAG AA (≥ 4,5:1 pour le petit texte).
- **Hiérarchie & mise en page** — titres / sous-titres / corps nettement
  distincts ; alignement régulier ; aucun chevauchement, aucun débordement.
- **Responsive** (web) — trois paliers ordinateur / tablette / téléphone ;
  plan de l'article et glossaire accessibles sur mobile.
- **Impression** (PDF) — `print-color-adjust: exact`, césure, veuves et
  orphelines maîtrisées, encadrés non coupés entre deux pages.
- **Accessibilité** — `prefers-reduced-motion` respecté, styles de focus
  visibles, `lang="fr"`.

## 3. Restitution

Produire un résumé dans le chat : note /25 par axe, total /50, puis la liste
des problèmes critiques par ordre de gravité. Corriger ensuite le document —
d'abord le contenu, puis la structure, puis le design. La version corrigée
doit être meilleure que l'originale, pas seulement rapiécée.

Cet audit est calqué sur la démarche du skill `audit-document`, spécialisée
ici pour les articles AgoraLive (web et PDF).
