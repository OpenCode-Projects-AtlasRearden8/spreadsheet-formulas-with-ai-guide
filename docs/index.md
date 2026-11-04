# Spreadsheet Formulas, With a Friend: A Beginner's Manual for Learning with AI

Welcome. This manual is for people who look at a spreadsheet the way most of
us look at a tax form: with respect, dread, and a strong desire to be
anywhere else.

The good news: **you do not need to memorize formulas anymore.** You need to
know two things:

1. How to *describe* what you want, in plain English, to a chat AI.
2. How to *read* a formula well enough to check it and fix it.

That's it. That's the whole skill. This guide teaches both, gently, with a
single small example dataset you can follow from the first page to the last.

> **What you need:** a spreadsheet (Excel, Google Sheets, or LibreOffice
> Calc — all work) and a free AI chat window. **No cloud subscriptions, no
> installs, no coding.** Everything in this book happens in two tabs: your
> spreadsheet and your chat.

## Who wrote it, and why

This guide comes from [Asdale Dynamics, LLC](https://dylanasdale.github.io) —
Dylan Asdale, a registered nurse turned AI author. Everything here is
written "like a friend would": plain English, step by step, never
condescending. It's the formula companion to the interface guide,
*Spreadsheet Comfort Guide* — that one teaches you where the buttons are;
this one teaches you to get the spreadsheet to *do math for you*.

## Meet the sample data

Every example in this manual uses the same tiny story: your friend **June
Tanaka** sells handmade candles as a side business, and she has one
spreadsheet of 12 orders from January 2026. (All names and orders are
fictional examples, safe to copy.)

You'll find the files in the `examples/` folder of this project:

| File | What it is | Where it first appears |
| --- | --- | --- |
| `examples/orders.csv` | 12 orders: date, customer, product, quantity, price, category, region | Chapter 1 |
| `examples/catalog.csv` | June's 4 products and their prices | Chapter 3 (VLOOKUP) |
| `examples/messy_names.csv` | A customer list typed by 7 different people | Chapter 7 (cleaning) |

Open `orders.csv` in any spreadsheet program and you'll see:

| | A | B | C | D | E | F | G | H |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **1** | OrderID | Date | Customer | Product | Qty | UnitPrice | Category | Region |
| **2** | 1001 | 2026-01-05 | Maya Chen | Candle Trio Gift Box | 2 | 42.00 | Gift Sets | Midwest |
| **3** | 1002 | 2026-01-07 | Maya Chen | Soy Wax Refill Kit | 1 | 18.50 | Refills | Midwest |
| ... | | | | | | | | |
| **13** | 1012 | 2026-01-25 | Grace Okafor | Tea Light Sampler | 1 | 12.00 | Candles | West |

Twelve rows of data, in rows 2 through 13. That's the whole universe for
this book. Small enough to check by hand — which you should always be able
to do, and which we'll practice.

## How to read this book

The chapters build on each other, but each one stands on its own too:

1. **[Asking in plain English](01-asking-in-plain-english.md)** — the core
   skill: telling your AI what you want so it produces a formula that works
   the first time *(most of the time).*
2. **[Reading and fixing a formula](02-reading-and-fixing-formulas.md)** —
   how to read `=SUMIF(...)` out loud, and what `#N/A` and its friends are
   trying to tell you.
3. **[VLOOKUP, without the fear](03-vlookup.md)** — the famously scary
   formula, made small.
4. **[SUMIF and COUNTIF](04-sumif-and-countif.md)** — "add it up, but only
   if…" and "count them, but only if…"
5. **[Dates without dread](05-dates.md)** — dates are numbers wearing
   costumes. Once you see that, everything gets easier.
6. **[Pivot tables, without the panic](06-pivot-tables.md)** — the moment
   the drag-and-drop menu stops being a maze.
7. **[Cleaning messy columns](07-cleaning-messy-columns.md)** — "  maya
   chen ", `OMAR HADDAD`, and `omar   haddad ` become normal people again.
8. **[Asking follow-up questions](08-follow-up-questions.md)** — the gentle
   loop of "does this look right?" that turns a formula into real
   understanding.
9. **[Prompt patterns cheat sheet](09-cheatsheet.md)** — one page to keep
   open while you work.

## One rule, stated up front

**Always keep a way to check the answer by hand.** With 12 rows you can
literally count on your fingers. Trust is built on small checks, and your AI
should be able to explain its work to you, not just hand you magic. We'll do
exactly that all book long.

Ready? [Chapter 1 →](01-asking-in-plain-english.md)
