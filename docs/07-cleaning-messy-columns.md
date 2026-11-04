# Chapter 7 · Cleaning Messy Columns

*Real spreadsheets have real mess. Not hero-movie mess — small, boring,
human mess: extra spaces, surprise capitalization, one column holding
three facts, the same customer existing twice as two people. This chapter
is a calm toolkit for exactly that mess, and your AI is a natural at it.*

## The specimen

Open `examples/messy_names.csv`. Seven rows in one column ("MessyName"),
typed by seven different people who were each in a hurry:

```
"  maya   chen "
"LUIS ORTEGA"
"priya patel "
"June  Tanaka"
"    Omar Haddad"
"omar   haddad "
"GRACE   okafor  "
```

Two things jump out if you look with spreadsheet eyes:

1. **Beauty faults** — leading spaces, trailing spaces, rages of capital —
   all styles, all fixable in one pass.
2. **One real problem**: rows 5 and 6 are the same person,
   `Omar Haddad`, typed two different ways. Cleaning isn't cosmetic —
   it's what lets COUNTIF, SUMIF, and deduping see them as one.

## The three cleaning formulas that handle 90% of cases

Freed by the sheet-map prompt pattern from [Chapter 1](01-asking-in-plain-english.md):

```
My sheet has one column: headers in row 1, data in A2:A8 — messy names
like "  maya   chen ". Give me formulas to put in B2 (filled down)
that produce clean names: no extra leading/trailing spaces, no doubled
inner spaces, and consistent capitalization. Explain each in one line.
```

You'll get some blend of the classic trio:

| Formula | What it does by hand |
| --- | --- |
| `=TRIM(A2)` | Trims leading *and* trailing spaces, and squashes runs of inner spaces to one |
| `=PROPER(A2)` | Capitalizes each word: `maya chen` → `Maya Chen` |
| `=SUBSTITUTE(A2,"  "," ")` | A surgical replace — rarely needed *by hand* since TRIM already collapses inner spaces |

Combining them yourself would look like
`=PROPER(TRIM(A2))` (inner-after-outer is fine, and your AI will write it
for you anyway). The honest beginner move is simple: **type `=PROPER(TRIM(A2))`
in B2, fill down, and look at the column gently.**

That produces our clean list for the seven rows:

```
Maya Chen
Luis Ortega
Priya Patel
June Tanaka
Omar Haddad
Omar Haddad      ← same person, now seen as the same person
Grace Okafor
```

And COUNTIF is now equipped to tell the truth:

```
=COUNTIF(B2:B8, "Omar Haddad")      → 2
```

Before cleaning, that count was invisibly split between `"    Omar Haddad"`
and `"omar   haddad "` and the total said 1 (or worse, if the AI's tests
were looking for capitalization variants). Multiply that by every column
in every sheet you'll ever touch, and you see why cleaning is worth an
entire chapter.

## The deduping honesty deserves its own moment

With clean names, finding duplicates becomes the fun kind of problem.
Two AI-assistable moves:

**Move 1 — flag duplicates next to the data:**

```
=IF(COUNTIF($B$2:B2, B2)>1, "dupe", "first")
```

Read aloud (with help if needed, [Chapter 2](02-reading-and-fixing-formulas.md)):
*"As I fill this down, it counts how many times this name appears in the
rows up to and including this one; more than once means 'dupe'."*
Fill down and the second `Omar Haddad` reads `dupe`. Nothing is deleted;
you see everything and decide.

**Move 2 — keep only firsts in one pass, when you're ready:**
Data → Remove duplicates (Sheets / Excel) or Data → More Filters →
Standard Filter → *no duplications* (LibreOffice), applied to column B.
Run it once, check the count dropped from 7 rows to **6**, then delete
column B if you no longer need the helper.

> **The sheets rule of thumb.** Don't destructively clean in columns
> people care about *until* you've checked the cleaned version beside the
> original. Duplicate-to-column-B (or duplicate the sheet — see our friend
> from [Chapter 2](02-reading-and-fixing-formulas.md)), sanity-check, then
> replace. Slow is smooth.

## Merging first and last names into one column

The other classic mess is its mirror image: a spreadsheet where names are
*bisected* into `First Name` / `Last Name` columns, and *now* you wish
they were one. The glue is:

```
=A2 & " " & B2
```

The `&` is the "glue these two pieces of text together" symbol, and `" "`
in the middle is the space between them. So `A2 = Maya`, `B2 = Chen` →
`Maya Chen`. Your AI will sometimes write this as
`=CONCATENATE(A2," ",B2)` or `=TEXTJOIN(" ",TRUE,A2:B2)` — all the same
job, different dialects.

## When a mess is bigger than three formulas

Three formulas handle 90% of column mess. The other 10% is where you say
the true sentence of this whole book out loud:

> **"Here's what column A looks like, here's what I want it to look like,
> here are three examples of rows — write me the formula or walk me
> through the tool for the rest."**

Examples include: names stuck in a single column as `"Tanaka, June"`;
product codes like `CANDLE-3PK-2026` where you only want the middle; a
date column that says `Jan 5, 2026` as *words*, not a date. Messes like
these have tools — "Split text to columns," Flash Fill (Excel),
`TEXTBEFORE`/`TEXTAFTER` (newer Excel/Sheets), `REGEXEXTRACT` (Sheets) —
and knowing *the name of the kind of tool* matters less than describing
the want and letting the AI pick. That's [Chapter 1](01-asking-in-plain-english.md)'s
job, and Chapter 8 is about what comes after.
