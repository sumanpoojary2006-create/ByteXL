## Introduction

Zoya is building order reports for a food delivery startup, and her very first attempt at a report exposes a problem the earlier chapters never had to deal with. The `orders` table stores a `customer_id` and a `restaurant_id` on every row, but not a single customer name or restaurant name.

That is not a mistake; it is the relational model working exactly as intended, storing customer details once in a `customers` table and restaurant details once in a `restaurants` table, so a customer's name is never duplicated across dozens of orders. The catch is that a report needs those names shown together, on the same line, and a single `SELECT` against `orders` alone simply cannot produce that.

This is precisely the problem a **join** solves: combining rows from two or more tables based on a matching column between them.

**Definition:** Joins exist because normalized tables intentionally keep related facts apart, one customer stored once, one restaurant stored once, and a query is what pulls those separated facts back together into a single readable result.

![Intro visual for why joins exist](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_intro_why_joins_exist_actual3d_536ca090.png)

## Seeing the Problem Without a Join

Three small tables model the food delivery system: customers who place orders, restaurants that fulfill them, and the orders that connect the two.

## Source Data Used in This Lesson

Before running the lesson queries, inspect the data they will use. The tables below show the rows loaded by the setup file.

### `customers`

| customer_id | customer_name | city |
| --- | --- | --- |
| 1 | Aditi Kulkarni | Pune |
| 2 | Rohan Das | Kolkata |
| 3 | Kavya Nair | Kochi |
| 4 | Imran Sheikh | Hyderabad |
| 5 | Neha Bhatt | Ahmedabad |

### `restaurants`

| restaurant_id | restaurant_name | city |
| --- | --- | --- |
| 1 | Pizza Palace | Pune |
| 2 | Sushi Central | Kolkata |
| 3 | Burger Barn | Pune |
| 4 | Taco Town | Hyderabad |

### `orders`

| order_id | customer_id | restaurant_id | amount | order_date |
| --- | --- | --- | --- | --- |
| 1 | 1 | 1 | 450 | 2025-05-01 |
| 2 | 2 | 2 | 620 | 2025-05-02 |
| 3 | 1 | 3 | 300 | 2025-05-03 |
| 4 | 3 | 1 | 500 | 2025-05-04 |
| 5 | 4 | 2 | 275 | 2025-05-05 |
| 6 | 2 | 3 | 180 | 2025-05-06 |

## Hands-On Setup: Prepare the Data

