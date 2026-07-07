## Introduction

Dev has been running the library system for three months. The catalog lives in a Python dictionary that resets every time the script restarts. One afternoon a power cut wipes out the day's additions — 47 newly catalogued books, gone. Dev needs storage that survives process restarts, can be queried efficiently, and supports multiple users without corrupting each other's changes.

That storage is a relational database.

![A Python dictionary on the left losing its data when the process dies; a database on the right persisting data to disk and surviving restarts](images/01_why_databases.png)

## What a Relational Database Is

A relational database stores data in tables: rows and columns, like a spreadsheet, but with strict rules about types, relationships, and constraints. Unlike a CSV file, a database:

- Keeps data on disk automatically after every write
- Lets you search, filter, and sort millions of rows efficiently with a query language (SQL)
- Enforces rules so bad data cannot enter (e.g., a book without a title is rejected)
- Handles multiple writers at once without corruption, using transactions

```python
# Without a database: data lives only in memory
catalog = {}
catalog["978-0-13-110362-7"] = {"title": "The C Programming Language", "author": "Kernighan"}
# Process ends -> catalog is gone

print("In-memory catalog has", len(catalog), "book(s)")
print("Restarting would lose:", list(catalog.keys()))
```

## Why Not Just Use Files?

Files work for simple storage but break down quickly:

```python
import json

# Simulate reading and writing a file-based catalog
catalog_data = json.dumps([
    {"isbn": "978-0-13-110362-7", "title": "The C Programming Language"},
    {"isbn": "978-0-201-63361-0", "title": "The Pragmatic Programmer"},
])

catalog = json.loads(catalog_data)

# Finding a book requires scanning every entry
results = [b for b in catalog if "Programming" in b["title"]]
print("Search results:", len(results), "book(s) found")

# What if two processes write simultaneously?
# The second write overwrites the first -> data loss
print("Problem: no protection against concurrent writes")
```

The file approach has no concurrent-write protection, no partial-update atomicity, and gets slower as the file grows because every query scans the whole file.

## SQL: The Language of Databases

SQL (Structured Query Language) is the standard way to talk to a relational database. Four operations cover almost everything:

| SQL operation | What it does | Python analogy |
|---|---|---|
| `SELECT` | Read rows | `list comprehension` / `filter` |
| `INSERT` | Add a row | `list.append()` |
| `UPDATE` | Change existing rows | `dict[key] = value` |
| `DELETE` | Remove rows | `list.remove()` |

```python
# SQL examples (as strings -- we will execute these in the next lesson)
select_all     = "SELECT title, author FROM books"
insert_book    = "INSERT INTO books (title, author, year) VALUES (?, ?, ?)"
update_copies  = "UPDATE books SET copies = copies + 1 WHERE isbn = ?"
delete_book    = "DELETE FROM books WHERE isbn = ?"

for stmt in [select_all, insert_book, update_copies, delete_book]:
    operation = stmt.split()[0]
    print(f"{operation:8s} -> {stmt[:50]}")
```

## SQLite: The Right Starting Point

Python ships with `sqlite3` in the standard library. SQLite stores an entire database in a single file. There is no separate server to install or configure. For the library system this is ideal: one file, no infrastructure, full SQL support.

```python
import sqlite3

# sqlite3 is in the standard library -- no pip install needed
print("sqlite3 version:", sqlite3.sqlite_version)
print("Python module version:", sqlite3.version)

# A database can also live entirely in memory (good for tests)
conn = sqlite3.connect(":memory:")
print("Connection created:", conn)

# Always close connections when done
conn.close()
print("Connection closed cleanly")
```

## When to Reach for a Real Database Server

SQLite is right for:
- Single-user applications
- Embedded databases (mobile apps, desktop tools)
- Development and testing environments
- Read-heavy workloads with moderate data size

Reach for PostgreSQL or MySQL when:
- Multiple servers write simultaneously
- The dataset grows beyond a few gigabytes
- You need advanced indexing, full-text search, or geographic queries
- Compliance requires a hardened server with access controls

```python
# Decision guide as data
scenarios = [
    ("library CLI tool, one librarian", "SQLite"),
    ("library web app, 10 concurrent staff", "PostgreSQL"),
    ("unit tests for database code", "SQLite :memory:"),
    ("embedded reader app on a tablet", "SQLite"),
    ("national library system, millions of records", "PostgreSQL"),
]

print(f"{'Scenario':<45} {'Recommendation'}")
print("-" * 60)
for scenario, choice in scenarios:
    print(f"{scenario:<45} {choice}")
```

## Why Databases at a Glance

| Problem with files | Database solution |
|---|---|
| Data lost on restart | Persisted to disk automatically |
| Slow scans for queries | Indexes speed up lookups |
| Concurrent write corruption | Transactions with locking |
| No schema enforcement | Column types and constraints |
| Hard to join related data | Foreign keys and JOIN queries |

## Your Turn

Run the code block above that prints `sqlite3.sqlite_version`. Confirm the module is available in your environment without any installation step. Then answer: what would happen to the in-memory catalog dictionary if you called the script twice in a row? What would happen with an SQLite file-based database?

## Conclusion

Relational databases solve the core problems that dictionaries and files cannot: persistence, concurrent access, efficient querying, and schema enforcement. SQLite is the right first database for the library system because it requires no server and ships with Python. The next lesson opens a real SQLite database and creates the first table.
