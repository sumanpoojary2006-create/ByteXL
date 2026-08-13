## Introduction

Ramesh has run the service desk at a diesel generator dealership in Nashik for thirty-one years, and in March he retires.

The management is not worried about the paperwork. They are worried about a specific thing Ramesh does. A customer rings to say the generator is running rough, and Ramesh asks four questions, in an order that seems to change every time, and then says something like "check the fuel filter, and if that is clean, the lift pump is going". He is right about nine times in ten. Nobody else at the dealership is right even half the time, including two engineers with better formal qualifications than his.

His manager sits with him for a week trying to write it all down, and produces eleven pages that are almost useless. Ramesh keeps saying things like "well, it depends on how it sounds" and "if the customer is from the sugar belt it is usually different". The knowledge is real, it produces correct answers daily, and it is about to walk out of the building.

The attempt to stop that happening, by putting an expert's knowledge into a machine in a form the machine can actually use, is what produced the first commercially successful AI systems. They are called **knowledge-based systems**.

**Definition:** A `knowledge-based system` is an AI system that separates what it knows, held explicitly in a `knowledge base`, from how it reasons, carried out by a general-purpose `inference engine`, so that the knowledge can be inspected, extended, and corrected without rewriting the program.

![Visual explanation of introduction](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_section_introduction.png)

## The Two Halves

The whole architecture rests on one split, and if you take a single thing from this lesson it should be this one.

- **The knowledge base** holds what the system knows about the domain: the facts, and the rules relating them. For Ramesh's dealership, it would hold things like "if fuel pressure is low and the filter is clean, the lift pump is suspect".
- **The inference engine** holds how to reason. It matches rules against known facts, works out which conclusions follow, and adds them. It contains no diesel knowledge at all.

The inference engine is deliberately, almost aggressively, ignorant. Point the same engine at a knowledge base about bank loan eligibility and it works just as well, because it never knew anything about generators in the first place. It only knows how to apply rules.

Two supporting components complete the usual picture. The **working memory** holds the facts about the case currently being handled, which for the dealership means this particular customer's symptoms, kept separate from the general knowledge that applies to every case. And the **explanation facility** answers questions about the system's own reasoning, which is discussed further below because it is more important than it first appears.

![Visual explanation of kbs anatomy](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_kbs_anatomy.png)

## Why the Separation Matters

It would be entirely possible to write Ramesh's knowledge as ordinary program logic, a long cascade of nested if-statements inside a function. It would even run faster. It is nonetheless the wrong design, for four reasons that are worth knowing because they apply far beyond expert systems.

1. **Knowledge can change without the program changing.** A new generator model arrives with a different fault pattern. In a knowledge-based system, somebody adds three rules. In a program of nested if-statements, somebody edits control flow that many other cases depend on, and hopes.

2. **The domain expert can read it.** Ramesh cannot read Python. He can read "if fuel pressure is low and the filter is clean then suspect the lift pump", and more importantly he can tell you it is wrong and how. Knowledge trapped inside code can only be reviewed by programmers, who are not the people who know whether it is correct.

3. **The reasoning is reusable.** One inference engine serves every domain the organisation ever needs. Knowledge baked into control flow is reusable for nothing.

4. **The system can explain itself.** Because the rules are data rather than instructions, the system can report which ones it used. A cascade of if-statements has no record of why it took the branch it took.

The general principle underneath all four is worth stating plainly: **knowledge that is data can be inspected, changed, and explained, whereas knowledge that is code cannot.** This is the same instinct that shows up throughout software engineering as the preference for configuration over hard-coding, and expert systems were among the first places it was taken seriously.

![Visual explanation of why the separation matters](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_section_why_the_separation_matters.png)

## The Explanation Facility

The third component is the one students skip, and it is the one that decides whether a system gets used.

A knowledge-based system can typically answer two questions about itself. Asked **why** it wants some piece of information, it can say which rule it is currently trying to apply and what that rule still needs. Asked **how** it reached a conclusion, it can replay the chain of rules that fired.

Consider the difference this makes to Ramesh's replacement. A system that says "replace the lift pump" is an instruction from a black box, and a technician who has been doing this for two years will simply ignore it when it conflicts with his instinct. A system that says "replace the lift pump, because fuel pressure is low, the filter has been reported clean, and low pressure with a clean filter indicates lift pump failure" is making an argument. The technician can check each step, and can say "actually the filter is not clean, I only replaced it last month and this fuel is filthy", which corrects the input rather than overriding the output.

