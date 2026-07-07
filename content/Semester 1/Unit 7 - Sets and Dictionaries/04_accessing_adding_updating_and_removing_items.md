## Introduction

The merch stall is never still for long. A new shipment of caps arrives partway through the day, so a brand new item needs adding to the price list. The badge price gets revised down to clear stock, so an existing value needs updating. The last mug sells, so the whole entry needs to disappear rather than sit there pointing at stock that no longer exists. Tara is doing to her price dictionary exactly what she once did to a list: changing it freely, in place, while the stall is open.

Dictionaries are mutable just like lists, and this lesson covers the small set of operations that add, change, and remove key-value pairs without ever needing to rebuild the whole dictionary from scratch.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-7-sets-and-dictionaries/04_stall_dictionary_editing.png)

## Adding a New Key

Assign to a key that does not exist yet, and Python creates it.

```python
prices = {"T-shirt": 350, "Mug": 150, "Badge": 50}
prices["Cap"] = 200
print(prices)    # {'T-shirt': 350, 'Mug': 150, 'Badge': 50, 'Cap': 200}
```

There is no separate "add" method to remember here; the square-bracket assignment itself decides whether it is adding or changing, based on one simple rule covered next.

## Updating an Existing Key

Assign to a key that already exists, and Python overwrites its value instead of creating a duplicate.

```python
prices = {"T-shirt": 350, "Mug": 150, "Badge": 50, "Cap": 200}
prices["Badge"] = 30
print(prices["Badge"])    # 30
```

The same `dictionary[key] = value` line either adds or updates, and the only thing that decides which one happens is whether that key was already present. This is worth sitting with for a moment: dictionaries never hold two entries with the same key, so an assignment to an existing key can only ever mean "replace the old value."

## Removing a Key: del and pop

The `del` keyword removes a key-value pair outright, with nothing handed back.

```python
prices = {"T-shirt": 350, "Mug": 150, "Badge": 30, "Cap": 200}
del prices["Mug"]
print(prices)    # Mug is gone entirely
```

`pop`, just like with lists, removes the entry and returns its value, which is handy when you want to use the removed value on your way out.

```python
prices = {"T-shirt": 350, "Badge": 30, "Cap": 200}
sold_out_price = prices.pop("Cap")
print(sold_out_price)    # 200
print(prices)             # Cap is gone, 200 was handed back
```

Both `del` and `pop` raise a `KeyError` if the key does not exist, so it is good practice to check with `in` first whenever you are not certain the key is there.

## Safe Lookups With get()

The `get` method looks up a key without ever raising an error, returning `None`, or a default value you choose, if the key is missing.

```python
prices = {"T-shirt": 350, "Badge": 30}
print(prices.get("Mug"))             # None, since Mug is not in this dict
print(prices.get("Mug", 0))          # 0, the chosen default instead of a crash
```

This is often nicer than an `if key in dictionary:` check followed by a lookup, because `get` does both jobs, look up and fall back safely, in one call.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-7-sets-and-dictionaries/04_get_vs_keyerror.png)


## Dictionary Editing at a Glance

| Action | Code | Notes |
|---|---|---|
| Add a new key | `d[key] = value` | Creates the entry if the key was missing |
| Update an existing key | `d[key] = value` | Same syntax, overwrites the old value |
| Remove a key | `del d[key]` | Raises `KeyError` if missing |
| Remove and return a value | `d.pop(key)` | Raises `KeyError` if missing |
| Look up safely | `d.get(key, default)` | Never raises an error |

## Your Turn: Manage the Stall Live

```python
stock = {"T-shirt": 20, "Mug": 15}

stock["Badge"] = 40
print("After adding Badge:", stock)

stock["Mug"] = stock["Mug"] - 1
print("After one mug sold:", stock)

if "T-shirt" in stock and stock["T-shirt"] == 0:
    del stock["T-shirt"]

print("Stock check for Cap:", stock.get("Cap", "not stocked"))
```

Notice the safe `get` call at the end never risks crashing on a key that was never added in the first place.

## Conclusion

Dictionaries are mutable: assigning to a key either adds it or updates it depending on whether it already exists, `del` and `pop` remove a key with `pop` handing back the removed value, and `get` looks up a key safely with a fallback default. With a stall's worth of items changing all day, the next lesson covers how to walk through the whole dictionary cleanly for an end-of-day report.
