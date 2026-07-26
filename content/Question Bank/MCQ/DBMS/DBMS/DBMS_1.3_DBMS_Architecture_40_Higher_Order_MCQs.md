# DBMS 1.3: DBMS Architecture — 40 Higher-Order MCQs

## Assessment specifications

- **Subject:** DBMS
- **Topic:** Database Foundations
- **Chapter:** DBMS Architecture
- **Scope:** All five Topic 1.3 subtopics in the attached course blueprint (Three-Schema Architecture; Data Independence; Components of a DBMS; The System Catalog; How a Query Travels)
- **Format:** Four options with exactly one best answer
- **Curriculum flag:** No
- **Design standard:** Every question explicitly identifies the database setting, explains what named tables or fields represent, and states the architectural event being evaluated. A student encountering this item among questions from several programming languages can still recognize it immediately as DBMS reasoning.
- **Table-use standard:** Architecture snapshots, catalog records, query logs, before-and-after states, and responsibility maps are shown as tables wherever they make the evidence easier to trace.
- **Scope guard:** Questions use only the five ideas taught in Topic 1.3. SQL appears only as a request travelling through the DBMS; writing SQL and later transaction theory are not assessed.
- **Difficulty policy:** Difficulty reflects the reasoning genuinely required by the question. No artificial quota is imposed.
- **Answer-quality controls:** A/B/C/D each correct exactly 10 times, no letter correct more than twice consecutively, no correct answer identifiable by length.
- **Coverage rule:** Questions 1–10 collectively cover all five Topic 1.3 subtopics.
- **Student/instructor separation:** Questions appear first; answers and explanations follow in the instructor key.

---

## Questions

### 1. Three descriptions of one billing database

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Three-Schema Architecture  
**Is Curriculum Based:** No  
**Assessment type:** Level-mapping selection

A telecom billing database stores subscriber accounts and their mobile plans. Its architecture document contains:

| Description | What it means in this database |
|---|---|
| 1 | The retention team's screen shows only a subscriber's phone number and plan name |
| 2 | The full design lists all tables, columns, and relationships |
| 3 | The storage document lists data files, indexes, and disk blocks |

Which mapping to the three-schema architecture is correct?

A. 1: internal, 2: external, 3: conceptual  
B. 1: external, 2: conceptual, 3: internal  
C. 1: conceptual, 2: internal, 3: external  
D. All three are the conceptual level, described three times

### 2. Faster disks, silent applications

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Data Independence  
**Is Curriculum Based:** No  
**Assessment type:** Change classification

A logistics database stores one row per parcel in `Parcels`; `parcel_id` identifies a parcel and `destination` records where it is going. A DBA makes these changes:

| Changed inside the DBMS | Left unchanged |
|---|---|
| Parcel files move to faster SSD storage | The `Parcels` columns and relationships |
| An index is added for locating `parcel_id` | Every application's database request |

All applications continue working.

Which principle made that possible?

A. Logical data independence, since the schema absorbed a brand-new column.  
B. The system catalog — metadata prevented the apps from noticing.  
C. Physical data independence: storage changes stay invisible above it.  
D. External schemas — each app was quietly rewritten by its view.

### 3. Rush hour at the checkout

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Components of a DBMS  
**Is Curriculum Based:** No  
**Assessment type:** Component-role identification

An online shop's `Stock` database table stores one row per product. `product_id` identifies the product, while `units_available` records how many can still be sold.

| Concurrent event | Required database outcome |
|---|---|
| Hundreds of shoppers try to buy the final units of product 81 | Successful purchases must not produce a negative count or overwrite one another |

Which DBMS component owns this coordination problem?

A. The query processor, which parses each purchase's SQL  
B. The storage manager, which physically reads the stock page from disk  
C. The system catalog, which lists the stock table's columns  
D. The transaction manager, which keeps simultaneous changes correct

### 4. Who knows whether `loyalty_points` exists?

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** The System Catalog  
**Is Curriculum Based:** No  
**Assessment type:** Metadata-source identification

A supermarket database has a `Customers` table with one row per shopper. A report requests `loyalty_points`, meaning the number of reward points held by a customer. Before reading customer rows, the DBMS must establish:

| Metadata question | Example answer it needs |
|---|---|
| Does `loyalty_points` exist in `Customers`? | Yes or no |
| What kind of value may it hold? | For example, a whole number |

Where does it look?

A. In the system catalog, the database's own metadata store.  
B. In the first data row of the table, which lists the column names.  
C. In the application's source code.  
D. In the operating system's file names.

