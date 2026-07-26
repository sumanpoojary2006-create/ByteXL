# DBMS 2.2: Normalization — 40 Higher-Order MCQs

## Assessment specifications

- **Subject:** DBMS
- **Topic:** Database Design & Modeling
- **Chapter:** Normalization
- **Scope:** All seven Topic 2.2 subtopics in the attached course blueprint (Why Normalize: Anomalies; Functional Dependencies; First Normal Form; Second Normal Form; Third Normal Form; Boyce-Codd Normal Form; When to Denormalize)
- **Format:** Four options with exactly one best answer
- **Curriculum flag:** No
- **Design standard:** Every scenario explicitly identifies the database, the role of its important fields, and the fact or rule being tested. Tables, dependency maps, before/after schemas, and workload evidence are used whenever they strengthen the reasoning task.
- **Scope guard:** Questions use only ideas taught in Topic 2.2. Business details provide context but do not require outside domain knowledge.
- **Answer-quality controls:** A/B/C/D each correct exactly 10 times, no letter correct more than twice consecutively, no correct answer identifiable by length.
- **Coverage rule:** Questions 1–10 collectively cover all seven Topic 2.2 subtopics.
- **Student/instructor separation:** Questions appear first; answers and explanations follow in the instructor key.

---

## Questions

### 1. One fact, fixed in one place only

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Why Normalize: Anomalies  
**Is Curriculum Based:** No  
**Assessment type:** Anomaly identification over data

A tea exporter's table after a clerk "corrected" the supplier's city on one row:

`shipments`

| shipment_id | supplier | supplier_city | qty_kg |
|---|---|---|---|
| S1 | BlueLeaf Estates | Coonoor | 500 |
| S2 | BlueLeaf Estates | Ooty | 300 |
| S3 | Karo Traders | Surat | 900 |

BlueLeaf has exactly one real city, yet the table now offers two.

The data-quality incident should be logged as:

A. Delete anomaly, because correcting a city removes a supplier record.  
B. Insert anomaly — a supplier could not be added.  
C. No anomaly — tables may hold both versions.  
D. Update anomaly: one fact in many rows, changed in only some.

### 2. What the arrow promises

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Functional Dependencies  
**Is Curriculum Based:** No  
**Assessment type:** Definition application

A tax platform stores one row per tax account. `pan_number` is the government-issued account identifier and `holder_name` is the registered person's name. Its design rule is:

| Determinant (X) | Dependent field (Y) |
|---|---|
| `pan_number` | `holder_name` |

What does this X → Y statement actually mean?

A. Rows sharing `pan_number` must show the same `holder_name` value.  
B. The name column stores a physical pointer to the PAN column in every row.  
C. Every holder determines their own PAN retroactively.  
D. The two columns must be stored adjacently.

### 3. Three languages in one cell

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** First Normal Form  
**Is Curriculum Based:** No  
**Assessment type:** Violation identification

A tour-guide agency stores one row per guide. In its database, `guide_id` identifies the guide and `spoken_languages` should record the languages the guide can speak.

| guide_id | guide_name | spoken_languages |
|---|---|---|
| G14 | Rehana | Hindi, Marathi, Tamil |

Why does this cell violate first normal form?

A. Language names must be translated into English before a database can compare them.  
B. 1NF requires atomic values, one per cell — this cell packs three.  
C. 1NF permits no more than two values in a text column.  
D. Text columns are not allowed in 1NF tables.

### 4. Only half the key is doing the work

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Second Normal Form  
**Is Curriculum Based:** No  
**Assessment type:** Partial-dependency detection

A spare-parts distributor's table, keyed on (`order_id`, `part_id`):

| order_id | part_id | part_name | qty |
|---|---|---|---|
| O1 | P7 | Brake pad | 4 |
| O1 | P9 | Air filter | 2 |
| O2 | P7 | Brake pad | 6 |

Select the dependency that the 2NF audit must flag.

A. (`order_id`, `part_id`) → `qty`, because a full dependency is prohibited.  
B. `order_id → part_id`, since orders contain parts.  
C. `part_id → part_name` depends on only part of the composite key.  
D. There is no violation; repeated names are coincidence.

### 5. Two hops to the max load

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Third Normal Form  
**Is Curriculum Based:** No  
**Assessment type:** Transitive-dependency detection

A courier fleet's table, keyed on `van_id`:

| van_id | model_code | model_max_load |
|---|---|---|
| V1 | M-200 | 800 |
| V2 | M-200 | 800 |
| V3 | M-450 | 1500 |

Complete the review note: “The table fails 3NF because of ______.”

A. `van_id → model_code → model_max_load`: transitive dependency.  
B. `model_max_load → van_id`, because every load value identifies one van.  
C. `van_id → van_id` — the key depends on itself.  
D. No chain exists; three columns cannot form one.

### 6. The judge who always sits at table five

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Boyce-Codd Normal Form  
**Is Curriculum Based:** No  
**Assessment type:** BCNF-violation detection

