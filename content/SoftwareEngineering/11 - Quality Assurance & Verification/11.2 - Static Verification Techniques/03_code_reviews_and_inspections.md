## Introduction

Reading is one of the cheapest and most effective ways to find defects. A second pair of eyes sees what the author has stopped seeing, brings different knowledge, and asks the questions the author forgot to ask. Unit 9 described the day-to-day workflow of pull requests. This topic looks at the broader family of review techniques, from informal conversations to formal inspections, what evidence shows about their effectiveness, and how to make reviews of code and other work products produce real value.

**Definition:** A review is a structured examination of a work product, such as code, a design, or a requirement, by people other than its author in order to find defects and improve quality before the work is used further, and an inspection is the most formal kind of review, with defined roles, procedures, and records.

<!--
IMAGE PROMPT  ->  generate as images/03_intro_code_reviews_and_inspections.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A spectrum bar from Informal on the left (two people at a screen) through Walkthrough, Technical review, to Formal inspection on the right (a table of four roles with documents and a checklist), with a rising effectiveness arrow.

ON-IMAGE TEXT: show a short bold title "Code Reviews and Inspections" plus only these few labels, large and legible: Read, Question, Improve. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Why Reviews Work

- **Fresh eyes.** Authors tend to read what they meant, not what they wrote.
- **Different knowledge.** Reviewers know other parts of the system, other techniques, and other failure modes.
- **Finding defects early,** before testing, when they are cheapest to fix and at the earliest possible stage, including requirements and design, which testing cannot examine.
- **Finding defects that tests miss,** such as unclear logic, missing cases, maintainability problems, and security flaws.
- **Sharing knowledge** and spreading standards across the team.
- **Reducing dependence** on single individuals.
- **Mentoring,** as less experienced developers learn from the reviewers and the reviewers from fresh perspectives.

## The Range of Review Types

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Type</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Description</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Formality</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical use</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Informal review (over-the-shoulder, ad hoc)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A colleague looks at work as the author explains it, or the author asks for a quick opinion</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Low</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quick feedback during development</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pair programming</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Two people write together, so review is continuous</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Low, continuous</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Complex or risky work; knowledge sharing</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Walkthrough</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The author leads colleagues through the work product, to educate them, gather feedback, and find problems</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Low to medium</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Early drafts, designs, training</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tool-assisted (modern) code review</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Changes are proposed through a tool, with line-by-line comments and approvals, as in pull requests</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Medium</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Everyday practice in most teams</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Technical review</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A group of technically qualified reviewers examines a product to evaluate suitability and find defects, led by a trained moderator</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Medium to high</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Designs, specifications, critical components</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Formal inspection</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A rigorous peer review with defined roles, entry and exit criteria, checklists, preparation, and recorded data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">High</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Safety-critical or high-risk work; requirements and designs</td>
    </tr>
  </tbody>
</table>

## Formal Inspections

Michael Fagan developed the formal inspection process at IBM in the mid-1970s, and it remains the model of rigorous review.

### Roles

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Role</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Responsibility</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Author</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Created the work product; answers questions, but does not defend or lead</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Moderator (facilitator)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Plans and runs the inspection, keeps the meeting efficient and focused on finding defects</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reader (or presenter)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Paraphrases the work product item by item during the meeting</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Recorder (scribe)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Writes down every defect and decision</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Inspectors</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Examine the product against a checklist and their experience, each often with a different focus</td>
    </tr>
  </tbody>
</table>

### Stages

1. **Planning:** check that the product meets the entry criteria, select the team, and schedule.
2. **Overview** (optional): the author briefly explains the context.
3. **Individual preparation:** each inspector reads the product alone, against the checklist, and notes issues. Much of the value comes from this stage.
4. **Inspection meeting:** the group goes through the product and logs defects. The meeting finds and records problems; it does **not** try to fix them or debate solutions.
5. **Rework:** the author corrects the defects.
6. **Follow-up:** the moderator verifies that the corrections were made, and decides whether the exit criteria are met or another inspection is needed.

### Evidence of Effectiveness

Studies over decades have found that formal inspections can detect a large share of the defects present in a work product, in many reports well over half and in some more than three quarters, at a lower cost per defect than testing, and that they find different kinds of defects. Because they apply to requirements and designs, they can prevent costly rework. Their cost lies in the people's time, which is repaid when defects are found early.

## What Evidence Says About Modern Review

Studies of everyday reviews give a more nuanced picture.

