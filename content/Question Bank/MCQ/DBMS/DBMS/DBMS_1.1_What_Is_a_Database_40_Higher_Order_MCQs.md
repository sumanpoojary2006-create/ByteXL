# DBMS 1.1: What is a Database? — 40 Higher-Order MCQs

## Assessment specifications

- **Subject:** DBMS
- **Topic:** Database Foundations
- **Chapter:** What is a Database?
- **Scope:** All eight Topic 1.1 subtopics in the attached course blueprint
- **Format:** Four options with exactly one best answer
- **Curriculum flag:** No
- **Design standard:** Every question is self-contained. Students inspect sample records, comparison tables, file states, timelines, workload descriptions, or application evidence rather than answering isolated definition statements.
- **Table-use standard:** Tables are included wherever row-by-row or side-by-side evidence materially improves reasoning. SQL-writing questions are intentionally excluded because SQL syntax is not taught in Topic 1.1.
- **Difficulty policy:** Difficulty is assigned from the reasoning genuinely required by each question; no predetermined difficulty quota is imposed.
- **Answer-quality controls:** A/B/C/D each correct exactly 10 times, no letter correct more than twice consecutively, no correct answer identifiable by length.
- **Coverage rule:** Questions 1–10 collectively cover all eight Topic 1.1 subtopics.
- **Student/instructor separation:** Questions appear first; answers and explanations follow in the instructor key.

---

## Questions

### 1. Same number, two displays

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** What is Data? Data vs. Information  
**Is Curriculum Based:** No  
**Assessment type:** Context-dependent classification

A container port's monitoring system produces two displays from the same reading:

| Display | Content |
|---|---|
| Raw feed | `81` |
| Supervisor dashboard | `Crane C-4 load: 81% of rated capacity` |

Why does only the second display qualify as information?

A. The dashboard changed the number, and changed numbers count as information.  
B. Both are information, because both originated from a real sensor.  
C. Context — the crane, the metric, the scale — makes the value actionable.  
D. Neither is information until the value is written into a database.

### 2. Three spreadsheets, two fees

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** The Problem with Files  
**Is Curriculum Based:** No  
**Assessment type:** Root-cause diagnosis

A talent agency stores performer fees in three separate spreadsheets. After a fee revision for one performer, an audit finds:

| File | Fee recorded for Rhea Kapoor |
|---|---|
| bookings.xlsx | 45,000 |
| contracts.xlsx | 45,000 |
| payouts.xlsx | 52,000 |

Which diagnosis fits this evidence most precisely?

A. Redundant copies of one fact have diverged because the update reached only one file.  
B. A lost update erased the revised fee from two of the files.  
C. Spreadsheets cannot reliably store numeric values.  
D. Nothing is wrong; the value held by two of the three files is automatically authoritative.

### 3. Name the two halves of one deployment

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** What is a Database? What is a DBMS?  
**Is Curriculum Based:** No  
**Assessment type:** Exact-mapping selection

A hotel deployment inventory contains:

| Inventory item | Observation |
|---|---|
| MySQL service | Installed software that starts, stops, reads, and protects records |
| Reservations | 1.2 million organized booking records |
| Guest profiles | 40,000 organized customer records |
| Rate data | Stored prices for room types and dates |

Which mapping correctly classifies the inventory?

A. MySQL itself is the database, while the reservation rows make up the DBMS entirely.  
B. Both terms describe the same physical server hardware, nothing more.  
C. The reservation rows become the DBMS whenever someone queries them.  
D. The reservations, profiles, and rates are the database; MySQL is the DBMS.

### 4. Two apps, one underlying guarantee

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Where Databases Live: Real Apps You Already Use  
**Is Curriculum Based:** No  
**Assessment type:** Cross-scenario pattern recognition

Two product teams record their non-negotiable rule:

| Application | Concurrent event | State that must remain valid |
|---|---|---|
| Concert ticketing | Two buyers tap “pay” for seat 14C | At most one confirmed owner |
| Mobile wallet | A transfer debits the sender | The merchant receives the matching credit |

Which database capability do both requirements depend on?

A. Serving every user a private copy of the seat map or balance.  
B. Coordinating simultaneous changes to keep shared state valid.  
C. Blocking all reads whenever any other user is connected.  
D. Storing a private seat map or balance on each buyer's own phone.

### 5. Records that refuse to share a shape

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Types of Databases  
**Is Curriculum Based:** No  
**Assessment type:** Model-selection judgment

An agritech platform samples records arriving in one collection:

| Record source | Fields present |
|---|---|
| Soil probe | `probe_id`, `moisture_pct`, `ph` |
| Survey drone | `drone_id`, `altitude_m`, `image_url`, `gps_track` |
| Weather mast | `mast_id`, `wind_speed`, `rainfall`, `battery_health` |

