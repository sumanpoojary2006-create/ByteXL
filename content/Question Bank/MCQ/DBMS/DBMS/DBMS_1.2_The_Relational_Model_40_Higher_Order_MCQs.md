# DBMS 1.2: The Relational Model — 40 Higher-Order MCQs

## Assessment specifications

- **Subject:** DBMS
- **Topic:** Database Foundations
- **Chapter:** The Relational Model
- **Scope:** All seven Topic 1.2 subtopics in the attached course blueprint
- **Format:** Four options with exactly one best answer
- **Curriculum flag:** No
- **Design standard:** Every question explicitly establishes the database, what each table represents, what unfamiliar fields mean, and the business event being evaluated. Students analyse shown rows, schemas, rules, or before-and-after states rather than isolated terminology.
- **Table-use standard:** Evidence tables are used wherever students need to trace records, compare candidate identifiers, validate domains, follow references, or predict dependent-row outcomes.
- **Scope guard:** Constraints and delete/update policies remain in plain language. SQL syntax and later chapters are intentionally excluded.
- **Difficulty policy:** Difficulty reflects the reasoning genuinely required by each question; no fixed quota is imposed.
- **Answer-quality controls:** A/B/C/D each correct exactly 10 times, no letter correct more than twice consecutively, no correct answer identifiable by length.
- **Coverage rule:** Questions 1–10 collectively cover all seven Topic 1.2 subtopics.
- **Student/instructor separation:** Questions appear first; answers and explanations follow in the instructor key.

---

## Questions

### 1. The row that came out sideways

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Tables, Rows, and Columns  
**Is Curriculum Based:** No  
**Assessment type:** Structure-violation identification

A dive shop is designing an `Equipment` database table with one row per rentable item. Here, `item` means the equipment name, `size` means its size label, and `daily_rate` means its rental price in rupees per day:

| item | size | daily_rate |
|---|---|---|
| Wetsuit | M | 400 |
| Fins | L | 150 |
| 250 | Snorkel | S |

Which relational principle does the third row break?

A. Tables may never contain more than two rows of equipment total.  
B. Numeric values may never appear in a table alongside text.  
C. Every table needs at least four separate columns to be considered fully valid.  
D. Every row follows the same structure, values under their own attributes.

### 2. Two values the rating column must refuse

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Attributes and Domains  
**Is Curriculum Based:** No  
**Assessment type:** Domain-enforcement prediction

A homestay platform stores one database row per guest review. Its `star_rating` field means the guest's whole-star score and has the domain 1, 2, 3, 4, or 5.

| Attempted review | Value entered in `star_rating` |
|---|---|
| Review R81 | `4.5` |
| Review R82 | `"five"` |

What does the domain definition imply about these two attempts?

A. Both are accepted, because both clearly express a rating.  
B. Both are illegal: one breaks the whole-number rule, the other isn't a number.  
C. `4.5` is accepted because it lies between 1 and 5; only `"five"` gets rejected here.  
D. `"five"` is accepted because domains govern only numeric precision.

### 3. Two cats named Simba

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Primary Keys  
**Is Curriculum Based:** No  
**Assessment type:** Problem-to-mechanism mapping

A veterinary clinic's `Pets` database table stores one row per animal. `pet_name` is the animal's name, `owner` identifies its owner, and `species` records the animal type:

| pet_name | owner | species |
|---|---|---|
| Simba | R. Iyer | Cat |
| Simba | K. Rao | Dog |

The vaccination system must refer to exactly one animal, every time, without ambiguity. What does the table need?

A. A primary key, such as `pet_id`, holding a distinct value for every row.  
B. A rule forbidding two pets from sharing a name.  
C. A second table listing the names in alphabetical order.  
D. An office agreement that staff always mention the species when speaking aloud.

### 4. The dish that names a missing chef

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Foreign Keys  
**Is Curriculum Based:** No  
**Assessment type:** Referential-integrity prediction

A restaurant database has a `Chefs` table with one row per chef and a `Dishes` table with one row per menu item. In both tables, `chef_id` is the numeric identifier used to connect a dish to its responsible chef.

`chefs`

| chef_id | name |
|---|---|
| 1 | Tanvi |
| 2 | Marco |
| 3 | Ibrahim |

Someone attempts to insert the dish `('Ramen', chef_id = 7)`.

What happens?

A. The dish is stored, and chef 7 is created automatically as a blank row.  
B. The dish is stored with chef_id 7 left as a note for later.  
C. The insert is rejected, since no chef 7 exists to point to.  
D. The insert succeeds but chef 3 is assigned, being the closest existing number.

### 5. Unique only as a trio

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Candidate, Composite, and Surrogate Keys  
**Is Curriculum Based:** No  
**Assessment type:** Key classification

An airline's `BoardingPasses` table stores one row per issued pass:

| Field | Meaning | Can it repeat alone? |
|---|---|---|
| `flight_no` | Scheduled flight code | Yes, on different dates |
| `seat_no` | Seat printed on the pass | Yes, on different flights |
| `travel_date` | Date of travel | Yes, across many passengers |

