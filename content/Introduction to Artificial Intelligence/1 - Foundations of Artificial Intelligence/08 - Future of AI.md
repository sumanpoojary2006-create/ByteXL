## Introduction

In 2019, Lakshmi's seniors submitted a final-year project they were rightly proud of: a chatbot for their department office. Six months of work, several hundred hand-written intents, a carefully assembled set of training phrases, and a demo that ran without crashing. It won them a good grade and one of them an internship.

In 2024, a second-year student rebuilt the same thing over a weekend, mostly by writing careful instructions to a model that somebody else had already trained.

It is worth being precise about what happened there, because the obvious readings are both wrong. The seniors were not incompetent; their approach was the correct one available to them. The junior is not more talented. What changed is that the expensive part of the work, teaching a system to understand language at all, stopped being something each team did for itself and became something you could simply use. The ground moved underneath the skill.

This is what makes the **future of AI** worth studying rather than merely speculating about. The useful question is not which product will exist in five years. It is which parts of the work are about to stop being work, because that is what actually reshapes an industry, and there are five shifts currently doing it.

**Definition:** The `future of AI` refers to the emerging directions reshaping how intelligent systems are built and deployed: foundation models, multimodal AI, agentic AI, physical AI, and edge AI, each of which changes what is expensive and what is cheap in building an intelligent system.

![Visual explanation of introduction](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/08_section_introduction.png)

## Why the Ground Moved: Foundation Models

A `foundation model` is a large model trained once on very broad data, which is then adapted to many different downstream tasks rather than being built for any one of them.

The inversion this causes is economic before it is technical. Under the older approach, every task required its own dataset, its own model, and its own team: a sentiment model, a summarising model, a classification model, each built from nothing. Under the foundation model approach, one organisation pays the enormous cost of training a broad model, and everyone else adapts it, sometimes by fine-tuning it on a modest amount of task-specific data and sometimes by nothing more than describing the task in the instructions. Lakshmi's junior did the second thing.

The consequence is that the barrier to building an AI application has collapsed while the barrier to building an AI *model* has risen sharply. This is genuinely double-edged. A two-person team in Hubballi can now build things that required a research lab in 2018. At the same time, the capability underneath most of those applications is trained by a small number of very well-funded organisations, which concentrates a great deal of influence over what these systems can do, what they refuse to do, and who can afford to use them. That concentration is one of the more consequential facts about the current moment, and it is rarely mentioned in the same breath as the excitement.

![Visual explanation of why the ground moved: foundation models](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/08_section_why_the_ground_moved_foundation_models.png)

## Multimodal AI

`Multimodal AI` refers to systems that take in and reason across more than one kind of data at once, such as text together with images, audio, or video.

The reason this matters is not that it adds features. It addresses one of the specific limitations identified earlier in this unit: a system trained only on text has learned how sentences about the world tend to continue, without ever encountering the world. Adding vision and audio does not solve grounding, but it narrows the gap, because the system now associates the phrase "the tap is leaking" with what a leaking tap looks like.

The practical difference shows up in problems that were previously awkward to express. A farmer photographs a leaf, describes the weather over the past fortnight in Kannada, and asks what is wrong. A technician films a vibrating machine and asks whether it is safe to run until Friday. Neither request fits a single-modality system, and both are ordinary human requests.

![Visual explanation of multimodal ai](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/08_section_multimodal_ai.png)

## Agentic AI

`Agentic AI` refers to systems that pursue a multi-step goal by planning, using external tools, retaining relevant information across steps, and acting rather than only producing an answer.

The distinction is between a system that tells you how to do something and a system that does it. Ask a conventional model to reconcile two spreadsheets and it explains the procedure. Ask an agent and it opens the files, compares them, writes the output, and reports what it found. Its outputs are actions in the world.

That is precisely why this shift raises the stakes so sharply, and there is a piece of arithmetic every student should carry. Suppose an agent performs each individual step correctly ninety-five percent of the time, which sounds excellent. Chain ten such steps and the probability that the whole task completes correctly is about sixty percent. Chain twenty and it is roughly a third. Reliability compounds downward, so agent systems fail far more often than their per-step accuracy suggests, and this, rather than intelligence, is currently the binding constraint on deploying them for anything consequential. Notice also that an incorrect answer can be ignored, while an incorrect action may have already sent the email.

![Visual explanation of agentic ai](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/08_section_agentic_ai_simple_v2.png)

## Physical AI

