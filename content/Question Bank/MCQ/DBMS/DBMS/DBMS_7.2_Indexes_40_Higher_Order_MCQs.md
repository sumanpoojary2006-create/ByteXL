# DBMS 7.2: Indexes — 40 Higher-Order MCQs

## Assessment specifications

- **Subject:** DBMS
- **Topic:** Performance
- **Chapter:** Indexes
- **Scope:** All five Topic 7.2 subtopics in the attached course blueprint (What is an Index; B-Tree Indexes; Hash, Composite, Partial, and Expression Indexes; Covering Indexes and Index-Only Scans; When Not to Index)
- **SQL dialect:** PostgreSQL
- **Format:** Four options with exactly one best answer
- **Curriculum flag:** No
- **Design standard:** Questions begin with a recognisable workload and show the query, index definition, plan evidence, selectivity, projected columns, or measured write cost needed to choose one defensible answer.
- **Evidence rule:** Students never need to invent column cardinality, query frequency, index order, partial predicate, included columns, visibility state, or existing overlapping indexes when those facts determine the answer.
- **Scope guard:** Questions use only Topic 7.2 material. Detailed optimizer estimation and broader execution-plan tuning belong to Topic 7.3.
- **Answer-quality controls:** A/B/C/D each correct exactly 10 times, no letter correct more than twice consecutively, no correct answer identifiable by length.
- **Coverage rule:** Questions 1–10 collectively cover all five Topic 7.2 subtopics.
- **Student/instructor separation:** Questions appear first; answers and explanations follow in the instructor key.

---

## Questions

### 1. The thing CREATE INDEX creates

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** What is an Index  
**Is Curriculum Based:** No  
**Assessment type:** Nature identification

A freight platform runs:

```sql
CREATE INDEX idx_awb ON shipments(awb_number);
```

Select the physical object created beside the `shipments` heap.

A. A second full copy of every shipment column, physically sorted by AWB number.  
B. A cache containing only AWB lookup results from queries already executed.  
C. A uniqueness rule that rejects two shipments sharing one AWB number.  
D. A separate, ordered structure mapping each `awb_number` to its row's location.

### 2. A million rows, four hops

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** B-Tree Indexes  
**Is Curriculum Based:** No  
**Assessment type:** Depth-scaling reasoning

A policy B-tree grows as follows:

| indexed rows | observed root-to-leaf page reads |
|---:|---:|
| 100,000 | 3 |
| 100,000,000 | 4–5 |

Select the structural explanation for this scaling.

A. PostgreSQL removed older policy keys whenever a leaf page filled.  
B. A B-tree grows wider far faster than it grows deeper; depth climbs slowly.  
C. Keys inserted after index creation remain outside the tree until a manual rebuild.  
D. Every page became 1,000 times larger as the policy table grew.

### 3. Index the 2%, ignore the 98%

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Hash, Composite, Partial, and Expression Indexes  
**Is Curriculum Based:** No  
**Assessment type:** Partial-index selection

A support desk reports:

| total tickets | open tickets | dashboard predicate |
|---:|---:|---|
| 5,000,000 | about 100,000 | `status = 'open'` |

The dashboard groups open tickets by `assigned_to`.

Choose the smallest index aligned with the dashboard.

A. `CREATE INDEX ON tickets(assigned_to) WHERE status = 'open';`  
B. A full index on every ticket column so any future query has some structure.  
C. No index, because a predicate matching only 2% cannot benefit from one.  
D. `CREATE INDEX ON tickets(assigned_to) WHERE status = 'closed';`

### 4. The query that never touched the table

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Covering Indexes and Index-Only Scans  
**Is Curriculum Based:** No  
**Assessment type:** Index-only-scan identification

A vacuumed orders table produces:

| query | plan | heap fetches |
|---|---|---:|
| `SELECT customer_id, order_date FROM orders WHERE customer_id = 3321` | Index Only Scan | 0 |

Choose the evidence required for this outcome.

A. The query returned no row, so PostgreSQL labelled a sequential scan as index-only.  
B. The index contains only `customer_id`; PostgreSQL reconstructs `order_date` from the key value itself.  
C. The index contains every referenced column, and visibility permits avoiding the heap.  
D. Index-only scans omit non-key columns and return an approximate projection.

### 5. The tax every INSERT pays

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** When Not to Index  
**Is Curriculum Based:** No  
**Assessment type:** Write-cost reasoning

A telemetry benchmark shows:

