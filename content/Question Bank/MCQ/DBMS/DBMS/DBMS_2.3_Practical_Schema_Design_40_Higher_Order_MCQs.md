# DBMS 2.3: Practical Schema Design — 40 Higher-Order MCQs

## Assessment specifications

- **Subject:** DBMS
- **Topic:** Database Design & Modeling
- **Chapter:** Practical Schema Design
- **Scope:** All six Topic 2.3 subtopics in the attached course blueprint (Choosing the Right Data Type; Primary Key Strategies; Naming Conventions; Audit Columns and Soft Deletes; Database Schemas and Namespaces; Schema Design Review)
- **Format:** Four options with exactly one best answer
- **Curriculum flag:** No
- **Design standard:** Every scenario defines the database, table, and important fields before asking for a judgment. Evidence tables, DDL fragments, access matrices, incident records, and before/after designs are used whenever they make the reasoning visible.
- **Scope guard:** Questions use only concepts taught in Topic 2.3. Business details establish context but require no outside industry knowledge.
- **Answer-quality controls:** A/B/C/D each correct exactly 10 times, no letter correct more than twice consecutively, no correct answer identifiable by length.
- **Coverage rule:** Questions 1–10 collectively cover all six Topic 2.3 subtopics.
- **Student/instructor separation:** Questions appear first; answers and explanations follow in the instructor key.

---

## Questions

### 1. Nineteen ninety-nine, thousands of times

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Choosing the Right Data Type  
**Is Curriculum Based:** No  
**Assessment type:** Type-selection judgment

A subscription database uses `charge_id` to identify a monthly bill and `amount` for the exact rupee amount charged:

| Intended charge | Draft type | Reconciliation result |
|---:|---|---|
| ₹19.99 per row | `FLOAT` | Total differs from the invoice sum by a few paise |

Select the repair that fixes the stored value rather than merely hiding the symptom.

A. Round the float totals in application code every single month instead.  
B. Store money as an exact fixed-point decimal type instead of float.  
C. Store the amount as text to preserve the digits.  
D. Switch to yearly billing so fewer rows are summed.

### 2. Keys minted in the field

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Primary Key Strategies  
**Is Curriculum Based:** No  
**Assessment type:** Strategy matching

Crop-survey teams create observations on offline tablets and later merge them into one database:

| Requirement | Value |
|---|---|
| Key assigned | Permanently, when the observation is created |
| Key generators | Many disconnected tablets |
| Coordination at creation | None |
| Merge destination | One central database |

Approve the key strategy that satisfies all four constraints.

A. Auto-incrementing integers assigned by each tablet.  
B. Letting the sync server renumber everything on arrival every single time.  
C. Using the surveyor's name as the key.  
D. UUIDs, generated independently by each device without coordination.

### 3. A column name that gives directions

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Naming Conventions  
**Is Curriculum Based:** No  
**Assessment type:** Naming selection

An inventory database has these two tables:

| Table | Role |
|---|---|
| `warehouses` | One row per warehouse, identified by `warehouse_id` |
| `stock_movements` | One row per stock arrival or departure |

`stock_movements` needs a foreign key pointing to `warehouses.warehouse_id`.

Fill the missing foreign-key name using the chapter's convention.

A. `warehouse_id`, saying exactly what it points to.  
B. `wh` — short and quick to type.  
C. `ref_1` — numbered references stay flexible.  
D. `location_data` — vague enough to survive many changes.

### 4. Gone, but not actually gone

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Audit Columns and Soft Deletes  
**Is Curriculum Based:** No  
**Assessment type:** Mechanism identification

A podcast platform "deletes" a cancelled show by running:

```sql
UPDATE shows SET deleted_at = NOW() WHERE show_id = 42;
```

The app's listing queries exclude rows where `deleted_at` is set.

Classify the update and identify the property it preserves.

A. A hard delete — the row is physically erased.  
B. An audit column — the row records its exact creation timestamp too.  
C. A soft delete: the row is marked gone but stays recoverable.  
D. A schema move — the row changed namespaces.

### 5. Two teams, one database, no collisions

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Database Schemas and Namespaces  
**Is Curriculum Based:** No  
**Assessment type:** Purpose identification

A fintech keeps billing and inventory data on one database server:

| Full table name | Owning area |
|---|---|
| `billing.invoices` | Billing |
| `billing.rates` | Billing |
| `inventory.items` | Inventory |
| `inventory.stock_counts` | Inventory |

Complete the architecture note: “`billing` and `inventory` are ______.”

A. Two separate servers connected by replication.  
B. Table prefixes stored inside each table's data rows themselves.  
C. Backup labels applied nightly.  
D. Schemas — named folders that group related tables together.