### 5. Put the journey in order

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** How a Query Travels  
**Is Curriculum Based:** No  
**Assessment type:** Sequence reconstruction

A college portal asks its results database for the marks belonging to one roll number. The monitoring log captured five events out of order:

| Event number | Logged event |
|---:|---|
| 1 | The result set is returned to the portal |
| 2 | The plan is executed against stored marks |
| 3 | The request arrives as plain SQL text |
| 4 | A plan is chosen from possible retrieval methods |
| 5 | The SQL is parsed and its names are checked against the catalog |

Which order is correct?

A. 3 → 4 → 5 → 2 → 1  
B. 5 → 3 → 4 → 2 → 1  
C. 3 → 5 → 2 → 4 → 1  
D. 3 → 5 → 4 → 2 → 1

### 6. Two teams, two windows, one truth

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Three-Schema Architecture  
**Is Curriculum Based:** No  
**Assessment type:** Purpose-of-views reasoning

An airline database stores passengers, flights, bookings, fares, seats, and baggage in one shared conceptual design.

| User group | Fields its screen displays |
|---|---|
| Check-in agents | Passenger name, seat, baggage allowance |
| Revenue analysts | Fare class, price paid, route |

What is the architectural purpose of giving each team its own external view?

A. To store each team's data completely separately so the copies can differ.  
B. Each group gets a tailored, simplified slice of one shared database.  
C. To prevent the conceptual schema from ever changing.  
D. To let each team choose its own storage hardware.

### 7. The error that never touched the disk

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** How a Query Travels  
**Is Curriculum Based:** No  
**Assessment type:** Stalled-stage diagnosis

A ticketing database contains an `Orders` table, with one row per ticket purchase. A developer mistypes the table name:

| Submitted request | Immediate DBMS response | Data rows read |
|---|---|---:|
| `SELECT * FROM ordrs;` | `relation "ordrs" does not exist` | 0 |

At which stage did the journey stop?

A. Plan execution, where the disk read apparently failed halfway through.  
B. Result return — the rows were lost in transit.  
C. Parsing and checking: the catalog had no table called `ordrs`.  
D. Plan choice — no plan exists for small tables.

### 8. A new column nobody noticed

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Data Independence  
**Is Curriculum Based:** No  
**Assessment type:** Change classification

A streaming database stores one row per customer in `Subscribers`. The field `preferred_language` means the language the customer wants the interface to use.

| Before the change | After the change |
|---|---|
| `Subscribers` has name and amount due | `preferred_language` is added |
| Billing report reads only name and amount due | The same report still reads only those two fields and runs unchanged |

Which principle protected the old report?

A. Logical data independence: the schema grew, views stayed unaffected.  
B. Physical data independence, since the disk layout stayed exactly the same.  
C. The transaction manager — it locked the report against changes.  
D. Query optimization — the plan skipped the new column for speed.

### 9. The component behind the grinding disk

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Components of a DBMS  
**Is Curriculum Based:** No  
**Assessment type:** Symptom-to-component mapping

A freight database stores one row per shipment. During a shipment report, its DBMS monitor records:

| Activity | Share of observed time |
|---|---:|
| Parsing and planning the request | 4% |
| Moving shipment data pages between disk and memory | 91% |
| Returning the result | 5% |

Which component performs that page traffic?

A. The query processor — it fetches pages while parsing.  
B. The storage manager, since moving data on disk is its job.  
C. The system catalog, where metadata lookups read every single page.  
D. The external schema — views control disk access.

### 10. The catalog's own storage format

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** The System Catalog  
**Is Curriculum Based:** No  
**Assessment type:** Self-description insight

A hospital DBMS can display this description of its own `Patients` table:

| Recorded fact | Example |
|---|---|
| Table name | `Patients` |
| Column definition | `patient_id` is a whole-number identifier |
| Permission | The admissions role may add rows |

How is this system-catalog information represented inside the DBMS?

A. As a printed manual that ships alongside the installed software.  
B. As comments inside each application's code.  
C. As encrypted files no query can ever reach.  
D. As tables: the catalog is itself data the DBMS can query.

### 11. Scan it, or jump straight to it?

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** How a Query Travels  
**Is Curriculum Based:** No  
**Assessment type:** Stage-responsibility identification

A courier database's `Parcels` table stores one row per delivery; `parcel_no` is the tracking identifier printed on a parcel. For the request `SELECT * FROM parcels WHERE parcel_no = 'PX-981'`, two routes are available:

| Candidate route | Work described |
|---|---|
| Full read | Check parcel rows one by one |
| Index route | Use the `parcel_no` index to locate the matching row |

Which stage of the query's journey makes that decision?

