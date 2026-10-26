## Introduction

Elicitation is the activity of finding out what stakeholders need. The word "elicit" is chosen carefully: requirements are not simply collected like items on a shelf, they must be drawn out, because much of what people know is unspoken, assumed, or not yet clear even to them. Skilled analysts use several techniques in combination, since each reveals different things.

**Definition:** Requirements elicitation is the set of techniques, such as interviews, surveys, observation, workshops, document analysis, and prototyping, used to discover, understand, and confirm what stakeholders need from a system.

<!--
IMAGE PROMPT  ->  generate as images/03_intro_requirements_elicitation_techniques.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A toolbox with seven labelled tools: interview, survey, observation, workshop, document analysis, prototype, brainstorm, each pointing to a glowing lightbulb labelled Needs.

ON-IMAGE TEXT: show a short bold title "Requirements Elicitation Techniques" plus only these few labels, large and legible: Ask, Watch, Try. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Why Asking Is Not Enough

People are poor reporters of their own work. They omit routine steps because these seem too obvious to mention, describe how a process should work instead of how it does, and cannot imagine possibilities they have not seen. This is the problem of **tacit knowledge**. Good elicitation combines asking, watching, and showing.

## Main Techniques

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Technique</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">How it works</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Best for</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Limitations</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Interviews</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Structured or open conversations with individuals</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Understanding goals, concerns, and detailed knowledge</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Time-consuming; people may omit tacit details or say what they think you want to hear</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Questionnaires and surveys</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Written questions sent to many people</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Gathering opinions from large groups, finding patterns</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Shallow answers; poorly worded questions mislead; no chance to follow up</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Observation and ethnography</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Watching people do their real work in their environment</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Finding what people actually do versus what they say</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Slow; observation can change behaviour</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Workshops</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Facilitated group sessions with several stakeholders</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Resolving conflicts, building shared understanding, quick decisions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dominant voices can silence others; scheduling is difficult</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Document and system analysis</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Studying forms, manuals, regulations, existing software</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Capturing rules and data, discovering existing behaviour</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Documents may be outdated or incomplete</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Prototyping</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Showing early versions or mock-ups to react to</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Clarifying uncertain requirements, testing ideas</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can focus attention on appearance rather than substance</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Brainstorming</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Generating many ideas quickly, judging later</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">New ideas, creative solutions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Needs good facilitation to be productive</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Scenarios and use cases</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Walking through concrete sequences of user activity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Revealing missing steps and exceptions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cover only the situations someone thought of</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Competitor and market analysis</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Studying similar products</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Understanding expectations and gaps</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">May copy features without understanding need</td>
    </tr>
  </tbody>
</table>

## Conducting a Good Interview

- **Prepare.** Know the person's role, the topics, and what you hope to learn.
- **Start with open questions**, such as "Can you walk me through a typical day?", then move to specifics.
- **Ask for examples and stories**, not opinions: "Tell me about the last time that happened."
- **Ask why** several times to reach the underlying need behind a stated solution.
- **Listen more than you talk**, and avoid leading questions that suggest the answer.
- **Confirm understanding** by summarising what you heard.
- **Record and follow up**, writing notes promptly and sharing them for correction.

## Solutions Disguised as Requirements

People often state a solution instead of a need: "We need a button that exports everything to a spreadsheet." An analyst asks what the person is trying to achieve. The real need might be to share monthly figures with finance, and a better solution may exist. Moving from stated solutions to underlying needs is one of the most valuable elicitation habits.

## Combining Techniques

No single method is enough. A common approach is: study existing documents first to prepare, interview key stakeholders to understand goals, observe real work to find what interviews missed, hold a workshop to reconcile differences, and build prototypes to confirm and refine understanding.

<!--
IMAGE PROMPT  ->  generate as images/02_elicitation_sequence.png   (16:9 explanatory diagram, place here)

A left-to-right sequence of five stages: Prepare (documents), Interview, Observe, Workshop, Prototype, with a feedback arrow looping from Prototype back to Interview. Under each, a small icon.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Pick the Technique

1. An analyst wants to know how nurses really use a paper form during a busy shift.
2. A project needs the opinions of 5,000 customers on possible new features.
3. A team has two departments that disagree about a process and must reach one decision.
4. A user stated a need for a screen but the team is unsure of the layout.

Case 1 calls for observation, because what people do often differs from what they report. Case 2 suits a questionnaire or survey to reach a large group. Case 3 suits a facilitated workshop with both departments. Case 4 suits prototyping, so users can react to something concrete.

## Conclusion

Requirements elicitation is the set of techniques, such as interviews, surveys, observation, workshops, document analysis, and prototyping, used to discover, understand, and confirm what stakeholders need from a system. Combining several techniques compensates for the weaknesses of each.

One of the most powerful ways to bring needs to life is to describe concrete sequences of interaction. The next topic introduces use cases and scenarios.