All are legitimate, and new device types with new fields arrive every season. Which storage model fits most naturally?

A. A document database, since one collection may hold varying fields.  
B. One relational table in which every single record must fill every column.  
C. A key-value store, meant only for expiring login sessions.  
D. A separate spreadsheet copied manually for each device type.

### 6. Three people, three relationships to one platform

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Who Uses a Database: End Users, Developers, and Administrators  
**Is Curriculum Based:** No  
**Assessment type:** Role classification

At a video-streaming company, an activity log shows:

| Person | Activity |
|---|---|
| A | Writes the database request behind “Continue Watching” |
| B | Restores last night's failed backup |
| C | Scrolls through a watchlist in the customer app |

Which assignment of roles is correct?

A. A: DBA, B: developer, C: end user  
B. A: end user, B: DBA, C: developer  
C. A: developer, B: end user, C: DBA  
D. A: developer, B: DBA, C: end user

### 7. One booking record, four dated events

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** The Lifecycle of Data: From Creation to Query to Deletion  
**Is Curriculum Based:** No  
**Assessment type:** Lifecycle-sequence trace

A freight booking record accumulates this history:

| Date | Event |
|---|---|
| 3 Jan | Record inserted when the booking is placed |
| 3 Jan – 20 Feb | Status read roughly 40 times by tracking pages |
| 9 Jan | Delivery address corrected |
| 20 Feb (+2 years) | Moved to low-cost cold storage per retention policy |

Which lifecycle sequence matches those events?

A. Creation → update → query → deletion  
B. Query → creation → update → archival  
C. Creation → query → update → archival  
D. Creation → query → archival → update

### 8. Why this model opens the course

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Why Relational Databases First: Tables, SQL, and the Industry Standard  
**Is Curriculum Based:** No  
**Assessment type:** Evidence-based justification

A curriculum reviewer challenges the syllabus: "Document and key-value stores are everywhere now — why do learners still start with relational databases?"

Which reply best matches the course material?

A. Relational engines are claimed to outperform every alternative on every possible workload.  
B. Tables and SQL recur across products and industries, forming a transferable skill.  
C. Non-relational models cannot hold data with business value.  
D. Learning SQL removes the need to understand how data is structured.

### 9. Two saves, one survivor

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** The Problem with Files  
**Is Curriculum Based:** No  
**Assessment type:** Final-state prediction

A dock-crew roster lives in one shared file; the drive keeps only the last complete file saved.

| Time | Action |
|---|---|
| 10:00 | Asha opens roster version 7 |
| 10:05 | Farhan also opens version 7 |
| 10:20 | Asha saves, having added Bay 2 |
| 10:25 | Farhan saves, having added Bay 5 |

What does the roster contain after 10:25?

A. Both bays, because the edits touched different rows.  
B. Bay 2 only, because Asha saved first.  
C. Both bays, because the drive merges simultaneous saves into version 8.  
D. Bay 5 but not Bay 2 — Farhan's copy, saved last, replaced Asha's work.

### 10. A token that points at exactly one thing

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Types of Databases  
**Is Curriculum Based:** No  
**Assessment type:** Requirement-to-model mapping

A game server documents one workload:

| Known input | Required response | Cross-session analysis needed? | Daily volume |
|---|---|---|---:|
| Login token `tok_9f3a` | Its one linked session object | No | Millions |

Which model matches that access pattern?

A. A key-value store, where the token maps straight to its value.  
B. A relational design built around relationships this lookup never uses.  
C. A document store, chosen only because tokens eventually expire.  
D. A spreadsheet sorted by token length.

### 11. Give the freezer reading a job to do

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** What is Data? Data vs. Information  
**Is Curriculum Based:** No  
**Assessment type:** Missing-context completion

A cold-chain dashboard currently shows:

| Device | Current display | Unit shown? | Safe-range context shown? |
|---|---:|---|---|
| Logger attached to Freezer F2 | `-18` | No | No |

The depot manager must decide whether any action is needed.

Which addition turns the value into decision-ready information?

A. Logging `-18` a second time, unlabeled, into a backup file.  
B. "Freezer F2: −18 °C; alarm threshold −15 °C."  
C. Rounding the value to −20 as an extra safety margin before logging it.  
D. Displaying `-18` in bold red without any label or explanation.

### 12. The smallest fix for four disagreeing price lists

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** The Problem with Files  
**Is Curriculum Based:** No  
**Assessment type:** Smallest-correct-repair selection

Four regional sales offices each keep their own copy of the parts price list. This month's audit of part PX-11:

| Office | Price on file |
|---|---|
| North, East | 320 |
| South, West | 285 |

Price corrections are routinely missing some offices. Which change addresses the root failure?

