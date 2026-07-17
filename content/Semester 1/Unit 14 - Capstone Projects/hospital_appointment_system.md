# Capstone Project: Hospital Appointment System

## Background

Long queues and missed appointments are a daily frustration at Indian district hospitals and clinics. MediBook is a command-line appointment management system for a small clinic. It lets staff register patients, manage doctor availability, book and cancel appointments, and generate daily schedules.

This project draws on everything from Units 1 through 13: input validation, loops, lists and dictionaries, functions, file handling, basic OOP, and exception handling. You will build it in six stages, progressing from a single appointment entry to a fully persistent, class-based system.

## Stages

### Stage 1: Book a Single Appointment

1. Ask the staff to enter:
   - Patient name (text)
   - Patient age (integer)
   - Doctor name (text)
   - Appointment date (DD-MM-YYYY)
   - Appointment time slot (choose from: 09:00, 09:30, 10:00, 10:30, 11:00, 11:30, 14:00, 14:30, 15:00, 15:30)

2. Display a confirmation slip after booking:
   ```
   ----------------------------------------
   APPOINTMENT CONFIRMED
   ----------------------------------------
   Patient     : Priya Sharma
   Age         : 34
   Doctor      : Dr. Mehta
   Date        : 20-07-2025
   Time        : 10:00
   Token No.   : 1
   ----------------------------------------
   ```

3. Validate patient age — must be between 0 and 120. Validate time slot — must be from the predefined list.

4. Assign a token number sequentially starting from 1 for each session.

**Answer these questions after completing Stage 1:**
- Token numbers restart at 1 every time the program runs. What would a real clinic need instead, and how would you implement it?
- Your time slot validation uses a list of valid slots. What happens if the clinic adds a new time slot — how many places in your code need to change?

### Stage 2: Manage Multiple Appointments with a Menu

1. Build a main menu:
   ```
   ========== MediBook ==========
   1. Book Appointment
   2. View All Appointments
   3. View by Doctor
   4. View by Date
   5. Cancel Appointment
   6. Exit
   ==============================
   ```

2. Store appointments as a list of dictionaries. Each appointment should include: `token`, `patient_name`, `age`, `doctor`, `date`, `time_slot`, `status` (Confirmed / Cancelled).

3. Cancel Appointment: takes a token number, marks the appointment's status as Cancelled, and frees up the time slot.

4. View by Doctor and View by Date should filter accordingly and display only Confirmed appointments.

**Answer these questions after completing Stage 2:**
- When a slot is cancelled and freed up, can it be rebooked? Test this and fix if it does not work.
- What happens if two appointments are booked for the same doctor, same date, and same time slot? Add a check to prevent this.

### Stage 3: Doctor Management and Availability

1. Add a doctor registry — a dictionary mapping doctor names to their specialisation and available days (e.g. Mon, Wed, Fri).

2. When booking an appointment, validate that:
   - The doctor exists in the registry
   - The appointment date falls on one of the doctor's available days
   - The time slot is not already taken by another confirmed appointment for that doctor on that date

3. Add a **Check Availability** menu option: given a doctor name and date, display all free and booked time slots.

**Answer these questions after completing Stage 3:**
- You are now validating three conditions before booking. In what order do you check them? What order gives the best user experience — which check should fail first?
- A doctor's available days are stored as a list of day abbreviations ("Mon", "Wed"). Your date is a string in DD-MM-YYYY format. How do you determine what day of the week a given date falls on?

### Stage 4: Patient Records and Daily Schedule

1. Maintain a patient registry: each patient has a unique patient ID (auto-generated), name, age, and appointment history (list of token numbers).

2. Add a **Daily Schedule** report: given a date, display all confirmed appointments sorted by time slot, with patient name, age, and token number.

3. Add a **Patient History** option: given a patient ID, display all past and upcoming appointments.

4. Add a **Statistics** option: display total appointments booked today, total cancellations, and busiest doctor (most confirmed appointments).

**Answer these questions after completing Stage 4:**
- Your daily schedule is sorted by time slot. Sorting time slots as strings ("09:00", "10:00") works here — but when would alphabetical sorting of time strings fail? Give a specific example.
- Two patients can have the same name. How does your patient ID system handle this, and how does the staff distinguish between them?

### Stage 5: Redesign with Classes

1. Create a `Patient` class with attributes `patient_id`, `name`, `age`, `appointment_history` and a `__str__` method.

2. Create a `Doctor` class with attributes `name`, `specialisation`, `available_days`, `appointments` (dict mapping date → list of booked slots) and methods `is_available(date, slot)` and `book_slot(date, slot)`.

3. Create a `Clinic` class that holds a dictionary of doctors and patients. Move all booking, cancellation, and reporting logic into `Clinic` methods.

4. The main menu should only call `Clinic` methods.

**Answer these questions after completing Stage 5:**
- After the refactor, where does the "slot already booked" check live — in the `Clinic` class or the `Doctor` class? Which is the better location and why?
- A `Patient` holds a list of token numbers as appointment history. But tokens are managed by the `Clinic`. Is storing tokens in the `Patient` object the right design, or should `Patient` hold something else?

### Stage 6: Make It Persistent and Robust

1. Save doctors, patients, and appointments to JSON files on every change. Load all three on startup.

2. Handle missing files, corrupted JSON, and permission errors with specific messages.

3. Add a custom exception `BookingError` with subclasses `SlotUnavailableError` and `DoctorUnavailableError`. Raise and catch these appropriately.

4. Find and fix the following three bugs:

**Bug 1:**
```python
def cancel_appointment(self, token):
    for appt in self.appointments:
        if appt["token"] == token:
            appt["status"] = "Cancelled"
    # the slot is marked cancelled but never removed from
    # the doctor's booked slots — it cannot be rebooked
```

**Bug 2:**
```python
def view_by_date(self, date):
    return [a for a in self.appointments if a["date"] == date]
    # returns cancelled appointments too
```

**Bug 3:**
```python
def generate_daily_schedule(self, date):
    appts = self.view_by_date(date)
    return sorted(appts, key=lambda x: x["time_slot"])
    # time slots are strings — "14:00" sorts before "9:00"
    # because "1" < "9" alphabetically
```

**Answer these questions after completing Stage 6:**
- Bug 3 is a sorting bug that only appears when morning slots (9:00) and afternoon slots (14:00) exist on the same day. How would you write a test to catch this before it reaches users?
- After adding persistence, what happens to an appointment that was booked in session but the program crashed before saving? How would you reduce the risk of data loss?

## The Complete Picture

When all six stages are complete, MediBook:

- Books, cancels, and tracks appointments with slot conflict detection
- Maintains separate registries for doctors and patients
- Validates doctor availability by day and time slot
- Generates daily schedules sorted by time and patient history reports
- Persists all data across sessions in JSON files
- Uses a clean three-class OOP design
- Handles invalid input and file errors without crashing
- Has three realistic bugs identified and fixed
