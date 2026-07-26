# DBMS 2.1: Entity-Relationship Modeling — 40 Higher-Order MCQs

## Assessment specifications

- **Subject:** DBMS
- **Topic:** Database Design & Modeling
- **Chapter:** Entity-Relationship Modeling
- **Scope:** All six Topic 2.1 subtopics in the attached course blueprint (Entities, Attributes, and Relationships; Types of Attributes; Relationship Cardinality; Participation Constraints; Drawing an ER Diagram; Converting an ER Diagram to Relational Tables)
- **Format:** Four options with exactly one best answer
- **Curriculum flag:** No
- **Design standard:** Every question establishes the database domain, explains what the named entities and fields mean, and provides the business rule or ER fragment being evaluated.
- **Table-use standard:** Domain evidence, attribute inventories, relationship rules, ER-notation fragments, and candidate relational schemas are shown as tables wherever students must compare or trace them.
- **Scope guard:** Only the six Topic 2.1 readings are assessed. Later normalization and SQL implementation details are excluded.
- **Difficulty policy:** Difficulty follows the actual reasoning required; no artificial quota is imposed.
- **Answer-quality controls:** A/B/C/D each correct exactly 10 times, no letter correct more than twice consecutively, no correct answer identifiable by length.
- **Coverage rule:** Questions 1–10 collectively cover all six Topic 2.1 subtopics.
- **Student/instructor separation:** Questions appear first; answers and explanations follow in the instructor key.

---

## Questions

### 1. Sort the three candidates

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Entities, Attributes, and Relationships  
**Is Curriculum Based:** No  
**Assessment type:** Concept classification

A car-rental database must remember customers, rentable vehicles, and each rental. A designer records:

| Candidate | Meaning in the business |
|---|---|
| **Vehicle** | A car the company tracks independently |
| `registration_no` | The official number describing one vehicle |
| **rents** | The connection stating which Customer rents which Vehicle |

Which classification is correct?

A. Vehicle: attribute; registration_no: entity; rents: attribute  
B. All three are entities of equal standing  
C. Vehicle: entity; registration_no: attribute; rents: relationship.  
D. Vehicle: relationship; registration_no: also a relationship; rents: an entity.

### 2. Find the attribute built from parts

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Types of Attributes  
**Is Curriculum Based:** No  
**Assessment type:** Attribute-type identification

A property portal's **Property** entity carries four attributes:

| Attribute | Detail |
|---|---|
| full_address | Made up of street, city, and PIN code |
| carpet_area | A single number in square feet |
| building_age | Worked out from the stored construction year |
| amenities | Gym, pool, parking — several at once |

Which attribute is **composite**?

A. `full_address`, assembled from smaller meaningful parts.  
B. `carpet_area`, which measures a specific physical thing directly.  
C. `building_age` — it changes every year.  
D. `amenities` — it has many values.

### 3. Name the shape of this connection

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Relationship Cardinality  
**Is Curriculum Based:** No  
**Assessment type:** Cardinality naming

An airline database tracks aircraft and their maintenance events:

| Direction read | Business rule |
|---|---|
| One Aircraft → MaintenanceLog | An aircraft may accumulate many log entries |
| One MaintenanceLog → Aircraft | Each entry describes exactly one aircraft |

What is the cardinality of Aircraft–MaintenanceLog?

A. One-to-one — each aircraft has one log entry.  
B. Many-to-many — logs mention many aircraft.  
C. MaintenanceLog is an attribute of Aircraft, so the connection has no cardinality.  
D. One-to-many from Aircraft to MaintenanceLog: one aircraft, many entries.

### 4. Who must take part, who may sit out

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Participation Constraints  
**Is Curriculum Based:** No  
**Assessment type:** Participation reading

An insurance database distinguishes clients from the policies they may hold:

| Relationship side | Minimum required participation |
|---|---|
| Policy | Must be linked to a Client |
| Client | May exist before holding any Policy |

Which participation reading is correct?

A. Total on both sides, so every client must hold a policy.  
B. Total on the Policy side, partial on the Client side.  
C. Partial on both sides, so a policy could exist without a client.  
D. Total on the Client side, partial on the Policy side.

### 5. Decode the whiteboard

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Drawing an ER Diagram  
**Is Curriculum Based:** No  
**Assessment type:** Notation-legend reading

A hospital database designer uses the following shapes on an ER whiteboard:

| Shape | Example label |
|---|---|
| Rectangle | `Patient` |
| Oval | `date_of_birth` |
| Diamond | `Admits` |

