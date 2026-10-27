## Introduction

Tools that suggest, explain, and write code using large language models have become part of everyday software development. They complete lines, draft functions from descriptions in plain language, explain unfamiliar code, propose tests, summarise changes, and in their more autonomous forms carry out multi-step tasks across a codebase. These tools can raise productivity and lower the barrier to starting, but they also produce plausible-looking errors, insecure code, and invented details with total confidence. The responsibility for what ships does not move: the engineer who accepts the output owns it. Learning to use these tools well, and to know when not to, is now part of professional practice. Tools and capabilities change quickly, so this topic concentrates on durable principles instead of particular products.

This topic explains what AI coding assistants are and how they work in outline, where they help, how to give them effective instructions, how to review what they produce, the main risks, and how teams and learners should use them responsibly.

**Definition:** AI-assisted software development is the use of machine-learning systems, typically large language models, to help with software engineering tasks such as writing, explaining, testing, and reviewing code, with the engineer remaining responsible for the correctness, security, and appropriateness of the result.

<!--
IMAGE PROMPT  ->  generate as images/17_intro_ai_assisted_software_development.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A person silhouette and an assistant icon sharing a workspace: the assistant offers suggestion cards labelled Draft, Explain, Test, and the person holds a large checkmark stamp labelled Review before a gate labelled Ship.

ON-IMAGE TEXT: show a short bold title "AI-Assisted Software Development" plus only these few labels, large and legible: Assist, Then Verify. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## What These Tools Are

- **Large language models (LLMs)** are neural networks trained on vast amounts of text and code to predict what comes next. Given a prompt, they generate a continuation that fits the patterns they learned. They produce **likely** text, not verified truth: they have no built-in guarantee that code compiles, runs, or is correct.
- **Forms of assistance:**

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Form</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Description</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical use</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Inline completion</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Suggests the next lines as you type</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Boilerplate, repetitive patterns</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Chat assistant</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Answers questions and writes code in conversation, in the editor or a web page</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Explaining code, exploring options, drafting functions</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Agentic tools</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Plan and carry out multi-step tasks: reading files, editing several files, running tests and commands, iterating on failures</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Larger changes, refactors, fixing failing tests</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Review and summarisation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Describe changes, suggest issues in pull requests</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">First-pass review (Unit 11)</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Specialised generators</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Create tests, documentation, queries, scripts, configuration</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Support tasks</td>
    </tr>
  </tbody>
</table>

- **Context:** the model sees only what it is given: the prompt, selected files, and any retrieved information. It does not truly know your system, requirements, or constraints unless they are provided. Limits on how much it can consider at once mean that large systems must be provided in parts.
- **Non-determinism:** the same prompt can yield different answers.

## Where They Help

- **Boilerplate and routine code:** repetitive structures, data transformations, standard integrations.
- **Learning and explanation:** summarising unfamiliar code, explaining error messages, comparing approaches. For novices these are valuable, provided the explanations are checked.
- **Starting points:** a first draft to react to is often faster than a blank page.
- **Tests:** suggesting test cases and edge cases (to be reviewed; Unit 10).
- **Documentation and commit messages** (Unit 8, Unit 9).
- **Refactoring and migration:** mechanical changes across many files (with strong tests).
- **Exploring unfamiliar languages and libraries.**
- **Searching and navigating** large codebases.
- **Prototyping** to learn quickly (and throwing the prototype away).
- **Drafting communication:** design notes, summaries, release notes (next topic).

Evidence on productivity is mixed: some controlled studies find substantial time savings on well-defined tasks, while others find that experienced developers working in familiar, complex codebases can be slowed by checking and correcting output. Perceived and measured speed can differ. Benefits depend on the task, the skill of the user, and the discipline of the process.

## Working With the Tool: Effective Instructions

The quality of the output depends greatly on the quality of the request. This is sometimes called prompting. Sound habits are close to the habits of good communication and requirements engineering (Unit 3).

