# Chapter 6 · Pivot Tables Without the Panic

*Pivot tables have a reputation as Expert Territory. They aren't. A pivot
table is a machine that answers "group by X, total Y" — the same question
you already solved with SUMIF in [Chapter 4](04-sumif-and-countif.md), just
for every group at once, and without writing any formulas.*

## The job, in one breath

June wants: **"How much revenue did each category bring in?"** Here is the
answer, as a pivot table:

| Category | Sum of Line Total |
| --- | --- |
| Candles | 216.00 |
| Gift Sets | 294.00 |
| Refills | 74.00 |

And when the same question gets asked with a different lens — *"what about
by region?"* — the click-path is identical:

| Region | Sum of Line Total |
| --- | --- |
| Midwest | 193.00 |
| Northeast | 79.00 |
| South | 114.00 |
| West | 198.00 |

Two details worth pausing on, both reassuring:

- Every table here sums to **584.00** — the grand total from
  [Chapter 1](01-asking-in-plain-english.md). When different views of the
  data agree like that, you've almost certainly set everything up right.
- Nothing about making them required you to type a formula. The pivot
  table is the *viewing* tool; SUMIF is the *building* tool. Both live in
  your toolbox now.

## The four boxes, in plain English

Google Sheets: select your data (A1:H13), then **Insert → Pivot table**
→ *New sheet* — and you meet four little boxes:

| Box | Meaning |
| --- | --- |
| **Rows** | "Group by…" — one row per distinct value (each Category, each Customer, …) |
| **Columns** | "…and split across…" — an optional second lens; leave it empty today |
| **Values** | "…and show me…" — the thing that gets summed, counted, or averaged |
| **Filters** | "…but only for rows where…" — optional spotlight |

Four boxes. Plain English names. For June's category revenue, fill in
exactly two of them:

1. **Rows:** `Category`
2. **Values:** `Line Total`, summarized as **SUM**

That's the entire table. (Excel calls the boxes by the same names in the
"PivotTable Fields" pane; LibreOffice Calc calls the feature DataPilot and
hides the same four fields behind friendlier labels once you know to find
**Insert → Pivot Table**.)

The written guide you're reading now is the slow, careful version —
the *click-by-click* version is genuinely better taught beside your AI,
and the prompt for that is one Chapter 1 shape you already know:

```
I'm about to make my first pivot table in Google Sheets. My data is in
A1:H13; Category is column G, Line Total is column I (=E*F, filled all
the way down). I want: Rows = Category, Values = Sum of Line Total.
Confirm that's the right setup, walk me through the click path one
step at a time, and warn me about any common beginner pitfalls before
I click anything.
```

Two honest answers you're likely to get, so you're not surprised:

1. **Your Line Total column must be filled all the way down.** A blank at
   the bottom silently shortens the sums; a pivot "finding" your last row
   is a classic reason for a total that looks 80% right.
2. **Start your selection at the header row (A1),** not the data rows, so
   the pivot finds column labels and shows friendly names instead of
   "Column G."

## Why this doesn't require panic

Pivot tables *sound* like they rewrite your data. They really, truly
don't. A few facts, so you can relax:

- The output is a summary that lives on **its own sheet** (or a corner of
  this one). Your `orders` data is untouched.
- Deleting costs nothing (right-click → Delete → whole sheet, or Ctrl+Z).
- Updating costs nothing except a *refresh* when the data changes (Sheets
  revises pivots on reload; Excel has an obvious "Refresh" button).
- They coexist peacefully with formulas — `SUMIF` calculations on one
  sheet, a pivot on another, never arguing.

This satisfies our rule from [Chapter 0](index.md): **keep a way to check
by hand.** Your hand-check here is beautiful: the pivot's grand total
should equal `=SUM(I2:I13)` from your orders sheet — **584.00** each.
You get to *watch* two independent tools agree, which is worth more than
any tutorial.

## When to pivot, when to SUMIF

| You want… | Best tool |
| --- | --- |
| One group's total ("Gift Sets only") | `SUMIF` |
| Every group's totals, stacked | **Pivot table** |
| Counts across several cut-lines ("orders → count per region and per category") | **Pivot table** |
| A number to feed the *next* formula (e.g., "Gift Sets share of total") | `SUMIF`, plainly in a cell |

That last row is quiet, practical wisdom. Pivots are great to *read* but
awkward to build on top of. `SUMIF` is less impressive to look at, but its
answer sits in a nice ordinary cell you can reference freely. Chapter 4 got
you both, which is exactly why it came first.

Onward to [Chapter 7](07-cleaning-messy-columns.md), where the data gets
messy in all the ways real data does.
