## Introduction

In a second-hand bookshop on Avenue Road, Rohit picks up a hardback called *Principles of Artificial Intelligence*, printed in 1987. He expects it to be a dusty version of what he is studying now. Instead he finds something stranger: four hundred pages about logic, rules, search trees, and a programming language called LISP, and not one mention of training data, neural networks, or models. The index has no entry for "learning".

This is the same subject, taught seriously, by serious people, thirty-eight years ago. Yet a student from that classroom and a student from Rohit's would struggle to agree on what the subject even is. That is not because the older book was wrong. It is because the field has changed its mind, more than once, about a single foundational question: **where does a machine's knowledge come from?**

Every era of AI is organised around one answer to that question. When an answer runs out of room, the field abandons it, adopts a new one, and rebuilds almost everything on top. Those successive answers are called **AI paradigms**, and the entire history of the subject is the story of the field moving from "we write the knowledge down" to "the machine works the knowledge out".

**Definition:** An `AI paradigm` is a shared assumption about where a system's intelligence comes from, which in turn determines how such systems are built, what they are good at, and how they fail.

![Visual explanation of ai paradigms 1987 vs today](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_ai_paradigms_1987_vs_today_draft.png)

## What a Paradigm Actually Is

It helps to be precise, because "paradigm" is a word that often gets used to mean nothing much.

A paradigm is not a technique or an algorithm. It is the belief underneath the techniques. Once a research community accepts a particular belief about the source of intelligence, everything else follows almost automatically:

- Which problems look important.
- Which problems look like distractions.
- What counts as progress.
- Which tools get built.
- Which people get hired.

Across seventy years, AI has held six such beliefs in sequence. Each one produced genuine successes, hit a wall it could not climb, and handed the field over to its successor. Crucially, none of them vanished completely. Rules still run inside your bank's transaction checks; probability still runs inside your phone's keyboard. The paradigms accumulated more than they replaced.

![Visual explanation of what a paradigm actually is](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_section_what_a_paradigm_actually_is.png)

## Symbolic AI: Intelligence as Rules and Logic

The field's founding meeting, a summer workshop at Dartmouth College in 1956, gave the subject its name and its first paradigm. The proposal behind that workshop rested on a bold conjecture: every aspect of intelligence can be described so precisely that a machine can be made to simulate it.

The answer this paradigm gave to our foundational question was direct. Knowledge comes from us. Human experts write down facts and rules in a formal language, and the machine applies logic to them. Intelligence, on this view, is symbol manipulation: represent the world as symbols, define rules for transforming those symbols, and reasoning falls out of the transformations.

Early results were genuinely thrilling. Programs proved mathematical theorems, solved logic puzzles, and played respectable chess. If a machine could prove a theorem in 1956, researchers reasoned, general intelligence was surely a decade or two away.

It was not. Symbolic AI ran into two walls that it never got past.

1. **Combinatorial explosion.** Reasoning by searching through possibilities works beautifully in a puzzle with a hundred states, and collapses entirely in a world with billions of them.

2. **Common sense could not be written down.** Consider the everyday fact that a person dropped in water becomes wet, that wet clothes are uncomfortable, and that uncomfortable people usually change out of them. A child knows millions of such facts. Nobody could enumerate them, and a system that lacks them makes absurd mistakes in any situation no rule anticipated.

By the mid-1970s, funding collapsed into the first AI winter.

![Visual explanation of symbolic ai: intelligence as rules and logic](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_section_symbolic_ai_intelligence_as_rules_and_logic.png)

## Expert Systems: Narrowing the Ambition, and Hitting a Wall

The 1980s response was clever. If common sense is impossible to write down, stop trying. Restrict the machine to a narrow domain where the knowledge is finite and the experts are identifiable.

This produced **expert systems**: programs holding a few hundred to a few thousand hand-written rules covering one specialised task. MYCIN, built at Stanford, diagnosed bacterial blood infections and recommended antibiotics from roughly six hundred rules, and evaluations found its recommendations comparable to those of specialist physicians. In industry, a system called XCON configured the components of Digital Equipment Corporation's computer orders, a fiddly task that humans regularly got wrong, and saved the company tens of millions of dollars a year. For the first time, AI made money.

Then the paradigm hit its own wall, and it is worth understanding exactly what it was, because the same wall reappears today whenever someone proposes solving a problem with rules. Three things went wrong.

1. **The knowledge acquisition bottleneck.** Extracting rules from experts turned out to be painfully slow, because experts are usually unable to articulate what they know.

2. **Brittleness.** The systems performed well inside their domain and failed without warning just outside it, with no sense of their own limits.

3. **Maintenance.** In a base of two thousand interacting rules, adding one rule can silently break several others.

By the early 1990s the market for these systems collapsed, and a second AI winter set in.

![Visual explanation of expert systems: narrowing the ambition, and hitting a wall](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_section_expert_systems_narrowing_the_ambition_and_hitting_a_wall.png)

## The Statistical Turn: Being Usefully Right Instead of Provably Right

The recovery began with a change of temperament rather than a new algorithm.

Symbolic AI had aimed for certainty: given true facts and valid rules, conclusions are guaranteed. But the real world does not supply true facts. It supplies noisy microphone recordings, blurred photographs, and ambiguous sentences. Researchers in the 1990s made a concession that the previous generation would have considered a defeat: stop demanding certainty, and start computing probabilities.

Speech recognition was the proving ground. Decades of effort encoding the grammar of English into rules had produced disappointing systems. Statistical models that simply counted, across enormous quantities of recorded speech, which sound sequences and which word sequences occur most often, outperformed them convincingly. The lesson was uncomfortable and important: for messy real-world problems, a model that is usefully right most of the time beats a model that is provably right in a world that does not exist. Spam filters, which score the probability that a message is junk rather than applying fixed rules, come from the same shift and remain in use today.

