# DBMS 1.4: Relational Algebra — 40 Higher-Order MCQs

## Assessment specifications

- **Subject:** DBMS
- **Topic:** Database Foundations
- **Chapter:** Relational Algebra
- **Scope:** All five Topic 1.4 subtopics in the attached course blueprint (What is Relational Algebra; Selection and Projection; Set Operations; The Join Operator; Mapping SQL to Relational Algebra)
- **Format:** Four options with exactly one best answer
- **Curriculum flag:** No
- **Design standard:** Every question explicitly identifies the database, explains what each relation represents, and defines unfamiliar fields before asking for a transformation or diagnosis.
- **Table-use standard:** Relations are shown whenever students must count rows, trace operators, test compatibility, follow join matches, or compare an expected result with an actual one.
- **Scope guard:** Only the five Topic 1.4 readings are assessed. SQL is used only for the clause-to-algebra mappings taught here; later SQL syntax and join variants are excluded.
- **Difficulty policy:** Difficulty reflects the reasoning genuinely required by each item; no fixed quota is imposed.
- **Answer-quality controls:** A/B/C/D each correct exactly 10 times, no letter correct more than twice consecutively, no correct answer identifiable by length.
- **Coverage rule:** Questions 1–10 collectively cover all five Topic 1.4 subtopics.
- **Student/instructor separation:** Questions appear first; answers and explanations follow in the instructor key.

---

## Questions

### 1. What comes out of the machine

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** What is Relational Algebra  
**Is Curriculum Based:** No  
**Assessment type:** Closure-property identification

A supply-chain database stores one row per delivery in `Shipments`; `destination` means the city receiving the shipment. An analyst applies selection to keep rows whose destination is Chennai:

| Input object | Operation | Result observed |
|---|---|---|
| `Shipments` relation | Keep rows where `destination = 'Chennai'` | Rows still arranged under the shipment columns |

In relational algebra, what is the nature of the operation's output?

A. Another relation that can feed the next operation.  
B. A plain text report that no further operation can use.  
C. A single number summarizing the matching rows.  
D. A modified version of the original `shipments`, which is destroyed.

### 2. Sigma or pi for the North sites?

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Selection and Projection  
**Is Curriculum Based:** No  
**Assessment type:** Operator selection

A solar database's `Sites` relation stores one row per power site. `site_id` identifies the site, `zone` is its operating region, and `capacity_mw` is its generating capacity in megawatts:

`sites`

| site_id | zone | capacity_mw |
|---|---|---|
| S1 | North | 12 |
| S2 | South | 20 |
| S3 | North | 8 |

The requirement: complete rows for the North-zone sites only, all columns intact.

Which operation is this?

A. Projection — π keeps matching rows.  
B. Union — the North rows are combined with themselves.  
C. Selection — σ keeps rows S1 and S3, matching `zone = 'North'`.  
D. Join — North would need to be matched against another relation first here.

### 3. Slice the menu vertically

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Selection and Projection  
**Is Curriculum Based:** No  
**Assessment type:** Projection outcome tracing

A café database's `Menu` relation stores one row per product. `item` is its name, `category` its product group, `price` its rupee price, and `calories` its energy value:

`menu`

| item | category | price | calories |
|---|---|---|---|
| Espresso | Drink | 120 | 5 |
| Croissant | Bake | 180 | 280 |
| Cold Brew | Drink | 200 | 10 |
| Brownie | Bake | 150 | 350 |

The display board needs only names and prices. What does π<sub>item, price</sub>(`menu`) produce?

A. Two rows — one per category.  
B. Four rows, each with just the `item` and `price` values.  
C. Four rows with all four columns, and prices specially highlighted.  
D. One row containing the total price.

### 4. Shapes that refuse to stack

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Set Operations  
**Is Curriculum Based:** No  
**Assessment type:** Union-compatibility judgment

An accounting database stores one row per client:

| Relation | Column meanings |
|---|---|
| `RetailClients(name, city)` | Client name and home city |
| `CorporateClients(name, city, gst_no)` | Company name, city, and tax-registration number |

The firm attempts to union the two complete relations.

What stands in the way?

A. Unions are limited to relations with identical names.  
B. The corporate relation has to contain fewer rows than the retail relation before union can run.  
C. Nothing — union pads the missing column automatically.  
D. The relations aren't union-compatible: different attribute counts.

### 5. Who gave blood only on weekdays?

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Set Operations  
**Is Curriculum Based:** No  
**Assessment type:** Difference computation

A blood-bank database keeps two one-column, union-compatible relations. Each row contains a donor's name:

`WeekdayDonors`

| name |
|---|
| Asha |
| Vikram |
| Neel |
| Divya |

`WeekendDonors`

| name |
|---|
| Neel |
| Sana |

What is `weekday_donors` − `weekend_donors`?

