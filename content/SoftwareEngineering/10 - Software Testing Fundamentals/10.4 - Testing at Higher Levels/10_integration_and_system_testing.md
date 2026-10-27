## Introduction

Every part of a system can pass its own tests and the whole can still fail. Two modules may disagree about the format of a date, a service may expect a field the other never sends, a database setting may differ from what the code assumes. These problems live at the boundaries between parts, and unit tests, which isolate parts on purpose, cannot find them. Integration testing checks that parts work together, and system testing checks the complete product. Because they are broader, they are slower and costlier than unit tests, and a team must use them with care.

**Definition:** Integration testing verifies that separately developed units or components work correctly together across their interfaces, and system testing verifies that the complete, integrated system meets its specified requirements in an environment like the one in which it will run.

<!--
IMAGE PROMPT  ->  generate as images/10_intro_integration_and_system_testing.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Left: two puzzle-piece modules with a mismatched connector highlighted red at the interface. Right: a complete system diagram of app, service, database, and external payment provider with an end-to-end path highlighted.

ON-IMAGE TEXT: show a short bold title "Integration and System Testing" plus only these few labels, large and legible: Interfaces, Whole system. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Where Integration Defects Come From

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Source of defect</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Mismatched interface assumptions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One module sends dates in one format; the receiver expects another</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Different understanding of units or meanings</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Amounts in the smallest currency unit versus whole units (recall the lost spacecraft of Unit 1)</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Wrong order or timing of calls</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A step assumes another has already completed</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data problems</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A field is optional on one side and required on the other; character encoding differs</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Configuration differences</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Wrong addresses, credentials, or settings between components</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Error handling across boundaries</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A failure in one part is not handled by its caller</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Resource and performance interactions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Connection pools exhausted when the parts are combined</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Changes in a dependency</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A service changes its interface without warning</td>
    </tr>
  </tbody>
</table>

## Integration Strategies

When several components must be combined, there are different orders in which to do so.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Strategy</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">How it works</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Advantages</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Disadvantages</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Big bang</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Combine all components at once and test</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Simple to plan; no scaffolding</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hard to locate faults; discovered late; risky</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Top-down</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Start with the top-level components, using stubs for those beneath, and replace stubs gradually</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Early test of main control flow and user-visible behaviour</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Needs many stubs; low-level detail tested late</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Bottom-up</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Start with the lowest-level components, using drivers (test callers) to exercise them, and build upwards</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Low-level parts tested thoroughly early</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The overall system works only at the end</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sandwich (hybrid)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Work from top and bottom towards the middle</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Balances the above</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">More complex to organise</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Incremental (continuous)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Integrate small pieces continuously, running tests at each step</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fast feedback; easy fault location</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Needs automation and discipline</td>
    </tr>
  </tbody>
</table>

Modern practice favours **continuous integration** of small changes, with automated tests running at every integration, as Unit 9 described.

## Kinds of Integration Test

- **Component (narrow) integration tests** check one component with its **real** immediate collaborator, such as a data access layer against a real database, with other parts replaced by doubles. They are focused and fast enough to run often.
- **Broad integration tests** exercise several real components together, sometimes across services.
- **Interface (API) tests** call a service interface directly, with requests and responses, checking behaviour, data formats, error codes, and security without involving a user interface. They are valuable and relatively stable.
- **Contract tests** verify that a provider and its consumers agree on the interface. In **consumer-driven contract testing**, each consumer states what it expects of the provider, and the provider's pipeline checks that it still meets all those expectations. This catches breaking changes without needing all services deployed together, and is especially useful in systems of many services.
- **Database and persistence tests** check that queries, mappings, and migrations work against a real database engine, often one started in a container for the test.
- **Messaging tests** check that messages are produced and consumed correctly.
- **Third-party integration tests** check integration with external services, usually against a provider's test environment, since calling the real service may cost money.

## Test Environments and Data

Integration tests need realistic surroundings.

