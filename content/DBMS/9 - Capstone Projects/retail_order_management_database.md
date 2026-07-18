# Capstone Project: Retail Order Management Database

## Background

RetailRx is a small online store selling electronics, stationery, and accessories. Behind every order screen is a database that has to model products and categories correctly, let staff query and update stock safely, answer "what sold well this month" without melting under load, survive two customers buying the last unit at the same instant, and finally hand off a reporting layer that support staff and analysts can use without ever seeing internal cost data.

This project draws on everything from Units 2 through 8: design and normalization, core SQL, retrieval and analytics, advanced querying, transactions, performance tuning, and production security. You will build it in seven stages, each one adding a layer on top of the last, using PostgreSQL throughout.

## Project Workspace

Maintain two PostgreSQL files throughout the capstone. Use `init.sql` as the reproducible source of truth for schema definitions, constraints, seed data, views, functions, triggers, roles, and indexes. Use the active SQL file for the query or test belonging to the stage you are currently completing. When a stage changes the permanent design, move the verified definition into `init.sql` before beginning the next stage.

Before running any query, display or sketch the source tables involved and predict the rows that should be returned or changed. After running it, save the result or execution plan with a short explanation of why it proves the requirement. Performance plans, WAL values, and live server statistics are environment-dependent, so record the operator or trend you observed instead of expecting identical numbers on every run.

## Stages

### Stage 1: Design the Schema

1. Model these entities and their relationships as an ER diagram before writing any SQL: `categories` (which can nest, for example Electronics > Laptops > Gaming Laptops), `products` (each belongs to exactly one category), `customers`, `orders`, and `order_items` (the many-to-many join between orders and products, carrying quantity and the price at the time of sale).

2. You are handed this flat spreadsheet a previous intern used to track orders. Identify at least three anomalies in it, identify the functional dependencies, and normalize it to 3NF before designing your real tables:

   | order_id | customer_name | customer_email | product_name | category | unit_price | quantity |
   |---|---|---|---|---|---|---|
   | 1 | Ananya Rao | ananya@mail.com | Wireless Mouse | Electronics | 599 | 1 |
   | 1 | Ananya Rao | ananya@mail.com | Notebook | Stationery | 45 | 5 |
   | 2 | Rahul Nair | rahul@mail.com | Wireless Mouse | Electronics | 599 | 2 |

3. Build the real schema with `CREATE TABLE` statements. Use a self-referencing `parent_category_id` on `categories` so categories can nest, surrogate `GENERATED ALWAYS AS IDENTITY` primary keys, foreign keys with explicit `ON DELETE` behaviour, `NOT NULL` and `CHECK` constraints where they matter (stock and price can never go negative), and `created_at`/`updated_at` audit columns on every table.

**Answer these questions after completing Stage 1:**
- The spreadsheet repeats `unit_price` for the same product on different orders. Why does your normalized `order_items` table still need its own `unit_price` column instead of always looking the price up from `products`? What happens to old orders if a product's price changes next month?
- Your `categories` table references itself through `parent_category_id`. What `ON DELETE` behaviour did you choose for that self-reference, and what would happen to "Gaming Laptops" if someone deleted "Laptops" with the wrong choice?

## Reference Schema and Starting Data

Compare your own Stage 1 design against this reference schema before moving on. It is deliberately one valid answer, not the only one, use it to check your instincts, then adapt it if your own reasoning led somewhere slightly different.

### `categories`

| category_id | name | parent_category_id |
| --- | --- | --- |
| 1 | Electronics | *NULL* |
| 2 | Laptops | 1 |
| 3 | Stationery | *NULL* |

### `products`

| product_id | name | category_id | price | stock_quantity |
| --- | --- | --- | ---: | ---: |
| 1 | Wireless Mouse | 1 | 599.00 | 40 |
| 2 | USB-C Hub | 1 | 1499.00 | 25 |
| 3 | Gaming Laptop Pro | 2 | 65000.00 | 6 |
| 4 | Ultrabook Air | 2 | 55000.00 | 10 |
| 5 | Notebook | 3 | 45.00 | 200 |
| 6 | Gel Pen Pack | 3 | 120.00 | 150 |

