"""4.2 - Aggregation - Coding Questions (28: aggregate functions, GROUP BY,
HAVING, and combining aggregation with joins, WHERE, and ORDER BY).

Amounts are modeled as decimal.Decimal (scale 2) to match NUMERIC(10,2)
exactly. Every AVG is wrapped in ROUND(..., N) with an explicit N, since
PostgreSQL's unrounded AVG(numeric) result scale is not reliably predictable
without a live server to test against, whereas ROUND(AVG(x), N) is fully
deterministic regardless of AVG's own internal precision -- this also matches
the lesson's own practice in its "combining several aggregates" example.
SUM(numeric) reliably preserves the input column's scale, so SUM is used
unrounded, matching the lesson.
"""
import decimal
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from dbms_cqlib import main, sql_insert

D = decimal.Decimal


def pg_round(value, places):
    quantum = D(1).scaleb(-places)
    return value.quantize(quantum, rounding=decimal.ROUND_HALF_UP)


TOPIC = "sql-for-data-retrieval-and-analytics"
AGG_TOPIC = "aggregate-functions"
GROUP_TOPIC = "grouping-data"
HAVING_TOPIC = "filtering-groups"
COMBINE_TOPIC = "combining-aggregation-with-sorting-filtering-and-joins"

# ----------------------------- orders dataset -----------------------------

ORDER_COLUMNS = ["order_id", "customer_name", "category", "amount", "order_date"]
ORDERS = [
    dict(order_id=1, customer_name="Ishita Rao", category="Fiction", amount=D("450.00"), order_date="2025-04-02"),
    dict(order_id=2, customer_name="Vivek Menon", category="Non-Fiction", amount=D("899.00"), order_date="2025-04-03"),
    dict(order_id=3, customer_name="Ishita Rao", category="Fiction", amount=D("320.00"), order_date="2025-04-05"),
    dict(order_id=4, customer_name="Aman Gupta", category="Children", amount=D("210.00"), order_date="2025-04-06"),
    dict(order_id=5, customer_name="Sonal Deshpande", category="Non-Fiction", amount=D("1450.00"), order_date="2025-04-08"),
    dict(order_id=6, customer_name="Vivek Menon", category="Fiction", amount=D("610.00"), order_date="2025-04-10"),
    dict(order_id=7, customer_name="Aman Gupta", category="Children", amount=D("175.00"), order_date="2025-04-12"),
    dict(order_id=8, customer_name="Ishita Rao", category="Non-Fiction", amount=D("990.00"), order_date="2025-04-14"),
]

ORDERS_DDL = """
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    category TEXT,
    amount NUMERIC(10, 2),
    order_date DATE
);
"""
ORDERS_SQL = ORDERS_DDL.strip("\n") + "\n\n" + sql_insert("orders", ORDER_COLUMNS, ORDERS)
ORDERS_SCHEMA_LINES = [
    "orders(order_id INTEGER PK, customer_name TEXT, category TEXT, amount NUMERIC(10,2), order_date DATE) -- 8 rows",
]

# ----------------------------- customers dataset (for the joined lesson) -----------------------------

CUSTOMER_COLUMNS = ["customer_name", "region"]
CUSTOMERS = [
    dict(customer_name="Ishita Rao", region="South"),
    dict(customer_name="Vivek Menon", region="West"),
    dict(customer_name="Aman Gupta", region="North"),
    dict(customer_name="Sonal Deshpande", region="West"),
]

CUSTOMERS_DDL = """
CREATE TABLE customers (
    customer_name TEXT PRIMARY KEY,
    region TEXT
);
"""
ORDERS_WITH_FK_DDL = """
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_name TEXT REFERENCES customers(customer_name),
    category TEXT,
    amount NUMERIC(10, 2),
    order_date DATE
);
"""
JOINED_SQL = (
    CUSTOMERS_DDL.strip("\n") + "\n\n" + sql_insert("customers", CUSTOMER_COLUMNS, CUSTOMERS) + "\n\n"
    + ORDERS_WITH_FK_DDL.strip("\n") + "\n\n" + sql_insert("orders", ORDER_COLUMNS, ORDERS)
)
JOINED_SCHEMA_LINES = [
    "customers(customer_name TEXT PK, region TEXT) -- 4 rows",
    "orders(order_id INTEGER PK, customer_name TEXT FK, category TEXT, amount NUMERIC(10,2), order_date DATE) -- 8 rows",
]

