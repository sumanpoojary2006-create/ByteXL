"""6.1 - Transactions and ACID - Coding Questions (26: what a transaction is,
atomicity, consistency, isolation, durability).

Design exception to the single-RETURNING-statement convention used since
3.4: a transaction is inherently a multi-statement construct (BEGIN ...
COMMIT/ROLLBACK), and testing transaction semantics with a single statement
would defeat the purpose of the chapter. Every solution here is a short
script whose LAST statement is a plain SELECT (never RETURNING, since these
are BEGIN/COMMIT-wrapped scripts, not single INSERT/UPDATE/DELETE
statements); the graded output is that final SELECT's result, matching the
same "last statement is the graded one" assumption used throughout this
bank, now extended to a multi-statement script instead of a single one.

No solution ever executes a statement that would genuinely violate a CHECK
or FOREIGN KEY constraint, since a real constraint violation raises a hard
Postgres error and aborts the whole script before it reaches any final
SELECT -- there would be no gradeable output at all, and (per this bank's
standing rule) a coding question's target answer must be correct, working
SQL, never intentionally-broken SQL. Questions about atomicity/consistency
under constraint violations are instead framed as the positive case: valid
transactions that respect a constraint, or the constraint's own creation,
observed through a final confirming SELECT. The genuinely unobservable
parts of this chapter (crash survival, another session's concurrent view)
are not testable via SQL at all and are left to the MCQ bank, which already
covers them conceptually.

The accounts table used throughout carries an inline CHECK (balance >= 0)
constraint from the start (matching lesson 3's cleaner inline-constraint
style), rather than being added via a separate ALTER TABLE in each
question's solution.
"""
import decimal
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from dbms_cqlib import main, sql_insert

D = decimal.Decimal

TOPIC = "transactions-and-reliability"
WHAT_TOPIC = "what-is-a-transaction"
ATOMICITY_TOPIC = "atomicity-all-or-nothing"
CONSISTENCY_TOPIC = "consistency-valid-states-only"
ISOLATION_TOPIC = "isolation-running-transactions-safely-together"
DURABILITY_TOPIC = "durability-surviving-a-crash"

# ----------------------------- accounts dataset -----------------------------

ACCOUNT_COLUMNS = ["account_id", "owner_name", "balance"]
ACCOUNTS = [
    dict(account_id=1, owner_name="Meera Iyer", balance=D("50000.00")),
    dict(account_id=2, owner_name="Sanjay Rathi", balance=D("12000.00")),
]

ACCOUNTS_DDL = """
CREATE TABLE accounts (
    account_id INTEGER PRIMARY KEY,
    owner_name TEXT,
    balance NUMERIC(10, 2) CHECK (balance >= 0)
);
"""
ACCOUNTS_SQL = ACCOUNTS_DDL.strip("\n") + "\n\n" + sql_insert("accounts", ACCOUNT_COLUMNS, ACCOUNTS)
ACCOUNTS_SCHEMA_LINES = [
    "accounts(account_id INTEGER PK, owner_name TEXT, balance NUMERIC(10,2) CHECK (balance >= 0)) -- 2 rows",
]

# ----------------------------- customers/orders dataset (consistency lesson) -----------------------------

CUSTOMER_COLUMNS = ["customer_id", "customer_name"]
CUSTOMERS = [dict(customer_id=1, customer_name="Aditi Kulkarni")]

ORDER_COLUMNS = ["order_id", "customer_id", "amount"]

CUSTOMERS_DDL = """
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT
);
"""
ORDERS_DDL = """
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(customer_id),
    amount NUMERIC(10, 2) CHECK (amount > 0)
);
"""
CUSTOMERS_ORDERS_SQL = (
    CUSTOMERS_DDL.strip("\n") + "\n\n" + sql_insert("customers", CUSTOMER_COLUMNS, CUSTOMERS) + "\n\n"
    + ORDERS_DDL.strip("\n")
)
CUSTOMERS_ORDERS_SCHEMA_LINES = [
    "customers(customer_id INTEGER PK, customer_name TEXT) -- 1 row: Aditi Kulkarni",
    "orders(order_id INTEGER PK, customer_id INTEGER FK, amount NUMERIC(10,2) CHECK (amount > 0)) -- empty",
]

