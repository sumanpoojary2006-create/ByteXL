## Introduction

Dev is tracking trip payments in a list of amounts, and the treasurer asks him for just the names of students who have actually paid the full fee, leaving out everyone who still owes money. The long way is familiar by now: make an empty list, loop through every student, check a condition, and append the ones that pass. It works, but it is four lines of scaffolding to express one simple idea: "give me the ones that qualify."

Python offers a shorter, more direct way to say exactly that, called a **list comprehension**. It builds a new list from an existing one, in a single readable line, by describing what you want rather than spelling out every step of how to get it.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-6-lists-and-tuples/04_paid_students_filter.png)

## The Long Way First

Before the shortcut, see the loop it replaces. Suppose you want a new list holding only the even numbers from another list.

```python
numbers = [3, 8, 5, 12, 7, 10]
evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)
print(evens)    # [8, 12, 10]
```

Four lines: set up an empty list, loop, check, append. The result is correct, but the shape of the problem, "keep the numbers that pass this test", deserves to read as clearly as it sounds.

## The List Comprehension Way

A list comprehension folds that entire pattern into one line, inside square brackets.

```python
numbers = [3, 8, 5, 12, 7, 10]
evens = [n for n in numbers if n % 2 == 0]
print(evens)    # [8, 12, 10]
```

Read it almost like English: "n, for n in numbers, if n is divisible by 2." The general shape is `[expression for item in sequence if condition]`, and the `if` part is optional whenever you do not need to filter at all.

## Transforming, Not Just Filtering

A comprehension does not only select items, it can also transform each one on the way in. Put an expression before the `for` instead of the bare loop variable.

```python
prices = [100, 250, 75]
discounted = [price * 0.9 for price in prices]
print(discounted)    # [90.0, 225.0, 67.5]
```

Here every price is multiplied by 0.9 as it goes into the new list, with no filtering at all, which shows that the `for` part is the only piece a comprehension truly requires.

## Combining Transform and Filter

The two abilities combine naturally: transform the items you keep, and skip the rest.

```python
students = ["Asha", "ravi", "MEERA", "kabir"]
tidy_names = [name.title() for name in students if len(name) > 4]
print(tidy_names)    # ['Meera', 'Kabir']
```

Each surviving name is reshaped with `.title()` exactly as it passes the length check, in the very same line. This is precisely the kind of "transform what qualifies" task Dev runs every time he needs a clean, formatted list pulled out of a messier one.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-6-lists-and-tuples/04_comprehension_transform_filter.png)


## List Comprehensions at a Glance

| Situation | Better Choice |
|---|---|
| Building a new list from an existing one with a simple rule | List comprehension |
| The logic needs several steps, or has side effects like printing | A regular `for` loop |
| Readability is suffering because the line is getting long | A regular `for` loop |

A list comprehension is a tool for clarity, not a badge of cleverness. If it stops being instantly readable, the plain loop from the start of this lesson is still the right answer.

## Your Turn: Filter the Paid List

```python
amounts = [4500, 0, 4500, 2000, 4500]
fee = 4500

paid_count = len([a for a in amounts if a >= fee])
print(f"{paid_count} students have paid the full fee.")

reminders = [a for a in amounts if a < fee]
print("Outstanding amounts:", reminders)
```

This builds two different filtered lists from the same data in two short lines, exactly the kind of quick reporting a trip coordinator does constantly.

## Conclusion

A list comprehension, written as `[expression for item in sequence if condition]`, builds a new list from an existing one in a single readable line, replacing the longer setup-loop-append pattern. Use it for simple selecting and transforming, and step back to a full loop once the logic grows complicated. So far every list has held one flat row of values; the next stop is tuples, a sibling of the list that trades flexibility for a guarantee that nothing inside it can ever change.
