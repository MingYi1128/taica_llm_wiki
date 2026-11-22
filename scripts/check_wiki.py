#!/usr/bin/env python3
"""Stage-1 check (at ingest time): every wiki claim must cite a source [Sx]
and carry a verbatim quote that really appears in wiki/raw/Sx_*.
Also checks frontmatter sources and that every page is listed in index.md.
Usage: python3 scripts/check_wiki.py
"""
import re, sys, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
raw_dir, pages_dir = root / "wiki/raw", root / "wiki/pages"

def norm(s):
    s = s.replace("⁡", "").replace("−", "-")
    return re.sub(r"\s+", " ", s).strip()

raw = {}
for f in raw_dir.iterdir():
    m = re.match(r"(S\d+)_", f.name)
    if m: raw[m.group(1)] = norm(f.read_text(encoding="utf-8"))

errs, n_claims = [], 0
index = (root / "wiki/index.md").read_text(encoding="utf-8") if (root / "wiki/index.md").exists() else ""
for p in sorted(pages_dir.glob("*.md")):
    text = p.read_text(encoding="utf-8")
    fm = re.search(r"^sources: \[(.*?)\]", text, re.M)
    declared = set(re.findall(r"S\d+", fm.group(1))) if fm else set()
    if not declared: errs.append(f"{p.name}: no sources in frontmatter")
    if f"pages/{p.name}" not in index: errs.append(f"{p.name}: not listed in index.md")
    for ln, line in enumerate(text.splitlines(), 1):
        if not line.startswith("- "): continue
        cites = re.findall(r"\[(S\d+)\]", line)
        q = re.search(r'> "(.*)"\s*$', line)
        if not cites and not q: continue          # plain note, not a factual claim
        n_claims += 1
        if not cites: errs.append(f"{p.name}:{ln}: quote without [Sx]"); continue
        if not q: errs.append(f"{p.name}:{ln}: cites {cites} but no verbatim quote"); continue
        for c in cites:
            if c not in raw: errs.append(f"{p.name}:{ln}: unknown source {c}")
            elif c not in declared: errs.append(f"{p.name}:{ln}: {c} not in frontmatter sources")
            elif norm(q.group(1)) not in raw[c]:
                errs.append(f"{p.name}:{ln}: quote NOT found in {c}: {q.group(1)[:50]}...")
print("\n".join(errs) or f"OK: {n_claims} claims, all quotes found in raw sources")
sys.exit(1 if errs else 0)
