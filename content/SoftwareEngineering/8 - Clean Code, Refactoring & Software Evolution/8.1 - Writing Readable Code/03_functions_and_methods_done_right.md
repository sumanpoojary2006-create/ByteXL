## Introduction

Functions, also called methods, are the basic units in which behaviour is organised. A system is a hierarchy of them, from top-level operations that tell a story down to small steps that do the work. If functions are well formed, the system reads like a clear description of what it does. If they are sprawling, tangled, or inconsistent, no amount of other care will save the code. Good functions are small, focused, and honest about what they do.

**Definition:** A well-designed function is a small, focused unit that does one thing at one level of abstraction, has a clear name and a minimal set of inputs, behaves predictably with few side effects, and can be understood and tested on its own.

<!--
IMAGE PROMPT  ->  generate as images/03_intro_functions_and_methods_done_right.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Left: one huge tangled function block with many arrows in and out, labelled Does everything. Right: a tidy tree of small labelled function blocks, a top-level one calling three small steps, labelled One thing each.

ON-IMAGE TEXT: show a short bold title "Functions and Methods Done Right" plus only these few labels, large and legible: Small, Focused, Honest. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Do One Thing

The guiding principle is that a function should do **one thing**, do it well, and do it only. A useful test is whether you can describe what the function does in one short sentence without using "and". If a function validates an order, saves it, and sends an email, it does three things and should be three functions, called in turn by a fourth that tells the story.

Splitting also helps naming: if a function is hard to name, it probably does too much, or the wrong thing.

## Keep Functions Small

Small functions are easier to understand, test, and reuse. There is no exact limit, but functions that do not fit on a screen, or that need scrolling to read, are usually doing too much. Warning signs include several distinct blocks separated by blank lines or comments, which suggest each block should be its own function with a name replacing the comment.

## One Level of Abstraction

A function should mix steps of the same kind, not high-level policy with low-level detail. A function that says "place order" and, in the middle, manipulates text to format a number is mixing levels. Instead, the top-level function calls steps such as validate order, calculate total, take payment, and confirm, each at the same level, and the detail lives in functions below.

This produces code that can be read **top-down**, like a story: each function is followed by the functions at the next level of detail. This is sometimes called the **stepdown rule**.

## Inputs

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Guideline</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Reason</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keep the number of inputs small, ideally none to three</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Each input adds a thing to understand and to test; many inputs often mean the function does too much or that related values belong in one object</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Group related inputs into an object</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A group such as street, city, and postcode is better expressed as an address</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Avoid flag inputs (true or false parameters that switch behaviour)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The function does two things; split it into two functions with clear names</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Avoid output inputs</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Having a function modify an input to return a result is surprising; return the result</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Order inputs consistently</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use the same order across related functions</td>
    </tr>
  </tbody>
</table>

## Outputs and Side Effects

A **side effect** is a change a function makes beyond returning a value: modifying a global, changing an input, writing a file, or sending a message. Side effects are not forbidden, since programs must do things, but hidden ones are a major source of bugs. A function named "check password" that also logs a user in has a surprising side effect.

- Prefer functions that **compute and return** a value without changing anything else (sometimes called pure functions): they are easy to test and to reason about.
- Keep functions that **change state** separate and clearly named.
- **Command-query separation**, a principle from Bertrand Meyer, says that a function should either **do something** (a command) or **answer something** (a query), but not both. Asking a question should not change the answer.
- Make necessary side effects **obvious** in the name.

## Control Flow

- **Reduce nesting** using guard clauses: handle invalid or special cases at the start and leave early, so that the main path is not indented inside layers of conditions.
- **Avoid deep loops within loops** by extracting the inner steps into named functions.
- **Prefer simple conditions.** Complex tests are better given a name, for example eligible for discount, than left as long expressions.
- **Return early** when the answer is known, rather than carrying flags through the rest of the function.
- **Avoid duplicated code**: if a block appears twice, give it a name and call it from both places.

## Structure of a Method in a Class

In object-oriented code, a method should relate closely to the class data and role. A method that uses mostly the data of another class belongs there, as the feature envy smell indicates. Methods that do not use the class data at all may belong elsewhere.

## Testability

Small, focused functions with clear inputs and outputs are easy to test. Functions that depend on hidden state, the current time, the network, or global values are hard to test; passing such things in as inputs makes the dependence visible and testable.

<!--
IMAGE PROMPT  ->  generate as images/02_function_story_and_guard_clauses.png   (16:9 explanatory diagram, place here)

Left: a function drawn as a staircase of nested blocks (deep nesting, red). Right: the same function drawn flat with early exits for invalid cases at the top and one clear main path below (green), each step labelled. A tree of small functions under a top-level Place order node on the far right.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Improve the Function

1. A function called update order changes the items, recalculates the total, emails the customer, and writes an audit entry.
2. A function takes a true or false input that switches between printing and emailing a receipt.
3. A function named is valid also deletes expired records.

Function 1 does several things and should be split, with a top-level function calling each step. Function 2 should be two functions, print receipt and email receipt. Function 3 hides a side effect in a name that suggests a pure question; the deletion should be separate, with its own clear name, in line with command-query separation.

## Conclusion

A well-designed function is a small, focused unit that does one thing at one level of abstraction, has a clear name and a minimal set of inputs, behaves predictably with few side effects, and can be understood and tested on its own. Systems built from such functions read like clear explanations.

Even excellent code sometimes needs words beside it. The next topic considers when comments help and when they hurt.
