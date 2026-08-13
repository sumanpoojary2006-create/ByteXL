## Background

A food delivery company receives forty thousand written reviews a week and reads a sample of them by hand every Friday. The summary is always late, always partial, and always slightly wrong. They want the reviews read automatically: searchable, scored for sentiment, and rolled up per restaurant so the operations team can act on Monday morning.

Every part of that is buildable with no libraries at all. The interesting question is not whether it works. It is whether the number that reaches the operations team still means anything by the time it gets there.

## What You Will Build

A review analysis system with three stages: a TF-IDF search over the review corpus, a sentiment scorer built two ways so the difference can be measured, and a per-restaurant ranking that shows what survives aggregation and what does not.

## Learning Objectives

By the end of this project, you will be able to:
- Compute TF-IDF and explain why it needs no stopword list
- Show that counting single words cannot see a negation, and fix it with word pairs
- Quantify how often two scoring methods disagree rather than asserting that they do
- Recognise that aggregation can conceal a disagreement rather than resolve it
- Decide which stage of a pipeline a reported number can safely be trusted at

**Difficulty:** Intermediate · **Estimated time:** 3 hours

## Tasks

### Task 1: Search Without a Stopword List

1. Write at least six reviews across three restaurants. Include reviews containing negations such as "not good" and "never slow".

2. Compute the inverse document frequency for every word in the corpus, then a TF-IDF vector per review.

3. Print the words grouped by how many reviews contain them, with the weight each group receives. Confirm that words appearing in every review score exactly zero.

4. Write a `search(query)` returning the best-matching reviews with their scores. Run at least two queries and check the results are sensible.

### Task 2: Two Sentiment Scorers

1. Write `bag_score(words)` that adds one for each positive word and subtracts one for each negative word, ignoring order entirely.

2. Write `negation_score(words)` that walks the review in overlapping pairs, so a negator flips the word immediately following it. Make sure the flipped word is not then counted a second time on its own.

3. Score every review both ways and print a table marking where the two disagree. Report the count of disagreements.

4. Every disagreement should be a review containing a negation. If one is not, your pair logic has a bug.

### Task 3: Roll It Up, and See What Survives

1. Assign each review to a restaurant and rank the restaurants by average sentiment, once under each scorer.

2. Print both rankings side by side and state plainly whether they differ.

3. Look carefully at any restaurant whose reviews disagree strongly under the pairs method. Check what the average does to that disagreement.

4. Then do the harder thing: construct a set of reviews for which the two scorers produce genuinely different rankings, and report it. If averaging always hides the difference, the difference cannot reach the operations team.

## Sample Run

```
REVIEW INTELLIGENCE SYSTEM
6 reviews, 23 distinct words

1. SEARCH: words in every review score zero, so no stopword list is needed
   in 6 reviews, idf 0.000   ['and', 'the', 'was']
   in 3 reviews, idf 0.693   ['biryani']
   in 2 reviews, idf 1.099   ['arrived', 'cold', 'delivery', 'dosa', 'excellent', 'hot']
   in 1 reviews, idf 1.792   ['again', 'food', 'good', 'never', 'not', 'on']

   query 'cold delivery'  ->  r3 (0.244), r4 (0.183), r6 (0.000)
   query 'excellent biryani'  ->  r1 (0.199), r2 (0.179), r3 (0.077)

2. SENTIMENT: the same reviews, scored two ways

review                                                 bag  pairs  agree
------------------------------------------------------------------------
the biryani was excellent and the service was quick      2      2  yes
the biryani arrived hot and on time and was excellen     2      2  yes
the delivery was late and the biryani was cold          -2     -2  yes
the delivery was late again and the food was cold an    -3     -3  yes
the dosa was not good and the packaging was terrible     0     -2  NO
the service was never slow and the dosa arrived hot      0      2  NO

The two methods disagree on 2 of 6 reviews.
Every disagreement is a review containing a negation.

3. RANKING: which restaurant would you recommend?

 rank  by bag of words               by word pairs
--------------------------------------------------------------------
    1  Anand Bhavan (+2.0)           Anand Bhavan (+2.0)
    2  Cafe Mysore (+0.0)            Cafe Mysore (+0.0)
    3  Spice Route (-2.5)            Spice Route (-2.5)

Identical ranking from both scorers: True
Cafe Mysore's two reviews are scored -2 and +2 by the pairs method and
0 and 0 by the bag. Both averages land on zero, so a real per-review
disagreement vanishes the moment it is averaged.
```

The third stage is the uncomfortable one. Two scorers that disagree on a third of the reviews produce exactly the same ranking, because averaging a clear negative against a clear positive lands in the same place as averaging two neutrals. The bug in the bag of words is real and it never reaches the person reading the report.

**Answer these questions after completing all tasks:**
- Both scorers rate Cafe Mysore at zero for opposite reasons. Describe a summary statistic other than the mean that would have separated them, and say what it would have shown the operations team.
- Your pair method handles a negator directly before the word it negates. Write a review it gets wrong, of the form "the food, despite the wait, was not good". What would you have to change to handle it, and why does no fixed window solve the general problem?
- The query "cold delivery" returned a review scoring 0.000. Explain what that score means and whether a search system should show such a result at all.

## Deliverables & Rubric

Submit your `.py` file, the full printed output including your constructed ranking-flip example, and your written answers.

Your project is assessed out of 10:

| Criteria | Points |
|---|---|
| TF-IDF computed correctly, with words in every review shown scoring zero | 2 |
| Search returns sensible results for at least two queries | 1 |
| Both scorers implemented, with the flipped word not double counted | 2 |
| Disagreements counted and every one traced to a negation | 2 |
| Rankings compared, and a dataset constructed where they genuinely differ | 2 |
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
