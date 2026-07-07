## Introduction

The trip fund split used to involve four people, reliably, every time, until one trip had five contributors and another had only three. Naveen cannot write a parameter for every possible headcount in advance, and he does not want a separate function for three people, a separate one for four, and another for five. What he actually needs is a function that accepts any number of contributions at all, decided fresh at each call, with no upper limit fixed in the definition.

Python provides exactly this with `*args`, which gathers any number of extra positional arguments into a single tuple, and its cousin `**kwargs`, which gathers any number of extra named arguments into a dictionary.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-8-functions/05_variable_args_gathering.png)

## *args: Any Number of Positional Arguments

A parameter written with a single star gathers every extra positional argument into a tuple.

```python
def total_contributions(*amounts):
    return sum(amounts)

print(total_contributions(300, 300, 300, 300))         # 1200
print(total_contributions(500, 400, 600))                # 1500
print(total_contributions(1000))                          # 1000
```

The name `amounts` is ordinary; the single star in front of it is what tells Python "collect everything here, however many there are." Inside the function, `amounts` behaves exactly like the tuples you already know from the lists and tuples unit, so `sum(amounts)` works immediately, and so would looping over it with a `for`.

## You Can Still Mix in Ordinary Parameters

`*args` does not have to be the only parameter; it simply has to come after any required, ordinary ones.

```python
def describe_trip(destination, *contributors):
    print(f"Trip to {destination} with {len(contributors)} contributors:")
    for name in contributors:
        print(f"  {name}")

describe_trip("Goa", "Asha", "Ravi", "Meera")
```

`destination` takes the first argument as always, and every argument after it, however many there are, gets swept into the `contributors` tuple.

## **kwargs: Any Number of Named Arguments

Two stars in front of a parameter name gather any number of extra keyword arguments into a dictionary instead of a tuple.

```python
def build_profile(**details):
    return details

profile = build_profile(name="Naveen", role="treasurer", year=2)
print(profile)    # {'name': 'Naveen', 'role': 'treasurer', 'year': 2}
```

Each keyword used in the call, `name`, `role`, `year`, becomes a key in the resulting dictionary, with whatever value was supplied. This is exactly the dictionary-from-pairs idea from the sets and dictionaries unit, just built automatically from a function call instead of typed out by hand.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-8-functions/05_args_kwargs_unpacking.png)


## Why the Names args and kwargs?

The single and double stars are what actually matter to Python; the names `args` and `kwargs` are simply the overwhelmingly common convention, short for "arguments" and "keyword arguments." You could legally write `*numbers` or `**details` instead, and both lessons above already did exactly that, but recognising `*args` and `**kwargs` by sight matters, because you will see this exact convention in almost every Python codebase and library you read from here on.

## Using Both Together

A function can accept ordinary parameters, `*args`, and `**kwargs` all at once, provided they appear in that order: ordinary parameters, then `*args`, then `**kwargs`.

```python
def register(event, *attendees, **details):
    print(f"Event: {event}")
    print(f"Attendees: {attendees}")
    print(f"Extra details: {details}")

register("Fest", "Asha", "Ravi", venue="Auditorium", entry_fee=0)
```

Output:

```
Event: Fest
Attendees: ('Asha', 'Ravi')
Extra details: {'venue': 'Auditorium', 'entry_fee': 0}
```

Every plain positional argument after `event` falls into `attendees`, and every keyword argument falls into `details`, sorted automatically by how each one was supplied.

## *args and **kwargs at a Glance

| Syntax | Gathers | Type Inside the Function |
|---|---|---|
| `*args` | Any number of extra positional arguments | Tuple |
| `**kwargs` | Any number of extra keyword arguments | Dictionary |
| Order in a definition | Ordinary parameters, then `*args`, then `**kwargs` | n/a |

## Your Turn: A Flexible Total

```python
def trip_summary(destination, *contributions, **extra_info):
    print(f"Destination: {destination}")
    print(f"Total collected: {sum(contributions)}")
    for key, value in extra_info.items():
        print(f"{key}: {value}")

trip_summary("Goa", 500, 400, 600, organiser="Naveen", days=3)
```

Call this with a different number of contributions and a different set of extra details each time, and notice the same function definition handles every shape of call without complaint.

## Conclusion

`*args` gathers any number of extra positional arguments into a tuple, and `**kwargs` gathers any number of extra keyword arguments into a dictionary, freeing a function from needing to know in advance exactly how many inputs a call will bring. The two can be combined with ordinary parameters, always in the order ordinary parameters, then `*args`, then `**kwargs`. With functions now this flexible, the next lesson turns to a much shorter way to write a small, throwaway function: the lambda.