REGION_BY_CUSTOMER = {c["customer_name"]: c["region"] for c in CUSTOMERS}

Q = []

# ==================== aggregate-functions ====================

Q.append(dict(
    title="Total Order Count", difficulty="Easy", topics=TOPIC, subTopics=AGG_TOPIC,
    bloomTaxonomy="apply",
    prose="Priya's first question from the founders: how many orders did the bookstore receive in "
          "total?",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["total_orders"],
    solution_sql="SELECT COUNT(*) AS total_orders FROM orders;",
    data=dict(orders=ORDERS),
    oracle=lambda orders: [(len(orders),)],
    hints="COUNT(*) counts every row in the result set, regardless of what any column contains.",
))

Q.append(dict(
    title="Total Revenue and Average Order Value", difficulty="Easy", topics=TOPIC, subTopics=AGG_TOPIC,
    bloomTaxonomy="apply",
    prose="Show the bookstore's total revenue and average order value in one query, with the "
          "average rounded to two decimal places.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["total_revenue", "average_order_value"],
    solution_sql="SELECT SUM(amount) AS total_revenue, ROUND(AVG(amount), 2) AS average_order_value FROM orders;",
    data=dict(orders=ORDERS),
    oracle=lambda orders: [
        (sum((o["amount"] for o in orders), D("0")),
         pg_round(sum((o["amount"] for o in orders), D("0")) / len(orders), 2))
    ],
    hints="SUM adds every value in the column; AVG divides that same sum by the row count "
          "automatically. Wrapping AVG in ROUND(..., 2) keeps the result at a clean two decimal "
          "places.",
))

Q.append(dict(
    title="Smallest and Largest Order", difficulty="Medium", topics=TOPIC, subTopics=AGG_TOPIC,
    bloomTaxonomy="apply",
    prose="Find the smallest and largest single order amounts the bookstore has received.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["smallest_order", "largest_order"],
    solution_sql="SELECT MIN(amount) AS smallest_order, MAX(amount) AS largest_order FROM orders;",
    data=dict(orders=ORDERS),
    oracle=lambda orders: [(min(o["amount"] for o in orders), max(o["amount"] for o in orders))],
    hints="MIN returns the smallest value found in the column across all matching rows; MAX "
          "returns the largest.",
))

Q.append(dict(
    title="Earliest and Latest Order Date", difficulty="Medium", topics=TOPIC, subTopics=AGG_TOPIC,
    bloomTaxonomy="apply",
    prose="MIN and MAX work on dates too, not just numbers. Find the earliest and latest order "
          "dates on record.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["earliest_order", "latest_order"],
    solution_sql="SELECT MIN(order_date) AS earliest_order, MAX(order_date) AS latest_order FROM orders;",
    data=dict(orders=ORDERS),
    oracle=lambda orders: [(min(o["order_date"] for o in orders), max(o["order_date"] for o in orders))],
    hints="Dates compare earliest-to-latest exactly like numbers compare smallest-to-largest, so "
          "MIN and MAX work on a DATE column the same way they work on amount.",
))

Q.append(dict(
    title="Full Summary Dashboard Row", difficulty="Medium", topics=TOPIC, subTopics=AGG_TOPIC,
    bloomTaxonomy="analyze",
    prose="Build the founders' single summary dashboard row: total order count, total revenue, "
          "average order value (rounded to two decimals), smallest order, and largest order, all "
          "in one query.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["total_orders", "total_revenue", "average_order_value", "smallest_order", "largest_order"],
    solution_sql="SELECT COUNT(*) AS total_orders,\n"
                 "       SUM(amount) AS total_revenue,\n"
                 "       ROUND(AVG(amount), 2) AS average_order_value,\n"
                 "       MIN(amount) AS smallest_order,\n"
                 "       MAX(amount) AS largest_order\n"
                 "FROM orders;",
    data=dict(orders=ORDERS),
    oracle=lambda orders: [(
        len(orders),
        sum((o["amount"] for o in orders), D("0")),
        pg_round(sum((o["amount"] for o in orders), D("0")) / len(orders), 2),
        min(o["amount"] for o in orders),
        max(o["amount"] for o in orders),
    )],
    hints="All five aggregate functions can appear together in a single SELECT, each summarizing "
          "the same set of rows in its own way, with no GROUP BY needed for one overall summary "
          "row.",
))