The airline's business rule guarantees that the combination (`flight_no`, `seat_no`, `travel_date`) never repeats—not merely that it happens to be unique in today's rows.

What kind of key is that combination?

A. A surrogate key, since three separate brand-new columns were invented just for it.  
B. A composite key: columns that only identify a row together.  
C. A foreign key, because it refers to three other tables.  
D. A domain, because it restricts three columns at once.

### 6. When the playlist goes, what follows it?

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** ON DELETE and ON UPDATE  
**Is Curriculum Based:** No  
**Assessment type:** Policy selection

A music database contains:

| Table | What one row represents | Connecting field |
|---|---|---|
| `Playlists` | One named playlist | `playlist_id`, the playlist's identifier |
| `PlaylistSongs` | One song's membership in one playlist | `playlist_id`, pointing to `Playlists` |

When a user deletes a playlist, its membership rows are meaningless leftovers and must not survive.

Which delete policy on the reference expresses this?

A. Block the playlist deletion whenever any entries exist.  
B. Keep the entries but clear their playlist reference to empty.  
C. Keep the entries pointing at the deleted playlist for history.  
D. Automatically delete the entries along with their playlist.

### 7. Three shop rules, three rule shapes

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Database Constraints  
**Is Curriculum Based:** No  
**Assessment type:** Rule-shape matching

An online eyewear database documents three fields:

| Table and field | Field meaning | Required rule |
|---|---|---|
| `Orders.delivery_address` | Where the order must be delivered | Must be recorded |
| `Accounts.login_email` | Address used to sign into one account | Must not repeat |
| `Orders.discount_pct` | Percentage removed from the price | Must remain from 0 to 90 |

Which matching of rule to constraint shape is correct?

A. 1: a value-must-be-present rule; 2: a no-duplicates rule; 3: a value-range rule.  
B. 1: a no-duplicates rule; 2: a value-range rule; 3: a value-must-be-present rule.  
C. 1: a value-range rule; 2: a value-must-be-present rule; 3: a strict no-duplicates rule.  
D. All three are the same rule shape, since all three reject bad data.

### 8. Find the connecting columns

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Foreign Keys  
**Is Curriculum Based:** No  
**Assessment type:** Schema reading

A racquet club database uses:

| Table | What one row represents | Identifier |
|---|---|---|
| `courts(court_id, surface)` | One playable court | `court_id` |
| `members(member_id, name)` | One club member | `member_id` |
| `bookings(booking_id, court_id, member_id, start_time)` | One member reserving one court | `booking_id` |

Inside `bookings`, the repeated `court_id` and `member_id` values connect each reservation to the court and member involved.

Which columns in `bookings` are foreign keys?

A. `booking_id` and `start_time`  
B. Only `booking_id`  
C. `court_id` and `member_id`, each one referencing another table's primary key  
D. `start_time` alone, since booking start times frequently repeat across many different rows

### 9. The phone number that seemed like a fine identifier

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Primary Keys  
**Is Curriculum Based:** No  
**Assessment type:** Design-critique selection

A salon database stores one row per client. Its `phone_number` field means the client's current contact number, while a primary key must preserve the row's identity throughout the client's lifetime. Management proposes using `phone_number` as that key because every current client has one.

Which critique identifies the deepest problem?

A. Phone numbers change hands, so they cannot promise a permanent identity.  
B. Phone numbers contain far too many digits to store efficiently in a key column.  
C. Primary keys are only allowed to be words, never digits.  
D. Clients might refuse to be listed in a table at all.

### 10. An identity invented on purpose

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Candidate, Composite, and Surrogate Keys  
**Is Curriculum Based:** No  
**Assessment type:** Design-rationale selection

A physiotherapy database stores one row per appointment:

| Field | Meaning |
|---|---|
| `visit_id` | Database-generated number with no business meaning |
| `patient` | Person receiving treatment |
| `therapist` | Professional delivering treatment |
| `datetime` | Scheduled appointment moment |

Although (`patient`, `therapist`, `datetime`) is already unique, the practice assigns `visit_id` values 1, 2, 3, and so on.

What is the main argument for the invented column?

A. It stores the visit's date in a more compact format than an ordinary date column.  
B. It lets two visits share the same patient, therapist, and time.  
C. It removes the need for any other columns in the table.  
D. A surrogate gives each row a stable identity nothing real-world can break.

### 11. What one row stands for

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Tables, Rows, and Columns  
**Is Curriculum Based:** No  
**Assessment type:** Concept-instance mapping

A mining company's shift log:

| shift_id | crew | pit |
|---|---|---|
| 1 | Alpha | North |
| 2 | Delta | North |
| 3 | Alpha | East |

In relational terms, what does row 2 represent?

A. The formal definition of what a shift is allowed to contain.  
B. The set of all shifts worked by crew Delta.  
C. One complete instance of what the table records here.  
D. A column that happens to be printed horizontally.

### 12. The keys that were not chosen

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Candidate, Composite, and Surrogate Keys  
**Is Curriculum Based:** No  
**Assessment type:** Key-vocabulary application