1. **State the goal and the context.** Say what you are building, why, the language and frameworks, and the constraints (performance, security, style).
2. **Be specific about what is wanted and what is not,** including inputs, outputs, error cases, and non-goals.
3. **Provide relevant material:** the surrounding code, the interface it must match, the conventions in use, examples of the desired style or output.
4. **Break large tasks into small steps.** Ask for a plan first, discuss it, then implement in pieces that can each be reviewed and tested.
5. **Ask for reasons and alternatives,** such as trade-offs, assumptions made, and edge cases considered.
6. **Iterate:** respond to what you see, correct misunderstandings, and refine; a conversation beats a single long request.
7. **Specify how to check:** ask for tests alongside code, and tell the tool how to run them.
8. **Keep control of the design.** Decide the architecture and interfaces yourself (Units 5 to 7) and ask the tool to fill in the parts; tools tend to produce locally plausible code that may not fit the whole.
9. **Do not include secrets or confidential data** in prompts unless the tool is approved for such use (see risks).

## Reviewing Generated Code

Treat generated output as an **unreviewed contribution from a fast, confident, junior colleague who cannot be trusted to know your system.** Everything in Units 8, 10, and 11 applies.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Check</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Questions</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Understanding</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can you explain every line? If not, do not ship it. Ask the tool to explain, and check the explanation against documentation</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Correctness against requirements</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Does it do what is needed in all cases, including edge cases and failure conditions? Is anything missing or silently different from what you asked?</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hallucinated details</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Do the functions, parameters, packages, and options it uses actually exist in the versions you use? Models invent plausible interfaces</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tests</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Run the tests. Are the generated tests meaningful, or do they merely repeat the implementation or assert nothing? Do they fail when the code is broken?</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Security</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Does it validate input, handle secrets, check authorisation, and avoid known weak patterns (Unit 14)? Generated code reproduces insecure practices found in training data</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dependencies</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Does it add new libraries? Are they real, maintained, safe, and licensed acceptably? Attackers register packages with names that models tend to invent</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Design fit</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Does it follow the architecture, naming, and style of the codebase (Unit 8)? Is it needlessly complex or duplicated?</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Performance and resources</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Is it efficient enough? Does it do wasteful work?</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Licensing and origin</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Could it reproduce copyrighted or restrictively licensed code? Follow the policy of your organisation (previous topics)</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Maintainability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Would a colleague understand and change it? Is it documented where necessary?</td>
    </tr>
  </tbody>
</table>

Use the normal safeguards: version control with small commits (Unit 9), code review by a human, continuous integration with tests and scanners, and the definition of done. Review the diffs line by line, particularly in agentic changes that touch many files, and be alert to unrequested changes, deleted tests, and weakened checks.

## Risks and Limits

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Risk</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Description</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Mitigation</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Plausible errors</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Output looks right and is subtly wrong; fluent explanations of wrong code</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tests, review, running the code, independent verification</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hallucination</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Invented APIs, options, facts, and package names</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Check against documentation; compile and run; verify dependencies exist and are legitimate</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Insecure code</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Missing validation, outdated or weak cryptography, injection-prone patterns</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Security review, scanners, secure coding standards (Unit 14)</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Confidential data leakage</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Proprietary code, secrets, or personal data sent to an external service, and possibly retained or used for training</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use approved tools with appropriate data terms; never paste secrets or personal data; follow organisational policy</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Licence and copyright uncertainty</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Generated code may resemble training material; legal status unsettled and varies by jurisdiction</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Follow policy; use tools with provenance filters or indemnities where offered; seek legal advice for sensitive uses</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Over-reliance and skill erosion</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Accepting output without understanding; learners fail to build fundamentals</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Write and reason yourself first on learning tasks; use the tool to explain and to check, not to replace thinking</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Automation bias</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Humans trust a confident machine over their own doubts</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Deliberate scepticism; require evidence</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hollow tests</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tests that pass but verify nothing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Mutation testing, deliberate bug injection, review of assertions (Unit 10)</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Homogeneity and technical debt</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Large quantities of similar, unreviewed code that nobody understands; duplication; inconsistent design</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keep changes small; refactor; maintain architecture ownership</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prompt injection and agent hazards</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Agents that read untrusted content (web pages, issues, files) can be tricked into following hidden instructions; agents with broad permissions can delete data or leak secrets</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Least privilege for agents; sandboxing; human approval for risky actions; treat external content as untrusted (Unit 14)</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Outdated knowledge</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Models are trained up to a cutoff and may suggest deprecated or vulnerable practices</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Check current documentation and advisories</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Bias and quality variation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Better support for popular languages and styles than for niche ones</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Be aware and verify</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cost and environment</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Large models use energy and money</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use proportionately (previous topics)</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Accountability gaps</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"The AI wrote it" is not an excuse</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The engineer who commits the code is responsible</td>
    </tr>
  </tbody>
