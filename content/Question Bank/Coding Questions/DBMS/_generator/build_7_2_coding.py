"""7.2 - Indexes - Coding Questions (23: what an index is, B-tree indexes,
hash/composite/partial/expression indexes, covering indexes, and the cost of
overindexing).

Scope note: this lesson is heavily about EXPLAIN plan output and physical
storage sizes (pg_relation_size), neither of which is reliably gradeable via
fixed-output comparison -- EXPLAIN's cost estimates and exact plan text
depend on the live planner/statistics, not something reproducible without a
real Postgres server. Every question here is instead built around CREATE
INDEX statements paired with a query whose RETURNED DATA is correct
regardless of whether the planner actually chooses to use that index (row
correctness never depends on the physical access path). Where a question
needs to confirm an index exists, it checks pg_indexes.indexname only, never
indexdef's reconstructed definition text, since PostgreSQL's catalog
deparser has real formatting subtleties (schema-qualification, explicit
type casts in WHERE clauses, function name casing) this bank cannot verify
without a live server.

The orders table used throughout is a small, hand-verifiable 12-row dataset
(not the 10000+ row generated tables the lesson uses to make EXPLAIN
differences visible), since row count doesn't affect data correctness for
any question here.
"""
import decimal
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from dbms_cqlib import main, sql_insert

D = decimal.Decimal

TOPIC = "performance"
WHAT_TOPIC = "what-is-an-index"
BTREE_TOPIC = "btree-indexes"
VARIANT_TOPIC = "hash-composite-partial-and-expression-indexes"
COVERING_TOPIC = "covering-indexes-and-index-only-scans"
OVERINDEX_TOPIC = "when-not-to-index-the-cost-of-overindexing"

ORDER_COLUMNS = ["order_id", "customer_name", "status", "region", "amount"]
ORDERS = [
    dict(order_id=1, customer_name="Customer 1", status="completed", region="North", amount=D("100.00")),
    dict(order_id=2, customer_name="Customer 2", status="active", region="North", amount=D("250.00")),
    dict(order_id=3, customer_name="Customer 3", status="completed", region="South", amount=D("75.00")),
    dict(order_id=4, customer_name="Customer 4", status="cancelled", region="South", amount=D("500.00")),
    dict(order_id=5, customer_name="Customer 5", status="completed", region="East", amount=D("300.00")),
    dict(order_id=6, customer_name="Customer 6", status="active", region="East", amount=D("150.00")),
    dict(order_id=7, customer_name="Customer 7", status="completed", region="West", amount=D("620.00")),
    dict(order_id=8, customer_name="Customer 8", status="cancelled", region="West", amount=D("90.00")),
    dict(order_id=9, customer_name="Customer 9", status="active", region="North", amount=D("410.00")),
    dict(order_id=10, customer_name="Customer 10", status="completed", region="South", amount=D("220.00")),
    dict(order_id=11, customer_name="Customer 11", status="completed", region="North", amount=D("999.00")),
    dict(order_id=12, customer_name="Customer 12", status="active", region="South", amount=D("45.00")),
]

ORDERS_DDL = """
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    status TEXT,
    region TEXT,
    amount NUMERIC(10, 2)
);
"""
ORDERS_SQL = ORDERS_DDL.strip("\n") + "\n\n" + sql_insert("orders", ORDER_COLUMNS, ORDERS)
ORDERS_SCHEMA_LINES = [
    "orders(order_id INTEGER PK, customer_name TEXT, status TEXT, region TEXT, amount NUMERIC(10,2)) -- 12 rows",
]

Q = []

# ==================== what-is-an-index ====================

Q.append(dict(
    title="Creating an Index and Confirming It Exists", difficulty="Easy", topics=TOPIC, subTopics=WHAT_TOPIC,
    bloomTaxonomy="apply",
    prose="Create an index on customer_name, then confirm it now appears among the table's "
          "indexes.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["indexname"],
    solution_sql="CREATE INDEX idx_orders_customer_name ON orders (customer_name);\n\n"
                 "SELECT indexname FROM pg_indexes\n"
                 "WHERE tablename = 'orders' AND indexname = 'idx_orders_customer_name';",
    data=dict(),
    oracle=lambda: [("idx_orders_customer_name",)],
    hints="CREATE INDEX builds a separate structure without physically reordering the table; "
          "pg_indexes lists every index that currently exists on a table.",
))

