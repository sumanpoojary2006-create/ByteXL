## Introduction

Knowing that `rows` live in pages raises a natural next question: in what order do `rows` actually land inside those pages? The answer is not automatically "sorted by `primary key`," or by anything else meaningful, unless the `database` is specifically told to organize the data that way.

There are a few standard strategies for how a `table`'s file can be organized, and PostgreSQL's default, called a heap, is deliberately the simplest and least structured of them. Understanding what a heap is, and the alternatives to it, explains why some `queries` that seem like they should be fast are not, without an `index` in the picture at all.

**Definition:** A heap places `rows` wherever space is free, with no ordering guarantee, sorted or clustered organization keeps `rows` physically near others with similar values in a chosen `column`, and hashed organization groups `rows` by a computed bucket for fast exact-match lookups, each with a different trade-off between write simplicity and read speed for a particular kind of `query`.

## Heap Organization: Rows Land Wherever There Is Room

By default, PostgreSQL stores a `table` as a heap, meaning new `rows` are simply placed wherever there happens to be free space, with no guaranteed ordering by any `column` at all.

## Source Data Used in This Lesson

Before running the lesson queries, inspect the starting data. The tables below show the rows loaded by the setup file.

### `orders`

| order_id | customer_name | amount |
| --- | --- | --- |
| 5 | Rohan Das | 450.00 |
| 2 | Aditi Kulkarni | 620.00 |
| 8 | Kavya Nair | 300.00 |
| 1 | Imran Sheikh | 900.00 |

The OneCompiler activity keeps preparation and practice separate. `init.sql` creates the displayed tables, rows, roles, or supporting objects. The active SQL file contains only the statement currently being studied, and `with=init.sql` runs the preparation file first.

## Hands-On Setup: Prepare the Database

```postgresql
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    amount NUMERIC(10, 2)
);

INSERT INTO orders (order_id, customer_name, amount) VALUES
(5, 'Rohan Das', 450.00),
(2, 'Aditi Kulkarni', 620.00),
(8, 'Kavya Nair', 300.00),
(1, 'Imran Sheikh', 900.00);
```

Before running each active statement, predict which rows, database objects, or server behavior should change. Then compare the result with the expected output or observation supplied beneath the statement.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkajmq8" 
 width="100%"
></iframe>

Expected output:

| ctid | order_id | customer_name |
| --- | --- | --- |
| (0,1) | 5 | Rohan Das |
| (0,2) | 2 | Aditi Kulkarni |
| (0,3) | 8 | Kavya Nair |
| (0,4) | 1 | Imran Sheikh |

Even though these `rows` were inserted with `order_id` values 5, 2, 8, then 1, their `ctid` values still reflect insertion order, not sorted `order_id` order, since a heap makes no attempt to keep `rows` physically sorted by any `column`.

This means a `query` that wants "every order with `order_id` between 1 and 4" cannot assume those `rows` sit near each other on disk. A heap offers no such guarantee, and finding them without help requires checking every page, a `full table scan`, the subject of the next lesson.

![Heap organization places rows wherever there is space while clustered organization keeps nearby keys together](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_heap_vs_sorted_clustered_layout.png)

## Sorted (Clustered) Organization: Rows Kept in Physical Order

An alternative organization keeps `rows` physically sorted by a chosen `column`, so that `rows` with nearby values in that `column` also sit near each other on disk. PostgreSQL does not maintain this automatically the way a heap works by default, but it can be requested explicitly with `CLUSTER`, which physically reorders an existing `table`'s `rows` to match an `index`'s order, as a one-time operation.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkajmzd" 
 width="100%"
></iframe>

Expected observation: PostgreSQL confirms that the index was created. The command does not return business rows; its effect is verified by rerunning the related query or `EXPLAIN` statement.

After `CLUSTER`, the `ctid` values now increase in the same order as `order_id`, confirming the `rows` have been physically rewritten on disk to sit in sorted order.

