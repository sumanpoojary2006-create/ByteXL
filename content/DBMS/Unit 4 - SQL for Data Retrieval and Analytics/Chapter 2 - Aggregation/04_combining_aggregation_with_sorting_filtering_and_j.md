## Introduction

Priya's reports so far have all come from one table, but the founders' latest request pulls in more: "show me total revenue by region, for regions with at least two customers, sorted highest revenue first, but only counting orders placed after the first week of April." That single sentence needs several pieces working together:

- A `join`, to bring in region data that is not stored on the `orders` table at all
- A row-level date filter
- A grouped total
- A group-level filter on customer count
- A final sort

None of these pieces are new on their own; what is new is seeing exactly how they fit together and in what order the database actually applies them.

## Setting Up a Second Table to Join

Region information lives on a separate `customers` table, not on `orders` itself, which is a completely normal way for a real `schema` to be organized.

```postgresql file=orders_customers.sql
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

```postgresql with=orders_customers.sql
SELECT c.region, SUM(o.amount) AS region_revenue
FROM orders o
JOIN customers c ON o.customer_name = c.customer_name
GROUP BY c.region;
```

The `JOIN` attaches each order to its customer's region before grouping ever happens, so `GROUP BY c.region` can collapse rows by a column that was never on the `orders` table to begin with. Aggregation and `joins` combine naturally this way: the `join` widens each row with extra columns, and grouping then works with whichever of those columns it needs.

## Layering in a Row-Level Filter

The founders' request also wants only orders placed after April 7. That is a row-level condition, so it belongs in `WHERE`, applied before grouping, exactly as covered when `WHERE` and `HAVING` were first compared.

```postgresql with=orders_customers.sql
SELECT c.region, SUM(o.amount) AS region_revenue
FROM orders o
JOIN customers c ON o.customer_name = c.customer_name
WHERE o.order_date > '2025-04-07'
GROUP BY c.region;
```

Only orders 5 through 8 survive the `WHERE` clause, and grouping happens on that smaller set, so the West region's total here reflects just Sonal's 1450.00 order and Vivek's 610.00 order, not his earlier 899.00 order from April 3.

## Adding a Group-Level Filter and a Sort

The last two pieces, "at least two customers" and "sorted highest revenue first," need `HAVING` on a `COUNT(DISTINCT ...)` and an `ORDER BY` on the computed total.

```postgresql with=orders_customers.sql
SELECT c.region, SUM(o.amount) AS region_revenue, COUNT(DISTINCT o.customer_name) AS customer_count
FROM orders o
JOIN customers c ON o.customer_name = c.customer_name
WHERE o.order_date > '2025-04-07'
GROUP BY c.region
HAVING COUNT(DISTINCT o.customer_name) >= 2
ORDER BY region_revenue DESC;
```

`COUNT(DISTINCT o.customer_name)` counts unique customers per region rather than unique orders, which matters because one customer with many orders should not be mistaken for many customers. `HAVING` then drops any region with fewer than two distinct customers in this filtered window, and `ORDER BY region_revenue DESC` puts the highest-earning surviving region first.

## The Logical Order a Query Actually Runs In

Every clause used above is written in a fixed syntax order (`SELECT`, `FROM`, `WHERE`, `GROUP BY`, `HAVING`, `ORDER BY`), but the database does not execute them in that written order. It is worth knowing the real sequence, because it explains every rule covered in this chapter.

| Step | Clause | What happens |
|---|---|---|
| 1 | `FROM` / `JOIN` | Tables are combined into one wide working set |
| 2 | `WHERE` | Individual rows are filtered, before any grouping |
| 3 | `GROUP BY` | Surviving rows are collapsed into groups |
| 4 | `HAVING` | Groups are filtered, using aggregate results |
| 5 | `SELECT` | Final columns and aggregate values are computed |
| 6 | `ORDER BY` | The finished result set is sorted |

This ordering is exactly why `WHERE` cannot reference `SUM(amount)`, that aggregate does not exist yet at step 2, and why `ORDER BY` can reference a column alias defined in `SELECT`, since sorting happens last, after the alias already exists.

## Your Turn

The founders want one more cut: total revenue and order count per category, but only for orders from the West and South regions, only categories with more than one order, sorted by revenue descending. Write that query against the `orders` and `customers` tables above.

```postgresql with=orders_customers.sql
-- Write your query below
```

If your query `joins` `orders` to `customers`, filters with `WHERE c.region IN ('West', 'South')`, groups by `o.category`, filters with `HAVING COUNT(*) > 1`, and orders by the summed revenue descending, Non-Fiction should come out on top at 3339.00, ahead of Fiction's 1380.00, once Aman Gupta's North-region Children orders are filtered out and Vivek's, Sonal's, and Ishita's Non-Fiction orders are summed together.

## Conclusion

`Joins`, row filters, grouping, group filters, and sorting are not separate skills; they are stages of one pipeline that runs in a fixed order regardless of how the query is written, and understanding that order explains every rule about what each clause is and is not allowed to reference. Priya can now answer any report the founders throw at her by reasoning through the same six steps every time. `Joins` have been used here just to bring in a column to group by; the next chapter looks at `joins` in their own right, in much more depth.
