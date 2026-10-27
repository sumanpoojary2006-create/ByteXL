## Introduction

Software that worked yesterday can be broken by a change made today, often in a place the developer never touched. Fixing one bug introduces another, a refactoring alters behaviour unexpectedly, an upgraded library changes a detail. The risk grows with every change, and checking by hand everything that used to work becomes impossible as the product grows. Regression testing is the discipline of re-running tests to catch such breakage, and test automation is what makes it practical. Together they underpin continuous integration and frequent release.

**Definition:** Regression testing is the repeated execution of previously passed tests after a change to confirm that existing behaviour has not been damaged, and test automation is the use of software to run tests and check their results without manual effort, so that regression checks can be run quickly, often, and consistently.

<!--
IMAGE PROMPT  ->  generate as images/11_intro_regression_testing_and_test_automation.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A change arrow entering a system, with a net of automated checks catching a broken existing feature, while a robot arm repeatedly runs a stack of test cards in a pipeline loop with a green or red light.

ON-IMAGE TEXT: show a short bold title "Regression Testing and Test Automation" plus only these few labels, large and legible: Change, Re-run, Catch. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Why Regressions Occur

- **Side effects** of a change in shared code.
- **Hidden dependencies** between parts.
- **Fixes that conflict** with earlier behaviour.
- **Merges** combining changes that work alone but not together.
- **Updated dependencies, platforms, or configuration.**
- **Refactoring** that unintentionally changes behaviour.

A regression is especially damaging because users notice that something that used to work has stopped, and trust falls.

## Regression Testing

A regression test is any test run again to see that the system still behaves as before. In practice it is a **growing collection**: each bug fixed gains a test that would have caught it, each feature adds its tests, and the whole collection is run after changes.

### What to Run

Running every test after every change is ideal if it is fast, but a large suite may take hours. Strategies for choosing:

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Strategy</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Idea</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Trade-off</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Retest all</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Run the entire suite</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Most thorough; slow for large suites</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Selective (impact-based)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Run only the tests related to the changed code, using dependency analysis and the change impact analysis of Unit 8</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Faster; risks missing indirect effects</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prioritised</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Run the most important or most failure-prone tests first</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Early feedback on risky areas; the rest follows</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tiered</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fast checks on every commit, broader tests on merge, full suite nightly or before release</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Balances speed and thoroughness</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Risk-based</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Concentrate on areas of high likelihood and impact of failure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Efficient; depends on good risk judgement</td>
    </tr>
  </tbody>
</table>

Automatic **test selection** tools, and parallel execution on many machines, reduce the cost.

### Regression Tests From Bugs

A valuable rule: **every defect fixed gets a test** that fails before the fix and passes after. This prevents the same bug returning, and builds a suite from real experience. It also confirms that the fix works.

## Test Automation

### What It Gives

- **Speed:** thousands of checks in minutes.
- **Repeatability:** the same steps and checks every time, without fatigue or variation.
- **Frequency:** tests run on every change, giving fast feedback.
- **Coverage over time:** the suite accumulates.
- **Freed people:** testers can spend time on exploration and judgement, which automation cannot do.
- **Enablement of continuous delivery:** frequent releases are only safe with automated checks.

### What to Automate

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Good candidates</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Poor candidates</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tests run often, such as regression and smoke tests</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tests run once or rarely</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stable behaviour that does not change frequently</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Features still changing rapidly</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tedious, repetitive checks</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Exploratory testing, which relies on human curiosity</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tests needing many data combinations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Usability and look-and-feel judgements</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">High-risk, business-critical flows</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cases where the automation costs more than the checks save</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Performance and load tests, which cannot be done by hand</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Highly unstable or poorly specified areas</td>
    </tr>
  </tbody>
</table>

### Testing and Checking

James Bach and Michael Bolton distinguish **checking**, the confirmation of specific expected results, which machines do well, from **testing**, the exploratory, investigative, and sense-making activity that needs human judgement. Automation is a powerful way to do checks; it does not replace testing.

### Levels of Automation

Automated tests can operate at every level of the pyramid: unit, integration, interface, and user interface. The lower the level, the cheaper and more stable the automation. User interface automation is the most fragile, since it depends on screens, element names, and timing.

### User Interface Automation

Tools such as Selenium, Playwright, and Cypress drive a real browser or application as a user would. Good practice includes:

- **Page objects** (or similar abstractions): keep knowledge of the screen structure in one place, so that when the interface changes, one object is updated and not hundreds of tests.
- **Stable locators:** identify elements by meaningful, dedicated attributes, not by position or appearance.
- **Waiting for conditions** (an element appears) rather than fixed delays.
- **Independent tests** with their own data and clean state.
- **Few tests,** covering key journeys.

## Flaky Tests

A **flaky test** passes and fails on the same code without any change. Flakiness is one of the most damaging problems in automation: people stop trusting red results and ignore real failures.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Cause</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Remedy</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Timing and asynchronous behaviour</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Wait for explicit conditions; avoid fixed sleeps</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Shared or leftover state and order dependence</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Isolate each test; reset state; randomise order to find dependence</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">External services and networks</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Replace with doubles or virtualised services</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Date, time, and randomness</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Control the clock and random sources</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Environment differences and resource limits</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use consistent containers; allocate adequate resources</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Concurrency problems in the code under test</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Investigate: the flakiness may reveal a real defect</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Poorly written test</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Review and rewrite</td>
    </tr>
  </tbody>
</table>

Teams should **track flakiness**, quarantine unreliable tests quickly while they are repaired (with an owner and a deadline), and never leave a flaky test to be ignored indefinitely.

## Maintaining the Suite

Automated tests are software and need maintenance. Tests that are slow, duplicated, or brittle cost more than they save. Healthy practice:

- **Treat test code like production code:** clear names, no duplication, code review.
- **Delete or fix obsolete tests.**
- **Keep the suite fast:** parallelise, and keep slow tests in a separate stage.
- **Report clearly:** a failure should point to the problem.
- **Review regularly** for value: what does each test protect?
- **Watch the cost-benefit:** automation is an investment that pays back through repeated use.

## Automation in the Pipeline

Tests run in the continuous integration pipeline in stages, fast ones first. Results are shown on the change under review, and failures block merging. Scheduled runs of slower suites, such as full regression or performance tests, run overnight or before release.

<!--
IMAGE PROMPT  ->  generate as images/02_regression_selection_and_flaky_causes.png   (16:9 explanatory diagram, place here)

Left: a tiered pipeline: commit triggers fast tests, merge triggers broader tests, nightly runs the full regression suite. Right: a flaky test icon with six cause arrows (timing, shared state, external services, time and randomness, environment, concurrency) and a quarantine box with an owner tag.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Automate or Not?

1. A check of twenty critical business rules that must run after every change.
2. A one-off exploration of a brand-new, still-changing feature.
3. A test that fails about one run in ten with no code change. What should the team do?

Case 1 is an excellent candidate for automation. Case 2 is better done manually, as exploratory testing, since the feature is unstable and learning is the aim. For case 3, find the cause of the flakiness; if it cannot be fixed quickly, quarantine it with an owner and a deadline, so that it does not teach the team to ignore failures.

## Conclusion

Regression testing is the repeated execution of previously passed tests after a change to confirm that existing behaviour has not been damaged, and test automation is the use of software to run tests and check their results without manual effort, so that regression checks can be run quickly, often, and consistently. Automation is valuable when applied to stable, repeated, important checks, and when the suite is kept fast, reliable, and maintained.

Automated checks confirm what was expected. Some important questions cannot be answered that way. The next topic describes acceptance, exploratory, and usability testing, which rely on human judgement.
