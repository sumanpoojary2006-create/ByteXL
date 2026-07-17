"""4.1 - Transforming Data - Coding Questions (30: string functions, numeric
functions, date/time functions, NULL-handling functions, CASE).

Design notes:
- Numeric columns are modeled as decimal.Decimal (never float) so rounding and
  scale exactly match PostgreSQL's NUMERIC type. ROUND uses ROUND_HALF_UP
  (round half away from zero), matching Postgres's numeric rounding
  convention, not Python's default banker's-rounding. CEIL/FLOOR/ROUND all
  return a value re-quantized to the correct output scale (0 decimal places
  for CEIL/FLOOR, N places for ROUND(x, N)), since PostgreSQL's numeric type
  displays trailing zeros according to its scale (e.g. ROUND(x, 2) always
  shows two decimal digits, even '600.00', not '600').
- NOW() / CURRENT_DATE / AGE(NOW(), ...) are never used in a graded solution,
  since their result depends on when the query actually runs and could never
  match a fixed expected output. The date/time lesson's "how long ago"
  concept is instead tested with EXTRACT and arithmetic against a fixed
  literal date/timestamp, which is fully deterministic while exercising the
  same mechanics (interval arithmetic, date subtraction, EXTRACT).
"""
import decimal
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from dbms_cqlib import main, sql_insert

D = decimal.Decimal


def pg_round(value, places):
    """Round like PostgreSQL's numeric ROUND: half away from zero, output
    re-quantized to exactly `places` decimal digits."""
    quantum = D(1).scaleb(-places)
    return value.quantize(quantum, rounding=decimal.ROUND_HALF_UP)


def pg_ceil(value):
    return value.to_integral_value(rounding=decimal.ROUND_CEILING)


def pg_floor(value):
    return value.to_integral_value(rounding=decimal.ROUND_FLOOR)


TOPIC = "sql-for-data-retrieval-and-analytics"
STRING_TOPIC = "string-functions"
NUMERIC_TOPIC = "numeric-functions"
DATE_TOPIC = "date-and-time-functions"
NULL_TOPIC = "nullhandling-functions"
CASE_TOPIC = "conditional-logic"

# ----------------------------- restaurants dataset -----------------------------

RESTAURANT_COLUMNS = ["restaurant_id", "branch_name", "locality", "manager_email"]
RESTAURANTS = [
    dict(restaurant_id=1, branch_name="Spice Route", locality="Koramangala", manager_email="  RAVI.KUMAR@SPICEROUTE.COM  "),
    dict(restaurant_id=2, branch_name="SPICE ROUTE", locality="Indiranagar", manager_email="anita.rao@spiceroute.com"),
    dict(restaurant_id=3, branch_name="Curry Leaf", locality="Whitefield", manager_email="sunil.d@curryleaf.com"),
    dict(restaurant_id=4, branch_name="curry leaf", locality="HSR Layout", manager_email="  priya.n@curryleaf.com"),
    dict(restaurant_id=5, branch_name="Tandoor Express", locality="Jayanagar", manager_email="kiran.m@tandoorexpress.com  "),
]

RESTAURANTS_DDL = """
CREATE TABLE restaurants (
    restaurant_id INTEGER PRIMARY KEY,
    branch_name TEXT,
    locality TEXT,
    manager_email TEXT
);
"""
RESTAURANTS_SQL = RESTAURANTS_DDL.strip("\n") + "\n\n" + sql_insert("restaurants", RESTAURANT_COLUMNS, RESTAURANTS)
RESTAURANTS_SCHEMA_LINES = [
    "restaurants(restaurant_id INTEGER PK, branch_name TEXT, locality TEXT, manager_email TEXT) -- 5 rows; "
    "branch_name has inconsistent casing, manager_email has leading/trailing spaces on some rows",
]

# ----------------------------- products dataset -----------------------------

PRODUCT_COLUMNS = ["product_id", "product_name", "cost_price", "selling_price", "stock_weight_kg"]
PRODUCTS = [
    dict(product_id=1, product_name="Wireless Mouse", cost_price=D("349.6789"), selling_price=D("599.9950"), stock_weight_kg=D("0.1450")),
    dict(product_id=2, product_name="USB-C Cable", cost_price=D("89.3333"), selling_price=D("149.0000"), stock_weight_kg=D("0.0500")),
    dict(product_id=3, product_name="Bluetooth Speaker", cost_price=D("1120.4567"), selling_price=D("1899.9900"), stock_weight_kg=D("0.6200")),
    dict(product_id=4, product_name="Laptop Stand", cost_price=D("610.1111"), selling_price=D("999.5000"), stock_weight_kg=D("1.3000")),
    dict(product_id=5, product_name="Webcam", cost_price=D("780.8888"), selling_price=D("-1249.0000"), stock_weight_kg=D("0.2100")),
]

PRODUCTS_DDL = """
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT,
    cost_price NUMERIC(10, 4),
    selling_price NUMERIC(10, 4),
    stock_weight_kg NUMERIC(10, 4)
);
"""
PRODUCTS_SQL = PRODUCTS_DDL.strip("\n") + "\n\n" + sql_insert("products", PRODUCT_COLUMNS, PRODUCTS)
PRODUCTS_SCHEMA_LINES = [
    "products(product_id INTEGER PK, product_name TEXT, cost_price NUMERIC(10,4), "
    "selling_price NUMERIC(10,4), stock_weight_kg NUMERIC(10,4)) -- 5 rows; the Webcam's "
    "selling_price is a negative data-entry mistake",
]

# ----------------------------- appointments dataset -----------------------------

