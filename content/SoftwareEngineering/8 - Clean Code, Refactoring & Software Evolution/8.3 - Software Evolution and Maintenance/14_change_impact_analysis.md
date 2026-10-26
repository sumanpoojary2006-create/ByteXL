## Introduction

Changing one part of a system can affect others in ways that are not obvious. A small modification to how prices are rounded may alter invoices, reports, tax summaries, and an integration with an accounting system. Unforeseen effects are a major source of defects after change, and the more tangled the system, the more likely they are. Change impact analysis is the activity of working out, before the change is made, what it will affect, so that the work can be planned, tested, and communicated properly.

**Definition:** Change impact analysis is the process of identifying the potential consequences of a proposed change, that is, which parts of the system, tests, documents, and people it will affect, so as to estimate the cost and risk and plan the work.

<!--
IMAGE PROMPT  ->  generate as images/14_intro_change_impact_analysis.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A ripple spreading outward from a single changed block in a network of connected blocks, with nearby blocks marked as directly affected and distant ones as possibly affected, and a magnifying glass tracing the connections.

ON-IMAGE TEXT: show a short bold title "Change Impact Analysis" plus only these few labels, large and legible: Ripple, Trace, Plan. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Ripple Effect

A change spreads through **dependencies**: a function called by others, data shared between modules, a contract relied on by another system, a document describing behaviour. The study of ripple effects in software goes back to work in the early 1970s. The aim of analysis is to estimate how far the ripples go.

## Why Do It

- **Estimate effort and cost** realistically, so that a change is not undersold.
- **Assess risk,** since changes touching many or critical areas are riskier.
- **Decide whether to proceed,** alter the approach, or defer.
- **Plan the testing,** knowing which areas to retest.
- **Coordinate with teams and users** who will be affected.
- **Avoid surprises** that lead to defects and rework.

## Sets of Elements

Analysts distinguish several sets.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Set</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Starting impact set</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The elements the analyst initially believes will change</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Candidate impact set</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The elements the analysis predicts might be affected</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Discovered impact set</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Elements found to be affected that were not predicted: the analysis missed them</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">False positives</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Elements predicted as affected that turned out not to be</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Actual impact set</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The elements actually changed in the end</td>
    </tr>
  </tbody>
</table>

A good analysis has few misses and few false alarms. Misses cause defects, and false alarms waste effort.

## Techniques

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Technique</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">How it works</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Strength</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Limit</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dependency analysis (static)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Follows calls, inheritance, and data usage in the code, often with tools that show where a function or field is used</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Systematic and fast</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">May overestimate, and cannot see dynamic or configured connections</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Traceability analysis</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Follows links from requirements to design, code, and tests</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Finds related documents and tests</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Needs up-to-date traces</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dynamic analysis</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Records which parts of the code run in given situations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Shows real usage</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Only covers the executions observed</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Co-change (history) analysis</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Mines version control to find files that have often changed together</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reveals hidden coupling</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Depends on history quality</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Expert judgement and walkthroughs</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Developers and users discuss what the change touches</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Captures knowledge not in the code</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Subjective; may miss things</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Searching the code and configuration</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Text search for names, constants, and settings</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Simple and effective</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Misses indirect uses</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Test results and impact of tests</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Running existing tests to see what fails</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Direct evidence</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Depends on test coverage</td>
    </tr>
  </tbody>
</table>

Using several techniques together gives better coverage than any one.

## Questions to Ask

- Which components, functions, and data does the change touch directly?
- What depends on those, in the code, in other systems, and in data stored earlier?
- Do any external parties, such as partner systems or customers, rely on the behaviour being changed?
- Which requirements, designs, tests, and documents describe it?
- Will existing data need to be migrated or converted?
- Does it change performance, security, or other quality attributes?
- What would be the effect of failure, and can the change be reversed?
- What must be retested, and what new tests are needed?
- Who must be told?

## From Analysis to Decision

The result is a short summary for the person or group deciding on the change: the scope, the impact on parts and on people, the effort, the risk and its mitigation, the testing needed, and recommendations for staging or release. In a change control process, it is the basis for accepting, deferring, or rejecting the request.

## Reducing the Impact of Change

Analysis is far easier, and impacts smaller, in a system with good structure.

- **Low coupling and clear interfaces** limit the spread.
- **Automated tests** reveal impacts quickly by failing.
- **Traceability** makes the links explicit.
- **Modular design with stable interfaces** lets changes stay inside a module.
- **Code search and navigation tools** make dependencies visible.
- **Versioned interfaces** protect other parties.

## Limits

No analysis is complete. Dynamic behaviour, configuration, reflection, and external systems hide dependencies. For this reason, analysis is combined with **safeguards**: tests, staged releases, feature switches, monitoring, and the ability to roll back.

<!--
IMAGE PROMPT  ->  generate as images/02_impact_sets_and_techniques.png   (16:9 explanatory diagram, place here)

Concentric circles: Starting impact set in the centre, Candidate impact set as a larger ring, Actual impact set overlapping as an irregular shape with a part outside the candidate ring labelled Missed (red) and a part of the candidate ring outside the actual shape labelled False alarm (orange). Beside it icons for the techniques.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Identify the Impact

A team plans to change how an order total is rounded.

1. Name three places the change could have effects.
2. Name two techniques to find them.

Possible effects are invoices and receipts, tax and financial reports, the integration that sends totals to an accounting system, stored historical totals, and tests that check amounts. Techniques include searching the code for every use of the total and the rounding function (dependency analysis), and asking people in finance and support which reports depend on it (expert judgement), or running the existing tests to see which fail.

## Conclusion

Change impact analysis is the process of identifying the potential consequences of a proposed change, that is, which parts of the system, tests, documents, and people it will affect, so as to estimate the cost and risk and plan the work. A systematic analysis, combined with safeguards, is the best protection against unexpected side effects.

To analyse an impact, one must first understand the system. The next topic describes how engineers recover understanding of software that is unfamiliar or poorly documented.
