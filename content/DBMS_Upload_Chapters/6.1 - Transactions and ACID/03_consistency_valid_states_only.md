## Introduction

Atomicity guarantees a transaction commits entirely or not at all, but it says nothing about whether the resulting data actually makes sense. A transaction could atomically commit a balance of -500.00 if nothing was stopping it, perfectly all-or-nothing, and perfectly wrong.

The second letter in ACID, **consistency**, is the guarantee that a transaction can only move a database from one valid state to another valid state, never into a state that breaks the rules the database has been told to enforce. Where atomicity is about the transaction as a whole succeeding or failing, consistency is about what "succeeding" is even allowed to look like.

**Definition:** Consistency guarantees that a transaction can only ever move a database from one valid state to another, with every declared constraint, `CHECK`, `foreign key`, `NOT NULL`, or `UNIQUE`, acting as the database's own definition of what "valid" means, while business rules that were never expressed as a constraint remain the application's responsibility to protect.

![Intro visual for consistency valid states only](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_intro_consistency_valid_states_only_matched_26d05f32.png)

## Constraints Are What Define a Valid State

The `accounts` table, with a constraint restored from the previous lesson, defines exactly what counts as valid.

## Source Data Used in This Lesson

Before running the lesson queries, inspect the starting data. The tables below show the rows loaded by the setup file.

### `accounts`

| account_id | owner_name | balance |
| --- | --- | --- |
| 1 | Meera Iyer | 50000.00 |
| 2 | Sanjay Rathi | 12000.00 |

The OneCompiler activity keeps preparation and practice separate. `init.sql` creates the displayed tables, rows, roles, or supporting objects. The active SQL file contains only the statement currently being studied, and `with=init.sql` runs the preparation file first.

## Hands-On Setup: Prepare the Database

```postgresql
CREATE TABLE accounts (
    account_id INTEGER PRIMARY KEY,
    owner_name TEXT,
    balance NUMERIC(10, 2) CHECK (balance >= 0)
);

INSERT INTO accounts (account_id, owner_name, balance) VALUES
(1, 'Meera Iyer', 50000.00),
(2, 'Sanjay Rathi', 12000.00);
```

Before running each active statement, predict which rows, database objects, or server behavior should change. Then compare the result with the expected output or observation supplied beneath the statement.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaj3qd" 
 width="100%"
></iframe>

Expected output:



| account_id | balance |
| --- | --- |
| 1 | 50000.00 |
| 2 | 12000.00 |

- The `CHECK (balance >= 0)` constraint is the database's own definition of a valid account row.
- This transaction tries to push Meera's balance to -10000.00, and the database refuses to let that become the committed state, rejecting the statement and, through atomicity, rolling back the whole transaction along with it.
- The final `SELECT` shows Meera's balance unchanged.

![A CHECK constraint blocking an invalid negative balance from becoming committed data](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_consistency_check_constraint_blocks_invalid.png)

This is consistency and atomicity working together:

- Atomicity ensures the rejected statement does not leave a half-applied transaction behind.
- Consistency is the reason the statement was rejected in the first place, since it would have produced an invalid row.

## Consistency Enforced Through Foreign Keys

Constraints that define validity are not limited to `CHECK`. A `foreign key` is just as much a consistency rule, and a transaction that would violate one is refused the same way.

```postgresql
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT
);

CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(customer_id),
    amount NUMERIC(10, 2)
);

INSERT INTO customers (customer_id, customer_name) VALUES (1, 'Aditi Kulkarni');
```

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaj3zu" 
 width="100%"
></iframe>

- Customer id 99 does not exist in `customers`, so this `INSERT` would create an order pointing to a customer that does not exist, a state the `foreign key` constraint defines as invalid.
- The database rejects it, the transaction fails, and `orders` remains empty.
- Consistency here means the database will never contain an order referencing a customer that is not really there, regardless of what any individual transaction tries to do.

![A foreign key allowing valid references and blocking orders with missing customers](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/06_consistency_foreign_key_valid_link.png)

## Consistency Also Depends on the Application

- Database-level consistency only enforces what has been explicitly declared as a constraint.
- A rule the database was never told about is not something it can protect.
- If the actual business rule is "the total money across all accounts in the bank must never change," but no constraint expresses that, the database cannot stop a transaction that deducts money from one account without crediting it anywhere.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaj4ay" 
 width="100%"
></iframe>

Expected output:



| total_money_in_bank |
| --- |
| 57000 |

- This transaction commits successfully, since it violates no constraint the database knows about, `balance >= 0` still holds.
- But 5000.00 has vanished from the total across the bank, a business-level inconsistency the database had no way to detect, since that particular rule was never declared as a constraint.
- This is why consistency is often described as a shared responsibility: the database enforces every rule it has been explicitly told about, through constraints, and the application is responsible for grouping the right statements into a transaction, as covered in the very first lesson of this chapter, so that whole business operations either complete together or not at all.

## Consistency at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Enforced by</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Who is responsible</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>CHECK</code> <code>constraints</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Balance cannot go negative</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The database, automatically</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Foreign keys</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An order cannot reference a nonexistent customer</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The database, automatically</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><code>NOT NULL</code>, <code>UNIQUE</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Every row has required data, no duplicate keys</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The database, automatically</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Business rules with no matching <code>constraint</code></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Total money in the system stays constant</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The application, by grouping the right statements into one transaction</td>
    </tr>
  </tbody>
</table>

## Your Turn

Add a `CHECK` constraint to the `orders` table requiring `amount > 0`, then attempt a transaction that inserts an order with `amount = -200.00`, and confirm it is rejected.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/postgresql/44vkaj4ma" 
 width="100%"
></iframe>

If you run `ALTER TABLE orders ADD CONSTRAINT positive_amount CHECK (amount > 0);` followed by a transaction inserting `amount = -200.00`, the `INSERT` is rejected, the transaction commits nothing, and a closing `SELECT * FROM orders;` shows the table still empty.

## Conclusion

Consistency guarantees that a transaction can only ever move a database from one valid state to another, with every declared constraint, `CHECK`, `foreign key`, `NOT NULL`, or `UNIQUE`, acting as the database's own definition of what "valid" means, while business rules that were never expressed as a constraint remain the application's responsibility to protect. Rahul's banking data can now be trusted to never violate a rule the database actually knows about.

Atomicity and consistency both concern a single transaction's own correctness; the next property addresses what happens when multiple transactions run at the same time.
