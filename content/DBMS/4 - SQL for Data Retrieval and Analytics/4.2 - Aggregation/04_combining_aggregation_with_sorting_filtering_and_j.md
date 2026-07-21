## Introduction

Priya's reports so far have all come from one `table`, but the founders' latest request pulls in more: "show me total revenue by region, for regions with at least two customers, sorted highest revenue first, but only counting orders placed after the first week of April." That single sentence needs several pieces working together:

- A `join`, to bring in region data that is not stored on the `orders` `table` at all
- A `row`-level date filter
- A grouped total
- A group-level filter on customer count
- A final sort

None of these pieces are new on their own; what is new is seeing exactly how they fit together and in what order the `database` actually applies them.

**Definition:** `Joins`, `row` filters, grouping, group filters, and sorting are not separate skills; they are stages of one pipeline that runs in a fixed order regardless of how the `query` is written, and understanding that order explains every rule about what each clause is and is not allowed to reference.

<!--
IMAGE PROMPT  ->  generate as images/04_intro_combining_aggregation_with_sorting_filtering_and.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: DBMS course introduction image based directly on the opening scene of this lesson. Use the named person, setting, and database problem from the Introduction.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue database forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A simple visual of the Introduction: Priya's reports so far have all come from one table, but the founders' latest request pulls in more: "show me total revenue by region, for regions with at least two customers, sorted highest revenue first, but only counting orders placed after the first week.

ON-IMAGE TEXT: show a short bold title "Combining Aggregation With Sorting Filtering And J" plus only these few labels, large and legible: Table, Row, Join. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing DBMS reading-material image standards.
-->

![Intro visual for combining aggregation with sorting filtering and j](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_intro_combining_aggregation_with_sorting_filtering_and_matched_260a2726.png)

## Setting Up a Second Table to Join

Region information lives on a separate `customers` `table`, not on `orders` itself, which is a completely normal way for a real `schema` to be organized.

## Source Data Used in This Lesson

Before running the lesson queries, inspect the data they will use. The tables below show the rows loaded by the setup file.

### `customers`

| customer_name | region |
| --- | --- |
| Ishita Rao | South |
| Vivek Menon | West |
| Aman Gupta | North |
| Sonal Deshpande | West |

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

```postgresql file=init.sql
CREATE TABLE customers (
    customer_name TEXT PRIMARY KEY,
    region TEXT
);

INSERT INTO customers (customer_name, region) VALUES
('Ishita Rao', 'South'),
('Vivek Menon', 'West'),
('Aman Gupta', 'North'),
('Sonal Deshpande', 'West');

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_name TEXT REFERENCES customers(customer_name),
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

```postgresql with=init.sql
SELECT c.region, SUM(o.amount) AS region_revenue
FROM orders o
JOIN customers c ON o.customer_name = c.customer_name
GROUP BY c.region;
```

Expected output:

| region | region_revenue |
| --- | --- |
| North | 385 |
| South | 1760 |
| West | 2959 |

The `JOIN` attaches each order to its customer's region before grouping ever happens, so `GROUP BY c.region` can collapse `rows` by a `column` that was never on the `orders` `table` to begin with. Aggregation and `joins` combine naturally this way: the `join` widens each `row` with extra `columns`, and grouping then works with whichever of those `columns` it needs.

![JOIN adding customer region to order rows before GROUP BY summarizes revenue by region](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/07_join_before_group_by_region.png)

## Layering in a Row-Level Filter

The founders' request also wants only orders placed after April 7. That is a `row`-level condition, so it belongs in `WHERE`, applied before grouping, exactly as covered when `WHERE` and `HAVING` were first compared.

```postgresql with=init.sql
SELECT c.region, SUM(o.amount) AS region_revenue
FROM orders o
JOIN customers c ON o.customer_name = c.customer_name
WHERE o.order_date > '2025-04-07'
GROUP BY c.region;
```

Expected output:

| region | region_revenue |
| --- | --- |
| North | 175 |
| South | 990 |
| West | 2060 |

Only orders 5 through 8 survive the `WHERE` clause, and grouping happens on that smaller set, so the West region's total here reflects just Sonal's 1450.00 order and Vivek's 610.00 order, not his earlier 899.00 order from April 3.

## Adding a Group-Level Filter and a Sort

The last two pieces, "at least two customers" and "sorted highest revenue first," need `HAVING` on a `COUNT(DISTINCT ...)` and an `ORDER BY` on the computed total.

```postgresql with=init.sql
SELECT c.region, SUM(o.amount) AS region_revenue, COUNT(DISTINCT o.customer_name) AS customer_count
FROM orders o
JOIN customers c ON o.customer_name = c.customer_name
WHERE o.order_date > '2025-04-07'
GROUP BY c.region
HAVING COUNT(DISTINCT o.customer_name) >= 2
ORDER BY region_revenue DESC;
```

Expected output:

| region | region_revenue | customer_count |
| --- | --- | --- |
| West | 2060 | 2 |

- `COUNT(DISTINCT o.customer_name)` counts unique customers per region rather than unique orders, which matters because one customer with many orders should not be mistaken for many customers.
- `HAVING` then drops any region with fewer than two distinct customers in this filtered window, and `ORDER BY region_revenue DESC` puts the highest-earning surviving region first.

## The Logical Order a Query Actually Runs In

Every clause used above is written in a fixed syntax order (`SELECT`, `FROM`, `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY`), but the `database` does not execute them in that written order. It is worth knowing the real sequence, because it explains every rule covered in this chapter.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Step</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Clause</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What happens</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>FROM</code> / <code>JOIN</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tables are combined into one wide working set</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>WHERE</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Individual rows are filtered, before any grouping</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">3</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>GROUP BY</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Surviving rows are collapsed into groups</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">4</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>HAVING</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Groups are filtered, using aggregate results</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">5</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>SELECT</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Final columns and aggregate values are computed</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">6</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>ORDER BY</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The finished result set is sorted</td>
    </tr>
  </tbody>
</table>

This ordering is exactly why `WHERE` cannot reference `SUM(amount)`, that aggregate does not exist yet at step 2, and why `ORDER BY` can reference a `column` alias defined in `SELECT`, since sorting happens last, after the alias already exists.

![Logical execution order of an aggregate SQL query from FROM JOIN through ORDER BY](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/08_logical_query_execution_order.png)

## Your Turn

The founders want one more cut: total revenue and order count per category, but only for orders from the West and South regions, only categories with more than one order, sorted by revenue descending. Write that `query` against the `orders` and `customers` `tables` above.

```postgresql with=init.sql
-- Write your query below
```

- If your `query` `joins` `orders` to `customers`, filters with `WHERE c.region IN ('West', 'South')`, groups by `o.category`, filters with `HAVING COUNT(*) > 1`.
- It then orders by summed revenue descending.
- `Non-Fiction` should come out on top at 3339.00, ahead of `Fiction` at 1380.00.
- That happens after Aman Gupta's North-region Children orders are filtered out and Vivek's, Sonal's, and Ishita's Non-Fiction orders are summed together.


Expected output for the practice query:

| category | total_revenue | order_count |
| --- | --- | --- |
| Non-Fiction | 3339 | 3 |
| Fiction | 1380 | 3 |

## Conclusion

`Joins`, `row` filters, grouping, group filters, and sorting are not separate skills; they are stages of one pipeline that runs in a fixed order regardless of how the `query` is written, and understanding that order explains every rule about what each clause is and is not allowed to reference.

Priya can now answer any report the founders throw at her by reasoning through the same six steps every time.

`Joins` have been used here just to bring in a `column` to group by; the next chapter looks at `joins` in their own right, in much more depth.
