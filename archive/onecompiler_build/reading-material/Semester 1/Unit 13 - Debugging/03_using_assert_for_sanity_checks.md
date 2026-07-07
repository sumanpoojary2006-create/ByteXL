## Introduction

Print debugging found Zara's bad RSVP value, but only because she happened to look at the right printed output at the right moment. A deeper worry remains: what about all the assumptions she is not actively watching right now, like every `rsvp_count` being a non-negative number, or every `Event` having at least one attendee before she calculates an average? Checking those by eye, every time, in every function, is not realistic. What she wants is a way to state an assumption directly in the code, so Python itself complains immediately and loudly the moment that assumption turns out to be false.

That is exactly what Python's `assert` statement is for.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-13-debugging/03_assert_sanity_checks.png)

## The Basic Shape of assert

`assert` takes a condition. If the condition is true, nothing happens at all, execution simply continues. If the condition is false, Python immediately raises an `AssertionError`.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX3VzaW5nX2Fzc2VydF9mb3Jfc2FuaXR5X2NoZWNrcyBjb2RlIDEiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDEucHkiLCJjb2RlIjoiZGVmIGF2ZXJhZ2VfcnN2cHMoYXR0ZW5kZWVzKTpcbiAgICBhc3NlcnQgbGVuKGF0dGVuZGVlcykgPiAwLCBcImF0dGVuZGVlcyBsaXN0IG11c3Qgbm90IGJlIGVtcHR5XCJcbiAgICB0b3RhbCA9IHN1bShhLnJzdnBfY291bnQgZm9yIGEgaW4gYXR0ZW5kZWVzKVxuICAgIHJldHVybiB0b3RhbCAvIGxlbihhdHRlbmRlZXMpXG5cbmF2ZXJhZ2VfcnN2cHMoW10pICAgICMgZXJyb3IhIn0"
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
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX3VzaW5nX2Fzc2VydF9mb3Jfc2FuaXR5X2NoZWNrcyBjb2RlIDIiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDIucHkiLCJjb2RlIjoiY2xhc3MgRXZlbnQ6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIG5hbWUsIG1heF9hdHRlbmRlZXMpOlxuICAgICAgICBhc3NlcnQgbWF4X2F0dGVuZGVlcyA-IDAsIFwiYW4gZXZlbnQgbXVzdCBhbGxvdyBhdCBsZWFzdCBvbmUgYXR0ZW5kZWVcIlxuICAgICAgICBzZWxmLm5hbWUgPSBuYW1lXG4gICAgICAgIHNlbGYubWF4X2F0dGVuZGVlcyA9IG1heF9hdHRlbmRlZXNcbiAgICAgICAgc2VsZi5hdHRlbmRlZXMgPSBbXSJ9"
 width="100%"
></iframe>

Anyone reading `__init__` now knows, instantly and explicitly, that a sensible `Event` can never have a zero or negative capacity, a rule that might otherwise live only in Zara's head, easy to forget and easy to violate by accident elsewhere in the project.

## assert Is for Bugs in Your Own Logic, Not for User Input

This is the detail that trips up nearly every beginner: `assert` exists to catch programming mistakes, situations that should be logically impossible if the rest of the code is correct, not to validate ordinary, expected bad input from a user or a file, which the previous unit's `try`/`except` already handles properly.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX3VzaW5nX2Fzc2VydF9mb3Jfc2FuaXR5X2NoZWNrcyBjb2RlIDMiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDMucHkiLCJjb2RlIjoiIyBXcm9uZyB1c2Ugb2YgYXNzZXJ0OiB0aGlzIGlzIGV4cGVjdGVkLCByZWNvdmVyYWJsZSB1c2VyIGlucHV0LCBub3QgYSBidWdcbmFnZV90ZXh0ID0gaW5wdXQoXCJFbnRlciB5b3VyIGFnZTogXCIpXG5hc3NlcnQgYWdlX3RleHQuaXNkaWdpdCgpLCBcIm11c3QgYmUgZGlnaXRzXCIgICAgIyBjcmFzaGVzIHRoZSB3aG9sZSBwcm9ncmFtIG9uIG9yZGluYXJ5IGJhZCBpbnB1dCFcblxuIyBSaWdodCB1c2Ugb2YgYXNzZXJ0OiB0aGlzIHNob3VsZCBiZSBsb2dpY2FsbHkgaW1wb3NzaWJsZSBpZiBlYXJsaWVyIGNvZGUgaXMgY29ycmVjdFxuZGVmIHNwbGl0X2Nvc3QodG90YWwsIHBlb3BsZSk6XG4gICAgYXNzZXJ0IHBlb3BsZSA-IDAsIFwicGVvcGxlIHNob3VsZCBhbHJlYWR5IGJlIHZhbGlkYXRlZCBhcyBwb3NpdGl2ZSBieSB0aGlzIHBvaW50XCJcbiAgICByZXR1cm4gdG90YWwgLyBwZW9wbGUifQ"
 width="100%"
