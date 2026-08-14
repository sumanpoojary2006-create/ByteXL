## Introduction

A free health screening camp runs for three days at a community hall in Nagpur. On the second morning a man in his forties is handed a slip saying his test came back positive, and he is told the test is 99 percent accurate.

He goes home and tells his family he almost certainly has the disease. Every person he speaks to that day agrees with him, including two who have degrees. Ninety-nine percent accurate, positive result, so a ninety-nine percent chance of being ill. It is the most natural inference in the world.

It is also badly wrong. Given the numbers the camp was actually working with, his chance of having the disease is closer to **17 percent**, and the reason has nothing to do with the quality of the test. Every figure he was told is correct. The mistake is in a step of reasoning that feels so obvious it is not noticed as a step at all.

Everything in this unit so far would be no help to him. Rules fire or they do not, statements are entailed or they are not, and none of that machinery has anywhere to put the words "probably" or "almost certainly". Handling questions like his requires a language of graded belief rather than truth, and that is **reasoning under uncertainty**.

**Definition:** `Reasoning under uncertainty` replaces truth values with degrees of belief expressed as probabilities, and updates those beliefs in the light of new evidence using `Bayes' theorem`, which combines how likely the evidence is under each hypothesis with how likely the hypothesis was beforehand.

![Opening scene: A free health screening camp runs for three days at a community hall in Nagpur.](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_section_introduction.png)

## Why Logic Alone Cannot Cope

Try writing the camp's medical knowledge as rules and the difficulty is immediate.

"If the test is positive then the patient has the disease" is false, because tests produce false alarms. Adding conditions does not save it, because there is no set of conditions under which a test result becomes conclusive. The honest statement is that a positive result makes the disease more likely than it was, and logic as presented so far has no way to say that.

Three features of the real world defeat pure logic, and they are worth separating.

1. **Evidence is partial.** No test reveals the underlying condition directly; it reveals something correlated with it.
2. **Rules have exceptions that cannot be enumerated.** A physician cannot list every circumstance under which a symptom fails to indicate its usual cause, so a rule with all its exceptions attached could never be written down.
3. **Decisions cannot wait.** Treatment must be chosen while the diagnosis remains uncertain, so a system that answers only when it is sure answers too late.

The response is not to abandon rigour. It is to change what is being computed, from whether a statement is true to how strongly it should be believed.

![Visual explanation of why logic alone cannot cope](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_section_why_logic_alone_cannot_cope.png)

## Probability as Degree of Belief

A probability is a number between 0 and 1 recording how strongly a proposition is believed, where 0 is certain falsehood, 1 is certain truth, and everything interesting lies between.

Three pieces of notation carry the rest of the lesson.

- **P(A)** is the `prior`: how likely A is before any evidence specific to this case. For the camp, the prior that a randomly chosen visitor has the disease is its prevalence in the population.
- **P(A | B)** is the `conditional probability` of A given B: how likely A is once B is known. Read the vertical bar as "given that".
- **P(B | A)** is the same two things in the opposite order, and it is a different number.

That last point deserves emphasis, because reversing it is the single most consequential error in this area.

**P(positive test | has the disease) is not P(has the disease | positive test).**

The first is a property of the test, measured in a laboratory on people already known to be ill. The second is what the man in Nagpur wants to know. They are different questions with different answers, and the camp told him the first while he heard the second. This confusion is common enough to have a name, the inverse fallacy, and it is worth checking for whenever a percentage is quoted about a test.

![Visual explanation of probability as degree of belief](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_section_probability_as_degree_of_belief.png)

## Bayes' Theorem

Bayes' theorem is the rule that converts one direction into the other.

**P(A | B) = P(B | A) × P(A) / P(B)**

Read in words rather than symbols, it says: the belief in A after seeing B equals how well A predicted B, multiplied by how plausible A was to begin with, divided by how likely B was overall.

The structure is worth naming, because it explains every result in this lesson.

- **P(B | A) is the likelihood.** How well the hypothesis accounts for the evidence. A good test scores highly here.
- **P(A) is the prior.** How plausible the hypothesis was before the evidence arrived. **This is the term people drop**, and dropping it is what produced the man's mistake.
- **P(B) is the normaliser.** How likely the evidence was in total, across all hypotheses, which is what keeps the result a genuine probability.

![Visual explanation of bayes theorem machine](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_bayes_theorem_machine.png)

## The Camp, Counted Out

Formulas are easier to mistrust than counts, so here is the same calculation done by counting people.

Reading the code below: there is no probability theory in it at all. Three given rates at the top, then simple multiplication to split ten thousand people into four groups, and one division at the end. If you can follow a headcount, you can follow this.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjmj4" 
 width="100%"
></iframe>

```
Out of 10000 people screened:
  100 have the condition
    99 test positive   (true positives)
    1 test negative    (missed cases)
  9900 do not have it
    495 test positive  (false alarms)
    9405 test negative

Everyone who tests positive: 594
Of those, actually ill:      99
P(ill | positive test) = 0.1667  =  16.7%
```