A. {Neel} — the donor in both.  
B. {Asha, Vikram, Divya} — weekday-only donors, absent from the weekend list.  
C. {Asha, Vikram, Neel, Divya, Sana} — everyone from both donor lists combined.  
D. {Sana} — the weekend-only donor.

### 6. Every trainer meets every slot

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** The Join Operator  
**Is Curriculum Based:** No  
**Assessment type:** Cartesian-product counting

A fitness database separately stores trainers and appointment slots. Before a join condition is applied, the Cartesian product pairs every trainer row with every slot row:

`trainers`

| trainer |
|---|
| Dev |
| Lina |
| Omar |

`time_slots`

| slot |
|---|
| 06:00 |
| 08:00 |
| 17:00 |
| 19:00 |

Before any matching condition is applied, how many paired rows does the Cartesian product contain?

A. 12 — the 3 × 4 possible trainer-slot pairs.  
B. 7 — the row counts of the two relations are added.  
C. 4 — one resulting row is produced per available time slot.  
D. 3 — one resulting row is produced per trainer.

### 7. The product, filtered into sense

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** The Join Operator  
**Is Curriculum Based:** No  
**Assessment type:** Join tracing

A street-food database stores one row per stall and one row per market zone. `zone_id` is the code connecting a stall to the zone where it operates:

`food_stalls`

| stall | zone_id |
|---|---|
| Wok Box | z1 |
| Dosa Cart | z2 |
| Grill Hut | z3 |

`zones`

| zone_id | zone_name |
|---|---|
| z1 | Riverside |
| z2 | Old Town |

What does the join on matching `zone_id` produce?

A. Six rows — every stall against every zone.  
B. Three rows — Grill Hut is retained with an empty zone name.  
C. Two rows: Wok Box with Riverside, Dosa Cart with Old Town.  
D. One row — only the first match is kept.

### 8. Translate the query into symbols

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Mapping SQL to Relational Algebra  
**Is Curriculum Based:** No  
**Assessment type:** SQL-to-algebra mapping

A logistics employee database stores one row per worker in `Employees`; `name` is the worker's name and `dept` is the department code. It runs:

```sql
SELECT name FROM employees WHERE dept = 'Ops';
```

Which algebra expression says the same thing?

A. σ<sub>name</sub>(π<sub>dept = 'Ops'</sub>(employees))  
B. employees ∪ dept  
C. π<sub>dept</sub>(σ<sub>name = 'Ops'</sub>(employees))  
D. π<sub>name</sub>(σ<sub>dept = 'Ops'</sub>(employees))

### 9. Read the chain aloud

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Mapping SQL to Relational Algebra  
**Is Curriculum Based:** No  
**Assessment type:** Algebra-to-English decoding

A film-archive database contains:

| Relation | What one row represents | Connecting field |
|---|---|---|
| `Films(title, year, studio_id)` | One film; `year` is its release year | `studio_id` identifies its studio |
| `Studios(studio_id, studio_name)` | One studio | `studio_id` |

It evaluates a join on equal `studio_id` values inside this expression:

π<sub>title</sub>(σ<sub>year > 2020</sub>(films ⋈ studios))

Which English description matches?

A. Keep only titles first, then attach studios, then filter — order is irrelevant.  
B. Combine every film with every studio, then keep only the year column.  
C. Join films to studios, keep rows newer than 2020, then keep just titles.  
D. Delete films older than 2020 from the archive permanently.

### 10. Why formality earns its keep

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** What is Relational Algebra  
**Is Curriculum Based:** No  
**Assessment type:** Purpose identification

A trainee examining a bookstore DBMS notices that two differently worded reports can be reduced to the same sequence of row, column, and relation operations. The trainee asks why that formal algebra is useful when SQL already exists.

Which answer reflects the chapter?

A. The algebra gives queries precise meaning, forming SQL's foundation.  
B. Using algebra notation guarantees that every query executes faster than its SQL form.  
C. The symbols exist only for academic examinations.  
D. SQL is being phased out in favour of raw algebra.

### 11. The clause behind the curtain

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Mapping SQL to Relational Algebra  
**Is Curriculum Based:** No  
**Assessment type:** Clause-to-operator mapping

A port database's `Arrivals` relation stores one row per ship arrival. `vessel` is the ship name, `tonnage` is its carrying measure, and `berth` is the dock position assigned to it:

```sql
SELECT vessel, tonnage FROM arrivals WHERE berth = 'B4';
```

One clause does the work of selection σ.

Which part?

A. `SELECT vessel, tonnage` — the part choosing which columns appear.  
B. `FROM arrivals` — naming the relation.  
C. The semicolon — ending the statement.  
D. `WHERE berth = 'B4'` — the row-filtering condition.

### 12. Count the survivors of sigma

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Selection and Projection  
**Is Curriculum Based:** No  
**Assessment type:** Selection tracing

A handicrafts database's `Items` relation stores one row per product; `item` is its name and `price` is its rupee selling price:

`items`