Q = []

# ==================== what-is-a-transaction ====================

Q.append(dict(
    title="Transfer 5000 From Meera to Sanjay", difficulty="Easy", topics=TOPIC, subTopics=WHAT_TOPIC,
    bloomTaxonomy="apply",
    prose="Move 5000.00 from Meera Iyer's account to Sanjay Rathi's account as a single "
          "transaction, and confirm both final balances.",
    schema_sql=ACCOUNTS_SQL, schema_lines=ACCOUNTS_SCHEMA_LINES,
    header=["account_id", "owner_name", "balance"],
    solution_sql="BEGIN;\n"
                 "UPDATE accounts SET balance = balance - 5000.00 WHERE account_id = 1;\n"
                 "UPDATE accounts SET balance = balance + 5000.00 WHERE account_id = 2;\n"
                 "COMMIT;\n\n"
                 "SELECT account_id, owner_name, balance FROM accounts ORDER BY account_id;",
    data=dict(),
    oracle=lambda: [(1, "Meera Iyer", D("45000.00")), (2, "Sanjay Rathi", D("17000.00"))],
    hints="BEGIN starts the transaction and COMMIT makes both UPDATE statements permanent "
          "together, as a single indivisible unit.",
))

Q.append(dict(
    title="Cancel a Transfer With ROLLBACK", difficulty="Medium", topics=TOPIC, subTopics=WHAT_TOPIC,
    bloomTaxonomy="analyze",
    prose="Meera wants to send 2000.00 to Sanjay, but decides midway through to cancel the "
          "transfer entirely. Perform both balance updates, then roll the whole transaction "
          "back, and confirm both balances are unchanged.",
    schema_sql=ACCOUNTS_SQL, schema_lines=ACCOUNTS_SCHEMA_LINES,
    header=["account_id", "owner_name", "balance"],
    solution_sql="BEGIN;\n"
                 "UPDATE accounts SET balance = balance - 2000.00 WHERE account_id = 1;\n"
                 "UPDATE accounts SET balance = balance + 2000.00 WHERE account_id = 2;\n"
                 "ROLLBACK;\n\n"
                 "SELECT account_id, owner_name, balance FROM accounts ORDER BY account_id;",
    data=dict(),
    oracle=lambda: [(1, "Meera Iyer", D("50000.00")), (2, "Sanjay Rathi", D("12000.00"))],
    hints="ROLLBACK discards every change made since BEGIN, as if the transaction had never "
          "happened; the final SELECT shows both accounts back at their original values.",
))

Q.append(dict(
    title="Transfer 3000 From Sanjay to Meera", difficulty="Medium", topics=TOPIC, subTopics=WHAT_TOPIC,
    bloomTaxonomy="apply",
    prose="Move 3000.00 from Sanjay Rathi's account to Meera Iyer's account as a single "
          "transaction, and confirm both final balances.",
    schema_sql=ACCOUNTS_SQL, schema_lines=ACCOUNTS_SCHEMA_LINES,
    header=["account_id", "owner_name", "balance"],
    solution_sql="BEGIN;\n"
                 "UPDATE accounts SET balance = balance - 3000.00 WHERE account_id = 2;\n"
                 "UPDATE accounts SET balance = balance + 3000.00 WHERE account_id = 1;\n"
                 "COMMIT;\n\n"
                 "SELECT account_id, owner_name, balance FROM accounts ORDER BY account_id;",
    data=dict(),
    oracle=lambda: [(1, "Meera Iyer", D("53000.00")), (2, "Sanjay Rathi", D("9000.00"))],
    hints="The same BEGIN/COMMIT pattern works regardless of which account debits and which "
          "credits.",
))