A. Email every price change to all four offices each Friday by hand.  
B. Add a fifth master copy kept on an offline drive.  
C. Forbid price changes after a list is first published.  
D. Replace the four copies with one shared, managed price list.

### 13. Maintenance night

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** What is a Database? What is a DBMS?  
**Is Curriculum Based:** No  
**Assessment type:** Counterfactual reasoning

During a planned maintenance window, the operations log reads:

| Component | State |
|---|---|
| Insurer's DBMS process | Stopped for two hours |
| Server disks | Powered and intact |
| Stored policy records | No deletion or overwrite performed |

What is true during those two hours?

A. The database is erased each time the managing process exits.  
B. Queries keep succeeding, since the disk can answer them unassisted.  
C. The database stays on disk; only the managing software is down.  
D. The data silently reverts to its state at the last backup.

### 14. The request the prototype cannot survive

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Types of Databases  
**Is Curriculum Based:** No  
**Assessment type:** Requirement that exposes a defect

A regional airline's prototype supports:

| Existing operation | Example |
|---|---|
| Retrieve by known key | `AI402 → 17 seats left` |
| Replace value by known key | `AI402 → 16 seats left` |
| Remove by known key | Delete cancelled flight `AI402` |

Which incoming requirement most clearly exposes the design's limitation?

A. "Show average seats remaining per route and aircraft type."  
B. "Read one flight's count whenever the flight number is already known."  
C. "Overwrite a flight's count after each booking."  
D. "Remove a cancelled flight's entry."

### 15. Checking a refund without writing a query

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Who Uses a Database: End Users, Developers, and Administrators  
**Is Curriculum Based:** No  
**Assessment type:** Role classification

An interaction trace shows:

| Actor | Action | Directly saw database internals? |
|---|---|---|
| Theatre-goer | Opened the app and tapped “Refund status” | No |
| Ticketing app | Displayed “Processed on 12 May” | Not applicable |

Which relationship to the database did they just demonstrate?

A. Developer, because tapping the button issued a query underneath.  
B. End user, reaching the database only through the application.  
C. DBA, because refund records are administrative data.  
D. Vendor engineer, tuning the storage engine.

### 16. Fourteen months old, still not disposable

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** The Lifecycle of Data: From Creation to Query to Deletion  
**Is Curriculum Based:** No  
**Assessment type:** Archive-versus-delete judgment

A payments processor reviews one record:

| Record age | Required retention | Possible future use | Current activity |
|---:|---:|---|---|
| 14 months | 7 years | Chargeback evidence | Rarely accessed |

Which lifecycle decision is appropriate now?

A. Delete it right away to reclaim a little storage space.  
B. Plan to re-create it later from staff memory if a dispute ever arrives.  
C. Retain it in archival storage, since policy and disputes may need it.  
D. Overwrite it with the newest transaction to keep the table small.

### 17. Thirty careful dispatchers

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** The Problem with Files  
**Is Curriculum Based:** No  
**Assessment type:** Scalability argument analysis

A trucking coordinator proposes this operating plan:

| Design fact | Proposed safeguard |
|---|---|
| Thirty dispatchers | Everyone promises not to edit simultaneously |
| Several scheduling spreadsheets | Everyone promises to update every copy |
| Shared deadlines | No software coordination is added |

Which evaluation of the proposal is most defensible?

A. The promises eliminate simultaneous saves in practice.  
B. The plan removes redundancy, since everyone edits identical values.  
C. Written rules give shared files the practical equivalent of transaction support.  
D. Human discipline cannot manage concurrency or guarantee copies update.

### 18. What actually changed between the two screens

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** What is Data? Data vs. Information  
**Is Curriculum Based:** No  
**Assessment type:** Before-and-after interpretation

A wind-farm team compares two display versions:

| Version | Display |
|---|---|
| Before | `230` |
| After | `Turbine T7 output: 230 kW at 14:00` |

What transformed the value's usefulness?

A. The number itself was silently converted into monitoring software.  
B. Context attached an identity, a unit, and a time to the raw value.  
C. Being stored twice — once per screen — made it information.  
D. The kilowatt unit changed the underlying numeric value.

### 19. What the disks alone were never doing

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** What is a Database? What is a DBMS?  
**Is Curriculum Based:** No  
**Assessment type:** Capability-boundary selection

A courier company's before-and-after inventory is:

| Before | Added layer |
|---|---|
| Organized parcel data stored on disk | DBMS software placed between applications and the data |

What is the DBMS adding?

A. Software managing organized data: access, coordination, retrieval.  
B. A guarantee that staff will never ever enter an incorrect value into it.  
C. A rule making every record visible to every employee.  
D. A second copy of every file under a new name.

