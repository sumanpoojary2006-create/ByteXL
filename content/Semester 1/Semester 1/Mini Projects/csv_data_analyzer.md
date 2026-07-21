## Background

CSV files are one of the most common ways data is shared — spreadsheets, exported reports, and database dumps all use this format. Being able to read a CSV, explore its contents, filter records, and compute basic statistics is a fundamental skill for any Python developer. This project gives you hands-on practice with file handling and the `csv` module.

## What You Will Build

A CLI tool that loads a CSV file, lets the user explore its contents, filter records by column value, and view basic statistics.

## Dataset

Use the following CSV file for this project — create it manually and save it as `students.csv`:

```
name,branch,cgpa,backlogs,placed
Ananya,CSE,8.7,0,Yes
Rahul,ECE,7.2,1,No
Priya,MECH,6.8,2,No
Karan,CSE,9.1,0,Yes
Divya,IT,8.3,0,Yes
Siddharth,ECE,5.9,3,No
Meera,MECH,7.8,1,Yes
Arjun,CSE,8.0,0,Yes
Fatima,IT,9.4,0,Yes
Ravi,ECE,6.1,2,No
```

## Tasks

### Task 1: Load and Display

1. Read `students.csv` using the `csv` module and `DictReader`. Store all rows as a list of dictionaries.
2. Display all records in a readable format with column headers.
3. Display the total number of records loaded.
4. If the file does not exist, display a clear error message — do not let the program crash.

### Task 2: Filter Records

1. Build a menu:
   ```
   ===== CSV Analyzer =====
   1. View All Records
   2. Filter by Branch
   3. Filter by Placement
   4. View Statistics
   5. Exit
   ========================
   ```

2. Filter by Branch: ask the user for a branch name and display only matching records. Make the search case-insensitive.

3. Filter by Placement: ask the user for Yes or No and display matching records.

### Task 3: Basic Statistics

1. Compute and display:
   - Total number of students
   - Number placed and number not placed
   - Average CGPA across all students
   - Highest CGPA and the student's name
   - Lowest CGPA and the student's name
   - Number of students with zero backlogs

2. Display the stats in a clean format.

**Answer these questions after completing all tasks:**
- When you read CGPA from the CSV, it comes in as a string. At what point did you convert it to a float, and what happens if a row has a missing or invalid CGPA value?
- Your filter by branch is case-insensitive. Try filtering for "cse" — does it return the CSE students correctly? What did you add to make this work?
- Add one more student row directly to `students.csv` using a text editor. Rerun the program. Does it pick up the new row automatically without any code changes? Why?

## Where to Build This Project

1. Go to [bytexl.app/nimbus](https://bytexl.app/nimbus).
2. Click **Create new workspace**.

![The Nimbus dashboard with the Create new workspace button highlighted](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/nimbus-python/01_create_new_workspace.png)

3. Select the **Python** template, then click **Next**.

![Select the Python template and click Next](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/nimbus-python/02_select_python_template.png)

4. Enter a workspace name and click **Launch Workspace**.

![Enter a workspace name and launch the Python workspace](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/nimbus-python/03_name_and_launch_workspace.png)
