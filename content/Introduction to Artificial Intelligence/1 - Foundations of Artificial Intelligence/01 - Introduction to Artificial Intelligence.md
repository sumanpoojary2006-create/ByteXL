## Introduction

Ananya leaves her hostel at 8:40 in the morning, plugs the college address into Google Maps, and starts riding. Four minutes later, at a junction she has crossed a hundred times, the app quietly reroutes her down a narrow side lane she has never taken. She is mildly annoyed, until she reaches college on time and hears that a lorry had broken down on her usual road at 8:43.

Sit with that for a second. Nobody typed "lorry broken down on Kanakapura Road" into the app, and no engineer at Google was watching that junction. The app noticed that hundreds of phones on that stretch had slowed from 40 kilometres per hour to walking pace, concluded that something was blocking the road, worked out that the side lane would now be faster, and changed its recommendation, all in the seconds before Ananya arrived at the turn.

Think about what that required. The system had to take in information about the world, work out what that information meant, weigh several routes against a goal, and commit to an action. If a traffic constable had done the same thing, standing at that junction waving riders down the side lane, nobody would hesitate to call it intelligent behaviour. That is the entire idea behind **artificial intelligence**: building systems that carry out tasks which, if a person did them, we would happily describe as requiring intelligence.

**Definition:** `Artificial Intelligence` is the field of building computational systems that perceive their environment, reason about what they perceive, learn from experience, and act to achieve goals in situations their designers did not individually anticipate.

![Visual explanation of intro ai rerouting story](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_intro_ai_rerouting_story_draft.png)

## What We Mean When We Say Intelligence

Before defining artificial intelligence, it is worth being honest about the harder half of the phrase. `Intelligence` is not one skill. It is a bundle of capabilities that we recognise most clearly when someone handles a situation they have never faced before.

A pocket calculator multiplies two twelve-digit numbers faster and more reliably than any human alive, and nobody calls it intelligent. A three-year-old cannot multiply at all, yet she can look at a photograph of a dog she has never seen, in a breed she has never encountered, from an angle she has never been shown, and say "dog". She generalises from a handful of examples to an endless variety of new cases. That is the thing calculators cannot do, and the thing the field of AI has spent seventy years chasing.

So when researchers talk about intelligence, they are pointing at a cluster of five abilities:

- **Perceiving** the world through some form of senses.
- **Learning** from experience, rather than being told everything in advance.
- **Reasoning** from what is known to what must follow.
- **Coping with ambiguity**, where the information available is incomplete or unclear.
- **Choosing actions** that move towards a goal.

Notice that speed and storage are not on that list. A system can be extraordinarily fast and hold enormous amounts of data while showing no intelligence whatsoever, and this distinction is the foundation everything else in this course is built on.

![A fast calculator compared with a child generalising across unfamiliar dogs, showing that speed is not intelligence](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_section_intelligence_speed_vs_generalisation_draft.png)

## From Intelligence to Artificial Intelligence

Artificial intelligence, then, is the engineering discipline that tries to reproduce that cluster of abilities in machines.

There is a subtlety here that trips up almost every beginner, and it is worth naming plainly. AI does not require the machine to think the way a human thinks. When Ananya's app rerouted her, it did not feel frustrated about the traffic, form a mental picture of the lorry, or feel relief at finding a way around. It ran calculations over speed data. The behaviour was intelligent; the internal experience was almost certainly nothing like Ananya's.

The field has historically pulled in two directions on this point. One camp asks whether we can build machines that replicate human thought itself, which is really a question about the nature of mind. The other asks whether we can build machines that act correctly in the world, whatever is happening inside them. Modern AI, and this course, is overwhelmingly concerned with the second question. The measure of success is behaviour: given what the system can perceive, does it choose an action that sensibly serves its goal? A system that does this reliably is described as acting **rationally**, and rational action, not simulated humanity, is the practical target of nearly every AI system in production today.

This is also why the phrase "artificial intelligence" quietly shifts meaning as the field advances. Optical character recognition, chess playing, and speech transcription were all landmark AI problems in their day. Once solved and shipped, they stopped feeling like intelligence and started feeling like ordinary software. Researchers call this the AI effect: AI is the name we give to whatever computers cannot yet do comfortably.

![Visual explanation of from intelligence to artificial intelligence](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_section_from_intelligence_to_artificial_intelligence.png)

## The Line Between Automation and Intelligence

Here is the misconception worth correcting early, because it is the most common one. Many students assume that any automatic machine is an AI system. It is not.

Consider two washing machines. The first has a dial. You set it to forty minutes, and it runs for forty minutes, whether the drum holds one shirt or eight kilograms of bedsheets. The second weighs the load, senses how dirty the water becomes in the first few minutes, and adjusts the wash time and water level accordingly. Both are automatic. Only the second is doing anything that resembles perceiving a situation and adapting to it.

The discriminator is not "does it run without a human". It is: **does the system's behaviour change appropriately when the situation changes, without a person rewriting its instructions?** The dial-based machine has one behaviour. The sensing machine has a different behaviour for every load it meets, and no engineer enumerated them one by one.

Be careful, though, not to turn this into a rigid yes-or-no test. Intelligence in machines is a spectrum, not a switch. A thermostat that switches on below eighteen degrees adapts to its environment in the most minimal way imaginable and sits at the very bottom of that spectrum; Ananya's routing system sits much higher; a system that learns her preferences over months, higher still. Arguing about exactly where the boundary falls is far less useful than asking how much perception, reasoning, learning, and goal-directed action a given system actually demonstrates.

