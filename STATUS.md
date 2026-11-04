# STATUS

Date: 2026-11-03
Project: Spreadsheet Formulas, With a Friend — a beginner manual on using AI
to learn spreadsheet formulas, by Asdale Dynamics, LLC.

## What was built

- **`docs/` — the manual (markdown, 10 files).** `index.md` + 9 chapters:
  plain-English prompting, reading/fixing formulas, VLOOKUP, SUMIF/COUNTIF/
  SUMIFS, dates, pivot tables, cleaning messy columns, follow-up
  questions, and a closing prompt-patterns cheat sheet. Warm tone, one
  continuous fictional example (a 12-order candle-shop dataset), hand
  checks throughout. Companion note to *Spreadsheet Comfort Guide*
  included on the welcome page.
- **`examples/` — the tested dataset.** `orders.csv` (12 orders with date,
  customer, product, qty, price, category, region), `catalog.csv`
  (VLOOKUP table), `messy_names.csv` (cleaning specimen). All names and
  orders fictional; no personal data.
- **`tests/test_examples.py` — 20 pytest tests** that recompute, from the
  CSV files, every number the manual quotes (grand total 584.00, SUMIF
  Gift Sets 294.00, VLOOKUP Beeswax 24.00, date-window SUMIFS 253.00,
  category/region pivots, the 20-day date math, the 6-unique-names
  cleaning result, etc.) and confirm the docs actually contain those
  figures — so the book and the data can't drift apart silently.
- **`scripts/build_site.py` + `site/` — a self-contained static HTML
  site.** One page per chapter plus a landing page, shared stylesheet,
  chapter nav and prev/next paging, wikified internal `.md → .html`
  links, no external assets, no tracking. Builds offline from `docs/` in
  one command. Also emits `site/chapters.json`.
- **`README.md` + `LICENSE`** (MIT, copyright (c) 2026 Asdale Dynamics,
  LLC; credit in README as required).

## How to run it

```bash
# read the manual
open site/index.html                      # already built
# or rebuild the site after editing docs/
python3 scripts/build_site.py             # needs: pip install markdown

# verify the examples
python3 -m pytest tests/ -v               # needs: pip install pandas pytest
```

Verified with Python 3.13.5, `markdown` 3.11.2, pandas 3.0.6, pytest 9.1.1.

## Verification results

- `python3 -m pytest tests/ -q` → **20 passed** (deterministic; no skips).
- `python3 scripts/build_site.py` → builds 10 chapter pages +
  `style.css` + `chapters.json` cleanly (fresh `rm -rf site` rebuild).
- Site link check: every internal `<a href>` resolves to an existing
  page; no unconverted markdown leaks; credits and the tested numbers
  (584.00, 294.00, 24.00, …) present in the rendered HTML.
- Docs lint test passes: no stray non-ASCII glitch text or garbled
  strings in any chapter.
- Git: initialized locally; single plain commit containing all files;
  nothing pushed, no remote.

## Known gaps / honest limits

- **All formula results are verified in Python, not by hands-on runs of
  Excel/Google Sheets/LibreOffice.** The formulas shown are standard
  and the translations are careful, but a quick open-and-check in your
  own spreadsheet app is still worthwhile (the manual teaches exactly
  that habit, so it fits).
- Site is intentionally plain offline HTML — no search, no dark mode,
  no print stylesheet tuned beyond defaults.
- LibreOffice Calc gets short mentions rather than full click-paths in
  the pivot chapter.
- No episode PDFs/epub of the manual (markdown and HTML only).
- The dataset is intentionally tiny (12 rows); it demonstrates every
  formula but not performance concerns at scale.
