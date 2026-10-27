## Introduction

Code is never finished. Requirements change, understanding improves, and each change risks leaving the structure a little worse. Left alone, the effect accumulates until the code is so tangled that every change is slow and dangerous. Refactoring is the disciplined practice that counters this decay: improving the structure of code continuously, in small safe steps, without changing what it does. It is to code what regular maintenance is to a building.

**Definition:** Refactoring is the process of changing the internal structure of software to make it easier to understand and cheaper to modify, without changing its observable behaviour, carried out as a sequence of small, safe, behaviour-preserving steps.

<!--
IMAGE PROMPT  ->  generate as images/08_intro_refactoring_fundamentals.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A building facade being renovated: the outside looks identical and the door still opens the same way, but the internal wiring and pipes are being tidied. A shield labelled Tests protects the front door.

ON-IMAGE TEXT: show a short bold title "Refactoring Fundamentals" plus only these few labels, large and legible: Same behaviour, Better structure. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Definition in Detail

Each part of the definition matters.

- **Internal structure:** names, organisation, duplication, and dependencies, which are changed.
- **Observable behaviour unchanged:** what users and other code can see stays exactly as it was. If behaviour changes, it is not refactoring but a feature change or fix.
- **Small, safe steps:** each step is tiny and is checked, so a mistake is easy to find and undo.
- **Purpose:** to make the code easier to understand and cheaper to change, not to make it prettier for its own sake.

The idea is old among programmers, and William Opdyke gave it an academic treatment in 1992. Martin Fowler's book *Refactoring*, with Kent Beck's contributions, made it a mainstream practice and catalogued the individual techniques.

## Two Hats

Kent Beck described the discipline of **wearing two hats** and never both at once.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Hat</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Activity</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Rule</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Adding function</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Writing new behaviour and the tests for it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Do not restructure existing code</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Refactoring</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Changing structure only</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Do not add behaviour; existing tests must keep passing</td>
    </tr>
  </tbody>
</table>

Switching between hats is frequent, but at any moment you wear one. Mixing them makes it impossible to tell whether a failing test is caused by the new behaviour or by the restructuring.

## The Safety Net: Tests

Refactoring depends on being able to **confirm that behaviour has not changed**. The principal means is a set of automated tests that run quickly and pass before the change begins.

- **Before refactoring,** ensure tests cover the behaviour of the area. If they do not, write tests first (for old code, the characterisation tests described in the legacy code topic).
- **After each small step,** run the tests. If they fail, undo the step and try again, in a smaller step.
- Tests that are too tightly coupled to the implementation break during refactoring, so tests should check **behaviour**, not internal structure.

Development with test-driven development follows a cycle of writing a failing test, making it pass in the simplest way, and then **refactoring** with the tests as protection: the familiar red, green, refactor rhythm.

## Small Steps

Large restructurings are done as a chain of tiny steps, each leaving the system working. After every step, tests pass and the code could be released. This is far safer than attempting a big change that leaves the system broken for hours. A refactoring in progress can be abandoned at any step without harm.

## When to Refactor

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Occasion</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Idea</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Preparatory refactoring</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Before adding a feature, restructure so the feature is easy to add. As Kent Beck put it, make the change easy, then make the easy change</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Comprehension refactoring</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">While reading code to understand it, rename and simplify so that the understanding is recorded in the code</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Litter-pickup refactoring</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fix small problems you notice on the way, leaving the code a little better than you found it, the scout rule</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rule of three</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The first time, just do it; the second time, tolerate the duplication; the third time, refactor</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Planned refactoring</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Occasionally a larger improvement needs dedicated time; keep it visible and break it into small steps</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Review-driven refactoring</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reviewers identify improvements, which are applied before merging or soon after</td>
    </tr>
  </tbody>
</table>

The best practice is **continuous**: small improvements as part of everyday work, not separate "refactoring projects" which are easily postponed.

## When Not to Refactor

- **When there are no tests** and none can be added: the risk is high; first create a safety net.
- **When the code should be rewritten,** because it is so poor or so unsuited that restructuring it costs more than replacing it.
- **When a hard deadline is imminent** and the code will not be touched again; though shortcuts should be recorded as debt.
- **When the code works, never changes, and nobody needs to read it.**
- **Never mixed with behaviour changes** in the same step.

## Tools and Process

- **Automated refactoring in editors** performs common operations, such as renaming, extracting a function, or moving a member, safely across the whole codebase, which is far safer than doing them by hand.
- **Version control** allows each step to be saved and undone. Commit refactorings **separately** from behaviour changes so that reviewers can see that each is pure restructuring.
- **Static analysis** shows smells and complexity to guide where to focus.
- **Code review** checks that refactoring is behaviour preserving and worthwhile.
- **Continuous integration** reruns all tests for every change.

## Convincing Others

Refactoring does not add visible features, which makes it hard to justify to people who see only features. Helpful arguments are that it **speeds future work**, reduces defects, makes onboarding easier, and that the alternative is progressively slower change. Doing it as part of feature work, without asking for separate time, is the usual and healthiest approach.

## Benefits

- **Improves design** continuously, preventing decay.
- **Makes code easier to understand,** and so cheaper to change.
- **Helps find bugs,** because understanding code deeply exposes errors.
- **Keeps development speed steady** instead of declining as the code ages.
- **Encourages design to emerge** as the problem becomes clearer, instead of requiring all decisions up front.

<!--
IMAGE PROMPT  ->  generate as images/02_refactoring_cycle_with_tests.png   (16:9 explanatory diagram, place here)

A loop of four steps: Tests pass (green), Make one small change, Run tests, Commit. A red branch from Run tests labelled Fail leads to Undo and try a smaller step. A side panel shows the Two hats: Add feature hat and Refactor hat, never worn together.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Is This Refactoring?

1. A developer renames a confusing variable throughout a module, and all tests still pass.
2. A developer restructures a function and, at the same time, changes the way discounts are calculated.
3. A developer wants to restructure a module that has no tests.

Change 1 is refactoring: structure changes and behaviour is the same. Change 2 mixes the two hats; the structural change and the behaviour change should be done and committed separately. In case 3, the developer should first add tests that capture existing behaviour, and then refactor in small steps.

## Conclusion

Refactoring is the process of changing the internal structure of software to make it easier to understand and cheaper to modify, without changing its observable behaviour, carried out as a sequence of small, safe, behaviour-preserving steps. It is how a codebase stays healthy while it changes.

The next topic describes the techniques that make up the working vocabulary of refactoring.
