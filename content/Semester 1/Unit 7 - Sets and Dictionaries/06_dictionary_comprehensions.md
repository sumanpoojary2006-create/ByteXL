## Introduction

The fest committee announces a closing-day sale: every item at the merch stall gets a flat 20 percent discount for the last hour. Tara could loop through her price dictionary, build a brand new empty dictionary, and add a discounted entry for each item one at a time, the same setup-loop-store pattern you have now seen for lists. It would work, but you already know there is usually a shorter way to say "build a new collection from an existing one by a simple rule."

Just as list comprehensions built a new list from an old one in a single line, a **dictionary comprehension** builds a new dictionary from an existing one, transforming or filtering its entries as it goes.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-7-sets-and-dictionaries/06_discounted_price_comprehension.png)

## The Long Way First

Here is the loop a dictionary comprehension is about to replace.

```python
prices = {"T-shirt": 350, "Mug": 150, "Badge": 50}
discounted = {}
for item, price in prices.items():
    discounted[item] = price * 0.8
print(discounted)
```

Set up an empty dictionary, loop through the pairs, compute a new value, store it under the same key. Four lines for one simple idea: "the same keys, with transformed values."

## The Dictionary Comprehension Way

A dictionary comprehension folds that pattern into a single line, written in curly braces with a `key: value` pair before the `for`.

```python
prices = {"T-shirt": 350, "Mug": 150, "Badge": 50}
discounted = {item: price * 0.8 for item, price in prices.items()}
print(discounted)    # {'T-shirt': 280.0, 'Mug': 120.0, 'Badge': 40.0}
```

Read it as "item maps to price times 0.8, for every item, price pair in the original prices." The general shape is `{key_expr: value_expr for key, value in dictionary.items() if condition}`, and just like with list comprehensions, the `if` part is optional.

## Filtering With a Dictionary Comprehension

Add a condition to keep only the entries that pass a test, exactly as you filtered a list earlier in the course.

```python
stock = {"T-shirt": 12, "Mug": 0, "Badge": 25, "Cap": 0}
in_stock = {item: count for item, count in stock.items() if count > 0}
print(in_stock)    # {'T-shirt': 12, 'Badge': 25}
```

This is exactly the kind of quick "show me only what is actually sellable" view Tara needs without permanently deleting the sold-out entries from her real records.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-7-sets-and-dictionaries/06_dict_comprehension_filter_transform.png)


## Building a Dictionary From Two Lists

A dictionary comprehension is also a clean way to pair up two related lists into key-value form, often combined with `zip` from the previous unit.

```python
items = ["T-shirt", "Mug", "Badge"]
prices_list = [350, 150, 50]
prices = {item: price for item, price in zip(items, prices_list)}
print(prices)    # {'T-shirt': 350, 'Mug': 150, 'Badge': 50}
```

`zip` pairs the two lists position by position, and the comprehension turns each pair straight into a dictionary entry, all in one readable line.

## When to Reach for a Dictionary Comprehension

| Situation | Better Choice |
|---|---|
| Transforming or filtering an existing dictionary with a simple rule | Dictionary comprehension |
| The logic needs several steps or has side effects | A regular `for` loop |
| Building a lookup from two related lists | Dictionary comprehension with `zip` |

## Your Turn: Build a Sale Price List

This example rounds each sale price to 2 decimal places with the built-in `round(value, digits)` function, so a price like 280.444 becomes a clean 280.44 instead of trailing off with extra decimals.

```python
prices = {"T-shirt": 350, "Mug": 150, "Badge": 50, "Cap": 200}
discount = float(input("Discount fraction, e.g. 0.2 for 20 percent: "))

sale_prices = {item: round(price * (1 - discount), 2) for item, price in prices.items()}
print("Sale prices:", sale_prices)

cheap_items = {item: price for item, price in sale_prices.items() if price < 150}
print("Under 150 after discount:", cheap_items)
```

Enter a discount and watch one comprehension build the whole sale list, then a second one filter straight from the result of the first.

## Conclusion

A dictionary comprehension, written as `{key: value for key, value in dictionary.items() if condition}`, builds a new dictionary from an existing one in a single line, whether transforming every value, filtering entries, or pairing up two related lists with `zip`. So far every dictionary has held one flat layer of values; the next lesson asks what happens when a value inside a dictionary is itself another dictionary.
