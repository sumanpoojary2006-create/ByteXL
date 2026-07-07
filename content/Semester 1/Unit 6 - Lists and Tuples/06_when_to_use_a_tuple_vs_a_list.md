## Introduction

Dev now has both tools in hand: the list, which bent and reshaped itself through every snack-list edit and playlist reorder, and the tuple, which locked his GPS stops the instant he created them. Sitting down to plan the rest of the trip data, he realises he is constantly making a small decision without even noticing: is this collection of values going to change while the program runs, or is it fixed the moment it is written down? That one question decides which container belongs in the code.

This lesson does not introduce anything new. It is a direct comparison, so the choice between a list and a tuple becomes an instant, confident decision rather than a guess.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-6-lists-and-tuples/06_list_vs_tuple_scale.png)

## The One Question That Decides It

Before writing a single bracket, ask: will the contents of this collection need to change after I create it? If yes, reach for a list. If no, a tuple is the better, safer fit.

```python
snacks = ["chips", "biscuits"]          # will grow and shrink -> list
resort_coords = (15.2993, 74.1240)      # will never change -> tuple
print(resort_coords)
```

The snack list is genuinely a moving target throughout planning. The resort's coordinates are a fact, fixed the moment they are looked up, and there is no reasonable scenario where the program itself should be allowed to edit them.

## Tuples Document Intent

Choosing a tuple is not just about preventing accidental edits, although that matters. It also tells anyone reading your code, including future you, "this set of values belongs together and is not meant to change." A function that returns `(name, lat, long)` is making a small promise about the shape of its result, in a way a list of the same three values would not.

```python
def get_stop():
    return "Dudhsagar Falls", 15.3144, 74.3144

name, lat, long = get_stop()

# Demo:
result = get_stop()
print(f"get_stop() ->", result)
```

Returning a tuple here reads as "these three values are a fixed, related group", which is exactly true, and exactly what a list would obscure.

## A Performance Side Note

Tuples are also slightly lighter and faster for Python to work with than lists, because Python does not need to keep room available for future growth that will never happen. For the small amounts of data in this course, the difference is invisible, but it is one more reason experienced programmers default to a tuple whenever a list's flexibility is not actually needed.

## Mixing Them: A List of Tuples

The two are frequent partners. A common, powerful shape is a list of tuples: a collection that itself can grow, made of individual fixed records.

```python
stops = [
    ("Resort", 15.2993, 74.1240),
    ("Dudhsagar Falls", 15.3144, 74.3144),
    ("Fort", 15.4989, 73.8278),
]
stops.append(("Beach", 15.2832, 73.9862))

for name, lat, long in stops:
    print(f"{name}: ({lat}, {long})")
```

The outer list can grow as Dev adds new stops to the itinerary, while every individual stop, once added, stays exactly as entered. This is precisely the structure real trip-planning data tends to take.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-6-lists-and-tuples/06_list_of_tuples_records.png)


## List vs Tuple at a Glance

| Question | Answer Points To |
|---|---|
| Will items be added or removed later? | List |
| Are these values a fixed, related group? | Tuple |
| Will I return several values together from a function? | Tuple |
| Do I need `sort()`, `append()`, or similar? | List |
| Am I building a collection of fixed records? | List of tuples |

## Your Turn: Choose the Right Container

```python
itinerary = []
itinerary.append(("Day 1", "Travel and check-in"))
itinerary.append(("Day 2", "Waterfall trek"))
itinerary.append(("Day 3", "Beach and departure"))

for day, plan in itinerary:
    print(f"{day}: {plan}")
```

Notice the shape: a list, because the itinerary may still grow a day, holding tuples, because each day's label and plan are a fixed pair once decided.

## Conclusion

Choose a list when the collection itself needs to grow, shrink, or reorder, and choose a tuple when you are grouping a fixed, related set of values that should never change, including whenever a function hands back more than one result at once. The two are not rivals; a list of tuples is one of the most common and useful shapes in real Python code. So far every list and tuple has held one flat row of values; the next lesson asks what happens when an item inside a list is itself another list.