![Visual explanation of the statistical turn: being usefully right instead of provably right](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_section_the_statistical_turn_being_usefully_right_instead_of_provably_right.png)

## Machine Learning: Writing Programs That Write the Rules

Statistical AI opened the door; **machine learning** walked through it and inverted the entire programming relationship.

In ordinary programming, you supply the rules and the data, and the computer produces answers. In machine learning, you supply the data and the answers, and the computer produces the rules. Show a system fifty thousand loan applications together with which ones defaulted, and it derives the pattern that separates them, a pattern no officer ever stated and possibly could not state.

This directly dissolved the knowledge acquisition bottleneck. Nobody had to interview experts, because the examples carried the knowledge. Through the 1990s and 2000s, techniques such as decision trees, support vector machines, and ensemble methods spread into credit scoring, recommendation, and fraud detection.

One limitation remained, and it was substantial. These systems learned relationships between features, but humans still had to decide what the features were. To detect fraud you first had to decide that transaction amount, time of day, and distance from the last transaction were the things worth measuring. This work, called feature engineering, was skilled, slow, and domain-specific. And for perception problems it was close to hopeless: nobody could say which measurable features distinguish a photograph of a cat from a photograph of a dog.

![Visual explanation of ai paradigms programming to generative](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_ai_paradigms_programming_to_generative_draft.png)

## Deep Learning: Learning the Features as Well

The breakthrough came in 2012, at an annual competition where systems classify photographs into a thousand categories. A neural network called AlexNet won by a margin so wide that the entire field changed direction within a year.

What made it matter was not accuracy alone. It was that nobody had told AlexNet what to look for. Given only raw pixels and labels, the network discovered its own features, and those features turned out to be layered: early layers responded to edges, middle layers to textures and shapes, later layers to recognisable objects. **Deep learning** had absorbed feature engineering into the learning process itself.

This paradigm demanded a price the earlier ones had not: enormous quantities of labelled data and enormous computing power, which is precisely why it arrived in 2012 and not 1992. The mathematics of neural networks had been available for decades. The internet's images and the graphics processor were what had been missing.

![Visual explanation of deep learning: learning the features as well](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_section_deep_learning_learning_the_features_as_well.png)

## Generative AI: From Recognising to Producing

Through all five paradigms above, AI systems mostly answered questions about things that already existed. Which category is this image? Will this customer default? Is this message spam.

A neural architecture published in 2017, the transformer, changed the target. Trained on very large quantities of text to predict what comes next, and then scaled up by orders of magnitude, these systems began producing new text, images, audio, and code rather than merely labelling existing examples. **Generative AI** is the paradigm in which the output is created content rather than a classification, and its most visible form, the large language model, reached the public with ChatGPT in late 2022.

![Visual explanation of generative ai: from recognising to producing](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_section_generative_ai_from_recognising_to_producing.png)

## Three Machines That Mark the Eras

Three famous systems, spread across twenty-five years, make the whole progression concrete. All three beat humans at something difficult. What differs is where each one's knowledge came from.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">System</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Where its knowledge came from</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Paradigm</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Deep Blue</strong> beats Kasparov at chess, 1997</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Grandmasters hand-tuned the scoring function; custom hardware searched roughly 200 million positions per second</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Symbolic search</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>AlphaGo</strong> beats Lee Sedol at Go, 2016</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Learned position judgment from human games, then improved by playing millions of games against itself</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Deep learning with search</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>ChatGPT</strong> reaches the public, 2022</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Absorbed patterns from vast quantities of text, with no task-specific rules written for any particular question</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Generative AI</td>
    </tr>
  </tbody>
</table>

The reason Go mattered more than chess is worth stating. Go has vastly more possible positions than chess, so Deep Blue's approach of searching hard and scoring positions with a human-written function was simply unavailable. AlphaGo had to acquire judgment about which positions look promising, and it acquired it from experience rather than from grandmasters. Human knowledge went from being the system's foundation to being merely its starting point.

![Visual explanation of three machines that mark the eras](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_section_three_machines_that_mark_the_eras.png)

## The Paradigms at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Paradigm</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Source of knowledge</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Wall it hit</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Symbolic AI</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Logic and rules written by humans</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Combinatorial explosion; common sense cannot be written down</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Expert Systems</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rules extracted from domain experts</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Slow to build, brittle at the edges, painful to maintain</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Statistical AI</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Probabilities estimated from observed frequencies</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Limited to problems that could be framed probabilistically by hand</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Machine Learning</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Patterns learned from labelled examples</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Humans still had to choose the features by hand</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Deep Learning</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Features and patterns both learned from raw data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Needs vast data and compute; decisions are hard to explain</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Generative AI</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Patterns absorbed at scale, then used to produce new content</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fluent output is not necessarily true output; currently being tested</td>
    </tr>
  </tbody>
</table>

![Visual explanation of ai paradigms timeline](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_ai_paradigms_timeline_draft.png)

## Your Turn

Build a one-page timeline of AI from 1956 to the present. Place these eight markers on it and write one line under each: the Dartmouth workshop, the first AI winter, MYCIN, the second AI winter, the statistical turn in speech recognition, AlexNet in 2012, AlphaGo in 2016, and ChatGPT in 2022.

Then answer the question that makes the timeline worth building. For each of the two AI winters, write down what the field had promised, what it actually delivered, and which specific limitation caused the gap. Finally, look at the last row of the table above and ask yourself honestly: what would a third AI winter look like, and what would have to go wrong for it to happen? You do not need a confident answer. You need the habit of asking, because every generation of AI researchers has believed its own paradigm was the last one needed.