APPOINTMENT_COLUMNS = ["appointment_id", "patient_name", "visit_time"]
APPOINTMENTS = [
    dict(appointment_id=1, patient_name="Rohit Nair", visit_time="2025-01-10 09:15:00"),
    dict(appointment_id=2, patient_name="Sanya Kapoor", visit_time="2025-02-03 14:30:00"),
    dict(appointment_id=3, patient_name="Faisal Ahmed", visit_time="2025-02-20 11:00:00"),
    dict(appointment_id=4, patient_name="Lakshmi Iyer", visit_time="2025-03-05 16:45:00"),
    dict(appointment_id=5, patient_name="Devika Menon", visit_time="2025-03-18 10:00:00"),
]

APPOINTMENTS_DDL = """
CREATE TABLE appointments (
    appointment_id INTEGER PRIMARY KEY,
    patient_name TEXT,
    visit_time TIMESTAMP
);
"""
APPOINTMENTS_SQL = APPOINTMENTS_DDL.strip("\n") + "\n\n" + sql_insert("appointments", APPOINTMENT_COLUMNS, APPOINTMENTS)
APPOINTMENTS_SCHEMA_LINES = [
    "appointments(appointment_id INTEGER PK, patient_name TEXT, visit_time TIMESTAMP) -- 5 rows",
]

import datetime as _dt


def _parse_ts(s):
    return _dt.datetime.strptime(s, "%Y-%m-%d %H:%M:%S")


# ----------------------------- employees dataset -----------------------------

EMPLOYEE_COLUMNS = ["employee_id", "full_name", "primary_phone", "secondary_phone", "manager_id"]
EMPLOYEES = [
    dict(employee_id=1, full_name="Neha Choudhary", primary_phone="9811100001", secondary_phone="9811100002", manager_id=None),
    dict(employee_id=2, full_name="Rahul Bose", primary_phone="9811100003", secondary_phone=None, manager_id=1),
    dict(employee_id=3, full_name="Ayesha Khan", primary_phone=None, secondary_phone=None, manager_id=1),
    dict(employee_id=4, full_name="Manoj Tiwari", primary_phone="9811100005", secondary_phone="9811100005", manager_id=2),
    dict(employee_id=5, full_name="Simran Kaur", primary_phone="9811100006", secondary_phone=None, manager_id=2),
]

EMPLOYEES_DDL = """
CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,
    full_name TEXT,
    primary_phone TEXT,
    secondary_phone TEXT,
    manager_id INTEGER
);
"""
EMPLOYEES_SQL = EMPLOYEES_DDL.strip("\n") + "\n\n" + sql_insert("employees", EMPLOYEE_COLUMNS, EMPLOYEES)
EMPLOYEES_SCHEMA_LINES = [
    "employees(employee_id INTEGER PK, full_name TEXT, primary_phone TEXT, secondary_phone TEXT, "
    "manager_id INTEGER) -- 5 rows; Manoj's secondary_phone duplicates his primary_phone by mistake",
]

# ----------------------------- members dataset -----------------------------

MEMBER_COLUMNS = ["member_id", "full_name", "visits_this_month", "membership_type"]
MEMBERS = [
    dict(member_id=1, full_name="Karan Malhotra", visits_this_month=18, membership_type="premium"),
    dict(member_id=2, full_name="Nisha Verma", visits_this_month=4, membership_type="standard"),
    dict(member_id=3, full_name="Aakash Jain", visits_this_month=11, membership_type="standard"),
    dict(member_id=4, full_name="Ritu Sharma", visits_this_month=0, membership_type="premium"),
    dict(member_id=5, full_name="Yusuf Ali", visits_this_month=9, membership_type="basic"),
]

MEMBERS_DDL = """
CREATE TABLE members (
    member_id INTEGER PRIMARY KEY,
    full_name TEXT,
    visits_this_month INTEGER,
    membership_type TEXT
);
"""
MEMBERS_SQL = MEMBERS_DDL.strip("\n") + "\n\n" + sql_insert("members", MEMBER_COLUMNS, MEMBERS)
MEMBERS_SCHEMA_LINES = [
    "members(member_id INTEGER PK, full_name TEXT, visits_this_month INTEGER, membership_type TEXT) -- 5 rows",
]

Q = []

# ==================== string-functions ====================

Q.append(dict(
    title="Combined Restaurant Display Name", difficulty="Easy", topics=TOPIC, subTopics=STRING_TOPIC,
    bloomTaxonomy="apply",
    prose="The delivery app wants branch name and locality shown as one combined string, like "
          "'Spice Route - Koramangala', for every restaurant.",
    schema_sql=RESTAURANTS_SQL, schema_lines=RESTAURANTS_SCHEMA_LINES,
    header=["display_name"],
    solution_sql="SELECT CONCAT(branch_name, ' - ', locality) AS display_name FROM restaurants;",
    data=dict(restaurants=RESTAURANTS),
    oracle=lambda restaurants: [(f'{r["branch_name"]} - {r["locality"]}',) for r in restaurants],
    hints="CONCAT glues its arguments together into one string; a literal ' - ' inserted between "
          "them becomes the separator.",
))

Q.append(dict(
    title="Shout Case and Quiet Case", difficulty="Easy", topics=TOPIC, subTopics=STRING_TOPIC,
    bloomTaxonomy="apply",
    prose="Show each branch_name alongside an all-uppercase and an all-lowercase version of "
          "itself, so inconsistent typing no longer matters for comparisons.",
    schema_sql=RESTAURANTS_SQL, schema_lines=RESTAURANTS_SCHEMA_LINES,
    header=["branch_name", "shout_case", "quiet_case"],
    solution_sql="SELECT branch_name, UPPER(branch_name) AS shout_case, LOWER(branch_name) AS quiet_case "
                 "FROM restaurants;",
    data=dict(restaurants=RESTAURANTS),
    oracle=lambda restaurants: [
        (r["branch_name"], r["branch_name"].upper(), r["branch_name"].lower()) for r in restaurants
    ],
    hints="UPPER and LOWER force text into one case so 'Spice Route' and 'SPICE ROUTE' collapse "
          "into the same value once compared consistently.",
))

