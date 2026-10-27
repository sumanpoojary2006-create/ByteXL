## Introduction

Modern applications do many things at once: a web server handles thousands of requests together, a mobile app downloads data while the screen stays responsive, and a back-end job processes a queue using several workers. Doing several things at overlapping times is called concurrency. It makes software responsive and efficient, but it also introduces problems that do not exist in sequential programs, because the order in which things happen is no longer fixed and shared data can be changed by two activities at once. These problems are difficult to reproduce and diagnose.

This topic explains the concepts of concurrency and parallelism, the models used to achieve them, the characteristic hazards, and the design principles that keep concurrent code correct.

**Definition:** Concurrency is the property of a system in which multiple tasks are in progress during overlapping periods of time, whether or not they execute at the same instant, and concurrent programming is the design of such systems so that they remain correct when the tasks interleave in unpredictable ways.

<!--
IMAGE PROMPT  ->  generate as images/10_intro_concurrency_in_application_code.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Two parallel timelines of tasks interleaved on a single processor on the left, and tasks running side by side on two processors on the right; a shared box in the middle with two arrows from both timelines pointing at it and a caution mark.

ON-IMAGE TEXT: show a short bold title "Concurrency in Application Code" plus only these few labels, large and legible: Interleaving and Sharing. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Concurrency and Parallelism

These terms are related but different.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Term</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Analogy</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Concurrency</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dealing with many things at once: structuring a program as tasks that may overlap in time</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One cook switching among several dishes</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Parallelism</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Doing many things at the same instant, on multiple processor cores</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Several cooks, each working on a dish</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Asynchrony</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Starting an operation and continuing with other work while waiting for it to finish</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Putting a dish in the oven and chopping vegetables</td>
    </tr>
  </tbody>
</table>

A concurrent program can run on a single core by switching rapidly among tasks, or in parallel on many cores.

## Why Use Concurrency

- **Responsiveness:** a user interface stays usable while work proceeds in the background.
- **Throughput:** servers handle many requests at once rather than one after another.
- **Using hardware:** modern processors have many cores that sequential code leaves idle.
- **Hiding waiting:** much of the time, programs wait for disks, networks, and databases. Waiting is cheap if other work can proceed meanwhile.

## Work That Waits and Work That Computes

Two kinds of workload need different approaches.

- **I/O-bound work** spends most of its time waiting for input or output, such as network and database calls. The remedy is to overlap the waiting.
- **CPU-bound work** spends its time computing. The remedy is to spread the computation across cores.

Applying the wrong technique wastes effort: adding more threads to a program that is slow because of one database query does nothing.

## Models of Concurrency

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Model</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Description</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Advantages</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Disadvantages</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Processes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Separate programs with their own memory, communicating through messages or files</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Strong isolation; a failure does not corrupt others</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Heavier; communication is more costly</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Threads</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Several lines of execution sharing the memory of one process</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Light; data is easily shared; use all cores</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Shared memory makes errors easy to make</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Thread pools</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A fixed set of reusable threads taking tasks from a queue</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Bounds resource use; avoids the cost of creating threads</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pool sizing and blocking must be managed</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Event loop (asynchronous, non-blocking I/O)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One thread handles many connections by reacting to events and never waiting idly</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Very efficient for many connections; avoids most locking</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A long computation blocks everything; code is structured around callbacks or async/await</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Futures and promises, async/await</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Representations of a result that will arrive later, with syntax to wait for it without blocking</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Readable asynchronous code</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Errors and cancellation need care</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Actors</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Independent entities with private state that communicate only by messages</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No shared data; scales across machines</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Message design and ordering complexity</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Message queues and workers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tasks put on a queue and consumed by separate workers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Decoupling; smoothing bursts; scale by adding workers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Delivery guarantees, duplicates, and ordering</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data parallelism</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The same operation applied to pieces of a large dataset on many cores or machines</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Good for large computations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Needs divisible work</td>
    </tr>
  </tbody>
</table>

Different programming languages favour different models. The principles of correctness below apply to all of them.

## The Fundamental Hazards

### Race Conditions

A **race condition** exists when the outcome depends on the unpredictable order in which concurrent tasks happen to run. The simplest form is the **read-modify-write** sequence: two tasks each read a counter, add one, and write it back; if they overlap, both write the same value and one increment is lost. This is the same as the lost update described for databases. Races produce errors that appear rarely, only under load, and vanish when examined.

### Data Races and Visibility

When two threads access the same memory, and at least one writes without coordination, the result is undefined in many languages. Even without overlap, modern processors and compilers reorder operations, and one thread may not see another's changes in the order or at the moment expected. Languages define **memory models** and provide tools to ensure that changes become visible.

### Deadlock

Tasks wait for each other in a cycle, and none can proceed. Four conditions together produce it: **mutual exclusion** (resources held exclusively), **hold and wait** (holding one while requesting another), **no pre-emption** (resources cannot be taken away), and **circular wait.** Removing any one prevents deadlock; the usual approach is to acquire locks in a consistent order.

### Livelock and Starvation

In **livelock** tasks keep responding to each other without making progress. In **starvation** a task is perpetually denied the resources it needs because others take precedence.

### Contention and Bottlenecks