### 6. Review the intern's draft

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Schema Design Review  
**Is Curriculum Based:** No  
**Assessment type:** Multi-flaw review

An intern's draft for a courier firm:

```sql
CREATE TABLE Shipment (
    tracking_text VARCHAR(300),
    Price FLOAT,
    dest VARCHAR(200)
);
```

Record every defect that can be justified from the shown DDL.

A. The only problem is that the table has three columns.  
B. Three mistakes: no primary key, float money, inconsistent naming.  
C. The draft is production-ready as written.  
D. The only issue is `dest`; table identity, approximate money, and casing require no review.

### 7. Exactly three letters, every time

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Choosing the Right Data Type  
**Is Curriculum Based:** No  
**Assessment type:** Fixed-versus-variable selection

An aviation database documents `airport_code` as exactly three letters:

| Accepted examples | Rejected by policy |
|---|---|
| `BLR`, `DEL`, `BOM` | `B`, `DELHI`, `1234` |

Choose the declaration that encodes the documented length rule.

A. A fixed-length `CHAR(3)` — the values never vary in length.  
B. `VARCHAR(300)`, to be generous about the uncertain future ahead.  
C. `TEXT`, since codes are text.  
D. `INTEGER`, mapping each airport to a number.

### 8. The admin tool that needs nothing fancy

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Primary Key Strategies  
**Is Curriculum Based:** No  
**Assessment type:** Strategy matching

An internal expense-approval database has this operating profile:

| Property | Evidence |
|---|---|
| Writers | One central database |
| Users | A few dozen employees |
| Public exposure | None |
| Future merging | Not planned |

Approve the least costly key strategy that meets the stated needs.

A. UUIDs, since they are the newer option.  
B. Composite keys built from user names and specific dates together.  
C. Auto-incrementing integers: simple, compact, and fast.  
D. No primary key, since the tool is internal.

### 9. The two quiet timestamps

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Audit Columns and Soft Deletes  
**Is Curriculum Based:** No  
**Assessment type:** Purpose identification

A ticketing platform adds two automatically maintained columns:

| Column | Example value |
|---|---|
| `created_at` | `2026-04-02 09:10` |
| `updated_at` | `2026-04-08 16:45` |

Use the two fields to complete the platform's audit capability statement.

A. Faster queries on all tables.  
B. A record of when each row was created and last changed.  
C. Automatic deletion of old, stale rows periodically every night.  
D. Encryption of sensitive values.

### 10. Pick one and never look back

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Naming Conventions  
**Is Curriculum Based:** No  
**Assessment type:** Consistency selection

Four teams submit naming proposals for the same new database:

| Proposal | Table names |
|---:|---|
| 1 | `Customers`, `order_items`, `Product`, `SHIPMENTS` |
| 2 | `customer`, `orders`, `Product_Item`, `shipments` |
| 3 | `tblCust`, `tbl_orders`, `TBLPRODUCTS`, `tbl-ship` |
| 4 | `customers`, `orders`, `products`, `shipments` |

Select the proposal a naming review should approve unchanged.

A. Proposal 1 — variety keeps names memorable.  
B. Proposal 2 — mixing singular and plural covers everyone's tastes nicely.  
C. Proposal 3 — prefixes make tables findable.  
D. Proposal 4 — one convention applied without exception.

### 11. True, false, and nothing else

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Choosing the Right Data Type  
**Is Curriculum Based:** No  
**Assessment type:** Type-selection judgment

A gym database uses `is_active` to record whether a membership can currently be used:

| membership_id | Draft `VARCHAR(10)` value | Intended meaning |
|---|---|---|
| M1 | `yes` | Active |
| M2 | `Y` | Active |
| M3 | `active` | Active |
| M4 | `no` | Inactive |

Replace the draft field with the type that admits only the two intended states.

A. A `BOOLEAN` column like `is_active`, true or false only.  
B. Standardizing on the string `"yes"` by informal team agreement only.  
C. An integer column storing 1, 2, or 3.  
D. Keeping the text column but adding a spell-checker.

### 12. What UUIDs charge for their independence

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Primary Key Strategies  
**Is Curriculum Based:** No  
**Assessment type:** Tradeoff analysis

A team compares key strategies for a product whose records may be created by independent services:

| Property | Auto-increment integer | UUID |
|---|---|---|
| Generation | Central counter | Independent |
| Storage | Compact | Larger |
| Natural order | Increasing | Unordered |

Complete the tradeoff note without hiding either the benefit or the cost.

A. UUIDs are smaller than integers but slower to generate.  
B. UUIDs and integers have the same size, ordering, and generation method.  
C. UUIDs buy independent generation but cost more storage per key.  
D. Integers cannot serve as primary keys in modern databases.

