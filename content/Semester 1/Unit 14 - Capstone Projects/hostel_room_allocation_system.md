# Capstone Project: Hostel Room Allocation System

## Background

Engineering college hostels in India allocate rooms manually at the start of every semester — a process that leads to errors, double allocations, and long queues. HostelHub is a command-line room allocation system that manages room inventory, allocates rooms to students, handles waitlists, tracks fee payments, and generates occupancy reports.

This project draws on everything from Units 1 through 13: input validation, loops, lists and dictionaries, functions, file handling, basic OOP, and exception handling. You will build it in six stages.

## Stages

### Stage 1: Set Up the Room Inventory

1. Ask the warden to enter details for one room:
   - Room number (text, e.g. A101)
   - Block (A / B / C)
   - Floor (integer)
   - Room type (Single / Double / Triple)
   - Monthly fee (float, in ₹)

2. Display a room card after adding:
   ```
   ----------------------------------------
   ROOM ADDED
   ----------------------------------------
   Room No.    : A101
   Block       : A
   Floor       : 1
   Type        : Double
   Capacity    : 2
   Status      : Vacant
   Monthly Fee : ₹ 4,500.00
   ----------------------------------------
   ```

3. Derive capacity automatically from room type: Single = 1, Double = 2, Triple = 3.

4. Validate floor is between 0 and 5. Validate room number is not already in use.

**Answer these questions after completing Stage 1:**
- Capacity is derived from room type. What happens if the warden enters a room type not in your predefined list — does capacity become None, 0, or does the program crash?
- Room numbers like "A101" encode information (block A, floor 1, room 01). Should your program parse this automatically instead of asking for block and floor separately? What are the tradeoffs?

### Stage 2: Manage Rooms and Students with a Menu

1. Build a main menu:
   ```
   ========== HostelHub ==========
   1. Add Room
   2. Add Student
   3. View All Rooms
   4. View Room Details
   5. Allocate Room
   6. Exit
   ================================
   ```

2. Add Student: name, student ID, gender, branch, year of study, contact number.

3. View All Rooms: display all rooms with current occupancy (e.g. "2/2 occupied") and status (Vacant / Partial / Full).

4. Status is derived dynamically — do not store it separately. A room is Vacant if 0 occupants, Full if at capacity, Partial otherwise.

**Answer these questions after completing Stage 2:**
- Status is computed dynamically each time. What is the benefit of this versus storing status as a field and updating it manually?
- Two students of different genders are assigned to a double room. Should your system allow this? Add a same-gender constraint if it does not exist.

### Stage 3: Room Allocation and Waitlist

1. Add an **Allocate Room** option: takes student ID and room number. Assigns the student to the room if capacity allows, records the allocation with the date.

2. If the requested room is full, offer to add the student to a room-specific waitlist. Waitlist is a queue — first in, first out.

3. When a room vacancy opens (due to a vacating student), automatically allocate it to the next student on the waitlist. Display a notification.

4. Add a **View Waitlist** option: shows the waitlist for each room in order.

**Answer these questions after completing Stage 3:**
- Your waitlist is room-specific. A student on the waitlist for room A101 will not be offered room A102 when it becomes available. Is this the right design for a real hostel, and how would you change it if not?
- When a room vacancy opens and a waitlisted student is auto-allocated, should the program ask for confirmation or allocate automatically? What are the implications of each approach?

### Stage 4: Vacating, Fee Tracking, and Reports

1. Add a **Vacate Room** option: removes a student from their room, records the vacating date, and triggers waitlist processing.

2. Add fee tracking: each allocation has an associated fee based on the room's monthly fee. Track fee status (Paid / Pending) for each student.

3. Add a **Mark Fee Paid** option: updates a student's fee status for the current month.

4. Add these reports to the menu:
   - **Occupancy Report**: total rooms, total occupied, total vacant, percentage occupancy per block
   - **Pending Fees Report**: list all students with Pending fee status with their room number and amount due

**Answer these questions after completing Stage 4:**
- Fee status is stored per allocation, not per month. If a student stays for six months, how does your system track whether they paid for each month? Is one `Paid / Pending` field sufficient?
- The occupancy percentage is computed at report time. If you run the report twice in the same session, will it always give the same result? What could cause it to differ?

### Stage 5: Redesign with Classes

1. Create a `Room` class with attributes `room_number`, `block`, `floor`, `room_type`, `capacity`, `monthly_fee`, `occupants` (list of student IDs), `waitlist` (list of student IDs) and methods `is_full()`, `is_vacant()`, `allocate(student_id)`, `vacate(student_id)`, `status()`.

2. Create a `Student` class with attributes `student_id`, `name`, `gender`, `branch`, `year`, `contact`, `room_number` (None if not allocated) and method `__str__`.

3. Create a `Hostel` class that holds dictionaries of rooms and students. Move all allocation, vacating, fee tracking, and reporting logic into `Hostel` methods.

**Answer these questions after completing Stage 5:**
- `Room.waitlist` is a list used as a queue (FIFO). Python lists support this with `append()` and `pop(0)`, but `pop(0)` is O(n). For a 500-room hostel, does this matter? What alternative data structure would be more efficient?
- After the refactor, when a student is allocated to a room, how many objects change state? List all of them and confirm your code updates all of them.

### Stage 6: Make It Persistent and Robust

1. Save rooms, students, and fee records to JSON files. Load on startup.

2. Handle file errors, missing files, and corrupted JSON. Back up corrupted files before starting fresh.

3. Add a custom exception `AllocationError` with subclasses `RoomFullError` and `StudentAlreadyAllocatedError`. Raise these in the appropriate methods.

4. Find and fix the following three bugs:

**Bug 1:**
```python
def allocate(self, student_id):
    if not self.is_full():
        self.occupants.append(student_id)
    # does not check if the student is already in this room
    # calling allocate() twice adds the student twice
```

**Bug 2:**
```python
def vacate(self, student_id):
    self.occupants.remove(student_id)
    # if student_id is not in occupants, raises ValueError
    # program crashes with no useful error message
```

**Bug 3:**
```python
def occupancy_report(self):
    for block in ["A", "B", "C"]:
        rooms = [r for r in self.rooms.values() if r.block == block]
        occupied = len([r for r in rooms if not r.is_vacant()])
        print(f"{block}: {occupied}/{len(rooms)} ({occupied/len(rooms)*100:.1f}%)")
    # division by zero if a block has no rooms
```

**Answer these questions after completing Stage 6:**
- Bug 1 means a student can be added to a room's occupant list twice. What would the occupancy count show for that room, and what would happen when the student tries to vacate?
- Bug 3 crashes on division by zero only when a block has no rooms. Is this a case your program needs to handle, or is it an impossible state if the rest of your code is correct?

## The Complete Picture

When all six stages are complete, HostelHub:

- Manages a room inventory with capacity and block tracking
- Allocates rooms to students with gender constraint enforcement
- Handles waitlists with automatic FIFO allocation on vacancy
- Tracks fee payment status per student per room
- Generates occupancy and pending fee reports
- Persists all data across sessions in JSON files
- Uses a clean three-class OOP design
- Has three realistic bugs identified and fixed
