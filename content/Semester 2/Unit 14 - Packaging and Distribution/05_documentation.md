## Introduction

A volunteer installs the library system package and opens Python. She types `help(LibraryDatabase)` and sees... nothing. The class has no docstrings. She reads the source code for twenty minutes trying to understand what `borrow_book` returns on failure. She emails Dev. Dev spends thirty minutes on a call explaining what he built.

Documentation is not an afterthought. For a package that others will install, it is the first thing they encounter and the primary reason they will succeed or give up.

![Three documentation layers: docstrings inside the code, a README at the project root for quick-start, and a hosted docs site for full reference](images/05_documentation.png)

## Docstrings: Documentation That Lives in Code

```python
class LibraryDatabase:
    """
    Manages a SQLite-backed library catalog.

    Provides methods to add books, search the catalog, record loans,
    and process returns. All write operations use transactions and roll
    back automatically on failure.

    Args:
        path: Path to the SQLite database file. Defaults to ':memory:'
              for an in-memory database (useful for testing).

    Example:
        db = LibraryDatabase("library.db")
        db.add_book(Book(title="Clean Code", author="Robert Martin",
                         isbn="978-0-13-235088-4", year=2008))
        results = db.find_books("Clean")
        db.close()
    """

    def find_books(self, query: str) -> list:
        """
        Search books by title or author.

        Args:
            query: Search string. Matched as a substring (case-insensitive)
                   against both title and author fields.

        Returns:
            List of sqlite3.Row objects with id, isbn, title, author,
            year, copies columns. Empty list if no matches.

        Example:
            results = db.find_books("Martin")
            for book in results:
                print(book['title'])
        """
        # Implementation here
        return []

    def borrow_book(self, isbn: str, member_name: str) -> str:
        """
        Record a book loan.

        Decrements the available copy count and creates a loan record.
        Uses a transaction: if either step fails, both are rolled back.

        Args:
            isbn: ISBN of the book to borrow.
            member_name: Name of the borrowing member.

        Returns:
            A success message string on success, or an error message
            string starting with 'Error:' if the book is not found
            or no copies are available.

        Example:
            msg = db.borrow_book("978-0-13-235088-4", "Alice Chen")
            if msg.startswith("Error"):
                print("Could not complete loan:", msg)
        """
        return ""


# Demonstrate that help() works
import inspect
print("Docstring for LibraryDatabase:")
print(inspect.cleandoc(LibraryDatabase.__doc__))
print()
print("Docstring for borrow_book:")
print(inspect.cleandoc(LibraryDatabase.borrow_book.__doc__))
```

## Docstring Styles

```python
# Three common docstring styles -- pick one and be consistent

def add_book_google_style(title: str, author: str, year: int) -> int:
    """Add a book to the catalog.

    Args:
        title: Book title.
        author: Author's full name.
        year: Publication year.

    Returns:
        The database id assigned to the new book.

    Raises:
        ValueError: If title or author is empty.
        sqlite3.IntegrityError: If a book with the same ISBN already exists.
    """
    return 0


def add_book_numpy_style(title: str, author: str, year: int) -> int:
    """Add a book to the catalog.

    Parameters
    ----------
    title : str
        Book title.
    author : str
        Author's full name.
    year : int
        Publication year.

    Returns
    -------
    int
        The database id assigned to the new book.
    """
    return 0


import inspect
print("Google style docstring:")
print(inspect.cleandoc(add_book_google_style.__doc__))
print()
print("NumPy style docstring:")
print(inspect.cleandoc(add_book_numpy_style.__doc__))
```

## README: The First Thing Anyone Reads

```python
# A good README follows this structure

readme_sections = [
    ("Project name + one-line description",
     "What is this? Can I use it in 5 seconds?"),
    ("Badges (optional)",
     "CI status, coverage, PyPI version"),
    ("Quick start / installation",
     "pip install library-system"),
    ("Usage example",
     "from library import LibraryDatabase; db = ..."),
    ("Feature list",
     "What can it do?"),
    ("Contributing",
     "How to submit changes"),
    ("License",
     "MIT, Apache 2.0, etc."),
]

print("README structure and why each section exists:")
print()
for section, purpose in readme_sections:
    print(f"  ## {section}")
    print(f"     Purpose: {purpose}")
    print()
```

## Writing a Useful README Quick-Start Section

```python
# The quick-start section must run without errors

quickstart_code = '''
# Installation
pip install library-system

# Basic usage
from library import LibraryDatabase, Book

db = LibraryDatabase("catalog.db")

# Add a book
db.add_book(Book(
    title="Clean Code",
    author="Robert Martin",
    isbn="978-0-13-235088-4",
    year=2008,
    copies=3,
))

# Search
results = db.find_books("Clean")
for book in results:
    print(book["title"], "--", book["author"])

# Borrow
msg = db.borrow_book("978-0-13-235088-4", "Alice Chen")
print(msg)
'''

print("A complete, runnable quick-start example:")
print(quickstart_code)

# Key principle: every code example in documentation must run
examples_rules = [
    "Every import must be to a real module",
    "Variable names must be consistent (no undefined 'db' appearing from nowhere)",
    "The example must produce visible output or a clear state change",
    "If setup is needed (database file, config), show that setup first",
]

print("Rules for documentation code examples:")
for rule in examples_rules:
    print(f"  - {rule}")
```

## Generating API Reference Documentation

```python
# pydoc generates HTML documentation from docstrings
# mkdocs + mkdocstrings creates a hosted documentation site

doc_tools = [
    ("pydoc",          "Built into Python. 'python -m pydoc library' in terminal."),
    ("help()",         "Built into Python. 'help(LibraryDatabase)' in REPL."),
    ("mkdocs",         "Generates a static site from Markdown + docstrings."),
    ("Sphinx",         "Most powerful; used by NumPy, Django, many large projects."),
    ("pdoc",           "Zero-config HTML docs from docstrings. Quick to set up."),
]

print("Documentation generation tools:")
for tool, description in doc_tools:
    print(f"  {tool:<18}: {description}")

print()
print("For the library project, pdoc is the best starting point:")
print("  $ pip install pdoc")
print("  $ pdoc library/  # opens browser with rendered API docs")
```

## Documentation at a Glance

| Layer | Where | Audience | Tool |
|---|---|---|---|
| Docstrings | Inside source code | Developers using `help()` or IDE | Built-in Python |
| README | Project root | Anyone who clones or installs | Markdown |
| API reference | Generated site | Developers integrating the package | pdoc / Sphinx |
| Changelog | CHANGELOG.md | Existing users upgrading | Markdown |

## Your Turn

Add a docstring to the `borrow_book` function in your library project that includes:
- A one-sentence description
- `Args:` section with `isbn` and `member_name`
- `Returns:` section explaining the success and error message formats
- A one-line `Example:` showing a call and its output

Then run `python -m pydoc -w library.database` and open the generated HTML file.

## Conclusion

Docstrings are documentation that lives with the code and is accessible through `help()`, IDE tooltips, and documentation generators. The README quick-start section is the most important page in the project -- it determines whether a new user succeeds in the first five minutes. Generated API reference documentation scales the docstrings into a browsable site. The next lesson brings the entire semester together in a capstone project.
