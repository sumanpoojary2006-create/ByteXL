## Introduction

When a tester, a user, or a colleague finds a defect, the person who must fix it is usually someone else, who was not there, cannot see the screen, and may not know what the reporter was trying to do. The bug report is the only bridge. A good report lets the developer reproduce the problem in minutes and begin diagnosing at once. A poor one, such as "the app is broken," triggers a chain of questions, delay, and sometimes a closed ticket with "cannot reproduce." Writing a good bug report is a small skill with a large effect on how quickly quality improves.

**Definition:** A bug report is a written record of a defect that gives the information a developer needs to understand, reproduce, assess, and fix it: what was done, what was expected, what happened instead, the circumstances, and the evidence.

<!--
IMAGE PROMPT  ->  generate as images/15_intro_writing_good_bug_reports.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A well-structured report card with labelled fields Title, Steps to reproduce, Expected, Actual, Environment, Evidence attached, beside a vague card reading It does not work crossed out in red.

ON-IMAGE TEXT: show a short bold title "Writing Good Bug Reports" plus only these few labels, large and legible: Reproduce, Evidence, Impact. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Goals of a Report

A bug report should enable the reader to:

- **understand** what the problem is
- **reproduce** it themselves
- **judge** its importance and urgency
- **find the cause** with the supplied evidence
- **verify the fix** later

It should be read without needing to ask the reporter any questions.

## The Components of a Good Report

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Field</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Content</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Title (summary)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A short, specific sentence: what fails, and where</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Order total ignores bulk discount for exactly ten items</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Environment</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The version or build, platform, browser or device, configuration, account type, and relevant data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Version 2.4.1, mobile web on a phone, logged in as a member</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Preconditions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The starting state needed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Basket contains ten different dishes</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Steps to reproduce</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A numbered, minimal, exact sequence of actions from a known starting point</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1. Add ten dishes to the basket. 2. Open the basket. 3. View the total</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Expected result</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What should happen, with the source of the expectation if relevant</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Total shows ten percent off, as in requirement 12</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Actual result</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What happened instead, factually</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Total shows the full price; no discount line</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reproducibility</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Always, intermittent (how often), or once</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Always, 5 out of 5 attempts</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Evidence</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Screenshots or a short recording, logs, error messages, stack traces, identifiers, sample data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Screenshot of the basket; order identifier</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Severity and priority</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Technical impact and urgency of the fix (see below)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Severity medium; priority high before the weekend promotion</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Impact and workaround</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Who is affected and how badly; any way to avoid it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">All members with ten items; none known</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Additional information</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What changed recently; whether it worked before; related reports</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Worked in version 2.3.0</td>
    </tr>
  </tbody>
</table>

## Principles

1. **One defect per report.** Several problems in one report get lost, cannot be assigned separately, and cannot be closed independently.
2. **Be specific and precise.** "Slow" is useless; "the basket takes 12 seconds to load with ten items" is actionable.
3. **Give exact steps,** including data values and the order of actions. Do not skip steps that seem obvious.
4. **Find the minimal reproduction.** Remove steps that are not necessary. Try on a clean state.
5. **Separate facts from guesses.** State what you observed. If you suspect a cause, say so but label it as a suspicion.
6. **Compare expected and actual,** and say why you expected it.
7. **Include evidence,** since a picture or a log line removes ambiguity. Redact secrets and personal data.
8. **Check for duplicates** before filing, and add information to the existing report if one exists.
9. **Use a neutral, professional tone.** Report the problem, not the blame. Words like "stupid" help nobody.
10. **Report promptly,** while details are fresh.
11. **Follow up** with extra information when asked, and verify the fix when it is delivered.

## A Poor Report and a Good Report

**Poor:** Title: "Basket broken." Description: "The discount does not work. Please fix ASAP."

This lacks the environment, the steps, any data, and the expected result. The developer must ask.

**Good:** Title: "Order total ignores bulk discount for exactly ten items." Environment: version 2.4.1, mobile web, member account. Steps: add ten different dishes; open the basket. Expected: ten percent discount shown, as the requirement states for ten or more. Actual: full price, no discount line. Reproducible: always; with nine or eleven items the behaviour is correct (nine has no discount, eleven has it). Evidence: screenshot attached. Suspected cause (unconfirmed): a boundary condition at ten. Worked in version 2.3.0.