</table>

## A Responsible Workflow

1. **Understand the task first;** write down the requirements and acceptance criteria yourself.
2. **Plan and decompose;** decide the design.
3. **Ask for small, well-defined pieces,** with context.
4. **Read and understand** what comes back; ask follow-up questions.
5. **Test:** run existing tests, add new ones (ideally written first or independently reviewed), and try to break it.
6. **Check quality and security** with tools and checklists.
7. **Commit in small steps** with clear messages that describe the change truthfully, so history is understandable.
8. **Get a human review,** and disclose AI assistance where your team or institution requires it.
9. **Reflect:** what did the tool get wrong, and what did you learn? Update prompts and team guidelines.

## For Teams and Organisations

- **Set a clear policy:** approved tools, what data may be shared, rules on disclosure, licence handling, and review requirements.
- **Keep standards unchanged:** generated code must meet the same quality, security, and testing bars as any other.
- **Invest in guardrails:** strong test suites, continuous integration, static analysis, and code review are what make faster generation safe.
- **Train people** in use and in critical evaluation.
- **Watch outcomes, not volume:** do not measure productivity by lines or commits generated (Unit 13); track quality, defects, lead time, and maintainability.
- **Protect learning:** junior engineers need to develop understanding; pair them with mentors and set exercises that require reasoning without the tool.
- **Review the legal and ethical position** with counsel and in light of regulation as it develops.

## For Learners

Software engineering education aims to build the ability to understand, design, and verify, not merely to produce code that runs. Using an assistant to skip the thinking defeats that purpose and leaves a person unable to judge the tool's output. Sensible habits:

- Attempt the problem yourself before asking, then compare.
- Ask for hints, explanations, and critique rather than complete solutions.
- Never submit what you do not understand; check your institution's rules on permitted assistance and be honest about your use of the tool.
- Build the foundations in this course: requirements, design, testing, version control, and security. These are exactly the skills needed to direct and check an assistant.

## Looking Ahead

Capabilities will continue to change, and the share of routine code written by machines will probably grow. This shifts the emphasis of the profession toward what tools do poorly: understanding the real problem, making design and trade-off decisions, verifying behaviour, taking responsibility for consequences, and working with people. The engineer's judgement becomes more important, not less.

<!--
IMAGE PROMPT  ->  generate as images/17_assist_review_verify_loop.png   (16:9 explanatory diagram, place here)

A loop of five steps in a ring: Specify, Generate, Review, Test, Commit; a human-icon at the centre with an authority badge; red warning tags on the Generate step (hallucination, insecure code, leaked data) and green shield tags on Review and Test.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Use the Assistant Wisely

1. An assistant suggests code that imports a library you have never heard of. What should you do before using it?
2. The assistant writes both a function and the tests for it, and everything passes. Is that enough?
3. A teammate wants to paste the company's customer database export into a public chat tool to ask for help with an error. What is the problem?

For case 1, check that the package really exists, is maintained, is the one you intend (not a look-alike name), and has an acceptable licence and no known vulnerabilities. For case 2, no: tests written by the same tool may only mirror the implementation; review the assertions, add independent cases, and try to break the code. For case 3, it sends confidential personal data to an external party, breaching privacy law and company policy; use synthetic or minimised data and approved tools.

## Conclusion

AI-assisted software development is the use of machine-learning systems, typically large language models, to help with software engineering tasks such as writing, explaining, testing, and reviewing code, with the engineer remaining responsible for the correctness, security, and appropriateness of the result. Clear instructions, small steps, rigorous review and testing, and careful handling of data and licences let engineers gain the benefit of the tools without giving up responsibility.

Whatever the tools, engineers must also be able to explain their work to other people. The final chapter turns to professional practice, beginning with technical writing and communicating designs.