### 13. Case closed on case

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Naming Conventions  
**Is Curriculum Based:** No  
**Assessment type:** Naming selection

A food-delivery database has documented plural table names and snake_case columns:

| Existing table | Existing columns |
|---|---|
| `orders` | `order_id`, `customer_id` |
| `delivery_zones` | `zone_id`, `zone_name` |

Fill the proposed fee column name so a teammate can predict it from the existing schema.

A. `DeliveryFee`, PascalCase.  
B. `delivery_fee`, per the snake_case column rule.  
C. `deliveryFee`, camelCase.  
D. `DELIVERY-FEE`, hyphenated and uppercase throughout.

### 14. Design the way back

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Audit Columns and Soft Deletes  
**Is Curriculum Based:** No  
**Assessment type:** Recovery-path design

A banking app marks closed accounts instead of removing them:

| account_id | customer_name | deleted_at | Transaction history |
|---|---|---|---|
| A72 | Diya Shah | `2025-11-04 14:20` | Still linked |

The customer is approved for reactivation with the existing history intact.

Choose the smallest database change that restores the existing account.

A. Restore last year's full database backup over the live system.  
B. Create a new account and ask the customer to re-enter their history.  
C. Nothing can be done; deletion is deletion.  
D. Clear the `deleted_at` marker on the account's row, a single update.

### 15. One grant instead of forty

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Database Schemas and Namespaces  
**Is Curriculum Based:** No  
**Assessment type:** Access-control application

A retailer groups tables and required access as follows:

| Schema | Tables | Analyst requirement |
|---|---:|---|
| `reporting` | 40 | Read |
| `sales` | 25 | None |
| `inventory` | 18 | None |

Select the access change that matches the analyst team's boundary.

A. Granting read access on the `reporting` schema as a group.  
B. Nothing; permissions are always per-table.  
C. Giving the analysts the admin password.  
D. Emailing the analysts nightly exports instead, manually every time.

### 16. The table where updates hit twins

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Schema Design Review  
**Is Curriculum Based:** No  
**Assessment type:** Missing-key consequence

A factory database has no primary key on `machine_readings`:

| machine_code | recorded_at | temperature |
|---|---|---:|
| MX7 | `2026-05-01 10:00` | 92.4 |
| MX7 | `2026-05-01 10:00` | 92.4 |

An engineer tries to correct only one of the two rows, but the matching update changes both.

The failed correction demonstrates the loss of:

A. Disk space only.  
B. Nothing; identical rows remain separately addressable without any identifying key column.  
C. Row identity: with no key, one row can't be addressed versus its twin.  
D. Backup speed.

### 17. The thirty-first of February

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Choosing the Right Data Type  
**Is Curriculum Based:** No  
**Assessment type:** Typed-column rationale

A clinic stores appointment dates in a free-text field:

| appointment_id | appointment_date_text |
|---|---|
| A1 | `31/02/2025` |
| A2 | `Feb 31` |
| A3 | `soonish` |

Choose the protection that a real `DATE` column would have provided at insertion and retrieval.

A. Prettier printing of the dates.  
B. Nothing; text already rejects impossible calendar values during insertion.  
C. Larger storage for long dates.  
D. Rejection of impossible values, plus real date sorting behavior.

### 18. Why the invoices must only pretend to die

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Audit Columns and Soft Deletes  
**Is Curriculum Based:** No  
**Assessment type:** Pattern-selection rationale

An e-commerce system has two stated requirements:

| Requirement | Meaning |
|---|---|
| Dashboard | Cancelled invoices must disappear from ordinary merchant views |
| Retention policy | Invoice rows must remain recoverable for seven years |

Select the design that satisfies both requirements simultaneously.

A. Hard deletes are slower to execute.  
B. It satisfies both masters: hidden from queries, kept years.  
C. Soft deletes compress the table.  
D. It grants every merchant permission to edit every retained invoice.

### 19. Four columns, four types

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Choosing the Right Data Type  
**Is Curriculum Based:** No  
**Assessment type:** Type-set selection

A hardware store defines four order-line facts:

| Column meaning | Example |
|---|---|
| Quantity of units | `4` |
| Unit price in rupees and paise | `249.50` |
| Gift note | `Leave at reception` |
| Delivered flag | `true` |

Complete the four-column design with types matching the shown values.

A. All four as `VARCHAR(100)` for flexibility.  
B. Quantity `FLOAT`, price `FLOAT`, note `CHAR(10)`, flag `INTEGER`, because all four can store numbers.  
C. Quantity `INTEGER`, price `DECIMAL`, note `VARCHAR`, flag `BOOLEAN`.  
D. Quantity `BOOLEAN`, price `DATE`, note `TEXT`, flag `CHAR(1)`.

