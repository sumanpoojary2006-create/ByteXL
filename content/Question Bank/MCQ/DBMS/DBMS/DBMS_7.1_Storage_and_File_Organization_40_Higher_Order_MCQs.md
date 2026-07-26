# DBMS 7.1: Storage and File Organization — 40 Higher-Order MCQs

## Assessment specifications

- **Subject:** DBMS
- **Topic:** Performance
- **Chapter:** Storage and File Organization
- **Scope:** All three Topic 7.1 subtopics in the attached course blueprint (How Data is Stored; File Organization: Heap, Sorted, and Hashed Files; Why Storage Layout Affects Query Speed)
- **SQL dialect:** PostgreSQL
- **Format:** Four options with exactly one best answer
- **Curriculum flag:** No
- **Design standard:** Questions begin with a recognisable database workload and define the rows, page layout, table size, access pattern, or observed plan needed to reason about physical cost.
- **Evidence rule:** Students never need to invent a page size, supporting structure, physical order, row width, result selectivity, or table-growth rate when it determines the answer.
- **Scope guard:** Questions use only Topic 7.1 material. Detailed index design and optimizer internals belong to Topics 7.2 and 7.3 and are not tested here.
- **Answer-quality controls:** A/B/C/D each correct exactly 10 times, no letter correct more than twice consecutively, no correct answer identifiable by length.
- **Coverage rule:** Questions 1–10 collectively cover all three Topic 7.1 subtopics.
- **Student/instructor separation:** Questions appear first; answers and explanations follow in the instructor key.

---

## Questions

### 1. One row wanted, one page delivered

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** How Data is Stored  
**Is Curriculum Based:** No  
**Assessment type:** I/O-unit reasoning

A courier app fetches one parcel row:

| requested row size | PostgreSQL page size | bytes read from disk |
|---:|---:|---:|
| 120 bytes | 8 KB | 8 KB |

Select the physical-storage explanation for the difference.

A. Pages are the unit of disk I/O; the wanted row is extracted once the page loads.  
B. Every SQL query expands its target row to one complete 8 KB row before evaluation.  
C. PostgreSQL stores each 120-byte row in a separate 8 KB operating-system file.  
D. The extra bytes must belong to unrelated tables because one page mixes rows from many relations.

### 2. Wherever there's room

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** File Organization: Heap, Sorted, and Hashed Files  
**Is Curriculum Based:** No  
**Assessment type:** Heap-behaviour identification

A ticket system inserts scans in this order:

| scan_id | scanned_at |
|---:|---|
| 41 | 10:04 |
| 12 | 10:05 |
| 87 | 10:06 |

The table is PostgreSQL's default heap and currently has free space on several pages.

Choose the placement rule the storage engine follows.

A. Into pages that preserve ascending `scan_id`, because primary keys physically order heaps.  
B. Into a bucket computed from the ticket number.  
C. Into alphabetical position by venue.  
D. Into any page with free space; heap order is unconstrained.

### 3. Every page, every row

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Why Storage Layout Affects Query Speed  
**Is Curriculum Based:** No  
**Assessment type:** Definition selection

A 90-page heap has no supporting structure for `delivery_zone`. A query filters `WHERE delivery_zone = 'EAST'` and the plan shows `Seq Scan`.

Translate that plan into physical work.

A. PostgreSQL reads only pages already known to contain EAST rows.  
B. The database reads every page, examining every row against the condition.  
C. PostgreSQL reads the first page completely, then uses its contents to infer the remaining rows.  
D. The database copies all 90 pages into a second scan file before checking the predicate.

### 4. The row's home address

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** How Data is Stored  
**Is Curriculum Based:** No  
**Assessment type:** Concept identification

An engineer inspects four rows:

| order_id | `ctid` |
|---:|---|
| 1 | `(0,1)` |
| 2 | `(0,2)` |
| 250 | `(2,30)` |
| 500 | `(4,60)` |

Interpret the two components in `ctid = (2,30)`.

A. Table file 2 and database server 30.  
B. Query-result page 2 and display row 30.  
C. Which page the row lives in and where it sits within that page.  
D. Transaction 2 and the thirtieth SQL statement that touched the row.

### 5. Neighbours on disk

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** File Organization: Heap, Sorted, and Hashed Files  
**Is Curriculum Based:** No  
**Assessment type:** Sorted-organization reasoning

A weather archive is physically clustered by `reading_date`. Its page map is:

| page range | dates stored |
|---|---|
| 0–299 | 2016–2020 |
| 300–599 | 2021–2024 |
| 600–669 | 2025 |