| item | price |
|---|---|
| Jute bag | 120 |
| Brass lamp | 450 |
| Silk scarf | 300 |
| Clay cup | 90 |
| Wood frame | 210 |

How many rows does σ<sub>price > 200</sub>(`items`) contain?

A. 5  
B. 3 — the lamp, scarf, and frame.  
C. 2 — only prices above 300.  
D. 0 — selection removes rows, leaving none.

### 13. The gift of closure

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** What is Relational Algebra  
**Is Curriculum Based:** No  
**Assessment type:** Property-consequence reasoning

An order database has an `Orders` relation with one row per purchase. An analyst records this pipeline:

| Step | Transformation |
|---:|---|
| 1 | Apply σ to keep orders above a chosen amount |
| 2 | Feed that result into π to retain selected columns |
| 3 | Feed the new result into a later join |

What property of the algebra makes such chains possible?

A. Union-compatibility of all relations.  
B. The fact that σ never removes any rows.  
C. Closure: each result is itself a relation, feeding the next step.  
D. The requirement that every single query use at most two total operations here.

### 14. Members of both branches

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Set Operations  
**Is Curriculum Based:** No  
**Assessment type:** Intersection computation

A bookshop database keeps one-column, union-compatible relations of members registered at two branches:

`BranchKoregaon`

| member_name |
|---|
| Meera |
| Divit |
| Sana |
| Kabir |

`BranchAundh`

| member_name |
|---|
| Sana |
| Ravi |
| Meera |

What is `branch_koregaon` ∩ `branch_aundh`?

A. {Meera, Sana} — the members appearing in both lists.  
B. {Divit, Kabir, Ravi} — members of exactly one branch.  
C. {Meera, Divit, Sana, Kabir, Ravi} — all members.  
D. {Ravi} — the newest member.

### 15. Three couriers, one hub each

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** The Join Operator  
**Is Curriculum Based:** No  
**Assessment type:** Join-cardinality tracing

A delivery database stores one row per courier and one row per hub. `hub_id` identifies the hub to which a courier is assigned.

`Couriers`

| courier | hub_id |
|---|---|
| Ravi | H1 |
| Tara | H1 |
| Zoya | H1 |
| Mohan | H2 |

`Hubs`

| hub_id | city |
|---|---|
| H1 | Pune |
| H2 | Nashik |

How many rows does the join on matching `hub_id` produce?

A. 8 — pairing every courier against every single hub.  
B. 2 — one per hub.  
C. 3 — Pune's couriers only.  
D. 4 — each courier paired once with its matching hub.

### 16. Pi's day job in SQL

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Mapping SQL to Relational Algebra  
**Is Curriculum Based:** No  
**Assessment type:** Clause-to-operator mapping

A clinic database stores patient visits. A report needs only the patient's name and visit date—not every stored column. Which part of its SQL query performs the role of projection π?

A. The `WHERE` condition, which drops rows.  
B. The column list after `SELECT`, keeping only named columns.  
C. The `JOIN` keyword, which physically merges two relations together.  
D. The table name after `FROM`.

### 17. Filter, then strip

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Selection and Projection  
**Is Curriculum Based:** No  
**Assessment type:** Combined-operation tracing

A wedding-band database's `Gigs` relation stores one row per booking; `gig` names the event and `fee` is the payment in rupees:

`gigs`

| gig | fee |
|---|---|
| Rooftop party | 8000 |
| Beach wedding | 4500 |
| Club night | 5000 |
| Trade fair | 3000 |

What does π<sub>gig</sub>(σ<sub>fee ≥ 5000</sub>(`gigs`)) return?

A. {Rooftop party, Club night}, the gigs clearing the fee bar.  
B. {Beach wedding, Trade fair} — the two gigs falling below it.  
C. All four gig names, with fees hidden.  
D. {8000, 5000} — the qualifying fees.

### 18. One order works, the other cannot

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Selection and Projection  
**Is Curriculum Based:** No  
**Assessment type:** Decomposition with ordering constraint

A podcast database uses `Shows(title, language, plays)`, where `title` is the programme name, `language` is its spoken language, and `plays` is its listening count.

| Required result |
|---|
| Titles of Hindi-language shows with more than 1,000,000 plays |

Which decomposition is correct — and why does the other order fail?

A. π<sub>title</sub> first, then σ, because `title` is the only requested output column.  
B. Either order works, because σ and π are always interchangeable.  
C. σ (filter) first, then π<sub>title</sub> — early projection discards needed columns.  
D. Union `Shows` with the filtered rows first, then apply σ to that combined relation.

### 19. What sigma never touches

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Selection and Projection  
**Is Curriculum Based:** No  
**Assessment type:** Operator-property discrimination

A payments database stores one row per payment in a six-column `Payments` relation. `amount` is the payment value in rupees. An auditor applies σ<sub>amount > 10000</sub>.

What is guaranteed about the output relation's structure?

