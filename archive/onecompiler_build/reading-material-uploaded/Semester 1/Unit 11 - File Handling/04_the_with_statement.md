## Introduction

Tara's script crashes partway through writing the day's sales report, somewhere between `open()` and the `close()` she dutifully wrote at the end, because of an unrelated bug a few lines in between. The crash means Python jumps straight to reporting the error and stops executing the rest of that block entirely, including her `close()` call, which never runs. The file is left open, possibly with only some of its intended content actually saved to disk, a quiet, easy-to-miss kind of bug that only shows up later, when something tries to read a report that turns out to be incomplete.

The problem is not that Tara forgot to write `close()`. It is that `close()` only runs if every single line before it succeeds, and real code occasionally does not. Python's `with` statement solves this by guaranteeing a file gets closed automatically, even when something goes wrong in between.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-11-file-handling/04_with_statement_guarantees_close.png)

## The Problem With Manual close()

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-11-file-handling-04-the-with-statement-001-b05f645fd8.html"
 width="100%"
></iframe>

The division by zero raises a `ZeroDivisionError` and stops the script immediately. `file.close()`, sitting right there on the next line, never gets a chance to run, because Python never reaches it. The file is left open, and the report is incomplete.

## The with Statement: A Guaranteed Close

`with open(...) as file:` opens a file, runs an indented block using it, and guarantees the file is closed the moment that block ends, whether it finishes normally or is interrupted by an error partway through.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-11-file-handling-04-the-with-statement-002-ec0e657518.html"
 width="100%"
></iframe>

There is no explicit `.close()` anywhere in this code, and none is needed. The instant the indented block under `with` finishes, for any reason at all, Python closes the file automatically.

## Confirming the Guarantee, Even With a Crash

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-11-file-handling-04-the-with-statement-003-9c7c0bee12.html"
 width="100%"
></iframe>

This still raises the exact same `ZeroDivisionError`, and the script still stops, but the file itself is correctly closed regardless, because `with` closes it as the block exits, even when it exits abnormally because of an error. The data already written before the crash is safely saved; only what came after the crash is missing, exactly as it should be.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-11-file-handling/04_with_context_manager_flow.png)


## Rewriting Earlier Lessons With with

Every `open()` and `close()` pair from the last two lessons can be rewritten this way, and from this point in the course onward, it is the way you should always open a file.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-11-file-handling-04-the-with-statement-004-cf827a2ef3.html"
 width="100%"
></iframe>

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-11-file-handling-04-the-with-statement-005-6a19d6266a.html"
 width="100%"
></iframe>

The mode argument, `"r"`, `"w"`, or `"a"`, works exactly as before; `with` changes nothing about how a file behaves, only how reliably it gets closed afterward.

## Manual close() vs with at a Glance

| | Manual open() / close() | with open() as file: |
|---|---|---|
| Closes on normal completion | Yes, if `close()` is reached | Yes, automatically |
| Closes if an error occurs first | No, `close()` is skipped | Yes, guaranteed regardless |
| Extra line needed | `file.close()` | None |
| Recommended for new code | No | Yes |

## Your Turn: Convert to a with Block

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-11-file-handling-04-the-with-statement-006-c638009310.html"
 width="100%"
></iframe>

Notice both operations, appending and then reading back, use the same `with` shape, each one opening, using, and automatically closing the file within its own clean, indented block.

## Conclusion

The `with` statement opens a file, runs an indented block, and guarantees that file is closed the moment the block ends, whether it finishes cleanly or is interrupted by an error partway through, solving exactly the kind of silently-incomplete-file bug a forgotten or skipped `close()` can cause. From here on, prefer `with open(...) as file:` over a manual `open()`/`close()` pair for every file you work with. With safe, reliable opening settled, the next lesson turns to a detail that matters increasingly as projects grow: working with file paths correctly, using `pathlib`.
