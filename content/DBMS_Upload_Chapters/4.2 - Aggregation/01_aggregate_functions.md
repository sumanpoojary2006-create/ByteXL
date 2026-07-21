## Introduction

Priya handles finance reporting for a small online bookstore, and every question she gets from the founders is about the whole business, not any single row:

- "How many orders did we get this month?"
- "What is our total revenue?"
- "What is the average order value?"
- "What was our biggest single sale?"

None of those questions can be answered by looking at one row of the `orders` table; each one requires looking at every row and boiling it down to a single number. SQL calls this **aggregation**, and it provides a small set of built-in `aggregate functions`, `COUNT`, `SUM`, `AVG`, `MIN`, and `MAX`, that do exactly this kind of summarizing.

**Definition:** `COUNT`, `SUM`, `AVG`, `MIN`, and `MAX` collapse an entire result set into single summary numbers, answering exactly the kind of whole-business questions raw rows cannot answer on their own.

![Intro visual for aggregate functions](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_intro_aggregate_functions_clean_279265b4.png)

## Counting Rows

The `orders` table holds one row per order placed on the bookstore's site.

## Source Data Used in This Lesson

Before running the lesson queries, inspect the data they will use. The tables below show the rows loaded by the setup file.

### `orders`

| order_id | customer_name | category | amount | order_date |
| --- | --- | --- | --- | --- |
| 1 | Ishita Rao | Fiction | 450 | 2025-04-02 |
| 2 | Vivek Menon | Non-Fiction | 899 | 2025-04-03 |
| 3 | Ishita Rao | Fiction | 320 | 2025-04-05 |
| 4 | Aman Gupta | Children | 210 | 2025-04-06 |
| 5 | Sonal Deshpande | Non-Fiction | 1450 | 2025-04-08 |
| 6 | Vivek Menon | Fiction | 610 | 2025-04-10 |
| 7 | Aman Gupta | Children | 175 | 2025-04-12 |
| 8 | Ishita Rao | Non-Fiction | 990 | 2025-04-14 |

The OneCompiler activity keeps setup and practice separate. `init.sql` creates and populates the displayed data, while the active SQL file contains only the query being studied.

## Hands-On Setup: Prepare the Data

```postgresql
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    category TEXT,
    amount NUMERIC(10, 2),
    order_date DATE
);

INSERT INTO orders (order_id, customer_name, category, amount, order_date) VALUES
(1, 'Ishita Rao', 'Fiction', 450.00, '2025-04-02'),
(2, 'Vivek Menon', 'Non-Fiction', 899.00, '2025-04-03'),
(3, 'Ishita Rao', 'Fiction', 320.00, '2025-04-05'),
(4, 'Aman Gupta', 'Children', 210.00, '2025-04-06'),
(5, 'Sonal Deshpande', 'Non-Fiction', 1450.00, '2025-04-08'),
(6, 'Vivek Menon', 'Fiction', 610.00, '2025-04-10'),
(7, 'Aman Gupta', 'Children', 175.00, '2025-04-12'),
(8, 'Ishita Rao', 'Non-Fiction', 990.00, '2025-04-14');
```

Before running the active query, read its `SELECT` list and clauses against the displayed source rows. Then compare the returned values with the expected output to see exactly what the function or operation changed.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkajt4y" 
 width="100%"
></iframe>

Expected output:

| total_orders |
| --- |
| 8 |

- `COUNT(*)` counts every row in the result set, regardless of what any column contains, and here it answers Priya's first question directly: the bookstore received 8 orders.
- `COUNT(column_name)` behaves slightly differently, counting only the rows where that specific column is not `NULL`, which matters once a table has optional fields.

![COUNT star counting every order row into one total order count](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_count_rows_total_orders.png)

## Totaling and Averaging a Column

Revenue and average order value both come from the same `amount` column, just combined differently.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkajte3" 
 width="100%"
></iframe>

Expected output:

| total_revenue | average_order_value |
| --- | --- |
| 5104 | 638 |

- `SUM` adds up every value in the specified column across all matching rows, giving Priya total revenue in one number.
- `AVG` divides that same sum by the count of rows automatically, giving the average order value without Priya having to calculate it by hand from the other two numbers.
- Both functions ignore `NULL` values in the column they are summarizing, rather than treating a `NULL` as zero.

![SUM and AVG collapsing order amounts into total revenue and average order value](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_sum_avg_order_amounts.png)

## Finding the Smallest and Largest Values

Priya's last question, the biggest single sale, needs a function that looks at every value and keeps only the extreme.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkajtq6" 
 width="100%"
></iframe>

Expected output:

| smallest_order | largest_order |
| --- | --- |
| 175 | 1450 |

- `MIN` returns the smallest value found in the column across all matching rows, and `MAX` returns the largest.
- Here, the smallest order is Aman Gupta's 175.00 children's book purchase, and the largest is Sonal Deshpande's 1450.00 non-fiction order.
- `MIN` and `MAX` work on dates and text too, not just numbers, so `MIN(order_date)` would return the earliest date in the table.

## Combining Several Aggregates in One Query

All five `aggregate functions` can appear together in a single `SELECT`, each one summarizing the same set of rows in its own way.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaju6z" 
 width="100%"
></iframe>

Expected output:

| total_orders | total_revenue | average_order_value | smallest_order | largest_order |
| --- | --- | --- | --- | --- |
| 8 | 5104 | 638 | 175 | 1450 |

This single query answers every question the founders originally asked, in one pass over the table, with `ROUND` from the previous chapter cleaning up the average to two decimal places. This is the shape a founder-facing summary dashboard query usually takes: a handful of `aggregate functions`, no `GROUP BY` yet, producing exactly one summary row for the whole table.

## Aggregate Functions at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Function</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Ignores NULLs?</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>COUNT(*)</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Number of rows</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No, counts every row</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>COUNT(column)</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Number of non-NULL values in a column</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Yes</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>SUM(column)</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Total of a numeric column</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Yes</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>AVG(column)</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Average of a numeric column</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Yes</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>MIN(column)</code> / <code>MAX(column)</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Smallest / largest value</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Yes</td>
    </tr>
  </tbody>
</table>

## Your Turn

The founders now want to know the total number of orders placed and the total revenue earned specifically from the "Fiction" category. Write a query against the `orders` table above that returns both numbers, aliased as `fiction_orders` and `fiction_revenue`.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkajug4" 
 width="100%"
></iframe>

If your query filters with `WHERE category = 'Fiction'` before aggregating, it returns 3 orders and 1380.00 in revenue, since `WHERE` narrows the rows down first and the `aggregate functions` only ever see what survives that filter.


Expected output for the practice query:

| fiction_orders | fiction_revenue |
| --- | --- |
| 3 | 1380 |

## Conclusion

`COUNT`, `SUM`, `AVG`, `MIN`, and `MAX` collapse an entire result set into single summary numbers, answering exactly the kind of whole-business questions raw rows cannot answer on their own.

Priya now has order counts, revenue, average order value, and the smallest and largest sales, all from one small table.

So far every aggregate has summarized the whole table at once; the next step is producing one summary per category instead of a single overall number.