Too many tasks competing for one lock or resource serialise the work, so that adding threads makes the program slower. Heavy locking gives the cost of concurrency without its benefit.

## Protecting Shared State

When data must be shared, access must be coordinated.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Mechanism</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Cautions</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lock (mutex)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Only one task at a time may enter a critical section</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Forgetting to lock, locking too much, deadlock</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Read-write lock</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Many readers or one writer</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">More complex; writers may starve</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Semaphore</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Limits the number of tasks using a resource</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Easy to misuse</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Atomic operations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Indivisible updates of single values supported by hardware</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cover only simple cases</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Condition variables and signals</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Let tasks wait until some condition becomes true</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Easy to misuse; spurious wake-ups</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Concurrent collections</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data structures designed to be used by many threads</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Compound operations may still need coordination</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Transactions (including software transactional memory)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Group of operations atomic as a whole</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not available everywhere</td>
    </tr>
  </tbody>
</table>

## Better Than Locking: Avoiding Shared State

The most reliable way to prevent concurrency bugs is to design so that they cannot occur.

- **Immutability:** data that never changes can be shared freely. A new version is created instead of modifying the old.
- **Confinement:** keep data within one thread or task, never shared.
- **Message passing:** tasks communicate by sending messages rather than sharing memory. The phrase "do not communicate by sharing memory; share memory by communicating" expresses the idea.
- **Statelessness:** services that keep no data between requests can be run in parallel without coordination, as the REST topic noted; state lives in a database or cache, which handles concurrency.
- **Idempotent operations:** repeating an operation has the same effect as doing it once, so retries and duplicates are safe.
- **Partitioning:** divide data so that each task owns its part.

## Concurrency in Web Applications

Most developers meet concurrency not by creating threads but through the environment.

- **A web server handles requests concurrently.** Any data shared across requests, such as global variables, caches, and singletons, must be safe for concurrent use. Request-specific data must never be stored where another request can reach it.
- **The database is the shared state.** Use transactions, constraints, and optimistic versioning, as the previous topics described.
- **Background jobs and queues** may run the same job twice, or in parallel with others. Make them idempotent and guard against double processing.
- **Multiple instances** of the application run at once, so in-process locks protect only one instance. Coordination across instances needs the database, a distributed lock, or a queue.
- **Timeouts and cancellation:** waiting forever for a slow dependency ties up resources. Every wait needs a limit and a policy.
- **Backpressure:** when work arrives faster than it can be handled, the system must slow producers or shed load, rather than queue without bound until memory is exhausted.
- **Resource limits:** pools of database connections and threads are finite; exhausting them makes the whole system stall.

## Testing and Diagnosing

Concurrency bugs are notorious because they are nondeterministic.

- **Design for correctness first.** Testing cannot prove the absence of races.
- **Keep concurrent parts small** and isolate them behind simple interfaces.
- **Stress tests** with many simultaneous tasks increase the chance of exposing problems.
- **Tools:** race detectors, thread sanitisers, and static analysis find problems that testing does not.
- **Logging with task identifiers and timestamps** helps reconstruct what happened.
- **Reviews** concentrating on shared data and lock use are effective.

## Guidelines

- Prefer **simple and well-known** patterns, such as thread pools, queues, and immutable messages, over inventing coordination schemes.
- **Minimise shared mutable state.**
- **Keep critical sections short,** and never call unknown or slow code while holding a lock.
- **Acquire locks in a fixed order.**
- **Use the highest-level tool available** (concurrent collections, queues, async frameworks) before low-level locks.
- **Document** which data is shared and how it is protected.
- **Measure** before adding concurrency to speed up a program; it adds risk and does not always add speed.

<!--
IMAGE PROMPT  ->  generate as images/02_race_condition_and_ways_to_avoid_it.png   (16:9 explanatory diagram, place here)

Top: two tasks both reading counter 5 and both writing 6, drawn on parallel timelines with a red lost-increment marker. Bottom: three green fixes side by side: a lock around the update, an atomic increment, and message passing to a single owner task.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Spot the Hazard

1. A web application keeps a counter of orders in a global variable updated by every request, and the count is sometimes too low. What is the cause and the remedy?
2. Two background workers each take a payment job from a queue and occasionally both process the same job. How can the system tolerate this?
3. A program uses fifty threads to speed up a task that mostly waits for a slow remote service, yet it gets no faster. Why?

For case 1, a race condition in a read-modify-write on shared state; use an atomic increment, or keep the count in the database. For case 2, make the job idempotent, for example by recording a unique job identifier and ignoring repeats. For case 3, the bottleneck is the remote service, not the computation; more threads only add waiting, so the remedy is to reduce or batch calls, cache, or fix the dependency.

## Conclusion

Concurrency is the property of a system in which multiple tasks are in progress during overlapping periods of time, whether or not they execute at the same instant, and concurrent programming is the design of such systems so that they remain correct when the tasks interleave in unpredictable ways. The safest designs avoid shared mutable state, use proven high-level tools, and assume that anything can run twice or in any order.

This completes the unit on APIs, data, and persistence. With the building blocks of interfaces, data storage, access, caching, and concurrency in place, the course turns from how software is built to how software work is managed, beginning with project management, estimation, and risk.
