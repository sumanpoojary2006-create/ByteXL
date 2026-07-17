# Capstone Project: Bus Ticket Booking System

## Background

State road transport corporations like KSRTC and MSRTC run hundreds of bus routes daily, but many smaller private operators still manage bookings manually. BusPass is a command-line bus ticket booking system that manages routes, schedules seats, books and cancels tickets, and generates passenger manifests.

This project draws on everything from Units 1 through 13: input validation, loops, lists and dictionaries, functions, file handling, basic OOP, and exception handling. You will build it in six stages, starting with a single route and ending with a multi-route, file-backed booking system.

## Stages

### Stage 1: Define a Bus Route

1. Ask the operator to enter details for one bus:
   - Bus number (text, e.g. KA-01-F-1234)
   - Route: source city and destination city
   - Departure time (HH:MM format)
   - Total seats (integer, between 10 and 60)
   - Ticket price (float, in ₹)

2. Generate a seat map and display it:
   ```
   Bus: KA-01-F-1234 | Bengaluru → Mysuru | 06:30 | ₹ 180.00
   Seats (O = Available, X = Booked):
   [ O][ O][ O][ O][ O]
   [ O][ O][ O][ O][ O]
   [ O][ O][ O][ O][ O]
   [ O][ O][ O][ O][ O]
   [ O][ O][ O][ O][ O]
   ```

3. Represent the seat map internally as a list of seat states (True = available, False = booked).

**Answer these questions after completing Stage 1:**
- You store seats as a flat list. Seat 1 is index 0, seat 2 is index 1, and so on. When displaying a seat map in rows of 5, how do you determine which row a seat belongs to?
- Bus number "KA-01-F-1234" is a string. What validation would a real booking system need on this field that yours does not currently have?

### Stage 2: Manage Routes and Book Tickets

1. Build a main menu:
   ```
   ========== BusPass ==========
   1. Add Bus Route
   2. View All Routes
   3. Search Routes
   4. Book Ticket
   5. Cancel Ticket
   6. View Seat Map
   7. Exit
   =============================
   ```

2. Store all routes in a dictionary keyed by bus number.

3. Search Routes: takes source and destination (case-insensitive), returns all matching buses with available seat count and price.

4. Book Ticket: takes bus number and passenger details (name, age, gender, phone). Asks which seat number the passenger wants. Marks it as booked. Returns a ticket with a unique booking ID.

5. Display a ticket after booking:
   ```
   ============================================
   BOOKING CONFIRMED
   ============================================
   Booking ID  : BKG-0001
   Passenger   : Ananya Krishnan (F, 23)
   Bus         : KA-01-F-1234
   Route       : Bengaluru → Mysuru
   Departure   : 06:30
   Seat No.    : 12
   Fare        : ₹ 180.00
   ============================================
   ```

**Answer these questions after completing Stage 2:**
- Booking IDs are generated sequentially (BKG-0001, BKG-0002...). What happens to the sequence when the program restarts? Fix this in Stage 6 when you add file persistence.
- A passenger requests seat 12 but the bus only has 20 seats. Your program rejects it. What if they request seat 0 or a negative number — does your validation catch those?

### Stage 3: Cancellations and Refunds

1. Cancel Ticket: takes a booking ID, marks the seat as available again, and computes a refund based on this policy:
   - Full refund if cancelled more than 24 hours before departure (you may simulate this with a flag for now)
   - 50% refund if cancelled less than 24 hours before departure
   - No refund if the bus has already departed

2. Maintain a booking registry: a dictionary mapping booking ID → booking details.

3. Add a **My Bookings** option: takes a phone number and displays all bookings for that passenger.

4. Add a **Revenue Report** option: displays total revenue collected, total refunds issued, and net revenue per route.

**Answer these questions after completing Stage 3:**
- Your refund policy depends on time before departure. You are comparing strings (departure time) to the current time. What is the easiest way to implement this comparison, and what assumption does it make about the date of travel?
- A booking ID that does not exist is entered for cancellation. Test this case — does your program crash, display an error, or silently do nothing?

### Stage 4: Passenger Manifest and Route Analytics

