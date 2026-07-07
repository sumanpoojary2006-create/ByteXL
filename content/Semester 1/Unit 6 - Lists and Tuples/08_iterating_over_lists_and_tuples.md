## Introduction

The trip is two days away, and Dev has the full itinerary sitting in front of him: a list of fixed day-and-plan tuples, a packing list, a snack list, a seating chart. None of this data is useful sitting still. He needs to walk through the itinerary morning by morning and read each plan aloud at the class briefing, and he wants to do it without typing `itinerary[0]`, then `itinerary[1]`, then `itinerary[2]` by hand like it is still the very first lesson of this unit.

You already know the `for` loop from the looping unit, and you have been quietly using it on lists and tuples throughout this one. This final lesson pulls those threads together properly, showing the small set of patterns that make looping over lists and tuples clean, readable, and complete.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-6-lists-and-tuples/08_itinerary_walkthrough.png)

## The Basic Walk-Through

A plain `for` loop visits every item of a list or tuple in order, with no indexing required at all.

```python
packing_list = ["water bottle", "charger", "ID card", "raincoat"]
for item in packing_list:
    print("Pack:", item)
```

This reads exactly as "for each item in the packing list, print it", and it works identically whether the collection is a list or a tuple, since both are ordered sequences a `for` loop can step through directly.

## When You Also Need the Position: enumerate()

Sometimes the position matters as much as the value, for example when numbering each day of the itinerary. `enumerate` hands you both the index and the item together.

```python
itinerary = ["Travel and check-in", "Waterfall trek", "Beach and departure"]
for day, plan in enumerate(itinerary, start=1):
    print(f"Day {day}: {plan}")
```

The `start=1` makes the numbering begin at 1 instead of 0, which reads far more naturally for a human audience than starting from zero would.

## Unpacking Tuples Inside a Loop

When a list holds tuples, you can unpack each tuple directly in the loop header, naming its parts instead of indexing into them one by one.

```python
stops = [
    ("Resort", 15.2993, 74.1240),
    ("Dudhsagar Falls", 15.3144, 74.3144),
]
for name, lat, long in stops:
    print(f"{name} is at ({lat}, {long})")
```

Each pass automatically unpacks the current tuple into `name`, `lat`, and `long`, exactly the packing-and-unpacking idea from earlier in this unit, now happening once per loop pass.

## Looping Over Two Lists Together: zip()

Occasionally you have two separate, related lists, such as student names and their seat numbers, and you want to walk through both together. `zip` pairs them up, position by position.

```python
names = ["Asha", "Ravi", "Meera"]
seats = [1, 2, 3]
for name, seat in zip(names, seats):
    print(f"{name} is in seat {seat}")
```

`zip` stops as soon as the shorter list runs out, so it is safest when both lists are meant to be the same length, which is exactly true of names lined up against their assigned seats.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-6-lists-and-tuples/08_enumerate_zip_unpacks.png)


## Looping Patterns at a Glance

| Goal | Pattern |
|---|---|
| Visit every value | `for item in collection:` |
| Visit value and position | `for index, item in enumerate(collection):` |
| Visit each tuple's parts directly | `for a, b, c in list_of_tuples:` |
| Walk two lists together | `for a, b in zip(list1, list2):` |

## Your Turn: Read Out the Itinerary

```python
itinerary = [
    ("Day 1", "Travel and check-in"),
    ("Day 2", "Waterfall trek"),
    ("Day 3", "Beach and departure"),
]

for day, plan in itinerary:
    print(f"{day}: {plan}")

print("\n--- Numbered version ---")
for number, (day, plan) in enumerate(itinerary, start=1):
    print(f"{number}. {day} - {plan}")
```

Notice the second loop unpacks a tuple from inside an `enumerate` call, combining two patterns from this lesson at once, exactly the kind of small combination real itineraries end up needing.

## Conclusion

A plain `for` loop steps through a list or tuple directly; `enumerate` adds the position when you need it; unpacking inside the loop header reads tuple parts by name instead of by index; and `zip` walks two related lists together, position by position. Across this entire unit you have learned to hold data in order, change it, organise it, filter it, lock it, group it, nest it, and now walk through it cleanly. Lists and tuples, together with the loops you already knew, are the backbone of almost every real program you will write from here on.
