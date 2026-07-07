## Introduction

The fest committee announces a closing-day sale: every item at the merch stall gets a flat 20 percent discount for the last hour. Tara could loop through her price dictionary, build a brand new empty dictionary, and add a discounted entry for each item one at a time, the same setup-loop-store pattern you have now seen for lists. It would work, but you already know there is usually a shorter way to say "build a new collection from an existing one by a simple rule."

Just as list comprehensions built a new list from an old one in a single line, a **dictionary comprehension** builds a new dictionary from an existing one, transforming or filtering its entries as it goes.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-7-sets-and-dictionaries/06_discounted_price_comprehension.png)

## The Long Way First

Here is the loop a dictionary comprehension is about to replace.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2RpY3Rpb25hcnlfY29tcHJlaGVuc2lvbnMgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6InByaWNlcyA9IHtcIlQtc2hpcnRcIjogMzUwLCBcIk11Z1wiOiAxNTAsIFwiQmFkZ2VcIjogNTB9XG5kaXNjb3VudGVkID0ge31cbmZvciBpdGVtLCBwcmljZSBpbiBwcmljZXMuaXRlbXMoKTpcbiAgICBkaXNjb3VudGVkW2l0ZW1dID0gcHJpY2UgKiAwLjhcbnByaW50KGRpc2NvdW50ZWQpIn0"
 width="100%"
></iframe>

Set up an empty dictionary, loop through the pairs, compute a new value, store it under the same key. Four lines for one simple idea: "the same keys, with transformed values."

## The Dictionary Comprehension Way

A dictionary comprehension folds that pattern into a single line, written in curly braces with a `key: value` pair before the `for`.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2RpY3Rpb25hcnlfY29tcHJlaGVuc2lvbnMgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6InByaWNlcyA9IHtcIlQtc2hpcnRcIjogMzUwLCBcIk11Z1wiOiAxNTAsIFwiQmFkZ2VcIjogNTB9XG5kaXNjb3VudGVkID0ge2l0ZW06IHByaWNlICogMC44IGZvciBpdGVtLCBwcmljZSBpbiBwcmljZXMuaXRlbXMoKX1cbnByaW50KGRpc2NvdW50ZWQpICAgICMgeydULXNoaXJ0JzogMjgwLjAsICdNdWcnOiAxMjAuMCwgJ0JhZGdlJzogNDAuMH0ifQ"
 width="100%"
></iframe>

Read it as "item maps to price times 0.8, for every item, price pair in the original prices." The general shape is `{key_expr: value_expr for key, value in dictionary.items() if condition}`, and just like with list comprehensions, the `if` part is optional.

## Filtering With a Dictionary Comprehension

Add a condition to keep only the entries that pass a test, exactly as you filtered a list earlier in the course.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2RpY3Rpb25hcnlfY29tcHJlaGVuc2lvbnMgY29kZSAzIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAzLnB5IiwiY29kZSI6InN0b2NrID0ge1wiVC1zaGlydFwiOiAxMiwgXCJNdWdcIjogMCwgXCJCYWRnZVwiOiAyNSwgXCJDYXBcIjogMH1cbmluX3N0b2NrID0ge2l0ZW06IGNvdW50IGZvciBpdGVtLCBjb3VudCBpbiBzdG9jay5pdGVtcygpIGlmIGNvdW50ID4gMH1cbnByaW50KGluX3N0b2NrKSAgICAjIHsnVC1zaGlydCc6IDEyLCAnQmFkZ2UnOiAyNX0ifQ"
 width="100%"
></iframe>

This is exactly the kind of quick "show me only what is actually sellable" view Tara needs without permanently deleting the sold-out entries from her real records.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-7-sets-and-dictionaries/06_dict_comprehension_filter_transform.png)


## Building a Dictionary From Two Lists

A dictionary comprehension is also a clean way to pair up two related lists into key-value form, often combined with `zip` from the previous unit.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2RpY3Rpb25hcnlfY29tcHJlaGVuc2lvbnMgY29kZSA0IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA0LnB5IiwiY29kZSI6Iml0ZW1zID0gW1wiVC1zaGlydFwiLCBcIk11Z1wiLCBcIkJhZGdlXCJdXG5wcmljZXNfbGlzdCA9IFszNTAsIDE1MCwgNTBdXG5wcmljZXMgPSB7aXRlbTogcHJpY2UgZm9yIGl0ZW0sIHByaWNlIGluIHppcChpdGVtcywgcHJpY2VzX2xpc3QpfVxucHJpbnQocHJpY2VzKSAgICAjIHsnVC1zaGlydCc6IDM1MCwgJ011Zyc6IDE1MCwgJ0JhZGdlJzogNTB9In0"
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
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA2X2RpY3Rpb25hcnlfY29tcHJlaGVuc2lvbnMgY29kZSA1IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA1LnB5IiwiY29kZSI6InByaWNlcyA9IHtcIlQtc2hpcnRcIjogMzUwLCBcIk11Z1wiOiAxNTAsIFwiQmFkZ2VcIjogNTAsIFwiQ2FwXCI6IDIwMH1cbmRpc2NvdW50ID0gZmxvYXQoaW5wdXQoXCJEaXNjb3VudCBmcmFjdGlvbiwgZS5nLiAwLjIgZm9yIDIwIHBlcmNlbnQ6IFwiKSlcblxuc2FsZV9wcmljZXMgPSB7aXRlbTogcm91bmQocHJpY2UgKiAoMSAtIGRpc2NvdW50KSwgMikgZm9yIGl0ZW0sIHByaWNlIGluIHByaWNlcy5pdGVtcygpfVxucHJpbnQoXCJTYWxlIHByaWNlczpcIiwgc2FsZV9wcmljZXMpXG5cbmNoZWFwX2l0ZW1zID0ge2l0ZW06IHByaWNlIGZvciBpdGVtLCBwcmljZSBpbiBzYWxlX3ByaWNlcy5pdGVtcygpIGlmIHByaWNlIDwgMTUwfVxucHJpbnQoXCJVbmRlciAxNTAgYWZ0ZXIgZGlzY291bnQ6XCIsIGNoZWFwX2l0ZW1zKSJ9"
 width="100%"
></iframe>

Enter a discount and watch one comprehension build the whole sale list, then a second one filter straight from the result of the first.

## Conclusion

A dictionary comprehension, written as `{key: value for key, value in dictionary.items() if condition}`, builds a new dictionary from an existing one in a single line, whether transforming every value, filtering entries, or pairing up two related lists with `zip`. So far every dictionary has held one flat layer of values; the next lesson asks what happens when a value inside a dictionary is itself another dictionary.
