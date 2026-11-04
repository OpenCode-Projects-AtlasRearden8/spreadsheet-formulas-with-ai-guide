# Chapter 5 · Dates Without Dread

*If formulas have a bogeyman, it's dates. "1/5/2026" looks like text, but
your spreadsheet secretly treats it as a number — and once you see that,
dates stop being scary and start being useful.*

## The big secret: dates are numbers wearing costumes

In Excel, Google Sheets, and LibreOffice Calc, a date is just a number —
how many days since some long-ago start point — displayed as a date. Try
it if you like: if June's order date cell B2 is a real date, then

```
=B2 + 20
```

gives back **2026-01-25**. Add 20 days and you're twenty days later. That
secret explains almost everything about dates:

- Arithmetic "*just works*" on well-formed date cells (`B3-B2` is days
  between them).
- Sorting by date is really sorting by number.
- "What's wrong with my date formula" is usually "this cell is secretly
  text, not a number."

## Your first useful date formulas

```
=B2 + 30                    → 30 days after Jan 5 → 2026-02-04
=B13 - B2                   → Jan 25 minus Jan 5    → 20 (days)
=DAYS(B13, B2)              → the same 20, spelled out
=EOMONTH(B2, 0)             → the last day of B2's month → 2026-01-31
=TEXT(B2, "mmmm yyyy")     → the wordy label → "January 2026"
=YEAR(B2), =MONTH(B2), =WEEKDAY(B2)
```

Every one of these is verifiable by hand with 12 rows of January data —
that's the point of the small dataset all book long. Ask your AI first
("with my sheet map: B = Date…"), then confirm the result yourself.

## The real-life trap: `1/5/2026` typed into the wrong place

Here's the classic, and it hits nurses' shift logs as hard as candle
orders. Someone types `1/5/2026` in a spreadsheet set to European
international formatting, or a cell was pre-formatted as Text, or the
value came from a cut-and-paste from a website. Same-looking cell, four
possible realities:

- A real date, meaning **January 5, 2026**
- A real date, meaning **May 1, 2026** (column formatted differently)
- The words "1/5/2026" sitting there as text (left-aligned!)
- Empty, with the source typing evicted by auto-correct

Three warnings that catch most cases:

1. **Alignment is the tell.** Real numbers (and real dates) line up
   right; text lines up left in a fresh General-formatted column.
2. **`=B2+1` either works** (real date), **or produces an error or a
   strange number** (text).
3. **`=ISNUMBER(B2)`** returns `TRUE` for a true date, `FALSE` for the
   impostor. This humble check may be the most useful formula in this
   book you've never needed before.

If you find impostor text-dates, don't fix 12 cells by re-typing; ask the
AI ("make these text cells real dates"), which will hand you a `DATEVALUE`
formula or a one-click Data → Split text/column settings approach —
whatever is right for your program.

> **Fictional footnote:** all dates used in this book are from a fictional
> January 2026 dataset in `examples/orders.csv`. No real orders, no real
> people, no personal data.

## SUMIFS with a date window: the useful one

The classic real-life question: *"how much between January 11 and January
20?"* A date range is just two conditions on the same Date column. With
your sheet map and the fix-it-routine from [Chapter 2](02-reading-and-fixing-formulas.md):

```
=SUMIFS(I2:I13, B2:B13, ">="&DATE(2026,1,11), B2:B13, "<="&DATE(2026,1,20))
```

Translation: *add line totals of the rows whose date is on or after
January 11, 2026 **and** on or before January 20, 2026.* That's orders
1004–1009 — six of them — and the answer is **253.00** (a `SUMIFS` our
test suite computes independently, too). The `">="&DATE(...)` sandwich
wall of symbols looks worse than it is: the first piece, `">="&DATE(...)`,
is AI-written for you, and you only need to know that it means "on or
after."

> If this is your first time seeing `DATE(2026,1,11)`: it builds a date
> from your own year, month, day — safer than typing `1/11/2026` into a
> formula, whose meaning can change based on your computer's country
> settings (the very trap from earlier).

## A friendly closing word about this chapter

Dates have a reputation for being *technical*, and this chapter is long —
but here is the entire take-home list:

- a date is a number in disguise,
- `+1` steps a day, subtracting gives a gap in days,
- `ISNUMBER` sniffs impostors,
- `SUMIFS` with two date conditions is how you say "between two dates."

Everything else you look up when you need it, ideally in the chat window,
in plain English — that's the method of this whole book.

Onward to [Chapter 6](06-pivot-tables.md), pivot tables without panic.