Q.append(dict(
    title="Cancel an 8000 Transfer With ROLLBACK", difficulty="Hard", topics=TOPIC, subTopics=WHAT_TOPIC,
    bloomTaxonomy="analyze",
    prose="Attempt to move 8000.00 from Meera to Sanjay, then cancel the whole transaction "
          "before it commits, and confirm both balances are unchanged.",
    schema_sql=ACCOUNTS_SQL, schema_lines=ACCOUNTS_SCHEMA_LINES,
    header=["account_id", "owner_name", "balance"],
    solution_sql="BEGIN;\n"
                 "UPDATE accounts SET balance = balance - 8000.00 WHERE account_id = 1;\n"
                 "UPDATE accounts SET balance = balance + 8000.00 WHERE account_id = 2;\n"
                 "ROLLBACK;\n\n"
                 "SELECT account_id, owner_name, balance FROM accounts ORDER BY account_id;",
    data=dict(),
    oracle=lambda: [(1, "Meera Iyer", D("50000.00")), (2, "Sanjay Rathi", D("12000.00"))],
    hints="It does not matter how large the attempted transfer was; ROLLBACK before COMMIT "
          "discards it completely regardless of amount.",
))

Q.append(dict(
    title="Transfer 10000 From Sanjay to Meera", difficulty="Hard", topics=TOPIC, subTopics=WHAT_TOPIC,
    bloomTaxonomy="apply",
    prose="Move 10000.00 from Sanjay's account to Meera's account as a single transaction, and "
          "confirm both final balances.",
    schema_sql=ACCOUNTS_SQL, schema_lines=ACCOUNTS_SCHEMA_LINES,
    header=["account_id", "owner_name", "balance"],
    solution_sql="BEGIN;\n"
                 "UPDATE accounts SET balance = balance - 10000.00 WHERE account_id = 2;\n"
                 "UPDATE accounts SET balance = balance + 10000.00 WHERE account_id = 1;\n"
                 "COMMIT;\n\n"
                 "SELECT account_id, owner_name, balance FROM accounts ORDER BY account_id;",
    data=dict(),
    oracle=lambda: [(1, "Meera Iyer", D("60000.00")), (2, "Sanjay Rathi", D("2000.00"))],
    hints="Sanjay's balance stays comfortably above zero here, so nothing about this transfer "
          "is close to any constraint boundary.",
))

Q.append(dict(
    title="Two Transfers in One Transaction", difficulty="Hard", topics=TOPIC, subTopics=WHAT_TOPIC,
    bloomTaxonomy="analyze",
    prose="A transaction is not limited to exactly two statements. Move 1000.00 from Meera to "
          "Sanjay, then move a further 500.00 the same direction, all inside one transaction, "
          "and confirm the combined final balances.",
    schema_sql=ACCOUNTS_SQL, schema_lines=ACCOUNTS_SCHEMA_LINES,
    header=["account_id", "owner_name", "balance"],
    solution_sql="BEGIN;\n"
                 "UPDATE accounts SET balance = balance - 1000.00 WHERE account_id = 1;\n"
                 "UPDATE accounts SET balance = balance + 1000.00 WHERE account_id = 2;\n"
                 "UPDATE accounts SET balance = balance - 500.00 WHERE account_id = 1;\n"
                 "UPDATE accounts SET balance = balance + 500.00 WHERE account_id = 2;\n"
                 "COMMIT;\n\n"
                 "SELECT account_id, owner_name, balance FROM accounts ORDER BY account_id;",
    data=dict(),
    oracle=lambda: [(1, "Meera Iyer", D("48500.00")), (2, "Sanjay Rathi", D("13500.00"))],
    hints="However many statements sit between BEGIN and COMMIT, they all commit together as "
          "one unit; four UPDATEs here behave exactly like two.",
))

# ==================== atomicity-all-or-nothing ====================

Q.append(dict(
    title="A Valid Transfer Within the Balance Constraint", difficulty="Easy", topics=TOPIC, subTopics=ATOMICITY_TOPIC,
    bloomTaxonomy="apply",
    prose="Move 3000.00 from Sanjay to Meera, a transfer that comfortably respects the "
          "balance_not_negative-style CHECK constraint on the accounts table, and confirm both "
          "final balances.",
    schema_sql=ACCOUNTS_SQL, schema_lines=ACCOUNTS_SCHEMA_LINES,
    header=["account_id", "balance"],
    solution_sql="BEGIN;\n"
                 "UPDATE accounts SET balance = balance - 3000.00 WHERE account_id = 2;\n"
                 "UPDATE accounts SET balance = balance + 3000.00 WHERE account_id = 1;\n"
                 "COMMIT;\n\n"
                 "SELECT account_id, balance FROM accounts ORDER BY account_id;",
    data=dict(),
    oracle=lambda: [(1, D("53000.00")), (2, D("9000.00"))],
    hints="As long as every statement in the transaction stays within what the CHECK constraint "
          "allows, the whole transaction commits together without any issue.",
))

