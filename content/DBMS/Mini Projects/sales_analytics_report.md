## Background

Raw transaction tables rarely answer a business question by themselves. "Which category sells the most?" or "Which customers have never come back?" needs functions to clean up messy values, aggregation to roll rows into totals, and joins to bring separated tables back together. This project builds a small analytics report over a mini e-commerce dataset, using exactly the tools this unit covers.

## What You Will Build

A set of analytical SQL queries over a small `customers`, `products`, and `orders` schema, producing cleaned data, category-level revenue reports, and customer relationship insights.

## Dataset

Before writing project queries, inspect the starting data so every task has a visible source to reason from.

### Starting `customers` rows

| full_name | email | city | referred_by |
| --- | --- | --- | --- |
| ananya rao | ananya@mail.com | Bengaluru | NULL |
| RAHUL NAIR | rahul@mail.com | NULL | 1 |
| Priya Menon | NULL | Kochi | 1 |
| Karan Shah | karan@mail.com | Mumbai | NULL |
| Divya Iyer | divya@mail.com | Bengaluru | 4 |

### Starting `products` rows

| name | category | price |
| --- | --- | --- |
| Notebook | Stationery | 45.00 |
| Pen | Stationery | 10.00 |
| Wireless Mouse | Electronics | 599.00 |
| Desk Lamp | Electronics | 350.00 |
| Backpack | Accessories | 899.00 |

### Starting `orders` rows

| customer_id | order_date |
| --- | --- |
| 1 | 2026-01-05 |
| 1 | 2026-02-14 |
| 2 | 2026-01-20 |
| 4 | 2026-02-02 |

### Starting `order_items` rows

| order_id | product_id | quantity |
| --- | --- | --- |
| 1 | 1 | 5 |
| 1 | 3 | 1 |
| 2 | 4 | 2 |
| 3 | 2 | 10 |
| 4 | 5 | 1 |
| 4 | 3 | 2 |
Keep all `CREATE TABLE` and `INSERT` statements in `init.sql`. Keep only the current task query in a separate SQL file so the setup code and task work remain easy to review.

```text
CREATE TABLE customers (
    customer_id  INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    full_name    TEXT NOT NULL,
    email        TEXT,
    city         TEXT,
    referred_by  INTEGER REFERENCES customers(customer_id)
);

CREATE TABLE products (
    product_id  INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name        TEXT NOT NULL,
    category    TEXT NOT NULL,
    price       NUMERIC(10, 2) NOT NULL
);

CREATE TABLE orders (
    order_id     INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    customer_id  INTEGER NOT NULL REFERENCES customers(customer_id),
    order_date   DATE NOT NULL
);

CREATE TABLE order_items (
    order_id    INTEGER NOT NULL REFERENCES orders(order_id),
    product_id  INTEGER NOT NULL REFERENCES products(product_id),
    quantity    INTEGER NOT NULL,
    PRIMARY KEY (order_id, product_id)
);

INSERT INTO customers (full_name, email, city, referred_by) VALUES
('ananya rao', 'ananya@mail.com', 'Bengaluru', NULL),
('RAHUL NAIR', 'rahul@mail.com', NULL, 1),
('Priya Menon', NULL, 'Kochi', 1),
('Karan Shah', 'karan@mail.com', 'Mumbai', NULL),
('Divya Iyer', 'divya@mail.com', 'Bengaluru', 4);

INSERT INTO products (name, category, price) VALUES
('Notebook', 'Stationery', 45.00),
('Pen', 'Stationery', 10.00),
('Wireless Mouse', 'Electronics', 599.00),
('Desk Lamp', 'Electronics', 350.00),
('Backpack', 'Accessories', 899.00);

INSERT INTO orders (customer_id, order_date) VALUES
(1, '2026-01-05'), (1, '2026-02-14'), (2, '2026-01-20'), (4, '2026-02-02');

INSERT INTO order_items (order_id, product_id, quantity) VALUES
(1, 1, 5), (1, 3, 1), (2, 4, 2), (3, 2, 10), (4, 5, 1), (4, 3, 2);
```

### Confirm the Setup

Run this in the active SQL file before starting the tasks. It confirms that `init.sql` loaded the expected number of rows.

```text
SELECT COUNT(*) AS loaded_rows FROM customers;
```

Expected output:

| loaded_rows |
| --- |
| 5 |

## Tasks

### Task 1: Clean the Data with Functions

1. Select every customer's name normalized to proper case (`Ananya Rao`, not `ananya rao` or `RAHUL NAIR`), regardless of how it was entered.
2. Extract just the domain part of each customer's email (the part after `@`).
3. Select every order alongside the month name it was placed in (for example "January"), using a date function.
4. Using `COALESCE` and `CASE`, produce a customer list where a missing `city` shows as `'Unknown'` and a missing `email` shows as `'No email on file'`.

### Task 2: Aggregate Category Revenue

1. Compute total revenue (`price * quantity`, summed) per product category.
2. Filter the result to categories whose total revenue exceeds 500, using `HAVING`.
3. Sort the final report by revenue, highest first.

   ```
   category      total_revenue
   Electronics       2497.00
   Accessories        899.00
   ```

### Task 3: Join the Picture Together

1. Produce a full itemized order report: order id, customer name, product name, quantity, and line total, joining `orders`, `order_items`, `products`, and `customers` with `INNER JOIN`.
2. Using a `LEFT JOIN`, find every customer who has never placed an order.
3. Using a self-join on `customers`, list each customer alongside the name of the person who referred them (if any).
4. Write two separate queries: "customers who spent more than 1000 in total" and "customers based in Bengaluru." Combine them with `UNION` into a single deduplicated mailing list, then combine them again with `INTERSECT` to find customers who satisfy both conditions at once.

**Answer these questions after completing all tasks:**
- Task 1.4 replaces missing values with placeholder text using `COALESCE`. If you instead left these as raw `NULL` values and tried to display them in a report, what would a user see, and why is an explicit placeholder usually better?
- Task 2 used `HAVING` rather than `WHERE` to filter by total revenue. What error do you get if you try writing the same condition using `WHERE` directly on the aggregate, and why does SQL enforce this separation?
- Your self-join in Task 3.3 uses `referred_by` to link a customer back to another row in the same table. Karan Shah has `referred_by = NULL`. What does the self-join return for his row, and does he disappear from the result or show up with a blank referrer?

## Where to Build This Project

1. Go to [bytexl.app/nimbus](https://bytexl.app/nimbus).
2. Click **Create new workspace**.

![The Nimbus dashboard with the Create new workspace button highlighted](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_create_new_workspace.png)

3. Select the **PostgreSQL** template, then click **Next**.

![Select the PostgreSQL template and click Next](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_select_postgresql_template.png)

4. Enter a workspace name and click **Launch Workspace**.

![Enter a workspace name and launch the PostgreSQL workspace](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_name_and_launch_workspace.png)
