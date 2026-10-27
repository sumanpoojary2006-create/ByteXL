## Introduction

Experienced designers recognise situations they have met before: the same kind of problem, the same set of forces, and a solution that has worked many times. Instead of inventing a new answer each time, they reuse a known one, adapting it to the case at hand. When such solutions are given names and described carefully, they become design patterns, and they let a team discuss design at a higher level than individual lines of code.

**Definition:** A design pattern is a named, general, reusable solution to a commonly occurring problem in software design, described by its intent, its structure, and its consequences, which a designer adapts to a particular context instead of copying directly.

<!--
IMAGE PROMPT  ->  generate as images/03_intro_why_design_patterns.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A shelf of labelled blueprint cards, each with a small diagram: a gear, a plug adapter, a wrapper, a tree, a broadcast antenna. A designer picks one card and fits it to a project sketch.

ON-IMAGE TEXT: show a short bold title "Why Design Patterns" plus only these few labels, large and legible: Problem, Solution, Name. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Origins

The idea came from architecture. Christopher Alexander, in *A Pattern Language* (1977), described recurring solutions to problems in buildings and towns, such as the way a window seat serves both light and conversation. In the late 1980s Kent Beck and Ward Cunningham applied the idea to software. In 1994 four authors, Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides, known as the **Gang of Four**, published *Design Patterns: Elements of Reusable Object-Oriented Software*, describing 23 patterns. It became one of the most influential books in the field.

## What a Pattern Contains

A pattern is more than a code trick. A good description gives:

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Element</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Content</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Name</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A short handle that becomes shared vocabulary</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Problem</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The situation and the forces that make it difficult</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Solution</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The general arrangement of parts, their roles, and how they collaborate, not a specific piece of code</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Consequences</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The benefits, costs, and trade-offs of using it</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Related patterns</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Alternatives and patterns often used together</td>
    </tr>
  </tbody>
</table>

The key phrase is **general solution to a problem in context**. A pattern is a template that must be fitted to the situation, and it records not only what to do but when it is appropriate and what it costs.

## The Classic Catalogue

The 23 patterns of the Gang of Four are grouped by purpose.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Category</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Patterns</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Creational</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Deal with how objects are created, making the system independent of how its objects are made</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Abstract Factory, Builder, Factory Method, Prototype, Singleton</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Structural</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Deal with how classes and objects are combined into larger structures</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Behavioural</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Deal with how objects interact and distribute responsibility</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Chain of Responsibility, Command, Interpreter, Iterator, Mediator, Memento, Observer, State, Strategy, Template Method, Visitor</td>
    </tr>
  </tbody>
</table>

This unit studies the ones most useful to a beginner. Other families of patterns exist, including architectural patterns such as those in Unit 6, enterprise application patterns described by Martin Fowler, and patterns for concurrent systems.

## Why Patterns Help

- **Reuse of experience.** Solutions that survived many projects carry knowledge about pitfalls.
- **Shared vocabulary.** Saying "use a strategy here" conveys a whole design in a few words, which speeds communication and review.
- **Better designs.** Many patterns embody the principles of the previous unit: low coupling, high cohesion, and depending on interfaces.
- **Easier learning.** Studying patterns is a quick route to understanding how skilled designers think.
- **Support for change.** Many patterns show how to isolate the part of a design that is likely to vary.

## Dangers

Patterns are often misused, and the misuse is common enough to have a name: **patternitis**, the urge to apply patterns everywhere.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Problem</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Forcing a pattern</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Choosing a pattern first and then bending the problem to fit it, producing needless complexity</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Over-engineering</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Adding flexibility for variation that never occurs, contrary to YAGNI</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Copying structure without understanding</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Imitating the arrangement of classes while missing the intent and trade-offs</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Treating patterns as a checklist of skill</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Knowing names is not the same as good design</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ignoring the language</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Some patterns exist to work around limits of a language, and may be unnecessary where the language provides the feature directly. Peter Norvig observed that many of the classic patterns are invisible or simpler in more dynamic languages</td>
    </tr>
  </tbody>
</table>

The remedy is to start from the **problem**: notice a difficulty, such as a long conditional that must be edited for every new case, and then ask whether a known pattern addresses it. Simple code that solves today needs is better than a pattern applied speculatively. Often the right sequence is to write straightforward code, and then **refactor towards a pattern** when the need appears, a practice described by Joshua Kerievsky.

## How to Study a Pattern

For each pattern in the following topics, ask:

1. **What problem** does it solve, and what makes the problem hard?
2. **What are the roles** of the participants, and who talks to whom?
3. **What varies** and what stays fixed? Most patterns separate the two.
4. **What are the costs** in indirection, number of classes, and complexity?
5. **When should it not be used?**
6. **What principle does it illustrate?** For example, dependency inversion or open-closed.

<!--
IMAGE PROMPT  ->  generate as images/02_pattern_catalogue_three_families.png   (16:9 explanatory diagram, place here)

Three columns labelled Creational (how objects are made), Structural (how objects are combined), Behavioural (how objects interact), each listing its patterns from the catalogue as small cards, with the patterns covered in this unit highlighted in blue.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Problem or Pattern First?

1. A team decides to use five patterns in a new project because they want it to look professional, before looking at the requirements.
2. A developer notices a long chain of conditionals that must be edited for every new discount type and looks for a known solution.
3. Someone says "make that a strategy," and everyone in the room understands.

Case 1 is patternitis: patterns should follow problems. Case 2 is the right way: a recurring problem leads to a known solution. Case 3 shows the value of a shared vocabulary.

## Conclusion

A design pattern is a named, general, reusable solution to a commonly occurring problem in software design, described by its intent, its structure, and its consequences, which a designer adapts to a particular context instead of copying directly. Patterns capture experience and vocabulary, and they are tools to be applied to real problems, not decorations.

The next chapter presents the patterns themselves, beginning with those that concern how objects are created and how they are combined.
