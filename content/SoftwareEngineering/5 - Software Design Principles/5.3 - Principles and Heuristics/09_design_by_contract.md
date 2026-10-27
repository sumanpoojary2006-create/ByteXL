## Introduction

Many bugs arise from a mismatch of assumptions between the code that calls an operation and the code that implements it. The caller assumes the operation will handle any input, and the implementer assumes the caller will never pass a negative amount. Neither assumption is written anywhere, so the first time they meet is a failure in production. Design by contract removes this ambiguity by making the obligations of each side explicit, in the manner of a legal contract between two parties.

**Definition:** Design by contract is an approach in which each operation of a module states a contract, the conditions the caller must satisfy before calling, the conditions the operation guarantees afterwards, and the conditions that always hold for the module, so that responsibilities are explicit and violations are detectable.

<!--
IMAGE PROMPT  ->  generate as images/09_intro_design_by_contract.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Two parties, Caller and Module, shaking hands over a document with three labelled clauses: Before (precondition), After (postcondition), Always (invariant).

ON-IMAGE TEXT: show a short bold title "Design by Contract" plus only these few labels, large and legible: Before, After, Always. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Origins

The approach was developed by Bertrand Meyer, who built it into the Eiffel programming language in the 1980s, and it draws on earlier work on program correctness by Tony Hoare and others. Many languages now support it through assertions or libraries, and the underlying thinking applies even without tool support.

## The Three Parts of a Contract

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Part</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Who is responsible</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example for "withdraw money from an account"</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Precondition</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What must be true before the operation is called</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The caller</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The amount is positive and not greater than the balance</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Postcondition</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What the operation guarantees will be true when it finishes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The implementer (the supplier)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The balance has decreased by exactly the amount</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Invariant</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A condition that is true whenever the module is in a stable state</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The module</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The balance is never negative</td>
    </tr>
  </tbody>
</table>

The contract is an **obligation and benefit** for both parties. The caller must meet the precondition, and gains the guarantee. The supplier may assume the precondition holds, and must deliver the postcondition. If a precondition is violated, the **caller** is at fault. If a postcondition is violated, the **supplier** is at fault. This clarity assigns responsibility for each defect.

## Contract Versus Defensive Programming

Two attitudes toward bad input exist.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Aspect</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Defensive programming</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Design by contract</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Assumption</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Never trust callers; check everything inside every operation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Callers must satisfy stated preconditions; the supplier relies on them</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Where checks live</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Repeated in many places</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stated once, in the contract</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cost</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Redundant checks, extra code and time</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fewer checks; violations signal a bug in the caller</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Risk</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hides bugs by quietly coping with bad input</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Needs discipline so that contracts are stated and honoured</td>
    </tr>
  </tbody>
</table>

Neither is absolute. At the **boundary of a system**, where input comes from users or other systems, defensive validation is essential, because those parties cannot be trusted to honour a contract. Inside a system, between well-controlled modules, contracts reduce clutter and make responsibility clear.

## Contracts and Inheritance

Contracts explain the Liskov substitution principle. A subtype can be used wherever its parent is expected only if it respects the parent's contract: it may **accept more** (weaken the precondition) and may **promise more** (strengthen the postcondition), but it must not demand more or deliver less. A subtype that rejects inputs the parent accepted, or that guarantees less, will break code written against the parent.

## How Contracts Are Expressed

- **In documentation,** as clear statements of what each operation requires and guarantees.
- **As assertions,** checks that the program makes while running, usually in development and test, that stop the program when a condition fails.
- **In types,** using specific types so that invalid values cannot exist, such as a positive amount type.
- **In tests,** that check postconditions and invariants for a range of inputs.
- **In tools,** with languages and libraries that support contract notation and can check or even prove contracts.

## Benefits

- **Clarity:** each module states what it needs and offers.
- **Better debugging:** a failed contract points at the party that broke it, close to the cause.
- **Executable documentation:** contracts remain accurate because they can be checked.
- **Simpler code:** less defensive clutter inside modules.
- **Foundation for testing and reasoning:** contracts define what to test.

## Limitations

Complex conditions can be hard to state. Contracts checked at run time cost performance, so they are often disabled in production, which means violations are found only where tests exercise them. Contracts do not replace validation of untrusted input, and they require teams to agree and maintain them.

<!--
IMAGE PROMPT  ->  generate as images/02_contract_clauses.png   (16:9 explanatory diagram, place here)

A timeline for the operation withdraw money: a Before box (Amount is positive and not more than balance, caller responsible), the operation in the middle, an After box (Balance reduced by amount, supplier responsible), and an Always banner across the top (Balance never negative, module responsible).

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Write the Contract

For an operation that adds an item to an order, state:

1. A precondition.
2. A postcondition.
3. An invariant of the Order.

A precondition could be that the quantity is at least one and the dish is available. A postcondition could be that the order now contains the dish with the requested quantity and the total has increased by the price times the quantity. An invariant could be that the order total always equals the sum of the prices of its lines.

## Conclusion

Design by contract is an approach in which each operation of a module states a contract, the conditions the caller must satisfy before calling, the conditions the operation guarantees afterwards, and the conditions that always hold for the module, so that responsibilities are explicit and violations are detectable. It turns hidden assumptions into stated agreements.

The principles in this chapter aim to make software easier to change. The final chapter considers change directly and how designs are judged.