A. Plan choice — the system weighs the possible strategies and picks one.  
B. Parsing — the syntax check selects the fastest grammar.  
C. Result return, where the client picks whichever answer arrives first now.  
D. The external schema — views always force index use.

### 12. Hide the salary, touch one level

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Three-Schema Architecture  
**Is Curriculum Based:** No  
**Assessment type:** Change placement

An HR database stores one row per employee. `salary` means the employee's pay amount.

| User | Current view | Required view |
|---|---|---|
| Team lead | Name, department, salary | Name and department only |
| Payroll officer | Name, department, salary | No change |

The stored employee data must remain unchanged.

At which level does this change belong?

A. Internal — encrypt the salary blocks on disk.  
B. Conceptual: delete the entire salary column from the schema itself.  
C. External: adjust the team leads' view so it omits the column.  
D. All three levels must change together.

### 13. The change no layer can hide

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Data Independence  
**Is Curriculum Based:** No  
**Assessment type:** Boundary-of-protection reasoning

A banking database stores one row per account. `account_status` tells applications whether the account is active, frozen, or closed. The team proposes:

| Change | Existing application dependency |
|---|---|
| Move account rows to another disk array | Apps never refer to disk locations |
| Add an index on account number | Apps request accounts without naming indexes |
| Add an optional `nickname` column | Existing apps do not request it |
| Remove `account_status` | Existing apps read it on every login |

Which change will break running applications despite the architecture?

A. Moving the entire transactions table to a different disk array.  
B. Adding an index on the account number.  
C. Adding a new optional column to the accounts table.  
D. Dropping the `account_status` column apps read constantly.

### 14. The component that reads your intentions

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Components of a DBMS  
**Is Curriculum Based:** No  
**Assessment type:** Component-role identification

A travel database's `Stays` table has one row per hotel stay. `hotel` is the hotel name, `nightly_rate` is its price per night, and `city` is its location. The DBMS receives:

```sql
SELECT hotel, nightly_rate FROM stays WHERE city = 'Jaipur';
```

| Required internal work before rows are fetched |
|---|
| Check the request's grammar |
| Resolve the table and column names |
| Prepare a sensible retrieval plan |

Which component does this?

A. The storage manager  
B. The query processor  
C. The transaction manager  
D. The backup scheduler

### 15. What the catalog actually lists

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** The System Catalog  
**Is Curriculum Based:** No  
**Assessment type:** Content discrimination

A gaming database has a `Players` table with one row per player; `player_id` identifies a player and `handle` is the public screen name. Its DBA compares four possible catalog records.

Which kind of entry belongs there?

A. "Table `players` has columns `player_id` and `handle`."  
B. "Player 88 logged in from Pune at 09:14."  
C. "The marketing team prefers charts in blue."  
D. "Yesterday's tournament winner was, once again, team Volt."

### 16. What actually arrives at the door

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** How a Query Travels  
**Is Curriculum Based:** No  
**Assessment type:** Journey-start identification

A weather database stores readings reported by monitoring stations. An analytics application asks this DBMS for today's temperature readings.

What does the DBMS actually receive at step one of the journey?

A. A finished result set for redistribution.  
B. A pre-chosen execution plan built by the app.  
C. Plain SQL text stating what data is wanted.  
D. A copy of the app's source code.

### 17. Why bother with layers at all?

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Three-Schema Architecture  
**Is Curriculum Based:** No  
**Assessment type:** Rationale selection

A port database supports a harbourmaster's vessel screen, a shared design of vessels and berths, and physical files on storage. A junior engineer proposes connecting the screen directly to those disk files and removing the three-level separation.

Which answer captures the architectural motive?

A. Three levels triple the storage capacity.  
B. Separation lets each level change without forcing rewrites elsewhere.  
C. Regulations formally require three copies of every design document filed.  
D. Each level holds a backup of the level above it.

### 18. Same query, suddenly faster

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** How a Query Travels  
**Is Curriculum Based:** No  
**Assessment type:** Behaviour explanation

A courier database's `Parcels` table stores one row per shipment; `tracking_no` is the code customers use to locate a parcel.

| Time | SQL sent by the application | Available storage route | Response |
|---|---|---|---|
| Monday | Same tracking request | Read many parcel rows | Slow |
| Tuesday | Same tracking request | New `tracking_no` index available | Fast |

What explains the change?

A. The SQL text was somehow rewritten automatically inside the app itself.  
B. The catalog deleted the slow table.  
C. The result set was cached permanently the night before.  
D. The plan-choice stage now selects the index strategy automatically.