A report requests one week from March 2025.

Select the page-level reason this layout helps.

A. Clustering removes all readings outside the requested week from the table.  
B. The week's rows sit physically together in a few adjacent pages nearby.  
C. Date sorting guarantees that each matching row occupies its own page.  
D. The WHERE predicate becomes unnecessary because physical order determines the result automatically.

### 6. Twice the data, twice the wait

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Why Storage Layout Affects Query Speed  
**Is Curriculum Based:** No  
**Assessment type:** Cost-scaling reasoning

A fraud team's unindexed filter performs a full scan:

| row count | page count | elapsed time |
|---:|---:|---:|
| 2 million | 18,000 | 3 seconds |
| 4 million | about 36,000 | ? |

Estimate the second runtime under comparable hardware and cache conditions.

A. About 3 seconds because only the number of matching rows controls scan cost.  
B. About 1.5 seconds because larger tables make sequential I/O twice as efficient.  
C. About 90 seconds because scan work grows with the square of the row count.  
D. Roughly 6 seconds; doubling rows doubles pages read, linear scan time.

### 7. Why the page is the price

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** How Data is Stored  
**Is Curriculum Based:** No  
**Assessment type:** Cost-model reasoning

A performance test compares two layouts:

| query | rows returned | distinct pages containing them |
|---|---:|---:|
| A | 5 | 5 |
| B | 50 | 1 |

Choose why query A can require more storage I/O despite returning fewer rows.

A. Moving a page between disk and memory is the expensive act, paid per page.  
B. PostgreSQL charges a fixed client-network fee for every row that occupies a different page.  
C. A row stored alone becomes physically wider than the same row stored beside neighbours.  
D. Result-row count alone determines disk work, so B must necessarily cost more than A.

### 8. Placed by arithmetic

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** File Organization: Heap, Sorted, and Hashed Files  
**Is Curriculum Based:** No  
**Assessment type:** Hashed-organization identification

A prepaid-SIM system assigns exact keys to hash buckets:

| `sim_number` | bucket |
|---|---:|
| 98220-41007 | 5 |
| 98220-41008 | 1 |
| 98220-41009 | 7 |

A lookup requests `sim_number = '98220-41007'`.

Select the access path supplied by the hashed organization.

A. Scan buckets 1 through 7 because nearby SIM numbers may occur in any of them.  
B. By binary-searching the sorted file.  
C. By computing the same hash that placed the row, going straight there.  
D. Sort all SIM numbers for this query, then search the temporary ordering.

### 9. Same table, wildly different speeds

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Why Storage Layout Affects Query Speed  
**Is Curriculum Based:** No  
**Assessment type:** Access-path contrast

One 5-million-row heap produces these observations:

| predicate | supporting structure | plan | elapsed |
|---|---|---|---:|
| `order_id = 88231` | primary-key structure | Index Scan | 2 ms |
| `courier_note = 'fragile'` | none | Seq Scan | 40 s |

Select the physical explanation supported by the plan evidence.

A. Text predicates always require one disk read per character, unlike integer predicates.  
B. Rows containing `fragile` are stored at the physical end of every PostgreSQL heap.  
C. The application cache answers every primary-key query before PostgreSQL sees it.  
D. The primary-key search rides a structure to just a few pages.

### 10. From CREATE TABLE to spinning disk

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** How Data is Stored  
**Is Curriculum Based:** No  
**Assessment type:** Full-path sequencing

A trainee draws four possible paths from SQL's logical table abstraction to disk.

Select the physically accurate path.

A. Table → one display page → one printed page.  
B. Rows are packed into fixed-size pages, which make up files on disk.  
C. Table → one operating-system file per row → individual storage block on the device.  
D. Table → rows held permanently in RAM → optional disk cache.

### 11. Roommates by the dozen

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** How Data is Stored  
**Is Curriculum Based:** No  
**Assessment type:** Packing reasoning

A bicycle-hire service estimates 100 bytes per row and uses 8 KB pages. Ignore the small page and row bookkeeping overhead for this estimate.

Estimate how many rows one page can hold.

A. About 8 rows, because each kilobyte can hold only one row.  
B. About 800 rows, because the page size is measured in bits.  
C. Dozens of rows share each page, roughly 80 per 8 KB page.  
D. Exactly one row, because PostgreSQL assigns every row a separate page address.

### 12. The fastest possible insert

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** File Organization: Heap, Sorted, and Hashed Files  
**Is Curriculum Based:** No  
**Assessment type:** Strength identification