### 20. A registry that cannot afford loose shapes

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Types of Databases  
**Is Curriculum Based:** No  
**Assessment type:** Multi-constraint model selection

A national land registry lists its requirements:

| Requirement | Evidence |
|---|---|
| Consistent shape | Every plot, owner, and transfer record has fixed mandatory fields |
| Connected reporting | Reports follow plots to owners and transfer history |
| Correctness | Inconsistencies can have legal consequences |

Which choice do these constraints support?

A. A key-value store, keyed by plot number and nothing else.  
B. Free-form documents, so each office can invent its own custom fields.  
C. A relational database, fitting uniform, connected records.  
D. One spreadsheet per village with no links between them.

### 21. Agreement today, and what it hides

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** The Problem with Files  
**Is Curriculum Based:** No  
**Assessment type:** Causal-chain analysis

A caterer's audit shows:

| File | Supplier address |
|---|---|
| `menus.xlsx` | 14 Mill Road |
| `orders.xlsx` | 14 Mill Road |
| `invoices.xlsx` | 14 Mill Road |

Which statement describes the present condition?

A. Inconsistency already exists, simply because three files exist.  
B. A lost update has already occurred silently, unnoticed by anyone.  
C. The agreement proves manual coordination remains reliable at any scale.  
D. Redundancy exists now; inconsistency is the risk if one copy changes.

### 22. Fuzzy search and the restore drill

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Who Uses a Database: End Users, Developers, and Administrators  
**Is Curriculum Based:** No  
**Assessment type:** Responsibility comparison

At a job portal, the work log shows:

| Specialist | Task |
|---|---|
| P | Implements search that treats “Bangalore” as a match for “Bengaluru” |
| Q | Runs a quarterly drill proving last night's backup can be restored |

Which comparison is accurate?

A. The DBA writes the fuzzy-search rules; the developer runs the restores.  
B. The developer shapes app behaviour; the DBA safeguards recoverability.  
C. Both tasks belong only to end users, since users benefit from either.  
D. The tasks are interchangeable because both touch the database.

### 23. Which action only looks?

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** The Lifecycle of Data: From Creation to Query to Deletion  
**Is Curriculum Based:** No  
**Assessment type:** Lifecycle-stage discrimination

A parcel's record currently holds status `shipped`. Four later events are proposed:

| Event | Description |
|---|---|
| 1 | Support changes the delivery address |
| 2 | Depot changes the status to `out for delivery` |
| 3 | Buyer opens the tracking page and reads `shipped` |
| 4 | System moves the completed record to an archive |

Which of these events is a query rather than a change to the record?

A. Support edits the delivery address again before the next scan.  
B. The depot flips the status to `out for delivery`.  
C. The buyer opens the tracking page and reads the status.  
D. The system moves the completed record into the archive.

### 24. Three hundred phantom steps versus one wrong serial

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Where Databases Live: Real Apps You Already Use  
**Is Curriculum Based:** No  
**Assessment type:** Risk-sensitive comparison

An incident review compares:

| Application | Incorrect stored fact | Plausible consequence |
|---|---|---|
| Smartwatch | 300 extra steps | Misleading personal total |
| Aviation maintenance | Wrong replacement-part serial | Invalid maintenance history and possible grounding |

Why must database design treat the second error as far more severe?

A. A wrong part record can ground a plane; a step miscount costs nothing.  
B. Smartwatches do not really store data.  
C. Aviation data becomes information automatically, so errors spread faster.  
D. High stakes permit the DBMS to skip validation for speed.

### 25. Modern is not a requirement

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Types of Databases  
**Is Curriculum Based:** No  
**Assessment type:** Design-critique selection

A payroll team's decision sheet contains:

| Evidence | Observation |
|---|---|
| Record shape | Identical mandatory fields for every employee |
| Workload | Cross-record finance reports every cycle |
| Stated reason for document storage | “JSON is modern” |

Which critique is strongest?

A. Document stores are incapable of holding numbers.  
B. Payroll data must never be stored digitally.  
C. JSON is entirely and permanently prohibited in all regulated financial software.  
D. The records are uniform and the reporting is relational, not document-shaped.

### 26. The one-time code with nothing left to do

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** The Lifecycle of Data: From Creation to Query to Deletion  
**Is Curriculum Based:** No  
**Assessment type:** Lifecycle-policy application

A food-delivery app's login code `882431` expired ten minutes after issue, must never be accepted again, and carries no audit requirement.

Which final lifecycle decision fits?

A. Keep it sitting untouched in the active lookup set forever.  
B. Update it into a fresh code for the next customer.  
C. Delete it under policy, since no purpose remains.  
D. Archive it in three separate systems for safety.

### 27. Mornings coding, afternoons checking backups

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Who Uses a Database: End Users, Developers, and Administrators  
**Is Curriculum Based:** No  
**Assessment type:** Multi-role interpretation

