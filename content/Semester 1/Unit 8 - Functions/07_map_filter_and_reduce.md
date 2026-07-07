## Introduction

Naveen has a list of pending dues and three quick jobs to do with it before the meeting: apply a 5 percent late fee to every single amount, pull out only the dues that are still above 200 after that fee, and finally collapse the whole list down into one grand total. Each job takes a list in and produces something new out, by applying the same small rule to every item. You already know one way to do this, the list comprehension from two units ago, but Python also offers three classic, purpose-built tools that do exactly these three jobs by name, and they pair naturally with the lambdas from the last lesson.

`map`, `filter`, and `reduce` each take a function and a sequence, and each does one very specific thing with that pairing.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-8-functions/07_map_filter_reduce_pipeline.png)

## map: Apply a Function to Every Item

`map` takes a function and a sequence, and applies that function to every item, handing back a `map` object that you usually wrap in `list()` to actually see.

```python
dues = [300, 150, 450, 200]
with_late_fee = list(map(lambda amount: amount * 1.05, dues))
print("Dues with fee:", with_late_fee)    # [315.0, 157.5, 472.5, 210.0]
```

Every single amount passed through the same lambda, each multiplied by 1.05 on its own. This is the exact same outcome a list comprehension would give you.

```python
dues = [300, 150, 450, 200]
with_late_fee = [amount * 1.05 for amount in dues]
print("Dues with fee:", with_late_fee)
```

Both lines do the same job. `map` is simply the older, function-first way of saying it, and you will meet it often enough in other people's code that recognising it matters, even if a comprehension often reads more naturally to a Python programmer today.

## map With a Named Function Instead of a Lambda

`map` does not require a lambda at all; any function that already exists, defined above with `def`, works exactly as well as the argument, and reads more clearly once the transformation itself deserves a name.

```python
def apply_late_fee(amount):
    return amount * 1.05

dues = [300, 150, 450, 200]
with_late_fee = list(map(apply_late_fee, dues))
print("Dues with fee:", with_late_fee)
```

`apply_late_fee` is a completely ordinary function, defined the normal way, tested and called on its own if needed. Handing its name to `map`, without parentheses, is what makes the difference; `map` calls it once per item on your behalf, exactly as it would have called a lambda.

## filter: Keep Only What Passes a Test

`filter` takes a function that returns `True` or `False`, and keeps only the items for which it returns `True`. Naveen's next job is different from the late-fee one: from a list of quiz scores, he wants only the scores that actually passed.

```python
scores = [45, 72, 30, 88, 55, 91]
passing = list(filter(lambda score: score >= 50, scores))
print("Passing scores:", passing)    # [72, 88, 55, 91]
```

Every score is tested by the lambda, and only the ones that pass survive into the result. Once again, a list comprehension can say the same thing.

```python
scores = [45, 72, 30, 88, 55, 91]
passing = [score for score in scores if score >= 50]
print("Passing scores:", passing)
```

`filter` also works with a named function instead of a lambda, exactly like `map` did.

```python
def has_passed(score):
    return score >= 50

scores = [45, 72, 30, 88, 55, 91]
passing = list(filter(has_passed, scores))
print("Passing scores:", passing)
```

## reduce: Collapse a Sequence Into One Value

`reduce` is different from the other two: instead of producing a new sequence, it collapses an entire sequence down into a single value, by repeatedly combining items two at a time. Unlike `map` and `filter`, it is not built in directly; it lives in the `functools` module, so it needs an import. This time the job is finding whichever contributor's name is the longest, on a printed committee list.

```python
from functools import reduce

names = ["Asha", "Ravi", "Meera", "Venkataraman", "Tara"]
longest_name = reduce(lambda longest, current: current if len(current) > len(longest) else longest, names)
print("Longest name:", longest_name)    # Venkataraman
```

Read the lambda as "compare the longest name found so far with the next name, and keep whichever one is longer." `reduce` starts by comparing the first two names, keeps the longer one, compares that against the third name, and so on, until only one name, the overall longest, is left. This is exactly the kind of job `reduce` is genuinely built for: combining logic that has no dedicated built-in function of its own, unlike plain addition.

## Most of the Time, sum() Already Does This

For the specific, extremely common case of adding everything up, `reduce` still works, but Python's built-in `sum()` does the exact same job with far less ceremony.

```python
from functools import reduce

above_200 = [315.0, 472.5, 210.0]
total_with_reduce = reduce(lambda running_total, amount: running_total + amount, above_200)
total_with_sum = sum(above_200)
print("reduce total:", total_with_reduce)    # 997.5
print("sum total:", total_with_sum)          # 997.5
```

Both lines reach the identical answer, 997.5. `reduce` can express addition, as shown here, but `sum()` is simpler and is what experienced Python programmers actually reach for whenever the job really is just adding everything up; `reduce` earns its place for jobs like the longest-name search above, where no ready-made built-in already exists.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-8-functions/07_map_filter_reduce_vs_loop.png)


## map, filter, and reduce at a Glance

| Tool | Job | Often Replaced By |
|---|---|---|
| `map(func, seq)` | Transform every item | `[func(x) for x in seq]` |
| `filter(func, seq)` | Keep items passing a test | `[x for x in seq if func(x)]` |
| `reduce(func, seq)` | Collapse to one value | `sum()`, `max()`, or a plain loop, depending on the job |

Knowing all three matters for reading other people's code and for understanding the ideas underneath comprehensions, even where a comprehension is the more natural choice for new code.

## Your Turn: The Full Pipeline

```python
from functools import reduce

dues = [300, 150, 450, 200]

with_late_fee = list(map(lambda amount: amount * 1.05, dues))
print("With late fee:", with_late_fee)

above_200 = list(filter(lambda amount: amount > 200, with_late_fee))
print("Above 200:", above_200)

total = reduce(lambda a, b: a + b, above_200)
print("Total of those above 200:", total)
```

Run all three stages in sequence and notice each tool did exactly one job, handing its result to the next.

## Conclusion

`map` transforms every item in a sequence, `filter` keeps only the items that pass a test, and `reduce`, imported from `functools`, collapses a whole sequence down to one value by combining items two at a time, though `sum()`, `max()`, and `min()` already cover the most common reductions directly. List comprehensions often express the same ideas more readably in modern Python, but recognising these three by name is essential for reading real code. With several ways now to process a sequence in one line, the next lesson tours a handful of built-in functions worth knowing by heart.
