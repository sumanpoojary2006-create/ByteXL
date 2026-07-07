## Introduction

The mess committee finally adds that service charge, but only sometimes, for special dinners, not the everyday split. If Naveen makes the service charge a required parameter, every single call to `split_cost` now needs a number for it, even the ordinary splits that never had one before, and every old call across his scripts suddenly breaks. What he actually wants is a parameter that is usually 0 and only needs to be mentioned on the rare calls where it matters.

Python lets a parameter carry a **default value**, used automatically whenever a call leaves it out. Paired with that, **keyword arguments** let you name which parameter you are supplying, instead of relying purely on position, which turns out to be just as useful.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-8-functions/04_default_argument_fallback.png)

## Giving a Parameter a Default Value

Assign a value to a parameter right in the function's definition, and any call that omits it falls back to that default automatically.

```python
def split_cost(total, people, service_charge=0):
    return (total + service_charge) / people

print(split_cost(1200, 4))             # 300.0, no service charge supplied
print(split_cost(1200, 4, 60))         # 315.0, service charge supplied
```

The first call never mentions `service_charge` at all, so Python quietly uses 0. The second call supplies 60, which overrides the default for just that one call. Every existing call to `split_cost` that predates this change keeps working exactly as before, because the new parameter is entirely optional.

## A Rule Worth Knowing: Defaults Come Last

Python requires every parameter with a default value to come after every parameter without one, in the definition.

```python
import ast

# Wrong: optional parameter placed before a required one -- Python rejects this
wrong = "def split_cost(total, service_charge=0, people): return (total + service_charge) / people"
try:
    ast.parse(wrong)
except SyntaxError as e:
    print(f"SyntaxError: {e}")
    print("Required parameters must always come before optional (defaulted) ones.")

# Correct order: required first, optional last
def split_cost(total, people, service_charge=0):
    return (total + service_charge) / people

print(f"split_cost(1200, 4, service_charge=100) -> {split_cost(1200, 4, service_charge=100)}")
```

This raises a `SyntaxError`, because Python cannot tell, partway through reading the parentheses, which arguments a future call is allowed to skip. Required parameters always come first; optional, defaulted ones always come last.

## Positional Arguments: Order Decides the Match

Every call you have written so far has used positional arguments, where Python matches each argument to a parameter purely by its position, left to right.

```python
def describe_member(name, role):
    print(f"{name} is the {role}")

describe_member("Naveen", "treasurer")
```

This works, but it depends entirely on getting the order right. Swap the arguments by mistake, and Python will not catch it, because both are valid strings; it will simply produce a wrong, confusing result.

```python
def describe_member(name, role):
    print(f"{name} is the {role}")

describe_member("treasurer", "Naveen")    # arguments swapped -- wrong output!
```

## Keyword Arguments: Naming Removes the Risk

A keyword argument names the parameter it is filling, directly in the call, removing any dependence on order.

```python
def describe_member(name, role):
    print(f"{name} is the {role}")

describe_member(role="treasurer", name="Naveen")    # keyword args -- order doesn't matter
```

Because each argument names its own parameter, the order no longer matters at all, and the call is arguably easier to read besides, since "role=treasurer" leaves nothing to guess.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-8-functions/04_positional_keyword_matching.png)


## Mixing Positional and Keyword Arguments

You can mix the two styles in one call, but positional arguments must always come before keyword arguments.

```python
def split_cost(total, people, service_charge=0):
    return (total + service_charge) / people

print(split_cost(1200, 4, service_charge=60))    # fine: 315.0

# The line below is left as a comment because it is a SyntaxError --
# a positional argument (4) cannot follow a keyword argument (total=1200):
#   print(split_cost(total=1200, 4))
print("split_cost(total=1200, 4) would be a SyntaxError: positional arg after keyword arg")
```

The second line fails with a `SyntaxError`, because once a call starts naming its arguments, it cannot go back to relying on position. Read this the same way you read the rule about default parameters: once you start being explicit, you have to stay explicit for the rest of that call.

## Defaults and Keywords at a Glance

| Idea | Syntax | Effect |
|---|---|---|
| Default value | `def f(a, b=0):` | Calls may omit `b`; it falls back to 0 |
| Positional argument | `f(10, 20)` | Matched to parameters by order |
| Keyword argument | `f(a=10, b=20)` | Matched to parameters by name, order-independent |
| Mixing both | `f(10, b=20)` | Positional arguments must come first |

## Your Turn: An Optional Discount

```python
def ticket_price(base_price, discount=0):
    return base_price - discount

print("Regular:", ticket_price(500))
print("Member discount:", ticket_price(500, discount=100))
print("Same call, positional:", ticket_price(500, 100))
```

Notice all three calls work, and the only difference between the second and third is style, not behaviour, because both correctly fill the same `discount` parameter.

## Conclusion

A default value, written as `parameter=value` in the definition, makes an argument optional, and Python requires all defaulted parameters to come after the required ones. Keyword arguments name the parameter they fill, freeing you from depending on order, though positional arguments must always come before keyword ones in the same call. These tools make a function flexible enough to serve both its oldest, simplest calls and its newest, more detailed ones. The next lesson goes one step further: what happens when you do not even know in advance how many arguments a call might need?
