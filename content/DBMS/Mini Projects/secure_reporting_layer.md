## Background

A database that only an application can query safely is not production-ready. Support staff need a reporting view that never sees a customer's payment details. Analysts need read-only access that cannot accidentally run an `UPDATE`. Every table needs to know when its own rows last changed, without every application query having to remember to set it. This project wraps a small order database with the layer that makes it safe to hand off: views, roles, row-level security, and a trigger for audit columns.

## What You Will Build

A `customers` and `orders` schema fronted by a reporting view, a materialized view for a heavy report, two least-privilege roles, a row-level security policy, and a trigger that keeps `updated_at` accurate automatically.

## Dataset

Before writing project queries, inspect the starting data so every task has a visible source to reason from.

### Starting `customers` rows

| full_name | email |
| --- | --- |
| Ananya Rao | ananya@mail.com |
| Rahul Nair | rahul@mail.com |

### Starting `orders` rows

| customer_id | total_amount | cost_price | order_date |
| --- | --- | --- | --- |
| 1 | 1200.00 | 700.00 | 2026-01-10 |
| 2 | 500.00 | 300.00 | 2026-02-02 |

Keep all `CREATE TABLE` and `INSERT` statements in `init.sql`. Keep only the current task query in a separate SQL file so the setup code and task work remain easy to review.

```text
CREATE TABLE customers (
    customer_id  INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    full_name    TEXT NOT NULL,
    email        TEXT NOT NULL
);

CREATE TABLE orders (
    order_id      INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    customer_id   INTEGER NOT NULL REFERENCES customers(customer_id),
    total_amount  NUMERIC(10, 2) NOT NULL,
    cost_price    NUMERIC(10, 2) NOT NULL,
    order_date    DATE NOT NULL DEFAULT CURRENT_DATE,
    updated_at    TIMESTAMP NOT NULL DEFAULT now()
);

INSERT INTO customers (full_name, email) VALUES
('Ananya Rao', 'ananya@mail.com'),
('Rahul Nair', 'rahul@mail.com');

INSERT INTO orders (customer_id, total_amount, cost_price, order_date) VALUES
(1, 1200.00, 700.00, '2026-01-10'),
(2, 500.00, 300.00, '2026-02-02');
```

### Confirm the Setup

Run this in the active SQL file before starting the tasks. It confirms that `init.sql` loaded the expected number of rows.

```text
SELECT COUNT(*) AS loaded_rows FROM customers;
```

Expected output:

| loaded_rows |
| --- |
| 2 |

`cost_price` is internal margin data that support staff and customers should never see directly.

## Tasks

### Task 1: Views for Different Audiences

1. Create a view `customer_order_summary` exposing only `order_id`, customer name, `total_amount`, and `order_date`, deliberately excluding `cost_price`.
2. Create a materialized view `monthly_revenue_report` that pre-computes total revenue per month across all orders, and refresh it with `REFRESH MATERIALIZED VIEW`.
3. Explain, in a comment, why a materialized view is appropriate for the monthly report but would be the wrong choice for `customer_order_summary`, which needs to reflect every order the moment it is placed.

### Task 2: Roles and Row-Level Security

1. Create a role `reporting_role` that can only `SELECT` from `customer_order_summary` and `monthly_revenue_report`, with no access at all to the base `orders` or `customers` tables.
2. Create a role `app_role` that can `SELECT`, `INSERT`, and `UPDATE` on `orders` and `customers`, but cannot `DELETE` from either, reflecting the principle of least privilege.
3. Enable row-level security on `orders` so that a policy restricts visibility to rows where `customer_id` matches a session variable, simulating a customer-facing portal where each customer can only see their own orders.

   ```text
   ALTER TABLE orders ENABLE ROW LEVEL SECURITY;

   CREATE POLICY customer_sees_own_orders
       ON orders
       FOR SELECT
       USING (customer_id = current_setting('app.current_customer_id')::int);
   ```

Expected result: the policy is created successfully. Test it with the intended role and confirm that rows belonging to other customers are absent even when the query has no customer filter.

4. Write one vulnerable query that builds a `WHERE` clause by concatenating a customer's raw email input directly into a SQL string, and one safe version using a parameterized query instead. Explain what an attacker could enter in the vulnerable version to read every customer's data.

### Task 3: Automate the Audit Trail

1. Write a trigger function that sets `updated_at = now()` automatically whenever a row in `orders` is updated, and attach it as a `BEFORE UPDATE` trigger.

   ```text
   CREATE OR REPLACE FUNCTION set_updated_at()
   RETURNS TRIGGER AS $$
   BEGIN
       NEW.updated_at = now();
       RETURN NEW;
   END;
   $$ LANGUAGE plpgsql;

   CREATE TRIGGER trg_orders_updated_at
   BEFORE UPDATE ON orders
   FOR EACH ROW
   EXECUTE FUNCTION set_updated_at();
   ```

Expected result: PostgreSQL creates the trigger function and trigger. Updating a row should then change `updated_at` automatically without the `UPDATE` statement assigning that column.

2. Test it: update an order's `total_amount` without touching `updated_at` yourself, then confirm `updated_at` changed anyway.
3. In one sentence, describe what a database migration tool would need to record about this trigger and function so that a teammate setting up the database from scratch gets the identical audit behaviour.

**Answer these questions after completing all tasks:**
- `reporting_role` in Task 2.1 can query the views but not the base tables. If someone granted it `SELECT` on `orders` directly "just to be safe," what would that undo, given that `cost_price` lives in that same table?
- Row-level security in Task 2.3 depends on `current_setting('app.current_customer_id')` being set correctly by the application on every connection. What would a customer see if the application forgot to set this session variable for one request?
- Task 2.4 asked you to compare a concatenated query against a parameterized one. Why does the parameterized version stay safe even if a customer's email field literally contains the text `' OR '1'='1`?

## Where to Build This Project

1. Go to [bytexl.app/nimbus](https://bytexl.app/nimbus).
2. Click **Create new workspace**.

![The Nimbus dashboard with the Create new workspace button highlighted](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_create_new_workspace.png)

3. Select the **PostgreSQL** template, then click **Next**.

![Select the PostgreSQL template and click Next](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_select_postgresql_template.png)

4. Enter a workspace name and click **Launch Workspace**.

![Enter a workspace name and launch the PostgreSQL workspace](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_name_and_launch_workspace.png)
