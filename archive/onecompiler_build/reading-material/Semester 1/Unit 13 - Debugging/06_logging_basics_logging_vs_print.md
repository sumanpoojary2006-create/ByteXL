## Introduction

Zara's RSVP tracker is almost ready to hand in, and she has been leaving informational `print()` statements scattered through it: "Loading attendees...", "Calculated total...", little notes that helped her while debugging. But these prints have no way to be turned off for the final submission without deleting them, no way to tell a routine status update apart from a genuine warning, and no record of when each one happened. What she actually wants is closer to a diary her program keeps of its own behavior, one she can make as detailed or as quiet as she likes, without rewriting a single line of the code that produces it.

Python's built-in `logging` module is built exactly for this, and it solves problems plain `print()` was never designed to solve.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-13-debugging/06_logging_vs_print.png)

## A First Log Message

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2xvZ2dpbmdfYmFzaWNzX2xvZ2dpbmdfdnNfcHJpbnQgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6ImltcG9ydCBsb2dnaW5nXG5cbmxvZ2dpbmcuYmFzaWNDb25maWcobGV2ZWw9bG9nZ2luZy5JTkZPKVxuXG5sb2dnaW5nLmluZm8oXCJMb2FkaW5nIGF0dGVuZGVlcyBmcm9tIGZpbGUuXCIpXG5sb2dnaW5nLndhcm5pbmcoXCJBdHRlbmRlZSAnTGluJyBoYXMgYW4gdW51c3VhbGx5IGhpZ2ggcnN2cF9jb3VudDogNTAuXCIpIn0"
 width="100%"
></iframe>

This prints both messages, each automatically labelled with its level, `INFO` or `WARNING`, something a plain `print()` never does on its own. `basicConfig(level=logging.INFO)` sets the minimum level that actually gets shown; messages below that level are silently skipped.

## Levels: Not Every Message Deserves the Same Attention

`logging` defines five standard levels, in increasing order of severity: `DEBUG`, `INFO`, `WARNING`, `ERROR`, and `CRITICAL`. Choosing the right level for each message is the entire point of using `logging` instead of `print`.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2xvZ2dpbmdfYmFzaWNzX2xvZ2dpbmdfdnNfcHJpbnQgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6ImltcG9ydCBsb2dnaW5nXG5cbmxvZ2dpbmcuYmFzaWNDb25maWcobGV2ZWw9bG9nZ2luZy5ERUJVRylcblxubG9nZ2luZy5kZWJ1ZyhcIlBhcnNpbmcgcmF3X3ZhbHVlOiAnMydcIikgICAgICAgICAgIyBmaW5lIGRldGFpbCwgdXNlZnVsIG9ubHkgd2hpbGUgZGVidWdnaW5nXG5sb2dnaW5nLmluZm8oXCJFdmVudCAnQ2x1YiBGYWlyJyBsb2FkZWQgc3VjY2Vzc2Z1bGx5LlwiKSAgICAjIHJvdXRpbmUgc3RhdHVzIHVwZGF0ZVxubG9nZ2luZy53YXJuaW5nKFwicnN2cF9jb3VudCB3YXMgbmVnYXRpdmU7IGNsYW1wZWQgdG8gMC5cIikgIyByZWNvdmVyYWJsZSwgYnV0IHdvcnRoIG5vdGljaW5nXG5sb2dnaW5nLmVycm9yKFwiQ291bGQgbm90IG9wZW4gYXR0ZW5kZWVzLmNzdi5cIikgICAgICAgICAgICAgIyBzb21ldGhpbmcgZmFpbGVkIn0"
 width="100%"
></iframe>

## Filtering by Level Without Touching the Messages Themselves