What does each shape conventionally mean?

A. Rectangle=entity, oval=attribute, diamond=relationship.  
B. Rectangles: attributes; ovals: relationships; diamonds: entities.  
C. Rectangles: relationships; ovals: entities; diamonds: attributes.  
D. The shapes are decorative; only the labels carry meaning.

### 6. The relationship that needs its own table

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Converting an ER Diagram to Relational Tables  
**Is Curriculum Based:** No  
**Assessment type:** Mapping-rule application

A streaming database models this rule:

| One side | Possible partners |
|---|---|
| One Actor | Many Films |
| One Film | Many Actors |

`actor_id` identifies an actor and `film_id` identifies a film.

How is this Actor–Film relationship converted to tables?

A. Add one `film_id` column to `actors`, allowing one film per actor.  
B. Add an `actor_id` column to the films table.  
C. A linking table holding `actor_id` and `film_id` per appearance.  
D. Merge actors and films into one wide table.

### 7. Spot the many-to-many in the wild

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Relationship Cardinality  
**Is Curriculum Based:** No  
**Assessment type:** Cardinality discrimination

Four database projects report:

| Rule | Business relationship |
|---:|---|
| 1 | Each ferry sails under one flag; one flag covers many ferries |
| 2 | One ad campaign runs on several platforms; each platform hosts several campaigns |
| 3 | One turbine has one nameplate; each nameplate belongs to one turbine |
| 4 | Each van-shift record names one driver; one driver appears on many shift records |

Which rule describes a many-to-many relationship?

A. Rule 1 — one-to-many, not many-to-many.  
B. Rule 2 — several on both sides.  
C. Rule 3 — one-to-one, not many-to-many.  
D. Rule 4 — one-to-many, not many-to-many.

### 8. To store or to compute?

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Types of Attributes  
**Is Curriculum Based:** No  
**Assessment type:** Derived-attribute policy judgment

A shipping database's `Crew` entity stores:

| Attribute | Meaning | Proposed maintenance |
|---|---|---|
| `join_date` | Date the crew member joined | Stored once |
| `years_of_service` | Years elapsed since joining | Manually updated when remembered |

What does the chapter's treatment of derived attributes recommend?

A. Store both and let them drift apart naturally.  
B. Delete `join_date` and keep only `years_of_service`.  
C. Store `years_of_service` separately and refresh it during periodic reviews.  
D. Treat `years_of_service` as derived, computed from `join_date` when needed.

### 9. Which side carries the key?

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Converting an ER Diagram to Relational Tables  
**Is Curriculum Based:** No  
**Assessment type:** Foreign-key placement

A winery database has `Vat`, identified by `vat_id`, and `Batch`, identified by `batch_id`:

| Direction read | Rule |
|---|---|
| One Vat → Batch | Many batches |
| One Batch → Vat | Exactly one vat |

When converting, where does the foreign key go?

A. On the "many" side — each `batches` row carries a `vat_id` foreign key.  
B. On the "one" side — the `vats` table lists all its batch IDs in one column.  
C. On both sides simultaneously, for symmetry.  
D. Nowhere — one-to-many relationships need a separate linking table.

### 10. What kind of thing is "Sponsors"?

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Entities, Attributes, and Relationships  
**Is Curriculum Based:** No  
**Assessment type:** Concept identification

A marathon database brief states:

| Model element | Meaning |
|---|---|
| **Company** | An organization that may fund events |
| **Event** | A race organized by the marathon team |
| **Sponsors** | Connects a Company to an Event it funds |

What is Sponsors?

A. An attribute of Company.  
B. An independent Sponsor entity representing the organization that provides funding.  
C. A relationship linking Company and Event.  
D. A cardinality label.

### 11. The one-fact-one-value attribute

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Types of Attributes  
**Is Curriculum Based:** No  
**Assessment type:** Attribute-type identification

A drone database's `Drone` entity lists:

| Attribute | Meaning |
|---|---|
| `max_speed` | One speed value |
| `home_base_address` | Street, city, and PIN |
| `flight_hours_remaining` | Computed from service records |
| `licensed_zones` | Several zone codes held at once |

Which attribute is **simple**?

A. `home_base_address`, composite.  
B. `max_speed`, a single atomic value.  
C. `flight_hours_remaining`, updated frequently.  
D. `licensed_zones`

### 12. One black box, one locomotive

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Relationship Cardinality  
**Is Curriculum Based:** No  
**Assessment type:** Cardinality naming

A railway database records:

