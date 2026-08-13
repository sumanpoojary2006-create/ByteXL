## Introduction

Aditya's team wins a college robotics contest with a chess-playing arm, and on the strength of it a local firm asks them to prototype a small delivery robot for a hospital corridor. The team is confident. They have solved a hard AI problem already, so how different can a corridor be?

Very different, and within a fortnight they know exactly how. Their chess program worked because it could see the entire board, because moving a piece always produced exactly the position it expected, because nothing changed while it was thinking, and because there were a finite number of legal moves to consider. In the corridor, none of those four things is true. The robot cannot see round the bend. Commanding the wheels to turn thirty degrees produces roughly thirty degrees on polished floor and rather less on a wet patch. Trolleys and people move while the robot deliberates. And "how far forward" is not a choice among a handful of options but a continuous quantity.

Their algorithms did not fail because they were badly written. They failed because chess and a hospital corridor are structurally different kinds of world, and the structure of the world decides which algorithms can work in it at all. Classifying that structure is what **AI environments** is about.

**Definition:** An `AI environment` is classified by a small number of structural properties, such as how much of it the agent can observe and how predictable its actions are, and these properties determine which techniques are viable for an agent operating within it.

![Visual explanation of introduction](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_section_introduction.png)

## Fully Observable vs Partially Observable

An environment is `fully observable` when the agent's sensors give it access to the complete state of the environment relevant to its decision at every moment. It is `partially observable` when something relevant is hidden, whether by sensor limits, noise, or physical obstruction.

Chess is fully observable. Every piece sits face up, and there is nothing about the position that either player cannot see.

The hospital corridor is partially observable, for three separate reasons worth distinguishing. Something can be **occluded**, like the trolley round the bend. A sensor can be **imprecise**, like a GPS reading accurate to fifty metres. And some things are simply **unsensed**, like whether the person ahead is about to turn left, which no sensor reports because it exists only as an intention.

This is the single most consequential property, because of what it forces on the agent's design. In a fully observable environment, the current percept is enough, and the agent needs no memory. In a partially observable one, the agent must maintain an internal belief about the parts of the world it cannot currently see, and that belief is a guess that can be wrong.

A caution: full observability is rarer than students assume. Card games with hidden hands, negotiation, medical diagnosis, and essentially all robotics are partially observable. Chess is unusual, not typical.

![Visual explanation of ai environment dimensions](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_ai_environment_dimensions.png)

## Deterministic vs Stochastic

An environment is `deterministic` when the next state is completely determined by the current state and the agent's action. It is `stochastic` when the same action in the same state can lead to different outcomes.

Move a rook four squares in chess and it lands four squares away, every time, with certainty. Command a robot to advance one metre and it advances roughly one metre, with the error depending on the floor surface, the battery level, and how worn the wheels are.

Two clarifications that trip people up.

- **Partially observable is not the same as stochastic.** An environment can be perfectly deterministic and still appear unpredictable to an agent that cannot see all of it. Much of what looks like randomness in practice is really hidden state.
- **Stochastic is not the same as adversarial.** Dice are stochastic and indifferent to you. An opponent is deterministic in the sense of following rules, and is actively trying to make your situation worse, which is a different problem again.

The design consequence is that in a deterministic environment an agent can plan a sequence of actions in advance and simply execute it. In a stochastic environment, any plan must be checked against what actually happened, which is why real robots re-plan continuously rather than following a fixed script.

![Visual explanation of deterministic vs stochastic](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_section_deterministic_vs_stochastic.png)

## Static vs Dynamic

An environment is `static` if it does not change while the agent is deliberating, and `dynamic` if it does.

Chess is static. Aditya's program could think for three minutes and return to a board in exactly the position it left. Nothing moved because nothing was allowed to.

The corridor is dynamic and unforgiving about it. A person walking at a normal pace covers a metre and a half every second, so a plan computed over two seconds is a plan for a world that no longer exists. This is the property that introduces real-time constraints: in a dynamic environment, an answer that arrives late is not a slightly worse answer, it is the wrong answer.

There is a useful middle category. An environment is **semi-dynamic** when the world itself does not change but the agent's score does, which is exactly what a chess clock creates. The board waits; the clock does not.

