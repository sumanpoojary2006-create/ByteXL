## Introduction

Testing shows that a program works for the cases tried. Review and analysis raise confidence. But for some software, such as the control of a railway, a cryptographic protocol, or the core of an operating system, "works for the cases we tried" is not enough, and we want to know that it is correct for **all** cases. Mathematics offers a way: describe what the software must do precisely, in a formal language, and prove that the design or code meets the description. These are the formal methods. They are demanding and used selectively, but they have achieved remarkable results, and they shape everyday practice through the ideas, such as preconditions, postconditions, and invariants, that they introduced.

**Definition:** Formal methods are techniques that use mathematically precise languages to specify the behaviour of a system and mathematical reasoning, such as proof or exhaustive checking, to verify that a design or program satisfies its specification.

<!--
IMAGE PROMPT  ->  generate as images/08_intro_formal_specification_and_verification_an_introduction.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A mathematical specification card on the left connected by a proof bridge to a program on the right, with a checking engine labelled Model checker exploring a graph of states and a stamp labelled Proved for all inputs.

ON-IMAGE TEXT: show a short bold title "Formal Specification and Verification" plus only these few labels, large and legible: Specify, Prove, Check. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Two Activities

- **Formal specification** states what the system must do, in a notation with a precise mathematical meaning, free of the ambiguity of natural language.
- **Formal verification** shows, by mathematical argument, that a model, design, or implementation satisfies the specification.

The contrast with testing is stark: a test examines individual executions, whereas verification reasons about **all possible** executions. Edsger Dijkstra's remark that testing can show the presence of bugs but never their absence is the motivation. Donald Knuth's quip is the warning: "Beware of bugs in the above code; I have only proved it correct, not tried it."

## A Spectrum

Formal methods are not all-or-nothing.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Level</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Description</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Examples</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lightweight</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use precise notations and automatic checks without full proof</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Type systems; assertions and contracts; specification languages with automatic analysers</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Model checking</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Build a model of the system and automatically explore all its reachable states to check properties</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Checking a protocol for deadlock</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Formal specification only</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Write a precise specification to remove ambiguity and aid review</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Specifying an interface in a formal language</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Full formal verification</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prove, with machine-checked proof, that code or design meets the specification</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A verified operating system kernel or compiler</td>
    </tr>
  </tbody>
</table>

## Specification Languages

Several languages have been developed to describe systems precisely.

- **Z** and **VDM**, based on set theory and logic, describing the state of a system and operations on it.
- **B and Event-B**, which support stepwise refinement from specification down to code.
- **Alloy,** a lightweight language with an automatic analyser that finds counterexamples to claimed properties in small models.
- **TLA+**, created by Leslie Lamport, for specifying and checking concurrent and distributed systems.
- **Languages in proof assistants** such as Coq, Isabelle, and Lean, in which both specifications and proofs are written.

## Pre- and Postconditions: Hoare Logic

The core idea of verifying programs goes back to Tony Hoare's 1969 paper. A piece of code is described by a **triple**: if a **precondition** holds before it runs, and it runs to completion, then the **postcondition** holds afterwards. This is the same idea as the preconditions and postconditions of design by contract in Unit 5, here given mathematical rules for proving that each statement and each combination of statements establishes its postcondition.

For loops, the central tool is the **loop invariant**: a condition that holds before the loop, is preserved by each pass, and, together with the loop's ending condition, implies the desired result. Finding invariants is the creative part of verifying algorithms by hand.

A tiny illustration in words: to prove that a routine adding up the prices of the items of an order returns the correct total, one states the invariant "after processing the first k items, the running total equals the sum of their prices," shows it is true at the start (zero items, total zero), shows that processing one more item preserves it, and concludes that after all items the total is the sum of all prices.

## Model Checking

Model checking, for which Edmund Clarke, Allen Emerson, and Joseph Sifakis received the Turing Award in 2007, automatically and exhaustively explores every state a model of the system can reach, checking that desired properties hold in all of them, such as "the system never deadlocks" or "every request is eventually answered." When a property fails, the tool produces a **counterexample**: the exact sequence of steps that leads to the violation, which is invaluable for debugging a design. Its main limitation is **state explosion**: the number of states grows enormously with the size of the system, so models must be abstracted or limited.

