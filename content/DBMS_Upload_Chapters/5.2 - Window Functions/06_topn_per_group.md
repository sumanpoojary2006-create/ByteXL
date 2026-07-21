## Introduction

The sales director's final request ties together nearly everything in this chapter: "show me the top 2 salespeople by revenue, within each region." This is a genuinely common business question, a top-N-per-group report, and it needs partitioned ranking, since "top 2" has to reset for every region rather than apply once across the whole company, combined with a way to filter down to just those top-ranked rows.

Ranking functions alone cannot filter, since `window functions` are not allowed inside `WHERE`, the same restriction noted when ranking functions were first introduced. Solving this cleanly needs a ranking function wrapped in a CTE.

**Definition:** A top-N-per-group report combines a ranking function partitioned by the grouping column with a CTE that makes the rank filterable, and the choice between `ROW_NUMBER`, `RANK`, and `DENSE_RANK` decides exactly how ties are handled in the result.

![Intro visual for topn per group](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_intro_topn_per_group_clean_65c2828c.png)

## Ranking Within Each Region

The `sales` table now includes a `region` column so rankings can be scoped per region.

## Source Data Used in This Lesson

Before running the lesson queries, inspect the starting data. The tables below show the rows loaded by the setup file.

### `sales`

| salesperson | region | total_amount |
| --- | --- | --- |
| Nikhil Rao | North | 29700.00 |
| Aarav Singh | North | 24000.00 |
| Devika Rao | North | 18500.00 |
| Sana Fatima | South | 21000.00 |
| Tarun Bakshi | South | 21000.00 |
| Reema Ghosh | South | 15000.00 |
| Kunal Verma | East | 11000.00 |

The OneCompiler activity keeps preparation and practice separate. `init.sql` creates the displayed tables, rows, roles, or supporting objects. The active SQL file contains only the statement currently being studied, and `with=init.sql` runs the preparation file first.

## Hands-On Setup: Prepare the Database

```postgresql
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

Before running each active statement, predict which rows, database objects, or server behavior should change. Then compare the result with the expected output or observation supplied beneath the statement.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkagg62" 
 width="100%"
></iframe>

Expected output:

| salesperson | region | total_amount | region_rank |
| --- | --- | --- | --- |
| Kunal Verma | East | 11000.00 | 1 |
| Nikhil Rao | North | 29700.00 | 1 |
| Aarav Singh | North | 24000.00 | 2 |
| Devika Rao | North | 18500.00 | 3 |
| Sana Fatima | South | 21000.00 | 1 |
| Tarun Bakshi | South | 21000.00 | 1 |
| Reema Ghosh | South | 15000.00 | 3 |

`PARTITION BY region` resets the ranking separately within North, South, and East:

- Nikhil Rao ranks 1st in North with 29700.00.
- Sana Fatima and Tarun Bakshi both rank 1st in South, tied at 21000.00 each, using `RANK`'s tie-handling behavior from earlier in this chapter.

Every region starts its own count from 1, which is exactly the "within each region" part of the director's request.

![Ranking rows within each region and keeping the top two per group](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/11_top_two_per_group_rank_filter.png)

## Filtering to the Top N Using a CTE

Since `region_rank` cannot be referenced directly in `WHERE` within the same query that defines it, the ranked result needs to be named with a CTE first, then filtered from there.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaggha" 
 width="100%"
></iframe>

Expected output:

| salesperson | region | total_amount | region_rank |
| --- | --- | --- | --- |
| Kunal Verma | East | 11000.00 | 1 |
| Nikhil Rao | North | 29700.00 | 1 |
| Aarav Singh | North | 24000.00 | 2 |
| Sana Fatima | South | 21000.00 | 1 |
| Tarun Bakshi | South | 21000.00 | 1 |

The CTE `ranked_sales` computes the ranking exactly as before, and the outer query then treats `region_rank` as an ordinary column, filterable with a plain `WHERE`. This returns 5 rows in total, not 6: North and South each contribute their expected 2 rows, but East has only one salesperson to begin with, Kunal Verma, so its entire top 2 is just that single row.

South's tie is handled cleanly too, Sana Fatima and Tarun Bakshi both hold rank 1 and both survive the `region_rank <= 2` filter, while Reema Ghosh, in third place by value, lands on rank 3 thanks to `RANK`'s skip-ahead behavior and is correctly excluded.

Had South instead had a three-way tie for first place, all three tied rows would have survived the same filter, since every one of them would hold rank 1, which is worth knowing before assuming a top-N query always returns exactly N rows per group.

![A CTE computing window ranks before an outer query filters to top rows](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/12_cte_filtering_window_rank.png)

## Choosing ROW_NUMBER Instead When Ties Should Not Multiply Results

If the business rule is strictly "exactly 2 per region, no matter what," regardless of ties, `ROW_NUMBER` guarantees exactly that count, at the cost of breaking ties arbitrarily.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaggt8" 
 width="100%"
></iframe>

Expected output:

| salesperson | region | total_amount |
| --- | --- | --- |
| Kunal Verma | East | 11000.00 |
| Nikhil Rao | North | 29700.00 |
| Aarav Singh | North | 24000.00 |
| Sana Fatima | South | 21000.00 |
| Tarun Bakshi | South | 21000.00 |

This returns at most 2 rows per region, 5 total here, since `ROW_NUMBER` never produces a tie in its numbering even when the underlying values tie, so North and South each contribute their full 2, while East, with only one salesperson on record, can only ever contribute the 1 row it actually has.

Whether `RANK`, `DENSE_RANK`, or `ROW_NUMBER` is the right choice for a top-N report depends entirely on how the business wants ties handled, a decision worth confirming explicitly rather than guessing.

## Top-N Per Group as a General Pattern

This CTE-plus-ranking-plus-filter shape generalizes far beyond sales regions: top 3 highest-paid employees per department, most recent 5 orders per customer, or highest-rated product per category all follow the exact same structure, just changing what `PARTITION BY` groups on and what `ORDER BY` ranks by.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Step</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ranking function with <code>PARTITION BY</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Restart the rank count within each group</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Wrap in a CTE</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Give the ranked result a name that can be filtered</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>WHERE rank_column &lt;= N</code> on the CTE</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keep only the top N rows per group</td>
    </tr>
  </tbody>
</table>

## Your Turn

Find the single lowest-selling salesperson in each region, using `RANK`. Write that query against the `sales` table above.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkagh4e" 
 width="100%"
></iframe>

One valid answer wraps `RANK() OVER (PARTITION BY region ORDER BY total_amount ASC) AS region_rank` in a CTE and filters with `WHERE region_rank = 1`, returning Devika Rao for North, Reema Ghosh for South, and Kunal Verma for East, since ordering ascending instead of descending flips the ranking to find the smallest value first.


Expected output:

| salesperson | region | total_amount |
| --- | --- | --- |
| Kunal Verma | East | 11000.00 |
| Devika Rao | North | 18500.00 |
| Reema Ghosh | South | 15000.00 |

## Conclusion

A top-N-per-group report combines a ranking function partitioned by the grouping column with a CTE that makes the rank filterable, and the choice between `ROW_NUMBER`, `RANK`, and `DENSE_RANK` decides exactly how ties are handled in the result. This pattern closes out the chapter by combining partitioning, ordering, ranking, and CTEs into a single, genuinely useful report shape.

With subqueries, CTEs, and `window functions` all in place, the course moves next into keeping data correct and consistent as multiple changes happen at once.
