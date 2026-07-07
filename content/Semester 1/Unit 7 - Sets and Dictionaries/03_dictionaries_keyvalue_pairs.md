## Introduction

Tara has moved from the gate to the merchandise stall, selling fest T-shirts, mugs, and badges. A customer asks the price of a mug, and Tara could keep two separate lists, one of item names and one of matching prices, then search the names list for "mug" and read off whatever price sits at the same position. It would work, but it is a clumsy, error-prone way to ask a question that should be instant: "what does a mug cost?"

What Tara actually wants is to ask for "mug" directly and get 150 back immediately, with no searching at all. That is exactly what a **dictionary** gives you: a collection of key-value pairs, where you look a value up by its key instead of by its position.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-7-sets-and-dictionaries/03_merch_price_lookup.png)

## Creating a Dictionary

A dictionary is written in curly braces, with each entry as `key: value`, separated by commas.

```python
prices = {"T-shirt": 350, "Mug": 150, "Badge": 50}
print(prices)
```

Each key, here an item name, is paired directly with its value, here a price. Keys are usually strings or numbers, and within one dictionary every key must be unique. If you accidentally repeat a key, the later value simply overwrites the earlier one, since a key can only ever point to one value at a time.

## Looking Up a Value by Key

Reach a value with square brackets, exactly as you would index a list, except you supply a key instead of a position.

```python
prices = {"T-shirt": 350, "Mug": 150, "Badge": 50}
print(prices["Mug"])    # 150
```

This is the instant lookup Tara wanted: no searching, no scanning, just naming the key and getting its value straight back. Ask for a key that does not exist, though, and Python raises a `KeyError`.

```python
prices = {"T-shirt": 350, "Mug": 150, "Badge": 50}
print(prices["Cap"])    # raises KeyError
```

```
KeyError: 'Cap'
```

The error names the missing key directly, which is your signal that the key simply was never added, not that something is broken.

## Checking Whether a Key Exists

Before looking up a key that might not be there, check with `in`, exactly as you checked membership in a set.

```python
prices = {"T-shirt": 350, "Mug": 150, "Badge": 50}
item = "Cap"
if item in prices:
    print(prices[item])
else:
    print(f"{item} is not sold here.")
```

Note carefully that `in` on a dictionary checks the keys, not the values. Asking `350 in prices` checks whether 350 is one of the keys (it is not), not whether it appears anywhere as a price.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-7-sets-and-dictionaries/03_unique_keys_replace_values.png)


## Counting Entries: len()

`len()` on a dictionary counts the number of key-value pairs, not the number of individual values.

```python
prices = {"T-shirt": 350, "Mug": 150, "Badge": 50}
print(len(prices))    # 3
```

## Dictionaries vs Lists at a Glance

| Feature | List | Dictionary |
|---|---|---|
| Brackets | `[ ]` | `{ }` |
| Lookup by | Position (`0`, `1`, ...) | Key (`"Mug"`, `"Badge"`, ...) |
| Missing lookup raises | `IndexError` | `KeyError` |
| Order | Items in sequence | Insertion order is preserved, but lookup is by key, not position |
| Best for | A sequence of values | A value looked up by a meaningful name |

## Your Turn: A Tiny Price Checker

```python
prices = {"T-shirt": 350, "Mug": 150, "Badge": 50}
item = input("Which item's price would you like? ")

if item in prices:
    print(f"{item} costs {prices[item]}.")
else:
    print(f"Sorry, {item} is not sold here.")
```

Try "Mug" and then something not on the list, like "Cap", and notice the program never crashes either way, because the membership check runs before the lookup.

## Conclusion

A dictionary stores key-value pairs in curly braces, with each value looked up directly by its key using square brackets, raising a `KeyError` for a missing key and answered safely with an `in` check beforehand. Where a list answers "what is at this position", a dictionary answers "what is paired with this name." Reading a price is only half the job at a real stall, though; the next lesson covers adding new items, updating prices, and removing what has sold out.
