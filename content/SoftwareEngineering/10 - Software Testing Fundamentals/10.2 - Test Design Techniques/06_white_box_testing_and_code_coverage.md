## Introduction

Test design from the specification can leave parts of the code that no test ever runs. A condition handled in an obscure branch, an error path that is never triggered, or a leftover piece of dead code can hide defects precisely because nothing exercises it. White-box testing uses knowledge of the code's structure to find such gaps, and code coverage measures how much of the code the tests execute. These tools are valuable, but they are often misunderstood: coverage shows what was **not** tested far more reliably than it shows what was tested well.

**Definition:** White-box testing designs and evaluates tests using knowledge of the internal structure of the software, and code coverage is a measure of the proportion of that structure, such as statements, branches, or conditions, that the tests have executed.

<!--
IMAGE PROMPT  ->  generate as images/06_intro_white_box_testing_and_code_coverage.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A flowchart of a function with decision diamonds and statement boxes, some coloured green as covered and one red branch uncovered, with a coverage percentage gauge beside it.

ON-IMAGE TEXT: show a short bold title "White-Box Testing and Code Coverage" plus only these few labels, large and legible: Paths, Branches, Gaps. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Idea

Black-box testing asks: does the software do what the specification says? White-box testing asks: **has every part of the code been exercised?** The two are complementary. Black-box tests may miss code paths that the specification never mentions, while white-box tests alone cannot reveal missing functionality, since code that was never written cannot be covered.

## Types of Coverage

Code can be viewed as statements connected by decisions, and several measures count different things.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Measure</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it counts</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Question it answers</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Statement (line) coverage</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The proportion of executable statements that ran</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Did every line run at least once?</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Branch (decision) coverage</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The proportion of decision outcomes, true and false for each decision, that ran</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Was every decision taken both ways?</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Condition coverage</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Each individual condition within a decision evaluated as both true and false</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Was every part of a compound test seen both true and false?</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Condition/decision and multiple condition coverage</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Combinations of the above, up to all combinations of conditions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How thoroughly were compound decisions exercised?</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Modified condition/decision coverage (MC/DC)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Each condition shown to independently affect the outcome of its decision</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Does every condition matter, as demonstrated by a test? Required for the most critical aviation software</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Path coverage</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The proportion of distinct paths through the code that ran</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Was every route followed? Usually impractical because the number of paths explodes</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Function (method) coverage</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The proportion of functions called</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Was every function entered?</td>
    </tr>
  </tbody>
</table>

The measures form a rough ladder of strength: statement coverage is the weakest of the common ones, and branch coverage is stronger.

## An Example in Words

Imagine a function that calculates a price with two steps. If the quantity is ten or more, it applies a bulk discount. If the customer is a member, it subtracts a fixed amount. There are two decisions, each with a true and a false outcome.

- A single test with a large quantity and a member customer **executes every statement**: both the bulk discount and the member reduction run. Statement coverage is 100 percent.
- But neither decision has ever been taken in the **false** direction. A defect that appears when the quantity is small or the customer is not a member would not be noticed. Branch coverage is only 50 percent.
- To achieve **full branch coverage** at least one more test is needed with a small quantity and a non-member. Four combinations of the two decisions would give full path coverage here.

This shows why statement coverage alone can be misleadingly comforting.

## Cyclomatic Complexity and Paths

Thomas McCabe's **cyclomatic complexity** (Unit 8) counts the independent paths through a function and equals, for simple code, the number of decisions plus one. It indicates the **minimum number of tests** needed to cover every independent path (basis path testing), and also how hard a function is to understand. Complex functions need many tests, which is a reason to keep them small.

## Loops

Loops deserve special attention. Typical cases are: the loop body never runs (zero iterations), runs once, runs a typical number of times, and runs the maximum allowed. Defects commonly appear at zero and at the limit.

## Using Coverage Tools

Coverage tools instrument the code, run the tests, and produce a report showing which lines and branches ran. Their best use is **to find untested code**:

- Examine the **uncovered** parts. Are they important logic, error handling, or dead code? Each uncovered important branch suggests a missing test.
- Use coverage **reports on new changes**, to check that the code just written is tested.
- Track the **trend** over time, and watch for falls.

## What Coverage Cannot Tell You

Coverage is easy to misuse.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Misconception</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Reality</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">100 percent coverage means the software is correct</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Coverage shows that code **ran**, not that the result was **checked**. A test with no assertions can achieve full coverage and verify nothing</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Higher coverage always means better testing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Beyond a point, the extra tests are low value; chasing the number can produce trivial, brittle tests</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A coverage target guarantees quality</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">When a measure becomes a target, it ceases to be a good measure. Teams reward the number and game it</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Covered code is tested for all inputs</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A line can run with one input and still fail with another</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Coverage shows missing requirements</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Missing functionality has no code to cover</td>
    </tr>
  </tbody>
</table>

Many teams adopt a **minimum threshold**, often around 70 to 90 percent, as a guard against neglect, but they treat it as a floor and not as a goal. The meaningful question is whether the **important behaviour** is tested, not what the percentage is.

## Mutation Testing

A stronger way to judge test quality is **mutation testing**. A tool makes small deliberate changes to the code, called **mutants**: changing a comparison, flipping a condition, removing a statement. It then runs the tests against each mutant. If the tests fail, the mutant is **killed**, which is good: the tests noticed the change. If the tests still pass, the mutant **survives**, showing that the tests do not check that behaviour. The **mutation score**, the percentage of mutants killed, measures the ability of the tests to detect real faults. It is more demanding and slower than coverage, so it is used selectively, but it directly measures what coverage only implies.

## When to Use White-Box Techniques

- To **find gaps** left by specification-based tests.
- For **critical code** where thoroughness is required by risk or regulation.
- For **complex logic** with many branches.
- When **reviewing** the strength of an existing test suite.

They are less useful alone for finding wrong or missing requirements, and they should not replace black-box thinking.

<!--
IMAGE PROMPT  ->  generate as images/02_statement_vs_branch_coverage.png   (16:9 explanatory diagram, place here)

A small flowchart with two decisions (Quantity at least 10, Member). A single test path through the true branches is highlighted: every statement box is green, but both false branches are red, labelled Statement 100 percent, Branch 50 percent. A second test path adds the false branches turning them green.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Interpret the Coverage

1. A test suite reports 100 percent statement coverage but contains no assertions. What does this tell you?
2. A report shows an error-handling branch with no coverage. What should you do?
3. Mutation testing finds that many mutants survive. What does that indicate?

The first tells you that the code ran, but nothing about whether it works. For the second, decide whether the branch matters; if it handles a real failure, write a test that triggers it and checks the response. Surviving mutants indicate that the tests do not detect real changes in behaviour, so they need stronger assertions or more cases.

## Conclusion

White-box testing designs and evaluates tests using knowledge of the internal structure of the software, and code coverage is a measure of the proportion of that structure, such as statements, branches, or conditions, that the tests have executed. Coverage is best used to find what has not been tested, and never as proof of quality.

Writing tests for code that depends on databases, networks, or clocks requires isolating those dependencies. The next chapter begins with the stand-ins used for that purpose: test doubles.
