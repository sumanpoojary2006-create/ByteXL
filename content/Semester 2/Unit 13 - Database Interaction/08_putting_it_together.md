## Introduction

Dev has all the pieces: a table, parameterized queries, transactions, a row factory, and migrations. This lesson assembles them into a complete `LibraryDatabase` module that the CLI tool from Unit 12 can import and use. It is the first component of the library system that persists data reliably across restarts.

![The complete system: LibraryDatabase module in the center, CLI calling it on the left, the SQLite file persisting data on the right, unit tests talking to an in-memory database at the bottom](images/08_putting_it_together.png)

## The Complete LibraryDatabase Module

```python
import sqlite3
from dataclasses import dataclass
from typing import Optional, List

# ── Data Models ──────────────────────────────────────────────────────────────

@dataclass
class Book:
    title: str
    author: str
    isbn: str
    year: int
    copies: int = 1
    genre: str = "General"
    id: Optional[int] = None

@dataclass
class Loan:
    book_id: int
    member_name: str
    loan_date: str
    id: Optional[int] = None

# ── Schema migrations ─────────────────────────────────────────────────────────

MIGRATIONS = [
    (1, """CREATE TABLE IF NOT EXISTS books (
               id      INTEGER PRIMARY KEY AUTOINCREMENT,
               isbn    TEXT    UNIQUE NOT NULL,
               title   TEXT    NOT NULL,
               author  TEXT    NOT NULL,
               year    INTEGER,
               copies  INTEGER DEFAULT 1,
               genre   TEXT    DEFAULT 'General'
           )"""),
    (2, """CREATE TABLE IF NOT EXISTS loans (
               id          INTEGER PRIMARY KEY AUTOINCREMENT,
               book_id     INTEGER NOT NULL REFERENCES books(id),
               member_name TEXT    NOT NULL,
               loan_date   TEXT    NOT NULL
           )"""),
    (3, """CREATE TABLE IF NOT EXISTS schema_version (version INTEGER)"""),
]

def _apply_migrations(conn):
    conn.execute("CREATE TABLE IF NOT EXISTS schema_version (version INTEGER)")
    row = conn.execute("SELECT MAX(version) FROM schema_version").fetchone()
    current = row[0] or 0
    for version, sql in MIGRATIONS:
        if version > current:
            conn.execute(sql)
            conn.execute("INSERT INTO schema_version VALUES (?)", (version,))
    conn.commit()
    return current

# ── Database class ────────────────────────────────────────────────────────────

class LibraryDatabase:
    def __init__(self, path=":memory:"):
        self.conn = sqlite3.connect(path)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute("PRAGMA foreign_keys = ON")
        _apply_migrations(self.conn)

    # ── Books ─────────────────────────────────────────────────────────────────

    def add_book(self, book: Book) -> int:
        with self.conn:
            cursor = self.conn.execute(
                "INSERT INTO books (isbn, title, author, year, copies, genre) VALUES (?, ?, ?, ?, ?, ?)",
                (book.isbn, book.title, book.author, book.year, book.copies, book.genre),
            )
        return cursor.lastrowid

    def find_books(self, query: str) -> List[sqlite3.Row]:
        pattern = f"%{query}%"
        cursor = self.conn.execute(
            "SELECT id, isbn, title, author, year, copies FROM books WHERE title LIKE ? OR author LIKE ?",
            (pattern, pattern),
        )
        return cursor.fetchall()

    def all_books(self) -> List[sqlite3.Row]:
        cursor = self.conn.execute(
            "SELECT id, isbn, title, author, year, copies, genre FROM books ORDER BY title"
        )
        return cursor.fetchall()

    # ── Loans ─────────────────────────────────────────────────────────────────

    def borrow_book(self, isbn: str, member_name: str) -> str:
        with self.conn:
            row = self.conn.execute(
                "SELECT id, copies FROM books WHERE isbn = ?", (isbn,)
            ).fetchone()
            if row is None:
                return f"Error: book '{isbn}' not found"
            if row["copies"] < 1:
                return f"Error: no copies of '{isbn}' available"
            self.conn.execute(
                "UPDATE books SET copies = copies - 1 WHERE isbn = ?", (isbn,)
            )
            self.conn.execute(
                "INSERT INTO loans (book_id, member_name, loan_date) VALUES (?, ?, date('now'))",
                (row["id"], member_name),
            )
        return f"Loaned '{isbn}' to {member_name}"

    def return_book(self, isbn: str, member_name: str) -> str:
        with self.conn:
            row = self.conn.execute(
                """SELECT l.id, b.isbn FROM loans l
                   JOIN books b ON b.id = l.book_id
                   WHERE b.isbn = ? AND l.member_name = ?
                   LIMIT 1""",
                (isbn, member_name),
            ).fetchone()
            if row is None:
                return f"Error: no active loan for {member_name} / {isbn}"
            self.conn.execute("DELETE FROM loans WHERE id = ?", (row["id"],))
            self.conn.execute("UPDATE books SET copies = copies + 1 WHERE isbn = ?", (isbn,))
        return f"Return recorded: '{isbn}' from {member_name}"

    def active_loans(self) -> List[sqlite3.Row]:
        cursor = self.conn.execute(
            """SELECT l.id, b.title, l.member_name, l.loan_date
               FROM loans l JOIN books b ON b.id = l.book_id
               ORDER BY l.loan_date"""
        )
        return cursor.fetchall()

    def close(self):
        self.conn.close()


# ── Demonstration ─────────────────────────────────────────────────────────────

db = LibraryDatabase()  # in-memory for this demo

# Add books
books = [
    Book("Clean Code",          "Robert Martin",   "978-0-13-235088-4", 2008, copies=3, genre="Programming"),
    Book("Design Patterns",     "Gang of Four",    "978-0-20-163361-0", 1994, copies=2, genre="Architecture"),
    Book("Fluent Python",       "Luciano Ramalho", "978-1-49-193200-3", 2022, copies=4, genre="Programming"),
    Book("The Pragmatic Programmer", "Thomas & Hunt", "978-0-13-595705-9", 2019, copies=2, genre="Programming"),
]
for b in books:
    book_id = db.add_book(b)
    print(f"Added book id={book_id}: {b.title}")

print()

# Search
results = db.find_books("Python")
print(f"Search 'Python' -> {len(results)} result(s)")
for r in results:
    print(f"  {r['title']} ({r['copies']} copies)")

print()

# Borrow
print(db.borrow_book("978-0-13-235088-4", "Alice"))
print(db.borrow_book("978-0-13-235088-4", "Bob"))
print(db.borrow_book("978-0-20-163361-0", "Carol"))

print()

# Active loans
loans = db.active_loans()
print(f"Active loans ({len(loans)}):")
for loan in loans:
    print(f"  '{loan['title']}' -> {loan['member_name']} on {loan['loan_date']}")

print()

# Return
print(db.return_book("978-0-13-235088-4", "Alice"))

# Confirm copy restored
results2 = db.find_books("Clean Code")
print(f"Clean Code copies after return: {results2[0]['copies']}")

db.close()
```

