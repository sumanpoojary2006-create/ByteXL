import random
import openpyxl

random.seed(79)

# (description, explanation, difficulty, bloom, subtopic, correct, [distractors])

WHY_JOINS_EXIST = [
    (
        "The orders table stores customer_id and restaurant_id as plain numbers, not names, because customer and restaurant details live in their own separate tables.\n\nWhy is this described as \"the relational model working exactly as intended\" rather than a mistake?",
        "Storing customer details once in a customers table and referencing them by id from orders means a customer's name is never duplicated across dozens of orders — the same normalization principle covered earlier: one fact, stored once, referenced everywhere it's needed.",
        "easy", "understand", "why-joins-exist",
        "It follows the normalization principle: a customer's details are stored once and referenced by id everywhere they're needed, avoiding duplication",
        ["It's a mistake in the schema that should be fixed by adding customer_name directly to orders", "It's done purely to save typing time when writing INSERT statements", "It's required because orders must always be smaller than customers in row count"],
    ),
    (
        "It might seem simpler to just store customer_name directly on every order row and skip the separate customers table entirely.\n\nWhy does the lesson say this approach \"breaks down quickly\"?",
        "If a customer places ten orders, their name would be duplicated ten times, and if they ever changed their registered name, all ten rows would need updating instead of just one — the exact update-anomaly problem normalization exists to prevent.",
        "medium", "analyze", "why-joins-exist",
        "The name would be duplicated across every order, and a name change would require updating every duplicate instead of one single row",
        ["It breaks down because SQL doesn't allow text columns on an orders table", "It breaks down because customer_name would need to be a foreign key, which text columns can't be", "It breaks down only because it would make the orders table too wide to query"],
    ),
    (
        "`SELECT orders.order_id, customers.customer_name, restaurants.restaurant_name, orders.amount FROM orders JOIN customers ON orders.customer_id = customers.customer_id JOIN restaurants ON orders.restaurant_id = restaurants.restaurant_id;` joins three tables at once.\n\nWhat happens to the orders, customers, and restaurants tables themselves after this query runs?",
        "Nothing was changed in any of the three tables; the join only affects what this one query returns, building a temporary, wider result on the fly for the duration of this query alone.",
        "medium", "understand", "why-joins-exist",
        "Nothing changes in any of the three source tables; the join only shapes the temporary result of this one query",
        ["All three tables are permanently merged into one combined table", "The customers and restaurants tables are deleted after the join completes", "The orders table gains new customer_name and restaurant_name columns permanently"],
    ),
    (
        "Zoya wants to know which restaurant order 4 went to, by name, not by id.\n\nWhich query correctly returns this?",
        "`SELECT orders.order_id, restaurants.restaurant_name FROM orders JOIN restaurants ON orders.restaurant_id = restaurants.restaurant_id WHERE orders.order_id = 4;` returns \"Pizza Palace,\" confirming order 4 went to the same restaurant as order 1.",
        "medium", "apply", "why-joins-exist",
        "SELECT orders.order_id, restaurants.restaurant_name FROM orders JOIN restaurants ON orders.restaurant_id = restaurants.restaurant_id WHERE orders.order_id = 4;",
        ["SELECT orders.order_id, restaurants.restaurant_name FROM orders WHERE orders.order_id = 4;", "SELECT restaurants.restaurant_name FROM restaurants WHERE restaurant_id = orders.order_id;", "SELECT orders.order_id, restaurants.restaurant_name FROM restaurants JOIN orders WHERE orders.order_id = restaurants.restaurant_id;"],
    ),
    (
        "The lesson describes a join as \"building a temporary, wider table on the fly... by pairing up matching rows from each side.\"\n\nWhy is a join necessary specifically because tables are normalized, rather than being an unrelated feature?",
        "Normalization intentionally keeps related facts apart (one customer stored once, one restaurant stored once) to avoid duplication, but a report needs those separated facts shown together on one line — a join is the tool that reassembles those deliberately separated facts back into one readable result whenever a query needs them together.",
        "hard", "analyze", "why-joins-exist",
        "Normalization deliberately keeps related facts in separate tables to avoid duplication, and joins exist specifically to reassemble those facts when a query needs them together",
        ["Joins exist to undo normalization by permanently merging tables back together", "Joins are unrelated to normalization; they exist purely for filtering rows", "Joins are only necessary when a table has no primary key defined"],
    ),
]

