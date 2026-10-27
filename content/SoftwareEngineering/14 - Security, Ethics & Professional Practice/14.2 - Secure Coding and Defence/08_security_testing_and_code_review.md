## Introduction

Writing secure code and designing secure systems are not enough; the result must be examined. Security testing looks for vulnerabilities in a system before attackers find them, using a mixture of human review, automated analysis, and simulated attack. No single technique finds everything: each sees a different kind of flaw. Effective programmes combine several and run them continuously, so that security problems are found at the same speed and in the same way as other defects.

This topic describes static and dynamic analysis, dependency and secret scanning, fuzzing, penetration testing, security-focused code review, and the way vulnerabilities found should be reported and handled.

**Definition:** Security testing is the set of activities, including automated analysis, manual review, and simulated attack, that evaluate a system to find vulnerabilities and verify that security controls work as intended, so that weaknesses can be corrected before they are exploited.

<!--
IMAGE PROMPT  ->  generate as images/08_intro_security_testing_and_code_review.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A magnifying glass over source code on the left labelled Static, a running application with a probe arrow in the centre labelled Dynamic, and a figure in a hooded outline probing a wall on the right labelled Pen test.

ON-IMAGE TEXT: show a short bold title "Security Testing and Code Review" plus only these few labels, large and legible: Look, Probe, Attack. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Testing Landscape

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Technique</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Looks at</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">When</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Finds</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Misses</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Static application security testing (SAST)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Source code or compiled code, without running it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Early; in the editor and pipeline</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Insecure patterns, injection paths, hard-coded secrets, unsafe functions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Runtime and configuration problems; many false positives; flaws in business logic</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Software composition analysis (SCA)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Third-party components and versions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Build time and continuously</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Known vulnerable libraries, licence issues</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unknown flaws; whether a vulnerable function is actually used</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Secret scanning</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Code, history, and configuration</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Commit time and continuously</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Exposed keys, tokens, passwords</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Secrets not matching known patterns</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dynamic application security testing (DAST)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The running application from outside</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Test environment</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Misconfiguration, injection and cross-site scripting through the interface, missing headers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Code never reached; business logic flaws</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Interactive testing (IAST)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The application instrumented from inside during tests</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Test environment</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Flaws with precise location and context</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Needs good test coverage</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Infrastructure and configuration scanning</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cloud settings, container images, infrastructure code</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Build time and continuously</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Open storage, weak permissions, outdated images</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Application logic</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fuzzing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Program inputs</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Test environment</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Crashes, hangs, memory errors, unexpected behaviour on malformed data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Flaws needing precise valid input sequences</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Penetration testing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The whole system from an attacker's view</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Before release and periodically</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Chained weaknesses, logic and design flaws, process failures</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Anything outside the scope and time</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Security code review</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Code and design read by humans</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">During development</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Logic errors, authorisation gaps, design flaws</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Large volumes; depends on reviewer skill</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Threat-model-driven tests</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Specific threats from the model</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Throughout</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Whether planned controls work</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Unknown threats</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Red teaming and bug bounties</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Realistic attack campaigns or open invitations to researchers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Mature organisations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Real-world weaknesses in people, process, and technology</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cost; requires a response capability</td>
    </tr>
  </tbody>
</table>

## Static Analysis

Static analysis tools examine code for patterns known to be dangerous: building queries from strings, use of weak cryptographic functions, missing checks, and unsafe memory use. More advanced ones trace the flow of untrusted data (**taint analysis**) from its source (user input) to its use in a sensitive place (a query or a command) and report paths that lack validation.

- **Benefits:** early feedback, covers all code, runs automatically.
- **Limits:** false positives waste time, false negatives give false assurance, and tuning is needed. Treat results as leads to be assessed, not verdicts.
- **Good practice:** run in the editor and the pipeline; fail builds only on high-confidence serious findings; track and age the backlog; agree on rules with the team.

Unit 11 covered static analysis for quality in general; here the focus is its security rules.

## Dynamic Testing

DAST tools behave like an automated attacker, sending crafted requests to a running application and examining the responses. They find problems that only appear at runtime and test the real configuration, without needing the source. Run them against a test environment, never against production without care, since they can create or delete data. Authenticated scanning, which logs in, reaches much more of the application.

**API testing** is similar: checking that each endpoint enforces authentication and authorisation, validates input, limits rates, and does not return excessive data.

## Fuzzing

A **fuzzer** generates huge numbers of unusual inputs, random or derived from valid ones, and watches for crashes, hangs, or errors. **Coverage-guided fuzzing** observes which parts of the code each input reaches and evolves inputs to explore more. It has found thousands of flaws in widely used software, particularly in parsers for files, images, and network protocols, and where programs written in languages without automatic memory safety are concerned. It suits any component that processes complex untrusted input.

## Penetration Testing

A **penetration test** is an authorised, time-limited attempt by skilled testers to break into a system, using the same methods as real attackers, and then to report what was achieved and how to fix it.

