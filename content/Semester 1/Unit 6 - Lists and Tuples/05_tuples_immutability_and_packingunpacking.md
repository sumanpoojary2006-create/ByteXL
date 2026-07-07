## Introduction

Dev is plotting the trip's fixed stops onto a map: the resort's GPS coordinates, the waterfall's coordinates, the fort's coordinates, each pair of latitude and longitude locked the moment he enters it. These are not values anyone should be editing later. A coordinate is a coordinate; if someone "fixes" the latitude by mistake, the whole bus could end up at the wrong resort. He wants the convenience of grouping two related values together, exactly like a list, but with a guarantee that nobody, including his own code, can quietly change one number and break the pair.

Python's answer is the **tuple**, written with parentheses instead of square brackets, an ordered collection just like a list, but locked the moment it is created.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-6-lists-and-tuples/05_gps_coordinate_lock.png)

## Creating a Tuple

A tuple looks almost like a list, but with round brackets instead of square ones.

```python
resort = (15.2993, 74.1240)
print(resort)          # (15.2993, 74.1240)
print(type(resort))    # <class 'tuple'>
```

Indexing and slicing work exactly as they do for lists and strings, because a tuple is an ordered sequence too.

```python
resort = (15.2993, 74.1240)
print(resort[0])    # 15.2993
print(resort[1])    # 74.1240
```

A tuple of a single item needs a trailing comma to be recognised as a tuple at all, since parentheses alone are just grouping: `(5,)` is a one-item tuple, while `(5)` is simply the number 5.

## The Defining Trait: Immutability

Try to change a tuple's contents and Python refuses immediately, just as it does for a string.

```python
resort = (15.2993, 74.1240)
resort[0] = 16.0    # TypeError: 'tuple' object does not support item assignment
```

```text
TypeError: 'tuple' object does not support item assignment
```

This raises a `TypeError`, because tuples do not support item assignment. There is no `append`, `insert`, `remove`, or `pop` on a tuple either, because every one of those methods exists to change a list in place, and a tuple makes no such promise. Once a tuple is built, it is built for good.

## Packing: Building a Tuple Without the Parentheses

Python lets you create a tuple just by separating values with commas, even without the parentheses; this is called packing.

```python
stop = "Dudhsagar Falls", 15.3144, 74.3144
print(stop)    # ('Dudhsagar Falls', 15.3144, 74.3144)
```

The parentheses are usually added for clarity, but the commas are doing the real work of packing the values together.

## Unpacking: Pulling a Tuple Apart Into Variables

The reverse trick is just as useful: assign a tuple straight into several variable names at once, one per position.

```python
stop = "Dudhsagar Falls", 15.3144, 74.3144
name, lat, long = stop
print(name)    # Dudhsagar Falls
print(lat)     # 15.3144
print(long)    # 74.3144
```

Python matches each variable to its position automatically. The number of variables on the left must match the number of items in the tuple, or Python raises a `ValueError` complaining about too many or too few values to unpack. This packing and unpacking pair is also exactly how a function will later hand back several results from one call.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-6-lists-and-tuples/05_tuple_packing_unpacking.png)


## Tuple vs List Syntax at a Glance

| Feature | List | Tuple |
|---|---|---|
| Brackets | `[ ]` | `( )` |
| Can change contents | Yes | No |
| Has `append`, `remove`, `sort` | Yes | No |
| Indexing and slicing | Yes | Yes |
| Single-item form | `[5]` | `(5,)` with a required comma |

## Your Turn: Pack and Unpack a Stop

```python
name = input("Stop name: ")
lat = float(input("Latitude: "))
long = float(input("Longitude: "))

stop = (name, lat, long)
print("Packed:", stop)

stop_name, stop_lat, stop_long = stop
print(f"Unpacked: {stop_name} is at ({stop_lat}, {stop_long})")
```

Enter a place and its coordinates, watch them pack into one tuple, and then unpack straight back into three readable variables.

## Conclusion

A tuple is an ordered, immutable sequence written in parentheses: indexable and sliceable like a list, but permanently locked once created, with no methods that change its contents. Packing builds a tuple from comma-separated values, and unpacking spreads a tuple straight into matching variables. With both a flexible container and a locked one now in hand, the next lesson tackles the practical question every programmer eventually asks: which one do you actually reach for?