### 20. The merge that minted twins

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Primary Key Strategies  
**Is Curriculum Based:** No  
**Assessment type:** Failure diagnosis

Two regional gyms generated auto-incrementing member IDs independently:

| Source database | Existing member-ID range |
|---|---|
| North region | 1–4,000 |
| South region | 1–4,000 |

Their records must now be merged into one chain-wide table.

The collision report should record this design limitation:

A. Auto-increment guarantees uniqueness only within one database.  
B. The import tool was too slow.  
C. Removing member IDs avoids collisions during the combined import.  
D. One gym's members must be deleted.

### 21. The column called `order`

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Naming Conventions  
**Is Curriculum Based:** No  
**Assessment type:** Reserved-word avoidance

A furniture database uses a column named `order` for the sequence of delivery attempts:

| Current column | Intended meaning | Developer experience |
|---|---|---|
| `order` | First, second, or third attempt | Queries fail or require quoting |

Diagnose the recurring need for quotes before proposing a rename.

A. Columns may not describe purchases.  
B. The name is too short to index.  
C. A reserved word is acceptable only when used as a table name.  
D. `order` collides with the database's reserved vocabulary.

### 22. When did this row last change?

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Audit Columns and Soft Deletes  
**Is Curriculum Based:** No  
**Assessment type:** Column-role application

A support engineer inspects this product row after a customer reports a wrong price:

| product_id | price | created_at | updated_at |
|---|---:|---|---|
| P18 | 849.00 | `2025-02-10 09:00` | `2026-07-03 17:42` |

Select the field that answers the support engineer's exact question.

A. `product_id`  
B. `updated_at`, recording the row's most recent change.  
C. `created_at` — when the row first originally appeared here.  
D. `price` itself.

### 23. Two tables named settings

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Database Schemas and Namespaces  
**Is Curriculum Based:** No  
**Assessment type:** Collision-resolution application

A gaming company has one physical database and two ownership boundaries:

| Team | Desired table name | Contents |
|---|---|---|
| Platform | `settings` | Game-service configuration |
| Payments | `settings` | Payment-provider configuration |

Assign the two tables full names that can coexist without ambiguity.

A. Each team's table lives in its own separate schema.  
B. One team must rename to `settings2`.  
C. The tables must be merged into one.  
D. The second team stores its settings outside the database.

### 24. The city that rode along on every order

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Schema Design Review  
**Is Curriculum Based:** No  
**Assessment type:** Redundancy detection

A flower-delivery table repeats customer facts on every purchase. `order_id` identifies an order and `customer_id` identifies the buyer:

| order_id | customer_id | customer_name | customer_city | customer_phone |
|---|---|---|---|---|
| O1 | C7 | Leena Rao | Mysuru | 98450 11111 |
| O2 | C7 | Leena Rao | Mysuru | 98450 11111 |
| O3 | C9 | Arun Das | Kochi | 98950 22222 |

The production table has 60,000 orders but only 9,000 customers.

The schema-review ticket should flag:

A. The orders table needs even more customer columns for full completeness.  
B. Nothing — copying is a performance feature by default.  
C. Redundant data that should have been normalized into its own table.  
D. The customers should be deleted.

### 25. `cst_adr_ln1`

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Naming Conventions  
**Is Curriculum Based:** No  
**Assessment type:** Abbreviation critique

A decade-old database exposes these names to every developer:

| Column name | Meaning found in an old legend |
|---|---|
| `cst_adr_ln1` | Customer address line 1 |
| `prd_ctg_cd` | Product category code |
| `shp_dt` | Shipment date |

The author has left, and new engineers cannot interpret the names without the legend.

Record the maintenance cost created by this abbreviation strategy.

A. They save meaningful storage space.  
B. Abbreviations only the author understood tax everyone after them.  
C. They are suitable if a separate abbreviation guide is kept current.  
D. Vowels are optional in professional schemas.

### 26. The word "schema," twice

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Database Schemas and Namespaces  
**Is Curriculum Based:** No  
**Assessment type:** Term disambiguation

A junior engineer hears the same word in two review notes:

| Statement | Context |
|---|---|
| “The schema has a flaw.” | Reviewing a table's columns, types, and keys |
| “Put that table in the `analytics` schema.” | Organizing tables inside one database |

Match each statement to the intended meaning of “schema.”

A. Only the design document uses the word correctly; a DBA must use “folder” instead.  
B. Both uses mean table design.  
C. Both uses mean folders.  
D. Two meanings share one word here: folder versus design.

### 27. Names stretch, codes don't

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Choosing the Right Data Type  
**Is Curriculum Based:** No  
**Assessment type:** Fixed-versus-variable pairing