- **Scope and rules of engagement** are agreed in writing: which systems, what methods, what times, how to handle data found. Unauthorised testing is illegal in most countries.
- **Approaches** are described by how much the testers know: **black box** (nothing beyond what an outsider has), **grey box** (some information, such as an account), **white box** (full access to source and design).
- **Phases** typically include reconnaissance, scanning, exploitation, post-exploitation (how far access extends), and reporting.
- **Reports** rank findings by severity with clear reproduction steps and recommended fixes.
- **Value:** reveals how weaknesses combine, tests detection and response, and satisfies customers and regulators. **Limit:** it is a snapshot; one test does not make a system secure.

**Red teams** run longer, goal-driven simulated campaigns, often including social engineering and physical access, and test the organisation's detection and response; **blue teams** defend; **purple teaming** has both collaborate to improve defences. **Bug bounty programmes** pay outside researchers for responsible reports of valid vulnerabilities.

## Security Code Review

Human review finds what tools cannot: missing authorisation on an endpoint, flawed business logic, misuse of cryptography, and design assumptions that do not hold. Unit 11 described review in general; for security, reviewers add a particular focus.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Review focus</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Questions</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Trust boundaries and inputs</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Where does untrusted data enter? Is it validated and handled safely?</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Authentication</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Are all entry points authenticated? Are credentials and sessions handled safely?</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Authorisation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Is every action and every object checked on the server? Could one user reach another's data?</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Secrets and cryptography</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Are secrets kept out of code? Are standard libraries and algorithms used?</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Error handling and logging</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Do errors reveal internals? Are security events recorded without sensitive data?</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dependencies</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Are new libraries needed, maintained, and free of known flaws?</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Configuration</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Are defaults safe? Are debug features off?</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Abuse</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How could this feature be misused or automated at scale?</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Is more personal data collected or retained than necessary?</td>
    </tr>
  </tbody>
</table>

Use **checklists** based on the OWASP categories; give the highest scrutiny to changes in security-critical areas (authentication, payment, access control, cryptography); and make a security specialist available. Pair review with threat modelling for new features.

## Testing the Controls Themselves

Security requirements should be turned into automated tests in the ordinary test suite (Unit 10).

- A user cannot read or change another user's record (access-control tests for each role).
- Repeated failed logins are limited.
- Invalid and oversized input is rejected.
- Sessions expire and are invalidated at logout.
- Sensitive data does not appear in logs or error messages.
- Security headers and secure cookie settings are present.

Such tests protect against regression: a control that works today can be removed accidentally tomorrow.

## Handling Findings

1. **Triage:** confirm that it is real, understand exposure and impact, and rate severity (for example with CVSS, adjusted for context).
2. **Assign** an owner and a deadline according to severity.
3. **Fix the root cause,** not just the instance: if one endpoint lacked an ownership check, look for others, and improve the shared mechanism.
4. **Verify** the fix and add a regression test.
5. **Record and learn:** feed lessons into training, checklists, and design, using blameless review as in Unit 9.
6. **Track metrics:** time to fix, recurring categories, and findings per release.

### Responsible Disclosure

When outsiders find a flaw, they should be able to report it safely. Organisations publish a **vulnerability disclosure policy** and a contact point (often via a standard file named security.txt on the website), promise not to take legal action against good-faith research, respond promptly, fix within a stated period, and credit the reporter. Researchers agree to keep details private until a fix is available, a practice called **coordinated disclosure.** Fixed flaws are assigned identifiers in the CVE system and described in advisories.

## Limits and Realism

- Testing can show the presence of vulnerabilities, never their absence.
- Tools produce noise; people need time to triage.
- Different techniques complement each other; use a mix.
- Cadence matters more than any single test: continuous checks in the pipeline, with deeper reviews and penetration tests for major releases and high-risk systems.
- Fix what is found: an unread report is worse than none.

<!--
IMAGE PROMPT  ->  generate as images/08_security_testing_techniques_in_the_pipeline.png   (16:9 explanatory diagram, place here)

A pipeline strip left to right (Commit, Build, Test, Stage, Release, Operate) with icons placed under the stages: secret scan and SAST under Commit and Build, SCA under Build, DAST and fuzzing under Test and Stage, penetration test under Release, monitoring and bug bounty under Operate.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Pick the Right Check

1. Which technique would catch a hard-coded cloud key at the moment of committing?
2. Which technique is best for finding crashes in a program that parses uploaded images?
3. A penetration test finds no serious flaws. Does that prove the system is secure?

For case 1, secret scanning (pre-commit or in the pipeline). For case 2, fuzzing. For case 3, no: it shows that the testers, within their scope and time, did not find serious flaws; it is a snapshot, and new code, new vulnerabilities, and different attackers continue to appear.

## Conclusion

Security testing is the set of activities, including automated analysis, manual review, and simulated attack, that evaluate a system to find vulnerabilities and verify that security controls work as intended, so that weaknesses can be corrected before they are exploited. Combining static, dynamic, dependency, and human techniques, running them continuously, and acting on what they find make security measurable.

Protecting the system is one part of protecting the people whose data it holds. The next chapter turns to privacy, ethics, and the law, beginning with privacy by design.