Leena's daily task log at a two-person startup is:

| Time | Task |
|---|---|
| Morning | Writes database requests used by the ordering application |
| Afternoon | Verifies that database backups completed |

Which interpretation is correct?

A. Leena is only an end user, since she works through a computer.  
B. One person is acting as both developer and administrator.  
C. Database roles must, by definition, belong to three different employees.  
D. Verifying backups converts Leena into a database vendor.

### 28. Migration is not amnesia

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** What is a Database? What is a DBMS?  
**Is Curriculum Based:** No  
**Assessment type:** Misconception correction

An insurance manager blocks a planned move from PostgreSQL to MySQL, arguing: "Changing the DBMS means our policy data becomes unrelated data — we'd be starting from nothing."

Which correction is accurate?

A. The manager is right: switching products always deletes the stored data.  
B. The two terms are marketing synonyms, so no migration is ever needed.  
C. The data must be laboriously re-entered from the original paper forms.  
D. The database is the content and can migrate; the DBMS is replaceable.

### 29. What the rider actually sees

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Where Databases Live: Real Apps You Already Use  
**Is Curriculum Based:** No  
**Assessment type:** Layered-system reasoning

A request passes through these stages:

| Stage | Action |
|---|---|
| 1 | Customer taps “Where is my order?” |
| 2 | Application sends a request |
| 3 | DBMS retrieves the stored courier position |
| 4 | Application draws the position on a map |

Which layer is the customer's direct experience?

A. The formatted application screen.  
B. The physical files holding the position data.  
C. The DBMS's internal coordination machinery.  
D. The administrator's monitoring console.

### 30. Update in place, or insert a stranger

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** The Lifecycle of Data: From Creation to Query to Deletion  
**Is Curriculum Based:** No  
**Assessment type:** Implementation comparison

Two builds handle the same parcel:

| Build | State before | Handling of status change |
|---|---|---|
| A | Parcel 88: `at depot` | Changes Parcel 88 to `on vehicle` |
| B | Parcel 88: `at depot` | Adds a new, unlinked record containing `on vehicle` |

Which review conclusion is correct?

A. The builds are equivalent, since the newest status exists somewhere in both.  
B. Build B is better, because inserting is always safer than updating.  
C. Build A keeps one record's lifecycle intact; Build B fragments it.  
D. Neither works, because records can never change after creation.

### 31. Design the experiment that catches the thief

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** The Problem with Files  
**Is Curriculum Based:** No  
**Assessment type:** Defect-exposing scenario selection

A quantity-surveying team suspects their shared costing sheet silently loses edits when two estimators work at once.

Which test most directly exposes the suspected defect?

A. Have one estimator open and close the file without editing.  
B. Have two estimators edit the file apart, then save one after the other.  
C. Rename the shared file and compare before-and-after file sizes.  
D. Enter the same rate into three different cells, then reopen the shared file.

### 32. Four workloads, one relational fit

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Types of Databases  
**Is Curriculum Based:** No  
**Assessment type:** Workload classification

Four storage needs land on an architect's desk:

| Workload | Dominant shape or access pattern |
|---|---|
| Invoicing | Customers, orders, and payments remain connected |
| Session cache | One object fetched by a known random token |
| Crash reports | Fields vary across device models |
| Page counter | One running number |

Which one most clearly calls for a relational database?

A. Invoicing, where customers, orders, and payments stay linked together.  
B. Caching one session object per random login token.  
C. Storing crash-report blobs whose fields differ across every device model type.  
D. Keeping a single running counter of page hits.

### 33. Proof that the skill travels

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Why Relational Databases First: Tables, SQL, and the Industry Standard  
**Is Curriculum Based:** No  
**Assessment type:** Evidence-selection judgment

A career mentor claims relational skills will follow a developer between employers and industries.

Which observation is the strongest evidence for that claim?

A. Every firm runs the exact same version of one particular database product.  
B. SQL never requires learning what the data means.  
C. Openings across logistics, gaming, and finance repeatedly ask for SQL.  
D. Relational tables never require design decisions.

### 34. The KYC record's busiest verb

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** The Lifecycle of Data: From Creation to Query to Deletion  
**Is Curriculum Based:** No  
**Assessment type:** Lifecycle-frequency reasoning

A bank estimates one KYC record's lifecycle activity:

| Lifecycle action | Approximate frequency |
|---|---:|
| Create | Once |
| Read | Every login and large transfer |
| Update | About twice |
| Archive | Once when the account closes |

Which operation dominates this record's working life?

A. Creation, repeated at every login.  
B. Deletion, performed after each read.  
C. Update, because every read operation modifies the row.  
D. Query, since it is read far more often than changed.

