## Introduction

Refactoring is carried out through a set of named, well-understood transformations. Each one has a clear purpose, a mechanical procedure of small steps, and a known effect on the code. Learning the common ones gives a developer a toolkit: when a smell appears, there is a standard remedy. Most modern editors can carry out many of them automatically, but understanding what they do and when to use them is the skill.

**Definition:** A refactoring is a named, behaviour-preserving transformation of code, such as extracting a function, renaming, or moving behaviour, applied in small steps to remove a specific weakness in structure.

<!--
IMAGE PROMPT  ->  generate as images/09_intro_common_refactorings.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A toolbox with labelled tools: Rename, Extract function, Inline, Move, Extract class, Parameter object, Replace conditional, Guard clauses, each with a small before and after sketch of boxes.

ON-IMAGE TEXT: show a short bold title "Common Refactorings" plus only these few labels, large and legible: Smell, Technique, Result. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Core Refactorings

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Refactoring</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it does</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical smell it addresses</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rename</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Gives a variable, function, or class a clearer name everywhere it is used</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unclear names</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Extract function (method)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Takes a block of code and turns it into a new function with a descriptive name, replacing the block with a call</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Long method; comments explaining a block</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Inline function</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The reverse: replaces a call with the body of the function when the body is as clear as the name, or the function does too little</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Needless indirection; middle man</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Extract variable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Gives the result of a complicated expression a name</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hard-to-read expression</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Inline variable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Removes a variable that adds no clarity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Needless temporary</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Move function (or field)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Moves behaviour to the class that uses it most</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Feature envy; misplaced responsibility</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Extract class</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Splits a class with several responsibilities into two</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Large class; divergent change</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Inline class</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Merges a class that does too little into another</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lazy class</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Introduce parameter object</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Replaces a group of inputs that travel together with one object</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Long parameter list; data clumps</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Replace magic number with named constant</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Gives a literal a name that states its meaning</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unexplained numbers and strings</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Encapsulate field or collection</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Makes data private and provides controlled operations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Exposed internals</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Replace primitive with object</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Introduces a small class for a concept such as money</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Primitive obsession</td>
    </tr>
  </tbody>
</table>

## Simplifying Conditional Logic

Conditionals are a common source of complexity, and several refactorings address them.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Refactoring</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it does</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Result</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Decompose conditional</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Extracts the test and each branch into named functions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The condition reads as intent</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Consolidate conditional expression</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Combines several tests with the same outcome into one named test</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Less repetition</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Replace nested conditional with guard clauses</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Handles special cases first and returns early</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A flat main path</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Replace conditional with polymorphism</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Moves each branch into a class for each kind, selected by type</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Adding a kind adds a class; no more chains</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Introduce special case</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Replaces repeated checks for a missing or exceptional value with an object that behaves appropriately</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No scattered checks</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Remove flag argument</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Splits a function with a true or false switch into two functions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Clear, separate behaviours</td>
    </tr>
  </tbody>
</table>

## Reorganising Class Hierarchies

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Refactoring</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it does</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pull up</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Moves behaviour common to subclasses into the parent</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Push down</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Moves behaviour used by only one subclass into that subclass</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Replace subclass with delegate</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Replaces inheritance with composition and delegation</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Extract interface</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Defines an interface from the operations clients actually use</td>
    </tr>
  </tbody>
</table>

## Doing a Refactoring: Extract Function as an Example

The mechanical procedure for extracting a function shows the style of all refactorings.

1. Identify the block of code that does one identifiable thing.
2. Choose a name that says **what** it does, not how.
3. Create the new function, copy the block into it, and note which values from the surrounding code it uses, which become its inputs, and which values it produces, which become its output.
4. Replace the original block with a call to the new function.
5. Run the tests.
6. Look for other places with the same block that could use the new function.

Each step is small, and the tests confirm after each that behaviour is unchanged. If the tests fail, the last step is undone.

## A Sequence in Practice

Suppose a function that calculates the price of an order has grown to sixty lines: it checks for an empty order, adds up the items, applies a bulk discount with a literal number, applies a member discount in a nested condition, and formats a text summary. A sequence of refactorings could be:

1. **Rename** unclear variables so that the existing steps can be read.
2. **Replace the magic numbers** with named constants.
3. **Replace the nested conditions** with guard clauses for the empty order and other special cases.
4. **Extract functions** for adding up items, applying each discount, and formatting the summary.
5. **Move** the summary formatting out of the pricing code to where output formatting belongs.

After each step the tests pass. The result is a short top-level function that reads as a list of steps, with small named helpers beneath it, and the original behaviour is intact.

## Good Habits

- **Let the tool do mechanical work** where possible.
- **Make one kind of change at a time,** and commit often.
- **Look for the next smell** after each change; refactorings often lead to further ones.
- **Stop at good enough.** Perfection is not the goal.
- **Review in terms of behaviour preservation,** with refactoring commits separate from feature commits.

<!--
IMAGE PROMPT  ->  generate as images/02_refactoring_sequence_before_after.png   (16:9 explanatory diagram, place here)

A before-and-after pair of abstract diagrams. Before: one long block with nested step-shaped sub-blocks and a red Magic number tag. After: a short top-level block listing five small named blocks (Validate, Add items, Apply bulk discount, Apply member discount, Format summary) with a green tick. Arrows between them labelled Rename, Extract, Guard clauses, Move.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Choose the Refactoring

1. A function takes street, city, postcode, and country as four separate inputs in many places.
2. A function contains three levels of nested conditions that handle special cases before the main logic.
3. A block in the middle of a long function has a comment saying "calculate shipping."
4. A class has a number of methods that mostly work with the data of another class.

Case 1 calls for Introduce parameter object, an address. Case 2 calls for Replace nested conditional with guard clauses. Case 3 calls for Extract function, named calculate shipping, replacing the comment. Case 4 calls for Move function to the other class.

## Conclusion

A refactoring is a named, behaviour-preserving transformation of code, such as extracting a function, renaming, or moving behaviour, applied in small steps to remove a specific weakness in structure. A repertoire of such techniques turns the recognition of a smell into a safe, routine response.

Some weaknesses are not repaired immediately, and the accumulated effect is a cost the project carries. The next topic examines this under the metaphor of technical debt.
