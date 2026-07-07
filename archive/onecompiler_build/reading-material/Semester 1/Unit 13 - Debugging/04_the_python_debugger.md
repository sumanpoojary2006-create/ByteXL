## Introduction

Print debugging works well once Zara has a specific suspicion about where things go wrong, but her RSVP tracker's worst bug so far is different: somewhere deep inside three nested function calls, a total comes out wrong, and she genuinely has no idea which call is responsible. Sprinkling print statements through three functions, rerunning, reading the output, then adding more prints in a slightly different place is slow and easy to lose track of. What she actually wants is to pause the program mid-run, right at the suspicious spot, and look around freely: check any variable, run any expression, take one step forward, and decide what to check next, all without editing the code at all.

That is exactly what Python's built-in debugger, `pdb`, is for.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-13-debugging/04_python_debugger_paused_execution.png)

## Pausing a Program with breakpoint()

Python's built-in `breakpoint()` function, called anywhere in your code, pauses execution at exactly that line and drops you into an interactive debugger prompt, `(Pdb)`, right inside your terminal.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3RoZV9weXRob25fZGVidWdnZXIgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6ImRlZiB0b3RhbF9yc3ZwcyhhdHRlbmRlZXMpOlxuICAgIHRvdGFsID0gMFxuICAgIGZvciBhdHRlbmRlZSBpbiBhdHRlbmRlZXM6XG4gICAgICAgIGJyZWFrcG9pbnQoKVxuICAgICAgICB0b3RhbCArPSBhdHRlbmRlZS5yc3ZwX2NvdW50XG4gICAgcmV0dXJuIHRvdGFsIn0"
 width="100%"
></iframe>

Run this, and the moment the loop reaches `breakpoint()`, the program freezes there, handing control to you. Nothing past that line has happened yet, and everything before it, including `total` and the current `attendee`, is available to inspect.

## A Debugger Session, Step by Step

Once paused, a small set of commands does almost everything you need. Typing a variable's name prints its current value; `n` (next) runs the current line and pauses again on the following one; `c` (continue) resumes normal execution until the next `breakpoint()` or the program's end; `q` (quit) stops the debugger and the program entirely.

```text
> tracker.py(4)total_rsvps()
-> total += attendee.rsvp_count
(Pdb) attendee.name
'Zara'
(Pdb) attendee.rsvp_count
2
(Pdb) total
0
(Pdb) n
> tracker.py(3)total_rsvps()
-> for attendee in attendees:
(Pdb) total
2
(Pdb) c
```

Notice this is a real, live conversation with the running program, not a guess based on printed text: Zara can check `attendee.rsvp_count`'s exact value before it is even added, confirm `total` afterward, and only then decide whether to step again or let the program continue.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-13-debugging/04_breakpoint_pause_controls.png)

*A breakpoint pauses execution so you can inspect the current state before choosing how the program should move next.*

## p and pp: Printing Any Expression

The `p` command prints any expression, not just a single variable's name, which is useful for checking something more specific than a bare variable.

```text
(Pdb) p attendee.rsvp_count > 5
False
(Pdb) p [a.name for a in attendees]
['Zara', 'Lin', 'Omar']
```

`pp` ("pretty print") does the same thing but formats longer or nested results, like lists of dictionaries, more readably than `p` would.

## l: Seeing Where You Are

`l` (list) prints the source code surrounding the current paused line, with an arrow marking exactly where execution stopped, useful after stepping through several lines and losing track of the surrounding context.

```text
(Pdb) l
  1     def total_rsvps(attendees):
  2         total = 0
  3         for attendee in attendees:
  4  ->         total += attendee.rsvp_count
  5         return total
```

## pdb Commands at a Glance

| Command | Effect |
|---|---|
| `breakpoint()` | Pauses the program at this exact line, in your own code |
| (just type a name) | Prints that variable's current value |
| `p expression` | Prints the result of any expression, not just a variable |
| `n` | Runs the current line, pauses on the next one |
| `c` | Continues running until the next `breakpoint()` or the program ends |
| `l` | Shows the source code around the current paused line |
| `q` | Quits the debugger and stops the program |

## Your Turn: Pause and Inspect

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA0X3RoZV9weXRob25fZGVidWdnZXIgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6ImRlZiBhdmVyYWdlX3JzdnBzKGF0dGVuZGVlcyk6XG4gICAgdG90YWwgPSAwXG4gICAgY291bnQgPSAwXG4gICAgZm9yIGF0dGVuZGVlIGluIGF0dGVuZGVlczpcbiAgICAgICAgYnJlYWtwb2ludCgpXG4gICAgICAgIHRvdGFsICs9IGF0dGVuZGVlLnJzdnBfY291bnRcbiAgICAgICAgY291bnQgKz0gMVxuICAgIHJldHVybiB0b3RhbCAvIGNvdW50XG5cbmNsYXNzIEF0dGVuZGVlOlxuICAgIGRlZiBfX2luaXRfXyhzZWxmLCBuYW1lLCByc3ZwX2NvdW50KTpcbiAgICAgICAgc2VsZi5uYW1lID0gbmFtZVxuICAgICAgICBzZWxmLnJzdnBfY291bnQgPSByc3ZwX2NvdW50XG5cbmF2ZXJhZ2VfcnN2cHMoW0F0dGVuZGVlKFwiWmFyYVwiLCAyKSwgQXR0ZW5kZWUoXCJMaW5cIiwgMyldKSJ9"
 width="100%"
></iframe>

Run this in a real terminal, not just read it. At the first pause, check `attendee.name`, `total`, and `count`, then use `n` a few times and watch each value change, then `c` to let it finish.

## Conclusion

Python's built-in debugger, started with `breakpoint()`, pauses a running program at an exact line and lets you inspect any variable or expression interactively, step forward one line at a time with `n`, and resume freely with `c`, replacing slow rounds of print-edit-rerun with a single live conversation with the running program. This lesson covered pausing and basic inspection; the next lesson goes deeper into stepping through nested function calls and reading the call stack, exactly the tool Zara needs for a bug buried three functions deep.