INNER_JOIN = [
    (
        "The plain JOIN keyword Zoya used earlier has a formal name.\n\nWhat is it, and what does JOIN default to when no other keyword is specified?",
        "INNER JOIN — JOIN by itself, with no other keyword in front of it, defaults to an inner join in every major database, so the two are the same thing, one just spelled out for clarity.",
        "easy", "remember", "inner-join",
        "INNER JOIN; plain JOIN defaults to INNER JOIN",
        ["OUTER JOIN; plain JOIN defaults to OUTER JOIN", "CROSS JOIN; plain JOIN defaults to CROSS JOIN", "NATURAL JOIN; plain JOIN defaults to NATURAL JOIN"],
    ),
    (
        "The customers table alone has 5 rows, but `SELECT COUNT(*) FROM customers INNER JOIN orders ON customers.customer_id = orders.customer_id;` returns 6, not 5 and not fewer.\n\nWhy is the joined count higher than the original table's row count?",
        "Aditi Kulkarni and Rohan Das each placed more than one order, so an inner join produces one output row for every matching pair — a customer with two orders contributes two rows to the result, which is why the total can exceed the original table's row count.",
        "medium", "analyze", "inner-join",
        "Customers with more than one order each contribute one row per matching order, so the total can exceed the original customer count",
        ["The count is wrong; INNER JOIN can never return more rows than the smaller table", "Neha Bhatt's row was somehow counted twice by mistake", "INNER JOIN always adds exactly one extra row to account for the join operation itself"],
    ),
    (
        "`SELECT customers.customer_name, restaurants.restaurant_name, orders.amount FROM orders INNER JOIN customers ON orders.customer_id = customers.customer_id INNER JOIN restaurants ON orders.restaurant_id = restaurants.restaurant_id WHERE orders.amount > 400;` runs in two clear stages.\n\nWhat happens at each stage?",
        "First, the two INNER JOIN clauses assemble the full combined view across all three tables. Only then does WHERE orders.amount > 400 remove the smaller orders, leaving just the three highest-value ones with both the customer's and restaurant's real names attached.",
        "medium", "understand", "inner-join",
        "The joins first assemble the full combined result across all three tables; WHERE then filters that combined result down to orders over 400",
        ["WHERE filters the orders table first; the joins then attach names only to the surviving rows", "Both stages happen simultaneously with no fixed order between them", "The joins only run after WHERE has already reduced the result to one row"],
    ),
    (
        "The lesson says an inner join is \"the right tool whenever a row without a match is not useful for the question being asked.\"\n\nWhy is a report on \"orders and who placed them\" a natural fit for INNER JOIN specifically?",
        "There's no reason to include a customer who has never placed an order in a report specifically about orders and who placed them, since there's nothing to report about them in that context — exactly the kind of situation where excluding unmatched rows is correct, not a limitation.",
        "medium", "apply", "inner-join",
        "A customer with no orders has nothing relevant to contribute to an orders report, so excluding them is the correct behavior, not a limitation",
        ["INNER JOIN is required any time more than one table is involved, regardless of the question", "INNER JOIN is the only join type PostgreSQL supports for reports", "A customer with no orders would cause an error if any other join type were used"],
    ),
    (
        "Zoya wants a list of every restaurant that has actually received at least one order, with no duplicates.\n\nWhich query correctly combines INNER JOIN and DISTINCT to achieve this?",
        "`SELECT DISTINCT restaurants.restaurant_name FROM orders INNER JOIN restaurants ON orders.restaurant_id = restaurants.restaurant_id;` returns Pizza Palace, Sushi Central, and Burger Barn, with Taco Town correctly missing since it has never matched an order.",
        "medium", "apply", "inner-join",
        "SELECT DISTINCT restaurants.restaurant_name FROM orders INNER JOIN restaurants ON orders.restaurant_id = restaurants.restaurant_id;",
        ["SELECT restaurants.restaurant_name FROM restaurants LEFT JOIN orders ON orders.restaurant_id = restaurants.restaurant_id;", "SELECT DISTINCT restaurants.restaurant_name FROM restaurants;", "SELECT restaurants.restaurant_name FROM orders INNER JOIN restaurants ON orders.restaurant_id = restaurants.restaurant_id GROUP BY orders.order_id;"],
    ),
]

