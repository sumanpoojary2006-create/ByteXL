## Introduction

At nine on a Sunday morning, Karthik's uncle forwards a message to the family group. It says that AI has now become smarter than humans, that it will replace all jobs within eighteen months, and that a well-known company has secretly built a machine that thinks. Below it, three relatives have already replied with folded-hands stickers.

Karthik is fairly sure this is wrong. What bothers him is that he cannot say precisely why. He knows ChatGPT writes better emails than he does. He knows a program beat the world's best Go player. He also knows that the same ChatGPT confidently invented a case citation for his cousin's law assignment, and that the Go program cannot play chess, or order groceries, or do anything at all except play Go. All of these facts are true at once, and Karthik has no vocabulary that holds them together.

That vocabulary exists, and it is one of the most practically useful things in this entire course. Instead of asking the unanswerable question "is this thing intelligent", classify it by how *broad* its competence is. This gives three **types of artificial intelligence**, and once you have them, family group arguments and newspaper headlines both become much easier to assess.

**Definition:** The `types of artificial intelligence` classify systems by the breadth of their capability rather than the technique inside them: `Artificial Narrow Intelligence` performs one task or a narrow set of related tasks, `Artificial General Intelligence` would match human flexibility across any intellectual task, and `Artificial Super Intelligence` would exceed the best human performance in essentially every domain.

