## Introduction

A large share of the software that runs the world, from operating systems and web servers to the libraries inside almost every application, is open source: developed in public, by individuals and companies, under licences that allow anyone to use and modify it. Taking part in an open-source project is one of the best ways for a developer to learn, to build a reputation, and to give back. It also teaches in practice nearly everything this unit has covered: version control, pull requests, review, issue tracking, and working with people who may never meet. Contributing to a project that is not your own has its own norms, and knowing them makes the experience smoother.

**Definition:** Open-source collaboration is the practice of developing software in public under licences that grant the right to use, study, modify, and share the code, through a community of users, contributors, and maintainers who coordinate their work using shared tools and agreed conventions.

<!--
IMAGE PROMPT  ->  generate as images/12_intro_open_source_collaboration.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A central repository icon with an open door, many different people around it contributing: one filing an issue, one forking, one opening a pull request, one reviewing, with a licence badge and a code of conduct card on the wall.

ON-IMAGE TEXT: show a short bold title "Open-Source Collaboration" plus only these few labels, large and legible: Fork, Propose, Review. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## What Open Source Means

The **Open Source Definition**, maintained by the Open Source Initiative, sets out criteria for open-source licences, including free redistribution, access to source code, and permission to create derived works. The movement grew out of the earlier **free software** movement begun by Richard Stallman in the 1980s, which emphasises the freedoms of users, and the two terms are often used together. Open source does not mean free of obligations: the licence sets the conditions.

## Common Licences

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Licence family</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Examples</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Key conditions</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Permissive</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">MIT, BSD, Apache 2.0</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Almost any use, including in proprietary products, with attribution and the licence notice; Apache 2.0 adds an explicit patent grant</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Weak copyleft</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">LGPL, Mozilla Public Licence</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Changes to the licensed files must be shared, but larger works that merely use them need not be</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Strong copyleft</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">GPL, AGPL</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Derived works distributed to others must be offered under the same licence; the AGPL extends this to software used over a network</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No licence</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not open source</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No permission is granted; reuse is legally risky</td>
    </tr>
  </tbody>
</table>

When contributing, your contribution is normally released under the project licence. When using open-source software, check that the licence fits your use, a point from the reuse topic in Unit 8.

## Anatomy of an Open-Source Project

Well-run projects have conventions and files that welcome newcomers.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Item</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">README</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What the project is, how to install and use it</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">LICENSE</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The terms of use</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">CONTRIBUTING guide</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How to propose changes: set-up, coding standards, tests, review process</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Code of conduct</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Expected behaviour in the community and how problems are handled; the Contributor Covenant is widely adopted</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Issue and pull request templates</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ensure reports and changes include the needed information</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Security policy</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How to report vulnerabilities privately and responsibly</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Governance document</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Who decides, and how</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Labels such as good first issue and help wanted</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Mark tasks suitable for newcomers</td>
    </tr>
  </tbody>
</table>

## How to Contribute

Contribution is not only code. Valuable contributions include:

- **Reporting bugs** with clear reproduction steps
- **Improving documentation,** fixing typos, adding examples, translating
- **Answering questions** and helping other users
- **Triage:** reproducing reports, confirming duplicates, labelling
- **Testing** releases and proposed changes
- **Reviewing** the changes of others
- **Fixing bugs and adding features**
- **Design, accessibility, and community work**

Documentation and small fixes are excellent first contributions.

## The Fork and Pull Request Workflow

Because strangers do not have write access, contributors work on their own copy.

1. **Find a project and a task.** Read the README, contributing guide, and code of conduct. Look for beginner-friendly issues.
2. **Discuss first** for anything non-trivial. Comment on the issue to say you would like to work on it, and ask questions. For a larger change, agree the approach before writing code.
3. **Fork** the repository to create your own copy on the hosting platform, and **clone** it to your machine.
4. **Add the original as an upstream remote,** and keep your fork up to date with it.
5. **Create a branch** for your change.
6. **Make the change,** following the project style and adding or updating tests and documentation.
7. **Commit** with clear messages, following the project convention.
8. **Push** to your fork and **open a pull request** against the original, referring to the issue.
9. **Respond to review** politely and promptly, updating the branch as requested.
10. **Celebrate and continue** once it is merged, or learn from a rejection.