Q.append(dict(
    title="Opening a New Account, Funded Atomically", difficulty="Medium", topics=TOPIC, subTopics=ATOMICITY_TOPIC,
    bloomTaxonomy="analyze",
    prose="Open a new account for Farah Ali (account_id 3, starting balance 0.00) and fund it "
          "with 1000.00 taken from Meera's account, all three statements acting as one atomic "
          "unit, then confirm every account's final balance.",
    schema_sql=ACCOUNTS_SQL, schema_lines=ACCOUNTS_SCHEMA_LINES,
    header=["account_id", "owner_name", "balance"],
    solution_sql="BEGIN;\n"
                 "INSERT INTO accounts (account_id, owner_name, balance) VALUES (3, 'Farah Ali', 0.00);\n"
                 "UPDATE accounts SET balance = balance - 1000.00 WHERE account_id = 1;\n"
                 "UPDATE accounts SET balance = balance + 1000.00 WHERE account_id = 3;\n"
                 "COMMIT;\n\n"
                 "SELECT account_id, owner_name, balance FROM accounts ORDER BY account_id;",
    data=dict(),
    oracle=lambda: [
        (1, "Meera Iyer", D("49000.00")),
        (2, "Sanjay Rathi", D("12000.00")),
        (3, "Farah Ali", D("1000.00")),
    ],
    hints="INSERT and UPDATE statements can sit in the same transaction together; all three "
          "commit as one unit, exactly like a two-statement transfer.",
))

Q.append(dict(
    title="Opening a New Account, Funded From Sanjay", difficulty="Medium", topics=TOPIC, subTopics=ATOMICITY_TOPIC,
    bloomTaxonomy="analyze",
    prose="Open a new account for Kabir Oberoi (account_id 4, starting balance 0.00) and fund it "
          "with 2000.00 taken from Sanjay's account, all in one transaction, then confirm every "
          "account's final balance.",
    schema_sql=ACCOUNTS_SQL, schema_lines=ACCOUNTS_SCHEMA_LINES,
    header=["account_id", "owner_name", "balance"],
    solution_sql="BEGIN;\n"
                 "INSERT INTO accounts (account_id, owner_name, balance) VALUES (4, 'Kabir Oberoi', 0.00);\n"
                 "UPDATE accounts SET balance = balance - 2000.00 WHERE account_id = 2;\n"
                 "UPDATE accounts SET balance = balance + 2000.00 WHERE account_id = 4;\n"
                 "COMMIT;\n\n"
                 "SELECT account_id, owner_name, balance FROM accounts ORDER BY account_id;",
    data=dict(),
    oracle=lambda: [
        (1, "Meera Iyer", D("50000.00")),
        (2, "Sanjay Rathi", D("10000.00")),
        (4, "Kabir Oberoi", D("2000.00")),
    ],
    hints="Meera's balance is untouched here, since this particular transaction never references "
          "account_id 1 at all.",
))

Q.append(dict(
    title="Sanjay Sends His Comfortable Margin to Meera", difficulty="Hard", topics=TOPIC, subTopics=ATOMICITY_TOPIC,
    bloomTaxonomy="apply",
    prose="Move 5000.00 from Sanjay to Meera, leaving Sanjay with a healthy remaining balance "
          "well clear of the CHECK constraint's boundary, and confirm both final balances.",
    schema_sql=ACCOUNTS_SQL, schema_lines=ACCOUNTS_SCHEMA_LINES,
    header=["account_id", "balance"],
    solution_sql="BEGIN;\n"
                 "UPDATE accounts SET balance = balance - 5000.00 WHERE account_id = 2;\n"
                 "UPDATE accounts SET balance = balance + 5000.00 WHERE account_id = 1;\n"
                 "COMMIT;\n\n"
                 "SELECT account_id, balance FROM accounts ORDER BY account_id;",
    data=dict(),
    oracle=lambda: [(1, D("55000.00")), (2, D("7000.00"))],
    hints="Sanjay's remaining balance, 7000.00, comfortably satisfies balance >= 0, so both "
          "statements succeed and commit together.",
))