A cinema database stores one row per screening hall:

| Field | Meaning | Repeats? |
|---|---|---|
| `screen_id` | Internal identifier for the hall | Never |
| `hall_name` | Public name printed on tickets | Never |
| `projector_serial` | Serial number of the installed projector | Never |

The team designates `screen_id` as the primary key.

What are `hall_name` and `projector_serial` properly called?

A. Candidate keys, since they could have served as the primary key.  
B. Foreign keys, because they were rejected.  
C. Composite keys, simply because there happen to be two of them here.  
D. Domains, because they restrict the table.

### 13. The two promises

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Primary Keys  
**Is Curriculum Based:** No  
**Assessment type:** Guarantee identification

A courier database stores one row per physical parcel. The field `parcel_id` is the tracking identifier printed on that parcel's label, and the firm declares it the primary key of the `Parcels` table.

Which pair of guarantees does that declaration make?

A. Every parcel is delivered on time, and none is lost.  
B. No two rows share a `parcel_id`, and no row may leave it empty.  
C. The table is sorted by `parcel_id`, and rows load faster.  
D. `parcel_id` values are kept secret, and only admins may ever read them.

### 14. Renaming a bin without breaking a warehouse

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** ON DELETE and ON UPDATE  
**Is Curriculum Based:** No  
**Assessment type:** Update-policy selection

A fulfilment database contains:

| Table | What one row represents | Relevant field |
|---|---|---|
| `Bins` | One physical storage bin | `bin_code`, the bin's identifier |
| `Stock` | One stored product quantity | `bin_code`, pointing to its location |

The centre renames bin `B-14` to `C-02`. Hundreds of stock rows must follow automatically, with no orphaned references or manual edits.

Which update policy on the reference achieves this?

A. Block any rename while stock rows reference the bin.  
B. Clear the bin reference on all stock rows to empty.  
C. Leave stock rows holding the old `B-14` code and trust staff to fix them.  
D. Propagate the new code to every referencing stock row automatically.

### 15. "We'll define the rules after launch"

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Attributes and Domains  
**Is Curriculum Based:** No  
**Assessment type:** Timing-consequence reasoning

An EV-charging database stores one row per charging port. Its `power_kw` field means the port's supported charging power in kilowatts.

| Design decision | Launch state |
|---|---|
| Legal type and range for `power_kw` | Not defined |
| Data entry | Real port records accepted immediately |
| Proposed plan | “Tighten the rules later” |

What is the strongest objection?

A. Rules defined later run more slowly than rules defined early.  
B. The table cannot physically store numbers until a domain exists.  
C. Every bad value accepted meanwhile becomes data someone must later clean up.  
D. Regulators require every domain to be formally filed before company registration.

### 16. One locker, one member

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Database Constraints  
**Is Curriculum Based:** No  
**Assessment type:** Rule-shape identification

A climbing gym database stores one row per member. `locker_no` means the one physical locker assigned to that member.

| member_id | member_name | locker_no |
|---:|---|---:|
| 81 | Tara | 14 |
| 82 | Yusuf | 27 |

The gym's rule is: “No two member rows may contain the same `locker_no`.”

Which constraint shape expresses this?

A. A value-must-be-present rule on the locker column.  
B. A no-duplicates rule on the locker column.  
C. A value-range rule keeping locker numbers below 500.  
D. A cross-table reference rule pointing at the members table.

### 17. Which table carries the pointer?

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Foreign Keys  
**Is Curriculum Based:** No  
**Assessment type:** Reference-direction reasoning

A tailoring database models:

| Table | What one row represents | Identifier |
|---|---|---|
| `Customers` | One customer | `customer_id` |
| `Fittings` | One fitting appointment | `fitting_id` |

One customer can attend many fittings. A junior designer proposes storing all fitting IDs together in one `Customers` cell.

Which correction reflects relational design?

A. Reverse it: each fitting carries one `customer_id` referencing its customer.  
B. The designer is entirely right; parent rows should enumerate all their children.  
C. Both tables should list each other's IDs for symmetry.  
D. Neither table needs references if both are backed up nightly.

### 18. The client who cannot be deleted yet

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** ON DELETE and ON UPDATE  
**Is Curriculum Based:** No  
**Assessment type:** Policy identification

A brokerage database contains:

| Table | What one row represents | Connection |
|---|---|---|
| `Clients` | One brokerage client | `client_id`, the parent identifier |
| `Accounts` | One investment account | `client_id`, pointing to its owner |

Compliance requires a client deletion to fail while any account row still references that client.

Which delete policy implements the rule?

A. Automatically delete the client's accounts first.  
B. Clear each account's client reference to empty.  
C. Allow the delete and let the accounts point at the missing client.  
D. Block the delete outright whenever referencing accounts exist.

### 19. Three writers, one gatekeeper

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Database Constraints  
**Is Curriculum Based:** No  
**Assessment type:** Enforcement-location judgment

A logistics database stores one row per shipment, where `weight_kg` means the shipment's weight in kilograms.

| Data-entry route | Checks that `weight_kg > 0`? |
|---|---|
| Mobile app | Yes |
| Partner API | No |
| Nightly CSV import | No |

