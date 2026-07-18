## Introduction

Meenal is the senior developer at a campus event-booking startup, and it is her turn to review a `schema` her colleague drafted for a new Bookings feature that lets students reserve seats at college events. Her colleague is proud of the draft and slides it across expecting a quick approval.

Meenal reads it twice instead, slower the second time, marking it up with the instinct a proofreader brings to a manuscript: not looking for what is missing in the feature, but for the quiet structural mistakes that will not hurt anyone today and will absolutely hurt someone in six months.

What Meenal is doing has a name, a **`schema` design review**, reading a proposed `table` design closely enough to catch the small, common mistakes that are cheap to fix now and expensive to fix once real `rows` and real code depend on them.

The draft in front of her is a single `table` called `booking`, and by the time she finishes her second pass, she has found six separate problems in it, each one a mistake worth recognising on sight, because each one shows up again and again across real `schemas` built by developers in a hurry.

![Schema review checklist catching key, naming, money, timestamp, and duplicate-data problems before launch](images/11_schema_review_checklist.png)

**Definition:** A **schema design review** is a structured examination of tables, keys, relationships, constraints, data types, and naming choices to find integrity and maintainability problems before the schema is deployed.

## The Flawed Draft

Here is the `table` exactly as Meenal's colleague proposed it.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Column</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Type as drafted</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Problem Meenal spots</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">StudentName</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Text</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No primary key anywhere in the table</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">StudentEmail</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Text</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Repeats a student&#x27;s details on every booking they make</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">eventTitle</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Text</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Inconsistent casing against StudentName, StudentEmail</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">event_date</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Date</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Snake_case mixed with camelCase in the same table</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">ticketPrice</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Floating-point number</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Money stored in a type that can silently round incorrectly</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">seatNo</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Text</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No column recording when the booking was made or changed</td>
    </tr>
  </tbody>
</table>

Meenal starts listing the problems out loud, in the order she noticed them, because the order itself tells a story about how a `schema` tends to go wrong.

## Missing Primary Key

The very first thing Meenal checks, out of habit, is whether the `table` has any `column`, or combination of `columns`, guaranteed to be unique for every `row`. It does not.

Nothing stops two `rows` from ending up completely identical, and nothing gives any other part of the system a reliable way to say "this specific booking, and no other." Every `table` needs an identifying `column` that can never repeat and is never left empty, and the fix here is as simple as adding a dedicated `booking_id` that the `database` generates automatically for every new `row`.

## Inconsistent Naming

- The second problem is visible before Meenal even reads what the `columns` mean: `StudentName` and `StudentEmail` use one capitalization style, `eventTitle` and `ticketPrice` use another, and `event_date` uses a third.
- A `schema` like this forces every new developer to guess, `table` by `table` and sometimes `column` by `column`, which style applies where.
- A consistent style, snake_case throughout, chosen once and applied everywhere, removes that guesswork entirely.

## Money Stored as an Imprecise Floating Type

The third problem is the one Meenal flags most urgently, because it is the kind of mistake that looks completely fine in testing and only reveals itself once thousands of real `transactions` have run through it. `ticketPrice` is declared as a floating-point number, which stores decimal amounts as an approximation rather than an exact value.

Summed across enough bookings, tiny rounding errors compound into totals that do not match what a printed receipt or an accountant's ledger says they should. The fix is a fixed-precision decimal type instead, one that holds an exact number of digits after the decimal point with no approximation at all.

## No Audit Columns

The fourth problem only shows up when Meenal imagines a support call six months from now: a student disputes a booking, claiming they never made it, and support has no way to check when the `row` was created or whether it was recently changed by anyone, including by mistake.

Two quiet `columns`, `created_at` and `updated_at`, filled in automatically by the `database` itself, would answer that question in seconds instead of leaving it unanswerable.

## Redundant Data That Should Have Been Normalized

- The fifth problem is the largest one structurally.
- `StudentName` and `StudentEmail` are copied directly into every single booking `row`, which means the same student's name and email get retyped, verbatim, once for every event they book.
- The moment a student changes their email, every past booking still shows the old one unless every single `row` is found and updated by hand, and the moment two students happen to share a name, there is no way to be certain which one made which booking.
- The redundancy is a symptom of a design that never separated "facts about a student" from "facts about a specific booking." The fix is to split the `table` in two: a Students `table` holding each student's details exactly once, and a Bookings `table` that refers back to a student by a stable identifier rather than repeating their details on every `row`.

## The Wrong Kind of Primary Key for the Situation

The last problem Meenal raises is a question about the future rather than the present. The booking system will expose booking confirmations to students through a shareable link, and if `booking_id` is a simple auto-incrementing integer, a student could edit that link and quietly browse other students' bookings just by changing one digit.

Because this identifier is meant to be public-facing, an unguessable identifier, generated independently rather than counted upward from a shared starting point, is the safer choice, even though a plain integer would have been fine for a purely internal `table` nobody outside the company ever sees.

Here is the flawed draft as runnable DDL, exactly as Meenal's colleague first proposed it, followed by the corrected two-table design so the difference is visible in code, not just prose.

```postgresql file=flawed.sql
CREATE TABLE booking (
    StudentName TEXT,
    StudentEmail TEXT,
    eventTitle TEXT,
    event_date DATE,
    ticketPrice FLOAT,
    seatNo TEXT
);

INSERT INTO booking (StudentName, StudentEmail, eventTitle, event_date, ticketPrice, seatNo) VALUES
    ('Naina Fernandes', 'naina@college.edu', 'Tech Fest Finals', '2026-08-10', 299.50, 'A12'),
    ('Naina Fernandes', 'naina@college.edu', 'Cultural Night', '2026-08-15', 149.00, 'B04');
```