Q.append(dict(
    title="Sanjay Empties His Account to Exactly Zero", difficulty="Hard", topics=TOPIC, subTopics=ATOMICITY_TOPIC,
    bloomTaxonomy="analyze",
    prose="Move Sanjay's entire 12000.00 balance to Meera, leaving Sanjay at exactly 0.00, the "
          "boundary the CHECK constraint allows (balance >= 0, not balance > 0), and confirm "
          "both final balances.",
    schema_sql=ACCOUNTS_SQL, schema_lines=ACCOUNTS_SCHEMA_LINES,
    header=["account_id", "balance"],
    solution_sql="BEGIN;\n"
                 "UPDATE accounts SET balance = balance - 12000.00 WHERE account_id = 2;\n"
                 "UPDATE accounts SET balance = balance + 12000.00 WHERE account_id = 1;\n"
                 "COMMIT;\n\n"
                 "SELECT account_id, balance FROM accounts ORDER BY account_id;",
    data=dict(),
    oracle=lambda: [(1, D("62000.00")), (2, D("0.00"))],
    hints="balance >= 0 explicitly allows exactly zero, so this transaction, right at the "
          "boundary, still commits successfully rather than being rejected.",
))

# ==================== consistency-valid-states-only ====================

Q.append(dict(
    title="Accounts Still Satisfy the Balance Constraint", difficulty="Easy", topics=TOPIC, subTopics=CONSISTENCY_TOPIC,
    bloomTaxonomy="understand",
    prose="Confirm that the existing account data satisfies the CHECK (balance >= 0) constraint "
          "that defines a valid account row, by simply reading the current balances.",
    schema_sql=ACCOUNTS_SQL, schema_lines=ACCOUNTS_SCHEMA_LINES,
    header=["account_id", "balance"],
    solution_sql="SELECT account_id, balance FROM accounts ORDER BY account_id;",
    data=dict(),
    oracle=lambda: [(1, D("50000.00")), (2, D("12000.00"))],
    hints="Both stored balances are non-negative, so both rows already satisfy the constraint "
          "that defines what a valid account row looks like.",
))

Q.append(dict(
    title="A Valid Order Referencing a Real Customer", difficulty="Medium", topics=TOPIC, subTopics=CONSISTENCY_TOPIC,
    bloomTaxonomy="apply",
    prose="Insert an order for Aditi Kulkarni (customer_id 1, a customer who genuinely exists) "
          "worth 500.00, respecting the foreign key that defines a valid order, and confirm it "
          "landed.",
    schema_sql=CUSTOMERS_ORDERS_SQL, schema_lines=CUSTOMERS_ORDERS_SCHEMA_LINES,
    header=["order_id", "customer_id", "amount"],
    solution_sql="INSERT INTO orders (order_id, customer_id, amount) VALUES (1, 1, 500.00);\n\n"
                 "SELECT order_id, customer_id, amount FROM orders ORDER BY order_id;",
    data=dict(),
    oracle=lambda: [(1, 1, D("500.00"))],
    hints="The foreign key on orders.customer_id only allows values that already exist in "
          "customers; customer_id 1 genuinely exists, so this insert succeeds cleanly.",
))

Q.append(dict(
    title="An Order Respecting the Positive-Amount Constraint", difficulty="Medium", topics=TOPIC, subTopics=CONSISTENCY_TOPIC,
    bloomTaxonomy="apply",
    prose="Insert a second order for Aditi Kulkarni worth 750.00, respecting the CHECK (amount > "
          "0) constraint already defined on the orders table, and confirm both orders on file.",
    schema_sql=CUSTOMERS_ORDERS_SQL, schema_lines=CUSTOMERS_ORDERS_SCHEMA_LINES,
    header=["order_id", "customer_id", "amount"],
    solution_sql="INSERT INTO orders (order_id, customer_id, amount) VALUES (1, 1, 500.00);\n"
                 "INSERT INTO orders (order_id, customer_id, amount) VALUES (2, 1, 750.00);\n\n"
                 "SELECT order_id, customer_id, amount FROM orders ORDER BY order_id;",
    data=dict(),
    oracle=lambda: [(1, 1, D("500.00")), (2, 1, D("750.00"))],
    hints="Both 500.00 and 750.00 satisfy amount > 0, so both inserts succeed and both rows "
          "appear in the final result.",
))