## Proof Assistants and Automated Provers

- **Interactive theorem provers** (proof assistants) check proofs written with human guidance. They give the highest assurance but demand great expertise and effort.
- **SMT solvers** (satisfiability modulo theories), such as Z3, automatically decide logical formulas about numbers, arrays, and the like, and underlie many verification and analysis tools.
- **Deductive verifiers** let developers annotate code with specifications that the tools try to prove automatically.

## Achievements

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What was done</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Paris Metro Line 14 (1998)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Safety-critical train control software developed with the B method; reported to have run with no defects found in operation</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">seL4 microkernel</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An operating system kernel whose implementation was proved to match its specification, and later to have security properties</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">CompCert</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A C compiler whose compilation was proved, with a proof assistant, to preserve the meaning of programs, work led by Xavier Leroy</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Amazon Web Services</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Engineers used TLA+ to specify and check designs of distributed systems and reported finding subtle design errors that testing and review had missed, errors needing long sequences of events to appear</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Intel Pentium division bug (1994)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A flaw in a floating-point division unit that cost the company an estimated several hundred million dollars; it prompted much greater use of formal verification in hardware design</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cryptographic and security libraries</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Verified implementations of important algorithms and protocols</td>
    </tr>
  </tbody>
</table>

## Limits and Costs

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Limit</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cost and expertise</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Proofs need highly skilled people and substantial effort, often several times the cost of the code</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The specification may be wrong</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Verification shows that the program meets the specification, not that the specification captures what is needed. This is verification, not validation, in the sense of Unit 2</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The model is not the system</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Proofs concern models; real systems involve hardware, compilers, operating systems, and users that may not behave as assumed</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Scale</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">State explosion and proof effort limit the size of what can be verified</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not everything can be formalised</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Usability, many quality attributes, and human factors resist formal treatment</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tools can have faults</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Proof tools and their assumptions have to be trusted</td>
    </tr>
  </tbody>
</table>

## When to Use Formal Methods

They repay their cost where failure is catastrophic or costly to repair, or where complexity defies informal reasoning.

- **Safety-critical systems,** where standards for the highest levels of assurance encourage or require formal methods (the next topic).
- **Security-critical components,** such as kernels and cryptography.
- **Protocols and concurrent or distributed algorithms,** where subtle interleavings defeat testing.
- **Core libraries and compilers** that many others depend on.
- **Hardware design,** where fixing a flaw after manufacture is impossible.

For ordinary applications, the **lightweight** end is most practical: strong type systems, contracts and assertions, property-based testing that checks general properties on many generated cases, and small models of the trickiest designs.

<!--
IMAGE PROMPT  ->  generate as images/02_spectrum_of_formal_methods_and_model_checking.png   (16:9 explanatory diagram, place here)

Top: a horizontal spectrum from Lightweight (types, assertions) through Model checking and Formal specification to Full proof, with cost increasing to the right. Bottom: a state graph explored by a checker, with a path highlighted in red labelled Counterexample, and a warning note The spec may be wrong.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Match the Need

1. A team designing a distributed protocol fears subtle problems that appear only with unusual sequences of events. Which technique suits?
2. A proof shows that a program meets its formal specification, but users still find the system useless. What went wrong?
3. What lightweight formal technique can any team use every day?

For case 1, model checking or a specification language such as TLA+ suits, since it explores all sequences. In case 2, the specification did not capture what users need: the program was verified but not validated. For case 3, types, contracts and assertions, and property-based tests apply formal thinking cheaply.

## Conclusion

Formal methods are techniques that use mathematically precise languages to specify the behaviour of a system and mathematical reasoning, such as proof or exhaustive checking, to verify that a design or program satisfies its specification. They are costly and used selectively, but they provide the strongest assurance available for the most critical software and enrich everyday practice with precise thinking.

The most demanding assurance is reserved for software whose failure can hurt people. The next chapter turns to safety-critical software and the lessons of failures.