| table design | secondary indexes | inserts/second |
|---|---:|---:|
| Before | 1 | 18,000 |
| After | 5 | 10,500 |

Select the most direct explanation for the measured difference.

A. Each INSERT now updates the table and all five indexes too.  
B. Each index forces a fixed one-second table lock for every inserted row.  
C. PostgreSQL supports at most four indexes, so the fifth triggers compatibility mode.  
D. Indexes increase response-network traffic but do not add storage-engine work.

### 6. Before and after, in the plan

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** What is an Index  
**Is Curriculum Based:** No  
**Assessment type:** Plan-change identification

A vehicle lookup has two plan observations:

| state | plan |
|---|---|
| Before `CREATE INDEX` | `Seq Scan on vehicles` |
| After `CREATE INDEX ON vehicles(plate_no)` | ? |

Complete the second plan and interpret it.

A. Seq Scan again, because a new index cannot affect an existing SQL statement.  
B. Sort, because PostgreSQL must reorder the whole table before looking up a plate.  
C. Two sequential scans, one over the heap and one over the index.  
D. An Index Scan using the new index — the planner found a cheaper path.

### 7. What the sorted tree is naturally good at

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** B-Tree Indexes  
**Is Curriculum Based:** No  
**Assessment type:** Capability-set reasoning

A bookings table has a B-tree on `booked_on`:

| query | operation |
|---:|---|
| 1 | `booked_on = DATE '2025-06-01'` |
| 2 | `booked_on BETWEEN DATE '2025-06-01' AND DATE '2025-06-30'` |
| 3 | `ORDER BY booked_on LIMIT 10` |

Choose the capability set supplied by the sorted tree.

A. Only query 1; B-trees lose ordering information after finding an equality match.  
B. All of them — sorted keys serve matches, ranges, and ordering alike.  
C. Only queries 2 and 3; equality predicates require a hash index.  
D. None; B-trees support only MIN and MAX calculations.

### 8. The lowercase that defeated the index

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Hash, Composite, Partial, and Expression Indexes  
**Is Curriculum Based:** No  
**Assessment type:** Expression-index selection

A signup service has `CREATE INDEX idx_email ON users(email);`, but its hot query is:

```sql
SELECT * FROM users
WHERE LOWER(email) = 'r.iyer@volt.in';
```

Complete the smallest index repair.

A. Create another plain index on raw `email` under a different name.  
B. Create an index on `username`, because the email contains a username component.  
C. `CREATE INDEX ON users (LOWER(email));` to store the searched expression.  
D. Create a hash index on raw `email`; hash access automatically applies `LOWER`.

### 9. Adding the payload

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Covering Indexes and Index-Only Scans  
**Is Curriculum Based:** No  
**Assessment type:** INCLUDE construction

The hot query and existing index are:

```sql
SELECT order_date, total
FROM orders
WHERE customer_id = 3321;

CREATE INDEX idx_customer ON orders(customer_id);
```

Choose the smallest replacement that can cover the query.

A. `CREATE INDEX ON orders (customer_id) INCLUDE (order_date, total);`.  
B. `CREATE INDEX ON orders (order_date, total);` because selected columns must be keys.  
C. `CREATE INDEX ON orders (customer_id);` again under a second index name.  
D. `CREATE INDEX ON orders (total) INCLUDE (customer_id);` without storing `order_date`.

### 10. The column with three values

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** When Not to Index  
**Is Curriculum Based:** No  
**Assessment type:** Low-cardinality judgment

A dispatcher evaluates this distribution:

| priority | rows |
|---|---:|
| low | 2,000,000 |
| normal | 2,000,000 |
| high | 2,000,000 |

The common query is `WHERE priority = 'normal'`.

Select why a plain full index on `priority` is a poor fit for this query.

A. PostgreSQL cannot build indexes on text values.  
B. An index requires at least ten distinct values before PostgreSQL allows CREATE INDEX to succeed.  
C. A three-value column cannot be maintained during UPDATE statements.  
D. The predicate selects about one-third of the table, so a scan may be cheaper.

### 11. Look it up, then go there

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** What is an Index  
**Is Curriculum Based:** No  
**Assessment type:** Lookup-path sequencing

With an index on `passport_no`, the query `WHERE passport_no = 'K8812734'` runs.

What is the two-step path?

A. Scan the heap first, then search the index to verify the value found.  
B. Search the index for K8812734, read off the location, fetch that row.  
C. Read every index leaf and then every heap page, regardless of the matching key.  
D. Search only recent query results because indexes store cached answers rather than locations.

