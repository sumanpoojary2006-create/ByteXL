## Introduction

Every character in Semester 2 worked on a piece of the library system. Tara built context managers for safe resource handling. Nadia used the standard library for data processing. Sam wrote tests. Raj enforced code quality. Miguel made the event loop work efficiently. Yuna parallelized the heavy operations. Priya built the CLI. Dev connected everything to a database.

This capstone brings all of those pieces together into one installable, tested, documented package.

![The whole team gathered around a single repository: Tara (context managers), Nadia (stdlib), Sam (tests), Raj (pre-commit), Miguel (async), Yuna (threading), Priya (CLI), Dev (database) -- all contributing to one package](images/06_capstone_project.png)

## What to Build

The `library-system` package must:

```python
# Requirements checklist as executable documentation

requirements = {
    "Structure":     "src layout with library/ package inside src/",
    "Database":      "sqlite3 backend via LibraryDatabase class",
    "CLI":           "typer commands: add, search, borrow, return, status",
    "Tests":         "pytest suite covering happy path + edge cases",
    "Code quality":  "ruff + black + mypy all pass with no errors",
    "Pre-commit":    ".pre-commit-config.yaml with ruff, black, mypy",
    "pyproject.toml":"complete metadata, entry point, optional deps",
    "Docstrings":    "all public classes and methods documented",
    "README":        "quick-start that runs without errors",
}

print("Capstone requirements:")
for category, requirement in requirements.items():
    print(f"  [{category}]")
    print(f"    {requirement}")
    print()
```

## The Core Data Model

```python
from dataclasses import dataclass, field
from typing import Optional
from datetime import date

@dataclass
class Book:
    title: str
    author: str
    isbn: str
    year: int
    copies: int = 1
    genre: str = "General"
    id: Optional[int] = None

    def is_available(self) -> bool:
        return self.copies > 0

    def __str__(self) -> str:
        status = "available" if self.is_available() else "all copies out"
        return f"[{self.isbn}] {self.title} by {self.author} ({self.year}) -- {status}"


@dataclass
class Loan:
    book_id: int
    member_name: str
    loan_date: date = field(default_factory=date.today)
    id: Optional[int] = None

    def days_outstanding(self) -> int:
        return (date.today() - self.loan_date).days

    def __str__(self) -> str:
        days = self.days_outstanding()
        return f"{self.member_name} -> book_id={self.book_id} ({days} days ago)"


# Demo
book = Book(
    title="Clean Code",
    author="Robert Martin",
    isbn="978-0-13-235088-4",
    year=2008,
    copies=2,
    genre="Programming",
    id=1,
)
print(book)
print("Available?", book.is_available())

loan = Loan(book_id=1, member_name="Alice Chen")
print(loan)
print("Days outstanding:", loan.days_outstanding())
```

## The Full LibraryDatabase

