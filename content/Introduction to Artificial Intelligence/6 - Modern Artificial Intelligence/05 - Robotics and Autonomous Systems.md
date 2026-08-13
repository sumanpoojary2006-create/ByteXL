## Introduction

A warehouse near Bhiwandi installs its first mobile robots, and the project manager's expectation is that the hard part will be teaching them to recognise things.

It is not. Recognition is largely solved and available. What consumes the next eight months is everything around it: the robot that knows exactly where it is until somebody parks a pallet in an aisle and the floor markers are covered; the one that plans a perfect route and then cannot execute it because the wheels slip differently on the loading dock; the one that stops correctly for a person and then cannot decide when it is safe to resume, and sits there.

None of these is a perception failure. They are failures of the harder thing, which is closing the loop between perceiving and acting, continuously, in a world that does not wait.

**Definition:** `Robotics and autonomous systems` concerns machines that sense their environment, determine their own position within it, plan a course of action, and execute it through physical actuators, operating in a continuous loop under real-time constraints where errors have physical consequences.

![Visual explanation of introduction](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_section_introduction.png)

## Why Acting Is Harder Than Recognising

Every system earlier in this unit produces information. A misread review is a wrong label; a bad recommendation is a wasted screen. A robot produces motion, and four things change as a result.

1. **Errors are not undoable.** A mislabelled photograph can be relabelled. A shelf pulled over cannot be unpulled, and the cost is not a metric but a repair bill and possibly an injury.

2. **The deadline is real.** A vision model that takes an extra 200 milliseconds is slightly slow. A robot that takes an extra 200 milliseconds to decide about braking has travelled further, and a late answer is not a slightly worse answer but a wrong one.

3. **Commands do not become actions reliably.** Instructing the wheels to turn thirty degrees produces roughly thirty degrees, varying with the floor, the load, the battery, and how worn the wheels are. Nothing in software fixes this; it must be measured and corrected for continuously.

4. **The world changes without asking.** People walk about, pallets appear, a spill makes an aisle unusable. A plan is a statement about a world that has already moved on by the time it executes.

The fourth is why the project manager's assumption was wrong. Perception is a component. The system is the loop.

![Visual explanation of why acting is harder than recognising](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_section_why_acting_is_harder_than_recognising.png)

## The Four Stages

An autonomous system runs the same four stages continuously, many times a second.

**Perception** turns sensor readings into a description of the surroundings. A warehouse robot fuses several sensors rather than trusting one, because each fails differently: cameras struggle in poor light, lidar measures distance precisely and cannot read a label, ultrasonic sensors are cheap and imprecise, and wheel encoders measure how far the wheels turned rather than how far the robot moved. Combining them is `sensor fusion`, and the reason for it is that no single sensor is reliable enough alone.

**Localisation** answers where the robot is. This deserves emphasis because it is the stage people underestimate. A robot with a perfect map and no idea where it is standing on that map can do nothing at all. Indoors there is no satellite positioning, so position is tracked by accumulating wheel rotations and correcting against recognised landmarks, floor markers, or matched lidar scans. Accumulated error is the enemy: `dead reckoning` from wheel rotations alone drifts steadily, so the robot must periodically see something it recognises to correct itself. The Bhiwandi robot that lost its position when a pallet covered the floor markers lost exactly this correction.

**Planning** chooses a route and a sequence of actions. This is the search problem from earlier in this course, applied to a map, with the additional constraint that the plan must be recomputed constantly because the map keeps changing.

**Control** converts the plan into actuator commands and corrects the difference between what was commanded and what happened. A `feedback controller` measures the error between desired and actual state and adjusts continuously, which is what handles the wheels slipping on the loading dock.

![Visual explanation of robotics loop](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_robotics_loop_context_v4.png)

## Localisation and Mapping Together

There is a chicken-and-egg problem worth naming because it defines much of the field.

