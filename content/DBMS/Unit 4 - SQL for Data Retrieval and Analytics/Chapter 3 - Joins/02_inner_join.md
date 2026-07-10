## Introduction

The plain `JOIN` Zoya used to combine orders with customer and restaurant names has a formal name that the previous lesson skipped over: an **`INNER JOIN`**. `JOIN` by itself, with no other keyword in front of it, defaults to an inner `join` in every major database, so the two are the same thing, one just spelled out for clarity. What matters is understanding exactly what "inner" means: an inner `join` keeps a row in the result only when a match is found on both sides of the `join` condition. Rows with no match on either side are silently left out, and that quiet exclusion is worth understanding precisely before relying on it.

## Confirming the Match-Only Behavior

The same delivery `schema` from the previous lesson is the setup here, with one detail worth noticing: customer 5, Neha Bhatt, has never placed an order, and restaurant 4, Taco Town, has never received one.

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
INNER JOIN orders ON customers.customer_id = orders.customer_id;
```

This returns six rows, one per order, but Neha Bhatt never appears anywhere in the output, even though she is a perfectly valid row in `customers`. She has no matching row in `orders`, so the inner `join` excludes her entirely rather than showing her with blank order columns. This is the defining trait of `INNER JOIN`: no match means no row in the result, on either side.

## Checking the Row Count Before and After

It helps to compare the row count of a table alone against the row count after joining, to see exactly how many rows an inner `join` keeps.

```postgresql with=delivery.sql
SELECT COUNT(*) AS total_customers FROM customers;
```

```postgresql with=delivery.sql
SELECT COUNT(*) AS customers_with_orders
FROM customers
INNER JOIN orders ON customers.customer_id = orders.customer_id;
```

The `customers` table alone has 5 rows, but the joined query returns 6, not 5 and not fewer:

| customer_name | Orders placed | Rows contributed to the `join` |
|---|---|---|
| Aditi Kulkarni | 2 | 2 |
| Rohan Das | 2 | 2 |
| Kavya Nair | 1 | 1 |
| Imran Sheikh | 1 | 1 |
| Neha Bhatt | 0 | 0 |

That number is higher than 5 because Aditi Kulkarni and Rohan Das each placed more than one order, so an inner `join` produces one output row for every matching pair, and a customer with two orders contributes two rows to the result. Meanwhile, Neha's row contributes zero, since it has no partner in `orders` at all. The inner `join` row count depends entirely on how many matches exist, not on how many rows either original table has.

## Adding a WHERE Clause on Top of an Inner Join

Once tables are joined, `WHERE` filters the combined rows exactly the way it filters a single table, since after the `join` runs, the database is working with one wide result set.

```postgresql with=delivery.sql
SELECT customers.customer_name, restaurants.restaurant_name, orders.amount
FROM orders
INNER JOIN customers ON orders.customer_id = customers.customer_id
INNER JOIN restaurants ON orders.restaurant_id = restaurants.restaurant_id
WHERE orders.amount > 400;
```

This query runs in two clear stages:

1. The two `INNER JOIN` clauses first assemble the full combined view across all three tables.
2. Only then does `WHERE orders.amount > 400` remove the smaller orders, leaving just the three highest-value ones, orders 1, 2, and 4, with both the customer's and the restaurant's real names attached.

## When an Inner Join Is the Right Choice

An inner `join` is the right tool whenever a row without a match is not useful for the question being asked. A report on "orders and who placed them" has no reason to include a customer who has never ordered, since there is nothing to report about them in that context. The next lesson introduces a `join` type built for the opposite situation, when unmatched rows are exactly what needs to stay visible.

## INNER JOIN at a Glance

| Behavior | Result |
|---|---|
| Match found on both sides | Row included, columns from both tables |
| No match on the left table's side | Left row excluded entirely |
| No match on the right table's side | Right row excluded entirely |
| `JOIN` with no keyword | Defaults to `INNER JOIN` |

## Your Turn

Zoya wants a list of every restaurant that has actually received at least one order, with no duplicates needed, just the restaurant names that appear in `orders`. Write a query against `orders` and `restaurants` above using `INNER JOIN` and `DISTINCT` together.

```postgresql with=delivery.sql
-- Write your query below
```

If your query is `SELECT DISTINCT restaurants.restaurant_name FROM orders INNER JOIN restaurants ON orders.restaurant_id = restaurants.restaurant_id;`, it returns Pizza Palace, Sushi Central, and Burger Barn, and Taco Town is correctly missing, since it has never matched an order.

## Conclusion

`INNER JOIN`, and its shorthand `JOIN`, keeps only the rows where both sides of the `join` condition find a partner, quietly dropping everything else, which makes it the right choice whenever unmatched rows carry no useful information for the question at hand. Zoya now knows precisely why Neha Bhatt and Taco Town never showed up in her earlier reports. Sometimes, though, an unmatched row is exactly the information a report needs to surface, and that is where outer `joins` come in.