Q.append(dict(
    title="Looking Up an Order by Amount", difficulty="Easy", topics=TOPIC, subTopics=WHAT_TOPIC,
    bloomTaxonomy="apply",
    prose="Create an index on amount, then find the order whose amount is exactly 250.00.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["order_id", "customer_name", "amount"],
    solution_sql="CREATE INDEX idx_orders_amount ON orders (amount);\n\n"
                 "SELECT order_id, customer_name, amount FROM orders WHERE amount = 250.00;",
    data=dict(),
    oracle=lambda: [(o["order_id"], o["customer_name"], o["amount"]) for o in ORDERS if o["amount"] == D("250.00")],
    hints="An index lets the database jump directly to matching rows, but the returned data is "
          "identical whether or not the planner actually chooses to use the index.",
))

Q.append(dict(
    title="Confirming Two Custom Indexes Exist", difficulty="Medium", topics=TOPIC, subTopics=WHAT_TOPIC,
    bloomTaxonomy="apply",
    prose="Create an index on customer_name and a separate index on amount, then list both "
          "custom index names, alphabetically.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["indexname"],
    solution_sql="CREATE INDEX idx_orders_customer_name ON orders (customer_name);\n"
                 "CREATE INDEX idx_orders_amount ON orders (amount);\n\n"
                 "SELECT indexname FROM pg_indexes\n"
                 "WHERE tablename = 'orders' AND indexname LIKE 'idx_%'\n"
                 "ORDER BY indexname;",
    data=dict(),
    oracle=lambda: [("idx_orders_amount",), ("idx_orders_customer_name",)],
    hints="Filtering with indexname LIKE 'idx_%' excludes the table's automatic primary-key "
          "index, showing only the two custom ones just created.",
))

Q.append(dict(
    title="Looking Up an Order by a Specific Amount", difficulty="Hard", topics=TOPIC, subTopics=WHAT_TOPIC,
    bloomTaxonomy="apply",
    prose="Create an index on amount, then find the order whose amount is exactly 410.00.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["order_id", "customer_name"],
    solution_sql="CREATE INDEX idx_orders_amount ON orders (amount);\n\n"
                 "SELECT order_id, customer_name FROM orders WHERE amount = 410.00;",
    data=dict(),
    oracle=lambda: [(o["order_id"], o["customer_name"]) for o in ORDERS if o["amount"] == D("410.00")],
    hints="The database can now look up matching rows through the sorted index instead of "
          "checking every row directly, though the query's actual result never depends on that "
          "choice.",
))

# ==================== btree-indexes ====================

Q.append(dict(
    title="Looking Up the Highest-Priced Order Directly", difficulty="Easy", topics=TOPIC, subTopics=BTREE_TOPIC,
    bloomTaxonomy="apply",
    prose="Create an index on amount, then find the single order with the exact amount 999.00.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["order_id", "customer_name", "status"],
    solution_sql="CREATE INDEX idx_orders_amount ON orders (amount);\n\n"
                 "SELECT order_id, customer_name, status FROM orders WHERE amount = 999.00;",
    data=dict(),
    oracle=lambda: [(o["order_id"], o["customer_name"], o["status"]) for o in ORDERS if o["amount"] == D("999.00")],
    hints="A B-tree is PostgreSQL's default index type, created automatically whenever a type "
          "is not specified.",
))

Q.append(dict(
    title="Orders in a Mid-Range Amount Band", difficulty="Medium", topics=TOPIC, subTopics=BTREE_TOPIC,
    bloomTaxonomy="analyze",
    prose="A B-tree's sorted leaf level naturally supports range conditions. Find every order "
          "with an amount between 100.00 and 300.00 inclusive, sorted from smallest to largest.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["order_id", "customer_name", "amount"],
    solution_sql="SELECT order_id, customer_name, amount FROM orders\n"
                 "WHERE amount BETWEEN 100.00 AND 300.00\n"
                 "ORDER BY amount;",
    data=dict(),
    oracle=lambda: sorted(
        [(o["order_id"], o["customer_name"], o["amount"]) for o in ORDERS if D("100.00") <= o["amount"] <= D("300.00")],
        key=lambda row: row[2],
    ),
    hints="A range query and its sort can both use the same B-tree, since matching values sit "
          "consecutively at the sorted leaf level.",
))