## Writing Tests Against the Module

The in-memory database makes testing effortless: each test starts with a fresh database, no teardown needed.

```python
import sqlite3
from dataclasses import dataclass
from typing import Optional

@dataclass
class Book:
    title: str
    author: str
    isbn: str
    year: int
    copies: int = 1
    genre: str = "General"
    id: Optional[int] = None

def make_test_db():
    conn = sqlite3.connect(":memory:")
    conn.row_factory = sqlite3.Row
    conn.execute("""CREATE TABLE books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        isbn TEXT UNIQUE NOT NULL,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year INTEGER,
        copies INTEGER DEFAULT 1,
        genre TEXT DEFAULT 'General'
    )""")
    conn.execute("""CREATE TABLE loans (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        book_id INTEGER NOT NULL,
        member_name TEXT NOT NULL,
        loan_date TEXT NOT NULL
    )""")
    conn.commit()
    return conn

def add_book(conn, book):
    with conn:
        cursor = conn.execute(
            "INSERT INTO books (isbn, title, author, year, copies, genre) VALUES (?, ?, ?, ?, ?, ?)",
            (book.isbn, book.title, book.author, book.year, book.copies, book.genre),
        )
    return cursor.lastrowid

def get_copies(conn, isbn):
    row = conn.execute("SELECT copies FROM books WHERE isbn = ?", (isbn,)).fetchone()
    return row["copies"] if row else None

# Test: adding a book
conn = make_test_db()
book_id = add_book(conn, Book("Test Book", "Test Author", "978-1-11-111111-1", 2024, copies=2))
assert book_id == 1, f"Expected id=1, got {book_id}"
print("PASS: book added with correct id")

# Test: copy count tracked correctly
assert get_copies(conn, "978-1-11-111111-1") == 2
print("PASS: initial copies correct")

# Test: duplicate isbn rejected
try:
    add_book(conn, Book("Duplicate", "Author", "978-1-11-111111-1", 2024))
    print("FAIL: should have raised IntegrityError")
except sqlite3.IntegrityError:
    print("PASS: duplicate isbn rejected")

conn.close()
print("\nAll tests passed")
```

## Putting It Together at a Glance

| Layer | Responsibility |
|---|---|
| Data models (`@dataclass`) | Hold row data with type information |
| Migrations | Evolve schema safely, run once per version |
| Repository methods | Encapsulate all SQL, handle transactions |
| `sqlite3.Row` factory | Column-name access on query results |
| `:memory:` in tests | Fresh isolated database for each test |

## Your Turn

Add a `get_stats()` method to `LibraryDatabase` that returns a dictionary with total books, total copies, active loans count, and most-borrowed genre. Use a single query with `COUNT` and `GROUP BY` where possible.

## Conclusion

This unit built a complete database layer: SQLite3 basics, parameterized queries, transactions, row factories, schema migrations, and an ORM-style repository. All of these skills apply directly to PostgreSQL and other databases -- the API differences are in the driver, not in the concepts. Unit 14 moves to packaging: how to turn the library system into a distributable Python package that anyone can install with `pip install`.