A. It has one column — the amount.  
B. It gains a Boolean column recording whether each original row passed the test.  
C. It has fewer columns to save space.  
D. It has exactly the same six columns as the input; only surviving rows change.

### 20. Everyone who volunteered at all

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Set Operations  
**Is Curriculum Based:** No  
**Assessment type:** Union computation

A volunteer database has two union-compatible relations, each with one `volunteer_name` column:

`MorningShift`

| volunteer_name |
|---|
| Ira |
| Tom |
| Lena |

`EveningShift`

| volunteer_name |
|---|
| Tom |
| Raj |

How many names are in `morning_shift` ∪ `evening_shift`?

A. 5 — each occurrence from the two input relations remains separate.  
B. 4 — Ira, Tom, Lena, Raj; Tom counted just once.  
C. 3 — only the larger list survives.  
D. 1 — only the shared name.

### 21. Whole rows wanted, no trimming

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Selection and Projection  
**Is Curriculum Based:** No  
**Assessment type:** Requirement-to-operator mapping

A relocation database's `Clients` relation stores one row per customer:

| client_id | name | destination_city | moving_date |
|---|---|---|---|
| C1 | Ishan | Surat | 12 Aug |
| C2 | Noor | Pune | 19 Aug |
| C3 | Gita | Surat | 21 Aug |

The agency needs the complete records—all four columns—of clients moving to Surat.

Which operation plan fits?

A. Projection alone, using π<sub>city</sub>(clients) on the relation.  
B. Projection then union with the original.  
C. Selection alone, since no columns need to be dropped here.  
D. Join — the clients must be matched to Surat first.

### 22. Two thousand mostly meaningless pairs

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** The Join Operator  
**Is Curriculum Based:** No  
**Assessment type:** Rationale reasoning

A bike-share database has `Riders(rider_id, assigned_route_id)` with 50 rows and `Routes(route_id, route_name)` with 40 rows. Here, `assigned_route_id` identifies the route assigned to a rider. A join on `assigned_route_id = route_id` begins conceptually with:

| Stage | Row count | Meaning |
|---|---:|---|
| Cartesian product | 2,000 | Every rider paired with every route, including routes not assigned to that rider |

Why is the join operator described as a *filtered* Cartesian product?

A. The product supplies every pairing; the join's condition keeps only real matches.  
B. Because the join deletes the original relations after pairing.  
C. The join definition filters each relation before any row pairings are considered.  
D. Because joins are limited to 2,000 rows by definition.

### 23. Subtraction is not symmetric

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Set Operations  
**Is Curriculum Based:** No  
**Assessment type:** Direction-sensitivity analysis

A webinar database stores participant identifiers in two one-column, union-compatible relations:

`Registered`

| person_id |
|---|
| P |
| Q |
| R |

`Attended`

| person_id |
|---|
| Q |
| S |

Which statement about difference is correct?

A. `registered` − `attended` always equals `attended` − `registered`, since both use the same exact lists.  
B. Both differences are empty.  
C. `registered` − `attended` = {S}.  
D. `registered` − `attended` = {P, R}; `attended` − `registered` = {S} — direction matters.

### 24. Union's rule follows the algebra

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Mapping SQL to Relational Algebra  
**Is Curriculum Based:** No  
**Assessment type:** Requirement-correspondence reasoning

A recruitment database attempts to combine two query results:

| Result | Returned columns |
|---|---|
| Internship applicants | `(name, city)` |
| Experienced applicants | `(name, city, expected_salary)` |

The DBMS rejects the SQL `UNION`.

Which algebra concept does this SQL rule mirror?

A. Closure, since every query result must always be a relation of some kind here.  
B. Union-compatibility: the combined relations must share matching shapes.  
C. Projection — SQL unions only work on single columns.  
D. The Cartesian product — unions multiply their inputs.

### 25. Pick the hinge

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** The Join Operator  
**Is Curriculum Based:** No  
**Assessment type:** Join-condition selection

A campsite database contains:

| Relation | Field meanings |
|---|---|
| `Bookings(booking_id, vehicle_id, nights)` | One stay; `vehicle_id` identifies the arriving vehicle |
| `Vehicles(vehicle_id, owner, plate)` | One vehicle; `vehicle_id` identifies it |

Which condition correctly joins a booking to the vehicle it belongs to?

A. `bookings.booking_id = vehicles.plate`  
B. `bookings.booking_id = vehicles.vehicle_id`  
C. Matching `vehicle_id` in `bookings` with `vehicle_id` in `vehicles`.  
D. Any condition at all — joins accept all possible comparisons equally well.

### 26. The whole pipeline in one line

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Mapping SQL to Relational Algebra  
**Is Curriculum Based:** No  
**Assessment type:** SQL-to-algebra mapping with join

A market database stores one row per food stall in `Stalls`; `rating` is its review score and `zone_id` identifies its zone. `Zones` stores each zone's name. The authority runs:

