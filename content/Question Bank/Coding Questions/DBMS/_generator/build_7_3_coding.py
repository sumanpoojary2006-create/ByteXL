"""7.3 - Query Optimization - Coding Questions (14, deliberately smaller than
this bank's usual 20-30: inside the query optimizer, reading EXPLAIN,
reading EXPLAIN ANALYZE, join algorithms, common bottlenecks, iterative
performance tuning).

Scope note: this chapter is almost entirely about EXPLAIN/EXPLAIN ANALYZE
output, optimizer cost estimation, and join-algorithm selection, none of
which is gradeable via fixed-output comparison (plan text, cost estimates,
and timings all depend on a live planner, not something reproducible here).
Per an explicit scoping decision, this file covers only the minority of the
chapter that produces a genuinely fixed, gradeable data result:
- join-algorithms: the JOIN queries themselves return correct data
  regardless of which algorithm the planner picks, so questions test the
  data, not the algorithm.
- common-bottlenecks: the missing-index fix, the N+1-to-single-query fix,
  and the cast-defeats-index equivalence rewrite are all data-correctness
  questions, even though whether an index was actually *used* isn't
  testable.
- iterative-performance-tuning: the underlying aggregation query and index
  creation are both gradeable, even though the "measure, remeasure, compare
  timings" workflow itself is not.
- inside-the-query-optimizer: reduced to COUNT-based selectivity questions,
  since the optimizer's actual plan choice can't be graded but the row
  counts its decision is based on can be.
- reading-explain: no gradeable angle was found; this subtopic has zero
  questions here (EXPLAIN's plan text itself is the entire lesson content).
- reading-explain-analyze: reduced to one question testing the
  ROLLBACK-wrapped-write safety pattern the lesson recommends, which does
  produce a genuinely checkable before/after data state.
"""
import decimal
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from dbms_cqlib import main, sql_insert

D = decimal.Decimal

TOPIC = "performance"
OPTIMIZER_TOPIC = "inside-the-query-optimizer"
EXPLAIN_ANALYZE_TOPIC = "reading-explain-analyze"
JOIN_ALGO_TOPIC = "join-algorithms"
BOTTLENECK_TOPIC = "common-bottlenecks"
TUNING_TOPIC = "iterative-performance-tuning"

# ----------------------------- optimizer dataset (skewed distribution) -----------------------------

OPT_COLUMNS = ["order_id", "customer_id"]
OPT_ORDERS = [dict(order_id=i, customer_id=cid) for i, cid in enumerate(
    [1, 1, 1, 1, 1, 1, 1, 2, 3, 4], start=1
)]
OPT_DDL = """
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER
);
"""
OPT_SQL = OPT_DDL.strip("\n") + "\n\n" + sql_insert("orders", OPT_COLUMNS, OPT_ORDERS)
OPT_SCHEMA_LINES = [
    "orders(order_id INTEGER PK, customer_id INTEGER) -- 10 rows; customer_id 1 accounts for 7 of them, a deliberately skewed distribution",
]

# ----------------------------- join-algorithms dataset -----------------------------

JC_COLUMNS = ["customer_id", "customer_name"]
JC_CUSTOMERS = [
    dict(customer_id=1, customer_name="Aditi Kulkarni"),
    dict(customer_id=2, customer_name="Rohan Das"),
    dict(customer_id=3, customer_name="Kavya Nair"),
    dict(customer_id=4, customer_name="Imran Sheikh"),
    dict(customer_id=5, customer_name="Neha Bhatt"),
]
JO_COLUMNS = ["order_id", "customer_id", "amount"]
JOIN_ORDERS = [
    dict(order_id=1, customer_id=1, amount=D("100.00")),
    dict(order_id=2, customer_id=1, amount=D("150.00")),
    dict(order_id=3, customer_id=2, amount=D("200.00")),
    dict(order_id=4, customer_id=2, amount=D("250.00")),
    dict(order_id=5, customer_id=3, amount=D("300.00")),
    dict(order_id=6, customer_id=3, amount=D("350.00")),
    dict(order_id=7, customer_id=4, amount=D("400.00")),
    dict(order_id=8, customer_id=4, amount=D("450.00")),
    dict(order_id=9, customer_id=5, amount=D("500.00")),
    dict(order_id=10, customer_id=5, amount=D("550.00")),
]
JC_DDL = """
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT
);
"""
JO_DDL = """
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(customer_id),
    amount NUMERIC(10, 2)
);
"""
JOIN_SQL = (
    JC_DDL.strip("\n") + "\n\n" + sql_insert("customers", JC_COLUMNS, JC_CUSTOMERS) + "\n\n"
    + JO_DDL.strip("\n") + "\n\n" + sql_insert("orders", JO_COLUMNS, JOIN_ORDERS)
)
JOIN_SCHEMA_LINES = [
    "customers(customer_id INTEGER PK, customer_name TEXT) -- 5 rows",
    "orders(order_id INTEGER PK, customer_id INTEGER FK, amount NUMERIC(10,2)) -- 10 rows, 2 per customer",
]