Q.append(dict(
    title="A Balanced Transfer Preserves the Bank's Total", difficulty="Hard", topics=TOPIC, subTopics=CONSISTENCY_TOPIC,
    bloomTaxonomy="analyze",
    prose="A business rule the database was never told about as a constraint is that total "
          "money across all accounts should never change from an internal transfer. Move "
          "4000.00 from Meera to Sanjay as a single transaction, then confirm the total money "
          "in the bank is exactly the same as before.",
    schema_sql=ACCOUNTS_SQL, schema_lines=ACCOUNTS_SCHEMA_LINES,
    header=["total_money_in_bank"],
    solution_sql="BEGIN;\n"
                 "UPDATE accounts SET balance = balance - 4000.00 WHERE account_id = 1;\n"
                 "UPDATE accounts SET balance = balance + 4000.00 WHERE account_id = 2;\n"
                 "COMMIT;\n\n"
                 "SELECT SUM(balance) AS total_money_in_bank FROM accounts;",
    data=dict(),
    oracle=lambda: [(D("62000.00"),)],
    hints="Grouping both halves of the transfer into one transaction is what keeps this "
          "business-level total constant, even though no CHECK constraint enforces that rule "
          "directly.",
))

Q.append(dict(
    title="Two Customers, Each With a Valid Order", difficulty="Hard", topics=TOPIC, subTopics=CONSISTENCY_TOPIC,
    bloomTaxonomy="analyze",
    prose="Add a second customer, Rohan Das (customer_id 2), then insert one order for each "
          "customer, and confirm both orders join cleanly back to their real customers.",
    schema_sql=CUSTOMERS_ORDERS_SQL, schema_lines=CUSTOMERS_ORDERS_SCHEMA_LINES,
    header=["order_id", "customer_name", "amount"],
    solution_sql="INSERT INTO customers (customer_id, customer_name) VALUES (2, 'Rohan Das');\n"
                 "INSERT INTO orders (order_id, customer_id, amount) VALUES (1, 1, 500.00);\n"
                 "INSERT INTO orders (order_id, customer_id, amount) VALUES (2, 2, 300.00);\n\n"
                 "SELECT o.order_id, c.customer_name, o.amount\n"
                 "FROM orders o JOIN customers c ON o.customer_id = c.customer_id\n"
                 "ORDER BY o.order_id;",
    data=dict(),
    oracle=lambda: [(1, "Aditi Kulkarni", D("500.00")), (2, "Rohan Das", D("300.00"))],
    hints="Consistently valid foreign-key data always joins cleanly back to its referenced "
          "table; there is no order here left dangling without a real customer behind it.",
))

# ==================== isolation-running-transactions-safely-together ====================

Q.append(dict(
    title="Checking the Current Isolation Level", difficulty="Easy", topics=TOPIC, subTopics=ISOLATION_TOPIC,
    bloomTaxonomy="remember",
    prose="Check the transaction isolation level this session is using.",
    schema_sql=ACCOUNTS_SQL, schema_lines=ACCOUNTS_SCHEMA_LINES,
    header=["transaction_isolation"],
    solution_sql="SHOW transaction_isolation;",
    data=dict(),
    oracle=lambda: [("read committed",)],
    hints="PostgreSQL defaults to read committed, which already guarantees a transaction never "
          "sees another transaction's uncommitted changes.",
))

