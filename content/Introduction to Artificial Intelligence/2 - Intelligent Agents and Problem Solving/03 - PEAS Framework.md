## Introduction

Two engineers at an agri-drone startup in Coimbatore spend a full hour arguing about whether their spraying drone works.

Vinay says it works. It covers a hectare in nine minutes, which is four times faster than a manual sprayer, and the flight logs are clean. Priyanka says it does not work. It sprays evenly across the whole field, including the twenty percent that had no pest problem, which wastes chemical and is the entire reason the farmer was interested in a drone rather than a tractor.

Neither of them is confused about the facts. They agree completely on what the drone does. They are arguing because nobody ever wrote down what the drone is *for*, and in the absence of that sentence, "works" means whatever each engineer privately assumed it meant six months ago.

This argument is preventable, and the thing that prevents it is a short specification written before anyone builds anything. It names four things: what counts as success, what world the agent operates in, what it can change, and what it can know. Its initials spell **PEAS**.

**Definition:** The `PEAS framework` specifies an intelligent agent by stating its `Performance measure`, its `Environment`, its `Actuators`, and its `Sensors`, fixing what the agent is for and what it has to work with before any design decisions are made.

![Opening scene: Two engineers at an agri-drone startup in Coimbatore spend a full hour arguing about whether their spraying drone works.](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_section_introduction.png)

## What PEAS Forces You To Do

PEAS is not a classification exercise to be filled in after the fact. Its value is entirely in being written first, because each of the four letters forces a question that teams otherwise leave unanswered until it is expensive.

- **P forces you to define success in advance**, so that "does it work" has an answer both engineers must accept.
- **E forces you to state the boundary of the problem**, which determines what the agent will meet and, more importantly, what it will not be built to handle.
- **A forces you to bound the agent's power**, because an agent can only ever change the world through its actuators.
- **S forces you to bound the agent's knowledge**, because an agent can never act on anything its sensors do not deliver.

Write the four honestly and most bad designs die on paper, which is the cheapest place for them to die.

![Visual explanation of what peas forces you to do](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_section_what_peas_forces_you_to_do.png)

## P: The Performance Measure

This is the hardest of the four and the one that decides whether the project succeeds, so it deserves the most care.

A performance measure states what success means as a property of the environment. Vinay and Priyanka were each using a different one without saying so: his was area covered per minute, hers was pest controlled per litre of chemical. Both are defensible. Only one of them is what the farmer is paying for, and that is a question a business decides, not a question an engineer resolves by intuition.

Three rules make a performance measure usable.

1. **State it as a property of the world, not of the agent's behaviour.** "Pest population reduced below the economic threshold with minimum chemical used" describes the field. "Follows the flight path accurately" describes the drone and can be satisfied perfectly while the crop dies.

2. **Make it measurable.** If nobody can compute the number after a flight, it is a slogan. "Sprays efficiently" is a slogan; "litres used per hectare of infested area" is a measure.

3. **Name every objective, including the ones in tension.** Coverage, chemical consumption, flight time, battery life, and drift onto neighbouring plots all matter. Leaving one out does not remove it from reality, it just means the agent is free to sacrifice it entirely.

The third rule is where most designs quietly fail. An objective that is not in the performance measure has an implicit weight of zero, and a competent optimiser will happily destroy it to gain a little on something that is measured.

![Visual explanation of p: the performance measure](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_section_p_the_performance_measure.png)

## E: The Environment

The environment is everything the agent operates within and interacts with. Specifying it means drawing a boundary and being explicit about what falls inside.

For the spraying drone, the environment includes the field with its crop rows and terrain, the weather and especially the wind, obstacles such as trees and power lines and irrigation towers, the neighbouring plots that must not be sprayed, other drones if several fly together, and the human operator.

The discipline here is stating what the agent will *not* be built for. If the specification says the environment is flat fields in daylight with wind below fifteen kilometres per hour, then hilly terrain at dusk in a gale is out of scope by agreement, rather than being an unpleasant surprise during a demonstration. Every deployed agent has such a boundary. The only choice is whether it is written down or discovered.

![Visual explanation of e: the environment](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_section_e_the_environment.png)

## A: Actuators

Actuators are the means by which the agent changes the world, and they set a hard ceiling on what it can achieve.

The drone's actuators are its rotors, the spray nozzles, the valve controlling flow rate, and the radio that reports status. Notice what follows immediately from that list. If the nozzle can only be fully on or fully off, then no amount of clever software will produce a variable spray rate, and the objective of using less chemical on lightly infested areas is unreachable. It is a hardware problem wearing a software costume.

This is why actuators belong in the specification rather than in a later engineering document. Listing them early is what surfaces the objectives that the machine physically cannot meet, at the point where the nozzle can still be changed.

![Visual explanation of a: actuators](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_section_a_actuators.png)

