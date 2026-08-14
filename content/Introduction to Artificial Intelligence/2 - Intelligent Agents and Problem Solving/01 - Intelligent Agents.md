## Introduction

Nandini's family buys a robot vacuum, and within a week her grandmother has formed a firm opinion about it. The thing is stupid. It cleans the same patch of the hall three times, ignores the visibly dusty corner near the shoe rack, and every single afternoon it drives into the same chair leg, reverses, turns, and drives into it again.

Nandini sits on the floor one Sunday and watches it properly, and what she notices changes how she thinks about the machine. The vacuum does not know there is a chair. It has no picture of the hall in its head, no memory of yesterday, no concept of a corner. It has a bump sensor, a dirt sensor, and wheels. Its entire experience of the universe is a short sentence that says either "I have hit something" or "I have not", and either "there is dirt here" or "there is not". Given only that, driving into the chair, reversing, and turning is not stupidity. It is the only thing the machine is in a position to do.

The grandmother was judging the vacuum against her own view of the hall. The vacuum was acting on its view of the hall, which is almost nothing. Once you separate those two things, you can reason clearly about any AI system, because every one of them is an **agent**: something that takes in whatever its sensors give it, and acts through whatever its actuators allow.

**Definition:** An `agent` is anything that perceives its environment through sensors and acts upon that environment through actuators, choosing each action on the basis of what it has perceived so far.