### 12. Root, branches, leaves

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** B-Tree Indexes  
**Is Curriculum Based:** No  
**Assessment type:** Shape identification

A storage diagram needs the correct root-to-leaf structure for a B-tree. Select it.

A. One flat sorted list that must be checked from its first entry for every lookup.  
B. Unordered pages reorganized only during a nightly maintenance job.  
C. A tree: root to internal pages, down to sorted leaf pages.  
D. One disconnected page per distinct key value, with no root directing searches.

### 13. Equality's specialist

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Hash, Composite, Partial, and Expression Indexes  
**Is Curriculum Based:** No  
**Assessment type:** Hash-index characterization

An API performs equality lookup by session token and never requests ranges or ordering. Select the accurate hash-index capability.

A. Hash buckets preserve key order, so the same structure also serves ranges and sorting.  
B. Hash is PostgreSQL's default access method whenever no type is specified.  
C. Hash indexes accept numeric keys only and reject text equality.  
D. They serve equality alone; ranges and ORDER BY get no help at all.

### 14. The extra trip per row

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Covering Indexes and Index-Only Scans  
**Is Curriculum Based:** No  
**Assessment type:** Heap-fetch mechanism

An index on `patient_ref` finds 20 matching entries, but the query also selects `visit_notes`, which the index does not contain.

What must happen for each of the 20 matches?

A. A trip to the table — the index yields the location, fetched for the notes.  
B. No heap visit, because every ordinary index implicitly stores all table columns.  
C. Reconstruct `visit_notes` from the value of `patient_ref` in the WHERE clause.  
D. Return the 20 rows with NULL notes because missing index payload is silently omitted.

### 15. The index nobody ever calls

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** When Not to Index  
**Is Curriculum Based:** No  
**Assessment type:** Waste identification

A year-old index on `warehouses.loading_dock_notes` has never been used by any query — no query filters on that column.

What is this index costing, and earning?

A. It incurs no ongoing cost because PostgreSQL maintains an index only when a SELECT uses it.  
B. It earns nothing while still charging full price on every write and storage.  
C. It speeds all warehouse queries by warming unrelated table pages in the cache.  
D. It improves INSERT speed by moving loading-dock notes out of the heap.

### 16. What you buy and what you pay

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** What is an Index  
**Is Curriculum Based:** No  
**Assessment type:** Trade-off statement

Which sentence states the index bargain correctly?

A. Indexes accelerate reads and writes equally because both follow the same tree.  
B. Indexes slow reads to protect writes.  
C. An index buys faster reads and charges for it on every write, too.  
D. Indexes add storage but have no effect on either read or write work.

### 17. Why the default is the default

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** B-Tree Indexes  
**Is Curriculum Based:** No  
**Assessment type:** Default rationale

`CREATE INDEX` with no type specified builds a B-tree.

Why is the B-tree the sensible default?

A. It is PostgreSQL's only implemented index access method.  
B. It is guaranteed to occupy less disk than every specialist index type.  
C. It is selected because access methods are chosen alphabetically by name whenever CREATE INDEX omits a type.  
D. Versatility: equality, ranges, sorting, and minimum or maximum access in one structure.

### 18. First column first

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Hash, Composite, Partial, and Expression Indexes  
**Is Curriculum Based:** No  
**Assessment type:** Composite-order reasoning

A rides table has one composite index: `(city, ride_date)`.

| query | predicate |
|---:|---|
| 1 | `city = 'Pune'` |
| 2 | `city = 'Pune' AND ride_date = DATE '2025-07-01'` |
| 3 | `ride_date = DATE '2025-07-01'` without `city` |

Which usage claim is correct?

A. Queries 1 and 2 can use the index; query 3 largely cannot, since order matters.  
B. Only query 2 can use it because every composite-index column must appear in a predicate.  
C. All three use it equally because each index column is independently sorted.  
D. Only query 3 can use it because the trailing column is searched before the leading column.

### 19. Why covering isn't automatic

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Covering Indexes and Index-Only Scans  
**Is Curriculum Based:** No  
**Assessment type:** Precondition reasoning

A developer expected an index-only scan, but the plan shows an ordinary index scan with table fetches. The query: `SELECT customer_id, delivery_slot FROM orders WHERE customer_id = 55` — with an index on `customer_id` only.

Why no index-only scan?

