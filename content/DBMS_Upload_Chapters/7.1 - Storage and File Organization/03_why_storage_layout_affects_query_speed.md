## Introduction

The previous two lessons established two physical facts: data is read in whole pages, not individual `rows`, and a heap, PostgreSQL's default organization, offers no guarantee about which `rows` end up on which pages.

This lesson connects those two facts directly to something Priya can actually see happen: without any help, finding `rows` in a heap `table` means reading every single page, checking every single `row`, an approach called a `full table scan`, and it gets slower in direct proportion to how large the `table` grows.

**Definition:** Without a supporting structure on the `column` being filtered, a heap-organized `table` forces a `query` into a `full table scan`, reading every single page and checking every single `row`, with cost that scales directly with `table` size regardless of how few `rows` the `query` actually needs; the `primary key` search escaped this fate only because PostgreSQL quietly built an `index` for it.

![Intro visual for why storage layout affects query speed](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_intro_why_storage_layout_affects_query_speed.png)

## Watching a Full Table Scan Happen

A larger `table` makes the cost of a full scan easy to observe directly.

## Source Data Used in This Lesson

Some lessons need a larger dataset to make execution plans or maintenance behavior visible. For those tables, `init.sql` generates the rows instead of listing every row manually.

### Generated `orders` dataset

| Column | Definition in the setup |
| --- | --- |
| `order_id` | `INTEGER PRIMARY KEY` |
| `customer_name` | `TEXT` |
| `amount` | `NUMERIC(10, 2)` |

The setup generates 5,000 rows, numbered from 1 through 5000. This scale is intentional because performance behavior is difficult to observe on a tiny table.

The OneCompiler activity keeps preparation and practice separate. `init.sql` creates the displayed tables, rows, roles, or supporting objects. The active SQL file contains only the statement currently being studied, and `with=init.sql` runs the preparation file first.

## Hands-On Setup: Prepare the Database

```postgresql
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    amount NUMERIC(10, 2)
);

INSERT INTO orders (order_id, customer_name, amount)
SELECT i, 'Customer ' || i, (i * 12.5)::NUMERIC(10,2)
FROM generate_series(1, 5000) AS i;
```

Before running each active statement, predict which rows, database objects, or server behavior should change. Then compare the result with the expected output or observation supplied beneath the statement.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkajk5j" 
 width="100%"
></iframe>

Expected output:

```
                        QUERY PLAN
------------------------------------------------------------
 Seq Scan on orders  (cost=0.00..97.50 rows=1 width=23)
   Filter: (customer_name = 'Customer 3000'::text)
```

- `EXPLAIN`, covered in full detail later in this unit, previews how the `database` plans to execute a `query` without actually running it.
- The plan here reports a "Seq Scan," short for `sequential scan`, meaning the `database` intends to read the `table` page by page, from the beginning, checking every `row`'s `customer_name` against 'Customer 3000' until it reaches the end.
- Even though this `query` is only interested in exactly one `row` out of 5000, the heap organization from the previous lesson gives the `database` no shortcut, no way to know in advance which page holds that customer without checking.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkajkeu" 
 width="100%"
></iframe>

Expected output:

| pages_a_full_scan_must_read |
| --- |
| 46 |

Using the same page-number extraction from the first lesson, this counts how many distinct pages the `table` occupies a `sequential scan` has to read every single one of them, even for this single-`row` lookup, because a `sequential scan`'s cost scales with the size of the whole `table`, not with how many `rows` the `query` actually needs, whether that need is 1 `row` or 1000.

![A full table scan checks every page even when only one target row is needed](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_full_scan_checks_every_page.png)

## Why the Primary Key Search Behaves Differently

Running the same shape of `query`, but filtering on `order_id`, the `table`'s `primary key`, produces a completely different plan.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkajkqw" 
 width="100%"
></iframe>

Expected output:

```
                                   QUERY PLAN
---------------------------------------------------------------------------------
 Index Scan using orders_pkey on orders  (cost=0.29..8.31 rows=1 width=23)
   Index Cond: (order_id = 3000)
```