This is a genuinely different physical layout from the heap version above, and it is why a range `query` like "every order between id 1 and 4" becomes dramatically cheaper afterward: the matching `rows` are now physically adjacent, reachable by reading a small, contiguous run of pages instead of scattering across the whole `table`.

The cost is that `CLUSTER` is a one-time, explicit reorganization; new `rows` inserted afterward go back to landing wherever there is free space, gradually drifting the `table` back toward an unsorted heap unless `CLUSTER` is run again periodically.

## Hashed Organization: Rows Placed by a Computed Bucket

A third strategy, hashing, places each `row` into one of a fixed number of "buckets," determined by running the `row`'s key value through a hash `function`:

- Rows with the same key always hash to the same bucket.
- Looking up a specific value means computing its hash once and going straight to that bucket, rather than scanning a range.

The mechanism is directly visible using `hashtext`, one of PostgreSQL's built-in hash `functions`, mapping each name into one of eight buckets:

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkajna3" 
 width="100%"
></iframe>

Expected output:

| customer_name | bucket |
| --- | --- |
| Aditi Kulkarni | 3 |
| Imran Sheikh | 7 |
| Kavya Nair | 1 |
| Rohan Das | 5 |

With the names listed alphabetically, the bucket numbers jump around with no pattern at all: names that sit next to each other in alphabetical order land in completely unrelated buckets, and that is not a flaw but the entire design. A hash `function` deliberately scatters values evenly so that no bucket gets overloaded, and the unavoidable price is that any notion of "nearby" or "in between" is destroyed on the way in.

PostgreSQL does not organize whole `tables` this way, but it offers `hash indexes`, which apply exactly this idea to speed up equality lookups specifically, at the cost of being unable to help at all with range `queries` like "greater than" or "between."

![Hashed organization sends an exact-match key to one bucket but cannot preserve ranges](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_hash_bucket_exact_match_layout.png)

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkajnjt" 
 width="100%"
></iframe>

Expected observation: PostgreSQL confirms that the index was created. The command does not return business rows; its effect is verified by rerunning the related query or `EXPLAIN` statement.

This creates a hash-organized structure specifically for looking up an exact `customer_name` quickly, and the equality lookup that follows is precisely the kind of `query` it exists to serve: one specific value, found by computing its bucket. What it cannot help with is "find every customer whose name comes after Kavya alphabetically," a limitation directly explained by how hashing scrambles order on purpose.

## Choosing Between the Three, at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Organization</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Rows are physically</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Best for</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Weak for</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Heap (default)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Wherever there is free space, insertion order roughly</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fast writes, no reorganization overhead</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Any query that benefits from physical ordering</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sorted / clustered</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ordered by a chosen column</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Range queries on that column</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Staying sorted as new rows are inserted, without periodic re-clustering</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hashed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Grouped by a computed bucket</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Exact-match lookups</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Range queries, since hashing destroys order</td>
    </tr>
  </tbody>
</table>

## Your Turn

Using the `idx_orders_id` `index` and clustered layout already set up earlier in this lesson, insert three more orders with `order_id` values 3, 6, and 9, check every `row`'s `ctid`, and note in a comment whether the new `rows` were interleaved into sorted position or simply placed wherever free space happened to be.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkajnuq" 
 width="100%"
></iframe>

Expected result and verification:

New `rows` inserted after a `CLUSTER` operation are placed wherever free space is available, heap-style, not necessarily in sorted position, since `CLUSTER` only reorganizes the `table` at the moment it runs the `ctid` values for these new `rows` will likely appear after the already-clustered block rather than interleaved into perfectly sorted position.

## Conclusion

A heap places `rows` wherever space is free, with no ordering guarantee, sorted or clustered organization keeps `rows` physically near others with similar values in a chosen `column`, and hashed organization groups `rows` by a computed bucket for fast exact-match lookups, each with a different trade-off between write simplicity and read speed for a particular kind of `query`.

Priya can now reason about why an unclustered heap makes some of her range `queries` slower than expected. The next lesson connects this physical organization directly to what happens when a `query` actually runs against it.
