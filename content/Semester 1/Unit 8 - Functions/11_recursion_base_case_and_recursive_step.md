## Introduction

Naveen is asked for the total number of ways the prize committee could rank the top entries in a contest, which turns out to need a factorial: 5 entries means 5 times 4 times 3 times 2 times 1. He could write that out as a loop easily enough, multiplying a running total down from 5 to 1. But the way he first explains it to a junior committee member out loud is different: "5 factorial is just 5 times 4 factorial, and 4 factorial is just 4 times 3 factorial," and so on, down to the obvious case that 1 factorial is simply 1.

That explanation, defining a problem in terms of a smaller version of itself, is exactly the idea behind **recursion**: a function that calls itself, narrowing the problem down each time, until it reaches a case simple enough to answer directly.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-8-functions/11_recursion_self_call_chain.png)

## The Two Things Every Recursive Function Needs

A recursive function needs a **base case**, the simplest version of the problem, answered directly with no further calls, and a **recursive step**, where the function calls itself on a smaller version of the same problem. Without a base case, a recursive function would call itself forever, exactly the way a `while` loop with no way to become false runs forever.

```python
def factorial(n):
    if n == 1:                  # base case
        return 1
    return n * factorial(n - 1)  # recursive step

print(factorial(5))    # 120
```

The base case, `n == 1`, stops the chain of calls cold and hands back a known answer. The recursive step expresses the rest of the problem in terms of a smaller call to the very same function, exactly the way Naveen explained it out loud.

## Tracing a Recursive Call by Hand

Tracing a recursive function is the best way to actually trust it. Follow `factorial(3)` all the way down and back up.

```
factorial(3)
  = 3 * factorial(2)
        = 2 * factorial(1)
              = 1                  <- base case reached
        = 2 * 1 = 2
  = 3 * 2 = 6
```

Notice the calls go all the way down to the base case first, and only then does the multiplication actually happen, on the way back up, each level using the answer the level below it just produced. This unwind-on-the-way-back-up pattern is the heart of how recursion actually computes anything.

## A Second Example: Summing a List Recursively

Recursion is not only for factorials. Anything that can be described as "this problem, solved using a smaller version of itself" fits the same shape.

```python
def sum_list(numbers):
    if not numbers:                      # base case: an empty list
        return 0
    return numbers[0] + sum_list(numbers[1:])

print(sum_list([10, 20, 30, 40]))    # 100
```

The base case here is an empty list, whose sum is obviously 0. The recursive step takes the first number and adds it to the sum of everything else, a strictly smaller list, one item shorter every single call.

## Why Not Just Use a Loop?

Every recursive function in this lesson could be rewritten with a loop, and often the loop version is the more efficient choice in real Python code. Placed side by side on the same job, factorial, the difference is really just which idea drives the repetition: a running total updated step by step, or a function narrowing the problem down through calls to itself.

```python
def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n == 1:                          # base case
        return 1
    return n * factorial_recursive(n - 1)  # recursive step

print("Iterative:", factorial_iterative(5))    # 120
print("Recursive:", factorial_recursive(5))    # 120
```

Both reach the exact same answer, 120, for the exact same input. The iterative version keeps one variable, `result`, and updates it once per loop turn, using no extra memory beyond that single running total. The recursive version instead builds a chain of five waiting function calls, `factorial(5)` waiting on `factorial(4)`, waiting on `factorial(3)`, and so on, each one paused until the call below it returns, which is real memory the loop version never spends. Recursion earns its place when a problem is naturally defined in terms of smaller copies of itself, especially problems involving nested structures, like folders inside folders or the family tree of a function calling other functions, which you will meet properly in later courses. For now, the goal is simply to recognise the shape and trust it, not to abandon loops altogether.

## What Happens Without a Base Case

Forgetting the base case is the recursive equivalent of an infinite loop, and Python eventually stops it for you rather than letting your computer hang forever.

```python
def broken_factorial(n):
    return n * broken_factorial(n - 1)    # no base case!

broken_factorial(5)    # RecursionError, eventually, once Python's call-depth limit is hit
```

```text
RecursionError: maximum recursion depth exceeded
```

This raises a `RecursionError` once Python's limit on how deep calls can nest is reached, which is Python's safety net catching a recursive function that can never stop calling itself.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-8-functions/11_recursion_base_case_stop.png)


## Recursion at a Glance

| Part | Job | Example from `factorial` |
|---|---|---|
| Base case | Stops the recursion with a direct answer | `if n == 1: return 1` |
| Recursive step | Calls itself on a smaller version of the problem | `return n * factorial(n - 1)` |
| Missing base case | Calls itself forever, until Python intervenes | `RecursionError` |

## Your Turn: Count Down Recursively

```python
def countdown(n):
    if n == 0:
        print("Liftoff!")
        return
    print(n)
    countdown(n - 1)

countdown(5)
```

Trace this one by hand before you run it: what is the base case, and what is getting smaller on each recursive step? Then run it and check your trace against the real output.

## Conclusion

A recursive function solves a problem by calling itself on a smaller version of that same problem, always anchored by a base case that stops the chain and answers directly with no further calls. Trace a recursive function by hand, all the way down to the base case and back up, before trusting it, and never write one without checking that every call genuinely moves closer to that base case. With functions now able to call themselves, the final lesson of this unit turns to writing functions other people, including future you, can actually trust and understand at a glance.