# ----------------------------- common-bottlenecks dataset -----------------------------

BN_COLUMNS = ["order_id", "customer_id", "status", "amount"]
BN_ORDERS = [
    dict(order_id=1, customer_id=1, status="normal", amount=D("100.00")),
    dict(order_id=2, customer_id=1, status="normal", amount=D("150.00")),
    dict(order_id=3, customer_id=2, status="flagged", amount=D("200.00")),
    dict(order_id=4, customer_id=2, status="normal", amount=D("250.00")),
    dict(order_id=5, customer_id=3, status="normal", amount=D("300.00")),
    dict(order_id=6, customer_id=3, status="flagged", amount=D("350.00")),
    dict(order_id=7, customer_id=4, status="normal", amount=D("400.00")),
    dict(order_id=8, customer_id=4, status="normal", amount=D("450.00")),
    dict(order_id=9, customer_id=5, status="normal", amount=D("500.00")),
    dict(order_id=10, customer_id=5, status="flagged", amount=D("550.00")),
    dict(order_id=11, customer_id=1, status="normal", amount=D("600.00")),
    dict(order_id=12, customer_id=2, status="normal", amount=D("650.00")),
]
BN_DDL = """
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    status TEXT,
    amount NUMERIC(10, 2)
);
"""
BN_SQL = BN_DDL.strip("\n") + "\n\n" + sql_insert("orders", BN_COLUMNS, BN_ORDERS)
BN_SCHEMA_LINES = [
    "orders(order_id INTEGER PK, customer_id INTEGER, status TEXT, amount NUMERIC(10,2)) -- 12 rows; only 3 are flagged",
]

# ----------------------------- iterative-tuning dataset -----------------------------

TN_COLUMNS = ["order_id", "customer_id", "status", "amount", "order_date"]
TUNE_ORDERS = [
    dict(order_id=1, customer_id=1, status="completed", amount=D("100.00"), order_date="2025-01-10"),
    dict(order_id=2, customer_id=1, status="refunded", amount=D("150.00"), order_date="2025-07-05"),
    dict(order_id=3, customer_id=2, status="completed", amount=D("200.00"), order_date="2025-02-15"),
    dict(order_id=4, customer_id=2, status="refunded", amount=D("250.00"), order_date="2025-08-01"),
    dict(order_id=5, customer_id=3, status="completed", amount=D("300.00"), order_date="2025-03-20"),
    dict(order_id=6, customer_id=3, status="refunded", amount=D("350.00"), order_date="2025-06-15"),
    dict(order_id=7, customer_id=4, status="completed", amount=D("400.00"), order_date="2025-04-25"),
    dict(order_id=8, customer_id=4, status="refunded", amount=D("450.00"), order_date="2025-09-10"),
    dict(order_id=9, customer_id=5, status="completed", amount=D("500.00"), order_date="2025-05-30"),
    dict(order_id=10, customer_id=5, status="refunded", amount=D("550.00"), order_date="2025-06-20"),
    dict(order_id=11, customer_id=1, status="refunded", amount=D("600.00"), order_date="2025-05-01"),
    dict(order_id=12, customer_id=2, status="completed", amount=D("650.00"), order_date="2025-01-01"),
]
TN_DDL = """
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    status TEXT,
    amount NUMERIC(10, 2),
    order_date DATE
);
"""
TN_SQL = TN_DDL.strip("\n") + "\n\n" + sql_insert("orders", TN_COLUMNS, TUNE_ORDERS)
TN_SCHEMA_LINES = [
    "orders(order_id INTEGER PK, customer_id INTEGER, status TEXT, amount NUMERIC(10,2), order_date DATE) -- 12 rows",
]

