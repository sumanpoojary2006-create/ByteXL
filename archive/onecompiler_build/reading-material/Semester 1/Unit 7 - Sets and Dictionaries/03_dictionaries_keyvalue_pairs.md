## Introduction

Tara has moved from the gate to the merchandise stall, selling fest T-shirts, mugs, and badges. A customer asks the price of a mug, and Tara could keep two separate lists, one of item names and one of matching prices, then search the names list for "mug" and read off whatever price sits at the same position. It would work, but it is a clumsy, error-prone way to ask a question that should be instant: "what does a mug cost?"

What Tara actually wants is to ask for "mug" directly and get 150 back immediately, with no searching at all. That is exactly what a **dictionary** gives you: a collection of key-value pairs, where you look a value up by its key instead of by its position.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-7-sets-and-dictionaries/03_merch_price_lookup.png)

## Creating a Dictionary

A dictionary is written in curly braces, with each entry as `key: value`, separated by commas.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2RpY3Rpb25hcmllc19rZXl2YWx1ZV9wYWlycyBjb2RlIDEiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDEucHkiLCJjb2RlIjoicHJpY2VzID0ge1wiVC1zaGlydFwiOiAzNTAsIFwiTXVnXCI6IDE1MCwgXCJCYWRnZVwiOiA1MH1cbnByaW50KHByaWNlcykifQ"
 width="100%"
></iframe>

Each key, here an item name, is paired directly with its value, here a price. Keys are usually strings or numbers, and within one dictionary every key must be unique. If you accidentally repeat a key, the later value simply overwrites the earlier one, since a key can only ever point to one value at a time.

## Looking Up a Value by Key

Reach a value with square brackets, exactly as you would index a list, except you supply a key instead of a position.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2RpY3Rpb25hcmllc19rZXl2YWx1ZV9wYWlycyBjb2RlIDIiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDIucHkiLCJjb2RlIjoicHJpbnQocHJpY2VzW1wiTXVnXCJdKSAgICAjIDE1MCJ9"
 width="100%"
></iframe>

This is the instant lookup Tara wanted: no searching, no scanning, just naming the key and getting its value straight back. Ask for a key that does not exist, though, and Python raises a `KeyError`.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2RpY3Rpb25hcmllc19rZXl2YWx1ZV9wYWlycyBjb2RlIDMiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDMucHkiLCJjb2RlIjoicHJpbnQocHJpY2VzW1wiQ2FwXCJdKSAgICAjIGVycm9yISJ9"
 width="100%"
></iframe>

The error names the missing key directly, which is your signal that the key simply was never added, not that something is broken.

## Checking Whether a Key Exists

Before looking up a key that might not be there, check with `in`, exactly as you checked membership in a set.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2RpY3Rpb25hcmllc19rZXl2YWx1ZV9wYWlycyBjb2RlIDQiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDQucHkiLCJjb2RlIjoiaXRlbSA9IFwiQ2FwXCJcbmlmIGl0ZW0gaW4gcHJpY2VzOlxuICAgIHByaW50KHByaWNlc1tpdGVtXSlcbmVsc2U6XG4gICAgcHJpbnQoZlwie2l0ZW19IGlzIG5vdCBzb2xkIGhlcmUuXCIpIn0"
 width="100%"
></iframe>

Note carefully that `in` on a dictionary checks the keys, not the values. Asking `350 in prices` checks whether 350 is one of the keys (it is not), not whether it appears anywhere as a price.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-7-sets-and-dictionaries/03_unique_keys_replace_values.png)


## Counting Entries: len()

`len()` on a dictionary counts the number of key-value pairs, not the number of individual values.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2RpY3Rpb25hcmllc19rZXl2YWx1ZV9wYWlycyBjb2RlIDUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDUucHkiLCJjb2RlIjoicHJpbnQobGVuKHByaWNlcykpICAgICMgMyJ9"
 width="100%"
></iframe>

## Dictionaries vs Lists at a Glance

| Feature | List | Dictionary |
|---|---|---|
| Brackets | `[ ]` | `{ }` |
| Lookup by | Position (`0`, `1`, ...) | Key (`"Mug"`, `"Badge"`, ...) |
| Missing lookup raises | `IndexError` | `KeyError` |
| Order | Items in sequence | Insertion order is preserved, but lookup is by key, not position |
| Best for | A sequence of values | A value looked up by a meaningful name |

## Your Turn: A Tiny Price Checker

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAzX2RpY3Rpb25hcmllc19rZXl2YWx1ZV9wYWlycyBjb2RlIDYiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDYucHkiLCJjb2RlIjoicHJpY2VzID0ge1wiVC1zaGlydFwiOiAzNTAsIFwiTXVnXCI6IDE1MCwgXCJCYWRnZVwiOiA1MH1cbml0ZW0gPSBpbnB1dChcIldoaWNoIGl0ZW0ncyBwcmljZSB3b3VsZCB5b3UgbGlrZT8gXCIpXG5cbmlmIGl0ZW0gaW4gcHJpY2VzOlxuICAgIHByaW50KGZcIntpdGVtfSBjb3N0cyB7cHJpY2VzW2l0ZW1dfS5cIilcbmVsc2U6XG4gICAgcHJpbnQoZlwiU29ycnksIHtpdGVtfSBpcyBub3Qgc29sZCBoZXJlLlwiKSJ9"
 width="100%"
></iframe>

Try "Mug" and then something not on the list, like "Cap", and notice the program never crashes either way, because the membership check runs before the lookup.

## Conclusion

A dictionary stores key-value pairs in curly braces, with each value looked up directly by its key using square brackets, raising a `KeyError` for a missing key and answered safely with an `in` check beforehand. Where a list answers "what is at this position", a dictionary answers "what is paired with this name." Reading a price is only half the job at a real stall, though; the next lesson covers adding new items, updating prices, and removing what has sold out.