Q.append(dict(
    title="Cleaned Email With Length Comparison", difficulty="Medium", topics=TOPIC, subTopics=STRING_TOPIC,
    bloomTaxonomy="analyze",
    prose="For restaurants 1, 4, and 5, show the raw manager_email, the trimmed version, and both "
          "the raw and trimmed character counts, to make the hidden whitespace visible.",
    schema_sql=RESTAURANTS_SQL, schema_lines=RESTAURANTS_SCHEMA_LINES,
    header=["manager_email", "cleaned_email", "raw_length", "clean_length"],
    solution_sql="SELECT manager_email, TRIM(manager_email) AS cleaned_email, "
                 "LENGTH(manager_email) AS raw_length, LENGTH(TRIM(manager_email)) AS clean_length "
                 "FROM restaurants WHERE restaurant_id IN (1, 4, 5) ORDER BY restaurant_id;",
    data=dict(restaurants=RESTAURANTS),
    oracle=lambda restaurants: [
        (r["manager_email"], r["manager_email"].strip(), len(r["manager_email"]), len(r["manager_email"].strip()))
        for r in sorted(restaurants, key=lambda r: r["restaurant_id"])
        if r["restaurant_id"] in (1, 4, 5)
    ],
    hints="TRIM removes whitespace from both ends; LENGTH counts characters, so comparing "
          "raw_length against clean_length reveals exactly how much whitespace was hiding there.",
))

Q.append(dict(
    title="Extract the Email Domain", difficulty="Medium", topics=TOPIC, subTopics=STRING_TOPIC,
    bloomTaxonomy="analyze",
    prose="Meera needs just the domain of each manager's email (everything after the @), to check "
          "which restaurants still use the old curryleaf.com address.",
    schema_sql=RESTAURANTS_SQL, schema_lines=RESTAURANTS_SCHEMA_LINES,
    header=["manager_email", "domain"],
    solution_sql="SELECT manager_email,\n"
                 "       SUBSTRING(TRIM(manager_email) FROM POSITION('@' IN TRIM(manager_email)) + 1) AS domain\n"
                 "FROM restaurants ORDER BY restaurant_id;",
    data=dict(restaurants=RESTAURANTS),
    oracle=lambda restaurants: [
        (r["manager_email"], r["manager_email"].strip().split("@", 1)[1])
        for r in sorted(restaurants, key=lambda r: r["restaurant_id"])
    ],
    hints="POSITION('@' IN ...) finds where @ sits in the cleaned email; SUBSTRING ... FROM starts "
          "pulling characters one position after it, giving back everything from the domain onward.",
))

Q.append(dict(
    title="Cleaned Manager Directory", difficulty="Hard", topics=TOPIC, subTopics=STRING_TOPIC,
    bloomTaxonomy="apply",
    prose="Head office wants the trimmed, lowercase email for every restaurant, aliased as "
          "contact_email, so every address reads the same clean way regardless of how it was "
          "originally typed.",
    schema_sql=RESTAURANTS_SQL, schema_lines=RESTAURANTS_SCHEMA_LINES,
    header=["contact_email"],
    solution_sql="SELECT LOWER(TRIM(manager_email)) AS contact_email FROM restaurants ORDER BY restaurant_id;",
    data=dict(restaurants=RESTAURANTS),
    oracle=lambda restaurants: [
        (r["manager_email"].strip().lower(),) for r in sorted(restaurants, key=lambda r: r["restaurant_id"])
    ],
    hints="Nest the functions: TRIM first removes the stray spaces, then LOWER normalizes whatever "
          "case is left.",
))

Q.append(dict(
    title="Shouted Display Name", difficulty="Hard", topics=TOPIC, subTopics=STRING_TOPIC,
    bloomTaxonomy="analyze",
    prose="Build an all-uppercase version of the combined 'branch - locality' display name for "
          "every restaurant, in one pass.",
    schema_sql=RESTAURANTS_SQL, schema_lines=RESTAURANTS_SCHEMA_LINES,
    header=["shout_display"],
    solution_sql="SELECT UPPER(CONCAT(branch_name, ' - ', locality)) AS shout_display "
                 "FROM restaurants ORDER BY restaurant_id;",
    data=dict(restaurants=RESTAURANTS),
    oracle=lambda restaurants: [
        (f'{r["branch_name"]} - {r["locality"]}'.upper(),)
        for r in sorted(restaurants, key=lambda r: r["restaurant_id"])
    ],
    hints="CONCAT and UPPER can nest just like any other expressions: build the combined string "
          "first, then uppercase the whole result.",
))

# ==================== numeric-functions ====================

Q.append(dict(
    title="Customer-Ready Selling Price", difficulty="Easy", topics=TOPIC, subTopics=NUMERIC_TOPIC,
    bloomTaxonomy="apply",
    prose="A price tag needs a whole-number price, not the over-precise stored value. Show every "
          "product's selling_price rounded to the nearest whole number.",
    schema_sql=PRODUCTS_SQL, schema_lines=PRODUCTS_SCHEMA_LINES,
    header=["product_name", "selling_price", "rounded_price"],
    solution_sql="SELECT product_name, selling_price, ROUND(selling_price, 0) AS rounded_price FROM products "
                 "ORDER BY product_id;",
    data=dict(products=PRODUCTS),
    oracle=lambda products: [
        (p["product_name"], p["selling_price"], pg_round(p["selling_price"], 0))
        for p in sorted(products, key=lambda p: p["product_id"])
    ],
    hints="ROUND(value, 0) rounds to the nearest whole number; the second argument controls how "
          "many decimal places survive.",
))