- A study at Microsoft by Alberto Bacchelli and Christian Bird found that although developers expected reviews to find defects, the main benefits actually obtained were **knowledge transfer, shared understanding of the code, and better solutions**, with defect finding less prominent than expected.
- A widely cited analysis of reviews at a networking company, published by a code review tools vendor, suggested that reviewers find defects most effectively when they examine **no more than about 200 to 400 lines of code at a time,** at a rate **below about 500 lines an hour,** for **no more than about an hour at a stretch.** Effectiveness fell with larger or faster reviews. The figures are rules of thumb, not laws, but the pattern is consistent: **small, unhurried reviews work best.**
- Reviews are more effective when reviewers use **checklists** and when the author **annotates** the change to guide attention.

## What Reviewers Look For

A review can examine many kinds of problem. A checklist helps ensure coverage.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Category</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Questions</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Correctness and logic</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Does it do what is required? Are conditions, loops, and boundaries right? Are edge cases handled?</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Requirements and design fit</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Does it implement the requirement? Does it follow the architecture and agreed design?</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Error handling</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Are failures detected and handled? Are resources released?</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Security</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Is input validated? Are secrets protected? Are access checks present?</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Performance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Any obvious inefficiency, such as repeated heavy work in a loop?</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Testing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Are there tests for the new behaviour and the edge cases? Do they check the right things?</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Readability and maintainability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Clear names, small functions, no duplication, understandable structure?</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Standards</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Does it follow the coding standards, which tools should check automatically?</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Documentation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Are comments and documents updated?</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dependencies and compatibility</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Are new libraries justified? Is it backward compatible?</td>
    </tr>
  </tbody>
</table>

Reviews of **non-code** work products use similar checklists: a requirements review asks whether each requirement is necessary, unambiguous, testable, and consistent, as Unit 3 described; a design review asks about coupling, cohesion, and fitness against the quality goals.

## Doing Reviews Well

- **Review small pieces,** frequently, and promptly.
- **Prepare:** read the description and understand the purpose before looking at the details.
- **Use checklists,** tailored to the team and updated with the defects it actually meets.
- **Let tools do tools' work:** formatting and mechanical checks are automated, leaving human attention for logic and design.
- **Focus on the work product, not the person.** Comment on the code, not the author, and phrase remarks as observations or questions.
- **Distinguish severity:** blockers, suggestions, and optional nitpicks.
- **Have the right people:** someone who knows the area, and someone with a fresh view.
- **Limit time** and take breaks; fatigue lowers effectiveness.
- **Follow through:** confirm that issues are fixed.
- **Record and learn:** keep data on defects found by type, to improve checklists and process.
- **Build a culture of safety,** where being reviewed is normal and welcome and no one is embarrassed by findings.

## Problems and Remedies

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Problem</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Remedy</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rubber stamping: approval without reading</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keep reviews small; expect comments; track review depth</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reviews that take days</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Agree turnaround times; distribute load</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Large changes nobody can review</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Split work; review designs before code is written</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Personal criticism and conflict</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Team norms; focus on the work; training</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Nitpicking on style</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Automate style checks</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Authors who treat review as an attack</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Show that finding defects is the purpose; reviewers share responsibility for the result</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One person always reviewing everything</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rotate; share knowledge</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reviews skipped under pressure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Make them a part of the Definition of Done</td>
    </tr>
  </tbody>
</table>

<!--
IMAGE PROMPT  ->  generate as images/02_inspection_stages_and_review_size.png   (16:9 explanatory diagram, place here)

Left: the Fagan inspection flow Planning, Overview, Preparation, Inspection meeting, Rework, Follow-up as six connected steps with role icons. Right: a gauge showing effective review size, a green zone up to 400 lines and a red zone beyond, with a clock showing under 60 minutes.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Choose the Review

1. A team writes the specification for a new component whose failure could injure people.
2. A developer wants quick feedback on an idea before writing more code.
3. A reviewer is asked to look at a change of 2,000 lines in one sitting. What is the likely outcome, and what is the remedy?

For case 1, a formal inspection of the specification is justified by the risk. For case 2, an informal over-the-shoulder discussion or a draft pull request suffices. In case 3, effectiveness drops sharply for very large reviews; the remedy is to split the change into smaller pieces and review them separately.

## Conclusion

A review is a structured examination of a work product, such as code, a design, or a requirement, by people other than its author in order to find defects and improve quality before the work is used further, and an inspection is the most formal kind of review, with defined roles, procedures, and records. Small, prepared, checklist-based reviews, held in a safe culture, find defects early and spread knowledge.

People are good at judgement but poor at tedious consistency. The next topic describes how tools examine code automatically: static analysis and linting.
