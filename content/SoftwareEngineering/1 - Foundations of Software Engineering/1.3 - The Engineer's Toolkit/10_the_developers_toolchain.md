## Introduction

Professional software is built with a connected set of tools: an editor to write code, a system to record every change, a mechanism to run checks automatically, and a pipeline to deliver the result. The arrangement of these tools matters more than the choice of any one of them, because it should give every team member the same result.

This topic describes the main categories of tools, shows how one change travels through them, and introduces the idea of a reproducible environment.

**Definition:** A toolchain is the set of connected tools a developer uses to write, build, test, version, and deliver software, arranged so that the same steps give the same result on every machine.

<!--
IMAGE PROMPT  ->  generate as images/10_intro_the_developers_toolchain.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A conveyor of glowing tool icons, an editor, version control, a terminal, a test runner, and a pipeline, feeding into a single running application.

ON-IMAGE TEXT: show a short bold title "The Developers Toolchain" plus only these few labels, large and legible: Editor, Version, Pipeline. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Main Categories of Tools

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Category</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Common examples</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Editor or IDE</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Write and navigate code, with hints and debugging</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Visual Studio Code, PyCharm, IntelliJ IDEA</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Language runtime or compiler</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Turn source code into something that runs</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Python interpreter, Java JDK, Node.js</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Package manager</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Download and track the libraries a project depends on</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">pip, npm, Maven</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Version control</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Record every change, support collaboration and rollback</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Git with GitHub or GitLab</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Terminal / shell</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Run commands, scripts, and tools quickly</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">bash, zsh, PowerShell</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Test runner</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Run automated checks on the software</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">pytest, JUnit, Jest</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Linter and formatter</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Catch likely mistakes and keep style consistent</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ruff, ESLint, Prettier</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Debugger</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pause a running program and inspect its state</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Debuggers built into editors</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Issue tracker</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Record bugs, tasks, and who is doing what</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">GitHub Issues, Jira, ClickUp</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">CI/CD pipeline</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Build, test, and deploy automatically on every change</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">GitHub Actions, GitLab CI, Jenkins</td>
    </tr>
  </tbody>
</table>

## Following One Change Through the Tools

1. A team member picks a task from the **issue tracker**.
2. They create a separate line of work in **version control**, so the main code stays untouched.
3. They edit in the **editor**, and the **linter** flags likely mistakes as they work.
4. They run the **tests**, using the **debugger** to investigate any failure.
5. They record the change and share it through version control.
6. The **CI pipeline** builds the software and runs all the tests automatically on a clean machine.
7. A teammate **reviews** the change, and once approved it is merged.
8. The pipeline **deploys** the new version.

## Reproducible Environments

"It works on my machine" is the classic symptom of a missing toolchain discipline. Machines differ: one has a newer library, another a different language version. The remedy is to **declare** what a project needs and install it from that declaration. Two ideas do the work:

- **Declared dependencies:** a file lists every library and version the project needs, so nobody relies on memory.
- **Isolated environments:** each project gets its own separate set of libraries, so projects on the same computer do not interfere with one another.

Anyone who follows the project's setup instructions on a fresh machine should reach the same working state. If they do not, the instructions are broken, and repairing them is real engineering work.

## Tool Choices: What to Standardise

A common beginner mistake is to treat the choice of tool as the main decision. What matters is that the team **agrees** on the shared parts, because those must be identical for everyone: the language version, the formatter settings, the test procedure, and the build steps. Personal choices such as editor theme or shell can vary freely.

## Your Turn: Which Tool?

Which category of tool addresses each problem?

1. Two developers keep overwriting each other's changes to the same file.
2. A project works for one developer but fails for another because of different library versions.
3. Arguments about code style consume time in every review.
4. Nobody remembers to run the tests before merging, and a broken change reached users last week.

Problem 1 needs version control. Problem 2 needs declared dependencies and isolated environments, handled by a package manager. Problem 3 needs a formatter and linter with agreed settings, checked automatically. Problem 4 needs a CI pipeline that runs the tests on every change so that nobody has to remember.

## Conclusion

A toolchain is the set of connected tools a developer uses to write, build, test, version, and deliver software, arranged so that the same steps give the same result on every machine. Tools are not a distraction from the real work, they are how teams make good work repeatable.

One tool underlies many of the others and is the main way into servers: the terminal. The next topic explains the ideas behind the command line.