A. Index-only scans require the query to omit WHERE and select every table row.  
B. The index doesn't contain `delivery_slot`, reinstating the table trip.  
C. The value 55 is too selective for an index-only scan but suitable for an index scan.  
D. Any SELECT list containing two columns automatically disables index-only scans.

### 20. Two indexes, one job

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** When Not to Index  
**Is Curriculum Based:** No  
**Assessment type:** Redundancy identification

A review finds a table carrying both `INDEX (supplier_id)` and `INDEX (supplier_id, invoice_date)`.

What is the finding?

A. Both are necessarily distinct because index names and key counts differ.  
B. The composite is redundant because a single-column index can serve all two-column filters.  
C. The single-column index is largely redundant with the composite's lead.  
D. Neither can serve a `supplier_id` predicate because both also store row locations.

### 21. The table is innocent

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** What is an Index  
**Is Curriculum Based:** No  
**Assessment type:** Side-effect boundary

A DBA runs `CREATE INDEX` on a busy products table and later drops it again.

What happened to the *table* through all this?

A. Its heap rows were physically sorted during CREATE INDEX and unsorted during DROP INDEX.  
B. Its heap shrank by the index size and expanded again when the index was dropped.  
C. Every table page was rewritten during both commands to embed and remove index keys.  
D. Its row layout stayed unchanged; the separate index structure was built and removed.

### 22. Count the hops

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** B-Tree Indexes  
**Is Curriculum Based:** No  
**Assessment type:** Traversal-cost tracing

A B-tree on 50 million subscription keys is 4 levels deep: root, two internal levels, leaves.

Roughly what does one exact-key lookup cost, and why?

A. About 4 page reads, one per level, from root to leaf holding the address.  
B. About 50 million reads — one per key.  
C. About 4,000 reads — a thousandth of the keys.  
D. One page read because the root stores every subscription key and row address itself.

### 23. Small index, sharp aim

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Hash, Composite, Partial, and Expression Indexes  
**Is Curriculum Based:** No  
**Assessment type:** Partial-benefit computation

The tickets table has:

| total rows | rows satisfying `status = 'open'` | partial-index predicate |
|---:|---:|---|
| 5,000,000 | 100,000 | `status = 'open'` |

Roughly how does it compare to a full-column index?

A. The same number of entries, because a partial predicate affects queries but not index contents.  
B. About one-fiftieth the entries, 100,000 versus 5 million, far smaller.  
C. More than 5 million entries because evaluating the predicate adds one entry per closed row.  
D. About 4.9 million entries because the partial index contains only tickets that are not open.

### 24. What the wider index charges

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Covering Indexes and Index-Only Scans  
**Is Curriculum Based:** No  
**Assessment type:** Trade-off analysis

A team converts a slim index into a covering one by INCLUDE-ing three payload columns, and the hot query goes index-only.

What did the conversion cost?

A. No storage or write cost because INCLUDE changes only planner metadata.  
B. The query results changed slightly.  
C. A bigger index — each entry now carries the payload, costing more storage.  
D. The three included columns were moved out of the table and into the index.

### 25. Nine meters running, one car moving

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** When Not to Index  
**Is Curriculum Based:** No  
**Assessment type:** Over-indexing diagnosis

A telemetry team records:

| insert rate | secondary indexes | unused indexes | write-latency trend |
|---:|---:|---:|---|
| 200/second | 9 | Several | Increased as indexes were added |

What is the structural diagnosis?

A. The index count proves the disk is full, regardless of measured free space.  
B. Telemetry rows cannot be indexed efficiently because they arrive in timestamp order.  
C. Inserts must slow with table age even if no indexes or constraints are added.  
D. Every insert performs ten structure updates now, scaling with index count.

### 26. Read the two plans

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** What is an Index  
**Is Curriculum Based:** No  
**Assessment type:** Plan-pair interpretation

The same query produces:

| state | plan | rows examined/located | elapsed |
|---|---|---:|---:|
| Before | `Seq Scan on parcels` | 8,000,000 | 21 s |
| After | `Index Scan using idx_tracking` | 1 | 0.4 ms |

What do the two plans establish?

A. The index changed the access path from 8 million rows to one direct match.  
B. The only established difference is cache warmth; the named access paths are equivalent.  
C. The table lost 7,999,999 rows when CREATE INDEX completed.  
D. Sequential scans report elapsed time in seconds while index scans report unrelated units.

### 27. Walking the shelf

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** B-Tree Indexes  
**Is Curriculum Based:** No  
**Assessment type:** Range-traversal mechanism