A wine-tasting system records scores keyed on (`wine`, `judge`). House rule: each judge works at exactly one table all evening, so `judge → table_no` holds.

| wine | judge | table_no |
|---|---|---|
| Shiraz '21 | Mira | 5 |
| Merlot '20 | Mira | 5 |
| Shiraz '21 | Aldo | 2 |

Why does this table fail BCNF?

A. The key has two columns, whereas BCNF permits only one-column candidate keys.  
B. `table_no` is numeric while judges are text.  
C. A wine occurs in more than one tasting row.  
D. `judge` determines `table_no`, but isn't a candidate key.

### 7. Buying speed with copies

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** When to Denormalize  
**Is Curriculum Based:** No  
**Assessment type:** Tradeoff characterization

A marketplace has a normalized operational database: `orders.category_id` identifies a product category, while `categories.category_name` stores its display name. Its bestseller dashboard joins four tables and has grown slow. The team proposes this change:

| Before | Proposed read-side copy |
|---|---|
| Orders hold `category_id` only | Orders also hold `category_name` |

What is the correct characterization of this move?

A. Normalization, because the copied field removes redundant joins.  
B. Denormalization, reintroducing redundancy for read speed.  
C. A violation of 1NF, since names repeat.  
D. A cost-free optimization with no downside.

### 8. The supplier who cannot exist yet

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Why Normalize: Anomalies  
**Is Curriculum Based:** No  
**Assessment type:** Anomaly identification

A furniture importer uses `shipment_id` for a received delivery and `supplier_id` for the company sending it. Supplier contact and payment terms exist only in shipment rows:

| shipment_id | supplier_id | supplier_phone | payment_terms |
|---|---|---|---|
| SH41 | SUP8 | 080-555-0181 | Net 30 |

A newly signed supplier, SUP9, has no shipment yet. The onboarding form therefore cannot save SUP9's phone or payment terms.

Assign the correct anomaly label to SUP9's failed onboarding.

A. Update anomaly, because every shipment row for SUP9 would require the same contact edit.  
B. Delete anomaly — a fact was lost.  
C. Insert anomaly: a fact can't be recorded until an unrelated event occurs.  
D. A 1NF violation — the contact is a list.

### 9. Read the rule out of the rows

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Functional Dependencies  
**Is Curriculum Based:** No  
**Assessment type:** Dependency reading from data

A land-records table:

| plot_no | sector | sector_office |
|---|---|---|
| P1 | S1 | Office A |
| P2 | S1 | Office A |
| P3 | S2 | Office B |
| P4 | S2 | Office B |

Every plot in a sector is always served by that sector's one office. Which functional dependency does the data (and rule) support?

A. `sector_office → plot_no`  
B. `plot_no → sector_office → sector`  
C. `sector_office → sector`, because each shown office serves one sector.  
D. `sector → sector_office` — same sector, same office, always.

### 10. Three phone columns

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** First Normal Form  
**Is Curriculum Based:** No  
**Assessment type:** Violation-variant identification

A charter-bus firm uses `operator_id` to identify a bus operator. Its database gives every operator three fixed phone slots:

| operator_id | phone_1 | phone_2 | phone_3 |
|---|---|---|---|
| OP7 | 98710 11111 |  |  |
| OP9 | 98110 22222 | 98220 33333 |  |

How does this design relate to 1NF?

A. It satisfies 1NF because each cell is atomic and the fixed phone slots are ordinary attributes.  
B. It is the repeating-group failure: fact type spread across columns.  
C. It fails only if a fourth phone appears.  
D. It is a BCNF issue, not a 1NF one.

### 11. Name the determinant

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Functional Dependencies  
**Is Curriculum Based:** No  
**Assessment type:** Vocabulary application

An airport stores a daily departure assignment. `flight_no` identifies a scheduled service, `departure_date` identifies its operating day, and `gate` is where passengers board.

| Documented rule |
|---|
| (`flight_no`, `departure_date`) → `gate` |

What is the determinant in this dependency?

A. `gate`, because the determined field on the right of an arrow is always the determinant.  
B. `flight_no` alone.  
C. The pair (`flight_no`, `departure_date`) is the determinant.  
D. The airport itself.

### 12. Why single-column keys sleep through 2NF

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Second Normal Form  
**Is Curriculum Based:** No  
**Assessment type:** Scope-of-rule reasoning

A hotel table is already in 1NF, and `booking_id` alone uniquely identifies each reservation:

| Table | Primary key |
|---|---|
| `bookings(booking_id, guest_id, room_no, check_in)` | `booking_id` |

A reviewer declares it free of *partial-key* dependency violations before inspecting the non-key fields.

Why is the reviewer right?

A. A partial dependency means depending on part of a composite key; impossible.  
B. Single-column keys disable all normal forms.  
C. Booking tables are exempt from normalization.  
D. The reviewer is wrong because every non-key field must depend on two key columns.