An IoT platform lands 50,000 sensor rows a minute and rarely queries them by value.

Select why heap organization fits this write-heavy workload.

A. It adds little ordering overhead because a row can use any page with suitable free space.  
B. It compresses every sensor row automatically and preserves exact sensor-time order during every insert.  
C. It avoids WAL and transaction processing for high-rate inserts.  
D. It discards older rows whenever the current heap page becomes full.

### 13. Caught in the act

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Why Storage Layout Affects Query Speed  
**Is Curriculum Based:** No  
**Assessment type:** Missing-command completion

A developer wants to preview whether an unindexed freight lookup will scan the whole table without executing the query. Complete the blank:

```sql
____ SELECT * FROM freight WHERE tracking_note = 'DAMAGED';
```

A. `CHECKPOINT` — it flushes pages and prints the chosen scan method  
B. `CLUSTER` — it previews the plan without changing the freight table  
C. `pg_relation_size` — it prefixes a SELECT with the relation's page count  
D. `EXPLAIN` — its output can show `Seq Scan` as the planned access path

### 14. The journey of one SELECT

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** How Data is Stored  
**Is Curriculum Based:** No  
**Assessment type:** Retrieval-path sequencing

A pharmacy system fetches one prescription row by its physical address.

Which sequence describes the retrieval?

A. Copy the row into a temporary table, then search that table by logical key.  
B. The address names the page; the page loads, the row extracts by position.  
C. Read every table page because a physical address identifies only the table, not a page.  
D. Request only the row's bytes from disk without transferring the page containing them.

### 15. What keeping order costs

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** File Organization: Heap, Sorted, and Hashed Files  
**Is Curriculum Based:** No  
**Assessment type:** Maintenance-limit repair

A registrar runs `CLUSTER` once to reorder a PostgreSQL heap by an index on `enrolled_on`. Months of new enrolments then arrive.

Select the maintenance limitation the registrar must plan for.

A. The table can no longer accept INSERT statements after it has been clustered.  
B. PostgreSQL automatically reclusters after every INSERT, creating unavoidable per-row sorting and page-rewrite work.  
C. New rows again use available heap space, so physical order drifts and periodic reclustering may be needed.  
D. The index used by CLUSTER is deleted once the table rewrite completes.

### 16. Two layouts, one week of readings

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Why Storage Layout Affects Query Speed  
**Is Curriculum Based:** No  
**Assessment type:** Layout-contrast reasoning

Two copies of a 10-year river-gauge archive hold identical rows: copy H is a heap, copy S is sorted by reading date. The same query fetches one week's readings from each.

Why do the copies perform so differently?

A. On S the week sits adjacent; on H the same rows may scatter across the file.  
B. H stores a second copy of every reading because heaps duplicate range values.  
C. Sorted copies use faster disks by convention.  
D. S evaluates fewer date comparisons even if both layouts read the same pages.

### 17. Not loose, ever

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** How Data is Stored  
**Is Curriculum Based:** No  
**Assessment type:** Structure statement

Which statement about rows and disk is correct?

A. Each logical row is saved as its own operating-system file.  
B. Rows are read from disk individually without loading surrounding bytes.  
C. Rows remain only in memory until a query requests them.  
D. Rows never sit loose on disk; they live packed inside pages instead.

### 18. The range the buckets can't serve

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** File Organization: Heap, Sorted, and Hashed Files  
**Is Curriculum Based:** No  
**Assessment type:** Limitation reasoning

The prepaid-SIM platform's hashed file answers single-SIM lookups instantly. A new report asks for all SIMs numbered between 98220-00000 and 98220-99999.

Why does the hashed organization fail this query?

A. SQL rejects `BETWEEN` whenever a hash function was used to place the values.  
B. Hashing scatters consecutive numbers into unrelated buckets, no locality.  
C. A hash lookup can compute a bucket only when the predicate contains two boundary values.  
D. Hash buckets preserve alphabetical rather than numeric order, so numeric ranges fail.

### 19. Do the scan math

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Why Storage Layout Affects Query Speed  
**Is Curriculum Based:** No  
**Assessment type:** Cost computation

A parcels table is scanned under comparable hardware and cache conditions:

| table state | pages | full-scan time |
|---|---:|---:|
| Before growth | 10,000 | 2 seconds |
| After growth | 40,000 | ? |

Estimate the new scan time using page-count scaling.

A. About 2 seconds because result selectivity, not pages, controls a full scan.  
B. About 4 seconds because a fourfold page increase doubles scan work.  
C. About 8 seconds — quadrupling the pages quadruples the scan's work.  
D. About 32 seconds because page reads compound with each additional page.

