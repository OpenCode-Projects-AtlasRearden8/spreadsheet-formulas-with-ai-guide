# Chapter 9 · Prompt Patterns Cheat Sheet

*A one-pager to keep open in a second window (or print). Same 12-row
example data all book long: `examples/orders.csv`.*

## The master template

> I have a spreadsheet with [what it is].
> [Sheet map: headers in row ?, data in rows ?–?, columns = names.]
> I want to [the goal, in your own words].
> Please give me [the formula / the click path], where to put it, and a
> short plain-English explanation of each part. I'm using
> [Excel / Google Sheets / LibreOffice Calc].

## Sheet map to copy once per session

```
My sheet has headers in row 1 and data in rows 2–13.
A = OrderID, B = Date, C = Customer, D = Product, E = Qty,
F = UnitPrice, G = Category, H = Region
(I = Line Total = E*F, filled down)
```

## Chapter 1 — plain-English requests

- "Add Qty × UnitPrice per row, then total all rows." → `=E2*F2`, `=SUM(I2:I13)` → **584.00**
- Weak ask → strong ask: name the **columns, rows, and destination**.

## Chapter 2 — reading & fixing

- Read formula aloud: `=FUNCTION(argument, argument)`.
- `$A$2:$B$5` = "pin this exact range, don't shift on fill-down."
- Fixing routine: **intent → reality (exact error/number) → sheet map →
  diagnosis → hand-check.**
- Error glossary: `#NAME?` typo · `#N/A` not found · `#REF!` pointed at
  deleted cell · `#VALUE!` math on a word · `#DIV/0!` divided by zero.

## Chapter 3 — VLOOKUP

- `=VLOOKUP(D2, Catalog!$A$2:$B$5, 2, FALSE)` → Beeswax Pillars → **24.00**
- The `2` counts columns **inside the range**; `FALSE` = exact match only.
- `#N/A` on SOME rows → invisible extra spaces (Chapter 7).
- Kinder face: `=IFERROR(VLOOKUP(...), "not in catalog")`.

## Chapter 4 — SUMIF / COUNTIF / SUMIFS

- `=SUMIF(G2:G13,"Gift Sets",I2:I13)` → **294.00**
- `=COUNTIF(G2:G13,"Candles")` → **5**
- `=SUMIF(H2:H13,"Midwest",I2:I13)` → **193.00**
- `=SUMIFS(I2:I13,G2:G13,"Gift Sets",H2:H13,"West")` → **126.00**
- Matching is case-insensitive but space-sensitive.

## Chapter 5 — dates

```
=B2+20                      → 2026-01-25
=DAYS(B13,B2)               → 20
=EOMONTH(B2,0)              → 2026-01-31
=TEXT(B2,"mmmm yyyy")       → "January 2026"
=ISNUMBER(B2)               → TRUE only if B2 is a real date
=SUMIFS(I2:I13, B2:B13, ">="&DATE(2026,1,11), B2:B13, "<="&DATE(2026,1,20))
                            → orders Jan 11–20 → 253.00 (6 orders)
```

## Chapter 6 — pivot tables

- Select **A1:H13** → Insert → Pivot table → New sheet.
- **Rows** = Category · **Values** = Line Total, SUM → Candles 216.00 ·
  Gift Sets 294.00 · Refills 74.00. (By region: Midwest 193 · Northeast
  79 · South 114 · West 198.)
- Pivot doesn't touch your data; refresh after edits; grand total
  cross-checks `=SUM(I2:I13)` = 584.00.

## Chapter 7 — cleaning

- `=PROPER(TRIM(A2))` — the 90% cleanup, filled down.
- `=IF(COUNTIF($B$2:B2,B2)>1,"dupe","first")` — flag dupes, don't delete.
- `=A2&" "&B2` — glue first + last name. (Watch the space between quotes.)
- Duplicate → clean the copy → check → replace.

## Chapter 8 — follow-up prompts

- "I got X, expected Y by hand. Sheet map: …"
- "Explain part by part, then tell me one manual check."
- "Show which specific rows you summed."
- "Compute it a different way so I can cross-check."
- "Let's start over — I'll describe everything again."
- "Can you slow down?" (always allowed)

## The five habits (when all else fades)

1. Map the sheet before asking.
2. Read formulas aloud; `$` means pinned.
3. Hand-check one number per formula.
4. Clean a copy, never the original.
5. Follow up — drafts become good formulas in the second message.

---

*Manual by Asdale Dynamics, LLC — [dylanasdale.github.io](https://dylanasdale.github.io).
Companion guide: **Spreadsheet Comfort Guide** (interface comfort), by the
same friendly publisher. Tested examples: `examples/` + `tests/`, verified
per `STATUS.md`.*
