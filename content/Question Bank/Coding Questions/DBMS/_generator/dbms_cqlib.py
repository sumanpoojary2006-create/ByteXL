"""Shared library for building ByteXL DBMS (PostgreSQL) coding-question xlsx files.

Design principle, mirrored from the Python cqlib.py: the question author supplies
a Python `oracle` function that computes the expected result rows by actually
running Python code against the same in-memory table data the SQL solution
targets. There is no local Postgres/Docker in this environment, so the oracle
substitutes for "run the solution and capture real output" -- it is executed
for real, so row selection, filtering, sorting, and arithmetic are verified by
code rather than hand-typed, even though the SQL <-> Python equivalence itself
is a manual (not executed) claim.

Output convention (no confirmed grader spec exists for SQL questions in this
codebase): a header line of the exact column/alias names the query would
produce, comma-separated, followed by one comma-separated data row per line,
NULL shown as the literal text NULL. The header line matters here specifically
because a no-header convention would make column-alias questions ungradeable
by output alone (AS only changes the header, never the data values). This is
stated explicitly in every question's Output Format section so it's
unambiguous to the student regardless of grader details.
"""

import decimal

import openpyxl

HEADERS = [
    "title", "description", "explanation", "score", "status", "difficulty",
    "bloomTaxonomy", "tags", "subjects", "topics", "subTopics", "companies",
    "codingType", "language", "supportAllLanguages", "enablePartialScore",
    "ignoreCase",
    "testcase1_input", "testcase1_output",
    "preloadCode_postgresql", "solution_postgresql", "hints",
]

DEFAULT_CONSTRAINTS = [
    "Query only the tables and columns described above; the schema is fixed and already loaded.",
    "Output must be comma-separated values: a header row of the exact column/alias "
    "names your query returns, then one data row per line, in the exact row order "
    "your query produces.",
    "A NULL value must appear as the literal text NULL.",
]


def sql_literal(value):
    """Render one Python value as a PostgreSQL literal for an INSERT statement."""
    if value is None:
        return "NULL"
    if isinstance(value, bool):
        return "TRUE" if value else "FALSE"
    if isinstance(value, (int, float, decimal.Decimal)):
        return str(value)
    escaped = str(value).replace("'", "''")
    return f"'{escaped}'"


def sql_insert(table, columns, rows):
    """Build an INSERT INTO ... VALUES ... statement from the same row dicts
    an oracle reads, so preloadCode can never drift from the data used to
    compute expected output."""
    values_lines = [
        "(" + ", ".join(sql_literal(row[c]) for c in columns) + ")"
        for row in rows
    ]
    values_block = ",\n".join(values_lines)
    cols = ", ".join(columns)
    return f"INSERT INTO {table} ({cols}) VALUES\n{values_block};"


def render_value(value):
    """Render one Python value into this bank's canonical CSV cell text."""
    if value is None:
        return "NULL"
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def render_rows(header, rows):
    """Render a header (list of column names) and data rows into the bank's
    comma-separated, header-plus-one-row-per-line text."""
    lines = [",".join(header)]
    lines += [",".join(render_value(v) for v in row) for row in rows]
    return "\n".join(lines)


def make_description(prose, schema_lines, header, sample_output, constraints=None):
    """Assemble the markdown description block used by every question."""
    parts = [prose.strip(), "", "### Schema"]
    for line in schema_lines:
        parts.append(f"- {line}")
    parts += ["", "### Output Format",
              f"Return columns, in this order, with exactly these header names: "
              f"{', '.join(header)}.",
              "Comma-separated values: header row first, then one data row per line.",
              "```", sample_output, "```", "",
              "### Constraints"]
    for c in (constraints or DEFAULT_CONSTRAINTS):
        parts.append(f"- {c}")
    return "\n".join(parts)


def build_workbook(questions, out_path, *, defaults=None):
    """Compute + validate every question's expected output, then write the xlsx.

    `questions` is a list of dicts with keys:
      title, prose, difficulty, topics, subTopics, schema_sql, header (list of
      exact output column/alias names), solution_sql, oracle (callable taking
      the dataset kwargs and returning a list of tuples), and optional
      description / constraints / score / hints / tags / explanation /
      bloomTaxonomy.
    Each question dict must also carry a `data` dict of the named table datasets
    the oracle needs (e.g. {"students": STUDENTS}).
    """
    defaults = defaults or {}
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    ws.append(HEADERS)

    report = []
    seen_titles = set()
    for q in questions:
        assert q["title"] not in seen_titles, f"duplicate title: {q['title']}"
        seen_titles.add(q["title"])

        rows = q["oracle"](**q["data"])
        assert rows or q.get("allow_empty_result"), (
            f"{q['title']}: oracle produced an empty result; if that is genuinely "
            f"correct, set allow_empty_result=True"
        )
        for r in rows:
            assert len(r) == len(q["header"]), (
                f"{q['title']}: row {r!r} has {len(r)} values, header has "
                f"{len(q['header'])} columns"
            )
        output = render_rows(q["header"], rows)

        desc = q.get("description") or make_description(
            q["prose"], q["schema_lines"], q["header"], output, q.get("constraints"),
        )
        row = {
            "title": q["title"],
            "description": desc,
            "explanation": q.get("explanation", ""),
            "score": q.get("score", 5),
            "status": "Published",
            "difficulty": q["difficulty"],
            "bloomTaxonomy": q.get("bloomTaxonomy", "apply"),
            "tags": q.get("tags", ""),
            "subjects": q.get("subjects", defaults.get("subjects", "dbms")),
            "topics": q["topics"],
            "subTopics": q["subTopics"],
            "companies": "",
            "codingType": "Database",
            "language": "PostgreSQL",
            "supportAllLanguages": False,
            "enablePartialScore": True,
            "ignoreCase": q.get("ignoreCase", True),
            "testcase1_input": "",
            "testcase1_output": output,
            "preloadCode_postgresql": q["schema_sql"].strip("\n"),
            "solution_postgresql": q["solution_sql"].strip("\n"),
            "hints": q.get("hints", ""),
        }
        ws.append([row[h] for h in HEADERS])
        report.append((q["title"], q["difficulty"], output.replace("\n", " | ")[:60]))

    wb.save(out_path)
    return report


def main(questions, out_path, *, defaults=None):
    """Convenience entry point: build, print a summary, verify counts."""
    from collections import Counter
    report = build_workbook(questions, out_path, defaults=defaults)
    diff = Counter(d for _, d, _ in report)
    print(f"Wrote {len(report)} questions -> {out_path}")
    print(f"  difficulty split: {dict(diff)}")
    for title, d, out in report:
        print(f"  [{d:6}] {title:42} -> {out}")
    return report