### 13. The row that took a fact down with it

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Why Normalize: Anomalies  
**Is Curriculum Based:** No  
**Assessment type:** Anomaly identification over data

A gallery's only record of artist contact details lives in its exhibit rows:

| exhibit_id | artist | artist_phone |
|---|---|---|
| E1 | R. Bose | 98200 11111 |

Exhibit E1 closes and its row is deleted. The gallery later tries to invite R. Bose back — and finds no trace of the phone number anywhere.

The post-deletion incident is best classified as:

A. Update anomaly: the phone was changed in only one exhibit row.  
B. Insert anomaly: a new artist could not be stored before an exhibit.  
C. 1NF violation: the phone cell contained multiple values.  
D. Delete anomaly, destroying an unrelated fact along with it.

### 14. Split along the chain

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Third Normal Form  
**Is Curriculum Based:** No  
**Assessment type:** Decomposition selection

The courier fleet uses `van_id` for an individual vehicle and `model_code` for its manufacturer model. Every model has one `model_max_load`.

| Existing table | Dependency chain |
|---|---|
| `vans(van_id, model_code, model_max_load)` | `van_id → model_code → model_max_load` |

Approve the only split that reaches 3NF while retaining the van-to-model link.

A. `vans(van_id)` and `loads(model_max_load)` — drop the model entirely.  
B. `vans(van_id, model_code)` and `models(model_code, model_max_load)`.  
C. `vans(van_id, model_max_load)` and `models(model_code)` — separate the numbers.  
D. No split; delete the max-load column instead.

### 15. What "atomic" actually requires

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** First Normal Form  
**Is Curriculum Based:** No  
**Assessment type:** Requirement statement

A data-model review lists four proposed rules for a customer table. Which one is the actual 1NF acceptance rule?

A. All values must be numbers.  
B. Every table requires a timestamp generated by an atomic clock before its values count as atomic.  
C. Each cell holds exactly one value — no lists, no repeat columns.  
D. Tables must have fewer than ten columns.

### 16. The right patient for the medicine

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** When to Denormalize  
**Is Curriculum Based:** No  
**Assessment type:** Candidate selection

Two systems at a logistics firm are candidates for denormalization:

| System | Reads | Writes | Refresh/control |
|---|---:|---:|---|
| Analytics dashboard | Thousands/day | Nightly rebuild | Generated from source |
| Live order entry | Continuous | Hundreds of clerks | Direct concurrent edits |

Which is the appropriate candidate, and why?

A. System 1 — heavy reads benefit from redundancy kept in sync nightly.  
B. System 2 — writes always benefit from redundancy.  
C. Both equally, because redundancy improves reads and writes by the same amount.  
D. Neither — denormalization is never acceptable.

### 17. The one question BCNF asks

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Boyce-Codd Normal Form  
**Is Curriculum Based:** No  
**Assessment type:** Rule statement

A database design checklist must contain BCNF's decisive test. Which line should the reviewer insert?

A. Every column must be atomic.  
B. No composite keys may exist.  
C. Every table may document only one functional dependency, regardless of how many candidate keys it has.  
D. For every dependency, the determinant must be a candidate key.

### 18. Partial or transitive? Tell them apart

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Third Normal Form  
**Is Curriculum Based:** No  
**Assessment type:** Dependency discrimination

Two database-design tickets contain these key and dependency maps:

| Ticket | Table key | Observed dependency |
|---|---|---|
| Invoice lines | (`invoice_no`, `line_no`) | `invoice_no → customer_name` |
| Employees | `employee_id` | `employee_id → branch_code → branch_city` |

`invoice_no` identifies an invoice, `line_no` one item on it, and `branch_code` identifies an office branch.

Which classification is correct?

A. Both are partial dependencies.  
B. Finding 1 is transitive through `invoice_no`; finding 2 is partial on `branch_code`.  
C. Finding 1 is a partial dependency; finding 2 is transitive.  
D. Both are BCNF violations only.

### 19. Two Priyas, one direction

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Functional Dependencies  
**Is Curriculum Based:** No  
**Assessment type:** Directionality reasoning

A security-badge register uses `badge_id` to identify one issued badge and `holder_name` for the person carrying it:

| badge_id | holder_name |
|---|---|
| B-101 | Priya Nair |
| B-207 | Priya Nair |

Which conclusion about dependencies is correct?

A. `holder_name → badge_id`, because every displayed name has one badge.  
B. `badge_id → holder_name` holds, but the reverse does not hold.  
C. Neither direction can hold when a name repeats.  
D. Both directions hold by symmetry.

### 20. The repair that ends the repetition

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Second Normal Form  
**Is Curriculum Based:** No  
**Assessment type:** Decomposition selection

In an order-line database, `order_id` identifies an order, `part_id` identifies a stocked part, and `qty` is the amount of that part ordered.

