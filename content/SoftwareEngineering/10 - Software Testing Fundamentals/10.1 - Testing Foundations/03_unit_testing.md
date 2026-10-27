## Introduction

Unit tests are the foundation of a healthy test suite. They check small pieces of code in isolation, run in a fraction of a second, and tell the developer within moments whether a change broke something. A project with thousands of good unit tests can be changed with confidence, while one without them is changed with fear. But writing unit tests is a skill: poor ones are slow, fragile, and misleading, and become a burden. This topic explains what a unit test is and what makes one good.

**Definition:** A unit test is an automated test that checks the behaviour of a small, isolated piece of code, such as a function or class, by arranging a known situation, performing an action, and asserting that the outcome matches what is expected, quickly and repeatably.

<!--
IMAGE PROMPT  ->  generate as images/03_intro_unit_testing.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A small unit block under a bright light with three labelled steps Arrange, Act, Assert along a track, a green tick at the end, and a stopwatch showing milliseconds.

ON-IMAGE TEXT: show a short bold title "Unit Testing" plus only these few labels, large and legible: Arrange, Act, Assert. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## What Is a Unit?

A **unit** is the smallest piece of code that can sensibly be tested alone: typically a function, a method, or a small class. What counts depends on the language and the design. Martin Fowler distinguishes two styles.

- **Solitary unit tests** isolate the unit from all its collaborators, replacing them with simple stand-ins.
- **Sociable unit tests** let the unit use its real collaborators if they are fast and simple, testing a small cluster of closely related objects as a unit.

Both are legitimate, and teams choose according to their design and preferences.

## Structure of a Unit Test: Arrange, Act, Assert

A clear unit test has three parts.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Part</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example for a discount rule</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Arrange (given)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Set up the situation: create the objects and data needed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An order containing ten items</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Act (when)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Perform the single action being tested</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ask the order for its total</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Assert (then)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Check the result against the expected outcome</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The total equals the sum of the item prices less the ten percent discount</td>
    </tr>
  </tbody>
</table>

The same shape appears in the Given-When-Then form used in behaviour-driven development. A test should have **one reason to fail**: it checks one behaviour, though that may need several assertions about its result.

## Qualities of Good Unit Tests: F.I.R.S.T.

Robert C. Martin's acronym summarises them.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Letter</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Quality</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">F</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fast</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Run in milliseconds, so that thousands can be run often; slow tests are skipped</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">I</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Independent (isolated)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Each test runs alone, in any order, and does not rely on another test having run</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">R</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Repeatable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Same result every time, in any environment; no dependence on time, randomness, or the network unless controlled</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">S</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Self-validating</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pass or fail automatically; no human reading of output</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">T</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Timely</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Written at about the same time as the code, ideally just before it</td>
    </tr>
  </tbody>
</table>

Additional qualities widely valued:

- **Readable:** the test documents the behaviour, with a name that says what is being checked and under what condition, such as "applies ten percent discount to orders of ten or more items."
- **Focused on behaviour, not implementation:** it checks **what** the code does, not **how**, so internal refactoring does not break it.
- **Deterministic:** no hidden dependencies on the date, order of execution, or leftover data.
- **Simple:** without logic, loops, or conditions of their own, since tests that need testing defeat their purpose.
- **Maintainable:** changes to the code require few changes to tests.
- **Failing for the right reason:** when it fails, the message makes the problem clear.

## Test Frameworks

Frameworks provide the machinery: finding tests, running them, comparing results, and reporting. The family originated with Kent Beck's SUnit for Smalltalk in the 1990s, and the JUnit framework, written by Beck and Erich Gamma, spread the approach across languages, so that frameworks in many languages share the name "xUnit" and a similar structure. Modern examples include pytest for Python, JUnit and TestNG for Java, and Jest for JavaScript. Typical features are:

- **assertions** that compare actual and expected results with clear failure messages
- **fixtures:** set-up and tear-down steps to create and clean up a known state
- **parameterised tests,** which run one test with many sets of inputs and expected results
- **test discovery,** grouping, and filtering
- **reports** and integration with build pipelines

## What to Test

- **Business rules and logic:** calculations, decisions, validations.
- **Boundaries and edge cases:** empty inputs, limits, unusual combinations, as the next topics explain.
- **Error handling:** that failures are reported correctly.
- **Behaviour that has caused bugs before:** each fixed defect deserves a test that would have caught it.

**What not to test:** trivial code with no logic, such as simple getters; the internals of third-party libraries; or private details better tested through the public behaviour that depends on them. Testing everything produces large suites that are costly to maintain without adding confidence.

## Organising Tests

- Put tests **near the code** they check, in a parallel structure, and follow a consistent naming convention.
- **Group** tests by behaviour or unit.
- Keep **shared set-up** small and visible, since heavy hidden set-up makes tests hard to understand.
- Use **builders or helper functions** to create test data, so the important details stand out.

## Common Unit Test Problems

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Problem</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Symptom</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Remedy</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tests tied to implementation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Refactoring breaks many tests although behaviour is unchanged</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Test through public behaviour, not internals</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Slow tests</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The suite takes minutes; developers avoid running it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Isolate from databases and networks; remove sleeps</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Order dependence</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tests pass alone but fail together</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Make each test set up and clean up its own state</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hidden dependencies on time or randomness</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tests fail at certain times or occasionally</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Control the clock and random sources through injection</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Too many assertions on unrelated things</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A failure does not say what is wrong</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Split into focused tests</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tests with logic</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The test itself has bugs</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keep tests simple and explicit</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Copy-and-paste tests</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Duplication makes changes costly</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use parameterised tests and helpers</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unclear names</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Failure messages do not explain</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Name tests for the behaviour and condition</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Testing the framework or mocks</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tests prove nothing about real behaviour</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Test real logic with meaningful assertions</td>
    </tr>
  </tbody>
</table>

## Unit Tests as Documentation and Design Feedback

A well-named test suite is **executable documentation**: it shows how the code is meant to be used and what it promises. Code that is difficult to unit test, because it needs many collaborators, hidden global state, or huge set-up, is giving feedback about its **design**: it probably has too many responsibilities or too much coupling, the design principles of Unit 5. Writing tests is therefore one of the best ways to find design weaknesses early.

<!--
IMAGE PROMPT  ->  generate as images/02_good_unit_test_qualities.png   (16:9 explanatory diagram, place here)

Left: an Arrange, Act, Assert flow around a pricing example with an orders-of-ten scenario. Right: five badges F.I.R.S.T. (Fast, Independent, Repeatable, Self-validating, Timely) and a red warning card listing Slow, Order-dependent, Tied to implementation.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Evaluate the Tests

1. A test only passes if another test ran before it.
2. A test fails every Monday because it depends on the current date.
3. A test is named test1 and checks eight unrelated things.

Test 1 is not independent; each test must create its own state. Test 2 is not repeatable; the date should be supplied by an injected clock. Test 3 has an unclear name and no focus; it should be split into separate tests with names stating the behaviour and condition.

## Conclusion

A unit test is an automated test that checks the behaviour of a small, isolated piece of code, such as a function or class, by arranging a known situation, performing an action, and asserting that the outcome matches what is expected, quickly and repeatably. Fast, independent, readable tests that check behaviour make a codebase safe to change.

Knowing how to write a test is only half of the skill. The other half is choosing which cases to test. The next chapter describes systematic techniques for designing test cases.
