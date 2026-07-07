## Introduction

Kabir is scrolling his feed looking for one particular post a friend told him about. The moment it appears on screen, he stops scrolling instantly, no point going further, he has found it. Earlier, as he scrolled, he had been flicking straight past the sponsored ad posts without really stopping on them, just skipping each one and carrying on.

By default a loop runs to completion, taking every value in turn, but real problems often need finer control like this. You want to stop the moment you find what you are looking for, rather than checking the rest pointlessly, or you want to skip a particular item and carry on with the others. Kabir's feed never paused on every single ad just because it kept scrolling, and it never kept scrolling past the post he wanted either. Python gives you two precise commands for this, `break` and `continue`, and a lesser known but useful partner, the loop `else`.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44tb5mm6y/05_break_continue.png)
## break: Stop the Loop Early

The `break` command immediately ends the loop, even if there are items left. It is perfect for a search, where there is no reason to keep looking once you have found a match.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2JyZWFrX2NvbnRpbnVlX2FuZF9sb29wX2Vsc2UgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6ImZvciBudW1iZXIgaW4gcmFuZ2UoMSwgMTAwKTpcbiAgICBpZiBudW1iZXIgKiBudW1iZXIgPiA1MDpcbiAgICAgICAgcHJpbnQoXCJGaXJzdCBudW1iZXIgd2hvc2Ugc3F1YXJlIGV4Y2VlZHMgNTA6XCIsIG51bWJlcilcbiAgICAgICAgYnJlYWsifQ"
 width="100%"
></iframe>

The loop counts upward, and as soon as a number's square passes 50 (which happens at 8), it prints the answer and breaks out. Without `break`, the loop would carry on uselessly to 99. Stopping early is not just tidy, it can save a great deal of work on large data, exactly the moment Kabir's thumb stops scrolling the instant the post he wanted appears on screen.

## continue: Skip This One and Move On

Where `break` abandons the whole loop, `continue` abandons only the current pass and jumps straight to the next item. It is ideal for skipping values you do not care about.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2JyZWFrX2NvbnRpbnVlX2FuZF9sb29wX2Vsc2UgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6ImZvciBudW1iZXIgaW4gcmFuZ2UoMSwgMTEpOlxuICAgIGlmIG51bWJlciAlIDIgPT0gMDpcbiAgICAgICAgY29udGludWVcbiAgICBwcmludChudW1iZXIpIn0"
 width="100%"
></iframe>

This prints only the odd numbers 1, 3, 5, 7, 9. When the number is even, `continue` skips the `print` and moves to the next value. The loop keeps running; it just ignores the items you told it to skip.

## The loop-else Clause

Here is a feature many programmers never learn: a loop can have an `else` block, which runs only if the loop finished normally without ever hitting a `break`. This is the clean way to handle "I searched everything and did not find it."

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2JyZWFrX2NvbnRpbnVlX2FuZF9sb29wX2Vsc2UgY29kZSAzIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAzLnB5IiwiY29kZSI6InRhcmdldCA9IDdcbmZvciBudW1iZXIgaW4gWzIsIDQsIDYsIDhdOlxuICAgIGlmIG51bWJlciA9PSB0YXJnZXQ6XG4gICAgICAgIHByaW50KFwiRm91bmQgaXQhXCIpXG4gICAgICAgIGJyZWFrXG5lbHNlOlxuICAgIHByaW50KFwiTm90IGZvdW5kIGluIHRoZSBsaXN0LlwiKSJ9"
 width="100%"
></iframe>

Because 7 is not in the list, the loop never breaks, so the `else` runs and reports that it was not found. Had the target been 4, the `break` would have fired and the `else` would have been skipped. It is a neat, readable way to express a search result.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44tb5mm6y/05_loop_else_not_found.png)

## break vs continue vs loop-else at a Glance

| Keyword | Effect | Use When |
|---|---|---|
| `break` | Stops the whole loop immediately | A search has already succeeded |
| `continue` | Skips only the current item, loop carries on | An item should be ignored, not stopped for |
| loop `else` | Runs only if the loop finished without a `break` | You need a clean "not found" message |

## Your Turn: Find the First Multiple

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X2JyZWFrX2NvbnRpbnVlX2FuZF9sb29wX2Vsc2UgY29kZSA0IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA0LnB5IiwiY29kZSI6Im4gPSBpbnQoaW5wdXQoXCJGaW5kIHRoZSBmaXJzdCBtdWx0aXBsZSBvZiB0aGlzIG51bWJlciBhYm92ZSA1MDogXCIpKVxuZm9yIHZhbHVlIGluIHJhbmdlKDUxLCAyMDApOlxuICAgIGlmIHZhbHVlICUgbiA9PSAwOlxuICAgICAgICBwcmludChcIkZpcnN0IG11bHRpcGxlIGFib3ZlIDUwIGlzXCIsIHZhbHVlKVxuICAgICAgICBicmVhayJ9"
 width="100%"
></iframe>

Enter 7 and the loop stops at 56. The search ends the instant it succeeds, thanks to `break`, instead of grinding all the way to 199.

## Conclusion

Inside a loop, `break` stops the whole loop early, which is ideal once a search has succeeded, and `continue` skips only the current item and carries on with the rest. The loop `else` runs when the loop completes without a `break`, giving you a clean way to say "not found." Together these turn a plain loop into a precise tool that does exactly as much work as needed and no more. A single loop has carried you far already, but some real layouts, like the very grid Kabir arranges his photos into, need one loop working inside another.