```postgresql
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

Before running the active query, read its `SELECT` list and clauses against the displayed source rows. Then compare the returned values with the expected output to see exactly what the function or operation changed.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkahkge" 
 width="100%"
></iframe>

Expected output:

| order_id | customer_id | restaurant_id | amount | order_date |
| --- | --- | --- | --- | --- |
| 1 | 1 | 1 | 450 | 2025-05-01 |
| 2 | 2 | 2 | 620 | 2025-05-02 |
| 3 | 1 | 3 | 300 | 2025-05-03 |
| 4 | 3 | 1 | 500 | 2025-05-04 |
| 5 | 4 | 2 | 275 | 2025-05-05 |
| 6 | 2 | 3 | 180 | 2025-05-06 |

Every row here is technically complete, an order id, who placed it, which restaurant it went to, an amount, and a date, but "who placed it" is just the number 1 or 2, not a name. Anyone reading this table has to separately look up `customer_id` 1 in the `customers` table to know it means Aditi Kulkarni. That lookup step, done manually, is exactly what a join automates.

## Why the Data Is Split Up Like This in the First Place

It might seem simpler to just store `customer_name` directly on every order row and skip the separate `customers` table entirely. That approach breaks down quickly. If Aditi places ten orders, her name would be duplicated ten times, and if she ever changed her registered name, all ten rows would need updating instead of one.

Keeping customer details in exactly one place, `customers`, and referencing that customer by id from `orders`, is the same normalization principle covered earlier in the course: one fact, stored once, referenced everywhere it is needed. A join is the tool that reassembles those separated facts back into one readable result whenever a query needs them together.

## A First Look at Combining Two Tables

Without naming a specific join type yet, here is what combining `orders` with `customers` on their shared id looks like.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkahktk" 
 width="100%"
></iframe>

Expected output:

| order_id | customer_name | amount |
| --- | --- | --- |
| 1 | Aditi Kulkarni | 450 |
| 2 | Rohan Das | 620 |
| 3 | Aditi Kulkarni | 300 |
| 4 | Kavya Nair | 500 |
| 5 | Imran Sheikh | 275 |
| 6 | Rohan Das | 180 |

`JOIN customers ON orders.customer_id = customers.customer_id` tells the database exactly how the two tables relate: a row in `orders` matches a row in `customers` when their `customer_id` values are equal. Two things happen for every match found:

1. The database locates the matching row in `customers`.

2. It produces one combined row carrying columns from both tables, which is how `customer_name`, a column that does not exist on `orders` at all, ends up in this result.

![A join using matching customer_id values to bring the customer name into an order report](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_join_lookup_ids_to_names.png)

## What a Join Actually Produces

It helps to think of a join as building a temporary, wider table on the fly, made only for the duration of this one query, by pairing up matching rows from each side.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkahm4f" 
 width="100%"
></iframe>

Expected output:

| order_id | customer_name | restaurant_name | amount |
| --- | --- | --- | --- |
| 1 | Aditi Kulkarni | Pizza Palace | 450 |
| 2 | Rohan Das | Sushi Central | 620 |
| 3 | Aditi Kulkarni | Burger Barn | 300 |
| 4 | Kavya Nair | Pizza Palace | 500 |
| 5 | Imran Sheikh | Sushi Central | 275 |
| 6 | Rohan Das | Burger Barn | 180 |

This joins three tables at once, and the result reads like a single flat table with an order id, the customer's real name, the restaurant's real name, and the amount, exactly the shape a report needs:

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">order_id</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">customer_name</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">restaurant_name</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">amount</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Aditi Kulkarni</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pizza Palace</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">450.00</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rohan Das</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sushi Central</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">620.00</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">3</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Aditi Kulkarni</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Burger Barn</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">300.00</td>
    </tr>
  </tbody>
</table>

Nothing was changed in `orders`, `customers`, or `restaurants` themselves; the join only affects what this one query returns.

![A join producing a temporary wider result table without changing the source tables](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_join_temporary_wider_result.png)

## Why Joins Exist, in One Line

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Without a <code>join</code></th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">With a <code>join</code></th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tables stay normalized, but reports show raw ids</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reports show readable names, ids stay hidden</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Customer or restaurant details stored once</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Same storage, just combined at query time</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A person has to manually cross-reference ids</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The database does the cross-referencing</td>
    </tr>
  </tbody>
</table>

## Your Turn

Zoya needs a quick check: which restaurant did order 4 go to, by name, not by id? Write a query against the `orders` and `restaurants` tables above that returns the `order_id` and the matching `restaurant_name`, for `order_id = 4`.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkahmda" 
 width="100%"
></iframe>

If your query joins `orders` to `restaurants` on `restaurant_id` and filters with `WHERE orders.order_id = 4`, it returns "Pizza Palace," confirming order 4 went to the same restaurant as order 1.

Expected output for the practice query:

| order_id | restaurant_name |
| --- | --- |
| 4 | Pizza Palace |

## Conclusion

Joins exist because normalized tables intentionally keep related facts apart, one customer stored once, one restaurant stored once, and a query is what pulls those separated facts back together into a single readable result.

Zoya can now see customer names and restaurant names sitting right next to order amounts, without ever duplicating that data in storage.

The join used here always found a match on both sides; the next lesson looks closely at what that matching actually requires and what happens to rows that do not find one.
