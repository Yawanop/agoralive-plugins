#!/usr/bin/env python3
"""
Export PDF d'un article AgoraLive — skill agoralive-article.

  python export_pdf.py article-print.html article.pdf

Rend un HTML d'impression (gabarit template-print ou template-livret) en PDF
A4 via un navigateur headless (Playwright / Chromium). Imprime les
arrière-plans et ajoute la pagination en pied de page.

L'exporteur pilote les marges : il neutralise le `@page` du gabarit pour que
la marge soit définie en un seul endroit (gouttière de reliure incluse pour
un livret).

Prérequis : pip install playwright  &&  playwright install chromium
"""
import sys
import argparse
import pathlib

FOOTER = (
    '<div style="font-family:Inter,Arial,sans-serif;font-size:8px;color:#6f6b63;'
    'width:100%;text-align:center;padding-top:4px;">'
    '<span class="pageNumber"></span> / <span class="totalPages"></span></div>'
)


def export(in_html, out_pdf, fmt="A4", margin=None):
    from playwright.sync_api import sync_playwright

    margin = margin or {"top": "14mm", "bottom": "16mm", "left": "15mm", "right": "15mm"}
    src = pathlib.Path(in_html).resolve().as_uri()

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(src, wait_until="networkidle")
        # marges pilotées ici : on neutralise le @page du gabarit
        page.add_style_tag(content="@page { margin: 0 !important; }")
        page.pdf(
            path=out_pdf,
            format=fmt,
            print_background=True,
            display_header_footer=True,
            header_template="<span></span>",
            footer_template=FOOTER,
            margin=margin,
        )
        browser.close()


def main():
    ap = argparse.ArgumentParser(description="Export PDF — agoralive-article")
    ap.add_argument("input", help="HTML d'impression (gabarit template-print / livret)")
    ap.add_argument("output", help="PDF de sortie")
    ap.add_argument("--format", default="A4", help="format de page (défaut A4)")
    args = ap.parse_args()

    try:
        export(args.input, args.output, args.format)
        print(f"PDF généré : {args.output}")
    except ImportError:
        print("Playwright manquant. Installer :\n"
              "  pip install playwright && playwright install chromium",
              file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Échec de l'export : {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
