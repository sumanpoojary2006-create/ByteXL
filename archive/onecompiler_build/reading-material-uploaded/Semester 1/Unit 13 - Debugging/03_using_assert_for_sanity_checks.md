## Introduction

Print debugging found Zara's bad RSVP value, but only because she happened to look at the right printed output at the right moment. A deeper worry remains: what about all the assumptions she is not actively watching right now, like every `rsvp_count` being a non-negative number, or every `Event` having at least one attendee before she calculates an average? Checking those by eye, every time, in every function, is not realistic. What she wants is a way to state an assumption directly in the code, so Python itself complains immediately and loudly the moment that assumption turns out to be false.

That is exactly what Python's `assert` statement is for.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-13-debugging/03_assert_sanity_checks.png)

## The Basic Shape of assert

`assert` takes a condition. If the condition is true, nothing happens at all, execution simply continues. If the condition is false, Python immediately raises an `AssertionError`.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-13-debugging-03-using-assert-for-sanity-checks-001-d984ec1ffb.html"
 width="100%"
></iframe>

This raises `AssertionError: attendees list must not be empty`, immediately, at the exact line where the bad assumption was checked, rather than letting the function proceed and fail two lines later with a less informative `ZeroDivisionError` that says nothing about the real cause.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-13-debugging/03_assert_checkpoint_gate.png)

*An `assert` is a sanity checkpoint for assumptions that should already be true inside your own code.*

## assert States an Assumption, Out Loud, in Code

The real value of `assert` is not just catching the error, it is making an assumption visible to anyone reading the function, including Zara herself in three weeks, who will have forgotten every detail of why this code was written this way.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-13-debugging-03-using-assert-for-sanity-checks-002-c05b8a0f55.html"
 width="100%"
></iframe>

Anyone reading `__init__` now knows, instantly and explicitly, that a sensible `Event` can never have a zero or negative capacity, a rule that might otherwise live only in Zara's head, easy to forget and easy to violate by accident elsewhere in the project.

## assert Is for Bugs in Your Own Logic, Not for User Input

This is the detail that trips up nearly every beginner: `assert` exists to catch programming mistakes, situations that should be logically impossible if the rest of the code is correct, not to validate ordinary, expected bad input from a user or a file, which the previous unit's `try`/`except` already handles properly.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-13-debugging-03-using-assert-for-sanity-checks-003-bca10bf4cc.html"
 width="100%"
></iframe>

A user mistyping their age is normal and expected, handled gracefully with `try`/`except` from the last unit. A negative `people` count reaching `split_cost`, after validation supposedly already happened earlier, is a sign something in your own logic is broken, exactly the case `assert` is built for.

## assert Can Be Disabled, So Never Rely on It for Real Validation

Python can run with assertions stripped out entirely, using the `-O` optimization flag, which means any check truly required for program correctness, like rejecting bad user input, must use `if` and `raise`, or `try`/`except`, never `assert` alone.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-13-debugging-03-using-assert-for-sanity-checks-004-643519f64c.html"
 width="100%"
></iframe>

## assert at a Glance

| Use Case | Right Tool |
|---|---|
| Catching a bug in your own logic that should be impossible | `assert condition, "message"` |
| Validating expected, ordinary bad input from a user or file | `if`/`raise`, or `try`/`except` from the previous unit |
| A check that must always run, even in optimized code | Never `assert` alone; use `if`/`raise` |

## Your Turn: State Three Assumptions

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-13-debugging-03-using-assert-for-sanity-checks-005-890e447aa4.html"
 width="100%"
></iframe>

Run this, confirm the second creation fails with a clear message naming exactly which assumption was broken, and try writing one more `assert` of your own for a rule this class should always satisfy.

## Conclusion

`assert condition, "message"` states an assumption directly in the code, raising `AssertionError` loudly and immediately the moment that assumption turns out false, making it ideal for catching bugs in your own logic early and documenting your own assumptions for future readers, but never a substitute for validating ordinary, expected bad input, which still belongs to `if`/`raise` or `try`/`except`. Print statements and `assert` both help once you already suspect something specific; the next lesson introduces a tool for when you have no idea yet where the problem even is: Python's own interactive debugger.
