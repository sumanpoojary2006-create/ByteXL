## Introduction

Back in the control flow unit, Asha's signup form learned to reject obviously bad input using conditions: checking `.isdigit()` before trusting a number, checking a range before accepting an age. That lesson ended with an honest admission, that conditions alone cannot catch every possible error, and that a more complete tool was still coming. This is that tool. No matter how many conditions Asha writes in advance, she cannot anticipate every single way a real operation might fail, and a single unanticipated crash still takes down her entire program.

Python's `try` and `except` let you run risky code, watch for it to fail, and respond on your own terms instead of letting the whole program crash.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-12-exception-handling/03_try_except_safety_net.png)

## The Shape of try and except

Code that might fail goes inside a `try` block; code that runs only if it actually does fail goes inside a matching `except` block.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-12-exception-handling-03-try-and-except-001-5bf7a07bbb.html"
 width="100%"
></iframe>

Type "20", and the `try` block succeeds completely, and the `except` block is simply skipped, never running at all. Type "twenty", and `int()` raises a `ValueError` partway through the `try` block; Python immediately jumps to the matching `except`, prints the friendly message, and the program continues running normally afterward, rather than crashing outright.

## Without try/except, the Same Failure Crashes Everything

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-12-exception-handling-03-try-and-except-002-c07c6afd4d.html"
 width="100%"
></iframe>

Type "twenty" here, and the program stops immediately with an unhandled `ValueError`, exactly the crash from the last lesson's traceback. The logic was identical; only the presence of `try`/`except` decided whether that failure ended the whole program or was handled gracefully and survived.

## try/except Lets the Program Keep Going

The real value of `except` is not just preventing an ugly traceback. It is that code after the `try`/`except` block keeps running normally, something a crash could never allow.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-12-exception-handling-03-try-and-except-003-2f2a299951.html"
 width="100%"
></iframe>

Whether the conversion succeeded or failed, `age` ends up with some usable value by the time execution reaches the final `print`, and that line runs either way. This is the core promise of exception handling: anticipate a specific failure, decide what should happen instead, and let the rest of your program continue with confidence.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-12-exception-handling/03_try_except_continue_flow.png)


## Catching Any Exception (and Why to Be Careful)

Leaving the exception type off `except` entirely catches anything at all that goes wrong inside the `try` block.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-12-exception-handling-03-try-and-except-004-fa28dd12c3.html"
 width="100%"
></iframe>

This works, but it is usually a mistake to write carelessly. A bare `except` catches every kind of failure indiscriminately, including ones you never anticipated and might not actually want to hide, silently swallowing bugs that you would otherwise have noticed immediately from a crash. The next lesson covers catching specific exception types deliberately, which is almost always the better habit.

## try/except at a Glance

| Part | Purpose |
|---|---|
| `try:` | Marks code that might fail |
| `except ExceptionType:` | Runs only if that specific kind of failure actually happens |
| If the `try` block succeeds | The `except` block is skipped entirely |
| If the `try` block fails | Python jumps straight to the matching `except`, then continues after the whole block |

## Your Turn: Protect a Risky Calculation

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-12-exception-handling-03-try-and-except-005-4d798d2362.html"
 width="100%"
></iframe>

Try entering "abc" for the total, then try entering 0 for the number of people, and notice each failure is caught by its own clearly named `except`, with the program surviving both, rather than crashing on either.

## Conclusion

`try` wraps code that might fail, and a matching `except` runs only if that failure actually happens, letting your program respond deliberately and keep running afterward, instead of crashing outright the way an unprotected operation would. A bare `except`, with no exception type named, catches everything indiscriminately, which is usually too broad to be a good habit. The next lesson builds directly on the example above: handling several different, specific kinds of failure, each with its own tailored response.
