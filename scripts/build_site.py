#!/usr/bin/env python3
"""Build the static HTML site from the markdown manual in docs/.

Usage:  python3 scripts/build_site.py

Reads every docs/*.md (chapter order = filename order) and writes:
  site/index.html            (landing page, from docs/index.md)
  site/<same-stem>.html      (one page per chapter)
  site/style.css             (single self-contained stylesheet)
  site/chapters.json         (list of chapters, handy for reuse)

No network, no dependencies beyond Python 3 + the `markdown` package.
"""

import json
import re
import sys
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SITE = ROOT / "site"

md_extensions = ["tables", "fenced_code", "smarty", "toc"]

CHAPTER_TITLES = {
    "index": "Welcome",
    "01-asking-in-plain-english": "1 · Asking in Plain English",
    "02-reading-and-fixing-formulas": "2 · Reading and Fixing a Formula",
    "03-vlookup": "3 · VLOOKUP, Without the Fear",
    "04-sumif-and-countif": "4 · SUMIF and COUNTIF",
    "05-dates": "5 · Dates Without Dread",
    "06-pivot-tables": "6 · Pivot Tables Without the Panic",
    "07-cleaning-messy-columns": "7 · Cleaning Messy Columns",
    "08-follow-up-questions": "8 · Asking Follow-Up Questions",
    "09-cheatsheet": "9 · Prompt Patterns Cheat Sheet",
}

STYLE = """\
/* Spreadsheet Formulas, With a Friend — site stylesheet */
:root {
  --ink: #2d2a26;
  --paper: #faf7f2;
  --card: #ffffff;
  --accent: #b45309;
  --accent-soft: #fdf0e0;
  --line: #e7e0d6;
  --muted: #6f6759;
}
* { box-sizing: border-box; }
html { font-size: 17px; }
body {
  margin: 0;
  font-family: Georgia, "Times New Roman", serif;
  color: var(--ink);
  background: var(--paper);
  line-height: 1.65;
}
header.site {
  background: var(--accent);
  color: #fff;
  padding: 0.9rem 1rem;
  text-align: center;
  font-family: "Helvetica Neue", Arial, sans-serif;
}
header.site a.title {
  color: #fff;
  text-decoration: none;
  font-weight: 700;
  font-size: 1.05rem;
  letter-spacing: 0.02em;
}
header.site a.title:hover { text-decoration: underline; }
main {
  max-width: 46rem;
  margin: 2rem auto;
  padding: 0 1.25rem;
}
nav.chapters {
  font-family: "Helvetica Neue", Arial, sans-serif;
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 10px;
  padding: 0.9rem 1.2rem;
  margin-bottom: 1.6rem;
  font-size: 0.88rem;
  line-height: 1.9;
}
nav.chapters strong {
  display: block;
  font-size: 0.78rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--muted);
  margin-bottom: 0.35rem;
}
nav.chapters a { color: var(--ink); text-decoration: none; }
nav.chapters a:hover { color: var(--accent); }
nav.chapters a.here { font-weight: 700; color: var(--accent); }
article {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 10px;
  padding: 2.2rem 2.5rem 1.4rem;
}
h1, h2 { font-family: "Helvetica Neue", Arial, sans-serif; line-height: 1.25; }
h1 { font-size: 1.55rem; margin-top: 0; }
h2 { font-size: 1.2rem; margin-top: 2.2rem; }
h2, h3 { color: #85460a; }
p, li { max-width: 42rem; }
code, pre {
  font-family: "SF Mono", Consolas, Menlo, monospace;
  font-size: 0.85rem;
}
code {
  background: var(--accent-soft);
  border-radius: 4px;
  padding: 0.1em 0.35em;
}
pre {
  background: #332f2a;
  color: #f4ede2;
  border-radius: 8px;
  padding: 0.9rem 1.1rem;
  overflow-x: auto;
  line-height: 1.55;
}
pre code { background: none; color: inherit; padding: 0; }
table {
  border-collapse: collapse;
  margin: 1.2rem 0;
  font-size: 0.92rem;
}
th, td {
  border: 1px solid var(--line);
  padding: 0.45rem 0.7rem;
  text-align: left;
}
th { background: var(--accent-soft); font-family: "Helvetica Neue", Arial, sans-serif; }
blockquote {
  margin: 1.2rem 0;
  padding: 0.65rem 1.1rem;
  border-left: 4px solid var(--accent);
  background: var(--accent-soft);
  border-radius: 0 8px 8px 0;
}
blockquote p { margin: 0.35rem 0; }
hr { border: none; border-top: 1px solid var(--line); margin: 2rem 0; }
footer.pager {
  display: flex;
  justify-content: space-between;
  gap: 1rem;
  font-family: "Helvetica Neue", Arial, sans-serif;
  font-size: 0.9rem;
  margin-top: 1.8rem;
}
footer.pager a {
  color: var(--accent);
  text-decoration: none;
  font-weight: 600;
}
footer.pager a:hover { text-decoration: underline; }
footer.colophon {
  text-align: center;
  color: var(--muted);
  font-size: 0.82rem;
  font-family: "Helvetica Neue", Arial, sans-serif;
  margin: 2.5rem 0 2.2rem;
}
footer.colophon a { color: var(--muted); }
@media (max-width: 620px) {
  article { padding: 1.4rem 1.25rem; }
  h1 { font-size: 1.3rem; }
}
"""