| Direction | Maximum partner count |
|---|---:|
| One Locomotive → Recorder | 1 |
| One Recorder → Locomotive | 1 |

What is the cardinality of Locomotive–Recorder?

A. One-to-many  
B. Many-to-many  
C. Many-to-one only, which isn't quite right.  
D. One-to-one — a single match on both sides.

### 13. What "total" actually demands

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Participation Constraints  
**Is Curriculum Based:** No  
**Assessment type:** Constraint interpretation

A consulate database models `Applicant` and `Application` through `FiledBy`:

| Proposed state | Allowed? |
|---|---|
| Application linked to an applicant | Yes |
| Application with no applicant | No |

What does this rule establish?

A. Total participation of Application in the FiledBy relationship.  
B. Partial participation of Application: filing is optional.  
C. A many-to-many cardinality between applications and applicants.  
D. That Application is an attribute of Applicant.

### 14. Pick the entities out of the brief

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Entities, Attributes, and Relationships  
**Is Curriculum Based:** No  
**Assessment type:** Entity discovery

A festival database brief separates the following candidates:

| Candidate | Facts or role |
|---|---|
| Food truck | Has a name and cuisine |
| Pitch | Has a size and daily rental rate |
| Occupies | Connects a truck to a pitch |

Which list correctly identifies the entities?

A. Name, cuisine, size, and daily rate.  
B. Only FoodTruck; each pitch should be stored as a descriptive attribute on FoodTruck.  
C. FoodTruck and Pitch are the entities here; the rest support them.  
D. Occupies, books, and tracks.

### 15. Read the numbers on the line

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Drawing an ER Diagram  
**Is Curriculum Based:** No  
**Assessment type:** Diagram-fragment reading

An animal-shelter ER specification contains:

| Left entity | Relationship | Right entity | Labels |
|---|---|---|---|
| **KENNEL** | *houses* | **DOG** | `1` at Kennel, `N` at Dog |

What does it say?

A. One dog lives in many kennels at once.  
B. One kennel houses many dogs; each dog, one kennel.  
C. Kennels and dogs pair one-to-one.  
D. The `N` means a dog's participation in *houses* is optional.

### 16. Rule one, applied

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Converting an ER Diagram to Relational Tables  
**Is Curriculum Based:** No  
**Assessment type:** Mapping-rule application

A pottery database's ER inventory shows:

| Entity | Attribute | Meaning |
|---|---|---|
| **KILN** | `kiln_id` | Identifies the kiln |
| **KILN** | `max_temp` | Highest safe temperature |
| **KILN** | `capacity` | Load capacity |

What does the first conversion rule produce from this?

A. Three tables — one per attribute.  
B. Nothing at all, until some relationship eventually touches the entity.  
C. A column in some other entity's table.  
D. A `kilns` table with `kiln_id`, `max_temp`, and `capacity` columns.

### 17. Same shape, read from the other end

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Relationship Cardinality  
**Is Curriculum Based:** No  
**Assessment type:** Bidirectional reading

A telecom database records:

| Direction | Rule |
|---|---|
| Household → Subscription | Zero or several subscriptions |
| Subscription → Household | Exactly one household |

Which statement expresses the same cardinality, read from the subscription side?

A. Subscriptions to households is many-to-many.  
B. Each household belongs to one subscription.  
C. Many subscriptions point to one Household.  
D. The two directions describe two separate relationships.

### 18. What the optional side permits

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Participation Constraints  
**Is Curriculum Based:** No  
**Assessment type:** Constraint-consequence reasoning

A port database models an `Assigned` relationship:

| Entity side | Participation rule |
|---|---|
| Warehouse | Partial; a warehouse may have no dock |
| Dock | Not relevant to the question |

What does this partial participation permit in the data that total participation would forbid?

A. Warehouses existing with no dock assignment at all.  
B. Several warehouses linked to one dock, regardless of cardinality.  
C. Warehouses with two names.  
D. Deleting the dock entity from the diagram.

### 19. The attribute with a plural answer

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Types of Attributes  
**Is Curriculum Based:** No  
**Assessment type:** Attribute-type identification

A contractor database's `Welder` entity lists:

| Attribute | Structure for one welder |
|---|---|
| `hourly_rate` | One number |
| `full_name` | First name plus last name |
| `date_of_birth` | One date |
| `certifications` | TIG, MIG, and underwater may all be held at once |

Which attribute is **multivalued**?

A. `hourly_rate`, numeric.  
B. `full_name`, textual.  
C. `date_of_birth`, a fixed calendar date value.  
D. `certifications`, multivalued.