Q = []

# ==================== inside-the-query-optimizer ====================

Q.append(dict(
    title="Counting a Highly Selective Filter", difficulty="Easy", topics=TOPIC, subTopics=OPTIMIZER_TOPIC,
    bloomTaxonomy="apply",
    prose="The optimizer estimates how many rows a condition will match before choosing a plan. "
          "Count how many orders belong to customer_id 4, a highly selective condition matching "
          "only a small fraction of the table.",
    schema_sql=OPT_SQL, schema_lines=OPT_SCHEMA_LINES,
    header=["matching_orders"],
    solution_sql="SELECT COUNT(*) AS matching_orders FROM orders WHERE customer_id = 4;",
    data=dict(),
    oracle=lambda: [(len([o for o in OPT_ORDERS if o["customer_id"] == 4]),)],
    hints="A condition this selective is exactly the situation where an index scan is cheaper "
          "than a sequential scan, since so few rows actually qualify.",
))

Q.append(dict(
    title="Counting a Broad, Unselective Filter", difficulty="Medium", topics=TOPIC, subTopics=OPTIMIZER_TOPIC,
    bloomTaxonomy="analyze",
    prose="Count how many orders belong to customer_id 1, whose orders dominate this "
          "deliberately skewed table, to see just how large a fraction of the table this one "
          "value actually matches.",
    schema_sql=OPT_SQL, schema_lines=OPT_SCHEMA_LINES,
    header=["matching_orders"],
    solution_sql="SELECT COUNT(*) AS matching_orders FROM orders WHERE customer_id = 1;",
    data=dict(),
    oracle=lambda: [(len([o for o in OPT_ORDERS if o["customer_id"] == 1]),)],
    hints="When a condition matches most of the table, like this one, a sequential scan can "
          "genuinely be the cheaper choice, even with an index available.",
))

# ==================== reading-explain-analyze ====================

Q.append(dict(
    title="Measuring a Write Statement Without Keeping Its Changes", difficulty="Medium", topics=TOPIC, subTopics=EXPLAIN_ANALYZE_TOPIC,
    bloomTaxonomy="apply",
    prose="EXPLAIN ANALYZE genuinely executes a statement, so measuring an UPDATE's real "
          "performance safely means wrapping it in a transaction that ends with ROLLBACK instead "
          "of COMMIT. Increase every refunded order's amount by 5%, then roll the change back, "
          "and confirm every refunded order's amount is completely unchanged.",
    schema_sql=TN_SQL, schema_lines=TN_SCHEMA_LINES,
    header=["order_id", "amount"],
    solution_sql="BEGIN;\n"
                 "UPDATE orders SET amount = amount * 1.05 WHERE status = 'refunded';\n"
                 "ROLLBACK;\n\n"
                 "SELECT order_id, amount FROM orders WHERE status = 'refunded' ORDER BY order_id;",
    data=dict(),
    oracle=lambda: [
        (o["order_id"], o["amount"]) for o in sorted(TUNE_ORDERS, key=lambda o: o["order_id"]) if o["status"] == "refunded"
    ],
    hints="ROLLBACK discards every change made since BEGIN, so the UPDATE's real cost can be "
          "measured (in a real EXPLAIN ANALYZE run) without its actual changes ever persisting.",
))

# ==================== join-algorithms ====================

Q.append(dict(
    title="Orders for the First Two Customers", difficulty="Easy", topics=TOPIC, subTopics=JOIN_ALGO_TOPIC,
    bloomTaxonomy="apply",
    prose="Join customers to their orders, filtered to a narrow range, customer_id between 1 and "
          "2, exactly the small-outer-input situation a nested loop join favors.",
    schema_sql=JOIN_SQL, schema_lines=JOIN_SCHEMA_LINES,
    header=["customer_name", "amount"],
    solution_sql="SELECT c.customer_name, o.amount\n"
                 "FROM customers c\n"
                 "JOIN orders o ON c.customer_id = o.customer_id\n"
                 "WHERE c.customer_id BETWEEN 1 AND 2\n"
                 "ORDER BY o.order_id;",
    data=dict(),
    oracle=lambda: [
        ([c for c in JC_CUSTOMERS if c["customer_id"] == o["customer_id"]][0]["customer_name"], o["amount"])
        for o in sorted(JOIN_ORDERS, key=lambda o: o["order_id"])
        if 1 <= o["customer_id"] <= 2
    ],
    hints="With only two customers to look up, a nested loop join can afford a fast, targeted "
          "lookup for each one; the returned rows are the same regardless of which algorithm the "
          "planner actually picks.",
))

