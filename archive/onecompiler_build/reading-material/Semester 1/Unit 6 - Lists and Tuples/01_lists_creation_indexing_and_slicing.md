## Introduction

Dev is the one everyone in class trusts to make sure nothing gets left behind on the annual college trip, so the night before departure he opens a fresh note on his phone and types out the master packing checklist exactly in the order he thinks of it: water bottle, charger, ID card, raincoat, snacks. He does not want five separate notes for five separate items. He wants one single note that holds all of them together, in the order he listed them, so he can glance at item three or skim the last two without rereading the whole thing from the top.

That is exactly the job Python's **list** does. A list is an ordered collection of values, written inside square brackets, and it is about to become the single most useful container in your entire toolkit.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-6-lists-and-tuples/01_packing_list_lineup.png)

## Creating a List

A list is written as a comma-separated sequence of values inside square brackets.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX2xpc3RzX2NyZWF0aW9uX2luZGV4aW5nX2FuZF9zbGljaW5nIGNvZGUgMSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMS5weSIsImNvZGUiOiJwYWNraW5nX2xpc3QgPSBbXCJ3YXRlciBib3R0bGVcIiwgXCJjaGFyZ2VyXCIsIFwiSUQgY2FyZFwiLCBcInJhaW5jb2F0XCIsIFwic25hY2tzXCJdXG5wcmludChwYWNraW5nX2xpc3QpIn0"
 width="100%"
></iframe>

That single variable now holds all five items, in the exact order Dev typed them. Unlike a string, which can only hold characters, a list can hold any type of value, and even a mix of types in the same list.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX2xpc3RzX2NyZWF0aW9uX2luZGV4aW5nX2FuZF9zbGljaW5nIGNvZGUgMiIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMi5weSIsImNvZGUiOiJ0cmlwX2luZm8gPSBbXCJHb2FcIiwgMywgNDUwMC41MCwgVHJ1ZV0ifQ"
 width="100%"
></iframe>

Here a list holds a city name, a number of days, a budget, and a boolean, side by side. You will rarely mix types this freely in real code, but Python places no restriction on it, because a list is simply an ordered container, not a fixed shape.

## Counting and Reaching Items: len() and Indexing

Just as with strings, `len()` tells you how many items a list holds, and square brackets reach a single item by its position, counting from 0.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX2xpc3RzX2NyZWF0aW9uX2luZGV4aW5nX2FuZF9zbGljaW5nIGNvZGUgMyIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwMy5weSIsImNvZGUiOiJwYWNraW5nX2xpc3QgPSBbXCJ3YXRlciBib3R0bGVcIiwgXCJjaGFyZ2VyXCIsIFwiSUQgY2FyZFwiLCBcInJhaW5jb2F0XCIsIFwic25hY2tzXCJdXG5wcmludChsZW4ocGFja2luZ19saXN0KSkgICAgICAgIyA1XG5wcmludChwYWNraW5nX2xpc3RbMF0pICAgICAgICAgIyB3YXRlciBib3R0bGVcbnByaW50KHBhY2tpbmdfbGlzdFsyXSkgICAgICAgICAjIElEIGNhcmRcbnByaW50KHBhY2tpbmdfbGlzdFstMV0pICAgICAgICAjIHNuYWNrcyJ9"
 width="100%"
></iframe>

Negative indices count from the end exactly as they did for strings, so `packing_list[-1]` is the last item Dev added without him needing to know there are five items in total. Ask for a position that does not exist, such as `packing_list[10]`, and Python raises the same `IndexError` you met with strings: the valid indices always run from 0 to the length minus one.

## Slicing a List

Slicing works on lists exactly as it did on strings: a start and a stop separated by a colon, with the stop excluded.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX2xpc3RzX2NyZWF0aW9uX2luZGV4aW5nX2FuZF9zbGljaW5nIGNvZGUgNCIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNC5weSIsImNvZGUiOiJwcmludChwYWNraW5nX2xpc3RbMTozXSkgICAgIyBbJ2NoYXJnZXInLCAnSUQgY2FyZCddXG5wcmludChwYWNraW5nX2xpc3RbOjJdKSAgICAgIyBbJ3dhdGVyIGJvdHRsZScsICdjaGFyZ2VyJ11cbnByaW50KHBhY2tpbmdfbGlzdFsyOl0pICAgICAjIFsnSUQgY2FyZCcsICdyYWluY29hdCcsICdzbmFja3MnXSJ9"
 width="100%"
></iframe>

Dev uses exactly this when he wants to check just the electronics at the front of his list or just the last two items he added in a hurry, without typing out the whole checklist again. A slice of a list is itself a brand new list, so you can store it, print it, or loop over it like any other.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-6-lists-and-tuples/01_list_index_slice_boxes.png)


## Lists vs Strings at a Glance

| Idea | Strings | Lists |
|---|---|---|
| Ordered sequence | Yes, characters in order | Yes, values in order |
| Indexing with `[ ]` | Reaches one character | Reaches one item |
| Negative indices | Count from the end | Count from the end |
| Slicing with `[a:b]` | Returns a substring | Returns a sub-list |
| What it can hold | Only characters | Any type, even mixed |

Everything you already know about indexing and slicing strings transfers directly, which is exactly why this lesson felt familiar rather than brand new.

## Your Turn: Build a Trip List

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjAxX2xpc3RzX2NyZWF0aW9uX2luZGV4aW5nX2FuZF9zbGljaW5nIGNvZGUgNSIsImxhbmd1YWdlIjoicHl0aG9uIiwiZmlsZW5hbWUiOiJtYWluXzAwNS5weSIsImNvZGUiOiJjaXR5ID0gaW5wdXQoXCJUcmlwIGRlc3RpbmF0aW9uOiBcIilcbmRheXMgPSBpbnQoaW5wdXQoXCJOdW1iZXIgb2YgZGF5czogXCIpKVxuY29tcGFuaW9ucyA9IGlucHV0KFwiVHJhdmVsbGluZyB3aXRoIGhvdyBtYW55IGZyaWVuZHM6IFwiKVxuXG50cmlwID0gW2NpdHksIGRheXMsIGNvbXBhbmlvbnNdXG5wcmludChcIlRyaXAgZGV0YWlsczpcIiwgdHJpcClcbnByaW50KFwiRmlyc3QgZGV0YWlsOlwiLCB0cmlwWzBdKVxucHJpbnQoXCJMYXN0IGRldGFpbDpcIiwgdHJpcFstMV0pIn0"
 width="100%"
></iframe>

Enter a destination, a day count, and a number of friends, and watch all three settle into one ordered list that you can index into immediately. You have just built your first list from scratch.

## Conclusion

A list is Python's ordered container, written in square brackets, able to hold any type of value and indexed and sliced exactly like a string: `[0]` for the first item, `[-1]` for the last, and `[a:b]` for a range. Where strings stop, though, lists keep going, because a list lets you change what is inside it after creation. That difference, and exactly how far it goes, is where the next lesson begins.
