## Introduction

The fest committee announces a closing-day sale: every item at the merch stall gets a flat 20 percent discount for the last hour. Tara could loop through her price dictionary, build a brand new empty dictionary, and add a discounted entry for each item one at a time, the same setup-loop-store pattern you have now seen for lists. It would work, but you already know there is usually a shorter way to say "build a new collection from an existing one by a simple rule."

Just as list comprehensions built a new list from an old one in a single line, a **dictionary comprehension** builds a new dictionary from an existing one, transforming or filtering its entries as it goes.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-7-sets-and-dictionaries/06_discounted_price_comprehension.png)

## The Long Way First

Here is the loop a dictionary comprehension is about to replace.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-7-sets-and-dictionaries-06-dictionary-comprehensions-001-021ffb8406.html"
 width="100%"
></iframe>

Set up an empty dictionary, loop through the pairs, compute a new value, store it under the same key. Four lines for one simple idea: "the same keys, with transformed values."

## The Dictionary Comprehension Way

A dictionary comprehension folds that pattern into a single line, written in curly braces with a `key: value` pair before the `for`.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-7-sets-and-dictionaries-06-dictionary-comprehensions-002-0ac62bd192.html"
 width="100%"
></iframe>

Read it as "item maps to price times 0.8, for every item, price pair in the original prices." The general shape is `{key_expr: value_expr for key, value in dictionary.items() if condition}`, and just like with list comprehensions, the `if` part is optional.

## Filtering With a Dictionary Comprehension

Add a condition to keep only the entries that pass a test, exactly as you filtered a list earlier in the course.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-7-sets-and-dictionaries-06-dictionary-comprehensions-003-95a8ea9448.html"
 width="100%"
></iframe>

This is exactly the kind of quick "show me only what is actually sellable" view Tara needs without permanently deleting the sold-out entries from her real records.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-7-sets-and-dictionaries/06_dict_comprehension_filter_transform.png)


## Building a Dictionary From Two Lists

A dictionary comprehension is also a clean way to pair up two related lists into key-value form, often combined with `zip` from the previous unit.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-7-sets-and-dictionaries-06-dictionary-comprehensions-004-6460c24e7f.html"
 width="100%"
></iframe>

`zip` pairs the two lists position by position, and the comprehension turns each pair straight into a dictionary entry, all in one readable line.

## When to Reach for a Dictionary Comprehension

| Situation | Better Choice |
|---|---|
| Transforming or filtering an existing dictionary with a simple rule | Dictionary comprehension |
| The logic needs several steps or has side effects | A regular `for` loop |
| Building a lookup from two related lists | Dictionary comprehension with `zip` |

## Your Turn: Build a Sale Price List

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-7-sets-and-dictionaries-06-dictionary-comprehensions-005-02fb3792ee.html"
 width="100%"
></iframe>

Enter a discount and watch one comprehension build the whole sale list, then a second one filter straight from the result of the first.

## Conclusion

A dictionary comprehension, written as `{key: value for key, value in dictionary.items() if condition}`, builds a new dictionary from an existing one in a single line, whether transforming every value, filtering entries, or pairing up two related lists with `zip`. So far every dictionary has held one flat layer of values; the next lesson asks what happens when a value inside a dictionary is itself another dictionary.