Negative weights keep appearing in reports.

Why does the fix belong in the database rather than in more application code?

A. Databases execute validation code faster than applications can.  
B. A database constraint applies to every write path, not just the ones that remember to check.  
C. Application-side validation is essentially impossible to write correctly for numeric columns.  
D. Moving the check reduces the licence cost of the mobile app.

### 20. What a column promises about every row

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Tables, Rows, and Columns  
**Is Curriculum Based:** No  
**Assessment type:** Concept discrimination

A ferry database stores one row per scheduled sailing:

| Field | Meaning |
|---|---|
| `sailing_id` | Identifier of the scheduled trip |
| `route` | Origin-to-destination path |
| `departure_time` | Planned starting time |
| `vessel` | Ferry assigned to operate the trip |

Which statement about the `vessel` column is correct?

A. It applies only to the rows entered after the column was added.  
B. It may hold a vessel name in some rows and a full departure time in others.  
C. It defines one attribute that every row records the same kind of value for.  
D. It is a row that has been rotated for display.

### 21. The second ticket 501

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Primary Keys  
**Is Curriculum Based:** No  
**Assessment type:** Enforcement prediction

A helpdesk database stores one row per support request. `ticket_id` is the number used to identify one request and is the table's primary key.

| Event | `ticket_id` | Request summary |
|---|---:|---|
| Existing row | 501 | Password reset |
| Batch-import attempt | 501 | Missing invoice |

What happens?

A. The database refuses the insert; uniqueness is enforced, not advisory.  
B. Both rows are somehow kept, distinguished only by their insertion time.  
C. The new row silently replaces the old one.  
D. The database renumbers the new row to 502 automatically.

### 22. Choose the parcel table's identifier

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Primary Keys  
**Is Curriculum Based:** No  
**Assessment type:** Best-candidate selection

A parcel-locker startup must pick a primary key for its `parcels` table from these columns:

| Column | Observation |
|---|---|
| recipient_name | Many recipients share names |
| weight_grams | Many parcels weigh the same |
| drop_off_date | Hundreds of parcels per day |
| parcel_id | Generated uniquely for each parcel |

Which column qualifies?

A. `recipient_name`  
B. `weight_grams`  
C. `drop_off_date`  
D. `parcel_id`

### 23. Rows that point at nobody

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Foreign Keys  
**Is Curriculum Based:** No  
**Assessment type:** Failure-mode identification

An orchestra database uses:

| Table | What one row represents | Relevant field |
|---|---|---|
| `Musicians` | One orchestra member | `musician_id`, the member's identifier |
| `InstrumentLoans` | One instrument issued to a member | `musician_id`, intended to point to `Musicians` |

No foreign-key rule was enforced. Musician 44 is deleted while three loan rows still contain `musician_id = 44`.

What is the resulting condition called, and why is it harmful?

A. A composite key: the loans now identify each other.  
B. Orphaned references: the loans point at a row that no longer exists.  
C. A surrogate key: the deleted row survives in spirit.  
D. A domain violation, since the loans now hold values of the wrong data type.

### 24. Two columns named "size"

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Attributes and Domains  
**Is Curriculum Based:** No  
**Assessment type:** Attribute-versus-label discrimination

A sportswear database uses two separate tables:

| Attribute | What it describes | Legal values |
|---|---|---|
| `Shoes.size` | Footwear size | Numbers such as 42 and 43 |
| `Jerseys.size` | Garment size | S, M, L, or XL |

What does this show about attributes?

A. Because both columns use the name `size`, the relational model requires them to accept exactly the same legal values.  
B. Column names must be globally unique across a database.  
C. Sharing a column name does not make two attributes equivalent; each can have its own domain.  
D. Text domains are always preferable to numeric domains.

### 25. Two references, two different fates

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** ON DELETE and ON UPDATE  
**Is Curriculum Based:** No  
**Assessment type:** Per-relationship policy design

An invoicing database models:

| Table | What one row represents | Relevant references |
|---|---|---|
| `Invoices` | One customer bill | Identified by `invoice_id` |
| `InvoiceLines` | One product charged on one bill | Points to both `invoice_id` and `product_id` |
| `Products` | One sellable catalogue item | Identified by `product_id` |

Here, `product_id` means the stable identifier of a product—not its name or price. Deleting an invoice must remove its lines, but a product must not be deletable while any line still refers to it.

Which policy assignment is correct?

A. Block deletes on both references.  
B. Cascade deletes on both references.  
C. Block on the invoice reference; cascade on the product reference.  
D. Cascade on the invoice reference; block on the product reference.

### 26. What earns a column the name "foreign key"

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Foreign Keys  
**Is Curriculum Based:** No  
**Assessment type:** Definition application

A hotel database contains:

| Table | What one row represents | Relevant field |
|---|---|---|
| `Rooms` | One hotel room | `room_no`, the room's primary key |
| `RoomServiceOrders` | One food or service request | `room_no`, identifying where to deliver |

Every `RoomServiceOrders.room_no` value matches an existing `Rooms.room_no`.

