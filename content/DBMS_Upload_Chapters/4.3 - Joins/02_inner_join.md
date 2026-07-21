## Introduction

- The plain JOIN Zoya used to combine orders with customer and restaurant names has a formal name that the previous lesson skipped over: an **`INNER JOIN`**.
- JOIN by itself, with no other keyword in front of it, defaults to an inner join in every major database, so the two are the same thing, one just spelled out for clarity.
- What matters is understanding exactly what "inner" means: an inner join keeps a row in the result only when a match is found on both sides of the join condition.
- Rows with no match on either side are silently left out, and that quiet exclusion is worth understanding precisely before relying on it.

**Definition:** `INNER JOIN`, and its shorthand JOIN, keeps only the rows where both sides of the join condition find a partner, quietly dropping everything else, which makes it the right choice whenever unmatched rows carry no useful information for the question at hand.

![Intro visual for inner join](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_intro_inner_join_matched_59125b6c.png)

## Confirming the Match-Only Behavior

The same delivery schema from the previous lesson is the setup here, with one detail worth noticing: customer 5, Neha Bhatt, has never placed an order, and restaurant 4, Taco Town, has never received one.

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

The OneCompiler activity keeps setup and practice separate. `init.sql` creates and populates the displayed data, while the active SQL file contains only the query being studied.

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
 src="https://onecompiler.com/embed/postgresql/44vkahp6s" 
 width="100%"
></iframe>

Expected output:

| customer_name | order_id | amount |
| --- | --- | --- |
| Aditi Kulkarni | 1 | 450 |
| Rohan Das | 2 | 620 |
| Aditi Kulkarni | 3 | 300 |
| Kavya Nair | 4 | 500 |
| Imran Sheikh | 5 | 275 |
| Rohan Das | 6 | 180 |

This returns six rows, one per order, but Neha Bhatt never appears anywhere in the output, even though she is a perfectly valid row in `customers`. She has no matching row in `orders`, so the inner join excludes her entirely rather than showing her with blank order columns. This is the defining trait of `INNER JOIN`: no match means no row in the result, on either side.

![INNER JOIN keeping only rows that have a matching partner on both sides](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_inner_join_matched_only.png)

## Checking the Row Count Before and After

It helps to compare the row count of a table alone against the row count after joining, to see exactly how many rows an inner join keeps.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkahpfu" 
 width="100%"
></iframe>

Expected output:

| total_customers |
| --- |
| 5 |

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkahps9" 
 width="100%"
></iframe>

Expected output:

| customers_with_orders |
| --- |
| 6 |

The `customers` table alone has 5 rows, but the joined query returns 6, not 5 and not fewer:

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">customer_name</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Orders placed</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Rows contributed to the <code>join</code></th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Aditi Kulkarni</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rohan Das</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Kavya Nair</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Imran Sheikh</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Neha Bhatt</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">0</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">0</td>
    </tr>
  </tbody>
</table>

That number is higher than 5 because Aditi Kulkarni and Rohan Das each placed more than one order, so an inner join produces one output row for every matching pair, and a customer with two orders contributes two rows to the result. Meanwhile, Neha's row contributes zero, since it has no partner in `orders` at all.

The inner join row count depends entirely on how many matches exist, not on how many rows either original table has.

![INNER JOIN producing two joined rows when one customer matches two orders](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_inner_join_one_to_many_rows.png)

## Adding a WHERE Clause on Top of an Inner Join

Once tables are joined, `WHERE` filters the combined rows exactly the way it filters a single table, since after the join runs, the database is working with one wide result set.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkahq3b" 
 width="100%"
></iframe>

Expected output:

| customer_name | restaurant_name | amount |
| --- | --- | --- |
| Aditi Kulkarni | Pizza Palace | 450 |
| Rohan Das | Sushi Central | 620 |
| Kavya Nair | Pizza Palace | 500 |

This query runs in two clear stages:

1. The two `INNER JOIN` clauses first assemble the full combined view across all three tables.

2. Only then does `WHERE orders.amount > 400` remove the smaller orders, leaving just the three highest-value ones, orders 1, 2, and 4, with both the customer's and the restaurant's real names attached.

## When an Inner Join Is the Right Choice

An inner join is the right tool whenever a row without a match is not useful for the question being asked. A report on "orders and who placed them" has no reason to include a customer who has never ordered, since there is nothing to report about them in that context.

The next lesson introduces a join type built for the opposite situation, when unmatched rows are exactly what needs to stay visible.

## INNER JOIN at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Behavior</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Result</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Match found on both sides</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Row included, columns from both tables</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No match on the left table&#x27;s side</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Left row excluded entirely</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No match on the right table&#x27;s side</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Right row excluded entirely</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>JOIN</code> with no keyword</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Defaults to <code>INNER JOIN</code></td>
    </tr>
  </tbody>
</table>

## Your Turn

Zoya wants a list of every restaurant that has actually received at least one order, with no duplicates needed, just the restaurant names that appear in `orders`. Write a query against `orders` and `restaurants` above using `INNER JOIN` and `DISTINCT` together.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkahqjb" 
 width="100%"
></iframe>

If your query is `SELECT DISTINCT restaurants.restaurant_name FROM orders INNER JOIN restaurants ON orders.restaurant_id = restaurants.restaurant_id;`, it returns Pizza Palace, Sushi Central, and Burger Barn, and Taco Town is correctly missing, since it has never matched an order.


Expected output for the practice query:

| restaurant_name |
| --- |
| Burger Barn |
| Pizza Palace |
| Sushi Central |

## Conclusion

`INNER JOIN`, and its shorthand JOIN, keeps only the rows where both sides of the join condition find a partner, quietly dropping everything else, which makes it the right choice whenever unmatched rows carry no useful information for the question at hand.

Zoya now knows precisely why Neha Bhatt and Taco Town never showed up in her earlier reports.

Sometimes, though, an unmatched row is exactly the information a report needs to surface, and that is where outer joins come in.
