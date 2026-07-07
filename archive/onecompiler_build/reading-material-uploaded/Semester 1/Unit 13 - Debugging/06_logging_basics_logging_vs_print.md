## Introduction

Zara's RSVP tracker is almost ready to hand in, and she has been leaving informational `print()` statements scattered through it: "Loading attendees...", "Calculated total...", little notes that helped her while debugging. But these prints have no way to be turned off for the final submission without deleting them, no way to tell a routine status update apart from a genuine warning, and no record of when each one happened. What she actually wants is closer to a diary her program keeps of its own behavior, one she can make as detailed or as quiet as she likes, without rewriting a single line of the code that produces it.

Python's built-in `logging` module is built exactly for this, and it solves problems plain `print()` was never designed to solve.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-13-debugging/06_logging_vs_print.png)

## A First Log Message

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-13-debugging-06-logging-basics-logging-vs-print-001-bf5e92b2f1.html"
 width="100%"
></iframe>

This prints both messages, each automatically labelled with its level, `INFO` or `WARNING`, something a plain `print()` never does on its own. `basicConfig(level=logging.INFO)` sets the minimum level that actually gets shown; messages below that level are silently skipped.

## Levels: Not Every Message Deserves the Same Attention

`logging` defines five standard levels, in increasing order of severity: `DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL`. Choosing the right level for each message is the entire point of using `logging` instead of `print`.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-13-debugging-06-logging-basics-logging-vs-print-002-8a5a82c932.html"
 width="100%"
></iframe>

## Filtering by Level Without Touching the Messages Themselves

The real advantage appears when Zara changes a single setting and every `debug` message disappears, while `warning` and `error` messages remain, with no need to find and delete or comment out individual `print()` calls scattered through the codebase.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-13-debugging-06-logging-basics-logging-vs-print-003-bd5a1b18e9.html"
 width="100%"
></iframe>

Setting the level to `WARNING` here silences both `debug` and `info` messages entirely, while `warning` and `error` still print, exactly the kind of selective quieting plain `print()` statements cannot offer without manually editing every line.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-13-debugging/06_logging_level_filter_logbook.png)

*Logging lets you keep useful messages in the program while filtering what appears by seriousness.*

## Why Not Just Use print() for Everything

`print()` always shows, always looks identical regardless of how serious the message is, and offers no built-in way to send messages somewhere other than the screen, like a file, without writing that logic yourself. `logging` solves all three: it can be silenced by level, it labels each message's severity automatically, and `basicConfig(filename=...)` can redirect every message to a log file with no other changes to the code.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-13-debugging-06-logging-basics-logging-vs-print-004-88d08f99c6.html"
 width="100%"
></iframe>

## logging vs print at a Glance

| Need | print() | logging |
|---|---|---|
| Quick one-off check while actively debugging | Perfectly fine | Slight overhead for no real benefit |
| Distinguishing routine info from a genuine warning | No built-in way | `logging.info(...)` vs `logging.warning(...)` |
| Silencing detail messages without deleting code | Not possible | Change one `level` setting |
| Redirecting messages to a file | Requires writing that yourself | `basicConfig(filename=...)` |

## Your Turn: Replace Prints With Levels

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-13-debugging-06-logging-basics-logging-vs-print-005-b8bdd23001.html"
 width="100%"
></iframe>

Run this once with `level=logging.INFO` and once with `level=logging.DEBUG`, and notice the `debug` message only appears in the second run, with no change to the function itself.

## Conclusion

The `logging` module replaces scattered `print()` statements with labelled, level-aware messages, `debug` through `critical`, that can be filtered or redirected to a file by changing a single setting, without rewriting the code that produces them, making it the right choice for anything beyond a quick, throwaway check. With print debugging, `assert`, the debugger, and logging all available, the next lesson covers a strategy that works alongside every one of them: reducing a complicated, multi-file bug down to the smallest possible piece of code that still reproduces it.
