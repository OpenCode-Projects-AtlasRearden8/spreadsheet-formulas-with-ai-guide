# Chapter 4 · SUMIF and COUNTIF

*SUM adds everything. SUMIF adds the ones you want. COUNTIF counts the
ones you want. That's the entire difference, and it's why these two
functions will quietly become the ones you reach for most.*

## The everyday question

Looking at June's January orders again: not just **"how much revenue?"**
(chapter 1 answered that, **584.00**) but things like:

- *How much came from Gift Sets?* (a single line — the question every
  small business asks when restocking)
- *How many orders were candles?*
- *How much revenue from the Midwest?*

Notice each question has the same skeleton: **add/count *something*, but
only where *some condition* holds.** SUMIF and COUNTIF are built for
exactly that shape.

## Asking the AI, with the sheet map

```
My sheet has headers in row 1 and data in rows 2–13.
A = OrderID, B = Date, C = Customer, D = Product, E = Qty,
F = UnitPrice, G = Category, H = Region
I = Line Total (=E*F, filled down)

Give me three formulas:
1. Total line-total revenue where Category is "Gift Sets"
2. Count of orders where Category is "Candles"
3. Total line-total revenue where Region is "Midwest"
Put each in a separate empty cell in row 16, like 16A/16B/16C labels
described to me. I'm using Google Sheets.
```

What comes back:

```
=SUMIF(G2:G13, "Gift Sets", I2:I13)      → the Gift Sets revenue
=COUNTIF(G2:G13, "Candles")              → how many candle orders
=SUMIF(H2:H13, "Midwest", I2:I13)        → the Midwest revenue
```

And the expected answers (which our project's test suite also computes
independently):

| Formula | Result |
| --- | --- |
| SUMIF Gift Sets | **294.00** (orders 84.00 + 42.00 + 42.00 + 126.00) |
| COUNTIF Candles | **5** |
| SUMIF Midwest | **193.00** |

## Reading one aloud

`=SUMIF(G2:G13, "Gift Sets", I2:I13)`, translated:

1. Walk down G2:G13 (the Category column)…
2. …stopping where the cell says exactly `Gift Sets`…
3. …and when you find one, add that row's value from I2:I13.

The shape is always the same:

```
=SUMIF( <range to test>, <test>, <range to add> )
=COUNTIF( <range to test>, <test> )
```

`COUNTIF` has no third argument — counting doesn't need an "add" range.

## The one pitfall worth knowing: exactly what "matches"

`SUMIF`/`COUNTIF` match on the *exact text*, ignoring capitalization but
**not** ignoring extra spaces. So `Gift Sets ` (trailing space) is *not*
`Gift Sets`, and `gift sets` *is* `Gift Sets`. Chapter 2 met this gremlin;
[Chapter 7](07-cleaning-messy-columns.md) evicts it for good.

If a SUMIF returns 0 when you "know" it shouldn't, tell the AI exactly
that (Chapter 2's fixing routine), and it'll likely ask to see the exact
text in one of the tested cells. Often it's a space in hiding.

## Two conditions at once: SUMIFS / COUNTIFS

"Yes, but Gift Sets **and** the West region" — that's `SUMIFS` (with an
S). The argument order flips (the *sum range* comes first):

```
=SUMIFS(I2:I13, G2:G13, "Gift Sets", H2:H13, "West")
```

Read aloud: *"From the line totals, add rows where Category is Gift Sets
**and** Region is West."* That's order 1010, worth **126.00**. The S
versions take condition pairs like a list of rules: range/what,
range2/what2, and so on.

> **Sanity-check it:** our test suite computes this same SUMIFS and
> confirms 126.00 exactly. When your sheet says 126.00 too, you've
> understood it.

## One more useful shape: cells whose totals you want *for every* value

Later you'll want not just Gift Sets but **every category at once**, each
with its total next to it. Two options, both worth knowing:

1. **One SUMIF per label.** In a small block, type each category
   (Candles, Gift Sets, Refills), and next to each one the AI's formula
   pointing at its row. Yes, three explicit rows, three formulas (or a
   single filled-down one with a `$` range and a reference to the label
   cell).
2. **A pivot table.** Which is literally purpose-built for exactly this
   shape of question, and is [Chapter 6](06-pivot-tables.md).

You'll meet the category revenue table in full (Candles **216.00**, Gift
Sets **294.00**, Refills **74.00**) in Chapter 6.

Next: [Chapter 5](05-dates.md) — dates without dread.
