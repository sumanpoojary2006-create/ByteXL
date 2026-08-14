## Introduction

Meera is three weeks from her internship deadline, and she has thirty tabs open on a hiring portal, every one of them titled some version of "AI Intern". She assumed they would want roughly the same things. They do not.

The first listing wants OpenCV and experience with image annotation. The second wants spaCy, tokenisation, and a portfolio of text classification work. The third wants ROS, familiarity with sensor fusion, and a willingness to work in a lab with actual hardware. The fourth wants nothing but SQL and scikit-learn. Meera stares at them and asks the reasonable question: are these even the same field?

They are, in the way that cardiology and dermatology are both medicine. Artificial intelligence is not a single technique that gets applied to different problems. It is a family of specialised areas, each shaped by a different kind of problem, each with its own tools, its own vocabulary, and its own idea of what "hard" means. Those specialised areas are the **branches of artificial intelligence**, and knowing which branch you are standing in is the difference between asking a useful question and a confused one.

**Definition:** The `branches of artificial intelligence` are the specialised subfields of AI, each defined by the kind of problem it tackles, from learning patterns in data to understanding language, interpreting images, representing knowledge, planning actions, and controlling physical machines.

![Opening scene: Meera is three weeks from her internship deadline, and she has thirty tabs open on a hiring portal, every one of them titled some version of "AI Intern".](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_section_introduction.png)

## Why the Branches Divide the Way They Do

Most course material lists the branches without saying what organises the list, which makes them feel arbitrary. They are not arbitrary. The branches fall into four groups, and once you see the grouping the whole map becomes memorable.

The four groups are these:

1. **Defined by how the system acquires knowledge:** machine learning and deep learning.
2. **Defined by what kind of raw input the system must make sense of:** computer vision and natural language processing.
3. **Defined by how the system stores facts and works out consequences:** knowledge representation, expert systems, and planning.
4. **Defined by having to act in the physical world:** robotics.

Learn, perceive, reason, act. Those are the same four capabilities that define an intelligent system in the first place, and the branches of AI are simply what happens when researchers specialise in one of them for forty years.

![Visual explanation of why the branches divide the way they do](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_section_why_the_branches_divide_the_way_they_do.png)

## The Learning Branches: Machine Learning and Deep Learning

`Machine learning` is the branch concerned with systems that improve at a task by processing data rather than by being reprogrammed. Its object of study is the learning process itself: how to fit a model to examples, how to tell whether the model has genuinely learned something or merely memorised, and how to make it work on data it has never seen.

`Deep learning` is the part of machine learning that uses neural networks with many layers, and whose defining trick is that it learns useful representations of the raw input as part of learning the task.

Here is the most common misconception among beginners, worth correcting immediately. Machine learning and deep learning are not two siblings sitting beside each other. They are nested. Deep learning is a subset of machine learning, which is a subset of artificial intelligence. Every deep learning system is a machine learning system; the reverse is not true. A decision tree predicting loan defaults is machine learning and is not deep learning, and there is nothing second-rate about that. On tabular data of the kind most businesses actually hold, simpler machine learning models frequently outperform neural networks while being faster to train and far easier to explain.

Note also that these two branches cut across all the others. Computer vision, natural language processing, and robotics all use deep learning today. That is exactly why the branches are not tidy boxes.

![Visual explanation of the learning branches: machine learning and deep learning](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_section_the_learning_branches_machine_learning_and_deep_learning.png)

## The Perception Branches: Computer Vision and Natural Language Processing

These two branches exist because raw sensory input is not meaning, and the gap between them is enormous.

`Computer vision` is the branch concerned with extracting meaning from images and video. To appreciate its difficulty, remember what a photograph actually is to a computer: a grid of numbers, perhaps two million of them, each recording a brightness value. Nothing in that grid announces "this region is a face". Worse, the same face produces completely different numbers under different lighting, at a different angle, at a different distance, or partly hidden behind a hand. Human vision handles all of this without noticing. The central technical problem of computer vision is this invariance problem: recognising that wildly different arrays of numbers refer to the same thing.

`Natural language processing` is the branch concerned with understanding and generating human language, and its central difficulty is ambiguity. Consider the sentence "the trophy would not fit in the suitcase because it was too big". Every competent speaker of English knows "it" means the trophy. Change one word to "too small" and "it" now means the suitcase. Nothing in the grammar tells you this. You resolve it using knowledge about physical objects and containers. Language is dense with such gaps, which the speaker expects the listener to fill from knowledge of the world, and filling them is the work.

![Visual explanation of the perception branches: computer vision and natural language processing](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_section_the_perception_branches_computer_vision_and_natural_language_processing.png)

## The Reasoning Branches: Knowledge Representation, Expert Systems, and Planning

These three form the classical core of AI, and they are frequently underestimated by students who assume everything modern is a neural network. They are not historical curiosities. They run inside systems you use daily.