## Etiquette

- **Read the guidelines first.** Many rejected contributions ignore them.
- **Search existing issues** before filing a new one.
- **Be respectful and patient.** Maintainers are often volunteers with limited time. Responses may take days or weeks.
- **Keep changes small and focused.** Do not mix unrelated changes.
- **Do not take rejection personally.** A project has goals and constraints you may not see.
- **Do not demand.** Ask, offer, and help.
- **Give credit** and use inclusive language.
- **Follow through.** An abandoned pull request is a burden on the maintainer.
- **Never submit code you do not have the right to contribute,** for example copied from a project with an incompatible licence.

## Legal Agreements for Contributions

Some projects require contributors to confirm that they have the right to submit their work.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Mechanism</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Developer Certificate of Origin (DCO)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A simple statement, signified by a sign-off line on each commit, that you wrote the contribution or have the right to submit it under the licence</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Contributor License Agreement (CLA)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A formal agreement, signed once, granting the project permissions to use the contribution, which may include relicensing rights</td>
    </tr>
  </tbody>
</table>

## The Maintainer's View

Understanding the other side makes contributors more effective. Maintainers must triage a flood of issues, review changes, keep quality and direction, respond to security reports, and handle difficult interactions, often unpaid and alongside other work. **Burnout is a serious and common problem.** Contributions that are well-prepared, well-tested, well-explained, and small reduce the load. Helping with triage and documentation is a significant gift.

## Governance and Sustainability

Projects are governed in various ways: a **benevolent dictator** who has the final say, a **core team** or **committee**, or a **foundation** that provides legal and organisational support, such as the Apache Software Foundation, the Linux Foundation, or the Cloud Native Computing Foundation. Funding comes from sponsorship, company employees paid to contribute, grants, and donations. Organisations that depend on open source have both a self-interest and a responsibility to support it.

## Benefits of Contributing

- **Learning** from real projects and experienced reviewers.
- **A public record** of your work, valued by employers.
- **Network and mentoring.**
- **Influence** over the tools you use.
- **Practising professional habits:** collaboration, communication, review.
- **Giving back** to the community that your work depends on.

## Using Open Source Responsibly in Your Own Work

Contributing is only one side. Companies that use open source should track their dependencies and licences, apply security updates promptly, and report problems upstream, since a vulnerability in a widely used library affects everyone who depends on it.

<!--
IMAGE PROMPT  ->  generate as images/02_fork_and_pull_request_flow.png   (16:9 explanatory diagram, place here)

A flow across three repository boxes: Original (upstream) on the right, Your fork (hosted copy) in the middle, Local clone on the left. Arrows: fork from upstream to fork, clone to local, branch and commit locally, push to fork, pull request arrow from fork to upstream, review comments returning. A side card lists README, CONTRIBUTING, Code of Conduct, License.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Contribute Well

1. You want to fix a typo in the documentation of a project. Is this a worthwhile contribution?
2. You plan a large change to the core design of a project. What should you do before writing code?
3. Your pull request receives several requests for changes. How should you respond?

A documentation fix is a fully valid contribution and a good first one. For a large change, open or comment on an issue and agree the approach with the maintainers first, to avoid wasted effort. Respond to review politely, make the requested changes or explain your reasoning, and keep the branch updated.

## Conclusion

Open-source collaboration is the practice of developing software in public under licences that grant the right to use, study, modify, and share the code, through a community of users, contributors, and maintainers who coordinate their work using shared tools and agreed conventions. It teaches the full range of collaborative engineering practice and sustains much of the software the world uses.

With the work of managing code and collaboration covered, the unit turns to how code becomes running software. The next chapter begins with building and delivering software.
