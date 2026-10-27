## Introduction

Real operations involve more than one change to data. Placing an order records the order, reduces stock, and records a payment. Transferring money subtracts from one account and adds to another. If the system fails between the steps, or if two users act at the same moment, the data can be left in a state that is wrong: money vanishing, stock sold twice, an order without lines. A transaction groups several operations into one unit of work that either happens completely or not at all, and that behaves as if it were alone even when others are running. Transactions are the central tool by which databases keep data correct.

This topic explains transactions and the ACID properties, the problems of concurrent access and the isolation levels that address them, the main approaches to concurrency control, and the other ways in which data integrity is protected.

**Definition:** A transaction is a sequence of database operations treated as a single logical unit of work that must be completed in its entirety or not at all, with guarantees of atomicity, consistency, isolation, and durability, so that data remains correct despite failures and concurrent activity.

<!--
IMAGE PROMPT  ->  generate as images/06_intro_transactions_and_data_integrity.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A bank-transfer style flow: a start marker, two linked steps (subtract from one box, add to another) enclosed in a bracket labelled Transaction, ending in either a green Commit stamp or a red Rollback arrow returning to the start state.

ON-IMAGE TEXT: show a short bold title "Transactions and Data Integrity" plus only these few labels, large and legible: All or nothing. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Unit of Work

A transaction begins, performs reads and changes, and ends in one of two ways.

- **Commit:** all the changes are made permanent and visible to others.
- **Rollback (abort):** all the changes are undone, as if the transaction had never started.

A classic example is a transfer between accounts: subtracting from the first account and adding to the second must both occur or neither. If the system fails after the subtraction and before the addition, the transaction is rolled back and the money returns.

## ACID

The properties that a transaction system guarantees are summarised by the acronym ACID, introduced by Theo Haerder and Andreas Reuter in 1983, building on work by Jim Gray.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Property</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Provided by</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Atomicity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">All of the transaction happens, or none of it does; no partial results are ever visible</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Logging of changes so that they can be undone or completed after failure</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Consistency</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A transaction takes the database from one valid state to another, respecting all the declared rules and constraints</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Constraints, together with correct application logic</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Isolation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Concurrent transactions do not interfere with one another; each behaves as though it were running alone, to a degree defined by the isolation level</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Locking or versioning of data</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Durability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Once a transaction has committed, its changes survive any failure, including a crash or power loss</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A write-ahead log written to durable storage before commit is acknowledged</td>
    </tr>
  </tbody>
</table>

Consistency is partly the database's job and partly the application's: the database enforces declared constraints, but only the application knows all the business rules.

## Concurrency Problems

When many transactions run at the same time, certain anomalies can occur if they are not properly isolated.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Anomaly</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What happens</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dirty read</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A transaction reads changes that another has not yet committed, and which may be rolled back</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A report shows an order total from a transaction that is later cancelled</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Non-repeatable read</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A transaction reads the same row twice and gets different values because another transaction changed and committed it in between</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A price changes during a calculation</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Phantom read</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A transaction runs the same query twice and finds a different set of rows, because another transaction added or removed rows</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A count of open orders changes during a report</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lost update</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Two transactions read the same value and each writes a new value based on it, so one overwrites the other</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Two customers each reduce the last portion in stock, and the stock shows one fewer instead of two</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Write skew</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Two transactions each check a condition and make non-overlapping changes that together violate a rule</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Two on-call staff each go off duty after checking that the other is on</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Deadlock</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Two transactions each wait for a resource that the other holds</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Each has locked a row the other needs</td>
    </tr>
  </tbody>
</table>

The lost update is the classic danger of the "check, then act" pattern: reading a value, deciding, and writing back without ensuring that nothing changed in between.

## Isolation Levels

Perfect isolation is costly, so databases offer levels that trade protection against concurrency and speed. The SQL standard defines four.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Level</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Dirty reads</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Non-repeatable reads</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Phantom reads</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Read uncommitted</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Possible</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Possible</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Possible</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Almost no isolation; rarely used</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Read committed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prevented</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Possible</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Possible</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A common default; each statement sees only committed data</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Repeatable read</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prevented</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prevented</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Possible in the standard; prevented in some systems</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A transaction sees a consistent view of rows it has read</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Serializable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prevented</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prevented</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prevented</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The result is the same as if transactions ran one after another; safest, with more cost and more conflicts</td>
    </tr>
  </tbody>
</table>

Systems differ in their exact behaviour, and some offer **snapshot isolation**, in which each transaction sees a consistent snapshot of the data taken at its start. A developer should know the default level of the database in use and the anomalies it still allows, and choose a stronger level, or use explicit controls, for operations that need it.

## Concurrency Control