The plan now reports an "Index Scan using orders_pkey" instead of a `sequential scan`.

The physical reality is that a `primary key` `constraint` does not change how `rows` are organized on disk, the `table` is still the same unordered heap, but PostgreSQL automatically builds a separate structure, an `index`, for every `primary key` in order to enforce uniqueness, and the planner uses that structure to jump straight to the right page instead of checking all of them.

Nothing about the `table`'s layout changed between these two `queries`; the only difference is that one `column` has a supporting structure and the other does not. That structure, the `index`, is exactly what the next chapter covers in depth.

![An index gives the database a shortcut to the page instead of scanning many pages](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_index_scan_jumps_to_page.png)

## How Table Size Directly Predicts Scan Cost

Doubling the number of `rows` in a heap `table` roughly doubles the number of pages it occupies, and a full scan reads every page, so a full scan's cost grows linearly with `table` size, a relationship worth being able to reason about directly.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkajm2y" 
 width="100%"
></iframe>

Expected output:

| current_size |
| --- |
| 368 kB |

| size_after_doubling_rows |
| --- |
| 736 kB |

Doubling the `row` count roughly doubles the reported `table` size, and a full scan against this larger `table` now has roughly twice as many pages to check for the exact same single-`row` lookup, even though the answer being searched for has not changed in any way.

This is precisely why "it worked fine on my small test `table`" is not evidence that a `query` will stay fast once real data volume arrives; a `full table scan`'s cost is a direct, predictable `function` of `table` size.

![As more rows create more pages, a full scan has more pages to read](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/07_more_rows_more_pages_full_scan_cost.png)

## What a Full Table Scan Is and Is Not

A full scan is not always the wrong choice:

- When a `query` genuinely needs most or all of a `table`'s `rows`, such as computing an aggregate across the entire `table`, reading every page is unavoidable regardless of any structure available, and a full scan is often the most efficient plan the `database` could choose.
- Full scans become a problem specifically when a `query` only needs a small fraction of a large `table`'s `rows`, since that is exactly the situation where reading every page is enormously wasteful compared to reading just the handful of pages that actually matter.

## Storage Layout and Query Speed at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Situation</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What happens</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Cost scales with</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Query needs most/all rows</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Full table scan, often the right plan anyway</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Table size, but unavoidable regardless</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Query needs a few rows, column has no supporting structure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Full table scan, checking every page for a rare match</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Table size, wastefully, since only a few rows were needed</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Query filters on the <code>primary key</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>Index scan</code>, because PostgreSQL automatically builds an <code>index</code> for every <code>primary key</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Only the handful of pages actually holding the answer</td>
    </tr>
  </tbody>
</table>

## Your Turn

Run `EXPLAIN` on a `query` filtering the `orders` `table` above for `amount > 120000`, a condition only a small fraction of `rows` will satisfy (`amount` tops out at 125000.00 for `order_id = 10000`), and note in a comment whether the plan shows a `sequential scan` and why that is expected given everything covered in this lesson.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkajmed" 
 width="100%"
></iframe>

Expected result and verification:

`EXPLAIN SELECT * FROM orders WHERE amount > 120000;` reports a `sequential scan`, exactly as expected, since `amount` has no supporting structure to help the `database` skip pages, meaning it must check every `row`'s `amount` value against the condition regardless of how few `rows` actually qualify.

## Conclusion

Without a supporting structure on the `column` being filtered, a heap-organized `table` forces a `query` into a `full table scan`, reading every single page and checking every single `row`, with cost that scales directly with `table` size regardless of how few `rows` the `query` actually needs; the `primary key` search escaped this fate only because PostgreSQL quietly built an `index` for it.

Priya finally has a concrete, physical explanation for why her reports slow down as the company's order history grows. The next chapter introduces that rescuing structure properly, and shows how to build one for any `column` a `query` filters on: the `index`.