```python
import sqlite3
from dataclasses import dataclass
from typing import Optional, List
from datetime import date

@dataclass
class Book:
    title: str
    author: str
    isbn: str
    year: int
    copies: int = 1
    genre: str = "General"
    id: Optional[int] = None

class LibraryDatabase:
    """Manages a SQLite-backed library catalog with full transaction support."""

    def __init__(self, path: str = ":memory:"):
        self.conn = sqlite3.connect(path)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute("PRAGMA foreign_keys = ON")
        self._setup()

    def _setup(self):
        with self.conn:
            self.conn.execute("""CREATE TABLE IF NOT EXISTS books (
                id      INTEGER PRIMARY KEY AUTOINCREMENT,
                isbn    TEXT    UNIQUE NOT NULL,
                title   TEXT    NOT NULL,
                author  TEXT    NOT NULL,
                year    INTEGER,
                copies  INTEGER DEFAULT 1,
                genre   TEXT    DEFAULT 'General'
            )""")
            self.conn.execute("""CREATE TABLE IF NOT EXISTS loans (
                id          INTEGER PRIMARY KEY AUTOINCREMENT,
                book_id     INTEGER NOT NULL REFERENCES books(id),
                member_name TEXT    NOT NULL,
                loan_date   TEXT    NOT NULL
            )""")

    def add_book(self, book: Book) -> int:
        with self.conn:
            cur = self.conn.execute(
                "INSERT INTO books (isbn, title, author, year, copies, genre) VALUES (?, ?, ?, ?, ?, ?)",
                (book.isbn, book.title, book.author, book.year, book.copies, book.genre),
            )
        return cur.lastrowid

    def search(self, query: str) -> List[sqlite3.Row]:
        pat = f"%{query}%"
        return self.conn.execute(
            "SELECT * FROM books WHERE title LIKE ? OR author LIKE ? ORDER BY title",
            (pat, pat),
        ).fetchall()

    def borrow(self, isbn: str, member: str) -> str:
        with self.conn:
            row = self.conn.execute("SELECT id, copies FROM books WHERE isbn=?", (isbn,)).fetchone()
            if not row:
                return f"Error: '{isbn}' not found"
            if row["copies"] < 1:
                return f"Error: no copies of '{isbn}' available"
            self.conn.execute("UPDATE books SET copies=copies-1 WHERE isbn=?", (isbn,))
            self.conn.execute(
                "INSERT INTO loans (book_id, member_name, loan_date) VALUES (?,?,date('now'))",
                (row["id"], member),
            )
        return f"Loaned '{isbn}' to {member}"

    def return_book(self, isbn: str, member: str) -> str:
        with self.conn:
            loan = self.conn.execute(
                "SELECT l.id FROM loans l JOIN books b ON b.id=l.book_id WHERE b.isbn=? AND l.member_name=? LIMIT 1",
                (isbn, member),
            ).fetchone()
            if not loan:
                return f"Error: no active loan for {member} / {isbn}"
            self.conn.execute("DELETE FROM loans WHERE id=?", (loan["id"],))
            self.conn.execute("UPDATE books SET copies=copies+1 WHERE isbn=?", (isbn,))
        return f"Return recorded"

    def stats(self) -> dict:
        total_books   = self.conn.execute("SELECT COUNT(*) FROM books").fetchone()[0]
        total_copies  = self.conn.execute("SELECT SUM(copies) FROM books").fetchone()[0] or 0
        active_loans  = self.conn.execute("SELECT COUNT(*) FROM loans").fetchone()[0]
        return {"total_books": total_books, "total_copies": total_copies, "active_loans": active_loans}

    def close(self):
        self.conn.close()


# Integration demo
db = LibraryDatabase()

catalog = [
    Book("Clean Code",           "Robert Martin",   "978-0-13-235088-4", 2008, 3, "Programming"),
    Book("Design Patterns",      "Gang of Four",    "978-0-20-163361-0", 1994, 2, "Architecture"),
    Book("Fluent Python",        "Luciano Ramalho", "978-1-49-193200-3", 2022, 4, "Programming"),
    Book("The Pragmatic Programmer", "Thomas & Hunt","978-0-13-595705-9", 2019, 2, "Programming"),
]
for b in catalog:
    db.add_book(b)

print("=== Library System Demo ===")
print()

results = db.search("Python")
print(f"Search 'Python': {len(results)} result(s)")
for r in results:
    print(f"  {r['title']} ({r['copies']} copies available)")

print()
print(db.borrow("978-0-13-235088-4", "Alice"))
print(db.borrow("978-0-13-235088-4", "Bob"))
print(db.borrow("978-0-13-235088-4", "Carol"))
print(db.borrow("978-0-13-235088-4", "Dave"))   # should fail

print()
stats = db.stats()
print("Stats:", stats)

print()
print(db.return_book("978-0-13-235088-4", "Alice"))
stats2 = db.stats()
print("Stats after return:", stats2)

db.close()
```

## Test Suite Sample

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

class LibraryDatabase:
    def __init__(self, path=":memory:"):
        self.conn = sqlite3.connect(path)
        self.conn.row_factory = sqlite3.Row
        with self.conn:
            self.conn.execute("""CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT, isbn TEXT UNIQUE NOT NULL,
                title TEXT NOT NULL, author TEXT NOT NULL, year INTEGER,
                copies INTEGER DEFAULT 1, genre TEXT DEFAULT 'General')""")
            self.conn.execute("""CREATE TABLE IF NOT EXISTS loans (
                id INTEGER PRIMARY KEY AUTOINCREMENT, book_id INTEGER NOT NULL,
                member_name TEXT NOT NULL, loan_date TEXT NOT NULL)""")

    def add_book(self, book):
        with self.conn:
            cur = self.conn.execute(
                "INSERT INTO books (isbn, title, author, year, copies, genre) VALUES (?,?,?,?,?,?)",
                (book.isbn, book.title, book.author, book.year, book.copies, book.genre))
        return cur.lastrowid

    def borrow(self, isbn, member):
        with self.conn:
            row = self.conn.execute("SELECT id, copies FROM books WHERE isbn=?", (isbn,)).fetchone()
            if not row: return f"Error: not found"
            if row["copies"] < 1: return "Error: no copies"
            self.conn.execute("UPDATE books SET copies=copies-1 WHERE isbn=?", (isbn,))
            self.conn.execute("INSERT INTO loans (book_id,member_name,loan_date) VALUES (?,?,date('now'))", (row["id"], member))
        return f"Loaned to {member}"

    def copies(self, isbn):
        row = self.conn.execute("SELECT copies FROM books WHERE isbn=?", (isbn,)).fetchone()
        return row["copies"] if row else None