### 20. Straight to the shelf

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** How Data is Stored  
**Is Curriculum Based:** No  
**Assessment type:** Address-use reasoning

A diagnostic query reports `ctid = (3,14)` for a prescription row.

Interpret this physical address using the chapter's page-and-slot model.

A. Page 3 contains the row, and it occupies position 14 within that page.  
B. File 3 contains the row, and PostgreSQL must scan 14 pages to reach it.  
C. The row occupies page 14, while 3 is the transaction that inserted it.  
D. The row is the fourteenth result returned by query number 3.

### 21. The right home for exact-match traffic

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** File Organization: Heap, Sorted, and Hashed Files  
**Is Curriculum Based:** No  
**Assessment type:** Organization selection

A tolling system's only query pattern, billions of times a year: fetch one vehicle's account by exact tag ID. Never ranges, never sorting, never prefix searches.

Which organization matches this workload best?

A. Heap on arrival time, requiring every exact tag lookup to scan pages in insertion order.  
B. Sorted by registration date, even though tag values are unrelated to that order.  
C. Sorted by tag ID, which helps but adds ordering work unused by other query patterns.  
D. Hashed on the tag ID — a pure equality workload is the hashed file's home ground.

### 22. The scan that was the right answer

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Why Storage Layout Affects Query Speed  
**Is Curriculum Based:** No  
**Assessment type:** Appropriateness judgment

A nightly job reads *every* row of a 40-page settings table, and its plan shows a sequential scan. A junior engineer files a performance bug.

What is the senior's correct reply?

A. Replace the scan because any plan reading every page is automatically defective.  
B. The scan is right: the job needs every row, and the table is tiny.  
C. Split the table into 40 one-page tables and query each table separately.  
D. Issue one primary-key query per row so every read uses the key structure.

### 23. Wide rows, thin pages

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** How Data is Stored  
**Is Curriculum Based:** No  
**Assessment type:** Packing-consequence chain

Two claims-table designs use 8 KB pages:

| design | rows | approximate row width | approximate rows/page |
|---|---:|---:|---:|
| N | 1 million | 200 bytes | 40 |
| W | 1 million | 2,000 bytes | 4 |

Choose the physical-cost chain that explains the scan difference.

A. PostgreSQL applies ten times more validation rules merely because a row is wider.  
B. About 40 of N's rows fit per page, only 4 of W's, so W needs 10× pages.  
C. W stores each column in a different table file, forcing ten extra table scans.  
D. Both designs occupy the same page count because only row count affects relation size.

### 24. The archive that lives by the calendar

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** File Organization: Heap, Sorted, and Hashed Files  
**Is Curriculum Based:** No  
**Assessment type:** Organization selection

A power utility's meter-reading archive is queried almost exclusively by date windows: "readings for March," "the last 14 days," "Q2 by feeder."

Which organization fits, and why?

A. Sorted on the reading date, turning ranges into contiguous sweeps.  
B. Hashed on the reading date, scattering nearby dates among independent buckets.  
C. Heap ordered by arrival time, assuming that arrival always equals measurement date.  
D. Sorted on customer name, even though the predicates contain only date boundaries.

### 25. Predict the winner, explain the loser

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Why Storage Layout Affects Query Speed  
**Is Curriculum Based:** No  
**Assessment type:** Access-path prediction

One 8-million-row heap produces:

| query | predicate | supporting structure |
|---|---|---|
| Q1 | `delivery_id = 4410877` | Primary-key structure |
| Q2 | `handler_initials = 'RK'` | None |

Predict the physical work required by each query.

A. Q2 reads fewer pages because two-character values are physically closer together in a heap.  
B. Both read all pages because a primary key does not create any supporting structure.  
C. Both read a fixed one-page location because PostgreSQL hashes every predicate automatically.  
D. Q1 navigates to the pages holding the key; Q2 reads every page.

### 26. What the scan is *not*

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Why Storage Layout Affects Query Speed  
**Is Curriculum Based:** No  
**Assessment type:** Misconception correction

A dashboard flags "Seq Scan detected" in red, and a manager asks if the database is malfunctioning.

What is the accurate answer?

A. Yes; a sequential scan means PostgreSQL detected corrupted page ordering.  
B. A sequential scan is a normal, legitimate strategy, not always wrong.  
C. Yes; reading a page sequentially changes its physical position in the table file.  
D. No malfunction occurred, but every sequential scan should still be replaced regardless of workload.