### 35. Why one correction became three tasks

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** The Problem with Files  
**Is Curriculum Based:** No  
**Assessment type:** Causal-property identification

When a venue changes its loading-dock entrance, an events company must edit `venues.xlsx`, `logistics.xlsx`, and `crew_notes.xlsx` — and a missed edit means crews drive to the wrong gate.

What property of the file approach created this triple workload?

A. Files are structurally unable to store the same value twice.  
B. Duplicating one fact across files multiplies the work of change.  
C. Spreadsheets recalculate their formulas too slowly for busy logistics teams.  
D. The address was too long to fit in a single file.

### 36. Five silent nights

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Who Uses a Database: End Users, Developers, and Administrators  
**Is Curriculum Based:** No  
**Assessment type:** Role-responsibility analysis

A marketplace operations report shows:

| Check | Result |
|---|---|
| Customer-facing site | Running normally |
| Nightly database backup | Failed for five consecutive nights |
| Recovery protection | Shrinking each night |

Someone must detect this and restore the backup process before the luck runs out.

Whose responsibility is this most directly?

A. The DBA, since backups are their remit.  
B. The most recent shopper on the site.  
C. The designer who originally chose the checkout button's colour.  
D. The courier who delivered the last order.

### 37. Three services, one decision rule

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Types of Databases  
**Is Curriculum Based:** No  
**Assessment type:** Comparative model evaluation

A media company compares three services:

| Service | Data characteristic |
|---|---|
| Subscriber billing | Uniform, connected subscribers, invoices, and payments |
| Device layout cache | Known device key returns one layout value |
| Episode metadata | Fields vary by production |

Which decision rule should guide all three choices?

A. Standardize all three on whichever engine is newest.  
B. Pick whichever product the current intern already knows.  
C. Use relational storage for all three, regardless of shape or access pattern.  
D. Match each service's shape and access pattern to a model that fits it.

### 38. First does not mean only

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Why Relational Databases First: Tables, SQL, and the Industry Standard  
**Is Curriculum Based:** No  
**Assessment type:** Limitation-aware judgment

Midway through the course, a learner concludes: "Relational databases are taught first, so every real system I ever build must use one."

Which correction best reflects the course?

A. The learner is entirely right: every production system must be relational.  
B. Relational databases should be abandoned once SQL is learned.  
C. Relational is the starting foundation, not the only valid model.  
D. Model choice depends only on the size of the team.

### 39. A dashboard number wearing no badge

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** What is Data? Data vs. Information  
**Is Curriculum Based:** No  
**Assessment type:** Information-design repair

A dashboard audit records:

| Site | Current display | Label | Unit or scale |
|---|---:|---|---|
| W3 | `96` | Missing | Missing |

Managers admit they ignore the value.

Which smallest change turns the value into information?

A. Round every value up to 100.  
B. Label it: "Site W3 occupancy: 96% of pallet capacity."  
C. Mirror the value into two more dashboards.  
D. Recolour the number without documenting what the colours mean.

### 40. Everything points the same way

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Foundations  
**Subtopic:** Why Relational Databases First: Tables, SQL, and the Industry Standard  
**Is Curriculum Based:** No  
**Assessment type:** Integrated realistic application

A growing marketplace scores its requirements:

| Evidence | Current need |
|---|---|
| Data shape | Structured customers, orders, and payouts |
| Relationships | Daily reports combine those records |
| Usage | Hundreds of concurrent users |
| Team skill | Existing SQL experience |

Which recommendation best combines that evidence?

A. Adopt a relational DBMS to match the structured, report-heavy load.  
B. Stay on departmental spreadsheets until something eventually and visibly breaks.  
C. Use a key-value store, since every order already has an ID.  
D. Defer any database until every future requirement is known.

---

## Instructor Key

### 1. C

The raw `81` could be a temperature, a percentage, or an ID. The dashboard supplies the crane's identity, the metric, and the scale, which is exactly the contextual layer that turns recorded data into actionable information. Option A mislocates the transformation in the number itself, which never changed.

### 2. A

One fact — Rhea's fee — is stored redundantly in three files, and the revision reached only `payouts.xlsx`. The two stale files still agreeing with each other (option D's trap) is what makes majority-vote reasoning dangerous: the majority here is the outdated value.

### 3. D

The organized content — reservations, profiles, rates — is the database; MySQL is the management software operating on it. Keeping the two separated is what later makes ideas like migration and backups coherent.

### 4. B

Double-selling a seat and half-completing a transfer are both failures of coordinated concurrent change. The shared capability is keeping one consistent state while many actions land on it at nearly the same instant — not isolation of copies (A, D), which would create the very disagreement the apps must prevent.

### 5. A