## S: Sensors

Sensors are how the agent perceives, and they set the ceiling on what it can know.

The drone's sensors are its GPS, altimeter, a camera, a wind sensor, the tank level, and the battery gauge. Look at Priyanka's complaint again with this list in view. She wants the drone to spray only infested areas. That requires the agent to know which areas are infested, which requires the camera to be good enough, positioned well enough, and paired with a model capable of telling infested crop from healthy crop at flight altitude and speed.

If that capability is absent, uniform spraying is not a flaw in the drone's decision-making. It is the only behaviour available to an agent that cannot perceive the distinction. The sensors decide what questions the agent is even able to ask.

![Visual explanation of s: sensors](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_section_s_sensors.png)

## Three Worked PEAS Descriptions

The framework is best learned by seeing it applied to systems with very different shapes.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Agent</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Performance measure</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Environment</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Actuators</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Sensors</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Self-driving car</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Passengers and others unharmed, traffic law obeyed, destination reached, journey time reasonable, ride comfortable, fuel or charge used efficiently</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Roads, lanes, signals, other vehicles, pedestrians and animals, weather, road surface quality, local traffic conventions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Steering, accelerator, brakes, indicators, horn, lights, passenger display</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cameras, lidar, radar, ultrasonic sensors, GPS, wheel odometry, accelerometer, microphone</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Agricultural spraying drone</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Infested area treated, chemical per hectare minimised, zero drift onto neighbouring plots, field completed within one battery, no collisions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The field and its crop rows, wind and weather, trees and power lines, plot boundaries, the operator</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rotors, spray nozzles, flow-rate valve, status radio</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">GPS, altimeter, downward camera, wind sensor, tank level, battery gauge</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Warehouse robot</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Orders picked correctly and on time, distance travelled minimised, no collisions with people or racks, stock never damaged, charge managed without blocking an aisle</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Aisles and racks, inventory locations, human staff walking about, other robots, charging stations, the order queue</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Drive wheels, lifting mechanism or arm, gripper, warning light and buzzer, network radio</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Floor markers or QR tags, cameras, proximity and bump sensors, weight sensor, barcode scanner, battery gauge</td>
    </tr>
  </tbody>
</table>

Read down the performance measure column rather than across the rows, because that column is where the design arguments live. Every entry contains at least two objectives that pull against each other: speed against safety in the car, coverage against chemical use in the drone, distance travelled against collision avoidance in the warehouse. A specification that lists only one objective per agent has not simplified the problem, it has hidden it.

![Visual explanation of peas three examples](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_peas_three_examples.png)

## Common Mistakes When Writing PEAS

Four errors account for most of the bad PEAS descriptions students write, and all four are worth recognising in your own work.

1. **Writing the performance measure as behaviour.** "Follows the planned route" instead of "arrives safely and on time". The behaviour version can be satisfied perfectly by an agent that is failing.

2. **Listing sensors the agent does not actually have.** Writing "detects pest infestation" as a sensor when the hardware is a plain camera. The camera is the sensor; infestation detection is something the agent program might infer from it, and only if it can.

3. **Describing the environment as one tidy sentence.** "A farm field" hides wind, power lines, and the neighbour's plot, which are precisely the things that will cause the first crash.

4. **Confusing actuators with actions.** The rotors are the actuator; "fly to the north-east corner" is an action the rotors make possible. Mixing them up conceals what the hardware can and cannot do.

![Visual explanation of common mistakes when writing peas](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_section_common_mistakes_when_writing_peas.png)

## PEAS at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Letter</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Question it answers</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it constrains</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Performance measure</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What does success mean, as a state of the world?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Every design trade-off, and what counts as a bug</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Environment</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What will the agent encounter, and what is out of scope?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Which situations the agent is accountable for</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Actuators</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How can the agent change the world?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The ceiling on what it can ever achieve</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Sensors</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What can the agent know?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The ceiling on what it can ever decide</td>
    </tr>
  </tbody>
</table>

![Visual explanation of peas framework](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_peas_framework.png)

## Your Turn

Write a full PEAS description for an automated attendance system in your own classroom, the kind that marks students present from a camera at the front.

Give the performance measure at least three objectives, and make sure two of them genuinely conflict. Then answer the question that makes this exercise real rather than clerical: your measure almost certainly includes something like "students correctly marked present". Split that into the two ways it can fail, marking an absent student present and marking a present student absent, and decide which is worse. Whatever you decide, a system optimising overall accuracy will trade them against each other on its own terms, so write your preference into the measure explicitly.

Then look hard at the sensors. A single camera at the front of a hall sees the front rows clearly and the back rows as a blur of heads. Given that, write down honestly which of your performance objectives is unreachable, and decide whether you would change the sensor or lower the objective. Either answer is defensible. Pretending the problem is not there is not.
