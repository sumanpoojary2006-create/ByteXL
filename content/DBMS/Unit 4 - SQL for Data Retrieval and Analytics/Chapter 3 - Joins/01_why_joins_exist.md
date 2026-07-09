## Introduction

Zoya is building order reports for a food delivery startup, and her very first attempt at a report exposes a problem the earlier chapters never had to deal with. The `orders` table stores a `customer_id` and a `restaurant_id` on every row, but not a single customer name or restaurant name. That is not a mistake; it is the relational model working exactly as intended, storing customer details once in a `customers` table and restaurant details once in a `restaurants` table, so a customer's name is never duplicated across dozens of orders. The catch is that a report needs those names shown together, on the same line, and a single `SELECT` against `orders` alone simply cannot produce that. This is precisely the problem a **`join`** solves: combining rows from two or more tables based on a matching column between them.

## Seeing the Problem Without a Join

Three small tables model the food delivery system: customers who place orders, restaurants that fulfill them, and the orders that connect the two.

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
SELECT * FROM orders;
```

Every row here is technically complete, an order id, who placed it, which restaurant it went to, an amount, and a date, but "who placed it" is just the number 1 or 2, not a name. Anyone reading this table has to separately look up `customer_id` 1 in the `customers` table to know it means Aditi Kulkarni. That lookup step, done manually, is exactly what a `join` automates.

## Why the Data Is Split Up Like This in the First Place

It might seem simpler to just store `customer_name` directly on every order row and skip the separate `customers` table entirely. That approach breaks down quickly. If Aditi places ten orders, her name would be duplicated ten times, and if she ever changed her registered name, all ten rows would need updating instead of one. Keeping customer details in exactly one place, `customers`, and referencing that customer by id from `orders`, is the same normalization principle covered earlier in the course: one fact, stored once, referenced everywhere it is needed. A `join` is the tool that reassembles those separated facts back into one readable result whenever a query needs them together.

## A First Look at Combining Two Tables

Without naming a specific `join` type yet, here is what combining `orders` with `customers` on their shared id looks like.

```postgresql with=delivery.sql
SELECT orders.order_id, customers.customer_name, orders.amount
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id;
```

`JOIN customers ON orders.customer_id = customers.customer_id` tells the database exactly how the two tables relate: a row in `orders` matches a row in `customers` when their `customer_id` values are equal. Two things happen for every match found:

1. The database locates the matching row in `customers`.
2. It produces one combined row carrying columns from both tables, which is how `customer_name`, a column that does not exist on `orders` at all, ends up in this result.

## What a Join Actually Produces

It helps to think of a `join` as building a temporary, wider table on the fly, made only for the duration of this one query, by pairing up matching rows from each side.

```postgresql with=delivery.sql
SELECT orders.order_id, customers.customer_name, restaurants.restaurant_name, orders.amount
FROM orders
JOIN customers ON orders.customer_id = customers.customer_id
JOIN restaurants ON orders.restaurant_id = restaurants.restaurant_id;
```

This `joins` three tables at once, and the result reads like a single flat table with an order id, the customer's real name, the restaurant's real name, and the amount, exactly the shape a report needs:

| order_id | customer_name | restaurant_name | amount |
|---|---|---|---|
| 1 | Aditi Kulkarni | Pizza Palace | 450.00 |
| 2 | Rohan Das | Sushi Central | 620.00 |
| 3 | Aditi Kulkarni | Burger Barn | 300.00 |

Nothing was changed in `orders`, `customers`, or `restaurants` themselves; the `join` only affects what this one query returns.

## Why Joins Exist, in One Line

| Without a `join` | With a `join` |
|---|---|
| Tables stay normalized, but reports show raw ids | Reports show readable names, ids stay hidden |
| Customer or restaurant details stored once | Same storage, just combined at query time |
| A person has to manually cross-reference ids | The database does the cross-referencing |

## Your Turn

Zoya needs a quick check: which restaurant did order 4 go to, by name, not by id? Write a query against the `orders` and `restaurants` tables above that returns the `order_id` and the matching `restaurant_name`, for `order_id = 4`.

```postgresql with=delivery.sql
-- Write your query below
```

If your query `joins` `orders` to `restaurants` on `restaurant_id` and filters with `WHERE orders.order_id = 4`, it returns "Pizza Palace," confirming order 4 went to the same restaurant as order 1.

## Conclusion

`Joins` exist because normalized tables intentionally keep related facts apart, one customer stored once, one restaurant stored once, and a query is what pulls those separated facts back together into a single readable result. Zoya can now see customer names and restaurant names sitting right next to order amounts, without ever duplicating that data in storage. The `join` used here always found a match on both sides; the next lesson looks closely at what that matching actually requires and what happens to rows that do not find one.