LEFT_JOIN = [
    (
        "Zoya's manager asks \"which registered customers have never placed a single order?\" — a question an INNER JOIN cannot answer.\n\nWhy is INNER JOIN structurally incapable of answering this?",
        "An inner join between customers and orders only ever shows customers who already have a match, which means it's structurally incapable of surfacing the very customers this question cares about, the ones with no match at all.",
        "easy", "understand", "left-join",
        "INNER JOIN only shows rows with a match on both sides, so customers with zero orders are excluded by definition, not surfaced",
        ["INNER JOIN can technically do this, but it's just slower than the alternative", "INNER JOIN requires a WHERE clause to answer any question about zero matches", "This question requires a different table structure that doesn't exist yet"],
    ),
    (
        "`SELECT customers.customer_name FROM customers LEFT JOIN orders ON customers.customer_id = orders.customer_id WHERE orders.order_id IS NULL;` returns exactly one name, Neha Bhatt.\n\nWhy does checking `orders.order_id IS NULL` correctly isolate customers with no orders?",
        "Since order_id is the primary key of orders, it can only be NULL in the joined result when no matching order row existed in the first place — the LEFT JOIN fills in NULL for the order columns of unmatched customers, and filtering for that NULL isolates exactly those customers.",
        "medium", "analyze", "left-join",
        "order_id, being the primary key of orders, can only be NULL in the result when the LEFT JOIN found no matching order row at all",
        ["order_id IS NULL matches customers whose id happens to be zero", "This pattern only works if orders.order_id is explicitly declared as nullable", "IS NULL here checks whether the customer_name itself is missing, not the order"],
    ),
    (
        "`SELECT restaurants.restaurant_name, orders.order_id FROM restaurants LEFT JOIN orders ON restaurants.restaurant_id = orders.restaurant_id WHERE orders.order_id IS NULL;` returns Taco Town instead of Neha Bhatt.\n\nWhy does the exact same LEFT JOIN + IS NULL pattern answer a completely different business question here?",
        "A LEFT JOIN is not symmetric; swapping which table comes first (restaurants instead of customers) changes which side is protected from being dropped, so the same pattern now finds restaurants with no orders instead of customers with no orders.",
        "medium", "apply", "left-join",
        "Swapping which table comes first changes which side's unmatched rows are protected and found, since LEFT JOIN is not symmetric",
        ["The pattern actually returns the exact same result regardless of table order; this is a trick question", "IS NULL automatically switches its meaning based on which table has more rows", "Taco Town appears because it shares an id number with Neha Bhatt by coincidence"],
    ),
    (
        "`SELECT customers.customer_name, COUNT(orders.order_id) AS order_count FROM customers LEFT JOIN orders ON customers.customer_id = orders.customer_id GROUP BY customers.customer_name ORDER BY order_count DESC;` correctly shows Neha Bhatt with 0 orders.\n\nWhy does the query use COUNT(orders.order_id) instead of COUNT(*), and what would go wrong with COUNT(*)?",
        "COUNT(orders.order_id) counts only non-NULL values, so Neha's row (where order_id is NULL after the LEFT JOIN) correctly shows 0. Using COUNT(*) instead would incorrectly count her as 1, since COUNT(*) counts rows regardless of NULL content, and the LEFT JOIN still produces one row for her even with no match.",
        "hard", "analyze", "left-join",
        "COUNT(orders.order_id) ignores NULLs, correctly showing 0 for unmatched customers; COUNT(*) would incorrectly count them as 1, since it counts rows regardless of NULL content",
        ["COUNT(*) and COUNT(orders.order_id) always produce identical results in a LEFT JOIN", "COUNT(orders.order_id) is required syntax whenever GROUP BY is combined with LEFT JOIN", "COUNT(*) would actually show Neha as having a negative order count"],
    ),
    (
        "The manager wants to know which restaurants in Pune have never received an order, by name.\n\nWhich query correctly answers this, and what does it return given that both Pune restaurants have received at least one order?",
        "`SELECT restaurants.restaurant_name FROM restaurants LEFT JOIN orders ON restaurants.restaurant_id = orders.restaurant_id WHERE restaurants.city = 'Pune' AND orders.order_id IS NULL;` returns an empty result, correctly showing that both Pune restaurants, Pizza Palace and Burger Barn, have each received at least one order.",
        "medium", "apply", "left-join",
        "The query above, returning an empty result since both Pune restaurants already have orders",
        ["The same query, but it should return Pizza Palace and Burger Barn as restaurants with orders", "SELECT restaurants.restaurant_name FROM restaurants INNER JOIN orders ON restaurants.restaurant_id = orders.restaurant_id WHERE restaurants.city = 'Pune';", "SELECT restaurants.restaurant_name FROM restaurants WHERE restaurants.city = 'Pune' AND restaurant_id NOT IN (SELECT restaurant_id FROM orders) IS NULL;"],
    ),
]

