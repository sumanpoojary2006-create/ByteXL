"""5.2 - Window Functions - Coding Questions (33: what a window function is,
OVER/PARTITION BY/ORDER BY, ranking functions, LAG/LEAD, window frames, and
top-N-per-group).

Tie-breaking note: the lesson itself states ROW_NUMBER breaks ties
"arbitrarily" (Sana Fatima and Tarun Bakshi, tied at 21000.00, get row_num 2
and 3 "based on whatever order the database happens to process them in").
That is unsafe for exact-match grading, so every ROW_NUMBER solution here
adds a deterministic secondary ORDER BY key inside OVER(...) (salesperson
name) to pin down which tied row gets which number. RANK and DENSE_RANK
don't need that fix, since tied rows always get the identical rank value
regardless of internal processing order -- but every ranking-function
question still adds an explicit outer ORDER BY (including a secondary key
among same-rank rows) so the *displayed row order* is deterministic too,
since a window function's OVER(...) ordering only affects the computed
value, never the final row order of the query's own result.

All salary/amount figures are decimal.Decimal (scale 2), and every displayed
AVG is wrapped in ROUND(..., 2) for the same reason as earlier chapters.
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


def row_numbers(n):
    return list(range(1, n + 1))


def ranks(sorted_keys):
    """sorted_keys is already in the desired OVER (ORDER BY ...) order."""
    result = []
    for i, k in enumerate(sorted_keys, start=1):
        if i > 1 and k == sorted_keys[i - 2]:
            result.append(result[-1])
        else:
            result.append(i)
    return result


def dense_ranks(sorted_keys):
    result = []
    current = 0
    prev = object()
    for k in sorted_keys:
        if k != prev:
            current += 1
            prev = k
        result.append(current)
    return result


TOPIC = "advanced-querying-with-sql"
WHAT_TOPIC = "what-is-a-window-function"
OVER_TOPIC = "over-partition-by-and-order-by"
RANKING_TOPIC = "ranking-functions"
OFFSET_TOPIC = "offset-functions-lag-and-lead"
FRAME_TOPIC = "running-totals-moving-averages-and-window-frames"
TOPN_TOPIC = "topn-per-group"

# ----------------------------- sales dataset (lessons 1-2) -----------------------------

SALES_COLUMNS = ["sale_id", "salesperson", "region", "amount", "sale_date"]
SALES = [
    dict(sale_id=1, salesperson="Nikhil Rao", region="North", amount=D("12000.00"), sale_date="2025-06-01"),
    dict(sale_id=2, salesperson="Nikhil Rao", region="North", amount=D("8500.00"), sale_date="2025-06-05"),
    dict(sale_id=3, salesperson="Sana Fatima", region="South", amount=D("15000.00"), sale_date="2025-06-02"),
    dict(sale_id=4, salesperson="Nikhil Rao", region="North", amount=D("9200.00"), sale_date="2025-06-10"),
    dict(sale_id=5, salesperson="Sana Fatima", region="South", amount=D("6000.00"), sale_date="2025-06-11"),
    dict(sale_id=6, salesperson="Tarun Bakshi", region="East", amount=D("11000.00"), sale_date="2025-06-03"),
]
SALES_DDL = """
CREATE TABLE sales (
    sale_id INTEGER PRIMARY KEY,
    salesperson TEXT,
    region TEXT,
    amount NUMERIC(10, 2),
    sale_date DATE
);
"""
SALES_SQL = SALES_DDL.strip("\n") + "\n\n" + sql_insert("sales", SALES_COLUMNS, SALES)
SALES_SCHEMA_LINES = ["sales(sale_id INTEGER PK, salesperson TEXT, region TEXT, amount NUMERIC(10,2), sale_date DATE) -- 6 rows"]


def partition(rows, key):
    groups = {}
    for r in rows:
        groups.setdefault(r[key], []).append(r)
    return groups


# ----------------------------- sales leaderboard dataset (lesson 3) -----------------------------

LB_COLUMNS = ["sale_id", "salesperson", "amount"]
LEADERBOARD = [
    dict(sale_id=1, salesperson="Nikhil Rao", amount=D("29700.00")),
    dict(sale_id=2, salesperson="Sana Fatima", amount=D("21000.00")),
    dict(sale_id=3, salesperson="Tarun Bakshi", amount=D("21000.00")),
    dict(sale_id=4, salesperson="Priya Bose", amount=D("18500.00")),
    dict(sale_id=5, salesperson="Kunal Verma", amount=D("11000.00")),
]
LB_DDL = """
CREATE TABLE sales (
    sale_id INTEGER PRIMARY KEY,
    salesperson TEXT,
    amount NUMERIC(10, 2)
);
"""
LB_SQL = LB_DDL.strip("\n") + "\n\n" + sql_insert("sales", LB_COLUMNS, LEADERBOARD)
LB_SCHEMA_LINES = ["sales(sale_id INTEGER PK, salesperson TEXT, amount NUMERIC(10,2)) -- 5 rows; Sana Fatima and Tarun Bakshi tie at 21000.00"]

# ----------------------------- monthly_sales dataset (lesson 4) -----------------------------

MS_COLUMNS = ["salesperson", "sale_month", "total_amount"]
MONTHLY_SALES = [
    dict(salesperson="Nikhil Rao", sale_month="2025-03-01", total_amount=D("22000.00")),
    dict(salesperson="Nikhil Rao", sale_month="2025-04-01", total_amount=D("25500.00")),
    dict(salesperson="Nikhil Rao", sale_month="2025-05-01", total_amount=D("21000.00")),
    dict(salesperson="Nikhil Rao", sale_month="2025-06-01", total_amount=D("29700.00")),
    dict(salesperson="Sana Fatima", sale_month="2025-05-01", total_amount=D("18000.00")),
    dict(salesperson="Sana Fatima", sale_month="2025-06-01", total_amount=D("21000.00")),
]
MS_DDL = """
CREATE TABLE monthly_sales (
    salesperson TEXT,
    sale_month DATE,
    total_amount NUMERIC(10, 2)
);
"""
MS_SQL = MS_DDL.strip("\n") + "\n\n" + sql_insert("monthly_sales", MS_COLUMNS, MONTHLY_SALES)
MS_SCHEMA_LINES = ["monthly_sales(salesperson TEXT, sale_month DATE, total_amount NUMERIC(10,2)) -- 6 rows, one per salesperson per month"]

# ----------------------------- monthly_sales frames dataset (lesson 5) -----------------------------

MSF_COLUMNS = ["salesperson", "sale_month", "total_amount"]
MONTHLY_SALES_FRAMES = [
    dict(salesperson="Nikhil Rao", sale_month="2025-01-01", total_amount=D("18000.00")),
    dict(salesperson="Nikhil Rao", sale_month="2025-02-01", total_amount=D("20000.00")),
    dict(salesperson="Nikhil Rao", sale_month="2025-03-01", total_amount=D("22000.00")),
    dict(salesperson="Nikhil Rao", sale_month="2025-04-01", total_amount=D("25500.00")),
    dict(salesperson="Nikhil Rao", sale_month="2025-05-01", total_amount=D("21000.00")),
    dict(salesperson="Nikhil Rao", sale_month="2025-06-01", total_amount=D("29700.00")),
]
MSF_SQL = MS_DDL.strip("\n") + "\n\n" + sql_insert("monthly_sales", MSF_COLUMNS, MONTHLY_SALES_FRAMES)
MSF_SCHEMA_LINES = ["monthly_sales(salesperson TEXT, sale_month DATE, total_amount NUMERIC(10,2)) -- 6 rows, all Nikhil Rao, Jan-Jun 2025"]
MSF_SORTED = sorted(MONTHLY_SALES_FRAMES, key=lambda r: r["sale_month"])

# ----------------------------- sales regions dataset (lesson 6) -----------------------------

SR_COLUMNS = ["salesperson", "region", "total_amount"]
SALES_REGIONS = [
    dict(salesperson="Nikhil Rao", region="North", total_amount=D("29700.00")),
    dict(salesperson="Aarav Singh", region="North", total_amount=D("24000.00")),
    dict(salesperson="Devika Rao", region="North", total_amount=D("18500.00")),
    dict(salesperson="Sana Fatima", region="South", total_amount=D("21000.00")),
    dict(salesperson="Tarun Bakshi", region="South", total_amount=D("21000.00")),
    dict(salesperson="Reema Ghosh", region="South", total_amount=D("15000.00")),
    dict(salesperson="Kunal Verma", region="East", total_amount=D("11000.00")),
]
SR_DDL = """
CREATE TABLE sales (
    salesperson TEXT,
    region TEXT,
    total_amount NUMERIC(10, 2)
);
"""
SR_SQL = SR_DDL.strip("\n") + "\n\n" + sql_insert("sales", SR_COLUMNS, SALES_REGIONS)
SR_SCHEMA_LINES = ["sales(salesperson TEXT, region TEXT, total_amount NUMERIC(10,2)) -- 7 rows across North, South, East; Sana Fatima and Tarun Bakshi tie in South"]

Q = []

# ==================== what-is-a-window-function ====================

Q.append(dict(
    title="Each Sale Beside Its Salesperson's Total", difficulty="Easy", topics=TOPIC, subTopics=WHAT_TOPIC,
    bloomTaxonomy="apply",
    prose="Leela wants every individual sale shown next to that salesperson's overall total, "
          "without losing any of the individual sale rows the way GROUP BY would.",
    schema_sql=SALES_SQL, schema_lines=SALES_SCHEMA_LINES,
    header=["salesperson", "sale_id", "amount", "salesperson_total"],
    solution_sql="SELECT salesperson, sale_id, amount,\n"
                 "       SUM(amount) OVER (PARTITION BY salesperson) AS salesperson_total\n"
                 "FROM sales\n"
                 "ORDER BY salesperson, sale_id;",
    data=dict(),
    oracle=lambda: [
        (r["salesperson"], r["sale_id"], r["amount"], sum((x["amount"] for x in SALES if x["salesperson"] == r["salesperson"]), D("0")))
        for r in sorted(SALES, key=lambda r: (r["salesperson"], r["sale_id"]))
    ],
    hints="SUM(amount) OVER (PARTITION BY salesperson) computes each salesperson's total without "
          "collapsing rows, unlike GROUP BY.",
))

Q.append(dict(
    title="Every Sale Beside the Company Total", difficulty="Easy", topics=TOPIC, subTopics=WHAT_TOPIC,
    bloomTaxonomy="understand",
    prose="Show every sale alongside the single company-wide total, the same number repeated on "
          "every row.",
    schema_sql=SALES_SQL, schema_lines=SALES_SCHEMA_LINES,
    header=["salesperson", "sale_id", "amount", "company_total"],
    solution_sql="SELECT salesperson, sale_id, amount,\n"
                 "       SUM(amount) OVER () AS company_total\n"
                 "FROM sales\n"
                 "ORDER BY sale_id;",
    data=dict(),
    oracle=lambda: [
        (r["salesperson"], r["sale_id"], r["amount"], sum((x["amount"] for x in SALES), D("0")))
        for r in sorted(SALES, key=lambda r: r["sale_id"])
    ],
    hints="An empty OVER () means the window is the entire result set, with no partitioning at "
          "all, so every row shows the same company-wide total.",
))

Q.append(dict(
    title="Salesperson Totals Excluding the East Region", difficulty="Medium", topics=TOPIC, subTopics=WHAT_TOPIC,
    bloomTaxonomy="analyze",
    prose="Show each remaining sale beside its salesperson's total, after filtering out the East "
          "region entirely before the window function ever runs.",
    schema_sql=SALES_SQL, schema_lines=SALES_SCHEMA_LINES,
    header=["salesperson", "sale_id", "amount", "salesperson_total"],
    solution_sql="SELECT salesperson, sale_id, amount,\n"
                 "       SUM(amount) OVER (PARTITION BY salesperson) AS salesperson_total\n"
                 "FROM sales\n"
                 "WHERE region != 'East'\n"
                 "ORDER BY salesperson, sale_id;",
    data=dict(),
    oracle=lambda: [
        (r["salesperson"], r["sale_id"], r["amount"],
         sum((x["amount"] for x in SALES if x["salesperson"] == r["salesperson"] and x["region"] != "East"), D("0")))
        for r in sorted(SALES, key=lambda r: (r["salesperson"], r["sale_id"]))
        if r["region"] != "East"
    ],
    hints="WHERE runs before the window function, so Tarun Bakshi's East-region row never factors "
          "into any partitioned total and does not appear in the output at all.",
))

Q.append(dict(
    title="Each Sale Beside Its Region's Total", difficulty="Hard", topics=TOPIC, subTopics=WHAT_TOPIC,
    bloomTaxonomy="apply",
    prose="Leela wants every sale alongside the total sales for that sale's region, without "
          "losing any individual sale rows.",
    schema_sql=SALES_SQL, schema_lines=SALES_SCHEMA_LINES,
    header=["salesperson", "region", "amount", "region_total"],
    solution_sql="SELECT salesperson, region, amount,\n"
                 "       SUM(amount) OVER (PARTITION BY region) AS region_total\n"
                 "FROM sales\n"
                 "ORDER BY region, salesperson;",
    data=dict(),
    oracle=lambda: sorted(
        [
            (r["salesperson"], r["region"], r["amount"], sum((x["amount"] for x in SALES if x["region"] == r["region"]), D("0")))
            for r in SALES
        ],
        key=lambda row: (row[1], row[0]),
    ),
    hints="Every South-region row should show 21000.00 as its region total, Sana's two sales "
          "combined.",
))

Q.append(dict(
    title="Each Sale Beside Its Salesperson's Sale Count", difficulty="Hard", topics=TOPIC, subTopics=WHAT_TOPIC,
    bloomTaxonomy="analyze",
    prose="Show every sale alongside how many total sales that salesperson has made, using "
          "COUNT as a window function instead of SUM.",
    schema_sql=SALES_SQL, schema_lines=SALES_SCHEMA_LINES,
    header=["salesperson", "sale_id", "amount", "sales_count"],
    solution_sql="SELECT salesperson, sale_id, amount,\n"
                 "       COUNT(*) OVER (PARTITION BY salesperson) AS sales_count\n"
                 "FROM sales\n"
                 "ORDER BY salesperson, sale_id;",
    data=dict(),
    oracle=lambda: [
        (r["salesperson"], r["sale_id"], r["amount"], len([x for x in SALES if x["salesperson"] == r["salesperson"]]))
        for r in sorted(SALES, key=lambda r: (r["salesperson"], r["sale_id"]))
    ],
    hints="Any aggregate function works as a window function, not just SUM; COUNT(*) OVER "
          "(PARTITION BY salesperson) counts each salesperson's rows without collapsing them.",
))

# ==================== over-partition-by-and-order-by ====================

Q.append(dict(
    title="Running Total by Salesperson, in Date Order", difficulty="Easy", topics=TOPIC, subTopics=OVER_TOPIC,
    bloomTaxonomy="apply",
    prose="Show each of a salesperson's sales next to their running total up to and including "
          "that sale, in date order.",
    schema_sql=SALES_SQL, schema_lines=SALES_SCHEMA_LINES,
    header=["salesperson", "sale_date", "amount", "running_total"],
    solution_sql="SELECT salesperson, sale_date, amount,\n"
                 "       SUM(amount) OVER (PARTITION BY salesperson ORDER BY sale_date) AS running_total\n"
                 "FROM sales\n"
                 "ORDER BY salesperson, sale_date;",
    data=dict(),
    oracle=lambda: [
        (r["salesperson"], r["sale_date"], r["amount"],
         sum((x["amount"] for x in sorted((y for y in SALES if y["salesperson"] == r["salesperson"]), key=lambda y: y["sale_date"])
              if x["sale_date"] <= r["sale_date"]), D("0")))
        for r in sorted(SALES, key=lambda r: (r["salesperson"], r["sale_date"]))
    ],
    hints="Adding ORDER BY sale_date inside OVER (...) changes the window's meaning to a running "
          "total: only rows up to and including the current one, in date order.",
))

Q.append(dict(
    title="Running Total Beside the Flat Salesperson Total", difficulty="Medium", topics=TOPIC, subTopics=OVER_TOPIC,
    bloomTaxonomy="analyze",
    prose="Show both an ordered running total and an unordered flat total side by side, making "
          "the difference between them visible in the same query.",
    schema_sql=SALES_SQL, schema_lines=SALES_SCHEMA_LINES,
    header=["salesperson", "sale_date", "amount", "running_total", "salesperson_total"],
    solution_sql="SELECT salesperson, sale_date, amount,\n"
                 "       SUM(amount) OVER (PARTITION BY salesperson ORDER BY sale_date) AS running_total,\n"
                 "       SUM(amount) OVER (PARTITION BY salesperson) AS salesperson_total\n"
                 "FROM sales\n"
                 "ORDER BY salesperson, sale_date;",
    data=dict(),
    oracle=lambda: [
        (r["salesperson"], r["sale_date"], r["amount"],
         sum((x["amount"] for x in sorted((y for y in SALES if y["salesperson"] == r["salesperson"]), key=lambda y: y["sale_date"])
              if x["sale_date"] <= r["sale_date"]), D("0")),
         sum((x["amount"] for x in SALES if x["salesperson"] == r["salesperson"]), D("0")))
        for r in sorted(SALES, key=lambda r: (r["salesperson"], r["sale_date"]))
    ],
    hints="running_total grows row by row within each partition, while salesperson_total, with no "
          "ORDER BY, stays fixed at the grand total on every row.",
))

Q.append(dict(
    title="Company-Wide Running Total by Date", difficulty="Medium", topics=TOPIC, subTopics=OVER_TOPIC,
    bloomTaxonomy="apply",
    prose="Track a single company-wide running total across every sale, regardless of "
          "salesperson, strictly in date order.",
    schema_sql=SALES_SQL, schema_lines=SALES_SCHEMA_LINES,
    header=["sale_date", "salesperson", "amount", "company_running_total"],
    solution_sql="SELECT sale_date, salesperson, amount,\n"
                 "       SUM(amount) OVER (ORDER BY sale_date) AS company_running_total\n"
                 "FROM sales\n"
                 "ORDER BY sale_date;",
    data=dict(),
    oracle=lambda: [
        (r["sale_date"], r["salesperson"], r["amount"],
         sum((x["amount"] for x in SALES if x["sale_date"] <= r["sale_date"]), D("0")))
        for r in sorted(SALES, key=lambda r: r["sale_date"])
    ],
    hints="ORDER BY inside OVER works even without PARTITION BY, producing one running "
          "calculation across the entire result set.",
))

Q.append(dict(
    title="South Region Running Total, in Date Order", difficulty="Hard", topics=TOPIC, subTopics=OVER_TOPIC,
    bloomTaxonomy="analyze",
    prose="Leela wants a running total of sales for the South region only, in date order, "
          "alongside each individual sale.",
    schema_sql=SALES_SQL, schema_lines=SALES_SCHEMA_LINES,
    header=["salesperson", "sale_date", "amount", "running_total"],
    solution_sql="SELECT salesperson, sale_date, amount,\n"
                 "       SUM(amount) OVER (PARTITION BY region ORDER BY sale_date) AS running_total\n"
                 "FROM sales\n"
                 "WHERE region = 'South'\n"
                 "ORDER BY sale_date;",
    data=dict(),
    oracle=lambda: [
        (r["salesperson"], r["sale_date"], r["amount"],
         sum((x["amount"] for x in SALES if x["region"] == "South" and x["sale_date"] <= r["sale_date"]), D("0")))
        for r in sorted((s for s in SALES if s["region"] == "South"), key=lambda r: r["sale_date"])
    ],
    hints="WHERE region = 'South' narrows the rows first; PARTITION BY region here is technically "
          "redundant once only one region remains, but keeps the pattern consistent.",
))

Q.append(dict(
    title="Running Count of Sales per Salesperson", difficulty="Hard", topics=TOPIC, subTopics=OVER_TOPIC,
    bloomTaxonomy="analyze",
    prose="Show, for each sale, how many sales that salesperson has made so far up to and "
          "including that date.",
    schema_sql=SALES_SQL, schema_lines=SALES_SCHEMA_LINES,
    header=["salesperson", "sale_date", "amount", "sales_so_far"],
    solution_sql="SELECT salesperson, sale_date, amount,\n"
                 "       COUNT(*) OVER (PARTITION BY salesperson ORDER BY sale_date) AS sales_so_far\n"
                 "FROM sales\n"
                 "ORDER BY salesperson, sale_date;",
    data=dict(),
    oracle=lambda: [
        (r["salesperson"], r["sale_date"], r["amount"],
         len([x for x in SALES if x["salesperson"] == r["salesperson"] and x["sale_date"] <= r["sale_date"]]))
        for r in sorted(SALES, key=lambda r: (r["salesperson"], r["sale_date"]))
    ],
    hints="COUNT(*) as a window function with ORDER BY inside OVER behaves just like the running "
          "SUM, but counts rows instead of adding a column's values.",
))

Q.append(dict(
    title="Running Average Sale Amount per Salesperson", difficulty="Hard", topics=TOPIC, subTopics=OVER_TOPIC,
    bloomTaxonomy="analyze",
    prose="Show each salesperson's running average sale amount, up to and including each sale, "
          "in date order, rounded to two decimal places.",
    schema_sql=SALES_SQL, schema_lines=SALES_SCHEMA_LINES,
    header=["salesperson", "sale_date", "amount", "running_avg"],
    solution_sql="SELECT salesperson, sale_date, amount,\n"
                 "       ROUND(AVG(amount) OVER (PARTITION BY salesperson ORDER BY sale_date), 2) AS running_avg\n"
                 "FROM sales\n"
                 "ORDER BY salesperson, sale_date;",
    data=dict(),
    oracle=lambda: [
        (r["salesperson"], r["sale_date"], r["amount"],
         pg_round(
             sum((x["amount"] for x in SALES if x["salesperson"] == r["salesperson"] and x["sale_date"] <= r["sale_date"]), D("0"))
             / len([x for x in SALES if x["salesperson"] == r["salesperson"] and x["sale_date"] <= r["sale_date"]]), 2))
        for r in sorted(SALES, key=lambda r: (r["salesperson"], r["sale_date"]))
    ],
    hints="AVG works as a running window calculation exactly like SUM does; wrap it in ROUND for "
          "a clean two-decimal result.",
))

# ==================== ranking-functions ====================

_LB_SORTED_FOR_ROWNUM = sorted(LEADERBOARD, key=lambda r: (-r["amount"], r["salesperson"]))
_LB_SORTED_FOR_RANK = sorted(LEADERBOARD, key=lambda r: -r["amount"])

Q.append(dict(
    title="Leaderboard by ROW_NUMBER", difficulty="Easy", topics=TOPIC, subTopics=RANKING_TOPIC,
    bloomTaxonomy="apply",
    prose="Assign a strict, no-ties sequence number to every salesperson ordered by amount, "
          "highest first. Since Sana Fatima and Tarun Bakshi tie at 21000.00, break the tie "
          "alphabetically by name so the numbering is reproducible.",
    schema_sql=LB_SQL, schema_lines=LB_SCHEMA_LINES,
    header=["salesperson", "amount", "row_num"],
    solution_sql="SELECT salesperson, amount,\n"
                 "       ROW_NUMBER() OVER (ORDER BY amount DESC, salesperson) AS row_num\n"
                 "FROM sales\n"
                 "ORDER BY row_num;",
    data=dict(),
    oracle=lambda: [
        (r["salesperson"], r["amount"], n)
        for r, n in zip(_LB_SORTED_FOR_ROWNUM, row_numbers(len(_LB_SORTED_FOR_ROWNUM)))
    ],
    hints="ROW_NUMBER() assigns a strictly increasing integer with no regard for ties; adding "
          "salesperson as a secondary ORDER BY key makes which tied row gets which number "
          "reproducible.",
))

Q.append(dict(
    title="Leaderboard by RANK", difficulty="Easy", topics=TOPIC, subTopics=RANKING_TOPIC,
    bloomTaxonomy="apply",
    prose="Rank every salesperson by amount, highest first, giving tied salespeople the same "
          "rank and skipping ahead by the tie count afterward.",
    schema_sql=LB_SQL, schema_lines=LB_SCHEMA_LINES,
    header=["salesperson", "amount", "rank_position"],
    solution_sql="SELECT salesperson, amount,\n"
                 "       RANK() OVER (ORDER BY amount DESC) AS rank_position\n"
                 "FROM sales\n"
                 "ORDER BY rank_position, salesperson;",
    data=dict(),
    oracle=lambda: sorted(
        [
            (r["salesperson"], r["amount"], rk)
            for r, rk in zip(_LB_SORTED_FOR_RANK, ranks([r["amount"] for r in _LB_SORTED_FOR_RANK]))
        ],
        key=lambda row: (row[2], row[0]),
    ),
    hints="Sana and Tarun both land on rank 2; Priya Bose, next in line, gets rank 4, not 3, "
          "since RANK counts the two tied rows above her.",
))

Q.append(dict(
    title="Leaderboard by DENSE_RANK", difficulty="Medium", topics=TOPIC, subTopics=RANKING_TOPIC,
    bloomTaxonomy="apply",
    prose="Rank every salesperson by amount using DENSE_RANK, which keeps the rank sequence "
          "consecutive even after a tie.",
    schema_sql=LB_SQL, schema_lines=LB_SCHEMA_LINES,
    header=["salesperson", "amount", "dense_rank_position"],
    solution_sql="SELECT salesperson, amount,\n"
                 "       DENSE_RANK() OVER (ORDER BY amount DESC) AS dense_rank_position\n"
                 "FROM sales\n"
                 "ORDER BY dense_rank_position, salesperson;",
    data=dict(),
    oracle=lambda: sorted(
        [
            (r["salesperson"], r["amount"], rk)
            for r, rk in zip(_LB_SORTED_FOR_RANK, dense_ranks([r["amount"] for r in _LB_SORTED_FOR_RANK]))
        ],
        key=lambda row: (row[2], row[0]),
    ),
    hints="Sana and Tarun again both land on rank 2, but Priya Bose now gets rank 3, since "
          "DENSE_RANK treats the tie as consuming only one rank position.",
))

Q.append(dict(
    title="All Three Ranking Functions Side by Side", difficulty="Medium", topics=TOPIC, subTopics=RANKING_TOPIC,
    bloomTaxonomy="analyze",
    prose="Show ROW_NUMBER, RANK, and DENSE_RANK together in one query, making the divergence "
          "between them visible right where Sana Fatima and Tarun Bakshi tie.",
    schema_sql=LB_SQL, schema_lines=LB_SCHEMA_LINES,
    header=["salesperson", "amount", "row_num", "rank_position", "dense_rank_position"],
    solution_sql="SELECT salesperson, amount,\n"
                 "       ROW_NUMBER() OVER (ORDER BY amount DESC, salesperson) AS row_num,\n"
                 "       RANK() OVER (ORDER BY amount DESC) AS rank_position,\n"
                 "       DENSE_RANK() OVER (ORDER BY amount DESC) AS dense_rank_position\n"
                 "FROM sales\n"
                 "ORDER BY rank_position, salesperson;",
    data=dict(),
    oracle=lambda: sorted(
        [
            (row_r["salesperson"], row_r["amount"], rn, rk, dr)
            for row_r, rn, rk, dr in zip(
                _LB_SORTED_FOR_ROWNUM,
                row_numbers(len(_LB_SORTED_FOR_ROWNUM)),
                [ranks([r["amount"] for r in _LB_SORTED_FOR_RANK])[_LB_SORTED_FOR_RANK.index(row_r)] for row_r in _LB_SORTED_FOR_ROWNUM],
                [dense_ranks([r["amount"] for r in _LB_SORTED_FOR_RANK])[_LB_SORTED_FOR_RANK.index(row_r)] for row_r in _LB_SORTED_FOR_ROWNUM],
            )
        ],
        key=lambda row: (row[3], row[0]),
    ),
    hints="For the tied pair, row_num shows 2 and 3, while rank_position and dense_rank_position "
          "both show 2 and 2; the real divergence appears on the very next row after the tie.",
))

Q.append(dict(
    title="Top 3 Tiers by DENSE_RANK", difficulty="Hard", topics=TOPIC, subTopics=RANKING_TOPIC,
    bloomTaxonomy="analyze",
    prose="Show only salespeople ranked in the top 3 tiers by DENSE_RANK. Since window functions "
          "cannot be referenced directly in WHERE, wrap the ranking in a CTE first.",
    schema_sql=LB_SQL, schema_lines=LB_SCHEMA_LINES,
    header=["salesperson", "amount", "dense_rank_position"],
    solution_sql="WITH ranked AS (\n"
                 "    SELECT salesperson, amount,\n"
                 "           DENSE_RANK() OVER (ORDER BY amount DESC) AS dense_rank_position\n"
                 "    FROM sales\n"
                 ")\n"
                 "SELECT * FROM ranked\n"
                 "WHERE dense_rank_position <= 3\n"
                 "ORDER BY dense_rank_position, salesperson;",
    data=dict(),
    oracle=lambda: sorted(
        [
            (r["salesperson"], r["amount"], rk)
            for r, rk in zip(_LB_SORTED_FOR_RANK, dense_ranks([r["amount"] for r in _LB_SORTED_FOR_RANK]))
            if rk <= 3
        ],
        key=lambda row: (row[2], row[0]),
    ),
    hints="This returns four rows, not three, since two people share the second tier and both "
          "survive the dense_rank_position <= 3 filter.",
))

Q.append(dict(
    title="Ranking From the Bottom", difficulty="Hard", topics=TOPIC, subTopics=RANKING_TOPIC,
    bloomTaxonomy="analyze",
    prose="Rank every salesperson from lowest amount to highest, reversing the usual leaderboard "
          "direction.",
    schema_sql=LB_SQL, schema_lines=LB_SCHEMA_LINES,
    header=["salesperson", "amount", "rank_from_bottom"],
    solution_sql="SELECT salesperson, amount,\n"
                 "       RANK() OVER (ORDER BY amount ASC) AS rank_from_bottom\n"
                 "FROM sales\n"
                 "ORDER BY rank_from_bottom, salesperson;",
    data=dict(),
    oracle=lambda: sorted(
        [
            (r["salesperson"], r["amount"], rk)
            for r, rk in zip(
                sorted(LEADERBOARD, key=lambda r: r["amount"]),
                ranks([r["amount"] for r in sorted(LEADERBOARD, key=lambda r: r["amount"])]),
            )
        ],
        key=lambda row: (row[2], row[0]),
    ),
    hints="Ordering ascending instead of descending flips which end of the amount range counts "
          "as rank 1; Sana and Tarun still tie, now at rank 3 rather than rank 2.",
))

# ==================== offset-functions-lag-and-lead ====================

Q.append(dict(
    title="Each Month Beside the Previous Month", difficulty="Easy", topics=TOPIC, subTopics=OFFSET_TOPIC,
    bloomTaxonomy="apply",
    prose="For each salesperson's monthly total, show the previous month's total in the same "
          "row.",
    schema_sql=MS_SQL, schema_lines=MS_SCHEMA_LINES,
    header=["salesperson", "sale_month", "total_amount", "previous_month"],
    solution_sql="SELECT salesperson, sale_month, total_amount,\n"
                 "       LAG(total_amount) OVER (PARTITION BY salesperson ORDER BY sale_month) AS previous_month\n"
                 "FROM monthly_sales\n"
                 "ORDER BY salesperson, sale_month;",
    data=dict(),
    oracle=lambda: [
        (r["salesperson"], r["sale_month"], r["total_amount"], prev)
        for group in [sorted(MONTHLY_SALES, key=lambda r: (r["salesperson"], r["sale_month"]))]
        for i, r in enumerate(group)
        for prev in [
            next((x["total_amount"] for x in reversed(group[:i]) if x["salesperson"] == r["salesperson"]), None)
        ]
    ],
    hints="LAG(total_amount) reaches back one row within each salesperson's partition, ordered "
          "by month; the very first row of each partition has nothing before it and shows NULL.",
))

Q.append(dict(
    title="Month-over-Month Change", difficulty="Medium", topics=TOPIC, subTopics=OFFSET_TOPIC,
    bloomTaxonomy="analyze",
    prose="Calculate each month's change from the previous month, using LAG directly inside a "
          "subtraction.",
    schema_sql=MS_SQL, schema_lines=MS_SCHEMA_LINES,
    header=["salesperson", "sale_month", "total_amount", "change_from_last_month"],
    solution_sql="SELECT salesperson, sale_month, total_amount,\n"
                 "       total_amount - LAG(total_amount) OVER (PARTITION BY salesperson ORDER BY sale_month) AS change_from_last_month\n"
                 "FROM monthly_sales\n"
                 "ORDER BY salesperson, sale_month;",
    data=dict(),
    oracle=lambda: [
        (r["salesperson"], r["sale_month"], r["total_amount"], (r["total_amount"] - prev) if prev is not None else None)
        for group in [sorted(MONTHLY_SALES, key=lambda r: (r["salesperson"], r["sale_month"]))]
        for i, r in enumerate(group)
        for prev in [
            next((x["total_amount"] for x in reversed(group[:i]) if x["salesperson"] == r["salesperson"]), None)
        ]
    ],
    hints="With the previous month's value sitting in the same row thanks to LAG, calculating "
          "growth becomes a plain subtraction.",
))

Q.append(dict(
    title="Each Month Beside the Next Month", difficulty="Medium", topics=TOPIC, subTopics=OFFSET_TOPIC,
    bloomTaxonomy="apply",
    prose="For each salesperson's monthly total, show next month's total in the same row, the "
          "mirror of LAG.",
    schema_sql=MS_SQL, schema_lines=MS_SCHEMA_LINES,
    header=["salesperson", "sale_month", "total_amount", "next_month"],
    solution_sql="SELECT salesperson, sale_month, total_amount,\n"
                 "       LEAD(total_amount) OVER (PARTITION BY salesperson ORDER BY sale_month) AS next_month\n"
                 "FROM monthly_sales\n"
                 "ORDER BY salesperson, sale_month;",
    data=dict(),
    oracle=lambda: [
        (r["salesperson"], r["sale_month"], r["total_amount"], nxt)
        for group in [sorted(MONTHLY_SALES, key=lambda r: (r["salesperson"], r["sale_month"]))]
        for i, r in enumerate(group)
        for nxt in [
            next((x["total_amount"] for x in group[i + 1:] if x["salesperson"] == r["salesperson"]), None)
        ]
    ],
    hints="LEAD reaches forward instead of backward; the last row of each partition has nothing "
          "after it and shows NULL.",
))

Q.append(dict(
    title="Two Months Ago, Defaulting to Zero", difficulty="Hard", topics=TOPIC, subTopics=OFFSET_TOPIC,
    bloomTaxonomy="analyze",
    prose="Show each month's total from two months prior, supplying 0 instead of NULL whenever "
          "there is no row that far back.",
    schema_sql=MS_SQL, schema_lines=MS_SCHEMA_LINES,
    header=["salesperson", "sale_month", "total_amount", "two_months_ago"],
    solution_sql="SELECT salesperson, sale_month, total_amount,\n"
                 "       LAG(total_amount, 2, 0) OVER (PARTITION BY salesperson ORDER BY sale_month) AS two_months_ago\n"
                 "FROM monthly_sales\n"
                 "ORDER BY salesperson, sale_month;",
    data=dict(),
    oracle=lambda: [
        (r["salesperson"], r["sale_month"], r["total_amount"],
         (group[i - 2]["total_amount"] if i - 2 >= 0 and group[i - 2]["salesperson"] == r["salesperson"] else D("0")))
        for group in [sorted(MONTHLY_SALES, key=lambda r: (r["salesperson"], r["sale_month"]))]
        for i, r in enumerate(group)
    ],
    hints="LAG's second argument sets how many rows to look back, and the third argument "
          "supplies a fallback value to use instead of NULL when no such row exists.",
))

Q.append(dict(
    title="Trend Label From Month to Month", difficulty="Hard", topics=TOPIC, subTopics=OFFSET_TOPIC,
    bloomTaxonomy="analyze",
    prose="Flag any month where a salesperson's total dropped compared to the previous month, "
          "labeling every row 'up' or 'down', with the first month of each salesperson "
          "defaulting to 'up' since it has nothing to compare against.",
    schema_sql=MS_SQL, schema_lines=MS_SCHEMA_LINES,
    header=["salesperson", "sale_month", "total_amount", "trend"],
    solution_sql="SELECT salesperson, sale_month, total_amount,\n"
                 "       CASE\n"
                 "           WHEN total_amount < LAG(total_amount) OVER (PARTITION BY salesperson ORDER BY sale_month)\n"
                 "           THEN 'down' ELSE 'up'\n"
                 "       END AS trend\n"
                 "FROM monthly_sales\n"
                 "ORDER BY salesperson, sale_month;",
    data=dict(),
    oracle=lambda: [
        (r["salesperson"], r["sale_month"], r["total_amount"],
         "down" if (prev is not None and r["total_amount"] < prev) else "up")
        for group in [sorted(MONTHLY_SALES, key=lambda r: (r["salesperson"], r["sale_month"]))]
        for i, r in enumerate(group)
        for prev in [
            next((x["total_amount"] for x in reversed(group[:i]) if x["salesperson"] == r["salesperson"]), None)
        ]
    ],
    hints="A CASE expression can directly compare a row's own value against LAG's result; ELSE "
          "'up' catches both genuine increases and the first row of each partition, where LAG "
          "returns NULL and the comparison is never true.",
))

Q.append(dict(
    title="Two Months Ahead, Defaulting to Zero", difficulty="Hard", topics=TOPIC, subTopics=OFFSET_TOPIC,
    bloomTaxonomy="analyze",
    prose="Show each month's total from two months in the future, supplying 0 instead of NULL "
          "whenever there is no row that far ahead, the forward-looking mirror of the "
          "two-months-ago question.",
    schema_sql=MS_SQL, schema_lines=MS_SCHEMA_LINES,
    header=["salesperson", "sale_month", "total_amount", "two_months_ahead"],
    solution_sql="SELECT salesperson, sale_month, total_amount,\n"
                 "       LEAD(total_amount, 2, 0) OVER (PARTITION BY salesperson ORDER BY sale_month) AS two_months_ahead\n"
                 "FROM monthly_sales\n"
                 "ORDER BY salesperson, sale_month;",
    data=dict(),
    oracle=lambda: [
        (r["salesperson"], r["sale_month"], r["total_amount"],
         (group[i + 2]["total_amount"] if i + 2 < len(group) and group[i + 2]["salesperson"] == r["salesperson"] else D("0")))
        for group in [sorted(MONTHLY_SALES, key=lambda r: (r["salesperson"], r["sale_month"]))]
        for i, r in enumerate(group)
    ],
    hints="LEAD accepts the same optional offset and default arguments as LAG, just reaching in "
          "the opposite direction.",
))

# ==================== running-totals-moving-averages-and-window-frames ====================

Q.append(dict(
    title="Running Total, Frame Written Explicitly", difficulty="Easy", topics=TOPIC, subTopics=FRAME_TOPIC,
    bloomTaxonomy="understand",
    prose="Write out the running total's window frame explicitly instead of relying on the "
          "default: from the first row of the window to the current row.",
    schema_sql=MSF_SQL, schema_lines=MSF_SCHEMA_LINES,
    header=["sale_month", "total_amount", "running_total"],
    solution_sql="SELECT sale_month, total_amount,\n"
                 "       SUM(total_amount) OVER (\n"
                 "           ORDER BY sale_month\n"
                 "           ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW\n"
                 "       ) AS running_total\n"
                 "FROM monthly_sales\n"
                 "ORDER BY sale_month;",
    data=dict(),
    oracle=lambda: [
        (r["sale_month"], r["total_amount"], sum((x["total_amount"] for x in MSF_SORTED[:i + 1]), D("0")))
        for i, r in enumerate(MSF_SORTED)
    ],
    hints="ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW names the default frame directly: "
          "start from the first row available and end at the current row.",
))

Q.append(dict(
    title="3-Month Moving Average", difficulty="Medium", topics=TOPIC, subTopics=FRAME_TOPIC,
    bloomTaxonomy="analyze",
    prose="Compute a 3-month moving average: each month's value is the average of itself and the "
          "two months before it.",
    schema_sql=MSF_SQL, schema_lines=MSF_SCHEMA_LINES,
    header=["sale_month", "total_amount", "moving_avg_3month"],
    solution_sql="SELECT sale_month, total_amount,\n"
                 "       ROUND(AVG(total_amount) OVER (\n"
                 "           ORDER BY sale_month\n"
                 "           ROWS BETWEEN 2 PRECEDING AND CURRENT ROW\n"
                 "       ), 2) AS moving_avg_3month\n"
                 "FROM monthly_sales\n"
                 "ORDER BY sale_month;",
    data=dict(),
    oracle=lambda: [
        (r["sale_month"], r["total_amount"],
         pg_round(sum((x["total_amount"] for x in MSF_SORTED[max(0, i - 2):i + 1]), D("0"))
                   / len(MSF_SORTED[max(0, i - 2):i + 1]), 2))
        for i, r in enumerate(MSF_SORTED)
    ],
    hints="January's moving average is just its own value, since zero rows precede it; February "
          "averages two rows; from March onward every row averages exactly three.",
))

Q.append(dict(
    title="Centered Average, One Before and One After", difficulty="Medium", topics=TOPIC, subTopics=FRAME_TOPIC,
    bloomTaxonomy="analyze",
    prose="Compute a centered average for each month: the average of itself, the month before, "
          "and the month after.",
    schema_sql=MSF_SQL, schema_lines=MSF_SCHEMA_LINES,
    header=["sale_month", "total_amount", "centered_avg"],
    solution_sql="SELECT sale_month, total_amount,\n"
                 "       ROUND(AVG(total_amount) OVER (\n"
                 "           ORDER BY sale_month\n"
                 "           ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING\n"
                 "       ), 2) AS centered_avg\n"
                 "FROM monthly_sales\n"
                 "ORDER BY sale_month;",
    data=dict(),
    oracle=lambda: [
        (r["sale_month"], r["total_amount"],
         pg_round(sum((x["total_amount"] for x in MSF_SORTED[max(0, i - 1):i + 2]), D("0"))
                   / len(MSF_SORTED[max(0, i - 1):i + 2]), 2))
        for i, r in enumerate(MSF_SORTED)
    ],
    hints="A frame can extend in both directions at once; the first and last rows only have a "
          "neighbor on one side, so their averages use just two values instead of three.",
))

Q.append(dict(
    title="2-Month Moving Total", difficulty="Hard", topics=TOPIC, subTopics=FRAME_TOPIC,
    bloomTaxonomy="apply",
    prose="Leela wants a 2-month moving total: the current month plus the one before it.",
    schema_sql=MSF_SQL, schema_lines=MSF_SCHEMA_LINES,
    header=["sale_month", "total_amount", "moving_total_2month"],
    solution_sql="SELECT sale_month, total_amount,\n"
                 "       SUM(total_amount) OVER (\n"
                 "           ORDER BY sale_month\n"
                 "           ROWS BETWEEN 1 PRECEDING AND CURRENT ROW\n"
                 "       ) AS moving_total_2month\n"
                 "FROM monthly_sales\n"
                 "ORDER BY sale_month;",
    data=dict(),
    oracle=lambda: [
        (r["sale_month"], r["total_amount"], sum((x["total_amount"] for x in MSF_SORTED[max(0, i - 1):i + 1]), D("0")))
        for i, r in enumerate(MSF_SORTED)
    ],
    hints="February shows January plus February combined, and March shows February plus March; "
          "January itself, with nothing before it, shows just its own value.",
))

Q.append(dict(
    title="Highest Total in the Last 3 Months", difficulty="Hard", topics=TOPIC, subTopics=FRAME_TOPIC,
    bloomTaxonomy="analyze",
    prose="For each month, show the highest single monthly total among itself and the two months "
          "before it, using MAX as the window function instead of SUM or AVG.",
    schema_sql=MSF_SQL, schema_lines=MSF_SCHEMA_LINES,
    header=["sale_month", "total_amount", "max_last_3months"],
    solution_sql="SELECT sale_month, total_amount,\n"
                 "       MAX(total_amount) OVER (\n"
                 "           ORDER BY sale_month\n"
                 "           ROWS BETWEEN 2 PRECEDING AND CURRENT ROW\n"
                 "       ) AS max_last_3months\n"
                 "FROM monthly_sales\n"
                 "ORDER BY sale_month;",
    data=dict(),
    oracle=lambda: [
        (r["sale_month"], r["total_amount"], max(x["total_amount"] for x in MSF_SORTED[max(0, i - 2):i + 1]))
        for i, r in enumerate(MSF_SORTED)
    ],
    hints="The same ROWS BETWEEN 2 PRECEDING AND CURRENT ROW frame from the moving average works "
          "with any aggregate, including MAX.",
))

# ==================== topn-per-group ====================

Q.append(dict(
    title="Rank Within Each Region", difficulty="Easy", topics=TOPIC, subTopics=TOPN_TOPIC,
    bloomTaxonomy="apply",
    prose="Rank every salesperson by total_amount within their own region, so the ranking "
          "restarts at 1 for each region separately.",
    schema_sql=SR_SQL, schema_lines=SR_SCHEMA_LINES,
    header=["salesperson", "region", "total_amount", "region_rank"],
    solution_sql="SELECT salesperson, region, total_amount,\n"
                 "       RANK() OVER (PARTITION BY region ORDER BY total_amount DESC) AS region_rank\n"
                 "FROM sales\n"
                 "ORDER BY region, region_rank, salesperson;",
    data=dict(),
    oracle=lambda: sorted(
        [
            (r["salesperson"], r["region"], r["total_amount"], rk)
            for region, group in partition(SALES_REGIONS, "region").items()
            for r, rk in zip(
                sorted(group, key=lambda r: -r["total_amount"]),
                ranks([r["total_amount"] for r in sorted(group, key=lambda r: -r["total_amount"])]),
            )
        ],
        key=lambda row: (row[1], row[3], row[0]),
    ),
    hints="PARTITION BY region resets the ranking separately within North, South, and East; "
          "Sana Fatima and Tarun Bakshi both rank 1st in South, tied at 21000.00 each.",
))

Q.append(dict(
    title="Top 2 Salespeople per Region, via RANK", difficulty="Medium", topics=TOPIC, subTopics=TOPN_TOPIC,
    bloomTaxonomy="analyze",
    prose="Show the top 2 salespeople by revenue within each region, using RANK wrapped in a CTE "
          "so the rank can be filtered.",
    schema_sql=SR_SQL, schema_lines=SR_SCHEMA_LINES,
    header=["salesperson", "region", "total_amount", "region_rank"],
    solution_sql="WITH ranked_sales AS (\n"
                 "    SELECT salesperson, region, total_amount,\n"
                 "           RANK() OVER (PARTITION BY region ORDER BY total_amount DESC) AS region_rank\n"
                 "    FROM sales\n"
                 ")\n"
                 "SELECT salesperson, region, total_amount, region_rank\n"
                 "FROM ranked_sales\n"
                 "WHERE region_rank <= 2\n"
                 "ORDER BY region, region_rank, salesperson;",
    data=dict(),
    oracle=lambda: sorted(
        [
            (r["salesperson"], r["region"], r["total_amount"], rk)
            for region, group in partition(SALES_REGIONS, "region").items()
            for r, rk in zip(
                sorted(group, key=lambda r: -r["total_amount"]),
                ranks([r["total_amount"] for r in sorted(group, key=lambda r: -r["total_amount"])]),
            )
            if rk <= 2
        ],
        key=lambda row: (row[1], row[3], row[0]),
    ),
    hints="This returns 5 rows, not 6: North and South each contribute 2, but East has only one "
          "salesperson to begin with, so its entire top 2 is just that one row.",
))

Q.append(dict(
    title="Top 2 Salespeople per Region, via ROW_NUMBER", difficulty="Medium", topics=TOPIC, subTopics=TOPN_TOPIC,
    bloomTaxonomy="analyze",
    prose="Repeat the top-2-per-region report, but using ROW_NUMBER instead of RANK, guaranteeing "
          "at most exactly 2 rows per region even where South has a tie.",
    schema_sql=SR_SQL, schema_lines=SR_SCHEMA_LINES,
    header=["salesperson", "region", "total_amount"],
    solution_sql="WITH ranked_sales AS (\n"
                 "    SELECT salesperson, region, total_amount,\n"
                 "           ROW_NUMBER() OVER (PARTITION BY region ORDER BY total_amount DESC, salesperson) AS row_num\n"
                 "    FROM sales\n"
                 ")\n"
                 "SELECT salesperson, region, total_amount\n"
                 "FROM ranked_sales\n"
                 "WHERE row_num <= 2\n"
                 "ORDER BY region, row_num;",
    data=dict(),
    oracle=lambda: [
        (r["salesperson"], r["region"], r["total_amount"])
        for region in sorted({r["region"] for r in SALES_REGIONS})
        for r in sorted(partition(SALES_REGIONS, "region")[region], key=lambda r: (-r["total_amount"], r["salesperson"]))[:2]
    ],
    hints="ROW_NUMBER never produces a tie in its numbering, so it guarantees at most 2 rows per "
          "region regardless of how the underlying values compare; South's tie is broken "
          "alphabetically here for reproducibility.",
))

Q.append(dict(
    title="Lowest-Selling Salesperson per Region", difficulty="Hard", topics=TOPIC, subTopics=TOPN_TOPIC,
    bloomTaxonomy="analyze",
    prose="Find the single lowest-selling salesperson in each region, using RANK ordered "
          "ascending instead of descending.",
    schema_sql=SR_SQL, schema_lines=SR_SCHEMA_LINES,
    header=["salesperson", "region", "total_amount"],
    solution_sql="WITH ranked_sales AS (\n"
                 "    SELECT salesperson, region, total_amount,\n"
                 "           RANK() OVER (PARTITION BY region ORDER BY total_amount ASC) AS region_rank\n"
                 "    FROM sales\n"
                 ")\n"
                 "SELECT salesperson, region, total_amount\n"
                 "FROM ranked_sales\n"
                 "WHERE region_rank = 1\n"
                 "ORDER BY region;",
    data=dict(),
    oracle=lambda: [
        (r["salesperson"], r["region"], r["total_amount"])
        for region in sorted({r["region"] for r in SALES_REGIONS})
        for r in [min(partition(SALES_REGIONS, "region")[region], key=lambda r: r["total_amount"])]
    ],
    hints="Ordering ascending instead of descending flips the ranking to find the smallest value "
          "first in each region; no region here has a tie for last place.",
))

Q.append(dict(
    title="Top-Ranked Salespeople per Region, via DENSE_RANK, Ties Included", difficulty="Hard", topics=TOPIC, subTopics=TOPN_TOPIC,
    bloomTaxonomy="analyze",
    prose="Find every salesperson holding rank 1 within their region using DENSE_RANK, "
          "confirming that a tie for first place can make a 'top 1 per region' report return "
          "more than one row for that region.",
    schema_sql=SR_SQL, schema_lines=SR_SCHEMA_LINES,
    header=["salesperson", "region", "total_amount"],
    solution_sql="WITH ranked_sales AS (\n"
                 "    SELECT salesperson, region, total_amount,\n"
                 "           DENSE_RANK() OVER (PARTITION BY region ORDER BY total_amount DESC) AS region_rank\n"
                 "    FROM sales\n"
                 ")\n"
                 "SELECT salesperson, region, total_amount\n"
                 "FROM ranked_sales\n"
                 "WHERE region_rank = 1\n"
                 "ORDER BY region, salesperson;",
    data=dict(),
    oracle=lambda: sorted(
        [
            (r["salesperson"], region, r["total_amount"])
            for region, group in partition(SALES_REGIONS, "region").items()
            for r in group
            if r["total_amount"] == max(x["total_amount"] for x in group)
        ],
        key=lambda row: (row[1], row[0]),
    ),
    hints="South contributes two rows here, Sana Fatima and Tarun Bakshi, since both genuinely "
          "tie for first place in that region; North and East each contribute exactly one.",
))

assert len(Q) == 33, len(Q)

for q in Q:
    q["tags"] = f"dbms - {q['subTopics']}"

OUT = "content/Question Bank/Coding Questions/DBMS/5.2 - Window Functions - Coding Questions.xlsx"

if __name__ == "__main__":
    main(Q, OUT)