Q.append(dict(
    title="Boxes Needed and Full Kilograms Only", difficulty="Easy", topics=TOPIC, subTopics=NUMERIC_TOPIC,
    bloomTaxonomy="apply",
    prose="For shipping, Arjun needs to know how many 1kg boxes each product's weight requires if "
          "rounding up (no leftover stock behind), and separately how many complete kilograms it "
          "weighs if the leftover fraction is simply discarded.",
    schema_sql=PRODUCTS_SQL, schema_lines=PRODUCTS_SCHEMA_LINES,
    header=["product_name", "stock_weight_kg", "boxes_needed_if_1kg_each", "full_kg_only"],
    solution_sql="SELECT product_name, stock_weight_kg,\n"
                 "       CEIL(stock_weight_kg) AS boxes_needed_if_1kg_each,\n"
                 "       FLOOR(stock_weight_kg) AS full_kg_only\n"
                 "FROM products ORDER BY product_id;",
    data=dict(products=PRODUCTS),
    oracle=lambda products: [
        (p["product_name"], p["stock_weight_kg"], pg_ceil(p["stock_weight_kg"]), pg_floor(p["stock_weight_kg"]))
        for p in sorted(products, key=lambda p: p["product_id"])
    ],
    hints="CEIL always rounds up to the next whole number; FLOOR always rounds down, discarding "
          "any fraction.",
))

Q.append(dict(
    title="Positive Magnitude of a Negative Price", difficulty="Medium", topics=TOPIC, subTopics=NUMERIC_TOPIC,
    bloomTaxonomy="apply",
    prose="One product's selling_price is negative, a data-entry mistake from a refund adjustment. "
          "Show that product's name, its raw selling_price, and its distance from zero.",
    schema_sql=PRODUCTS_SQL, schema_lines=PRODUCTS_SCHEMA_LINES,
    header=["product_name", "selling_price", "positive_price"],
    solution_sql="SELECT product_name, selling_price, ABS(selling_price) AS positive_price "
                 "FROM products WHERE selling_price < 0;",
    data=dict(products=PRODUCTS),
    oracle=lambda products: [
        (p["product_name"], p["selling_price"], abs(p["selling_price"]))
        for p in products if p["selling_price"] < 0
    ],
    hints="ABS strips the sign off a number; a negative selling_price is exactly the kind of value "
          "that should never occur, which is what makes it worth flagging.",
))

Q.append(dict(
    title="Which Product IDs Pack Evenly Into Sixes", difficulty="Medium", topics=TOPIC, subTopics=NUMERIC_TOPIC,
    bloomTaxonomy="apply",
    prose="Show each product_id alongside the remainder when divided by 6, to see which IDs would "
          "divide evenly into groups of 6 (a remainder of 0) and which would not.",
    schema_sql=PRODUCTS_SQL, schema_lines=PRODUCTS_SCHEMA_LINES,
    header=["product_id", "product_name", "remainder_when_packed_in_sixes"],
    solution_sql="SELECT product_id, product_name, product_id % 6 AS remainder_when_packed_in_sixes "
                 "FROM products ORDER BY product_id;",
    data=dict(products=PRODUCTS),
    oracle=lambda products: [
        (p["product_id"], p["product_name"], p["product_id"] % 6)
        for p in sorted(products, key=lambda p: p["product_id"])
    ],
    hints="The % operator returns the remainder of a division; it works the same on a column as it "
          "does on two plain numbers.",
))

Q.append(dict(
    title="Profit Margin Report", difficulty="Hard", topics=TOPIC, subTopics=NUMERIC_TOPIC,
    bloomTaxonomy="analyze",
    prose="Arjun needs a margin report: for every product, show the product name and the profit "
          "margin (selling_price minus cost_price) rounded to two decimal places, aliased as "
          "margin.",
    schema_sql=PRODUCTS_SQL, schema_lines=PRODUCTS_SCHEMA_LINES,
    header=["product_name", "margin"],
    solution_sql="SELECT product_name, ROUND(selling_price - cost_price, 2) AS margin FROM products "
                 "ORDER BY product_id;",
    data=dict(products=PRODUCTS),
    oracle=lambda products: [
        (p["product_name"], pg_round(p["selling_price"] - p["cost_price"], 2))
        for p in sorted(products, key=lambda p: p["product_id"])
    ],
    hints="Subtraction between two columns is just another expression; wrap it in ROUND(..., 2) "
          "exactly like rounding any other value. The webcam's margin should come out sharply "
          "negative, one more sign its price needs a manual fix.",
))

Q.append(dict(
    title="Rounded Price Magnitude", difficulty="Hard", topics=TOPIC, subTopics=NUMERIC_TOPIC,
    bloomTaxonomy="analyze",
    prose="Combine two numeric functions in one pass: show each product's selling_price magnitude "
          "(ignoring any negative sign), rounded to the nearest whole number.",
    schema_sql=PRODUCTS_SQL, schema_lines=PRODUCTS_SCHEMA_LINES,
    header=["product_name", "rounded_magnitude"],
    solution_sql="SELECT product_name, ROUND(ABS(selling_price), 0) AS rounded_magnitude FROM products "
                 "ORDER BY product_id;",
    data=dict(products=PRODUCTS),
    oracle=lambda products: [
        (p["product_name"], pg_round(abs(p["selling_price"]), 0))
        for p in sorted(products, key=lambda p: p["product_id"])
    ],
    hints="Functions can nest: ABS(selling_price) resolves to a plain positive number first, and "
          "ROUND(..., 0) is then applied to that result.",
))

# ==================== date-and-time-functions ====================
# NOW()/CURRENT_DATE are never used as the graded solution, since their value
# depends on when the query runs; deterministic EXTRACT and fixed-literal
# arithmetic exercise the same mechanics without that risk.

