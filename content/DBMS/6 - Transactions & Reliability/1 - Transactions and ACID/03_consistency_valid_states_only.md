## Introduction

Atomicity guarantees a transaction commits entirely or not at all, but it says nothing about whether the resulting data actually makes sense. A transaction could atomically commit a balance of -500.00 if nothing was stopping it, perfectly all-or-nothing, and perfectly wrong. The second letter in ACID, **consistency**, is the guarantee that a transaction can only move a database from one valid state to another valid state, never into a state that breaks the rules the database has been told to enforce. Where atomicity is about the transaction as a whole succeeding or failing, consistency is about what "succeeding" is even allowed to look like.

## Constraints Are What Define a Valid State

The `accounts` table, with a `constraint` restored from the previous lesson, defines exactly what counts as valid.

```postgresql file=accounts_consistency.sql
CREATE TABLE accounts (
    account_id INTEGER PRIMARY KEY,
    owner_name TEXT,
    balance NUMERIC(10, 2) CHECK (balance >= 0)
);

INSERT INTO accounts (account_id, owner_name, balance) VALUES
(1, 'Meera Iyer', 50000.00),
(2, 'Sanjay Rathi', 12000.00);
```

```postgresql with=accounts_consistency.sql
BEGIN;
UPDATE accounts SET balance = balance - 60000.00 WHERE account_id = 1;
COMMIT;

SELECT account_id, balance FROM accounts;
```

The `CHECK (balance >= 0)` `constraint` is the database's own definition of a valid account row. This transaction tries to push Meera's balance to -10000.00, and the database refuses to let that become the committed state, rejecting the statement and, through atomicity, rolling back the whole transaction along with it. The final `SELECT` shows Meera's balance unchanged.

This is consistency and atomicity working together:

- Atomicity ensures the rejected statement does not leave a half-applied transaction behind.
- Consistency is the reason the statement was rejected in the first place, since it would have produced an invalid row.

## Consistency Enforced Through Foreign Keys

`Constraints` that define validity are not limited to `CHECK`. A `foreign key` is just as much a consistency rule, and a transaction that would violate one is refused the same way.

```postgresql file=orders_consistency.sql
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

```postgresql with=orders_consistency.sql
BEGIN;
INSERT INTO orders (order_id, customer_id, amount) VALUES (1, 99, 500.00);
COMMIT;

SELECT * FROM orders;
```

Customer id 99 does not exist in `customers`, so this `INSERT` would create an order pointing to a customer that does not exist, a state the `foreign key` `constraint` defines as invalid. The database rejects it, the transaction fails, and `orders` remains empty. Consistency here means the database will never contain an order referencing a customer that is not really there, regardless of what any individual transaction tries to do.

## Consistency Also Depends on the Application

Database-level consistency only enforces what has been explicitly declared as a `constraint`. A rule the database was never told about is not something it can protect. If the actual business rule is "the total money across all accounts in the bank must never change," but no `constraint` expresses that, the database cannot stop a transaction that deducts money from one account without crediting it anywhere.

```postgresql with=accounts_consistency.sql
BEGIN;
UPDATE accounts SET balance = balance - 5000.00 WHERE account_id = 1;
COMMIT;

SELECT SUM(balance) AS total_money_in_bank FROM accounts;
```

This transaction commits successfully, since it violates no `constraint` the database knows about, `balance >= 0` still holds. But 5000.00 has vanished from the total across the bank, a business-level inconsistency the database had no way to detect, since that particular rule was never declared as a `constraint`. This is why consistency is often described as a shared responsibility: the database enforces every rule it has been explicitly told about, through `constraints`, and the application is responsible for grouping the right statements into a transaction, as covered in the very first lesson of this chapter, so that whole business operations either complete together or not at all.

## Consistency at a Glance

| Enforced by | Example | Who is responsible |
|---|---|---|
| `CHECK` `constraints` | Balance cannot go negative | The database, automatically |
| Foreign keys | An order cannot reference a nonexistent customer | The database, automatically |
| `NOT NULL`, `UNIQUE` | Every row has required data, no duplicate keys | The database, automatically |
| Business rules with no matching `constraint` | Total money in the system stays constant | The application, by grouping the right statements into one transaction |

## Your Turn

Add a `CHECK` `constraint` to the `orders` table requiring `amount > 0`, then attempt a transaction that inserts an order with `amount = -200.00`, and confirm it is rejected.

```postgresql with=orders_consistency.sql
-- Write your transaction below
```

If you run `ALTER TABLE orders ADD CONSTRAINT positive_amount CHECK (amount > 0);` followed by a transaction inserting `amount = -200.00`, the `INSERT` is rejected, the transaction commits nothing, and a closing `SELECT * FROM orders;` shows the table still empty.

## Conclusion

Consistency guarantees that a transaction can only ever move a database from one valid state to another, with every declared `constraint`, `CHECK`, `foreign key`, `NOT NULL`, or `UNIQUE`, acting as the database's own definition of what "valid" means, while business rules that were never expressed as a `constraint` remain the application's responsibility to protect. Rahul's banking data can now be trusted to never violate a rule the database actually knows about. Atomicity and consistency both concern a single transaction's own correctness; the next property addresses what happens when multiple transactions run at the same time.