The real advantage appears when Zara changes a single setting and every `debug` message disappears, while `warning` and `error` messages remain, with no need to find and delete or comment out individual `print()` calls scattered through the codebase.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2xvZ2dpbmdfYmFzaWNzX2xvZ2dpbmdfdnNfcHJpbnQgY29kZSAzIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAzLnB5IiwiY29kZSI6ImltcG9ydCBsb2dnaW5nXG5cbmxvZ2dpbmcuYmFzaWNDb25maWcobGV2ZWw9bG9nZ2luZy5XQVJOSU5HKVxuXG5sb2dnaW5nLmRlYnVnKFwiVGhpcyBkZXRhaWxlZCBtZXNzYWdlIHdpbGwgbm90IGJlIHNob3duLlwiKVxubG9nZ2luZy5pbmZvKFwiTmVpdGhlciB3aWxsIHRoaXMgcm91dGluZSBzdGF0dXMgdXBkYXRlLlwiKVxubG9nZ2luZy53YXJuaW5nKFwiVGhpcyB3YXJuaW5nIHdpbGwgYmUgc2hvd24uXCIpXG5sb2dnaW5nLmVycm9yKFwiVGhpcyBlcnJvciB3aWxsIGJlIHNob3duIHRvby5cIikifQ"
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
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2xvZ2dpbmdfYmFzaWNzX2xvZ2dpbmdfdnNfcHJpbnQgY29kZSA0IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA0LnB5IiwiY29kZSI6ImltcG9ydCBsb2dnaW5nXG5cbmxvZ2dpbmcuYmFzaWNDb25maWcobGV2ZWw9bG9nZ2luZy5JTkZPKVxuXG4jIEEgZ2VudWluZSBidWcgd29ydGggaW52ZXN0aWdhdGluZywgZm91bmQgdmlhIGxvZ2dpbmcgaW5zdGVhZCBvZiBwcmludDpcbmF0dGVuZGVlcyA9IFsoXCJaYXJhXCIsIDIpLCAoXCJMaW5cIiwgLTEpXVxuZm9yIG5hbWUsIGNvdW50IGluIGF0dGVuZGVlczpcbiAgICBpZiBjb3VudCA8IDA6XG4gICAgICAgIGxvZ2dpbmcud2FybmluZyhmXCJ7bmFtZX0gaGFzIGEgbmVnYXRpdmUgcnN2cF9jb3VudDoge2NvdW50fVwiKVxuICAgIGVsc2U6XG4gICAgICAgIGxvZ2dpbmcuaW5mbyhmXCJ7bmFtZX06IHtjb3VudH0gUlNWUHNcIikifQ"
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
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2xvZ2dpbmdfYmFzaWNzX2xvZ2dpbmdfdnNfcHJpbnQgY29kZSA1IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA1LnB5IiwiY29kZSI6ImltcG9ydCBsb2dnaW5nXG5cbmxvZ2dpbmcuYmFzaWNDb25maWcobGV2ZWw9bG9nZ2luZy5JTkZPKVxuXG5kZWYgdG90YWxfcnN2cHMoYXR0ZW5kZWVzKTpcbiAgICBsb2dnaW5nLmRlYnVnKGZcIlN0YXJ0aW5nIHRvdGFsX3JzdnBzIHdpdGgge2xlbihhdHRlbmRlZXMpfSBhdHRlbmRlZXMuXCIpXG4gICAgdG90YWwgPSBzdW0oY291bnQgZm9yIF8sIGNvdW50IGluIGF0dGVuZGVlcylcbiAgICBsb2dnaW5nLmluZm8oZlwiQ29tcHV0ZWQgdG90YWw6IHt0b3RhbH1cIilcbiAgICByZXR1cm4gdG90YWxcblxucHJpbnQodG90YWxfcnN2cHMoWyhcIlphcmFcIiwgMiksIChcIkxpblwiLCAzKV0pKSJ9"
 width="100%"
></iframe>

Run this once with `level=logging.INFO` and once with `level=logging.DEBUG`, and notice the `debug` message only appears in the second run, with no change to the function itself.

## Conclusion

The `logging` module replaces scattered `print()` statements with labelled, level-aware messages, `debug` through `critical`, that can be filtered or redirected to a file by changing a single setting, without rewriting the code that produces them, making it the right choice for anything beyond a quick, throwaway check. With print debugging, `assert`, the debugger, and logging all available, the next lesson covers a strategy that works alongside every one of them: reducing a complicated, multi-file bug down to the smallest possible piece of code that still reproduces it.
