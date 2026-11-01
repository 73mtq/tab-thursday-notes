# -*- coding: utf-8 -*-
"""抓取 zyscj.com 全站（sitemap 列出的页面），转为 markdown 落地到 docs/"""
import json, os, re, time
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
BASE = "https://zyscj.com"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/131.0 Safari/537.36"}

os.makedirs(DOCS, exist_ok=True)
s = requests.Session()
s.headers.update(UA)

urls = [u.strip() for u in open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "urls.txt"), encoding="utf-8") if u.strip()]
print("urls:", len(urls))

manifest = []
for u in urls:
    path = u[len(BASE):] or "/"
    rel = path.strip("/")
    if rel == "":
        out = os.path.join(DOCS, "index.md")
    elif path.endswith("/"):
        out = os.path.join(DOCS, rel.rstrip("/"), "index.md")
    else:
        out = os.path.join(DOCS, re.sub(r"\.html$", ".md", rel))
    os.makedirs(os.path.dirname(out), exist_ok=True)

    try:
        r = s.get(u, timeout=30)
        r.encoding = "utf-8"
        html = r.text
    except Exception as e:
        print("FAIL", u, e)
        manifest.append({"url": u, "path": rel, "file": None, "title": "", "error": str(e)})
        continue

    soup = BeautifulSoup(html, "lxml")
    h1 = soup.select_one(".vp-page-title h1")
    title = h1.get_text(" ", strip=True) if h1 else (soup.title.get_text(strip=True) if soup.title else rel)
    body = soup.select_one("#markdown-content") or soup.select_one("main")
    sel = body if body else soup
    text = md(str(sel), heading_style="ATX", bullets="-")
    text = re.sub(r"\n{3,}", "\n\n", text).strip()

    heads = re.findall(r"^(#{2,4})\s+(.+)$", text, re.M)
    ext, seen = [], set()
    for a in sel.select("a[href]"):
        href = a.get("href", "")
        name = a.get_text(" ", strip=True)
        if href.startswith("http") and "zyscj.com" not in href and name and href not in seen:
            seen.add(href)
            ext.append({"name": name, "url": href})

    with open(out, "w", encoding="utf-8") as f:
        f.write("# " + title + "\n\n")
        f.write("> 来源：<%s>  ·  抓取时间：2026-11-01  ·  外链 %d 个\n\n" % (u, len(ext)))
        f.write(text + "\n")

    manifest.append({"url": u, "path": path, "file": os.path.relpath(out, ROOT).replace(os.sep, "/"),
                     "title": title, "h2": [h[1] for h in heads if h[0] == "##"],
                     "links": len(ext), "bytes": len(text)})
    print("OK", rel, "|", title, "| links", len(ext))
    time.sleep(0.25)

mpath = os.path.join(ROOT, "scripts", "_manifest.json")
json.dump(manifest, open(mpath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("done", len([m for m in manifest if m.get("file")]))