This is also what makes the knowledge maintainable. When the system is wrong, the explanation identifies exactly which rule was wrong, so the fix is local and specific.

![Visual explanation of the explanation facility](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_section_the_explanation_facility.png)

## Case Study: MYCIN

The system that established the whole field was built at Stanford in the 1970s to diagnose bacterial infections of the blood and recommend antibiotic therapy.

MYCIN held roughly six hundred rules acquired from infectious-disease specialists. It conducted a consultation by asking a physician questions, one at a time, each chosen because some rule needed the answer. When it finished it recommended a therapy, and it could explain every step of its reasoning on request.

Four aspects of it are worth knowing.

- **It handled uncertainty.** Medical rules are not certain, so MYCIN attached a numerical confidence to each rule and combined these as it reasoned. This is a rough approach compared with later probabilistic methods, and it was an honest acknowledgement that real expertise is not a set of certainties.
- **It performed well.** In formal evaluations where its recommendations were assessed blind against those of specialists, it did comparably to them and better than junior doctors.
- **It never treated a patient.** Not because the diagnosis was inadequate, but because of the surrounding practicalities: who is liable when a machine's recommendation harms someone, and the fact that in the 1970s a physician would have had to sit at a terminal answering questions for half an hour with no hospital system to draw the data from automatically.
- **Its architecture outlived it.** The engine was separated from the medical knowledge so cleanly that the knowledge could be stripped out entirely, leaving a general-purpose shell that others could load with their own rules. That idea, the empty expert system waiting to be filled, is what made the technology commercial.

The honest lesson of MYCIN is one that recurs constantly in AI. **Technical adequacy is not deployment.** A system can be measurably as good as a specialist and still not be used, for reasons of liability, workflow, and trust that have nothing to do with its accuracy.

![Visual explanation of mycin expert system](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_mycin_expert_system.png)

## Why Expert Systems Faded, and What Survived

In the 1980s these systems became a real industry, and by the early 1990s that industry had collapsed. The reasons are the ones a careful reader can already predict from Ramesh's eleven useless pages.

Getting the knowledge out of the expert was extraordinarily slow, because experts cannot articulate most of what they know. Ramesh saying "it depends on how it sounds" is not evasion; it is an accurate report that his judgment includes things he has no words for. The resulting systems were brittle at the edges of their domain and had no sense of their own limits. And a knowledge base of two thousand interacting rules eventually became something no single person understood, so every change risked breaking something invisible.

But it is a mistake to file this away as a dead technology, and the mistake is common. The architecture is running everywhere, usually under a different name.

- **Business rules engines** in banking and insurance are expert systems, and they are used precisely because eligibility decisions must be auditable and changeable by non-programmers.
- **Clinical decision support** built into hospital software checks prescriptions against interactions and allergies using exactly this design.
- **Configuration systems** that validate whether a chosen set of components will actually work together are direct descendants of the 1980s systems that first made money.

What faded was the ambition that rules alone could produce general intelligence. What survived is the architecture, wherever a decision must be explainable and correctable by the people responsible for it.

![Visual explanation of why expert systems faded, and what survived](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_section_why_expert_systems_faded_and_what_survived.png)

## Anatomy at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Component</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it holds</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">At the dealership</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Knowledge base</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">General facts and rules about the domain</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Every fault pattern Ramesh knows, written as rules</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Inference engine</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The reasoning procedure, with no domain knowledge</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Matches rules to symptoms and derives conclusions</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Working memory</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Facts about the case in hand</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">This customer's symptoms, this morning</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Explanation facility</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The record of which rules fired and why</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The argument a technician can check or challenge</td>
    </tr>
  </tbody>
</table>

![Visual explanation of anatomy at a glance](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_section_anatomy_at_a_glance.png)

## Your Turn

Find an expert in your own life whose knowledge is not written down anywhere: a tailor who can tell from a glance which fabric will not survive a wash, a mechanic, a cook, a lab technician.

Interview them for twenty minutes with one goal, which is to get five of their rules into the form "if these conditions hold, then conclude this". Write down exactly what they say, not a tidied version.

Then examine what you have collected, because the exercise is really about the failure. Count how many of your five rules contain a word like "usually", "sometimes", or "it depends", and decide how a machine should treat those words. Then find at least one thing they clearly know and could not put into words at all, and write down what a system would need to perceive in order to capture it. If you conclude that some of their expertise cannot be written as rules by anyone, you have discovered the knowledge acquisition bottleneck for yourself, which is the single most important fact about this entire technology.
