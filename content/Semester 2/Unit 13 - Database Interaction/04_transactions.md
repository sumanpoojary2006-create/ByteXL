## Introduction

A library member returns a book and immediately borrows another. Dev's code updates the `copies` count in two separate SQL statements. Halfway through the second update, the process crashes. The returned copy was added back, but the new loan was never recorded. The database now shows more copies than actually exist.

Transactions prevent this class of bug. A transaction groups multiple SQL statements into a single atomic unit: either every statement succeeds and the changes are committed, or a failure rolls back all of them as if none ran.

![Two operations (return book, borrow book) wrapped in a transaction: if step 2 fails, step 1 is also undone, leaving the database in its original clean state](images/04_transactions.md.png)

## The ACID Properties

Every database transaction follows four guarantees:

```python
# Illustrate ACID properties as a data structure
acid = {
    "Atomic":    "All statements in the transaction succeed, or none do",
    "Consistent":"The database moves from one valid state to another valid state",
    "Isolated":  "Concurrent transactions do not see each other's partial writes",
    "Durable":   "A committed transaction survives a crash or power failure",
}

for prop, meaning in acid.items():
    print(f"{prop:12s}: {meaning}")
```

## The Default sqlite3 Transaction Mode

By default, `sqlite3` operates in a deferred transaction mode. Changes are not written to disk until you call `conn.commit()`. If you close the connection without committing, the changes are lost.

```python
import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("CREATE TABLE accounts (name TEXT PRIMARY KEY, balance INTEGER)")
cursor.execute("INSERT INTO accounts VALUES ('Library Fund', 1000)")
conn.commit()

# Simulate a change that we decide to undo
cursor.execute("UPDATE accounts SET balance = balance - 500 WHERE name = 'Library Fund'")

cursor.execute("SELECT balance FROM accounts WHERE name = 'Library Fund'")
balance_before_rollback = cursor.fetchone()[0]
print(f"Balance after UPDATE (not committed): {balance_before_rollback}")

# Roll back -- the UPDATE never happened
conn.rollback()

cursor.execute("SELECT balance FROM accounts WHERE name = 'Library Fund'")
balance_after_rollback = cursor.fetchone()[0]
print(f"Balance after ROLLBACK: {balance_after_rollback}")

conn.close()
```

`rollback()` discards all uncommitted changes. The database returns to the state it was in at the last `commit()`.

## A Real Transaction: Loan Processing

```python
import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE books (
    isbn TEXT PRIMARY KEY, title TEXT, copies INTEGER
)""")
cursor.execute("""CREATE TABLE loans (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    isbn TEXT, member TEXT, loan_date TEXT
)""")
cursor.execute("INSERT INTO books VALUES ('978-0-13-235088-4', 'Clean Code', 2)")
conn.commit()

def borrow_book(isbn, member):
    try:
        # Check availability
        cursor.execute("SELECT copies FROM books WHERE isbn = ?", (isbn,))
        row = cursor.fetchone()
        if row is None:
            raise ValueError(f"Book {isbn} not found")
        if row[0] < 1:
            raise ValueError("No copies available")

        # Deduct one copy
        cursor.execute("UPDATE books SET copies = copies - 1 WHERE isbn = ?", (isbn,))

        # Record the loan
        cursor.execute(
            "INSERT INTO loans (isbn, member, loan_date) VALUES (?, ?, date('now'))",
            (isbn, member),
        )

        conn.commit()
        print(f"Loan recorded: '{member}' borrowed {isbn}")
    except Exception as e:
        conn.rollback()
        print(f"Transaction rolled back: {e}")

borrow_book("978-0-13-235088-4", "Alice")
borrow_book("978-0-13-235088-4", "Bob")
borrow_book("978-0-13-235088-4", "Carol")   # should fail: 0 copies left

cursor.execute("SELECT isbn, copies FROM books")
print("\nBook copies remaining:", cursor.fetchall())

cursor.execute("SELECT member, loan_date FROM loans")
print("Active loans:", cursor.fetchall())

conn.close()
```

The pattern is: `try` the multi-step operation, `commit()` on success, `rollback()` on any exception. The database never lands in a half-updated state.

## Using a Context Manager (Recommended)

The `sqlite3.connect` object can be used as a context manager. It commits on clean exit and rolls back on exception:

```python
import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("CREATE TABLE books (isbn TEXT PRIMARY KEY, title TEXT, copies INTEGER)")
cursor.execute("INSERT INTO books VALUES ('978-0-13-235088-4', 'Clean Code', 3)")
conn.commit()

# The 'with conn' block auto-commits on exit, auto-rollbacks on exception
try:
    with conn:
        conn.execute("UPDATE books SET copies = copies - 1 WHERE isbn = ?",
                     ("978-0-13-235088-4",))
        conn.execute("INSERT INTO loans_log VALUES ('borrow', '978-0-13-235088-4')")
        # If loans_log does not exist, the exception triggers rollback
except Exception as e:
    print(f"Rolled back due to: {e}")

cursor.execute("SELECT copies FROM books WHERE isbn = '978-0-13-235088-4'")
print("Copies after attempted transaction:", cursor.fetchone()[0])
conn.close()
```

The `with conn:` block is the cleanest pattern for transactions. No manual `commit` or `rollback` calls needed.

## Savepoints for Partial Rollback

For complex workflows, SQLite supports savepoints: named checkpoints within a transaction that you can roll back to without undoing the entire transaction.

```python
import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("CREATE TABLE log (msg TEXT)")
conn.commit()

cursor.execute("BEGIN")
cursor.execute("INSERT INTO log VALUES ('step 1 -- always keep')")

cursor.execute("SAVEPOINT sp1")
cursor.execute("INSERT INTO log VALUES ('step 2 -- might fail')")

# Simulate a failure at step 2
try:
    raise ValueError("Step 2 failed")
except ValueError:
    cursor.execute("ROLLBACK TO SAVEPOINT sp1")
    print("Rolled back to savepoint -- step 1 preserved")

cursor.execute("INSERT INTO log VALUES ('step 3 -- recovery')")
conn.commit()

cursor.execute("SELECT msg FROM log")
print("Log entries after partial rollback:")
for row in cursor.fetchall():
    print(" ", row[0])

conn.close()
```

## Transactions at a Glance

| Concept | What it means |
|---|---|
| `conn.commit()` | Write all pending changes to disk |
| `conn.rollback()` | Discard all pending changes |
| `with conn:` | Auto-commit on success, auto-rollback on exception |
| Savepoint | Named checkpoint inside a transaction for partial rollback |
| ACID | Atomic, Consistent, Isolated, Durable |

## Your Turn

Write a `return_book(isbn, member_id)` function that:
1. Deletes the loan record for that member and book
2. Increments the copy count in the books table
3. Wraps both steps in a transaction so either both happen or neither does

Test it by calling it after `borrow_book` from the lesson above, and confirm the copy count returns to the original value.

## Conclusion

Transactions group multiple SQL statements into a single atomic unit. `commit()` persists the group; `rollback()` discards it. The `with conn:` context manager handles both automatically. No multi-step database operation should run without a transaction. The next lesson covers the row factory, which makes query results easier to work with by returning dictionaries instead of bare tuples.