![Opening scene: At nine on a Sunday morning, Karthik's uncle forwards a message to the family group.](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_section_introduction.png)

## A Different Way of Slicing the Field

It is worth being clear about how this classification differs from the branches, because students routinely mix the two up.

Branches slice AI by **the kind of problem being solved**: vision, language, planning, robotics. A system belongs to a branch based on what it works on. Types slice AI by **how much the system can do**: one narrow thing, everything a human can do, or more than any human can do. A system belongs to a type based on the scope of its competence.

The two are independent. A computer vision system and a language system sit in different branches while belonging to the same type. That is why this second classification earns its place: it answers the question the branches cannot, which is how close any of this is to the thing people imagine when they hear the words artificial intelligence.

![Visual explanation of a different way of slicing the field](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_section_a_different_way_of_slicing_the_field.png)

## Artificial Narrow Intelligence: Everything That Exists Today

`Artificial Narrow Intelligence`, usually shortened to ANI and sometimes called weak AI, is a system built to perform one task or one tightly bounded family of tasks.

Start with the sentence that matters most in this lesson: **every AI system that has ever been built, without exception, is narrow AI.** Your spam filter, your bank's fraud model, the face unlock on your phone, every self-driving car on every road, every image generator, and every large language model. All of them. There is no exception waiting in a laboratory somewhere.

The word "weak" is badly chosen and causes real confusion, so discard it. Narrow does not mean feeble. A narrow system can be wildly superhuman inside its band. No human will ever beat the strongest chess engine again. No radiologist can screen ten thousand scans before lunch. AlphaGo did not lose to Lee Sedol because it was weak; it beat him four games to one and played at least one move that professional commentators initially assumed was a mistake and later described as beautiful.

The correct reading of "narrow" is about **width, not height**. These systems are extraordinarily tall within a very thin column, and there is nothing at all outside the column.

![Visual explanation of artificial narrow intelligence: everything that exists today](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_section_artificial_narrow_intelligence_everything_that_exists_today.png)

## Why Narrow Systems Break Outside Their Band

Understanding *why* the column has walls is what separates a student who has memorised three acronyms from one who can actually evaluate a claim.

Three limitations do the work.

1. **Absence of transfer.** A human who learns chess acquires something portable: patience, planning several steps ahead, reading an opponent's intentions. A chess engine acquires nothing portable at all. Its competence is entirely bound to the representation it was trained on, which is why a Go program cannot play chess despite the two games sharing so much of their strategic character.

2. **Absence of a world model.** A large language model can produce a fluent paragraph about a glass of water tipping over a laptop without possessing any physical understanding of liquid, gravity, or electronics. It has learned how sentences about such events tend to continue. This is a real capability, and it is not the same thing as understanding, which is exactly why such a system can be simultaneously articulate and confidently wrong. The invented legal citation in Karthik's cousin's assignment is not a bug in an otherwise knowledgeable system; it is what fluency without grounding looks like.

3. **Absence of self-directed goals.** Every narrow system optimises an objective its designers chose. It cannot decide that the objective is misguided, notice that a more important problem exists, or invent a new task for itself. It will pursue the given target with total commitment and no judgment about whether the target is worth pursuing.

![Visual explanation of narrow ai brittleness](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_narrow_ai_brittleness.png)

## Artificial General Intelligence: The Open Problem

`Artificial General Intelligence`, or AGI, is a hypothetical system that could understand, learn, and apply knowledge across any intellectual task a human can perform, transferring what it learns from one domain to another.

Note the word in the definition doing all the work: **any**. Not "many tasks", not "most tasks a knowledge worker does", but the open-ended flexibility of a reasonably capable adult who can be taught a new job. Such a system would need to:

- Learn a genuinely new skill from a handful of examples.
- Carry insight from one field into an unrelated one.
- Hold a working model of how the physical and social world behaves.
- Know the boundaries of its own knowledge.
- Set sensible subgoals of its own.

No such system exists, and honest researchers disagree sharply about whether current approaches will produce one. A crucial and often missed point is that AGI may not be simply a larger version of what we have now. Scaling has produced repeated surprises over the past decade, so dismissing it would be foolish. But the three limitations above are not obviously the kind of problem that more data fixes, and several serious researchers argue that a new idea, not a bigger model, is what is missing.

![Visual explanation of artificial general intelligence: the open problem](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_section_artificial_general_intelligence_the_open_problem.png)

## Artificial Super Intelligence: The Hypothetical Beyond

`Artificial Super Intelligence`, or ASI, is a hypothetical system that would surpass the best human performance in virtually every domain, including scientific creativity, strategic judgment, and social skill.

This is the territory of serious philosophical work and of a great deal of unserious speculation, and the two are worth keeping apart. The serious version argues that a system able to improve its own design might improve rapidly and repeatedly, and that ensuring such a system's goals remained aligned with human interests would be a genuinely hard technical problem worth beginning early. The unserious version is the WhatsApp forward.

For your purposes as a student, hold two things at once. ASI is entirely hypothetical, separated from today's systems by AGI, which does not exist either, so treating it as imminent is not supportable. And it is not a silly topic, because the question of how to keep a highly capable system's objectives aligned with what we actually want is already a live engineering concern in systems that exist right now.

![Visual explanation of artificial super intelligence: the hypothetical beyond](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_section_artificial_super_intelligence_the_hypothetical_beyond.png)

## The Three Types at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Type</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Scope of capability</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Status</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Defining limitation</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>ANI</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One task or a narrow family of related tasks, sometimes at superhuman level</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Every system that exists today</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No transfer, no world model, no goals of its own</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>AGI</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Any intellectual task a human can do, with transfer between domains</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Does not exist; timeline genuinely disputed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No agreed definition, and therefore no agreed test</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>ASI</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Exceeds the best humans in essentially every domain</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Entirely hypothetical, beyond AGI</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keeping its objectives aligned with human interests</td>
    </tr>
  </tbody>
</table>

![Visual explanation of types of ai](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_types_of_ai.png)

## Three Familiar Systems Placed on the Scale

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">System</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Type</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Why it sits there</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>AlphaGo</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">ANI, superhuman and extremely narrow</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Beat the world's best at Go and can do literally nothing else, not even a simpler board game</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>ChatGPT</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">ANI, unusually broad</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Handles a huge range of language tasks, yet cannot perceive the world, learn permanently from a conversation, or reliably know when it is wrong</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>JARVIS</strong> (fictional)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">AGI, arguably approaching ASI</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Converses, reasons about physics, runs engineering analysis, controls hardware, takes initiative, and moves between all of these without being retrained</td>
    </tr>
  </tbody>
</table>

ChatGPT is the interesting row, because it is the one that makes people hesitate, and their hesitation is reasonable. It is far broader than any previous narrow system, and breadth was supposed to be the AGI signature. But breadth within language is not the same as generality across the world. The gap shows up the moment you ask it to remember something permanently, act on a live physical situation, or say honestly that it does not know.

![Visual explanation of three familiar systems placed on the scale](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_section_three_familiar_systems_placed_on_the_scale.png)

## Is Today's AI Approaching AGI?

This deserves a real answer rather than a dismissal, because the case on both sides is stronger than partisans of either admit.

**The case that we are getting closer.**

- **Breadth without task-specific training.** Today's largest models perform competently across translation, code, summarising, mathematics, and analysis, without being separately built for each. That is a qualitatively different profile from a chess engine.
- **Capabilities appearing with scale.** Abilities have repeatedly shown up in larger models that were not present in smaller ones and were not deliberately engineered.
- **Multimodality.** Systems now take in images, audio, and text together, which begins to address the grounding complaint.
- **Something resembling goal pursuit.** Agent systems plan, call tools, and act over several steps.

**The case that we are not.**

- **No learning after deployment.** Close the conversation and everything is gone, whereas a human intern improves every week.
- **Confident falsehoods.** There is no mechanism for tracking what is true as opposed to what is plausible.
- **Persistent brittleness.** Small rephrasings of a problem can flip a correct answer into a wrong one, exactly as with earlier narrow systems.
- **Untrustworthy benchmarks.** Material resembling the test may sit somewhere in the training data.
- **The goals are still entirely ours.** Nothing in these systems sets its own objectives.

**Why the argument does not resolve.** There is no agreed definition of AGI and therefore no agreed test for it. The Turing test, proposed in 1950, has effectively been passed by systems nobody considers generally intelligent, which tells you the test was measuring the wrong thing. Until the field agrees on what would count as evidence, both sides can look at the same system and see confirmation.

The defensible position, and the one to take into any argument, is this: current systems are the broadest narrow AI ever built, the distance to genuine generality is real and not merely a matter of scale, and anyone who tells you they know the timeline with confidence is telling you about their temperament rather than about the technology.

![Visual explanation of is today's ai approaching agi?](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_section_is_today_s_ai_approaching_agi.png)

## Your Turn

Go back to Karthik's family group message and write the reply he could not. In four sentences, use the three types to explain what is true in the forward, what is false, and what is simply unknowable at present.

Then take the harder challenge. Pick the AI system you personally find most impressive, and construct the strongest possible argument that it is approaching AGI, using the case in this lesson. Then construct the strongest possible argument that it is not. Write both, at similar length, without letting your preferred conclusion make one of them lazy. The point of the exercise is not to reach a verdict. It is that being able to argue both sides of a genuinely open question is the difference between having an opinion about AI and understanding it.