### `customers`

| customer_id | full_name | email |
| --- | --- | --- |
| 1 | Ananya Rao | ananya@mail.com |
| 2 | Rahul Nair | rahul@mail.com |
| 3 | Priya Menon | priya@mail.com |
| 4 | Karan Shah | karan@mail.com |

Use two files in OneCompiler throughout the capstone. Keep every `CREATE TABLE` and `INSERT` statement in `init.sql`; keep only the task query currently being worked on in the active SQL file.

```postgresql file=init.sql
CREATE TABLE categories (
    category_id         INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name                TEXT NOT NULL,
    parent_category_id  INTEGER REFERENCES categories(category_id) ON DELETE SET NULL,
    created_at          TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at          TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE products (
    product_id      INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    name            TEXT NOT NULL,
    category_id     INTEGER NOT NULL REFERENCES categories(category_id) ON DELETE RESTRICT,
    price           NUMERIC(10, 2) NOT NULL CHECK (price >= 0),
    stock_quantity  INTEGER NOT NULL DEFAULT 0 CHECK (stock_quantity >= 0),
    created_at      TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE customers (
    customer_id  INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    full_name    TEXT NOT NULL,
    email        TEXT NOT NULL UNIQUE,
    created_at   TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at   TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE orders (
    order_id     INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    customer_id  INTEGER NOT NULL REFERENCES customers(customer_id) ON DELETE RESTRICT,
    order_date   DATE NOT NULL DEFAULT CURRENT_DATE,
    created_at   TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at   TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE TABLE order_items (
    order_id    INTEGER NOT NULL REFERENCES orders(order_id) ON DELETE CASCADE,
    product_id  INTEGER NOT NULL REFERENCES products(product_id) ON DELETE RESTRICT,
    quantity    INTEGER NOT NULL CHECK (quantity > 0),
    unit_price  NUMERIC(10, 2) NOT NULL CHECK (unit_price >= 0),
    PRIMARY KEY (order_id, product_id)
);

INSERT INTO categories (name, parent_category_id) VALUES
('Electronics', NULL),
('Laptops', 1),
('Stationery', NULL);

INSERT INTO products (name, category_id, price, stock_quantity) VALUES
('Wireless Mouse', 1, 599.00, 40),
('USB-C Hub', 1, 1499.00, 25),
('Gaming Laptop Pro', 2, 65000.00, 6),
('Ultrabook Air', 2, 55000.00, 10),
('Notebook', 3, 45.00, 200),
('Gel Pen Pack', 3, 120.00, 150);

INSERT INTO customers (full_name, email) VALUES
('Ananya Rao', 'ananya@mail.com'),
('Rahul Nair', 'rahul@mail.com'),
('Priya Menon', 'priya@mail.com'),
('Karan Shah', 'karan@mail.com');
```

### Confirm the Setup

Run this in the active SQL file before starting Stage 2. It confirms `init.sql` loaded the expected number of rows and that "Gaming Laptops" nests correctly under "Electronics."

```postgresql with=init.sql
SELECT p.name, c.name AS category, parent.name AS parent_category
FROM products p
JOIN categories c ON p.category_id = c.category_id
LEFT JOIN categories parent ON c.parent_category_id = parent.category_id
WHERE p.name = 'Gaming Laptop Pro';
```

Expected output:

| name | category | parent_category |
| --- | --- | --- |
| Gaming Laptop Pro | Laptops | Electronics |

### Worked Example: Products Over 500

To calibrate what a finished Stage 2 query and its expected output should look like, here is one worked answer to the "which products cost more than 500" task.

```postgresql with=init.sql
SELECT name, price
FROM products
WHERE price > 500
ORDER BY price DESC;
```

Expected output:

| name | price |
| --- | ---: |
| Gaming Laptop Pro | 65000.00 |
| Ultrabook Air | 55000.00 |
| USB-C Hub | 1499.00 |
| Wireless Mouse | 599.00 |

Four of the six seeded products clear the 500 threshold; the Notebook (45.00) and Gel Pen Pack (120.00) are correctly excluded. Use this same reasoning, source data first, then the query, then a checked expected-output table, for the remaining Stage 2 tasks and every stage that follows.

