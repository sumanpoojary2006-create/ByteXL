## Introduction

In a request-response system, one part calls another and waits for the answer. This is simple, but it ties the caller to the availability and speed of the callee. Another way for parts to cooperate is for one to announce that something happened and for any interested party to react in its own time. This is the idea behind event-driven architecture. It is widely used for integrating services, handling bursts of work, and building systems that react to changes in the world.

**Definition:** Event-driven architecture is a style in which components communicate by producing and consuming events, records that something has happened, usually through an intermediary such as a message broker, so that producers and consumers are decoupled in time and in knowledge of each other.

<!--
IMAGE PROMPT  ->  generate as images/08_intro_event_driven_and_message_based_architecture.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A producer box Order Service on the left placing envelopes labelled Order placed into a central broker pipe, from which arrows fan out to three consumers: Kitchen, Receipts, Analytics.

ON-IMAGE TEXT: show a short bold title "Event-Driven and Message-Based Architecture" plus only these few labels, large and legible: Event, Broker, React. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Key Concepts

- **Event:** a fact that something has happened, in the past tense, such as "order placed." An event is not an instruction.
- **Message:** a unit of data sent between components. Messages can carry events, commands (requests to do something), or queries.
- **Producer (publisher):** the component that creates the event.
- **Consumer (subscriber):** a component that reacts to events.
- **Broker (message bus or queue):** the intermediary that receives, stores, and delivers messages.
- **Topic:** a named channel to which events are published and from which many consumers can read.
- **Queue:** a channel in which each message is handled by one consumer from a group of competing workers.

## Communication Patterns

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Pattern</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">How it works</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Point-to-point queue</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A message is delivered to exactly one of several workers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pending orders are shared among kitchen workers</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Publish-subscribe</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Each event is delivered to every interested subscriber</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An "order placed" event reaches the kitchen, the receipts service, and analytics</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Request-reply over messages</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A request message and a later reply message carry the interaction</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A service asks for a price quote and awaits the answer message</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Event streaming</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Events are kept in an ordered log that consumers can read and re-read at their own pace</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Analysing a stream of order events</td>
    </tr>
  </tbody>
</table>

## Benefits

- **Loose coupling:** the producer need not know who consumes its events, and new consumers can be added without changing the producer.
- **Resilience:** if a consumer is down, events wait in the broker and are processed when it returns.
- **Smoothing of load:** a queue absorbs bursts, letting consumers work at a steady rate instead of being overwhelmed.
- **Scalability:** more consumers can be added to share a queue.
- **Responsiveness:** a user request can be accepted quickly while slow work is done later in the background.
- **Extensibility:** new behaviours are added by subscribing to existing events.
- **Auditability:** a log of events provides a record of what happened.

## Challenges

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Challenge</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Explanation</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Common response</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Eventual consistency</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Different parts see changes at different times</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Design the interface and rules to tolerate short delays</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Harder to follow</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Control flow is implicit; no single place shows the whole process</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Document events, use tracing and correlation identifiers</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Duplicate delivery</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Many brokers guarantee delivery at least once, so a message may arrive twice</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Make consumers idempotent: processing a message again has no further effect</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ordering</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Events may arrive out of order, especially across partitions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Carry sequence information; design for order where it matters</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Failure handling</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A message that repeatedly fails must not block others</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Retry with limits, and move failures to a dead-letter queue for inspection</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Event design and evolution</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Event structures become contracts used by many consumers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Version events carefully and keep them backward compatible</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Broker as critical component</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">It becomes a point of failure and a thing to operate</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Run it with replication and monitoring</td>
    </tr>
  </tbody>
</table>

## Event Notification, Event-Carried State, and Event Sourcing

Martin Fowler distinguishes several meanings of event-driven design.

1. **Event notification:** the event only announces that something happened; consumers ask for details if needed. Coupling is low, but follow-up requests are required.
2. **Event-carried state transfer:** the event contains the data consumers need, so they do not need to call back, at the cost of copying data.
3. **Event sourcing:** the state of an entity is stored as the **sequence of events** that produced it, and the current state is derived from them. It gives a full history, at the cost of complexity.

A related idea is **CQRS** (command query responsibility segregation), in which the model used for changing data is separated from the model used for reading it, often combined with events to update read models.

## Orchestration and Choreography

When a business process spans several services, two ways of coordinating it exist.

- **Choreography:** each service reacts to events and emits its own, with no central controller. It is highly decoupled but the overall process is hard to see.
- **Orchestration:** a central coordinator tells each service what to do and tracks progress. It makes the process explicit but concentrates control.

Teams choose according to the complexity of the process and the need for visibility.

<!--
IMAGE PROMPT  ->  generate as images/02_pub_sub_and_queue_patterns.png   (16:9 explanatory diagram, place here)

Two panels. Left, Publish-subscribe: one Order placed event fanning out to Kitchen, Receipts, and Analytics. Right, Work queue: a queue of orders shared by three competing Kitchen workers. A small dead-letter queue icon sits beneath the queue for failed messages.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Queue or Topic?

1. An order must be prepared by exactly one available kitchen worker.
2. The same "order placed" event must reach the kitchen, the receipts service, and the analytics service.
3. A consumer receives the same payment confirmation twice. What property must it have?

Case 1 uses a queue with competing workers. Case 2 uses publish-subscribe, with a topic and several subscribers. In case 3 the consumer must be idempotent, so that handling the duplicate message does not charge or record twice.

## Conclusion

Event-driven architecture is a style in which components communicate by producing and consuming events, records that something has happened, usually through an intermediary such as a message broker, so that producers and consumers are decoupled in time and in knowledge of each other. It brings flexibility and resilience, in exchange for eventual consistency and harder-to-follow flow.

Events and messages are not the only way to connect parts in a flow of data. The next topic describes an older and very different style: pipes and filters.
