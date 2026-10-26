## Introduction

Studying good solutions is only half of design knowledge. The other half is recognising bad ones, the structures that look attractive at first and cause trouble later. Developers noticed that bad solutions, too, recur in recognisable forms, and gave them names so they could be spotted and discussed. The study of these recurring failures complements the study of patterns: patterns show what to aim for, and anti-patterns and smells show what to avoid and how to notice trouble early.

**Definition:** An anti-pattern is a commonly occurring solution to a problem that appears reasonable but produces more harm than good, and a code smell is a surface sign in code or design that suggests a deeper problem, to be investigated and, if confirmed, repaired by refactoring.

<!--
IMAGE PROMPT  ->  generate as images/12_intro_anti_patterns_and_code_smells_in_design.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A well-organised neat desk on the left labelled Pattern, and a chaotic overflowing desk with warning signs on the right labelled Anti-pattern, with a nose icon sniffing the second labelled Smell.

ON-IMAGE TEXT: show a short bold title "Anti-Patterns and Code Smells in Design" plus only these few labels, large and legible: Spot, Name, Repair. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Anti-Patterns

The term was popularised by Andrew Koenig in 1995, and by a 1998 book on the subject. An anti-pattern has three parts: a **recurring bad solution**, an explanation of **why it fails**, and a **better way** out. The best-known ones are:

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Anti-pattern</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Description</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Why it hurts</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Remedy</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">God object (the Blob)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One class that knows and does too much, with many unrelated responsibilities and many dependents</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hard to understand, change, or test; every change risks something</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Split by responsibility; move behaviour to the objects that own the data</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Spaghetti code</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tangled control flow with no clear structure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Impossible to follow; changes break unrelated parts</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Restructure into cohesive units; refactor in small steps with tests</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Golden hammer</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Using a favourite tool or pattern for every problem</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The solution does not fit the problem</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Choose tools for the problem; learn alternatives</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lava flow</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dead or unexplained code retained because nobody dares remove it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Clutter, confusion, and risk</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Remove with the help of tests and version history</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Copy-and-paste programming</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Duplicating code instead of sharing it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Bugs are fixed in one copy and remain in the others</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Extract shared behaviour; follow DRY</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Poltergeist</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A short-lived object with no real responsibility that only passes messages between others</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Needless complexity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Remove it and let the real objects talk</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Boat anchor</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An unused part kept in case it is needed some day</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Maintenance burden for no benefit</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Delete it; version control remembers it</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cargo cult programming</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Using code or practices without understanding why</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Brittle and cargo-driven design</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Learn the reasons; remove what has no purpose</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Speculative generality</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Building hooks and abstractions for needs that never arrive</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Complexity without benefit</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Remove; follow YAGNI</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Singleton abuse</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Using global single instances for convenience</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hidden coupling, hard testing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Inject dependencies instead</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Anaemic domain model</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Objects that hold only data, with logic in separate service classes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Loses encapsulation; rules scatter</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Move behaviour into the objects</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Big ball of mud</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A system with no discernible structure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Slow, risky change and no way to reason about it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Gradual restructuring toward clear modules</td>
    </tr>
  </tbody>
</table>

## Code Smells

Kent Beck introduced the term **code smell**, and Martin Fowler's book on refactoring catalogued many. A smell is a **hint**, not a proof: it suggests looking more closely. Some common ones concerning design:

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Smell</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Sign</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Likely underlying problem</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Long method or large class</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Too big to understand at a glance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Several responsibilities mixed together</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Feature envy</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A method uses the data of another class more than its own</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Behaviour is in the wrong place</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Shotgun surgery</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One change requires many small edits across many classes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A responsibility is scattered</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Divergent change</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One class changes for many unrelated reasons</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Too many responsibilities; violates single responsibility</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data clumps</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The same group of values travels together everywhere</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A missing concept that should be an object</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Primitive obsession</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Using bare numbers and strings for concepts like money or postcodes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A missing small class that would enforce rules</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Repeated conditionals on type</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The same switch on kind appears in several places</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Polymorphism or a pattern such as Strategy or State is needed</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Refused bequest</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A subclass ignores or rejects what it inherits</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Inheritance used where it is not an is-a relationship</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Message chains</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Code navigating through many objects to reach what it needs</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Violation of the Law of Demeter; coupling to structure</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Inappropriate intimacy</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Two classes know too much about each other internals</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Excessive coupling; boundaries in the wrong place</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Duplicated code</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The same logic in several places</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Missing abstraction</td>
    </tr>
  </tbody>
</table>

## Patterns, Smells, and Refactoring

The three ideas form a working cycle.

1. **Notice a smell,** such as repeated conditionals on payment kind.
2. **Diagnose** the underlying design problem: variation by type is handled by conditionals.
3. **Choose a remedy,** possibly a pattern such as Strategy or Factory Method.
4. **Refactor in small, safe steps,** with tests protecting behaviour, until the design improves.

This is the practice of **refactoring toward patterns**: starting with simple code, and introducing a pattern only when a smell shows that it is needed. It guards against both the failure of ignoring structure and the failure of imposing it too early.

## Causes of Anti-Patterns

Bad structure usually results from understandable pressure, not carelessness: deadlines, changing requirements, lack of knowledge, absent reviews, and the accumulation of small shortcuts, which is technical debt. Naming the problem helps a team talk about it without blaming individuals, and supports a decision to repay the debt.

## Using the Names Well

Labels are useful, but they can be misused as insults or as simple verdicts. The value lies in the question they raise: what is the underlying issue, what does it cost, and what is the cheapest sensible fix? A smell present in rarely changed code may not be worth the effort of repair, whereas the same smell in a hot area of frequent change deserves attention first.

<!--
IMAGE PROMPT  ->  generate as images/02_smell_to_remedy_cycle.png   (16:9 explanatory diagram, place here)

A circular flow of four steps: Notice a smell (nose icon, repeated conditionals), Diagnose (magnifier, variation handled by if chains), Choose a remedy (pattern card Strategy), Refactor safely (test shield). A side list shows God object, Spaghetti code, Golden hammer as example anti-patterns.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Name the Smell

1. A single class handles menu management, order processing, payment, and email, and has hundreds of operations.
2. The same list of payment kinds is checked with a conditional in seven different places.
3. A method spends most of its time reading values from another class to calculate something.
4. A developer applies the same pattern to every problem, whether or not it fits.

Case 1 is a God object, or a large class. Case 2 is repeated conditionals on type, suggesting polymorphism or a Strategy. Case 3 is feature envy: the behaviour belongs in the other class. Case 4 is the golden hammer.

## Conclusion

An anti-pattern is a commonly occurring solution to a problem that appears reasonable but produces more harm than good, and a code smell is a surface sign in code or design that suggests a deeper problem, to be investigated and, if confirmed, repaired by refactoring. Knowing these failures lets a team notice trouble early and name it clearly.

This completes Unit 7. You can now explain the object-oriented ideas behind good design, why composition is usually preferable to inheritance, what design patterns are and when they help, apply the main creational, structural, and behavioural patterns, use dependency injection to decouple components, and recognise the anti-patterns and smells that signal a design in trouble. Unit 8 turns from the structure of design to the craft of writing and improving code: clean code, refactoring, and software evolution.