Q.append(dict(
    title="Hour of Day for Each Visit", difficulty="Easy", topics=TOPIC, subTopics=DATE_TOPIC,
    bloomTaxonomy="apply",
    prose="Divya wants to know which hour of the day patients tend to book, without caring about "
          "the specific date at all.",
    schema_sql=APPOINTMENTS_SQL, schema_lines=APPOINTMENTS_SCHEMA_LINES,
    header=["patient_name", "hour_of_day"],
    solution_sql="SELECT patient_name, EXTRACT(HOUR FROM visit_time) AS hour_of_day "
                 "FROM appointments ORDER BY appointment_id;",
    data=dict(appointments=APPOINTMENTS),
    oracle=lambda appointments: [
        (a["patient_name"], _parse_ts(a["visit_time"]).hour)
        for a in sorted(appointments, key=lambda a: a["appointment_id"])
    ],
    hints="EXTRACT(HOUR FROM timestamp) pulls out just the hour, in 24-hour format.",
))

Q.append(dict(
    title="Day of the Week for Each Visit", difficulty="Easy", topics=TOPIC, subTopics=DATE_TOPIC,
    bloomTaxonomy="apply",
    prose="Show which day of the week each appointment falls on, as PostgreSQL's numbering: 0 for "
          "Sunday through 6 for Saturday.",
    schema_sql=APPOINTMENTS_SQL, schema_lines=APPOINTMENTS_SCHEMA_LINES,
    header=["patient_name", "day_of_week_number"],
    solution_sql="SELECT patient_name, EXTRACT(DOW FROM visit_time) AS day_of_week_number "
                 "FROM appointments ORDER BY appointment_id;",
    data=dict(appointments=APPOINTMENTS),
    oracle=lambda appointments: [
        (a["patient_name"], (_parse_ts(a["visit_time"]).isoweekday() % 7))
        for a in sorted(appointments, key=lambda a: a["appointment_id"])
    ],
    hints="EXTRACT(DOW FROM timestamp) returns 0 for Sunday through 6 for Saturday, unlike Python's "
          "own Monday-first weekday numbering.",
))

Q.append(dict(
    title="Suggested Follow-Up Date", difficulty="Medium", topics=TOPIC, subTopics=DATE_TOPIC,
    bloomTaxonomy="apply",
    prose="Generate a suggested follow-up date for every patient, exactly 7 days after their "
          "recorded visit_time.",
    schema_sql=APPOINTMENTS_SQL, schema_lines=APPOINTMENTS_SCHEMA_LINES,
    header=["patient_name", "suggested_followup"],
    solution_sql="SELECT patient_name, visit_time + INTERVAL '7 days' AS suggested_followup "
                 "FROM appointments ORDER BY appointment_id;",
    data=dict(appointments=APPOINTMENTS),
    oracle=lambda appointments: [
        (a["patient_name"], (_parse_ts(a["visit_time"]) + _dt.timedelta(days=7)).strftime("%Y-%m-%d %H:%M:%S"))
        for a in sorted(appointments, key=lambda a: a["appointment_id"])
    ],
    hints="Adding an INTERVAL directly to a timestamp shifts it forward by exactly that span; the "
          "time-of-day portion carries over unchanged.",
))

Q.append(dict(
    title="Year, Month, and Day of Each Visit", difficulty="Medium", topics=TOPIC, subTopics=DATE_TOPIC,
    bloomTaxonomy="apply",
    prose="Break each visit_time into its calendar year, month number, and day of month, all in "
          "one row per appointment.",
    schema_sql=APPOINTMENTS_SQL, schema_lines=APPOINTMENTS_SCHEMA_LINES,
    header=["patient_name", "visit_year", "visit_month", "visit_day"],
    solution_sql="SELECT patient_name,\n"
                 "       EXTRACT(YEAR FROM visit_time) AS visit_year,\n"
                 "       EXTRACT(MONTH FROM visit_time) AS visit_month,\n"
                 "       EXTRACT(DAY FROM visit_time) AS visit_day\n"
                 "FROM appointments ORDER BY appointment_id;",
    data=dict(appointments=APPOINTMENTS),
    oracle=lambda appointments: [
        (a["patient_name"], _parse_ts(a["visit_time"]).year, _parse_ts(a["visit_time"]).month, _parse_ts(a["visit_time"]).day)
        for a in sorted(appointments, key=lambda a: a["appointment_id"])
    ],
    hints="EXTRACT accepts several field names besides DOW and HOUR: YEAR, MONTH, and DAY each "
          "pull a different slice of the same timestamp.",
))

Q.append(dict(
    title="Days Before a Fixed Cutoff Date", difficulty="Hard", topics=TOPIC, subTopics=DATE_TOPIC,
    bloomTaxonomy="analyze",
    prose="For a reproducible report (using a fixed reference date, 2025-04-01, rather than "
          "today's date), show each patient's visit_time and how many days before that cutoff "
          "their visit fell, ordered with the most days-before first.",
    schema_sql=APPOINTMENTS_SQL, schema_lines=APPOINTMENTS_SCHEMA_LINES,
    header=["patient_name", "visit_time", "days_before_cutoff"],
    solution_sql="SELECT patient_name, visit_time, DATE '2025-04-01' - visit_time::DATE AS days_before_cutoff\n"
                 "FROM appointments ORDER BY days_before_cutoff DESC;",
    data=dict(appointments=APPOINTMENTS),
    oracle=lambda appointments: sorted(
        [
            (a["patient_name"], a["visit_time"], (_dt.date(2025, 4, 1) - _parse_ts(a["visit_time"]).date()).days)
            for a in appointments
        ],
        key=lambda row: row[2], reverse=True,
    ),
    hints="visit_time::DATE drops the time-of-day portion first, so subtracting from a fixed DATE "
          "literal returns a clean whole number of days, exactly like subtracting from CURRENT_DATE "
          "would, but reproducible regardless of when this runs.",
))

