## Introduction

The sales director's final request ties together nearly everything in this chapter: "show me the top 2 salespeople by revenue, within each region." This is a genuinely common business question, a top-N-per-group report, and it needs partitioned ranking, since "top 2" has to reset for every region rather than apply once across the whole company, combined with a way to filter down to just those top-ranked rows. Ranking functions alone cannot filter, since `window functions` are not allowed inside `WHERE`, the same restriction noted when ranking functions were first introduced. Solving this cleanly needs a ranking function wrapped in a CTE.

## Ranking Within Each Region

The `sales` table now includes a `region` column so rankings can be scoped per region.

```postgresql file=regional_sales.sql
CREATE TABLE sales (
    salesperson TEXT,
    region TEXT,
    total_amount NUMERIC(10, 2)
);

INSERT INTO sales (salesperson, region, total_amount) VALUES
('Nikhil Rao', 'North', 29700.00),
('Aarav Singh', 'North', 24000.00),
('Devika Rao', 'North', 18500.00),
('Sana Fatima', 'South', 21000.00),
('Tarun Bakshi', 'South', 21000.00),
('Reema Ghosh', 'South', 15000.00),
('Kunal Verma', 'East', 11000.00);
```

```postgresql with=regional_sales.sql
SELECT salesperson, region, total_amount,
       RANK() OVER (PARTITION BY region ORDER BY total_amount DESC) AS region_rank
FROM sales;
```

`PARTITION BY region` resets the ranking separately within North, South, and East:

- Nikhil Rao ranks 1st in North with 29700.00.
- Sana Fatima and Tarun Bakshi both rank 1st in South, tied at 21000.00 each, using `RANK`'s tie-handling behavior from earlier in this chapter.

Every region starts its own count from 1, which is exactly the "within each region" part of the director's request.

## Filtering to the Top N Using a CTE

Since `region_rank` cannot be referenced directly in `WHERE` within the same query that defines it, the ranked result needs to be named with a CTE first, then filtered from there.

```postgresql with=regional_sales.sql
WITH ranked_sales AS (
    SELECT salesperson, region, total_amount,
           RANK() OVER (PARTITION BY region ORDER BY total_amount DESC) AS region_rank
    FROM sales
)
SELECT salesperson, region, total_amount, region_rank
FROM ranked_sales
WHERE region_rank <= 2
ORDER BY region, region_rank;
```

The CTE `ranked_sales` computes the ranking exactly as before, and the outer query then treats `region_rank` as an ordinary column, filterable with a plain `WHERE`. South region shows three rows here, not two, because Sana Fatima and Tarun Bakshi are tied for rank 1, and `RANK`'s skip-ahead behavior means Reema Ghosh, in third place by value, actually holds rank 3, correctly excluded. Choosing `DENSE_RANK` instead of `RANK` in the CTE would change this outcome, since a tie at rank 1 under `DENSE_RANK` would push the next distinct value to rank 2, not rank 3.

## Choosing ROW_NUMBER Instead When Ties Should Not Multiply Results

If the business rule is strictly "exactly 2 per region, no matter what," regardless of ties, `ROW_NUMBER` guarantees exactly that count, at the cost of breaking ties arbitrarily.

```postgresql with=regional_sales.sql
WITH ranked_sales AS (
    SELECT salesperson, region, total_amount,
           ROW_NUMBER() OVER (PARTITION BY region ORDER BY total_amount DESC) AS row_num
    FROM sales
)
SELECT salesperson, region, total_amount
FROM ranked_sales
WHERE row_num <= 2
ORDER BY region, row_num;
```

This returns exactly 2 rows per region every time, six total, since `ROW_NUMBER` never produces a tie in its numbering, even when the underlying values tie. Whether `RANK`, `DENSE_RANK`, or `ROW_NUMBER` is the right choice for a top-N report depends entirely on how the business wants ties handled, a decision worth confirming explicitly rather than guessing.

## Top-N Per Group as a General Pattern

This CTE-plus-ranking-plus-filter shape generalizes far beyond sales regions: top 3 highest-paid employees per department, most recent 5 orders per customer, or highest-rated product per category all follow the exact same structure, just changing what `PARTITION BY` groups on and what `ORDER BY` ranks by.

| Step | Purpose |
|---|---|
| Ranking function with `PARTITION BY` | Restart the rank count within each group |
| Wrap in a CTE | Give the ranked result a name that can be filtered |
| `WHERE rank_column <= N` on the CTE | Keep only the top N rows per group |

## Your Turn

Find the single lowest-selling salesperson in each region, using `RANK`. Write that query against the `sales` table above.

```postgresql with=regional_sales.sql
-- Write your query below
```

One valid answer wraps `RANK() OVER (PARTITION BY region ORDER BY total_amount ASC) AS region_rank` in a CTE and filters with `WHERE region_rank = 1`, returning Devika Rao for North, Reema Ghosh for South, and Kunal Verma for East, since ordering ascending instead of descending flips the ranking to find the smallest value first.

## Conclusion

A top-N-per-group report combines a ranking function partitioned by the grouping column with a CTE that makes the rank filterable, and the choice between `ROW_NUMBER`, `RANK`, and `DENSE_RANK` decides exactly how ties are handled in the result. This pattern closes out the chapter by combining partitioning, ordering, ranking, and CTEs into a single, genuinely useful report shape. With subqueries, CTEs, and `window functions` all in place, the course moves next into keeping data correct and consistent as multiple changes happen at once.
