## Introduction

Zoya's manager asks a question the inner `join` from the last lesson cannot answer: "which registered customers have never placed a single order? I want to send them a welcome discount." An inner `join` between `customers` and `orders` only ever shows customers who already have a match, which means it is structurally incapable of surfacing the very customers this question cares about, the ones with no match at all. What Zoya needs is a `join` that keeps every row from `customers` regardless of whether a matching order exists, filling in the order columns with `NULL` when nothing matches. That is exactly what a **`LEFT JOIN`** does.

## Keeping Every Row From the Left Table

The same delivery `schema` is used again, including Neha Bhatt, who has never placed an order.

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
SELECT customers.customer_name, orders.order_id, orders.amount
FROM customers
LEFT JOIN orders ON customers.customer_id = orders.customer_id;
```

Every one of the 5 customers appears in this result, including Neha Bhatt, whose row now shows `NULL` for `order_id` and `amount` instead of being dropped. "Left" refers to `customers`, the table named first, right after `FROM`:

- A `LEFT JOIN` guarantees every row from that left-hand table survives, matched or not.
- The right-hand table, `orders`, only contributes columns when a match exists.

## Finding Unmatched Rows on Purpose

Combining a `LEFT JOIN` with a `WHERE` clause that checks for `NULL` on the right-hand table's key is the standard pattern for finding exactly the rows with no match, answering the manager's original question directly.

```postgresql with=delivery.sql
SELECT customers.customer_name
FROM customers
LEFT JOIN orders ON customers.customer_id = orders.customer_id
WHERE orders.order_id IS NULL;
```

`WHERE orders.order_id IS NULL` only keeps rows where the `join` found nothing to attach, and since `order_id` is the `primary key` of `orders`, it can only be `NULL` in the result when no matching order row existed in the first place. This returns exactly one name, Neha Bhatt, the customer the discount campaign needs to reach.

## Why the Table Order Matters

A `LEFT JOIN` is not symmetric; swapping which table comes first changes which side is protected from being dropped.

```postgresql with=delivery.sql
SELECT restaurants.restaurant_name, orders.order_id
FROM restaurants
LEFT JOIN orders ON restaurants.restaurant_id = orders.restaurant_id
WHERE orders.order_id IS NULL;
```

Here `restaurants` is on the left, so every restaurant is guaranteed to appear, and filtering for `orders.order_id IS NULL` now finds restaurants with no orders instead of customers with no orders. This returns Taco Town, the one restaurant from earlier lessons that has never received a single order. The same `LEFT JOIN ... WHERE ... IS NULL` pattern answers two entirely different business questions, depending purely on which table is written first.

## Counting Orders Per Customer, Including Zero

A `LEFT JOIN` combined with `GROUP BY` and `COUNT` is how a report shows every customer's order count, including customers who legitimately have zero, something an `INNER JOIN` could never produce since a zero-order customer has no rows to count in the first place.

```postgresql with=delivery.sql
SELECT customers.customer_name, COUNT(orders.order_id) AS order_count
FROM customers
LEFT JOIN orders ON customers.customer_id = orders.customer_id
GROUP BY customers.customer_name
ORDER BY order_count DESC;
```

`COUNT(orders.order_id)` counts only non-`NULL` values, as covered when `aggregate functions` were introduced, so Neha's row correctly shows 0 instead of being counted as 1 or omitted from the report entirely:

| customer_name | order_count |
|---|---|
| Aditi Kulkarni | 2 |
| Rohan Das | 2 |
| Kavya Nair | 1 |
| Imran Sheikh | 1 |
| Neha Bhatt | 0 |

Using `COUNT(*)` here instead would incorrectly count her as 1, since `COUNT(*)` counts rows regardless of `NULL` content, which is why `COUNT(orders.order_id)` is the deliberate choice.

## LEFT JOIN at a Glance

| Behavior | Result |
|---|---|
| Match found | Row included, columns from both tables |
| No match, right table | Left row still included, right-side columns are `NULL` |
| Filter for `right_table.key IS NULL` | Isolates rows with no match at all |
| Table order | The table right after `FROM` is the protected "left" side |

## Your Turn

The manager also wants to know which restaurants in Pune have never received an order, by name. Write a query against `restaurants` and `orders` above using `LEFT JOIN`, filtering to restaurants in the "Pune" city with no matching orders.

```postgresql with=delivery.sql
-- Write your query below
```

If your query left-`joins` `restaurants` to `orders` and filters with `WHERE restaurants.city = 'Pune' AND orders.order_id IS NULL`, the result is empty, correctly showing that both Pune restaurants, Pizza Palace and Burger Barn, have received at least one order each.

## Conclusion

`LEFT JOIN` guarantees every row from the first-named table survives the `join`, filling in `NULL` for the other side when no match exists, which makes it the right tool whenever "customers with no orders" or "restaurants with no orders" is itself the question. Zoya answered a question the inner `join` structurally could not answer, just by changing one keyword. A `RIGHT JOIN` mirrors this same idea from the opposite side, and a `FULL OUTER JOIN` protects both sides at once.