What makes `room_no` in the orders table a foreign key?

A. It happens to be the leftmost column of the orders table currently.  
B. It holds another table's primary-key values, linking order to room.  
C. It contains numbers rather than text.  
D. It was created after the rooms table was.

### 27. Keep the battery honest

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Database Constraints  
**Is Curriculum Based:** No  
**Assessment type:** Rule-shape selection

A drone database stores one row per aircraft. `battery_charge_pct` means the current battery charge as a percentage of full capacity.

| drone_id | attempted `battery_charge_pct` |
|---|---:|
| DR-18 | 76 |
| DR-19 | 240 |

The operations team must reject values that cannot represent a percentage.

Which rule shape prevents it?

A. A no-duplicates rule, so 240 can occur at most once.  
B. A value-must-be-present rule, so the column is never empty.  
C. A value-range rule confining the column to 0 through 100.  
D. A cross-table reference rule pointing at the drones table.

### 28. The case against the national ID

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Candidate, Composite, and Surrogate Keys  
**Is Curriculum Based:** No  
**Assessment type:** Natural-versus-surrogate judgment

A blood-donation database stores one row per donor:

| Possible identifier | Meaning | Controlled by the registry? |
|---|---|---|
| Government ID | External real-world identifier assigned by government | No |
| `donor_id` | Internal number generated for one donor row | Yes |

The registry is deciding which should become the primary key.

Which argument for the surrogate is strongest?

A. Real-world identifiers sit outside the database's control.  
B. Government IDs contain letters, which primary keys forbid.  
C. Surrogate keys make the table's rows physically smaller than any alternative.  
D. Donors will donate more often if their row number is small.

### 29. The coach leaves, the team remains

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** ON DELETE and ON UPDATE  
**Is Curriculum Based:** No  
**Assessment type:** Policy identification

A sports-league database contains:

| Table | What one row represents | Connection |
|---|---|---|
| `Coaches` | One coach | `coach_id`, the coach's identifier |
| `Teams` | One team | Optional `coach_id`, identifying its current coach |

A coach leaves. Team rows must survive, but their `coach_id` should become empty until a replacement is hired.

Which delete policy matches?

A. Block the coach's deletion while teams reference them.  
B. Delete the teams together with the coach.  
C. Keep the teams pointing permanently at the deleted coach's old row still.  
D. Clear the reference — the team rows survive with an empty coach field.

### 30. Unique alone, or unique together?

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Candidate, Composite, and Surrogate Keys  
**Is Curriculum Based:** No  
**Assessment type:** Uniqueness analysis over data

A cold-storage database stores one row per physical storage location. `warehouse` means the building code, while `bin` means a labelled position inside that building:

| warehouse | bin |
|---|---|
| W1 | A1 |
| W1 | A2 |
| W2 | A1 |

Based on the data's intent, which uniqueness claim is correct?

A. `warehouse` alone can fully and uniquely identify a row here.  
B. Neither alone works, but the pair (`warehouse`, `bin`) does.  
C. `bin` alone can fully and uniquely identify a row in this table.  
D. No key is possible for this table.

### 31. A column with exactly eight legal values

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Attributes and Domains  
**Is Curriculum Based:** No  
**Assessment type:** Domain selection

A blood-bank database stores one row per donor. The field `blood_group` means the donor's medically recorded blood type.

| Field | Business meaning | Permitted values |
|---|---|---|
| `blood_group` | Donor's blood type | A+, A−, B+, B−, AB+, AB−, O+, O− |

What is the appropriate domain for this attribute?

A. Any text up to 100 characters.  
B. Any whole number at all, positive or negative.  
C. A fixed, enumerated set of exactly those eight values.  
D. Any value already present in some other donor's existing row.

### 32. Vans among the electricians

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Tables, Rows, and Columns  
**Is Curriculum Based:** No  
**Assessment type:** Entity-separation judgment

An electrical contractor has placed two different kinds of records into one database table:

| row_kind | name | licence_no | hourly_rate | registration | capacity_kg |
|---|---|---|---:|---|---:|
| Electrician | Maya | EL-81 | 700 | — | — |
| Van | — | — | — | KA-01-V8 | 1200 |

Here, staff fields describe workers, while registration and capacity describe vehicles.

What does the relational model prescribe?

A. Widen the table further until every row can somehow fill every column.  
B. Delete the vehicles, since staff matter more.  
C. Store vehicles as text notes inside the staff rows.  
D. Split into two tables, since staff and vans are different kinds.

### 33. Spot the invented identity

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Candidate, Composite, and Surrogate Keys  
**Is Curriculum Based:** No  
**Assessment type:** Key classification over a schema

A public aquarium database stores one row per water tank:

| Possible identifier | Meaning | Repeats? |
|---|---|---|
| `tank_id` | Number generated by the database | Never |
| (`building`, `room_no`) | Tank's physical location | Pair never repeats |
| `manufacturer_serial` | Serial printed by the manufacturer | Never |

Which is the surrogate key?

