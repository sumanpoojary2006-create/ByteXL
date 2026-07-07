## Introduction

The library system has been running for a month with a `books` table. Dev needs to add a `genre` column so librarians can filter by category. But the table already has 600 rows. Running `CREATE TABLE` again would fail -- the table exists. Deleting and recreating it would lose all the data.

Schema migration is the process of modifying a live database schema without destroying its data. Every production database eventually needs it.

![A timeline showing a books table evolving: v1 has 4 columns, an ALTER TABLE adds genre in v2, another adds a series table in v3, each step tracked by a migrations log](images/06_schema_migrations.png)

## Checking What the Schema Looks Like

Before changing a schema, inspect the current structure:

```python
import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# Simulate an existing v1 database
cursor.execute("""
    CREATE TABLE books (
        id     INTEGER PRIMARY KEY AUTOINCREMENT,
        isbn   TEXT UNIQUE NOT NULL,
        title  TEXT NOT NULL,
        author TEXT NOT NULL,
        year   INTEGER
    )
""")
cursor.executemany("INSERT INTO books (isbn, title, author, year) VALUES (?, ?, ?, ?)", [
    ("978-0-13-235088-4", "Clean Code",      "Robert Martin",   2008),
    ("978-0-20-163361-0", "Design Patterns", "Gang of Four",    1994),
])
conn.commit()

# Inspect the schema
cursor.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='books'")
print("Current schema:")
print(cursor.fetchone()[0])

cursor.execute("PRAGMA table_info(books)")
print("\nColumn details:")
for col in cursor.fetchall():
    print(f"  cid={col[0]}, name={col[1]}, type={col[2]}, notnull={col[3]}")

conn.close()
```

`PRAGMA table_info(table_name)` returns one row per column with name, type, and constraints.

## ALTER TABLE: Adding a Column

```python
import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        isbn TEXT UNIQUE NOT NULL,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year INTEGER
    )
""")
cursor.executemany("INSERT INTO books (isbn, title, author, year) VALUES (?, ?, ?, ?)", [
    ("978-0-13-235088-4", "Clean Code",      "Robert Martin",   2008),
    ("978-0-20-163361-0", "Design Patterns", "Gang of Four",    1994),
    ("978-0-59-651798-1", "Python Cookbook", "Beazley & Jones", 2013),
])
conn.commit()

print("BEFORE migration:")
cursor.execute("SELECT title, author FROM books")
for row in cursor.fetchall():
    print(f"  {row[0]} by {row[1]}")

# Migration: add the genre column with a default value
cursor.execute("ALTER TABLE books ADD COLUMN genre TEXT DEFAULT 'General'")
conn.commit()

print("\nAFTER migration:")
cursor.execute("SELECT title, genre FROM books")
for row in cursor.fetchall():
    print(f"  {row[0]}: genre='{row[1]}'")

# Update specific rows with their actual genre
cursor.execute("UPDATE books SET genre = 'Programming' WHERE author LIKE '%Martin%'")
cursor.execute("UPDATE books SET genre = 'Architecture' WHERE title = 'Design Patterns'")
conn.commit()

print("\nAFTER backfill:")
cursor.execute("SELECT title, genre FROM books")
for row in cursor.fetchall():
    print(f"  {row[0]}: {row[1]}")

conn.close()
```

`ALTER TABLE ... ADD COLUMN` is the safest SQLite migration. Existing rows get the default value. No data is lost.

## Tracking Migrations with a Version Table

For anything beyond a single ALTER, use a migrations table to track which changes have been applied:

```python
import sqlite3

MIGRATIONS = [
    (1, "CREATE TABLE books (id INTEGER PRIMARY KEY AUTOINCREMENT, isbn TEXT UNIQUE, title TEXT, author TEXT, year INTEGER)"),
    (2, "ALTER TABLE books ADD COLUMN genre TEXT DEFAULT 'General'"),
    (3, "CREATE TABLE members (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, email TEXT UNIQUE)"),
]

def get_current_version(conn):
    conn.execute("CREATE TABLE IF NOT EXISTS schema_version (version INTEGER)")
    row = conn.execute("SELECT MAX(version) FROM schema_version").fetchone()
    return row[0] or 0

def run_migrations(conn):
    current = get_current_version(conn)
    print(f"Database is at schema version {current}")

    for version, sql in MIGRATIONS:
        if version > current:
            print(f"  Applying migration {version}: {sql[:50]}...")
            conn.execute(sql)
            conn.execute("INSERT INTO schema_version VALUES (?)", (version,))
            conn.commit()
            print(f"  Migration {version} applied")

    final = get_current_version(conn)
    print(f"Database is now at schema version {final}")

conn = sqlite3.connect(":memory:")
run_migrations(conn)

# Run again -- should apply nothing
print()
run_migrations(conn)

conn.close()
```

Each migration has a version number. The function applies only migrations whose version is higher than the current database version. Running it twice is safe because already-applied migrations are skipped.

## What SQLite Cannot Do with ALTER TABLE

SQLite's `ALTER TABLE` only supports `ADD COLUMN` and `RENAME`. For more complex changes (remove a column, change a column type, rename a column in older SQLite), the workaround is:

```python
import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# Original table
cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, isbn TEXT, titl TEXT, author TEXT)")
cursor.execute("INSERT INTO books VALUES (1, '978-0', 'Clean Code', 'Martin')")
conn.commit()

# Cannot ALTER TABLE to rename titl -> title in older SQLite
# Workaround: create new table, copy data, drop old, rename
cursor.execute("""
    CREATE TABLE books_new (
        id INTEGER PRIMARY KEY,
        isbn TEXT,
        title TEXT,
        author TEXT
    )
""")
cursor.execute("INSERT INTO books_new SELECT id, isbn, titl, author FROM books")
cursor.execute("DROP TABLE books")
cursor.execute("ALTER TABLE books_new RENAME TO books")
conn.commit()

cursor.execute("SELECT * FROM books")
print("After rename-column migration:")
for row in cursor.fetchall():
    print(f"  {row}")

cursor.execute("PRAGMA table_info(books)")
print("\nColumn names:")
for col in cursor.fetchall():
    print(f"  {col[1]}")

conn.close()
```

## Schema Migrations at a Glance

| Operation | SQLite support | Notes |
|---|---|---|
| Add column | `ALTER TABLE t ADD COLUMN c TYPE DEFAULT v` | Safe on live data |
| Rename table | `ALTER TABLE old RENAME TO new` | Safe |
| Rename column | Supported in SQLite 3.25+ | Check version first |
| Remove column | Not directly | Use create-copy-drop-rename workaround |
| Change column type | Not directly | Use create-copy-drop-rename workaround |
| Track versions | Custom `schema_version` table | Apply each migration once |

## Your Turn

Add a migration step 4 to the `MIGRATIONS` list that creates a `genres` reference table with columns `(id INTEGER PRIMARY KEY, name TEXT UNIQUE)`. Run the migration system and confirm step 4 is applied on the first call and skipped on the second.

## Conclusion

Schema migrations evolve the database structure without destroying existing data. `ALTER TABLE ... ADD COLUMN` is the safest SQLite operation. A version table ensures each migration runs exactly once. For changes beyond adding columns, the create-copy-drop-rename pattern handles the limitation safely. The next lesson looks at connecting Python to a PostgreSQL database and the differences between the two drivers.
