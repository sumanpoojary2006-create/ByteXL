# Capstone Project: Library Book Management System

## Background

Every engineering college has a library, but most of them still track book borrowing in registers. LibTrack is a command-line library management system that lets librarians add books, register members, issue and return books, track overdue fines, and generate inventory reports.

This project draws on everything from Units 1 through 13: input validation, loops, lists and dictionaries, functions, file handling, basic OOP, and exception handling. You will build it in six stages, starting with a simple book catalogue and ending with a fully file-backed system with a clean class design and robust error handling.

## Stages

### Stage 1: Build the Book Catalogue

1. Ask the librarian to enter details for one book:
   - Title (text)
   - Author (text)
   - ISBN (text — treat as a string, not a number)
   - Total copies (integer)

2. Display the book entry in a formatted block after adding it.

3. Validate that total copies is a positive integer. Keep asking until valid input is received.

4. Validate that the ISBN is exactly 13 characters long. If not, display an error and ask again.

**Answer these questions after completing Stage 1:**
- Two books can have the same title but must have different ISBNs. What data structure would you use to enforce uniqueness when you extend to multiple books in Stage 2?
- Your ISBN validation checks length only. What other checks would a real library system need, and why are you not adding them now?

### Stage 2: Manage Multiple Books with a Menu

1. Build a main menu that repeats until the librarian exits:
   ```
   ========== LibTrack ==========
   1. Add Book
   2. View All Books
   3. Search by Title
   4. Search by Author
   5. Exit
   ==============================
   ```

2. Store all books as a list of dictionaries. Each book should track: `title`, `author`, `isbn`, `total_copies`, `available_copies` (initially equal to total copies).

3. Search by title and author should be case-insensitive and support partial matches — searching "pyt" should return books with "Python" in the title.

4. Display available copies alongside total copies in the book listing.

**Answer these questions after completing Stage 2:**
- Your search returns all partial matches. What happens if the library has 200 books and the user searches for "the"? Is this the right behaviour?
- `available_copies` starts equal to `total_copies`. Where in the program will these two values diverge, and what logic will govern that?

### Stage 3: Member Registration and Book Issuing

1. Add member management to the menu:
   - Register a member: name, member ID, email
   - View all members
   - Issue a book: takes member ID and ISBN, reduces available copies by 1, records the issue

2. Enforce these rules:
   - A member cannot borrow more than 3 books at a time
   - A book cannot be issued if available copies is 0
   - A member ID must be unique

3. Store issued books as a list of records with: `member_id`, `isbn`, `issue_date` (as a string in DD-MM-YYYY format), `due_date` (14 days after issue date — compute this using string arithmetic or the `datetime` module if covered).

**Answer these questions after completing Stage 3:**
- Your issuing logic checks two conditions: member borrow limit and book availability. In what order do you check them, and does the order matter for the user experience?
- What happens if a member ID is entered that does not exist in the system? Test this case and handle it if you have not.

### Stage 4: Returns, Fines, and Reports

1. Add a **Return Book** option: takes member ID and ISBN, increases available copies by 1, removes the issue record.

2. Compute overdue fines on return: ₹5 per day beyond the 14-day due date. If returned on time, the fine is ₹0.

3. Add a **Generate Report** option that displays:
   - Total books in the library
   - Total members registered
   - Currently issued books with member name and due date
   - Books with 0 available copies (fully issued out)

4. Add a **Member History** option: shows all books currently issued to a given member ID.

**Answer these questions after completing Stage 4:**
- Your fine calculation depends on today's date. What happens if the librarian's computer date is wrong? Is there anything your program can do about this?
- A book is returned but the issue record is not found. How does your program handle this? Test it and fix any crash.

### Stage 5: Redesign with Classes

1. Create a `Book` class with attributes `title`, `author`, `isbn`, `total_copies`, `available_copies` and methods `issue()`, `return_book()`, `is_available()`, and `__str__`.

2. Create a `Member` class with attributes `name`, `member_id`, `email`, `borrowed_books` (a list of ISBNs) and methods `borrow(isbn)`, `return_book(isbn)`, `can_borrow()`, and `__str__`.

3. Create a `Library` class that holds a dictionary of books (keyed by ISBN) and a dictionary of members (keyed by member ID). Move all business logic — issuing, returning, searching, reporting — into `Library` methods.

4. The main menu should only call `Library` methods. No business logic inside the menu loop.

**Answer these questions after completing Stage 5:**
- You now have three classes. Draw (on paper or in a comment) the relationship between them — which class holds references to which other class? Is this a good design?
- After the refactor, does issuing a book update both the `Book` object and the `Member` object? Trace through the code and confirm both are updated in a single `issue()` call.

### Stage 6: Make It Persistent and Robust

1. Save books, members, and issue records to three separate JSON files: `books.json`, `members.json`, `issues.json`. Load all three on startup.

2. Wrap all file operations in `try-except` blocks. Handle missing files (first run), corrupted JSON, and permission errors separately.

3. Add a custom exception `LibraryError` with two subclasses: `BookNotAvailableError` and `BorrowLimitExceededError`. Raise these in the appropriate `Library` methods and catch them in the menu.

4. Find and fix the following three bugs:

**Bug 1:**
```python
def return_book(self, isbn):
    self.available_copies += 1
    # available_copies could exceed total_copies
    # if return_book() is called twice for the same issue
```

**Bug 2:**
```python
def search_by_title(self, query):
    return [b for b in self.books if query in b.title]
    # case-sensitive — searching "python" misses "Python Programming"
```

**Bug 3:**
```python
def load_members(self):
    with open("members.json") as f:
        data = json.load(f)
    for m in data:
        self.members[m["member_id"]] = Member(m["name"], m["member_id"], m["email"])
    # borrowed_books list is not restored from the saved data
```

**Answer these questions after completing Stage 6:**
- Bug 3 means that after restarting the program, members appear to have no books borrowed. What real-world consequence would this have in a library — what incorrect action could a librarian take because of this bug?
- You now have three JSON files that must stay consistent with each other. What could go wrong if the program crashes after writing `books.json` but before writing `issues.json`?

## The Complete Picture

When all six stages are complete, LibTrack:

- Maintains a searchable catalogue of books with copy tracking
- Registers members and enforces borrowing limits
- Issues and returns books with automatic fine calculation
- Generates inventory and member history reports
- Persists all data across sessions in three JSON files
- Uses a clean three-class OOP design
- Handles bad input and file errors without crashing
- Has three realistic bugs identified and fixed