Q.append(dict(
    title="Fiction Category Orders and Revenue", difficulty="Hard", topics=TOPIC, subTopics=AGG_TOPIC,
    bloomTaxonomy="apply",
    prose="The founders want the total number of orders and total revenue specifically from the "
          "Fiction category, aliased as fiction_orders and fiction_revenue.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["fiction_orders", "fiction_revenue"],
    solution_sql="SELECT COUNT(*) AS fiction_orders, SUM(amount) AS fiction_revenue "
                 "FROM orders WHERE category = 'Fiction';",
    data=dict(orders=ORDERS),
    oracle=lambda orders: [(
        len([o for o in orders if o["category"] == "Fiction"]),
        sum((o["amount"] for o in orders if o["category"] == "Fiction"), D("0")),
    )],
    hints="WHERE narrows the rows down first; the aggregate functions only ever see whatever "
          "survives that filter.",
))

Q.append(dict(
    title="Average Order Value Rounded to Whole Rupees", difficulty="Hard", topics=TOPIC, subTopics=AGG_TOPIC,
    bloomTaxonomy="apply",
    prose="For a rough, whole-number summary, show total revenue alongside the average order "
          "value rounded to zero decimal places.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["total_revenue", "average_order_value_rounded"],
    solution_sql="SELECT SUM(amount) AS total_revenue, ROUND(AVG(amount), 0) AS average_order_value_rounded "
                 "FROM orders;",
    data=dict(orders=ORDERS),
    oracle=lambda orders: [(
        sum((o["amount"] for o in orders), D("0")),
        pg_round(sum((o["amount"] for o in orders), D("0")) / len(orders), 0),
    )],
    hints="ROUND's second argument controls the output precision; 0 rounds to the nearest whole "
          "number, exactly like rounding any other numeric expression.",
))

# ==================== grouping-data ====================

Q.append(dict(
    title="Revenue by Category", difficulty="Easy", topics=TOPIC, subTopics=GROUP_TOPIC,
    bloomTaxonomy="apply",
    prose="The founders want to know which category earns the most: Fiction, Non-Fiction, or "
          "Children's books. Show total revenue for each category.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["category", "category_revenue"],
    solution_sql="SELECT category, SUM(amount) AS category_revenue FROM orders GROUP BY category "
                 "ORDER BY category;",
    data=dict(orders=ORDERS),
    oracle=lambda orders: [
        (cat, sum((o["amount"] for o in orders if o["category"] == cat), D("0")))
        for cat in sorted({o["category"] for o in orders})
    ],
    hints="GROUP BY category gathers all rows that share the same category value into one group "
          "before SUM runs, producing one total per category instead of one grand total.",
))

Q.append(dict(
    title="Orders Placed and Revenue by Category", difficulty="Easy", topics=TOPIC, subTopics=GROUP_TOPIC,
    bloomTaxonomy="apply",
    prose="Extend the category breakdown to also show how many orders landed in each category, "
          "alongside the revenue.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["category", "orders_placed", "category_revenue"],
    solution_sql="SELECT category, COUNT(*) AS orders_placed, SUM(amount) AS category_revenue "
                 "FROM orders GROUP BY category ORDER BY category;",
    data=dict(orders=ORDERS),
    oracle=lambda orders: [
        (cat, len([o for o in orders if o["category"] == cat]),
         sum((o["amount"] for o in orders if o["category"] == cat), D("0")))
        for cat in sorted({o["category"] for o in orders})
    ],
    hints="Every column in the SELECT list must either appear in GROUP BY or be wrapped in an "
          "aggregate function; category satisfies the first, COUNT(*) and SUM the second.",
))

Q.append(dict(
    title="Spending by Customer and Category", difficulty="Medium", topics=TOPIC, subTopics=GROUP_TOPIC,
    bloomTaxonomy="analyze",
    prose="Group by more than one column at once: show each customer's order count and total "
          "spend broken down separately by category, so a customer's Fiction orders are "
          "summarized apart from their Non-Fiction orders.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["customer_name", "category", "orders_placed", "total_spent"],
    solution_sql="SELECT customer_name, category, COUNT(*) AS orders_placed, SUM(amount) AS total_spent\n"
                 "FROM orders GROUP BY customer_name, category ORDER BY customer_name, category;",
    data=dict(orders=ORDERS),
    oracle=lambda orders: [
        (cust, cat, len([o for o in orders if o["customer_name"] == cust and o["category"] == cat]),
         sum((o["amount"] for o in orders if o["customer_name"] == cust and o["category"] == cat), D("0")))
        for cust, cat in sorted({(o["customer_name"], o["category"]) for o in orders})
    ],
    hints="GROUP BY customer_name, category produces one group for every distinct combination of "
          "the two values, not one group per customer alone.",
))