`Knowledge representation` studies how to encode facts about the world in a form a machine can compute over. The problem is subtler than it sounds. Storing "Bengaluru is in Karnataka" is easy. Storing it so that a machine can also work out that a person in Bengaluru is in India, and is therefore subject to Indian law, requires structure: categories, relationships, inheritance, and rules about what follows from what. This branch produced semantic networks, ontologies, and the knowledge graphs behind modern search engines.

`Expert systems` is the branch that captures the decision-making of human specialists as an explicit rule base paired with an inference engine that applies those rules to a case. This branch is why your loan application is checked against eligibility rules that a compliance officer can read and audit, rather than against a neural network nobody can interrogate.

`Planning` is the branch concerned with choosing an ordered sequence of actions that transforms a starting state into a goal state. Recognising a parcel is perception; working out that the robot must first move to aisle four, then lower its arm, then grip, then reverse, then travel to packing, is planning. Every logistics system, every automated warehouse, and every AI agent that chains together tool calls is doing planning.

![Visual explanation of the reasoning branches: knowledge representation, expert systems, and planning](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_section_the_reasoning_branches_knowledge_representation_expert_systems_and_plann.png)

## The Acting Branch: Robotics

`Robotics` is the branch concerned with machines that sense and act in the physical world, and it is different from every other branch in one decisive respect: it cannot ignore physics.

A language model that produces a poor sentence wastes a moment. A robot arm that miscalculates by two centimetres breaks something. Physical systems face noisy sensors, unreliable actuators, unforgiving real-time deadlines, and consequences that cannot be undone by pressing a back button.

Robotics also delivers one of the most useful lessons in the whole of AI, known as Moravec's paradox. The tasks humans find intellectually demanding, such as playing grandmaster chess or integrating a difficult function, turned out to be comparatively easy to automate. The tasks any toddler performs without thought, such as picking up an unfamiliar object, walking across an uneven floor, or recognising a friend's face in a crowd, turned out to be extraordinarily hard. The reason is evolutionary: perception and movement were refined over hundreds of millions of years and run below conscious awareness, while abstract reasoning is a recent and shallow layer. Whenever your intuition says a task should be easy for a machine because it feels easy to you, that intuition is probably wrong.

![Visual explanation of the acting branch: robotics](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_section_the_acting_branch_robotics.png)

## The Branches at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Branch</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">The question it answers</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">A system you have met</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Machine Learning</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How can a system improve at a task from data instead of instructions?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Credit card fraud scoring</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Deep Learning</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How can a system learn what to measure, as well as what to conclude?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Face unlock on a phone</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Computer Vision</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How can a system extract meaning from pixels?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Automatic number plate reading at a toll gate</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Natural Language Processing</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How can a system understand and produce human language?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Autocomplete and translation</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Knowledge Representation</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How should facts be stored so consequences can be derived?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The knowledge panel beside a search result</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Expert Systems</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How can a specialist's decision rules be captured and audited?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Loan eligibility checks</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Planning</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What sequence of actions reaches the goal?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Delivery route and warehouse pick sequencing</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Robotics</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How can a machine sense and act reliably in the physical world?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A warehouse picking robot</td>
    </tr>
  </tbody>
</table>

![Visual explanation of branches of ai](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_branches_of_ai_context_v4.png)

## How Many Branches Fit Inside One Left Turn

Branches are useful for organising a syllabus. Real systems ignore them completely. Watch a self-driving car make a single unprotected left turn across oncoming traffic, and count.

1. **Computer vision** turns raw camera, radar, and lidar data into objects: a scooter at eleven o'clock, a pedestrian at the kerb, a lane marking, a signal showing amber.

2. **Deep learning** is doing that recognition work, and it also feeds a prediction model estimating where the scooter will be in three seconds, since a turn must be planned against the future, not the present.

3. **Knowledge representation** supplies the structured facts the perception system cannot see: that this junction permits a left turn on amber, that the road ahead is one-way, that a school zone begins forty metres later.

4. **Expert system rules** enforce the non-negotiable constraints that no learned model is trusted to decide, such as never entering an occupied crossing.

5. **Planning** chooses the action sequence: hold, allow the scooter to clear, then turn along a specific trajectory at a specific speed.

6. **Robotics** executes it, converting that trajectory into steering, throttle, and braking commands, correcting continuously as the tyres respond slightly differently from the model's prediction.

7. **Machine learning** closes the loop overnight, as every difficult junction the fleet encountered becomes training data and the next version turns better.

Seven branches, one left turn, a few seconds. This is what people mean when they say a real AI system is an integration problem, and it is why an engineer who understands only one branch can build a component but cannot build a system.

![Visual explanation of branches collaboration](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_branches_collaboration.png)

## Your Turn

Take one AI-powered product you use often, and reverse-engineer it into branches. Write down each branch you believe is involved, and beside it the specific evidence in your own experience that made you think so.

Then do the harder half. For each branch you listed, name the input it receives and the output it produces, and check that the outputs actually connect: does the output of the perception branch look like something the reasoning branch could consume? If two of your branches do not connect, you have either missed a branch in between or misjudged what one of them does. Working this out for a food delivery app is a genuinely instructive hour, because the answer involves at least four branches and most people initially guess one.