RIGHT_FULL_OUTER_JOIN = [
    (
        "Zoya realizes `restaurants LEFT JOIN orders` and `orders RIGHT JOIN restaurants` protect the same table from opposite directions.\n\nWhat does a RIGHT JOIN guarantee?",
        "A RIGHT JOIN guarantees every row from the table named after RIGHT JOIN survives, regardless of a match — it's the mirror image of a LEFT JOIN, just protecting the table on the other side of the keyword.",
        "easy", "understand", "right-join-and-full-outer-join",
        "Every row from the table named after RIGHT JOIN survives, matched or not",
        ["Every row from the table named after FROM survives, matched or not", "Every row from both tables survives, matched or not", "Only rows matched on both sides survive, exactly like INNER JOIN"],
    ),
    (
        "The lesson notes most SQL style guides prefer LEFT JOIN over RIGHT JOIN for readability.\n\nWhat practical benefit does being able to mentally convert a RIGHT JOIN into an equivalent LEFT JOIN provide?",
        "Since LEFT JOIN is far more commonly used across real codebases, being able to convert a RIGHT JOIN into an equivalent LEFT JOIN makes it easier to read queries written by other people without keeping two separate mental models for what is ultimately the same underlying operation.",
        "medium", "understand", "right-join-and-full-outer-join",
        "It avoids needing two separate mental models, since LEFT JOIN is far more common in real codebases and the two are functionally mirror images",
        ["It makes RIGHT JOIN queries run measurably faster once converted", "It's required, since PostgreSQL doesn't actually support RIGHT JOIN natively", "It only matters for queries involving exactly three or more tables"],
    ),
    (
        "Neither LEFT JOIN nor RIGHT JOIN alone can show unmatched rows from both customers and orders simultaneously in one result.\n\nWhat does FULL OUTER JOIN do differently?",
        "FULL OUTER JOIN protects both sides simultaneously, keeping every row from either table, matched or not — essentially a LEFT JOIN and a RIGHT JOIN combined into a single result, with no row from either side left out.",
        "medium", "understand", "right-join-and-full-outer-join",
        "It keeps every row from both tables at once, matched or not, combining what LEFT JOIN and RIGHT JOIN each do separately",
        ["It keeps only rows matched on both sides, exactly like INNER JOIN", "It keeps rows from neither table unless matched on a third table", "It only works when both tables have exactly the same number of rows"],
    ),
    (
        "`SELECT customers.customer_name, orders.order_id FROM customers FULL OUTER JOIN orders ON customers.customer_id = orders.customer_id WHERE customers.customer_id IS NULL OR orders.order_id IS NULL;`\n\nWhat does this query surface, and why does it check both sides with OR rather than just one?",
        "It surfaces every row missing a partner on either side, in one query — checking customers.customer_id IS NULL catches orders with no matching customer, while orders.order_id IS NULL catches customers with no matching order, and OR combines both possibilities since a FULL OUTER JOIN can produce mismatches from either direction.",
        "hard", "analyze", "right-join-and-full-outer-join",
        "It finds rows missing a partner on either side; OR is needed because a FULL OUTER JOIN can leave unmatched rows originating from either table",
        ["It surfaces only customers with orders, since OR always selects the more permissive condition", "Checking both sides with OR is redundant; either condition alone would work identically", "It surfaces rows that match on both sides simultaneously, the opposite of what OR usually means"],
    ),
    (
        "According to the full join family table, which join type keeps \"All, matched or not\" rows from BOTH the left table and the right table simultaneously?",
        "FULL OUTER JOIN — INNER JOIN keeps only matched rows on both sides, LEFT JOIN protects only the left table's rows, RIGHT JOIN protects only the right table's rows, and FULL OUTER JOIN is the only one protecting both sides at once.",
        "easy", "remember", "right-join-and-full-outer-join",
        "FULL OUTER JOIN",
        ["INNER JOIN", "LEFT JOIN", "RIGHT JOIN"],
    ),
]

SELF_JOINS = [
    (
        "The riders table stores every rider once, with a mentor_id column pointing back to another rider's own rider_id, and Zoya needs each rider's name next to their mentor's name.\n\nWhy does this report still need a join, even though only one table (riders) is involved?",
        "A query cannot visually trace mentor_id back up to the mentor's row the way a human reading the table by eye can — it needs the mentor's row and the mentee's row joined together as two separate table references, even though both rows live in the exact same physical table.",
        "easy", "understand", "self-joins",
        "A query can't visually trace a reference back to another row the way a human can; it needs the two rows joined as separate table references",
        ["It doesn't actually need a join; a single SELECT with no JOIN can produce this report", "It needs a join only because riders has more than 100 rows", "It needs a join because mentor_id is stored as text rather than a number"],
    ),
    (
        "The plain INNER JOIN self join drops Suresh and Arjun entirely, since their mentor_id is NULL and finds no match.\n\nWhich change makes the report show every rider, mentored or not, with NULL in the mentor column for unmentored riders?",
        "Switching to a LEFT JOIN self join: `SELECT mentee.rider_name AS rider, mentor.rider_name AS mentor FROM riders mentee LEFT JOIN riders mentor ON mentee.mentor_id = mentor.rider_id;` — this solves the unmatched-row problem for a self join exactly the same way LEFT JOIN solved it for two different tables.",
        "medium", "apply", "self-joins",
        "Changing the self join from INNER JOIN to LEFT JOIN",
        ["Adding a WHERE clause that explicitly checks mentor_id IS NOT NULL", "Switching the aliases so mentor comes before mentee in the FROM clause", "Adding a third alias to represent riders with no mentor separately"],
    ),
    (
        "`SELECT DISTINCT mentor.rider_name AS is_a_mentor FROM riders mentee JOIN riders mentor ON mentee.mentor_id = mentor.rider_id;` returns Suresh, Arjun, and Deepa.\n\nWhy is DISTINCT necessary here, and why does Deepa appear even though she herself is mentored by Suresh?",
        "DISTINCT collapses duplicates, since Suresh mentors two people (Deepa and Farhan) and without it his name would appear twice. Deepa appears because she mentors Om Prakash even though she is also mentored by Suresh, showing that a rider can be both a mentee and a mentor at the same time.",
        "medium", "analyze", "self-joins",
        "DISTINCT removes repeat entries for mentors with multiple mentees; Deepa appears because she is simultaneously a mentee (of Suresh) and a mentor (of Om Prakash)",
        ["DISTINCT is not actually necessary here; the query would return the same result without it", "Deepa appears by mistake, since the query is only supposed to find riders with no mentor", "DISTINCT removes Deepa from the result, but she reappears due to a separate join"],
    ),
    (
        "Zoya wants to know which riders share the same mentor as Farhan Iqbal, not including Farhan himself.\n\nWhat kind of self join, combined with which additional filter, correctly answers this?",
        "A self join on matching mentor_id values (finding riders whose mentor_id equals Farhan's mentor_id), filtered to exclude Farhan's own name from the result — returning Deepa Krishnan, since both she and Farhan are mentored by Suresh Pillai.",
        "hard", "apply", "self-joins",
        "A self join matching on shared mentor_id, with a filter excluding Farhan's own name from the result",
        ["A self join on matching rider_id values, with no filter needed at all", "A LEFT JOIN self join specifically, since Farhan himself has no mentor", "An INNER JOIN on rider_name instead of mentor_id, filtering for exact matches"],
    ),
    (
        "The lesson concludes that \"a self join is not a different kind of join mechanically.\"\n\nWhat does this mean about the relationship between a self join and the other join types (INNER, LEFT, etc.) covered earlier?",
        "A self join is the same JOIN, LEFT JOIN, or any other join type covered so far, just applied to one table referenced twice under two different aliases — the mechanics are identical to a two-table join, only the source table happens to be the same physical table on both sides.",
        "medium", "understand", "self-joins",
        "A self join uses the exact same JOIN mechanics as a two-table join; the only difference is that both sides happen to reference the same physical table",
        ["A self join requires entirely different SQL syntax not used by any other join type", "A self join can only ever be an INNER JOIN, never a LEFT or RIGHT JOIN", "A self join is a completely separate SQL feature unrelated to JOIN, LEFT JOIN, etc."],
    ),
]