Q.append(dict(
    title="Categories Ranked by Revenue", difficulty="Medium", topics=TOPIC, subTopics=GROUP_TOPIC,
    bloomTaxonomy="apply",
    prose="Turn the category revenue breakdown into a ranked list, highest-earning category "
          "first.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["category", "category_revenue"],
    solution_sql="SELECT category, SUM(amount) AS category_revenue FROM orders "
                 "GROUP BY category ORDER BY category_revenue DESC;",
    data=dict(orders=ORDERS),
    oracle=lambda orders: sorted(
        [(cat, sum((o["amount"] for o in orders if o["category"] == cat), D("0")))
         for cat in {o["category"] for o in orders}],
        key=lambda row: row[1], reverse=True,
    ),
    hints="GROUP BY does not control result order by itself; combine it with ORDER BY on the "
          "aggregated column for a ranked summary.",
))

Q.append(dict(
    title="Customer Leaderboard by Spend", difficulty="Hard", topics=TOPIC, subTopics=GROUP_TOPIC,
    bloomTaxonomy="analyze",
    prose="The founders want to know how many orders each individual customer has placed, and "
          "their total spend, ranked from the highest spender down.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["customer_name", "order_count", "total_spent"],
    solution_sql="SELECT customer_name, COUNT(*) AS order_count, SUM(amount) AS total_spent\n"
                 "FROM orders GROUP BY customer_name ORDER BY total_spent DESC;",
    data=dict(orders=ORDERS),
    oracle=lambda orders: sorted(
        [(cust, len([o for o in orders if o["customer_name"] == cust]),
          sum((o["amount"] for o in orders if o["customer_name"] == cust), D("0")))
         for cust in {o["customer_name"] for o in orders}],
        key=lambda row: row[2], reverse=True,
    ),
    hints="Group by customer_name alone this time, then order the grouped result by the computed "
          "total_spent, largest first.",
))

Q.append(dict(
    title="Average Order Value per Customer", difficulty="Hard", topics=TOPIC, subTopics=GROUP_TOPIC,
    bloomTaxonomy="analyze",
    prose="Show each customer's average order value, rounded to two decimal places, to see who "
          "tends to place the highest-value individual orders on average.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["customer_name", "average_order_value"],
    solution_sql="SELECT customer_name, ROUND(AVG(amount), 2) AS average_order_value\n"
                 "FROM orders GROUP BY customer_name ORDER BY customer_name;",
    data=dict(orders=ORDERS),
    oracle=lambda orders: [
        (cust, pg_round(
            sum((o["amount"] for o in orders if o["customer_name"] == cust), D("0"))
            / len([o for o in orders if o["customer_name"] == cust]), 2))
        for cust in sorted({o["customer_name"] for o in orders})
    ],
    hints="AVG works inside a GROUP BY exactly like SUM and COUNT do, computing separately within "
          "each group; wrap it in ROUND for a clean two-decimal result.",
))

Q.append(dict(
    title="Price Range per Category", difficulty="Hard", topics=TOPIC, subTopics=GROUP_TOPIC,
    bloomTaxonomy="analyze",
    prose="For each category, show the smallest and largest individual order amount within that "
          "category.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["category", "smallest_order", "largest_order"],
    solution_sql="SELECT category, MIN(amount) AS smallest_order, MAX(amount) AS largest_order\n"
                 "FROM orders GROUP BY category ORDER BY category;",
    data=dict(orders=ORDERS),
    oracle=lambda orders: [
        (cat, min(o["amount"] for o in orders if o["category"] == cat),
         max(o["amount"] for o in orders if o["category"] == cat))
        for cat in sorted({o["category"] for o in orders})
    ],
    hints="MIN and MAX summarize separately within each group exactly like SUM and COUNT do, once "
          "GROUP BY has partitioned the rows.",
))

# ==================== filtering-groups ====================

