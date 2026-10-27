## Introduction

Few subjects in programming provoke as much disagreement as comments. Some developers insist that every function should be documented, while others hold that comments are a sign of code that failed to explain itself. The truth lies in between and depends on what the comment says. A comment that explains why a surprising decision was made is invaluable. A comment that repeats what the code obviously does is noise, and one that is out of date is worse than none, because it lies.

**Definition:** Self-documenting code is code whose names and structure express its intent so clearly that it needs little explanation, and comments are the supplementary human-language notes that record what the code cannot say for itself, above all the reasons behind it.

<!--
IMAGE PROMPT  ->  generate as images/04_intro_comments_and_self_documenting_code.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Left: a code block buried under many redundant sticky notes reading This adds one, labelled Noise. Right: clean code with one highlighted note beside a surprising line reading Why: partner system rounds down, labelled Useful.

ON-IMAGE TEXT: show a short bold title "Comments and Self-Documenting Code" plus only these few labels, large and legible: Why, Not What. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Core Idea

Comments cannot make bad code good. If a block of code is hard to understand, the first response should be to **improve the code**: rename things, extract a function with a descriptive name, simplify the structure. Often the comment that would have been written becomes the name of the new function. Comments are for **what the code cannot express**, which is mainly **why**.

## Good Comments

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Kind</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Explaining intent or reasoning (why)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Record the reason for a decision that is not obvious from the code</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The partner service rejects amounts with more than two decimals, so the total is rounded here</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Warning of consequences</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prevent mistakes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Do not change the order of these steps; the receipt depends on it</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Clarifying a complicated algorithm or formula</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Point to the source or explain the idea</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Uses the method described in a named reference</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Public interface documentation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Describe what an operation does, its inputs, outputs, errors, and constraints, for users who should not need to read the implementation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The standard documentation comments for functions and classes</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">To-do notes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Mark known work that is not done, with an owner or ticket</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">To do: support partial refunds, see ticket reference</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Legal and licence notices</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Required statements</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Copyright and licence header</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reasons for rejecting alternatives</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prevent others from retrying a failed idea</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A simpler approach was tried and failed because of a specific limit</td>
    </tr>
  </tbody>
</table>

## Bad Comments

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Kind</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Problem</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Remedy</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Restating the code</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Adds noise and nothing else, and must be maintained</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Delete; make the code clear</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Misleading or outdated comments</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The code changed and the comment did not, so it now lies</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Delete or update; avoid comments that depend on details likely to change</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Commented-out code</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Clutter that nobody dares delete, and confuses readers about what is live</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Delete it; version control remembers</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Journal comments</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A log of changes at the top of a file</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use the version control history</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Position markers and banners</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lines of symbols dividing sections</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Split the file or function instead</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Closing-brace comments</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Notes marking the end of long blocks</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Shorten the block</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Attribution and bylines</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Names in comments that become outdated</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Version control records authorship</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Excuses and jokes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Comments that apologise for or celebrate poor code</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Improve the code</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Comments instead of better names</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A variable named d with a comment saying days</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rename the variable</td>
    </tr>
  </tbody>
</table>

## Self-Documenting Code

Techniques that let code explain itself:

- **Descriptive names** for everything.
- **Small functions** whose names summarise their steps, so that the top-level function reads as a list of what happens.
- **Named constants** instead of unexplained numbers.
- **Explaining variables:** give the result of a complicated expression a name that states its meaning.
- **Named conditions:** put a complex test in a function with a clear name, such as is eligible for discount, so the condition reads as intention.
- **Types and structure** that make wrong use impossible or obvious.
- **Tests** as examples of behaviour: well-named tests document how code is expected to act.

## Comments as Interface Documentation

For parts of a system that others will use, such as a library or a public interface, documentation of **what** each operation does and **how to use it** is essential, since users should not read the implementation. Languages provide standard conventions for such documentation comments, from which reference pages can be generated. These describe the contract: inputs, outputs, errors, side effects, and examples. Internal details are not repeated.

## Keeping Comments Honest

- **Put the comment close to the code it describes,** so that a change to one prompts a change to the other.
- **Comment on reasons, not mechanics,** since reasons change less often.
- **Review comments in code review** as seriously as code.
- **Delete comments that no longer apply.**
- **Prefer links to durable explanations** for long background, such as a decision record, instead of long passages in the code.

## The Balance

The advice to avoid comments is easily taken too far. Code can show **how** but not always **why**, and a team that never writes comments loses the reasoning behind decisions. The practical rule is: **explain in code what can be explained in code, and use comments for what cannot.**

<!--
IMAGE PROMPT  ->  generate as images/02_good_vs_bad_comments.png   (16:9 explanatory diagram, place here)

Two columns. Left, Helpful: icons for Why, Warning, Public interface, To-do with ticket, Licence, each with a green tick. Right, Harmful: icons for Restating code, Outdated, Commented-out code, Journal log, Excuse, each with a red cross. A note at the bottom reads Improve the code first.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Keep or Delete?

1. A comment above a line that adds one to a counter reads: add one to the counter.
2. A comment explains that a delay of two seconds is needed because the partner system cannot handle faster requests.
3. A block of old code has been commented out for six months, with a note saying maybe needed later.

Comment 1 restates the code and should be deleted. Comment 2 explains a surprising reason and should be kept, ideally with a pointer to its source. Comment 3 should be deleted, since version control keeps the history if it is needed.

## Conclusion

Self-documenting code is code whose names and structure express its intent so clearly that it needs little explanation, and comments are the supplementary human-language notes that record what the code cannot say for itself, above all the reasons behind it. Improve the code first, and use comments to explain why.

Readable code also depends on a consistent look. The next topic covers formatting and coding standards.
