## Introduction

Compilers have always checked that code is well formed, and a good deal more can be checked without running the program. Static analysis tools read source code, or the compiled form of it, and look for defects, risky patterns, rule violations, and signs of poor quality. They are tireless, consistent, and fast, and they work at every change. They complement testing, which runs the code on chosen inputs, by examining all of the code, including paths that no test reaches. Understanding what they can and cannot do is essential to using them well.

**Definition:** Static analysis is the automated examination of software without executing it, in order to detect defects, vulnerabilities, deviations from standards, and signs of poor design, and linting is the everyday form of static analysis that flags suspicious or non-conforming code as it is written.

<!--
IMAGE PROMPT  ->  generate as images/04_intro_static_analysis_and_linting.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A scanner passing over a block of code from side to side, flagging coloured markers on lines: red for serious bug, orange for warning, blue for style, and a report panel listing counts, with a pipeline gate icon beside it.

ON-IMAGE TEXT: show a short bold title "Static Analysis and Linting" plus only these few labels, large and legible: Scan, Flag, Fix. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Static and Dynamic Analysis

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Aspect</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Static analysis</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Dynamic analysis (including testing)</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Runs the program?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Yes</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Examines</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">All the code, including rarely executed paths</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Only the paths actually executed</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Finds</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Patterns that are likely to be defects; rule violations; some security flaws</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Actual failures in behaviour, performance, and integration</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Weakness</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">May report false alarms or miss problems that depend on run-time conditions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cannot show that untested paths are correct</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">When</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Early; as the code is written</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">After there is something to run</td>
    </tr>
  </tbody>
</table>

The two are complementary.

## Origins

The name **lint** comes from a tool written by Stephen Johnson at Bell Labs in the late 1970s to check C programs for suspicious constructs that the compiler accepted; like lint on a garment, it picked up small flaws. Today "linter" is the common term for tools that check code for stylistic and likely-bug issues in many languages.

## What Static Analysis Can Find

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Kind</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Examples</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Syntax and type errors</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Calls with the wrong kind of input; use of the wrong type, caught by compilers and type checkers</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Likely bugs</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Variables used before being set; code that can never run; conditions that are always true or false; comparing things of different kinds; missing returns</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Resource problems</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Files, connections, or memory not released</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Null and missing value problems</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dereferencing something that may be absent</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Security vulnerabilities</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Injection flaws; unsafe use of input; hard-coded secrets; weak cryptography; buffer overflows in languages that allow them</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Concurrency problems</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Possible race conditions; inconsistent locking</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Style and standards violations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Naming, formatting, missing documentation, forbidden constructs</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Complexity and design smells</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Very long or complex functions; deep nesting; duplicated code; excessive coupling</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dependency and licence issues</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Vulnerable or disallowed libraries</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Infrastructure and configuration problems</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Insecure settings in infrastructure definitions and container build files</td>
    </tr>
  </tbody>
</table>

## How It Works: A Brief Look

Tools use a range of techniques of increasing sophistication.

- **Pattern matching and syntax analysis:** looking for known risky shapes in the structure of the code.
- **Type checking:** verifying that values are used consistently with their declared kinds. A strong type system is a built-in form of static analysis that rules out whole classes of error.
- **Control-flow analysis:** examining the possible routes through the code, to find unreachable code or missing cases.
- **Data-flow analysis:** following how values move through the program, to find uses of unset values, unused values, and the like.
- **Taint analysis:** tracking data that comes from untrusted sources, such as user input, to see whether it reaches a sensitive operation, like a database query, without being cleaned. This is the heart of many security tools.
- **Abstract interpretation and symbolic execution:** reasoning about all possible values or paths mathematically, which can prove the absence of certain errors, at greater cost.
- **Metrics computation:** measuring size, complexity, duplication, and coupling.

## Accuracy: The Fundamental Trade-Off

