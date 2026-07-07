## Introduction

Asha opens the college app on her phone and taps to see her exam result. The screen loads and shows exactly one of two outcomes, never both and never neither: a green "Result: PASS", or a red "Result: FAIL", depending only on her marks. Pass or fail, in stock or sold out, adult or minor, very often a program needs to take one action or the other, never neither.

A plain `if` on its own, the kind from the last lesson, could show the PASS message but would leave the screen blank on a fail, which is clearly not what the result app does. For these two-way decisions Python gives you `else`, the partner of `if` that handles the "otherwise" case.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t8he64e/03_if_else_two_doors.png)

## When There Are Exactly Two Paths

Add an `else` block and the program is guaranteed to take exactly one of the two paths.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2lmX2Vsc2VfdHdvX3dheV9kZWNpc2lvbnMgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6Im1hcmtzID0gMzVcbmlmIG1hcmtzID49IDQwOlxuICAgIHByaW50KFwiUmVzdWx0OiBQYXNzXCIpXG5lbHNlOlxuICAgIHByaW50KFwiUmVzdWx0OiBGYWlsXCIpIn0"
 width="100%"
></iframe>

If the condition is true, the first block runs. If it is false, the `else` block runs instead. There is no situation where both run, and no situation where neither runs. With marks of 35 the program prints "Fail"; with 70 it prints "Pass". One question, two outcomes, always one answer.

## else Has No Condition of Its Own

Notice that `else` does not get its own test. It is the catch-all, the "in every other case" branch. It simply runs whenever the `if` condition turns out false. This is what makes it perfect for the leftover situation: you state the interesting condition in the `if`, and `else` quietly covers everything else. Asha's result app never had to write a second condition asking "did she fail?"; failing is just whatever is left once passing has been ruled out.

Like the `if`, the `else` line ends with a colon and its block is indented. The two keywords line up at the same level, which makes the two-way choice easy to read at a glance.

## The Bug Two Separate ifs Can Hide

The previous section asked whether two separate `if` statements could replace `if`/`else`. Here is exactly why that choice is riskier than it looks, not just more verbose.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2lmX2Vsc2VfdHdvX3dheV9kZWNpc2lvbnMgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6Im1hcmtzID0gNDBcblxuaWYgbWFya3MgPj0gNDA6XG4gICAgcHJpbnQoXCJSZXN1bHQ6IFBhc3NcIilcbmlmIG1hcmtzIDwgNDA6XG4gICAgcHJpbnQoXCJSZXN1bHQ6IEZhaWxcIikifQ"
 width="100%"
></iframe>

This happens to work today, but it works only because the two conditions were written as exact opposites by hand. A small, easy-to-make slip, say changing the second condition to `marks <= 40` during a later edit without noticing the first one still says `marks >= 40`, would make both print at once for a mark of exactly 40, a bug `if`/`else` makes structurally impossible, because `else` never needs its own condition to get right in the first place.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t8he64e/03_two_ifs_vs_if_else_bug.png)


## if/else Outcomes at a Glance

| Condition Result | Block That Runs |
|---|---|
| True | The `if` block |
| False | The `else` block |

Exactly one of the two ever runs, never both and never neither.

## Your Turn: Even or Odd

Here the modulo operator from the last unit meets your new decision-making skill.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2lmX2Vsc2VfdHdvX3dheV9kZWNpc2lvbnMgY29kZSAzIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAzLnB5IiwiY29kZSI6Im51bWJlciA9IGludChpbnB1dChcIkVudGVyIGEgbnVtYmVyOiBcIikpXG5pZiBudW1iZXIgJSAyID09IDA6XG4gICAgcHJpbnQoZlwie251bWJlcn0gaXMgZXZlbi5cIilcbmVsc2U6XG4gICAgcHJpbnQoZlwie251bWJlcn0gaXMgb2RkLlwiKSJ9"
 width="100%"
></iframe>

Try 8 and then 7. The remainder when dividing by 2 is the test: a remainder of 0 means even, anything else means odd. The `else` neatly catches the odd case without you having to write a second condition for it.

A question to sharpen the idea: could you have written two separate `if` statements instead, one for even and one for odd? You could, but then Python would check both conditions every time, and a future edit could accidentally make both true or both false. The `if`/`else` pair guarantees exactly one outcome, which is safer and clearer.

## Conclusion

The `if`/`else` structure handles a two-way decision: the `if` block runs when the condition is true, and the `else` block runs in every other case. Because `else` has no condition, it is the reliable catch-all, ensuring your program always takes exactly one of the two paths. Whenever a problem has a clear "this or that" shape, `if`/`else` is the natural fit. But not every real decision is so neatly two-sided, and the grade table on Asha's app is about to prove it.