A B-tree on `checkin_date` serves `BETWEEN '2025-03-01' AND '2025-03-07'`.

How does the tree execute the range?

A. It hashes both range endpoints and merges every bucket between their hash values.  
B. It descends to the start leaf, then walks forward to the end date.  
C. It returns to the root and descends again for every date in the seven-day range.  
D. It reads every leaf page because sorted keys cannot establish where the range ends.

### 28. Match the specialist to the workload

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Hash, Composite, Partial, and Expression Indexes  
**Is Curriculum Based:** No  
**Assessment type:** Type-selection matrix

Four workloads:

1. Only ever `WHERE session_token = ?` — pure equality, high volume.  
2. `WHERE city = ? AND placed_on BETWEEN ? AND ?` — two columns together.  
3. Queries touching only the 1% of rows marked `flagged = true`.  
4. `WHERE UPPER(code) = ?`.

Which assignment is correct?

A. Hash for all four because equality appears somewhere in every workload.  
B. Partial for 1, hash for 2, expression for 3, and composite for 4.  
C. Hash for 1, composite for 2, partial for 3, expression for 4 — one each.  
D. Four single-column B-trees because specialized index forms cannot coexist with PostgreSQL heaps.

### 29. When the index can answer alone

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Covering Indexes and Index-Only Scans  
**Is Curriculum Based:** No  
**Assessment type:** Condition identification

Under what conditions can PostgreSQL serve a query without fetching its heap tuples?

A. When the query has no WHERE clause, regardless of its selected columns or the table's visibility state.  
B. When the table has fewer than one thousand rows and fits in memory.  
C. When the DBA grants a separate INDEX ONLY privilege to the query role.  
D. When the index contains every referenced column and visibility permits skipping the heap.

### 30. A third of everything

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** When Not to Index  
**Is Curriculum Based:** No  
**Assessment type:** Selectivity reasoning

Despite the new index on `priority`, the planner still chooses a Seq Scan for `WHERE priority = 'normal'` on the 6-million-row jobs table.

Why is the planner right?

A. The filter matches about two million rows, so many heap visits can cost more than one scan.  
B. PostgreSQL ignores every new index for seven days while it gathers usage statistics and waits for a maintenance window.  
C. Text equality cannot use any PostgreSQL index, regardless of selectivity.  
D. An index is usable only when its file resides on a different disk from the table.

### 31. Kept true, automatically

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** What is an Index  
**Is Curriculum Based:** No  
**Assessment type:** Maintenance-model identification

Rows in an indexed table are inserted, updated, and deleted all day.

Who keeps the index in sync with the table?

A. A nightly full rebuild that the DBA must schedule after the final write of each day.  
B. The database itself, within each write, adjusting affected indexes automatically.  
C. The application, by issuing a REFRESH INDEX statement after every transaction.  
D. Nobody; index entries are allowed to drift until a query reports an incorrect result.

### 32. Same depth everywhere

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** B-Tree Indexes  
**Is Curriculum Based:** No  
**Assessment type:** Balance-property reasoning

The "B" family of trees stays *balanced*: every leaf sits at the same depth.

What does balance buy the database?

A. Alphabetical output for every query, even when the key is numeric or no ORDER BY appears.  
B. Half the storage of an unbalanced tree because alternate levels are omitted.  
C. Predictable, uniform lookup cost — no key is buried deeper than any other.  
D. Freedom from index-maintenance work during INSERT, UPDATE, and DELETE.

### 33. The function that must match

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Hash, Composite, Partial, and Expression Indexes  
**Is Curriculum Based:** No  
**Assessment type:** Expression-matching trace

A team builds `CREATE INDEX ON users (LOWER(email));` — then is puzzled that `WHERE email = 'R.Iyer@volt.in'` still runs as a Seq Scan.

Why doesn't the expression index serve this query?

A. The index is unusable until every stored email is physically rewritten in lowercase.  
B. Equality can never use expression indexes.  
C. Expression indexes require numeric expressions.  
D. The index stores LOWER(email), but the query filters raw `email`, mismatched.

### 34. Two plans, one word apart

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Covering Indexes and Index-Only Scans  
**Is Curriculum Based:** No  
**Assessment type:** Plan-line discrimination

Two similar queries show:

| plan | access path | table-page reads |
|---:|---|---|
| 1 | `Index Scan using idx_cust on orders` | Yes |
| 2 | `Index Only Scan using idx_cust_cov on orders` | No |

What distinguishes the two executions?

