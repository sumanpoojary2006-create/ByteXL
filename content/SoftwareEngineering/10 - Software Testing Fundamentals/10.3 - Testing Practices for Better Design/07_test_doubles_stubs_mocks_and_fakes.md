## Introduction

Real code rarely stands alone. An order service talks to a database, a payment provider, an email gateway, and the system clock. A test that uses the real versions is slow, may cost money, depends on networks being available, and cannot easily produce failures on demand, such as a payment timing out. Test doubles solve this by substituting simple stand-ins for the real collaborators during a test. Used well, they make tests fast, reliable, and focused. Used carelessly, they make tests that pass while the real system fails.

**Definition:** A test double is any object that stands in for a real dependency during a test, such as a stub that returns prepared answers, a mock that checks it was called as expected, or a fake that provides a simplified working implementation, so that the code under test can be exercised in isolation.

<!--
IMAGE PROMPT  ->  generate as images/07_intro_test_doubles_stubs_mocks_and_fakes.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A film-set stunt double standing in for an actor, with a code unit in the centre connected by sockets to five stand-in figures labelled Dummy, Stub, Spy, Mock, Fake, instead of a real database and payment cloud which are greyed out.

ON-IMAGE TEXT: show a short bold title "Test Doubles" plus only these few labels, large and legible: Stand-ins, Isolate, Control. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Why Replace Dependencies

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Reason</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Speed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A real database or network call takes milliseconds to seconds; thousands of tests would take hours</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reliability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A real service may be unavailable, causing failures unrelated to the code under test</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Determinism</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The real clock, random numbers, and external data change from run to run</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Control over scenarios</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">It is easy to make a stand-in time out, return an error, or return an unusual value; hard with the real thing</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cost and side effects</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A real payment provider charges money; a real email gateway sends messages</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Isolation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A failure points at the unit under test, not at a distant dependency</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unavailable dependencies</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The other component does not exist yet</td>
    </tr>
  </tbody>
</table>

This works only if the code is designed so that dependencies can be **substituted**, by receiving them from outside through dependency injection, as Unit 7 described. Code that creates its own collaborators cannot easily be tested in isolation.

## The Kinds of Test Double

The standard vocabulary comes from Gerard Meszaros in his book on xUnit test patterns, and is used by Martin Fowler.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Kind</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it does</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dummy</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fills a parameter but is never actually used</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A logger passed to a function that does not log in this scenario</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stub</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Returns prepared answers to calls made during the test; provides indirect input</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A payment service stub that always replies "approved," or one that replies "declined" to test the failure path</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Spy</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A stub that also records how it was called, for later inspection</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An email sender that remembers which messages it was asked to send</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Mock</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pre-programmed with expectations about the calls it should receive, and fails if they are not met; verifies behaviour</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A kitchen notifier that expects to be told exactly once to prepare a given order</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fake</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A working but simplified implementation, not suitable for production</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An in-memory database that stores orders in a list instead of a real database</td>
    </tr>
  </tbody>
</table>

The terms are used loosely in practice, and many tools call everything a "mock." The important distinction is the purpose: **stubs and fakes provide inputs** and behaviour so the unit can run, while **mocks and spies check outputs**, the interactions the unit has with its collaborators.

## State Verification and Behaviour Verification

- **State verification** runs the code and then checks the **resulting state** or return value: the order total is correct, the order is stored.
- **Behaviour verification** checks the **interactions**: the unit asked the payment service to charge the right amount, exactly once.

Prefer state verification where possible, since it tests **what** happened and leaves the implementation free to change. Use behaviour verification when the interaction **is** the behaviour, such as sending a message that has no other visible result.

## Two Schools

Two styles of testing have developed.

- The **classicist (Detroit or Chicago) school** uses real objects wherever practical and test doubles only for awkward dependencies such as databases and networks. Tests are less coupled to implementation.
- The **mockist (London) school** isolates every unit from all its collaborators with mocks and uses tests to drive out the design of interactions. It gives very focused tests but ties them closely to how the units talk to each other.

Neither is universally right, and many teams blend them.

## Risks and Good Practice

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Risk</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Explanation</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Remedy</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Over-mocking</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tests describe the exact implementation; any refactoring breaks them although behaviour is unchanged</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Verify outcomes; mock only at boundaries</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tests that prove nothing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Everything is mocked, so the test only checks the mocks</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keep real logic in the path under test</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">False confidence</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The double behaves differently from the real thing, so tests pass but the integration fails</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Add integration tests against the real dependency; use contract tests to keep the double faithful</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Mocking what you do not own</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Doubles of a third-party interface break when it changes in ways the double does not reflect</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Wrap the third-party library in your own adapter, and mock your adapter</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Complex set-up</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Many doubles with intricate expectations make tests unreadable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Redesign: too many collaborators signals a class with too many responsibilities</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Brittle expectations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tests check the number and order of calls that do not matter</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Check only what matters to the behaviour</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stateful fakes that drift</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A fake database that behaves unlike the real one</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Test fakes against the same contract as the real implementation</td>
    </tr>
  </tbody>
</table>

Guidelines:

1. **Use real objects when they are fast and simple.** Only replace what is slow, non-deterministic, or external.
2. **Isolate at architectural boundaries:** databases, networks, file systems, clocks, random numbers, third-party services.
3. **Prefer fakes for stateful dependencies,** such as in-memory repositories, since they behave more like the real thing than a mock programmed call by call.
4. **Keep doubles simple** and make the test explicit about what they do.
5. **Do not forget the real thing.** A suite full of doubles needs some tests that use the real database or service, at the integration level.
6. **Design for testability:** inject dependencies, program to interfaces, and keep side effects at the edges.

## Controlling Time and Randomness

Two dependencies cause most non-deterministic tests: the **clock** and **random numbers**. The remedy is to have the code ask an injected clock or random source for its values, and to replace them in tests with controlled ones that return a fixed time or a fixed sequence. Tests of expiry, schedules, and time-based discounts then run instantly and identically every time.

## Tools

Mocking frameworks in every major language generate doubles from interfaces and let tests declare what they should return and what calls to expect. They are convenient, but the concepts above matter more than the tool.

<!--
IMAGE PROMPT  ->  generate as images/02_five_kinds_of_test_double.png   (16:9 explanatory diagram, place here)

Five labelled cards in a row. Dummy (placeholder, unused), Stub (returns a canned answer), Spy (records calls), Mock (expects specific calls, red if not met), Fake (simple working in-memory version). Under them, arrows show Inputs for stub and fake, Outputs checked for spy and mock.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Choose the Double

1. A test must show how an order behaves when the payment provider says "declined."
2. A test must check that the kitchen was notified exactly once when an order is confirmed.
3. A test needs a repository that stores and retrieves orders without a real database.

Case 1 needs a stub that returns "declined." Case 2 needs a mock or spy that verifies the notification. Case 3 needs a fake, an in-memory repository. Whichever is chosen, a separate integration test should confirm the real provider and database work as the doubles assume.

## Conclusion

A test double is any object that stands in for a real dependency during a test, such as a stub that returns prepared answers, a mock that checks it was called as expected, or a fake that provides a simplified working implementation, so that the code under test can be exercised in isolation. They make tests fast and deterministic, provided they are used sparingly and supported by tests of the real integrations.

Tests are usually written after the code. The next topic describes an approach that reverses the order and uses tests to shape the design: test-driven development.
