## Introduction

Priya has fully working `Student` and `BankAccount` classes now, but on her way out of the office she jots down a single one-off note: today's visitor count at the help desk, 47. Writing a whole class, with an `__init__` and methods, just to hold the number 47 would be absurd, and some quiet part of her already knows that. Yet earlier in this very unit, building a class for a student felt obviously worth it. What actually separates these two cases?

This final lesson of the unit is a direct, practical comparison, so that choosing between a class and a plain dictionary or tuple becomes a quick, confident decision rather than a reflex to use whichever tool you learned most recently.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-9-basic-object-oriented-programming/08_plain_data_vs_class_decision.png)

## The Question Underneath the Decision

Ask yourself: does this thing have behaviour, actions it can do or questions it can answer about itself, or is it simply a value or a flat bundle of facts? A visitor count is just a number; it cannot "do" anything. A student can be judged pass or fail, graded, and reported on. A bank account can be deposited into and will refuse an overdraft. The moment a real-world thing needs its own actions, not just its own data, a class is earning its keep.

## When Plain Data Is Genuinely Enough

```python
visitor_count = 47

trip_stop = ("Resort", 15.2993, 74.1240)

prices = {"T-shirt": 350, "Mug": 150}
print(prices)
```

None of these need a class. A single number needs nothing more than a variable. A fixed, related group of values with no behaviour, like a GPS coordinate, is exactly what a tuple was built for, back in the lists and tuples unit. A simple lookup table is exactly what a dictionary was built for. Reaching for a class here would not be wrong, exactly, but it would be needless ceremony around data that was never going to do anything on its own.

## When a Class Earns Its Place

A class earns its place once a "thing" needs to carry both data and the logic that acts on that data together, especially when you expect many independent instances, each enforcing the same rules on its own values.

```text
class BankAccount:
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
```

Try to build this same guarantee, "never let a withdrawal exceed the balance," using a plain dictionary, and you will find the rule has nowhere natural to live. You would end up writing a separate function every time you wanted to withdraw safely, and nothing would stop another part of the program from editing `account["balance"]` directly, bypassing the check entirely. A class keeps the rule and the data it protects locked together, in one place, every single time.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-9-basic-object-oriented-programming/08_when_class_earns_place.png)


## A Worked Comparison: Representing a Student

A dictionary can certainly hold a student's data.

```python
student = {"name": "Asha", "marks": 92}
status = "Pass" if student["marks"] >= 40 else "Fail"
print(status)
```

This works for one student, once. The moment you need this exact pass/fail logic for fifty students, or you want to add a `grade()` calculation later without rewriting every place that checks marks by hand, the class version from earlier in this unit starts paying for itself: the logic lives once, on the class, and every student object reuses it automatically.

## Objects vs Plain Data at a Glance

| Question | Points To |
|---|---|
| Is this just one standalone value? | A plain variable |
| Is this a fixed, related group of values with no behaviour? | A tuple |
| Is this a simple lookup from a name to a value? | A dictionary |
| Does this thing have its own actions or rules to enforce? | A class |
| Will there be many independent instances, each behaving the same way? | A class |
| Am I about to write the same "does X / can X" check in many places? | A class, with that check as a method |

## Your Turn: Decide, Then Justify

```python
# Option A: a plain tuple
launch_date = ("2026-06-29",)

# Option B: a class
class Event:
    def __init__(self, name, date, capacity):
        self.name = name
        self.date = date
        self.capacity = capacity
        self.registered = 0

    def register(self, count):
        if self.registered + count > self.capacity:
            print("Not enough capacity.")
        else:
            self.registered += count

fest = Event("Annual Fest", "2026-03-15", 500)
fest.register(120)
print(fest.registered)    # 120
```

A bare launch date is a single fixed fact with no behaviour, so a tuple, or even just a string, is enough; nothing about it needs protecting or reasoning about. An event with a capacity that must never be exceeded by a registration is exactly the kind of rule-enforcing behaviour that earns a class its place.

## Conclusion

Reach for a plain variable, tuple, or dictionary when you are holding standalone values or a flat group of facts with no behaviour attached, and reach for a class the moment a real-world thing needs its own actions, questions it can answer about itself, or rules it must always enforce on its own data. Across this entire unit, you have learned to define a class, instantiate independent objects, attach attributes, write methods that reason through `self`, guarantee completeness with `__init__`, and now judge when a class is actually the right tool at all. That judgment, knowing when OOP helps and when it is unnecessary ceremony, is exactly what separates code that merely uses classes from code that uses them well.