A trade platform documents two text fields:

| Field | Observed/policy length |
|---|---|
| Customer name | Varies from 2 to more than 60 characters |
| Country code | Exactly 2 letters |

Complete the type mapping from the two documented length patterns.

A. Names in `VARCHAR`, country codes in fixed `CHAR(2)`.  
B. Both in `CHAR(60)`, padded with spaces.  
C. Names in `CHAR(2)`, country codes in `VARCHAR(60)` so both fields have spare capacity.  
D. Both as `INTEGER` lookups only.

### 28. Four situations, two counters, two mints

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Primary Key Strategies  
**Is Curriculum Based:** No  
**Assessment type:** Multi-situation matching

Four systems need key strategies:

| System | Record-creation pattern |
|---:|---|
| 1 | One warehouse; one central inventory database |
| 2 | Offline IoT sensors; weekly merge |
| 3 | Internal HR; one writer and one database |
| 4 | Independent regional databases; eventual merge |

Assign a key strategy to all four systems.

A. UUIDs for all four, always.  
B. Integers for all four, always.  
C. Integers for 1 and 3; UUIDs for 2 and 4.  
D. UUIDs for 1 and 3; integers for 2 and 4.

### 29. One rule for the whole team

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Naming Conventions  
**Is Curriculum Based:** No  
**Assessment type:** Consistency rationale

A logistics database currently contains:

| Name | Style |
|---|---|
| `Trip` | Singular PascalCase |
| `driver_logs` | Plural snake_case |
| `VEHICLES` | Plural uppercase |
| `fuelEntries` | Plural camelCase |

Choose the reason that follows from the evidence rather than inventing a performance effect.

A. Lowercase identifiers reduce both row storage and the time required to execute every query.  
B. Mixed names are illegal SQL.  
C. Regulators audit naming style.  
D. Predictability: one convention lets anyone guess any name correctly.

### 30. The deleted rows that came back at quarter end

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Audit Columns and Soft Deletes  
**Is Curriculum Based:** No  
**Assessment type:** Discipline-failure diagnosis

A CRM stores cancelled subscriptions using `deleted_at`. A new revenue report produces:

| Rows included | Revenue |
|---|---:|
| Active subscriptions only | ₹8,20,000 |
| New query result | ₹8,74,000 |

The new query did not test `deleted_at IS NULL`.

Diagnose the inflated result and identify the missed soft-delete obligation.

A. The soft-deleted rows resurrected themselves.  
B. The query counted rows still physically present but logically deleted.  
C. Finance misread correct numbers.  
D. Soft deletes should be replaced with hard deletes in every reporting table to prevent double-counting.

### 31. Draw the folder boundaries

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Database Schemas and Namespaces  
**Is Curriculum Based:** No  
**Assessment type:** Namespace design

A hotel group plans one physical database:

| Table group | Owning team | Access boundary |
|---|---|---|
| Reservations | Guest-services team | Operational read/write |
| Staff payroll | Finance team | Restricted read/write |
| Analytics | Reporting team | Reporting access |

Approve the namespace layout that mirrors ownership and access boundaries.

A. Three schemas: `reservations`, `payroll`, `analytics`, per team.  
B. One schema holding all tables, with a detailed naming wiki instead.  
C. One schema per table, ninety schemas in all.  
D. Three separate database servers, one per team.

### 32. The audit that starts with a missing paisa

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Schema Design Review  
**Is Curriculum Based:** No  
**Assessment type:** Symptom-to-flaw diagnosis

During review, a payments table shows:

| Stored balance | Expected financial value |
|---:|---:|
| `104.99999999999` | `105.00` |
| `249.50000000003` | `249.50` |

Reconciliation drifts by a paisa after several thousand transactions.

Trace this numeric signature back to its schema-level cause.

A. A missing primary key.  
B. Inconsistent capitalization in the table names, which changes the stored balance digits.  
C. Money stored in an imprecise floating type, leaking tiny errors.  
D. An oversized VARCHAR.

### 33. The "fix" that isn't one

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Schema Design Review  
**Is Curriculum Based:** No  
**Assessment type:** Repair critique

An invoicing review records:

| Finding | Risk |
|---|---|
| `Price FLOAT` | Stored money is approximate |

Four repairs are proposed. Three address the data or the review process; one leaves approximate money in storage.

Reject the proposal that leaves the original storage defect in place.

A. Migrate the column to an exact decimal type.  
B. Audit historical totals for accumulated drift after migrating fully.  
C. Add a review checklist so money-as-float is caught at design time.  
D. Keep the FLOAT column, rounding every result in application code.

### 34. A billion little rows

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Primary Key Strategies  
**Is Curriculum Based:** No  
**Assessment type:** Constraint-driven selection