Q.append(dict(
    title="A Transaction Sees Its Own Uncommitted Change", difficulty="Medium", topics=TOPIC, subTopics=ISOLATION_TOPIC,
    bloomTaxonomy="analyze",
    prose="Reduce Meera's balance by 5000.00 inside a transaction, and, before committing, "
          "confirm the reduced balance is already visible within that same transaction.",
    schema_sql=ACCOUNTS_SQL, schema_lines=ACCOUNTS_SCHEMA_LINES,
    header=["balance"],
    solution_sql="BEGIN;\n"
                 "UPDATE accounts SET balance = balance - 5000.00 WHERE account_id = 1;\n"
                 "SELECT balance FROM accounts WHERE account_id = 1;",
    data=dict(),
    oracle=lambda: [(D("45000.00"),)],
    hints="Isolation is not about hiding a transaction's work from itself; a transaction always "
          "sees its own uncommitted changes, even before COMMIT runs.",
))

Q.append(dict(
    title="Sanjay's Balance, Visible Mid-Transaction", difficulty="Medium", topics=TOPIC, subTopics=ISOLATION_TOPIC,
    bloomTaxonomy="analyze",
    prose="Increase Sanjay's balance by 1000.00 inside a transaction, and, before committing, "
          "confirm the increased balance is already visible within that same transaction.",
    schema_sql=ACCOUNTS_SQL, schema_lines=ACCOUNTS_SCHEMA_LINES,
    header=["balance"],
    solution_sql="BEGIN;\n"
                 "UPDATE accounts SET balance = balance + 1000.00 WHERE account_id = 2;\n"
                 "SELECT balance FROM accounts WHERE account_id = 2;",
    data=dict(),
    oracle=lambda: [(D("13000.00"),)],
    hints="The same visibility guarantee applies regardless of which account or which direction "
          "the change moves in.",
))

Q.append(dict(
    title="A Change Becomes Visible Everywhere Only After COMMIT", difficulty="Hard", topics=TOPIC, subTopics=ISOLATION_TOPIC,
    bloomTaxonomy="analyze",
    prose="Move 5000.00 from Meera to Sanjay, commit the transaction, then confirm both "
          "balances, now genuinely permanent and visible to any session, not just the one that "
          "made the change.",
    schema_sql=ACCOUNTS_SQL, schema_lines=ACCOUNTS_SCHEMA_LINES,
    header=["account_id", "balance"],
    solution_sql="BEGIN;\n"
                 "UPDATE accounts SET balance = balance - 5000.00 WHERE account_id = 1;\n"
                 "UPDATE accounts SET balance = balance + 5000.00 WHERE account_id = 2;\n"
                 "COMMIT;\n\n"
                 "SELECT account_id, balance FROM accounts ORDER BY account_id;",
    data=dict(),
    oracle=lambda: [(1, D("45000.00")), (2, D("17000.00"))],
    hints="Before COMMIT, a concurrent session would still see the old balances; only once COMMIT "
          "actually runs does the change become visible to every session, including brand new "
          "ones.",
))

Q.append(dict(
    title="Two Stacked Uncommitted Changes, Both Visible", difficulty="Hard", topics=TOPIC, subTopics=ISOLATION_TOPIC,
    bloomTaxonomy="analyze",
    prose="Reduce Meera's balance by 2000.00, then by a further 1000.00, both inside the same "
          "still-open transaction, and confirm the cumulative effect of both uncommitted changes "
          "is already visible within that transaction.",
    schema_sql=ACCOUNTS_SQL, schema_lines=ACCOUNTS_SCHEMA_LINES,
    header=["balance"],
    solution_sql="BEGIN;\n"
                 "UPDATE accounts SET balance = balance - 2000.00 WHERE account_id = 1;\n"
                 "UPDATE accounts SET balance = balance - 1000.00 WHERE account_id = 1;\n"
                 "SELECT balance FROM accounts WHERE account_id = 1;",
    data=dict(),
    oracle=lambda: [(D("47000.00"),)],
    hints="A transaction sees every one of its own changes stacked together, not just the most "
          "recent one; both UPDATE statements' effects are already reflected before any COMMIT.",
))

# ==================== durability-surviving-a-crash ====================