# ── Tests ─────────────────────────────────────────────────────────────────────

def test_add_book():
    db = LibraryDatabase()
    book_id = db.add_book(Book("Clean Code", "Martin", "ISBN-001", 2008, copies=2))
    assert book_id == 1
    assert db.copies("ISBN-001") == 2
    print("PASS: test_add_book")

def test_borrow_reduces_copies():
    db = LibraryDatabase()
    db.add_book(Book("Clean Code", "Martin", "ISBN-002", 2008, copies=1))
    msg = db.borrow("ISBN-002", "Alice")
    assert "Loaned" in msg
    assert db.copies("ISBN-002") == 0
    print("PASS: test_borrow_reduces_copies")

def test_borrow_fails_when_no_copies():
    db = LibraryDatabase()
    db.add_book(Book("Clean Code", "Martin", "ISBN-003", 2008, copies=0))
    msg = db.borrow("ISBN-003", "Alice")
    assert msg.startswith("Error")
    print("PASS: test_borrow_fails_when_no_copies")

def test_borrow_nonexistent_book():
    db = LibraryDatabase()
    msg = db.borrow("ISBN-NOTEXIST", "Alice")
    assert msg.startswith("Error")
    print("PASS: test_borrow_nonexistent_book")

def test_duplicate_isbn_rejected():
    db = LibraryDatabase()
    db.add_book(Book("Book A", "Author", "ISBN-DUP", 2020))
    try:
        db.add_book(Book("Book B", "Author", "ISBN-DUP", 2021))
        print("FAIL: expected IntegrityError")
    except sqlite3.IntegrityError:
        print("PASS: test_duplicate_isbn_rejected")

# Run all tests
test_add_book()
test_borrow_reduces_copies()
test_borrow_fails_when_no_copies()
test_borrow_nonexistent_book()
test_duplicate_isbn_rejected()

print("\nAll 5 tests passed")
```

## The Complete Semester in One Picture

```python
# Every unit of Semester 2 contributed a layer to this system

semester_map = [
    ("Unit 1",  "Python Internals",     "Understand how Python executes your code"),
    ("Unit 2",  "Encapsulation",        "Book and Loan as clean data models"),
    ("Unit 3",  "Inheritance",          "Specialised book types (AudioBook, EBook)"),
    ("Unit 4",  "Iterators/Generators", "Stream catalog without loading all rows"),
    ("Unit 5",  "Decorators",           "@retry, @validate_isbn on database methods"),
    ("Unit 6",  "Context Managers",     "'with db:' ensures connection is closed"),
    ("Unit 7",  "Standard Library",     "datetime for loan dates, csv for exports"),
    ("Unit 8",  "Testing",              "pytest suite for every database operation"),
    ("Unit 9",  "Code Quality",         "pre-commit: ruff, black, mypy on every commit"),
    ("Unit 10", "Async Programming",    "Async batch import of 10,000 records"),
    ("Unit 11", "Multithreading",       "Parallel nightly backup with ThreadPoolExecutor"),
    ("Unit 12", "CLI Development",      "typer commands: add, search, borrow, return"),
    ("Unit 13", "Database Interaction", "sqlite3 with transactions and migrations"),
    ("Unit 14", "Packaging",            "pip install library-system works anywhere"),
]

print(f"{'Unit':<10} {'Topic':<25} {'Contribution to the system'}")
print("-" * 75)
for unit, topic, contribution in semester_map:
    print(f"{unit:<10} {topic:<25} {contribution}")
```

## Capstone at a Glance

| Component | File | Skills used |
|---|---|---|
| Data models | `library/models.py` | Dataclasses, type hints |
| Database layer | `library/database.py` | sqlite3, transactions, row factory |
| CLI | `library/cli.py` | typer, entry points |
| Tests | `tests/test_database.py` | pytest, fixtures, parametrize |
| Configuration | `pyproject.toml` | Packaging, tool config |
| Quality gates | `.pre-commit-config.yaml` | pre-commit, ruff, black, mypy |

## Your Turn

Complete the full capstone. Start with the project structure from Lesson 1, write `pyproject.toml` from Lesson 2, set up the virtual environment from Lesson 3, add `LibraryDatabase` from this lesson, write at least 10 tests, configure pre-commit, and confirm `pip install -e .` works.

The stretch goal: add an `async_import(csv_data)` method that uses `asyncio` to process rows concurrently.

## Conclusion

The capstone integrates every concept from Semester 2 into one working, tested, installable package. Context managers for safe connections. Dataclasses for typed models. Transactions for data integrity. pytest for confidence. pre-commit for consistent quality. typer for a usable interface. pyproject.toml for distribution.

Python as a language is just the beginning. What makes code professional is the ecosystem: structure, testing, automation, and the habit of shipping something others can install and trust.

Congratulations on completing Semester 2.
