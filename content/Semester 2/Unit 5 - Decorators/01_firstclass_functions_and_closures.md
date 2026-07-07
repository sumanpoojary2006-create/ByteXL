## Introduction

Kiran is building the library management system's API. She has twelve endpoint handlers, and every one needs to log its execution time. She starts by copying a timing block into each handler, then stops herself. Twelve functions, twelve copies of the same boilerplate. If the timing format ever changes, she has to update twelve places.

She knows Python treats functions as first-class values, and she has a vague sense that this is related to the solution. This lesson makes that vague sense precise: it covers what first-class functions actually mean in practice and introduces the related concept of closures, which is the foundation that makes decorators work.

![A function shown as a value being stored in a variable, passed to another function, and returned from a function, like an ordinary object](images/01_firstclass_functions_closures.png)

## Functions Are Just Objects

In Python, a function is an object. Like an integer or a string, a function can be:
- Assigned to a variable
- Stored in a list or dictionary
- Passed to another function as an argument
- Returned from a function

This is what "first-class" means: functions enjoy all the same rights as any other value.

```python
def greet(name):
    return f"Hello, {name}"

# Assign to a variable
say_hello = greet
print(say_hello("Kiran"))   # Hello, Kiran

# Store in a list
actions = [greet, str.upper, str.lower]
for fn in actions:
    print(fn("Library"))
# Hello, Library
# LIBRARY
# library

# Pass as an argument
def apply(fn, value):
    return fn(value)

print(apply(greet, "Asel"))   # Hello, Asel
```

The name `greet` and the function object it points to are separate things. `say_hello = greet` makes two names point to the same function object; it does not copy or rename the function.

## Functions Defined Inside Other Functions

A function can be defined inside another function's body. The inner function has access to the outer function's variables, even after the outer function has returned. This combination of an inner function plus the surrounding variables it can see is called a **closure**.

```python
def make_greeter(greeting):
    def greet(name):
        return f"{greeting}, {name}!"   # greeting is captured from make_greeter
    return greet

hello = make_greeter("Hello")
hi = make_greeter("Hi")

print(hello("Kiran"))    # Hello, Kiran!
print(hi("Asel"))        # Hi, Asel!
print(hello("Leila"))    # Hello, Leila!
```

After `make_greeter("Hello")` returns, the local variable `greeting` would normally be gone. But `greet` captured it in a closure: the variable is kept alive as long as `greet` is alive. `hello` and `hi` are two separate function objects, each carrying a different `greeting` in their respective closures.

## Inspecting a Closure

Python exposes closure variables through the `__closure__` attribute:

```python
def make_multiplier(factor):
    def multiply(n):
        return n * factor
    return multiply

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))    # 10
print(triple(5))    # 15

# The closure carries 'factor' as a cell
print(double.__closure__[0].cell_contents)   # 2
print(triple.__closure__[0].cell_contents)   # 3
```

The `cell_contents` shows exactly what value each closure is holding. This is the mechanism that will underpin every decorator: a wrapper function that closes over the original function and some extra behavior.

## The Closure Pattern: Behavior Factories

Closures are most useful as **behavior factories**: functions that return customized functions without inheritance or classes.

```python
def make_validator(min_val, max_val):
    def validate(value):
        if not (min_val <= value <= max_val):
            raise ValueError(f"{value} is outside [{min_val}, {max_val}]")
        return value
    return validate

validate_copies = make_validator(0, 1000)
validate_price = make_validator(0.01, 9999.99)

print(validate_copies(5))     # 5
print(validate_price(19.99))  # 19.99

validate_copies(-1)   # error! ValueError
```

`validate_copies` and `validate_price` are two functions that behave differently because they carry different closure values. No class, no subclass, no boilerplate: just a factory function and two closures.

## First-Class Functions and Closures at a Glance

| Concept | What it means |
|---|---|
| First-class function | A function is an ordinary value: assignable, passable, returnable |
| Inner function | A function defined inside another function's body |
| Closure | An inner function plus the outer variables it captured |
| Behavior factory | A function that returns customized inner functions |

## Your Turn

```python
def make_logger(prefix):
    def log(message):
        print(f"[{prefix}] {message}")
    return log

api_log = make_logger("API")
db_log = make_logger("DB")
```

Create both loggers and call each with a message. Then inspect `api_log.__closure__[0].cell_contents` to confirm it contains the string `"API"`. Finally, write a `make_rate_limiter(max_calls)` factory that returns a function `call()` which increments a counter and raises a `RuntimeError` when the counter exceeds `max_calls`. You will need to use a mutable container (a list) to hold the counter inside the closure, since closures cannot reassign outer variables directly.

## Conclusion

Python functions are first-class objects: they can be stored, passed, and returned like any other value. An inner function that refers to variables from its enclosing scope creates a closure, keeping those variables alive even after the outer function returns. Behavior factories exploit closures to produce customized functions with minimal code. These are the two foundational ideas that make decorators possible: the next lesson shows how passing and returning functions enables the next step.
