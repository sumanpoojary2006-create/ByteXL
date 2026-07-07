## Introduction

Kabir leaves a song playing while he studies, but he has accidentally left it on single-track repeat, so the same song plays over and over and never moves on to the next one. Later, setting up chairs for a class event, he counts them out and ends up one chair short, having miscounted by exactly one right at the end of the row.

Loops are powerful, but those two particular bugs catch almost every beginner, and you will certainly meet them. The first is the infinite loop, which never stops and leaves your program frozen, exactly like Kabir's song looping forever because the player never moved on to the next track. The second is the off-by-one error, where a loop runs one time too many or one time too few, the same single missing chair Kabir miscounted by exactly one. Both are easy to create by accident and easy to fix once you know what to look for. Naming them is the first step to defeating them.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44tb5nv3h/08_infinite_loop_repeat.png)

## The Infinite Loop

An infinite loop happens when a `while` loop's condition never becomes false, so it repeats forever.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2F2b2lkaW5nX2luZmluaXRlX2xvb3BzX2FuZF9vZmZfYnlfb25lX2Vycm9ycyBjb2RlIDEiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDEucHkiLCJjb2RlIjoiY291bnQgPSAxXG53aGlsZSBjb3VudCA8PSA1OlxuICAgIHByaW50KGNvdW50KVxuICAgICMgZm9yZ290IHRvIHVwZGF0ZSBjb3VudCJ9"
 width="100%"
></iframe>

Because nothing ever changes `count`, the condition stays true and the loop prints 1 endlessly. If this happens to you, do not panic: you can stop a runaway program by pressing Ctrl and C in the terminal, or the stop button in your editor. The real fix is to make sure something inside the loop moves you toward the end, here by adding `count = count + 1`.

One useful exception is worth knowing: programmers sometimes write `while True:` on purpose to loop deliberately forever, and then use `break` to escape when the right moment comes. That is a controlled infinite loop, not an accident, and you saw it in the previous lesson when gathering numbers until the user typed "done".

## Off-by-One Errors

An off-by-one error is being wrong by exactly one, usually at the boundary of a loop. It often comes from the fencepost problem: to put up a fence with 5 sections you need 6 posts, not 5, because the ends need posts too. Loops have the same trap at their edges, and it is exactly what left Kabir one chair short: counting gaps between people instead of the people themselves quietly drops one seat from the true total.

The most common cause is forgetting that `range()` excludes its stop value. What do you think this prints?

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2F2b2lkaW5nX2luZmluaXRlX2xvb3BzX2FuZF9vZmZfYnlfb25lX2Vycm9ycyBjb2RlIDIiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDIucHkiLCJjb2RlIjoiZm9yIGkgaW4gcmFuZ2UoMSwgNSk6XG4gICAgcHJpbnQoaSkifQ"
 width="100%"
></iframe>

It prints 1, 2, 3, 4, not 1 to 5, because the stop value 5 is left out. If you wanted to include 5, you needed `range(1, 6)`. The same care applies to comparisons: a condition using `<` stops one step earlier than the same condition using `<=`. A single wrong symbol here changes the result by exactly one.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44tb5nv3h/08_off_by_one_chair.png)

## How to Catch Both

You do not need luck to find these bugs, just a habit. Trace the first and last passes of your loop by hand: what is the loop variable on the very first run, and on the very last? If the last value is one more or one less than you expected, you have found an off-by-one. To catch a suspected infinite loop, print the loop variable each pass and check that it is genuinely moving toward the stopping condition. A few seconds of checking the boundaries saves hours of confusion.

## Two Classic Bugs at a Glance

| Bug | Cause | Fix | Warning Sign |
|---|---|---|---|
| Infinite loop | A `while` condition never turns false | Update the variable the condition depends on, inside the loop | Program seems frozen |
| Off-by-one | `range()` excludes its stop value, or `<` was used where `<=` was needed | Trace the first and last pass by hand | Loop runs one time too many or too few |

## Your Turn: Find the Bug Before Running It

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2F2b2lkaW5nX2luZmluaXRlX2xvb3BzX2FuZF9vZmZfYnlfb25lX2Vycm9ycyBjb2RlIDMiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDMucHkiLCJjb2RlIjoidG90YWwgPSAwXG5pID0gMVxud2hpbGUgaSA8IDEwOlxuICAgIHRvdGFsID0gdG90YWwgKyBpXG4gICAgaSA9IGkgKyAxXG5cbnByaW50KHRvdGFsKSAgICAjIHdoYXQgZG9lcyB0aGlzIGFjdHVhbGx5IGFkZCB1cCB0bz8ifQ"
 width="100%"
></iframe>

Before running this, trace it by hand: what is `i` on the very first pass, and what is `i` on the very last pass before the loop stops? Decide whether this sums 1 through 9 or 1 through 10, then run it and check your trace against the real answer.

## Conclusion

Two loop bugs will test you again and again. An infinite loop never ends, usually because a `while` condition never turns false, so always ensure each pass makes progress (and remember that `while True:` with a `break` is a deliberate, controlled version). An off-by-one error misses or repeats the edge by one, often because `range()` excludes its stop value or because `<` and `<=` were confused. Check the first and last iterations by hand, and these two classic traps lose their power over you. From a single repeated print to a fully validated, pattern-aware grid of logic, you now have the same toolkit Kabir leans on without ever calling it programming: repeat, count, search, and know exactly when to stop. The next unit turns from repeating numbers to repeating over something far more common in real programs: the individual characters inside a string.