Q.append(dict(
    title="Customers Who Spent Over 1000", difficulty="Easy", topics=TOPIC, subTopics=HAVING_TOPIC,
    bloomTaxonomy="apply",
    prose="Show only customers whose total spend across all their orders exceeds 1000.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["customer_name", "total_spent"],
    solution_sql="SELECT customer_name, SUM(amount) AS total_spent FROM orders\n"
                 "GROUP BY customer_name HAVING SUM(amount) > 1000 ORDER BY customer_name;",
    data=dict(orders=ORDERS),
    oracle=lambda orders: [
        (cust, total) for cust, total in sorted(
            [(cust, sum((o["amount"] for o in orders if o["customer_name"] == cust), D("0")))
             for cust in {o["customer_name"] for o in orders}]
        ) if total > 1000
    ],
    hints="HAVING runs after GROUP BY has already produced each group's total, so it can filter "
          "directly on SUM(amount), something WHERE cannot do.",
))

Q.append(dict(
    title="Customer Spend Excluding Children's Books", difficulty="Medium", topics=TOPIC, subTopics=HAVING_TOPIC,
    bloomTaxonomy="analyze",
    prose="Exclude Children's category orders entirely before grouping, then show only customers "
          "whose remaining total exceeds 500.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["customer_name", "total_spent"],
    solution_sql="SELECT customer_name, SUM(amount) AS total_spent FROM orders\n"
                 "WHERE category != 'Children'\n"
                 "GROUP BY customer_name HAVING SUM(amount) > 500 ORDER BY customer_name;",
    data=dict(orders=ORDERS),
    oracle=lambda orders: [
        (cust, total) for cust, total in sorted(
            [(cust, sum((o["amount"] for o in orders
                         if o["customer_name"] == cust and o["category"] != "Children"), D("0")))
             for cust in {o["customer_name"] for o in orders
                          if any(o2["category"] != "Children" for o2 in orders if o2["customer_name"] == o["customer_name"])}]
        ) if total > 500
    ],
    hints="WHERE removes rows before grouping starts; HAVING then filters the totals computed from "
          "whatever survived the WHERE clause.",
))

Q.append(dict(
    title="Customers With Three or More Orders", difficulty="Medium", topics=TOPIC, subTopics=HAVING_TOPIC,
    bloomTaxonomy="apply",
    prose="Surface only the customers who placed 3 or more orders in total.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["customer_name", "orders_placed"],
    solution_sql="SELECT customer_name, COUNT(*) AS orders_placed FROM orders\n"
                 "GROUP BY customer_name HAVING COUNT(*) >= 3 ORDER BY customer_name;",
    data=dict(orders=ORDERS),
    oracle=lambda orders: [
        (cust, cnt) for cust, cnt in sorted(
            [(cust, len([o for o in orders if o["customer_name"] == cust]))
             for cust in {o["customer_name"] for o in orders}]
        ) if cnt >= 3
    ],
    hints="HAVING works with any aggregate function, not just SUM; COUNT(*) >= 3 filters on how "
          "many rows landed in each group.",
))

Q.append(dict(
    title="Categories Under 1000 in Revenue", difficulty="Hard", topics=TOPIC, subTopics=HAVING_TOPIC,
    bloomTaxonomy="apply",
    prose="The team wants to see only the product categories that generated less than 1000 in "
          "total revenue, to decide whether to keep stocking them.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["category", "total_revenue"],
    solution_sql="SELECT category, SUM(amount) AS total_revenue FROM orders\n"
                 "GROUP BY category HAVING SUM(amount) < 1000 ORDER BY category;",
    data=dict(orders=ORDERS),
    oracle=lambda orders: [
        (cat, total) for cat, total in sorted(
            [(cat, sum((o["amount"] for o in orders if o["category"] == cat), D("0")))
             for cat in {o["category"] for o in orders}]
        ) if total < 1000
    ],
    hints="HAVING SUM(amount) < 1000 discards any group whose total meets or exceeds that "
          "threshold, keeping only the underperforming categories.",
))

Q.append(dict(
    title="Categories With Above-Average Order Value", difficulty="Hard", topics=TOPIC, subTopics=HAVING_TOPIC,
    bloomTaxonomy="analyze",
    prose="Show categories whose average order value (rounded to two decimals) exceeds 500, "
          "alongside that rounded average.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["category", "avg_order_value"],
    solution_sql="SELECT category, ROUND(AVG(amount), 2) AS avg_order_value FROM orders\n"
                 "GROUP BY category HAVING AVG(amount) > 500 ORDER BY category;",
    data=dict(orders=ORDERS),
    oracle=lambda orders: [
        (cat, pg_round(avg, 2)) for cat, avg in sorted(
            [(cat, sum((o["amount"] for o in orders if o["category"] == cat), D("0"))
              / len([o for o in orders if o["category"] == cat]))
             for cat in {o["category"] for o in orders}]
        ) if avg > 500
    ],
    hints="HAVING can filter on AVG exactly like it filters on SUM or COUNT; the comparison in "
          "HAVING can use the raw AVG(amount) even while SELECT shows the rounded version.",
))

