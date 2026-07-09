## Introduction

Meenal is the senior developer at a campus event-booking startup, and it is her turn to review a `schema` her colleague drafted for a new Bookings feature that lets students reserve seats at college events. Her colleague is proud of the draft and slides it across expecting a quick approval. Meenal reads it twice instead, slower the second time, marking it up with the instinct a proofreader brings to a manuscript: not looking for what is missing in the feature, but for the quiet structural mistakes that will not hurt anyone today and will absolutely hurt someone in six months. What Meenal is doing has a name, a **schema design review**, reading a proposed table design closely enough to catch the small, common mistakes that are cheap to fix now and expensive to fix once real rows and real code depend on them.

The draft in front of her is a single table called `booking`, and by the time she finishes her second pass, she has found six separate problems in it, each one a mistake worth recognising on sight, because each one shows up again and again across real `schemas` built by developers in a hurry.

## The Flawed Draft

Here is the table exactly as Meenal's colleague proposed it.

| Column | Type as drafted | Problem Meenal spots |
|---|---|---|
| StudentName | Text | No primary key anywhere in the table |
| StudentEmail | Text | Repeats a student's details on every booking they make |
| eventTitle | Text | Inconsistent casing against StudentName, StudentEmail |
| event_date | Date | Snake_case mixed with camelCase in the same table |
| ticketPrice | Floating-point number | Money stored in a type that can silently round incorrectly |
| seatNo | Text | No column recording when the booking was made or changed |

Meenal starts listing the problems out loud, in the order she noticed them, because the order itself tells a story about how a `schema` tends to go wrong.

## Missing Primary Key

The very first thing Meenal checks, out of habit, is whether the table has any column, or combination of columns, guaranteed to be unique for every row. It does not. Nothing stops two rows from ending up completely identical, and nothing gives any other part of the system a reliable way to say "this specific booking, and no other." Every table needs an identifying column that can never repeat and is never left empty, and the fix here is as simple as adding a dedicated `booking_id` that the database generates automatically for every new row.

## Inconsistent Naming

The second problem is visible before Meenal even reads what the columns mean: `StudentName` and `StudentEmail` use one capitalization style, `eventTitle` and `ticketPrice` use another, and `event_date` uses a third. A `schema` like this forces every new developer to guess, table by table and sometimes column by column, which style applies where. A consistent style, snake_case throughout, chosen once and applied everywhere, removes that guesswork entirely.

## Money Stored as an Imprecise Floating Type

The third problem is the one Meenal flags most urgently, because it is the kind of mistake that looks completely fine in testing and only reveals itself once thousands of real transactions have run through it. `ticketPrice` is declared as a floating-point number, which stores decimal amounts as an approximation rather than an exact value. Summed across enough bookings, tiny rounding errors compound into totals that do not match what a printed receipt or an accountant's ledger says they should. The fix is a fixed-precision decimal type instead, one that holds an exact number of digits after the decimal point with no approximation at all.

## No Audit Columns

The fourth problem only shows up when Meenal imagines a support call six months from now: a student disputes a booking, claiming they never made it, and support has no way to check when the row was created or whether it was recently changed by anyone, including by mistake. Two quiet columns, `created_at` and `updated_at`, filled in automatically by the database itself, would answer that question in seconds instead of leaving it unanswerable.

## Redundant Data That Should Have Been Normalized

The fifth problem is the largest one structurally. `StudentName` and `StudentEmail` are copied directly into every single booking row, which means the same student's name and email get retyped, verbatim, once for every event they book. The moment a student changes their email, every past booking still shows the old one unless every single row is found and updated by hand, and the moment two students happen to share a name, there is no way to be certain which one made which booking. The redundancy is a symptom of a design that never separated "facts about a student" from "facts about a specific booking." The fix is to split the table in two: a Students table holding each student's details exactly once, and a Bookings table that refers back to a student by a stable identifier rather than repeating their details on every row.

## The Wrong Kind of Primary Key for the Situation

The last problem Meenal raises is a question about the future rather than the present. The booking system will expose booking confirmations to students through a shareable link, and if `booking_id` is a simple auto-incrementing integer, a student could edit that link and quietly browse other students' bookings just by changing one digit. Because this identifier is meant to be public-facing, an unguessable identifier, generated independently rather than counted upward from a shared starting point, is the safer choice, even though a plain integer would have been fine for a purely internal table nobody outside the company ever sees.

## The Corrected Design

After Meenal's notes, the single flawed table becomes two well-formed ones.

| Table | Column | Type, in plain English | Purpose |
|---|---|---|---|
| students | student_id | Unguessable public identifier | Uniquely and safely identifies each student |
| students | full_name | Variable-length text | The student's name, stored exactly once |
| students | email | Variable-length text, unique | The student's contact email, stored exactly once |
| bookings | booking_id | Unguessable public identifier | Uniquely and safely identifies each booking |
| bookings | student_id | Reference to students.student_id | Points to the student who made the booking, nothing duplicated |
| bookings | event_title | Variable-length text | The name of the event booked |
| bookings | event_date | Date | When the event takes place |
| bookings | ticket_price | Fixed-precision decimal | The exact amount charged, immune to rounding drift |
| bookings | seat_no | Fixed-length text | The assigned seat code |
| bookings | created_at / updated_at | Date and time | Tracks when each booking was made or last changed |

## Common Mistakes at a Glance

| Mistake | Why it hurts later | Fix |
|---|---|---|
| No primary key | Rows cannot be reliably told apart | Add a dedicated, always-unique identifying column |
| Inconsistent naming | New developers must guess the style per table | Pick one casing convention and apply it everywhere |
| Money as a floating type | Totals silently drift from rounding errors | Use a fixed-precision decimal type instead |
| No audit columns | Nobody can answer "when was this created or changed" | Add created_at and updated_at |
| Redundant, unnormalized data | The same fact must be updated in many places at once | Split into separate tables linked by a stable reference |
| Wrong primary key strategy | A predictable public ID lets others guess neighbouring rows | Use an unguessable identifier for anything public-facing |

## Conclusion

None of the six mistakes Meenal found were exotic or hard to explain once named; each one was a small, ordinary shortcut that felt harmless while the table only existed on a whiteboard with three sample rows in it. A `schema` review exists precisely to catch these shortcuts before real students, real bookings, and real money start depending on a design that quietly cannot be trusted to stay accurate or safe as it grows. Meenal's corrected Students and Bookings tables are not clever or unusual, they are simply careful, built from the same handful of habits:

- A real `primary key`
- Consistent names
- Exact money
- A visible history
- No duplicated facts
- An identifier suited to how it will actually be used

With a design this solid finally in place, the last piece left is learning the language that actually reaches into these tables and pulls answers back out of them, which is where the real, hands-on work of asking a database questions begins.
