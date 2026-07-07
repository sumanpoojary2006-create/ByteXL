## Introduction

Tara's script crashes partway through writing the day's sales report, somewhere between `open()` and the `close()` she dutifully wrote at the end, because of an unrelated bug a few lines in between. The crash means Python jumps straight to reporting the error and stops executing the rest of that block entirely, including her `close()` call, which never runs. The file is left open, possibly with only some of its intended content actually saved to disk, a quiet, easy-to-miss kind of bug that only shows up later, when something tries to read a report that turns out to be incomplete.

The problem is not that Tara forgot to write `close()`. It is that `close()` only runs if every single line before it succeeds, and real code occasionally does not. Python's `with` statement solves this by guaranteeing a file gets closed automatically, even when something goes wrong in between.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-11-file-handling/04_with_statement_guarantees_close.png)

## The Problem With Manual close()

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3RoZV93aXRoX3N0YXRlbWVudCBjb2RlIDEiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDEucHkiLCJjb2RlIjoiZmlsZSA9IG9wZW4oXCJzYWxlc19yZXBvcnQudHh0XCIsIFwid1wiKVxuZmlsZS53cml0ZShcIkRheSAxIFNhbGVzIFJlcG9ydFxcblwiKVxudG90YWwgPSAxMDAgLyAwICAgICAgICAgICMgYW4gdW5yZWxhdGVkIGJ1ZywgY3Jhc2hlcyByaWdodCBoZXJlXG5maWxlLndyaXRlKFwiVG90YWw6IFwiICsgc3RyKHRvdGFsKSArIFwiXFxuXCIpXG5maWxlLmNsb3NlKCkgICAgICAgICAgICAgICMgbmV2ZXIgcmVhY2hlZCEifQ"
 width="100%"
></iframe>

The division by zero raises a `ZeroDivisionError` and stops the script immediately. `file.close()`, sitting right there on the next line, never gets a chance to run, because Python never reaches it. The file is left open, and the report is incomplete.

## The with Statement: A Guaranteed Close

`with open(...) as file:` opens a file, runs an indented block using it, and guarantees the file is closed the moment that block ends, whether it finishes normally or is interrupted by an error partway through.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3RoZV93aXRoX3N0YXRlbWVudCBjb2RlIDIiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDIucHkiLCJjb2RlIjoid2l0aCBvcGVuKFwic2FsZXNfcmVwb3J0LnR4dFwiLCBcIndcIikgYXMgZmlsZTpcbiAgICBmaWxlLndyaXRlKFwiRGF5IDEgU2FsZXMgUmVwb3J0XFxuXCIpXG4gICAgZmlsZS53cml0ZShcIlRvdGFsOiA0NTAwXFxuXCIpIn0"
 width="100%"
></iframe>

There is no explicit `.close()` anywhere in this code, and none is needed. The instant the indented block under `with` finishes, for any reason at all, Python closes the file automatically.

## Confirming the Guarantee, Even With a Crash

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3RoZV93aXRoX3N0YXRlbWVudCBjb2RlIDMiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDMucHkiLCJjb2RlIjoid2l0aCBvcGVuKFwic2FsZXNfcmVwb3J0LnR4dFwiLCBcIndcIikgYXMgZmlsZTpcbiAgICBmaWxlLndyaXRlKFwiRGF5IDEgU2FsZXMgUmVwb3J0XFxuXCIpXG4gICAgdG90YWwgPSAxMDAgLyAwICAgICAgICAgICMgc3RpbGwgY3Jhc2hlcyBoZXJlXG4gICAgZmlsZS53cml0ZShcIlRvdGFsOiBcIiArIHN0cih0b3RhbCkgKyBcIlxcblwiKSJ9"
 width="100%"
></iframe>

This still raises the exact same `ZeroDivisionError`, and the script still stops, but the file itself is correctly closed regardless, because `with` closes it as the block exits, even when it exits abnormally because of an error. The data already written before the crash is safely saved; only what came after the crash is missing, exactly as it should be.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-11-file-handling/04_with_context_manager_flow.png)


## Rewriting Earlier Lessons With with

Every `open()` and `close()` pair from the last two lessons can be rewritten this way, and from this point in the course onward, it is the way you should always open a file.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3RoZV93aXRoX3N0YXRlbWVudCBjb2RlIDQiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDQucHkiLCJjb2RlIjoid2l0aCBvcGVuKFwiYXR0ZW5kZWVzLnR4dFwiLCBcIndcIikgYXMgZmlsZTogICAgIyByZWNyZWF0aW5nIHRoZSBmaWxlIGZyb20gZWFybGllciBsZXNzb25zXG4gICAgZmlsZS53cml0ZWxpbmVzKFtcIkExMDFcXG5cIiwgXCJBMTAyXFxuXCIsIFwiQTEwM1xcblwiXSlcblxud2l0aCBvcGVuKFwiYXR0ZW5kZWVzLnR4dFwiLCBcInJcIikgYXMgZmlsZTpcbiAgICBmb3IgbGluZSBpbiBmaWxlOlxuICAgICAgICBwcmludChsaW5lLnN0cmlwKCkpIn0"
 width="100%"
></iframe>

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3RoZV93aXRoX3N0YXRlbWVudCBjb2RlIDUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDUucHkiLCJjb2RlIjoid2l0aCBvcGVuKFwiZmVzdF9sb2cudHh0XCIsIFwiYVwiKSBhcyBmaWxlOlxuICAgIGZpbGUud3JpdGUoXCJTdGFsbCBjbG9zZWQgYXQgNiBQTVxcblwiKSJ9"
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
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3RoZV93aXRoX3N0YXRlbWVudCBjb2RlIDYiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDYucHkiLCJjb2RlIjoid2l0aCBvcGVuKFwiYXR0ZW5kZWVzLnR4dFwiLCBcImFcIikgYXMgZmlsZTpcbiAgICBmaWxlLndyaXRlKFwiQTEwOFxcblwiKVxuXG53aXRoIG9wZW4oXCJhdHRlbmRlZXMudHh0XCIsIFwiclwiKSBhcyBmaWxlOlxuICAgIHByaW50KGZpbGUucmVhZCgpKSJ9"
 width="100%"
></iframe>

Notice both operations, appending and then reading back, use the same `with` shape, each one opening, using, and automatically closing the file within its own clean, indented block.

## Conclusion

The `with` statement opens a file, runs an indented block, and guarantees that file is closed the moment the block ends, whether it finishes cleanly or is interrupted by an error partway through, solving exactly the kind of silently-incomplete-file bug a forgotten or skipped `close()` can cause. From here on, prefer `with open(...) as file:` over a manual `open()`/`close()` pair for every file you work with. With safe, reliable opening settled, the next lesson turns to a detail that matters increasingly as projects grow: working with file paths correctly, using `pathlib`.