Q.append(dict(
    title="Repeat Customers Outside Children's Books", difficulty="Hard", topics=TOPIC, subTopics=HAVING_TOPIC,
    bloomTaxonomy="analyze",
    prose="Show customers with more than one order, counting only orders outside the Children's "
          "category, ranked by total spend from that filtered set.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["customer_name", "total_spent"],
    solution_sql="SELECT customer_name, SUM(amount) AS total_spent FROM orders\n"
                 "WHERE category != 'Children'\n"
                 "GROUP BY customer_name HAVING COUNT(*) > 1 ORDER BY total_spent DESC;",
    data=dict(orders=ORDERS),
    oracle=lambda orders: sorted(
        [
            (cust, sum((o["amount"] for o in orders if o["customer_name"] == cust and o["category"] != "Children"), D("0")))
            for cust in {o["customer_name"] for o in orders}
            if len([o for o in orders if o["customer_name"] == cust and o["category"] != "Children"]) > 1
        ],
        key=lambda row: row[1], reverse=True,
    ),
    hints="WHERE removes the Children's-category rows first; HAVING COUNT(*) > 1 then keeps only "
          "customers who still have more than one order left after that filter.",
))

Q.append(dict(
    title="Frequent, High-Spending Customers", difficulty="Hard", topics=TOPIC, subTopics=HAVING_TOPIC,
    bloomTaxonomy="analyze",
    prose="Identify customers who both placed at least 2 orders and spent more than 1000 in "
          "total, combining two conditions on two different aggregates in a single HAVING clause.",
    schema_sql=ORDERS_SQL, schema_lines=ORDERS_SCHEMA_LINES,
    header=["customer_name", "order_count", "total_spent"],
    solution_sql="SELECT customer_name, COUNT(*) AS order_count, SUM(amount) AS total_spent FROM orders\n"
                 "GROUP BY customer_name\n"
                 "HAVING COUNT(*) >= 2 AND SUM(amount) > 1000\n"
                 "ORDER BY customer_name;",
    data=dict(orders=ORDERS),
    oracle=lambda orders: [
        (cust, cnt, total) for cust, cnt, total in sorted(
            [(cust, len([o for o in orders if o["customer_name"] == cust]),
              sum((o["amount"] for o in orders if o["customer_name"] == cust), D("0")))
             for cust in {o["customer_name"] for o in orders}]
        ) if cnt >= 2 and total > 1000
    ],
    hints="HAVING accepts a compound condition with AND just like WHERE does, combining a count "
          "threshold and a sum threshold in one filter.",
))

# ==================== combining-aggregation-with-sorting-filtering-and-joins ====================

Q.append(dict(
    title="Revenue by Region", difficulty="Easy", topics=TOPIC, subTopics=COMBINE_TOPIC,
    bloomTaxonomy="apply",
    prose="Region information lives on a separate customers table. Join orders to customers and "
          "show total revenue per region.",
    schema_sql=JOINED_SQL, schema_lines=JOINED_SCHEMA_LINES,
    header=["region", "region_revenue"],
    solution_sql="SELECT c.region, SUM(o.amount) AS region_revenue\n"
                 "FROM orders o JOIN customers c ON o.customer_name = c.customer_name\n"
                 "GROUP BY c.region ORDER BY c.region;",
    data=dict(),
    oracle=lambda: [
        (region, sum((o["amount"] for o in ORDERS if REGION_BY_CUSTOMER[o["customer_name"]] == region), D("0")))
        for region in sorted(set(REGION_BY_CUSTOMER.values()))
    ],
    hints="The JOIN attaches each order to its customer's region before grouping happens, so "
          "GROUP BY c.region can collapse rows by a column that was never on orders to begin with.",
))

