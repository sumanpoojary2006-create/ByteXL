## Introduction

Zara's RSVP tracker now spans four files: `attendee.py`, `event.py`, a CSV loader, and `main.py`, and somewhere in that web of imports, one specific event's attendee count comes out wrong. Stepping through the entire program with the debugger from the file the CSV is loaded all the way to the final printed summary works, but it is slow, and most of what she steps through is completely fine. What she actually wants is to strip away everything that is not part of the problem, until only the smallest possible piece of code that still reproduces the bug remains.

This is called finding a **minimal failing case**, and it is one of the most powerful debugging strategies precisely because it works alongside every tool from this entire unit, making each of them faster and clearer to use.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-13-debugging/07_minimal_failing_case.png)

## Why Smaller Is Genuinely Easier to Debug

A bug inside a four-file, multi-class program could be caused by dozens of interacting pieces. A bug inside five lines has nowhere left to hide.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X2lzb2xhdGluZ19hX21pbmltYWxfZmFpbGluZ19jYXNlIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiIjIFRoZSBmdWxsIHBpcGVsaW5lOiBDU1YgZmlsZSAtPiBsb2FkZXIgZnVuY3Rpb24gLT4gQXR0ZW5kZWUgb2JqZWN0cyAtPiBFdmVudCAtPiBzdW1tYXJ5XG4jIFNvbWV3aGVyZSBpbiB0aGVyZSwgb25lIGNvdW50IGlzIHdyb25nLiBXaGVyZSwgc3BlY2lmaWNhbGx5PyJ9"
 width="100%"
></iframe>

Rather than debugging the whole pipeline at once, Zara starts removing pieces, one at a time, checking after each removal whether the bug still reproduces.

## Step One: Reproduce It Outside the Full Program

The first move is confirming the bug does not actually require the CSV file, the command-line entry point, or any of the surrounding machinery, only the specific data and the specific function that mishandles it.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X2lzb2xhdGluZ19hX21pbmltYWxfZmFpbGluZ19jYXNlIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJkZWYgdG90YWxfcnN2cHMoYXR0ZW5kZWVzKTpcbiAgICByZXR1cm4gc3VtKGF0dGVuZGVlLnJzdnBfY291bnQgZm9yIGF0dGVuZGVlIGluIGF0dGVuZGVlcylcblxuY2xhc3MgQXR0ZW5kZWU6XG4gICAgZGVmIF9faW5pdF9fKHNlbGYsIG5hbWUsIHJzdnBfY291bnQpOlxuICAgICAgICBzZWxmLm5hbWUgPSBuYW1lXG4gICAgICAgIHNlbGYucnN2cF9jb3VudCA9IHJzdnBfY291bnRcblxuYXR0ZW5kZWVzID0gW0F0dGVuZGVlKFwiWmFyYVwiLCAyKSwgQXR0ZW5kZWUoXCJMaW5cIiwgXCIzXCIpXVxucHJpbnQodG90YWxfcnN2cHMoYXR0ZW5kZWVzKSkgICAgIyBlcnJvciEifQ"
 width="100%"
></iframe>

This five-line reproduction, with no file reading and no command-line arguments at all, already crashes with the exact same `TypeError` Zara saw in the full program, confirming the bug lives in how a count becomes a string somewhere, not in anything related to files or the program's entry point.

## Step Two: Remove Anything That Does Not Affect the Crash

With the bug isolated outside the full program, Zara keeps stripping. Does the `Attendee` class even matter, or would a plain list of numbers crash the same way?

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X2lzb2xhdGluZ19hX21pbmltYWxfZmFpbGluZ19jYXNlIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiJjb3VudHMgPSBbMiwgXCIzXCJdXG5wcmludChzdW0oY291bnRzKSkgICAgIyBlcnJvciEifQ"
 width="100%"
></iframe>

It does crash, identically, which is a genuinely useful discovery: the bug has nothing to do with the `Attendee` class at all. It is purely about a string ending up inside a list of numbers, somewhere upstream, most likely in whatever code reads the CSV file and forgets to convert the text into an integer.

## A Minimal Case Turns a Vague Bug Into a Specific Question

Once reduced this far, "why is my whole RSVP tracker wrong" has become "why does my CSV-reading code leave one value as a string instead of converting it with `int()`," a question small enough to answer by reading a handful of lines, rather than tracing through four files.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X2lzb2xhdGluZ19hX21pbmltYWxfZmFpbGluZ19jYXNlIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiIjIEJlZm9yZSBpc29sYXRpbmc6IFwidGhlIHRvdGFsIGlzIHdyb25nIHNvbWV3aGVyZSBpbiB0aGlzIHdob2xlIHByb2plY3RcIlxuIyBBZnRlciBpc29sYXRpbmc6IFwidGhlIENTViBsb2FkZXIgZm9yZ290IHRvIGNhbGwgaW50KCkgb24gb25lIGNvbHVtblwiIn0"
 width="100%"
></iframe>

This is the real payoff: minimization does not fix the bug by itself, but it transforms a vague, intimidating problem into a small, specific, answerable one.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-13-debugging/07_minimal_case_shrinking_funnel.png)

*A minimal failing case removes everything except the smallest code needed to reproduce the same bug.*

## Minimal Failing Cases at a Glance

| Step | Action |
|---|---|
| 1 | Reproduce the bug outside the full program, with no files or command-line input involved |
| 2 | Remove one piece at a time (a class, a loop, an argument), rerunning after each removal |
| 3 | Keep only what is still necessary to trigger the exact same failure |
| 4 | Use the now-tiny reproduction with print debugging, `assert`, or the debugger |

## Your Turn: Shrink the Bug

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X2lzb2xhdGluZ19hX21pbmltYWxfZmFpbGluZ19jYXNlIGNvZGUgNSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5weSIsImNvZGUiOiJkZWYgZGlzY291bnRlZF90b3RhbChwcmljZXMsIGRpc2NvdW50X3BlcmNlbnQpOlxuICAgIHRvdGFsID0gc3VtKHByaWNlcylcbiAgICByZXR1cm4gdG90YWwgLSAodG90YWwgKiBkaXNjb3VudF9wZXJjZW50IC8gMTAwKVxuXG5jbGFzcyBDYXJ0OlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBwcmljZXMpOlxuICAgICAgICBzZWxmLnByaWNlcyA9IHByaWNlc1xuXG5jYXJ0ID0gQ2FydChbMTAwLCAyMDAsIFwiNTBcIl0pXG5wcmludChkaXNjb3VudGVkX3RvdGFsKGNhcnQucHJpY2VzLCAxMCkpICAgICMgZXJyb3IhIn0"
 width="100%"
></iframe>

Strip this down the way Zara did: first confirm the bug survives without the `Cart` class at all, using a plain list directly, and identify the smallest possible reproduction that still crashes with the same error.

## Conclusion

Isolating a minimal failing case means stripping away everything not actually required to trigger a bug, one piece at a time, until a small, self-contained reproduction remains, turning a vague "something is wrong somewhere in this project" into a specific, answerable question. This strategy makes every other tool in this unit faster to use, since print statements, `assert`, and the debugger are all easier to apply to five lines than to four files. The next lesson covers what to do once you are stuck even after minimizing: explaining the problem clearly, often to nobody but yourself.