A. Plan 1 visited the table for missing columns; plan 2 needed nothing extra.  
B. Plan 2 skipped predicate evaluation because index-only scans ignore WHERE clauses.  
C. Plan 1 uses newer PostgreSQL syntax but performs the same physical reads.  
D. The two names are cosmetic; both plans fetch every matching heap tuple.

### 35. The checklist before CREATE INDEX

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** When Not to Index  
**Is Curriculum Based:** No  
**Assessment type:** Decision-criteria selection

A DBA drafts a checklist for when an index proposal should be approved.

Which set of questions is the right filter?

A. Is the identifier short, is the heap alphabetized, and was the proposal submitted on a weekday?  
B. Is it filtered on? Selective? Does read benefit outweigh writes? Not served already?  
C. Does the column contain text, and has the table existed for more than one year?  
D. Approve every proposal because unused indexes stop consuming storage and maintenance work.

### 36. Where the speed comes from

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** What is an Index  
**Is Curriculum Based:** No  
**Assessment type:** Mechanism-of-benefit reasoning

Without an index, a lookup on an 80,000-page table reads 80,000 pages. With one, it reads about 5.

What did the index fundamentally change?

A. It compressed the heap from 80,000 pages to five pages without changing table size.  
B. It moved the table into memory permanently.  
C. It replaced search with navigation, walking straight to the row's address.  
D. It stored the query schedule on disk so the drive could predict future lookups.

### 37. One thousand times the data, one more hop

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** B-Tree Indexes  
**Is Curriculum Based:** No  
**Assessment type:** Scan-versus-tree scaling contrast

A reporting table grows 1,000×. Two access paths are compared before and after: a full scan, and a B-tree lookup.

Which comparison is correct?

A. Both paths slow by exactly 1,000 times because every structure scales linearly.  
B. The scan is unaffected; the tree slows 1,000×.  
C. Both stay constant regardless of size.  
D. The scan grows ~1,000×, while the B-tree grows by perhaps one level only.

### 38. Composite or two singles?

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Hash, Composite, Partial, and Expression Indexes  
**Is Curriculum Based:** No  
**Assessment type:** Design-choice judgment

The dominant query filters `WHERE branch_id = ? AND txn_date BETWEEN ? AND ?` — always both conditions together. The team debates one composite index `(branch_id, txn_date)` versus two single-column indexes.

Which choice fits, and why?

A. The composite — descend on branch, walk the date range within it.  
B. Two singles, because PostgreSQL cannot place equality and range columns in one index.  
C. Neither; combined filters cannot be indexed.  
D. Six indexes, so every permutation exists even though the workload uses one fixed predicate order.

### 39. Spell the covering index

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Covering Indexes and Index-Only Scans  
**Is Curriculum Based:** No  
**Assessment type:** Syntax selection

The hot query: `SELECT loyalty_tier, joined_on FROM members WHERE member_no = ?`.

Which statement builds a covering index for it?

A. `CREATE COVERING INDEX idx_member_lookup ON members (member_no, loyalty_tier, joined_on);`  
B. `CREATE INDEX ON members (member_no) INCLUDE (loyalty_tier, joined_on);`, index-only.  
C. `CREATE INDEX idx_member_payload ON members (loyalty_tier, joined_on) WITHOUT (member_no);`  
D. `INCLUDE INDEX idx_member_lookup ON members WITH (member_no, loyalty_tier, joined_on);`

### 40. Prune the index garden

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** When Not to Index  
**Is Curriculum Based:** No  
**Assessment type:** Integrated review

A write-heavy payments table carries:

| index | definition | observed use |
|---:|---|---|
| 1 | `(merchant_id)` | Frequent selective lookups |
| 2 | `(merchant_id, settled_on)` | Frequent settlement report |
| 3 | `(currency)` | Four values across 90 million rows |
| 4 | `(internal_memo)` | No query filters or sorts on it |
| 5 | `(merchant_id)` | Duplicate of index 1 under another name |

Which pruning is correct?

A. Drop both frequently used merchant indexes because any shared leading column makes both useless.  
B. Keep all five because unused and duplicate indexes stop receiving write updates automatically.  
C. Drop 3, 4, and 5; keep 2; note 1 largely overlaps 2's lead column.  
D. Drop every index, then recreate one on a randomly selected column after each slowdown.

---

## Instructor Key

### 1. D

An index is an auxiliary structure, not a table transformation: an ordered directory from values to row locations, living beside the untouched table. Everything else in the chapter — costs, plans, variants — follows from this separateness.

