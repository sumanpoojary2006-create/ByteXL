## Introduction

Zara's deepest bug yet lives across three functions: `main` calls `summarize_event`, which calls `total_rsvps`, which calls `attendee.rsvp_count` on each attendee in a loop. The final summary is wrong, but `c` and a single `breakpoint()` only show her one function's local variables at a time. What she actually needs is to step **into** a function call, follow execution as it moves between functions, and see the full chain of who-called-whom, called the **call stack**, so she can find exactly which function along that chain first introduces the wrong value.

`pdb` supports exactly this, with two commands beyond the `n` and `c` from the last lesson.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-13-debugging/05_stepping_call_stack.png)

## s: Stepping Into a Call, Not Over It

The last lesson's `n` (next) runs a line completely, including any function it calls, then pauses on the following line, without ever pausing inside that called function. `s` (step) does the opposite: if the current line calls a function, `s` pauses at the very first line *inside* that function, letting you follow execution downward.

```python
class Attendee:
    def __init__(self, name, rsvp_count):
        self.name = name
        self.rsvp_count = rsvp_count

def total_rsvps(attendees):
    print("  [stepped into] total_rsvps, about to sum rsvp_count values")
    total = 0
    for attendee in attendees:
        total += attendee.rsvp_count
    return total

def summarize_event(attendees):
    # breakpoint()   <-- pause here in a real terminal, then type `s` to step
    # into total_rsvps. onecompiler cannot run (Pdb), so the prints below trace
    # the same path the debugger would walk you through.
    print("  [paused] in summarize_event, about to call total_rsvps")
    total = total_rsvps(attendees)
    return f"Total RSVPs: {total}"

people = [Attendee("Zara", 2), Attendee("Lin", 3)]
print(summarize_event(people))
```

Paused at `total = total_rsvps(attendees)`, typing `n` would run the entire `total_rsvps` call and pause on the `return` line, never showing what happened inside it. Typing `s` instead drops straight into `total_rsvps`'s very first line, exactly where Zara needs to be if the bug is suspected to live inside that function specifically.

## w: Seeing the Full Call Stack

Once stepped several functions deep, it is easy to lose track of who called what. The `w` (where) command prints the entire call stack: every function currently waiting for the one you are paused in to finish, from the outermost call down to your current location.

```text
(Pdb) w
  tracker.py(12)<module>()
-> summarize_event(attendees)
  tracker.py(8)summarize_event()
-> total = total_rsvps(attendees)
> tracker.py(3)total_rsvps()
-> total += attendee.rsvp_count
```

Read bottom to top, exactly like the traceback-reading skill from the exception handling unit: the bottom line is exactly where execution is paused right now, and each line above it is one level further out, the chain of calls that led here.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-13-debugging/05_call_stack_elevator.png)

*The call stack is a vertical map of who called whom, with the current frame sitting at the active level.*

## u and d: Moving Up and Down the Stack Without Resuming

Sometimes you want to check a variable from an outer function, like `attendees` back in `summarize_event`, without actually resuming execution. `u` (up) moves your inspection point one level up the call stack; `d` (down) moves it back down, and at each level you can inspect that function's own local variables exactly as if paused there.

```text
(Pdb) u
> tracker.py(8)summarize_event()
-> total = total_rsvps(attendees)
(Pdb) attendees
[<Attendee object at 0x...>, <Attendee object at 0x...>]
(Pdb) d
> tracker.py(3)total_rsvps()
-> total += attendee.rsvp_count
```

This lets Zara confirm that `attendees` already looked correct one level up, before `total_rsvps` ever touched it, narrowing the bug specifically to something happening inside `total_rsvps` itself, not to bad data arriving from outside it.

## Stepping Commands at a Glance

| Command | Effect |
|---|---|
| `n` | Run the current line fully; do not pause inside any function it calls |
| `s` | Step into the function the current line calls, pausing at its first line |
| `w` | Show the full call stack, from outermost caller to the current paused line |
| `u` | Move inspection up one level in the call stack, without resuming |
| `d` | Move inspection back down one level, toward the current paused line |

## Your Turn: Follow the Chain Downward

```python
class Attendee:
    def __init__(self, base_fee, discount_percent):
        self.base_fee = base_fee
        self.discount_percent = discount_percent

def discount_price(price, percent_off):
    print(f"  [stepped into] discount_price(price={price}, percent_off={percent_off})")
    return price - (price * percent_off / 100)

def total_for_attendee(attendee):
    # breakpoint()   <-- pause here in a real terminal, then `s` into discount_price.
    print(f"  [paused] in total_for_attendee: base_fee={attendee.base_fee}, discount={attendee.discount_percent}")
    return discount_price(attendee.base_fee, attendee.discount_percent)

print(total_for_attendee(Attendee(100, 20)))
```

At the pause, use `s` to step into `discount_price`, check `price` and `percent_off` there directly, then `w` to see the full call stack before letting it finish with `c`.

## Conclusion

`s` steps into a called function rather than running over it, and `w`, together with `u` and `d`, lets you see and move freely through the full call stack of functions currently waiting on each other, exactly what a bug buried several calls deep requires. With both pausing and stepping in hand, the next lesson turns to a tool meant for after development, when a program is running unattended and `breakpoint()` is no longer practical: Python's `logging` module.