![Visual explanation of static vs dynamic](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_section_static_vs_dynamic.png)

## Discrete vs Continuous

An environment is `discrete` when its states, time, and available actions take distinct separated values, and `continuous` when they vary smoothly across a range.

Chess is discrete throughout. There are sixty-four squares, a finite number of legal moves in any position, and the game proceeds in turns rather than flowing.

Driving and corridor navigation are continuous. Position, speed, and steering angle are real numbers, and time flows rather than ticking. This matters enormously for the algorithms available: a discrete environment can in principle be searched by enumerating possibilities, whereas a continuous one has infinitely many, so it must either be handled with mathematics suited to continuous quantities or **discretised**, meaning carved into a finite grid of choices. Discretisation is the standard practical move, and it always involves throwing away some precision in exchange for being able to enumerate at all.

![Visual explanation of discrete vs continuous](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_section_discrete_vs_continuous.png)

## Classifying Three Familiar Environments

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Property</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Chess</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Autonomous driving</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Robot vacuum</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Observability</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fully observable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Partially observable, and severely so</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Partially observable; it senses only the patch it occupies</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Predictability</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Deterministic</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stochastic; grip, other drivers, and pedestrians all vary</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stochastic; wheels slip on rugs and carpet edges</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Change during deliberation</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Static, or semi-dynamic with a clock</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dynamic, with hard real-time deadlines</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Mildly dynamic; pets and chairs move, but slowly</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Values</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Discrete in states, time, and actions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Continuous in position, speed, and steering</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Continuous in position, usually discretised onto a grid</td>
    </tr>
  </tbody>
</table>

The vacuum row is the instructive one, because most people classify it as the easy case and get it wrong. It is partially observable and stochastic, exactly like the self-driving car, and differs mainly in that mistakes are cheap and deadlines are soft. The environment is not simpler. The consequences of failure are.

Note also that these labels describe the environment **as the agent experiences it**, not as it exists. Give the vacuum a camera and a stored map and it becomes considerably more observable, without a single thing changing in the room. Aditya's team eventually understood this: some of their corridor problem was the corridor, and some of it was their sensor budget.

![Visual explanation of classifying three familiar environments](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_section_classifying_three_familiar_environments.png)

## Why the Classification Changes the Engineering

This is not taxonomy for its own sake. Each property rules techniques in or out before a line of code is written.

1. **Partially observable rules out stateless agents.** The agent must maintain and update a belief about what it cannot see, which means memory, a transition model, and a sensor model are mandatory rather than optional.

2. **Stochastic rules out fixed plans.** A sequence computed in advance cannot be trusted to execute, so the agent must sense and re-plan in a loop, and must reason about probabilities rather than certainties.

3. **Dynamic rules out unbounded deliberation.** The agent needs an answer within a deadline, which usually means accepting a good answer quickly over the best answer eventually.

4. **Continuous rules out plain enumeration.** Either the problem is discretised onto a grid, accepting the loss of precision, or it needs methods built for continuous quantities.

Read those four together and Aditya's fortnight makes complete sense. His chess program assumed the opposite of each, so all four assumptions broke at once. This is also the honest reason board games were solved decades before driving: not because game AI was more difficult, but because a board is the friendliest environment that exists.

One further note for completeness. Researchers use several other dimensions beyond these four, including whether the agent is alone or competing with others, whether the current decision affects future ones, and whether the rules of the environment are known in advance. The four covered here are the ones that most directly determine which algorithm is viable.

![Visual explanation of environment changes engineering](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_environment_changes_engineering.png)

## Your Turn

Classify three environments on all four properties: a lift in your building, an online multiplayer game you have played, and an ATM.

For each property, write one sentence of justification naming the specific feature of the environment that decides it. Then look for the disagreement, because there will be one. The ATM will look fully observable to most people, so ask what it actually knows: it sees a card, a PIN, and a balance, but it cannot see whether the person holding the card is the person the card belongs to. Does that make it partially observable? Argue it either way, but argue it from the definition rather than from intuition.

Then do the useful part. For whichever environment you classified as most difficult, name one sensor you could add that would flip one property towards the easier side, and state what that would cost. Environments are not fixed facts about the world; they are facts about the world as your agent can perceive it, and engineering the perception is often cheaper than engineering the intelligence.