### 27. Finding one needle without a map

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** File Organization: Heap, Sorted, and Hashed Files  
**Is Curriculum Based:** No  
**Assessment type:** Heap-lookup cost reasoning

A heap-organized returns table holds 3 million rows. A clerk searches for one RMA code — a value the table has no supporting structure for.

What must the database do, and why?

A. Compute a bucket from the RMA code even though no hashed structure exists.  
B. Binary-search the heap because its pages are automatically ordered by RMA code.  
C. Scan the heap end to end; no page can be ruled out without looking.  
D. Read only the newest page because heap lookup values are always stored most recently.

### 28. Three matches, ten thousand pages

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Why Storage Layout Affects Query Speed  
**Is Curriculum Based:** No  
**Assessment type:** Selectivity-versus-work analysis

A bookings heap has:

| total rows | total pages | matching rows | supporting structure on `voucher_code` |
|---:|---:|---:|---|
| 500,000 | 10,000 | 3 | None |

For `WHERE voucher_code = 'MON50FEB'`, select the pages read and the lesson it demonstrates.

A. All 10,000 pages — 3 rows found, but the whole table was the work.  
B. About 3 pages because PostgreSQL knows each match must occupy a distinct page.  
C. About 60 pages because a heap reserves twenty candidate pages for each expected match.  
D. Zero pages because predicates returning fewer than ten rows are precomputed.

### 29. Counting in the right currency

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** How Data is Stored  
**Is Curriculum Based:** No  
**Assessment type:** Cost-unit application

Two queries against the same table return:

| query | rows returned | distinct pages touched |
|---|---:|---:|
| A | 100 | 100 |
| B | 100 | 2 |

Compare only their page-read I/O.

A. Identical because equal result-row counts always imply equal disk work.  
B. B performs more I/O because packed rows require unpacking the entire page.  
C. Page-read cost cannot be compared unless both queries return different row counts.  
D. A cost roughly 50× more I/O than B — 100 page reads against 2.

### 30. Match the three to their homes

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** File Organization: Heap, Sorted, and Hashed Files  
**Is Curriculum Based:** No  
**Assessment type:** At-a-glance matching

Three workloads:

1. Relentless bulk inserts, almost no value lookups.  
2. Constant date-range reporting.  
3. Pure single-key equality lookups.

Which pairing of workload to organization is correct?

A. 1: sorted for insert order; 2: hashed for ranges; 3: heap for equality.  
B. 1: heap, cheapest writes; 2: sorted, ranges; 3: hashed, direct buckets.  
C. 1: hashed for writes; 2: heap for ranges; 3: sorted by an unrelated date.  
D. All three want hashed organization because bucket placement preserves both ranges and insertion order.

### 31. Two columns asked, forty delivered

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Why Storage Layout Affects Query Speed  
**Is Curriculum Based:** No  
**Assessment type:** Row-width consequence

An analyst scans a 40-column heap containing wide address and notes fields but returns only `order_id, status`. The plan still reads every table page.

Select why projecting two columns does not eliminate the page-read cost.

A. PostgreSQL creates a separate two-column copy of every page before evaluating the scan.  
B. Page I/O is billed by the number of column names written in the SELECT list.  
C. Rows are stored whole inside pages; the scan reads full pages regardless.  
D. Wide columns force PostgreSQL to evaluate the predicate once per column, even without a WHERE clause.

### 32. Inside the 8 KB box

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** How Data is Stored  
**Is Curriculum Based:** No  
**Assessment type:** Page-content identification

A curious engineer inspects what a single table page actually contains.

Which description is accurate?

A. A batch of one table's rows together with the page's bookkeeping information.  
B. Exactly one row, with every unused byte on the page reserved as padding for that single row.  
C. Rows from unrelated tables mixed together whenever they share a schema.  
D. Column definitions only; row data is stored outside table pages.

### 33. The sorted table that grew tired

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** File Organization: Heap, Sorted, and Hashed Files  
**Is Curriculum Based:** No  
**Assessment type:** Degradation reasoning

A registrar runs `CLUSTER admissions USING idx_application_id;`. Immediately afterward, nearby application IDs occupy nearby pages. Two years of randomly ordered inserts then accumulate.

Choose the explanation and repair consistent with PostgreSQL's one-time `CLUSTER`.

A. Application IDs lose their comparison order as numeric values age and must be regenerated.  
B. PostgreSQL automatically preserves clustering after every insert, so the slowdown cannot involve any physical layout drift.  
C. The index stops supporting range conditions after the heap reaches one million rows.  
D. New rows used available heap space, weakening locality; running CLUSTER again can restore it.

