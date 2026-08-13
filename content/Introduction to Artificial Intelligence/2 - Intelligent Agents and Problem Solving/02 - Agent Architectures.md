## Introduction

Rehana works at a delivery company in Pune that is building a navigation assistant for its riders, and over eighteen months she watches the same product get rebuilt five times.

Version one was a set of rules. If the signal is red, stop. If the road ahead is blocked, turn right. It shipped in a fortnight and worked until a rider got stuck in a loop, turning right into a lane that fed back into the same blocked junction, turning right again, for eleven minutes.

Version two remembered where the rider had already been. Version three was told the delivery address and worked out a route to it. Version four started weighing a faster route against a safer one when it was raining. Version five began noticing which of its own suggested routes riders quietly ignored, and stopped suggesting them.

Five products, one problem, and each version differs from the last not in what it perceives but in **what it keeps and what it considers** between the percept arriving and the action going out. That internal design is an **agent architecture**, and there are five standard ones, which are exactly the five versions Rehana shipped.

**Definition:** An `agent architecture` is the internal organisation of an agent program: what information it retains, what it reasons about before acting, and therefore what range of behaviours it can produce.

![Visual explanation of introduction](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_section_introduction.png)

## Simple Reflex Agents

A `simple reflex agent` chooses its action from the current percept alone, using condition-action rules. Nothing is remembered, nothing about the future is considered.

Rehana's version one was exactly this. Each rule reads "if this condition holds in what I can see right now, do this". It is the architecture of a thermostat, an automatic door, and a spam filter that blocks any message containing a banned phrase.

The appeal is real, and it is not just simplicity. These agents are fast, they need almost no memory, their behaviour is completely predictable, and anybody can read the rules and say exactly what the agent will do.

The failure is equally real, and version one demonstrated it precisely. **A simple reflex agent cannot distinguish two situations that look identical but are not.** The blocked junction looked the same on the eleventh pass as on the first, because the only thing distinguishing them was history, and history is exactly what this architecture discards. The rider looped because the agent had no way to know it was looping.

This failure has a name worth remembering: simple reflex agents work only when the correct action depends solely on the current percept. The moment the right answer depends on what happened earlier, the architecture is not merely weak, it is incapable.

![Visual explanation of reflex vs model based agent](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_reflex_vs_model_based_agent.png)

## Model-Based Reflex Agents

A `model-based reflex agent` keeps an internal state summarising the percept history, and updates it using a model of how the world works.

Version two did this. It maintained a small record of which junctions the rider had passed and when, so "I have been here before" became something the agent could know. The loop stopped, not because the rules got cleverer, but because the situations stopped looking identical.

Maintaining that internal state requires two distinct pieces of knowledge, and separating them is the part students usually blur together.

1. **The transition model.** How the world changes, both on its own and as a result of the agent's actions. Turning right at this junction puts the rider on that road. Traffic tends to build up after six in the evening whether or not the rider does anything.

2. **The sensor model.** How the world's state is reflected in the percepts. A GPS reading of fifty metres accuracy means the rider is somewhere in a circle, not at a point.

With these, the agent can maintain a best guess about the parts of the world it cannot currently see. This is the architecture that makes an agent useful in an environment where the sensors do not reveal everything, which is nearly every real environment.

What it still cannot do is aim. Version two knew where the rider had been. It had no idea where the rider was trying to go.

![Visual explanation of model-based reflex agents](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_section_model_based_reflex_agents.png)

## Goal-Based Agents

A `goal-based agent` holds an explicit description of a desired situation and chooses actions by considering how they lead towards it.

This is a genuine change in kind, not degree. Version three was given the delivery address, and for the first time the agent's action depended on the future rather than only on the present and past. Deciding whether to turn right now requires thinking several steps ahead about where each option leads, which is why this is the architecture where search and planning enter.

Goal-based agents are slower and more computationally expensive than reflex agents. They buy something valuable with that cost: **flexibility**. Change the destination and the behaviour changes completely, with nothing rewritten. A reflex agent would need a new rule set for every destination, which is an impossible way to build a delivery app.

The limitation is that a goal is binary. The address is either reached or not. Version three had no way to express that arriving in twenty minutes on a well-lit main road is better than arriving in eighteen minutes through an unlit industrial lane in the rain. Both reach the goal, so both are equally good, which is obviously wrong.

![Visual explanation of goal-based agents](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_section_goal_based_agents.png)

## Utility-Based Agents

A `utility-based agent` scores outcomes on a continuous scale rather than sorting them into achieved and not achieved, and chooses the action with the highest expected score.