Q.append(dict(
    title="Region Revenue, Highest First", difficulty="Medium", topics=TOPIC, subTopics=COMBINE_TOPIC,
    bloomTaxonomy="apply",
    prose="Rank the regions by total revenue, highest-earning region first.",
    schema_sql=JOINED_SQL, schema_lines=JOINED_SCHEMA_LINES,
    header=["region", "region_revenue"],
    solution_sql="SELECT c.region, SUM(o.amount) AS region_revenue\n"
                 "FROM orders o JOIN customers c ON o.customer_name = c.customer_name\n"
                 "GROUP BY c.region ORDER BY region_revenue DESC;",
    data=dict(),
    oracle=lambda: sorted(
        [
            (region, sum((o["amount"] for o in ORDERS if REGION_BY_CUSTOMER[o["customer_name"]] == region), D("0")))
            for region in set(REGION_BY_CUSTOMER.values())
        ],
        key=lambda row: row[1], reverse=True,
    ),
    hints="ORDER BY can reference the column alias defined in SELECT, since sorting happens after "
          "the aggregate values already exist.",
))

Q.append(dict(
    title="Distinct Customers per Region", difficulty="Medium", topics=TOPIC, subTopics=COMBINE_TOPIC,
    bloomTaxonomy="analyze",
    prose="Show how many distinct customers each region has, based on who has actually placed an "
          "order.",
    schema_sql=JOINED_SQL, schema_lines=JOINED_SCHEMA_LINES,
    header=["region", "customer_count"],
    solution_sql="SELECT c.region, COUNT(DISTINCT o.customer_name) AS customer_count\n"
                 "FROM orders o JOIN customers c ON o.customer_name = c.customer_name\n"
                 "GROUP BY c.region ORDER BY c.region;",
    data=dict(),
    oracle=lambda: [
        (region, len({o["customer_name"] for o in ORDERS if REGION_BY_CUSTOMER[o["customer_name"]] == region}))
        for region in sorted(set(REGION_BY_CUSTOMER.values()))
    ],
    hints="COUNT(DISTINCT o.customer_name) counts unique customers per region rather than unique "
          "orders, so a customer with many orders is still only counted once.",
))

Q.append(dict(
    title="Region Revenue for Orders After April 7", difficulty="Hard", topics=TOPIC, subTopics=COMBINE_TOPIC,
    bloomTaxonomy="analyze",
    prose="Restrict the region revenue breakdown to only orders placed after April 7, 2025, "
          "before any grouping happens.",
    schema_sql=JOINED_SQL, schema_lines=JOINED_SCHEMA_LINES,
    header=["region", "region_revenue"],
    solution_sql="SELECT c.region, SUM(o.amount) AS region_revenue\n"
                 "FROM orders o JOIN customers c ON o.customer_name = c.customer_name\n"
                 "WHERE o.order_date > '2025-04-07'\n"
                 "GROUP BY c.region ORDER BY c.region;",
    data=dict(),
    oracle=lambda: [
        (region, sum(
            (o["amount"] for o in ORDERS
             if REGION_BY_CUSTOMER[o["customer_name"]] == region and o["order_date"] > "2025-04-07"),
            D("0")))
        for region in sorted(set(REGION_BY_CUSTOMER.values()))
        if any(REGION_BY_CUSTOMER[o["customer_name"]] == region and o["order_date"] > "2025-04-07" for o in ORDERS)
    ],
    hints="A row-level date filter belongs in WHERE, applied before grouping, exactly the same way "
          "WHERE and GROUP BY always interact.",
))

Q.append(dict(
    title="Multi-Customer Regions After April 7, Ranked", difficulty="Hard", topics=TOPIC, subTopics=COMBINE_TOPIC,
    bloomTaxonomy="analyze",
    prose="Combine every piece: total revenue and distinct customer count per region, counting "
          "only orders after April 7, 2025, keeping only regions with at least two distinct "
          "customers in that window, sorted by revenue highest first.",
    schema_sql=JOINED_SQL, schema_lines=JOINED_SCHEMA_LINES,
    header=["region", "region_revenue", "customer_count"],
    solution_sql="SELECT c.region, SUM(o.amount) AS region_revenue, COUNT(DISTINCT o.customer_name) AS customer_count\n"
                 "FROM orders o JOIN customers c ON o.customer_name = c.customer_name\n"
                 "WHERE o.order_date > '2025-04-07'\n"
                 "GROUP BY c.region\n"
                 "HAVING COUNT(DISTINCT o.customer_name) >= 2\n"
                 "ORDER BY region_revenue DESC;",
    data=dict(),
    oracle=lambda: [
        row for row in sorted(
            [
                (region,
                 sum((o["amount"] for o in ORDERS if REGION_BY_CUSTOMER[o["customer_name"]] == region and o["order_date"] > "2025-04-07"), D("0")),
                 len({o["customer_name"] for o in ORDERS if REGION_BY_CUSTOMER[o["customer_name"]] == region and o["order_date"] > "2025-04-07"}))
                for region in set(REGION_BY_CUSTOMER.values())
            ],
            key=lambda row: row[1], reverse=True,
        ) if row[2] >= 2
    ],
    hints="Each clause runs in a fixed logical order regardless of how it is written: FROM/JOIN, "
          "then WHERE, then GROUP BY, then HAVING, then SELECT, then ORDER BY last.",
))

