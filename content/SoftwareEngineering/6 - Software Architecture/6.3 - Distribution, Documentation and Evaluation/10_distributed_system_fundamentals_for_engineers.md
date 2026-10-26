## Introduction

Inside a single program, a function call either works or the program fails. Between machines, a request can be lost, delayed, duplicated, or answered after the sender has given up. Different parts of a system may disagree about what has happened. Most modern systems, from mobile apps to large services, are distributed, so every software engineer needs a working intuition for these problems, even without studying the mathematics behind them.

**Definition:** A distributed system is a collection of independent computers that cooperate over a network to appear to users as one coherent system, and its engineering is dominated by problems that do not occur on a single machine: network delay, partial failure, lack of shared time, and the difficulty of keeping copies of data consistent.

<!--
IMAGE PROMPT  ->  generate as images/10_intro_distributed_system_fundamentals_for_engineers.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Several computer nodes connected by lines, one connection shown broken with a red lightning mark, a clock beside each node showing a slightly different time, and a message envelope lost in the middle of a line.

ON-IMAGE TEXT: show a short bold title "Distributed System Fundamentals" plus only these few labels, large and legible: Network, Failure, Time. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## What Makes Distribution Hard

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Difficulty</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Explanation</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Consequence</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Latency</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A call over a network takes far longer than a call in memory, and the delay varies</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Chatty designs are slow; waiting must be bounded</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Partial failure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Some parts fail while others keep working, and the sender often cannot tell which</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A caller may not know whether a request was carried out</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unreliable networks</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Messages can be lost, delayed, duplicated, or reordered</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Retries are needed, but they may cause duplicates</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No shared clock</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Each machine keeps its own time, and clocks drift</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Events cannot always be ordered by timestamp</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No shared memory</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Machines exchange information only by messages</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">State must be copied, so copies can disagree</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Concurrency</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Many operations run at once on different machines</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Conflicting updates and race conditions</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Scale</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">More machines mean more components and more chances of failure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Failure is routine, not exceptional</td>
    </tr>
  </tbody>
</table>

## The Fallacies of Distributed Computing

Engineers at Sun Microsystems, notably Peter Deutsch, listed assumptions that newcomers wrongly make. Each is false:

1. The network is reliable.
2. Latency is zero.
3. Bandwidth is infinite.
4. The network is secure.
5. Topology does not change.
6. There is one administrator.
7. Transport cost is zero.
8. The network is homogeneous.

Designs that rely on any of these break in production. Awareness of them is the first defence.

## Handling Failure

Because failure is normal, systems are designed to expect and contain it.

- **Timeouts:** never wait forever for a response; decide how long is reasonable.
- **Retries with backoff:** retry a failed request, waiting longer between attempts and adding random variation, so that many clients do not retry at the same moment and overwhelm a recovering service.
- **Idempotency:** design operations so that repeating them has the same effect as doing them once, such as setting a value, not adding to it. Then retries are safe.
- **Circuit breakers:** if a dependency keeps failing, stop calling it for a while and fail quickly, giving it time to recover and preventing failures from spreading. The pattern was popularised by Michael Nygard.
- **Redundancy:** run several copies so that the loss of one does not stop the service.
- **Graceful degradation:** keep providing the essential function when a non-essential part fails, for example showing the menu without personalised recommendations.
- **Bulkheads:** isolate resources so that overload in one area cannot exhaust everything, like watertight compartments in a ship.

## Replication, Partitioning, and Consistency

Two techniques underlie most scalable data systems.

- **Replication** keeps copies of data on several machines, for availability and read performance. The difficulty is keeping the copies in agreement when updates occur.
- **Partitioning (sharding)** divides data among machines, for capacity and write performance. The difficulty is queries and transactions that span partitions.

**Consistency** describes what a reader may see after a write.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Model</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Trade-off</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Strong consistency</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Every read sees the most recent write, as if there were one copy</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Simple to reason about, but slower and less available during failures</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Eventual consistency</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">If no new updates occur, all copies eventually agree; reads may briefly return old data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fast and highly available, but the application must tolerate stale reads</td>
    </tr>
  </tbody>
</table>

## The CAP Theorem

Eric Brewer conjectured in 2000, and Seth Gilbert and Nancy Lynch proved in 2002, a result about data shared across machines: when a **network partition** occurs, so that machines cannot communicate, a system must choose between **consistency** (refusing some requests so that all copies stay in agreement) and **availability** (answering every request, possibly with stale data). It cannot have both during the partition. Partitions are a fact of networks, so the practical choice is what to give up when they happen. A later refinement notes that even without partitions there is a trade-off between latency and consistency. The theorem is a reminder that **trade-offs are unavoidable**, not a rule that classifies products.

## Availability in Numbers

Availability targets are often described in "nines".

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Availability</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Approximate downtime per year</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">99% (two nines)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">About 3.65 days</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">99.9% (three nines)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">About 8.8 hours</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">99.99% (four nines)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">About 53 minutes</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">99.999% (five nines)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">About 5 minutes</td>
    </tr>
  </tbody>
</table>

When a request depends on several components in series, the overall availability is the product of theirs, so a chain of services each at 99.9% is less available than any one of them. This is a strong argument against long chains of synchronous calls.

## Scalability

Systems scale **vertically** by using bigger machines, or **horizontally** by adding machines. Horizontal scaling needs designs that spread work: stateless services behind load balancers, data partitioned or replicated, and slow work moved to queues. A system is scalable when adding resources increases capacity roughly in proportion, and the bottlenecks, such as a single database, are removed or managed.

<!--
IMAGE PROMPT  ->  generate as images/02_failure_handling_toolkit.png   (16:9 explanatory diagram, place here)

A client calling a service through a ring of protective icons labelled Timeout, Retry with backoff, Circuit breaker, Bulkhead, Redundant copies. A side panel shows three replicas of a data store with an arrow labelled Replication and a split labelled Partitioning.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Choose the Defence

1. A call to a payment service sometimes hangs for minutes, tying up the application.
2. A client retries a "charge the customer" request after a timeout, and the customer is charged twice.
3. One failing recommendation service slows every page of the application.

Case 1 needs a timeout. Case 2 needs an idempotent operation, for example by giving each charge request a unique identifier so that repeats are recognised. Case 3 needs a circuit breaker and graceful degradation: stop calling the failing service and show the page without recommendations.

## Conclusion

A distributed system is a collection of independent computers that cooperate over a network to appear to users as one coherent system, and its engineering is dominated by problems that do not occur on a single machine: network delay, partial failure, lack of shared time, and the difficulty of keeping copies of data consistent. Designing for failure and understanding the consistency trade-off are the essential skills.

Architectural decisions only help if they are communicated. The next topic describes how architecture is documented.