```sql
SELECT z.zone_name
FROM stalls s JOIN zones z ON s.zone_id = z.zone_id
WHERE s.rating > 4;
```

Which algebra chain corresponds?

A. σ<sub>rating > 4</sub>(π<sub>zone_name</sub>(stalls ⋈ zones)) — project first, filter after.  
B. (stalls ∪ zones) − σ<sub>rating > 4</sub>  
C. π<sub>rating</sub>(σ<sub>zone_name</sub>(stalls))  
D. π<sub>zone_name</sub>((σ<sub>rating > 4</sub>(stalls)) ⋈ zones) — filter stalls, then join.

### 27. The optimizer's native tongue

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** What is Relational Algebra  
**Is Curriculum Based:** No  
**Assessment type:** Beyond-the-classroom relevance

A bookstore sends a query to its DBMS. Internally, the request is represented as a chain such as “select qualifying book rows, join their publishers, then project titles.” Long after an exam, where does relational algebra keep mattering?

A. Inside the DBMS, reasoning about queries as chains of algebra operations.  
B. It doesn't — the algebra is retired once SQL is parsed.  
C. Only in the printed documentation.  
D. Only in the storage manager, where algebra symbols determine the physical page layout.

### 28. Fewer rows, all columns — name the worker

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Selection and Projection  
**Is Curriculum Based:** No  
**Assessment type:** Result-shape diagnosis

An insurance database's `Policies` relation stores one row per policy:

| Input rows | Input columns | Output rows | Output columns |
|---:|---:|---:|---:|
| 900 | 8 | 212 | The same 8 |

Which algebra operation did the conceptual work?

A. Projection — columns were selected.  
B. Selection: rows filtered by a condition, shape fully preserved.  
C. Union — two relations were stacked.  
D. Cartesian product, because it reduces a relation to rows meeting a condition.

### 29. Rows versus columns, once and for all

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Selection and Projection  
**Is Curriculum Based:** No  
**Assessment type:** Operator-pair discrimination

A university database receives two requests against `Students`: one asks for only rows from the Physics programme; the other asks for only the `name` and `email` columns. Which pairing states the two operators correctly?

A. σ keeps the named columns; π keeps rows satisfying a condition.  
B. Both keep rows; they differ only in symbol.  
C. σ keeps matching rows; π keeps the named columns.  
D. σ sorts; π counts.

### 30. Make the shapes match, then stack

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Set Operations  
**Is Curriculum Based:** No  
**Assessment type:** Compatibility-repair planning

A design-studio database contains:

| Relation | What one row represents | Columns |
|---|---|---|
| `Interns` | One intern | `(name, dept)` |
| `Staff` | One permanent employee | `(name, dept, salary)` |

Head office needs one two-column list of every person's name and department.

Which plan produces a legal union?

A. Union them directly; the DBMS aligns the shared columns and ignores `salary`.  
B. Join the two relations on `name` instead.  
C. Take `staff` − `interns` first.  
D. Project `staff` down to (name, dept) with π, then union the two relations.

### 31. The operator in one sentence

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** The Join Operator  
**Is Curriculum Based:** No  
**Assessment type:** Definition selection

A school database keeps student names in `Students` and course registrations in `Enrollments`. Neither relation alone can show a student's name beside a course code. Which sentence describes the operator needed?

A. It stacks two union-compatible relations into one relation.  
B. It combines matching rows from two relations.  
C. It removes the rows of one relation from another.  
D. It renames a relation's columns.

### 32. Two tables walk into a query

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Mapping SQL to Relational Algebra  
**Is Curriculum Based:** No  
**Assessment type:** Clause-to-operator mapping

An orchard database has `Harvests`, one row per harvest, and `Orchards`, one row per orchard. In both relations, `orchard_id` identifies the orchard. A query includes:

```sql
FROM harvests h JOIN orchards o ON h.orchard_id = o.orchard_id
```

Which algebra operator does this SQL construction correspond to?

A. The join operator ⋈, combining the relations on their matching condition.  
B. The difference operator −, removing orchard rows represented in `harvests`.  
C. Projection π, since two names are listed.  
D. Selection σ applied to a single relation.

### 33. The vanished stall

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** The Join Operator  
**Is Curriculum Based:** No  
**Assessment type:** Missing-row diagnosis

A night-market database stores one row per stall and one row per zone. `zone_id` is the code meant to connect each stall to its location. It joins `Stalls` to `Zones` on that field:

`Stalls`

| stall | zone_id |
|---|---|
| Momo Star | z1 |
| Kulfi King | z9 |

`Zones`

| zone_id | zone_name |
|---|---|
| z1 | Lakeside |

Kulfi King is absent from the join result. Why?

A. Its name sorts last alphabetically.  
B. A join requires both input relations to contain the same number of rows.  
C. Its `zone_id` z9 has no match in `zones`, so no row forms.  
D. Joins return at most one row.

