## Introduction

Asha wants to set a quick status on her phone that simply reads "Pass" if her marks are at least 40 and "Fail" otherwise. Spelled out the long way, such a tiny choice takes four whole lines:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-3-control-flow-08-conditional-ternary-expressions-001-61018fec5b.html"
 width="100%"
></iframe>

Four lines to make a single choice between two words. For a status that is only ever going to be set once and printed once, that much ceremony feels heavier than the decision deserves. Python offers a tidy shortcut for exactly this situation, called the conditional expression, often nicknamed the ternary operator. It folds that whole decision into one readable line.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t8hnwp7/08_ternary_one_line.png)

## A Decision in a Single Line

Here is the same logic written as a conditional expression:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-3-control-flow-08-conditional-ternary-expressions-002-a76a3b0330.html"
 width="100%"
></iframe>

Read it almost like a sentence: status is "Pass" if marks are at least 40, else "Fail". The condition sits in the middle, the value to use when it is true comes first, and the value to use when it is false comes last.

## The Shape to Remember

The general form is:

```
value_if_true if condition else value_if_false
```

It is an expression, which means it produces a single value, so it fits naturally wherever a value is expected: on the right of an assignment, inside a `print`, or even inside an f-string, unlike a full `if`/`else` statement, which only ever runs actions and never hands back a value you can drop straight into another line.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-3-control-flow-08-conditional-ternary-expressions-003-c963be201e.html"
 width="100%"
></iframe>

## Resist Nesting One Inside Another

Python does technically allow a conditional expression inside another one, to cover more than two outcomes, but the moment you try it, the readability that made the ternary worthwhile quietly disappears.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-3-control-flow-08-conditional-ternary-expressions-004-8c5bf47d00.html"
 width="100%"
></iframe>

This single line genuinely works, computing the same result a full `elif` chain from the previous lessons would, but reading it requires holding three nested conditions in your head at once, in a line that does not even visually show the nesting. Compare it to the equivalent `elif` chain, which lays each threshold out on its own line, in plain top-to-bottom order, exactly as readable as it was when you first met it earlier in this unit. The ternary saved characters here, but it cost clarity, and clarity is the trade you almost never want to make.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t8hnwp7/08_nested_ternary_warning.png)


## Ternary Expressions at a Glance

So when should you reach for it?

| Situation | Better Choice |
|---|---|
| Choosing between two values based on one condition | Conditional expression |
| Several branches needed | Full `if`/`elif`/`else` |
| Running actions, not just picking a value | Full `if`/`elif`/`else` |
| Tempted to nest one inside another | Full `if`/`elif`/`else` |

Clear always beats clever.

## Your Turn: Larger of Two Numbers

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-3-control-flow-08-conditional-ternary-expressions-005-4e2d6413bb.html"
 width="100%"
></iframe>

Try 7 and 10. The expression checks `a > b`, and since it is false, it chooses `b`. One line decided and stored the answer, with no separate `if` block needed.

## Conclusion

A conditional expression, written as `value_if_true if condition else value_if_false`, makes a two-way choice between values in a single readable line, perfect for setting a variable or filling a slot in your output. Use it for simple either/or choices, and switch back to a full `if`/`else` when the logic has more branches or needs to do more than pick a value. It is a small piece of polish that keeps simple decisions from sprawling across four lines. With every shape of decision now in hand, the final lesson of the unit turns to the problem every one of them was quietly built to solve: trusting what a real user actually types.
