## Introduction

Software engineering is the discipline of producing software that many people use, many developers change, and that must keep working for years. It differs from programming, which is the act of producing code that works, in that it also asks whether the software can be understood, changed safely, trusted, and afforded over its whole life.

This topic defines both terms and the difference between them. Every other topic in the course builds on this distinction.

**Definition:** Software engineering is the disciplined practice of building software that many people can understand, change, trust, and rely on over a long time, while working within real limits of cost, time, and people.

<!--
IMAGE PROMPT  ->  generate as images/01_intro_what_is_software_engineering.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A single small laptop on the left grows into a large connected system of servers, teams, and users on the right, with three arrows labelled Scale, Time, People.

ON-IMAGE TEXT: show a short bold title "What Is Software Engineering" plus only these few labels, large and legible: Scale, Time, People. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Programming: Making the Computer Do What You Want

Programming is the act of writing instructions so that a computer produces a result. For a small program written and used by one person, the only question that matters is: **does it work?** The author is the only user, the only maintainer, and the only judge of success.

## What Changes When Software Grows Up

Three pressures change the problem for every piece of software that survives long enough to matter.

- **Scale.** The software grows from a single program into many parts, serving many users on many machines.
- **Time.** It must keep working next year, not just today, and it will need changes nobody has thought of yet.
- **People.** Many developers read and edit the same code, and each must understand it without asking its original author.

Once these pressures appear, "does it work?" is no longer enough. The team must also ask whether the software can be **understood**, **changed** safely, **trusted**, and **afforded**. Answering those questions is the work of software engineering.

## Programming vs Software Engineering

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Dimension</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Programming</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Software engineering</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Main question</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Does it work?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Does it keep working, and can we keep changing it safely?</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Who uses it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Usually the author</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Many users the author may never meet</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lifetime</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hours to weeks</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Years to decades</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Who works on it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One person</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Teams that change over time</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What is produced</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Code</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Code, tests, designs, documentation, releases, and a working process</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How success is judged</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The output looks right</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Requirements are met within budget and schedule, and the system stays maintainable</td>
    </tr>
  </tbody>
</table>

## A Formal Definition

The IEEE, the professional body that publishes many of the field's standards, defines software engineering as the application of "a systematic, disciplined, quantifiable approach to the development, operation, and maintenance of software." Each word carries meaning:

- **Systematic:** follow a repeatable method instead of improvising.
- **Disciplined:** keep to the method even when a deadline tempts you to skip it.
- **Quantifiable:** measure things such as defects, effort, and delivery speed, so decisions rest on evidence.
- **Development, operation, and maintenance:** the job continues after the first release, and for most successful software, maintenance is the longest phase of its life.

## Why the Word "Engineering"?

Civil engineers do not begin a bridge by pouring concrete and hoping. They gather requirements, calculate loads, compare designs, test materials, and accept responsibility for the result. Software engineers apply the same mindset to a different material.

Software is harder in some ways. It has no physical limits that force simplicity, it can be changed at almost no cost (which tempts people to change it carelessly), and its failures often stay invisible until a user meets them. Engineering discipline is how teams compensate for those properties.

## More Than Writing Code

Code is the visible output, but a software engineer's work also includes:

- talking to users and stakeholders about what they actually need
- deciding how a new feature fits into the existing design
- writing tests that prove the software behaves as intended
- reviewing teammates' work before it is accepted
- estimating effort honestly and communicating risk
- investigating production problems and recording what was learned

The decisions, conversations, and checks around the code are what make the code worth trusting.

## Your Turn: Programming Concern or Engineering Concern?

For each situation, decide whether the main concern is **programming** (making it work) or **software engineering** (making it last, scale, or be shared).

1. A student writes a one-off script to rename a folder of photos and runs it once.
2. A team of eight must decide how to split a payments feature so two people can work on it at once without breaking each other's work.
3. A developer finds that a function written two years ago is so confusing that nobody dares touch it.
4. A learner works out why a loop produces the wrong total.

Situation 1 is programming: one author, one use, no future. Situation 2 is software engineering, because it concerns people sharing a codebase. Situation 3 is software engineering, because it concerns long-term understandability and safe change. Situation 4 is programming: it is about making one piece of logic correct. Real jobs contain both. Engineering does not replace programming, it surrounds it.

## Conclusion

Software engineering is the disciplined practice of building software that many people can understand, change, trust, and rely on over a long time, while working within real limits of cost, time, and people. Programming is one essential skill inside it, but not sufficient on its own.

Every practice in this course exists because earlier teams ran into limits that programming alone could not overcome. The next topic traces how those limits were discovered and how the discipline took shape.