`Physical AI` is the application of the foundation model approach to machines that sense and act in the physical world, aiming for robots that generalise across tasks rather than being programmed for one.

Robotics has lagged the rest of AI for a reason worth understanding. Foundation models became possible because the internet contained enormous quantities of text and images. There is no comparable corpus of physical interaction. Nobody has a billion recorded examples of a hand picking up an unfamiliar object on a cluttered surface, because that data has to be generated by actually doing it, one attempt at a time, with hardware that wears out.

The current strategies address exactly this gap:

- **Simulation.** Train in a physics simulation, then transfer to real machines.
- **Teleoperation.** Learn from recordings of humans driving robots directly.
- **Borrowed world knowledge.** Reuse what language and vision models already hold, so the robot at least knows what a mug is and what it is for.

Progress here is real but slower than in software, and Moravec's paradox is still collecting its debt.

![Visual explanation of physical ai](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/08_section_physical_ai.png)

## Edge AI

`Edge AI` means running models directly on the device, a phone, a camera, a vehicle, a sensor, rather than sending data to a server.

Four forces push in this direction.

1. **Latency.** A vehicle cannot wait for a network round trip to decide whether to brake.
2. **Privacy.** Data that never leaves the device cannot be leaked from a server, which is a genuinely strong answer to several of the concerns raised earlier in this unit.
3. **Cost.** Inference at scale on someone else's hardware is expensive.
4. **Connectivity.** This matters disproportionately in a country where a great deal of useful AI needs to work in places with unreliable data coverage, from a field to a rural clinic.

The tradeoff is honest and unavoidable: a model that fits on a phone is much smaller than one running in a data centre, so the engineering discipline here is about compressing models while losing as little capability as possible. Expect hybrid designs, where routine cases are handled on the device and only the difficult ones are sent onwards.

![Visual explanation of edge ai](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/08_section_edge_ai.png)

## The Five Directions at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Direction</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it changes</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Its main open problem</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Foundation models</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Build once, adapt many times, instead of one model per task</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Capability concentrated in a few organisations</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Multimodal AI</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One system reasons across text, images, audio, and video together</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Still not genuine grounding in the physical world</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Agentic AI</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Outputs become actions, taken over many steps</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reliability compounds downward across a chain of steps</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Physical AI</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Robots that generalise instead of being programmed per task</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No internet-scale data for physical interaction</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Edge AI</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Models run on the device rather than in a data centre</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fitting useful capability into a small model</td>
    </tr>
  </tbody>
</table>

![Visual explanation of future of ai](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/08_future_of_ai.png)

## How to Think About Predictions

You will be handed confident forecasts about AI for the rest of your career, and the single most valuable thing this lesson can give you is a way to assess them.

Start with the observation, usually credited to the futurist Roy Amara, that people tend to overestimate what a technology will do in a couple of years and underestimate what it will do over a couple of decades. Both halves are important. The short-term overestimate happens because capability is visible and deployment friction is not: a demonstration takes an afternoon, while integrating a system into an organisation's actual workflow, satisfying its regulators, earning the trust of the people who must use it, and handling the awkward twenty percent of cases takes years. The long-term underestimate happens because a technology's second-order effects, the new practices and institutions built on top of it, are almost impossible to imagine in advance.

Then ask three questions of any specific claim.

1. **What exactly is being automated, a task or a job?** Almost all real automation is task-level, which reshapes work rather than eliminating it, and a role is usually a bundle of dozens of tasks with very different exposure.

2. **What has to be true for this to work, besides the model?** Data availability, regulatory approval, hardware cost, and organisational willingness are usually the constraint.

3. **Who is making the claim, and what do they gain if you believe it?** This is not cynicism, it is basic source assessment, and it applies equally to those predicting utopia and those predicting catastrophe.

![Visual explanation of assessing future claims](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/08_assessing_future_claims.png)

## Your Turn

Choose one profession you might realistically enter and analyse it honestly against these five directions.

List ten concrete tasks somebody in that role performs in a week, described specifically enough that a stranger could picture them. For each task, mark which of the five directions could affect it and how, then rate whether it is likely to be automated, made faster with a human still deciding, or left essentially untouched because it depends on physical presence, accountability, or trust.

Then write the paragraph that makes this exercise worth doing. Given your ten rows, describe what the role looks like in ten years, what proportion of the current work remains, what new work appears that does not exist today, and which skills you would therefore invest in now. Keep it. Reread it in a year and mark what you got wrong, because being wrong in a way you can inspect is how forecasting is actually learned.