Version four introduced this, and the entire monsoon problem dissolved. `Utility` is a measure of how desirable a state is, so the agent can now say that a route is worth 0.9 in daylight and 0.4 in heavy rain at night, and trade three extra minutes against a large gain in safety.

Two situations force this architecture, and neither is exotic.

- **Conflicting goals.** Fast, safe, and cheap cannot all be maximised at once, and a utility function states the exchange rate between them instead of leaving it to whoever wrote the rules.
- **Uncertain outcomes.** When an action might succeed or might not, the agent needs to weigh how good each outcome is against how likely it is. Choosing the action with the highest **expected utility**, meaning the value of each outcome weighted by its probability, is what rational behaviour reduces to under uncertainty.

The catch is that somebody must write the utility function, and writing it honestly is difficult. Stating how many minutes of delay a rider's safety is worth is an uncomfortable question, but note that a system without a utility function has still answered it, just implicitly and without anyone taking responsibility for the answer.

![Visual explanation of utility-based agents](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_section_utility_based_agents.png)

## Learning Agents

A `learning agent` improves its own performance over time from experience, and can be layered on top of any of the four architectures above.

Version five was the first to get better without an engineer editing it. Any learning agent decomposes into four parts, and the fourth is the one people forget.

1. **The performance element.** The part that actually selects actions. This is whichever of the four architectures above the agent is using.
2. **The learning element.** The part that makes improvements, using feedback about how things went.
3. **The critic.** The part that judges how well the agent is doing against a fixed external standard. The critic is essential because the performance measure cannot come from the agent itself; an agent that could rewrite its own definition of success would simply declare victory.
4. **The problem generator.** The part that deliberately suggests suboptimal exploratory actions in order to learn something new.

That last component is worth dwelling on. An agent that always takes the action it currently believes is best will never discover a better one, because it never tries anything else. Version five occasionally suggested an untested route precisely so it could find out whether that route was good. Short-term performance drops; long-term performance improves. This tension between exploiting what you know and exploring what you do not is one of the recurring problems in the whole field.

![Visual explanation of learning agents](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_section_learning_agents.png)

## The Five Architectures at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Architecture</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it holds</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Rehana's version</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What defeats it</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Simple reflex</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Condition-action rules only</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stop at red, turn right if blocked</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Two situations that look identical but need different actions</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Model-based reflex</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Internal state, plus transition and sensor models</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Remembers junctions already passed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Having no destination to aim at</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Goal-based</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An explicit goal, and reasoning about the future</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Routes to the delivery address</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Two routes that both reach the goal but are not equally good</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Utility-based</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A scoring function over outcomes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Trades speed against safety in the rain</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A utility function nobody can write honestly</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Learning</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Performance element, learning element, critic, problem generator</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Drops routes that riders keep ignoring</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Needing feedback, and needing to explore to improve</td>
    </tr>
  </tbody>
</table>

![Visual explanation of agent architectures overview](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_agent_architectures_overview.png)

## Choosing an Architecture

The five are usually drawn as a ladder, and that picture causes a specific and expensive mistake: assuming the top rung is the goal.

It is not. **The right architecture is the simplest one that produces the required behaviour.** A thermostat should be a simple reflex agent. Giving it a utility function and a learning element would make it slower, more expensive, harder to certify, and prone to failures that a rule set cannot have. Three considerations decide the question.

- **Does the correct action depend on history?** If no, stop at simple reflex.
- **Does it depend on a goal that changes?** If no, you do not need goal-based machinery.
- **Are there competing objectives or uncertain outcomes?** Only if yes do you need utility.

Real systems also mix architectures rather than picking one. A self-driving car runs reflex rules for emergency braking, because a braking decision cannot wait for a planner to finish, while a goal-based planner works out the route and a utility-based layer decides how aggressively to overtake. Rehana's final product still contained every rule from version one, sitting underneath everything else, doing the job it was always good at.

![Visual explanation of choosing an architecture](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_section_choosing_an_architecture.png)

## Your Turn

Take a lift, an air conditioner with a remote, and a music streaming app, and assign each the simplest architecture that could produce the behaviour you actually observe.

For each, justify your choice by naming the specific behaviour that rules out the architecture one rung below. If you claim the streaming app is a learning agent, point to the observable evidence, and then work out which of the four learning components you can actually see operating from the outside.

Then design the upgrade. Pick the one you rated lowest and describe what would have to be added, in terms of retained information rather than features, to move it up one rung. The air conditioner is the interesting case: most of them are simple reflex agents comparing current temperature against a target, and making one model-based requires deciding what it should remember and why. If your answer is "how quickly this particular room heats up", you have just described a transition model, and you have understood the architecture.
