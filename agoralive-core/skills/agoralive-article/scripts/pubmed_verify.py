#!/usr/bin/env python3
"""
Vérification PubMed — skill agoralive-article.

Deux usages :
  Recherche :  python pubmed_verify.py "remote orthodontic monitoring AI" --max 6
  Vérif PMID : python pubmed_verify.py --pmid 33573897

GARDE-FOU ABSOLU (mode sponsorisé) : aucune référence ne doit être citée sans
avoir été vérifiée ici. Si --pmid ne renvoie rien, la référence n'existe pas :
ne pas la citer, ne jamais fabriquer un PMID plausible.

S'appuie sur les E-utilities publiques de NCBI (esearch + esummary). Aucune
clé API requise pour un usage modéré.
"""
import sys
import json
import argparse
import urllib.parse
import urllib.request

EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"


def _get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "agoralive-article/1.0"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read().decode("utf-8"))


def summary(pmid):
    """Renvoie les métadonnées réelles d'un PMID, ou found=False s'il n'existe pas."""
    pmid = str(pmid).strip()
    url = f"{EUTILS}/esummary.fcgi?db=pubmed&retmode=json&id={pmid}"
    data = _get(url).get("result", {}).get(pmid)
    if not data or "error" in data:
        return {"pmid": pmid, "found": False}
    authors = [a["name"] for a in data.get("authors", []) if a.get("authtype") == "Author"]
    return {
        "pmid": pmid,
        "found": True,
        "title": data.get("title", "").rstrip("."),
        "authors": authors,
        "journal": data.get("source", ""),
        "year": (data.get("pubdate", "") or "")[:4],
        "volume": data.get("volume", ""),
        "issue": data.get("issue", ""),
        "pages": data.get("pages", ""),
        "doi": data.get("elocationid", ""),
        "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
    }


def search(query, max_results):
    q = urllib.parse.quote(query)
    url = f"{EUTILS}/esearch.fcgi?db=pubmed&retmode=json&retmax={max_results}&term={q}"
    ids = _get(url).get("esearchresult", {}).get("idlist", [])
    return [summary(pmid) for pmid in ids]


def main():
    ap = argparse.ArgumentParser(description="Vérification PubMed — agoralive-article")
    ap.add_argument("query", nargs="?", help="requête de recherche PubMed")
    ap.add_argument("--pmid", help="vérifier un PMID précis")
    ap.add_argument("--max", type=int, default=6, help="nombre de résultats (recherche)")
    args = ap.parse_args()

    try:
        if args.pmid:
            res = summary(args.pmid)
            if not res.get("found"):
                print(json.dumps(
                    {"pmid": args.pmid, "found": False,
                     "message": "PMID introuvable — NE PAS citer cette référence."},
                    ensure_ascii=False, indent=2))
                sys.exit(1)
            print(json.dumps(res, ensure_ascii=False, indent=2))
        elif args.query:
            print(json.dumps(search(args.query, args.max), ensure_ascii=False, indent=2))
        else:
            ap.print_help()
            sys.exit(2)
    except Exception as e:
        print(json.dumps(
            {"error": str(e),
             "message": "Échec réseau PubMed — réessayer ; ne jamais inventer de référence."},
            ensure_ascii=False, indent=2))
        sys.exit(1)


if __name__ == "__main__":
    main()