### 2. B

B-trees buy shallowness with width: each level's fan-out multiplies capacity, so a thousandfold data increase adds a level or so. Lookups pay per level, which is why they barely notice the growth.

### 3. A

The queries only ever want the 2%; the partial index stores only that 2%. Small, cheap to maintain, perfectly aimed — the partial index is workload-shaped indexing.

### 4. C

The index stores every referenced value, and the stated visibility state lets PostgreSQL verify row visibility without heap visits. Both conditions support the observed `Heap Fetches: 0`.

### 5. A

Each index is an independent ordered structure with an opinion about every write. Five indexes means every insert does six structures' worth of bookkeeping — the write tax rises linearly with the index count.

### 6. D

The plan is the receipt: Seq Scan before, Index Scan naming the new index after. Watching the plan flip is the standard verification that an index landed and is chosen.

### 7. B

Sorted order is a triple gift: descend for equality, descend-and-walk for ranges, read-in-order for sorting. That breadth across the patterns real workloads mix is exactly the case for B-tree as default.

### 8. C

Indexes match expressions literally: an index on `email` knows nothing about `LOWER(email)`. Building the index on the same computation the query performs restores the alignment.

### 9. A

INCLUDE turns a finding index into a serving one: the payload columns ride inside each entry, so the query's whole SELECT list is present at the point of discovery. Option B indexes what is selected but not what is *searched* — backwards.

### 10. D

Selectivity is the index's fuel. A filter matching a third of a huge table turns the index path into millions of scattered fetches — costlier than one straight read-through. Few distinct values usually means little selectivity, and little payoff.

### 11. B

Two steps: search the small ordered directory, then fetch at the address it yields. The index's job ends at the address; the table still holds the row.

### 12. C

Root to internal to leaves, each step slicing the candidate space by the page's fan-out. The sorted leaves are the destination; everything above is routing.

### 13. D

Hashing trades order for equality access: scatter makes `=` a direct hit but provides no ordered path for ranges or sorting. It is a specialist for equality-only workloads.

### 14. A

Index entries hold indexed values plus addresses — not the whole row. Twenty matches with an uncovered column means twenty address-following trips to the heap. This gap is precisely what covering indexes close.

### 15. B

An index earns by being used and charges by existing. Zero uses, full maintenance: the drop decision writes itself once usage is measured.

### 16. C

Reads cheaper, writes dearer — the bargain in one line. The approval question is always whether the column's read traffic justifies the table's write surcharge.

### 17. D

Defaults should serve the common case, and the common case is mixed access patterns. The B-tree's generality — good at nearly everything, best-in-class at nothing narrow — is exactly the profile a default wants.

### 18. A

A composite sorts by its leading column first; within equal leading values, by the next. Pin the leader and the structure narrows immediately; skip the leader and the wanted dates are sprayed across every city — order of columns is the index's API.

### 19. B

Index-only is all-or-nothing: one uncovered column resurrects the heap trips. Covering must be designed against the query's full column list, not assumed.

### 20. C

The composite's leading portion can serve `supplier_id` filters, so the single-column index overlaps heavily. It is a removal candidate, but usage and measured plan differences should be checked before dropping it because the smaller index can sometimes still be cheaper.

### 21. D

Indexes are bolt-on and bolt-off: the table is never modified by their lifecycle. That reversibility is why index tuning is a low-risk, iterative activity.

### 22. A

Depth is the bill: four levels, four page reads, whether the tree holds fifty thousand or fifty million keys. The root's guidance compounds level by level until the leaf answers.

### 23. B

100,000 entries versus 5,000,000 — a fiftieth the size, and closed tickets never generate maintenance. The condition in the index definition is the workload's filter, promoted into the structure itself.

### 24. C

INCLUDE physically widens every entry: more bytes stored, more bytes maintained per write. The read win is genuine and so is the invoice — covering is a purchase, priced in width.

### 25. D

Ten structures per insert, several returning nothing: the write tax accumulated one index at a time, which is why it crept rather than jumped. Index count is a liability register, and unused entries should be struck off.

### 26. A

Same query, same data, different access path: 8 million rows read versus 1. The plan names the index, the timing shows the factor, and together they close the case.

### 27. B

Ranges exploit the leaves' sorted adjacency: one descent to the start, then a forward walk to the end. The tree is consulted once; the shelf is read in order.

### 28. C

