# Chapter 2 · Reading and Fixing a Formula

*First: you will never be fluent in formulas from reading this once. Nobody
is. The trick isn't memorization — it's reading a formula the way you read a
to-do list, and having a routine for when something comes back wrong.*

## Reading a formula out loud

Take June's revenue formula from [Chapter 1](01-asking-in-plain-english.md):

```
=SUM(I2:I13)
```

Read it like a sentence: *"Sum — add up — the range from cell I2 to cell
I13."* That's all it says. It's not magic; it's a to-do list with cell
addresses.

Now `=E2*F2`: *"Times the qty in E2 by the price in F2."* The pattern is
always:

```
= FUNCTION( arguments )
```

- The **`=`** means "this cell does a job."
- The **function name** (`SUM`, `VLOOKUP`, `SUMIF`…) is the *verb*.
- The **arguments**, separated by commas, are its *details*.
- A **range** like `I2:I13` means "cells I2 through I13, inclusive."

When an AI hands you a formula, recite it aloud, and if it's longer than a
line, ask the AI directly:

> Please translate this formula into plain English, one step per line:
> `=SUMIF(G2:G13,"Gift Sets",I2:I13)`

You'll get something like:

1. Look down the Category column (G2:G13).
2. Where the category is exactly "Gift Sets"…
3. …add up the matching row's line total from I2:I13.

Glance at June's data — Gift Sets are orders 1001, 1004, 1006, 1010 with
line totals 84.00 + 42.00 + 42.00 + 126.00 — and you'll see the answer
should be **294.00**. Which is what that formula produces. You just
*verified an AI-written formula by hand.* That's the whole chapter in one
move, and you're more capable than you thought.

> **Filling down, the honest way**
>
> The formula in `I2` says `=E2*F2`. Copy it to I3 and spreadsheets are
> smart enough that it becomes `=E3*F3` on its own — the references
> "shift" as you copy. This is called a *relative reference*, and it's
> usually what you want. When you *don't* want shifting (see Chapter 3's
> catalog range), the AI will use dollar signs — `catalog!$A$2:$B$5` —
> which means "this exact range, don't shift it." If that sounds abstract,
> no need to master it today; just know **$ pins a reference in place.**

Also worth knowing: **`SUM(A2:A13)` that includes a blank cell is fine** —
blanks count as zero. An error usually means a *word* got in, not a blank.

## When it comes back wrong: the error glossary

Errors look scary and shouty. Read them as *polite complaints*, each with a
specific meaning:

| You see | Plain meaning | Usual first suspect |
| --- | --- | --- |
| `#NAME?` | Spreadsheet doesn't recognize a word you typed | Misspelled function name, or quotes missing around text |
| `#N/A` | "I looked for that and found nothing" | Lookup value doesn't exist in the table (Chapter 3's topic) |
| `#REF!` | Formula points at a cell that isn't there anymore | You deleted rows/columns the formula used |
| `#VALUE!` | You asked math of a word, or vice versa | Number stored as text (common with dates — Chapter 5) |
| `#DIV/0!` | Divide by zero | A total in the denominator is 0 or blank |
| `#SPILL!` (Excel) | The formula wants to output multiple cells but they're not empty | Something stuck in the way |
| Err:5xx / Err:52x (LibreOffice) | Same complaints, different accents | Same triage |

## The fixing routine (a conversation, not a spell)

When a formula gives you an error or a number you don't believe, run this
5-step loop. You run it *with the AI*, and nothing more is required of you
than honesty:

1. **State the intent.** "This was supposed to total revenue by category.
   I expected 294.00 for Gift Sets."
2. **State the reality.** "I got 0." (Or `#N/A`, or 2,940.00 — say the
   exact thing you saw.)
3. **Give the map.** Re-paste your sheet map. AI can't fix formulas it
   can't see.
4. **Ask for diagnosis, then a candidate.** "What would cause that? Give
   me a corrected formula to try."
5. **Ask for a hand check.** "How could I verify the answer with just one
   manual addition?"

Real example from the writing of this book:

> **You:** My formula `=SUMIF(G2:G13,"Gift Sets",I2:I13)` returns 0. I
> calculated by hand that Gift Sets should be 84.00 + 42.00 + 42.00 +
> 126.00 = 294.00. What's going on?
>
> **AI:** If your line totals are in column I and your categories in G,
> that formula should be right — which means we're likely missing the
> *categories* matching "Gift Sets" exactly. Check whether G2:G13 contains
> things like `Gift Sets ` (trailing space), `gift sets`
> (lowercase), or `Gift Set` (singular). Tell me what the exact text in
> G2 is.

Notice: the AI didn't just spit a new formula and pray. It made a
*hypothesis* and asked you for evidence. That's a good sign your AI is
being a good collaborator — and exactly how Chapter 8's follow-up loop
begins.

> **Why manual checks matter — the self-trust loop**
>
> Every chapter in this book includes a number you can verify by hand
> (like 294.00 above). When a spreadsheet and your own quick check
> agree, that *builds* trust faster than any tutorial can. When they
> don't agree, you found a real problem while it's still tiny. Either
> way you win. The AI is a fast, patient, occasionally-wrong colleague —
> your hand check is the safety net.

## One formula at a time, in a sheet you can undo

Final practical advice, especially if you're uneasy in spreadsheets:

- Open the copy of the file — never the original — and
  **duplicate your sheet** (right-click the tab, "Duplicate") before big
  changes. Now mistakes cost nothing.
- Make **one formula at a time**, sanity-check it, then continue.
- If a formula builds on a formula, give the AI the *whole stack* ("I have
  =E2*F2 in I2, =SUM(I2:I13) in I15, and a =SUMIF in I17") when you ask.

That's habits, not heroics. On to [Chapter 3](03-vlookup.md) and the
famous one: VLOOKUP.