### 34. Same SQL, different bill

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Why Storage Layout Affects Query Speed  
**Is Curriculum Based:** No  
**Assessment type:** Abstraction-boundary reasoning

The same `SELECT ... WHERE reading_date BETWEEN ...` runs against two physically different layouts of identical data, and the SQL never mentions pages, heaps, or sorting — yet one run is 40× faster.

What principle does this demonstrate?

A. A physical-layout difference necessarily changes the rows returned by identical SQL.  
B. `BETWEEN` uses a different comparison definition whenever data is clustered.  
C. SQL is declarative about what, silent about where; layout changes cost.  
D. PostgreSQL rewrites the faster query into different SQL text before execution.

### 35. Page, defined

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** How Data is Stored  
**Is Curriculum Based:** No  
**Assessment type:** Definition selection

A storage diagram needs a correct label for the block between individual rows and a table file. Select that label's definition.

A. A page is one screenful of rows selected by the client application's display size.  
B. A page is one row plus its history.  
C. A fixed-size block of storage, commonly 8 KB, holding a batch of rows.  
D. A page is an operating-system file created separately for every query result.

### 36. The heap's silent partner

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** File Organization: Heap, Sorted, and Hashed Files  
**Is Curriculum Based:** No  
**Assessment type:** Combination reasoning

PostgreSQL tables are heaps, yet primary-key lookups on them are fast.

How are the heap's cheap disorderly writes reconciled with fast lookups?

A. A separate primary-key structure locates rows while the heap itself remains unordered.  
B. PostgreSQL physically sorts every heap by primary key during each nightly checkpoint.  
C. Declaring a primary key converts the table file from heap organization to hash buckets.  
D. Primary-key lookups still full-scan the heap; their speed comes only from shorter comparisons.

### 37. Three queries walk into a table

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Why Storage Layout Affects Query Speed  
**Is Curriculum Based:** No  
**Assessment type:** Multi-query strategy prediction

A shipping table is physically clustered by `manifest_no`, and its primary key also has PostgreSQL's automatic supporting structure.

| query | predicate | relation to layout/support |
|---:|---|---|
| 1 | `manifest_no = 'MN-88421'` | Primary-key equality |
| 2 | `manifest_no BETWEEN 'MN-88000' AND 'MN-89000'` | Clustered-key range |
| 3 | `crate_colour = 'red'` | Unrelated unindexed column |

Choose the query with no taught way to rule out pages.

A. Query 1, because equality cannot use a primary-key structure on a heap.  
B. Query 2, because physical clustering helps exact matches but not ranges.  
C. Queries 1 and 2, because both predicates mention the physically sorted column.  
D. Query 3 — crate colour is unrelated to the sort order used here.

### 38. Prove it's a scan, without reading plans

**Difficulty:** Intermediate

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Why Storage Layout Affects Query Speed  
**Is Curriculum Based:** No  
**Assessment type:** Experimental-design reasoning

A trainee wants behavioural evidence — not just the plan — that a query full-scans its table.

Which experiment gives it?

A. Compare morning and evening runtimes without changing data volume or configuration.  
B. Time the query, double the data, and time it again; scans roughly double.  
C. Rename the table without changing its pages, then compare the same predicate.  
D. Run the unchanged query twice and treat any second-run speedup as proof of a full scan.

### 39. Heap, in one sentence

**Difficulty:** Foundational

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** File Organization: Heap, Sorted, and Hashed Files  
**Is Curriculum Based:** No  
**Assessment type:** Definition selection

A storage review must describe PostgreSQL's default table organization without promising a physical order. Select the accurate description.

A. Rows are stored with no imposed order, each landing wherever has room, cheap writes.  
B. Rows remain physically sorted by the primary key after every future INSERT.  
C. Rows are assigned to hash buckets computed from the first declared column.  
D. Rows are reordered automatically to match whichever predicate is queried most often.

### 40. The report that aged badly

**Difficulty:** Advanced

**Subject:** DBMS  
**Topic:** Performance  
**Subtopic:** Why Storage Layout Affects Query Speed  
**Is Curriculum Based:** No  
**Assessment type:** Integrated diagnosis

A compliance report has these measurements under comparable conditions:

| table size | predicate | supporting structure | elapsed |
|---:|---|---|---:|
| 1 GB | unindexed `status` | None | 4 s |
| 12 GB | same predicate | None | 55 s |

Select the diagnosis that connects logical selectivity to physical page work.