### 19. File the change under the right heading

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Data Independence  
**Is Curriculum Based:** No  
**Assessment type:** Physical-or-logical classification

A grain-trading database stores one row per trade. `trade_date` records when the deal occurred.

| Changed | Unchanged |
|---|---|
| Physical organization: unordered trade file becomes date-organized storage | Tables, columns, relationships, screens, and requests |

How is this change classified?

A. A physical-level change, shielded by physical data independence.  
B. A logical-level change, since dates are considered core business data.  
C. An external-level change, since reports show dates.  
D. A catalog change, since sorting rewrites metadata.

### 20. Three components, three duties

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Components of a DBMS  
**Is Curriculum Based:** No  
**Assessment type:** Duty matching

A railway booking database receives many requests for seats. Its internal duties are:

| Duty number | Work inside the DBMS |
|---:|---|
| 1 | Understand and prepare to answer SQL |
| 2 | Move data between disk and memory |
| 3 | Keep simultaneous seat changes from corrupting one another |

Which assignment is correct?

A. 1: storage manager, 2: transaction manager, 3: query processor  
B. 1: transaction manager, 2: query processor, 3: storage manager  
C. 1: query processor, 2: storage manager, 3: transaction manager  
D. All three duties belong to the storage manager

### 21. What the parser verifies before moving on

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** How a Query Travels  
**Is Curriculum Based:** No  
**Assessment type:** Stage-detail tracing

A film-festival database's `Screenings` table stores one row per scheduled film. `title` is the film name and `hall_id` identifies the hall showing it. The DBMS receives:

```sql
SELECT title FROM screenings WHERE hall_id = 7;
```

Its log says that parsing and the catalog check completed successfully.

What did the DBMS necessarily confirm, using the catalog, before this step could pass?

A. That hall 7 currently has seats available.  
B. That the query will return at least one row.  
C. That the disk blocks for `screenings` are stored physically contiguous.  
D. That `screenings` exists and that `title`, `hall_id` are real columns.

### 22. The morning the catalog was corrupted

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** The System Catalog  
**Is Curriculum Based:** No  
**Assessment type:** Counterfactual dependency analysis

A brewery database still has intact rows describing batches and ingredients, but its catalog records have become unreadable:

| Catalog fact the DBMS can no longer retrieve | Example |
|---|---|
| Table names | Whether `Batches` exists |
| Column definitions | Whether `batch_id` belongs to `Batches` |
| Rules and permissions | Which values and users are allowed |

Why can normal query processing no longer proceed reliably?

A. Without metadata, the DBMS cannot validate queries or resolve names.  
B. The data tables are always fully encrypted with the catalog as the key.  
C. The catalog physically contains all the row data.  
D. It is not unusable — queries simply run without any checking.

### 23. Two transfers collide

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Components of a DBMS  
**Is Curriculum Based:** No  
**Assessment type:** Component-role identification

A coffee-chain database stores each customer's reward balance. Two checkout terminals try to update customer 71's points at the same time:

| Terminal | Concurrent operation |
|---|---|
| A | Redeem 50 points |
| B | Add 20 points from a purchase |

Both changes must be coordinated so one does not silently overwrite the other.

Which component owns that coordination?

A. The query processor itself  
B. The transaction manager  
C. The external schema layer  
D. The report generator tool

### 24. One table becomes two, and nobody screams

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Data Independence  
**Is Curriculum Based:** No  
**Assessment type:** Change classification

A marketplace database originally stores seller identity and payment details in one `Sellers` table.

| Conceptual design before | Conceptual design after | Existing seller app |
|---|---|---|
| One `Sellers` table | `Sellers` plus `SellerBankDetails` and a relationship between them | Continues to see its original fields through an unchanged view |

Which principle is demonstrated?

A. Physical data independence, simply because two tables now use two files.  
B. Catalog independence, because metadata doubled.  
C. Logical data independence, since the schema was reorganized quietly.  
D. Plan independence, because the optimizer chose new plans.

### 25. Who does what for one SELECT

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Components of a DBMS  
**Is Curriculum Based:** No  
**Assessment type:** Cooperation-sequence reasoning

A bus-fleet database stores vehicles and scheduled journeys. An application requests the journeys assigned to bus 19.

| Phase | Needed work |
|---|---|
| Before execution | Understand the request and choose a retrieval plan |
| During execution | Bring the required database pages from storage |

Which description of component cooperation is accurate?

A. The query processor settles on a plan; the storage manager then fetches pages.  
B. The storage manager parses the SQL, then the query processor reads the disk.  
C. The transaction manager parses the SQL and also reads all pages itself.  
D. Each component executes the full query independently, and the fastest answer wins.

