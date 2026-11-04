# Chapter 8 · Asking Follow-Up Questions

*Here is the truest thing in this book: the first formula the AI gives
you is a draft. A good first draft, most of the time — but a draft. The
magic isn't in the first answer. It's in the little conversation that
comes after.*

## The loop (small and friendly)

Every chapter so far has quietly used the same three-beat loop. Naming it
now, so it's a tool instead of a vibe:

1. **Ask in plain English** (Chapter 1's template).
2. **Read what came back, out loud** (Chapter 2's skill) and *verify*
   against a hand-checked expectation.
3. **Follow up** — and this beat has more range than you'd guess.

That third beat is its own skill, and it's the difference between people
who feel "AI does spreadsheets for me" and people who feel
"AI and I do spreadsheets together."

## The follow-up menu

Keep this list in your back pocket. Every one of these is a full, complete
follow-up question, ready to paste:

| When… | Ask… |
| --- | --- |
| The number looks wrong | "I got X but I expected Y by my own count. Here's my sheet map. What could cause that?" |
| The formula works but you don't trust it | "Explain what this formula does, part by part, in plain English — and tell me one manual check I could do." |
| You didn't understand the explanation | "Explain that again, but simpler — like to someone who's never used a spreadsheet before." |
| You want to learn, not just finish | "Why is that the best way? What's the second-best way, and when would I prefer it?" |
| It gave an error | "This formula gives `#N/A`. What usually causes that? Give me a yes/no checklist to narrow it down." |
| You're asked something you can't answer | "I don't know what that means. Could you show me exactly how to find out, step by step?" |
| You've fixed it and want confidence | "How would I test whether my fixed formula is truly correct before I trust it for the whole sheet?" |
| It's *almost* what you want | "That's close — but instead of ___, can it do ___? Keep the same columns." |
| You're feeling lost inside the sheet | "List every formula currently touching cell I15, and what each is for." |
| You want to protect future-you | "What could break this sheet later, and how would I notice right away if it did?" |

Print that table, or keep a copy of this file open. Nine times out of ten,
the question you need is already written down above.

## What follow-ups look like in real life

A small, true-to-life conversation from the making of this very chapter's
examples. June (fictional candle shop, remember), after getting her first
working VLOOKUP:

> **June:** =VLOOKUP(D2, Catalog!$A$2:$B$5, 2, FALSE) works on all but two
> rows, which give #N/A. I double-checked and both products ARE in the
> catalog. Why just those two?
>
> **AI:** If only *some* rows miss, the products are in the catalog, but
> those two cells are *visibly different from inside* — most often extra
> leading/trailing spaces, or a double space inside. Try =LEN(D2) filled
> down next to the misses, and compare with the same-length values…
> actually first, simply try =D2=Catalog!$A$4 for one failing row. If it
> says FALSE, we've found a formatting difference and I'll walk you
> through cleaning the column.
>
> **June:** It says FALSE.
>
> **AI:** Then it's almost certainly stray whitespace. In a new column K,
> fill down =TRIM(Clean version)…

…which is exactly how [Chapter 7](07-cleaning-messy-columns.md) got its
specimen, and Chapter 2's fixing routine's step 4 got its example of a
hypothesis. Three follow-ups and June went from "the AI gave me a broken
formula" to "we found it, together" — and she can now recognize that
particular bug on her own forever.

Notice two qualities in her follow-ups worth stealing:

- She **reports the difference between expectation and reality**
  ("works on all but two rows" — not "it's broken").
- She **feeds the AI the check result it asked for** ("It says FALSE")
  instead of restarting from scratch.

## When the AI is confidently wrong

It happens; it's the price of a fast free intern with infinite patience.
Your defenses, in order:

1. **Your hand check** (this book's drumbeat): 12 rows you can count on
   your fingers is your *immunity*.
2. **Ask it to show its work:** "Show me, with my data, which specific
   rows you added for that total." If it lists rows, add them yourself.
   If it can't list rows, that's information too.
3. **Ask for a second method:** "Can you compute this a different way —
   a different function or even a different order of operations — so I
   can check one against the other?" Two roads agreeing is solid
   evidence.
4. **Restart with fresh framing:** sometimes a stubborn wrong answer
   (yours or its) clears with "Let's start over; I'll describe the whole
   situation again from the beginning." One clean restate beats five
   rounds of patching.

And a meta-defense: **when you undertand *why* a formula works, wrong
answers can't hurt you** — that's why Chapters 2 through 7 each taught the
"read it aloud" habit before the fancy stuff. You're not memorizing
spreadsheet factoids; you're collecting readable, checkable tools you can
rebuild in any sheet, with any AI, forever.

## One last follow-up you should always feel free to ask

Nobody says this in tutorials, so I will: **"Can you slow down?
I'm following but I want to make sure I've got it before we move on."**

Any decent AI chat handles that parenthetically — and so would any decent
human teacher. This is your learning experience, sized to your Tuesday,
and neither the spreadsheet nor the AI is grading you.

Onward to [Chapter 9](09-cheatsheet.md) — the single-page keeper: prompt
patterns and a formula quick-reference.