| Current table | Key | Problem rule |
|---|---|---|
| `order_lines(order_id, part_id, part_name, qty)` | (`order_id`, `part_id`) | `part_id → part_name` |

Select the smallest repair that moves the partially dependent fact to its proper home.

A. `order_lines(order_id, part_id, qty)` and `parts(part_id, part_name)`.  
B. `order_lines(order_id, part_name)` and `parts(part_id, qty)`, with the name detached from its identifier.  
C. One wider table including the supplier as well.  
D. Delete `part_name` from the database entirely.

### 21. Match the three failures to their names

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Why Normalize: Anomalies  
**Is Curriculum Based:** No  
**Assessment type:** Anomaly matching

A database review logs three incidents:

| Incident | Observed effect |
|---|---|
| 1 | A supplier cannot be recorded until its first shipment exists. |
| 2 | A supplier phone change requires many shipment-row edits. |
| 3 | Removing the last shipment also removes the supplier's only address. |

Match incidents 1–3 to their anomaly names.

A. 1: update, 2: delete, 3: insert anomaly  
B. 1: delete, 2: insert, 3: update  
C. All three are update anomalies.  
D. 1: insert, 2: update, 3: delete.

### 22. Directly on the key, or not at all

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Third Normal Form  
**Is Curriculum Based:** No  
**Assessment type:** Rule statement

A designer has already confirmed that `employees(employee_id, branch_code, branch_city)` is in 2NF. The business rule is `branch_code → branch_city`. Which review comment correctly states what 3NF adds?

A. Every cell must be atomic.  
B. Composite keys are banned.  
C. Non-key attributes must depend on the key directly, not transitively.  
D. Tables must be split until each table contains exactly two columns, even when no dependency requires it.

### 23. Unpack the languages

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** First Normal Form  
**Is Curriculum Based:** No  
**Assessment type:** Repair selection

In `guides`, `guide_id` identifies a guide, but `spoken_languages` stores a comma-separated list:

| guide_id | spoken_languages |
|---|---|
| G14 | Hindi, Marathi, Tamil |

The agency wants each language to become an independently searchable database fact.

Choose the redesign that makes each language an atomic fact.

A. A separate `guide_languages` table, one row per guide-language pair.  
B. Wider cells so longer lists fit.  
C. Rename the column to `spoken_languages_list`.  
D. Keep the combined list, replace commas with semicolons, and index the full text field.

### 24. The bill for the speed

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** When to Denormalize  
**Is Curriculum Based:** No  
**Assessment type:** Cost identification

A marketplace deliberately copied category names into historical order rows:

| order_id | category_id | copied_category_name |
|---|---|---|
| O71 | C4 | Home & Kitchen |
| O85 | C4 | Home & Kitchen |
| O92 | C8 | Books |

The authoritative category row C4 is renamed to “Home Living.”

Identify the new maintenance obligation created by the copied name.

A. The dashboard can no longer read category names from orders.  
B. Every order row with the old name must be updated too.  
C. Nothing — copies update themselves.  
D. The orders table drops out of 1NF.

### 25. The loophole BCNF closes

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Boyce-Codd Normal Form  
**Is Curriculum Based:** No  
**Assessment type:** Rule-comparison reasoning

An academy records which instructor teaches each student-subject pairing:

`teaching(student_id, subject_code, instructor_id)`

The documented rules produce two candidate keys:

- (`student_id`, `subject_code`)
- (`student_id`, `instructor_id`)

Each instructor teaches exactly one subject, so `instructor_id → subject_code`. The dependent `subject_code` is a *prime attribute* because it belongs to a candidate key. This permits 3NF, but `instructor_id` alone is not a candidate key.

What does BCNF do differently that catches this?

A. It bans every table that has more than one candidate key or any composite candidate key.  
B. It requires every attribute to be numeric.  
C. It counts rows rather than dependencies.  
D. It asks one question: is every determinant a candidate key?

### 26. Full or partial: judge each column

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Second Normal Form  
**Is Curriculum Based:** No  
**Assessment type:** Dependency discrimination

A football league uses `match_id` for a scheduled match and `player_id` for a registered player. Its appearance table is keyed on (`match_id`, `player_id`):

| Column | Depends on |
|---|---|
| minutes_played | the specific player in the specific match |
| player_name | the player, regardless of match |

Which assessment is correct?

A. `minutes_played` is fully dependent; `player_name` only partially.  
B. Both are partial dependencies.  
C. Both are fully dependent on the key.  
D. `minutes_played` violates 2NF because needing both key columns is a partial dependency.

### 27. From house rules to arrows

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Functional Dependencies  
**Is Curriculum Based:** No  
**Assessment type:** Rule-to-dependency translation

A single hotel's database uses a unique `room_no` for each room. Every room is on exactly one floor and has one nightly rate; a floor contains many rooms.

| Example room_no | floor | nightly_rate |
|---|---:|---:|
| R201 | 2 | 4200 |
| R202 | 2 | 4600 |
| R305 | 3 | 5100 |

