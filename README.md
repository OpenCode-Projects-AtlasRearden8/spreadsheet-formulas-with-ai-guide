# Spreadsheet Formulas, With a Friend

A beginner manual on using AI to learn spreadsheet formulas — written like
a friend would explain it: plain English, step by step, never
condescending. You describe what you want in a chat window; the manual
teaches you to read, check, and fix what comes back.

**Covers:** describing needs in plain English · reading and fixing formulas ·
VLOOKUP · SUMIF / COUNTIF / SUMIFS · dates · pivot tables without panic ·
cleaning messy columns · asking good follow-up questions.

**What you need:** Excel, Google Sheets, or LibreOffice Calc, plus a free AI
chat window. No cloud services beyond the chat, no installs, no API keys,
no coding.

Companion guide: **Spreadsheet Comfort Guide** (getting comfortable with the
spreadsheet interface itself). Formulas-with-a-friend is the natural next
step after interface-comfort.

## Layout

```
docs/            the manual (markdown, reads from cover to cover)
  index.md           welcome, who it's for, the sample story
  01-… 09-…          nine chapters (one per topic, in reading order)
examples/        tiny fictional dataset used by every chapter
  orders.csv         12 candle-shop orders (January 2026)
  catalog.csv        4 products → prices (for the VLOOKUP chapter)
  messy_names.csv    messy names (for the cleaning chapter)
tests/           pytest suite verifying every number quoted in the manual
scripts/build_site.py   markdown → static HTML site builder
site/            the built static site (open site/index.html)
```

All names, orders, and dates in the examples are fictional — no real
people, no real business data, no personal data anywhere in this project.

## Read or run it

**Read the manual**

- In the repo: open `docs/index.md` and follow chapter links.
- In a browser: open `site/index.html` (already built, self-contained).
- To rebuild the HTML after editing `docs/`:

  ```bash
  python3 scripts/build_site.py
  ```

  (Requires Python 3 and the `markdown` package: `pip install markdown`.)

**Verify the examples**

Every sum, lookup, pivot, and date result quoted in the manual is asserted
by `tests/test_examples.py`, which recomputes them independently from the
CSV files:

```bash
python3 -m pip install pandas pytest   # once
python3 -m pytest tests/ -v            # -> 20 passed
```

If you change `examples/` data, run the tests first — they name exactly
which documented figures must change with the data.

## The idea in one line

Keep a sheet map pinned in your chat, ask in plain English, read the
formula aloud, hand-check one number — repeat. The five habits are on the
closing page of [the cheat sheet](docs/09-cheatsheet.md).

## Credits and license

Book, examples, and site by **Asdale Dynamics, LLC**
([dylanasdale.github.io](https://dylanasdale.github.io)) — beginner-friendly
AI education from the author of *The Massive AI Manual*.

Licensed under the MIT License — see [LICENSE](LICENSE).
