## Introduction

Naveen has quietly become the hostel's go-to "script guy." First he wrote a few lines to split the mess bill evenly across however many people showed up that month. The cricket league asked him for the same split-the-cost logic for umpire fees. Then the trip fund needed it too. Each time, Naveen copy-pasted the same handful of lines into a new chat, changed the numbers, and moved on. It worked, right up until the mess committee decided a 5 percent service charge should be added to every split from now on. Naveen had to hunt down all three copies of his logic and fix each one by hand, and he still is not sure he caught every place it was pasted.

That sinking feeling, the same logic scattered across many places, each copy one missed edit away from being wrong, is the exact problem this unit solves. A **function** is a named, reusable block of logic that you write once and run as many times as you like, from as many places as you like, by simply calling its name.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-8-functions/01_copy_pasted_calculation.png)

## The Cost of Copy-Paste

Here is roughly what Naveen kept retyping, written as a plain script with no function at all.

```python
total = 1200
people = 4
print("Each pays:", total / people)
```

Run it for the mess bill, then run a near-identical block for the umpire fee, then again for the trip fund. Three blocks, one idea. The moment the calculation needs to change, every single copy needs to change with it, and a busy person fixing three places by hand is exactly how bugs slip through.

## Naming the Idea Once

A function lets Naveen say "splitting a cost between people" exactly once, under one name, and then simply call that name wherever the calculation is needed.

```python
def split_cost(total, people):
    return total / people

print("Mess bill share:", split_cost(1200, 4))
print("Umpire fee share:", split_cost(600, 3))
print("Trip fund share:", split_cost(4500, 9))
```

You have not seen the full rules for writing a function yet, that is the very next lesson, but notice the shape already: one block named `split_cost`, called three times with three different numbers. If the formula needs a service charge added tomorrow, Naveen changes it in exactly one place, and every call benefits instantly.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-8-functions/01_function_recipe_card.png)


## Two Habits Functions Encourage

Functions are not just about avoiding retyping. They encourage two habits that make your whole program easier to reason about.

The first is **reuse**: write the logic once, trust it everywhere it is called, rather than hoping every copy was pasted correctly.

The second is **decomposition**, the very skill from the start of this course: breaking a big problem into smaller, named pieces. A program that calculates an entire trip's budget is overwhelming as one giant block, but broken into `split_cost`, `add_service_charge`, and `format_receipt`, each piece is small enough to write, test, and trust on its own.

## Before and After at a Glance

| Without Functions | With Functions |
|---|---|
| Same logic copy-pasted everywhere it is needed | Logic written once, called by name |
| A fix means finding and editing every copy | A fix means editing one definition |
| Hard to tell which copies are still correct | Every call always uses the current version |
| One giant block of code | Small, named, understandable pieces |

## Your Turn: Spot the Repetition

```python
shirt_price = 350
shirt_qty = 2
print("Shirt total:", shirt_price * shirt_qty)

mug_price = 150
mug_qty = 3
print("Mug total:", mug_price * mug_qty)

badge_price = 50
badge_qty = 5
print("Badge total:", badge_price * badge_qty)
```

Look closely at these three blocks. They are not identical line by line, but they repeat the same idea three times: price times quantity, then a print. That repeated idea, "calculate and report a line total," is exactly the kind of thing a function is about to let you name once and reuse, which the very next lesson shows you how to do.

## Conclusion

A function is a named, reusable block of logic, written once and called wherever it is needed, which is exactly what rescues you from the copy-paste trap Naveen kept falling into. Functions support two habits worth holding onto for the rest of your programming life: reuse, so a fix in one place reaches every call, and decomposition, so a big problem becomes a set of small, named, trustworthy pieces. You have seen the shape of a function in passing; the next lesson gives you the precise rules for defining and calling one yourself.
