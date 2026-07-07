## Introduction

Asha writes a function that calculates each person's share of a trip cost, and someone calls it with zero people, a number that converts to an `int` perfectly validly, and so triggers no `ValueError` at all, yet is obviously nonsensical for this particular job. Python itself has no opinion about whether zero people is a reasonable input to `split_cost`; it only knows that dividing by zero specifically is impossible. Asha, on the other hand, knows something Python does not: in her function, a headcount of zero, or a negative number, is invalid, and she wants her own function to refuse it clearly, the moment it is called, rather than letting a confusing, unrelated error surface deeper inside.

Python's `raise` statement lets your own code deliberately trigger an exception, on purpose, the moment it detects a problem it knows about.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-12-exception-handling/06_raise_deliberate_exception.png)

## Raising a Built-in Exception

`raise` is followed by an exception type, called like a function, usually with a message describing exactly what went wrong.

```python
import traceback

def split_cost(total, people):
    if people <= 0:
        raise ValueError("Number of people must be greater than zero.")
    return total / people

try:
    print(split_cost(1200, 0))    # raises, because people is 0
except ValueError:
    print(traceback.format_exc())
```

This raises a `ValueError`, with the message Asha chose herself, the instant `split_cost` is called with an invalid headcount, rather than letting the function proceed and fail later with a less helpful `ZeroDivisionError`, or worse, silently returning a nonsensical result for a negative headcount that would not have crashed at all.

## Why Raise Instead of Just Returning None or Printing an Error

A function could quietly return `None`, or print a message and return `0`, instead of raising. Both choices hide the problem from whoever called the function, who might never check for `None`, or might mistake `0` for a genuinely valid answer.

```python
def split_cost_silent(total, people):
    if people <= 0:
        print("Invalid people count.")
        return None    # easy to forget to check for this!

share = split_cost_silent(1200, 0)
print("Each person pays:", share)    # Each person pays: None, easy to miss the real problem
```

Raising instead makes the failure impossible to silently ignore: it stops execution immediately, exactly where the problem was detected, and forces whoever called the function to either fix the bad input or explicitly handle the exception with `try`/`except`.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-12-exception-handling/06_raise_contract_boundary.png)


## A Function That Raises, Called Safely

The whole point of raising is that the caller, not the function itself, decides how to respond, using exactly the `try`/`except` tools from earlier in this unit.

```python
def split_cost(total, people):
    if people <= 0:
        raise ValueError("Number of people must be greater than zero.")
    return total / people

try:
    share = split_cost(1200, 0)
except ValueError as error:
    print("Could not split the cost:", error)
```

`split_cost` itself stays simple and trustworthy, refusing bad input unconditionally, while the calling code decides what "handling it gracefully" actually looks like in its own context.

## Re-raising: Catching, Then Raising Again

Sometimes you want to notice an exception, perhaps to log it or print extra context, and then let it continue propagating anyway, rather than swallowing it entirely. A bare `raise` inside an `except` block re-raises the exact exception that was just caught.

```text
def split_cost(total, people):
    try:
        return total / people
    except ZeroDivisionError:
        print("Logging: someone tried to split a cost among zero people.")
        raise
```

The `print` runs, as a quiet log entry, and then `raise` on its own sends the original `ZeroDivisionError` onward, exactly as if this `except` had never caught it at all, simply leaving a record behind on its way out.

## raise at a Glance

| Form | Effect |
|---|---|
| `raise ValueError("message")` | Triggers a new exception immediately, with your own message |
| Inside a function, before returning anything | Refuses to proceed with invalid input, instead of returning a bad result |
| `raise` alone, inside `except` | Re-raises the exception currently being handled, unchanged |

## Your Turn: Defend Your Own Function

```python
def calculate_age_group(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    if age < 13:
        return "Child"
    elif age < 20:
        return "Teenager"
    else:
        return "Adult"

try:
    print(calculate_age_group(-5))
except ValueError as error:
    print("Invalid age:", error)

print(calculate_age_group(15))    # Teenager
```

Notice the function refuses clearly on bad input, and works exactly as expected on good input, with no overlap or ambiguity between the two paths.

## Conclusion

`raise ExceptionType("message")` lets your own code deliberately trigger an exception the moment it detects a problem, refusing to proceed with invalid input rather than silently continuing or returning a misleading result, and leaving the decision of how to respond to whoever called the function, via `try`/`except`. A bare `raise` inside an `except` re-raises the original exception unchanged, useful for logging on the way out without swallowing the failure. So far every exception, raised or caught, has been a built-in Python type; the next lesson covers defining your own, named specifically for the problems your own programs care about.
