## Introduction

Relational databases are not the only way to keep data. A family of systems usually grouped under the name NoSQL ("not only SQL") store data in other shapes, such as documents, key-value pairs, wide columns, and graphs. They emerged because some applications needed to spread data across many machines, to handle very large volumes or very flexible structures, or to answer particular kinds of question more naturally than tables allow. Each makes different trade-offs, so the practical skill is not to prefer one family but to match the store to the data and the access patterns of the application.

This topic describes the main kinds of data store, the trade-offs that distinguish them, and a method for choosing among them.

**Definition:** A data store is a system that persists data and provides ways of reading and changing it; NoSQL data stores are those that use a data model other than the relational tables-and-joins model, such as documents, key-value pairs, wide columns, or graphs, typically trading some of the guarantees or generality of relational databases for scale, flexibility, or specialised performance.

<!--
IMAGE PROMPT  ->  generate as images/07_intro_nosql_and_choosing_a_data_store.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Five differently shaped containers in a row: a table grid (relational), a nested document card, a key-and-value pair list, a wide column grid, and a node-and-edge graph, each with a small label, and a funnel above them labelled Access patterns.

ON-IMAGE TEXT: show a short bold title "NoSQL and Choosing a Data Store" plus only these few labels, large and legible: One size does not fit all. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Kinds of Data Store

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Kind</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Data model</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Strengths</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Weaknesses</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical uses</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Examples</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Relational</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tables with rows, columns, keys, and joins</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Strong consistency, rich queries, transactions, mature tooling</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Scaling writes across machines is harder; rigid schema changes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Orders, accounts, inventories, most business data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">PostgreSQL, MySQL, SQL Server</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Document</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Self-contained documents, usually JSON-like, grouped in collections; flexible structure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Natural fit for nested data; flexible schema; the whole object is fetched at once</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Joins and cross-document transactions are limited or costly; duplication of data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Content, catalogues, user profiles</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">MongoDB, Couchbase</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Key-value</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A simple map from a unique key to a value</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Extremely fast and simple; scales easily</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Query only by key; value is opaque to the store</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sessions, caches, counters, feature flags</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Redis, DynamoDB</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Wide-column</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rows identified by a key, holding flexible sets of columns grouped into families, distributed across machines</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Massive write volume; linear scaling; high availability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Queries must be designed around the key; limited joins</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Time-series, event logs, very large datasets</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cassandra, HBase</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Graph</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Nodes and edges, both with properties</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Relationships are first-class; traversals over connections are fast</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Less suited to bulk reporting; smaller ecosystems</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Social networks, recommendations, fraud detection</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Neo4j</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Search engine</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Inverted indexes over text and fields</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Full-text search, relevance ranking, filtering and aggregation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not a primary record of truth; eventual consistency</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Search boxes, log analysis</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Elasticsearch, OpenSearch</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Time-series</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Values indexed by time</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Efficient storage and queries over ranges of time</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Specialised</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Metrics, sensor data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">InfluxDB, TimescaleDB</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Object or blob storage</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Files stored under names in a flat space</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cheap, durable, near-limitless storage</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No queries on content; whole-object access</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Images, documents, backups</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Amazon S3, Azure Blob Storage</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data warehouse</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Columnar storage optimised for analysis</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fast scans and aggregations over huge data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not for transactional workloads</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reporting and analytics</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">BigQuery, Snowflake, Redshift</td>
    </tr>
  </tbody>
</table>

## Why These Differ: The Trade-offs

### Scaling

- **Vertical scaling** means a bigger machine. It is simple but has limits.
- **Horizontal scaling** means more machines. Data is divided among them by **sharding** (partitioning), assigning each piece of data to a node by a key, and often **replicated** for availability.

Many NoSQL systems were designed for horizontal scaling from the start. Relational databases can also scale out, with effort or through newer distributed products.

### Replication and Consistency

Copies of data on several machines may be updated at different moments.

- **Strong consistency:** after a write, every read sees it.
- **Eventual consistency:** copies converge given time, so a reader may briefly see old data.

### The CAP Theorem

Eric Brewer proposed, and Seth Gilbert and Nancy Lynch proved in 2002, that a distributed data system facing a **network partition** (a break in communication between nodes) must choose between **consistency** (all nodes agree) and **availability** (every request receives a response); it cannot have both during the partition. A refinement, **PACELC**, adds that even without partitions there is a trade-off between latency and consistency. In practice, the lesson is that distributed designs force explicit choices, and that each store has chosen differently.

