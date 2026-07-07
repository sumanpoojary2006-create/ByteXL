## Introduction

The bus seating chart is the one piece of trip logistics Dev cannot flatten into a single list. It is not just forty names in a row; it is four rows of ten seats each, and a name belongs to a row and a position within that row. He needs to say "the student in row 2, seat 5" and get a single, exact answer, not search through forty names hoping he counted correctly.

A single list cannot capture that shape on its own, because it only has one level of position. What Dev actually needs is a list whose items are themselves lists, a structure called a **nested list**, and it turns out to be the natural way to represent anything with rows and columns, just like the grids you built with nested loops in the looping unit.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-6-lists-and-tuples/07_bus_seating_grid.png)

## A List Whose Items Are Lists

A nested list is simply a list where one or more items are themselves lists.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X25lc3RlZF9saXN0cyBjb2RlIDEiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDEucHkiLCJjb2RlIjoic2VhdGluZyA9IFtcbiAgICBbXCJBc2hhXCIsIFwiUmF2aVwiLCBcIk1lZXJhXCJdLFxuICAgIFtcIkthYmlyXCIsIFwiRGV2XCIsIFwiUml5YVwiXSxcbl0ifQ"
 width="100%"
></iframe>

Here `seating` has two items, and each of those items is itself a three-item list, one row per bus row. Printing `seating` shows the whole structure, brackets within brackets, exactly mirroring rows within a chart.

## Reaching a Single Seat: Double Indexing

To reach one specific value, you index twice: once for the outer list, the row, and once for the inner list, the seat within that row.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X25lc3RlZF9saXN0cyBjb2RlIDIiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDIucHkiLCJjb2RlIjoicHJpbnQoc2VhdGluZ1swXSkgICAgICAgICMgWydBc2hhJywgJ1JhdmknLCAnTWVlcmEnXVxucHJpbnQoc2VhdGluZ1swXVswXSkgICAgICMgQXNoYVxucHJpbnQoc2VhdGluZ1sxXVsyXSkgICAgICMgUml5YSJ9"
 width="100%"
></iframe>

Read `seating[1][2]` from left to right: "go to row 1, then within that row, go to seat 2." This is exactly the row-then-seat lookup Dev needs to answer "who is sitting in row 2, seat 3" precisely, without scanning anything.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-6-lists-and-tuples/07_double_index_row_column.png)


## Changing One Seat

Because lists are mutable, you can update a single nested value directly, by indexing all the way down to it.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X25lc3RlZF9saXN0cyBjb2RlIDMiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDMucHkiLCJjb2RlIjoic2VhdGluZ1sxXVsxXSA9IFwiQW1hblwiXG5wcmludChzZWF0aW5nWzFdKSAgICAjIFsnS2FiaXInLCAnQW1hbicsICdSaXlhJ10ifQ"
 width="100%"
></iframe>

Only that one seat changes. Every other row, and every other seat in that row, is left exactly as it was, which is the whole point of being able to reach precisely one value instead of rebuilding the structure around it.

## Looping Through a Nested List

A nested loop, just like the grid-building loops from the looping unit, is the natural way to visit every item in a nested list.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X25lc3RlZF9saXN0cyBjb2RlIDQiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDQucHkiLCJjb2RlIjoiZm9yIHJvd19udW1iZXIsIHJvdyBpbiBlbnVtZXJhdGUoc2VhdGluZyk6XG4gICAgZm9yIHNlYXRfbnVtYmVyLCBuYW1lIGluIGVudW1lcmF0ZShyb3cpOlxuICAgICAgICBwcmludChmXCJSb3cge3Jvd19udW1iZXJ9LCBTZWF0IHtzZWF0X251bWJlcn06IHtuYW1lfVwiKSJ9"
 width="100%"
></iframe>

The outer loop walks through each row, and the inner loop walks through each seat within that row, exactly matching the two-level shape of the data itself. The structure of the loop mirrors the structure of the list, which is no accident: nested data is visited with nested loops.

## Building a Grid From Scratch

You do not have to type every row by hand. A nested list comprehension can build a grid in one line, combining ideas from two earlier lessons.

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X25lc3RlZF9saXN0cyBjb2RlIDUiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDUucHkiLCJjb2RlIjoiZ3JpZCA9IFtbMCBmb3IgXyBpbiByYW5nZSgzKV0gZm9yIF8gaW4gcmFuZ2UoMildXG5wcmludChncmlkKSAgICAjIFtbMCwgMCwgMF0sIFswLCAwLCAwXV0ifQ"
 width="100%"
></iframe>

The inner comprehension builds one row of three zeros, and the outer comprehension repeats that twice, producing a two-by-three grid ready to be filled in.

## Nested Indexing at a Glance

| Expression | Meaning |
|---|---|
| `seating[0]` | The whole first row |
| `seating[0][0]` | The first seat of the first row |
| `seating[1][2] = "Aman"` | Replace one specific seat |
| `for row in seating:` | Visit each row, one list at a time |
| `for row in seating: for seat in row:` | Visit every individual seat |

## Your Turn: Build and Query a Seating Chart

<iframe
 frameBorder="0"
 height="350px"
 src="http://127.0.0.1:8765/embed.html#eyJ0aXRsZSI6IjA3X25lc3RlZF9saXN0cyBjb2RlIDYiLCJsYW5ndWFnZSI6InB5dGhvbiIsImZpbGVuYW1lIjoibWFpbl8wMDYucHkiLCJjb2RlIjoic2VhdGluZyA9IFtdXG5mb3Igcm93X251bWJlciBpbiByYW5nZSgyKTpcbiAgICByb3cgPSBbXVxuICAgIGZvciBzZWF0X251bWJlciBpbiByYW5nZSgzKTpcbiAgICAgICAgcm93LmFwcGVuZChpbnB1dChmXCJOYW1lIGZvciByb3cge3Jvd19udW1iZXJ9LCBzZWF0IHtzZWF0X251bWJlcn06IFwiKSlcbiAgICBzZWF0aW5nLmFwcGVuZChyb3cpXG5cbnByaW50KFwiRnVsbCBjaGFydDpcIiwgc2VhdGluZylcbnByaW50KFwiUm93IDEsIHNlYXQgMiBpczpcIiwgc2VhdGluZ1sxXVsyXSkifQ"
 width="100%"
></iframe>

Build a small two-row chart from your own input, then reach straight into one exact seat to confirm double indexing lands where you expect.

## Conclusion

A nested list is a list containing other lists, the natural shape for anything with rows and columns, and reaching one value takes two indices: `data[row][column]`. Visiting every item pairs naturally with a nested loop, one level of loop for each level of nesting. You can now hold, change, sort, filter, lock, and grid any data the trip can throw at you; the final lesson of this unit ties it together by walking cleanly through lists and tuples with the loop tools you already know.
