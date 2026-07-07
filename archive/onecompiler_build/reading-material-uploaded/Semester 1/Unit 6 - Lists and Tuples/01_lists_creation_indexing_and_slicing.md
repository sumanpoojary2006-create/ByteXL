## Introduction

Dev is the one everyone in class trusts to make sure nothing gets left behind on the annual college trip, so the night before departure he opens a fresh note on his phone and types out the master packing checklist exactly in the order he thinks of it: water bottle, charger, ID card, raincoat, snacks. He does not want five separate notes for five separate items. He wants one single note that holds all of them together, in the order he listed them, so he can glance at item three or skim the last two without rereading the whole thing from the top.

That is exactly the job Python's **list** does. A list is an ordered collection of values, written inside square brackets, and it is about to become the single most useful container in your entire toolkit.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-6-lists-and-tuples/01_packing_list_lineup.png)

## Creating a List

A list is written as a comma-separated sequence of values inside square brackets.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-6-lists-and-tuples-01-lists-creation-indexing-and-slicing-001-78538b510b.html"
 width="100%"
></iframe>

That single variable now holds all five items, in the exact order Dev typed them. Unlike a string, which can only hold characters, a list can hold any type of value, and even a mix of types in the same list.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-6-lists-and-tuples-01-lists-creation-indexing-and-slicing-002-4f28f86118.html"
 width="100%"
></iframe>

Here a list holds a city name, a number of days, a budget, and a boolean, side by side. You will rarely mix types this freely in real code, but Python places no restriction on it, because a list is simply an ordered container, not a fixed shape.

## Counting and Reaching Items: len() and Indexing

Just as with strings, `len()` tells you how many items a list holds, and square brackets reach a single item by its position, counting from 0.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-6-lists-and-tuples-01-lists-creation-indexing-and-slicing-003-ba64d1eb5d.html"
 width="100%"
></iframe>

Negative indices count from the end exactly as they did for strings, so `packing_list[-1]` is the last item Dev added without him needing to know there are five items in total. Ask for a position that does not exist, such as `packing_list[10]`, and Python raises the same `IndexError` you met with strings: the valid indices always run from 0 to the length minus one.

## Slicing a List

Slicing works on lists exactly as it did on strings: a start and a stop separated by a colon, with the stop excluded.

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-6-lists-and-tuples-01-lists-creation-indexing-and-slicing-004-0c9d91b843.html"
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
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-1-unit-6-lists-and-tuples-01-lists-creation-indexing-and-slicing-005-b2ca43a62f.html"
 width="100%"
></iframe>

Enter a destination, a day count, and a number of friends, and watch all three settle into one ordered list that you can index into immediately. You have just built your first list from scratch.

## Conclusion

A list is Python's ordered container, written in square brackets, able to hold any type of value and indexed and sliced exactly like a string: `[0]` for the first item, `[-1]` for the last, and `[a:b]` for a range. Where strings stop, though, lists keep going, because a list lets you change what is inside it after creation. That difference, and exactly how far it goes, is where the next lesson begins.