></iframe>

A user mistyping their age is normal and expected, handled gracefully with `try`/`except` from the last unit. A negative `people` count reaching `split_cost`, after validation supposedly already happened earlier, is a sign something in your own logic is broken, exactly the case `assert` is built for.

## assert Can Be Disabled, So Never Rely on It for Real Validation

Python can run with assertions stripped out entirely, using the `-O` optimization flag, which means any check truly required for program correctness, like rejecting bad user input, must use `if` and `raise`, or `try`/`except`, never `assert` alone.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX3VzaW5nX2Fzc2VydF9mb3Jfc2FuaXR5X2NoZWNrcyBjb2RlIDQiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDQucHkiLCJjb2RlIjoiZGVmIHdpdGhkcmF3KGJhbGFuY2UsIGFtb3VudCk6XG4gICAgYXNzZXJ0IGFtb3VudCA-IDAgICAgIyBmaW5lIGFzIGEgc2FuaXR5IGNoZWNrIGR1cmluZyBkZXZlbG9wbWVudFxuICAgIGlmIGFtb3VudCA-IGJhbGFuY2U6ICAgICMgdGhpcyBvbmUgZ2VudWluZWx5IG11c3QgYWx3YXlzIHJ1biwgc28gaXQgaXMgYSByZWFsIGlmLCBub3QgYW4gYXNzZXJ0XG4gICAgICAgIHJhaXNlIFZhbHVlRXJyb3IoXCJJbnN1ZmZpY2llbnQgZnVuZHMuXCIpXG4gICAgcmV0dXJuIGJhbGFuY2UgLSBhbW91bnQifQ"
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
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX3VzaW5nX2Fzc2VydF9mb3Jfc2FuaXR5X2NoZWNrcyBjb2RlIDUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDUucHkiLCJjb2RlIjoiY2xhc3MgQXR0ZW5kZWU6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIG5hbWUsIHJzdnBfY291bnQpOlxuICAgICAgICBhc3NlcnQgaXNpbnN0YW5jZShuYW1lLCBzdHIpIGFuZCBuYW1lLnN0cmlwKCksIFwibmFtZSBtdXN0IGJlIGEgbm9uLWVtcHR5IHN0cmluZ1wiXG4gICAgICAgIGFzc2VydCByc3ZwX2NvdW50ID49IDAsIFwicnN2cF9jb3VudCBjYW5ub3QgYmUgbmVnYXRpdmVcIlxuICAgICAgICBzZWxmLm5hbWUgPSBuYW1lXG4gICAgICAgIHNlbGYucnN2cF9jb3VudCA9IHJzdnBfY291bnRcblxuemFyYSA9IEF0dGVuZGVlKFwiWmFyYVwiLCAyKVxucHJpbnQoZlwie3phcmEubmFtZX06IHt6YXJhLnJzdnBfY291bnR9XCIpXG5cbmJyb2tlbiA9IEF0dGVuZGVlKFwiXCIsIDIpICAgICMgZXJyb3IhIn0"
 width="100%"
></iframe>

Run this, confirm the second creation fails with a clear message naming exactly which assumption was broken, and try writing one more `assert` of your own for a rule this class should always satisfy.

## Conclusion

`assert condition, "message"` states an assumption directly in the code, raising `AssertionError` loudly and immediately the moment that assumption turns out false, making it ideal for catching bugs in your own logic early and documenting your own assumptions for future readers, but never a substitute for validating ordinary, expected bad input, which still belongs to `if`/`raise` or `try`/`except`. Print statements and `assert` both help once you already suspect something specific; the next lesson introduces a tool for when you have no idea yet where the problem even is: Python's own interactive debugger.
