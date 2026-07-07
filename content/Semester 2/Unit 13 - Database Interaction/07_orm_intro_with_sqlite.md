## Introduction

Dev's repository class works, but every time the schema changes he has to update two things: the SQL strings and the Python data model. A type error in an SQL string only shows up at runtime, not at import time. The book attributes have no IDE completion because they come from a dictionary.

An ORM (Object-Relational Mapper) bridges this gap. It lets you define tables as Python classes. The ORM generates the SQL. The Python class gives full type information and IDE support.

![A Book Python class on one side; a books database table on the other; the ORM arrow in the middle translating between them automatically](images/07_orm_intro_with_sqlite.png)

## What an ORM Does

```python
# Without ORM: SQL strings scattered through code
# cursor.execute("SELECT id, title, author FROM books WHERE year > ?", (2000,))

# With an ORM: query expressed as Python
# session.query(Book).filter(Book.year > 2000).all()

# The ORM translates the Python into SQL automatically
# Both reach the database the same way -- ORM adds a layer of abstraction

benefits = {
    "Type safety":        "Column types are declared in Python, not SQL strings",
    "IDE completion":     "book.title works; row['title'] doesn't autocomplete",
    "No SQL injection":   "ORM parameterizes automatically",
    "Schema migrations":  "ORM can generate ALTER TABLE statements",
    "Database agnostic":  "Same code works on SQLite and PostgreSQL",
}

print("ORM benefits:")
for benefit, description in benefits.items():
    print(f"  {benefit:<20}: {description}")
```

## SQLAlchemy Core: Building Queries as Python

SQLAlchemy is the most widely used Python ORM. It has two layers: Core (close to SQL) and ORM (full object mapping). We start with Core since it maps most directly to what you already know:

```python
# SQLAlchemy is not in the standard library.
# We simulate its concept here using sqlite3 directly.

import sqlite3
from dataclasses import dataclass, field
from typing import List, Optional

# Simulated ORM-style approach using Python classes + sqlite3
@dataclass
class BookRecord:
    title: str
    author: str
    year: int
    genre: str = "General"
    id: Optional[int] = None

class BookTable:
    CREATE_SQL = """
        CREATE TABLE IF NOT EXISTS books (
            id     INTEGER PRIMARY KEY AUTOINCREMENT,
            title  TEXT    NOT NULL,
            author TEXT    NOT NULL,
            year   INTEGER,
            genre  TEXT    DEFAULT 'General'
        )
    """

    def __init__(self, conn):
        self.conn = conn
        self.conn.row_factory = self._row_factory
        self.conn.execute(self.CREATE_SQL)
        self.conn.commit()

    @staticmethod
    def _row_factory(cursor, row):
        fields = [col[0] for col in cursor.description]
        data = dict(zip(fields, row))
        return BookRecord(**data)

    def insert(self, book: BookRecord) -> int:
        cursor = self.conn.execute(
            "INSERT INTO books (title, author, year, genre) VALUES (?, ?, ?, ?)",
            (book.title, book.author, book.year, book.genre),
        )
        self.conn.commit()
        return cursor.lastrowid

    def filter_by_year_after(self, year: int) -> List[BookRecord]:
        cursor = self.conn.execute(
            "SELECT id, title, author, year, genre FROM books WHERE year > ? ORDER BY year",
            (year,),
        )
        return cursor.fetchall()

    def all(self) -> List[BookRecord]:
        cursor = self.conn.execute("SELECT id, title, author, year, genre FROM books ORDER BY year")
        return cursor.fetchall()


conn = sqlite3.connect(":memory:")
table = BookTable(conn)

# Insert using typed objects -- no raw SQL in application code
table.insert(BookRecord("Clean Code",       "Robert Martin",   2008, "Programming"))
table.insert(BookRecord("Design Patterns",  "Gang of Four",    1994, "Architecture"))
table.insert(BookRecord("Fluent Python",    "Luciano Ramalho", 2022, "Programming"))
table.insert(BookRecord("The Pragmatic Programmer", "Thomas & Hunt", 2019, "Programming"))

print("All books:")
for book in table.all():
    print(f"  [{book.id}] {book.title:<30} {book.year}  ({book.genre})")

print("\nBooks after 2000:")
for book in table.filter_by_year_after(2000):
    print(f"  {book.title} ({book.year})")

conn.close()
```