### Schema Flexibility

Relational databases enforce a schema when data is written. Document stores often accept any structure, which is easy to start with but moves the responsibility for structure to the application, a model sometimes called **schema-on-read.** In either case there is a schema; the question is where it is enforced.

### Joins and Duplication

Relational modelling stores each fact once and combines tables with joins. Many NoSQL stores avoid joins, so data is **denormalised**: copies are embedded where they will be read together. This speeds reads and complicates updates, since every copy must be changed.

### Query Flexibility

Relational databases support ad hoc queries on any column. Many NoSQL stores require the **access patterns to be known in advance,** and the data is modelled around them. Asking a new question can mean restructuring the data.

### Transactions

Relational databases offer multi-row transactions as standard. Support in NoSQL stores varies, from none to limited scope, to full distributed transactions in some newer products.

## Choosing a Data Store

A sound method starts from the needs, not the technology.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Step</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Question</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1. Understand the data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What entities and relationships exist? Is it structured, nested, or highly connected?</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2. List the access patterns</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What reads and writes occur, how often, and how fast must they be? Which queries are not yet known?</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">3. Define the consistency needs</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can users ever see slightly old data? Which operations must never be wrong, such as payments?</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">4. Estimate the scale</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data volume, growth, and request rates now and in the future</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">5. Consider availability and durability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What happens if a node or region fails? What can be lost?</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">6. Weigh operations and skills</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Who will run it? What does the team know? Is a managed service available?</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">7. Consider cost and ecosystem</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Licence, hosting, tooling, community, and risk of lock-in</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">8. Prototype and measure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Test with realistic data and load before committing</td>
    </tr>
  </tbody>
</table>

### Sensible Defaults

- For most business applications, **start with a relational database.** It is flexible, well understood, strongly consistent, and scales further than many assume.
- **Choose specialised stores for specialised needs:** a key-value store for caching, a search engine for text search, blob storage for files, a graph database for heavily connected data, a warehouse for analytics.
- **Avoid choosing a technology for fashion, or because it is novel.** Each new store adds operating cost, a new failure mode, and a new skill to learn.

## Polyglot Persistence

A system may use **several stores, each for the job it does best**: relational for orders, a key-value store for sessions and caches, a search engine for the menu, and blob storage for images. This is called **polyglot persistence.** It brings benefits and a price.

- **Data duplication:** the same fact may exist in several stores, and they must be kept in step, often by publishing change events.
- **Consistency across stores:** there are no shared transactions, so designs rely on eventual consistency and sagas.
- **Operational burden:** every store must be monitored, secured, backed up, and upgraded.

A **system of record** (source of truth) should be identified for each kind of data, with other stores treated as derived copies that can be rebuilt.

## Changing Your Mind

Choices are costly to reverse. Protect against that by:

- Keeping access to the store behind a layer in your own code (the next topic),
- Keeping a clear model of the data independent of the product,
- Using standard interfaces where possible,
- Starting simple and splitting out specialised stores when real evidence demands.

<!--
IMAGE PROMPT  ->  generate as images/02_choosing_a_data_store.png   (16:9 explanatory diagram, place here)

A decision flow: Start at Needs and access patterns, branching by questions (structured and relational? connected? text search? cache? files? analytics?) to the matching store icon. Beside it, a small system diagram of polyglot persistence with one system of record and several derived stores.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Match the Store

1. Which store family suits a user session record looked up by a session identifier and discarded after an hour?
2. An application must offer fast full-text search over thousands of product descriptions. What is a sensible addition to the architecture?
3. A team proposes a graph database for a straightforward order-entry application because it is fashionable. How should you respond?

For case 1, a key-value store with expiry. For case 2, a search engine fed from the primary database, treated as a derived copy. For case 3, ask about access patterns and consistency needs; a relational database almost certainly fits, and a new store would add cost without benefit.

## Conclusion

A data store is a system that persists data and provides ways of reading and changing it; NoSQL data stores are those that use a data model other than the relational tables-and-joins model, such as documents, key-value pairs, wide columns, or graphs, typically trading some of the guarantees or generality of relational databases for scale, flexibility, or specialised performance. The right choice follows from the data, the access patterns, and the consistency needs, and the sensible default is relational, with specialised stores added for specialised needs.

Whatever the store, application code needs a disciplined way of working with it. The next topic describes object-relational mapping and data access layers.
