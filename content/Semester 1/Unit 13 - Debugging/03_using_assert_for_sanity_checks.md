## Introduction

Print debugging found Zara's bad RSVP value, but only because she happened to look at the right printed output at the right moment. A deeper worry remains: what about all the assumptions she is not actively watching right now, like every `rsvp_count` being a non-negative number, or every `Event` having at least one attendee before she calculates an average? Checking those by eye, every time, in every function, is not realistic. What she wants is a way to state an assumption directly in the code, so Python itself complains immediately and loudly the moment that assumption turns out to be false.

That is exactly what Python's `assert` statement is for.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-13-debugging/03_assert_sanity_checks.png)

## The Basic Shape of assert

`assert` takes a condition. If the condition is true, nothing happens at all, execution simply continues. If the condition is false, Python immediately raises an `AssertionError`.

```python
import traceback

def average_rsvps(attendees):
    assert len(attendees) > 0, "attendees list must not be empty"
    total = sum(a.rsvp_count for a in attendees)
    return total / len(attendees)

try:
    average_rsvps([])    # empty list trips the assert
except AssertionError:
    print(traceback.format_exc())
```

This raises `AssertionError: attendees list must not be empty`, immediately, at the exact line where the bad assumption was checked, rather than letting the function proceed and fail two lines later with a less informative `ZeroDivisionError` that says nothing about the real cause.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-13-debugging/03_assert_checkpoint_gate.png)

*An `assert` is a sanity checkpoint for assumptions that should already be true inside your own code.*

## assert States an Assumption, Out Loud, in Code

The real value of `assert` is not just catching the error, it is making an assumption visible to anyone reading the function, including Zara herself in three weeks, who will have forgotten every detail of why this code was written this way.

```python
class Event:
    def __init__(self, name, max_attendees):
        assert max_attendees > 0, "an event must allow at least one attendee"
        self.name = name
        self.max_attendees = max_attendees
        self.attendees = []

# Demo: a sensible capacity passes the assert and builds fine
event = Event("Fresher's Night", 300)
print(f"{event.name}: capacity {event.max_attendees}, {len(event.attendees)} signed up")
```

Anyone reading `__init__` now knows, instantly and explicitly, that a sensible `Event` can never have a zero or negative capacity, a rule that might otherwise live only in Zara's head, easy to forget and easy to violate by accident elsewhere in the project.

## assert Is for Bugs in Your Own Logic, Not for User Input

This is the detail that trips up nearly every beginner: `assert` exists to catch programming mistakes, situations that should be logically impossible if the rest of the code is correct, not to validate ordinary, expected bad input from a user or a file, which the previous unit's `try`/`except` already handles properly.

```python
# Wrong use of assert: this is expected, recoverable user input, not a bug
age_text = input("Enter your age: ")
assert age_text.isdigit(), "must be digits"    # crashes the whole program on ordinary bad input!

# Right use of assert: this should be logically impossible if earlier code is correct
def split_cost(total, people):
    assert people > 0, "people should already be validated as positive by this point"
    return total / people

# Demo:
result = split_cost(1200, 4)
print(f"split_cost(1200, 4) -> {result}")
```

A user mistyping their age is normal and expected, handled gracefully with `try`/`except` from the last unit. A negative `people` count reaching `split_cost`, after validation supposedly already happened earlier, is a sign something in your own logic is broken, exactly the case `assert` is built for.

## assert Can Be Disabled, So Never Rely on It for Real Validation

Python can run with assertions stripped out entirely, using the `-O` optimization flag, which means any check truly required for program correctness, like rejecting bad user input, must use `if` and `raise`, or `try`/`except`, never `assert` alone.

```python
def withdraw(balance, amount):
    assert amount > 0    # fine as a sanity check during development
    if amount > balance:    # this one genuinely must always run, so it is a real if, not an assert
        raise ValueError("Insufficient funds.")
    return balance - amount

# Demo:
result = withdraw(5, 5)
print(f"withdraw(5, 5) ->", result)
```

## assert at a Glance

| Use Case | Right Tool |
|---|---|
| Catching a bug in your own logic that should be impossible | `assert condition, "message"` |
| Validating expected, ordinary bad input from a user or file | `if`/`raise`, or `try`/`except` from the previous unit |
| A check that must always run, even in optimized code | Never `assert` alone; use `if`/`raise` |

## Your Turn: State Three Assumptions

```python
import traceback

class Attendee:
    def __init__(self, name, rsvp_count):
        assert isinstance(name, str) and name.strip(), "name must be a non-empty string"
        assert rsvp_count >= 0, "rsvp_count cannot be negative"
        self.name = name
        self.rsvp_count = rsvp_count

zara = Attendee("Zara", 2)
print(f"{zara.name}: {zara.rsvp_count}")    # valid: builds fine

try:
    broken = Attendee("", 2)    # empty name trips the first assert
except AssertionError:
    print(traceback.format_exc())
```

Run this, confirm the second creation fails with a clear message naming exactly which assumption was broken, and try writing one more `assert` of your own for a rule this class should always satisfy.

## Conclusion

`assert condition, "message"` states an assumption directly in the code, raising `AssertionError` loudly and immediately the moment that assumption turns out false, making it ideal for catching bugs in your own logic early and documenting your own assumptions for future readers, but never a substitute for validating ordinary, expected bad input, which still belongs to `if`/`raise` or `try`/`except`. Print statements and `assert` both help once you already suspect something specific; the next lesson introduces a tool for when you have no idea yet where the problem even is: Python's own interactive debugger.
