# Chapter 3 · VLOOKUP, Without the Fear

*VLOOKUP has a reputation. It's the formula with its own fan club and its
own anxiety support group. Here's the secret: it's just "look up one thing
in a table, and bring back something next to it." You do this every time
you search your contacts for a name and read off the phone number.*

## The job, in plain English

June's order sheet (`examples/orders.csv`) lists products by name, and her
price list lives in a second sheet (`examples/catalog.csv`):

| | A | B | C |
| --- | --- | --- | --- |
| **1** | Product | UnitPrice | Category |
| **2** | Candle Trio Gift Box | 42.00 | Gift Sets |
| **3** | Soy Wax Refill Kit | 18.50 | Refills |
| **4** | Beeswax Pillars | 24.00 | Candles |
| **5** | Tea Light Sampler | 12.00 | Candles |

The classic everyday need: *"In my order sheet, for each product, look up
its current catalog price next to it, so I can check the order sheet's
prices against the master list."*

That's VLOOKUP's entire job: **V = vertical** (it searches down a column),
**lookup** (it finds your value, then brings back a neighbor).

## Ask the AI with your two-sheet map

```
I have two sheets.

Orders sheet: headers in row 1, data in rows 2–13.
  A = OrderID, B = Date, C = Customer, D = Product, E = Qty,
  F = UnitPrice, G = Category, H = Region

Catalog sheet: headers in row 1, data in rows 2–5.
  A = Product, B = UnitPrice

In Orders, column J, look up each product's UnitPrice from the
Catalog sheet (match on Product name). I'm using Google Sheets.
Give me the formula for J2 and tell me if I need to fill it down.
```

What comes back:

```
J2:  =VLOOKUP(D2, Catalog!$A$2:$B$5, 2, FALSE)
```

Fill it down J3…J13 and every order row now shows its catalog price.

## Reading it aloud — and the two scary numbers

*=VLOOKUP(D2, Catalog!$A$2:$B$5, 2, FALSE)*:

1. Take the product name in **D2**.
2. Search column A of the **Catalog** sheet, rows 2–5 (the `$` pins the
   range so it doesn't shift when you fill down — see [Chapter 2](02-reading-and-fixing-formulas.md)).
3. When you find it, come back with the value from the **2nd** column of
   that range (A is 1st, B is 2nd — so this is the UnitPrice).
4. `FALSE` means **exact match only.**

Two things to memorize — and this is the whole of VLOOKUP's hard part:

- **The `2`** is a *column number within the range you gave it*, not
  spreadsheet column B. If your range were `A:C`, the `2` would still be
  "the second column of the range," which would be column B.
- **The `FALSE`** insists on an exact match. Leave it off (or say `TRUE`)
  and the function happily hands you the *nearest wrong answer*. Your AI
  writing `FALSE` for you is a small kindness.

## Verify one by hand

Order **1008** is Omar Haddad, Beeswax Pillars. J column lookup for that
row should read **24.00** — exactly the Beeswax price from the catalog.
Check one cell against the price list with your eyes and you now trust the
other eleven.

## When VLOOKUP gives you `#N/A`

`#N/A` after a lookup isn't a scolding. It's the most polite error in
spreadsheet land: *"I looked; I found nothing."* (See the glossary in
[Chapter 2](02-reading-and-fixing-formulas.md).) In practice it almost
always means one of:

| Cause | Example | What to do |
| --- | --- | --- |
| Spelling/spacing mismatch | Order says `Beeswax Pillars ` (trailing space), catalog says `Beeswax Pillars` | Clean the column — [Chapter 7](07-cleaning-messy-columns.md) |
| It's genuinely absent | Order sheet contains "Wick Trimmer Set" but catalog doesn't | Add it to the catalog, or accept and flag the row |
| Wrong first column | Catalog's lookup column is actually B | Point the formula at the true leftmost column |

And this is where AI shines — a typical honest exchange goes:

> **You:** My J column gets `#N/A` in some rows with this formula:
> `=VLOOKUP(D2, Catalog!$A$2:$B$5, 2, FALSE)`. D13 is `Tea Light Sampler`
> and the catalog definitely has it. Why only some rows?
>
> **AI:** If it's only *some* rows, the value itself exists — those
> lookup cells probably have invisible differences: extra spaces, or the
> text sitting in the catalog with different capitalization. In a blank
> cell, try `=D2=Catalog!A2` style checks for two of the failing pairs…
> actually, simpler: run `=LEN(D13)` on the failing cell and tell me the
> number. If it's longer than `Tea Light Sampler`, we'll count the
> suspects.

> **You:** LEN says 19.
>
> **AI:** `Tea Light Sampler` is 17 characters. Two extra ones —
> almost certainly leading or trailing spaces. Let's clean the column;
> want a formula for K2 like `=TRIM(D2)` to fill down, or are you up for
> fixing it in place?

(That cleanup is exactly [Chapter 7](07-cleaning-messy-columns.md).)

> **The #N/A with eyes.** If you'd rather see friendly text than `#N/A`,
> ask the AI: *"wrap it so an unmatched lookup shows 'not in catalog'
> instead of #N/A."* You'll get an IFERROR wrapper:
> `=IFERROR(VLOOKUP(D2, Catalog!$A$2:$B$5, 2, FALSE), "not in catalog")`.
> Same logic, kinder face.

## Sidebar: XLOOKUP, the younger sibling

If you're on recent Excel or Google Sheets, you may also meet
`XLOOKUP`, which does the same job with clearer arguments (lookup range,
return range, no "2nd column" counting). The AI can give you either one —
and VLOOKUP remains worth learning because *half the spreadsheets on Earth*
use it. Try asking the AI for both versions of this formula and see them
side by side; it's a genuinely instructive five minutes.

Next: [Chapter 4](04-sumif-and-countif.md) — SUMIF and COUNTIF, the pair
you'll reach for most often.