Two broad strategies prevent conflicting changes.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Strategy</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Idea</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Advantages</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Disadvantages</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pessimistic (locking)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Assume conflicts are likely; lock the data when reading it for update so that others must wait</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Simple to reason about; prevents conflicts</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Waiting, reduced throughput, risk of deadlock, locks held while users think</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Optimistic (versioning)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Assume conflicts are rare; do not lock. Each row carries a version number or timestamp; an update succeeds only if the version is unchanged since it was read, otherwise it fails and the operation is retried</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">High concurrency; no waiting; suits web applications where users hold data for a long time</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Failed updates must be handled; poor when conflicts are frequent</td>
    </tr>
  </tbody>
</table>

Optimistic control extends naturally to APIs, as the REST topic noted: a version tag lets a consumer update a resource only if it has not changed since it was read.

A related technique is to make the **change itself atomic**, for example asking the database to subtract from the stock only if enough remains and to report whether it succeeded, so that the check and the action are one indivisible step.

### Deadlocks

When transactions wait for one another in a cycle, the database detects it and aborts one, which the application must be ready to retry. Deadlocks are reduced by accessing resources in a **consistent order**, by keeping **transactions short**, and by locking only what is needed.

## Durability and Recovery

Databases achieve durability and atomicity with a **write-ahead log**: before changing data, the system records the intended change in a log on durable storage. After a crash, the log is replayed to complete committed work and undone for uncommitted work. **Backups** and **replication** protect against loss of the whole system, and recovery must be rehearsed, as Unit 9 stressed.

## Designing Transactions

- **Define the unit of work** to include all the changes that must succeed or fail together.
- **Keep transactions short.** Long ones hold locks, increase conflicts, and risk timeouts. Never keep a transaction open while waiting for a user.
- **Do not include slow external calls** in a transaction.
- **Choose the right isolation level** for the operation.
- **Handle failure:** be ready to retry on deadlock or conflict, and make operations **idempotent** so that retries are safe.
- **Test concurrent behaviour,** which is hard to see in single-user testing.

## Beyond a Single Database

A transaction in one database does not extend across several databases or services. Options are:

- **Two-phase commit:** a coordinator asks all participants to prepare and then to commit together. It gives atomicity across systems at the cost of complexity, blocking, and availability, and is rarely used between services.
- **Sagas,** as Unit 6 described: a sequence of local transactions, each with a **compensating action** to undo it if a later step fails. The system is eventually consistent and must tolerate intermediate states.
- **Designing so that one transaction suffices,** by keeping data that must change together in the same database.

## Other Ways of Protecting Integrity

Transactions are one layer among many.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Layer</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Protection</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Input validation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reject bad data at the boundary of the application</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Application rules</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Business logic that enforces rules not expressible in the database</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Database constraints</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keys, uniqueness, checks, and references that nothing can bypass</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Transactions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Atomic and isolated changes</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Audit trails</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Immutable records of who changed what and when</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Backups and point-in-time recovery</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Return to a known good state after corruption or error</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reconciliation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Regular comparison of related data, such as ledgers, to detect discrepancies</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Access control</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Limit who and what can change data</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Monitoring</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Detect anomalies in data and behaviour</td>
    </tr>
  </tbody>
</table>

<!--
IMAGE PROMPT  ->  generate as images/02_lost_update_and_isolation_levels.png   (16:9 explanatory diagram, place here)

Left: two transactions reading stock 1, both writing 0 and one update lost, drawn as parallel timelines with the overwritten write in red; below it a fixed version using a version check that makes the second fail and retry (green). Right: a ladder of four isolation levels with anomalies prevented ticked at each rung.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Protect the Data

1. Two customers order the last portion of a dish at the same moment, and both orders are accepted. Which anomaly is this, and how can it be prevented?
2. A system crashes after the database reported a commit. What property ensures the data is still there?
3. A transaction stays open for several minutes while a user fills in a form. What is wrong?

Case 1 is a lost update, from a check-then-act race; prevent it with an atomic conditional update, optimistic version checking, or locking the stock row. Case 2 is durability, provided by the write-ahead log. In case 3, long transactions hold locks and raise conflicts; the transaction should begin only when the user submits, and optimistic control can protect against changes made meanwhile.

## Conclusion

A transaction is a sequence of database operations treated as a single logical unit of work that must be completed in its entirety or not at all, with guarantees of atomicity, consistency, isolation, and durability, so that data remains correct despite failures and concurrent activity. Understanding the anomalies of concurrent access, the isolation levels, and the choice between pessimistic and optimistic control lets developers keep data correct under real load.

Relational databases are one family of data stores. The next chapter turns to the alternatives, and to how application code works with data stores, begins with NoSQL and the question of how to choose.
