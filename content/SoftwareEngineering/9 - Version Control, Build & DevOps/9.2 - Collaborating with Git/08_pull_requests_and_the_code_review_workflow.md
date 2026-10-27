## Introduction

In most professional teams, nobody commits straight to the main line. Changes are proposed, examined by colleagues, checked by automation, and only then accepted. The mechanism on hosting platforms is the **pull request**, or **merge request** in some tools. It is the point at which a private piece of work becomes a team matter. Done well, the review is the most effective quality practice a team has and the main way knowledge spreads. Done badly, it is a bottleneck and a source of friction.

**Definition:** A pull request is a proposal to merge the changes of one branch into another, presented with a description for discussion, automated checks, and review by teammates, and the code review workflow is the process by which changes are examined, discussed, improved, and approved before they are merged.

<!--
IMAGE PROMPT  ->  generate as images/08_intro_pull_requests_and_the_code_review_workflow.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A flow: Branch with commits, Open pull request with description, Automated checks (green ticks), Reviewers leaving comments, Author updating, Approval, Merge into main.

ON-IMAGE TEXT: show a short bold title "Pull Requests and the Code Review Workflow" plus only these few labels, large and legible: Propose, Review, Merge. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Workflow

1. **Work on a branch** and keep the change focused.
2. **Open a pull request,** with a clear title and description.
3. **Automated checks run:** build, tests, linters, security scans.
4. **Reviewers examine** the change and comment.
5. **The author responds,** adjusting the code or explaining, and pushes updates to the same branch, which the request shows automatically.
6. **Reviewers approve** when satisfied.
7. **The change is merged** by an agreed method, and the branch is deleted.

## The Author Side

A good pull request makes review easy.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Practice</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Reason</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keep it small and focused on one purpose</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Small changes are reviewed faster and more thoroughly; large ones receive superficial approval. Guidance from large companies advocates changes small enough to review in minutes</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Write a clear description: what changed, why, how it was tested, and what to look at</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Gives reviewers context; reduces questions</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Link the related issue or requirement</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Traceability and context</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Review your own change first</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Catches obvious mistakes and debugging leftovers before others see them</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ensure the checks pass before asking for review</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Respect for the time of reviewers</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Include tests and update documentation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A change is complete when its tests and docs are</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Separate refactoring from behaviour changes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Easier to review each</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Add screenshots or notes for visible changes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Helps reviewers understand the effect</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Respond to every comment, and be open to feedback</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The goal is a better change, not victory</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use a draft request for early feedback</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Invites input on direction before polish</td>
    </tr>
  </tbody>
</table>

## The Reviewer Side

The aim of review is to improve the **health of the codebase** and to share knowledge, not to find fault with the author.

**What reviewers consider**

- **Correctness:** does it do what is intended, including edge cases and failures?
- **Design:** does it fit the architecture, and is it simple and well structured?
- **Tests:** are there good tests, and do they fail when the behaviour breaks?
- **Readability:** are names clear, and is the code easy to follow?
- **Maintainability:** will the next person be able to change it?
- **Security and privacy:** are inputs validated, secrets protected, and permissions right?
- **Performance:** any obvious inefficiency in a hot path?
- **Documentation and consistency** with standards.

Automated tools should handle style and mechanical issues, so that human attention goes to design and logic.

**How reviewers behave**

- **Review promptly.** Waiting days is costly; many teams aim for a response within a working day.
- **Be kind and specific.** Comment on the code, not the person, and explain the reason.
- **Ask questions** instead of issuing orders where intent is unclear: "What happens if the list is empty?"
- **Distinguish required changes from suggestions,** for example by marking minor remarks as optional nitpicks.
- **Praise good work.**
- **Do not block on personal preference** when the standards allow the approach.
- **Approve when the change improves the codebase,** even if it is not perfect.
- **Know when to talk.** If a thread becomes long or tense, move to a conversation and record the outcome.

## Merge Options

Platforms offer ways to complete the merge, and the choice follows the team convention, as the branching topic described.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Option</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Result</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Merge commit</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">All commits kept, with a merge commit</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Squash and merge</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">All commits combined into one</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rebase and merge</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Commits replayed onto the target, giving a straight line</td>
    </tr>
  </tbody>
</table>

## Rules and Automation

- **Branch protection** can require passing checks and a minimum number of approvals.
- **Code owners** files name the people or teams who must review changes to particular areas.
- **Required checks** run the pipeline, security scans, and licence checks.
- **Templates** for descriptions remind authors to supply the information needed.
- **Bots** label, assign reviewers, and remind about stale requests.

## Benefits

- **Defects found early,** before they reach users.
- **Shared knowledge:** more than one person understands each part, which also reduces the risk when someone leaves.
- **Consistency** of design and style.
- **Mentoring:** juniors learn from reviewers, and reviewers learn from fresh eyes.
- **Collective ownership** of the code.
- **A record** of discussion and decisions attached to the change.

## Common Problems

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Problem</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Remedy</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Huge changes that nobody can review properly</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Split work; commit to small changes</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Slow reviews, blocking work</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Agree turnaround expectations; rotate reviewers; reduce size</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One person bottleneck</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Spread knowledge; use code owners wisely</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rubber stamping: approving without reading</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Culture and expectations; checklists; reviewer accountability</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Harsh or personal comments</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Team norms; training; blameless attitude</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Endless nitpicking and style fights</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Automate style; separate nits from blockers</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reviews that miss design problems because they come too late</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Discuss design early, with a draft or a short design note</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Review fatigue</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Limit size and time; take breaks</td>
    </tr>
  </tbody>
</table>

## Alternatives and Complements

**Pair programming** and **mob programming** review continuously as code is written. Some teams with strong automation and trust use **post-merge review**, reviewing after changes land on the trunk. The central point is that **someone other than the author looks at the change**, whichever form is used.

<!--
IMAGE PROMPT  ->  generate as images/02_pull_request_lifecycle_and_roles.png   (16:9 explanatory diagram, place here)

A lifecycle loop: Draft, Open, Checks, Review comments, Updates, Approved, Merged. Two figures labelled Author and Reviewer each with a short checklist of responsibilities. A small gauge shows change size with a green zone labelled Small and a red zone labelled Too big.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Improve the Review

1. A pull request changes 3,000 lines across forty files, and the single approval arrives in two minutes.
2. A reviewer comments: This is stupid, who wrote this?
3. Reviewers spend most of their comments on indentation and spacing.

Case 1 is too large and was probably not really reviewed: it should be split. Case 2 is personal and unhelpful; a good comment explains the concern and suggests an improvement. Case 3 calls for an automatic formatter and linter, so that human review attention goes to substance.

## Conclusion

A pull request is a proposal to merge the changes of one branch into another, presented with a description for discussion, automated checks, and review by teammates, and the code review workflow is the process by which changes are examined, discussed, improved, and approved before they are merged. Small changes, prompt and kind reviews, and good automation make it a strength of the team.

Sometimes the history of a branch needs tidying before it is shared, or a single change must be moved to another branch. The next topic covers these advanced operations and the care they require.