### 34. Blueprint and building

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** What is Relational Algebra  
**Is Curriculum Based:** No  
**Assessment type:** Relationship characterization

A curriculum reviewer compares two descriptions:

| Layer | Role |
|---|---|
| Relational algebra | Formal operations over relations |
| SQL | Practical structured language used to request database results |

Which characterization is accurate?

A. They are alternative practical query languages, so a database chooses one of them.  
B. SQL is the theory and algebra the practical tool.  
C. The algebra is obsolete notation for spreadsheets.  
D. The algebra is the formal foundation; SQL is the practical language built on it.

### 35. Join first, then judge the ratings

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** The Join Operator  
**Is Curriculum Based:** No  
**Assessment type:** Join-plus-selection tracing

A market database stores one row per stall and one row per zone. `zone_id` connects a stall to its location, while `rating` is the stall's review score.

`Stalls`

| stall | zone_id | rating |
|---|---|---|
| Wok Box | z1 | 4.5 |
| Dosa Cart | z2 | 3.8 |
| Grill Hut | z1 | 4.2 |

`Zones`

| zone_id | zone_name |
|---|---|
| z1 | Riverside |
| z2 | Old Town |

After joining on `zone_id` and then applying σ<sub>rating > 4.0</sub>, which stalls remain?

A. Dosa Cart only.  
B. Wok Box and Grill Hut, since both exceed the 4.0 rating bar.  
C. All three stalls.  
D. None — a selection condition must be applied before two relations are joined.

### 36. The filter that lost its column

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Selection and Projection  
**Is Curriculum Based:** No  
**Assessment type:** Invalid-chain diagnosis

A booking database uses `Gigs(gig, fee)`, where `gig` is the event name and `fee` is the payment amount. An analyst creates this intermediate relation:

| Step | Columns remaining |
|---:|---|
| Start with `Gigs` | `gig`, `fee` |
| Apply π<sub>gig</sub> | `gig` only |
| Next attempt | Apply σ<sub>fee ≥ 5000</sub> |

Why does this chain fail?

A. The projection discarded `fee`, so selection has nothing left to test.  
B. σ may never follow π in any expression.  
C. Selection cannot use the ≥ comparison.  
D. The chain works because selection can still retrieve `fee` from the original relation.

### 37. Same shape, so which tool?

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Set Operations  
**Is Curriculum Based:** No  
**Assessment type:** Operation-versus-join discrimination

Two gyms keep relations with the identical shape `(member_name, phone)`:

`EastGym`

| member_name | phone |
|---|---|
| Aria | 8011 |
| Ben | 8022 |

`WestGym`

| member_name | phone |
|---|---|
| Ben | 8022 |
| Chen | 8033 |

Head office wants the complete member rows present at both gyms.

Which operation answers the question directly?

A. A full Cartesian product computed directly from the two relations here.  
B. A projection of either relation.  
C. A union — everyone from either gym.  
D. An intersection, returning exactly the rows present in both relations.

### 38. The full phrasebook

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Mapping SQL to Relational Algebra  
**Is Curriculum Based:** No  
**Assessment type:** Correspondence-table selection

A database trainee is annotating SQL clauses with the relational-algebra work each one represents. Which mapping is correct?

A. SELECT list ↔ σ; WHERE ↔ π; UNION ↔ ⋈; JOIN ↔ ∪  
B. SELECT list ↔ ∪; WHERE ↔ ⋈; UNION ↔ σ; JOIN ↔ π  
C. SELECT list ↔ π; WHERE ↔ σ; UNION ↔ ∪; JOIN ↔ ⋈  
D. All four SQL constructs map to selection.

### 39. Dana appears twice

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** The Join Operator  
**Is Curriculum Based:** No  
**Assessment type:** Repeated-match tracing

A fitness database stores one row per scheduled session and one row per coach. `coach_id` identifies the coach leading a session.

`Sessions`

| day | coach_id |
|---|---|
| Mon | c1 |
| Tue | c1 |
| Wed | c2 |

`Coaches`

| coach_id | name |
|---|---|
| c1 | Dana |
| c2 | Louis |

After joining on `coach_id`, how many rows carry the name Dana, and why?

A. One — a coach may join at most once.  
B. Two — each of Dana's two sessions forms its own combined row.  
C. Three — Dana joins to every session.  
D. Zero — repeated `coach_id` values in `Sessions` prevent those rows from matching.

### 40. Choose the chain that answers the brief

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Mapping SQL to Relational Algebra  
**Is Curriculum Based:** No  
**Assessment type:** Integrated decomposition

A ferry database contains:

`Sailings`

| sailing_id | route | vessel_id |
|---|---|---|
| S1 | Harbor | V2 |
| S2 | Island | V1 |
| S3 | Harbor | V1 |

`Vessels`

| vessel_id | vessel_name |
|---|---|
| V1 | Sea Fern |
| V2 | Blue Arc |

Here, `vessel_id` identifies the vessel assigned to a sailing. The authority needs only the vessel names used on the Harbor route.