MULTITABLE_JOINS = [
    (
        "A real order touches four tables at once: customers, restaurants, riders, and orders. The dispatch manager wants one line per order showing the customer's, restaurant's, and rider's names together.\n\nDoes answering this require learning a new kind of join?",
        "No — it just needs more of the same JOIN clauses chained one after another, each one attaching another table to the growing result; multi-table joins aren't a new mechanism, just more JOIN clauses used together.",
        "easy", "understand", "multi-table-joins",
        "No, it just requires chaining more JOIN clauses, each attaching one more table, using the same JOIN mechanics already covered",
        ["Yes, it requires a special MULTIJOIN keyword not used for two-table joins", "Yes, it requires converting all four tables into one physical table first", "No, but it does require abandoning JOIN entirely in favor of subqueries"],
    ),
    (
        "As the number of joined tables grows, writing the full table name in front of every column gets noisy.\n\nWhat solves this, and what does `FROM orders o JOIN customers c ON o.customer_id = c.customer_id ...` accomplish compared to spelling out full table names?",
        "Table aliases (o, c, r, d) give each table a short alias immediately after naming it, and every column reference afterward uses that alias instead of the full table name — producing an identical result to spelling out full names, just noticeably shorter to type and easier to scan.",
        "medium", "apply", "multi-table-joins",
        "Table aliases shorten column references while producing an identical result, making the query easier to type and read as more tables are added",
        ["Aliases change which rows are returned, filtering out unmatched rows more aggressively", "Aliases are required by SQL syntax once more than two tables are joined", "Aliases replace the need for ON conditions in each JOIN clause"],
    ),
    (
        "The dispatch manager wants every order shown even for a rider who has somehow not yet been assigned.\n\n`FROM orders o JOIN customers c ON o.customer_id = c.customer_id JOIN restaurants r ON o.restaurant_id = r.restaurant_id LEFT JOIN riders d ON o.rider_id = d.rider_id;` mixes join types.\n\nWhat does this mixture express about which relationships are mandatory versus optional?",
        "Every order still requires a valid customer and a valid restaurant to appear, since those two joins stay as strict INNER JOIN, but an order would still show up even with a NULL rider name if its rider_id didn't match anything in riders, since that join is a LEFT JOIN — mixing join types lets a query express exactly which relationships are mandatory and which are optional, all in one statement.",
        "hard", "analyze", "multi-table-joins",
        "Customer and restaurant matches are mandatory (INNER JOIN); a rider match is optional (LEFT JOIN), so orders without an assigned rider still appear with a NULL rider name",
        ["All three relationships become optional the moment any one JOIN in the chain is a LEFT JOIN", "Mixing join types is invalid SQL and this query would fail to run", "The LEFT JOIN on riders makes customer and restaurant matches optional too, by cascading"],
    ),
    (
        "`SELECT d.rider_name, COUNT(*) AS deliveries, SUM(o.amount) AS total_delivered_value FROM orders o JOIN riders d ON o.rider_id = d.rider_id GROUP BY d.rider_name ORDER BY deliveries DESC;`\n\nWhat does this query demonstrate about how GROUP BY and aggregate functions interact with a join, once the join has already run?",
        "Once tables are joined, WHERE, GROUP BY, and aggregate functions all work exactly as they did on a single table or a two-table join, just with more columns available to filter or group by — grouping happens by rider name after the join has already attached each order to its rider.",
        "medium", "understand", "multi-table-joins",
        "GROUP BY and aggregates work exactly as they do on a single table, just now with additional columns available from the joined tables",
        ["GROUP BY cannot be combined with a JOIN at all; this query would raise an error", "The join must run after GROUP BY completes, reversing the usual execution order", "Aggregate functions only work on the original orders table, ignoring joined columns"],
    ),
    (
        "The dispatch manager wants, for every order over 300 in amount, the customer's name and rider's name only, ordered by amount descending, across the orders, customers, and riders tables.\n\nWhich query correctly produces this?",
        "Joining orders to customers and riders, filtering with WHERE o.amount > 300, and ordering by o.amount DESC — Rohan Das's order delivered by Suresh Pillai comes out on top at 620.00.",
        "medium", "apply", "multi-table-joins",
        "JOIN orders to customers and riders, filter with WHERE o.amount > 300, order by o.amount DESC",
        ["JOIN orders to customers and riders, filter with HAVING o.amount > 300, order by o.amount DESC", "JOIN orders to customers and riders, order by o.amount DESC, then filter with WHERE o.amount > 300 written after ORDER BY", "GROUP BY o.amount, then JOIN customers and riders, filtering with WHERE amount > 300"],
    ),
]