A. The SQL statement becomes computationally older each month and must be reparsed more slowly.  
B. PostgreSQL moves status values toward the end of the file as the table ages.  
C. The report was always a full scan; cost simply grew in lockstep with pages.  
D. The result has few rows, so the larger table should not change the number of pages read.

---

## Instructor Key

### 1. A

The page is the indivisible unit of I/O: rows are residents, pages are what travel. The 8 KB read for a 120-byte row is the architecture, not waste — and it pays off whenever neighbouring rows are wanted too.

### 2. D

Heap means no imposed order: free space anywhere is a valid home. That indifference is the heap's entire performance personality — cheap to write, oblivious to value locality.

### 3. B

A full table scan is exhaustive by necessity: with nothing to say where matches live, every page must be read and every row tested. The definition is honest work, not malfunction.

### 4. C

The physical address is page-plus-position: enough to walk directly to the row. It is the difference between knowing an answer's location and searching for it.

### 5. B

Physical order on date makes a date range a *neighbourhood*: locate the start, read adjacent pages, stop at the end. Contiguity is the sorted layout's product, and range queries are its customer.

### 6. D

Scans are paid per page, and pages track rows: double the data, double the reading. Linear growth is the full scan's signature — and the reason it becomes untenable quietly, then suddenly.

### 7. A

Disk-to-memory transfer dominates, and it is billed per page. Once a page is in memory, its rows cost almost nothing to inspect — so five scattered rows out-cost fifty packed ones. Pages predict the bill; rows only describe the merchandise.

### 8. C

Hashing is placement by computation: the same function that stored the row re-finds it. No search, no order, no scan — one arithmetic step to the right bucket.

### 9. D

The 20,000× gap is a tale of access paths: the key search reads a handful of pages; the note filter reads them all. Column types are bystanders — what differs is whether anything narrows the hunt.

### 10. B

Table → pages → files: the SQL abstraction down to the operating system's storage. Every later cost argument in the chapter stands on this chain.

### 11. C

8 KB ÷ ~100 bytes ≈ 80 residents per page. Dense packing is why one page read can serve many rows — and why row width (later questions) matters so much.

### 12. A

The heap asks nothing of an insert: no position to find, no order to preserve. For a firehose of writes with few reads, that is precisely the right indifference.

### 13. D

`EXPLAIN` is the missing prefix: it previews the plan without running the SELECT. A `Seq Scan on freight` line is direct evidence that PostgreSQL plans to examine the heap page by page.

### 14. B

Address → page → extraction: the page is fetched (or found already in memory) and the row is lifted from its known slot. No page other than the named one is touched.

### 15. C

PostgreSQL's `CLUSTER` rewrites the table into the chosen index order once; it does not maintain that order automatically. Later inserts use available heap space, so locality can fade and the table may need to be clustered again.

### 16. A

Same rows, different neighbourhoods: S packs the week shoulder-to-shoulder; H scattered it by arrival. The query's bill is the number of pages visited, and layout decides that number.

### 17. D

Rows live in pages, always — packed, tracked, and moved as page contents. "Loose on disk" is not a state the storage engine has.

### 18. B

Hashing buys equality speed by destroying locality: neighbours in value are strangers in placement. A range wants neighbourhoods, and the hashed file has none to offer.

### 19. C

10,000 pages → 2 s implies 40,000 → ~8 s: the scan reads them all, so the multiplier passes straight through. Size predicts cost because the work *is* the size.

### 20. A

In PostgreSQL's `ctid`, the first component is the table-page number and the second is the row's slot within that page. Thus `(3,14)` means page 3, position 14—not a query-result position or transaction number.

### 21. D

An equality-only workload never invokes the hashed file's weakness and always invokes its strength. Fit is the whole decision: the layout's blind spot must be a query the workload never asks.

### 22. B

Two independent justifications: total-read jobs cannot be beaten by selective structures, and 40 pages is trivial. The scan is optimal here — flagging it is pattern-matching without cost-thinking.

### 23. B

Width divides residents per page: 40/page versus 4/page means ~25,000 versus ~250,000 pages for the same million rows. Scans pay per page, so the same data costs ten times more to sweep. Column diet is page arithmetic.

### 24. A

The dominant query is a date range, and sorted-on-date turns every such range into a short contiguous sweep. Layout should chase the workload's shape — here, the calendar.

### 25. D

Q1 has a path; Q2 has none. Milliseconds versus a full-file read on the same table — the values' sizes are irrelevant; the existence of a route to the rows is everything.

### 26. B

