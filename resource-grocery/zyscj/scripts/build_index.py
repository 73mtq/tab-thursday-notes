# -*- coding: utf-8 -*-
"""生成 INDEX.md（接在 scripts/head.md 后）与 LINKS.md"""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
BT = chr(96)

CAT_ORDER = [("zy", "关于本站"), ("AI", "AI 人工智能"), ("music", "音乐动听"), ("book", "阅读漫画"),
             ("guide", "各种指南"), ("office", "办公素材"), ("soft", "软件游戏"),
             ("search", "资源搜索"), ("tool", "实用工具"), ("tool/imagetool", "图片工具"),
             ("study", "学习教育"), ("video", "视频直播")]

man = json.load(open(os.path.join(HERE, "_manifest.json"), encoding="utf-8"))
pages = [m for m in man if m.get("file")]
total_links = sum(m["links"] for m in pages)


def catkey(m):
    p = m["path"].strip("/")
    if p in ("", "zy") or p == "zy/about.html":
        return "zy"
    if p.endswith("/"):
        return p.split("/")[-1] if p.count("/") == 1 else p.replace("zy/", "")
    seg = p.split("/")
    if len(seg) > 2 and seg[1] == "tool" and seg[2] == "imagetool":
        return "tool/imagetool"
    return seg[1] if len(seg) > 1 else "zy"


def is_index(m):
    return m["path"].endswith("/") or m["path"] in ("", "/")


def h2text(h):
    h = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", h)
    return h.replace("**", "").strip()


out = []
for ck, cname in CAT_ORDER:
    leaf = [m for m in pages if catkey(m) == ck and not is_index(m) and "about" not in (m.get("file") or "")]
    if not leaf:
        continue
    out.append("### %s（%d 页 · %d 条外链）" % (cname, len(leaf), sum(m["links"] for m in leaf)))
    out.append("")
    for m in sorted(leaf, key=lambda x: -x["links"]):
        line = "- [%s](%s) · **%d 条外链**" % (m["title"], m["file"], m["links"])
        hs = [h2text(h) for h in m.get("h2") or []]
        hs = [h for h in hs if h][:8]
        if hs:
            line += "  \n  小节：" + " · ".join(BT + h + BT for h in hs)
        out.append(line)
    out.append("")

txt = open(os.path.join(HERE, "head.md"), encoding="utf-8").read() + chr(10).join(out)
txt += (chr(10) * 2).join([
    "---", "",
    "## 三、外链总表", "",
    "全部 %d 条外链按页面分组见 [LINKS.md](LINKS.md)（也可直接 grep）。" % total_links, "",
    "---", "",
    "## 四、维护", "",
    "- 重新抓取：" + BT + "python scripts/crawl.py" + BT + "（读 scripts/urls.txt，需能访问 zyscj.com）",
    "- 重建索引：" + BT + "python scripts/build_index.py" + BT,
    "- 站点有新页面时先更新 " + BT + "scripts/urls.txt" + BT + "（源：https://zyscj.com/sitemap.xml）",
    "- " + BT + "scripts/head.md" + BT + " 为手写部分（需求速查表），改完重跑 build 生效",
    ""])
open(os.path.join(ROOT, "INDEX.md"), "w", encoding="utf-8").write(txt)

LINK_RE = re.compile(r"\[([^\]]*)\]\((https?://[^)\s]+)\)|<(https?://[^>\s]+)>")
lines = ["# 全站外链总表", "",
         "> %d 个页面、%d 条外链（按页面分组；正文见 docs/，需求导航见 INDEX.md）" % (len(pages), total_links),
         "> 抓取时间 2026-11-01", ""]
got = 0
for ck, cname in CAT_ORDER:
    group = [m for m in pages if catkey(m) == ck and "about" not in (m.get("file") or "")]
    if not group:
        continue
    lines.append("## " + cname)
    lines.append("")
    for m in sorted(group, key=lambda x: (-x["links"], x["title"])):
        body = open(os.path.join(ROOT, m["file"]), encoding="utf-8").read()
        links, seen = [], set()
        for mm in LINK_RE.finditer(body):
            name = (mm.group(1) or "").replace("|", "/").strip()
            url = mm.group(2) or mm.group(3)
            if "zyscj.com" in url or url in seen:
                continue
            seen.add(url)
            links.append((name or url, url))
        if not links:
            continue
        got += len(links)
        lines.append("### %s · %d 条" % (m["title"], len(links)))
        lines.append("<!-- " + m["file"] + " -->")
        lines.append("")
        for name, url in links:
            lines.append("- [%s](%s)" % (name, url))
        lines.append("")
open(os.path.join(ROOT, "LINKS.md"), "w", encoding="utf-8").write(chr(10).join(lines))
print("INDEX chars=%d | LINKS=%d | manifest=%d" % (len(txt), got, total_links))