A. `tank_id` — invented by the system, carrying no real-world meaning.  
B. The pair (`building`, `room_no`), because it uses two columns.  
C. `manufacturer_serial`, since it comes from entirely outside the aquarium.  
D. All three equally, since all three are unique.

### 34. No destination, no delivery

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Database Constraints  
**Is Curriculum Based:** No  
**Assessment type:** Rule-shape identification

A drone-delivery database stores one row per delivery. `destination` means the physical address or coordinates to which the parcel must travel.

| delivery_id | destination |
|---:|---|
| 701 | Sector 18, Noida |
| 702 | *empty* |

The business declares the second kind of row meaningless.

Which constraint shape enforces this?

A. A value-range rule on the destination column.  
B. A value-must-be-present rule on the destination column.  
C. A strict no-duplicates rule placed directly on the destination column.  
D. A rule referencing the pilots table.

### 35. The key is not the row number

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Primary Keys  
**Is Curriculum Based:** No  
**Assessment type:** Misconception correction

A wind-farm database stores one row per turbine. `turbine_id` is the equipment identifier attached to the machine.

| Current display position | turbine_id | location |
|---:|---:|---|
| 1 | 12 | Ridge |
| 2 | 83 | Valley |
| 3 | 47 | Coast |

An intern asks whether turbine 47's primary key should therefore be 3.

Which correction is accurate?

A. The intern is right; keys must match display position.  
B. The database should renumber keys after every query.  
C. A primary key is a stored identity, not a position; rows have no fixed order.  
D. Primary keys apply only to printed reports, never to the stored tables themselves.

### 36. Design the booking table's rulebook

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Database Constraints  
**Is Curriculum Based:** No  
**Assessment type:** Constraint-set synthesis

A ferry database stores one row per passenger booking:

| Field | Meaning |
|---|---|
| `booking_id` | Identifier of one booking |
| `passenger_name` | Traveller named on that booking |
| `sailing_id` | Particular ferry departure |
| `seat_no` | Seat assigned on that departure |

The database must identify every booking, require a passenger name, and prevent the same (`sailing_id`, `seat_no`) pair from appearing twice.

Which constraint set delivers all three?

A. Primary key on `booking_id`, presence on name, uniqueness on the seat pair.  
B. A no-duplicates rule on `passenger_name` alone.  
C. A value-range rule on `seat_no`; nothing else.  
D. A primary key placed on `passenger_name`; a no-duplicates rule on `booking_id` too.

### 37. Customer 12, five times

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Foreign Keys  
**Is Curriculum Based:** No  
**Assessment type:** Misconception correction

A subscription-box database stores one row per dispatched box. `shipment_id` identifies the shipment, while `customer_id` points to the customer receiving it.

| shipment_id | customer_id | month |
|---:|---:|---|
| 901 | 12 | January |
| 934 | 12 | February |
| 978 | 12 | March |

A reviewer flags the repeated `customer_id` as a uniqueness violation.

What is the correct assessment?

A. The reviewer is right; references may appear once only.  
B. This is normal — a foreign key may repeat freely across many rows.  
C. The database should have automatically merged the five shipments into one row.  
D. Customer 12 must be split into five customer rows to match.

### 38. Three parts in one cell

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Tables, Rows, and Columns  
**Is Curriculum Based:** No  
**Assessment type:** Atomic-value judgment

A bicycle-workshop database stores one row per repair job. Its `parts_used` cell is intended to record which replacement part was fitted:

| repair_id | bicycle_owner | parts_used |
|---:|---|---|
| 301 | Anita | `chain, tube, brake cable` |

Why does this conflict with the relational way of thinking?

A. Part names may not contain spaces.  
B. Cells are limited to two commas each.  
C. A cell should always hold just one value, never any packed-in list at all.  
D. The parts should instead all be stored together as one single combined number value.

### 39. Count the survivors

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** ON DELETE and ON UPDATE  
**Is Curriculum Based:** No  
**Assessment type:** Cascade outcome prediction

A meal-kit database has a `Boxes` table with one row per subscription box and a `BoxItems` table with one row per meal kit placed inside a box. In `BoxItems`, `box_id` identifies the parent box. The reference uses automatic deletion (cascade).

`box_items`

| item_id | box_id | kit |
|---|---|---|
| 1 | 1 | Thai Green Curry |
| 2 | 1 | Falafel Bowl |
| 3 | 2 | Ramen Kit |
| 4 | 2 | Paella Kit |
| 5 | 2 | Biryani Kit |
| 6 | 3 | Taco Kit |

Box 2 is deleted. How many rows remain in `box_items`?

A. 6 — deletes never affect other tables.  
B. 0 — cascade empties the entire table.  
C. 5 — only the very first matching item follows the box away.  
D. 3 — items 3,4,5 go with their box; 1,2,6 remain untouched.

### 40. Read the schema like a designer

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Foreign Keys  
**Is Curriculum Based:** No  
**Assessment type:** Integrated schema interpretation

An esports database uses:

| Table | What one row represents | Fields and roles |
|---|---|---|
| `Leagues` | One competition league | `league_id` uniquely identifies it; `name` labels it |
| `Teams` | One competing team | `team_id` identifies it; `league_id` points to its league |