### Stage 2: Populate and Query the Catalogue

1. Insert at least 3 categories (with one nested inside another), 6 products spread across them, and 4 customers. If you are working from the reference schema above, this step is already done, extend it with your own additional rows if you want more variety to query against.

2. Write `SELECT` queries using aliases, `DISTINCT`, calculated columns, `ORDER BY`, and `LIMIT` to answer: which products cost more than 500, what are the distinct categories represented, and which 3 products are the most expensive.

3. Add a `stock_quantity` column to `products` if you have not already. Write a safe `UPDATE` that adjusts stock after a manual warehouse recount, filtered by `product_id`, and confirm with `RETURNING` how many rows changed and what the new value is.

4. Use `INSERT ... ON CONFLICT` so that re-registering a customer with an email that already exists updates their name instead of failing or creating a duplicate row.

**Answer these questions after completing Stage 2:**
- Your `UPDATE` in step 3 used `RETURNING` to confirm the change in the same statement. What extra round trip would you need without it, and why does that matter for an application under load?
- The `ON CONFLICT` clause in step 4 needs a unique constraint on `email` to work. What error do you get if you try it without one?

### Stage 3: Build the Sales Report

1. Insert at least 6 orders spread across your 4 customers, each with 1 to 3 `order_items`.

2. Using string, date, and numeric functions, produce a clean customer list: proper-case names regardless of how they were entered, the month name each order was placed in, and a `COALESCE`-filled placeholder for any missing `city` values.

3. Compute total revenue per category using `GROUP BY` and `SUM`, filter to categories earning more than a threshold you choose with `HAVING`, and sort by revenue descending.

4. Produce one full itemized order report joining `orders`, `order_items`, `products`, and `customers` with `INNER JOIN`. Then use a `LEFT JOIN` to list every customer who has never placed an order, and `UNION` two segment queries ("spent over X in total" and "based in a specific city") into one deduplicated marketing list.

**Answer these questions after completing Stage 3:**
- Step 3's `HAVING` filters on a `SUM(...)`. What error do you get if you try the same condition with `WHERE` instead, and why does SQL require the aggregate filter to live in `HAVING`?
- Step 4's `LEFT JOIN` for customers with no orders relies on checking for `NULL` on the joined side. Which specific column did you check `IS NULL` on, and why would checking a column from the `customers` table instead have given the wrong answer?

### Stage 4: Advanced Queries and the Leaderboard

1. Write a correlated subquery finding every product priced above the average price within its own category.

2. Write a recursive CTE that walks your `categories` hierarchy from the top-level categories down, showing each category alongside its depth level, so "Gaming Laptops" correctly shows up two levels below its top-level ancestor.

3. Using window functions, rank products by total revenue within each category with `RANK() OVER (PARTITION BY category_id ORDER BY ...)`, compute a running total of daily revenue across all orders ordered by date, and return only the top 2 revenue-generating products per category.

**Answer these questions after completing Stage 4:**
- Step 1's subquery compares each product's price to its own category's average. Would replacing the correlated subquery with a single `JOIN` against a pre-aggregated category-average table give the same result? Which is easier to read, and which would you expect to run faster on a large catalogue?
- Step 2's recursive CTE needs a starting condition (`WHERE parent_category_id IS NULL`) and a joining condition. What happens to the query if you accidentally swap the join direction, matching a category to its own children instead of its parent?

### Stage 5: Place Orders Safely

1. Add a `payments` table (`payment_id`, `order_id`, `amount`, `paid_at`, `method`). Write the full "place an order" sequence as a single transaction: insert the order, insert its `order_items`, decrement `stock_quantity` on each product, and insert the matching payment, then `COMMIT`.

2. Add a `CHECK (stock_quantity >= 0)` constraint on `products`. Attempt to place an order for more units than are in stock, and confirm the entire transaction rolls back, leaving stock and order tables completely unchanged, not partially updated.

3. Simulate two customers both trying to buy the last unit of a product at the same moment. Rewrite the stock-decrement step using `SELECT stock_quantity FROM products WHERE product_id = ... FOR UPDATE` before the `UPDATE`, so the second transaction waits instead of reading a stale stock count and overselling.

