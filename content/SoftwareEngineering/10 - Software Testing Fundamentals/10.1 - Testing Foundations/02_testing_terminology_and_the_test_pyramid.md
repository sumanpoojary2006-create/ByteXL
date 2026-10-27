## Introduction

Testing conversations often go wrong because people use the same words for different things. One person's "integration test" is another's "system test," and "bug," "defect," "error," and "failure" are used interchangeably though they mean different things. Agreed terms make planning, reporting, and diagnosis clearer. Once the vocabulary is in place, a simple picture, the test pyramid, helps decide how many tests of each kind a project needs.

**Definition:** Testing terminology is the shared vocabulary of terms such as error, defect, failure, test case, oracle, and test level that lets a team describe testing precisely, and the test pyramid is a model that recommends many fast, small tests at the base, fewer broader tests above, and very few end-to-end tests at the top.

<!--
IMAGE PROMPT  ->  generate as images/02_intro_testing_terminology_and_the_test_pyramid.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A triangle divided into three layers: a wide base labelled Unit tests (many, fast, cheap), a middle layer labelled Service and integration tests, and a narrow top labelled End-to-end and UI tests (few, slow, costly), with arrows showing speed and cost.

ON-IMAGE TEXT: show a short bold title "Testing Terminology and the Test Pyramid" plus only these few labels, large and legible: Many, Some, Few. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Error, Defect, and Failure

Three words describe three stages in a chain.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Term</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Error (mistake)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A human action that produces something incorrect</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A developer misreads the rule for the bulk discount threshold</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Defect (fault, bug)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A flaw in a work product, such as code or a requirement, caused by an error</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The code applies the bulk discount at nine items instead of ten</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Failure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The visible deviation of the system from what is expected, when the defect is triggered</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A customer ordering nine items is given a discount they should not receive</td>
    </tr>
  </tbody>
</table>

Not every defect causes a failure: a flaw in code that is never executed, or that is executed with inputs that do not trigger it, may remain hidden. Testing aims to trigger failures so that defects can be found.

## Core Vocabulary

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Term</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Test case</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A set of inputs, preconditions, and expected results, designed to check one behaviour or condition</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Test suite</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A collection of test cases that are run together</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Test oracle</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The source of truth that tells you whether the result is correct: a specification, a calculation, a previous version, a human expert</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Test data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The inputs and stored data used in tests</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Test environment</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The hardware, software, and configuration in which tests run</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Test plan</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A document describing scope, approach, resources, schedule, and risks of testing</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Test script</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Instructions for running a test, manual or automated</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Test fixture</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The fixed starting state or setup needed to run a test</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Test run and test report</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The execution of tests and the record of results</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Smoke test</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A quick set of basic checks to see whether the build is stable enough for further testing</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Regression test</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A test run again to confirm that a change has not broken something that worked</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Defect (bug) report</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A record of a failure and the information needed to investigate it</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Coverage</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A measure of how much of something, such as code or requirements, the tests exercise</td>
    </tr>
  </tbody>
</table>

The **oracle problem** deserves emphasis: a test is only as good as the ability to say what the correct result is. For some software, such as complex simulations, this is difficult, and teams use approximations, comparisons with other implementations, or properties that results must satisfy.

## Test Levels

Tests are grouped by the scale of what they exercise, corresponding to the levels of the V-model in Unit 2.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Level</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Scope</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical performer</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unit (component) testing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A single function, class, or small module in isolation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Developers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The pricing rule gives the right discount for ten items</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Integration testing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Interaction between modules or services</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Developers and testers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The order service stores an order through the data layer correctly</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">System testing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The complete system against its requirements</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Testers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A full ordering journey works with real components</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Acceptance testing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Whether the system meets the needs of users and the business</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Users, customers, product owners</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The mess manager confirms the weekly report is usable</td>
    </tr>
  </tbody>
</table>

## Test Types

Independently of level, tests can be classified by what they examine.