Which reading of this schema is correct?

A. Each team row points to its league through `league_id`.  
B. Each league row points to one team, so a league may contain only one team.  
C. `team_id` and `league_id` must always hold equal values in a row.  
D. The reference means teams and leagues are the same kind of entity.

---

## Instructor Key

### 1. D

Rows 1 and 2 follow the structure: item, size, rate. Row 3 scatters its values across the wrong attributes — a rate where the item belongs, an item where the size belongs. Relational tables demand that every row be the same kind of record, with each value under its own column.

### 2. B

The domain — whole numbers 1 through 5 — excludes `4.5` for not being whole and `"five"` for not being a number. Option C is the tempting half-answer: range is only part of the domain; the whole-number requirement is equally binding.

### 3. A

The data shows why names fail: two animals legitimately share one. No naming rule (B) can fix legitimate duplication; only a column guaranteed distinct per row — a primary key — makes "exactly this animal" expressible.

### 4. C

The declared reference makes the database verify that `chef_id = 7` exists before accepting the dish. It does not — so the insert fails. The database never invents parent rows (A) or reassigns references to "close" values (D); it simply refuses to create a pointer to nowhere.

### 5. B

Each column repeats individually, but the trio never does: identification exists only in combination, which is the definition of a composite key. A surrogate (A) would be a single invented column, the opposite of combining natural ones.

### 6. D

The entries exist only as parts of their playlist, so the correct policy removes them with it — the cascade behaviour described in the chapter. Blocking (A) would make playlists undeletable in practice, and clearing references (B) would litter the app with entries belonging to nothing.

### 7. A

Rule 1 demands presence, rule 2 demands no duplicates, rule 3 demands staying inside a range — three distinct rule shapes the chapter names. Option D erases exactly the distinction the classification exists to teach.

### 8. C

`court_id` and `member_id` each hold the primary-key values of another table, tying every booking to a real court and a real member. `booking_id` identifies the booking itself, and `start_time` is ordinary data.

### 9. A

The proposal's hidden assumption is permanence. Numbers get changed, recycled by carriers, and shared within families — so both uniqueness and stability decay over time, which is fatal for a value whose job is permanent identity.

### 10. D

The natural combination is unique today, but its parts carry meaning that reality can revise — appointments get rescheduled, therapists reassigned. The surrogate's entire virtue is having no meaning to revise: it identifies the visit no matter what else changes.

### 11. C

A row is one complete instance of the table's subject: here, one shift with its crew and pit. The definition of allowed contents (option A) is the job of the columns and their domains, not of any row.

### 12. A

Columns that could each serve as the primary key are candidate keys; choosing one leaves the others as perfectly good alternates. "Composite" (C) would require them to work only in combination — each of these works alone.

### 13. B

A primary key promises uniqueness (no two rows share a value) and presence (no row leaves it empty). Sorting and speed (C) are storage concerns the relational model does not attach to the key's definition.

### 14. D

The requirement — referencing rows follow the parent's new value automatically — is the propagate-on-update (cascade) policy described in the chapter. Blocking (A) prevents the rename; clearing (B) destroys the very links the business wants preserved.

### 15. C

Domains exist to stop bad values at the door. Launch without them and the door stands open: every nonsense wattage accepted meanwhile is stored, reported on, and eventually someone's cleanup project. The cost of "later" is the accumulating spoiled data, not performance (A).

### 16. B

"No two members share a locker" is a duplication ban on the stored value — the no-duplicates rule shape. It says nothing about presence, range, or references.

### 17. A

In relational design, the many-side rows each carry one reference to their one-side parent; parent rows enumerate nothing. Packing a list of IDs into one cell breaks the one-value-per-cell principle and makes the links unsearchable.

### 18. D

"The attempt itself must fail" is the blocking policy: the database refuses to delete a parent while references to it exist. Options A and B both allow the delete to proceed — precisely what compliance forbids.

### 19. B

The recurring negative weights arrive through the paths that don't validate. A database constraint sits below all three writers, so no path — present or future — can skip it. That positional advantage, not speed (A), is the argument.

### 20. C

A column defines one attribute and commits every row to supplying a value of that same kind. Mixed content per row (B) is exactly what column discipline rules out.

### 21. A

A primary key is enforced by the database, not suggested to it: the duplicate insert fails outright. Silent replacement (C) or automatic renumbering (D) would both hide a data error the constraint exists to surface.

### 22. D

Every natural column shown repeats across rows, so none can promise uniqueness. The generated `parcel_id` exists precisely to make that promise.

### 23. B

With no reference rule, the database allowed a parent to vanish while children still point at it — orphaned references. The harm is unanswerable data: loans held by a musician who, as far as the database knows, never existed.

### 24. C

The two columns share a label but describe different properties with different legal values—one numeric, one an enumerated set. A shared name does not force two attributes to share a domain.

### 25. D

Lines are parts of their invoice and should die with it: cascade. Products are independent entities other lines may reference: block. Option C assigns each policy to the wrong relationship, which would delete the catalogue and preserve the debris.