### 26. The plan meets the platters

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** How a Query Travels  
**Is Curriculum Based:** No  
**Assessment type:** Stage-outcome identification

An auction database stores one row per item for sale; `lot_no` is the identifier printed in the catalogue. Its chosen plan says:

| Planned operation | Meaning |
|---|---|
| Use the index on `lot_no` | Locate the requested lot |
| Fetch matching rows | Read the stored item data |
| Keep the requested columns | Shape the answer requested by the client |

What happens at step four — execution — and what does it produce?

A. The plan is translated back into SQL for the client to run.  
B. The catalog is rebuilt to match the plan.  
C. The plan is compared once more against other candidate plans, one final time.  
D. The plan's operations run against stored data, producing the actual rows.

### 27. Metadata or data?

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** The System Catalog  
**Is Curriculum Based:** No  
**Assessment type:** Content discrimination

A florist database has a `Customers` table, where `customer_id` identifies a customer. Compare:

| Statement | Fact |
|---:|---|
| 1 | "`Customers` has 8 columns, and `customer_id` is its primary key." |
| 2 | "Customer 14 lives in Pune and ordered lilies twice." |

Which statement describes catalog content?

A. Statement 2, since the catalog apparently stores customer facts too.  
B. Both equally, since the catalog apparently stores everything here.  
C. Statement 1, holding facts about structure, not the data.  
D. Neither — catalogs store only user passwords.

### 28. What lives at the bottom level

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Three-Schema Architecture  
**Is Curriculum Based:** No  
**Assessment type:** Level-content identification

A shipping registry database stores vessels, owners, and harbour visits. A DBA must document the internal level—not the harbourmaster's screen or the shared business design.

Which concerns belong in that document?

A. Which columns the harbourmaster's screen displays.  
B. File organization, indexes, and how rows sit in disk blocks.  
C. The precise business meaning of the `vessel_class` attribute itself.  
D. Which analysts may see the owners' contact details.

### 29. The homemade engine that loses updates

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Components of a DBMS  
**Is Curriculum Based:** No  
**Assessment type:** Missing-component diagnosis

A startup's homemade database engine can already parse requests and read or write stored files. Its test results show:

| Test | Result |
|---|---|
| One user changes a value | Correct |
| Two users change the same value at once | One update silently overwrites the other |

Which standard DBMS component is their engine missing?

A. A transaction manager, since nothing coordinates simultaneous writes.  
B. A storage manager — files clearly cannot be read.  
C. A query processor — the SQL was never parsed.  
D. An external schema, since views would somehow prevent all overwrites here.

### 30. Where the journey ends

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** How a Query Travels  
**Is Curriculum Based:** No  
**Assessment type:** Final-stage identification

An energy-trading application asks its database for today's completed trades. The trace shows:

| Stage | Status |
|---|---|
| SQL arrival | Complete |
| Parsing and catalog check | Complete |
| Plan choice | Complete |
| Plan execution | Complete; matching rows assembled |

What is the fifth and final step of the journey?

A. The DBMS emails the DBA a summary of the run.  
B. The plan is archived into the catalog for reuse.  
C. The app's original view definition somehow gets updated with the new answer.  
D. The assembled result set is returned to the client application that asked.

### 31. The two shields, side by side

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Data Independence  
**Is Curriculum Based:** No  
**Assessment type:** Definition pairing

A university database team considers two maintenance events:

| Event | What applications should not need to know |
|---|---|
| Student-record files are reorganized and indexed | New disk layout |
| An optional `preferred_name` column is added | A field unused by existing views |

Which pairing states the two forms of data independence correctly?

A. Physical: apps survive schema deletions; logical: apps survive disk failures.  
B. Physical: no change is ever allowed to storage; logical: no change is ever allowed to the schema.  
C. Physical shields apps from storage changes; logical shields views from schema growth.  
D. Both terms mean the database is backed up twice.

### 32. The tool that lists your tables

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** The System Catalog  
**Is Curriculum Based:** No  
**Assessment type:** Mechanism explanation

A robotics database stores robots, maintenance visits, and replacement parts. A developer selects “list all tables” in its administration tool and receives:

| Returned names |
|---|
| `Robots` |
| `MaintenanceVisits` |
| `Parts` |

Where does the tool get that list?

A. It scans every single data file on disk and guesses table boundaries.  
B. It queries the system catalog, whose own tables hold this metadata.  
C. It asks the most recently connected user.  
D. It reads through the application's own configuration files instead.

### 33. Route the request to the right level

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Three-Schema Architecture  
**Is Curriculum Based:** No  
**Assessment type:** Change routing