A telemetry database has these constraints:

| Property | Evidence |
|---|---|
| Row count | Billions |
| Writers | One server-side writer |
| Database | One central instance |
| Dominant cost | Key and index storage |
| Public identifiers | Not exposed |

Approve the key strategy selected by the dominant constraint.

A. UUIDs, for their global uniqueness.  
B. Auto-incrementing integers, with no collision risk here.  
C. The full timestamp as a text key.  
D. No key at all, to save the absolute most possible space here today.

### 35. Five statuses, five hundred characters

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Choosing the Right Data Type  
**Is Curriculum Based:** No  
**Assessment type:** Over-generous-type critique

A parcel tracker declares `status VARCHAR(500)`, although the intended values are `created`, `packed`, `shipped`, `delivered`, and `returned`.

| Row | Stored status |
|---|---|
| 1 | `shipped` |
| 2 | `shiped` |
| 3 | `delivered to neighbour, dog was barking` |

The review note should conclude:

A. Statuses need even more room, not less.  
B. Every text column should use `VARCHAR(500)` for consistent storage and validation rules.  
C. A too-generous type is an open door for stray values to enter.  
D. Statuses should be stored as floats.

### 36. What the counter actually promises

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Primary Key Strategies  
**Is Curriculum Based:** No  
**Assessment type:** Mechanism understanding

A bakery lets its single database assign order IDs:

| Insert order | Assigned `order_id` |
|---:|---:|
| First | 1 |
| Second | 2 |
| Third | 3 |

Complete the mechanism description from the observed sequence.

A. The database itself hands each new row the next number automatically.  
B. The application must query the current maximum and add one itself manually.  
C. The numbers repeat once they reach 10,000.  
D. Each clerk is assigned a personal number range to type in.

### 37. The convention nobody wrote down

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Naming Conventions  
**Is Curriculum Based:** No  
**Assessment type:** Practice application

A scooter-rental database is moving from two authors to twenty:

| Current practice | New risk |
|---|---|
| Naming rules exist only in founders' memory | New tables may use incompatible cases and patterns |

Select the action that converts personal habit into a team convention.

A. Let each engineer adopt a personal style for the tables they create.  
B. Rename all tables quarterly to stay fresh.  
C. Keep conventions oral to stay agile.  
D. Write the convention down: case style and naming pattern.

### 38. Which timestamp moves?

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Audit Columns and Soft Deletes  
**Is Curriculum Based:** No  
**Assessment type:** Column-behaviour discrimination

A rental platform shows this listing:

| listing_id | created_at | updated_at |
|---|---|---|
| L42 | `2024-03-01` | `2025-06-18` |

Interpret the two timestamps without inventing an extra event.

A. The row was created twice.  
B. Both timestamps are replaced whenever any field is edited after the row was first created.  
C. `created_at` is set once; `updated_at` moves with each edit.  
D. The columns are in the wrong order.

### 39. Cutting off the contractors

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Database Schemas and Namespaces  
**Is Curriculum Based:** No  
**Assessment type:** Group-access application

An engineering firm's access register shows:

| Role | Schema | Access | Tables covered |
|---|---|---|---:|
| Contractors | `projects` | Read | 30 |

The engagement ends, so the entire permission must be withdrawn today.

Choose the revocation matching the level at which access was granted.

A. Thirty separate individual revocations, one for each table here.  
B. A single revocation at the `projects` schema level.  
C. A password change for the whole database.  
D. A physical deletion of the thirty tables.

### 40. The corrected design

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Database Design & Modeling  
**Subtopic:** Schema Design Review  
**Is Curriculum Based:** No  
**Assessment type:** Integrated correction selection

The courier table stores one row per shipment. `shipment_charge` is the exact customer charge and `destination` is its delivery location. Review finds:

| Current design element | Problem |
|---|---|
| Table `Shipment` and column `Price` | Inconsistent naming |
| `Price FLOAT` | Approximate money |
| No identifying column | Rows lack a primary key |
| No timestamps | Creation and modification times unavailable |

Approve the redesign that closes every documented finding.

A. `shipments(shipment_id PK, shipment_charge DECIMAL, destination VARCHAR, created_at TIMESTAMP, updated_at TIMESTAMP)`.  
B. `shipments(Price FLOAT, dest VARCHAR)`, with the table name changed only.  
C. `Shipment(price FLOAT UNIQUE, dest VARCHAR)`, using uniqueness to address rounding.  
D. `shipments(reference VARCHAR, shipment_charge DECIMAL, destination VARCHAR, created_at TIMESTAMP, updated_at TIMESTAMP)`, without a primary key.

---

## Instructor Key