The three record types legitimately carry different fields, and new shapes keep arriving. Document databases allow records in one collection to vary, which is the defining fit here; a rigid single table (B) would force meaningless empty columns onto every row.

### 6. D

Writing the feature's query is development; restoring a backup is administration; browsing a watchlist through the app is end use. The tell in each case is the person's relationship to the database — building on it, safeguarding it, or consuming it through an interface.

### 7. C

Insertion creates the record; forty status reads are queries; the address correction is an update; cold storage is archival. Option A ends in deletion, which never happens in the shown history — retention moved the record, it did not destroy it.

### 8. B

The justification in the material is transferability: tables and SQL recur across vendors and industries, so the skill compounds. It is not a supremacy claim (A) — which is why the course also covers when other models fit better.

### 9. D

The drive keeps the last complete file. Farhan saved a copy that never contained Asha's Bay 2 edit, so his 10:25 save overwrote it. That both edits touched "different rows" (option A) is irrelevant — whole-file replacement has no notion of rows.

### 10. A

A known key mapping directly to one value, at high volume, with no relational questions asked, is the textbook key-value access pattern. The relational option isn't wrong because relational is bad — it is simply machinery the workload never uses.

### 11. B

Identity (Freezer F2), unit (°C), and the alarm threshold connect the reading to the decision the manager must make. Duplicating the value (A) or styling it (D) adds no meaning; altering it (C) destroys accuracy in the name of caution.

### 12. D

The failure mode is multiple independently edited copies. Reminders (A) leave the copy count untouched, and a fifth copy (B) increases it. Only consolidating to one managed source removes the possibility of copies disagreeing.

### 13. C

Databases persist on storage; the DBMS is a process that must run to serve queries, but its downtime does not evaporate the data. Option B fails the other direction — without the managing software, nothing is answering queries at all.

### 14. A

Options B, C, and D are exactly the operations a key-value store excels at: get, put, delete by key. The analytics request forces relating and aggregating across many records — the capability the single-key design gave up.

### 15. B

The theatre-goer consumed a database-backed answer entirely through the application. That a query ran underneath does not make them its author — the developer wrote it once; the end user merely triggered it.

### 16. C

"Completed" does not mean "useless." Retention law and possible disputes are future queries waiting to happen, so the record must remain retrievable — archival storage satisfies that while acknowledging the record has left the hot path.

### 17. D

The plan asks intention to do what mechanism must do: at thirty people, someone will forget a copy, and two will eventually save at once. The proposal manages neither concurrency nor completeness — it only hopes about both.

### 18. B

The number 230 is unchanged; what changed is that it now names a turbine, a unit, and a moment. That contextual attachment — not storage, styling, or duplication — is the data-to-information step.

### 19. A

The disks were already storing bytes. What they never provided was management: who may access what, how simultaneous updates are coordinated, and how retrieval stays reliable. That management layer is precisely what a DBMS is.

### 20. C

Fixed mandatory fields, heavily connected entities, and legally consequential consistency are the three signatures of a relational fit. Flexible-shape freedom (B) is a liability, not a feature, in a registry.

### 21. D

Nothing has diverged yet, so inconsistency is absent — but three copies of one fact mean redundancy is present, and redundancy is the precondition for divergence. The distinction matters because the risk exists before any symptom does.

### 22. B

Search semantics are application behaviour, authored by the developer. Proving a backup restores is recoverability assurance, owned by the DBA. The quarterly drill detail is the giveaway: verifying restores is an administrative discipline, not a feature.

### 23. C

Reading the tracking page inspects the record without altering it. Editing the address and flipping the status are updates; moving the record to the archive changes where it lives.

### 24. A

Correctness requirements should scale with real-world consequence. A wrong turbine serial can invalidate airworthiness; phantom steps cost nothing. Option D inverts the lesson — high stakes demand more validation, never less.

### 25. D

The workload has uniform mandatory fields and constant cross-record reporting: the relational signature. The document model's genuine strength — flexible shapes — is not needed anywhere in the scenario, leaving fashion as the only argument, and fashion is not a requirement.

### 26. C

The code has no operational future (expired, non-reusable) and no retention obligation. That is the exact profile of a record whose lifecycle correctly ends in deletion.

### 27. B

Roles describe responsibilities, not headcount. Writing application queries is developer work; verifying backups is DBA work; one person in a small company can hold both.

### 28. D

The manager has fused content with software. The policy data is the database and survives the move; PostgreSQL and MySQL are alternative management layers around it. Migration is transfer, not amnesia.

### 29. A

The customer experiences the presentation layer. The files, the DBMS's internals, and the admin console all participate invisibly — which is precisely the layering the lesson describes.

### 30. C

A status change is one record's continuing story. Build B tells that story as unlinked strangers, making "what happened to parcel 88?" unanswerable without forensic matching. The newest status existing "somewhere" (A) is not the same as the record having a coherent lifecycle.

