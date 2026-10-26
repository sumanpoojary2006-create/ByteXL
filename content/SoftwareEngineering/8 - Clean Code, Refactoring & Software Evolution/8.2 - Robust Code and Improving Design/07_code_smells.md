## Introduction

Experienced developers often sense that something is wrong with code before they can say what. A function feels too long, a class seems to know too much, the same change must be made in several places. Kent Beck described these hunches as **smells**: surface signs that suggest a deeper problem. A smell does not prove a defect, since the code may work perfectly, but it indicates that the code will be harder to understand or change than it should be. Naming the common smells gives teams a shared vocabulary for discussing and repairing them.

Unit 7 introduced smells that signal problems of object-oriented design. This topic concentrates on smells at the level of code, organised into the families used in the refactoring literature.

**Definition:** A code smell is a recognisable pattern in code that is not itself an error but suggests a weakness in design or structure, signalling that the code may be hard to understand, change, or extend, and is a prompt to investigate and, if justified, to refactor.

<!--
IMAGE PROMPT  ->  generate as images/07_intro_code_smells.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A cartoon nose icon hovering over a block of code shaped like a messy room, with five labelled bins around it: Bloaters, Abusers, Change preventers, Dispensables, Couplers.

ON-IMAGE TEXT: show a short bold title "Code Smells" plus only these few labels, large and legible: Sniff, Name, Repair. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Families of Smells

Martin Fowler's catalogue in *Refactoring*, and later groupings by others, divide smells into families by the kind of trouble they cause.

### Bloaters: Things That Have Grown Too Large

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Smell</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Sign</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Why it is a problem</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical repair</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Long method</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A function too long to grasp</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Does many things; hard to test and name</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Extract smaller functions</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Large class</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A class with many responsibilities, fields, and operations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Changes for many reasons; hard to understand</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Extract classes by responsibility</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Primitive obsession</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Plain numbers and strings used for concepts such as money, dates, or codes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rules are scattered and unenforced</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Introduce small classes for the concepts</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Long parameter list</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Many inputs to a function</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hard to call correctly; suggests missing concept</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Group inputs into an object</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data clumps</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The same group of values appears together in many places</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A concept is missing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Give the group a class</td>
    </tr>
  </tbody>
</table>

### Object-Orientation Abusers

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Smell</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Sign</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical repair</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Repeated conditionals on type</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The same choice by kind is made in several places</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Replace with polymorphism, Strategy, or State</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Temporary field</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A field used only in some circumstances</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Move into a separate object</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Refused bequest</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A subclass ignores what it inherits</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Replace inheritance with composition</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Alternative classes with different interfaces</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Two classes do the same job with different names</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unify the interface</td>
    </tr>
  </tbody>
</table>

### Change Preventers

These smells make change expensive.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Smell</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Sign</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical repair</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Divergent change</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One class changes for many unrelated reasons</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Split it by reason for change</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Shotgun surgery</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One change requires many small edits in many classes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Gather the scattered behaviour in one place</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Parallel inheritance hierarchies</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Adding a subclass in one hierarchy forces adding one in another</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Merge or restructure the hierarchies</td>
    </tr>
  </tbody>
</table>

### Dispensables: Things That Add Nothing

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Smell</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Sign</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical repair</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Duplicate code</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The same logic in several places</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Extract and share</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dead code</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Code that is never used</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Delete it</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lazy class</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A class that does too little to justify existing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Merge into another</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data class</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A class holding only data, with no behaviour</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Move related behaviour into it</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Speculative generality</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hooks and abstractions for needs that never arrived</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Remove them</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Needless comments</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Comments that restate code or excuse bad code</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Improve the code; delete the comment</td>
    </tr>
  </tbody>
</table>

### Couplers: Excessive Dependence

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Smell</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Sign</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical repair</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Feature envy</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A method uses another class data far more than its own</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Move the method to that class</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Inappropriate intimacy</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Two classes know each other internal details</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Separate, or merge</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Message chains</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Code navigates through a long chain of objects</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hide the chain behind a method</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Middle man</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A class that only forwards requests to another</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Remove it and talk directly</td>
    </tr>
  </tbody>
</table>

## Smells Are Hints, Not Verdicts

A smell directs attention, and judgement must decide whether to act.

- **Context matters.** A long function that is a plain list of steps may be fine, while a short one that is tangled is not.
- **Cost matters.** A smell in code that never changes costs little. The same smell in an area of frequent change deserves attention first.
- **Fixing has risk.** Changes need tests. Without them, improvement may introduce defects.
- **Avoid dogma.** Removing every smell, or applying a repair mechanically, can make code worse.

## Finding Smells

- **Reading code,** especially when preparing to change it.
- **Code review,** where a fresh pair of eyes notices what the author no longer sees.
- **Static analysis tools,** which measure length, complexity, duplication, and coupling and flag outliers.
- **Change history,** which shows which files change most often and which change together, pointing to the smells that cost the most.
- **Pain:** if a task feels harder than it should, there is probably a smell responsible.

## From Smell to Action

1. Notice the smell and name it.
2. Ask what problem it is causing, or will cause.
3. Decide whether it is worth fixing now, considering how often the code changes and the risk.
4. Ensure there are tests, then apply a suitable **refactoring**, which the next topics describe.
5. Check that behaviour is unchanged.

<!--
IMAGE PROMPT  ->  generate as images/02_five_smell_families.png   (16:9 explanatory diagram, place here)

Five labelled panels: Bloaters (an overstuffed suitcase), Object-orientation abusers (a misused tool), Change preventers (a chain of dominoes needing many pushes), Dispensables (items in a skip bin), Couplers (two objects tangled by cables). Each lists two example smells.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Name the Smell and Its Family

1. Adding a new payment type requires editing code in nine different classes.
2. A function takes eleven inputs.
3. A method spends most of its time reading values from another object.
4. A class has not been used by any other code for a year.

Case 1 is shotgun surgery, a change preventer. Case 2 is a long parameter list, a bloater. Case 3 is feature envy, a coupler. Case 4 is dead code, a dispensable.

## Conclusion

A code smell is a recognisable pattern in code that is not itself an error but suggests a weakness in design or structure, signalling that the code may be hard to understand, change, or extend, and is a prompt to investigate and, if justified, to refactor. Knowing the families of smells helps a team see problems early.

Once a smell is found, the response is a disciplined change to the structure of the code. The next topic introduces the practice of refactoring.