It is a mathematical result, related to Rice's theorem and the halting problem, that no tool can decide perfectly, for all programs, whether a program has a given behaviour. So every static analyser must compromise.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Term</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">True positive</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A real problem correctly reported</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">False positive</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A report of a problem that is not really one (a false alarm)</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">False negative</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A real problem the tool failed to report (a miss)</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sound analysis</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reports every possible error of its kind, accepting false positives</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Complete analysis</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reports only real errors, accepting that it may miss some</td>
    </tr>
  </tbody>
</table>

Many practical tools favour **few false alarms** over completeness, because developers ignore tools that cry wolf. Some safety-critical tools favour soundness and accept the effort of dismissing false alarms.

## Alert Fatigue and How to Avoid It

The greatest practical problem with static analysis is a flood of warnings. A tool pointed at an old codebase can report thousands of findings, and the team stops reading them.

- **Start with a small, high-value rule set,** concentrating on likely bugs and security. Add rules gradually.
- **Tune the configuration:** disable rules that do not suit the project, and set severities.
- **Baseline legacy code:** record existing findings and fail the build only for **new** problems in changed code, while improving old areas gradually.
- **Fix or deliberately suppress,** with a comment explaining why, instead of ignoring.
- **Treat serious findings as build failures,** using quality gates.
- **Review the suppressions** from time to time.
- **Measure** the trend and the rate of false alarms.

## Linting and Formatting in Practice

Linters and formatters are the most common form of static analysis, and as Unit 8 described, automatic formatters settle layout and linters catch likely mistakes.

- Run them **in the editor,** so that feedback is immediate while writing.
- Run them **before commit,** to avoid noise in reviews.
- Run them **in the pipeline,** as a required check.
- Use a **shared configuration** held in the repository.
- Treat **compiler warnings** as errors where practical, since a warning is an early sign of trouble.

## Tools

The landscape is wide. Examples include language-specific linters such as ESLint for JavaScript and Pylint or Ruff for Python, bug finders such as SpotBugs for Java, style checkers such as Checkstyle, multi-language platforms such as SonarQube, pattern-based scanners such as Semgrep, deeper security query engines such as CodeQL, and scanners for dependencies, secrets, and infrastructure definitions. The best choice depends on the languages and risks of the project.

## Quality Gates

A **quality gate** is a condition that a change must meet to proceed in the pipeline. Typical conditions are: no new serious defects or vulnerabilities, no new security hotspots left unreviewed, complexity and duplication within limits, and adequate test coverage on new code. Gates turn static analysis from advice into enforcement, as the earlier topic on quality assurance described.

## Limits

- Static analysis **does not replace testing or review.** It finds what it has rules for.
- It cannot judge whether the code does what the **requirements** intend.
- Findings **need interpretation:** an expert must judge which are important.
- **Over-reliance** gives false confidence: a clean report is not proof of correctness.
- Metrics-based rules can encourage **gaming** if used as targets.

<!--
IMAGE PROMPT  ->  generate as images/02_static_analysis_pipeline_and_false_alarms.png   (16:9 explanatory diagram, place here)

Left: layers of checks from Editor linting to Pre-commit to Pipeline quality gate with a block icon. Right: a two-by-two of True positive, False positive, False negative, True negative for the tool's reports, and a funnel labelled Tune and baseline to reduce noise.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Interpret the Tool

1. A tool reports 4,000 warnings on an old codebase. The team decides to ignore all of them. What is a better approach?
2. A tool reports a possible database injection flaw, but the code actually cleans the input in a way the tool cannot see. What kind of report is this?
3. Why can a static analyser find a defect on a path that no test has ever executed?

A better approach in case 1 is to baseline the existing findings and require that new or changed code have no new serious findings, then reduce the backlog gradually. Case 2 is a false positive. In case 3, static analysis examines the structure of the code and does not need to run it, so it considers all paths, not only the executed ones.

## Conclusion

Static analysis is the automated examination of software without executing it, in order to detect defects, vulnerabilities, deviations from standards, and signs of poor design, and linting is the everyday form of static analysis that flags suspicious or non-conforming code as it is written. Used with sensible configuration, quality gates, and a plan for managing noise, it catches many problems earlier and more cheaply than any other technique.

Static analysis can measure as well as detect. The next topic considers software metrics: what they can tell us and how they are misused.