### 31. B

The suspected defect is last-save-wins overwriting. Reproducing it requires its exact preconditions: two independent copies, divergent edits, sequential saves. The other tests never create a second concurrent editor, so they can never trigger the failure.

### 32. A

Linked entities plus combined reporting is the relational signature. The token cache (B) is key-value, the variable-shape crash blobs (C) are document territory, and a single counter (D) needs almost no model at all.

### 33. C

Transferability is an empirical claim about the market, and repeated demand across unrelated industries is direct evidence for it. Options A, B, and D are all false as facts, so they can support nothing.

### 34. D

Once created, the record is read at every login and transfer — thousands of queries against a handful of updates and a single archival. Reads dominating writes is the typical shape of a long-lived record's life.

### 35. B

Each copy of the fact is one more place every change must reach, so N copies turn one correction into N tasks with N chances to miss one. The wrong-gate risk is the inconsistency that a single missed task produces.

### 36. A

Backup health and recovery readiness are administrative duties — and the silent nature of the failure is the point: detecting it requires someone whose job includes watching, not someone who happens to use the site.

### 37. D

Three different shapes and access patterns are on the table, so the rule must be fit-driven: billing's linked, uniform records point relational; the token cache points key-value; the variable metadata points document. Any one-size answer discards two of the three fits.

### 38. C

Teaching order reflects pedagogy — a transferable foundation first — not a universal architecture mandate. The course itself presents key-value and document models as legitimate fits for other workloads.

### 39. B

The label supplies identity, metric, and scale, which is what the managers were missing when they learned to ignore the number. Rounding (A) corrupts the value, and unexplained colour (D) just adds a second mystery.

### 40. A

Every listed fact — structure, relationships, reporting, concurrency, existing SQL skill — independently points at a relational DBMS. Option B ignores the concurrency already present; option C mistakes having identifiers for having key-value access patterns.

---

## Question-Type Distribution

| Higher-order assessment family | Question numbers |
|---|---|
| Contextual classification and exact mapping | 1, 3, 6, 15, 23, 27, 29, 32 |
| Root-cause and causal-chain diagnosis | 2, 9, 21, 28, 35 |
| Smallest repair and missing-context completion | 11, 12, 39 |
| Defect-exposing scenario or requirement | 14, 31 |
| Implementation comparison and equivalence | 22, 30 |
| Model and structure selection | 5, 10, 20, 25, 32, 37, 40 |
| Lifecycle tracing, final state, and policy | 7, 16, 23, 26, 30, 34 |
| Role and responsibility analysis | 6, 15, 22, 27, 36 |
| Evidence, risk, and realistic design judgment | 4, 8, 13, 17, 19, 24, 33, 38, 40 |

## Blueprint Taxonomy Coverage

| Subtopic from the attached blueprint | Question numbers | Count |
|---|---|---:|
| What is Data? Data vs. Information | 1, 11, 18, 39 | 4 |
| The Problem with Files | 2, 9, 12, 17, 21, 31, 35 | 7 |
| What is a Database? What is a DBMS? | 3, 13, 19, 28 | 4 |
| Where Databases Live: Real Apps You Already Use | 4, 24, 29 | 3 |
| Types of Databases | 5, 10, 14, 20, 25, 32, 37 | 7 |
| Why Relational Databases First: Tables, SQL, and the Industry Standard | 8, 33, 38, 40 | 4 |
| Who Uses a Database: End Users, Developers, and Administrators | 6, 15, 22, 27, 36 | 5 |
| The Lifecycle of Data: From Creation to Query to Deletion | 7, 16, 23, 26, 30, 34 | 6 |

Questions 1–10 collectively cover all eight Topic 1.1 subtopics.

## Difficulty and Answer-Key Balance

- Foundational: 17 questions (1, 3, 6, 8, 10, 11, 13, 18, 19, 23, 27, 28, 29, 33, 36, 38, 39)
- Intermediate: 23 questions (2, 4, 5, 7, 9, 12, 14, 15, 16, 17, 20, 21, 22, 24, 25, 26, 30, 31, 32, 34, 35, 37, 40)
- Advanced: 0 questions — appropriate for this introductory conceptual chapter
- Correct option A: 10 questions (2, 5, 10, 14, 19, 24, 29, 32, 36, 40)
- Correct option B: 10 questions (4, 8, 11, 15, 18, 22, 27, 31, 35, 39)
- Correct option C: 10 questions (1, 7, 13, 16, 20, 23, 26, 30, 33, 38)
- Correct option D: 10 questions (3, 6, 9, 12, 17, 21, 25, 28, 34, 37)
- Longest consecutive run of one correct letter: below 3 throughout