- **Starting real dependencies** such as databases and queues in containers for the duration of a test gives realism without shared, fragile environments.
- **Test data** must be controlled: each test creates the data it needs and cleans up, so that tests are independent.
- **Service virtualisation** simulates external systems that are unavailable, costly, or unreliable, by replaying recorded behaviour.
- **Environment parity** with production reduces surprises, as Unit 9 argued.

## System Testing

System testing examines the **whole product**, integrated and running in an environment that resembles production, against the **requirements**. It is usually black-box and covers:

- **Functional requirements:** complete workflows from the user's viewpoint.
- **Non-functional requirements:** performance, security, reliability, usability, covered in a later topic.
- **Interfaces with external systems.**
- **Installation, configuration, and upgrade.**
- **Data migration and recovery.**

System tests are often organised around **scenarios and user journeys**, such as registering, ordering, paying, and receiving a confirmation.

### End-to-End Tests

**End-to-end (E2E) tests** drive the complete system as a user would, often through the real user interface or public interface, from the first action to the last observable outcome. They offer the highest confidence that the whole fits together, but they are:

- **slow**, because many components start up and interact
- **brittle**, since small interface or timing changes break them
- **hard to diagnose**, as a failure could be anywhere
- **costly to maintain** and prone to being flaky

For these reasons the test pyramid recommends **few** of them, focusing on the **critical journeys**, such as completing a purchase, and relying on lower levels for detail.

## Smoke and Sanity Tests

- A **smoke test** is a small, fast set of checks of the most essential functions run after each build or deployment, to confirm that the system starts and basic paths work before deeper testing begins. A failed smoke test stops the pipeline.
- A **sanity test** is a narrow check that a particular fix or change behaves sensibly.

## Balancing Levels

Mike Cohn's test pyramid, J. B. Rainsberger's argument that excessive broad integrated tests are expensive and give poor fault localisation, and Martin Fowler's distinction between narrow and broad integration tests all lead to the same guidance:

1. Test **logic** with fast unit tests.
2. Test **each boundary** with narrow integration and contract tests.
3. Test **a handful of critical journeys** end to end.
4. Do not repeat at a higher level what is already well covered below.

## Common Problems

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Problem</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Cause</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Remedy</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tests fail intermittently</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Shared environments, timing, leftover data, unreliable external services</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Isolated environments; explicit waits on conditions; reset state; stub unreliable externals</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Slow suites</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Too many broad tests</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Push tests down; run in parallel; separate fast and slow groups</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hard to find the cause of failures</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Broad tests with many parts</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Narrow tests; good logging and traces</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Broken by unrelated changes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Brittle assertions on irrelevant details</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Assert on behaviour that matters</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Environments differ from production</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hidden differences</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use containers and defined environments</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Interface changes break consumers late</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No contract checking</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Contract tests in the pipeline</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Test data conflicts</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tests share records</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unique, independent data per test</td>
    </tr>
  </tbody>
</table>

<!--
IMAGE PROMPT  ->  generate as images/02_integration_layers_and_contract_test.png   (16:9 explanatory diagram, place here)

Left: a consumer service and a provider service with a contract card between them, each side running its own check against the contract. Right: layers of tests: many unit tests, some narrow integration tests with a real database in a container, few end-to-end tests covering the order journey.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Which Test?

1. Two services must agree on the format of an order message, and one team changes it without warning.
2. A team wants to check that its queries work against a real database engine.
3. A team wants to be sure that a customer can browse, order, and pay in the complete system.

Problem 1 suits contract testing. Problem 2 suits a narrow integration test with a real database, perhaps started in a container. Problem 3 suits an end-to-end system test of the critical journey, kept few in number.

## Conclusion

Integration testing verifies that separately developed units or components work correctly together across their interfaces, and system testing verifies that the complete, integrated system meets its specified requirements in an environment like the one in which it will run. Careful balance, with narrow integration and contract tests at boundaries and few end-to-end tests, gives confidence without crippling speed.

As the system grows, the number of tests grows too, and each change risks breaking old behaviour. The next topic describes regression testing and test automation.