Q.append(dict(
    title="Appointments After a Fixed Mid-February Cutoff", difficulty="Hard", topics=TOPIC, subTopics=DATE_TOPIC,
    bloomTaxonomy="apply",
    prose="Show the patient_name and visit_time of every appointment recorded strictly after "
          "2025-02-15 00:00:00, sorted from earliest to latest.",
    schema_sql=APPOINTMENTS_SQL, schema_lines=APPOINTMENTS_SCHEMA_LINES,
    header=["patient_name", "visit_time"],
    solution_sql="SELECT patient_name, visit_time FROM appointments\n"
                 "WHERE visit_time > '2025-02-15 00:00:00' ORDER BY visit_time;",
    data=dict(appointments=APPOINTMENTS),
    oracle=lambda appointments: [
        (a["patient_name"], a["visit_time"])
        for a in sorted(appointments, key=lambda a: a["visit_time"])
        if _parse_ts(a["visit_time"]) > _parse_ts("2025-02-15 00:00:00")
    ],
    hints="A timestamp column compares directly against a fixed timestamp literal, exactly like "
          "comparing a DATE column against a fixed date.",
))

# ==================== nullhandling-functions ====================

Q.append(dict(
    title="Contact Number With Fallback", difficulty="Easy", topics=TOPIC, subTopics=NULL_TOPIC,
    bloomTaxonomy="apply",
    prose="The directory needs a phone number for every employee: use secondary_phone if present, "
          "otherwise fall back to primary_phone, and if even that is missing, show 'Not on file'.",
    schema_sql=EMPLOYEES_SQL, schema_lines=EMPLOYEES_SCHEMA_LINES,
    header=["full_name", "contact_number"],
    solution_sql="SELECT full_name, COALESCE(secondary_phone, primary_phone, 'Not on file') AS contact_number "
                 "FROM employees ORDER BY employee_id;",
    data=dict(employees=EMPLOYEES),
    oracle=lambda employees: [
        (e["full_name"], e["secondary_phone"] or e["primary_phone"] or "Not on file")
        for e in sorted(employees, key=lambda e: e["employee_id"])
    ],
    hints="COALESCE scans its arguments left to right and returns the first one that is not NULL.",
))

Q.append(dict(
    title="Flagging a Duplicated Secondary Phone", difficulty="Easy", topics=TOPIC, subTopics=NULL_TOPIC,
    bloomTaxonomy="apply",
    prose="One employee has the same number recorded as both their primary and secondary phone by "
          "mistake. Show every employee's real_secondary_phone, treating a secondary number that "
          "exactly matches the primary as if it were not provided.",
    schema_sql=EMPLOYEES_SQL, schema_lines=EMPLOYEES_SCHEMA_LINES,
    header=["full_name", "primary_phone", "secondary_phone", "real_secondary_phone"],
    solution_sql="SELECT full_name, primary_phone, secondary_phone,\n"
                 "       NULLIF(secondary_phone, primary_phone) AS real_secondary_phone\n"
                 "FROM employees ORDER BY employee_id;",
    data=dict(employees=EMPLOYEES),
    oracle=lambda employees: [
        (e["full_name"], e["primary_phone"], e["secondary_phone"],
         None if e["secondary_phone"] == e["primary_phone"] else e["secondary_phone"])
        for e in sorted(employees, key=lambda e: e["employee_id"])
    ],
    hints="NULLIF(a, b) returns NULL if the two arguments are equal, otherwise it returns a "
          "unchanged.",
))

Q.append(dict(
    title="Best Contact Number, Duplicates Cleaned First", difficulty="Medium", topics=TOPIC, subTopics=NULL_TOPIC,
    bloomTaxonomy="analyze",
    prose="Combine both fixes into one column: first treat a secondary phone that duplicates the "
          "primary as missing, then apply the same fallback chain as before, ending in "
          "'Not on file' if nothing at all is on record.",
    schema_sql=EMPLOYEES_SQL, schema_lines=EMPLOYEES_SCHEMA_LINES,
    header=["full_name", "best_contact_number"],
    solution_sql="SELECT full_name,\n"
                 "       COALESCE(NULLIF(secondary_phone, primary_phone), primary_phone, 'Not on file') AS best_contact_number\n"
                 "FROM employees ORDER BY employee_id;",
    data=dict(employees=EMPLOYEES),
    oracle=lambda employees: [
        (e["full_name"],
         (None if e["secondary_phone"] == e["primary_phone"] else e["secondary_phone"])
         or e["primary_phone"] or "Not on file")
        for e in sorted(employees, key=lambda e: e["employee_id"])
    ],
    hints="Read from the inside out: NULLIF first turns a duplicated secondary number into NULL, "
          "then COALESCE falls back through primary_phone and finally the literal fallback text.",
))

Q.append(dict(
    title="Reporting Line for Every Employee", difficulty="Medium", topics=TOPIC, subTopics=NULL_TOPIC,
    bloomTaxonomy="apply",
    prose="Build a 'reports to' column: show manager_id if present, otherwise show the employee's "
          "own employee_id, marking anyone with no manager as the top of the chart.",
    schema_sql=EMPLOYEES_SQL, schema_lines=EMPLOYEES_SCHEMA_LINES,
    header=["full_name", "reports_to"],
    solution_sql="SELECT full_name, COALESCE(manager_id, employee_id) AS reports_to "
                 "FROM employees ORDER BY employee_id;",
    data=dict(employees=EMPLOYEES),
    oracle=lambda employees: [
        (e["full_name"], e["manager_id"] if e["manager_id"] is not None else e["employee_id"])
        for e in sorted(employees, key=lambda e: e["employee_id"])
    ],
    hints="COALESCE's fallback does not have to be a literal; it can be another column entirely, "
          "here the employee's own employee_id.",
))

