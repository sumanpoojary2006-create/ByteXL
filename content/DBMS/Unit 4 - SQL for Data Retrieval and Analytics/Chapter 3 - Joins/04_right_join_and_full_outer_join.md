## Introduction

Zoya now understands `LEFT JOIN` well enough to solve it a different way: instead of writing `restaurants LEFT JOIN orders` to protect every restaurant, she could write `orders RIGHT JOIN restaurants` and protect the same table from the other side. A **`RIGHT JOIN`** is the mirror image of a `LEFT JOIN`, guaranteeing every row from the table named after `RIGHT JOIN` survives, regardless of a match. There is also a third option, a **`FULL OUTER JOIN`**, for the rarer case where unmatched rows on both sides need to stay visible at the same time, not just one side or the other.

## RIGHT JOIN as the Mirror of LEFT JOIN

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
SELECT orders.order_id, restaurants.restaurant_name
FROM orders
RIGHT JOIN restaurants ON orders.restaurant_id = restaurants.restaurant_id;
```

Every one of the 4 restaurants appears here, including Taco Town, whose row shows `NULL` for `order_id` since it has never received an order. This is exactly the same result the previous lesson's `restaurants LEFT JOIN orders` produced, just written with the table order reversed and the `join` keyword swapped. In practice, most SQL style guides, and most of the lessons in this course, prefer `LEFT JOIN` over `RIGHT JOIN` for readability, since it reads left to right in the same order the tables are typically listed, but both exist and behave as exact mirrors of each other.

## Rewriting a RIGHT JOIN as a LEFT JOIN

Because a `RIGHT JOIN` is only ever the mirror of a `LEFT JOIN`, any query using one can be rewritten using the other in two steps:

1. Swap which table is named first, right after `FROM`.
2. Swap `RIGHT JOIN` for `LEFT JOIN`.

```postgresql with=delivery.sql
SELECT orders.order_id, restaurants.restaurant_name
FROM restaurants
LEFT JOIN orders ON restaurants.restaurant_id = orders.restaurant_id;
```

This produces the identical result to the `RIGHT JOIN` version above. Since `LEFT JOIN` is far more commonly used across real codebases, being able to mentally convert a `RIGHT JOIN` into an equivalent `LEFT JOIN` makes it easier to read queries written by other people without keeping two separate mental models.

## Protecting Both Sides at Once with FULL OUTER JOIN

Neither `LEFT JOIN` nor `RIGHT JOIN` can show unmatched rows from both `customers` and `restaurants`-style tables in the same result; each one only protects a single side. `FULL OUTER JOIN` protects both sides simultaneously, keeping every row from either table, matched or not.

```postgresql with=delivery.sql
SELECT customers.customer_name, orders.order_id
FROM customers
FULL OUTER JOIN orders ON customers.customer_id = orders.customer_id;
```

This result includes Neha Bhatt with `NULL` order columns, exactly as a `LEFT JOIN` would, and it would also include any order row with no matching customer, exactly as a `RIGHT JOIN` would, though in this particular data every order does have a valid customer. A `FULL OUTER JOIN` is essentially a `LEFT JOIN` and a `RIGHT JOIN` combined into a single result, with no row from either side left out.

## Finding Rows Unmatched on Either Side

The same `IS NULL` filtering pattern from the `LEFT JOIN` lesson still applies, just checking both sides now.

```postgresql with=delivery.sql
SELECT customers.customer_name, orders.order_id
FROM customers
FULL OUTER JOIN orders ON customers.customer_id = orders.customer_id
WHERE customers.customer_id IS NULL OR orders.order_id IS NULL;
```

This surfaces every row that is missing a partner on either side, in one query. With the data used across this chapter, only Neha Bhatt qualifies, since every order in this dataset does have a matching customer, but the pattern itself is what generalizes to any dataset where mismatches could appear on both sides.

## The Full Join Family at a Glance

| `Join` type | Left table rows | Right table rows |
|---|---|---|
| `INNER JOIN` | Only if matched | Only if matched |
| `LEFT JOIN` | All, matched or not | Only if matched |
| `RIGHT JOIN` | Only if matched | All, matched or not |
| `FULL OUTER JOIN` | All, matched or not | All, matched or not |

## Your Turn

Zoya wants a single audit report showing every restaurant and every order, with no restaurant left out even if it has zero orders. Write that query against `restaurants` and `orders` above using whichever `join` type guarantees every restaurant appears, ordering the result by `restaurant_name`.

```postgresql with=delivery.sql
-- Write your query below
```

If your query uses `restaurants LEFT JOIN orders ON restaurants.restaurant_id = orders.restaurant_id ORDER BY restaurants.restaurant_name`, all four restaurants appear, with Taco Town showing `NULL` order details since it has none.

## Conclusion

`RIGHT JOIN` mirrors `LEFT JOIN` from the opposite table, and `FULL OUTER JOIN` protects both sides of a `join` at once, together completing the full family of ways two tables can be combined based on whether unmatched rows should be kept or dropped, and on which side. Zoya's audit report can now guarantee every restaurant appears regardless of which side of the `join` it sits on. With `INNER`, `LEFT`, `RIGHT`, and `FULL OUTER` all covered, the next lesson looks at a `join` where a table is matched not against a different table, but against itself.
