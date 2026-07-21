## Introduction

The double-booking scenario from the previous lesson is one specific example of a broader family of problems that show up whenever transactions overlap in time. Database theory gives each pattern in that family a precise name, so that a specific symptom can be diagnosed and discussed precisely, rather than everyone just calling every concurrency bug "a race condition":

- `Dirty reads`
- `Non-repeatable reads`
- `Phantom reads`
- `Lost updates`

Naming each one clearly is what makes the next lessons, on `locking` and `isolation levels`, possible to reason about at all.

**Definition:** `Dirty reads`, non-repeatable reads, phantom reads, and lost updates each name a specific way concurrent transactions can interfere with each other, giving a precise vocabulary for problems that would otherwise all just look like unpredictable bugs under load.

![Intro visual for concurrency problems](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_intro_concurrency_problems_clean_7c74ff1e.png)

## Dirty Reads: Seeing Data That Was Never Actually Committed

A `dirty read` happens when one transaction reads a change made by another transaction that has not yet committed, and might still be rolled back.

## Source Data Used in This Lesson

Before running the lesson queries, inspect the starting data. The tables below show the rows loaded by the setup file.

### `inventory`

| product_id | product_name | stock_count |
| --- | --- | --- |
| 1 | Wireless Mouse | 50 |

The OneCompiler activity keeps preparation and practice separate. `init.sql` creates the displayed tables, rows, roles, or supporting objects. The active SQL file contains only the statement currently being studied, and `with=init.sql` runs the preparation file first.

## Hands-On Setup: Prepare the Database

```postgresql
CREATE TABLE inventory (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    stock_count INTEGER
);

INSERT INTO inventory (product_id, product_name, stock_count) VALUES
(1, 'Wireless Mouse', 50);
```

Before running each active statement, predict which rows, database objects, or server behavior should change. Then compare the result with the expected output or observation supplied beneath the statement.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkafav2" 
 width="100%"
></iframe>

Expected output:



| stock_count |
| --- |
| 50 |

- The final `SELECT` correctly shows 50, since PostgreSQL's default isolation level prevents `dirty reads` entirely, a concurrent transaction is never allowed to see this kind of in-progress, uncommitted change, exactly the isolation guarantee covered in the previous chapter.
- `Dirty reads` are catalogued here because some databases, or some deliberately relaxed isolation levels, do allow them, and knowing the name of the problem is what makes a setting like "read uncommitted" understandable later in this chapter.

![Dirty read showing one transaction reading an uncommitted value that later rolls back](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_dirty_read_uncommitted_then_rollback.png)

## Non-Repeatable Reads: The Same Query, Two Different Answers

A `non-repeatable read` happens when a transaction reads the same row twice, and gets two different values, because another transaction committed a change to that row in between the two reads.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkafb65" 
 width="100%"
></iframe>

Expected output 1:



| stock_count |
| --- |
| 50 |

Expected output 2:



| stock_count |
| --- |
| 50 |

Unlike a `dirty read`, the second read here would reflect genuinely committed data, so nothing incorrect was ever seen the issue is that a single transaction's own view of the data changed mid-flight, which can be surprising or outright wrong for logic that assumes a value stays stable for the duration of a transaction.

## Phantom Reads: A Changing Set of Rows, Not Just a Changing Value

A `phantom read` is the same underlying problem as a non-repeatable read, but at the level of an entire query's row count rather than a single row's value: a transaction runs the same filtered query twice and gets a different number of rows back, because another transaction inserted or deleted matching rows in between.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkafbf8" 
 width="100%"
></iframe>

Expected output 1:



| COUNT(*) |
| --- |
| 0 |

Expected output 2:



| COUNT(*) |
| --- |
| 0 |

The new row was not a value that changed underneath Transaction A, it is an entirely new row matching a condition Transaction A was relying on, which is why this gets its own name distinct from a `non-repeatable read`.

![Non-repeatable read changing one row and phantom read adding a new matching row](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_nonrepeatable_vs_phantom_read.png)

## Lost Updates: Two Writes, One Silently Overwritten

A `lost update` happens when two transactions both read the same value, both calculate a new value based on that same original reading, and both write their result, with the second write silently overwriting the first, so one of the two changes disappears entirely, exactly the double-booking scenario from the previous lesson.

![Lost update where two transactions read the same value and one write overwrites the other](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_lost_update_overwritten_write.png)

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkafbrc" 
 width="100%"
></iframe>

Expected output:



| stock_count |
| --- |
| 47 |

The final value here is 47, reflecting only the second `UPDATE`; the first sale's reduction of 5 units was computed correctly but never actually preserved, because both updates were based on the same stale reading of 50 rather than each other's results.

## Concurrency Problems at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Problem</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What happens</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dirty read</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reading another transaction&#x27;s uncommitted, possibly-to-be-rolled-back change</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Non-repeatable read</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The same row read twice within one transaction returns two different values</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Phantom read</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The same filtered query run twice within one transaction returns a different set of rows</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lost update</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Two transactions both read the same value, both write a new value based on it, one write silently disappears</td>
    </tr>
  </tbody>
</table>

## Your Turn

Using the `inventory` table above, write a query sequence that demonstrates a `lost update` on `stock_count` for product 1, where two separate deductions of 10 and 15 units are both computed from the same starting value of 50, and show what the final stock count incorrectly ends up as.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkafc5e" 
 width="100%"
></iframe>

Expected result and verification:

If both updates are written as `UPDATE inventory SET stock_count = 50 - 10 WHERE product_id = 1;` and `UPDATE inventory SET stock_count = 50 - 15 WHERE product_id = 1;`, run one after the other, the final stock count is 35, reflecting only the second deduction, with the first 10-unit sale's effect on stock lost entirely.

## Conclusion

`Dirty reads`, non-repeatable reads, phantom reads, and lost updates each name a specific way concurrent transactions can interfere with each other, giving a precise vocabulary for problems that would otherwise all just look like unpredictable bugs under load. Recognizing which one is happening is the first step toward choosing the right fix. The next lesson covers `locking`, the mechanism a database uses to prevent these problems from happening in the first place.