## The Key Concept: Separating Schema from Logic

The ORM pattern keeps the schema definition in one place (the class) instead of scattered across SQL strings. When a column is added, only the class changes:

```python
import sqlite3
from dataclasses import dataclass
from typing import Optional

@dataclass
class Member:
    name: str
    email: str
    membership_tier: str = "standard"   # NEW column
    id: Optional[int] = None

class MemberRepository:
    def __init__(self, conn):
        self.conn = conn
        self.conn.row_factory = lambda cursor, row: Member(
            **dict(zip([col[0] for col in cursor.description], row))
        )
        conn.execute("""
            CREATE TABLE IF NOT EXISTS members (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                name            TEXT    NOT NULL,
                email           TEXT    UNIQUE NOT NULL,
                membership_tier TEXT    DEFAULT 'standard'
            )
        """)
        conn.commit()

    def add(self, member: Member) -> int:
        cursor = self.conn.execute(
            "INSERT INTO members (name, email, membership_tier) VALUES (?, ?, ?)",
            (member.name, member.email, member.membership_tier),
        )
        self.conn.commit()
        return cursor.lastrowid

    def get_by_tier(self, tier: str):
        cursor = self.conn.execute(
            "SELECT id, name, email, membership_tier FROM members WHERE membership_tier = ?",
            (tier,),
        )
        return cursor.fetchall()


conn = sqlite3.connect(":memory:")
repo = MemberRepository(conn)

repo.add(Member("Alice Chen",   "alice@example.com", "premium"))
repo.add(Member("Bob Sharma",   "bob@example.com",   "standard"))
repo.add(Member("Carol Davis",  "carol@example.com", "premium"))
repo.add(Member("Dev Patel",    "dev@example.com",   "standard"))

premium = repo.get_by_tier("premium")
print(f"Premium members ({len(premium)}):")
for m in premium:
    print(f"  {m.name} <{m.email}>")

standard = repo.get_by_tier("standard")
print(f"\nStandard members ({len(standard)}):")
for m in standard:
    print(f"  {m.name}")

conn.close()
```

## ORM vs Raw SQL: Choosing

```python
# Decision guide -- which approach fits which situation

scenarios = [
    ("Quick script, 1-2 queries",               "Raw sqlite3",        "No overhead, no dependency"),
    ("Application with many queries",            "Repository pattern", "Organizes code, still raw SQL"),
    ("Complex queries with joins",               "Raw sqlite3",        "SQL is clearer than ORM for joins"),
    ("Multi-database app (SQLite + Postgres)",   "SQLAlchemy ORM",     "Abstract away dialect differences"),
    ("Rapid prototyping",                        "SQLAlchemy ORM",     "Auto-generate schema from classes"),
    ("Performance-critical queries",             "Raw sqlite3",        "Fine-tune SQL directly"),
]

print(f"{'Scenario':<45} {'Choice':<22} {'Reason'}")
print("-" * 90)
for scenario, choice, reason in scenarios:
    print(f"{scenario:<45} {choice:<22} {reason}")
```

## ORM Intro at a Glance

| Concept | What it means |
|---|---|
| ORM | Maps Python classes to database tables |
| Schema in one place | Column definitions live in the class, not SQL strings |
| Row factory | Converts query results to typed Python objects |
| Repository pattern | Encapsulates all database access for a table |
| SQLAlchemy | Most popular Python ORM (two layers: Core and ORM) |

## Your Turn

Add a `LoanRepository` class that models loans with `book_id`, `member_id`, and `loan_date` columns. Write `borrow(book_id, member_id)` and `active_loans()` methods. Test both with data from `BookTable` and `MemberRepository` in the same in-memory database.

## Conclusion

An ORM bridges Python classes and database tables, placing schema definitions in one location and generating SQL automatically. Even without a full ORM library like SQLAlchemy, the repository pattern with a row factory achieves many of the same benefits using only the standard library. The final lesson in this unit brings everything together in a complete database-backed library management module.
