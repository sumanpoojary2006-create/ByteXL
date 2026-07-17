"""4.3 - Joins - Coding Questions (34: why joins exist, INNER JOIN, LEFT
JOIN, RIGHT JOIN / FULL OUTER JOIN, self joins, multi-table joins, semi/anti
joins).

Every multi-row solution carries an explicit ORDER BY (ORDER BY was already
taught in 3.2), removing any dependence on PostgreSQL's otherwise-unspecified
row order for joined results. Generic inner_join/left_join/right_join/
full_outer_join helpers below replicate SQL join semantics directly against
the in-memory dataset, so join logic is verified by actual code execution
rather than hand-traced for every question.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from dbms_cqlib import main, sql_insert

TOPIC = "sql-for-data-retrieval-and-analytics"
WHY_TOPIC = "why-joins-exist"
INNER_TOPIC = "inner-join"
LEFT_TOPIC = "left-join"
RIGHT_FULL_TOPIC = "right-join-and-full-outer-join"
SELF_TOPIC = "self-joins"
MULTI_TOPIC = "multitable-joins"
SEMI_ANTI_TOPIC = "semi-joins-and-anti-joins"


def inner_join(left, right, kl, kr):
    return [(l, r) for l in left for r in right if kl(l) == kr(r)]


def left_join(left, right, kl, kr):
    result = []
    for l in left:
        matches = [r for r in right if kl(l) == kr(r)]
        if matches:
            result.extend((l, r) for r in matches)
        else:
            result.append((l, None))
    return result


def right_join(left, right, kl, kr):
    return [(l, r) for (r, l) in left_join(right, left, kr, kl)]


def full_outer_join(left, right, kl, kr):
    result = list(left_join(left, right, kl, kr))
    matched_right = {id(r) for _, r in result if r is not None}
    result.extend((None, r) for r in right if id(r) not in matched_right)
    return result


# ----------------------------- delivery dataset (lessons 1-4, 7) -----------------------------

CUSTOMER_COLUMNS = ["customer_id", "customer_name", "city"]
CUSTOMERS = [
    dict(customer_id=1, customer_name="Aditi Kulkarni", city="Pune"),
    dict(customer_id=2, customer_name="Rohan Das", city="Kolkata"),
    dict(customer_id=3, customer_name="Kavya Nair", city="Kochi"),
    dict(customer_id=4, customer_name="Imran Sheikh", city="Hyderabad"),
    dict(customer_id=5, customer_name="Neha Bhatt", city="Ahmedabad"),
]

RESTAURANT_COLUMNS = ["restaurant_id", "restaurant_name", "city"]
RESTAURANTS = [
    dict(restaurant_id=1, restaurant_name="Pizza Palace", city="Pune"),
    dict(restaurant_id=2, restaurant_name="Sushi Central", city="Kolkata"),
    dict(restaurant_id=3, restaurant_name="Burger Barn", city="Pune"),
    dict(restaurant_id=4, restaurant_name="Taco Town", city="Hyderabad"),
]

ORDER_COLUMNS = ["order_id", "customer_id", "restaurant_id", "amount", "order_date"]
ORDERS = [
    dict(order_id=1, customer_id=1, restaurant_id=1, amount="450.00", order_date="2025-05-01"),
    dict(order_id=2, customer_id=2, restaurant_id=2, amount="620.00", order_date="2025-05-02"),
    dict(order_id=3, customer_id=1, restaurant_id=3, amount="300.00", order_date="2025-05-03"),
    dict(order_id=4, customer_id=3, restaurant_id=1, amount="500.00", order_date="2025-05-04"),
    dict(order_id=5, customer_id=4, restaurant_id=2, amount="275.00", order_date="2025-05-05"),
    dict(order_id=6, customer_id=2, restaurant_id=3, amount="180.00", order_date="2025-05-06"),
]

CUSTOMERS_DDL = """
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT,
    city TEXT
);
"""
RESTAURANTS_DDL = """
CREATE TABLE restaurants (
    restaurant_id INTEGER PRIMARY KEY,
    restaurant_name TEXT,
    city TEXT
);
"""
ORDERS_DDL = """
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(customer_id),
    restaurant_id INTEGER REFERENCES restaurants(restaurant_id),
    amount NUMERIC(10, 2),
    order_date DATE
);
"""
DELIVERY_SQL = (
    CUSTOMERS_DDL.strip("\n") + "\n\n" + sql_insert("customers", CUSTOMER_COLUMNS, CUSTOMERS) + "\n\n"
    + RESTAURANTS_DDL.strip("\n") + "\n\n" + sql_insert("restaurants", RESTAURANT_COLUMNS, RESTAURANTS) + "\n\n"
    + ORDERS_DDL.strip("\n") + "\n\n" + sql_insert("orders", ORDER_COLUMNS, ORDERS)
)
DELIVERY_SCHEMA_LINES = [
    "customers(customer_id INTEGER PK, customer_name TEXT, city TEXT) -- 5 rows; Neha Bhatt has never ordered",
    "restaurants(restaurant_id INTEGER PK, restaurant_name TEXT, city TEXT) -- 4 rows; Taco Town has never received an order",
    "orders(order_id INTEGER PK, customer_id INTEGER FK, restaurant_id INTEGER FK, amount NUMERIC(10,2), order_date DATE) -- 6 rows",
]

# ----------------------------- riders dataset (self-joins) -----------------------------

RIDER_COLUMNS = ["rider_id", "rider_name", "mentor_id"]
RIDERS = [
    dict(rider_id=1, rider_name="Suresh Pillai", mentor_id=None),
    dict(rider_id=2, rider_name="Arjun Verma", mentor_id=None),
    dict(rider_id=3, rider_name="Deepa Krishnan", mentor_id=1),
    dict(rider_id=4, rider_name="Farhan Iqbal", mentor_id=1),
    dict(rider_id=5, rider_name="Nikita Rao", mentor_id=2),
    dict(rider_id=6, rider_name="Om Prakash", mentor_id=3),
]

RIDERS_DDL = """
CREATE TABLE riders (
    rider_id INTEGER PRIMARY KEY,
    rider_name TEXT,
    mentor_id INTEGER REFERENCES riders(rider_id)
);
"""
RIDERS_SQL = RIDERS_DDL.strip("\n") + "\n\n" + sql_insert("riders", RIDER_COLUMNS, RIDERS)
RIDERS_SCHEMA_LINES = [
    "riders(rider_id INTEGER PK, rider_name TEXT, mentor_id INTEGER FK referencing riders.rider_id) -- 6 rows; "
    "Suresh Pillai and Arjun Verma have mentor_id NULL (senior riders with no mentor)",
]

# ----------------------------- multi-table dataset (lesson 6) -----------------------------

MT_CUSTOMER_COLUMNS = ["customer_id", "customer_name"]
MT_CUSTOMERS = [
    dict(customer_id=1, customer_name="Aditi Kulkarni"),
    dict(customer_id=2, customer_name="Rohan Das"),
    dict(customer_id=3, customer_name="Kavya Nair"),
]
MT_RESTAURANT_COLUMNS = ["restaurant_id", "restaurant_name"]
MT_RESTAURANTS = [
    dict(restaurant_id=1, restaurant_name="Pizza Palace"),
    dict(restaurant_id=2, restaurant_name="Sushi Central"),
    dict(restaurant_id=3, restaurant_name="Burger Barn"),
]
MT_RIDER_COLUMNS = ["rider_id", "rider_name"]
MT_RIDERS = [
    dict(rider_id=1, rider_name="Suresh Pillai"),
    dict(rider_id=2, rider_name="Deepa Krishnan"),
    dict(rider_id=3, rider_name="Om Prakash"),
]
MT_ORDER_COLUMNS = ["order_id", "customer_id", "restaurant_id", "rider_id", "amount"]
MT_ORDERS = [
    dict(order_id=1, customer_id=1, restaurant_id=1, rider_id=2, amount="450.00"),
    dict(order_id=2, customer_id=2, restaurant_id=2, rider_id=1, amount="620.00"),
    dict(order_id=3, customer_id=1, restaurant_id=3, rider_id=3, amount="300.00"),
    dict(order_id=4, customer_id=3, restaurant_id=1, rider_id=2, amount="500.00"),
    dict(order_id=5, customer_id=2, restaurant_id=3, rider_id=1, amount="180.00"),
]

MT_CUSTOMERS_DDL = """
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    customer_name TEXT
);
"""
MT_RESTAURANTS_DDL = """
CREATE TABLE restaurants (
    restaurant_id INTEGER PRIMARY KEY,
    restaurant_name TEXT
);
"""
MT_RIDERS_DDL = """
CREATE TABLE riders (
    rider_id INTEGER PRIMARY KEY,
    rider_name TEXT
);
"""
MT_ORDERS_DDL = """
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(customer_id),
    restaurant_id INTEGER REFERENCES restaurants(restaurant_id),
    rider_id INTEGER REFERENCES riders(rider_id),
    amount NUMERIC(10, 2)
);
"""
MULTITABLE_SQL = (
    MT_CUSTOMERS_DDL.strip("\n") + "\n\n" + sql_insert("customers", MT_CUSTOMER_COLUMNS, MT_CUSTOMERS) + "\n\n"
    + MT_RESTAURANTS_DDL.strip("\n") + "\n\n" + sql_insert("restaurants", MT_RESTAURANT_COLUMNS, MT_RESTAURANTS) + "\n\n"
    + MT_RIDERS_DDL.strip("\n") + "\n\n" + sql_insert("riders", MT_RIDER_COLUMNS, MT_RIDERS) + "\n\n"
    + MT_ORDERS_DDL.strip("\n") + "\n\n" + sql_insert("orders", MT_ORDER_COLUMNS, MT_ORDERS)
)
MULTITABLE_SCHEMA_LINES = [
    "customers(customer_id INTEGER PK, customer_name TEXT) -- 3 rows",
    "restaurants(restaurant_id INTEGER PK, restaurant_name TEXT) -- 3 rows",
    "riders(rider_id INTEGER PK, rider_name TEXT) -- 3 rows",
    "orders(order_id INTEGER PK, customer_id INTEGER FK, restaurant_id INTEGER FK, rider_id INTEGER FK, amount NUMERIC(10,2)) -- 5 rows",
]

Q = []

# ==================== why-joins-exist ====================

Q.append(dict(
    title="Order IDs With Customer Names", difficulty="Easy", topics=TOPIC, subTopics=WHY_TOPIC,
    bloomTaxonomy="apply",
    prose="The orders table stores customer_id, not a customer name. Show each order's id, the "
          "matching customer's real name, and the order amount.",
    schema_sql=DELIVERY_SQL, schema_lines=DELIVERY_SCHEMA_LINES,
    header=["order_id", "customer_name", "amount"],
    solution_sql="SELECT orders.order_id, customers.customer_name, orders.amount\n"
                 "FROM orders\n"
                 "JOIN customers ON orders.customer_id = customers.customer_id\n"
                 "ORDER BY orders.order_id;",
    data=dict(),
    oracle=lambda: [
        (o["order_id"], c["customer_name"], o["amount"])
        for o, c in sorted(
            inner_join(ORDERS, CUSTOMERS, lambda o: o["customer_id"], lambda c: c["customer_id"]),
            key=lambda pair: pair[0]["order_id"],
        )
    ],
    hints="JOIN customers ON orders.customer_id = customers.customer_id tells the database exactly "
          "how the two tables relate, matching rows where that id is equal.",
))

Q.append(dict(
    title="Order IDs With Restaurant Names", difficulty="Easy", topics=TOPIC, subTopics=WHY_TOPIC,
    bloomTaxonomy="apply",
    prose="Symmetrically, show each order's id, the matching restaurant's real name, and the "
          "order amount.",
    schema_sql=DELIVERY_SQL, schema_lines=DELIVERY_SCHEMA_LINES,
    header=["order_id", "restaurant_name", "amount"],
    solution_sql="SELECT orders.order_id, restaurants.restaurant_name, orders.amount\n"
                 "FROM orders\n"
                 "JOIN restaurants ON orders.restaurant_id = restaurants.restaurant_id\n"
                 "ORDER BY orders.order_id;",
    data=dict(),
    oracle=lambda: [
        (o["order_id"], r["restaurant_name"], o["amount"])
        for o, r in sorted(
            inner_join(ORDERS, RESTAURANTS, lambda o: o["restaurant_id"], lambda r: r["restaurant_id"]),
            key=lambda pair: pair[0]["order_id"],
        )
    ],
    hints="The same join pattern works against any related table; here it is restaurant_id being "
          "matched instead of customer_id.",
))

Q.append(dict(
    title="Full Order Report With Customer and Restaurant Names", difficulty="Medium", topics=TOPIC, subTopics=WHY_TOPIC,
    bloomTaxonomy="analyze",
    prose="Build the complete report: every order's id, the customer's real name, the "
          "restaurant's real name, and the amount, joining three tables in one query.",
    schema_sql=DELIVERY_SQL, schema_lines=DELIVERY_SCHEMA_LINES,
    header=["order_id", "customer_name", "restaurant_name", "amount"],
    solution_sql="SELECT orders.order_id, customers.customer_name, restaurants.restaurant_name, orders.amount\n"
                 "FROM orders\n"
                 "JOIN customers ON orders.customer_id = customers.customer_id\n"
                 "JOIN restaurants ON orders.restaurant_id = restaurants.restaurant_id\n"
                 "ORDER BY orders.order_id;",
    data=dict(),
    oracle=lambda: [
        (o["order_id"],
         [c for c in CUSTOMERS if c["customer_id"] == o["customer_id"]][0]["customer_name"],
         [r for r in RESTAURANTS if r["restaurant_id"] == o["restaurant_id"]][0]["restaurant_name"],
         o["amount"])
        for o in sorted(ORDERS, key=lambda o: o["order_id"])
    ],
    hints="Chaining two JOIN clauses widens the result twice: first with customer details, then "
          "with restaurant details, producing one flat row per order.",
))

Q.append(dict(
    title="Which Restaurant Did Order 4 Go To", difficulty="Hard", topics=TOPIC, subTopics=WHY_TOPIC,
    bloomTaxonomy="apply",
    prose="Zoya needs a quick check: which restaurant did order 4 go to, by name, not by id?",
    schema_sql=DELIVERY_SQL, schema_lines=DELIVERY_SCHEMA_LINES,
    header=["order_id", "restaurant_name"],
    solution_sql="SELECT orders.order_id, restaurants.restaurant_name\n"
                 "FROM orders\n"
                 "JOIN restaurants ON orders.restaurant_id = restaurants.restaurant_id\n"
                 "WHERE orders.order_id = 4;",
    data=dict(),
    oracle=lambda: [
        (o["order_id"], [r for r in RESTAURANTS if r["restaurant_id"] == o["restaurant_id"]][0]["restaurant_name"])
        for o in ORDERS if o["order_id"] == 4
    ],
    hints="Join first, then filter with WHERE on the order_id, exactly like filtering any other "
          "joined result.",
))

# ==================== inner-join ====================

Q.append(dict(
    title="Customers With Their Orders, Matches Only", difficulty="Easy", topics=TOPIC, subTopics=INNER_TOPIC,
    bloomTaxonomy="understand",
    prose="Join customers to orders and observe which customer never appears in the result, since "
          "an INNER JOIN silently drops rows with no match on either side.",
    schema_sql=DELIVERY_SQL, schema_lines=DELIVERY_SCHEMA_LINES,
    header=["customer_name", "order_id", "amount"],
    solution_sql="SELECT customers.customer_name, orders.order_id, orders.amount\n"
                 "FROM customers\n"
                 "INNER JOIN orders ON customers.customer_id = orders.customer_id\n"
                 "ORDER BY orders.order_id;",
    data=dict(),
    oracle=lambda: [
        (c["customer_name"], o["order_id"], o["amount"])
        for c, o in sorted(
            inner_join(CUSTOMERS, ORDERS, lambda c: c["customer_id"], lambda o: o["customer_id"]),
            key=lambda pair: pair[1]["order_id"],
        )
    ],
    hints="No match means no row in the result on either side; Neha Bhatt, who has never ordered, "
          "will not appear anywhere in this output.",
))

Q.append(dict(
    title="Row Count After Joining Customers to Orders", difficulty="Medium", topics=TOPIC, subTopics=INNER_TOPIC,
    bloomTaxonomy="analyze",
    prose="Count how many rows the inner join between customers and orders actually produces, to "
          "see that it depends on the number of matches, not on either table's own row count.",
    schema_sql=DELIVERY_SQL, schema_lines=DELIVERY_SCHEMA_LINES,
    header=["customers_with_orders"],
    solution_sql="SELECT COUNT(*) AS customers_with_orders\n"
                 "FROM customers\n"
                 "INNER JOIN orders ON customers.customer_id = orders.customer_id;",
    data=dict(),
    oracle=lambda: [(len(inner_join(CUSTOMERS, ORDERS, lambda c: c["customer_id"], lambda o: o["customer_id"])),)],
    hints="A customer with two orders contributes two rows to an inner join; the count is not "
          "capped at 5, the number of customers.",
))

Q.append(dict(
    title="High-Value Orders With Customer and Restaurant Names", difficulty="Medium", topics=TOPIC, subTopics=INNER_TOPIC,
    bloomTaxonomy="analyze",
    prose="Join all three tables, then filter for orders worth more than 400, showing the "
          "customer's name, restaurant's name, and amount.",
    schema_sql=DELIVERY_SQL, schema_lines=DELIVERY_SCHEMA_LINES,
    header=["customer_name", "restaurant_name", "amount"],
    solution_sql="SELECT customers.customer_name, restaurants.restaurant_name, orders.amount\n"
                 "FROM orders\n"
                 "INNER JOIN customers ON orders.customer_id = customers.customer_id\n"
                 "INNER JOIN restaurants ON orders.restaurant_id = restaurants.restaurant_id\n"
                 "WHERE orders.amount > 400\n"
                 "ORDER BY orders.order_id;",
    data=dict(),
    oracle=lambda: [
        ([c for c in CUSTOMERS if c["customer_id"] == o["customer_id"]][0]["customer_name"],
         [r for r in RESTAURANTS if r["restaurant_id"] == o["restaurant_id"]][0]["restaurant_name"],
         o["amount"])
        for o in sorted(ORDERS, key=lambda o: o["order_id"])
        if float(o["amount"]) > 400
    ],
    hints="The joins assemble the full combined view first; only then does WHERE remove the "
          "smaller orders from that already-widened result.",
))

Q.append(dict(
    title="Distinct Restaurants That Have Received an Order", difficulty="Hard", topics=TOPIC, subTopics=INNER_TOPIC,
    bloomTaxonomy="apply",
    prose="List every restaurant that has actually received at least one order, with no "
          "duplicates, just the restaurant names that appear in orders.",
    schema_sql=DELIVERY_SQL, schema_lines=DELIVERY_SCHEMA_LINES,
    header=["restaurant_name"],
    solution_sql="SELECT DISTINCT restaurants.restaurant_name\n"
                 "FROM orders\n"
                 "INNER JOIN restaurants ON orders.restaurant_id = restaurants.restaurant_id\n"
                 "ORDER BY restaurant_name;",
    data=dict(),
    oracle=lambda: [
        (name,) for name in sorted({
            [r for r in RESTAURANTS if r["restaurant_id"] == o["restaurant_id"]][0]["restaurant_name"]
            for o in ORDERS
        })
    ],
    hints="INNER JOIN alone would repeat a restaurant name once per order it received; DISTINCT "
          "collapses that down to one row per restaurant.",
))

Q.append(dict(
    title="Orders From Pune Restaurants", difficulty="Hard", topics=TOPIC, subTopics=INNER_TOPIC,
    bloomTaxonomy="analyze",
    prose="Show the restaurant name and order amount for every order placed at a restaurant "
          "located in Pune.",
    schema_sql=DELIVERY_SQL, schema_lines=DELIVERY_SCHEMA_LINES,
    header=["restaurant_name", "amount"],
    solution_sql="SELECT restaurants.restaurant_name, orders.amount\n"
                 "FROM restaurants\n"
                 "INNER JOIN orders ON restaurants.restaurant_id = orders.restaurant_id\n"
                 "WHERE restaurants.city = 'Pune'\n"
                 "ORDER BY orders.order_id;",
    data=dict(),
    oracle=lambda: [
        (r["restaurant_name"], o["amount"])
        for o in sorted(ORDERS, key=lambda o: o["order_id"])
        for r in RESTAURANTS if r["restaurant_id"] == o["restaurant_id"] and r["city"] == "Pune"
    ],
    hints="Filtering on restaurants.city works exactly like filtering on any joined column, once "
          "the join has attached it to the result.",
))

# ==================== left-join ====================

Q.append(dict(
    title="Every Customer, With Orders if Any", difficulty="Easy", topics=TOPIC, subTopics=LEFT_TOPIC,
    bloomTaxonomy="understand",
    prose="Show every customer, including those with no orders at all, alongside any order id "
          "and amount they have (NULL if none).",
    schema_sql=DELIVERY_SQL, schema_lines=DELIVERY_SCHEMA_LINES,
    header=["customer_name", "order_id", "amount"],
    solution_sql="SELECT customers.customer_name, orders.order_id, orders.amount\n"
                 "FROM customers\n"
                 "LEFT JOIN orders ON customers.customer_id = orders.customer_id\n"
                 "ORDER BY customers.customer_id, orders.order_id;",
    data=dict(),
    oracle=lambda: [
        (c["customer_name"], o["order_id"] if o else None, o["amount"] if o else None)
        for c, o in sorted(
            left_join(CUSTOMERS, ORDERS, lambda c: c["customer_id"], lambda o: o["customer_id"]),
            key=lambda pair: (pair[0]["customer_id"], pair[1]["order_id"] if pair[1] else 0),
        )
    ],
    hints="A LEFT JOIN guarantees every row from customers, the table named first, survives, "
          "matched or not; Neha Bhatt appears once with NULL order columns.",
))

Q.append(dict(
    title="Customers With No Orders At All", difficulty="Medium", topics=TOPIC, subTopics=LEFT_TOPIC,
    bloomTaxonomy="analyze",
    prose="The manager wants to send a welcome discount to registered customers who have never "
          "placed a single order. Find them.",
    schema_sql=DELIVERY_SQL, schema_lines=DELIVERY_SCHEMA_LINES,
    header=["customer_name"],
    solution_sql="SELECT customers.customer_name\n"
                 "FROM customers\n"
                 "LEFT JOIN orders ON customers.customer_id = orders.customer_id\n"
                 "WHERE orders.order_id IS NULL;",
    data=dict(),
    oracle=lambda: [
        (c["customer_name"],)
        for c, o in left_join(CUSTOMERS, ORDERS, lambda c: c["customer_id"], lambda o: o["customer_id"])
        if o is None
    ],
    hints="WHERE orders.order_id IS NULL only keeps rows where the join found nothing to attach, "
          "isolating customers with no matching order.",
))

Q.append(dict(
    title="Restaurants With No Orders At All", difficulty="Medium", topics=TOPIC, subTopics=LEFT_TOPIC,
    bloomTaxonomy="analyze",
    prose="A LEFT JOIN is not symmetric: swapping which table comes first changes which side is "
          "protected. Find every restaurant that has never received a single order.",
    schema_sql=DELIVERY_SQL, schema_lines=DELIVERY_SCHEMA_LINES,
    header=["restaurant_name"],
    solution_sql="SELECT restaurants.restaurant_name\n"
                 "FROM restaurants\n"
                 "LEFT JOIN orders ON restaurants.restaurant_id = orders.restaurant_id\n"
                 "WHERE orders.order_id IS NULL;",
    data=dict(),
    oracle=lambda: [
        (r["restaurant_name"],)
        for r, o in left_join(RESTAURANTS, ORDERS, lambda r: r["restaurant_id"], lambda o: o["restaurant_id"])
        if o is None
    ],
    hints="Putting restaurants first this time protects every restaurant instead of every "
          "customer, answering a completely different business question with the same pattern.",
))

Q.append(dict(
    title="Order Count per Customer, Including Zero", difficulty="Hard", topics=TOPIC, subTopics=LEFT_TOPIC,
    bloomTaxonomy="analyze",
    prose="Show every customer's order count, including customers who legitimately have zero, "
          "ranked from most orders to fewest.",
    schema_sql=DELIVERY_SQL, schema_lines=DELIVERY_SCHEMA_LINES,
    header=["customer_name", "order_count"],
    solution_sql="SELECT customers.customer_name, COUNT(orders.order_id) AS order_count\n"
                 "FROM customers\n"
                 "LEFT JOIN orders ON customers.customer_id = orders.customer_id\n"
                 "GROUP BY customers.customer_name\n"
                 "ORDER BY order_count DESC, customers.customer_name;",
    data=dict(),
    oracle=lambda: sorted(
        [
            (c["customer_name"], len([o for o in ORDERS if o["customer_id"] == c["customer_id"]]))
            for c in CUSTOMERS
        ],
        key=lambda row: (-row[1], row[0]),
    ),
    hints="COUNT(orders.order_id) counts only non-NULL values, so a customer with no matching "
          "orders correctly shows 0 instead of being counted as 1 the way COUNT(*) would.",
))

Q.append(dict(
    title="Pune Restaurants With No Orders", difficulty="Hard", topics=TOPIC, subTopics=LEFT_TOPIC,
    bloomTaxonomy="analyze",
    prose="The manager also wants to know which restaurants in Pune have never received an "
          "order, by name.",
    schema_sql=DELIVERY_SQL, schema_lines=DELIVERY_SCHEMA_LINES,
    header=["restaurant_name"],
    solution_sql="SELECT restaurants.restaurant_name\n"
                 "FROM restaurants\n"
                 "LEFT JOIN orders ON restaurants.restaurant_id = orders.restaurant_id\n"
                 "WHERE restaurants.city = 'Pune' AND orders.order_id IS NULL;",
    data=dict(),
    oracle=lambda: [
        (r["restaurant_name"],)
        for r, o in left_join(RESTAURANTS, ORDERS, lambda r: r["restaurant_id"], lambda o: o["restaurant_id"])
        if o is None and r["city"] == "Pune"
    ],
    allow_empty_result=True,
    hints="Both Pune restaurants, Pizza Palace and Burger Barn, have received at least one order "
          "each, so this specific combination of filters is expected to return nothing at all.",
))

# ==================== right-join-and-full-outer-join ====================

Q.append(dict(
    title="Every Restaurant, via RIGHT JOIN", difficulty="Easy", topics=TOPIC, subTopics=RIGHT_FULL_TOPIC,
    bloomTaxonomy="understand",
    prose="Use RIGHT JOIN to guarantee every restaurant appears in the result, including Taco "
          "Town, which has never received an order.",
    schema_sql=DELIVERY_SQL, schema_lines=DELIVERY_SCHEMA_LINES,
    header=["order_id", "restaurant_name"],
    solution_sql="SELECT orders.order_id, restaurants.restaurant_name\n"
                 "FROM orders\n"
                 "RIGHT JOIN restaurants ON orders.restaurant_id = restaurants.restaurant_id\n"
                 "ORDER BY restaurants.restaurant_id, orders.order_id;",
    data=dict(),
    oracle=lambda: [
        (o["order_id"] if o else None, r["restaurant_name"])
        for o, r in sorted(
            right_join(ORDERS, RESTAURANTS, lambda o: o["restaurant_id"], lambda r: r["restaurant_id"]),
            key=lambda pair: (pair[1]["restaurant_id"], pair[0]["order_id"] if pair[0] else 0),
        )
    ],
    hints="RIGHT JOIN guarantees every row from the table named after it, restaurants here, "
          "survives regardless of a match.",
))

Q.append(dict(
    title="The Same Result, Rewritten as LEFT JOIN", difficulty="Medium", topics=TOPIC, subTopics=RIGHT_FULL_TOPIC,
    bloomTaxonomy="analyze",
    prose="Any RIGHT JOIN can be rewritten as a LEFT JOIN by swapping which table is named first "
          "and swapping the keyword. Produce the identical restaurant report this way instead.",
    schema_sql=DELIVERY_SQL, schema_lines=DELIVERY_SCHEMA_LINES,
    header=["order_id", "restaurant_name"],
    solution_sql="SELECT orders.order_id, restaurants.restaurant_name\n"
                 "FROM restaurants\n"
                 "LEFT JOIN orders ON restaurants.restaurant_id = orders.restaurant_id\n"
                 "ORDER BY restaurants.restaurant_id, orders.order_id;",
    data=dict(),
    oracle=lambda: [
        (o["order_id"] if o else None, r["restaurant_name"])
        for r, o in sorted(
            left_join(RESTAURANTS, ORDERS, lambda r: r["restaurant_id"], lambda o: o["restaurant_id"]),
            key=lambda pair: (pair[0]["restaurant_id"], pair[1]["order_id"] if pair[1] else 0),
        )
    ],
    hints="Swap the table order after FROM and change RIGHT JOIN to LEFT JOIN; the join condition "
          "itself does not need to change.",
))

Q.append(dict(
    title="Every Customer and Every Order Match, via FULL OUTER JOIN", difficulty="Medium", topics=TOPIC, subTopics=RIGHT_FULL_TOPIC,
    bloomTaxonomy="analyze",
    prose="Use FULL OUTER JOIN to keep every customer row and every order row, whether or not "
          "each side finds a match.",
    schema_sql=DELIVERY_SQL, schema_lines=DELIVERY_SCHEMA_LINES,
    header=["customer_name", "order_id"],
    solution_sql="SELECT customers.customer_name, orders.order_id\n"
                 "FROM customers\n"
                 "FULL OUTER JOIN orders ON customers.customer_id = orders.customer_id\n"
                 "ORDER BY customers.customer_id, orders.order_id;",
    data=dict(),
    oracle=lambda: [
        (c["customer_name"] if c else None, o["order_id"] if o else None)
        for c, o in sorted(
            full_outer_join(CUSTOMERS, ORDERS, lambda c: c["customer_id"], lambda o: o["customer_id"]),
            key=lambda pair: (pair[0]["customer_id"] if pair[0] else 999, pair[1]["order_id"] if pair[1] else 0),
        )
    ],
    hints="FULL OUTER JOIN is essentially a LEFT JOIN and a RIGHT JOIN combined; here every order "
          "does have a valid customer, so only the customer side shows any NULL.",
))

Q.append(dict(
    title="Rows Unmatched on Either Side", difficulty="Hard", topics=TOPIC, subTopics=RIGHT_FULL_TOPIC,
    bloomTaxonomy="analyze",
    prose="Surface every row missing a partner on either side of the customers/orders "
          "relationship, in one query.",
    schema_sql=DELIVERY_SQL, schema_lines=DELIVERY_SCHEMA_LINES,
    header=["customer_name", "order_id"],
    solution_sql="SELECT customers.customer_name, orders.order_id\n"
                 "FROM customers\n"
                 "FULL OUTER JOIN orders ON customers.customer_id = orders.customer_id\n"
                 "WHERE customers.customer_id IS NULL OR orders.order_id IS NULL;",
    data=dict(),
    oracle=lambda: [
        (c["customer_name"] if c else None, o["order_id"] if o else None)
        for c, o in full_outer_join(CUSTOMERS, ORDERS, lambda c: c["customer_id"], lambda o: o["customer_id"])
        if c is None or o is None
    ],
    hints="With this dataset, only Neha Bhatt qualifies, since every order does have a matching "
          "customer, but the same WHERE pattern generalizes to datasets with mismatches on both "
          "sides.",
))

Q.append(dict(
    title="Restaurant Audit Report, Ordered by Name", difficulty="Hard", topics=TOPIC, subTopics=RIGHT_FULL_TOPIC,
    bloomTaxonomy="apply",
    prose="Build a single audit report showing every restaurant and every order, with no "
          "restaurant left out even if it has zero orders, sorted alphabetically by restaurant "
          "name.",
    schema_sql=DELIVERY_SQL, schema_lines=DELIVERY_SCHEMA_LINES,
    header=["restaurant_name", "order_id"],
    solution_sql="SELECT restaurants.restaurant_name, orders.order_id\n"
                 "FROM restaurants\n"
                 "LEFT JOIN orders ON restaurants.restaurant_id = orders.restaurant_id\n"
                 "ORDER BY restaurants.restaurant_name, orders.order_id;",
    data=dict(),
    oracle=lambda: [
        (r["restaurant_name"], o["order_id"] if o else None)
        for r, o in sorted(
            left_join(RESTAURANTS, ORDERS, lambda r: r["restaurant_id"], lambda o: o["restaurant_id"]),
            key=lambda pair: (pair[0]["restaurant_name"], pair[1]["order_id"] if pair[1] else 0),
        )
    ],
    hints="Whichever join type guarantees every restaurant appears -- LEFT JOIN with restaurants "
          "named first -- Taco Town will show up with a NULL order_id since it has none.",
))

# ==================== self-joins ====================

Q.append(dict(
    title="Rider and Mentor Name Pairs", difficulty="Easy", topics=TOPIC, subTopics=SELF_TOPIC,
    bloomTaxonomy="understand",
    prose="Produce a list showing each rider's name next to their mentor's name, for riders who "
          "actually have a mentor assigned.",
    schema_sql=RIDERS_SQL, schema_lines=RIDERS_SCHEMA_LINES,
    header=["rider", "mentor"],
    solution_sql="SELECT mentee.rider_name AS rider, mentor.rider_name AS mentor\n"
                 "FROM riders mentee\n"
                 "JOIN riders mentor ON mentee.mentor_id = mentor.rider_id\n"
                 "ORDER BY mentee.rider_id;",
    data=dict(),
    oracle=lambda: [
        (mentee["rider_name"], mentor["rider_name"])
        for mentee, mentor in sorted(
            inner_join(RIDERS, RIDERS, lambda x: x["mentor_id"], lambda x: x["rider_id"]),
            key=lambda pair: pair[0]["rider_id"],
        )
    ],
    hints="riders mentee and riders mentor are the same table referenced twice with two different "
          "aliases, joined on mentee.mentor_id = mentor.rider_id.",
))

Q.append(dict(
    title="Every Rider, Including Those With No Mentor", difficulty="Medium", topics=TOPIC, subTopics=SELF_TOPIC,
    bloomTaxonomy="analyze",
    prose="Show all six riders, with NULL in the mentor column for the senior riders who have no "
          "one assigned above them.",
    schema_sql=RIDERS_SQL, schema_lines=RIDERS_SCHEMA_LINES,
    header=["rider", "mentor"],
    solution_sql="SELECT mentee.rider_name AS rider, mentor.rider_name AS mentor\n"
                 "FROM riders mentee\n"
                 "LEFT JOIN riders mentor ON mentee.mentor_id = mentor.rider_id\n"
                 "ORDER BY mentee.rider_id;",
    data=dict(),
    oracle=lambda: [
        (mentee["rider_name"], mentor["rider_name"] if mentor else None)
        for mentee, mentor in sorted(
            left_join(RIDERS, RIDERS, lambda x: x["mentor_id"], lambda x: x["rider_id"]),
            key=lambda pair: pair[0]["rider_id"],
        )
    ],
    hints="A LEFT JOIN self join keeps every rider row, filling NULL for the mentor side wherever "
          "mentor_id itself is NULL to begin with.",
))

Q.append(dict(
    title="Riders Who Are Mentors Themselves", difficulty="Medium", topics=TOPIC, subTopics=SELF_TOPIC,
    bloomTaxonomy="analyze",
    prose="List, once each, every rider who currently mentors at least one other rider.",
    schema_sql=RIDERS_SQL, schema_lines=RIDERS_SCHEMA_LINES,
    header=["is_a_mentor"],
    solution_sql="SELECT DISTINCT mentor.rider_name AS is_a_mentor\n"
                 "FROM riders mentee\n"
                 "JOIN riders mentor ON mentee.mentor_id = mentor.rider_id\n"
                 "ORDER BY is_a_mentor;",
    data=dict(),
    oracle=lambda: [
        (name,) for name in sorted({
            mentor["rider_name"]
            for mentee, mentor in inner_join(RIDERS, RIDERS, lambda x: x["mentor_id"], lambda x: x["rider_id"])
        })
    ],
    hints="DISTINCT collapses duplicates here, since a rider who mentors two people would "
          "otherwise appear twice.",
))

Q.append(dict(
    title="Farhan Iqbal's Mentorship Siblings", difficulty="Hard", topics=TOPIC, subTopics=SELF_TOPIC,
    bloomTaxonomy="analyze",
    prose="Find every rider who shares the same mentor as Farhan Iqbal, not including Farhan "
          "himself.",
    schema_sql=RIDERS_SQL, schema_lines=RIDERS_SCHEMA_LINES,
    header=["rider_name"],
    solution_sql="SELECT a.rider_name\n"
                 "FROM riders a\n"
                 "JOIN riders b ON a.mentor_id = b.mentor_id\n"
                 "WHERE b.rider_name = 'Farhan Iqbal' AND a.rider_name != 'Farhan Iqbal';",
    data=dict(),
    oracle=lambda: [
        (a["rider_name"],)
        for a, b in inner_join(RIDERS, RIDERS, lambda x: x["mentor_id"], lambda x: x["mentor_id"])
        if b["rider_name"] == "Farhan Iqbal" and a["rider_name"] != "Farhan Iqbal" and a["mentor_id"] is not None
    ],
    hints="Join riders to itself on matching mentor_id values (not rider_id this time), then "
          "filter for Farhan's mentor_id and exclude Farhan's own row from the result.",
))

Q.append(dict(
    title="Mentee Count per Mentor", difficulty="Hard", topics=TOPIC, subTopics=SELF_TOPIC,
    bloomTaxonomy="analyze",
    prose="Show each mentor's name alongside how many mentees they currently have.",
    schema_sql=RIDERS_SQL, schema_lines=RIDERS_SCHEMA_LINES,
    header=["mentor", "mentee_count"],
    solution_sql="SELECT mentor.rider_name AS mentor, COUNT(*) AS mentee_count\n"
                 "FROM riders mentee\n"
                 "JOIN riders mentor ON mentee.mentor_id = mentor.rider_id\n"
                 "GROUP BY mentor.rider_name\n"
                 "ORDER BY mentor.rider_name;",
    data=dict(),
    oracle=lambda: [
        (name, len([1 for mentee, mentor in inner_join(RIDERS, RIDERS, lambda x: x["mentor_id"], lambda x: x["rider_id"]) if mentor["rider_name"] == name]))
        for name in sorted({
            mentor["rider_name"]
            for _, mentor in inner_join(RIDERS, RIDERS, lambda x: x["mentor_id"], lambda x: x["rider_id"])
        })
    ],
    hints="GROUP BY works on a self join exactly like it works on any joined result, once the "
          "mentor's name has been attached to each mentee row.",
))

# ==================== multitable-joins ====================

Q.append(dict(
    title="Every Order With Customer, Restaurant, and Rider Names", difficulty="Easy", topics=TOPIC, subTopics=MULTI_TOPIC,
    bloomTaxonomy="understand",
    prose="A real order touches four tables at once. Show one line per order with the customer's "
          "name, the restaurant's name, the rider's name, and the amount.",
    schema_sql=MULTITABLE_SQL, schema_lines=MULTITABLE_SCHEMA_LINES,
    header=["order_id", "customer_name", "restaurant_name", "rider_name", "amount"],
    solution_sql="SELECT o.order_id, c.customer_name, r.restaurant_name, d.rider_name, o.amount\n"
                 "FROM orders o\n"
                 "JOIN customers c ON o.customer_id = c.customer_id\n"
                 "JOIN restaurants r ON o.restaurant_id = r.restaurant_id\n"
                 "JOIN riders d ON o.rider_id = d.rider_id\n"
                 "ORDER BY o.order_id;",
    data=dict(),
    oracle=lambda: [
        (o["order_id"],
         [c for c in MT_CUSTOMERS if c["customer_id"] == o["customer_id"]][0]["customer_name"],
         [r for r in MT_RESTAURANTS if r["restaurant_id"] == o["restaurant_id"]][0]["restaurant_name"],
         [d for d in MT_RIDERS if d["rider_id"] == o["rider_id"]][0]["rider_name"],
         o["amount"])
        for o in sorted(MT_ORDERS, key=lambda o: o["order_id"])
    ],
    hints="Each JOIN clause attaches one more table to the growing result; by the time all three "
          "have run, every order row carries all three related names.",
))

Q.append(dict(
    title="Orders With an Optional Rider", difficulty="Medium", topics=TOPIC, subTopics=MULTI_TOPIC,
    bloomTaxonomy="analyze",
    prose="Show every order's customer and restaurant names as mandatory matches, but make the "
          "rider name optional, so an order would still appear even without a valid rider "
          "assigned.",
    schema_sql=MULTITABLE_SQL, schema_lines=MULTITABLE_SCHEMA_LINES,
    header=["order_id", "customer_name", "restaurant_name", "rider_name"],
    solution_sql="SELECT o.order_id, c.customer_name, r.restaurant_name, d.rider_name\n"
                 "FROM orders o\n"
                 "JOIN customers c ON o.customer_id = c.customer_id\n"
                 "JOIN restaurants r ON o.restaurant_id = r.restaurant_id\n"
                 "LEFT JOIN riders d ON o.rider_id = d.rider_id\n"
                 "ORDER BY o.order_id;",
    data=dict(),
    oracle=lambda: [
        (o["order_id"],
         [c for c in MT_CUSTOMERS if c["customer_id"] == o["customer_id"]][0]["customer_name"],
         [r for r in MT_RESTAURANTS if r["restaurant_id"] == o["restaurant_id"]][0]["restaurant_name"],
         next((d["rider_name"] for d in MT_RIDERS if d["rider_id"] == o["rider_id"]), None))
        for o in sorted(MT_ORDERS, key=lambda o: o["order_id"])
    ],
    hints="Customer and restaurant stay strict INNER JOIN, since those must always match; only "
          "the rider join is switched to LEFT JOIN to make it optional.",
))

Q.append(dict(
    title="Deliveries and Total Value per Rider", difficulty="Medium", topics=TOPIC, subTopics=MULTI_TOPIC,
    bloomTaxonomy="analyze",
    prose="Show each rider's total number of deliveries and the total value of everything they "
          "have delivered, ranked from most deliveries to fewest.",
    schema_sql=MULTITABLE_SQL, schema_lines=MULTITABLE_SCHEMA_LINES,
    header=["rider_name", "deliveries", "total_delivered_value"],
    solution_sql="SELECT d.rider_name, COUNT(*) AS deliveries, SUM(o.amount) AS total_delivered_value\n"
                 "FROM orders o\n"
                 "JOIN riders d ON o.rider_id = d.rider_id\n"
                 "GROUP BY d.rider_name\n"
                 "ORDER BY deliveries DESC, d.rider_name;",
    data=dict(),
    oracle=lambda: sorted(
        [
            (d["rider_name"],
             len([o for o in MT_ORDERS if o["rider_id"] == d["rider_id"]]),
             "%.2f" % sum(float(o["amount"]) for o in MT_ORDERS if o["rider_id"] == d["rider_id"]))
            for d in MT_RIDERS
        ],
        key=lambda row: (-row[1], row[0]),
    ),
    hints="GROUP BY, COUNT, and SUM all work exactly as they did on a single table, just applied "
          "to the wider result the joins have already produced.",
))

Q.append(dict(
    title="Orders Over 300, Customer and Rider Only", difficulty="Hard", topics=TOPIC, subTopics=MULTI_TOPIC,
    bloomTaxonomy="analyze",
    prose="For every order over 300 in amount, show the customer's name and the rider's name "
          "only, ordered by amount descending.",
    schema_sql=MULTITABLE_SQL, schema_lines=MULTITABLE_SCHEMA_LINES,
    header=["customer_name", "rider_name"],
    solution_sql="SELECT c.customer_name, d.rider_name\n"
                 "FROM orders o\n"
                 "JOIN customers c ON o.customer_id = c.customer_id\n"
                 "JOIN riders d ON o.rider_id = d.rider_id\n"
                 "WHERE o.amount > 300\n"
                 "ORDER BY o.amount DESC;",
    data=dict(),
    oracle=lambda: [
        ([c for c in MT_CUSTOMERS if c["customer_id"] == o["customer_id"]][0]["customer_name"],
         [d for d in MT_RIDERS if d["rider_id"] == o["rider_id"]][0]["rider_name"])
        for o in sorted((o for o in MT_ORDERS if float(o["amount"]) > 300), key=lambda o: float(o["amount"]), reverse=True)
    ],
    hints="Only two of the three related tables are actually needed here, since restaurant name "
          "was not asked for; joining restaurants at all would be unnecessary extra work.",
))

Q.append(dict(
    title="Orders From Burger Barn, With Customer and Rider", difficulty="Hard", topics=TOPIC, subTopics=MULTI_TOPIC,
    bloomTaxonomy="analyze",
    prose="Show the customer name, rider name, and amount for every order placed at Burger Barn.",
    schema_sql=MULTITABLE_SQL, schema_lines=MULTITABLE_SCHEMA_LINES,
    header=["customer_name", "rider_name", "amount"],
    solution_sql="SELECT c.customer_name, d.rider_name, o.amount\n"
                 "FROM orders o\n"
                 "JOIN customers c ON o.customer_id = c.customer_id\n"
                 "JOIN restaurants r ON o.restaurant_id = r.restaurant_id\n"
                 "JOIN riders d ON o.rider_id = d.rider_id\n"
                 "WHERE r.restaurant_name = 'Burger Barn'\n"
                 "ORDER BY o.order_id;",
    data=dict(),
    oracle=lambda: [
        ([c for c in MT_CUSTOMERS if c["customer_id"] == o["customer_id"]][0]["customer_name"],
         [d for d in MT_RIDERS if d["rider_id"] == o["rider_id"]][0]["rider_name"],
         o["amount"])
        for o in sorted(MT_ORDERS, key=lambda o: o["order_id"])
        if [r for r in MT_RESTAURANTS if r["restaurant_id"] == o["restaurant_id"]][0]["restaurant_name"] == "Burger Barn"
    ],
    hints="All four tables can be joined even when the filter only touches one of them; "
          "restaurant_name just happens to be the column WHERE checks.",
))

# ==================== semi-joins-and-anti-joins ====================

Q.append(dict(
    title="Customers Who Have Placed at Least One Order", difficulty="Easy", topics=TOPIC, subTopics=SEMI_ANTI_TOPIC,
    bloomTaxonomy="understand",
    prose="Using an existence check rather than a join that pulls in order columns, list every "
          "customer who has placed at least one order.",
    schema_sql=DELIVERY_SQL, schema_lines=DELIVERY_SCHEMA_LINES,
    header=["customer_name"],
    solution_sql="SELECT customer_name\n"
                 "FROM customers c\n"
                 "WHERE EXISTS (\n"
                 "    SELECT 1 FROM orders o WHERE o.customer_id = c.customer_id\n"
                 ")\n"
                 "ORDER BY customer_name;",
    data=dict(),
    oracle=lambda: [
        (c["customer_name"],) for c in sorted(CUSTOMERS, key=lambda c: c["customer_name"])
        if any(o["customer_id"] == c["customer_id"] for o in ORDERS)
    ],
    hints="EXISTS checks whether the inner query returns at least one row for the current "
          "customer; it never pulls any actual columns from orders into the result, so a customer "
          "with many orders still appears only once.",
))

Q.append(dict(
    title="Customers With No Orders, via NOT EXISTS", difficulty="Medium", topics=TOPIC, subTopics=SEMI_ANTI_TOPIC,
    bloomTaxonomy="analyze",
    prose="Find customers with no orders using a direct existence check instead of a LEFT JOIN "
          "with a NULL filter.",
    schema_sql=DELIVERY_SQL, schema_lines=DELIVERY_SCHEMA_LINES,
    header=["customer_name"],
    solution_sql="SELECT customer_name\n"
                 "FROM customers c\n"
                 "WHERE NOT EXISTS (\n"
                 "    SELECT 1 FROM orders o WHERE o.customer_id = c.customer_id\n"
                 ");",
    data=dict(),
    oracle=lambda: [
        (c["customer_name"],) for c in CUSTOMERS
        if not any(o["customer_id"] == c["customer_id"] for o in ORDERS)
    ],
    hints="NOT EXISTS states the intent directly: keep this customer only if no order references "
          "them, without ever joining a single column from orders into the result.",
))

Q.append(dict(
    title="Customers Who Have Ordered, via IN", difficulty="Medium", topics=TOPIC, subTopics=SEMI_ANTI_TOPIC,
    bloomTaxonomy="apply",
    prose="Write the same 'has ordered' check as a shorter single-column subquery using IN "
          "instead of EXISTS.",
    schema_sql=DELIVERY_SQL, schema_lines=DELIVERY_SCHEMA_LINES,
    header=["customer_name"],
    solution_sql="SELECT customer_name\n"
                 "FROM customers\n"
                 "WHERE customer_id IN (SELECT customer_id FROM orders)\n"
                 "ORDER BY customer_name;",
    data=dict(),
    oracle=lambda: [
        (c["customer_name"],) for c in sorted(CUSTOMERS, key=lambda c: c["customer_name"])
        if c["customer_id"] in {o["customer_id"] for o in ORDERS}
    ],
    hints="When the check only involves a single column with no other condition tying the two "
          "queries together, IN offers a shorter alternative to EXISTS.",
))

Q.append(dict(
    title="Customers With No Orders, via NOT IN", difficulty="Hard", topics=TOPIC, subTopics=SEMI_ANTI_TOPIC,
    bloomTaxonomy="analyze",
    prose="Write the 'has never ordered' check using NOT IN, being careful to filter out any NULL "
          "customer_id from the subquery first so the comparison stays safe.",
    schema_sql=DELIVERY_SQL, schema_lines=DELIVERY_SCHEMA_LINES,
    header=["customer_name"],
    solution_sql="SELECT customer_name\n"
                 "FROM customers\n"
                 "WHERE customer_id NOT IN (SELECT customer_id FROM orders WHERE customer_id IS NOT NULL);",
    data=dict(),
    oracle=lambda: [
        (c["customer_name"],) for c in CUSTOMERS
        if c["customer_id"] not in {o["customer_id"] for o in ORDERS if o["customer_id"] is not None}
    ],
    hints="If even one NULL slipped into the list NOT IN compares against, the entire condition "
          "would return no rows for every customer; filtering with IS NOT NULL first avoids that "
          "trap, which is why NOT EXISTS is generally the safer default.",
))

Q.append(dict(
    title="Restaurants With No Orders, via NOT EXISTS", difficulty="Hard", topics=TOPIC, subTopics=SEMI_ANTI_TOPIC,
    bloomTaxonomy="apply",
    prose="Find every restaurant that has never received an order, using an existence check "
          "rather than a LEFT JOIN.",
    schema_sql=DELIVERY_SQL, schema_lines=DELIVERY_SCHEMA_LINES,
    header=["restaurant_name"],
    solution_sql="SELECT restaurant_name\n"
                 "FROM restaurants r\n"
                 "WHERE NOT EXISTS (\n"
                 "    SELECT 1 FROM orders o WHERE o.restaurant_id = r.restaurant_id\n"
                 ");",
    data=dict(),
    oracle=lambda: [
        (r["restaurant_name"],) for r in RESTAURANTS
        if not any(o["restaurant_id"] == r["restaurant_id"] for o in ORDERS)
    ],
    hints="The same NOT EXISTS pattern used for customers works identically against restaurants, "
          "just checking restaurant_id instead of customer_id.",
))

assert len(Q) == 34, len(Q)

for q in Q:
    q["tags"] = f"dbms - {q['subTopics']}"

OUT = "content/Question Bank/Coding Questions/DBMS/4.3 - Joins - Coding Questions.xlsx"

if __name__ == "__main__":
    main(Q, OUT)
