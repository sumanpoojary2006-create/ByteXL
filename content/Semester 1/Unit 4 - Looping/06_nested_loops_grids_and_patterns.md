## Introduction

Kabir is arranging the photo grid on his Instagram profile, and he fills it the same way every time: he completes one whole row of photos across, then moves down to the next row and fills that one across, and so on until the grid is full. There is a loop for moving down through the rows, and inside each row, another loop for placing every photo across it.

A single loop walks through one sequence, but many problems are built from rows and columns just like that wall: a multiplication grid, a seating chart, a pattern of stars, comparing every item with every other item. A single loop could place every photo in one long strip, but it has no natural way to start a new row once the current one is full; that decision needs a second loop watching over it. For these you place one loop inside another, creating a nested loop. The outer loop handles the rows, and the inner loop handles the columns within each row.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44tb5n423/06_nested_loops_grid.png)
## A Loop Inside a Loop

When loops nest, the inner loop runs all the way through for every single pass of the outer loop.

```python
for row in range(1, 4):
    for star in range(row):
        print("*", end="")
    print()
```

This prints a small triangle:

```
*
**
***
```

Trace it gently. On the first outer pass `row` is 1, so the inner loop prints one star. On the second pass `row` is 2, so it prints two stars, and so on. The `end=""` keeps the stars on the same line, and the empty `print()` after the inner loop moves to a new line for the next row.

## How the Repetitions Multiply

Here is the idea that makes nested loops powerful and, occasionally, dangerous. The total number of inner steps is the outer count multiplied by the inner count.

So if an outer loop runs 3 times and its inner loop runs 4 times each, how many times does the inner block run in total? It runs 3 times 4, which is 12. This multiplication is exactly what you want for filling a grid, the same row-times-column arithmetic that decides how many photo squares Kabir's profile grid actually holds.

![](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/44tb5n423/06_nested_loop_multiplication.png)


## How Fast the Total Grows

| Outer Count | Inner Count | Total Inner Steps |
|---|---|---|
| 3 | 4 | 12 |
| 10 | 10 | 100 |
| 1,000 | 1,000 | 1,000,000 |

For small data this is fine; for large data it is something to watch, a theme you will meet again when you study performance.

## Your Turn: A Times-Table Grid

```python
for a in range(1, 6):
    for b in range(1, 6):
        print(f"{a * b:3}", end=" ")
    print()
```

This prints a neat 5 by 5 multiplication grid. The outer loop picks the row number, the inner loop runs across the columns, and the `:3` in the f-string pads each result to three spaces so the columns line up. Change the 6 to 11 and you have the full grid up to 10.

## Conclusion

A nested loop is a loop inside another loop, ideal for anything shaped like rows and columns: grids, tables, and patterns. The inner loop completes fully for each pass of the outer loop, so the total work is the outer count multiplied by the inner count. That multiplication builds grids beautifully, but it also grows quickly, so keep an eye on it with large amounts of data. Master the row-and-column rhythm and a whole class of pattern problems becomes straightforward. With single loops, nested loops, and early exits all in hand, it is worth stepping back to name the handful of shapes almost every loop you will ever write actually falls into.
