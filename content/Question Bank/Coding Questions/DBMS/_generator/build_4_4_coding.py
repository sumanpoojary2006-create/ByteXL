"""4.4 - Set Operations and Combining Queries - Coding Questions (22: UNION /
UNION ALL, INTERSECT / EXCEPT, and choosing between set operations, joins,
and EXISTS).

Row-order notes:
- UNION ALL never needs to deduplicate, so PostgreSQL has no operational
  reason to reorder anything: its natural output is simply the first SELECT's
  rows followed by the second SELECT's rows, in each query's own scan order.
  This is used (without an explicit ORDER BY) for every UNION ALL question
  that mirrors the lesson's own bare queries.
- Plain UNION, INTERSECT, and EXCEPT all involve an internal dedup/compare
  step with an otherwise-unspecified result order. Questions that mirror the
  lesson's own worked examples use the row order the lesson's own text
  documents (real execution evidence on this dataset); any question that is
  this bank's own novel variation adds an explicit ORDER BY instead of
  relying on unconfirmed order.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from dbms_cqlib import main, sql_insert

TOPIC = "sql-for-data-retrieval-and-analytics"
UNION_TOPIC = "union-and-union-all"
INTERSECT_TOPIC = "intersect-and-except"
CHOOSING_TOPIC = "when-to-use-set-operations-vs-joins"

# ----------------------------- dataset -----------------------------

CUSTOMER_COLUMNS = ["customer_name", "email"]
ONLINE_CUSTOMERS = [
    dict(customer_name="Aditi Kulkarni", email="aditi.k@example.com"),
    dict(customer_name="Rohan Das", email="rohan.das@example.com"),
    dict(customer_name="Kavya Nair", email="kavya.nair@example.com"),
]
STORE_CUSTOMERS = [
    dict(customer_name="Kavya Nair", email="kavya.nair@example.com"),
    dict(customer_name="Imran Sheikh", email="imran.s@example.com"),
    dict(customer_name="Neha Bhatt", email="neha.bhatt@example.com"),
]

ONLINE_DDL = """
CREATE TABLE online_customers (
    customer_name TEXT,
    email TEXT
);
"""
STORE_DDL = """
CREATE TABLE store_customers (
    customer_name TEXT,
    email TEXT
);
"""
SCHEMA_SQL = (
    ONLINE_DDL.strip("\n") + "\n\n" + sql_insert("online_customers", CUSTOMER_COLUMNS, ONLINE_CUSTOMERS) + "\n\n"
    + STORE_DDL.strip("\n") + "\n\n" + sql_insert("store_customers", CUSTOMER_COLUMNS, STORE_CUSTOMERS)
)
SCHEMA_LINES = [
    "online_customers(customer_name TEXT, email TEXT) -- 3 rows",
    "store_customers(customer_name TEXT, email TEXT) -- 3 rows; Kavya Nair appears in both tables",
]

Q = []

# ==================== union-and-union-all ====================

Q.append(dict(
    title="Combined Mailing List, No Duplicates", difficulty="Easy", topics=TOPIC, subTopics=UNION_TOPIC,
    bloomTaxonomy="apply",
    prose="Tanvi needs one mailing list combining names and emails from both online and store "
          "customers, with no regard for channel, and no customer listed twice even if they shop "
          "both ways.",
    schema_sql=SCHEMA_SQL, schema_lines=SCHEMA_LINES,
    header=["customer_name", "email"],
    solution_sql="SELECT customer_name, email FROM online_customers\n"
                 "UNION\n"
                 "SELECT customer_name, email FROM store_customers;",
    data=dict(),
    oracle=lambda: [
        ("Aditi Kulkarni", "aditi.k@example.com"),
        ("Rohan Das", "rohan.das@example.com"),
        ("Kavya Nair", "kavya.nair@example.com"),
        ("Imran Sheikh", "imran.s@example.com"),
        ("Neha Bhatt", "neha.bhatt@example.com"),
    ],
    hints="UNION stacks the two result sets and automatically removes exact duplicate rows, so "
          "Kavya Nair, who shops both channels, appears only once.",
))

Q.append(dict(
    title="Every Customer Record, Duplicates Included", difficulty="Easy", topics=TOPIC, subTopics=UNION_TOPIC,
    bloomTaxonomy="apply",
    prose="Tanvi wants to know exactly how many total customer records exist across both "
          "channels, counting a cross-channel shopper twice since they genuinely are a customer "
          "of both.",
    schema_sql=SCHEMA_SQL, schema_lines=SCHEMA_LINES,
    header=["customer_name", "email"],
    solution_sql="SELECT customer_name, email FROM online_customers\n"
                 "UNION ALL\n"
                 "SELECT customer_name, email FROM store_customers;",
    data=dict(),
    oracle=lambda: [(c["customer_name"], c["email"]) for c in ONLINE_CUSTOMERS + STORE_CUSTOMERS],
    hints="UNION ALL keeps every row from both queries with no deduplication, so Kavya Nair "
          "appears twice, once from each source table.",
))

Q.append(dict(
    title="Combined List Tagged by Channel", difficulty="Medium", topics=TOPIC, subTopics=UNION_TOPIC,
    bloomTaxonomy="analyze",
    prose="Build the combined customer list with a third column showing which channel each row "
          "originally came from, 'online' or 'store'.",
    schema_sql=SCHEMA_SQL, schema_lines=SCHEMA_LINES,
    header=["person", "contact_email", "source"],
    solution_sql="SELECT customer_name AS person, email AS contact_email, 'online' AS source FROM online_customers\n"
                 "UNION ALL\n"
                 "SELECT customer_name, email, 'store' FROM store_customers;",
    data=dict(),
    oracle=lambda: (
        [(c["customer_name"], c["email"], "online") for c in ONLINE_CUSTOMERS]
        + [(c["customer_name"], c["email"], "store") for c in STORE_CUSTOMERS]
    ),
    hints="A literal string added as a third column tags each row's origin; the final column "
          "headers come from the first SELECT's aliases (person, contact_email), and the second "
          "SELECT's own column names are ignored for labeling.",
))

Q.append(dict(
    title="Combined Mailing List, Alphabetical", difficulty="Medium", topics=TOPIC, subTopics=UNION_TOPIC,
    bloomTaxonomy="apply",
    prose="Present the deduplicated combined mailing list sorted alphabetically by customer name, "
          "the standard way to review a merged list before it goes out.",
    schema_sql=SCHEMA_SQL, schema_lines=SCHEMA_LINES,
    header=["customer_name", "email"],
    solution_sql="SELECT customer_name, email FROM online_customers\n"
                 "UNION\n"
                 "SELECT customer_name, email FROM store_customers\n"
                 "ORDER BY customer_name;",
    data=dict(),
    oracle=lambda: sorted(
        {(c["customer_name"], c["email"]) for c in ONLINE_CUSTOMERS + STORE_CUSTOMERS}
    ),
    hints="ORDER BY can only appear once, at the very end of the combined query, and it sorts the "
          "final stacked result rather than either SELECT individually.",
))

Q.append(dict(
    title="Every Unique Email Address", difficulty="Hard", topics=TOPIC, subTopics=UNION_TOPIC,
    bloomTaxonomy="apply",
    prose="Tanvi wants a single list of every unique email address across both channels, with no "
          "names, sorted alphabetically.",
    schema_sql=SCHEMA_SQL, schema_lines=SCHEMA_LINES,
    header=["email"],
    solution_sql="SELECT email FROM online_customers\n"
                 "UNION\n"
                 "SELECT email FROM store_customers\n"
                 "ORDER BY email;",
    data=dict(),
    oracle=lambda: sorted({(c["email"],) for c in ONLINE_CUSTOMERS + STORE_CUSTOMERS}),
    hints="Selecting just one column still follows the same UNION rules; "
          "kavya.nair@example.com appears in both tables but only once in the result.",
))

Q.append(dict(
    title="Combined List Tagged by Channel, All Records", difficulty="Hard", topics=TOPIC, subTopics=UNION_TOPIC,
    bloomTaxonomy="analyze",
    prose="Build the tagged combined list again, but this time keep every record from both "
          "channels, including Kavya Nair's row from each side separately.",
    schema_sql=SCHEMA_SQL, schema_lines=SCHEMA_LINES,
    header=["person", "contact_email", "channel"],
    solution_sql="SELECT customer_name AS person, email AS contact_email, 'online' AS channel FROM online_customers\n"
                 "UNION ALL\n"
                 "SELECT customer_name, email, 'store' FROM store_customers;",
    data=dict(),
    oracle=lambda: (
        [(c["customer_name"], c["email"], "online") for c in ONLINE_CUSTOMERS]
        + [(c["customer_name"], c["email"], "store") for c in STORE_CUSTOMERS]
    ),
    hints="Since UNION ALL keeps every row, Kavya Nair now appears twice: once tagged 'online' "
          "and once tagged 'store', reflecting her genuine presence in both channels.",
))

Q.append(dict(
    title="Total Customer Record Count", difficulty="Hard", topics=TOPIC, subTopics=UNION_TOPIC,
    bloomTaxonomy="analyze",
    prose="Compute the single total record count across both channels in one query, wrapping a "
          "UNION ALL in an outer COUNT.",
    schema_sql=SCHEMA_SQL, schema_lines=SCHEMA_LINES,
    header=["total_records"],
    solution_sql="SELECT COUNT(*) AS total_records FROM (\n"
                 "    SELECT customer_name, email FROM online_customers\n"
                 "    UNION ALL\n"
                 "    SELECT customer_name, email FROM store_customers\n"
                 ") AS combined;",
    data=dict(),
    oracle=lambda: [(len(ONLINE_CUSTOMERS) + len(STORE_CUSTOMERS),)],
    hints="A UNION ALL query can itself be wrapped in parentheses and treated as a subquery, "
          "letting COUNT(*) summarize the combined result in one pass.",
))

# ==================== intersect-and-except ====================

Q.append(dict(
    title="Cross-Channel Shoppers", difficulty="Easy", topics=TOPIC, subTopics=INTERSECT_TOPIC,
    bloomTaxonomy="apply",
    prose="Find exactly which customers shop both online and in-store, for a cross-channel "
          "loyalty reward.",
    schema_sql=SCHEMA_SQL, schema_lines=SCHEMA_LINES,
    header=["customer_name", "email"],
    solution_sql="SELECT customer_name, email FROM online_customers\n"
                 "INTERSECT\n"
                 "SELECT customer_name, email FROM store_customers;",
    data=dict(),
    oracle=lambda: [("Kavya Nair", "kavya.nair@example.com")],
    hints="INTERSECT keeps only the rows that appear in both result sets, matching on every "
          "selected column at once.",
))

Q.append(dict(
    title="Online-Only Customers", difficulty="Easy", topics=TOPIC, subTopics=INTERSECT_TOPIC,
    bloomTaxonomy="apply",
    prose="Find online customers who have never once shopped in a physical store, for a "
          "'visit us in person' campaign.",
    schema_sql=SCHEMA_SQL, schema_lines=SCHEMA_LINES,
    header=["customer_name", "email"],
    solution_sql="SELECT customer_name, email FROM online_customers\n"
                 "EXCEPT\n"
                 "SELECT customer_name, email FROM store_customers;",
    data=dict(),
    oracle=lambda: [("Aditi Kulkarni", "aditi.k@example.com"), ("Rohan Das", "rohan.das@example.com")],
    hints="EXCEPT takes the first query's results and removes anything that also appears in the "
          "second query's results.",
))

Q.append(dict(
    title="Store-Only Customers", difficulty="Medium", topics=TOPIC, subTopics=INTERSECT_TOPIC,
    bloomTaxonomy="analyze",
    prose="Now find the opposite: store customers who have never shopped online. EXCEPT is "
          "directional, so reversing which query comes first changes the answer.",
    schema_sql=SCHEMA_SQL, schema_lines=SCHEMA_LINES,
    header=["customer_name", "email"],
    solution_sql="SELECT customer_name, email FROM store_customers\n"
                 "EXCEPT\n"
                 "SELECT customer_name, email FROM online_customers;",
    data=dict(),
    oracle=lambda: [("Imran Sheikh", "imran.s@example.com"), ("Neha Bhatt", "neha.bhatt@example.com")],
    hints="Starting from store_customers and subtracting online_customers is a genuinely "
          "different question from the reverse; EXCEPT is directional like regular subtraction.",
))

Q.append(dict(
    title="Cross-Channel Shoppers by Name Only", difficulty="Medium", topics=TOPIC, subTopics=INTERSECT_TOPIC,
    bloomTaxonomy="analyze",
    prose="Repeat the cross-channel shopper check, but comparing only customer_name this time, "
          "not the full row.",
    schema_sql=SCHEMA_SQL, schema_lines=SCHEMA_LINES,
    header=["customer_name"],
    solution_sql="SELECT customer_name FROM online_customers\n"
                 "INTERSECT\n"
                 "SELECT customer_name FROM store_customers;",
    data=dict(),
    oracle=lambda: [("Kavya Nair",)],
    hints="Choosing which columns to include in a set operation is choosing exactly how strict "
          "the matching should be; here only the name needs to match, not the email too.",
))

Q.append(dict(
    title="Cross-Channel Shoppers, Starting From Store", difficulty="Hard", topics=TOPIC, subTopics=INTERSECT_TOPIC,
    bloomTaxonomy="analyze",
    prose="Confirm the loyalty reward list a different way: find every store customer who is "
          "also an online customer, using INTERSECT starting from store_customers this time.",
    schema_sql=SCHEMA_SQL, schema_lines=SCHEMA_LINES,
    header=["customer_name", "email"],
    solution_sql="SELECT customer_name, email FROM store_customers\n"
                 "INTERSECT\n"
                 "SELECT customer_name, email FROM online_customers;",
    data=dict(),
    oracle=lambda: [("Kavya Nair", "kavya.nair@example.com")],
    hints="Unlike EXCEPT, swapping the order of the two queries in an INTERSECT does not change "
          "which rows come back.",
))

Q.append(dict(
    title="Online-Only Customer Names", difficulty="Hard", topics=TOPIC, subTopics=INTERSECT_TOPIC,
    bloomTaxonomy="apply",
    prose="Find the names (not full rows) of online customers who have never shopped in-store, "
          "sorted alphabetically.",
    schema_sql=SCHEMA_SQL, schema_lines=SCHEMA_LINES,
    header=["customer_name"],
    solution_sql="SELECT customer_name FROM online_customers\n"
                 "EXCEPT\n"
                 "SELECT customer_name FROM store_customers\n"
                 "ORDER BY customer_name;",
    data=dict(),
    oracle=lambda: sorted(
        {(c["customer_name"],) for c in ONLINE_CUSTOMERS} - {(c["customer_name"],) for c in STORE_CUSTOMERS}
    ),
    hints="EXCEPT on a single column follows the same column rules as a multi-column EXCEPT, just "
          "with a narrower basis for comparison.",
))

Q.append(dict(
    title="Cross-Channel Shopper Count", difficulty="Hard", topics=TOPIC, subTopics=INTERSECT_TOPIC,
    bloomTaxonomy="analyze",
    prose="Compute the single count of how many customers shop both channels, wrapping an "
          "INTERSECT in an outer COUNT.",
    schema_sql=SCHEMA_SQL, schema_lines=SCHEMA_LINES,
    header=["cross_channel_count"],
    solution_sql="SELECT COUNT(*) AS cross_channel_count FROM (\n"
                 "    SELECT customer_name, email FROM online_customers\n"
                 "    INTERSECT\n"
                 "    SELECT customer_name, email FROM store_customers\n"
                 ") AS common;",
    data=dict(),
    oracle=lambda: [(1,)],
    hints="Just like UNION ALL, an INTERSECT query can be wrapped in parentheses and counted as a "
          "subquery.",
))

Q.append(dict(
    title="Online-Only Customers, Explicitly Sorted", difficulty="Hard", topics=TOPIC, subTopics=INTERSECT_TOPIC,
    bloomTaxonomy="apply",
    prose="Repeat the online-only customer check, but with the result explicitly sorted "
          "alphabetically by customer name for a presentable report.",
    schema_sql=SCHEMA_SQL, schema_lines=SCHEMA_LINES,
    header=["customer_name", "email"],
    solution_sql="SELECT customer_name, email FROM online_customers\n"
                 "EXCEPT\n"
                 "SELECT customer_name, email FROM store_customers\n"
                 "ORDER BY customer_name;",
    data=dict(),
    oracle=lambda: sorted(
        {(c["customer_name"], c["email"]) for c in ONLINE_CUSTOMERS}
        - {(c["customer_name"], c["email"]) for c in STORE_CUSTOMERS}
    ),
    hints="ORDER BY after EXCEPT sorts the final result of the subtraction, exactly like sorting "
          "after any other set operation.",
))

# ==================== when-to-use-set-operations-vs-joins ====================

Q.append(dict(
    title="Cross-Channel Match, Widened Sideways via JOIN", difficulty="Easy", topics=TOPIC, subTopics=CHOOSING_TOPIC,
    bloomTaxonomy="understand",
    prose="Find the same cross-channel shopper using a JOIN instead of INTERSECT, observing how "
          "a join widens the row with columns from both tables rather than producing one set of "
          "columns.",
    schema_sql=SCHEMA_SQL, schema_lines=SCHEMA_LINES,
    header=["customer_name", "email", "store_side_name"],
    solution_sql="SELECT o.customer_name, o.email, s.customer_name AS store_side_name\n"
                 "FROM online_customers o\n"
                 "JOIN store_customers s ON o.email = s.email;",
    data=dict(),
    oracle=lambda: [
        (o["customer_name"], o["email"], s["customer_name"])
        for o in ONLINE_CUSTOMERS for s in STORE_CUSTOMERS if o["email"] == s["email"]
    ],
    hints="A join produces a row with columns from both tables side by side, even though "
          "customer_name and store_side_name happen to hold the same value here.",
))

Q.append(dict(
    title="Online-Only Customers via NOT EXISTS", difficulty="Medium", topics=TOPIC, subTopics=CHOOSING_TOPIC,
    bloomTaxonomy="analyze",
    prose="Find the same online-only customers as the EXCEPT version, but phrased as an "
          "existence check instead.",
    schema_sql=SCHEMA_SQL, schema_lines=SCHEMA_LINES,
    header=["customer_name", "email"],
    solution_sql="SELECT customer_name, email FROM online_customers o\n"
                 "WHERE NOT EXISTS (\n"
                 "    SELECT 1 FROM store_customers s WHERE s.email = o.email\n"
                 ");",
    data=dict(),
    oracle=lambda: [
        (o["customer_name"], o["email"]) for o in ONLINE_CUSTOMERS
        if not any(o["email"] == s["email"] for s in STORE_CUSTOMERS)
    ],
    hints="NOT EXISTS reads naturally as 'keep this row if no match exists,' and generalizes more "
          "easily than EXCEPT to conditions beyond a whole-row comparison.",
))

Q.append(dict(
    title="Both Emails Side by Side for Matched Customers", difficulty="Medium", topics=TOPIC, subTopics=CHOOSING_TOPIC,
    bloomTaxonomy="analyze",
    prose="For customers who shop both channels, show their name alongside both their "
          "online-recorded email and their store-recorded email in the same row, something only "
          "a join can naturally produce.",
    schema_sql=SCHEMA_SQL, schema_lines=SCHEMA_LINES,
    header=["customer_name", "online_email", "store_email"],
    solution_sql="SELECT o.customer_name, o.email AS online_email, s.email AS store_email\n"
                 "FROM online_customers o\n"
                 "JOIN store_customers s ON o.customer_name = s.customer_name;",
    data=dict(),
    oracle=lambda: [
        (o["customer_name"], o["email"], s["email"])
        for o in ONLINE_CUSTOMERS for s in STORE_CUSTOMERS if o["customer_name"] == s["customer_name"]
    ],
    hints="A set operation could only ever return one shared set of columns; a join is what makes "
          "it possible to see both emails, even though in this data they happen to be identical.",
))

Q.append(dict(
    title="Single-Channel-Only Customers", difficulty="Hard", topics=TOPIC, subTopics=CHOOSING_TOPIC,
    bloomTaxonomy="analyze",
    prose="Find every customer name that appears in exactly one of the two tables, not both: the "
          "customers who shop through only one channel. This needs EXCEPT run once in each "
          "direction, stitched together with UNION ALL, sorted alphabetically for a clean report.",
    schema_sql=SCHEMA_SQL, schema_lines=SCHEMA_LINES,
    header=["customer_name"],
    solution_sql="(SELECT customer_name FROM online_customers EXCEPT SELECT customer_name FROM store_customers)\n"
                 "UNION ALL\n"
                 "(SELECT customer_name FROM store_customers EXCEPT SELECT customer_name FROM online_customers)\n"
                 "ORDER BY customer_name;",
    data=dict(),
    oracle=lambda: sorted(
        ({(c["customer_name"],) for c in ONLINE_CUSTOMERS} - {(c["customer_name"],) for c in STORE_CUSTOMERS})
        | ({(c["customer_name"],) for c in STORE_CUSTOMERS} - {(c["customer_name"],) for c in ONLINE_CUSTOMERS})
    ),
    hints="Each EXCEPT isolates one direction's exclusive customers; UNION ALL then stacks both "
          "single-channel lists together, since a name from one EXCEPT can never also appear in "
          "the other.",
))

Q.append(dict(
    title="Cross-Channel Match via EXISTS", difficulty="Hard", topics=TOPIC, subTopics=CHOOSING_TOPIC,
    bloomTaxonomy="analyze",
    prose="Find the cross-channel shopper using EXISTS instead of INTERSECT, the existence-check "
          "counterpart to the same question.",
    schema_sql=SCHEMA_SQL, schema_lines=SCHEMA_LINES,
    header=["customer_name", "email"],
    solution_sql="SELECT customer_name, email FROM online_customers o\n"
                 "WHERE EXISTS (\n"
                 "    SELECT 1 FROM store_customers s WHERE s.email = o.email\n"
                 ");",
    data=dict(),
    oracle=lambda: [
        (o["customer_name"], o["email"]) for o in ONLINE_CUSTOMERS
        if any(o["email"] == s["email"] for s in STORE_CUSTOMERS)
    ],
    hints="Just as NOT EXISTS mirrors EXCEPT for the no-match case, EXISTS mirrors INTERSECT for "
          "the has-a-match case.",
))

Q.append(dict(
    title="Confirming the Cross-Channel Count via JOIN", difficulty="Hard", topics=TOPIC, subTopics=CHOOSING_TOPIC,
    bloomTaxonomy="analyze",
    prose="Confirm, using a JOIN this time, that the same single cross-channel shopper count "
          "results as the INTERSECT-based count did.",
    schema_sql=SCHEMA_SQL, schema_lines=SCHEMA_LINES,
    header=["matched_via_join"],
    solution_sql="SELECT COUNT(*) AS matched_via_join\n"
                 "FROM online_customers o\n"
                 "JOIN store_customers s ON o.email = s.email;",
    data=dict(),
    oracle=lambda: [(len([1 for o in ONLINE_CUSTOMERS for s in STORE_CUSTOMERS if o["email"] == s["email"]]),)],
    hints="Whether counted through a JOIN or through an INTERSECT wrapped in a subquery, the "
          "number of genuinely matching customers must agree, since both are answering the same "
          "underlying question.",
))

Q.append(dict(
    title="Online-Only Customers via LEFT JOIN and IS NULL", difficulty="Hard", topics=TOPIC, subTopics=CHOOSING_TOPIC,
    bloomTaxonomy="analyze",
    prose="Find the same online-only customers a third way, using the LEFT JOIN plus IS NULL "
          "pattern from the joins chapter, confirming it agrees with both the EXCEPT and NOT "
          "EXISTS versions of the same question.",
    schema_sql=SCHEMA_SQL, schema_lines=SCHEMA_LINES,
    header=["customer_name", "email"],
    solution_sql="SELECT o.customer_name, o.email\n"
                 "FROM online_customers o\n"
                 "LEFT JOIN store_customers s ON o.email = s.email\n"
                 "WHERE s.email IS NULL;",
    data=dict(),
    oracle=lambda: [
        (o["customer_name"], o["email"]) for o in ONLINE_CUSTOMERS
        if not any(o["email"] == s["email"] for s in STORE_CUSTOMERS)
    ],
    hints="LEFT JOIN plus a NULL check on the right-hand key, NOT EXISTS, and EXCEPT are three "
          "genuinely different ways to express the identical question here, each reading with a "
          "slightly different emphasis.",
))

assert len(Q) == 22, len(Q)

for q in Q:
    q["tags"] = f"dbms - {q['subTopics']}"

OUT = "content/Question Bank/Coding Questions/DBMS/4.4 - Set Operations and Combining Queries - Coding Questions.xlsx"

if __name__ == "__main__":
    main(Q, OUT)