Which dependency set matches?

A. `floor → room_no` and `nightly_rate → room_no`, because shared floors and rates identify rooms.  
B. `room_no → floor → nightly_rate`  
C. `room_no → floor` and `room_no → nightly_rate` hold.  
D. No dependencies exist in hotels.

### 28. First things first

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Second Normal Form  
**Is Curriculum Based:** No  
**Assessment type:** Sequencing rationale

A freight table stores one dispatch per row, but its `container_codes` cell combines every container on that dispatch:

| dispatch_id | container_codes |
|---|---|
| D18 | CX4, CX7, CX9 |

A consultant begins testing its non-key columns for partial dependency.

Complete the consultant's review note: “Do not classify this table as 2NF yet because ______.”

A. 2NF checks are alphabetical, and commas sort first.  
B. 2NF is defined on top of 1NF, presuming atomic cells already.  
C. It need not be; the forms are independent.  
D. Because every comma-separated value necessarily depends on half a key.

### 29. One table, three stories

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Why Normalize: Anomalies  
**Is Curriculum Based:** No  
**Assessment type:** Root-cause analysis

A trading firm's table mixes three kinds of facts. `supplier_id` identifies a supplier, `warehouse_id` a storage site, and `shipment_id` a delivery event.

| shipment_id | supplier_id | supplier_phone | warehouse_id | warehouse_city |
|---|---|---|---|---|
| SH1 | S7 | 040-555-0101 | W2 | Jaipur |
| SH2 | S7 | 040-555-0101 | W5 | Pune |

It cannot store a supplier without a shipment, repeats supplier phones, and may lose a warehouse's only details when its last shipment is deleted.

What is the structural root cause?

A. Facts about three kinds of things share one table, entangled.  
B. The table has exceeded the maximum safe row count for a relation.  
C. The clerks type too quickly.  
D. The table lacks a colourful header row.

### 30. What the chain costs in practice

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Third Normal Form  
**Is Curriculum Based:** No  
**Assessment type:** Consequence tracing

A staffing agency uses `staff_id` to identify an employee and `branch_code` to identify the employee's office branch. Each branch has one `branch_city`, giving `staff_id → branch_code → branch_city`.

| staff_id | branch_code | branch_city |
|---|---|---|
| 1 | BR-N | Indore |
| 2 | BR-N | Indore |
| 3 | BR-S | Kochi |

Branch BR-N relocates to Bhopal.

Choose the maintenance outcome the existing rows predict.

A. One update to the first BR-N staff row, after which the database propagates the city automatically.  
B. Deleting all BR-N staff first.  
C. Nothing; cities never change.  
D. Every BR-N row must be edited; a missed row would leave conflicting cities.

### 31. The one table that passes

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** First Normal Form  
**Is Curriculum Based:** No  
**Assessment type:** Compliance discrimination

A gym database uses `member_id` to identify a member. It must store zero or more emergency contacts per member. Four designs are proposed:

1. `contacts = "Ravi 98x, Meera 97x"` in one cell  
2. Columns `contact_1`, `contact_2`, `contact_3`  
3. A `member_contacts` table: one row per member-contact pair  
4. A `notes` column mixing contacts with diet preferences

Which design satisfies 1NF?

A. Design 1 — lists in cells.  
B. Design 2 — repeat columns.  
C. Design 3 — atomic cells.  
D. Design 4 — mixed formats.

### 32. A discipline, not a free pass

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** When to Denormalize  
**Is Curriculum Based:** No  
**Assessment type:** Practice-standard selection

A junior engineer proposes this design sequence for a new inventory database:

| Stage | Proposed action |
|---|---|
| Initial design | Store product, supplier, and order facts together |
| Later | Call the repeated fields “denormalized” |

No measured query bottleneck or synchronization method has been identified.

Which correction reflects the chapter?

A. Agreed — normal forms are obsolete.  
B. Denormalization is an exception, not a starting point: normalize first.  
C. Denormalization is forbidden even after measurement, planning, and a controlled refresh strategy.  
D. The order does not matter as long as the tables load.

### 33. Run the check yourself

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Boyce-Codd Normal Form  
**Is Curriculum Based:** No  
**Assessment type:** BCNF verification

An airfield uses `flight` for a scheduled service and `aircraft` for a physical plane. Its roster is keyed on (`flight`, `aircraft`):

| flight | aircraft | hangar |
|---|---|---|
| AX101 | VT-A7 | H2 |
| AX205 | VT-A7 | H2 |
| BX300 | VT-K4 | H5 |

Each aircraft has exactly one home hangar, so `aircraft → hangar`.

Record the BCNF verdict and the dependency-based reason.

A. No — `aircraft` is a determinant but not a candidate key here.  
B. Yes — composite keys always guarantee BCNF.  
C. Yes, because dependencies apply only to identifiers, not locations.  
D. Cannot be decided without row counts.