Q.append(dict(
    title="The Single Largest Order Amount", difficulty="Medium", topics=TOPIC, subTopics=BTREE_TOPIC,
    bloomTaxonomy="apply",
    prose="A B-tree's sorted structure also supports finding the minimum or maximum value "
          "directly. Find the largest order amount in the table.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["highest_order"],
    solution_sql="SELECT MAX(amount) AS highest_order FROM orders;",
    data=dict(),
    oracle=lambda: [(max(o["amount"] for o in ORDERS),)],
    hints="A B-tree can jump straight to the far end of its sorted leaf level to answer a MAX "
          "query, rather than comparing every row's value.",
))

Q.append(dict(
    title="Orders Above a Narrow High-End Threshold", difficulty="Hard", topics=TOPIC, subTopics=BTREE_TOPIC,
    bloomTaxonomy="analyze",
    prose="Find every order with an amount greater than 600.00, a condition only a few of the "
          "highest-priced orders satisfy, sorted from smallest to largest.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["order_id", "customer_name", "amount"],
    solution_sql="SELECT order_id, customer_name, amount FROM orders\n"
                 "WHERE amount > 600.00\n"
                 "ORDER BY amount;",
    data=dict(),
    oracle=lambda: sorted(
        [(o["order_id"], o["customer_name"], o["amount"]) for o in ORDERS if o["amount"] > D("600.00")],
        key=lambda row: row[2],
    ),
    hints="A narrow range like this is exactly the situation a B-tree index is best at: walking "
          "to the start of the range and reading forward, rather than checking every row.",
))

# ==================== hash-composite-partial-and-expression-indexes ====================

Q.append(dict(
    title="Exact-Match Lookup With a Hash Index", difficulty="Easy", topics=TOPIC, subTopics=VARIANT_TOPIC,
    bloomTaxonomy="apply",
    prose="Create a hash index on customer_name, well suited to exact-match lookups, then find "
          "the status of Customer 7's order.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["order_id", "status"],
    solution_sql="CREATE INDEX idx_orders_name_hash ON orders USING hash (customer_name);\n\n"
                 "SELECT order_id, status FROM orders WHERE customer_name = 'Customer 7';",
    data=dict(),
    oracle=lambda: [(o["order_id"], o["status"]) for o in ORDERS if o["customer_name"] == "Customer 7"],
    hints="A hash index stores entries by their computed hash value, well suited to equality "
          "lookups but useless for ranges or sorting.",
))

Q.append(dict(
    title="Filtering on Both Composite Index Columns", difficulty="Medium", topics=TOPIC, subTopics=VARIANT_TOPIC,
    bloomTaxonomy="analyze",
    prose="Create a composite index on (status, region), then find every completed order from "
          "the North region.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["order_id", "customer_name", "amount"],
    solution_sql="CREATE INDEX idx_orders_status_region ON orders (status, region);\n\n"
                 "SELECT order_id, customer_name, amount FROM orders\n"
                 "WHERE status = 'completed' AND region = 'North'\n"
                 "ORDER BY order_id;",
    data=dict(),
    oracle=lambda: [
        (o["order_id"], o["customer_name"], o["amount"]) for o in sorted(ORDERS, key=lambda o: o["order_id"])
        if o["status"] == "completed" and o["region"] == "North"
    ],
    hints="A composite index sorted by status first, then region, serves a query filtering on "
          "both columns together efficiently.",
))

Q.append(dict(
    title="Filtering on the Composite Index's Leading Column Alone", difficulty="Medium", topics=TOPIC, subTopics=VARIANT_TOPIC,
    bloomTaxonomy="analyze",
    prose="The same composite index on (status, region) can still help a query filtering on "
          "status alone, since status is the leading column. Find every active order.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["order_id", "customer_name"],
    solution_sql="CREATE INDEX idx_orders_status_region ON orders (status, region);\n\n"
                 "SELECT order_id, customer_name FROM orders\n"
                 "WHERE status = 'active'\n"
                 "ORDER BY order_id;",
    data=dict(),
    oracle=lambda: [
        (o["order_id"], o["customer_name"]) for o in sorted(ORDERS, key=lambda o: o["order_id"])
        if o["status"] == "active"
    ],
    hints="Filtering on region alone, without status, would get little help from this same "
          "index, since it is not separately sorted by region on its own.",
))

