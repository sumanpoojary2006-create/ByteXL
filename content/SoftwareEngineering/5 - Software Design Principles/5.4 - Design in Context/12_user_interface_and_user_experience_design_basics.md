## Introduction

All the design principles so far concern the inside of software. Yet most people judge software by what they see and do: how easily they find a function, how clearly the system tells them what happened, how it treats mistakes. A technically excellent system with a confusing interface will be considered poor, and may not be used at all. Designing for the people who use software is therefore an engineering concern, not a cosmetic one.

**Definition:** User interface design is the design of the visible and interactive parts of a system through which people operate it, and user experience design is the broader practice of shaping the whole of a person's interaction with a product so that it is useful, usable, and satisfying.

<!--
IMAGE PROMPT  ->  generate as images/12_intro_user_interface_and_user_experience_design_basics.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A progression of three drawings from left to right: a user journey sketch, a wireframe of a screen with labelled blocks, and a polished interface, with a person testing the middle one.

ON-IMAGE TEXT: show a short bold title "User Interface and User Experience Design Basics" plus only these few labels, large and legible: Journey, Wireframe, Test. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## UI and UX

The two terms are related but distinct.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Term</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Concern</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Questions it answers</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">User interface (UI)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The look and interactive elements of the product: layout, controls, text, colour, feedback</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What do users see and touch? Is it clear and consistent?</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">User experience (UX)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The entire experience of using the product, including goals, tasks, emotions, and context</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Does it help the person achieve their goal easily and pleasantly?</td>
    </tr>
  </tbody>
</table>

Interface design is one part of experience design. A beautiful interface can still give a poor experience if it supports the wrong tasks or demands too much effort.

## Start With Users and Tasks

Good design begins with understanding **who** the users are, **what** they are trying to do, and **in what context**: a person ordering lunch on a phone while queuing has different needs from an administrator preparing a weekly report at a desk. Techniques include interviews and observation, **personas** that summarise typical users, and **user journeys** that map the steps a person takes toward a goal, including their feelings and problems at each step. These connect to the requirements work of Unit 3.

## Usability Heuristics

Jakob Nielsen proposed ten general guidelines, widely used to inspect interfaces.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Heuristic</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Visibility of system status</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keep users informed about what is happening</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A progress indicator while an order is being placed</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Match between system and the real world</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use the user language and concepts</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"Basket" and "checkout," not internal terms</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">User control and freedom</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Provide ways to undo and escape</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A cancel option, an undo for deletion</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Consistency and standards</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Same words and actions mean the same thing everywhere</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Buttons that behave alike on every screen</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Error prevention</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Design to prevent mistakes before they happen</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Disable the pay button until required details are filled in</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Recognition rather than recall</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Make options visible instead of making users remember</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Show recent orders for re-ordering</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Flexibility and efficiency of use</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Serve both new and expert users</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Shortcuts for frequent actions</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Aesthetic and minimalist design</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Show only relevant information</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Do not crowd screens with rarely used items</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Help users recognise, diagnose, and recover from errors</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Plain-language messages that explain the problem and a remedy</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"Card declined. Try another card or contact your bank."</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Help and documentation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Provide concise, searchable help when needed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Short tips in context</td>
    </tr>
  </tbody>
</table>

## Principles from Everyday Design

Don Norman, in studies of everyday objects, described ideas that apply equally to software.

- **Affordances and signifiers:** an element should suggest how it can be used, such as a button that looks pressable.
- **Feedback:** every action should produce a visible, immediate response.
- **Mapping:** controls should relate naturally to their effects.
- **Constraints:** limiting the possible actions prevents errors.
- **Conceptual model:** users build a mental picture of how the system works, and the design should support a correct one.

## The Design Process

1. **Research** users and their tasks.
2. **Define** the problems and the flows that matter most.
3. **Sketch** ideas quickly on paper or whiteboard.
4. **Build wireframes,** simple layouts showing the structure of screens without visual styling, and **prototypes** that can be clicked through.
5. **Test with real users,** watching them attempt tasks, noting where they hesitate or fail.
6. **Refine,** and repeat.

Usability testing is the most reliable method. Even a small number of participants in a round, around five, typically reveals a large share of the main problems, and repeated small rounds work better than one large one. What users **do** is more informative than what they say they would do.

## Accessibility

An interface should be usable by people with a wide range of abilities, including those with visual, hearing, motor, or cognitive differences, and those using assistive technology. The Web Content Accessibility Guidelines (WCAG) organise requirements under four principles: content must be **perceivable**, **operable**, **understandable**, and **robust**. Practical examples include sufficient contrast between text and background (at least 4.5 to 1 for normal text at level AA), text alternatives for images, operation by keyboard alone, and clear labels on form fields. Accessibility is a requirement in many countries, and designing for it helps everyone: captions are used in noisy places and clear contrast helps in bright sunlight.

## Common Interface Problems

- Hidden or unclear navigation
- Too many choices at once, which slows decisions (Hick's law notes that decision time grows with the number of options)
- Small or distant targets that are hard to hit (Fitts's law relates time to reach a target to its size and distance)
- Inconsistent terms and behaviour
- Error messages that blame the user or say nothing helpful
- Forms that demand too much information
- Designs tested only on the team, who already know how things work

<!--
IMAGE PROMPT  ->  generate as images/02_wireframe_and_usability_heuristics.png   (16:9 explanatory diagram, place here)

A simple wireframe of an ordering screen with numbered callouts pointing to elements and matching labelled heuristics: status indicator, familiar words, cancel link, consistent buttons, error prevention, clear error message. A small user-test scene beside it with an observer taking notes.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Apply the Heuristics

1. A user submits an order and the screen shows nothing for ten seconds.
2. An error message reads "Error 4032."
3. A form clears all fields when one entry is invalid.

Case 1 violates visibility of system status; the system should show that the order is being processed. Case 2 violates the guideline on error messages: it should say in plain language what went wrong and how to fix it. Case 3 violates error prevention and user control: a good form keeps valid entries and highlights only the problem.

## Conclusion

User interface design is the design of the visible and interactive parts of a system through which people operate it, and user experience design is the broader practice of shaping the whole of a person's interaction with a product so that it is useful, usable, and satisfying. Understanding users, applying proven heuristics, and testing with real people matter more than visual polish.

This completes Unit 5. You can now explain what software design is, how abstraction, information hiding, modularity, cohesion, and coupling shape a structure, how encapsulation and interfaces control change, how SOLID and other heuristics guide choices, how design by contract states obligations, how to design for change and judge design quality, and how to design for the people who use software. Unit 6 builds on these foundations at a larger scale, with software architecture.
