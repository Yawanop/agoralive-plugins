#!/usr/bin/env python3
"""
Assemblage d'un livret de congrès — skill agoralive-article.

  python build_livret.py --brand brands/congres-sfodf.json \
      --titre "Les actes du congrès" --millesime "Édition 2026" \
      --out livret.html  article1-print.html article2-print.html ...

Insère les articles (HTML d'impression déjà rendus) dans le gabarit livret,
construit le sommaire et applique la charte du congrès. L'export PDF/X final
se fait ensuite avec export_pdf.py.

Note : les numéros de page du sommaire sont une estimation ; la pagination
exacte est posée à l'export PDF.
"""
import json
import re
import argparse
import pathlib

PAGES_PAR_ARTICLE = 6  # estimation pour le sommaire


def extract_body(html):
    m = re.search(r"<body[^>]*>(.*)</body>", html, re.S | re.I)
    return m.group(1) if m else html


def extract_title(html):
    m = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.S | re.I)
    return re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else "Article"


def apply_brand(shell, brand):
    colors = brand.get("colors", {})
    for key, var in (("accent", "--brand-accent"),
                     ("accent_soft", "--brand-accent-soft"),
                     ("accent_bright", "--brand-accent-bright"),
                     ("tint", "--brand-tint")):
        if key in colors:
            shell = re.sub(rf"({re.escape(var)}\s*:\s*)[^;]+;",
                           rf"\g<1>{colors[key]};", shell, count=1)
    return shell


def main():
    ap = argparse.ArgumentParser(description="Assemblage d'un livret — agoralive-article")
    ap.add_argument("articles", nargs="+", help="HTML d'impression des articles")
    ap.add_argument("--brand", required=True, help="profil du congrès JSON")
    ap.add_argument("--template", default="assets/template-livret.html",
                    help="gabarit livret")
    ap.add_argument("--titre", default="Les actes du congrès")
    ap.add_argument("--millesime", default="Édition 2026")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    brand = json.loads(pathlib.Path(args.brand).read_text(encoding="utf-8"))
    shell = pathlib.Path(args.template).read_text(encoding="utf-8")

    shell = apply_brand(shell, brand)
    shell = shell.replace("Congrès SFODF", brand.get("name", "Congrès"))
    shell = shell.replace("Les actes du congrès", args.titre)
    shell = shell.replace("Édition 2026", args.millesime)

    sommaire, corps, page = [], [], 3
    for i, path in enumerate(args.articles, 1):
        html = pathlib.Path(path).read_text(encoding="utf-8")
        titre = extract_title(html)
        sommaire.append(
            f'<li class="somm-item"><span class="somm-num">{i:02d}</span>'
            f'<span class="somm-text"><span class="somm-art">{titre}</span></span>'
            f'<span class="somm-dots"></span><span class="somm-page">{page}</span></li>')
        corps.append(f'<div class="page article-start">{extract_body(html)}</div>')
        page += PAGES_PAR_ARTICLE

    shell = re.sub(r'<li class="somm-item">.*?</li>',
                   "\n".join(sommaire), shell, count=1, flags=re.S)
    shell = re.sub(r'<div class="page article-start">.*?</div>',
                   "\n".join(corps), shell, count=1, flags=re.S)

    pathlib.Path(args.out).write_text(shell, encoding="utf-8")
    print(f"Livret assemblé : {args.out}  ({len(args.articles)} articles)")
    print("Étape suivante : export_pdf.py pour le PDF/X final.")


if __name__ == "__main__":
    main()
