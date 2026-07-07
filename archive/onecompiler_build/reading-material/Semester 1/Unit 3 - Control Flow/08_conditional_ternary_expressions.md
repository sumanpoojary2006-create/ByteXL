## Introduction

Asha wants to set a quick status on her phone that simply reads "Pass" if her marks are at least 40 and "Fail" otherwise. Spelled out the long way, such a tiny choice takes four whole lines:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2NvbmRpdGlvbmFsX3Rlcm5hcnlfZXhwcmVzc2lvbnMgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6Im1hcmtzID0gNzJcbmlmIG1hcmtzID49IDQwOlxuICAgIHN0YXR1cyA9IFwiUGFzc1wiXG5lbHNlOlxuICAgIHN0YXR1cyA9IFwiRmFpbFwiIn0"
 width="100%"
></iframe>

Four lines to make a single choice between two words. For a status that is only ever going to be set once and printed once, that much ceremony feels heavier than the decision deserves. Python offers a tidy shortcut for exactly this situation, called the conditional expression, often nicknamed the ternary operator. It folds that whole decision into one readable line.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t8hnwp7/08_ternary_one_line.png)

## A Decision in a Single Line

Here is the same logic written as a conditional expression:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2NvbmRpdGlvbmFsX3Rlcm5hcnlfZXhwcmVzc2lvbnMgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6Im1hcmtzID0gNzJcbnN0YXR1cyA9IFwiUGFzc1wiIGlmIG1hcmtzID49IDQwIGVsc2UgXCJGYWlsXCJcbnByaW50KHN0YXR1cykifQ"
 width="100%"
></iframe>

Read it almost like a sentence: status is "Pass" if marks are at least 40, else "Fail". The condition sits in the middle, the value to use when it is true comes first, and the value to use when it is false comes last.

## The Shape to Remember

The general form is:

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2NvbmRpdGlvbmFsX3Rlcm5hcnlfZXhwcmVzc2lvbnMgY29kZSAzIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAzLnB5IiwiY29kZSI6InZhbHVlX2lmX3RydWUgaWYgY29uZGl0aW9uIGVsc2UgdmFsdWVfaWZfZmFsc2UifQ"
 width="100%"
></iframe>

It is an expression, which means it produces a single value, so it fits naturally wherever a value is expected: on the right of an assignment, inside a `print`, or even inside an f-string, unlike a full `if`/`else` statement, which only ever runs actions and never hands back a value you can drop straight into another line.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2NvbmRpdGlvbmFsX3Rlcm5hcnlfZXhwcmVzc2lvbnMgY29kZSA0IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA0LnB5IiwiY29kZSI6ImFnZSA9IDIwXG5wcmludChmXCJZb3UgYXJlIHsnYW4gYWR1bHQnIGlmIGFnZSA-PSAxOCBlbHNlICdhIG1pbm9yJ30uXCIpIn0"
 width="100%"
></iframe>

## Resist Nesting One Inside Another

Python does technically allow a conditional expression inside another one, to cover more than two outcomes, but the moment you try it, the readability that made the ternary worthwhile quietly disappears.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2NvbmRpdGlvbmFsX3Rlcm5hcnlfZXhwcmVzc2lvbnMgY29kZSA1IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA1LnB5IiwiY29kZSI6Im1hcmtzID0gNzJcbmdyYWRlID0gXCJBXCIgaWYgbWFya3MgPj0gOTAgZWxzZSBcIkJcIiBpZiBtYXJrcyA-PSA3NSBlbHNlIFwiQ1wiIGlmIG1hcmtzID49IDQwIGVsc2UgXCJGXCJcbnByaW50KGdyYWRlKSJ9"
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
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA4X2NvbmRpdGlvbmFsX3Rlcm5hcnlfZXhwcmVzc2lvbnMgY29kZSA2IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA2LnB5IiwiY29kZSI6ImEgPSBpbnQoaW5wdXQoXCJGaXJzdCBudW1iZXI6IFwiKSlcbmIgPSBpbnQoaW5wdXQoXCJTZWNvbmQgbnVtYmVyOiBcIikpXG5sYXJnZXIgPSBhIGlmIGEgPiBiIGVsc2UgYlxucHJpbnQoXCJUaGUgbGFyZ2VyIG51bWJlciBpc1wiLCBsYXJnZXIpIn0"
 width="100%"
></iframe>

Try 7 and 10. The expression checks `a > b`, and since it is false, it chooses `b`. One line decided and stored the answer, with no separate `if` block needed.

## Conclusion

A conditional expression, written as `value_if_true if condition else value_if_false`, makes a two-way choice between values in a single readable line, perfect for setting a variable or filling a slot in your output. Use it for simple either/or choices, and switch back to a full `if`/`else` when the logic has more branches or needs to do more than pick a value. It is a small piece of polish that keeps simple decisions from sprawling across four lines. With every shape of decision now in hand, the final lesson of the unit turns to the problem every one of them was quietly built to solve: trusting what a real user actually types.