### 1. B

Binary floating point cannot represent most decimal fractions exactly, so each 19.99 is stored as a near-miss and thousands of near-misses add up to visible drift. Exact decimal types store the value the invoice actually says; rounding in app code (A) treats the symptom while every other query stays wrong.

### 2. D

The requirements — key at creation, offline, many independent generators, zero collision tolerance — are the UUID use case verbatim. Per-tablet counters (A) guarantee collisions at sync; server renumbering (B) violates "permanent at creation."

### 3. A

The convention: a foreign key is named after what it points to. `warehouse_id` makes every query self-documenting; `wh`, `ref_1`, and `location_data` each force the reader to go look something up.

### 4. C

Setting a `deleted_at` timestamp and filtering it out of normal queries is the soft-delete pattern: gone from the app's perspective, present in the table for history, audits, and recovery.

### 5. D

Schemas are named folders within one database: related tables grouped, identical table names allowed in different folders, and permissions grantable per folder. They are organization, not hardware (A).

### 6. B

Three findings from the chapter's common-mistakes list are present: no primary key, money in `FLOAT`, and naming that mixes PascalCase with snake_case and an unexplained shortening. Reporting only `dest` would leave the two riskier flaws untouched.

### 7. A

When a value's length is a rule (exactly three letters), the fixed CHAR(3) encodes that rule in the type. VARCHAR(300) (B) documents nothing and accepts anything.

### 8. C

One central database handing out numbers is precisely where auto-increment shines: simple, compact, fast. Reaching for UUIDs by fashion (A) pays their storage cost and buys nothing this tool needs.

### 9. B

Audit columns are the schema's memory of time: when each row appeared and when it last changed. They speed up investigations, not queries (A).

### 10. D

The chapter's rule is not "plural is right" but "pick one and never look back." Proposal 4 is the only one applying a single convention uniformly; every other proposal makes future engineers guess per table.

### 11. A

A boolean column makes illegal states unrepresentable — the five spellings of "yes" collapse into `true`. Team agreements about strings (B) decay; types endure.

### 12. C

The chapter's tradeoff, both sides: UUIDs grant coordination-free global uniqueness, and charge for it in key size and unordered arrival. Choosing without weighing (A, B, D) is exactly what "tradeoffs nobody should skip past" warns against.

### 13. B

One convention, all identifiers: snake_case for tables means snake_case for columns. `delivery_fee` is the only candidate a teammate could have predicted sight unseen.

### 14. D

Soft delete's payoff scene: because the delete was a marker, recovery is clearing the marker. The row, its balances, and its history were never gone — no backups (A), no re-entry (B).

### 15. A

Schemas make permissions match team structure: the team can receive read access across the current reporting tables as one group instead of forty unrelated grants. Future tables inherit that access only if the database's default-permission policy is configured accordingly.

### 16. C

A primary key is the ability to say "this row and not that one." Without it, exact duplicates are legal and unaddressable, and any targeted correction becomes a broadside hitting everything that matches.

### 17. D

A typed column is a bouncer: impossible dates never enter, and real date semantics (ordering, ranges, arithmetic) come free. Free text stored the strings happily and made "next 7 days" unanswerable.

### 18. B

The pattern's defining virtue is serving two contradictory requirements: user-facing disappearance and legal-facing retention, in one table, with one timestamp column.

### 19. C

Each fact gets the type that matches its nature: counted units (integer), exact currency (decimal), variable prose (varchar), and a two-state flag (boolean). Any all-text scheme (A) surrenders validation, math, and meaning at once.

### 20. A

Each database's counter was a local authority, and local authorities issue overlapping numbers. The merge is where that latent assumption becomes a visible collision — and the scenario UUIDs exist to preempt.

### 21. D

Shadowing the database's own vocabulary sentences every future query to quoting. The convention costs nothing at design time (`purchase_order`) and the alternative costs a little forever.

### 22. B

"Last modified" is the definition of `updated_at`. `created_at` answers a different question — when the row was born — and the price column says what, never when.

### 23. A

Namespaces exist so both teams keep the natural name: `platform.settings` and `payments.settings` are distinct full names. Renaming (B) solves the collision by making one name worse.

### 24. C

Nine thousand customers' facts stored sixty thousand times is the redundancy normalization removes: customer data lives once in `customers`, and orders carry only the key. As drafted, one customer's move means chasing every order they ever placed.

### 25. B

Names are read hundreds of times and written once, so the economics favour the reader. Compressed names shift the cost onto every future engineer — with a side effect that the legend leaves when its author does.

### 26. D

The chapter's disambiguation: here, a schema is a folder — a namespace grouping tables — not the table design the word also means elsewhere. Both parties are speaking correctly, in two different senses.