### 34. Why the comma cell defeats the database

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** First Normal Form  
**Is Curriculum Based:** No  
**Assessment type:** Rationale selection

A training company stores instructors' skills in one field:

| instructor_id | skill_names |
|---|---|
| I17 | Python, SQL, Linux |

The reporting team must count SQL instructors and link each skill to its certification record. What practical obstacle does this design create?

A. The ability to store the instructor's name.  
B. No obstacle; the commas make each skill independently searchable, countable, and linkable.  
C. Reliable skill searches, counts, and certification links become difficult.  
D. The ability to back up the table.

### 35. A pattern is not yet a rule

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Functional Dependencies  
**Is Curriculum Based:** No  
**Assessment type:** Rule-versus-coincidence judgment

An online shop is considering the business rule `product_code → tax_rate`, meaning one product code must always have one tax rate. Its three-row pilot sample happens to show:

| product_code | tax_rate |
|---|---:|
| P10 | 5 |
| P10 | 5 |
| P21 | 12 |

An analyst says these rows alone prove the rule for all future data.

Choose the response that separates a sample pattern from a functional dependency.

A. A functional dependency becomes proven after at least ten agreeing rows from the production database.  
B. Numeric rates cannot depend on text product codes.  
C. The arrow points the wrong way.  
D. A sample can disprove an FD, but agreement cannot prove it for every valid row.

### 36. The repetition 2NF was warning about

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Second Normal Form  
**Is Curriculum Based:** No  
**Assessment type:** Consequence tracing

The spare-parts distributor keeps the partially dependent `part_name` in its order-line table:

| order_id | part_id | part_name |
|---|---|---|
| O1 | P7 | Brake pad |
| O2 | P7 | Brake pad |
| O3 | P9 | Air filter |

Part P7 is renamed “Brake pad (ceramic).”

What happens?

A. The rename lands automatically everywhere.  
B. Every order line for P7 carries the old name and must be edited.  
C. Only the newest P7 row needs editing because it is the latest copy.  
D. The composite key blocks the rename entirely.

### 37. The system that should stay normalized

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** When to Denormalize  
**Is Curriculum Based:** No  
**Assessment type:** Tradeoff decision

A payments processor compares two workloads:

| Database component | Reads | Writes | Consistency requirement |
|---|---:|---:|---|
| Core ledger | High | Hundreds/second | Every balance exact |
| Nightly report copy | High next morning | One controlled rebuild | May reflect last rebuild |

An engineer proposes adding editable repeated balance fields to the core ledger for reporting convenience.

Which decision is right?

A. Denormalize — ledgers enjoy redundancy.  
B. Denormalize half the balance fields to reduce the inconsistency risk.  
C. Flip a coin; the tradeoff is symmetric.  
D. Keep the ledger normalized; write-heavy data resists redundancy.

### 38. Choose the split that loses nothing

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Third Normal Form  
**Is Curriculum Based:** No  
**Assessment type:** Decomposition judgment

A weather network uses `sensor_id` for a measuring device and `station_code` for the site hosting it. One station has one `station_altitude`. Its table has the chain `sensor_id → station_code → station_altitude`. Four decompositions are proposed:

1. `sensors(sensor_id, station_code)` + `stations(station_code, station_altitude)`  
2. `sensors(sensor_id)` + `stations(station_code, station_altitude)`  
3. `sensors(sensor_id, station_altitude)` + `stations(station_code)`  
4. `sensors(sensor_id, station_code, station_altitude)` unchanged

Approve the proposal that reaches 3NF without breaking the sensor-to-station link.

A. Proposal 3 — altitude stays with the sensor.  
B. Proposal 2, because the smallest possible tables preserve every relationship.  
C. Proposal 1 — the chain is cut cleanly at its joint.  
D. Proposal 4 — the chain is harmless.

### 39. The strict sibling

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Boyce-Codd Normal Form  
**Is Curriculum Based:** No  
**Assessment type:** Relationship statement

A revision card compares 3NF and BCNF. Which sentence should be retained because it states their relationship correctly?

A. They are identical rules with two names.  
B. BCNF is strictly stronger than 3NF, though not vice versa.  
C. 3NF is stronger, while BCNF permits more dependency patterns.  
D. They apply to different databases entirely.

### 40. Sunrise Traders, six months later

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** When to Denormalize  
**Is Curriculum Based:** No  
**Assessment type:** Integrated tradeoff assessment

After normalization, a trading firm's sales dashboard needs four joins and runs slowly. Measurements show:

| Item | Evidence |
|---|---|
| Report use | 60,000 reads/day |
| Source updates | Continuous |
| Proposed summary | Read-only; rebuilt nightly |
| Source of truth | Normalized operational tables |

The architecture review should record this arrangement as:

A. A disciplined denormalization: a documented, one-way copy of the truth.  
B. A mistake, because the summary should accept direct edits and become the operational source of truth.  
C. A return to the original mega-table design.  
D. Unnecessary — normalized tables are always fast enough.