To know where you are, you need a map. To build a map, you need to know where you were when you observed each thing. A robot placed in an unmapped building has neither.

`SLAM`, simultaneous localisation and mapping, solves both at once: the robot moves, observes, and incrementally builds a map while tracking its position within the partially built map, with each improving the other. Every observation of a previously seen landmark tightens both estimates.

The characteristic difficulty is `loop closure`. A robot that travels a long circuit accumulates position error, so when it returns to its starting point its map says it is somewhere else. Recognising that this place is the same place already mapped, and then correcting the whole accumulated map to fit, is what makes the map globally consistent rather than locally plausible.

![Visual explanation of slam autonomy levels](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_slam_autonomy_levels.png)

## Degrees of Autonomy

"Autonomous" is used loosely, and the useful question is always what the machine handles and what a person handles.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Level</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">The machine does</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">A person does</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Teleoperated</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Executes commands</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Every decision, in real time</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Surgical robots, bomb disposal</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Supervised</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Runs a task, asks when unsure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Handles exceptions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Warehouse robots calling for help</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Conditionally autonomous</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Everything within a defined situation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Must be ready to take over</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Motorway driving assistance</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Fully autonomous</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Everything, including failures</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Nothing during operation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Driverless taxis in mapped areas</td>
    </tr>
  </tbody>
</table>

The third row hides the hardest human-factors problem in the field. A system that handles everything until it suddenly cannot, and then requires a person to take over within a second or two, is asking that person to remain alert for hours with nothing to do. People are extremely bad at this, and the failure is predictable rather than a matter of individual carelessness. This is why some developers skipped that level deliberately, judging a partially attentive human worse than no human.

Note also the qualifier on the last row. "In mapped areas" is doing a great deal of work: a system that is fully autonomous within a carefully surveyed and continuously updated region is a different proposition from one that works anywhere.

![Visual explanation of degrees of autonomy](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_section_degrees_of_autonomy.png)

## Why Physical Machines Learn Slowly

Almost everything in this course learns from data. Robots learn less, and the reasons are practical.

**Collecting data is slow and expensive.** A language model reads billions of documents at no marginal cost. A robot arm attempting a grasp takes several seconds, occupies a physical machine, and wears it out.

**Failures cost real money.** Exploration is how reinforcement learning works, and a robot exploring is a robot occasionally driving into a rack.

**Simulation helps and does not transfer cleanly.** Training in a physics simulation is fast, free, and safe, and the resulting behaviour often fails on real hardware because the simulation's friction, latency, and sensor noise are not the real ones. Closing that `reality gap` is an active research problem, usually approached by deliberately randomising the simulation so the learned behaviour cannot depend on any particular set of physical constants.

The consequence is that deployed robots are far more hand-engineered than deployed language or vision systems, with learned components sitting inside a scaffolding of explicitly programmed safety rules and controllers. That is an engineering judgment about consequences, not a lag in ambition.

![Visual explanation of why physical machines learn slowly](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_section_why_physical_machines_learn_slowly.png)

## Your Turn

Work out where the Bhiwandi robot's position error comes from and what to do about it.

Suppose its wheel encoders are accurate to within half a percent, and it travels 200 metres on a circuit. Compute the worst-case position error on returning to its start if it relies on dead reckoning alone. Then decide how frequently it needs to see a recognisable landmark to keep the error under ten centimetres, and say what that implies about how many floor markers the warehouse must install.

Then diagnose the third failure from the opening. The robot stops correctly for a person and then will not resume. Describe two quite different causes, one in perception and one in decision-making, and for each say what evidence in the robot's logs would distinguish it. Being able to separate "it cannot tell the person has gone" from "it can tell, and its resume rule is too cautious" is the difference between a week of work and a month.

Finally, take a position on the third row of the autonomy table. Argue that conditional autonomy with a human backup is the responsible way to deploy, then argue it is the least safe of the four levels. Both cases rest on real evidence about how people behave when supervising an automated system that is usually right.