Q.append(dict(
    title="Contact Number and Reporting Line Together", difficulty="Hard", topics=TOPIC, subTopics=NULL_TOPIC,
    bloomTaxonomy="analyze",
    prose="Build one combined row per employee: the cleaned-up best_contact_number (duplicate "
          "secondary numbers treated as missing, falling back through primary_phone to "
          "'Not on file') alongside the reports_to reporting line, in a single query.",
    schema_sql=EMPLOYEES_SQL, schema_lines=EMPLOYEES_SCHEMA_LINES,
    header=["full_name", "best_contact_number", "reports_to"],
    solution_sql="SELECT full_name,\n"
                 "       COALESCE(NULLIF(secondary_phone, primary_phone), primary_phone, 'Not on file') AS best_contact_number,\n"
                 "       COALESCE(manager_id, employee_id) AS reports_to\n"
                 "FROM employees ORDER BY employee_id;",
    data=dict(employees=EMPLOYEES),
    oracle=lambda employees: [
        (e["full_name"],
         (None if e["secondary_phone"] == e["primary_phone"] else e["secondary_phone"])
         or e["primary_phone"] or "Not on file",
         e["manager_id"] if e["manager_id"] is not None else e["employee_id"])
        for e in sorted(employees, key=lambda e: e["employee_id"])
    ],
    hints="Nothing stops a single SELECT list from using COALESCE and NULLIF more than once, each "
          "solving a separate gap in the same row.",
))

Q.append(dict(
    title="Manager ID With a Sentinel Flag", difficulty="Hard", topics=TOPIC, subTopics=NULL_TOPIC,
    bloomTaxonomy="apply",
    prose="For a legacy report that expects a numeric manager_id with no blanks, show -1 for any "
          "employee with no manager on file instead of falling back to their own employee_id.",
    schema_sql=EMPLOYEES_SQL, schema_lines=EMPLOYEES_SCHEMA_LINES,
    header=["full_name", "manager_id_or_flag"],
    solution_sql="SELECT full_name, COALESCE(manager_id, -1) AS manager_id_or_flag "
                 "FROM employees ORDER BY employee_id;",
    data=dict(employees=EMPLOYEES),
    oracle=lambda employees: [
        (e["full_name"], e["manager_id"] if e["manager_id"] is not None else -1)
        for e in sorted(employees, key=lambda e: e["employee_id"])
    ],
    hints="COALESCE's fallback can be any literal value that makes sense for the report, not just "
          "another column.",
))

# ==================== conditional-logic ====================

Q.append(dict(
    title="Activity Labels by Visit Count", difficulty="Easy", topics=TOPIC, subTopics=CASE_TOPIC,
    bloomTaxonomy="apply",
    prose="The front desk wants members labeled 'Highly Active' (12 or more visits this month), "
          "'Active' (4 to 11 visits), or 'At Risk' (fewer than 4 visits).",
    schema_sql=MEMBERS_SQL, schema_lines=MEMBERS_SCHEMA_LINES,
    header=["full_name", "visits_this_month", "activity_label"],
    solution_sql="SELECT full_name, visits_this_month,\n"
                 "       CASE\n"
                 "           WHEN visits_this_month >= 12 THEN 'Highly Active'\n"
                 "           WHEN visits_this_month >= 4 THEN 'Active'\n"
                 "           ELSE 'At Risk'\n"
                 "       END AS activity_label\n"
                 "FROM members ORDER BY member_id;",
    data=dict(members=MEMBERS),
    oracle=lambda members: [
        (m["full_name"], m["visits_this_month"],
         "Highly Active" if m["visits_this_month"] >= 12
         else "Active" if m["visits_this_month"] >= 4
         else "At Risk")
        for m in sorted(members, key=lambda m: m["member_id"])
    ],
    hints="CASE checks each WHEN condition top to bottom and returns the value after the first "
          "THEN whose condition is true, falling back to ELSE if none match.",
))

Q.append(dict(
    title="Membership Plan Descriptions", difficulty="Medium", topics=TOPIC, subTopics=CASE_TOPIC,
    bloomTaxonomy="apply",
    prose="Translate each member's raw membership_type into a plain-language plan description for "
          "the front desk to read at a glance.",
    schema_sql=MEMBERS_SQL, schema_lines=MEMBERS_SCHEMA_LINES,
    header=["full_name", "membership_type", "plan_description"],
    solution_sql="SELECT full_name, membership_type,\n"
                 "       CASE membership_type\n"
                 "           WHEN 'premium' THEN 'Full access, all branches'\n"
                 "           WHEN 'standard' THEN 'Full access, home branch only'\n"
                 "           WHEN 'basic' THEN 'Gym floor only, no classes'\n"
                 "           ELSE 'Unknown plan'\n"
                 "       END AS plan_description\n"
                 "FROM members ORDER BY member_id;",
    data=dict(members=MEMBERS),
    oracle=lambda members: [
        (m["full_name"], m["membership_type"], {
            "premium": "Full access, all branches",
            "standard": "Full access, home branch only",
            "basic": "Gym floor only, no classes",
        }.get(m["membership_type"], "Unknown plan"))
        for m in sorted(members, key=lambda m: m["member_id"])
    ],
    hints="CASE column_name WHEN value THEN ... compares the column directly against each listed "
          "value, a shorter form for pure equality checks.",
))