### 26. B

A foreign key is defined by what its values are: primary-key values of another table, used to link rows. Position (A), datatype (C), and creation order (D) are all incidental.

### 27. C

The failure was a value outside physical possibility. A range rule (0–100) rejects such values at the door. A duplicate ban (A) would absurdly allow one impossible reading per value.

### 28. A

The core principle: a primary key's value should never need to change, and the registry does not control government IDs — corrections and re-issues happen in the outside world. The invented `donor_id` is immune because it means nothing.

### 29. D

Teams survive with an emptied reference: the clear-the-reference policy. Blocking (A) would trap the coach's row forever; cascading (B) would delete teams that still exist in reality.

### 30. B

W1 repeats, and A1 repeats — each column fails alone. The pair never repeats: each bin is identified by which warehouse it is in plus its label. Unique only together is the composite-key signature.

### 31. C

The attribute's legal values are a fixed list of eight; the domain should be exactly that enumerated set. "Any text" (A) admits typos like "AB±" that the domain exists to refuse.

### 32. D

A table holds one kind of thing. Staff and vans have different attributes, which is why every mixed row is half-empty; the model's answer is one table per entity kind, not a wider mixed table (A).

### 33. A

The surrogate is the identity invented by the system with no outside meaning — `tank_id`. The room pair and manufacturer serial are natural facts about the tank; both are candidate keys, but neither is invented.

### 34. B

The rule demands that a value exist in every row: the presence rule shape. Range and duplication are different rule shapes answering different questions.

### 35. C

Rows have no inherent position; today's third row may print first tomorrow. The key is stored identity that travels with the row — which is exactly why display order can be left free.

### 36. A

Three requirements, three mechanisms: a primary key for identity, a presence rule for the name, and a no-duplicates rule on the (sailing, seat) pair so a seat can sell once per sailing yet exist on every sailing. Option D makes passenger names unique — banning repeat customers.

### 37. B

Uniqueness belongs to the referenced primary key (`customers.customer_id`), not to the referencing column. Five shipments for one customer is the many-to-one shape working exactly as designed.

### 38. C

Searching for tube repairs, counting chains used, or linking to a parts inventory all require parts as separate values. A comma-packed cell hides three values where the model expects one, defeating each of those operations.

### 39. D

Cascade removes exactly the rows referencing the deleted box: items 3, 4, and 5. The policy is surgical, not global (B) — rows referencing boxes 1 and 3 are untouched.

### 40. A

`league_id` in `teams` is the foreign key: many teams may point at one league. And because references exist, removing a league is no longer a free action — some deliberate policy (block, cascade, or clear) must govern the teams left behind.

---

## Question-Type Distribution

| Higher-order assessment family | Question numbers |
|---|---|
| Structure and schema reading | 1, 8, 11, 20, 26, 33, 40 |
| Enforcement and outcome prediction | 2, 4, 21, 39 |
| Problem-to-mechanism and rule-shape mapping | 3, 7, 16, 27, 34 |
| Key classification and uniqueness analysis | 5, 12, 13, 22, 30 |
| Policy selection and per-relationship design | 6, 14, 18, 25, 29 |
| Design critique and rationale | 9, 10, 15, 17, 19, 28, 36 |
| Misconception correction | 23, 24, 31, 32, 35, 37, 38 |

## Blueprint Taxonomy Coverage

| Subtopic from the attached blueprint | Question numbers | Count |
|---|---|---:|
| Tables, Rows, and Columns | 1, 11, 20, 32, 38 | 5 |
| Attributes and Domains | 2, 15, 24, 31 | 4 |
| Primary Keys | 3, 9, 13, 21, 22, 35 | 6 |
| Foreign Keys | 4, 8, 17, 23, 26, 37, 40 | 7 |
| Candidate, Composite, and Surrogate Keys | 5, 10, 12, 28, 30, 33 | 6 |
| Database Constraints | 7, 16, 19, 27, 34, 36 | 6 |
| ON DELETE and ON UPDATE | 6, 14, 18, 25, 29, 39 | 6 |

Questions 1–10 collectively cover all seven Topic 1.2 subtopics.

## Difficulty and Answer-Key Balance

- Foundational: 12 questions (1, 3, 5, 8, 10, 11, 13, 16, 20, 22, 31, 34)
- Intermediate: 19 questions (2, 4, 7, 9, 12, 15, 18, 19, 21, 24, 26, 27, 29, 32, 33, 35, 37, 38, 40)
- Advanced: 9 questions (6, 14, 17, 23, 25, 28, 30, 36, 39)
- Correct option A: 10 questions (3, 7, 9, 12, 17, 21, 28, 33, 36, 40)
- Correct option B: 10 questions (2, 5, 13, 16, 19, 23, 26, 30, 34, 37)
- Correct option C: 10 questions (4, 8, 11, 15, 20, 24, 27, 31, 35, 38)
- Correct option D: 10 questions (1, 6, 10, 14, 18, 22, 25, 29, 32, 39)
- Longest consecutive run of one correct letter: below 3 throughout