### 20. Both directions say "many"

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Relationship Cardinality  
**Is Curriculum Based:** No  
**Assessment type:** Cardinality naming

A fitness database states:

| Direction | Rule |
|---|---|
| Member → Branch | A member may use several branches |
| Branch → Member | A branch serves many members |

What is the cardinality of Member–Branch?

A. One-to-one, a rare exact match.  
B. Many-to-many.  
C. One-to-many from Member to Branch.  
D. One-to-many from Branch to Member.

### 21. Total here, partial there

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Participation Constraints  
**Is Curriculum Based:** No  
**Assessment type:** Two-sided participation reading

A veterinary database models `Vet — Writes — Prescription`:

| Entity side | Can an instance exist without participating? |
|---|---|
| Prescription | No; every prescription has a vet |
| Vet | Yes; a newly licensed vet may have written none |

Which reading is correct?

A. Prescription participates totally; Vet participates partially.  
B. Both sides are total.  
C. Vet participates totally; Prescription partially.  
D. Participation cannot differ between the two sides of one relationship.

### 22. Inside the linking table

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Converting an ER Diagram to Relational Tables  
**Is Curriculum Based:** No  
**Assessment type:** Junction-table structure

A music database models Musicians and Bands as many-to-many. `musician_id` identifies a musician and `band_id` identifies a band. Conversion produces:

| `Memberships` row | Meaning |
|---|---|
| (`musician_id`, `band_id`) | One musician's membership in one band |

What identifies each row of that table?

A. A `band_name` column alone.  
B. The row's position in the table.  
C. A single `musician_id`, since musicians come first alphabetically.  
D. The combination of `musician_id` and `band_id` together.

### 23. Attribute, or entity in disguise?

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Entities, Attributes, and Relationships  
**Is Curriculum Based:** No  
**Assessment type:** Boundary judgment

A book-distribution database first treats `publisher` as text inside Book. New requirements add:

| Candidate publisher fact | Needed independently? |
|---|---|
| Address | Yes |
| Founding year | Yes |
| Contact person | Yes |

What should `publisher` become?

A. A longer text attribute containing the name, address, year, and contact together.  
B. A derived attribute computed from the title.  
C. An entity of its own, since it now has attributes of its own.  
D. A cardinality label on the Book entity.

### 24. Read the diagram like a sentence

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Drawing an ER Diagram  
**Is Curriculum Based:** No  
**Assessment type:** Full-fragment reading

A resort database's ER fragment is:

| First entity | Relationship | Second entity | Cardinality |
|---|---|---|---|
| **GUEST** | *makes* | **RESERVATION** | 1:N |
| **RESERVATION** | *for* | **ROOM** | N:1 |

Which sentence matches the diagram?

A. Each guest makes one reservation, and that reservation covers many rooms.  
B. A guest makes many reservations; each reservation, one guest, one room.  
C. Rooms make reservations for guests.  
D. Guests and rooms pair one-to-one through reservations.

### 25. One-to-one, but where's the key?

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Converting an ER Diagram to Relational Tables  
**Is Curriculum Based:** No  
**Assessment type:** Mapping-rule application

A corporate database records:

| Direction | Rule |
|---|---|
| Executive → Space | At most one dedicated space |
| Space → Executive | One executive |

The ER line is `EXECUTIVE —1— assigned —1— SPACE`.

How is this converted?

A. A linking table with two foreign keys, as for many-to-many.  
B. Foreign keys on both tables pointing at each other, both freely repeating.  
C. No keys — one-to-one needs no connection.  
D. A foreign key on either table, with a rule preventing repeated partners.

### 26. Count the tables

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Converting an ER Diagram to Relational Tables  
**Is Curriculum Based:** No  
**Assessment type:** Conversion-outcome counting

A conference database's ER inventory contains:

| Element | Rule |
|---|---|
| **VENUE** entity | One venue may host many events |
| **EVENT** entity | One event may span many venues |
| *hosts* relationship | Many-to-many |

How many tables does the standard conversion produce?

A. Three — `venues`, `events`, and a `hosts` linking table.  
B. Two — the relationship dissolves into a foreign key.  
C. One — everything merges.  
D. Four — one per entity, one per direction of the relationship.

### 27. The total that should not be typed in

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Types of Attributes  
**Is Curriculum Based:** No  
**Assessment type:** Derived-attribute identification

An invoicing database stores:

| Stored fact | Meaning |
|---|---|
| Line-item `quantity` | Units purchased |
| Line-item `unit_price` | Price per unit |
| Proposed `invoice_total` | Manually typed sum of all line items |

Which classification and treatment fits `invoice_total`?

A. Simple, because the result is one number that can be entered directly.  
B. Derived, since it's computable directly from the line items.  
C. Multivalued — invoices have many totals.  
D. Composite — totals are built from digits.

### 28. Why the shape decision cannot wait

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Relationship Cardinality  
**Is Curriculum Based:** No  
**Assessment type:** Design-consequence reasoning

Two hospital database designers compare:

| Possible business rule | Relational consequence |
|---|---|
| Each patient has one physiotherapist; one physiotherapist treats many patients | Foreign key on the many side |
| Patients may see many physiotherapists, and each therapist treats many patients | Junction table |

Why is that risky?

A. Diagrams are legally binding once drawn.  
B. Cardinality has no effect on tables.  
C. The cardinality decides the schema: foreign keys versus linking tables.  
D. Choose many-to-many by default so later business growth never requires redesign.

### 29. The double line

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Participation Constraints  
**Is Curriculum Based:** No  
**Assessment type:** Notation-to-meaning mapping

An insurance database's ER notation records:

| Entity side | Line to *covers* |
|---|---|
| **POLICY** | Double line |
| **VEHICLE** | Single line |

What does the doubled line declare?

A. The relationship is many-to-many.  
B. Policy participates in two separate *covers* relationships.  
C. Vehicles participate totally.  
D. Total participation of Policy in the *covers* relationship.

### 30. From one-to-many to actual columns

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Converting an ER Diagram to Relational Tables  
**Is Curriculum Based:** No  
**Assessment type:** Schema-outcome selection

A news database's ER design states:

| Entity | Attributes | Relationship reading |
|---|---|---|
| **AUTHOR** | `author_id`, `name` | One author writes many articles |
| **ARTICLE** | `article_id`, `headline` | Each article has one author |

Which resulting schema is correct?

A. `authors(author_id, name, article_id)` and `articles(article_id, headline)`  
B. `authors(author_id, name)` and `articles(article_id, headline, author_id)`.  
C. `authors(author_id, name)` and `articles(article_id, headline)` with a linking table `writes`.  
D. One table: `authors_articles(author_id, name, article_id, headline)`.

### 31. What attributes are for

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Entities, Attributes, and Relationships  
**Is Curriculum Based:** No  
**Assessment type:** Role identification

An emergency-services database models one independently tracked **Ambulance** with facts about its identity, equipment, and base.

Which list contains attributes — the facts the system needs to remember about each ambulance?

A. Registration number, equipment level, and base station address.  
B. The dispatcher, the on-call paramedic, and the workshop — as attribute values.  
C. "Responds-to" and "is-serviced-at."  
D. Other ambulances in the fleet.

### 32. The intern's inverted diagram

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Drawing an ER Diagram  
**Is Curriculum Based:** No  
**Assessment type:** Notation-error diagnosis

A marina database intern submits:

| Label | Shape used |
|---|---|
| `berth_length`, a measurement describing a berth | Rectangle |
| **BOAT**, a vessel tracked independently | Oval |

What is wrong?

A. Nothing — shape choice is stylistic.  
B. The oval and rectangle are correct, but their connecting line should be doubled.  
C. The shapes are inverted: BOAT needs a rectangle, not an oval.  
D. Attributes may not appear in diagrams at all.

### 33. Map the whole marina wall

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Converting an ER Diagram to Relational Tables  
**Is Curriculum Based:** No  
**Assessment type:** Multi-rule conversion

An art-district database has:

| ER relationship | Rule |
|---|---|
| `STUDIO —1— contains —N— ROOM` | A room belongs to one studio |
| `STUDIO —M— exhibits —N— ARTIST` | Studios exhibit many artists and artists appear at many studios |

Which table set results from the standard rules?

A. `studios`, `rooms`, and `artists`, with both relationships recorded only in application notes.  
B. `studios(artist_id)`, `rooms(studio_id)`, `artists(studio_id)`.  
C. A single `district` table holding everything.  
D. `studios`; `rooms(studio_id)`; `artists`; and `exhibits(studio_id, artist_id)`.

### 34. Where does the rate belong?

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Converting an ER Diagram to Relational Tables  
**Is Curriculum Based:** No  
**Assessment type:** Relationship-attribute placement

A work-platform database models one engagement as a Freelancer–Project pairing:

