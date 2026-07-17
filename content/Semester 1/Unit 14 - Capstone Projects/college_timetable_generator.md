# Capstone Project: College Timetable Generator

## Background

Scheduling classes at an engineering college is a logistical challenge — faculty have availability constraints, rooms have capacity limits, and no two classes for the same batch can run at the same time. TimeTable is a command-line timetable generator that assigns subjects, faculty, and rooms to time slots for a given semester, detects scheduling conflicts, and exports the final timetable to a CSV file.

This project draws on everything from Units 1 through 13: input validation, loops, lists and dictionaries, functions, file handling, basic OOP, and exception handling. You will build it in six stages.

## Stages

### Stage 1: Define the Schedule Structure

1. Ask the user to define the timetable parameters:
   - Number of working days per week (e.g. 5)
   - Time slots per day (e.g. 8:30-9:30, 9:30-10:30, 10:30-11:30, 11:30-12:30, 14:00-15:00, 15:00-16:00)
   - Batch name (e.g. CSE-A)

2. Generate and display an empty timetable grid:
   ```
   Batch: CSE-A
   +-----------+----------+----------+----------+----------+----------+
   | Slot      | Monday   | Tuesday  | Wednesday| Thursday | Friday   |
   +-----------+----------+----------+----------+----------+----------+
   | 8:30-9:30 | ---      | ---      | ---      | ---      | ---      |
   | 9:30-10:30| ---      | ---      | ---      | ---      | ---      |
   ...
   ```

3. Represent the timetable internally as a dictionary: keys are time slots, values are dictionaries mapping day → class entry (or None if free).

**Answer these questions after completing Stage 1:**
- You represent the timetable as a nested dictionary. What is the tradeoff versus a 2D list? When would a list be easier to work with?
- Your time slots are strings like "8:30-9:30". If you need to sort them or check if two slots overlap, what problem does the string format create?

### Stage 2: Add Subjects, Faculty, and Rooms

1. Build a menu:
   ```
   ========== TimeTable ==========
   1. Add Subject
   2. Add Faculty
   3. Add Room
   4. Assign Class
   5. View Timetable
   6. Exit
   ================================
   ```

2. Add Subject: name, code, hours per week required, subject type (Theory / Lab).

3. Add Faculty: name, faculty ID, subjects they can teach (list of subject codes), available days.

4. Add Room: room number, capacity, type (Classroom / Lab).

5. Store all three in separate dictionaries keyed by their unique identifier.

**Answer these questions after completing Stage 2:**
- A faculty member can teach multiple subjects and a subject can be taught by multiple faculty. What kind of relationship is this, and how did you represent it in your data structures?
- Lab subjects typically require double slots (2 consecutive hours). How will you handle this when assigning classes in Stage 3?

### Stage 3: Assign Classes and Detect Conflicts

1. Add an **Assign Class** option: the user selects a subject, faculty, room, day, and time slot. The system adds the entry to the timetable.

2. Before confirming the assignment, check all three conflict conditions:
   - The slot is not already occupied for this batch
   - The faculty member is not already teaching another class at the same slot
   - The room is not already booked at the same slot

3. If any conflict is detected, display which condition failed and reject the assignment.

4. Add a **View Conflicts** option that scans the entire timetable and reports any violations found.

**Answer these questions after completing Stage 3:**
- You check three conflict conditions. If all three fail simultaneously, your program reports one of them. Should it report all three? What would be more useful to the timetable coordinator?
- Faculty availability days were stored in Stage 2. Your conflict check verifies the slot is free — but does it also verify the faculty is available on that day? Test this case.

### Stage 4: Workload Tracking and Validation

1. Track each faculty member's assigned hours per week. After every assignment, update their hour count.

2. Enforce a maximum of 20 teaching hours per week per faculty. Reject assignments that would exceed this.

3. Track each subject's assigned hours against the required hours per week. Add a **Subject Coverage** report that shows how many hours of each subject have been scheduled versus required.

4. Add a **Faculty Workload** report showing each faculty member's current weekly hours and remaining capacity.

**Answer these questions after completing Stage 4:**
- A faculty member has 18 hours assigned and a 3-hour lab is being scheduled. Your limit is 20. Should you reject it, or allow it with a warning? What does your program do, and is that the right behaviour?
- Subject coverage shows hours scheduled versus required. What happens when a subject is over-scheduled — more hours assigned than required? Should this be an error or a warning?

### Stage 5: Redesign with Classes

1. Create a `Subject` class with attributes `name`, `code`, `hours_per_week`, `subject_type`.

2. Create a `Faculty` class with attributes `name`, `faculty_id`, `subjects`, `available_days`, `assigned_hours` and methods `can_teach(subject_code)`, `is_available(day)`, `add_hours(n)`, and `__str__`.

3. Create a `Room` class with attributes `room_number`, `capacity`, `room_type`.

4. Create a `Timetable` class that holds the schedule grid, a list of subjects, faculty, and rooms. Move all assignment, conflict checking, and reporting logic into `Timetable` methods.

**Answer these questions after completing Stage 5:**
- The conflict check for faculty availability now lives inside the `Timetable` class, but it needs to know whether a faculty member is free. Should this logic be in `Timetable.assign()` or in `Faculty.is_free(day, slot)`? Argue for one design.
- After the refactor, when you assign a class, how many objects are updated — the timetable grid, the faculty object, and anything else? List all state changes that happen in a single assignment.

### Stage 6: Export, Load, and Debug

1. Add an **Export to CSV** option: writes the full timetable grid to `timetable.csv` with days as columns and time slots as rows.

2. Save the full timetable state (subjects, faculty, rooms, assignments) to `timetable.json`. Load on startup.

3. Handle file errors and corrupted saves. If a saved timetable cannot be loaded, start fresh.

4. Add a custom exception `TimetableError` with subclasses `SlotConflictError` and `WorkloadExceededError`. Raise these in the appropriate assignment checks and catch them in the menu.

5. Find and fix the following three bugs:

**Bug 1:**
```python
def assign(self, slot, day, subject, faculty, room):
    self.grid[slot][day] = {
        "subject": subject.name,
        "faculty": faculty.name,
        "room": room.room_number
    }
    faculty.add_hours(1)
    # lab subjects require 2 hours but only 1 hour is added
```

**Bug 2:**
```python
def check_faculty_conflict(self, faculty_id, day, slot):
    for s, days in self.grid.items():
        if days[day] and days[day]["faculty"] == faculty_id:
            return True
    return False
    # checks all slots including the one being assigned
    # always returns True when the faculty has any class that day
```

**Bug 3:**
```python
def export_csv(self):
    with open("timetable.csv", "w") as f:
        for slot, days in self.grid.items():
            row = [slot] + [days[d] for d in self.days]
            f.write(",".join(row) + "\n")
    # days[d] is a dictionary, not a string
    # joining it will raise a TypeError
```

**Answer these questions after completing Stage 6:**
- Bug 2 is a logic error that makes the conflict checker always return True. What symptom would the timetable coordinator see — what would the program do when they tried to assign any class to a faculty member who already has one class?
- After exporting to CSV, open the file in Excel or a text editor. Does the timetable grid look correct? What formatting issues, if any, did you have to fix?

## The Complete Picture

When all six stages are complete, TimeTable:

- Generates a weekly timetable grid for a given batch
- Manages subjects, faculty, and room registries
- Detects and rejects slot, faculty, and room conflicts
- Tracks faculty workload and subject coverage
- Exports the timetable to a CSV file
- Persists all state across sessions in JSON
- Uses a clean four-class OOP design
- Has three realistic bugs identified and fixed
