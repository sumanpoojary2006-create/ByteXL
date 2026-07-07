## Introduction

Asha glances at her phone and a single yellow banner slides down from the top of the screen: "Battery Low." It only appears because the battery has just dropped below twenty percent, and the rest of her home screen carries on exactly as before. If the battery were comfortably full, that same banner would simply never show up, no warning, nothing happening at all. There is no second outcome here, no alternate path, just one action that happens only if its condition is true. Show a low-battery warning only if the battery is low, add a bonus only if the score is high enough, show "Welcome back" only if the user is logged in.

Notice how unremarkable this feels from Asha's side. She never asked for a warning; the phone simply decided, on its own, whether one was needed at all. That quiet ability to sometimes act and sometimes do absolutely nothing is the job of the `if` statement, the most fundamental tool in all of control flow.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t8hdc6u/02_if_single_door.png)

## Do Something Only If

The shape of an `if` statement reads almost like English:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-3-control-flow-02-the-if-statement-001-768badc758.html"
 width="100%"
></iframe>

Read it aloud: "if balance is less than 500, print the warning." When the condition `balance < 500` is true, the indented line runs. When it is false, Python simply skips that line and moves on. With a balance of 120 the warning appears; change it to 900 and the program prints nothing, which is exactly what we want.

## The Colon and the Indentation Are Not Optional

Two small details carry big meaning here, and Python takes both seriously.

First, the line that states the condition ends with a colon. Second, the action that belongs to the `if` is indented, usually by four spaces. That indentation is how Python knows which lines are inside the decision and which are not. In many other languages, curly braces do this job. In Python, the indentation itself is the syntax.

So what happens if you forget? Leaving out the colon, or indenting incorrectly, stops the program with an error such as `IndentationError` or `SyntaxError`. Far from being annoying, this is Python protecting you, because messy indentation is exactly where logic bugs hide. A line that looks like it belongs to the decision but is actually indented one space too far, or too few, would otherwise run at the wrong moment without ever announcing the mistake.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44t8hdc6u/02_if_indentation_block.png)


## The if Statement at a Glance

| Part | Required? | Purpose |
|---|---|---|
| `if` keyword | Yes | Marks the start of a decision |
| Condition | Yes | A boolean expression Python checks |
| Colon `:` | Yes | Marks the end of the condition line |
| Indented block | Yes | The line(s) that run only when the condition is true |

Look at how indentation decides meaning:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-3-control-flow-02-the-if-statement-002-cf10d8c189.html"
 width="100%"
></iframe>

The first two prints are indented, so they belong to the `if` and run only when there is a fever. The last line is not indented, so it sits outside the decision and runs every time. The indentation is doing real work.

## The Condition Can Be Any Yes or No Test

The condition after `if` is just a boolean, so everything you learned about operators applies. You can compare, and you can combine with `and`, `or`, and `not`.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-3-control-flow-02-the-if-statement-003-0a8b9793a2.html"
 width="100%"
></iframe>

One classic slip to avoid: use two equals signs to compare. Writing `if score = 90` is an assignment by mistake and Python will flag it; you want `if score == 90`.

## Your Turn: Positive Number Check

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-3-control-flow-02-the-if-statement-004-344fea77d5.html"
 width="100%"
></iframe>

Run it with 7 and the positive message appears before "Done." Run it with -3 and only "Done." prints, because the indented line was skipped. Notice that "Done." appears either way, because it lives outside the `if`.

## Conclusion

The `if` statement runs a block of code only when its condition is true, and skips it otherwise. Remember the two rules of its shape: end the condition line with a colon, and indent the lines that belong to the decision. That indentation is not decoration in Python, it is how the language knows what is inside the decision and what is not. With this single tool you can already make your programs react instead of just calculate. The next question is the natural follow-up Asha's PASS-or-FAIL result screen raises: what should happen in the case where the condition is false, instead of nothing at all?
