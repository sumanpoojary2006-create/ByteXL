## Introduction

Anitha finishes this course in 2026, and three weeks later an interviewer asks her about a technique that appears nowhere in it. She has not been taught badly. The technique did not exist when the material was written.

That is the awkward fact about a course like this one. Parts of what she has learned will still be accurate in 2036, and parts will read the way a 1987 textbook full of LISP and expert systems reads today: serious, careful, and about a world that moved on.

The difficulty is that nobody can reliably say which parts. Predictions in this field have a poor record in both directions. Practical machine translation was declared a few years away in the 1960s and took fifty. Systems producing fluent text on any subject were not expected by most researchers in 2015 and arrived within a decade.

So the useful thing this lesson can offer is not a forecast. It is a description of five directions the field is currently moving in, each with a reason it is being pursued and an honest note on what stands in its way, together with a way of assessing the next claim you encounter.

**Definition:** `Emerging trends` in AI are the directions of current research and investment, including `agentic AI`, `physical AI`, `edge AI`, AI for scientific discovery, and the drive towards more efficient models, each pursued for a specific reason and each facing specific unsolved problems.

![Visual explanation of introduction](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/13_section_introduction.png)

## Five Directions

**Agentic AI.** Moving from systems that answer to systems that act, planning several steps, calling tools, and completing tasks. The reason is straightforward commercial value: answering a question about an expense claim is worth far less than processing it. The obstacle is the arithmetic of reliability, since success rates multiply across steps and a twenty-step workflow built from steps that work nineteen times in twenty completes barely a third of the time. Progress here depends less on better models than on better error recovery, verification between steps, and restricting what an agent may do without confirmation.

**Physical AI.** Bringing the capability of recent software models into machines that move. The reason is that most human work is physical, and almost none of it has been touched by the last decade of progress. The obstacle is that data is slow and expensive to gather, failures break things, and behaviour learned in simulation does not transfer cleanly to real hardware. Robotics has no equivalent of the internet's supply of free training text, and manufacturing one is the central bet of several well-funded efforts.

**Edge AI.** Running models on the device rather than in a data centre. Four forces push this way: latency, since a vehicle cannot wait for a network round trip; privacy, since data that never leaves the device cannot leak from a server; cost, since inference at scale on somebody else's hardware is expensive; and connectivity, which matters disproportionately where useful AI must work in places with unreliable coverage. The obstacle is that capable models are large, so this depends on compression, distillation into smaller models, and hardware designed for the purpose.

**AI for science.** Using these methods to predict protein structures, screen materials, or search chemical space. The reason is that many scientific problems are search problems over spaces too large to explore by hand, which is what these methods are for. The obstacle is that a prediction is a hypothesis rather than a result, and the laboratory work needed to confirm it has not accelerated at the same rate. The bottleneck is moving from theory to verification.

**Efficiency.** Making models cheaper to train and run rather than larger. The reason is partly cost and partly that the readily available supply of high-quality training text is finite and substantially used. The obstacle is that the field's recent progress came largely from scale, and it is genuinely unclear how much remains available from better methods alone.

Note what these five have in common. **Only one of them is about making models more capable in the abstract.** The rest are about deploying capability that already exists into settings that resist it: multi-step tasks, physical machines, small devices, laboratories, and constrained budgets.

![Visual explanation of five emerging trends](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/13_five_emerging_trends_context_v4.png)

## What Is Not Improving

An honest account of direction requires naming what has stayed stubborn, because these are the constraints any forecast has to clear.

**Sample efficiency.** A person shown two photographs of an unfamiliar bird can recognise it afterwards. These systems still need orders of magnitude more examples, and the gap has narrowed far less than headline capability suggests.

**Reliable factuality.** Models remain fluent without being accurate, and the output still carries no signal distinguishing what is reliable from what is invented. Retrieval helps by supplying sources; it does not fix the underlying property.

**Robustness to adversarial input.** Small deliberate changes still flip confident decisions, and prompt injection remains unsolved rather than merely difficult.

**Causal understanding.** These systems learn associations. Distinguishing what causes what, which is what you need to predict the effect of an intervention, is largely outside what they do.

**Explaining a specific decision.** Post-hoc methods approximate, and the approximation can be wrong exactly where it matters.

Each of these has been described as nearly solved at some point in the last five years. None is.

![Visual explanation of assess ai claims](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/13_assess_ai_claims_context_v4.png)

## How to Assess a Claim

The most durable thing this lesson can leave you with is not a list of trends but a habit for reading the next announcement.

Six questions, in rough order of how quickly they dispose of a weak claim.

1. **What exactly was demonstrated, and on what?** A result on a benchmark is not a result in service. Ask what the evaluation set was and whether it resembles the intended use.
2. **Task or job?** Almost all real automation is task-level. A claim that a role is automated usually means a few of its dozens of tasks are.
3. **What is the failure rate, and what happens on failure?** A capability that works 90 percent of the time is transformative for drafting and unusable for anything unsupervised.
4. **What else has to be true?** Data availability, regulatory approval, hardware cost, and organisational willingness are usually the binding constraint rather than the model.
5. **Who benefits from you believing it?** Applies equally to those predicting transformation and those predicting collapse.
6. **What would change my mind?** Ask it of your own position too. A view that no evidence could shift is not a view about the world.

The third question deserves emphasis because it separates demonstrations from products more reliably than anything else. **The gap between a capability and a deployed system is mostly the gap between working usually and failing safely.**

![Visual explanation of how to assess a claim](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/13_section_how_to_assess_a_claim.png)

## What Is Likely to Remain True

Speculation is cheap, so it is worth ending with the parts of this course that seem most durable, and saying why.

The four capabilities that organised the whole course, perceiving, representing, reasoning, and acting, are a description of what an intelligent system has to do rather than of any technology. The specific methods will change; the decomposition will not.

The habits are more durable than the techniques. Measuring on data the model has not seen. Insisting on a baseline before believing a number. Choosing metrics that expose the failure that matters rather than flattering the system. Asking whether a feature will be available at prediction time. Noticing that a model optimises what was written down rather than what was meant. None of these depends on which architecture is current, and every one of them will still catch errors in a decade.

And the structural facts hold regardless of capability. A system trained on data inherits what is in that data. A model given nonsense returns confident nonsense. Reliability multiplies across steps. Whoever supplies the objective determines what gets optimised. These follow from what these systems are, not from how good they currently are.

![Visual explanation of what is likely to remain true](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/13_section_what_is_likely_to_remain_true.png)

## Your Turn

Take one specific claim from the last month, in any form, and put the six questions to it in writing.

Choose something concrete: a product announcement, a benchmark result, a prediction about employment in a particular occupation. Answer all six honestly, including the last one about yourself. Then write a single sentence stating what you now believe and with what confidence. Most claims survive this in a much weaker form than they were made, and a few survive intact, which is the point of doing it rather than reacting.

Then pick the direction from the five that most affects the work you expect to do, and write down the specific obstacle standing in its way, not the general one. If your answer is "it needs to get better", you have not looked closely enough. The obstacles named above are concrete: reliability compounding across steps, the absence of a free supply of physical-world training data, model size against device memory, laboratory verification not accelerating.

Finally, do the exercise that makes this course useful in five years. Write down three things you believe about AI today, and for each, the observation that would show you were wrong. Keep it. Whether the predictions were right will matter less than whether you specified them clearly enough to find out, which is the difference between having a view and having an opinion.