SEMI_ANTI_JOINS = [
    (
        "Zoya's earlier LEFT JOIN + WHERE orders.order_id IS NULL pattern found customers with no orders, but it \"quietly relies on picking exactly the right column to check for NULL.\"\n\nWhat more direct way does the lesson introduce for asking \"does a matching row exist\" or \"does no matching row exist\"?",
        "EXISTS and NOT EXISTS — these patterns are known as a semi join (returns rows from one table where a match exists elsewhere, without pulling in columns from that other table) and an anti join (returns rows where no match exists).",
        "easy", "remember", "semi-and-anti-joins",
        "EXISTS and NOT EXISTS",
        ["UNION and INTERSECT", "GROUP BY and HAVING", "CAST and CONVERT"],
    ),
    (
        "The lesson notes EXISTS \"behaves differently from an INNER JOIN in one important way\": a customer can never appear more than once in an EXISTS result, even if they placed multiple orders.\n\nWhy would an equivalent INNER JOIN produce duplicate customer rows that EXISTS avoids?",
        "EXISTS only ever checks yes-or-no per customer, while an INNER JOIN version of the same idea would duplicate a customer once per matching order, exactly the multiplying-rows behavior covered in the INNER JOIN lesson (a customer with two orders contributes two joined rows).",
        "medium", "analyze", "semi-and-anti-joins",
        "An INNER JOIN produces one row per matching order pair, so a customer with multiple orders appears multiple times; EXISTS only checks yes-or-no once per customer",
        ["INNER JOIN and EXISTS always produce identical row counts; this is a misconception", "EXISTS actually produces more duplicate rows than an equivalent INNER JOIN would", "The difference only appears when the orders table has fewer rows than customers"],
    ),
    (
        "`SELECT customer_name FROM customers c WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.customer_id);` returns exactly Neha Bhatt, the same answer as the earlier LEFT JOIN + IS NULL pattern.\n\nWhat does NOT EXISTS state more directly than that pattern, according to the lesson?",
        "NOT EXISTS states the intent more directly: \"keep this customer only if no order references them,\" rather than \"join every order, then throw away everything except the empty matches,\" which is what the LEFT JOIN + IS NULL approach effectively does.",
        "medium", "understand", "semi-and-anti-joins",
        "It directly states \"keep this row only if no match exists,\" rather than joining everything and then filtering for the empty matches afterward",
        ["NOT EXISTS runs measurably faster in every database system, which is its only real advantage", "NOT EXISTS is the only pattern capable of finding customers with zero orders", "NOT EXISTS requires fewer characters to type, which is its primary benefit"],
    ),
    (
        "`WHERE customer_id NOT IN (SELECT customer_id FROM orders WHERE customer_id IS NOT NULL)` deliberately filters out NULL values from the subquery first.\n\nWhat would happen if that `WHERE customer_id IS NOT NULL` filter were left out, and even one NULL slipped into the subquery's results?",
        "The entire NOT IN condition would return no rows at all for every customer — a well-known trap with NOT IN that NOT EXISTS does not share, which is exactly why NOT EXISTS is generally the safer default over NOT IN whenever the compared column can contain NULL.",
        "hard", "analyze", "semi-and-anti-joins",
        "The entire NOT IN condition would silently return zero rows for every customer, a known trap that NOT EXISTS avoids",
        ["Nothing would change; NOT IN handles NULL values in the subquery gracefully", "It would only affect the one customer whose id happens to match the NULL row", "The query would raise a clear, explicit error naming the NULL as the cause"],
    ),
    (
        "The lesson states that semi and anti joins \"are not written using JOIN, LEFT JOIN, or any other join keyword in standard SQL.\"\n\nWhat does the term \"semi join\" or \"anti join\" actually describe, if not a specific SQL keyword?",
        "It describes the shape of the result, one row from the outer table per match found or not found, with no columns pulled in from the other table, rather than a specific piece of SQL syntax — semi and anti joins are existence checks expressed with EXISTS, NOT EXISTS, IN, or NOT IN.",
        "medium", "understand", "semi-and-anti-joins",
        "The shape of the result (existence-checked rows with no columns pulled from the other table), not a specific SQL keyword or syntax",
        ["A deprecated SQL feature that has been replaced entirely by EXISTS", "A join type only available in NoSQL databases, not in PostgreSQL", "A synonym for INNER JOIN used interchangeably in casual conversation"],
    ),
]

