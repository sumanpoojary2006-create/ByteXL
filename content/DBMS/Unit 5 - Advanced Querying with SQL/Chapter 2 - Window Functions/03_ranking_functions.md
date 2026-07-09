## Introduction

The sales director wants a leaderboard: every salesperson ranked by their total sales, first place, second place, and so on, with ties handled sensibly if two people happen to tie exactly. `ORDER BY` alone can sort a result, but it cannot label each row with its rank, and it has no built-in way to decide what should happen to the rank numbers that follow a tie. SQL provides three dedicated **ranking functions**, `ROW_NUMBER`, `RANK`, and `DENSE_RANK`, each a `window function` used with `OVER (ORDER BY ...)`, and each with a different, precise rule for handling ties.

## Numbering Rows with ROW_NUMBER

The `sales` table again holds individual sales, this time including a tie for illustration.

```postgresql file=sales_ranking.sql
CREATE TABLE sales (
    sale_id INTEGER PRIMARY KEY,
    salesperson TEXT,
    amount NUMERIC(10, 2)
);

INSERT INTO sales (sale_id, salesperson, amount) VALUES
(1, 'Nikhil Rao', 29700.00),
(2, 'Sana Fatima', 21000.00),
(3, 'Tarun Bakshi', 21000.00),
(4, 'Priya Bose', 18500.00),
(5, 'Kunal Verma', 11000.00);
```

```postgresql with=sales_ranking.sql
SELECT salesperson, amount,
       ROW_NUMBER() OVER (ORDER BY amount DESC) AS row_num
FROM sales;
```

`ROW_NUMBER()` assigns a strictly increasing integer to every row, 1, 2, 3, 4, 5, in the order defined by `ORDER BY amount DESC`, with no regard for ties at all:

- Sana Fatima and Tarun Bakshi both have 21000.00.
- `ROW_NUMBER` still gives them different numbers, 2 and 3, arbitrarily breaking the tie based on whatever order the database happens to process them in. This makes `ROW_NUMBER` useful for a strict, no-ties-allowed sequence, but not ideal for a leaderboard where a genuine tie should probably be reflected as one.

## Ranking with Gaps Using RANK

`RANK()` gives tied rows the exact same rank number, and then skips ahead by the number of tied rows before continuing.

```postgresql with=sales_ranking.sql
SELECT salesperson, amount,
       RANK() OVER (ORDER BY amount DESC) AS rank_position
FROM sales;
```

Sana and Tarun both land on rank 2, correctly reflecting their tie, but the next row, Priya Bose, gets rank 4, not rank 3, because `RANK` counts the two tied second-place rows and skips the number that would have been "third." This mirrors how a real sporting leaderboard usually works:

- Two people tied for second place.
- Whoever comes next is in fourth, not third, since two people already occupy the ranks above them.

## Ranking Without Gaps Using DENSE_RANK

`DENSE_RANK()` also gives tied rows the same rank, but it does not skip any numbers afterward, keeping the rank sequence consecutive.

```postgresql with=sales_ranking.sql
SELECT salesperson, amount,
       DENSE_RANK() OVER (ORDER BY amount DESC) AS dense_rank_position
FROM sales;
```

Sana and Tarun again both land on rank 2, but Priya Bose now gets rank 3, not 4, since `DENSE_RANK` treats the tie as consuming only one rank position, not two. Whether `RANK` or `DENSE_RANK` is the right choice depends entirely on what the ranking is meant to represent:

- **`RANK`**: use it if the count of people above someone genuinely matters.
- **`DENSE_RANK`**: use it if only the relative tier matters.

## Comparing All Three Side by Side

Placing all three ranking functions in the same query makes the difference between them immediately visible.

```postgresql with=sales_ranking.sql
SELECT salesperson, amount,
       ROW_NUMBER() OVER (ORDER BY amount DESC) AS row_num,
       RANK() OVER (ORDER BY amount DESC) AS rank_position,
       DENSE_RANK() OVER (ORDER BY amount DESC) AS dense_rank_position
FROM sales;
```

For the tied pair, `row_num` shows 2 and 3, `rank_position` shows 2 and 2, and `dense_rank_position` also shows 2 and 2, and the divergence appears clearly on Priya Bose's row right after: 4, 4, and 3, respectively, for the three functions.

## Ranking Within Partitions

Ranking functions combine naturally with `PARTITION BY`, ranking rows separately within each group rather than across the whole table, the same partitioning behavior covered for aggregate `window functions`.

```postgresql with=sales_ranking.sql
SELECT salesperson, amount,
       RANK() OVER (ORDER BY amount DESC) AS overall_rank
FROM sales;
```

Without a region or team column in this smaller table, this example ranks across everyone, but the same `PARTITION BY team_column` pattern from earlier lessons would restart the ranking at 1 within each team, which becomes the foundation for finding a top performer per group in a later lesson.

## Ranking Functions at a Glance

| Function | Tied rows | Rank after a tie |
|---|---|---|
| `ROW_NUMBER()` | Different numbers, arbitrarily | Always consecutive |
| `RANK()` | Same number | Skips ahead by the tie count |
| `DENSE_RANK()` | Same number | Stays consecutive, no gap |

## Your Turn

The sales director wants a leaderboard using `DENSE_RANK`, showing only salespeople ranked in the top 3 tiers. Write a query against the `sales` table above that computes `DENSE_RANK` and filters to ranks 1 through 3.

```postgresql with=sales_ranking.sql
-- Write your query below
```

Filtering directly with `WHERE DENSE_RANK() OVER (...) <= 3` is not allowed, since `window functions` cannot be referenced in `WHERE`, the same restriction that applies to `aggregate functions`; instead, wrap the ranking in a CTE first, then filter the CTE's result: `WITH ranked AS (SELECT salesperson, amount, DENSE_RANK() OVER (ORDER BY amount DESC) AS dense_rank_position FROM sales) SELECT * FROM ranked WHERE dense_rank_position <= 3;`, which returns the top four rows since two people share the second tier.

## Conclusion

`ROW_NUMBER`, `RANK`, and `DENSE_RANK` each turn an ordered set of rows into rank numbers, differing only in how they handle ties, strict sequencing with no ties, ranking with gaps after a tie, or ranking with no gaps at all. The director's leaderboard can now be built with exactly the tie-handling behavior the business actually wants. Ranking looks at a row's position; the next lesson looks at comparing a row directly to the rows immediately before or after it.