Which chain answers it?

A. π<sub>vessel_name</sub>(σ<sub>route = 'Harbor'</sub>(sailings ⋈ vessels)).  
B. σ<sub>vessel_name</sub>(π<sub>route</sub>(sailings)), claiming no join is needed here.  
C. sailings ∪ vessels, then σ<sub>route = 'Harbor'</sub>.  
D. π<sub>route</sub>(σ<sub>vessel_name = 'Harbor'</sub>(vessels)).

---

## Instructor Key

### 1. A

Closure is the algebra's defining convenience: operations consume relations and yield relations. The filtered shipments are themselves a relation, immediately usable by the next operation in a chain.

### 2. C

The request keeps *rows* (North sites) and all columns — selection's exact job, written σ<sub>zone = 'North'</sub>. Projection (A's claim) works on columns, not rows.

### 3. B

Projection is the vertical slice: all four rows survive, but each is reduced to the two named columns. Nothing about π drops or merges rows here — it drops columns.

### 4. D

Union demands union-compatible inputs: the same number of attributes with corresponding domains. These complete relations have two versus three columns; for the requested name-and-city list, the corporate relation could first be projected to those two columns.

### 5. B

Difference keeps rows of the first relation absent from the second. Neel appears in both, so he is removed; Asha, Vikram, and Divya remain. Option A is the intersection; option C the union.

### 6. A

The Cartesian product pairs every row of one relation with every row of the other: 3 × 4 = 12. This inflated intermediate is the conceptual starting point that a join's matching condition then prunes.

### 7. C

The join keeps only combined rows where `zone_id` matches on both sides: Wok Box–Riverside and Dosa Cart–Old Town. Grill Hut's z3 matches nothing in `zones`, so it contributes no row — joins do not invent blank partners (B).

### 8. D

`WHERE dept = 'Ops'` is the selection σ<sub>dept = 'Ops'</sub>, and `SELECT name` is the projection π<sub>name</sub> around it. Option A swaps the operators' roles; option C swaps the column and the condition.

### 9. C

Reading inside-out: the join builds film–studio rows, the selection keeps those newer than 2020, the projection reduces the survivors to titles. Option A's "order is irrelevant" fails because projecting titles first would delete the year the filter needs.

### 10. A

The algebra's value is precision and foundation: it defines exactly what each operation means, which is both what SQL's semantics rest on and what lets a database treat a query as a rearrangeable chain of operations.

### 11. D

Row filtering by condition is σ's role, and `WHERE berth = 'B4'` is that condition. The column list is π; the FROM clause names the input relation.

### 12. B

Testing each price against 200: 450, 300, and 210 pass; 120 and 90 fail. Selection keeps the three matching rows whole.

### 13. C

The chain works because every intermediate result is a full-fledged relation — the closure property. Without it, σ's output might be some other kind of object that π could not accept.

### 14. A

Intersection returns rows present in both relations: Meera and Sana. Option B instead lists members who occur in exactly one of the two relations, not in both.

### 15. D

A join pairs each courier row with the hub row satisfying the condition—exactly one hub for each courier here. Four couriers therefore produce four combined rows, with H1 appearing in three. Option A is the unfiltered product.

### 16. B

Choosing which columns survive is projection, and in SQL that is the column list after `SELECT`. WHERE plays σ's part.

### 17. A

The selection keeps Rooftop party (8000) and Club night (5000 — the ≥ bar includes the boundary), then projection reduces those rows to their names. Option D keeps the wrong column.

### 18. C

The filter examines `language` and `plays`, so it must run while those columns still exist. Projecting only `title` first removes both fields, making σ-then-π the workable order for this brief.

### 19. D

Selection is shape-preserving: it evaluates a condition per row and keeps or discards whole rows. The six-column structure passes through untouched; changing columns is π's business.

### 20. B

Union merges the lists and eliminates duplicates: Ira, Tom, Lena, Raj. Tom volunteered twice but is one person — and one row — in the result.

### 21. C

"All columns, some rows" is pure selection. Adding a projection would either do nothing (project everything) or violate the "every column" requirement — so the correct plan needs no π at all.

### 22. A

The product enumerates all possible pairings with no judgment; the join's condition is the judgment. "Filtered Cartesian product" captures exactly that two-step idea: generate every pair conceptually, keep the pairs that belong.

### 23. D

Difference asks "in the first but not the second," so the operands' order changes the question: no-shows versus walk-ins. The computed sets {P, R} and {S} demonstrate the asymmetry concretely.

### 24. B

SQL's matching-column rule for UNION is union-compatibility wearing SQL syntax: relations (or SELECT lists) being stacked must agree in shape. The rejection is the algebra's requirement, enforced.

### 25. C

The link between the relations is the shared `vehicle_id` — bookings store it precisely to point at the vehicle. Joining on unrelated columns (A, B) would pair rows by coincidence rather than by connection.