Q.append(dict(
    title="Active Orders Above a Threshold, via Partial Index", difficulty="Hard", topics=TOPIC, subTopics=VARIANT_TOPIC,
    bloomTaxonomy="analyze",
    prose="Create a partial index on amount, covering only active-status rows, then find active "
          "orders worth more than 200.00, sorted by amount.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["order_id", "customer_name", "amount"],
    solution_sql="CREATE INDEX idx_orders_active_amount ON orders (amount) WHERE status = 'active';\n\n"
                 "SELECT order_id, customer_name, amount FROM orders\n"
                 "WHERE status = 'active' AND amount > 200.00\n"
                 "ORDER BY amount;",
    data=dict(),
    oracle=lambda: sorted(
        [(o["order_id"], o["customer_name"], o["amount"]) for o in ORDERS if o["status"] == "active" and o["amount"] > D("200.00")],
        key=lambda row: row[2],
    ),
    hints="A partial index only ever contains rows matching its own condition, active here, "
          "keeping it small and cheap to maintain compared to a full index on the same column.",
))

Q.append(dict(
    title="Cancelled Orders Above a Threshold, via Partial Index", difficulty="Hard", topics=TOPIC, subTopics=VARIANT_TOPIC,
    bloomTaxonomy="apply",
    prose="Create a partial index on amount, covering only cancelled-status rows, then find "
          "cancelled orders worth more than 200.00.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["order_id", "customer_name", "amount"],
    solution_sql="CREATE INDEX idx_orders_cancelled_amount ON orders (amount) WHERE status = 'cancelled';\n\n"
                 "SELECT order_id, customer_name, amount FROM orders\n"
                 "WHERE status = 'cancelled' AND amount > 200.00;",
    data=dict(),
    oracle=lambda: [
        (o["order_id"], o["customer_name"], o["amount"]) for o in ORDERS if o["status"] == "cancelled" and o["amount"] > D("200.00")
    ],
    hints="The partial index's condition matches the query's filter exactly, so it only ever "
          "needs to consider the table's cancelled orders.",
))

Q.append(dict(
    title="Case-Insensitive Lookup With an Expression Index", difficulty="Hard", topics=TOPIC, subTopics=VARIANT_TOPIC,
    bloomTaxonomy="analyze",
    prose="Create an expression index on LOWER(customer_name), then find the status of the "
          "order matching 'customer 9' regardless of how the name was originally capitalized.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["order_id", "status"],
    solution_sql="CREATE INDEX idx_orders_lower_name ON orders (LOWER(customer_name));\n\n"
                 "SELECT order_id, status FROM orders WHERE LOWER(customer_name) = 'customer 9';",
    data=dict(),
    oracle=lambda: [(o["order_id"], o["status"]) for o in ORDERS if o["customer_name"].lower() == "customer 9"],
    hints="A plain B-tree on customer_name is sorted by the raw value, not a lowercased "
          "transformation of it; the expression index stores the already-lowercased value "
          "directly.",
))

# ==================== covering-indexes-and-index-only-scans ====================

Q.append(dict(
    title="Active Orders via a Covering Index", difficulty="Easy", topics=TOPIC, subTopics=COVERING_TOPIC,
    bloomTaxonomy="apply",
    prose="Create a covering index on status that also stores order_id and amount, then select "
          "exactly those two columns for every active order.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["order_id", "amount"],
    solution_sql="CREATE INDEX idx_orders_status_covering ON orders (status) INCLUDE (order_id, amount);\n\n"
                 "SELECT order_id, amount FROM orders\n"
                 "WHERE status = 'active'\n"
                 "ORDER BY order_id;",
    data=dict(),
    oracle=lambda: [
        (o["order_id"], o["amount"]) for o in sorted(ORDERS, key=lambda o: o["order_id"]) if o["status"] == "active"
    ],
    hints="INCLUDE stores extra columns in the index purely for retrieval; since both requested "
          "columns are included, the query can in principle be answered from the index alone.",
))

