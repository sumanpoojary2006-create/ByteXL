## Introduction

Asha's college event signup form, the one she kept hardening with conditions back in the control flow unit, has grown into a small but genuinely used script. Over one busy week she hits three completely different kinds of "wrong." One afternoon, her script will not even start, and Python refuses before a single line runs. Another time, it starts fine, runs for a while, and then stops abruptly partway through, complaining loudly. A third time, it runs perfectly, prints a result with total confidence, and the result is simply incorrect, with no complaint from Python at all.

These are three genuinely different categories of error, and learning to tell them apart on sight is the first real skill this unit builds: **syntax errors**, **runtime errors**, and **logic errors**.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-12-exception-handling/01_three_kinds_of_errors.png)

## Syntax Errors: Python Cannot Even Read This

A syntax error means the code itself does not follow Python's grammar, and Python refuses to run any of it, not even the lines that would have been fine.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-12-exception-handling-01-what-are-errors-syntax-vs-runtime-vs-001-db7f789b3a.html"
 width="100%"
></iframe>

This raises a `SyntaxError`, pointing at the missing colon after the condition. Notice that nothing at all runs, not even a single `print`, because Python checks that an entire file's grammar is valid before executing any of it. A syntax error is the earliest, and in some ways the kindest, kind of error: it is caught before your program ever has a chance to do anything wrong.

## Runtime Errors: Valid Grammar, Fails While Running

A runtime error means the code is grammatically valid Python, and starts running successfully, but encounters a situation it cannot proceed past partway through.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-12-exception-handling-01-what-are-errors-syntax-vs-runtime-vs-002-1189ed9488.html"
 width="100%"
></iframe>

Type "twenty" instead of a number, and this raises a `ValueError` the moment `int()` tries to convert text that does not actually look like a number. The grammar was perfectly fine; the problem only appeared once the program actually tried to act on a specific, real value. This is exactly the kind of failure a syntax check could never catch in advance, because the code itself is valid; only certain inputs at runtime expose the problem.

## Logic Errors: No Complaint at All

A logic error is the quietest and often the most dangerous kind: the code runs perfectly, with no error message whatsoever, and simply produces the wrong answer.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-12-exception-handling-01-what-are-errors-syntax-vs-runtime-vs-003-6c72be88da.html"
 width="100%"
></iframe>

Nothing about this crashes. Python runs it, prints a confident-looking number, and moves on, because operator precedence, from the data types unit, made `b / 2` happen before the addition. The only way to catch a logic error is to actually check the result against what you expected, by hand-tracing, testing, or simply noticing the number looks wrong.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-12-exception-handling/01_logic_error_tests_needed.png)


## Three Kinds of Wrong at a Glance

| | Syntax Error | Runtime Error | Logic Error |
|---|---|---|---|
| When it appears | Before the program starts at all | While the program is running | Never, as an error message |
| Symptom | Python refuses to run anything | The program stops partway through | The program finishes, with a wrong result |
| Example | A missing colon | `int("twenty")` | `a + b / 2` instead of `(a + b) / 2` |
| How you notice | Python tells you immediately | Python tells you when it happens | You have to check the answer yourself |

## Why This Unit Focuses on Runtime Errors

Syntax errors are the easiest to fix, since Python points at them before anything runs at all. Logic errors are covered properly in the debugging unit that closes this course, since they need a different set of habits, tracing and testing, rather than error-handling syntax. This unit, exception handling, is specifically about runtime errors: anticipating that some operation might fail while the program is genuinely running, and deciding in advance how your program should respond when it does, rather than simply crashing.

## Your Turn: Sort the Three

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-12-exception-handling-01-what-are-errors-syntax-vs-runtime-vs-004-e7c08df9df.html"
 width="100%"
></iframe>

Look at each of these three on paper before running anything. Which one would stop Python before any code runs at all? Which one runs fine until one specific moment? And which one might quietly produce a wrong answer under different circumstances, with no warning at all? (A) is a syntax error, missing its closing parenthesis. (B) is a runtime error, a `ZeroDivisionError` the moment it executes. (C) happens to be correct here, but is exactly the shape a logic error takes when the implementation does not match its real intention.

## Conclusion

A syntax error stops Python before any code runs, caught by Python's own grammar check; a runtime error lets valid code start running and then fails partway through, when a specific operation cannot proceed; and a logic error produces no error message at all, simply the wrong answer, discoverable only by checking the result. This unit is about handling runtime errors deliberately, rather than letting them crash your program outright. Before you can handle one, though, you need to be able to read the wall of text Python shows you when one occurs, which is exactly what the next lesson covers: the traceback.