A ride-sharing database contains drivers, riders, and trips. Three requests arrive:

| Request | Meaning |
|---:|---|
| 1 | Remove unused fields from the dispatcher's screen only |
| 2 | Add carpooling, so the shared database design needs a new relationship between trips and multiple riders |
| 3 | Increase physical archive capacity because its disk is nearly full |

Where does request 2 belong?

A. The conceptual level, adding entities and relationships to the design.  
B. The external level — a new screen will suffice.  
C. The internal level — buy a bigger disk.  
D. No level at all — new relationships cannot ever be added after the launch.

### 34. What CREATE TABLE really writes

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** The System Catalog  
**Is Curriculum Based:** No  
**Assessment type:** Side-effect identification

A vineyard DBA creates an empty `Harvests` table. One row will eventually represent one grape harvest; `harvest_id` will identify it and `harvest_date` will record when it occurred.

| Immediately after creation | Count |
|---|---:|
| Harvest data rows | 0 |
| Defined columns | 2 |

What did the DBMS record the moment the table was created?

A. One blank data row is inserted, so the table is not empty.  
B. Nothing at all — records only begin once the very first insert eventually happens.  
C. A full backup of the database.  
D. New catalog entries describing the table's name, columns, and types.

### 35. Count the schemas

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Three-Schema Architecture  
**Is Curriculum Based:** No  
**Assessment type:** Cardinality reasoning

A stock-exchange database has one shared design of traders, orders, and trades and one physical storage organization. Its users need different screens:

| User group | Tailored information |
|---|---|
| Trader | Own orders and trades |
| Compliance officer | Audit details |
| Market analyst | Aggregated market activity |

Which statement about schema counts in the three-schema architecture is correct?

A. Many separate conceptual schemas, one external view, many internal layouts.  
B. One of each, always — one screen for all users.  
C. One conceptual schema, one internal schema, but many external views.  
D. The counts must all be equal.

### 36. Fetching what the plan demands

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Components of a DBMS  
**Is Curriculum Based:** No  
**Assessment type:** Component-interaction tracing

A museum database stores one row per admission ticket. During execution of a request for ticket `M-481`, the trace shows:

| Plan request | Physical action needed |
|---|---|
| Consult ticket index | Read index pages |
| Retrieve ticket `M-481` | Read the referenced data page |

Which interaction is taking place?

A. The catalog is executing the plan itself.  
B. The executing query calls the storage manager to fetch pages from disk.  
C. The transaction manager fetches all the pages, bypassing every other component.  
D. The client application reads the disk directly.

### 37. Same SQL, new plan next year

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** How a Query Travels  
**Is Curriculum Based:** No  
**Assessment type:** Plan-variability explanation

A food-delivery database's `Restaurants` table grows while the application request remains unchanged:

| Time | Rows | Available index | Plan chosen |
|---|---:|---|---|
| Launch | 200 | None | Read the table |
| One year later | 200,000 | Restaurant-location index | Use the index |

Why can the plan differ while the SQL stays identical?

A. The SQL text secretly changes as tables grow.  
B. Plans are fixed forever at the first execution.  
C. The catalog rewrites queries when tables pass 100,000 rows.  
D. SQL states *what* is wanted, not *how* it's fetched.

### 38. A database that can describe itself

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** The System Catalog  
**Is Curriculum Based:** No  
**Assessment type:** Purpose identification

A school database catalog records that `Students` exists, `roll_no` is required, and the registrar role may add rows. Why must the DBMS keep metadata like this about itself?

A. To have something to print in error messages.  
B. Because regulations formally require every database to keep detailed diaries.  
C. To validate queries and enforce constraints against known structure.  
D. To slow queries down enough to be auditable.

### 39. Independence is not a speed guarantee

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Data Independence  
**Is Curriculum Based:** No  
**Assessment type:** Scope-of-promise correction

An advertising database is physically reorganized:

| Observation after the change | Result |
|---|---|
| Application code modified | No |
| Reports still return correct rows | Yes |
| One report's running time | Doubled |

An analyst concludes, “Physical data independence failed.”

Which correction is accurate?

A. The analyst is entirely right — independence guarantees fully identical run times.  
B. Independence promises apps keep *working*, not that performance stays identical.  
C. The report must be reading the old disk.  
D. Independence only applies to queries written after the change.

### 40. Two queries, two fates, one architecture

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** How a Query Travels  
**Is Curriculum Based:** No  
**Assessment type:** Integrated journey reasoning

A print-on-demand database stores one row per order. `order_status` records whether an order is queued, printing, or shipped.

