#!/usr/bin/env python3
"""Refresh links.json from the official Tab Thursday recap pages.

The generated file is committed to the repository so that build_site.py stays
fully offline. Run this only when a new issue is published or official links
change:

    python refresh_links.py && python build_site.py
"""

from __future__ import annotations

import html
import json
import re
from pathlib import Path
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "links.json"
PAGES = {
    "001": "https://tabthursday.com/001",
    "002": "https://tabthursday.com/002",
}
UA = "Mozilla/5.0 (compatible; tab-thursday-notes-link-builder/1.0)"

A_RE = re.compile(r'<a\s+href="([^"]+)"[^>]*>(.*?)</a>', re.S | re.I)
TAG_RE = re.compile(r"<[^>]+>")


def clean(text: str) -> str:
    return html.unescape(TAG_RE.sub("", text)).strip()


def normalize(url: str) -> str:
    url = url.strip().rstrip("/")
    url = re.sub(r"^https?://", "", url, flags=re.I)
    url = re.sub(r"^www\.", "", url, flags=re.I)
    return url.lower()


def is_domain_label(label: str) -> bool:
    return bool(
        re.fullmatch(r"[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/[^\s]*)?", label.strip())
    )


def dedupe(pairs) -> list[dict]:
    seen: set[str] = set()
    out = []
    for url, label in pairs:
        label = clean(label)
        if not label or not url.startswith(("http://", "https://")):
            continue
        n = normalize(url)
        if n in seen:
            continue
        host = n.split("/")[0]
        if is_domain_label(label) and any(s.split("/")[0] == host for s in seen):
            continue
        seen.add(n)
        out.append({"label": label, "url": url})
    return out


def fetch(url: str) -> str:
    req = Request(url, headers={"User-Agent": UA})
    with urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


def parse_001(page: str) -> list[dict]:
    """Issue #001 uses <ol><li><strong>name</strong>（homepage）<ul>..."""
    m = re.search(r"<ol>(.*?)</ol>", page, re.S)
    if not m:
        raise RuntimeError("issue 001: <ol> list not found")
    ol = m.group(1)
    chunks = re.split(r"<li>\s*<p>\s*<strong>", ol)[1:]
    result = []
    for chunk in chunks:
        head, _, rest = chunk.partition("</strong>")
        name = clean(head)
        hm = re.match(r"\s*（\s*<a\s+href=\"([^\"]+)\"[^>]*>(.*?)</a>\s*）", rest, re.S)
        homepage = None
        if hm:
            homepage = {"label": clean(hm.group(2)), "url": hm.group(1)}
            rest = rest[hm.end():]
        ul = re.search(r"<ul>(.*?)</ul>", rest, re.S)
        body = ul.group(1) if ul else rest
        links = dedupe(A_RE.findall(body))
        if homepage:
            links = [x for x in links if normalize(x["url"]) != normalize(homepage["url"])]
        result.append({"name": name, "homepage": homepage, "links": links})
    return result


def parse_002(page: str) -> list[dict]:
    """Issue #002 uses <h3>name</h3><p>主页：<a...>...</a></p>..."""
    parts = re.split(r"<h3>(.*?)</h3>", page, flags=re.S)
    result = []
    for i in range(1, len(parts), 2):
        name = clean(parts[i])
        body = parts[i + 1].split("<h2")[0]
        hm = re.search(r"<p>\s*主页：\s*<a\s+href=\"([^\"]+)\"[^>]*>(.*?)</a>\s*</p>", body, re.S)
        homepage = None
        if hm:
            homepage = {"label": clean(hm.group(2)), "url": hm.group(1)}
        links = dedupe(A_RE.findall(body))
        if homepage:
            links = [x for x in links if normalize(x["url"]) != normalize(homepage["url"])]
        result.append({"name": name, "homepage": homepage, "links": links})
    return result


def main() -> None:
    data = {}
    for key, url in PAGES.items():
        page = fetch(url)
        people = parse_001(page) if key == "001" else parse_002(page)
        data[key] = people
        total = sum(len(p["links"]) for p in people)
        homes = sum(1 for p in people if p["homepage"])
        print(
            "issue %s: %d people, %d homepages, %d project/reference links"
            % (key, len(people), homes, total)
        )
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("wrote", OUT.name, OUT.stat().st_size, "bytes")


if __name__ == "__main__":
    main()