Q.append(dict(
    title="West and South Categories, Repeat Orders Only", difficulty="Hard", topics=TOPIC, subTopics=COMBINE_TOPIC,
    bloomTaxonomy="analyze",
    prose="Show total revenue and order count per category, counting only orders from customers "
          "in the West and South regions, keeping only categories with more than one order in "
          "that set, sorted by revenue descending.",
    schema_sql=JOINED_SQL, schema_lines=JOINED_SCHEMA_LINES,
    header=["category", "total_revenue", "order_count"],
    solution_sql="SELECT o.category, SUM(o.amount) AS total_revenue, COUNT(*) AS order_count\n"
                 "FROM orders o JOIN customers c ON o.customer_name = c.customer_name\n"
                 "WHERE c.region IN ('West', 'South')\n"
                 "GROUP BY o.category\n"
                 "HAVING COUNT(*) > 1\n"
                 "ORDER BY total_revenue DESC;",
    data=dict(),
    oracle=lambda: [
        row for row in sorted(
            [
                (cat,
                 sum((o["amount"] for o in ORDERS if o["category"] == cat and REGION_BY_CUSTOMER[o["customer_name"]] in ("West", "South")), D("0")),
                 len([o for o in ORDERS if o["category"] == cat and REGION_BY_CUSTOMER[o["customer_name"]] in ("West", "South")]))
                for cat in {o["category"] for o in ORDERS if REGION_BY_CUSTOMER[o["customer_name"]] in ("West", "South")}
            ],
            key=lambda row: row[1], reverse=True,
        ) if row[2] > 1
    ],
    hints="WHERE c.region IN ('West', 'South') removes Aman Gupta's North-region orders before "
          "grouping by category ever starts.",
))

Q.append(dict(
    title="Fiction and Non-Fiction Revenue by Region", difficulty="Hard", topics=TOPIC, subTopics=COMBINE_TOPIC,
    bloomTaxonomy="analyze",
    prose="Show total revenue and order count per region, counting only Fiction and Non-Fiction "
          "orders (excluding Children's books entirely), keeping only regions with more than one "
          "such order, sorted by revenue descending.",
    schema_sql=JOINED_SQL, schema_lines=JOINED_SCHEMA_LINES,
    header=["region", "region_revenue", "order_count"],
    solution_sql="SELECT c.region, SUM(o.amount) AS region_revenue, COUNT(*) AS order_count\n"
                 "FROM orders o JOIN customers c ON o.customer_name = c.customer_name\n"
                 "WHERE o.category IN ('Fiction', 'Non-Fiction')\n"
                 "GROUP BY c.region\n"
                 "HAVING COUNT(*) > 1\n"
                 "ORDER BY region_revenue DESC;",
    data=dict(),
    oracle=lambda: [
        row for row in sorted(
            [
                (region,
                 sum((o["amount"] for o in ORDERS if REGION_BY_CUSTOMER[o["customer_name"]] == region and o["category"] in ("Fiction", "Non-Fiction")), D("0")),
                 len([o for o in ORDERS if REGION_BY_CUSTOMER[o["customer_name"]] == region and o["category"] in ("Fiction", "Non-Fiction")]))
                for region in set(REGION_BY_CUSTOMER.values())
            ],
            key=lambda row: row[1], reverse=True,
        ) if row[2] > 1
    ],
    hints="Excluding Children's books entirely removes Aman Gupta from the result set, since both "
          "of his orders were in that category.",
))

assert len(Q) == 28, len(Q)

for q in Q:
    q["tags"] = f"dbms - {q['subTopics']}"

OUT = "content/Question Bank/Coding Questions/DBMS/4.2 - Aggregation - Coding Questions.xlsx"

if __name__ == "__main__":
    main(Q, OUT)