Q.append(dict(
    title="Every Customer's Orders, Unfiltered", difficulty="Medium", topics=TOPIC, subTopics=JOIN_ALGO_TOPIC,
    bloomTaxonomy="apply",
    prose="Join every customer to every one of their orders, with no filter narrowing either "
          "side down, the situation a hash join favors when neither table is small.",
    schema_sql=JOIN_SQL, schema_lines=JOIN_SCHEMA_LINES,
    header=["customer_name", "amount"],
    solution_sql="SELECT c.customer_name, o.amount\n"
                 "FROM customers c\n"
                 "JOIN orders o ON c.customer_id = o.customer_id\n"
                 "ORDER BY o.order_id;",
    data=dict(),
    oracle=lambda: [
        ([c for c in JC_CUSTOMERS if c["customer_id"] == o["customer_id"]][0]["customer_name"], o["amount"])
        for o in sorted(JOIN_ORDERS, key=lambda o: o["order_id"])
    ],
    hints="A hash join builds an in-memory table from the smaller side (customers here) and "
          "probes it once per order, avoiding repeated lookups entirely.",
))

Q.append(dict(
    title="Every Customer's Orders, Sorted by Customer", difficulty="Medium", topics=TOPIC, subTopics=JOIN_ALGO_TOPIC,
    bloomTaxonomy="apply",
    prose="Join every customer to their orders, sorted by customer_id, exactly the situation a "
          "merge join favors when both sides can already be produced in that order.",
    schema_sql=JOIN_SQL, schema_lines=JOIN_SCHEMA_LINES,
    header=["customer_name", "amount"],
    solution_sql="SELECT c.customer_name, o.amount\n"
                 "FROM customers c\n"
                 "JOIN orders o ON c.customer_id = o.customer_id\n"
                 "ORDER BY c.customer_id, o.order_id;",
    data=dict(),
    oracle=lambda: [
        (c["customer_name"], o["amount"])
        for c in sorted(JC_CUSTOMERS, key=lambda c: c["customer_id"])
        for o in sorted(JOIN_ORDERS, key=lambda o: o["order_id"])
        if o["customer_id"] == c["customer_id"]
    ],
    hints="A merge join walks both already-sorted inputs forward together; requesting the result "
          "in customer_id order is exactly what makes that approach attractive here.",
))

Q.append(dict(
    title="Orders for a Single Customer", difficulty="Hard", topics=TOPIC, subTopics=JOIN_ALGO_TOPIC,
    bloomTaxonomy="apply",
    prose="Filter the join down to a single customer, customer_id 4, the situation where a "
          "nested loop beats building a whole hash table for just one lookup.",
    schema_sql=JOIN_SQL, schema_lines=JOIN_SCHEMA_LINES,
    header=["customer_name", "amount"],
    solution_sql="SELECT c.customer_name, o.amount\n"
                 "FROM customers c\n"
                 "JOIN orders o ON c.customer_id = o.customer_id\n"
                 "WHERE c.customer_id = 4\n"
                 "ORDER BY o.order_id;",
    data=dict(),
    oracle=lambda: [
        ([c for c in JC_CUSTOMERS if c["customer_id"] == o["customer_id"]][0]["customer_name"], o["amount"])
        for o in sorted(JOIN_ORDERS, key=lambda o: o["order_id"])
        if o["customer_id"] == 4
    ],
    hints="Filtering down to one customer makes the outer input tiny, exactly the situation "
          "nested loop favors.",
))

# ==================== common-bottlenecks ====================

