## Introduction

Anjali is setting up a smart home system for her parents' flat, and it takes her about an hour to hit a wall that is far more interesting than the product manual suggests.

She wants one thing: the geyser should switch on before her father's bath. The app offers her a timer, so she sets it for six in the morning. On Sunday her father sleeps until nine and the geyser has been holding forty litres of water hot for three hours. She switches to a motion trigger in the bathroom, which turns the geyser on when he is already standing in the bathroom and wants water now, not in twelve minutes.

What Anjali actually knows is something like this: her father bathes shortly after he wakes, he wakes around six on weekdays and later on Sundays, the geyser needs twelve minutes, and heating water nobody uses is a waste. The system has no way to hold any of that. It can hold a time, or a sensor event. She has plenty of knowledge and no way to write it down that the machine can use.

That gap is the subject of this lesson. Before a system can reason, someone must decide what a piece of knowledge looks like when written down, and that decision is called **knowledge representation**.

**Definition:** `Knowledge representation` is the study of how to encode what a system knows in a form a machine can store and reason over, choosing structures that capture the domain accurately while remaining efficient to use and practical to build.

![Visual explanation of introduction](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_section_introduction.png)

## Facts, and Why They Are Not Enough

The simplest unit is a `fact`: a single piece of information asserted to be true right now.

The water heater is off. The bathroom light is on. It is 06:10. The outside temperature is 22 degrees.

Facts are indispensable and, on their own, inert. A thousand facts about Anjali's flat let a system report the current state and do nothing else, because nothing in a list of facts says what follows from what. Knowing the geyser is off does not tell you whether it should be on.

Notice also that facts have a lifespan. "The bathroom light is on" is true for eleven minutes. "The geyser holds forty litres" is true until somebody replaces it. Systems usually separate these, keeping volatile facts about the current situation apart from stable facts about how the world is arranged, which is the same split between working memory and the knowledge base that a knowledge-based system makes.

![Visual explanation of facts, and why they are not enough](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_section_facts_and_why_they_are_not_enough.png)

## Declarative Knowledge: Knowing That

`Declarative knowledge` states what is true about the world, without saying how to use it.

- Water heated above 60 degrees can scald.
- Anjali's father bathes shortly after waking.
- The geyser takes twelve minutes to reach temperature.
- Sunday is not a working day.

Each of these is a claim, standing on its own, meaningful without reference to any procedure. That independence is the source of its value. A declarative statement can be used for many different purposes by many different procedures: the twelve-minute heating time can be used to schedule the geyser, to warn a guest that hot water is not available yet, or to estimate the flat's electricity bill. Nobody had to anticipate those uses when writing it down.

Declarative knowledge is also inspectable and correctable. If the geyser is replaced with a faster one, someone changes twelve to seven, and every use of that number updates at once.

![Visual explanation of declarative vs procedural](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_declarative_vs_procedural.png)

## Procedural Knowledge: Knowing How

`Procedural knowledge` specifies how to do something: a sequence of steps that achieves a result.

To prepare hot water for a bath: check the tank level, switch on the heating element, wait until the thermostat reports 55 degrees, and then switch off the element.

This is knowledge too, and for many tasks it is the only practical form. It is fast, because the procedure is already worked out and does not have to be derived. It captures skill that resists being stated as claims, which is exactly the difficulty Ramesh's manager ran into in the previous lesson.

Its weakness is the mirror image of its strength. A procedure is opaque, in that you cannot ask it what it believes, only run it and watch. It serves one purpose, so knowledge locked inside a heating routine cannot be reused by the billing estimate. And it is hard to modify safely, because changing one step can break assumptions made by later steps.

![Visual explanation of procedural knowledge: knowing how](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_section_procedural_knowledge_knowing_how.png)

## The Distinction Is an Engineering Decision

Here is the point most treatments of this topic miss. Declarative and procedural are not two kinds of knowledge that exist in nature. **They are two ways of encoding the same knowledge, and choosing between them is a design decision with consequences.**

Take the single piece of knowledge that the geyser needs twelve minutes. Encoded declaratively, it is a stated duration that any part of the system can consult. Encoded procedurally, it is a `wait(12)` buried inside a heating routine. The knowledge is identical. What differs is everything else about it.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Property</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Declarative</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Procedural</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Form</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Statements that are true or false</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Steps that are carried out</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reuse</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Any procedure can consult it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Serves the one purpose it was written for</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Inspection</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can be read and checked by a domain expert</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can only be run and observed</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Speed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Slower, since the use must be derived</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Faster, since the use is already decided</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Change</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Edit one statement, every use updates</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Edit the steps, and hope nothing downstream assumed otherwise</td>
    </tr>
  </tbody>
