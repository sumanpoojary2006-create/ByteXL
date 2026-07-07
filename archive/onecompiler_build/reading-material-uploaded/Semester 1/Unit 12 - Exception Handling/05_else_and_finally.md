## Introduction

Asha's registration script needs two more refinements that `try` and `except` alone do not quite give her. First, she wants one block of code that runs only when the risky part genuinely succeeded, separate from the `try` block itself, to keep the "might fail" code and the "now that it worked" code visually distinct. Second, she wants a closing message, "registration attempt finished," to print every single time, whether the attempt succeeded or failed, without duplicating that print statement inside both the success path and every single `except`.

Python's `try` structure has two more optional parts built exactly for this: `else`, which runs only if the `try` block succeeded, and `finally`, which runs no matter what happened.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-12-exception-handling/05_else_and_finally_blocks.png)

## else: Only on Success

An `else` clause attached to a `try` runs only if the `try` block completed with no exception at all.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-12-exception-handling-05-else-and-finally-001-c357c05404.html"
 width="100%"
></iframe>

Type a real number, and the `try` succeeds, the `except` is skipped, and `else` runs, printing the thank-you message. Type letters, and the `try` fails, the `except` runs instead, and `else` is skipped entirely, because it only ever runs after a clean, exception-free `try`.

## Why Not Just Put That Code Inside try?

You could write the success message as the last line inside the `try` block itself, and it would behave almost identically here. The real value of `else` shows up once the `try` block has several risky lines: it draws a clear, visual line between "the part that might fail" and "the part that only matters once we know it did not," which keeps a longer `try` block easier to read and reason about.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-12-exception-handling-05-else-and-finally-002-1dcd464b46.html"
 width="100%"
></iframe>

## finally: No Matter What

A `finally` clause runs every single time, whether the `try` block succeeded, failed and was caught, or even failed in a way no `except` caught at all.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-12-exception-handling-05-else-and-finally-003-f51e344272.html"
 width="100%"
></iframe>

"Registration attempt finished." prints whether you type a real number or nonsense, because `finally` does not care which path was taken, only that the `try` structure as a whole has now finished running.

## finally Is for Cleanup That Must Always Happen

`finally`'s real purpose is guaranteeing cleanup, the same guarantee the `with` statement gave you automatically for files, in the file handling unit, except `finally` is the general-purpose version, usable for any cleanup at all, not just closing files.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-12-exception-handling/05_else_finally_cleanup_success.png)


<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-12-exception-handling-05-else-and-finally-004-2e6ec483e7.html"
 width="100%"
></iframe>

The connection-closing message prints whether the entry was valid, invalid, or even zero, exactly the unconditional guarantee `finally` exists to provide.

## All Four Parts Together

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-12-exception-handling-05-else-and-finally-005-645bce5f9b.html"
 width="100%"
></iframe>

Read this top to bottom as a single story: attempt the risky thing, handle it if it fails, celebrate quietly if it succeeded, and clean up regardless, every single time.

## try Structure at a Glance

| Clause | Runs When |
|---|---|
| `try:` | Always attempted first |
| `except ExceptionType:` | Only if that specific failure happened |
| `else:` | Only if the `try` block succeeded, with no exception at all |
| `finally:` | Always, regardless of success, failure, or which `except` ran |

## Your Turn: All Four Clauses

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-12-exception-handling-05-else-and-finally-006-1ac00db942.html"
 width="100%"
></iframe>

Run this once with valid numbers and once with invalid text, and trace which clauses ran each time, confirming `finally`'s message appeared in both runs while `else`'s message appeared in only one.

## Conclusion

`else`, attached to a `try`, runs only when the `try` block completed with no exception, keeping success-only code visually separate from the risky code itself, while `finally` runs unconditionally, success or failure, making it the right place for cleanup that must always happen regardless of outcome. Together with `try` and `except`, these four clauses give you precise control over every path a risky operation can take. So far every exception in this unit has come from Python itself; the next lesson covers deliberately raising one of your own, on purpose, when your own code detects a problem.