"Seq Scan" is a strategy name, not an alarm. The right reaction is cost interpretation: how big is the table, how selective the filter, how often does it run. Red dashboards teach reflexes; plans deserve reading.

### 27. C

The heap's order says nothing about values, so no page can be excluded unread. The same indifference that blessed the inserts curses the hunt — one layout, two faces.

### 28. A

Three rows returned, ten thousand pages read: selectivity of the *result* does not shrink the *work* when no structure narrows the search. That gap — rows versus pages — is the entire motivation for the next chapter's indexes.

### 29. D

Same merchandise, different shipping: 100 page fetches versus 2. Cost lives in pages moved, which is why clustering related rows together (and structures that exploit it) matter.

### 30. B

Heap for the firehose, sorted for the calendar, hashed for the exact match. Each layout is a specialist; the glance table exists so the match takes one look.

### 31. C

Storage is row-whole: pages carry entire rows, and scans read entire pages. The SELECT list trims the *output*, never the *input* — asking for two columns of a wide row still hauls the row's whole page.

### 32. A

A page is a small self-describing container: this table's rows plus internal bookkeeping about where each sits and what space remains. One table per page; many rows per page.

### 33. D

`CLUSTER` created locality at one moment, but PostgreSQL did not preserve it for later inserts. New rows used available heap space, so the physical ordering gradually drifted; rerunning `CLUSTER` can restore the chosen order.

### 34. C

Identical text, identical results, 40× cost difference: the physical layer is meaning-invisible and cost-decisive. That separation is why storage tuning is safe — and why it is powerful.

### 35. C

Fixed size, many rows, the unit of storage and transfer. The definition carries the whole chapter's cost model inside it.

### 36. A

The reconciliation is division of labour: heap for cheap storage, separate structures for finding. Neither bends to the other's job — which is exactly the design the indexes chapter formalizes.

### 37. D

The sort key serves queries 1 and 2 — a jump and a sweep respectively. Crate colour is orthogonal to the physical order, so query 3 inherits the layout's indifference: all pages, no exemptions.

### 38. B

Under controlled conditions, a near-doubling of runtime when pages double is behavioural evidence consistent with a full scan. It is not as direct as reading the plan, but it tests the chapter's predicted linear scaling.

### 39. A

No imposed order, land-anywhere writes, and value-searches that need either a scan or outside help. The definition names both the gift and the bill.

### 40. C

Nothing broke; arithmetic accrued. A full scan priced at 1 GB was affordable; at 12 GB the same strategy costs twelvefold. Growth converts tolerable scans into incidents — and the fix is an access path, not nostalgia for the smaller table.

---

## Question-Type Distribution

| Higher-order assessment family | Question numbers |
|---|---|
| Cost computation and scaling | 6, 19, 23, 28, 29, 31, 40 |
| Mechanism and structure identification | 1, 2, 4, 8, 10, 11, 14, 17, 20, 32, 35, 39 |
| Missing command and direct plan evidence | 13 |
| Layout selection and fit judgment | 12, 21, 24, 30, 36 |
| Contrast and prediction | 5, 9, 16, 25, 37 |
| Misconception correction and appropriateness | 22, 26, 27 |
| Trade-off, degradation, repair, and experimentation | 3, 7, 15, 18, 33, 34, 38 |

## Blueprint Taxonomy Coverage

| Subtopic from the attached blueprint | Question numbers | Count |
|---|---|---:|
| How Data is Stored | 1, 4, 7, 10, 11, 14, 17, 20, 23, 29, 32, 35 | 12 |
| File Organization: Heap, Sorted, and Hashed Files | 2, 5, 8, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39 | 13 |
| Why Storage Layout Affects Query Speed | 3, 6, 9, 13, 16, 19, 22, 25, 26, 28, 31, 34, 37, 38, 40 | 15 |

Questions 1–10 collectively cover all three Topic 7.1 subtopics.

## Difficulty and Answer-Key Balance

- Foundational: 10 questions (3, 4, 10, 11, 12, 17, 26, 30, 35, 39)
- Intermediate: 24 questions
- Advanced: 6 questions (23, 25, 28, 33, 37, 40)
- Correct option A: 10 questions (1, 7, 12, 16, 20, 24, 28, 32, 36, 39)
- Correct option B: 10 questions (3, 5, 10, 14, 18, 22, 23, 26, 30, 38)
- Correct option C: 10 questions (4, 8, 11, 15, 19, 27, 31, 34, 35, 40)
- Correct option D: 10 questions (2, 6, 9, 13, 17, 21, 25, 29, 33, 37)
- Longest consecutive run of one correct letter: below 3 throughout
