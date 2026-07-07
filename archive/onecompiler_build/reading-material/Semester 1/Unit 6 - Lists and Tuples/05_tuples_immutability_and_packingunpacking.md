## Introduction

Dev is plotting the trip's fixed stops onto a map: the resort's GPS coordinates, the waterfall's coordinates, the fort's coordinates, each pair of latitude and longitude locked the moment he enters it. These are not values anyone should be editing later. A coordinate is a coordinate; if someone "fixes" the latitude by mistake, the whole bus could end up at the wrong resort. He wants the convenience of grouping two related values together, exactly like a list, but with a guarantee that nobody, including his own code, can quietly change one number and break the pair.

Python's answer is the **tuple**, written with parentheses instead of square brackets, an ordered collection just like a list, but locked the moment it is created.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-6-lists-and-tuples/05_gps_coordinate_lock.png)

## Creating a Tuple

A tuple looks almost like a list, but with round brackets instead of square ones.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X3R1cGxlc19pbW11dGFiaWxpdHlfYW5kX3BhY2tpbmd1bnBhY2tpbmcgY29kZSAxIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAxLnB5IiwiY29kZSI6InJlc29ydCA9ICgxNS4yOTkzLCA3NC4xMjQwKVxucHJpbnQocmVzb3J0KSAgICAgICAgICAjICgxNS4yOTkzLCA3NC4xMjQwKVxucHJpbnQodHlwZShyZXNvcnQpKSAgICAjIDxjbGFzcyAndHVwbGUnPiJ9"
 width="100%"
></iframe>

Indexing and slicing work exactly as they do for lists and strings, because a tuple is an ordered sequence too.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X3R1cGxlc19pbW11dGFiaWxpdHlfYW5kX3BhY2tpbmd1bnBhY2tpbmcgY29kZSAyIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAyLnB5IiwiY29kZSI6InByaW50KHJlc29ydFswXSkgICAgIyAxNS4yOTkzXG5wcmludChyZXNvcnRbMV0pICAgICMgNzQuMTI0MCJ9"
 width="100%"
></iframe>

A tuple of a single item needs a trailing comma to be recognised as a tuple at all, since parentheses alone are just grouping: `(5,)` is a one-item tuple, while `(5)` is simply the number 5.

## The Defining Trait: Immutability

Try to change a tuple's contents and Python refuses immediately, just as it does for a string.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X3R1cGxlc19pbW11dGFiaWxpdHlfYW5kX3BhY2tpbmd1bnBhY2tpbmcgY29kZSAzIiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDAzLnB5IiwiY29kZSI6InJlc29ydFswXSA9IDE2LjAgICAjIGVycm9yISJ9"
 width="100%"
></iframe>

This raises a `TypeError`, because tuples do not support item assignment. There is no `append`, `insert`, `remove`, or `pop` on a tuple either, because every one of those methods exists to change a list in place, and a tuple makes no such promise. Once a tuple is built, it is built for good.

## Packing: Building a Tuple Without the Parentheses

Python lets you create a tuple just by separating values with commas, even without the parentheses; this is called packing.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X3R1cGxlc19pbW11dGFiaWxpdHlfYW5kX3BhY2tpbmd1bnBhY2tpbmcgY29kZSA0IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA0LnB5IiwiY29kZSI6InN0b3AgPSBcIkR1ZGhzYWdhciBGYWxsc1wiLCAxNS4zMTQ0LCA3NC4zMTQ0XG5wcmludChzdG9wKSAgICAjICgnRHVkaHNhZ2FyIEZhbGxzJywgMTUuMzE0NCwgNzQuMzE0NCkifQ"
 width="100%"
></iframe>

The parentheses are usually added for clarity, but the commas are doing the real work of packing the values together.

## Unpacking: Pulling a Tuple Apart Into Variables

The reverse trick is just as useful: assign a tuple straight into several variable names at once, one per position.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X3R1cGxlc19pbW11dGFiaWxpdHlfYW5kX3BhY2tpbmd1bnBhY2tpbmcgY29kZSA1IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA1LnB5IiwiY29kZSI6Im5hbWUsIGxhdCwgbG9uZyA9IHN0b3BcbnByaW50KG5hbWUpICAgICMgRHVkaHNhZ2FyIEZhbGxzXG5wcmludChsYXQpICAgICAjIDE1LjMxNDRcbnByaW50KGxvbmcpICAgICMgNzQuMzE0NCJ9"
 width="100%"
></iframe>

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

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA1X3R1cGxlc19pbW11dGFiaWxpdHlfYW5kX3BhY2tpbmd1bnBhY2tpbmcgY29kZSA2IiwibGFuZ3VhZ2UiOiJweXRob24iLCJmaWxlbmFtZSI6Im1haW5fMDA2LnB5IiwiY29kZSI6Im5hbWUgPSBpbnB1dChcIlN0b3AgbmFtZTogXCIpXG5sYXQgPSBmbG9hdChpbnB1dChcIkxhdGl0dWRlOiBcIikpXG5sb25nID0gZmxvYXQoaW5wdXQoXCJMb25naXR1ZGU6IFwiKSlcblxuc3RvcCA9IChuYW1lLCBsYXQsIGxvbmcpXG5wcmludChcIlBhY2tlZDpcIiwgc3RvcClcblxuc3RvcF9uYW1lLCBzdG9wX2xhdCwgc3RvcF9sb25nID0gc3RvcFxucHJpbnQoZlwiVW5wYWNrZWQ6IHtzdG9wX25hbWV9IGlzIGF0ICh7c3RvcF9sYXR9LCB7c3RvcF9sb25nfSlcIikifQ"
 width="100%"
></iframe>

Enter a place and its coordinates, watch them pack into one tuple, and then unpack straight back into three readable variables.

## Conclusion

A tuple is an ordered, immutable sequence written in parentheses: indexable and sliceable like a list, but permanently locked once created, with no methods that change its contents. Packing builds a tuple from comma-separated values, and unpacking spreads a tuple straight into matching variables. With both a flexible container and a locked one now in hand, the next lesson tackles the practical question every programmer eventually asks: which one do you actually reach for?
