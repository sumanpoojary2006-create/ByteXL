## Introduction

Naveen keeps reinventing small pieces of logic that Python actually already hands him for free. He once wrote a loop just to check whether every single member had paid their dues. He wrote another loop just to find the single largest pending due. He has used `len()` and `sum()` for units now without ever stopping to notice how often they show up. A handful of built-in functions cover almost every one of these everyday questions, and knowing them by name saves you from writing a loop for a job Python has already solved.

This lesson is a tour of the built-ins worth knowing cold: `all`, `any`, `len`, `sum`, `sorted`, `min`, and `max`.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-8-functions/08_builtin_functions_toolbox.png)

## all(): Is Everything True?

`all` takes a sequence and returns `True` only if every single item in it is truthy.

```python
paid = [True, True, True, False]
print(all(paid))    # False, because one member has not paid
```

This replaces the exact loop Naveen used to write by hand: set a flag to `True`, loop through everyone, and flip the flag to `False` the moment one person has not paid. `all()` does that in a single call.

## any(): Is At Least One True?

`any` takes a sequence and returns `True` if at least one item in it is truthy.

```python
overdue = [False, False, True, False]
print(any(overdue))    # True, at least one member is overdue
```

`all` asks "does everyone qualify?" while `any` asks "does anyone qualify at all?" Keeping the two straight is mostly about remembering which word matches which question in plain English: "all of them" versus "any of them."

## len(): How Many Items?

You have used `len()` since the strings unit, and it works identically on lists, tuples, sets, and dictionaries, always counting how many items the collection holds.

```python
members = ["Asha", "Ravi", "Meera", "Naveen"]
print(len(members))    # 4
```

## sum(): Add Everything Up

`sum()` adds every number in a sequence together, and it accepts an optional second argument as a starting value, useful when you want to begin counting from something other than zero.

```python
dues = [300, 150, 450, 200]
print(sum(dues))           # 1100
print(sum(dues, 500))      # 1600, starting from a 500 carry-over balance
```

## sorted(): A New, Ordered List

`sorted()` returns a brand new sorted list from any sequence, leaving the original untouched, exactly as you met it in the lists and tuples unit. It accepts `reverse=True` and a `key` function, which you have already seen paired with a lambda.

```python
dues = [300, 150, 450, 200]
print(sorted(dues))                       # [150, 200, 300, 450]
print(sorted(dues, reverse=True))         # [450, 300, 200, 150]
```

## min() and max(): The Smallest and Largest

`min()` and `max()` find the smallest and largest values in a sequence directly, no loop and no "best so far" variable required.

```python
dues = [300, 150, 450, 200]
print(min(dues))    # 150
print(max(dues))    # 450
```

Both also accept a `key` argument, exactly like `sorted()`, letting you find the minimum or maximum by some derived value rather than the raw value itself.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-8-functions/08_builtin_function_selector.png)


```python
members_with_dues = [("Asha", 300), ("Ravi", 150), ("Meera", 450)]
print(max(members_with_dues, key=lambda m: m[1]))    # ('Meera', 450)
```

## Built-ins at a Glance

| Function | Answers | Example |
|---|---|---|
| `all(seq)` | Is every item truthy? | `all(paid)` |
| `any(seq)` | Is at least one item truthy? | `any(overdue)` |
| `len(seq)` | How many items? | `len(members)` |
| `sum(seq)` | What is the total? | `sum(dues)` |
| `sorted(seq)` | What is the ordered version? | `sorted(dues, reverse=True)` |
| `min(seq)` | What is the smallest? | `min(dues)` |
| `max(seq)` | What is the largest? | `max(dues)` |

## Your Turn: A One-Glance Dues Report

```python
dues = [300, 150, 450, 200, 0]

print("Total collected so far:", sum(dues))
print("Largest pending due:", max(dues))
print("Smallest pending due:", min(dues))
print("Has everyone paid something?", all(amount > 0 for amount in dues))
print("Is anyone fully cleared at zero?", any(amount == 0 for amount in dues))
print("Sorted, highest first:", sorted(dues, reverse=True))
```

Notice `all` and `any` here are fed a generator expression, written just like a list comprehension but without the square brackets, which is a common, efficient way to feed a quick condition straight into these two functions.

## Conclusion

`all` and `any` answer "does everyone" and "does anyone" without a hand-written loop, `len` and `sum` count and total a sequence, and `sorted`, `min`, and `max` order and extract extremes, all accepting an optional `key` for custom comparisons. Recognising and reaching for these built-ins, rather than rebuilding their logic from scratch with a loop, is one of the fastest ways to write shorter, more reliable code. The next lesson turns from these ready-made tools to a technique for organising your own functions: defining one function inside another.