Q.append(dict(
    title="Checking the Synchronous Commit Setting", difficulty="Easy", topics=TOPIC, subTopics=DURABILITY_TOPIC,
    bloomTaxonomy="remember",
    prose="Check this session's synchronous_commit setting, the one that controls whether COMMIT "
          "waits for its change to be safely recorded before reporting success.",
    schema_sql=ACCOUNTS_SQL, schema_lines=ACCOUNTS_SCHEMA_LINES,
    header=["synchronous_commit"],
    solution_sql="SHOW synchronous_commit;",
    data=dict(),
    oracle=lambda: [("on",)],
    hints="The default value, on, means every COMMIT waits until its change is safely recorded "
          "before reporting success, the full durability guarantee.",
))

Q.append(dict(
    title="A Committed Transfer Is Permanent", difficulty="Medium", topics=TOPIC, subTopics=DURABILITY_TOPIC,
    bloomTaxonomy="analyze",
    prose="Move 6000.00 from Sanjay to Meera, commit the transaction, and confirm both final "
          "balances, values durability guarantees would survive even a crash the instant after "
          "COMMIT returned.",
    schema_sql=ACCOUNTS_SQL, schema_lines=ACCOUNTS_SCHEMA_LINES,
    header=["account_id", "balance"],
    solution_sql="BEGIN;\n"
                 "UPDATE accounts SET balance = balance - 6000.00 WHERE account_id = 2;\n"
                 "UPDATE accounts SET balance = balance + 6000.00 WHERE account_id = 1;\n"
                 "COMMIT;\n\n"
                 "SELECT account_id, balance FROM accounts ORDER BY account_id;",
    data=dict(),
    oracle=lambda: [(1, D("56000.00")), (2, D("6000.00"))],
    hints="Once COMMIT finishes, durability guarantees this new balance is already recorded "
          "somewhere that survives a crash, not sitting only in memory waiting to be lost.",
))

Q.append(dict(
    title="Crediting Sanjay's Account, Durably", difficulty="Hard", topics=TOPIC, subTopics=DURABILITY_TOPIC,
    bloomTaxonomy="apply",
    prose="Add 500.00 to Sanjay's balance in a committed transaction, and confirm the result, "
          "reasoning through why that value would still hold even if the server crashed the "
          "instant after COMMIT returned.",
    schema_sql=ACCOUNTS_SQL, schema_lines=ACCOUNTS_SCHEMA_LINES,
    header=["balance"],
    solution_sql="BEGIN;\n"
                 "UPDATE accounts SET balance = balance + 500.00 WHERE account_id = 2;\n"
                 "COMMIT;\n\n"
                 "SELECT balance FROM accounts WHERE account_id = 2;",
    data=dict(),
    oracle=lambda: [(D("12500.00"),)],
    hints="COMMIT would not have returned successfully until the change was already recorded "
          "somewhere a crash cannot erase, which is exactly why durability lets this result be "
          "trusted unconditionally.",
))

Q.append(dict(
    title="A Larger Committed Transfer Survives Just as Durably", difficulty="Hard", topics=TOPIC, subTopics=DURABILITY_TOPIC,
    bloomTaxonomy="apply",
    prose="Move 15000.00 from Meera to Sanjay, commit the transaction, and confirm both final "
          "balances, permanent the moment COMMIT succeeds regardless of the transfer's size.",
    schema_sql=ACCOUNTS_SQL, schema_lines=ACCOUNTS_SCHEMA_LINES,
    header=["account_id", "balance"],
    solution_sql="BEGIN;\n"
                 "UPDATE accounts SET balance = balance - 15000.00 WHERE account_id = 1;\n"
                 "UPDATE accounts SET balance = balance + 15000.00 WHERE account_id = 2;\n"
                 "COMMIT;\n\n"
                 "SELECT account_id, balance FROM accounts ORDER BY account_id;",
    data=dict(),
    oracle=lambda: [(1, D("35000.00")), (2, D("27000.00"))],
    hints="Durability makes no distinction based on the size of a committed change; a 15000.00 "
          "transfer is exactly as permanent, once committed, as a 500.00 one.",
))

assert len(Q) == 25, len(Q)

for q in Q:
    q["tags"] = f"dbms - {q['subTopics']}"

OUT = "content/Question Bank/Coding Questions/DBMS/6.1 - Transactions and ACID - Coding Questions.xlsx"

if __name__ == "__main__":
    main(Q, OUT)