Q.append(dict(
    title="Active Orders, Requesting a Column Beyond the Covering Index", difficulty="Medium", topics=TOPIC, subTopics=COVERING_TOPIC,
    bloomTaxonomy="analyze",
    prose="Using the same covering index on status (including order_id and amount), select "
          "order_id, amount, and customer_name for every active order. customer_name is not "
          "part of the covering index, but the query's returned data is still correct.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["order_id", "amount", "customer_name"],
    solution_sql="CREATE INDEX idx_orders_status_covering ON orders (status) INCLUDE (order_id, amount);\n\n"
                 "SELECT order_id, amount, customer_name FROM orders\n"
                 "WHERE status = 'active'\n"
                 "ORDER BY order_id;",
    data=dict(),
    oracle=lambda: [
        (o["order_id"], o["amount"], o["customer_name"])
        for o in sorted(ORDERS, key=lambda o: o["order_id"]) if o["status"] == "active"
    ],
    hints="Asking for even one column the index does not store means the database can no longer "
          "answer the query from the index alone, though the data returned is exactly the same "
          "either way.",
))

Q.append(dict(
    title="A Single Customer's Status via a Covering Index", difficulty="Medium", topics=TOPIC, subTopics=COVERING_TOPIC,
    bloomTaxonomy="apply",
    prose="Create a covering index on customer_name that includes status, then find Customer "
          "5's name and status together.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["customer_name", "status"],
    solution_sql="CREATE INDEX idx_orders_name_covering ON orders (customer_name) INCLUDE (status);\n\n"
                 "SELECT customer_name, status FROM orders WHERE customer_name = 'Customer 5';",
    data=dict(),
    oracle=lambda: [(o["customer_name"], o["status"]) for o in ORDERS if o["customer_name"] == "Customer 5"],
    hints="Both the filtered column (customer_name) and the selected columns (customer_name, "
          "status) are fully available from this covering index.",
))

Q.append(dict(
    title="South Region Orders via a Covering Index", difficulty="Hard", topics=TOPIC, subTopics=COVERING_TOPIC,
    bloomTaxonomy="apply",
    prose="Create a covering index on region that includes amount, then find the order_id and "
          "amount for every South region order, sorted by order_id.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["order_id", "amount"],
    solution_sql="CREATE INDEX idx_orders_region_covering ON orders (region) INCLUDE (amount);\n\n"
                 "SELECT order_id, amount FROM orders\n"
                 "WHERE region = 'South'\n"
                 "ORDER BY order_id;",
    data=dict(),
    oracle=lambda: [
        (o["order_id"], o["amount"]) for o in sorted(ORDERS, key=lambda o: o["order_id"]) if o["region"] == "South"
    ],
    hints="INCLUDE columns can be built around any base column, not just status; here it is "
          "region carrying amount alongside it.",
))

Q.append(dict(
    title="Confirming Both a Plain and a Covering Index Exist", difficulty="Hard", topics=TOPIC, subTopics=COVERING_TOPIC,
    bloomTaxonomy="analyze",
    prose="Create a plain index on status and a separate covering index on status that includes "
          "order_id and amount, then list both index names, since a covering index adds a "
          "genuinely separate structure rather than replacing the plain one.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["indexname"],
    solution_sql="CREATE INDEX idx_orders_status ON orders (status);\n"
                 "CREATE INDEX idx_orders_status_covering ON orders (status) INCLUDE (order_id, amount);\n\n"
                 "SELECT indexname FROM pg_indexes\n"
                 "WHERE tablename = 'orders' AND indexname LIKE '%status%'\n"
                 "ORDER BY indexname;",
    data=dict(),
    oracle=lambda: [("idx_orders_status",), ("idx_orders_status_covering",)],
    hints="Building a covering index does not remove or replace an existing plain index on the "
          "same column; both structures exist side by side, each with its own storage cost.",
))

# ==================== when-not-to-index-the-cost-of-overindexing ====================