![Opening scene: Nandini's family buys a robot vacuum, and within a week her grandmother has formed a firm opinion about it.](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_section_introduction.png)

## The Agent Loop: Percept In, Action Out

Strip away every difference between a vacuum, a navigation app, and a self-driving car, and the same loop remains. The agent perceives, decides, acts, and the environment changes, which produces the next perception. Round and round, for as long as the agent runs.

Four terms make this precise, and they will be used constantly from here on.

1. **Percept.** What the agent's sensors deliver at one instant. For the vacuum, a single percept is the pair "bumped, no dirt".

2. **Percept sequence.** The complete history of everything the agent has perceived since it started. This is the largest amount of information the agent could possibly base a decision on.

3. **Actuators.** The means by which the agent changes the world. Wheels and a suction motor for the vacuum, a screen and a speaker for a navigation app.

4. **Action.** One choice from the set of things the actuators can do. The vacuum's entire action set might be no more than move forward, turn left, turn right, and suck.

There is one further distinction that separates people who really understand agents from people who have only memorised the loop. The **agent function** is the mapping from every possible percept sequence to the action the agent should take. It is a specification, an idea, and for any interesting agent it would be an unimaginably large table. The **agent program** is the actual code that runs on the machine and produces those actions. The function says what the behaviour should be; the program is how it is achieved in a few kilobytes instead of a few billion rows. Designing an agent means choosing a function you want and then finding a program compact enough to implement it.

![Visual explanation of agent loop and percept sequence](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_agent_loop_and_percept_sequence.png)

## Why the Percept Sequence Matters

Return to the chair leg, because it illustrates the single most important constraint on any agent: **an agent can act only on what it has perceived, plus whatever it has chosen to remember.**

Nandini's vacuum bumps the chair every day because it keeps no history. Each percept arrives, an action is chosen, and the percept is discarded. Its effective percept sequence has a length of one. It cannot learn that this particular spot always ends in a collision, because by the time it reaches the spot again it has no record that it was ever there.

A newer vacuum with a camera and a map behaves completely differently, and not because it is cleverer in some vague sense. It is because its percept sequence is retained and organised into a map, so the phrase "the chair is there" becomes something it can hold. The upgrade that fixed the behaviour was an upgrade to perception and memory, not to reasoning.

This gives you a diagnostic question worth asking of any AI system that behaves strangely: is this a failure of decision-making, or is the system simply unable to perceive the thing you are judging it for? Most of the time it is the second.

![Visual explanation of why the percept sequence matters](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_section_why_the_percept_sequence_matters.png)

## Rationality Is Not Perfection

Now to the concept that beginners most reliably get wrong. In AI, a `rational agent` is one that selects the action expected to maximise its performance measure, given the percept sequence it has and the knowledge built into it.

Read that carefully, because of what it does not say. It does not say the agent always succeeds, and it does not say the agent knows everything.

Imagine you look both ways at a crossing, see nothing coming, and step onto the road. A loose panel falls from a building and lands on you. Were you irrational? Obviously not. You took the action that was expected to work, on the evidence available. Rationality is judged on the quality of the decision given what could be known, never on the outcome, because judging on outcome would require the agent to be clairvoyant.

Three separations are worth fixing in your mind.

- **Rationality is not omniscience.** An omniscient agent knows the actual outcome of its actions in advance. No real agent does, so omniscience is not a standard anyone can be held to.
- **Rationality is not perfection.** A rational agent can fail, and often will, whenever the environment is uncertain or the information is incomplete.
- **Rationality does depend on gathering information.** An agent that could easily have looked and did not is being irrational, because taking a cheap action that improves future percepts is itself part of maximising expected performance. Doing nothing while remaining ignorant is not a defence.

![Visual explanation of rationality is not perfection](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_section_rationality_is_not_perfection.png)

## The Four Things Rationality Depends On

Whether an action is rational is never an absolute fact. It depends on four things at once, and changing any one of them can turn a rational action into an irrational one.

1. **The performance measure.** The criterion of success, defined by the designer.
2. **The agent's prior knowledge.** What was built into it about how the environment behaves.
3. **The actions available.** An agent cannot be faulted for failing to do something it has no actuator for.
4. **The percept sequence to date.** Everything it has actually observed.

The vacuum's chair-leg behaviour is rational under a percept sequence of length one and irrational for an agent holding a map. Same action, same environment, different rationality, because the fourth item changed.

![Visual explanation of the four things rationality depends on](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_section_the_four_things_rationality_depends_on.png)

## Performance Measure: Judge the Environment, Not the Agent

The first item on that list is where most agent designs go wrong, and it deserves its own warning.

A performance measure states what success means. The tempting mistake is to write it as a description of the behaviour you imagine the agent should have, rather than the state of the world you actually want.

Suppose you reward Nandini's vacuum for the quantity of dirt it collects. That sounds reasonable for about ten seconds. A sufficiently capable agent maximising that measure would discover that the fastest route to a high score is to collect dirt, eject it back onto the floor, and collect it again. It would be behaving perfectly rationally and leaving the house filthy. The correct measure is the one that describes the world you want: a clean floor, over time, with reasonable power consumption and no furniture damaged.

The general rule, and it is one of the most quietly important rules in the whole subject: **specify the performance measure in terms of what you want the environment to look like, not in terms of how you imagine the agent should behave.** An agent will satisfy exactly what you wrote, which is rarely the same as what you meant.

![Visual explanation of rationality and performance measures](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_rationality_and_performance_measures.png)

## Three Agents You Already Use

The vocabulary becomes concrete the moment it is applied to systems you already rely on. Notice how little the three have in common physically, and how identically they decompose.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Agent</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Percepts</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Actions</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Performance measure</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>GPS navigation app</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Current location, road network, live speed data from other users, the destination you typed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Display a route, announce a turn, recalculate</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Arrival time, route reliability, number of confusing instructions</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Robot vacuum</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Bump sensor, dirt sensor, cliff sensor, battery level, and on newer models a camera and a stored map</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Move, turn, suck, return to dock</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Floor area actually cleaned, time taken, power used, furniture undamaged</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Virtual assistant</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Audio from the microphone, the request text, time of day, calendar and contacts</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Speak a reply, set an alarm, send a message, play audio</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Requests correctly fulfilled, response time, mistakes that cost the user something</td>
    </tr>
  </tbody>
</table>

Look at the last column and notice how much of the design argument lives there. If the navigation app's performance measure were arrival time alone, it would happily route every rider down a terrifying unlit shortcut. Real navigation apps include reliability and road quality precisely because someone thought harder about the measure.

![Visual explanation of three agents you already use](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_section_three_agents_you_already_use.png)

## Agents at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Term</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">For Nandini's vacuum</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Percept</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sensor input at one instant</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"Bumped, no dirt"</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Percept sequence</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Everything perceived so far</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Length one, since nothing is retained</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Agent function</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The mapping from percept sequences to actions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"If bumped, reverse and turn; if dirt, suck; else move forward"</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Agent program</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The code that implements the function</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A few lines running on the vacuum's chip</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Rational action</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The action expected to maximise the performance measure on current evidence</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reversing after a bump, given that it cannot see the chair</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Performance measure</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The definition of success, stated as a property of the environment</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A clean floor, not a full dust bin</td>
    </tr>
  </tbody>
</table>

![Visual explanation of agents at a glance](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_section_agents_at_a_glance.png)

## Your Turn

Take the ceiling fan regulator in your room and the lift in your building, and decide which of them is an agent.

For each, write down the four elements: what it perceives, what actions it can take, what its performance measure appears to be, and how much of its percept sequence it retains. Then judge it. Is its behaviour rational given what it can perceive, or is it genuinely making poor decisions with good information available?

The lift is the interesting one. Most lifts perceive only the buttons currently pressed and the floors they are passing, which is why a lift will sail past you going down when you wanted to go up and then come back. Work out what extra percept would fix that behaviour, and then write a performance measure for a lift in the correct form, as a statement about the building rather than about the lift. If your measure is "minimise total waiting time across all passengers", ask yourself what a rational agent maximising it would do to the person on the top floor at a busy hour, and whether you are willing to accept that answer.