4. Give every order placement a client-generated `order_reference` (a UUID), unique on the `orders` table, so that if the application retries a timed-out request, the same reference does not create a second order.

**Answer these questions after completing Stage 5:**
- Step 2 relies on a `CHECK` constraint to stop overselling. If it did not exist, would the transaction still fail on its own, or would it silently leave `stock_quantity` negative? What does this tell you about enforcing business rules in the database versus only in application code?
- Step 4's `order_reference` must be generated by the application before the request is sent, not by the database afterward. Why would generating it with `GENERATED ALWAYS AS IDENTITY` instead break the whole idempotency design?

### Stage 6: Make It Fast at Scale

1. Populate `order_items` with a much larger synthetic volume (100000+ rows) using `generate_series`, spreading them across your existing orders and products (or a widened synthetic order set).

2. Identify a realistic slow query, for example looking up a customer's order history filtered by status and sorted by date, and capture its baseline plan and timing with `EXPLAIN ANALYZE`.

3. Add the index that matches your access pattern (a composite index, or a partial index if most orders share one common status), re-run `EXPLAIN ANALYZE`, and confirm the plan changes from a sequential scan to an index scan.

4. Identify one N+1 pattern your application code could fall into (fetching each order's items in a loop instead of one join or one `IN (...)` query), and rewrite it as a single query.

**Answer these questions after completing Stage 6:**
- After adding your index in step 3, every future `INSERT` into that table pays a small extra cost to maintain it. At what point would you decide an index is not worth keeping, and how would you check its actual size and usage?
- `EXPLAIN` alone shows the planner's estimate without running the query; `EXPLAIN ANALYZE` actually executes it. Why would you prefer plain `EXPLAIN` when checking a `DELETE` or `UPDATE` you have not tested yet?

### Stage 7: Go to Production

1. Add a `cost_price` column to `products`, representing internal margin data. Create a view `product_catalogue_public` that exposes only customer-facing columns, and a materialized view `monthly_sales_report` for the heavy revenue-by-month aggregation, refreshed on a schedule rather than computed live.

2. Create a `reporting_role` that can only query the two views above, with no access to the base tables that contain `cost_price`. Create an `app_role` with `SELECT`, `INSERT`, and `UPDATE` on the operational tables, but not `DELETE`, following the principle of least privilege.

3. Enable row-level security on `orders` so a customer-facing role only sees rows where `customer_id` matches the current session's customer, and write one vulnerable string-concatenated query alongside a safe parameterized version, explaining what an attacker could do with the vulnerable one.

4. Add a trigger that automatically sets `updated_at = now()` on every `UPDATE` to `products` and `orders`, so no application code path can forget to maintain it.

**Answer these questions after completing Stage 7:**
- `reporting_role` can query `product_catalogue_public` but not `products` directly. If someone later granted it `SELECT` on `products` "just to help with a report," what protection would that quietly undo?
- Your row-level security policy in step 3 depends on the application correctly setting a session variable on every connection. What would a customer see if the application forgot to set it for one request: nothing, an error, or every customer's orders?

## The Complete Picture

When all seven stages are complete, the RetailRx database:

- Models products, nested categories, customers, orders, and payments in a properly normalized schema with audit columns and sane constraints
- Answers catalogue and customer questions through filtered, sorted, safely modified queries
- Produces category revenue reports and customer segments through aggregation, joins, and set operations
- Ranks products and walks the category hierarchy using subqueries, recursive CTEs, and window functions
- Places orders as all-or-nothing transactions that cannot oversell stock, even under concurrent access
- Serves order history quickly at real-world data volumes, backed by indexes chosen from measured evidence, not guesswork
- Hands off a reporting layer that never exposes internal cost data, enforces least privilege, and keeps its own audit trail automatically

Submit the ER diagram, the final `init.sql`, the task-query file, before-and-after execution plans for the performance stage, and evidence for the rollback, concurrency, role, and row-level security tests. A capstone is complete only when the database can be rebuilt from an empty PostgreSQL instance and every saved verification query still demonstrates the stated result.