SYNTHESIS = [
    (
        "Zoya's LEFT JOIN + WHERE order_id IS NULL pattern and her later NOT EXISTS pattern both correctly find customers with no orders.\n\nWhat structural difference between the two approaches explains why NOT EXISTS is described as more \"direct\"?",
        "LEFT JOIN first widens every customer row with order columns (filling NULL where there's no match), and only then filters for those NULLs as a second step; NOT EXISTS skips the widening step entirely and directly tests for the absence of a match, without ever attaching any order columns to the result at all.",
        "medium", "analyze", "semi-and-anti-joins",
        "LEFT JOIN widens rows first and then filters for NULLs as a separate step; NOT EXISTS directly tests for absence without ever widening the rows at all",
        ["The two approaches are identical in every respect, including performance and readability", "NOT EXISTS actually widens rows the same way LEFT JOIN does, just with different syntax", "LEFT JOIN cannot check for absence at all; only NOT EXISTS is capable of it"],
    ),
    (
        "Zoya's mentorship self join (riders joined to riders) and her four-table dispatch report (orders joined to customers, restaurants, and riders) both chain JOIN clauses, but for different structural reasons.\n\nWhat's the key difference between why each one needs multiple table references?",
        "The self join needs two references to the *same* table because a hierarchy (mentor and mentee) is stored within one table's own rows, requiring aliases to distinguish the two roles a row can play. The multi-table join needs references to *different* tables because customer, restaurant, and rider facts are genuinely stored in separate tables, each needing its own JOIN clause to attach.",
        "hard", "analyze", "multi-table-joins",
        "The self join joins one table to itself to resolve a hierarchy stored within its own rows; the multi-table join attaches genuinely separate tables holding different kinds of facts",
        ["Both joins exist for exactly the same reason: combining data spread across multiple physical tables", "The self join actually involves four different tables, just like the dispatch report", "The multi-table join is really a self join in disguise, since orders references itself indirectly"],
    ),
    (
        "INNER JOIN drops unmatched rows, LEFT JOIN keeps unmatched rows from one side with NULLs filled in, and NOT EXISTS keeps only the unmatched rows themselves with no columns from the other table at all.\n\nIf a report needs to show every customer along with their order count (including customers with a genuine 0), which of these three tools is the right fit, and why do the other two fall short?",
        "LEFT JOIN combined with GROUP BY and COUNT(orders.order_id) is the right fit, since it keeps every customer (matched or not) and lets COUNT correctly report 0 for unmatched ones. INNER JOIN falls short because it would drop zero-order customers entirely, and NOT EXISTS falls short because it only returns a yes/no existence result, not a count that also includes customers who do have orders.",
        "hard", "apply", "left-join",
        "LEFT JOIN with GROUP BY and COUNT is the right fit; INNER JOIN would drop zero-order customers, and NOT EXISTS can't report a count at all, only existence",
        ["INNER JOIN is the right fit, since it naturally includes a count of zero for every customer", "NOT EXISTS is the right fit, since it can return both a count and a yes/no existence flag in one query", "All three tools produce identical results for this particular report"],
    ),
    (
        "Comparing the RIGHT JOIN / LEFT JOIN mirror relationship with the EXISTS / NOT EXISTS pairing: both pairs are described as \"opposites\" of each other in some sense.\n\nWhat's the key difference in what each pair's \"opposite\" actually means?",
        "RIGHT JOIN and LEFT JOIN are opposites in terms of which table's rows get protected from being dropped (structurally identical, just mirrored). EXISTS and NOT EXISTS are opposites in terms of the truth value being tested (keep rows where a match exists vs. keep rows where no match exists) — one is about which side is protected, the other is about which condition (presence vs. absence) is being checked.",
        "hard", "analyze", "right-join-and-full-outer-join",
        "LEFT/RIGHT JOIN are opposite in which table's rows get protected (a structural mirror); EXISTS/NOT EXISTS are opposite in which truth value is tested (presence vs. absence of a match)",
        ["Both pairs are opposites in exactly the same way: which table appears first in the FROM clause", "LEFT/RIGHT JOIN test presence vs. absence; EXISTS/NOT EXISTS protect different tables from being dropped", "There is no meaningful difference; all four keywords behave identically under the hood"],
    ),
    (
        "Every join lesson in this chapter (INNER, LEFT, RIGHT, FULL OUTER, self, multi-table) combines rows from two or more table references based on a matching condition, widening each row with extra columns.\n\nHow does this shared \"widen sideways\" behavior distinguish every kind of JOIN from the semi/anti join patterns covered in the final lesson?",
        "Every JOIN variant, no matter how many tables or which match/no-match rules apply, produces wider rows carrying columns from more than one table reference. Semi and anti joins (EXISTS/NOT EXISTS/IN/NOT IN) never widen a row at all; they only test for existence and return rows from a single table, unchanged in shape, regardless of how many other tables are checked against.",
        "medium", "understand", "semi-and-anti-joins",
        "Every JOIN variant widens rows with columns from multiple tables; semi/anti joins never widen rows at all, only testing existence and returning unchanged rows from one table",
        ["Semi and anti joins also widen rows, just using a different keyword than JOIN", "JOIN variants never widen rows; only semi and anti joins add extra columns", "There is no real distinction; JOIN and EXISTS-based patterns behave identically in every case"],
    ),
]