</table>

The working guideline that falls out of this table: **encode declaratively whatever is likely to change or to be needed for more than one purpose, and procedurally whatever is fixed, performance-critical, and used in exactly one way.** Anjali's father's waking habits belong in the first category. The sequence of electrical operations that safely switches an element on belongs in the second.

![Visual explanation of the distinction is an engineering decision](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_section_the_distinction_is_an_engineering_decision.png)

## What a Good Representation Must Do

A representation scheme is judged on four criteria, and they pull against each other, which is why no single scheme has ever won.

1. **Representational adequacy.** Can it express everything the domain requires? A scheme that can record "the geyser is on" but cannot record "the geyser is usually on by seven" has failed before reasoning begins.

2. **Inferential adequacy.** Can new knowledge be derived from what is stored? A representation that holds facts but supports no derivation is a database, not a knowledge base.

3. **Inferential efficiency.** Can the derivation be done quickly enough to be useful? Highly expressive schemes tend to be slow to reason with, and this trade-off between expressiveness and tractability is the central tension of the whole field.

4. **Acquisitional efficiency.** Can the knowledge be got into the system at reasonable cost? A beautiful scheme that requires a logician three days per rule will never be populated.

Read those four together and the pattern is clear. Gains on the first two are usually paid for on the second two. A representation rich enough to say anything is generally too slow to reason with and too laborious to fill, which is why practical systems choose a scheme barely expressive enough for their domain and no more.

![Visual explanation of good representation smart home](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_good_representation_smart_home.png)

## Representing Anjali's Smart Home

Applying all of this, here is what her system would need to hold, sorted by kind.

| Kind | Example | Why this kind |
| --- | --- | --- |
| Volatile fact | The bathroom light is on | Changes minute to minute; belongs in working memory |
| Stable fact | The geyser holds 40 litres | A property of the flat, true until the hardware changes |
| Declarative rule | If someone is likely to bathe within 15 minutes, the geyser should be on | Reusable, and readable by Anjali when it misbehaves |
| Declarative pattern | Her father wakes around 06:00 on weekdays, later on Sundays | Likely to change; must be editable without touching code |
| Procedure | The safe sequence for switching the heating element on | Fixed, performance-critical, single purpose |
| Constraint | Water must never exceed 60 degrees | A rule that may never be violated, whatever else is inferred |

That last row is worth noticing, because it is a different sort of statement from the others. Most knowledge in a system suggests what to conclude. A constraint states what may never be true regardless of what anything else concludes, and separating the two is what stops a system reasoning its way to a dangerous action.

![Visual explanation of representing anjali's smart home](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_section_representing_anjali_s_smart_home.png)

## The Hardest Part Is What You Leave Out

Two problems appear the moment a representation is written down, and both are worth meeting now, because they never go away.

**What does silence mean?** Anjali's system holds no fact saying her mother is at home. Does that mean her mother is out, or that nobody has checked? Under the `closed-world assumption`, anything not known to be true is taken as false, which is convenient, keeps the knowledge base small, and is exactly what a railway timetable enquiry does when it says no such train exists. Under the open-world assumption, absence means unknown, which is honest and much harder to reason with. Neither is correct in general; the designer must choose, and must know which one they chose.

**What stays the same when something changes?** When the geyser switches on, the bathroom light does not change, the outside temperature does not change, and the flat's address does not change. Obvious to a person, and not obvious to a machine, which in principle must be told that each action leaves everything else alone. Stating all of that explicitly is impossible, and the difficulty of specifying what does *not* change is known as the `frame problem`. Practical systems dodge it by assuming that anything an action does not explicitly alter is unaffected, which works well and is a convention rather than a discovery.

Both problems have the same shape, and it is the shape of this whole subject: **a representation is defined as much by what it deliberately leaves unsaid as by what it records.**

![Visual explanation of the hardest part is what you leave out](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_section_the_hardest_part_is_what_you_leave_out.png)

## Your Turn

Represent a college library for a system that answers member questions, and do it in the four categories used above: volatile facts, stable facts, declarative rules, and procedures.

Write at least three entries in each category. Then apply the four criteria. Ask whether your representation can express "a book is overdue only if the borrower has not renewed it and the library was open on the due date", and if it cannot, say which criterion has failed.

Then confront the closed-world assumption directly. Your system has no record that a particular student has returned a book. Write down what your system will therefore conclude, and what it should conclude, and if those differ, decide what extra thing you must record to close the gap. Most people discover they need to distinguish "recorded as not returned" from "no record either way", and that discovery is the entire lesson: representation choices are not neutral, and the wrong one produces a system that is confidently wrong about a student who did nothing wrong.
