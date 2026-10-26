## Introduction

Software is invisible. A building can be walked through and a bridge can be seen from a distance, but the structure of a program exists only in text and in the heads of the people who wrote it. To discuss, check, and agree a design before it is built, engineers draw pictures. These pictures are called models, and the Unified Modeling Language (UML) is the most widely used notation for them.

This topic explains why modeling is worth the effort, what a model is and is not, the ways teams use models in practice, and how UML is organised.

**Definition:** A software model is a simplified representation of some aspect of a system, expressed in text or diagrams, that helps people understand, discuss, evaluate, and communicate it without needing to read every detail of the code.

<!--
IMAGE PROMPT  ->  generate as images/01_intro_why_model_software.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A complex tangled structure on the left being simplified into a clear labelled diagram on the right, with a magnifying glass between them labelled Abstraction.

ON-IMAGE TEXT: show a short bold title "Why Model Software" plus only these few labels, large and legible: Simplify, Show, Share. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## What a Model Is

A model is an **abstraction**: it keeps what matters for a particular purpose and leaves out the rest. A map of a metro network shows stations and connections but not street layouts, because its purpose is planning journeys. A software model likewise shows only the aspect under discussion, such as the main classes and their relationships, or the order of messages in one scenario.

Because models omit detail on purpose, no single model describes a whole system. Different views answer different questions.

## Why Teams Model

- **Understanding.** Drawing a problem forces clarity. Gaps and contradictions that hide in prose appear in a diagram.
- **Communication.** A diagram can be read by developers, testers, and stakeholders with different backgrounds, and it gives a shared vocabulary.
- **Exploring alternatives cheaply.** Changing a sketch costs minutes. Changing built software costs days.
- **Early checking.** Reviewers can find design flaws before anything is coded.
- **Documentation.** Models record structure and intent for people who join later.
- **Reasoning about complexity.** Large systems cannot be held in one head; models provide manageable views.

## What UML Is

The Unified Modeling Language was created in the 1990s when three leading methodologists, Grady Booch, Ivar Jacobson, and James Rumbaugh, combined their separate notations. It was adopted as a standard by the Object Management Group in 1997 and later published as an international standard. UML is a **language for expressing models**, not a process: it does not say how to develop software, only how to draw and describe it.

UML 2 defines fourteen diagram types, divided into two families.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Family</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Diagram types</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Structure diagrams</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Show what the system is made of: parts and relationships that exist regardless of time</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Class, object, component, composite structure, deployment, package, profile</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Behaviour diagrams</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Show what the system does and how it changes over time</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use case, activity, state machine</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Interaction diagrams (a kind of behaviour diagram)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Show how parts exchange messages</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sequence, communication, timing, interaction overview</td>
    </tr>
  </tbody>
</table>

Most practising teams regularly use only a handful: use case, class, sequence, activity, state machine, component, and deployment diagrams. These are the focus of this unit.

## Three Ways to Use Models

Martin Fowler describes three modes of using UML, which are useful for deciding how much effort a diagram deserves.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Mode</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Purpose</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Level of detail</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical form</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sketch</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Communicate ideas and explore options in a discussion</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Selective, informal</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Whiteboard, quick drawing, thrown away afterwards</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Blueprint</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Specify design in enough detail that others can implement it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Complete and precise</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Maintained diagrams or documents</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Programming language</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Generate software directly from the model</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Executable, fully specified</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Specialised model-driven tools</td>
    </tr>
  </tbody>
</table>

Most agile teams use UML as sketches: just enough drawing to think and communicate. Blueprint use appears in regulated or large-scale work. Fully executable models remain rare in general practice.

## Principles of Good Modeling

- **Have a purpose.** Decide what question the diagram answers and who will read it.
- **Choose the right level of abstraction.** Too much detail hides the point, too little says nothing.
- **Keep models consistent** with each other and with the code.
- **Use several views.** Structure, behaviour, and deployment each need their own diagram.
- **Iterate.** Models are improved as understanding grows.
- **Avoid modeling for its own sake.** A diagram nobody uses is waste.

## Risks

Modeling can go wrong: heavy up-front diagramming that is never updated, treating diagrams as proof the software is correct, and models so detailed that they duplicate the code with none of its checks. The remedy is to model to the point where the understanding is gained, and then to stop.

<!--
IMAGE PROMPT  ->  generate as images/02_uml_diagram_families.png   (16:9 explanatory diagram, place here)

A tree with UML at the top and two branches: Structure (class, component, deployment) and Behaviour (use case, activity, state machine, with an Interaction sub-branch containing sequence). Small thumbnails of each diagram type sit at the leaves.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Which View?

Choose the family and a suitable diagram for each question.

1. Which parts make up the system, and how are they related?
2. In what order do objects exchange messages when a customer places an order?
3. What can a user do with the system?

Question 1 asks about structure and is answered by a class or component diagram. Question 2 asks about behaviour over time and is answered by a sequence diagram. Question 3 asks about goals and users, and is answered by a use case diagram.

## Conclusion

A software model is a simplified representation of some aspect of a system, expressed in text or diagrams, that helps people understand, discuss, evaluate, and communicate it without needing to read every detail of the code. UML provides a shared notation, and good modeling is purposeful, selective, and kept as light as the situation allows.

We begin with the diagram that shows what users want to do. The next topic describes use case diagrams.