| Relationship fact | Example |
|---|---|
| Freelancer | F12 |
| Project | P8 |
| Negotiated `hourly_rate` | ₹1,800 for this pairing |

When converting, where does `hourly_rate` go?

A. On the freelancers table, treated as their one true fixed rate.  
B. In the linking table, describing the pairing itself.  
C. On the projects table, as the project's budget.  
D. Nowhere — rates cannot be modelled.

### 35. Why split the address at all?

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Types of Attributes  
**Is Curriculum Based:** No  
**Assessment type:** Composite-decomposition rationale

A catering database compares:

| Design | Stored address structure |
|---|---|
| A | One text value |
| B | `street`, `city`, and `PIN` as meaningful components |

Reports frequently filter clients by city.

What does recognizing `address` as composite buy the designer?

A. The parts become usable individually, enabling filtering by city.  
B. The address occupies less disk space.  
C. Clients can have several addresses.  
D. The three parts can be recalculated automatically from the original address text.

### 36. The genuine one-to-one

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Relationship Cardinality  
**Is Curriculum Based:** No  
**Assessment type:** Cardinality discrimination

A sports database team proposes:

| Pair | Business rule |
|---:|---|
| 1 | One cricket team has many squad members |
| 2 | Players appear in many matches and matches contain many players |
| 3 | One coach may hold several certifications |
| 4 | One national team has one current head coach, who leads only that team |

Which pairing is genuinely one-to-one?

A. Pairing 1 — squad members.  
B. Pairing 2 — matches played.  
C. Pairing 3 — certifications held, which is multivalued.  
D. Pairing 4 — a single permitted match on both sides.

### 37. Zero is allowed here

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Participation Constraints  
**Is Curriculum Based:** No  
**Assessment type:** Combined reading

A delivery database records:

| Direction | Minimum | Maximum |
|---|---:|---:|
| Rider → assigned Order | 0 | Many |
| Order → assigned Rider | 1 | 1 |

Which statement combines the cardinality and participation correctly?

A. Rider–Order is one-to-one with total participation on both sides.  
B. Orders participate partially, since riders may have zero.  
C. One-to-many from Rider to Order; riders partial, orders total.  
D. Riders participate totally because deliveries matter.

### 38. The diamond between vendor and part

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Drawing an ER Diagram  
**Is Curriculum Based:** No  
**Assessment type:** Notation reading

A manufacturing database's ER fragment contains:

| Shape | Label | Connected to |
|---|---|---|
| Diamond | *supplies* | **VENDOR** and **PART** rectangles |

What does the diamond represent?

A. An attribute whose value is shared by both Vendor and Part entities.  
B. The *supplies* relationship connecting Vendor and Part.  
C. Total participation of Vendor in Part.  
D. A third entity called Supplies.

### 39. Why a plain column cannot hold "many-to-many"

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Converting an ER Diagram to Relational Tables  
**Is Curriculum Based:** No  
**Assessment type:** Rule-rationale reasoning

A consulting database models:

| Direction | Rule |
|---|---|
| Consultant → Project | One consultant may work on many projects |
| Project → Consultant | One project may use many consultants |

A developer proposes putting one `project_id` field in each Consultant row.

What is the answer?

A. A single column stores one value per row, but consultants relate to many projects.  
B. Foreign keys are forbidden on tables with more than ten columns.  
C. The one foreign key can repeat across consultant rows to represent several projects.  
D. Put one `consultant_id` field on Project instead; reversing the direction solves the issue.

### 40. Convert the cinema, end to end

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Converting an ER Diagram to Relational Tables  
**Is Curriculum Based:** No  
**Assessment type:** Integrated conversion

A cinema database's ER design is:

| Relationship | Rule |
|---|---|
| `HALL —1— shows in —N— SCREENING` | Each screening uses one hall |
| `FILM —1— screened as —N— SCREENING` | Each screening shows one film |
| `VIEWER —M— attends —N— SCREENING` | Viewers attend many screenings; screenings have many viewers |

`hall_id`, `film_id`, `viewer_id`, and `screening_id` identify their respective entities.

Which table set is the correct conversion?

A. `halls`, `films`, `screenings`, `viewers` — no keys anywhere.  
B. `screenings(hall_id, film_id, viewer_id)`, storing one viewer directly on every screening and creating no junction table.  
C. `screenings(hall_id, film_id)` plus `halls`, `films`, `viewers`, and `attends(viewer_id, screening_id)`.  
D. One `cinema` table with every attribute of all four entities.

---

## Instructor Key