---

## Instructor Key

### 1. D

One real-world fact (BlueLeaf's city) lives in multiple rows; an update touched some copies and not others, and the table now disagrees with itself. That partial-fix disagreement is the update anomaly.

### 2. A

X → Y is a promise about value agreement: rows agreeing on X must agree on Y. It is a semantic rule, not a storage arrangement (D) or a pointer (B).

### 3. B

Atomicity means one value per cell. Three languages in one string are invisible to the database as individual facts — they can only be pattern-matched as text, which is exactly the unreliability 1NF exists to prevent.

### 4. C

`part_name` is settled by `part_id` alone — half the key — so the same name is re-stored on every order that touches the part. Full dependencies like `qty` (option A) are what 2NF *wants*; the partial one is the violation.

### 5. A

The load reaches the van only through the model: van determines model, model determines load. That two-hop route through a non-key attribute is the transitive dependency 3NF forbids — and it is why 800 appears twice.

### 6. D

BCNF's single test: every determinant must be a candidate key. `judge` determines `table_no` but cannot identify a row of the (wine, judge) table alone — so the dependency fails the test, and the table number is stored redundantly per wine scored.

### 7. B

Copying the category name back onto orders reintroduces redundancy on purpose — that is denormalization, and its price is the synchronization duty the team now carries. Option D denies the price; option A inverts the direction.

### 8. C

The supplier's facts have no home of their own; they can only enter the database attached to a shipment that does not exist yet. Facts held hostage by missing unrelated rows are the insert anomaly.

### 9. D

All rows agreeing on sector agree on office, and the stated business rule ("each sector served by one office") confirms it as a rule rather than coincidence: `sector → sector_office`.

### 10. B

Numbered repeat columns are the second face of the 1NF failure: one fact type (phone) fragmented across a fixed set of columns, with emptiness padding the gaps and a hard ceiling when a fourth number arrives.

### 11. C

The determinant is the left-hand side — here the composite pair. Neither column alone settles the gate; the pair does.

### 12. A

Partial dependency is defined as dependence on a proper part of a composite key. A single-column key has no proper part, so the definition cannot be triggered — the reviewer's shortcut is structurally sound.

### 13. D

The exhibit row was the phone number's only home, so a routine deletion silently destroyed an unrelated fact. That collateral loss is the delete anomaly — and the reason artist details deserved their own table.

### 14. B

The chain is cut at its middle link: vans keep their model reference, models keep their load. Each attribute now depends directly on the key of its own table, and joining the two reproduces the original facts.

### 15. C

1NF's demand is structural honesty: one cell, one value — no lists smuggled into cells, no fact type scattered across repeat columns.

### 16. A

Denormalization suits read-heavy, refresh-synchronized workloads, where copies are rebuilt wholesale and never hand-edited. The write-heavy order system is the anti-candidate: every redundant copy there is another thing each of hundreds of writers can leave inconsistent.

### 17. D

BCNF is one uniform question asked of every dependency: is the determinant a candidate key? No special cases, no exemptions — which is precisely its difference from the earlier forms.

### 18. C

Finding 1's determinant is *part of the key* — partial. Finding 2's route runs *through another non-key attribute* — transitive. Telling them apart matters because each names a different repair.

### 19. B

Badges determine names, but names — which legitimately repeat — cannot determine badges. Dependency direction encodes which side is the identifier, and the two Priyas are the counterexample that kills the reverse arrow.

### 20. A

The partially dependent column leaves with its true determinant: `part_name` moves to a parts table keyed on `part_id`, storing each name once. The order-lines table keeps `qty`, which genuinely needs both halves of the key.

### 21. D

Cannot record yet: insert. Many places to fix: update. Lost with a deleted row: delete. Three failure modes, three names — and one shared cause in entangled tables.

### 22. C

3NF's addition is directness: non-key attributes must depend on the key itself, not on another non-key attribute that depends on the key. The "hitched ride" is the transitive chain.

### 23. A

One row per guide-language pair makes every value atomic and every language a first-class fact — searchable, countable, linkable. Options B and D rearrange the list without unpacking it.

### 24. B

The copy was the price tag: renaming the category now means updating every order row that carries the old text. The update anomaly is back by invitation, and managing it is the ongoing cost of the speed.

### 25. D

3NF permits `instructor_id → subject_code` because the dependent `subject_code` is prime—it appears in a candidate key. BCNF removes that exception and asks whether the determinant itself is a candidate key. `instructor_id` is not, so the relation fails BCNF.

### 26. A

`minutes_played` needs both halves (the player *in that match*): full dependency, exactly what 2NF wants. `player_name` needs only `player_id`: partial, and the source of names repeating per match.

### 27. C

The room determines its floor and its rate — two arrows out of `room_no`. The reverse `floor → room_no` fails immediately: one floor, many rooms means shared X with differing Y.

### 28. B

The forms are cumulative: a table must satisfy 1NF before it can be classified as 2NF. The container list must therefore be represented atomically before the designer proceeds to 2NF classification.

### 29. A

Three kinds of facts share one table, so each fact's lifecycle is chained to rows about the others: suppliers can't exist without shipments, supplier edits multiply across shipment rows, and deleting the last shipment evicts the supplier. Separation is the cure because entanglement is the disease.

### 30. D

The city is stored once per staff member, not once per branch — so the relocation must be applied to every BR-N row, and each missed row is a live inconsistency. The transitive chain is the update anomaly's delivery route.

### 31. C

Design 3 gives each contact its own row: atomic cells, no repeat columns, no ceilings. Designs 1, 2, and 4 are the comma list, the repeating group, and the mixed grab-bag — the catalogue of 1NF failures.

### 32. B

Denormalization in the chapter is an earned exception: normalize, measure, then reintroduce specific redundancy with a synchronization plan. Starting denormalized is simply starting with anomalies and no map of where they live.

### 33. A

Run the one test: `aircraft → hangar`, and `aircraft` alone cannot identify a roster row (it appears on many flights). Determinant, not candidate key — the table fails BCNF, and the hangar fact belongs in a table keyed on `aircraft`.

### 34. C

The database sees one opaque string rather than three independently addressable skills. Finding SQL instructors becomes error-prone text matching, counts are unreliable, and there is no single skill value to link to a certification record.

### 35. D

Data can refute a dependency but cannot prove it for every valid future row. The sample is consistent with `product_code → tax_rate`, but the dependency must come from the shop's enduring business rule, not merely three observations.

### 36. B

The name was stored once per order line, so history holds the stale text in every line ever written. One rename becomes a hunt across the order archive — the maintenance bill 2NF's split would have cancelled.

### 37. D

Write-heavy plus correctness-critical is the profile where redundancy hurts most: every copy is one more thing hundreds of writers per second can desynchronize. The chapter's pattern is to protect the core and serve reports from separate read-side structures.

### 38. C

Proposal 1 cuts the chain at its joint and preserves the join path: sensor → station → altitude survives across the two tables. Proposal 2 orphans sensors from stations; proposal 3 re-stores altitude per sensor — the original redundancy in new clothes.

### 39. B

BCNF is stricter: every BCNF relation satisfies 3NF, but a 3NF relation can fail BCNF. Question 25 demonstrates the gap because a non-key determinant determines a prime attribute.

### 40. A

The arrangement fences the redundancy: read-only, rebuilt nightly, source of truth documented and untouched. That is denormalization as the chapter teaches it — a priced, contained purchase of speed rather than a structural surrender.

---

## Question-Type Distribution

| Higher-order assessment family | Question numbers |
|---|---|
| Anomaly identification and root-cause analysis | 1, 8, 13, 21, 29 |
| Dependency reading, translation, and discrimination | 2, 9, 11, 18, 19, 26, 27, 35 |
| Violation detection over shown data | 3, 4, 5, 6, 10, 33 |
| Decomposition selection and judgment | 14, 20, 23, 31, 38 |
| Rule boundaries, rationale, and comparisons | 12, 15, 17, 22, 25, 28, 34, 39 |
| Consequence tracing | 24, 30, 36 |
| Tradeoff decisions | 7, 16, 32, 37, 40 |

## Blueprint Taxonomy Coverage

| Subtopic from the attached blueprint | Question numbers | Count |
|---|---|---:|
| Why Normalize: Anomalies | 1, 8, 13, 21, 29 | 5 |
| Functional Dependencies | 2, 9, 11, 19, 27, 35 | 6 |
| First Normal Form | 3, 10, 15, 23, 31, 34 | 6 |
| Second Normal Form | 4, 12, 20, 26, 28, 36 | 6 |
| Third Normal Form | 5, 14, 18, 22, 30, 38 | 6 |
| Boyce-Codd Normal Form | 6, 17, 25, 33, 39 | 5 |
| When to Denormalize | 7, 16, 24, 32, 37, 40 | 6 |

Questions 1–10 collectively cover all seven Topic 2.2 subtopics.

## Difficulty and Answer-Key Balance

- Foundational: 11 questions (2, 3, 10, 11, 15, 17, 19, 21, 23, 31, 34)
- Intermediate: 24 questions
- Advanced: 5 questions (6, 25, 33, 38, 40)
- Correct option A: 10 questions (2, 5, 12, 16, 20, 23, 26, 29, 33, 40)
- Correct option B: 10 questions (3, 7, 10, 14, 19, 24, 28, 32, 36, 39)
- Correct option C: 10 questions (4, 8, 11, 15, 18, 22, 27, 31, 34, 38)
- Correct option D: 10 questions (1, 6, 9, 13, 17, 21, 25, 30, 35, 37)
- Longest consecutive run of one correct letter: below 3 throughout