Q.append(dict(
    title="Flagged Orders, Fixed With an Index", difficulty="Easy", topics=TOPIC, subTopics=BOTTLENECK_TOPIC,
    bloomTaxonomy="apply",
    prose="Only a few orders are flagged out of the whole table, a highly selective condition. "
          "Create an index on status, then find every flagged order.",
    schema_sql=BN_SQL, schema_lines=BN_SCHEMA_LINES,
    header=["order_id", "customer_id", "amount"],
    solution_sql="CREATE INDEX idx_orders_status ON orders (status);\n\n"
                 "SELECT order_id, customer_id, amount FROM orders\n"
                 "WHERE status = 'flagged'\n"
                 "ORDER BY order_id;",
    data=dict(),
    oracle=lambda: [
        (o["order_id"], o["customer_id"], o["amount"]) for o in sorted(BN_ORDERS, key=lambda o: o["order_id"])
        if o["status"] == "flagged"
    ],
    hints="Without a supporting index, this selective filter would be forced into a full "
          "sequential scan; the fix is exactly the same CREATE INDEX pattern covered in the "
          "previous chapter.",
))

Q.append(dict(
    title="Fixing an N+1 Pattern With a Single Query", difficulty="Medium", topics=TOPIC, subTopics=BOTTLENECK_TOPIC,
    bloomTaxonomy="analyze",
    prose="Instead of fetching the 3 lowest customer_ids and then looping with one query per "
          "customer, retrieve every order belonging to those 3 customers in a single query.",
    schema_sql=BN_SQL, schema_lines=BN_SCHEMA_LINES,
    header=["customer_id", "order_id", "amount"],
    solution_sql="SELECT customer_id, order_id, amount FROM orders\n"
                 "WHERE customer_id IN (\n"
                 "    SELECT DISTINCT customer_id FROM orders ORDER BY customer_id LIMIT 3\n"
                 ")\n"
                 "ORDER BY customer_id, order_id;",
    data=dict(),
    oracle=lambda: sorted(
        [
            (o["customer_id"], o["order_id"], o["amount"])
            for o in BN_ORDERS
            if o["customer_id"] in sorted({o["customer_id"] for o in BN_ORDERS})[:3]
        ],
        key=lambda row: (row[0], row[1]),
    ),
    hints="One query with IN retrieves the exact same data a loop of separate per-customer "
          "queries would have gathered, as a single round trip instead of many.",
))

Q.append(dict(
    title="Filtering Without an Unnecessary Cast", difficulty="Hard", topics=TOPIC, subTopics=BOTTLENECK_TOPIC,
    bloomTaxonomy="analyze",
    prose="Create an index on amount, then find the order worth exactly 350.00 by comparing "
          "directly against the numeric value, rather than casting amount to text first, which "
          "would defeat the index without changing the correct result.",
    schema_sql=BN_SQL, schema_lines=BN_SCHEMA_LINES,
    header=["order_id", "customer_id"],
    solution_sql="CREATE INDEX idx_orders_amount ON orders (amount);\n\n"
                 "SELECT order_id, customer_id FROM orders WHERE amount = 350.00;",
    data=dict(),
    oracle=lambda: [(o["order_id"], o["customer_id"]) for o in BN_ORDERS if o["amount"] == D("350.00")],
    hints="WHERE amount::TEXT = '350.00' would return this exact same row, just by defeating the "
          "index along the way; comparing directly against the numeric value keeps the index "
          "usable without changing the answer.",
))

Q.append(dict(
    title="Orders for a Customer, Confirmed After Adding an Index", difficulty="Hard", topics=TOPIC, subTopics=BOTTLENECK_TOPIC,
    bloomTaxonomy="apply",
    prose="Create an index on customer_id, then find every order belonging to customer_id 4.",
    schema_sql=BN_SQL, schema_lines=BN_SCHEMA_LINES,
    header=["order_id", "status", "amount"],
    solution_sql="CREATE INDEX idx_orders_customer_id ON orders (customer_id);\n\n"
                 "SELECT order_id, status, amount FROM orders\n"
                 "WHERE customer_id = 4\n"
                 "ORDER BY order_id;",
    data=dict(),
    oracle=lambda: [
        (o["order_id"], o["status"], o["amount"]) for o in sorted(BN_ORDERS, key=lambda o: o["order_id"])
        if o["customer_id"] == 4
    ],
    hints="Before the index exists, this filter would be forced into a sequential scan; the "
          "returned rows are identical either way, only the access path changes.",
))