There is the whole thing, and once seen as counts it is hard to unsee.

| In the code | The count | Where it comes from |
| --- | --- | --- |
| `have_it` | 100 | 1 percent of 10,000 |
| `true_positives` | 99 | 99 percent of those 100 are caught |
| `do_not_have_it` | 9,900 | Everybody else |
| `false_positives` | 495 | 5 percent of 9,900 are wrongly flagged |
| `all_positives` | 594 | 99 real cases plus 495 false alarms |
| `posterior` | 0.167 | 99 divided by 594 |

The test is excellent. It catches 99 of the 100 people who are ill. But it is applied to 9,900 healthy people as well, and even a 5 percent false alarm rate on that many people produces 495 false alarms. So of the 594 people who go home with a positive slip, only 99 are ill. Ninety-nine out of five hundred and ninety-four is one in six.

**The false alarms outnumber the true positives five to one, purely because the healthy group is ninety-nine times larger.** No flaw in the test causes this. A rare condition tested in a general population produces mostly false positives, and that is arithmetic rather than bad engineering.

Presenting the calculation as counts out of 10,000 rather than as decimals is called the natural frequency format, and studies of how doctors and patients reason have found it dramatically easier to get right. It is a good habit whenever a probability has to be explained to someone.

![Visual explanation of bayes base rate](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_bayes_base_rate.png)

## The Same Test in Different Populations

The result above is often summarised as "the test is unreliable", which is the wrong lesson. The test never changes in what follows; only the population does.

Reading the code below: the same calculation as before, now written as a formula rather than a headcount, so it can be run repeatedly. `SENSITIVITY` and `SPECIFICITY` are fixed at the top and never touched. Only `prevalence` varies down the loop.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjmuj" 
 width="100%"
></iframe>

```
Same test, different populations
  prevalence |  P(ill | positive)
----------------------------------
       0.01% |               0.2%
       0.10% |               1.9%
       1.00% |              16.7%
       5.00% |              51.0%
      20.00% |              83.2%
      50.00% |              95.2%
```

One test, six answers, spanning almost the entire range from nothing to near certainty. A positive result means 0.2 percent in a population where the disease is very rare and 95 percent where half the population has it.

This is the practical reason screening programmes are targeted rather than universal. Running the test on everyone puts you in the top rows, where nearly every positive is a false alarm and the harm of investigating them all outweighs the benefit. Running it on people already showing symptoms puts you in the bottom rows, where the same test is genuinely informative, because the prior has already been raised by the symptoms.

It is also a general lesson about evidence. **A piece of evidence has no fixed meaning on its own.** The same result supports a conclusion strongly or barely at all, depending entirely on how plausible that conclusion was beforehand.

![Visual explanation of the same test in different populations](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_section_the_same_test_in_different_populations.png)

## Your Turn

The camp offers the man a second test, independent of the first. Before running this, predict what a second positive would do to his 17 percent, and predict what a subsequent negative would do.

Reading the code below: `update` is the same formula again, extended to handle a negative result as well as a positive one. The important line is in the loop, where the answer from one test becomes the starting belief for the next.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjn64" 
 width="100%"
></iframe>

```
Before any test:              1.00%
After test 1 (positive):  16.67%
After test 2 (positive):  79.84%
After test 3 (negative):   4.00%
```

Three things in that output are worth sitting with.

The belief moves from 1 percent to 17 to 80 and back down to 4. **Each result becomes the prior for the next**, which is what makes this a procedure a system can run continuously rather than a one-off sum. This is exactly how a spam filter accumulates evidence across the words in a message.

The second positive is far more convincing than the first, moving belief 63 points where the first moved it 16. Evidence is not additive; its effect depends on where belief currently sits.

And the single negative undoes almost everything. That is correct rather than surprising, because this test misses only 1 in 100 ill people, so a negative is strong evidence of health even after two positives.

Now change one number and watch the whole picture shift. Set `SPECIFICITY` to 0.999, meaning one false alarm in a thousand instead of one in twenty, and rerun both the second and third programs. Work out why a modest-looking change in specificity matters so much more than an equivalent change in sensitivity when the condition is rare. If your explanation mentions the size of the healthy group, you have understood the arithmetic properly rather than memorising the result.

## Uncertainty at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Term</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">At the camp</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Prior</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Belief before this case's evidence</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1% prevalence in the population screened</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Likelihood</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How well a hypothesis predicts the evidence</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">99% of ill people test positive</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Posterior</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Belief after the evidence</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">16.7% after one positive result</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Sensitivity</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">P(positive | ill), the rate of catching real cases</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">99 of the 100 ill people found</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Specificity</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">P(negative | well), the rate of clearing healthy people</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">9,405 of 9,900 healthy people cleared</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Base rate neglect</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ignoring the prior and reading the likelihood as the answer</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hearing "99% accurate" as "99% likely ill"</td>
    </tr>
  </tbody>
</table>

![Visual explanation of uncertainty at a glance](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_section_uncertainty_at_a_glance.png)