### 26. D

The selection first keeps only stalls rated above 4, the join then attaches each survivor's zone, and the final projection keeps `zone_name`. Option A projects away `rating` before trying to test it, so its outer selection cannot be evaluated.

### 27. A

The algebra gives the DBMS a precise vocabulary for representing a query as familiar operations and comparing possible ways to carry them out. It therefore remains useful inside query planning rather than disappearing once the SQL is received.

### 28. B

Rows reduced, shape intact is selection's fingerprint. Projection would have narrowed the columns; union and product would have grown the row count.

### 29. C

The one-line summary is that σ filters rows by a condition while π keeps named columns. Option A reverses those two responsibilities.

### 30. D

Union needs matching shapes, and projection is the tool that creates them: π<sub>name, dept</sub>(staff) has the same two attributes as `interns`, making the union legal. Option A assumes the database repairs shapes silently — it refuses instead.

### 31. B

A join combines rows across two relations under a matching condition. Option A describes union; option C, difference; option D, renaming.

### 32. A

`JOIN ... ON` is SQL's surface for ⋈: combine the two relations, keep combinations satisfying the ON condition.

### 33. C

This join keeps only row pairs whose `zone_id` values match. Kulfi King's z9 has no partner in `Zones`, so no combined row can be formed for it.

### 34. D

The algebra is the small, precise foundation; SQL is the practical language layered over it. Every SQL query in the chapter can be read as a composition of σ, π, ∪, −, ∩, and ⋈ — which is what makes the mapping lessons possible at all.

### 35. B

The join attaches zone names, then the selection tests ratings: Wok Box (4.5) and Grill Hut (4.2) pass; Dosa Cart (3.8) fails. Both survivors happen to be Riverside stalls.

### 36. A

After π<sub>gig</sub>, the intermediate relation has one column: `gig`. The σ that follows references `fee`, an attribute that no longer exists — the chain is illegal, and the repair is to filter before projecting.

### 37. D

Same shape, and the question is "present in both" — the definition of intersection. A join is unnecessary machinery here, and the union (C) answers "either," not "both."

### 38. C

The chapter's correspondence: column list ↔ π, WHERE ↔ σ, UNION ↔ ∪, JOIN ↔ ⋈. Each SQL construct is an algebra operation in practical clothing.

### 39. B

Each session row joins to the coach row its `coach_id` matches. Dana's ID appears on two session rows, so she appears in two combined rows — repetition in the result reflects repetition in the referencing relation, not an error.

### 40. A

The route lives in `Sailings`, while the names live in `Vessels`, so the relations must be joined on `vessel_id`. Selection keeps S1 and S3, and projection returns `{Blue Arc, Sea Fern}`. The other options either discard a needed field or never connect the relations.

---

## Question-Type Distribution

| Higher-order assessment family | Question numbers |
|---|---|
| Operation tracing over shown data | 3, 5, 7, 12, 14, 15, 17, 20, 23, 35, 39 |
| Operator and requirement mapping | 2, 8, 11, 16, 21, 25, 26, 28, 32, 37, 38 |
| Property and rationale reasoning | 1, 10, 13, 19, 22, 27, 34 |
| Compatibility and ordering diagnosis | 4, 18, 24, 30, 33, 36 |
| Counting and cardinality prediction | 6, 15, 20 |
| Integrated decomposition | 9, 29, 31, 40 |

## Blueprint Taxonomy Coverage

| Subtopic from the attached blueprint | Question numbers | Count |
|---|---|---:|
| What is Relational Algebra | 1, 10, 13, 27, 34 | 5 |
| Selection and Projection | 2, 3, 12, 17–19, 21, 28, 29, 36 | 10 |
| Set Operations | 4, 5, 14, 20, 23, 30, 37 | 7 |
| The Join Operator | 6, 7, 15, 22, 25, 31, 33, 35, 39 | 9 |
| Mapping SQL to Relational Algebra | 8, 9, 11, 16, 24, 26, 32, 38, 40 | 9 |

Questions 1–10 collectively cover all five Topic 1.4 subtopics.

## Difficulty and Answer-Key Balance

- Foundational: 12 questions (1, 3, 6, 10, 12, 15, 16, 20, 27, 29, 31, 38)
- Intermediate: 28 questions (2, 4, 5, 7–9, 11, 13, 14, 17–19, 21–26, 28, 30, 32–37, 39, 40)
- Advanced: 0 questions
- Correct option A: 10 questions (1, 6, 10, 14, 17, 22, 27, 32, 36, 40)
- Correct option B: 10 questions (3, 5, 12, 16, 20, 24, 28, 31, 35, 39)
- Correct option C: 10 questions (2, 7, 9, 13, 18, 21, 25, 29, 33, 38)
- Correct option D: 10 questions (4, 8, 11, 15, 19, 23, 26, 30, 34, 37)
- Longest consecutive run of one correct letter: below 3 throughout
