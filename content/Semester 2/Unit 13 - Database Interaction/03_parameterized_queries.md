## Introduction

Dev shows a junior volunteer the search feature. The volunteer types `'; DROP TABLE books; --` into the search box and grins. Dev's stomach drops. The catalog searches by building a string like `"SELECT * FROM books WHERE title LIKE '%" + user_input + "%'"`. That one input would delete the entire catalog.

Parameterized queries close this vulnerability completely. They are not a nice-to-have; they are the minimum bar for any code that touches a database.

![Two code paths: string concatenation building a query with malicious input injected; parameterized query with the placeholder keeping user input and SQL syntax completely separate](images/03_parameterized_queries.png)

## The Injection Vulnerability

```python
import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT, author TEXT)")
cursor.execute("INSERT INTO books (title, author) VALUES ('Clean Code', 'Robert Martin')")
cursor.execute("INSERT INTO books (title, author) VALUES ('Design Patterns', 'Gang of Four')")
conn.commit()

# DANGEROUS -- never do this with real user input
def search_unsafe(user_input):
    query = f"SELECT title FROM books WHERE title LIKE '%{user_input}%'"
    print("Query built:", query)
    cursor.execute(query)
    return cursor.fetchall()

# Normal search works fine
results = search_unsafe("Code")
print("Normal search results:", results)

# Malicious input -- the comment (--) discards the rest of the query
# In a real scenario the attacker could add ; DROP TABLE books; --
print("\nDangerous because user controls the SQL text directly")
conn.close()
```

The problem is that `user_input` is treated as SQL syntax. Any character that has meaning in SQL (quotes, semicolons, dashes) can change what the query does.

## The Safe Version: Parameterized Queries

```python
import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title TEXT, author TEXT)")

books = [
    ("Clean Code",       "Robert Martin"),
    ("Design Patterns",  "Gang of Four"),
    ("The Pragmatic Programmer", "Thomas & Hunt"),
]
cursor.executemany("INSERT INTO books (title, author) VALUES (?, ?)", books)
conn.commit()

def search_safe(user_input):
    # The ? is a placeholder -- the driver sends value and SQL separately
    cursor.execute("SELECT title, author FROM books WHERE title LIKE ?", (f"%{user_input}%",))
    return cursor.fetchall()

results = search_safe("Code")
print("Search for 'Code':")
for title, author in results:
    print(f"  {title} by {author}")

# Even with injection-looking input, only the literal string is searched
results2 = search_safe("'; DROP TABLE books; --")
print("\nSearch for malicious string:")
print("  Results:", results2)
print("  Table still exists -- injection had no effect")

conn.close()
```

The `?` tells the database driver: "the SQL ends here; the next argument is a data value, not code." The driver sends them on separate channels. No amount of SQL syntax in the value can alter the query structure.

## Named Placeholders

SQLite also supports named placeholders, which improve readability when a query has many parameters:

```python
import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE books (
        isbn TEXT PRIMARY KEY,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year INTEGER,
        copies INTEGER DEFAULT 1
    )
""")

book = {
    "isbn":   "978-0-13-235088-4",
    "title":  "Clean Code",
    "author": "Robert Martin",
    "year":   2008,
    "copies": 3,
}

cursor.execute(
    "INSERT INTO books VALUES (:isbn, :title, :author, :year, :copies)",
    book,
)
conn.commit()

cursor.execute("SELECT title, author, year FROM books WHERE isbn = :isbn", {"isbn": "978-0-13-235088-4"})
row = cursor.fetchone()
print(f"Found: '{row[0]}' by {row[1]} ({row[2]})")
conn.close()
```

Named placeholders (`:isbn`, `:title`) accept a dictionary instead of a tuple. When the query has five or more parameters, named placeholders are much easier to read and maintain than positional `?`.

## Filtering, Sorting, and Limiting

```python
import sqlite3

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT, year INTEGER, copies INTEGER)")

books = [
    ("The Pragmatic Programmer",  "Thomas & Hunt",   2019, 2),
    ("Clean Code",                "Robert Martin",   2008, 5),
    ("Design Patterns",           "Gang of Four",    1994, 1),
    ("Python Cookbook",           "Beazley & Jones", 2013, 3),
    ("Fluent Python",             "Luciano Ramalho", 2022, 4),
]
cursor.executemany("INSERT INTO books (title, author, year, copies) VALUES (?, ?, ?, ?)", books)
conn.commit()

# Filter by year range, order by year, limit results
cursor.execute("""
    SELECT title, author, year
    FROM books
    WHERE year >= ? AND copies >= ?
    ORDER BY year DESC
    LIMIT ?
""", (2000, 2, 3))

rows = cursor.fetchall()
print("Books since 2000 with 2+ copies (newest first, top 3):")
for title, author, year in rows:
    print(f"  {year}  {title:<30}  {author}")

conn.close()
```

## Parameterized Queries at a Glance

| Technique | Syntax | Use when |
|---|---|---|
| Positional placeholder | `WHERE id = ?`, tuple param | Few parameters, order is clear |
| Named placeholder | `WHERE id = :id`, dict param | Many parameters, readability matters |
| `executemany` | same SQL, list of tuples/dicts | Batch inserts or updates |
| Never do | `f"WHERE id = {user_id}"` | Never -- SQL injection risk |

## Your Turn

Write a function `find_by_author(cursor, author_name)` that uses a parameterized `LIKE` query to find all books whose author field contains `author_name`. Test it with a partial name like `"Thomas"` and confirm it returns the expected row without crashing on unusual input like `"O'Brien"`.

## Conclusion

Parameterized queries separate SQL syntax from data values at the protocol level. Nothing the user types can alter the query structure. Use `?` for positional parameters and `:name` for named parameters. String formatting for SQL is a security vulnerability, not a convenience. The next lesson covers transactions: how to group multiple queries so that either all of them succeed or none of them do.
