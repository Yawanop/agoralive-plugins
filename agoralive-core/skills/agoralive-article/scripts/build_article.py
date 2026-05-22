#!/usr/bin/env python3
"""
Finalisation d'un article AgoraLive — skill agoralive-article.

  python build_article.py --brand brands/sponsor-dentalmonitoring.json \
      --in article.html --out article-final.html

Le corps de l'article est rédigé par le skill en adaptant le gabarit de
référence (assets/template-web.html ou template-print.html). Ce script
finalise le fichier :

  1. applique le profil de marque — couleurs --brand-* dans le bloc :root ;
  2. vérifie que le fichier est autonome (aucune ressource externe hors
     Google Fonts).

Il ne réécrit jamais le contenu éditorial.
"""
import sys
import json
import re
import argparse

# nom de couleur dans le profil  ->  variable CSS dans le gabarit
BRAND_VARS = [
    ("accent",        "--brand-accent"),
    ("accent_soft",   "--brand-accent-soft"),
    ("accent_bright", "--brand-accent-bright"),
    ("tint",          "--brand-tint"),
    ("tint_deep",     "--brand-tint-deep"),
]


def apply_brand(html, brand):
    colors = brand.get("colors", {})
    for key, cssvar in BRAND_VARS:
        if key in colors:
            html = re.sub(
                rf"({re.escape(cssvar)}\s*:\s*)[^;]+;",
                rf"\g<1>{colors[key]};",
                html, count=1)
    return html


def check_autonomous(html):
    """Signale les ressources EXTERNES chargees (images/scripts via src, et
    feuilles de style externes). Les liens de navigation <a href="..."> ne sont
    pas concernes : un lien PubMed est legitime, il ne casse pas l'autonomie."""
    warnings = []
    for m in re.finditer(r'\ssrc\s*=\s*"([^"]+)"', html):
        u = m.group(1)
        if u.startswith(("http://", "https://")):
            warnings.append(u)
    for m in re.finditer(r'<link\b[^>]*\bhref\s*=\s*"([^"]+)"', html, re.I):
        u = m.group(1)
        if u.startswith(("http://", "https://")) and "fonts.g" not in u:
            warnings.append(u)
    return warnings


def main():
    ap = argparse.ArgumentParser(description="Finalisation d'un article — agoralive-article")
    ap.add_argument("--brand", required=True, help="profil de marque JSON")
    ap.add_argument("--in", dest="inp", required=True, help="HTML de l'article rédigé")
    ap.add_argument("--out", required=True, help="HTML finalisé")
    args = ap.parse_args()

    with open(args.brand, encoding="utf-8") as f:
        brand = json.load(f)
    with open(args.inp, encoding="utf-8") as f:
        html = f.read()

    html = apply_brand(html, brand)
    warnings = check_autonomous(html)

    with open(args.out, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Article finalisé : {args.out}")
    print(f"Marque appliquée : {brand.get('name')} ({brand.get('type')})")
    if warnings:
        print("AVERTISSEMENT — ressources externes non embarquées :")
        for w in warnings:
            print("  - " + w)
    else:
        print("Fichier autonome : OK.")


if __name__ == "__main__":
    main()