Q.append(dict(
    title="Confirming Three Indexes Were Created", difficulty="Easy", topics=TOPIC, subTopics=OVERINDEX_TOPIC,
    bloomTaxonomy="apply",
    prose="Create three indexes on orders: one on customer_name, one on amount, and one "
          "composite index on (customer_name, amount), then list all three by name.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["indexname"],
    solution_sql="CREATE INDEX idx_many_name ON orders (customer_name);\n"
                 "CREATE INDEX idx_many_amount ON orders (amount);\n"
                 "CREATE INDEX idx_many_name_amount ON orders (customer_name, amount);\n\n"
                 "SELECT indexname FROM pg_indexes\n"
                 "WHERE tablename = 'orders' AND indexname LIKE 'idx_many%'\n"
                 "ORDER BY indexname;",
    data=dict(),
    oracle=lambda: [("idx_many_amount",), ("idx_many_name",), ("idx_many_name_amount",)],
    hints="Each of these three indexes adds its own ongoing write cost; whether all three "
          "genuinely earn their keep is exactly the question this lesson raises.",
))

Q.append(dict(
    title="A Query the Redundant Index Would Serve", difficulty="Medium", topics=TOPIC, subTopics=OVERINDEX_TOPIC,
    bloomTaxonomy="analyze",
    prose="With both idx_many_name and the composite idx_many_name_amount present, find Customer "
          "4's order amount, a query either index could serve equally well.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["order_id", "amount"],
    solution_sql="CREATE INDEX idx_many_name ON orders (customer_name);\n"
                 "CREATE INDEX idx_many_name_amount ON orders (customer_name, amount);\n\n"
                 "SELECT order_id, amount FROM orders WHERE customer_name = 'Customer 4';",
    data=dict(),
    oracle=lambda: [(o["order_id"], o["amount"]) for o in ORDERS if o["customer_name"] == "Customer 4"],
    hints="Since idx_many_name_amount already sorts by customer_name first, idx_many_name adds "
          "no distinct capability for this specific query, even though the query itself still "
          "returns the correct row either way.",
))

Q.append(dict(
    title="Order Counts by Status", difficulty="Hard", topics=TOPIC, subTopics=OVERINDEX_TOPIC,
    bloomTaxonomy="analyze",
    prose="status has only three possible values, spread across the table. Show how many orders "
          "fall into each status, to see how large a fraction of the table a single-status "
          "lookup would actually match.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["status", "order_count"],
    solution_sql="SELECT status, COUNT(*) AS order_count FROM orders\n"
                 "GROUP BY status\n"
                 "ORDER BY status;",
    data=dict(),
    oracle=lambda: sorted(
        [(status, len([o for o in ORDERS if o["status"] == status])) for status in {o["status"] for o in ORDERS}]
    ),
    hints="A low-cardinality column like status, with only a few distinct values, often matches "
          "a large fraction of the table for any single value, closer to a sequential scan than "
          "a precise, narrow index lookup.",
))

Q.append(dict(
    title="Confirming the Automatic Primary Key Index Exists Too", difficulty="Hard", topics=TOPIC, subTopics=OVERINDEX_TOPIC,
    bloomTaxonomy="analyze",
    prose="Create the same three indexes as before, then count every index now on the orders "
          "table, including the one PostgreSQL creates automatically for the PRIMARY KEY "
          "constraint.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["index_count"],
    solution_sql="CREATE INDEX idx_many_name ON orders (customer_name);\n"
                 "CREATE INDEX idx_many_amount ON orders (amount);\n"
                 "CREATE INDEX idx_many_name_amount ON orders (customer_name, amount);\n\n"
                 "SELECT COUNT(*) AS index_count FROM pg_indexes WHERE tablename = 'orders';",
    data=dict(),
    oracle=lambda: [(4,)],
    hints="A PRIMARY KEY constraint always creates its own unique index automatically; the three "
          "explicitly created here add to that one, for four indexes total, each with its own "
          "ongoing write cost.",
))

assert len(Q) == 23, len(Q)

for q in Q:
    q["tags"] = f"dbms - {q['subTopics']}"

OUT = "content/Question Bank/Coding Questions/DBMS/7.2 - Indexes - Coding Questions.xlsx"

if __name__ == "__main__":
    main(Q, OUT)