The good report even points to the **boundary**, saving the developer time.

## Severity and Priority

The two are often confused and are set by different people.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Term</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Decided by</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Severity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The technical impact of the defect on the system or users</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tester or engineer, by the effect</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Critical: data loss or crash. Major: a main function fails. Minor: a small problem with a workaround. Trivial: cosmetic</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Priority</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The urgency of fixing it, considering business needs</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Product owner or manager, by business value and schedule</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">High: fix now. Medium: this release. Low: when convenient</td>
    </tr>
  </tbody>
</table>

They are independent. A **typographical error in the company name on the home page** has low severity but may be high priority. A **crash in a rarely used administrative feature** may be high severity and low priority.

## The Life of a Bug Report

Reports move through a workflow, as the issue tracking topic in Unit 9 described.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">State</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">New</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reported, not yet reviewed</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Triaged or confirmed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reviewed, reproduced, and prioritised</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Assigned</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Given to a person</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">In progress</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Being fixed</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fixed (resolved)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A fix has been made</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Verified</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A tester has confirmed the fix</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Closed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Complete</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reopened</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The fix failed or the problem returned</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rejected states</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Duplicate, cannot reproduce, works as designed, will not fix (with an explanation)</td>
    </tr>
  </tbody>
</table>

**Triage** meetings or routines review new reports regularly. **Verification** by someone other than the fixer, by repeating the original steps and checking nearby behaviour, is the final check.

## Special Cases

- **Security vulnerabilities** must be reported **privately**, through the designated channel, not in a public tracker, so that they can be fixed before attackers learn of them.
- **Intermittent bugs** need as much context as possible: time, frequency, conditions, logs, and what was different when it did and did not occur.
- **Production incidents** follow the incident process of Unit 9, with bug reports created for follow-up work.
- **Reports from users** are often vague. Support staff and testers turn them into complete reports, asking for the missing details politely.

## Defect Data as Feedback

Collected reports show patterns: where defects cluster, which causes recur, how many escape to production, and how long fixing takes. Useful measures include **defect density** (defects per unit of size), **defect escape rate** (the share of defects found after release), and **time to fix**. Used to improve processes and not to blame or rank people, they guide where to invest in testing, design, and training. The next unit builds on them in its treatment of quality assurance.

<!--
IMAGE PROMPT  ->  generate as images/02_bug_report_template_and_severity_priority.png   (16:9 explanatory diagram, place here)

Left: a bug report template card with numbered fields (Title, Environment, Steps, Expected, Actual, Evidence, Severity, Priority). Right: a two-axis grid with Severity (low to high) and Priority (low to high), with examples placed: company name typo (low severity, high priority), crash in rare admin tool (high severity, low priority).

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Improve the Report

1. A report reads: "The search does not work."
2. A tester reports three different problems in the same ticket.
3. Which has high severity but may have low priority: a crash in a rarely used feature, or a spelling mistake on the home page?

Report 1 needs the environment, steps, the term searched for, the expected and actual results, and evidence. Ticket 2 should be split into three, so that each can be tracked and closed on its own. In case 3, the crash in a rarely used feature has high severity but may have low priority, while the spelling error on the home page has low severity but possibly high priority because it is highly visible.

## Conclusion

A bug report is a written record of a defect that gives the information a developer needs to understand, reproduce, assess, and fix it: what was done, what was expected, what happened instead, the circumstances, and the evidence. Clear, minimal, factual reports save time for everyone and speed the improvement of quality.

This completes Unit 10. You can now explain why and how software is tested, use the vocabulary and the test pyramid, write good unit tests, design test cases with partitions, boundaries, decision tables, and state models, use coverage wisely, apply test doubles, practise test-driven and behaviour-driven development, test at integration and system levels, manage regression suites and automation, perform acceptance, exploratory, usability, and non-functional testing, debug systematically, and report defects clearly. Unit 11 takes the next step from testing to the broader discipline of quality assurance and verification.
