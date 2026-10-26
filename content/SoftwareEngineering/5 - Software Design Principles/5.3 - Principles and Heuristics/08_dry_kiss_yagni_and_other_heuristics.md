## Introduction

Alongside the formal principles are shorter sayings that experienced developers use daily to check their own design instincts. They are easy to remember and easy to misuse, and they sometimes pull in opposite directions. Knowing them, and knowing when each applies, helps a designer make pragmatic choices instead of following rules blindly.

**Definition:** Design heuristics such as DRY, KISS, and YAGNI are concise rules of thumb that capture common lessons about duplication, simplicity, and over-engineering, and they guide design decisions by prompting the right questions rather than prescribing exact answers.

<!--
IMAGE PROMPT  ->  generate as images/08_intro_dry_kiss_yagni_and_other_heuristics.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Three labelled signposts: DRY showing one master copy with many arrows pointing to it, KISS showing a simple straight path beside a tangled one, YAGNI showing an unused extra room crossed out.

ON-IMAGE TEXT: show a short bold title "DRY, KISS, YAGNI and Other Heuristics" plus only these few labels, large and legible: Once, Simple, Needed. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## DRY: Do Not Repeat Yourself

Andrew Hunt and David Thomas stated it as: **every piece of knowledge must have a single, unambiguous, authoritative representation within a system.** The concern is not repeated text but repeated **knowledge**: the same business rule, such as how tax is calculated, expressed in several places. When the rule changes, every copy must be found and changed, and one missed copy produces an inconsistency.

Applying DRY means putting each rule, decision, or piece of data in one place and referring to it elsewhere.

**Caution:** code that looks similar is not always duplication of knowledge. Two pieces that happen to look alike today but change for different reasons should remain separate. Merging them creates coupling that forces them to change together. A useful rule is to wait until a pattern appears three times before abstracting, so the right shared form is clear.

## KISS: Keep It Simple

The phrase is attributed to the engineer Kelly Johnson at Lockheed, who held that aircraft should be repairable with basic tools under field conditions. In software it says that **the simplest design that meets the need is usually the best**. Simple designs have fewer parts, fewer interactions, and fewer places for defects, and they are quicker for others to understand.

Simple does not mean easy to produce: it often takes effort to find a simple solution. It also does not mean simplistic: a design must still meet its requirements.

## YAGNI: You Are Not Going to Need It

From Extreme Programming, YAGNI warns against building features or flexibility for needs that are only imagined. Speculative generality has costs: the time to build it, the complexity of carrying it, and the real risk that the guess was wrong and the code must be removed or worked around.

YAGNI does not forbid planning. It says to build what is needed now, and to keep the design clean so that adding the next thing later is cheap. It must be balanced against decisions that are costly to reverse, where thinking ahead is justified.

## Other Useful Heuristics

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Heuristic</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Why it helps</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Separation of concerns</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Handle one aspect of a problem at a time</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Changes to one concern do not disturb others</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Law of Demeter (least knowledge)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A module should talk only to its direct collaborators, not to the internals of their collaborators</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reduces coupling and fragile chains of calls</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Principle of least astonishment</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Behaviour should match what a reasonable user expects</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reduces misuse and surprise</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Composition over inheritance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Build behaviour by combining objects instead of inheriting from classes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Avoids rigid hierarchies and tight coupling to parents</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Favour immutability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prefer data that cannot change after creation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Removes whole classes of bugs involving unexpected change</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fail fast</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Detect and report errors as early as possible</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Problems are found close to their cause</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rule of three</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Wait for the third occurrence before generalising</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Avoids premature, wrong abstractions</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Premature optimisation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Do not optimise before measuring; Donald Knuth called it the root of much evil</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prevents complexity added for imagined performance needs</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Convention over configuration</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Provide sensible defaults so that users need to specify only the unusual</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reduces effort and error</td>
    </tr>
  </tbody>
</table>

## When the Heuristics Conflict

Heuristics are rules of thumb, and several can pull in opposite directions.

- **DRY versus simplicity:** removing every duplication can create abstractions so indirect that the code is harder to follow than the duplication was.
- **DRY versus independence:** merging similar code couples things that should change separately.
- **YAGNI versus design for change:** doing nothing for the future may make it expensive, while building for it may waste effort.
- **KISS versus SOLID:** interface layers add structure that is useful at scale but burdensome for a small program.

The skill lies in noticing the tension and deciding for the case at hand. A good question is: **which choice will make the next likely change cheaper?**

## Heuristics Are Not Substitutes for Thinking

Quoting a heuristic ends few design arguments. Saying "YAGNI" to dismiss a necessary safeguard, or "DRY" to justify a convoluted abstraction, misuses the idea. Use heuristics as prompts for discussion and ground the decision in the actual requirements, risks, and costs.

<!--
IMAGE PROMPT  ->  generate as images/02_heuristics_in_tension.png   (16:9 explanatory diagram, place here)

A seesaw with DRY on the left end and Simplicity on the right end, with a small balance point labelled Judgement. Two smaller seesaws below: YAGNI versus Design for change, KISS versus Structure for scale.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Which Heuristic?

1. The same tax rule is written out in four modules, and one was missed during an update.
2. A team adds a plug-in system for features nobody has requested.
3. A solution uses five layers and three design patterns to solve a problem that needs one function.
4. Two functions look alike but one is for invoices and the other for delivery notes, and are owned by different teams. A developer wants to merge them.

Case 1 violates DRY. Case 2 violates YAGNI. Case 3 violates KISS. Case 4 warns against over-applying DRY: the similarity may be accidental, and merging couples two things that change for different reasons.

## Conclusion

Design heuristics such as DRY, KISS, and YAGNI are concise rules of thumb that capture common lessons about duplication, simplicity, and over-engineering, and they guide design decisions by prompting the right questions rather than prescribing exact answers. Their value lies in the judgement used to apply them.

The next topic describes a more formal way to state what each part of a design promises and expects: design by contract.
