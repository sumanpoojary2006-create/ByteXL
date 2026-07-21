## Background

A contact book is one of the most natural applications for a dictionary — contacts have names (keys) and details (values). Building one teaches you how to structure data, write functions for each operation, and keep your code organised. By the time you finish, you will have a working tool you could actually use.

## What You Will Build

A CLI contact book where the user can add, view, search, update, and delete contacts — all through a menu driven by functions.

## Tasks

### Task 1: Add and View Contacts

1. Store contacts in a dictionary where the key is the contact's name and the value is a dictionary with: phone number, email, and category (Friend, Family, Work, Other).

2. Write an `add_contact()` function that asks for all four fields and adds the contact. If a contact with that name already exists, ask the user if they want to overwrite it.

3. Write a `view_all()` function that displays all contacts in a readable format. If no contacts exist, display a helpful message.

### Task 2: Search, Update, and Delete

1. Write a `search_contact(name)` function that finds a contact by name. Make it case-insensitive. If no exact match is found, show contacts whose names contain the search term.

2. Write an `update_contact(name)` function that lets the user change any one field for an existing contact (phone, email, or category).

3. Write a `delete_contact(name)` function that removes a contact after asking for confirmation.

### Task 3: The Menu

1. Build a main menu that calls the appropriate function for each option:
   ```
   ===== Contact Book =====
   1. Add Contact
   2. View All
   3. Search
   4. Update
   5. Delete
   6. Exit
   ========================
   ```

2. The menu loop should keep running until the user chooses Exit.

3. Each menu option should call exactly one function — no business logic inside the menu loop itself.

**Answer these questions after completing all tasks:**
- You use the contact's name as the dictionary key. What problem arises if the user saves "Rahul Sharma" and later searches for "rahul sharma"? How did you handle this?
- Your `update_contact()` lets the user change one field at a time. What happens if the user enters the name of a contact that does not exist? Test this and handle it if it crashes.
- Count how many lines are inside your main menu loop. If the answer is more than 10, what does that suggest about where your logic should live?

## Where to Build This Project

1. Go to [bytexl.app/nimbus](https://bytexl.app/nimbus).
2. Click **Create new workspace**.

![The Nimbus dashboard with the Create new workspace button highlighted](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/nimbus-python/01_create_new_workspace.png)

3. Select the **Python** template, then click **Next**.

![Select the Python template and click Next](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/nimbus-python/02_select_python_template.png)

4. Enter a workspace name and click **Launch Workspace**.

![Enter a workspace name and launch the Python workspace](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/nimbus-python/03_name_and_launch_workspace.png)