1. Add a **Passenger Manifest** option: given a bus number, display a numbered list of all booked passengers with their seat number, name, age, gender, and phone — sorted by seat number.

2. Add a **Route Analytics** report showing:
   - Total seats, booked seats, available seats, and occupancy percentage for each route
   - The most popular route (highest occupancy percentage)
   - Average ticket price across all routes

3. Add a **Seat Preference** feature: passengers can specify a preference (Window / Aisle / No Preference). Display window and aisle seats differently in the seat map.

**Answer these questions after completing Stage 4:**
- Seat preference is a preference, not a guarantee. If no window seats are available, should your program assign the next best option automatically or ask the passenger? What does your program do?
- The most popular route is determined by occupancy percentage. If two routes have the same percentage, how does your program break the tie?

### Stage 5: Redesign with Classes

1. Create a `Seat` class with attributes `seat_number`, `is_booked`, `seat_type` (Window / Aisle / Middle) and methods `book()`, `release()`, and `__str__`.

2. Create a `Booking` class with attributes `booking_id`, `passenger_name`, `age`, `gender`, `phone`, `bus_number`, `seat_number`, `fare`, `status` (Confirmed / Cancelled) and `__str__`.

3. Create a `Bus` class with attributes `bus_number`, `source`, `destination`, `departure_time`, `price`, `seats` (list of `Seat` objects), `bookings` (dict of booking ID → `Booking`) and methods `book_seat(seat_num, passenger_details)`, `cancel_booking(booking_id)`, `available_seats()`, `display_seat_map()`.

4. Create a `BusSystem` class that holds a dictionary of buses. Move search, manifest, and analytics into `BusSystem` methods.

**Answer these questions after completing Stage 5:**
- After the refactor, `Bus.book_seat()` needs to create a `Booking` object and a booking ID. Should the `Bus` generate the booking ID, or should `BusSystem` generate it? Which has the information needed to ensure uniqueness across all buses?
- `Seat.book()` changes `is_booked` to True. What should it do if called on a seat that is already booked — silently succeed, return False, or raise an exception?

### Stage 6: Make It Persistent and Robust

1. Save all buses and bookings to `buses.json` and `bookings.json`. Load on startup and restore the last booking ID counter so sequence continues correctly.

2. Handle file errors, missing files, and corrupted JSON.

3. Add a custom exception `BookingError` with subclasses `SeatUnavailableError` and `InvalidBookingError`. Raise and catch these in the appropriate places.

4. Find and fix the following three bugs:

**Bug 1:**
```python
def display_seat_map(self):
    for i, seat in enumerate(self.seats):
        print(f"[{'X' if seat.is_booked else 'O':>2}]", end="")
        if (i + 1) % 5 == 0:
            print()
    # no newline at the end if total seats is not a multiple of 5
```

**Bug 2:**
```python
def cancel_booking(self, booking_id):
    booking = self.bookings[booking_id]
    booking.status = "Cancelled"
    self.seats[booking.seat_number].release()
    # seat_number is 1-indexed (seat 1 = index 0)
    # self.seats[booking.seat_number] accesses the wrong seat
```

**Bug 3:**
```python
def search_routes(self, source, destination):
    return [b for b in self.buses.values()
            if b.source == source and b.destination == destination]
    # case-sensitive — "bengaluru" misses "Bengaluru"
```

**Answer these questions after completing Stage 6:**
- Bug 2 is an off-by-one error. This is one of the most common bugs in programming. What practice — in naming, commenting, or testing — would have caught this before it reached users?
- After adding file persistence, test this scenario: book a ticket, close the program, reopen it, and cancel that booking. Does everything work correctly? What had to be restored from the file for this to succeed?

## The Complete Picture

When all six stages are complete, BusPass:

- Manages bus routes with seat maps and pricing
- Books tickets with seat selection and generates booking IDs
- Processes cancellations with a time-based refund policy
- Generates passenger manifests and route analytics
- Persists all bookings and routes across sessions
- Uses a clean four-class OOP design
- Handles bad input and file errors without crashing
- Has three realistic bugs identified and fixed