### 27. A

The rule keys off the value's nature: genuinely varying lengths take VARCHAR; a length that is itself a rule of the format (exactly two letters) takes CHAR. Option B pads names with spaces for no benefit.

### 28. C

Situations 1 and 3 have one central counter and no merge horizon — the integer's home ground. Situations 2 and 4 feature independent generators and merging — the two problems UUIDs exist to solve. Blanket answers ignore the situations entirely.

### 29. D

The payoff of convention is predictability: names become guessable, so nobody detours to check spelling before writing a query. Four styles in one schema means four guesses per query.

### 30. B

Soft-deleted rows are physically present by design, so every query must opt out of them explicitly. The forgotten filter is the pattern's recurring tax — which is why teams standardize the filter or hide it behind a view.

### 31. A

Folders that mirror the team and access boundaries: each schema groups one team's tables and takes one team's permissions. Ninety single-table schemas (C) create folders with nothing to group; separate servers (D) buy isolation the problem never asked for.

### 32. C

Impossible trailing digits on money and totals that drift by the smallest unit are floating point's fingerprints. No other listed flaw manufactures values the business never entered.

### 33. D

Rounding at display keeps the approximation in storage and turns correctness into a ritual every future query must remember. The other three repairs fix the data, the history, and the process; option D decorates the bug.

### 34. B

One writer eliminates collision risk, so UUIDs' selling point buys nothing here — while their extra bytes multiply across billions of keys and every index entry. The compact integer is what the constraints, not fashion, select.

### 35. C

The 500-character allowance contradicts the field's short, controlled meaning and admits accidental prose. A sensible bound documents the intended shape and rejects oversized entries; additional validation may still be needed to prevent misspellings such as `shiped`.

### 36. A

Auto-increment is the database's own counter: keys are assigned at insert, uniquely, with zero application coordination. Option B describes the fragile manual pattern the mechanism exists to replace.

### 37. D

A convention that lives in two founders' heads stops scaling at two. Writing it down — cases, plurality, FK patterns, banned words — is what turns personal habit into team predictability.

### 38. C

The two columns divide time between them: birth (set once, immutable) and latest change (moves with every edit). Read together they say: created March 2024, last touched June 2025.

### 39. B

Access granted at the group boundary can be withdrawn at that same boundary: one schema-level revocation removes the contractors' access across the thirty covered project tables.

### 40. A

Every checklist item lands: `shipment_id` restores row identity, `DECIMAL` keeps the charge exact, the names are descriptive snake_case, and the two timestamps preserve creation and modification history. The other proposals leave several original defects intact.

---

## Question-Type Distribution

| Higher-order assessment family | Question numbers |
|---|---|
| Type selection and critique | 1, 7, 11, 17, 19, 27, 35 |
| Key-strategy matching and diagnosis | 2, 8, 12, 20, 28, 34, 36 |
| Naming selection and rationale | 3, 10, 13, 21, 25, 29, 37 |
| Audit and soft-delete mechanics | 4, 9, 14, 18, 22, 30, 38 |
| Schema and namespace application | 5, 15, 23, 26, 31, 39 |
| Design review and repair judgment | 6, 16, 24, 32, 33, 40 |

## Blueprint Taxonomy Coverage

| Subtopic from the attached blueprint | Question numbers | Count |
|---|---|---:|
| Choosing the Right Data Type | 1, 7, 11, 17, 19, 27, 35 | 7 |
| Primary Key Strategies | 2, 8, 12, 20, 28, 34, 36 | 7 |
| Naming Conventions | 3, 10, 13, 21, 25, 29, 37 | 7 |
| Audit Columns and Soft Deletes | 4, 9, 14, 18, 22, 30, 38 | 7 |
| Database Schemas and Namespaces | 5, 15, 23, 26, 31, 39 | 6 |
| Schema Design Review | 6, 16, 24, 32, 33, 40 | 6 |

Questions 1–10 collectively cover all six Topic 2.3 subtopics.

## Difficulty and Answer-Key Balance

- Foundational: 11 questions (9, 10, 11, 13, 14, 19, 21, 22, 29, 35, 38)
- Intermediate: 26 questions
- Advanced: 3 questions (6, 28, 40)
- Correct option A: 10 questions (3, 7, 11, 15, 20, 23, 27, 31, 36, 40)
- Correct option B: 10 questions (1, 6, 9, 13, 18, 22, 25, 30, 34, 39)
- Correct option C: 10 questions (4, 8, 12, 16, 19, 24, 28, 32, 35, 38)
- Correct option D: 10 questions (2, 5, 10, 14, 17, 21, 26, 29, 33, 37)
- Longest consecutive run of one correct letter: below 3 throughout