| Request | DBMS observation |
|---|---|
| X asks for misspelled `order_stats` | Instant “column does not exist”; zero rows read |
| Y asks for real `order_status` | Valid; 4,000 rows returned after a pause |

Which account of the two journeys is correct?

A. X died at step two, caught by the catalog check before any data was touched.  
B. Both queries reached execution; X's rows were simply lost.  
C. X failed at result-return; Y skipped planning because it was valid.  
D. X was rejected by the storage manager, which checks spelling during disk reads.

---

## Instructor Key

### 1. B

The retention team's tailored screen is an external view; the complete design is the conceptual schema; files, indexes, and blocks are the internal level. The three levels describe the same database at different distances from the disk.

### 2. C

Both changes — new hardware placement and a new index — live at the internal level. Physical data independence means such storage decisions need not force changes to the conceptual design or application requests.

### 3. D

Simultaneous updates that must not lose or corrupt each other are the transaction manager's territory. The query processor and storage manager each touch every purchase too, but coordinating concurrent correctness is not their duty.

### 4. A

Metadata about what exists — tables, columns, types — lives in the system catalog, which is consulted during parsing before any data page is read. Data rows (B) hold values, not schema definitions.

### 5. D

Arrival of SQL text, parsing and catalog checking, plan choice, execution, and result return — in that order. Option A plans before checking, which would mean optimizing queries that might reference nonexistent tables.

### 6. B

External views are windows, not copies: each team sees the slice it needs, everything stays consistent underneath, and neither team is burdened with the other's detail. Option A describes exactly the duplication the architecture avoids.

### 7. C

The instant failure and its wording are the fingerprints of step two: the parser asked the catalog for `ordrs`, found nothing, and ended the journey before planning or disk access. A typo never gets far enough to touch data.

### 8. A

The conceptual schema changed by gaining a column, but the old report did not depend on that field. Logical data independence allows that unaffected external view to continue working.

### 9. B

Moving pages between disk and memory is the storage manager's defining job. The query processor decides *what* to fetch; the storage manager does the fetching.

### 10. D

The catalog is stored as tables — data about data, queryable with the same machinery as everything else. That self-description is what lets tools list tables and parsers verify names.

### 11. A

Choosing between a full read and an index jump is exactly the plan-choice stage: the system weighs alternatives and commits to a strategy before execution begins.

### 12. C

The requirement is about what one user group sees, with data and schema unchanged — the definition of an external-level change. Deleting the column (B) would break payroll, which still needs it.

### 13. D

Independence shields applications from storage changes and from schema *growth* — but removing a column that applications actively read takes away something they depend on. No layer can hide an amputation.

### 14. B

Grammar checking, name resolution, and preparing an answer strategy are the query processor's job — the component that turns SQL text into something the system can act on.

### 15. A

The catalog holds structural facts: tables, columns, types, keys, constraints. Login events and tournament results are ordinary data rows in ordinary tables; team preferences (C) are not database content at all.

### 16. C

The journey begins with plain SQL — a declaration of *what* is wanted. Plans (B) are built inside the DBMS at step three, never shipped in by the client.

### 17. B

The layers exist to decouple change: screens can be redesigned, the schema extended, storage reorganized — each without dragging the others along. That absorption of change is the payoff for the layering.

### 18. D

SQL describes the goal, and the plan-choice stage picks the method. With a new index available, the same goal now has a faster method, so the unedited query benefits — declarative language plus re-planning is the whole mechanism.

### 19. A

Heap versus sorted file organization is squarely an internal-level concern. Physical data independence is why the platform's applications need never learn the file was reorganized.

### 20. C

The query processor understands, the storage manager moves data, the transaction manager protects concurrent correctness — the chapter's three-component division of labour.

### 21. D

Step two validates existence and sense: the table is real, the columns belong to it, and the comparison is type-coherent — all answered from the catalog. Whether rows will match (B) is knowable only after execution.

### 22. A

Every stage of every query leans on the catalog: name resolution, type checking, constraint enforcement. Intact data without its metadata is a library with the index burned — the books exist, but the system can no longer find or interpret them.

### 23. B

Both terminals are changing the same stored balance concurrently. Coordinating those operations so neither silently overwrites the other is the transaction manager's responsibility; parsing and file access alone cannot protect the result.

### 24. C

The conceptual schema was reorganized while external views preserved the shape applications expect. Surviving schema reorganization — not just storage moves — is the logical form of independence.

### 25. A

The components cooperate in sequence: understanding and planning first (query processor), then page retrieval on demand as the plan runs (storage manager). They are stations on one assembly line, not competitors (D).