def chapter_nav(stems: list[str], current: str) -> str:
    links = []
    for stem in stems:
        label = CHAPTER_TITLES.get(stem, stem)
        href = "index.html" if stem == "index" else f"{stem}.html"
        css = ' class="here"' if stem == current else ""
        links.append(f'<a{css} href="{href}">{label}</a>')
    body = "<br>".join(links)
    return f'<nav class="chapters"><strong>Chapters</strong>{body}</nav>'


def pager(stems: list[str], current: str) -> str:
    i = stems.index(current)
    left = stems[i - 1] if i > 0 else None
    right = stems[i + 1] if i < len(stems) - 1 else None
    def link(stem: str | None, before: bool) -> str:
        if stem is None:
            return "<span></span>"
        label = CHAPTER_TITLES.get(stem, stem)
        href = "index.html" if stem == "index" else f"{stem}.html"
        arrow = "&#8592; " if before else " &#8594;"
        return f'<a href="{href}">{arrow}{label}</a>'
    return (
        '<footer class="pager">'
        + link(left, True)
        + link(right, False)
        + "</footer>"
    )


def docs_links_to_site(html: str) -> str:
    """Point internal chapter links at the html pages, not the md sources."""
    def swap(m: re.Match) -> str:
        href = m.group(1)
        if href.startswith("http"):
            return m.group(0)
        target = href[:-3]  # strip ".md"
        label = "index.html" if target == "index" else f"{target}.html"
        return f'href="{label}"'
    return re.sub(r'href="([^"]+\.md)"', swap, html)


def render_html(title: str, body_markdown: str, nav: str, pager_html: str) -> str:
    body = docs_links_to_site(
        markdown.markdown(body_markdown, extensions=md_extensions)
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · Spreadsheet Formulas, With a Friend</title>
<meta name="description" content="A beginner manual on learning spreadsheet formulas (VLOOKUP, SUMIF, dates, pivot tables) with an AI chat window. Plain English, tested examples, by Asdale Dynamics, LLC.">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header class="site"><a class="title" href="index.html">
Spreadsheet Formulas, With a Friend &#183; learning spreadsheet formulas with AI
</a></header>
<main>
{nav}
<article>
{body}
</article>
{pager_html}
</main>
<footer class="colophon">
Spreadsheet Formulas, With a Friend &#8212; a beginner manual by
<a href="https://dylanasdale.github.io">Asdale Dynamics, LLC</a>.
Markdown source in <code>docs/</code>; this site rebuilds with
<code>python3 scripts/build_site.py</code>. No data leaves your machine.
</footer>
</body>
</html>
"""


def main() -> int:
    if not DOCS.is_dir():
        print(f"error: {DOCS} not found", file=sys.stderr)
        return 1
    stems = sorted(p.stem for p in DOCS.glob("*.md"))
    if "index" not in stems:
        print("error: docs/index.md is missing", file=sys.stderr)
        return 1
    SITE.mkdir(exist_ok=True)
    (SITE / "style.css").write_text(STYLE, encoding="utf-8")

    for stem in stems:
        src = DOCS / f"{stem}.md"
        text = src.read_text(encoding="utf-8")
        title = CHAPTER_TITLES.get(stem, stem)
        html = render_html(
            title, text, chapter_nav(stems, stem), pager(stems, stem)
        )
        dest = SITE / ("index.html" if stem == "index" else f"{stem}.html")
        dest.write_text(html, encoding="utf-8")
        print(f"built {dest.relative_to(ROOT)}")

    (SITE / "chapters.json").write_text(
        json.dumps(
            [
                {"slug": s, "title": CHAPTER_TITLES.get(s, s),
                 "file": "index.html" if s == "index" else f"{s}.html"}
                for s in stems
            ],
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"built {SITE / 'chapters.json'} ({len(stems)} chapters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