SET1_SOURCES = [
    (WHY_JOINS_EXIST, 0),
    (INNER_JOIN, 0),
    (LEFT_JOIN, 0),
    (RIGHT_FULL_OUTER_JOIN, 0),
    (SELF_JOINS, 0),
    (MULTITABLE_JOINS, 0),
    (SEMI_ANTI_JOINS, 0),
]

SET1 = [src[idx] for src, idx in SET1_SOURCES]
SET1.extend(SYNTHESIS[:3])

SET2 = (
    WHY_JOINS_EXIST[1:]
    + INNER_JOIN[1:]
    + LEFT_JOIN[1:]
    + RIGHT_FULL_OUTER_JOIN[1:]
    + SELF_JOINS[1:]
    + MULTITABLE_JOINS[1:]
    + SEMI_ANTI_JOINS[1:]
    + SYNTHESIS[3:]
)

assert len(SET1) == 10, len(SET1)
assert len(SET2) == 30, len(SET2)


def build_rows(items, set_label, title_prefix):
    positions = [(i % 4) + 1 for i in range(len(items))]
    random.shuffle(positions)

    rows = []
    for idx, (desc, expl, diff, bloom, subtopic, correct, distractors) in enumerate(items, start=1):
        pos = positions[idx - 1]
        options = distractors[:]
        options.insert(pos - 1, correct)
        rows.append({
            "title": f"{title_prefix}.{idx}",
            "description": desc,
            "explanation": expl,
            "score": 1,
            "status": "published",
            "difficulty": diff,
            "bloomTaxonomy": bloom,
            "tags": f"dbms - {set_label}",
            "subjects": "dbms",
            "topics": "sql-for-data-retrieval-and-analytics",
            "subTopics": subtopic,
            "companies": None,
            "option1": options[0],
            "option2": options[1],
            "option3": options[2],
            "option4": options[3],
            "answer": pos,
        })
    return rows


rows1 = build_rows(SET1, "Set 1", "DBMS - MCQ - 4.3.1")
rows2 = build_rows(SET2, "Set 2", "DBMS - MCQ - 4.3.2")
all_rows = rows1 + rows2


def summarize(name, rs):
    diff, bloom, sub, ans = {}, {}, {}, {1: 0, 2: 0, 3: 0, 4: 0}
    for r in rs:
        diff[r["difficulty"]] = diff.get(r["difficulty"], 0) + 1
        bloom[r["bloomTaxonomy"]] = bloom.get(r["bloomTaxonomy"], 0) + 1
        sub[r["subTopics"]] = sub.get(r["subTopics"], 0) + 1
        ans[r["answer"]] += 1
    print(name, "diff:", diff)
    print(name, "bloom:", bloom)
    print(name, "subtopics:", sub)
    print(name, "answers:", ans)


summarize("SET1", rows1)
summarize("SET2", rows2)

descs = [r["description"] for r in all_rows]
assert len(descs) == len(set(descs)), "duplicate description found"
for r in all_rows:
    opts = [r["option1"], r["option2"], r["option3"], r["option4"]]
    assert len(set(opts)) == 4, f"duplicate option in {r['title']}: {opts}"

headers = ["title", "description", "explanation", "score", "status", "difficulty", "bloomTaxonomy",
           "tags", "subjects", "topics", "subTopics", "companies",
           "option1", "option2", "option3", "option4", "answer"]

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "DBMS - MCQ - Unit 4.3"
ws.append(headers)
for r in all_rows:
    ws.append([r[h] for h in headers])

out_path = "content/Question Bank/MCQ/DBMS/Unit 4 - SQL for Data Retrieval and Analytics/4.3 - Joins - MCQ.xlsx"
wb.save(out_path)
print("Saved", out_path, "with", len(all_rows), "questions")
