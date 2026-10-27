## Introduction

Sooner or later every engineer inherits a system that others wrote, that is important to the business, that nobody fully understands, and that is frightening to change. This is legacy code. It is not necessarily old, and it is not necessarily bad. It is code whose behaviour must be preserved, whose design is unclear, and which lacks the safety net that would make change comfortable. Working with it is a distinct skill, and in many careers the dominant one.

**Definition:** Legacy code is existing code that is valuable and in use but difficult to change safely, typically because it is poorly understood and lacks automated tests, and working with it means making changes in small, protected steps that preserve behaviour while gradually improving the code and its tests.

<!--
IMAGE PROMPT  ->  generate as images/11_intro_working_with_legacy_code.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A large old machine with many tangled pipes and a locked control panel, with a technician adding small labelled safety sensors and a test meter to one section, and a clean new module bolted beside it.

ON-IMAGE TEXT: show a short bold title "Working with Legacy Code" plus only these few labels, large and legible: Protect, Change, Improve. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## What Makes Code "Legacy"

Michael Feathers, in *Working Effectively with Legacy Code* (2004), gave a famous and deliberately provocative definition: **legacy code is code without tests.** Without tests, you cannot tell whether a change has broken anything, so every change is a gamble. Other features often accompany it: unclear design, missing documentation, departed authors, obsolete technology, and fear.

Legacy code also carries **value**: it encodes years of business rules, edge cases, and fixes that nobody remembers. This is why it is rarely safe to throw it away.

## The Dilemma

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">The problem</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Why it is a trap</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">To change code safely, you need tests</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">But the code was not designed to be tested</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">To add tests, you must change the code to make it testable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">But changing code without tests is risky</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">To understand the code, you need documentation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">But there is none, and the authors have gone</td>
    </tr>
  </tbody>
</table>

Feathers' techniques are ways out of this circle.

## The Legacy Change Process

A reliable sequence of steps for any change:

1. **Identify the change points:** find where the change must be made.
2. **Find test points:** locate where behaviour can be observed.
3. **Break dependencies** so that the code can be placed in a test.
4. **Write tests** that pin down current behaviour.
5. **Make the change and refactor,** with the tests as protection.

## Characterisation Tests

When the existing behaviour is not documented, **characterisation tests** (also called golden master or approval tests) record what the code **actually does**, whether or not that is correct. The method is to run the code with chosen inputs, observe the outputs, and write tests asserting those outputs. They do not claim that the behaviour is right, only that it is the current behaviour, so any change in it is detected and can be judged. For large outputs, such as a long report, the whole output is saved as the reference and compared after each change.

## Seams

A **seam** is a place where behaviour can be changed without editing the code at that place. Seams let a test replace a troublesome dependency, such as a database or a network call, with a simple stand-in. Feathers describes several kinds: **object seams**, where a different object is supplied through an interface or inheritance, **link seams**, where a different library is linked in, and **preprocessing seams**, in languages that support them. Finding or creating seams is the key technique for getting legacy code under test.

## Techniques for Adding Features Safely

When tests cannot be added easily to the existing code, new code can be written to be clean and tested, and attached with minimal change.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Technique</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Idea</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">When useful</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sprout method or class</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Write the new behaviour as a separate, fully tested function or class, and call it from the old code with a one-line change</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The old code is too hard to test</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Wrap method or class</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rename the existing operation and create a new one with the old name that calls the old one plus new behaviour (or wrap the whole object)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Adding behaviour before or after an existing operation</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Extract and override</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Extract the troublesome part into a method that a test can override</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A dependency makes the code untestable</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Introduce parameter or interface</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pass the dependency in from outside so it can be replaced in tests</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hidden creation of dependencies</td>
    </tr>
  </tbody>
</table>

## Understanding Before Changing

- **Read and run it.** Observe behaviour in practice.
- **Draw sketches** of what depends on what, and mark things you learn.
- **Use scratch refactoring:** restructure the code purely to learn, without keeping the result, then discard it.
- **Use version history** to see why code looks the way it does.
- **Talk to people** who know the system, including users and those who support it.
- **Add logging** or tracing to observe real behaviour in a safe environment.

## Improve Gradually

The most successful approach is **incremental**. Do not attempt to fix everything. Each time a change is made, leave the area slightly better: add tests around the part touched, rename confusing names, remove dead code. Over time the healthy areas grow, and the hard core shrinks. Concentrate effort where changes are most frequent, since that is where improvement pays back.

## Rewrite or Improve?

The temptation is to throw it away and start again. The risks are large: rewriting takes longer than expected, the new system must reproduce all the hidden behaviours of the old, and during the rewrite the old system still needs maintenance. A famous essay by Joel Spolsky called a complete rewrite one of the worst strategic mistakes a software company can make, citing the experience of a well-known browser maker. Fred Brooks warned of the related **second-system effect**: the tendency to over-design a replacement. In many cases the sensible path is incremental replacement, as described in the topic on modernisation.

## Working Habits

- **Respect the code.** It works, and it has survived in production; there are reasons for its oddities.
- **Prefer small changes** with frequent releases, so that problems are noticed quickly.
- **Never change behaviour and structure together.**
- **Keep a record** of what you learn, in tests and documentation.
- **Treat fear as information:** areas people avoid are the ones most in need of tests.

<!--
IMAGE PROMPT  ->  generate as images/02_legacy_change_process_and_sprout.png   (16:9 explanatory diagram, place here)

Left: a five-step flow Find change points, Find test points, Break dependencies, Write characterisation tests, Change and refactor. Right: an old tangled block with a thin one-line connector to a new clean tested block labelled Sprout, plus a seam marker where a test stand-in replaces a database.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Choose the Approach

1. A team must add a new discount rule to an old, untested pricing function, and cannot easily test the function.
2. Nobody knows exactly what a legacy report produces, and the team wants to change the code behind it without altering the output.
3. A function creates a real database connection inside itself, so it cannot be tested.

Case 1 suits sprouting: write the new rule as a new tested function and call it from the old code. Case 2 suits characterisation or golden master tests: record the current output and compare it after each change. Case 3 calls for a seam: introduce a way to supply the connection from outside so a test can replace it.

## Conclusion

Legacy code is existing code that is valuable and in use but difficult to change safely, typically because it is poorly understood and lacks automated tests, and working with it means making changes in small, protected steps that preserve behaviour while gradually improving the code and its tests. Patience, safety nets, and incremental improvement are the tools.

This ends the chapter on writing and improving code. The next chapter widens the view to the life of software over years, beginning with why software must change at all.
