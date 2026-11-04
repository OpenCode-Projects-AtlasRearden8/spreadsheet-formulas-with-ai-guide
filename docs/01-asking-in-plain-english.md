# Chapter 1 · Asking in Plain English

*You already know how to do this. Not with spreadsheets — with people.
"You know how I keep losing my keys? Help me find a way to always know
where they are." That's describing a problem in plain English, and it's
exactly how you talk to AI about formulas.*

The single biggest misconception beginners carry is that they need to learn
"a language" — formulas, functions, that sideways mountain `=C2+B2` —
before they're allowed to ask for help. In 2026, you don't. The AI writes
the formula. Your job is to *describe the need*, then *read and check* what
comes back.

## What a "formula request" for a human sounds like

Imagine June's candle spreadsheet from [the intro](index.md). You want to
know how much money January brought in. What do you tell a helpful human?
Probably:

> "Add up the money from all 12 orders — quantity times unit price for each
> row, and then total all of those."

Notice what's in that sentence:

- **The goal** (total money from January)
- **The math rules** (quantity × unit price per row, then sum)
- **The scope** (all 12 orders)

A good AI prompt is basically that sentence, plus one more thing: **a map
of your sheet.**

## Step 1: Give the AI a map of your sheet

The AI can't see your spreadsheet (unless you paste a screenshot or upload a
file). So it doesn't know whether "Price" is in column F or Q, or whether
the data starts in row 1 or row 500. Fix this by describing your sheet in
one compact block, like this:

> My sheet has headers in row 1 and data in rows 2–13.
> Columns:
> A = OrderID, B = Date, C = Customer, D = Product,
> E = Qty, F = UnitPrice, G = Category, H = Region.

Paste that at the top of your chat, keep it pinned while you work, and
**every formula the AI writes for the rest of the session will line up with
your real columns.** Later chapters call this the *sheet map*.

## Step 2: State the want in plain English

Now finish your request:

> My sheet has headers in row 1 and data in rows 2–13.
> Columns: A = OrderID, B = Date, C = Customer, D = Product,
> E = Qty, F = UnitPrice, G = Category, H = Region.
>
> In column I, I want each order's line total (Qty × UnitPrice).
> Below the data, I want the total of all line totals.

Sit with this for a second, because it's the whole book in miniature. You
did not write `=E2*F2`. You described a *job*, the way you'd ask a coworker
sitting next to you.

**What comes back** should look like this (column I, next to your data):

```
I2:  =E2*F2
```

…filled down through I13, and then, whichever empty cell you asked for:

```
I15: =SUM(I2:I13)
```

Type those in (or let the AI's click-by-click instructions walk you), and
you'll see **584.00** — every dollar and cent January earned, 12 orders
added up.

The test suite that ships with this project checks that number by
re-adding the data from scratch; see `tests/test_examples.py` if you're
curious how a book *knows* its examples are right.

## The prompt template worth memorizing

You can copy this one. It has four parts, and they never change:

> I have a spreadsheet with [what it is].
> [Sheet map: headers in row ?, data rows ?–?, column letters = names.]
> I want [the goal, in your own words].
> Please give me the formula to put in [where], and tell me if I need to
> fill it down or adjust any cell references. Explain each part briefly.

Four parts: *context, map, want, deliverables.* You'll see variations all
through this manual, but the bones are always those four.

## Weak prompt, strong prompt

Compare:

| Weak | Strong | Why |
| --- | --- | --- |
| "Make a formula." | "Add Qty × UnitPrice in column I for rows 2–13." | The AI can't read minds; columns and rows matter. |
| "Do a VLOOKUP" | "Look up each product's price from my catalog sheet and put it in column J." | Names the data to look up *and* where to put it. |
| "Fix this: =SUMIF(...)" | "This =SUMIF was supposed to be 294.00 but I get 0. My sheet map is [paste]. What's wrong?" | Gives intent + expected result + map. Chapter 2 lives here. |

The strong column isn't "formal." It's just *the details a helpful human
would need.* If you'd hate to ask a coworker "do the thing," don't do it to
your AI either.

## Quick note: Excel, Sheets, or LibreOffice?

Formulas are nearly identical in Excel, Google Sheets, and LibreOffice Calc,
and our examples all work in all three. Where they *do* differ (mostly
cross-sheet references and a few newer functions like `XLOOKUP`), the
chapter will flag it in a small note. If your AI knows which program you're
using, mention it in the prompt — "I'm using Google Sheets" — because that
lets it pick the right syntax for you.

## Your first worked homework (optional, low stakes)

Open `examples/orders.csv` and try, without looking ahead:

1. Ask your AI (with the sheet map) for a formula in column I for line
   totals. Check two rows by hand: row for OrderID **1010** should be
   3 × 42.00 = **126.00**, and OrderID **1002** should be 1 × 18.50.
2. Ask for the grand total in an empty cell. It should be **584.00**.
3. If either number came back wrong, tell the AI exactly that: *"I got
   ___ but I expected ___ using manual math. Here's my sheet map: …"*

If all three went smoothly, you've already done the core loop of this
entire book. On to [Chapter 2](02-reading-and-fixing-formulas.md) — reading
what the AI wrote, out loud.