### 26. D

Execution is where the chosen plan finally touches stored data: index consulted, rows fetched, columns projected. Its product is the actual answer — the rows — which step five then delivers.

### 27. C

"Eight columns, this primary key" is structure — catalog material. Where customer 14 lives is content, stored in the table itself. The catalog describes the container, not the contents.

### 28. B

The internal level is the storage story: file organization, indexes, block layout. Screens belong to the external level, attribute meaning to the conceptual, and permissions to access control.

### 29. A

Parsing and file I/O are present — what's absent is coordination of simultaneous work. Silent mutual overwriting is the textbook symptom of running without a transaction manager.

### 30. D

The journey ends where it began, at the client: the assembled result set travels back to the application that asked.

### 31. C

Physical independence shields applications from storage-level change; logical independence shields unaffected views from conceptual-schema growth. Option A swaps the two; option B mistakes independence for immutability.

### 32. B

The catalog is queryable data, and "list all tables" is simply a query against it. That is the practical payoff of the catalog being tables rather than a sealed internal file.

### 33. A

A new kind of entity and relationship reshapes the overall design of the database — conceptual-level work. The screen complaint routes to the external level and the full disk to the internal level, which is what makes request 2's placement distinctive.

### 34. D

Creating a table is a metadata event: the catalog gains entries describing the new structure. Data rows arrive later; the structure exists the moment the catalog says so.

### 35. C

The architecture has one shared truth (conceptual), one storage story (internal), and as many tailored windows (external) as user groups need. The many-ness lives only at the top.

### 36. B

Execution consumes pages, and page retrieval is the storage manager's service: index pages first, then the data pages the index pointed to, all staged into memory for the plan to use.

### 37. D

The request fixes the answer wanted, not the physical route used to retrieve it. The plan-choice stage may select a different route as tables grow and indexes appear, so identical SQL can legitimately travel differently later.

### 38. C

Self-knowledge is operational, not decorative: without knowing its own tables, columns, types, and rules, the DBMS could not validate a single query or enforce a single constraint.

### 39. B

Physical data independence is a compatibility promise, not a promise of identical running time: applications continue to work unmodified, which is exactly what happened. Performance after reorganization is a separate concern.

### 40. A

X's misspelled column was caught by the catalog check at step two — no plan, no disk access, instant failure. Y traversed all five steps: checked, planned, executed against storage, and its 4,000 rows returned as the result set. The pause lives in steps three and four.

---

## Question-Type Distribution

| Higher-order assessment family | Question numbers |
|---|---|
| Level and change classification | 1, 2, 8, 12, 19, 24, 28, 33 |
| Component-role and symptom mapping | 3, 9, 14, 20, 23, 25, 29, 36 |
| Catalog content and dependency reasoning | 4, 10, 15, 22, 27, 32, 34, 38 |
| Journey sequencing and stage tracing | 5, 7, 11, 16, 18, 21, 26, 30, 37, 40 |
| Rationale, cardinality, and scope-of-promise judgment | 6, 13, 17, 31, 35, 39 |

## Blueprint Taxonomy Coverage

| Subtopic from the attached blueprint | Question numbers | Count |
|---|---|---:|
| Three-Schema Architecture | 1, 6, 12, 17, 28, 33, 35 | 7 |
| Data Independence | 2, 8, 13, 19, 24, 31, 39 | 7 |
| Components of a DBMS | 3, 9, 14, 20, 23, 25, 29, 36 | 8 |
| The System Catalog | 4, 10, 15, 22, 27, 32, 34, 38 | 8 |
| How a Query Travels | 5, 7, 11, 16, 18, 21, 26, 30, 37, 40 | 10 |

Questions 1–10 collectively cover all five Topic 1.3 subtopics.

## Difficulty and Answer-Key Balance

- Foundational: 11 questions (1, 4, 10, 16, 20, 23, 27, 30, 31, 34, 38)
- Intermediate: 28 questions (2, 3, 5–9, 11–15, 17–19, 21, 24–26, 28–29, 32–33, 35–37, 39–40)
- Advanced: 1 question (22)
- Correct option A: 10 questions (4, 8, 11, 15, 19, 22, 25, 29, 33, 40)
- Correct option B: 10 questions (1, 6, 9, 14, 17, 23, 28, 32, 36, 39)
- Correct option C: 10 questions (2, 7, 12, 16, 20, 24, 27, 31, 35, 38)
- Correct option D: 10 questions (3, 5, 10, 13, 18, 21, 26, 30, 34, 37)
- Longest consecutive run of one correct letter: below 3 throughout