![Visual explanation of intro ai automation vs intelligence](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_intro_ai_automation_vs_intelligence_draft.png)

## Four Characteristics Every AI System Shows

Whatever the technique underneath, an AI system tends to exhibit the same four characteristics. These four recur throughout this entire course, so it is worth learning them properly now.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Characteristic</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it means</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">In Ananya's routing app</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Perception</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Taking in data about the environment through sensors, cameras, microphones, text, or streams of numbers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reading GPS speed signals from thousands of phones on the road</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Reasoning</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Drawing conclusions that were never explicitly supplied, by combining what is known</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Concluding that a stretch of unusually slow phones means the road is blocked</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Learning</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Improving performance from experience or data instead of from new instructions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Getting better at predicting travel times because millions of past journeys refined the estimates</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Goal-directed action</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Choosing and committing to the action that best serves an objective, then acting on it</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Selecting the side lane because it minimises arrival time, and issuing the turn instruction</td>
    </tr>
  </tbody>
</table>

Two clarifications matter here.

1. **Not every AI system shows all four strongly.** A spam filter perceives, reasons, and learns, but takes no action beyond sorting mail into a folder. A chess engine reasons and acts with enormous depth while perceiving only a board position.

2. **These four are not stages in a fixed pipeline.** In a self-driving car they run continuously and simultaneously, thousands of times per second, each feeding the others.

![Visual explanation of intro ai four characteristics](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_intro_ai_four_characteristics_draft.png)

## Four Familiar Systems, Four Different Kinds of Intelligence

The four characteristics become much clearer when you use them to compare systems Ananya already uses every day. Each of these is called AI in ordinary conversation, and each is intelligent in a genuinely different way.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">System</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Form of intelligence it demonstrates</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it plainly cannot do</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Google Maps</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Searching an enormous space of possible routes and optimising against a cost such as time</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hold a conversation, or understand why you are travelling</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Siri</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Converting speech to text, matching the request to a known intent, and triggering the right action</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reason its way through a request that fits none of its known intents</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>ChatGPT</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Generating fluent, contextually appropriate language across an open-ended range of topics</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Perceive the physical world, or guarantee that a confident statement is true</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>A Tesla on Autopilot</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Perceiving a physical scene from cameras and acting on it under hard real-time deadlines</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Explain its decisions in language, or plan anything beyond the driving task</td>
    </tr>
  </tbody>
</table>

Read the third column again, because it carries the real lesson of this comparison. Every one of these systems is superb inside a narrow band and helpless outside it. Ananya's car cannot summarise a chapter of this unit; ChatGPT cannot spot a child stepping off a kerb. Intelligence in machines today is deep and narrow, whereas human intelligence is shallower in each of these tasks but astonishingly broad. Holding that contrast in mind will keep you honest every time somebody claims a system is close to human-level.

![Visual explanation of four familiar systems, four different kinds of intelligence](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_section_four_familiar_systems_four_different_kinds_of_intelligence.png)

## What the Field Is Actually Trying to Achieve

The goals of AI split into two families, and confusing them causes a surprising amount of muddled argument.

- **The scientific goal: understand intelligence itself.** Building a machine that reasons, or learns language, is a way of testing theories about how reasoning and language work at all. On this view even a failed system is a useful result, because it tells you the theory was wrong.
- **The engineering goal: build systems that are useful.** Whether or not they illuminate anything about human cognition. A fraud detection model that saves a bank crores of rupees each year is a complete success by this standard, even if it teaches us nothing about how humans spot deception.

Within the engineering goal, four objectives recur across almost every system in this course.

1. **Automate tasks that need judgment, not just repetition.** Payroll software automates arithmetic; a loan risk model automates an assessment that used to require an experienced officer's judgment.

2. **Handle uncertainty and incomplete information.** A doctor diagnoses without knowing everything, and so must a diagnostic system. Real environments are noisy, partly hidden, and constantly changing, and a system that only works on perfect inputs is not useful.

3. **Improve from experience rather than from rewrites.** The commercial appeal of learning systems is that they get better as data accumulates, without an engineer editing rules for every new case.

4. **Augment human capability rather than merely replace it.** The most successful deployed systems pair a human with a machine: the radiologist reviews the scans the model flagged, the fraud analyst investigates the transactions the model scored as risky. Each covers the other's weakness.

![Visual explanation of what the field is actually trying to achieve](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_section_what_the_field_is_actually_trying_to_achieve.png)

## Your Turn

Pick any three apps or devices you used in the last twenty-four hours. For each one, work through the four characteristics from earlier and write a single sentence answering each question:

1. What does this system perceive, and through what?
2. What conclusion does it draw that nobody explicitly programmed for your specific case?
3. Does it get better as more people use it, and how would you know?
4. What goal is it optimising for, and is that goal the same as yours?

Then find the honest gap: for each system, name one thing it clearly cannot do that a reasonably attentive person could do easily. If you cannot find such a gap, you have not looked hard enough. And if question 4 reveals a system optimising for something other than what you wanted, engagement rather than your time well spent, say, you have just stumbled onto one of the central concerns this unit returns to later.
