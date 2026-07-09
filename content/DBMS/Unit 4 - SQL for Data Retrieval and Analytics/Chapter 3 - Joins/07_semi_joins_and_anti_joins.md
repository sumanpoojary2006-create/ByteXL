## Introduction

Back in the `LEFT JOIN` lesson, Zoya found customers with no orders by joining `customers` to `orders` and filtering for `WHERE orders.order_id IS NULL`. That query works, but it is solving a check-for-existence question using a tool built for combining columns, and it quietly relies on picking exactly the right column to check for `NULL`. There is a more direct way to ask "does a matching row exist" or "does no matching row exist," using `EXISTS` and `NOT EXISTS`. These patterns are known as a **semi `join`**, which returns rows from one table where a match exists elsewhere without pulling in any columns from that other table, and an **anti `join`**, which returns rows where no match exists.

## Finding Rows That Have a Match, Without Pulling in Columns

The same delivery `schema` applies here, with Neha Bhatt having no orders and Taco Town having no orders.

```postgresql file=delivery.sql
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    city TEXT
);

CREATE TABLE restaurants (
    restaurant_id INTEGER PRIMARY KEY,
    restaurant_name TEXT,
    city TEXT
);

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(customer_id),
    restaurant_id INTEGER REFERENCES restaurants(restaurant_id),
    amount NUMERIC(10, 2),
    order_date DATE
);

INSERT INTO customers (customer_id, customer_name, city) VALUES
(1, 'Aditi Kulkarni', 'Pune'),
(2, 'Rohan Das', 'Kolkata'),
(3, 'Kavya Nair', 'Kochi'),
(4, 'Imran Sheikh', 'Hyderabad'),
(5, 'Neha Bhatt', 'Ahmedabad');

INSERT INTO restaurants (restaurant_id, restaurant_name, city) VALUES
(1, 'Pizza Palace', 'Pune'),
(2, 'Sushi Central', 'Kolkata'),
(3, 'Burger Barn', 'Pune'),
(4, 'Taco Town', 'Hyderabad');

INSERT INTO orders (order_id, customer_id, restaurant_id, amount, order_date) VALUES
(1, 1, 1, 450.00, '2025-05-01'),
(2, 2, 2, 620.00, '2025-05-02'),
(3, 1, 3, 300.00, '2025-05-03'),
(4, 3, 1, 500.00, '2025-05-04'),
(5, 4, 2, 275.00, '2025-05-05'),
(6, 2, 3, 180.00, '2025-05-06');
```

```postgresql with=delivery.sql
SELECT customer_name
FROM customers c
WHERE EXISTS (
    SELECT 1 FROM orders o WHERE o.customer_id = c.customer_id
);
```

`EXISTS` checks whether the inner query returns at least one row for the current customer, and if it does, that customer is kept. The inner query, `SELECT 1 FROM orders o WHERE o.customer_id = c.customer_id`, never actually needs the value 1 for anything; it exists purely to test for a matching row, so the database can stop looking the moment it finds one match, without ever needing to return an order's actual columns.

This behaves differently from an `INNER JOIN` in one important way:

- `EXISTS` only ever checks yes-or-no, so a customer can never appear more than once in the result.
- An `INNER JOIN` version of the same idea would duplicate a customer once per matching order, exactly the multiplying-rows behavior covered earlier in this chapter.

This returns four customers, everyone except Neha Bhatt.

## Finding Rows That Have No Match

`NOT EXISTS` flips the same idea around, keeping only the rows where the inner query finds nothing at all.

```postgresql with=delivery.sql
SELECT customer_name
FROM customers c
WHERE NOT EXISTS (
    SELECT 1 FROM orders o WHERE o.customer_id = c.customer_id
);
```

This returns exactly one row, Neha Bhatt, the same answer the `LEFT JOIN ... WHERE order_id IS NULL` pattern produced earlier, but arrived at without ever `joining` a single column from `orders` into the result. For a pure existence check like this one, `NOT EXISTS` states the intent more directly: "keep this customer only if no order references them," rather than "`join` every order, then throw away everything except the empty matches."

## Using IN as a Simpler Alternative for Single-Column Checks

When the check only involves a single column with no other condition tying the two queries together, `IN` and `NOT IN` offer a shorter alternative to `EXISTS` and `NOT EXISTS`.

```postgresql with=delivery.sql
SELECT customer_name
FROM customers
WHERE customer_id IN (SELECT customer_id FROM orders);
```

```postgresql with=delivery.sql
SELECT customer_name
FROM customers
WHERE customer_id NOT IN (SELECT customer_id FROM orders WHERE customer_id IS NOT NULL);
```

The first query is a semi `join` written with `IN`, returning customers whose id appears anywhere in the `orders.customer_id` column. The second is an anti `join` written with `NOT IN`, and it deliberately filters out `NULL` values from the subquery first with `WHERE customer_id IS NOT NULL`; if that filter were left out and even one `NULL` slipped into the list `NOT IN` compares against, the entire `NOT IN` condition would return no rows at all for every customer, a well-known trap with `NOT IN` that `NOT EXISTS` does not share. For that reason, `NOT EXISTS` is generally the safer default over `NOT IN` whenever the compared column can contain `NULL`.

## Why Semi and Anti Joins Are Not Written with a JOIN Keyword

Despite the name, semi and anti `joins` are not written using `JOIN`, `LEFT JOIN`, or any other `join` keyword in standard SQL; they are existence checks expressed with `EXISTS`, `NOT EXISTS`, `IN`, or `NOT IN`. The term describes the shape of the result, one row from the outer table per match found or not found, with no columns pulled in from the other table, rather than a specific piece of SQL syntax.

## Semi and Anti Joins at a Glance

| Pattern | Meaning | Safe with NULLs? |
|---|---|---|
| `WHERE EXISTS (subquery)` | Keep rows with at least one match | Yes |
| `WHERE NOT EXISTS (subquery)` | Keep rows with no match at all | Yes |
| `WHERE col IN (subquery)` | Shorter form of a semi `join`, single column | Yes |
| `WHERE col NOT IN (subquery)` | Shorter form of an anti `join`, single column | No, breaks if subquery returns a `NULL` |

## Your Turn

Zoya wants to find every restaurant that has never received an order, using an existence check rather than a `LEFT JOIN`. Write a query against `restaurants` and `orders` above using `NOT EXISTS`.

```postgresql with=delivery.sql
-- Write your query below
```

If your query is `SELECT restaurant_name FROM restaurants r WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.restaurant_id = r.restaurant_id);`, it returns Taco Town, the one restaurant with no matching orders.

## Conclusion

Semi `joins` and anti `joins` answer "does a match exist" and "does no match exist" directly, using `EXISTS`, `NOT EXISTS`, `IN`, or `NOT IN`, without pulling in columns from the other table or risking duplicated rows the way an `INNER JOIN` or `LEFT JOIN` can. Zoya now has two ways to find unmatched customers and restaurants, a `LEFT JOIN` with a `NULL` check, and a direct existence check, and can choose whichever fits a given query's intent most clearly. With `joins` covering how separate tables combine, the next chapter turns to combining entire query results directly, using set operations.