# ==================== iterative-performance-tuning ====================

Q.append(dict(
    title="Refund Totals After a Cutoff Date", difficulty="Medium", topics=TOPIC, subTopics=TUNING_TOPIC,
    bloomTaxonomy="analyze",
    prose="Establish the baseline report before any tuning: total refunded amount per customer, "
          "counting only refunded orders placed after 2025-06-01, ranked highest total first.",
    schema_sql=TN_SQL, schema_lines=TN_SCHEMA_LINES,
    header=["customer_id", "total_refunded"],
    solution_sql="SELECT customer_id, SUM(amount) AS total_refunded\n"
                 "FROM orders\n"
                 "WHERE status = 'refunded' AND order_date > '2025-06-01'\n"
                 "GROUP BY customer_id\n"
                 "ORDER BY total_refunded DESC;",
    data=dict(),
    oracle=lambda: sorted(
        [
            (cid, sum((o["amount"] for o in TUNE_ORDERS if o["customer_id"] == cid and o["status"] == "refunded" and o["order_date"] > "2025-06-01"), D("0")))
            for cid in {o["customer_id"] for o in TUNE_ORDERS}
        ],
        key=lambda row: row[1], reverse=True,
    ),
    hints="This is the exact query a tuning session would measure a baseline for, before adding "
          "any index; the underlying data and its correct result do not depend on that "
          "measurement.",
))

Q.append(dict(
    title="Top 3 Refund Totals After a Cutoff Date", difficulty="Hard", topics=TOPIC, subTopics=TUNING_TOPIC,
    bloomTaxonomy="analyze",
    prose="If the real business need only ever wants the top 3 customers by refund total, adding "
          "LIMIT 3 to the baseline report is itself a legitimate tuning iteration. Apply it.",
    schema_sql=TN_SQL, schema_lines=TN_SCHEMA_LINES,
    header=["customer_id", "total_refunded"],
    solution_sql="SELECT customer_id, SUM(amount) AS total_refunded\n"
                 "FROM orders\n"
                 "WHERE status = 'refunded' AND order_date > '2025-06-01'\n"
                 "GROUP BY customer_id\n"
                 "ORDER BY total_refunded DESC\n"
                 "LIMIT 3;",
    data=dict(),
    oracle=lambda: sorted(
        [
            (cid, sum((o["amount"] for o in TUNE_ORDERS if o["customer_id"] == cid and o["status"] == "refunded" and o["order_date"] > "2025-06-01"), D("0")))
            for cid in {o["customer_id"] for o in TUNE_ORDERS}
        ],
        key=lambda row: row[1], reverse=True,
    )[:3],
    hints="Changing the query itself, not just the schema, is a legitimate next iteration, worth "
          "measuring separately from an indexing change to keep each iteration's effect "
          "distinct.",
))

Q.append(dict(
    title="Confirming the Tuning Index Was Created", difficulty="Hard", topics=TOPIC, subTopics=TUNING_TOPIC,
    bloomTaxonomy="apply",
    prose="Create the composite index matching both filter columns from the baseline report, "
          "status and order_date together, then confirm it now exists.",
    schema_sql=TN_SQL, schema_lines=TN_SCHEMA_LINES,
    header=["indexname"],
    solution_sql="CREATE INDEX idx_orders_status_date ON orders (status, order_date);\n\n"
                 "SELECT indexname FROM pg_indexes\n"
                 "WHERE tablename = 'orders' AND indexname = 'idx_orders_status_date';",
    data=dict(),
    oracle=lambda: [("idx_orders_status_date",)],
    hints="This single, targeted change is the entire first iteration; nothing else about the "
          "query or schema is touched, keeping the next measurement a clean, isolated comparison "
          "against the baseline.",
))

assert len(Q) == 14, len(Q)

for q in Q:
    q["tags"] = f"dbms - {q['subTopics']}"

OUT = "content/Question Bank/Coding Questions/DBMS/7.3 - Query Optimization - Coding Questions.xlsx"

if __name__ == "__main__":
    main(Q, OUT)