Q.append(dict(
    title="Loyalty Points by Membership Multiplier", difficulty="Medium", topics=TOPIC, subTopics=CASE_TOPIC,
    bloomTaxonomy="analyze",
    prose="Calculate a loyalty-points figure for each member: their visits_this_month multiplied "
          "by a per-visit multiplier that depends on membership type (premium earns 10 points per "
          "visit, standard earns 5, anything else earns 2).",
    schema_sql=MEMBERS_SQL, schema_lines=MEMBERS_SCHEMA_LINES,
    header=["full_name", "loyalty_points"],
    solution_sql="SELECT full_name,\n"
                 "       visits_this_month * CASE membership_type\n"
                 "                                WHEN 'premium' THEN 10\n"
                 "                                WHEN 'standard' THEN 5\n"
                 "                                ELSE 2\n"
                 "                            END AS loyalty_points\n"
                 "FROM members ORDER BY member_id;",
    data=dict(members=MEMBERS),
    oracle=lambda members: [
        (m["full_name"], m["visits_this_month"] * {"premium": 10, "standard": 5}.get(m["membership_type"], 2))
        for m in sorted(members, key=lambda m: m["member_id"])
    ],
    hints="A CASE expression resolves to a plain value before the surrounding arithmetic runs, so "
          "it can sit directly inside a multiplication.",
))

Q.append(dict(
    title="Discount Offer Eligibility", difficulty="Hard", topics=TOPIC, subTopics=CASE_TOPIC,
    bloomTaxonomy="apply",
    prose="Flag members for a discount offer: anyone with fewer than 5 visits this month gets "
          "'Send Offer', everyone else gets 'No Offer Needed'.",
    schema_sql=MEMBERS_SQL, schema_lines=MEMBERS_SCHEMA_LINES,
    header=["full_name", "offer_status"],
    solution_sql="SELECT full_name,\n"
                 "       CASE WHEN visits_this_month < 5 THEN 'Send Offer' ELSE 'No Offer Needed' END AS offer_status\n"
                 "FROM members ORDER BY member_id;",
    data=dict(members=MEMBERS),
    oracle=lambda members: [
        (m["full_name"], "Send Offer" if m["visits_this_month"] < 5 else "No Offer Needed")
        for m in sorted(members, key=lambda m: m["member_id"])
    ],
    hints="A CASE expression with just one WHEN and an ELSE is a simple two-way branch, exactly "
          "like an if/else.",
))

Q.append(dict(
    title="Three-Tier Visit Category, Correctly Ordered", difficulty="Hard", topics=TOPIC, subTopics=CASE_TOPIC,
    bloomTaxonomy="analyze",
    prose="Categorize members into three visit tiers: 'Power User' for 15 or more visits, "
          "'Regular' for 8 to 14 visits, and 'Occasional' for anything below 8. Order the WHEN "
          "conditions so every member lands in the correct tier.",
    schema_sql=MEMBERS_SQL, schema_lines=MEMBERS_SCHEMA_LINES,
    header=["full_name", "visits_this_month", "visit_tier"],
    solution_sql="SELECT full_name, visits_this_month,\n"
                 "       CASE\n"
                 "           WHEN visits_this_month >= 15 THEN 'Power User'\n"
                 "           WHEN visits_this_month >= 8 THEN 'Regular'\n"
                 "           ELSE 'Occasional'\n"
                 "       END AS visit_tier\n"
                 "FROM members ORDER BY member_id;",
    data=dict(members=MEMBERS),
    oracle=lambda members: [
        (m["full_name"], m["visits_this_month"],
         "Power User" if m["visits_this_month"] >= 15
         else "Regular" if m["visits_this_month"] >= 8
         else "Occasional")
        for m in sorted(members, key=lambda m: m["member_id"])
    ],
    hints="The most specific or most restrictive condition (>= 15) must come first, or a looser "
          "condition checked earlier would catch a row before the tighter one ever gets a chance.",
))

Q.append(dict(
    title="Plan Description and Activity Label Together", difficulty="Hard", topics=TOPIC, subTopics=CASE_TOPIC,
    bloomTaxonomy="analyze",
    prose="Combine both CASE styles in one query: the equality-based plan_description alongside "
          "the range-based activity_label, one row per member.",
    schema_sql=MEMBERS_SQL, schema_lines=MEMBERS_SCHEMA_LINES,
    header=["full_name", "plan_description", "activity_label"],
    solution_sql="SELECT full_name,\n"
                 "       CASE membership_type\n"
                 "           WHEN 'premium' THEN 'Full access, all branches'\n"
                 "           WHEN 'standard' THEN 'Full access, home branch only'\n"
                 "           WHEN 'basic' THEN 'Gym floor only, no classes'\n"
                 "           ELSE 'Unknown plan'\n"
                 "       END AS plan_description,\n"
                 "       CASE\n"
                 "           WHEN visits_this_month >= 12 THEN 'Highly Active'\n"
                 "           WHEN visits_this_month >= 4 THEN 'Active'\n"
                 "           ELSE 'At Risk'\n"
                 "       END AS activity_label\n"
                 "FROM members ORDER BY member_id;",
    data=dict(members=MEMBERS),
    oracle=lambda members: [
        (m["full_name"],
         {"premium": "Full access, all branches", "standard": "Full access, home branch only",
          "basic": "Gym floor only, no classes"}.get(m["membership_type"], "Unknown plan"),
         "Highly Active" if m["visits_this_month"] >= 12
         else "Active" if m["visits_this_month"] >= 4
         else "At Risk")
        for m in sorted(members, key=lambda m: m["member_id"])
    ],
    hints="A single SELECT list can hold more than one CASE expression, each computing its own "
          "column independently.",
))

assert len(Q) == 30, len(Q)

for q in Q:
    q["tags"] = f"dbms - {q['subTopics']}"

OUT = "content/Question Bank/Coding Questions/DBMS/4.1 - Transforming Data - Coding Questions.xlsx"

if __name__ == "__main__":
    main(Q, OUT)
