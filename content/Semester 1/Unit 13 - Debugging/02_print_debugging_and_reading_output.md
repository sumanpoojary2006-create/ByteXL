## Introduction

With the panic gone, Zara still has a real bug: somewhere between reading her RSVP file and printing the final total, one attendee's count is arriving as the text `"three"` instead of the number `3`. The traceback names the line that crashed, but not the earlier line that actually caused the bad value to exist in the first place. To find that, she needs to watch the data as it moves through her program, step by step, and the simplest tool for that job is one she already knows: `print()`, used deliberately as an investigation tool rather than just a way to show final output.

This is called **print debugging**, and despite being almost embarrassingly simple, it remains one of the most useful techniques in any programmer's toolkit, beginner or expert.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-13-debugging/02_print_debugging_tracing_values.png)

## Placing Prints to Narrow the Search

Rather than guessing which line is wrong, Zara adds a print right before and right after the suspicious step, turning a vague "something in here is wrong" into a precise before-and-after comparison.

```python
import traceback

def parse_rsvp_count(raw_value):
    print(f"raw_value before parsing: {raw_value!r}")
    count = int(raw_value)
    print(f"count after parsing: {count!r}")
    return count

try:
    parse_rsvp_count("three")    # error!
except ValueError:
    print(traceback.format_exc())
```

The first print runs and shows `raw_value before parsing: 'three'`, then the program crashes on the `int()` line, before the second print ever has a chance to run. That gap, between the printed value before and the crash itself, is exactly where the problem lives: the raw text itself is already bad, long before this function tries to convert it.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-13-debugging/02_print_probe_timeline.png)

*A print probe is useful because it marks the exact checkpoint where a value stops matching your expectation.*

## Why !r Matters More Than It Looks

Notice the `!r` inside the f-string above. It prints the value's `repr()`, the precise, unambiguous form, rather than its friendly display form, which matters enormously when debugging.

```python
value = "3 "    # a sneaky trailing space
print(f"Value: {value}")       # Value: 3   (the space is invisible here)
print(f"Value: {value!r}")     # Value: '3 '   (the space is now visible)
```

A trailing space, an empty string versus `None`, or `"3"` versus `3` can look identical with a plain print but completely different with `!r`. This single habit catches an entire category of bugs that are otherwise nearly invisible.

## Tracing a Value Across Multiple Functions

Print debugging is most useful when a value passes through several functions before something goes wrong, since it lets you watch exactly where the value stops matching what you expected.

```python
import traceback

def load_counts(raw_counts):
    print(f"loaded: {raw_counts!r}")
    return raw_counts

def total_rsvps(raw_counts):
    counts = load_counts(raw_counts)
    print(f"about to sum: {counts!r}")
    return sum(counts)

try:
    total_rsvps([2, 3, "1"])    # error!
except TypeError:
    print(traceback.format_exc())
```

The prints show the list arriving unchanged at each step, with the bad `"1"` already present from the very first line, which immediately tells Zara the problem is in whoever built this list, not in `load_counts` or `total_rsvps` themselves.

## The Discipline of Removing Prints Afterward

Print debugging's biggest weakness is also the easiest to manage: leftover debug prints clutter real output and confuse anyone reading it later, your future self included. Once a bug is found and fixed, remove the prints you added specifically to find it, or comment them out clearly if you genuinely expect to need them again soon.

```text
def total_rsvps(raw_counts):
    counts = load_counts(raw_counts)
    # print(f"about to sum: {counts!r}")    # debug print, remove before committing
    return sum(counts)
```

## Print Debugging at a Glance

| Habit | Why |
|---|---|
| Print right before and right after a suspicious line | Narrows exactly where a value stops matching expectations |
| Use `!r` for the value, not just plain f-string interpolation | Reveals hidden differences like spaces, types, or `None` |
| Trace a value across multiple functions, not just one | Finds where a bad value first entered, not just where it crashed |
| Remove or comment out debug prints once the bug is fixed | Keeps real program output clean and uncluttered |

## Your Turn: Trace the Mismatch

```python
import traceback

def average_rating(ratings):
    total = sum(ratings)
    count = len(ratings)
    return total / count

try:
    print(average_rating([4, 5, "3"]))    # error!
except TypeError:
    print(traceback.format_exc())
```

Add print statements inside `average_rating` to show `ratings`, `total`, and `count` before the division. Run it, read the printed values with `!r`, and identify exactly which value is not what the function expected.

## Conclusion

Print debugging means placing deliberate, temporary `print()` calls, ideally with `!r`, around suspicious lines to watch a value's actual state at each step, narrowing a vague bug into a precise, specific mismatch, then removing those prints once the cause is found. It is simple, universal, and works in any Python environment, but it does not scale well to deeply nested logic or long-running programs, exactly the gap the next lesson's tool, `assert`, helps close by encoding your expectations directly into the code itself.
