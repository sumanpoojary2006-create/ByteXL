## Introduction

The tools of this unit, version control, pipelines, containers, infrastructure as code, and monitoring, are often called DevOps tools, but tools alone do not make a team effective. Many organisations have adopted all of them and found that little changed, because the underlying relationship between the people who build software and the people who run it was unchanged. DevOps is first a way of working and thinking, and the tools are what make that way of working possible. This topic describes the idea, its origins, its principles, and the common mistakes in applying it.

**Definition:** DevOps is a culture and set of practices that bring together software development and IT operations, emphasising shared responsibility, automation, fast feedback, and continuous learning, so that software can be delivered and run reliably at high speed.

<!--
IMAGE PROMPT  ->  generate as images/23_intro_the_devops_culture.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Left: two teams separated by a high wall labelled Development and Operations with a package being thrown over it. Right: the wall removed, one team in a continuous loop of Plan, Build, Test, Release, Operate, Monitor with shared ownership.

ON-IMAGE TEXT: show a short bold title "The DevOps Culture" plus only these few labels, large and legible: Share, Automate, Learn. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Problem DevOps Addressed

In the traditional model, developers and operations staff were separate groups with opposing incentives.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Group</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Rewarded for</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Therefore tends to</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Development</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Delivering new features quickly</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Push changes, which are the main cause of instability</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Operations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keeping systems stable and available</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Resist change, which is the main cause of instability</td>
    </tr>
  </tbody>
</table>

Developers finished their work and handed software to operations, with little shared understanding, in a handover that came to be known as the **wall of confusion**. Releases were rare, large, and risky. Problems in production were blamed on whoever was on the other side of the wall, and learning was slow.

## Origins

The movement grew in the late 2000s. At the Velocity conference in 2009, John Allspaw and Paul Hammond of Flickr gave a talk titled "10+ Deploys Per Day: Dev and Ops Cooperation at Flickr," showing that cooperation made frequent release safe. The same year Patrick Debois organised the first DevOpsDays conference in Ghent, Belgium, which gave the movement its name. Its influences included agile software development, lean thinking from manufacturing, continuous delivery, and the practices of large internet companies. The novel *The Phoenix Project* (2013) by Gene Kim, Kevin Behr, and George Spafford presented the ideas in story form and reached a wide audience.

## Principles

### CALMS

A commonly used summary, associated with Damon Edwards, John Willis, and Jez Humble, is the acronym CALMS.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Letter</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Principle</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">C</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Culture</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Shared responsibility, trust, collaboration, and no blame</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Automation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Automate repetitive work: building, testing, deploying, provisioning, and monitoring</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">L</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lean</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Small batches, limited work in progress, elimination of waste, and continuous flow</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">M</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Measurement</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Decide with data: delivery performance, reliability, and customer outcomes</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">S</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sharing</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Share knowledge, tools, and lessons across teams</td>
    </tr>
  </tbody>
</table>

### The Three Ways

*The Phoenix Project* and its companion *The DevOps Handbook* describe three underlying principles.

1. **Flow:** speed up the movement of work from development through operations to the customer, by making work visible, limiting work in progress, reducing batch sizes, and removing constraints.
2. **Feedback:** create fast, constant feedback from right to left, from production and customers back to development, through monitoring, testing, and review, so problems are found and fixed at the source.
3. **Continual learning and experimentation:** build a culture of trust and risk-taking, in which failures lead to learning, and improvement of daily work is as important as the work itself.

## Shared Ownership: You Build It, You Run It

A defining idea is that the team that builds a service also **operates** it. Werner Vogels, chief technology officer of Amazon, summarised it in 2006: "You build it, you run it." When developers are responsible for the production behaviour of their software, including being on call for it, they have a direct incentive to make it reliable, observable, and easy to operate, and operations knowledge spreads into design. This replaces a handover with **ownership throughout the life of the service.**

## DevOps in Practice

The practices of this unit are the means.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Practice</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Contribution to DevOps goals</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Version control for everything, including infrastructure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Shared, auditable, reproducible work</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Continuous integration</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fast feedback; integration problems found at once</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Continuous delivery and deployment</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Small, frequent, low-risk releases</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Infrastructure as code and containers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Consistent environments; repeatable operation</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Release strategies and feature flags</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Safe exposure and quick reversal</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Monitoring and observability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Feedback from production</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Blameless incident response and postmortems</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Learning from failure</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Shared tooling and platforms</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Shorter paths for every team</td>
    </tr>
  </tbody>
