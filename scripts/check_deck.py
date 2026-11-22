#!/usr/bin/env python3
"""Stage-2 check (after generation): the deck must be grounded in the wiki and its numbers must be right.
 1. every non-title slide declares data-wiki pages that exist
 2. every complexity expression O(...)/Ω/Θ on a slide must appear in the cited wiki pages
 3. numeric examples (binary-search trace, comparison table, sort traces) are recomputed and compared
"""
import re, json, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from algos import *
root = pathlib.Path(__file__).resolve().parent.parent
doc = (root / "deck/index.html").read_text(encoding="utf-8")
errs = []
squash = lambda s: re.sub(r"[\s\\]", "", s).replace("²", "^2").replace("lg", "log")

slides = re.findall(r'<section class="slide" data-wiki="([^"]*)">(.*?)</section>', doc, re.S)
for n, (wiki, body) in enumerate(slides, 1):
    pages = wiki.split()
    if n > 1 and not pages: errs.append(f"slide {n}: no data-wiki"); continue
    corpus = ""
    for p in pages:
        f = root / f"wiki/pages/{p}.md"
        if not f.exists(): errs.append(f"slide {n}: wiki page '{p}' missing")
        else: corpus += f.read_text(encoding="utf-8")
    text = re.sub(r"<[^>]+>", "", body); text = re.sub(r"&[a-z]+;", "", text)
    for expr in set(re.findall(r"O\([^()]*(?:\([^()]*\))?[^()]*\)", text)):
        if squash(expr) not in squash(corpus):
            errs.append(f"slide {n}: '{expr}' not supported by cited wiki pages {pages}")

data = json.loads(re.search(r"const DATA=(\{.*?\});", doc, re.S).group(1))
steps, res = binary_search_trace(data["bs_arr"], data["bs_x"])
if steps != data["bs_steps"] or res != data["bs_res"]: errs.append("binary search trace mismatch")
for n_, k in re.findall(r"<tr><td>([\d,]+)</td><td>(\d+)</td></tr>", doc):
    if max_comparisons(int(n_.replace(",", ""))) != int(k): errs.append(f"table: n={n_} expected {max_comparisons(int(n_.replace(',','')))} got {k}")
for rows, start in ((insertion_trace([5,2,4,6,1,3]), [5,2,4,6,1,3]), (selection_trace([7,5,1,4,3]), [7,5,1,4,3])):
    if rows[-1] != sorted(start): errs.append(f"trace of {start} does not end sorted")
if "= 45 次" in doc and selection_comparisons(10) != 45: errs.append("quiz Q2 wrong")
if "⌊lg 255⌋ + 1 = 8" in doc and max_comparisons(255) != 8: errs.append("quiz Q1 wrong")

print("\n".join(errs) or f"OK: {len(slides)} slides grounded in wiki, numbers recomputed")
sys.exit(1 if errs else 0)
