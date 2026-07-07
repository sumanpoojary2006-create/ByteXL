## Introduction

The bus seating chart is the one piece of trip logistics Dev cannot flatten into a single list. It is not just forty names in a row; it is four rows of ten seats each, and a name belongs to a row and a position within that row. He needs to say "the student in row 2, seat 5" and get a single, exact answer, not search through forty names hoping he counted correctly.

A single list cannot capture that shape on its own, because it only has one level of position. What Dev actually needs is a list whose items are themselves lists, a structure called a **nested list**, and it turns out to be the natural way to represent anything with rows and columns, just like the grids you built with nested loops in the looping unit.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-6-lists-and-tuples/07_bus_seating_grid.png)

## A List Whose Items Are Lists

A nested list is simply a list where one or more items are themselves lists.

```python
seating = [
    ["Asha", "Ravi", "Meera"],
    ["Kabir", "Dev", "Riya"],
]
print(seating)
```

Here `seating` has two items, and each of those items is itself a three-item list, one row per bus row. Printing `seating` shows the whole structure, brackets within brackets, exactly mirroring rows within a chart.

## Reaching a Single Seat: Double Indexing

To reach one specific value, you index twice: once for the outer list, the row, and once for the inner list, the seat within that row.

```python
seating = [
    ["Asha", "Ravi", "Meera"],
    ["Kabir", "Dev", "Riya"],
]
print(seating[0])        # ['Asha', 'Ravi', 'Meera']
print(seating[0][0])     # Asha
print(seating[1][2])     # Riya
```

Read `seating[1][2]` from left to right: "go to row 1, then within that row, go to seat 2." This is exactly the row-then-seat lookup Dev needs to answer "who is sitting in row 2, seat 3" precisely, without scanning anything.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/unit-6-lists-and-tuples/07_double_index_row_column.png)


## Changing One Seat

Because lists are mutable, you can update a single nested value directly, by indexing all the way down to it.

```python
seating = [
    ["Asha", "Ravi", "Meera"],
    ["Kabir", "Dev", "Riya"],
]
seating[1][1] = "Aman"
print(seating[1])    # ['Kabir', 'Aman', 'Riya']
```

Only that one seat changes. Every other row, and every other seat in that row, is left exactly as it was, which is the whole point of being able to reach precisely one value instead of rebuilding the structure around it.

## Looping Through a Nested List

A nested loop, just like the grid-building loops from the looping unit, is the natural way to visit every item in a nested list.

```python
seating = [
    ["Asha", "Ravi", "Meera"],
    ["Kabir", "Dev", "Riya"],
]
for row_number, row in enumerate(seating):
    for seat_number, name in enumerate(row):
        print(f"Row {row_number}, Seat {seat_number}: {name}")
```

The outer loop walks through each row, and the inner loop walks through each seat within that row, exactly matching the two-level shape of the data itself. The structure of the loop mirrors the structure of the list, which is no accident: nested data is visited with nested loops.

## Building a Grid From Scratch

You do not have to type every row by hand. A nested list comprehension can build a grid in one line, combining ideas from two earlier lessons.

```python
grid = [[0 for _ in range(3)] for _ in range(2)]
print(grid)    # [[0, 0, 0], [0, 0, 0]]
```

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

```python
seating = []
for row_number in range(2):
    row = []
    for seat_number in range(3):
        row.append(input(f"Name for row {row_number}, seat {seat_number}: "))
    seating.append(row)

print("Full chart:", seating)
print("Row 1, seat 2 is:", seating[1][2])
```

Build a small two-row chart from your own input, then reach straight into one exact seat to confirm double indexing lands where you expect.

## Conclusion

A nested list is a list containing other lists, the natural shape for anything with rows and columns, and reaching one value takes two indices: `data[row][column]`. Visiting every item pairs naturally with a nested loop, one level of loop for each level of nesting. You can now hold, change, sort, filter, lock, and grid any data the trip can throw at you; the final lesson of this unit ties it together by walking cleanly through lists and tuples with the loop tools you already know.