### 1. C

Vehicle is a thing the business tracks (entity); registration_no is a fact about a vehicle (attribute); rents is the association connecting customers to vehicles (relationship). The three concepts are the model's basic vocabulary.

### 2. A

A composite attribute is one built from smaller meaningful parts — street, city, PIN. `building_age` is derived (computed), `amenities` is multivalued, and `carpet_area` is simple; each answers a different classification.

### 3. D

Read both directions: aircraft → logs is "many"; log → aircraft is "one." That asymmetric pair is one-to-many, and reading only one direction (which option A does) is how cardinalities get misnamed.

### 4. B

"No policy without a client" makes the policy side total; "clients may hold nothing" makes the client side partial. Participation is read per side, and the two sides here genuinely differ.

### 5. A

The conventional legend: rectangles for entities, ovals for attributes, diamonds for relationships. The convention is what lets any trained reader parse any team's diagram.

### 6. C

Both directions say "many," and a foreign key column on either side could only record one partner per row. The standard rule: many-to-many becomes its own linking table with a foreign key to each participant.

### 7. B

Rule 2 says "several" in both readings — the many-to-many signature. Rules 1 and 4 are one-to-many; rule 3 is one-to-one.

### 8. D

`years_of_service` is derivable from `join_date`, and a stored copy has no mechanism keeping it current — "whenever someone remembers" is the staleness problem in one phrase. Derived attributes are computed at need, not stored.

### 9. A

The many side carries the reference: each batch names its vat. Option B — a list of batch IDs in the vat row — would pack many values into one cell, exactly what the relational model forbids.

### 10. C

Sponsors is not a thing with its own existence but a meaningful association between two entities — the definition of a relationship. If it later acquired attributes (amount, year), it would still be a relationship, just one carrying data.

### 11. B

`max_speed` is one atomic value — the simple attribute. The address decomposes (composite), the flight-hours figure is computed (derived), and the zones are plural (multivalued).

### 12. D

Exactly one on each side, read in both directions, is one-to-one. The recorder–locomotive pairing is a physical example of a single mutual match.

### 13. A

"Cannot exist without" is the language of total participation: every instance of Application must appear in FiledBy. It says nothing about how many applications one applicant may file (cardinality).

### 14. C

Entities are the tracked things — trucks and pitches. The names, cuisines, sizes, and rates are facts about them, and "occupies" is how they connect. Option A promotes the attributes; option D promotes the verbs.

### 15. B

The 1 sits at the kennel end and the N at the dog end: one kennel, many dogs; each dog, one kennel. N marks multiplicity, not optionality (option D confuses cardinality with participation).

### 16. D

Rule one: every entity becomes a table, and its attributes become the columns. One entity, one table — relationships add keys and tables in later rules.

### 17. C

One relationship, two readings: household → subscriptions is one-to-many; subscription → household is many-to-one. They are the same fact from opposite ends — not two relationships (option D).

### 18. A

Partial participation is permission to sit out: warehouse rows with no dock link are legal data. Total participation on that side would make an unassigned warehouse a constraint violation.

### 19. D

Multivalued means several values of the same attribute held simultaneously — three certifications at once. The composite (`full_name`) has parts; the multivalued has copies.

### 20. B

"Several branches" and "many members" — many in both directions is many-to-many. Options C and D each capture only one of the two readings.

### 21. A

Every prescription is written (total on the prescription side); some vets have written none (partial on the vet side). The two sides of one relationship carry independent participation constraints.

### 22. D

A membership pairing is identified by who and which band — the two foreign keys together. One column alone cannot distinguish a musician's several memberships.

### 23. C

The dividing line: something with attributes of its own is an entity. Once the publisher has an address, a founding year, and a contact, it has outgrown being a value in someone else's column.

### 24. B

Walking the fragment: guest 1—N reservation gives "a guest makes many, each made by one"; reservation N—1 room gives "each reservation is for one room, a room has many." Option A reverses the first reading.

### 25. D

One-to-one converts as a foreign key on either one of the tables, constrained unique so a partner cannot be claimed twice. A junction table (option A) is legal but is the many-to-many machinery — heavier than the rule requires.

### 26. A

Rule one gives a table per entity (two), and rule four gives the many-to-many its own linking table (one more): three. The relationship cannot dissolve into a foreign key (option B) because both sides are "many."

### 27. B

The total is computable from the line items, making it derived. Hand-entering a copy creates a number that can disagree with the rows it claims to summarize — the exact drift the derived classification warns about.

### 28. C