Each variant answers one shape: hash for pure equality, composite for the two-column predicate, partial for the tiny hot subset, expression for the computed filter. The matrix *is* the lesson: variants exist because workloads have shapes.

### 29. D

Index-only access requires every referenced column to be present and PostgreSQL's visibility information to permit skipping heap checks. Missing either condition brings heap visits back.

### 30. A

Two million scattered matches served via index means millions of page hops; one sequential sweep is cheaper. The planner's defection to the scan is cost arithmetic, not stubbornness — and it is the low-cardinality warning made concrete.

### 31. B

Index maintenance is built into every write — synchronous, automatic, non-optional. That is both why indexes are always trustworthy and why each one raises the price of every insert.

### 32. C

Balance equalizes fate: all leaves at one depth, all lookups at one price. Predictability is a performance feature in itself — no value hits a pathological path.

### 33. D

The symmetry rule: the index serves queries whose expression matches its own. Built on LOWER(email), it answers LOWER(email) filters — and is invisible to raw-column ones, just as a raw index was invisible to LOWER queries.

### 34. A

One word, one architectural difference: "Only" means the index sufficed. Plan 1 paid per-row heap visits for uncovered columns; plan 2's covering index kept the whole answer in-structure.

### 35. B

Four gates: real usage, real selectivity, favourable read/write balance, no existing coverage. Each gate exists because some index in this chapter failed exactly that test.

### 36. C

The index converts the problem's scaling: from work-proportional-to-table to work-proportional-to-tree-depth. Navigation replaces exhaustive search — that substitution is the entire speedup.

### 37. D

Growth splits the paths: scans track size linearly; trees add a level per orders-of-magnitude. The bigger and faster-growing the table, the wider the divergence — indexes are insurance against growth itself.

### 38. A

The predicate's shape is "equality, then range" — exactly a composite's sort order: pin the branch, walk its dates contiguously. Two singles each solve half and leave the intersection as extra work; the composite solves the whole shape natively.

### 39. B

Key on the searched column, INCLUDE for the selected payload. Option A is invented syntax; option C indexes the payload and forgets the search.

### 40. C

Three failures, three prunes: low cardinality (3), zero usage (4), duplication (5). The survivors are the earning indexes — with the footnote that 2's leading column may make even 1 negotiable. Pruning is the write-tax audit in action.

---

## Question-Type Distribution

| Higher-order assessment family | Question numbers |
|---|---|
| Mechanism and structure identification | 1, 4, 11, 12, 13, 14, 21, 27, 29, 31, 32, 36 |
| Cost, scaling, and trade-off analysis | 2, 5, 16, 22, 23, 24, 25, 37 |
| Missing/smallest index repair and syntax | 3, 8, 9, 39 |
| Index-type and column-order design | 17, 18, 28, 38 |
| Plan reading and evidence interpretation | 6, 26, 34 |
| When-not-to-index judgment | 10, 15, 20, 30, 35, 40 |
| Capability and matching reasoning | 7, 19, 33 |

## Blueprint Taxonomy Coverage

| Subtopic from the attached blueprint | Question numbers | Count |
|---|---|---:|
| What is an Index | 1, 6, 11, 16, 21, 26, 31, 36 | 8 |
| B-Tree Indexes | 2, 7, 12, 17, 22, 27, 32, 37 | 8 |
| Hash, Composite, Partial, and Expression Indexes | 3, 8, 13, 18, 23, 28, 33, 38 | 8 |
| Covering Indexes and Index-Only Scans | 4, 9, 14, 19, 24, 29, 34, 39 | 8 |
| When Not to Index | 5, 10, 15, 20, 25, 30, 35, 40 | 8 |

Questions 1–10 collectively cover all five Topic 7.2 subtopics.

## Difficulty and Answer-Key Balance

- Foundational: 10 questions (6, 10, 11, 12, 13, 15, 16, 20, 29, 31)
- Intermediate: 23 questions
- Advanced: 7 questions (18, 25, 28, 33, 37, 38, 40)
- Correct option A: 10 questions (3, 5, 9, 14, 18, 22, 26, 30, 34, 38)
- Correct option B: 10 questions (2, 7, 11, 15, 19, 23, 27, 31, 35, 39)
- Correct option C: 10 questions (4, 8, 12, 16, 20, 24, 28, 32, 36, 40)
- Correct option D: 10 questions (1, 6, 10, 13, 17, 21, 25, 29, 33, 37)
- Longest consecutive run of one correct letter: below 3 throughout