</table>

## Site Reliability Engineering and Platform Engineering

Two related ideas deserve mention.

- **Site Reliability Engineering (SRE)**, developed at Google and described by Ben Treynor Sloss, applies software engineering to operations. It uses service level objectives and error budgets to balance speed against reliability, limits repetitive manual work (called toil), and treats operations as an engineering discipline. It is sometimes described as one concrete way of implementing DevOps.
- **Platform engineering** builds an **internal platform** of self-service tools, templates, and automated paths, so that product teams can deploy and run software easily without each needing deep infrastructure expertise. It lowers the **cognitive load** on teams, and treats the platform as a product with developers as its customers.

## Shifting Left and DevSecOps

DevOps encourages moving checks **earlier**, or "to the left," in the flow of work: testing, performance checks, and security reviews built into the pipeline, not saved for the end. **DevSecOps** applies this to security: automated scanning of code, dependencies, and images, secrets checks, and infrastructure policy checks on every change, with security experts helping teams instead of acting as a final gate.

## Measuring DevOps

The four delivery measures of the previous chapter, deployment frequency, lead time for changes, change failure rate, and time to restore service, give a balanced picture of speed and stability. Research from the DORA programme also found that **culture predicts performance**: generative cultures with high trust and information flow, where failures lead to inquiry and not to blame, deliver better results. The research of Amy Edmondson on **psychological safety**, and an internal study at Google that identified it as the key factor in effective teams, support the same conclusion.

## Common Mistakes

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Mistake</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Why it fails</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Treating DevOps as a tool purchase</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tools do not change incentives, responsibilities, or habits</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Creating a separate "DevOps team" that sits between development and operations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Builds a new wall instead of removing one; though a platform team serving others is different</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Renaming operations staff as DevOps engineers without changing how work happens</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A label change only</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Automating a bad process</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Makes bad outcomes faster</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pursuing speed with no regard for stability or reliability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ignores the "operations" half of the idea</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Using the measures to rank or punish individuals</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Encourages gaming and destroys trust</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Leaving out security, testing, or the business</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">DevOps works end to end</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Expecting an overnight transformation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Culture changes slowly, through repeated practice and leadership support</td>
    </tr>
  </tbody>
</table>

## Starting

1. **Understand the current flow** of work from idea to production, and find where it waits.
2. **Choose one pain point,** such as slow, manual releases, and improve it.
3. **Build trust** between development, operations, security, and the business: shared goals and shared on-call.
4. **Automate** the repetitive and error-prone first.
5. **Measure** a few outcomes, and review them regularly.
6. **Share what you learn,** and celebrate improvements.
7. **Be patient,** and make leaders visible supporters.

<!--
IMAGE PROMPT  ->  generate as images/02_devops_infinity_loop_and_calms.png   (16:9 explanatory diagram, place here)

An infinity loop with left half Dev: Plan, Code, Build, Test and right half Ops: Release, Deploy, Operate, Monitor, with a feedback arrow from Monitor back to Plan. Around it the five CALMS letters with one-word captions Culture, Automation, Lean, Measurement, Sharing.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Spot the Misunderstanding

1. A company buys a set of automation tools and renames its operations group "DevOps" but keeps the same handovers and approvals.
2. A team that builds a service also carries the pager for it.
3. A manager ranks developers by the number of deployments each made.

Case 1 shows the confusion of tools and titles with culture: nothing about shared responsibility or flow has changed. Case 2 is "you build it, you run it," a core DevOps idea. Case 3 misuses a measure to judge individuals; delivery measures are about the system and should not be used to rank people, since this invites gaming.

## Conclusion

DevOps is a culture and set of practices that bring together software development and IT operations, emphasising shared responsibility, automation, fast feedback, and continuous learning, so that software can be delivered and run reliably at high speed. The tools matter, but the heart of DevOps is people working together without walls, learning from failure, and improving continuously.

This completes Unit 9. You can now explain why and how teams use version control and Git, collaborate through branches, reviews, issues, and open-source workflows, and mark releases with semantic versions. You understand how source code becomes a deployable artefact, how builds and dependencies are managed, how continuous integration and delivery keep software releasable, how environments, containers, and infrastructure as code make deployment consistent, how releases are made safely, how running systems are observed and incidents handled, and why DevOps is above all a culture. Unit 10 turns to the discipline that gives the pipeline its confidence: software testing.