Running `SELECT * FROM booking;` against this table shows every one of Meenal's six problems at once: no `primary key` to tell the two rows apart reliably, `StudentName` and `StudentEmail` retyped verbatim on both rows, three different casing styles across the columns, and `ticketPrice` sitting in a type that can silently round.

The corrected design splits students from bookings and fixes every naming and type issue Meenal flagged:

```postgresql file=init.sql
CREATE TABLE students (
    student_id  INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    full_name   TEXT NOT NULL,
    email       TEXT NOT NULL UNIQUE
);

CREATE TABLE bookings (
    booking_id    INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    student_id    INTEGER NOT NULL REFERENCES students(student_id),
    event_title   TEXT NOT NULL,
    event_date    DATE NOT NULL,
    ticket_price  NUMERIC(10, 2) NOT NULL,
    seat_no       TEXT NOT NULL,
    created_at    TIMESTAMP NOT NULL DEFAULT now(),
    updated_at    TIMESTAMP NOT NULL DEFAULT now()
);

INSERT INTO students (full_name, email) VALUES
    ('Naina Fernandes', 'naina@college.edu');

INSERT INTO bookings (student_id, event_title, event_date, ticket_price, seat_no) VALUES
    (1, 'Tech Fest Finals', '2026-08-10', 299.50, 'A12'),
    (1, 'Cultural Night', '2026-08-15', 149.00, 'B04');
```

```postgresql with=init.sql
SELECT b.booking_id, s.full_name, b.event_title, b.ticket_price
FROM bookings b
JOIN students s ON b.student_id = s.student_id
ORDER BY b.booking_id;
```

Expected output:

| booking_id | full_name | event_title | ticket_price |
| -----------: | ---------------- | ----------------- | -------------: |
| 1 | Naina Fernandes | Tech Fest Finals | 299.50 |
| 2 | Naina Fernandes | Cultural Night | 149.00 |

Naina's name and email now exist exactly once, in `students`, no matter how many events she books, and `ticket_price` holds an exact `NUMERIC` value instead of a `FLOAT` that could quietly round.

## The Corrected Design

After Meenal's notes, the single flawed `table` becomes two well-formed ones.

![Corrected booking design splitting one crowded table into students and bookings linked by student_id](images/12_corrected_booking_schema_split.png)

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Table</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Column</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Type, in plain English</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">students</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">student_id</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unguessable public identifier</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Uniquely and safely identifies each student</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">students</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">full_name</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Variable-length text</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The student&#x27;s name, stored exactly once</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">students</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">email</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Variable-length text, unique</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The student&#x27;s contact email, stored exactly once</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">bookings</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">booking_id</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unguessable public identifier</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Uniquely and safely identifies each booking</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">bookings</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">student_id</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reference to students.student_id</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Points to the student who made the booking, nothing duplicated</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">bookings</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">event_title</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Variable-length text</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The name of the event booked</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">bookings</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">event_date</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Date</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">When the event takes place</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">bookings</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">ticket_price</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fixed-precision decimal</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The exact amount charged, immune to rounding drift</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">bookings</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">seat_no</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fixed-length text</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The assigned seat code</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">bookings</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">created_at / updated_at</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Date and time</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tracks when each booking was made or last changed</td>
    </tr>
  </tbody>
</table>

## Common Mistakes at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Mistake</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Why it hurts later</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Fix</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No primary key</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rows cannot be reliably told apart</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Add a dedicated, always-unique identifying column</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Inconsistent naming</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">New developers must guess the style per table</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pick one casing convention and apply it everywhere</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Money as a floating type</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Totals silently drift from rounding errors</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use a fixed-precision decimal type instead</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No audit columns</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Nobody can answer &quot;when was this created or changed&quot;</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Add created_at and updated_at</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Redundant, unnormalized data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The same fact must be updated in many places at once</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Split into separate tables linked by a stable reference</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Wrong primary key strategy</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A predictable public ID lets others guess neighbouring rows</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use an unguessable identifier for anything public-facing</td>
    </tr>
  </tbody>
</table>

## Your Turn: Run the Review

A colleague drafts a single `feedback` table with columns `RespondentName`, `RespondentEmail`, `courseTitle`, `rating` (declared FLOAT), and `comment`, with no primary key. Run Meenal's review against it: list the problems, in the order she would likely notice them.

A working answer: first, no primary key exists anywhere, so nothing guarantees two identical feedback rows can be told apart. Second, `RespondentName` mixes PascalCase with `courseTitle`'s camelCase, an inconsistent naming style. Third, `rating` stored as FLOAT risks the same silent rounding problem as `ticketPrice`, though ratings are usually small whole numbers so an INTEGER might be the honest fix here instead of NUMERIC. Fourth, there are no `created_at` or `updated_at` columns, so nobody can tell when feedback was submitted. Fifth, `RespondentName` and `RespondentEmail` would repeat on every piece of feedback the same respondent ever leaves, the same redundancy Meenal split into a separate Students table.

## Conclusion

None of the six mistakes Meenal found were exotic or hard to explain once named; each one was a small, ordinary shortcut that felt harmless while the `table` only existed on a whiteboard with three sample `rows` in it.

A `schema` review exists precisely to catch these shortcuts before real students, real bookings, and real money start depending on a design that quietly cannot be trusted to stay accurate or safe as it grows. Meenal's corrected Students and Bookings `tables` are not clever or unusual, they are simply careful, built from the same handful of habits:

Those habits are straightforward: choose a real `primary key`, use consistent names, store money exactly, preserve a visible history, avoid duplicated facts, and select an identifier that suits how it will actually be used.

With a design this solid finally in place, the last piece left is learning the language that actually reaches into these `tables` and pulls answers back out of them, which is where the real, hands-on work of asking a `database` questions begins.
