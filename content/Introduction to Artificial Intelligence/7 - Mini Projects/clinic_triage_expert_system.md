## Background

A rural clinic sees more patients each morning than its two nurses can assess carefully. The senior doctor can state most of her triage reasoning as rules: fever with cough suggests a respiratory infection, and a respiratory infection in a breathless patient over sixty needs a chest review today rather than next week. Those rules can be written down, which makes this a job for a knowledge-based system rather than a model.

What the clinic has not decided is how the system should run. Should it take everything the nurse observed and work out all the consequences, or should it start from the question "is this urgent" and ask only what it needs? Both answers are correct, they cost different amounts, and which is cheaper depends on something you can measure.

## What You Will Build

A triage expert system with one rule base and two inference engines, forward and backward chaining, plus a comparison showing what each one costs. You will then extend it with a Bayesian update so the system can revise a belief when a test result arrives.

## Learning Objectives

By the end of this project, you will be able to:
- Keep a knowledge base separate from the engine that reasons over it
- Implement forward chaining as a fixed-point loop and backward chaining as a recursive proof
- Measure the cost of each strategy in the units a clinic actually cares about
- Identify the point at which the cheaper strategy becomes the more expensive one
- Update a belief with Bayes' theorem and explain why the prior changes what a positive test means

**Difficulty:** Intermediate · **Estimated time:** 3 hours

## Tasks

### Task 1: The Rule Base

1. Write at least eight rules, each a set of conditions and one conclusion. Include rules that chain, so the conclusion of one rule is a condition of another. Include at least two different rules that can each independently establish `urgent_referral`.

2. Keep a separate set naming which facts are directly observable by a nurse. Everything else must be derived. Nothing in your engines may mention a specific medical term.

3. Represent one patient as a mapping from every observable sign to true or false.

### Task 2: Two Engines Over One Knowledge Base

1. Write `forward_chain(known)` that repeatedly fires every rule whose conditions hold, adding conclusions until nothing changes. Return the facts and the order in which rules fired. Adding a fact already present must not count as a change, or your loop will not terminate.

2. Write `backward_chain(goal, asked)` that proves a goal recursively. When it reaches an observable sign it records a question and consults the patient. When it reaches a derived fact it tries every rule that concludes that fact. Guard against a rule base that loops back on itself.

3. Report, for the goal `urgent_referral`, how many rules forward chaining fired and how many questions backward chaining asked.

4. Be careful how you count the cost of forward chaining. It is data-driven, so the nurse must record every observable sign before it runs, because the engine cannot know in advance which will matter. That count, not the number of rules fired, is what the clinic pays.

### Task 3: Find the Crossover, Then Add Uncertainty

1. Run backward chaining separately for four different goals and total the questions asked. Compare that total against the fixed cost of forward chaining. Report which strategy is cheaper at one goal and what happens as goals are added.

2. Add a rapid test for one condition, with a stated sensitivity and specificity, and a prevalence for the population the clinic serves. Given a positive result, compute the posterior probability using Bayes' theorem.

3. Print the prior, the likelihood, and the posterior as three separate labelled numbers. Then print the same calculation for a high-risk group with a higher prevalence, leaving the test unchanged.

## Sample Run

```
CLINIC TRIAGE: two ways to reach the same conclusion
Rule base: 9 rules over 11 observable signs

FORWARD CHAINING, one goal (is this urgent?)
   signs the nurse must record  11
   rules fired                  4  (R1, R2, R5, R7)
   conclusions derived          4  (chest_review_needed, prescribe_rest, respiratory_infection, urgent_referral)
   urgent?                      True

BACKWARD CHAINING, same goal
   questions asked              5  (low_platelets, breathless, cough, fever, over_60)
   urgent?                      True

BACKWARD CHAINING, all 4 goals separately
   questions asked across the four passes  11

One goal:   backward asks 5, forward needs 11. Backward wins.
Four goals: backward asks 11, forward still needs 11. The advantage has gone.
The more goals tested against the same facts, the better forward chaining looks.
```

Notice that backward chaining asked about low platelets before it asked about anything relevant. It was attempting the dengue route to `urgent_referral` and abandoned it. A wasted question is not a bug, and how many get wasted depends on the order your rules happen to sit in.

**Answer these questions after completing all tasks:**
- Forward chaining derived a conclusion the clinic never asked for. Name it, and describe one situation in which deriving it anyway is worth the cost, and one in which it is not.
- Reorder the rules so that the rule establishing urgency through the chest route is tried before the dengue route. Rerun backward chaining and report the new question count. What does the change tell you about how much of backward chaining's efficiency is a property of the algorithm and how much is an accident of your rule ordering?
- Your test has a fixed sensitivity and specificity, yet a positive result means something different in the general clinic queue and in the high-risk group. Explain to a nurse, without using the word Bayes, why the same positive result supports two different conclusions.

## Deliverables & Rubric

Submit your `.py` file, the printed comparison, the Bayesian calculation for both populations, and your written answers.

Your project is assessed out of 10:

| Criteria | Points |
|---|---|
| Rule base with chaining rules and two routes to urgency, held apart from the engines | 2 |
| Forward chaining reaches a fixed point and terminates correctly | 2 |
| Backward chaining proves the goal and asks only for observables it needs | 2 |
| Cost comparison counts signs recorded, not rules fired, and finds the crossover | 2 |
| Bayesian update correct for both populations, with prior and likelihood labelled | 1 |
| Code readability and organisation | 1 |
| **Total** | **10** |

## Where to Build This Project

1. Go to [bytexl.app/nimbus](https://bytexl.app/nimbus).
2. Click **Create new workspace**.

![The Nimbus dashboard with the Create new workspace button highlighted](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/nimbus-python/01_create_new_workspace.png)

3. Select the **Python** template, then click **Next**.

![Select the Python template and click Next](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/nimbus-python/02_select_python_template.png)

4. Enter a workspace name and click **Launch Workspace**.

![Enter a workspace name and launch the Python workspace](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/nimbus-python/03_name_and_launch_workspace.png)
