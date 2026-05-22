#!/usr/bin/env python3
"""
Audit d'un article AgoraLive — skill agoralive-article.

  python audit_article.py article.html [--mode conference|sponsorise]

Contrôles DÉTERMINISTES sur le HTML d'un article (sans rendu navigateur) :
  - intégrité citations <-> références (aucun appel orphelin ni référence morte)
  - validité des ancres internes (#xxx)
  - autonomie du fichier (aucune ressource externe chargée hors polices)
  - présence d'un PMID sur chaque référence
  - déclaration de sponsoring (mode sponsorisé)

Renvoie un rapport JSON ; code de sortie 1 s'il reste au moins une ALERTE.
Les axes subjectifs (cohérence des chiffres, qualité de la prose, harmonie de
la mise en page) relèvent de l'audit guidé — voir references/audit-article.md.
"""
import sys
import re
import json
import argparse


def audit(html, mode=None):
    checks = []

    # 1. Intégrité citations <-> références
    cited = set(re.findall(r'href="#(ref\d+)"', html))
    defined = set(re.findall(r'<li[^>]*\sid="(ref\d+)"', html))
    dangling = sorted(cited - defined)
    orphans = sorted(defined - cited)
    checks.append({
        "controle": "Integrite citations <-> references",
        "statut": "OK" if not dangling and not orphans else "ALERTE",
        "detail": {
            "appels_sans_reference": dangling,
            "references_jamais_citees": orphans,
        },
    })

    # 2. Ancres internes
    used = set(a for a in re.findall(r'href="#([^"]+)"', html) if a)
    ids = set(re.findall(r'\sid="([^"]+)"', html))
    broken = sorted(a for a in used if a not in ids)
    checks.append({
        "controle": "Ancres internes",
        "statut": "OK" if not broken else "ALERTE",
        "detail": {"ancres_cassees": broken},
    })

    # 3. Autonomie du fichier
    ext = []
    for m in re.finditer(r'\ssrc\s*=\s*"(https?://[^"]+)"', html):
        ext.append(m.group(1))
    for m in re.finditer(r'<link\b[^>]*\bhref\s*=\s*"(https?://[^"]+)"', html, re.I):
        if "fonts.g" not in m.group(1):
            ext.append(m.group(1))
    checks.append({
        "controle": "Autonomie du fichier",
        "statut": "OK" if not ext else "ALERTE",
        "detail": {"ressources_externes": ext},
    })

    # 4. PMID present sur chaque reference
    refs = re.findall(r'<li[^>]*\sid="ref\d+"[^>]*>(.*?)</li>', html, re.S)
    sans_pmid = [i + 1 for i, r in enumerate(refs) if "PMID" not in r.upper()]
    checks.append({
        "controle": "PMID present sur chaque reference",
        "statut": ("INFO" if not refs else ("OK" if not sans_pmid else "ALERTE")),
        "detail": {"nombre_references": len(refs), "references_sans_pmid": sans_pmid},
    })

    # 5. Declaration de sponsoring (mode sponsorise)
    if mode == "sponsorise":
        bandeau = "sponsoris" in html.lower()
        encadre = "sponsor-box" in html or "propos de ce contenu" in html.lower()
        checks.append({
            "controle": "Declaration de sponsoring",
            "statut": "OK" if bandeau and encadre else "ALERTE",
            "detail": {"mention_sponsorise": bandeau, "encadre_sponsor": encadre},
        })

    alertes = sum(1 for c in checks if c["statut"] == "ALERTE")
    return {
        "mode": mode or "non precise",
        "controles": checks,
        "synthese": {
            "total": len(checks),
            "alertes": alertes,
            "verdict": "A CORRIGER" if alertes else "Controles deterministes OK",
        },
    }


def main():
    ap = argparse.ArgumentParser(description="Audit d'un article — agoralive-article")
    ap.add_argument("input", help="HTML de l'article")
    ap.add_argument("--mode", choices=["conference", "sponsorise"],
                    help="mode de l'article (active le contrôle de sponsoring)")
    args = ap.parse_args()

    with open(args.input, encoding="utf-8") as f:
        html = f.read()

    report = audit(html, args.mode)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    sys.exit(1 if report["synthese"]["alertes"] else 0)


if __name__ == "__main__":
    main()