Cardinality is not a label; it is the schema decision. One-to-many yields a foreign key, many-to-many a junction table — structurally different databases. Settling it "later" means rebuilding, not renaming.

### 29. D

The doubled line is the notation for total participation: every policy must cover something. The single line on the vehicle side leaves vehicles free to exist uncovered.

### 30. B

The many side (articles) carries the foreign key `author_id`. Option A puts a single article ID on the author — capping every author at one article; option C spends a junction table where a foreign key suffices.

### 31. A

Attributes are the remembered facts about each instance: registration, equipment, base address. Dispatchers and workshops are other entities; "responds-to" is a relationship.

### 32. C

The notation is a shared language: entities in rectangles, attributes in ovals. Swapping them doesn't change the marina — it changes what every fluent reader will believe the marina is.

### 33. D

Rule one gives three entity tables. The one-to-many places `studio_id` on `rooms`, while the many-to-many *exhibits* relationship becomes a junction table containing both identifiers. Option B would incorrectly cap a studio or artist at one partner.

### 34. B

The rate belongs to neither party alone — it describes one specific pairing. Attributes of a many-to-many relationship ride on the junction row that represents that pairing.

### 35. A

Decomposing the composite makes its parts addressable: filter by city, sort by PIN, validate the code's format. A single blob can only ever be matched whole.

### 36. D

At any time: one team, one head coach — singular in both directions. A squad (1) is one-to-many; matches played (2) is many-to-many; certifications (3) is a multivalued attribute, not a relationship cardinality at all.

### 37. C

"Zero, one, or many" on the rider side is one-to-many cardinality plus partial participation (zero allowed). "Exactly one rider" on the order side is total participation. The two constraint types answer different questions about the same line.

### 38. B

Diamonds carry relationships. *Supplies* is the association itself — not a property of either entity, and not a third entity unless it someday needs attributes and independent existence.

### 39. A

One cell, one value: a lone foreign key can point at one project only. Many pairings need many rows, and rows of pairings are exactly what a linking table is — each Consultant–Project combination stored as its own row.

### 40. C

The two one-to-many relationships put `hall_id` and `film_id` on `screenings`. Viewer–Screening is many-to-many, so `attends(viewer_id, screening_id)` stores one attendance pairing per row. Option B would cap each screening at one viewer.

---

## Question-Type Distribution

| Higher-order assessment family | Question numbers |
|---|---|
| Classification and identification | 1, 2, 10, 11, 12, 19, 20, 23, 27, 31 |
| Diagram and notation reading | 5, 15, 24, 29, 32, 38 |
| Cardinality and participation analysis | 3, 4, 7, 13, 17, 18, 21, 28, 36, 37 |
| Conversion-rule application | 6, 9, 16, 22, 25, 26, 30, 33, 34, 40 |
| Rationale and consequence reasoning | 8, 14, 35, 39 |

## Blueprint Taxonomy Coverage

| Subtopic from the attached blueprint | Question numbers | Count |
|---|---|---:|
| Entities, Attributes, and Relationships | 1, 10, 14, 23, 31 | 5 |
| Types of Attributes | 2, 8, 11, 19, 27, 35 | 6 |
| Relationship Cardinality | 3, 7, 12, 17, 20, 28, 36 | 7 |
| Participation Constraints | 4, 13, 18, 21, 29, 37 | 6 |
| Drawing an ER Diagram | 5, 15, 24, 32, 38 | 5 |
| Converting an ER Diagram to Relational Tables | 6, 9, 16, 22, 25, 26, 30, 33, 34, 39, 40 | 11 |

Questions 1–10 collectively cover all six Topic 2.1 subtopics.

## Difficulty and Answer-Key Balance

- Foundational: 13 questions (1, 5, 10–12, 15, 18, 20, 23, 29, 31, 36, 38)
- Intermediate: 25 questions (2–4, 6–9, 13–14, 16–17, 19, 21–22, 24–28, 30, 32, 34–35, 37, 39)
- Advanced: 2 questions (33, 40)
- Correct option A: 10 questions (2, 5, 9, 13, 18, 21, 26, 31, 35, 39)
- Correct option B: 10 questions (4, 7, 11, 15, 20, 24, 27, 30, 34, 38)
- Correct option C: 10 questions (1, 6, 10, 14, 17, 23, 28, 32, 37, 40)
- Correct option D: 10 questions (3, 8, 12, 16, 19, 22, 25, 29, 33, 36)
- Longest consecutive run of one correct letter: below 3 throughout