- **Functional testing** checks what the system does.
- **Non-functional testing** checks how well, such as speed, security, and usability.
- **Structural (white-box) testing** is based on the internal structure of the code.
- **Change-related testing** checks changes: retesting a fix, and regression testing for side effects.

## Black-Box, White-Box, and Grey-Box

- **Black-box testing** designs tests from the specification, with no knowledge of the internal code. It asks only what output a given input should produce.
- **White-box (glass-box) testing** designs tests from the internal structure, aiming to exercise particular statements, branches, or paths.
- **Grey-box testing** uses partial knowledge of internals, for example the data model, to design better tests.

Both approaches are valuable and find different defects.

## Static and Dynamic Testing

- **Static testing** examines work products without running them: reviews of requirements, designs, and code, and automated static analysis. It finds defects early.
- **Dynamic testing** runs the software and observes its behaviour.

## Manual and Automated

Tests can be run by a person following steps or by a program. Automation excels at repeated, precise checks. Manual testing excels at exploring, judging usability, and noticing the unexpected. Mature teams use both, as a later topic describes.

## The Test Pyramid

Mike Cohn described the **test pyramid** in his 2009 book on agile development, as a guide to how many tests of each level to have.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Layer</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Number</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Speed</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Cost to write and maintain</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Reliability</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it catches</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unit tests (base)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Many, thousands</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Milliseconds each</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Low</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">High</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Logic errors in small parts</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Service or integration tests (middle)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fewer</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Seconds</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Moderate</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Moderate</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Problems at boundaries between parts</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">End-to-end or user interface tests (top)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Few</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Seconds to minutes each</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">High</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lower: prone to failures from timing and environment</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Whole-journey problems</td>
    </tr>
  </tbody>
</table>

The shape reflects economics. Tests lower in the pyramid are fast, precise, and cheap, so a failure points straight at the problem. Tests higher up are slower, more brittle, and harder to diagnose, but they check that the whole fits together. A healthy suite has **a broad base and a narrow top.**

### The Ice-Cream Cone

The opposite shape, with most effort in manual and user interface tests and few unit tests, is called the **ice-cream cone** anti-pattern. It leads to slow feedback, expensive maintenance, flaky results, and defects found late. Teams that start with it should move tests downward, replacing slow broad tests with fast precise ones wherever they can.

### Variations

Some writers argue for different shapes. The **testing trophy**, proposed by Kent C. Dodds, emphasises integration tests in the middle, while the **honeycomb** model used for service-based systems stresses tests of interactions between services. The principle behind them all is the same: choose the cheapest test that gives the needed confidence, and keep slow, broad tests to a minimum.

<!--
IMAGE PROMPT  ->  generate as images/02_pyramid_vs_ice_cream_cone.png   (16:9 explanatory diagram, place here)

Left: a green pyramid with a broad Unit tests base, Integration layer, narrow End-to-end tip, labelled Healthy. Right: an inverted orange ice-cream cone shape with a large Manual and UI layer on top, small Unit tests at the bottom, labelled Slow feedback and flaky.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Use the Vocabulary

1. A developer misunderstands a requirement and writes the wrong condition into a function. Name the error, the defect, and a possible failure.
2. A team has two thousand end-to-end tests and almost no unit tests, and its test runs take six hours. What shape is this, and what is the remedy?
3. A tester designs tests by reading the specification without looking at the code. What kind of testing is this?

In case 1, the misunderstanding is the error, the wrong condition is the defect, and a user receiving a wrong price is the failure. In case 2, the shape is an ice-cream cone; the remedy is to add many fast unit tests and replace broad tests with lower-level ones. Case 3 is black-box testing.

## Conclusion

Testing terminology is the shared vocabulary of terms such as error, defect, failure, test case, oracle, and test level that lets a team describe testing precisely, and the test pyramid is a model that recommends many fast, small tests at the base, fewer broader tests above, and very few end-to-end tests at the top. A shared language and a sensible balance of test types make a suite fast, reliable, and useful.

The base of the pyramid is made of unit tests. The next topic describes how to write them well.
