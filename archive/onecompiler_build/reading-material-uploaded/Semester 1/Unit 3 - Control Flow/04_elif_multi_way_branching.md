## Introduction

Asha checks her marks on the college app, and this time it shows a full grade table, A, B, C, then F, listed top to bottom. The app checks her marks against each row in order and highlights exactly one matching grade, stopping as soon as it finds the row that fits. Two outcomes were enough for pass or fail, but a table like this needs more than that. A grade might be A, B, C, or F, a movie ticket price depends on whether you are a child, an adult, or a senior, and a traffic light is red, yellow, or green. For these many-option decisions, chaining a single `if` to an `else` is not enough, and writing lots of separate `if` statements is clumsy.

An `if`/`else` only ever splits the world in two, but a grade table splits it into four. Python's answer is `elif`, short for "else if", which lets you line up several conditions and pick the first that fits.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t8hgejq/04_elif_grade_staircase.png)

## More Than Two Choices

An `elif` chain checks one condition after another until one is true.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-3-control-flow-04-elif-multi-way-branching-001-ec808bb8bf.html"
 width="100%"
></iframe>

With marks of 72, Python checks 90 (false), then 75 (false), then 40 (true) and prints "Grade: C". The final `else` catches anyone who failed every test above. You can have as many `elif` branches as you need, and the `else` at the end is optional. This is exactly the row-by-row scan Asha watched her app perform: check the A row, check the B row, check the C row, and stop the instant one of them fits.

## The Order of Conditions Matters

Here is the most important idea in this lesson, and a question that catches many beginners. The chain is checked strictly from top to bottom, and the very first true condition wins. Every branch after it is skipped, even if it is also true.

So what would happen if you put the easiest condition first?

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-3-control-flow-04-elif-multi-way-branching-002-5d7aec4d81.html"
 width="100%"
></iframe>

A brilliant score of 95 prints "Grade: C", because `marks >= 40` is true and Python stops right there, never reaching the checks for B or A. The logic is not broken, the order is. When you build an `elif` chain on ranges, arrange the conditions from the highest threshold down to the most general.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t8hgejq/04_elif_wrong_order_bug.png)

## Order Changes the Answer

| Chain Order | Marks = 95 Prints | Why |
|---|---|---|
| `>= 90`, then `>= 75`, then `>= 40` | Grade: A | Highest threshold checked first, matches correctly |
| `>= 40`, then `>= 75`, then `>= 90` | Grade: C | The first true condition wins, and 40 was checked first |

Same marks, same conditions, different order, different answer. The order is part of the logic.

## Only One Branch Ever Runs

Whatever the values, an `if`/`elif`/`else` structure runs exactly one block: the first whose condition is true, or the `else` if none are. This guarantee is what makes it so reliable for sorting a value into one of several categories.

## elif Chains at a Glance

| Rule | Why It Matters |
|---|---|
| Conditions are checked top to bottom | The first true condition wins, and the rest are skipped |
| `elif` only runs if every condition above it was false | This is what makes the branches mutually exclusive |
| `else` is optional, and catches whatever no condition matched | A safety net for values you did not explicitly account for |
| Order conditions from most specific to least specific | A wide early condition can wrongly catch values meant for a later one |

## Your Turn: Ticket Pricing

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-3-control-flow-04-elif-multi-way-branching-003-65d2b0b6fc.html"
 width="100%"
></iframe>

Try ages 3, 12, 30, and 70. Each one lands in a different branch, and only one message ever prints. Notice how each `elif` quietly assumes the ones above it were false, so `age < 18` really means "between 5 and 17" by the time Python reaches it.

## Conclusion

The `elif` keyword extends a decision to several options, checking conditions top to bottom and running the block of the first true one, then skipping the rest. Because only the first match wins, the order of your conditions is part of the logic, not just style. Arrange range checks carefully, finish with an `else` to catch everything left over, and you can sort any value into the right category cleanly. As your chains of conditions grow longer, though, a new question appears: what happens when one decision genuinely depends on another, rather than just sitting beside it?
