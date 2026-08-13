# Unit 4 - Machine Learning Fundamentals - MCQ

**Course:** Introduction to Artificial Intelligence
**Title pattern:** `Introduction to Artificial Intelligence - MCQ - U.S.Q`
**Set 1 (questions 1 to 20) is the upload set.** It covers all 11 subtopics of this unit.
**Set 2 (questions 21 to 50) is the reserve bank.**

## Subtopic coverage in the upload set

| Subtopic | Covered by |
| --- | --- |
| `introduction-to-machine-learning` | 4.1.1, 4.1.19 |
| `learning-paradigms` | 4.1.2, 4.1.11 |
| `data-for-machine-learning` | 4.1.3, 4.1.12 |
| `regression` | 4.1.4 |
| `classification` | 4.1.5, 4.1.13 |
| `decision-trees` | 4.1.6, 4.1.14 |
| `clustering` | 4.1.7, 4.1.15 |
| `model-training` | 4.1.8, 4.1.16 |
| `model-evaluation` | 4.1.9, 4.1.17 |
| `model-generalization` | 4.1.10, 4.1.18 |
| `machine-learning-with-scikit-learn` | 4.1.20 |

---

# Set 1

## Introduction to Artificial Intelligence - MCQ - 4.1.1

**description**
A payroll team can state the rule for computing tax exactly, from published slabs. A fraud team cannot state the rule for spotting a suspicious transaction, though they have five years of confirmed cases. Which problem suits machine learning, and what decides it?

- **option1** Neither, because machine learning requires continuous numeric outputs and both of these problems produce categorical decisions about individual records
- **option2** The payroll problem, because the rules are already known and can be encoded as training targets
- **option3** Both equally, since any problem with historical data can be learned
- **option4** The fraud problem, because nobody can state the rule but the answers exist in quantity

**answer** 4
**difficulty** easy
**bloomTaxonomy** apply
**topics** machine-learning-fundamentals
**subTopics** introduction-to-machine-learning

**explanation**
Rule-based programming takes rules and data and produces answers, and it fails when nobody can state the rule. Machine learning takes data and answers and produces the rule, and it fails when examples are too few or the answers are wrong. Tax has published rules and demands exactness, so learning it would be strictly worse than encoding it.

## Introduction to Artificial Intelligence - MCQ - 4.1.2

**description**
A warehouse robot must learn a fast route through the aisles. Nobody has recorded a set of good routes for it to copy, but the time each attempt takes can be measured. Which paradigm fits, and what makes it hard?

- **option1** Supervised learning, and the difficulty is obtaining enough labelled routes
- **option2** Reinforcement learning, and the difficulty is delayed credit assignment together with generating its own data
- **option3** Unsupervised learning, and the difficulty is that there is no answer key against which to check the grouping
- **option4** Semi-supervised learning, and the difficulty is deciding how much weight to place on the small number of routes that have been labelled by a human observer

**answer** 2
**difficulty** easy
**bloomTaxonomy** apply
**topics** machine-learning-fundamentals
**subTopics** learning-paradigms

**explanation**
Reinforcement learning is defined by rewards that follow actions, often after a delay, and the agent generates its own data by acting. Working out which of many earlier moves earned a late reward is delayed credit assignment. Supervised learning would need recorded good routes, which is precisely what does not exist here.

## Introduction to Artificial Intelligence - MCQ - 4.1.3

**description**
A dataset records locality names as 1, 2 and 3 so a model can use them. What has gone wrong?

- **option1** The encoding invents an order and a spacing between localities that do not exist
- **option2** The encoding will slow training, since numeric features take longer to process than text
- **option3** Nothing, provided the same numbering is applied consistently to the test set as well
- **option4** The encoding loses information, because three numbers cannot represent the number of distinct localities that a real city would contain

**answer** 1
**difficulty** easy
**bloomTaxonomy** analyze
**topics** machine-learning-fundamentals
**subTopics** data-for-machine-learning

**explanation**
Categorical features are labels from a fixed set with no order, and numbering them 1, 2, 3 tells the model that locality 3 is somehow greater than locality 1 and that the gap from 1 to 2 matches the gap from 2 to 3. Ordinal features do have a real order, and even there the gaps are not equal.

## Introduction to Artificial Intelligence - MCQ - 4.1.4

**description**
A price model reports a training error of 3.57 lakh and a test error of 0.52 lakh. Why should that pattern make an analyst suspicious rather than pleased?

- **option1** Because a test error below the training error usually means the test set was unusually easy or too small to measure anything
- **option2** Because test error should always exceed training error, so one of the two figures must have been computed incorrectly
- **option3** Because errors expressed in lakh cannot be compared unless both sets contain flats in the same price range
- **option4** Because a low test error indicates the model has memorised the test set, which is the definition of overfitting and requires the model to be retrained from the beginning

**answer** 1
**difficulty** easy
**bloomTaxonomy** analyze
**topics** machine-learning-fundamentals
**subTopics** regression

**explanation**
A model normally does better on data it was fitted to, so the reverse ordering points at the measurement rather than the model. With only three test flats the figure is one draw from a wide distribution and says little. Overfitting produces the opposite pattern, a low training error with a high test error.

## Introduction to Artificial Intelligence - MCQ - 4.1.5

**description**
A nearest-neighbour classifier sorts mail into three folders. With k set to 13 on a training set of 14 messages, accuracy is zero rather than merely low. What explains an accuracy of exactly zero?

- **option1** The distance calculation overflows when k approaches the number of examples available, which causes every comparison to return an identical value
- **option2** Thirteen is an odd number, which prevents the vote from being decided
- **option3** The classifier has no training phase, so it cannot generalise from so few examples
- **option4** With k almost as large as the dataset, every query returns the same majority folder, so every message in the minority folders is wrong

**answer** 4
**difficulty** easy
**bloomTaxonomy** analyze
**topics** machine-learning-fundamentals
**subTopics** classification

**explanation**
As k grows towards the size of the dataset, the neighbourhood stops being local and the vote is decided by whichever folder is largest overall. Every query then gets the same answer. Odd values of k help avoid ties in two-class problems, which is a different concern and does not produce zero.

## Introduction to Artificial Intelligence - MCQ - 4.1.6

**description**
A loan tree splits on credit score at 615. Nobody told the algorithm that 615 was significant. Where did the threshold come from?

- **option1** From trying the midpoint between every pair of adjacent observed values and keeping whichever separated the classes best
- **option2** From a default supplied by the library, which uses the midpoint of the feature's overall range
- **option3** From the domain expert who specified the feature list before training began
- **option4** From the average credit score across the training set, which is the conventional starting point for a numeric split

**answer** 1
**difficulty** easy
**bloomTaxonomy** understand
**topics** machine-learning-fundamentals
**subTopics** decision-trees

**explanation**
Thresholds are found, not supplied. The algorithm considers every feature and every candidate cut point, scoring each by how pure the resulting groups are, and keeps the best. This is why decision trees handle numeric features with no preparation, and why a decision tree is a set of rules that was learned rather than written.

## Introduction to Artificial Intelligence - MCQ - 4.1.7

**description**
Customers are clustered on annual spend, which runs into tens of thousands of rupees, and monthly visits, which runs from 1 to 22. The resulting groups separate cleanly on spend and mix visits wildly. What happened?

- **option1** The visits feature contains too little variation to be useful for grouping customers
- **option2** The algorithm converged on a local optimum, and a different starting point would have used both features
- **option3** Four groups was too few for two features, and increasing the number of clusters would allow visits to influence the result
- **option4** Distance is dominated by the feature measured in bigger numbers, so visits was effectively ignored

**answer** 4
**difficulty** easy
**bloomTaxonomy** analyze
**topics** machine-learning-fundamentals
**subTopics** clustering

**explanation**
A gap of fourteen visits counts for nothing beside a gap of several thousand rupees, so the feature measured in bigger numbers silently becomes the only feature that matters. Scaling both onto a comparable range fixes it. For any method that measures distance, scaling is part of the model rather than preprocessing hygiene.

## Introduction to Artificial Intelligence - MCQ - 4.1.8

**description**
Two analysts fit the same model to the same twelve flats and report accuracies of 0.52 lakh and 5.74 lakh. Their methods are identical. What differs, and what should be reported instead?

- **option1** The number of features each analyst included, and the honest report is the result from whichever feature set produced the lower error on the held-out data
- **option2** Their choice of error measure, and the honest report is to state which measure was used
- **option3** Only which rows landed in the test set, and the honest report is an average across many splits together with the spread
- **option4** The random seed used to initialise the model, and the honest report is the best result obtained

**answer** 3
**difficulty** easy
**bloomTaxonomy** evaluate
**topics** machine-learning-fundamentals
**subTopics** model-training

**explanation**
A single test score is one draw from a distribution, and on three test rows that distribution is very wide. Cross-validation trains repeatedly, holding out each part once, and reports an average with a spread. The spread is as valuable as the average, because it says how much to trust the estimate.

## Introduction to Artificial Intelligence - MCQ - 4.1.9

**description**
A screening model for a condition affecting two people in a hundred reports 98 percent accuracy. It finds none of the cases. How is that possible, and what would have exposed it?

- **option1** Saying healthy to everybody is right 98 times in 100, and recall would have shown zero
- **option2** The accuracy figure was computed on the training set, and a test set would have revealed the failure
- **option3** The model is overfitted, and cross-validation would have revealed the gap
- **option4** The accuracy figure excludes the cases the model declined to classify, and counting those as errors would have brought the reported figure down sharply

**answer** 1
**difficulty** easy
**bloomTaxonomy** analyze
**topics** machine-learning-fundamentals
**subTopics** model-evaluation

**explanation**
When one class is rare, accuracy is dominated by the majority and a model that never flags anyone scores well. Recall asks what fraction of real cases were caught, and zero recall is the single number that exposes it. The confusion matrix shows the same thing directly, with an entire column of zeros.

## Introduction to Artificial Intelligence - MCQ - 4.1.10

**description**
Fitting polynomials of increasing degree to ten noisy points, the training error falls steadily and reaches exactly zero at degree nine, while the test error falls to a minimum around degree five and then climbs to its worst value at degree nine. What does the zero training error indicate?

- **option1** That the model has found the true underlying curve, and the rising test error reflects noise in the test set
- **option2** That the fitting procedure has converged, since an error of zero means no further improvement is available to it
- **option3** That the training set was too small, and the same degree would generalise well given more points
- **option4** That ten coefficients can pass exactly through ten points, which says nothing about the curve between them

**answer** 4
**difficulty** easy
**bloomTaxonomy** analyze
**topics** machine-learning-fundamentals
**subTopics** model-generalization

**explanation**
More flexibility always fits the training points better, which is why training error is not evidence of anything. Overfitting is not being wrong about the training data; it is being unconstrained everywhere else, and inspecting the fitted curve between the points shows it swinging wildly. Adding data does help this specific failure, but the zero itself indicates memorisation.

---

# Set 2

## Introduction to Artificial Intelligence - MCQ - 4.1.11

**description**
A retailer has two lakh customer records and no labels of any kind. The marketing head wants to know what kinds of customer exist. Which paradigm applies, and what is the hardest part of the work?

- **option1** Supervised learning, and the hardest part is obtaining labels for a sample large enough to train on
- **option2** Reinforcement learning, and the hardest part is defining a reward for a correct grouping
- **option3** Unsupervised learning, and the hardest part is that there is no answer key, so there is no clean way to be right
- **option4** Unsupervised learning, and the hardest part is the computational cost of comparing two lakh records against one another in every possible pairing

**answer** 3
**difficulty** medium
**bloomTaxonomy** apply
**topics** machine-learning-fundamentals
**subTopics** learning-paradigms

**explanation**
Unsupervised learning finds structure in data that carries no answers, which is exactly the request. Its defining difficulty is the absence of an answer key, so usefulness replaces correctness as the standard. Computational cost is real and secondary, since clustering algorithms avoid comparing every pair.

## Introduction to Artificial Intelligence - MCQ - 4.1.12

**description**
A model predicting whether a patient will be readmitted performs superbly in testing and collapses in deployment. An audit finds one of its features was recorded only after the readmission decision had been taken. What is this, and why did testing miss it?

- **option1** Representation bias, and testing missed it because the test set was drawn from the same clinics as the training set
- **option2** Overfitting, and testing missed it because the test set was too small to reveal the gap
- **option3** Leakage, and testing missed it because the feature was present in the test set too, so it helped there as well
- **option4** Measurement bias, and testing missed it because the feature was a proxy for the outcome rather than a direct record of it

**answer** 3
**difficulty** medium
**bloomTaxonomy** analyze
**topics** machine-learning-fundamentals
**subTopics** data-for-machine-learning

**explanation**
A feature recorded after the outcome carries the answer, and because the test set contains it too, the test reports the same inflated performance. Only deployment, where the feature is not yet available, exposes it. Overfitting shows up as a gap between training and test scores, which is precisely what leakage hides.

## Introduction to Artificial Intelligence - MCQ - 4.1.13

**description**
Why is "slightly wrong" a meaningful idea in regression but not in classification?

- **option1** Because classification models output probabilities rather than categories, and a probability cannot be described as slightly wrong until a threshold has been applied to it
- **option2** Because classification uses whole numbers, which cannot express partial error
- **option3** Because regression models are more accurate than classification models in general
- **option4** Because a predicted quantity can miss by a little or a lot, whereas a message is either in the right folder or it is not

**answer** 4
**difficulty** medium
**bloomTaxonomy** understand
**topics** machine-learning-fundamentals
**subTopics** classification

**explanation**
Being off by 2 lakh beats being off by 20, so regression error is measured as the average size of the miss in the label's own units. A category is right or wrong, so classification error is the proportion placed correctly. This difference is why the two use entirely different measures.

## Introduction to Artificial Intelligence - MCQ - 4.1.14

**description**
A bank likes decision trees because a branch manager can read the rules. Which weakness should temper that enthusiasm most?

- **option1** Trees cannot handle numeric and categorical features in the same model
- **option2** Trees select their own features, so the bank cannot control which information the model is permitted to consider when reaching a decision
- **option3** Trees require every feature to be scaled to a comparable range before training
- **option4** Trees are unstable, so a few changed rows can produce a completely different set of rules

**answer** 4
**difficulty** medium
**bloomTaxonomy** evaluate
**topics** machine-learning-fundamentals
**subTopics** decision-trees

**explanation**
Instability undercuts the readability argument directly: if next quarter's data produces a visibly different set of rules, the explanation offered to a customer changes without the underlying policy changing. Handling mixed feature types and needing no scaling are strengths of trees, and automatic feature selection is usually welcome.

## Introduction to Artificial Intelligence - MCQ - 4.1.15

**description**
Run k-means with k set to four on entirely random data with no structure in it. What comes back?

- **option1** An error, since the algorithm cannot converge when no groups exist
- **option2** Four neat groups, because the algorithm always returns something and the output is not evidence that structure exists
- **option3** A single cluster containing every point, since none is closer to any centre than to another
- **option4** Four groups of unequal size, whose imbalance is the signal that no real structure was present in the data

**answer** 2
**difficulty** medium
**bloomTaxonomy** evaluate
**topics** machine-learning-fundamentals
**subTopics** clustering

**explanation**
The algorithm partitions whatever it is given, and it will hand back four tidy groups from noise. This is one of three reasons clustering deserves more scepticism than supervised learning, alongside the absence of a correct answer and the fact that a group means nothing until a person supplies the meaning.

## Introduction to Artificial Intelligence - MCQ - 4.1.16

**description**
A team tries five values of a hyperparameter, keeps whichever scored best on the test set, and reports that score. What have they done, and what is the less obvious consequence?

- **option1** Used too few candidate values, and the consequence is that a better setting outside the five was never considered at any point in the process
- **option2** Tuned on the test set, which inflates the reported score while leaving the choice of hyperparameter sound
- **option3** Tuned on the test set, and beyond an optimistic score they have probably also chosen a worse value of the hyperparameter
- **option4** Nothing wrong, provided the five values were chosen before the test set was examined

**answer** 3
**difficulty** medium
**bloomTaxonomy** evaluate
**topics** machine-learning-fundamentals
**subTopics** model-training

**explanation**
Choosing on the test set makes the reported figure optimistic, which most people expect. The less obvious harm is that the selection optimises for the accident of which rows landed in the test set, so it can pick a setting that generalises worse. The remedy is a validation set for choosing and a test set opened once at the end.

## Introduction to Artificial Intelligence - MCQ - 4.1.17

**description**
A model flags 76 people, of whom 16 genuinely have the condition, and misses 4 of the 20 real cases. Which pair of figures describes this, and which is the one a follow-up clinic cares about?

- **option1** Recall 0.211 and precision 0.800, and the clinic cares about recall
- **option2** Recall 0.800 and precision 0.211, and the clinic cares about precision because every false alarm costs an appointment
- **option3** Accuracy 0.936 and F1 0.333, and the clinic cares about F1 as the balanced figure
- **option4** Recall 0.800 and precision 0.211, and the clinic cares about recall because catching cases is the purpose of the programme

**answer** 2
**difficulty** medium
**bloomTaxonomy** apply
**topics** machine-learning-fundamentals
**subTopics** model-evaluation

**explanation**
Recall is 16 of 20 caught, which is 0.800. Precision is 16 of 76 flagged, which is 0.211. The clinic bears the cost of the 60 unnecessary appointments, so precision is their figure, while the health programme worries about the 4 missed cases and watches recall. Both are true at once, which is why they are quoted as a pair.

## Introduction to Artificial Intelligence - MCQ - 4.1.18

**description**
A model scores 0.66 on training data and 0.64 on test data. A colleague proposes collecting ten times more data. Why is that unlikely to help?

- **option1** Because more data always increases the risk of leakage, which would make the gap worse
- **option2** Because the scores are close, which indicates overfitting, and overfitting is addressed by reducing flexibility rather than by adding examples
- **option3** Because ten times more data would require the model to be retrained from scratch, losing what it has already learned
- **option4** Because the two scores are close, which indicates underfitting, and a model too rigid to represent the pattern stays rigid with more examples

**answer** 4
**difficulty** medium
**bloomTaxonomy** evaluate
**topics** machine-learning-fundamentals
**subTopics** model-generalization

**explanation**
Poor and similar scores are the signature of underfitting, which needs more flexibility or better features. Adding data is the standard remedy for overfitting, where training is excellent and test is much worse. Getting these the wrong way round is the commonest diagnostic mistake in the unit.

## Introduction to Artificial Intelligence - MCQ - 4.1.19

**description**
Which statement about the relationship between AI, machine learning and deep learning is correct?

- **option1** All AI is machine learning, and all machine learning is deep learning
- **option2** Machine learning and AI are the same field under two names, and deep learning is a separate discipline
- **option3** All deep learning is machine learning, and all machine learning is AI, so the three terms may be used interchangeably in any technical context
- **option4** Not all AI is machine learning, and not all machine learning is deep learning

**answer** 4
**difficulty** medium
**bloomTaxonomy** understand
**topics** machine-learning-fundamentals
**subTopics** introduction-to-machine-learning

**explanation**
A rule-based tax calculator is AI without being machine learning, and a decision tree is machine learning without being deep learning. The nesting is real, which is why the answer calling the three terms interchangeable is half right, and the nesting is precisely why they are not.

## Introduction to Artificial Intelligence - MCQ - 4.1.20

**description**
A linear model over four flat features returns a positive weight on distance from the city centre, implying that flats further out cost more. Test error is nonetheless low. What should be concluded?

- **option1** The model is broken and must be retrained, since a nonsensical coefficient invalidates its predictions
- **option2** Distance genuinely raises prices in this city, and the analyst's intuition is wrong
- **option3** A model can predict well and still contain coefficients that are worthless as explanations, because correlated features share credit unpredictably
- **option4** The coefficient sign is arbitrary in linear models, so no coefficient should ever be read as carrying meaning about the feature it belongs to

**answer** 3
**difficulty** medium
**bloomTaxonomy** evaluate
**topics** machine-learning-fundamentals
**subTopics** machine-learning-with-scikit-learn

**explanation**
Distance moves with area and bedrooms in a small sample, and least squares distributes credit among correlated features in a way that fits twelve rows without describing reality. Reading weights as causes is one of the commonest mistakes made with linear models. Coefficients are not arbitrary in general, which is why the overreach in the final option is wrong.

---

# Set 3

---

# Set 2

## Introduction to Artificial Intelligence - MCQ - 4.2.1

**description**
Which limitation applies to machine learning regardless of how good the algorithm is?

- **option1** It requires the rules to be stated before training can begin
- **option2** It cannot produce continuous outputs without a separate regression stage
- **option3** It inherits whatever is in the data, including patterns nobody intended it to learn
- **option4** It cannot be applied to problems where the correct answer changes over time, since the model would then be learning a moving target

**answer** 3
**difficulty** medium
**bloomTaxonomy** understand
**topics** machine-learning-fundamentals
**subTopics** introduction-to-machine-learning

**explanation**
The model learns what the data contains, so historical discrimination is learned as readily as any other pattern. It also needs data in quantity with answers attached. Requiring the rules in advance describes rule-based programming, and shifting targets are handled by retraining rather than being impossible.

## Introduction to Artificial Intelligence - MCQ - 4.2.2

**description**
What is dimensionality reduction, and which paradigm does it belong to?

- **option1** Discarding rows that contribute little to the model, under supervised learning
- **option2** Finding a smaller set of features that retains most of the structure, under unsupervised learning
- **option3** Reducing the number of categories a classifier must distinguish, under supervised learning
- **option4** Shrinking the number of hyperparameters that must be searched, which applies to every paradigm equally since all of them require settings chosen before training

**answer** 2
**difficulty** medium
**bloomTaxonomy** remember
**topics** machine-learning-fundamentals
**subTopics** learning-paradigms

**explanation**
Dimensionality reduction works on columns rather than rows and needs no labels, which places it with clustering under unsupervised learning. Both are ways of finding structure: one groups examples, the other compresses the description of each example.

## Introduction to Artificial Intelligence - MCQ - 4.2.3

**description**
Why is the choice of features described as setting a limit that the algorithm cannot exceed?

- **option1** Because algorithms are chosen after the features and cannot be changed later
- **option2** Because more features always produce a better model, so the limit is simply the number collected
- **option3** Because a model can only relate what it is shown to what it predicts, so information absent from the features is unavailable at any accuracy
- **option4** Because feature values must be scaled before training, and scaling caps how much any single feature can contribute to the final prediction

**answer** 3
**difficulty** medium
**bloomTaxonomy** understand
**topics** machine-learning-fundamentals
**subTopics** data-for-machine-learning

**explanation**
The features set the limit and the algorithm only determines how close to that limit you get. If the thing that actually drives the outcome was never recorded, no model recovers it. More features are not automatically better, since irrelevant ones add noise and leaked ones destroy the evaluation.

## Introduction to Artificial Intelligence - MCQ - 4.2.4

**description**
In fitting a straight line by least squares, what does the slope represent, and why is it described as interpretable?

- **option1** The average value of the label, which is interpretable because it has the label's units
- **option2** The change in the label per unit change in the feature, stated in the label's units per feature unit
- **option3** The proportion of variation the model explains, which is interpretable as a percentage
- **option4** The point at which the fitted line crosses the vertical axis, which is interpretable because it gives the prediction when the feature is zero

**answer** 2
**difficulty** medium
**bloomTaxonomy** understand
**topics** machine-learning-fundamentals
**subTopics** regression

**explanation**
A slope of 0.07 lakh per square foot says exactly that, which a person can check against their own sense of the market. The intercept is where the line crosses zero and is described in the final option. Neither is the proportion of variation explained, which is a separate summary statistic.

## Introduction to Artificial Intelligence - MCQ - 4.2.5

**description**
A three-class nearest-neighbour classifier finds that among five neighbours, two vote for one folder, two for another and one for a third. The system reports the first folder. What has been discarded?

- **option1** Nothing, since reporting the largest group is the correct behaviour for a vote
- **option2** The information that the vote was split, which the system could have surfaced as low confidence
- **option3** The distances to the neighbours, which should have been used to break the tie automatically
- **option4** The two neighbours that voted for the second folder, which should have been re-examined before the decision was finalised

**answer** 2
**difficulty** medium
**bloomTaxonomy** analyze
**topics** machine-learning-fundamentals
**subTopics** classification

**explanation**
A split vote is information, and throwing it away is a design decision rather than a necessity. Surfacing it lets the system flag the case for a human or abstain. Distance weighting is one reasonable way to break ties and is a separate choice from whether the split is reported at all.

## Introduction to Artificial Intelligence - MCQ - 4.2.6

**description**
Decision tree splits are described as axis-aligned. What practical consequence follows?

- **option1** A boundary that runs diagonally through the feature space needs many splits to approximate
- **option2** Features must be rotated onto the axes before training
- **option3** Only one feature may appear anywhere in the finished tree
- **option4** The tree can use numeric features but not categorical ones, since a categorical feature has no axis along which a threshold can be placed

**answer** 1
**difficulty** medium
**bloomTaxonomy** understand
**topics** machine-learning-fundamentals
**subTopics** decision-trees

**explanation**
Each split tests one feature against a threshold, which cuts the space with a line perpendicular to that feature's axis. A diagonal boundary must then be built from a staircase of such cuts. Handling numeric and categorical features together is one of the tree's strengths, so the last option inverts the truth.

## Introduction to Artificial Intelligence - MCQ - 4.2.7

**description**
Inertia falls from 2.810 at k equal to 1 to 0.098 at k equal to 4, then to 0.082 and 0.066 for k of 5 and 6. What does this pattern support, and what does it not establish?

- **option1** It supports choosing k of 1, since the largest single drop follows it, and does not establish anything further
- **option2** It supports choosing k of 6, since inertia is lowest there, and does not establish that the groups are meaningful
- **option3** It supports choosing k of 4 by the elbow, and does not establish that four is the correct number of groups
- **option4** It supports choosing k of 4, and it does establish that four is correct, since inertia has effectively stopped falling by that point

**answer** 3
**difficulty** medium
**bloomTaxonomy** analyze
**topics** machine-learning-fundamentals
**subTopics** clustering

**explanation**
Inertia always falls as k rises, reaching zero when every point is its own group, so the lowest value never settles the question. The elbow is read as a hint rather than computed as an answer, and four groups and six groups can both be defensible. Nothing in the data makes a number correct.

## Introduction to Artificial Intelligence - MCQ - 4.2.8

**description**
Why should a fraud dataset with two percent positive cases be split in a stratified way rather than at random?

- **option1** Because a random split may leave the test set with almost no fraud, so it measures nothing about the case of interest
- **option2** Because stratification increases the total number of fraudulent examples available for training
- **option3** Because random splitting is only valid when the data has a time order
- **option4** Because stratification guarantees the model will perform equally well on both classes once it has been trained on the balanced split it produces

**answer** 1
**difficulty** medium
**bloomTaxonomy** apply
**topics** machine-learning-fundamentals
**subTopics** model-training

**explanation**
Stratifying divides each class separately and takes the same proportion from each, so both sets preserve the original balance. It creates no new examples and guarantees nothing about performance. Time order is a separate situation calling for a time-based split rather than a stratified one.

## Introduction to Artificial Intelligence - MCQ - 4.2.9

**description**
Moving the threshold of a scoring model from 0.30 to 0.80 takes recall from 1.000 to 0.150 and precision from 0.037 to 1.000. Which conclusion is correct?

- **option1** The model should be retrained, since a well-calibrated model would not show such a wide swing between two thresholds only 0.50 apart
- **option2** The model at 0.30 is the better model, since no case is missed
- **option3** The model at 0.80 is the better model, since precision is perfect
- **option4** Neither is better; they are one model configured for different priorities, and the choice belongs to whoever bears the cost of each error

**answer** 4
**difficulty** medium
**bloomTaxonomy** evaluate
**topics** machine-learning-fundamentals
**subTopics** model-evaluation

**explanation**
Precision and recall trade against each other continuously and the model itself is unchanged across the sweep. Which point to choose depends on what a missed case costs against what an unnecessary follow-up costs, which is a policy judgment. Shipping a model with the threshold buried inside it takes that decision away from the person who should make it.

## Introduction to Artificial Intelligence - MCQ - 4.2.10

**description**
Keeping the degree fixed at nine and increasing the training set from 10 points to 200 takes the test error from 1.352 to 0.187 while the training error rises from 0.000 to 0.219. Why is the rising training error a good sign?

- **option1** Because it shows the model has stopped memorising and is being forced to represent the actual pattern
- **option2** Because training error and test error must always move in the same direction for a model to be valid
- **option3** Because a non-zero training error is required before a model can be considered fitted
- **option4** Because the increase confirms that the additional points were drawn from a different distribution, which is what broadens the model's coverage

**answer** 1
**difficulty** medium
**bloomTaxonomy** analyze
**topics** machine-learning-fundamentals
**subTopics** model-generalization

**explanation**
With 200 points the polynomial can no longer pass through every one, so it has to capture the underlying shape instead. The two columns converging is the visible signature of a model that has stopped memorising, and it is a useful sanity check whenever training error rises while test error falls.

---

# Set 4

## Introduction to Artificial Intelligence - MCQ - 4.2.11

**description**
Which situation makes rule-based programming the better choice over machine learning, even when plenty of historical data exists?

- **option1** When the outcome being predicted is a category rather than a number
- **option2** When the rule is published and the output must be exactly correct
- **option3** When the historical data contains more rows than the team can process
- **option4** When the rule is known but complicated, so encoding it by hand would take longer than training a model on the recorded outcomes

**answer** 2
**difficulty** medium
**bloomTaxonomy** apply
**topics** machine-learning-fundamentals
**subTopics** introduction-to-machine-learning

**explanation**
A learned model is accurate to some percentage on data resembling its training set, which is unacceptable where the answer is defined by law and must be exact. Complexity alone is not a reason to learn a known rule, because the learned version would reproduce past mistakes and offer no guarantee.

## Introduction to Artificial Intelligence - MCQ - 4.2.12

**description**
What defines semi-supervised learning, and when is it worth using?

- **option1** Two models trained separately and combined, worth using when neither alone is accurate enough
- **option2** Supervised learning followed by unsupervised refinement, worth using when the categories are expected to change after the model has been deployed
- **option3** Labels that are correct only some of the time, worth using when the labelling process is unreliable
- **option4** A small quantity of labelled data alongside a large quantity of unlabelled data, worth using when labels are expensive

**answer** 4
**difficulty** medium
**bloomTaxonomy** remember
**topics** machine-learning-fundamentals
**subTopics** learning-paradigms

**explanation**
Getting enough labels is the hardest part of supervised learning, and semi-supervised methods exploit the structure visible in unlabelled data to stretch a small labelled set further. Unreliable labels are a data quality problem addressed differently, and combining two models is ensembling.

## Introduction to Artificial Intelligence - MCQ - 4.2.13

**description**
Which of these is an ordinal feature?

- **option1** Whether the flat has a lift, recorded as yes or no
- **option2** Condition, recorded as poor, fair, good or excellent
- **option3** Facing direction, recorded as north, south, east or west
- **option4** Locality, recorded as one of the twenty neighbourhood names used by the municipal corporation

**answer** 2
**difficulty** easy
**bloomTaxonomy** remember
**topics** machine-learning-fundamentals
**subTopics** data-for-machine-learning

**explanation**
Ordinal categories have a real order, though the gaps between them are not equal, so the step from poor to fair need not match the step from good to excellent. Facing direction and locality are categorical with no order, and a lift is binary.

## Introduction to Artificial Intelligence - MCQ - 4.2.14

**description**
Why does squaring the errors, rather than taking their absolute size, change what a regression fit optimises?

- **option1** Squaring removes the sign, which absolute size does not
- **option2** Squaring penalises large misses disproportionately, so the fit is pulled harder towards outliers
- **option3** Squaring makes the arithmetic faster, which is the only practical difference between the two
- **option4** Squaring converts the error into the label's own units, whereas absolute size leaves it in the units of the feature being measured

**answer** 2
**difficulty** medium
**bloomTaxonomy** understand
**topics** machine-learning-fundamentals
**subTopics** regression

**explanation**
Both measures remove the sign, so that is not the distinction. Squaring makes a miss of ten count a hundred times a miss of one, which drags the line towards unusual points. Root mean squared error takes the square root at the end to restore the label's units, which absolute error never left.

## Introduction to Artificial Intelligence - MCQ - 4.2.15

**description**
A nearest-neighbour classifier is described as having no training phase. What follows from that?

- **option1** It cannot be used on datasets larger than memory allows, and it has no summary of the data to inspect
- **option2** It converges faster than any model requiring training
- **option3** It cannot handle more than two classes
- **option4** It produces identical predictions whatever value of k is chosen, since no parameters were fitted that k could influence

**answer** 1
**difficulty** medium
**bloomTaxonomy** understand
**topics** machine-learning-fundamentals
**subTopics** classification

**explanation**
The model is the dataset, so every prediction searches it and there is no fitted summary a person can read, unlike a tree's rules or a line's slope. It handles any number of classes, and k changes the predictions considerably, which is the whole reason it must be chosen carefully.

## Introduction to Artificial Intelligence - MCQ - 4.2.16

**description**
A tree is grown with no depth limit and reaches 100 percent training accuracy, with several leaves covering a single applicant each. What has happened?

- **option1** The tree has grown branches that describe individual examples rather than patterns, which is overfitting
- **option2** The tree has become unstable, which is a separate problem from depth and would be resolved by collecting more applicants
- **option3** The tree has run out of features and has begun splitting on the same feature repeatedly
- **option4** The tree has found the true decision rule, and the single-applicant leaves are rare but genuine cases

**answer** 1
**difficulty** medium
**bloomTaxonomy** analyze
**topics** machine-learning-fundamentals
**subTopics** decision-trees

**explanation**
Unless restricted, a tree keeps splitting until each leaf is pure, and a leaf covering one applicant has memorised that applicant. Limiting the depth is the standard control. Instability is a related weakness concerning how much the tree changes when rows change, which is not what a single-example leaf demonstrates.

## Introduction to Artificial Intelligence - MCQ - 4.2.17

**description**
Running k-means from five different random starting points gives inertia of 0.098 four times and 0.592 once. What does that tell you, and what is the standard response?

- **option1** That k of four is wrong, since a correct k would give identical inertia from every start
- **option2** That one run encountered a computational error, so that run should be discarded and the remainder reported
- **option3** That the algorithm converges to a local optimum depending on where it started, so it is run repeatedly and the lowest inertia kept
- **option4** That the data contains an outlier which one of the five runs happened to select as an initial centre, so the outlier should be removed before clustering again

**answer** 3
**difficulty** medium
**bloomTaxonomy** analyze
**topics** machine-learning-fundamentals
**subTopics** clustering

**explanation**
k-means finds a local optimum rather than the best possible grouping, and which one depends on the starting centres. Running it many times from different starts and keeping the lowest inertia is what library implementations do by default. The odd run is a legitimate result, not an error to discard.

## Introduction to Artificial Intelligence - MCQ - 4.2.18

**description**
Four-fold cross-validation on twelve flats gives fold scores of 2.68, 5.08, 3.74 and 0.52 lakh. Which report is the honest one?

- **option1** 0.52 lakh, since that is the best the model achieved on unseen data
- **option2** Around 3.0 lakh, give or take about 1.7, since the spread says how much to trust the average
- **option3** 3.0 lakh, since the average across folds is the single correct summary
- **option4** Between 0.52 and 5.08 lakh, since quoting the full range of observed fold scores is more informative than any single summary figure could be

**answer** 2
**difficulty** medium
**bloomTaxonomy** evaluate
**topics** machine-learning-fundamentals
**subTopics** model-training

**explanation**
A spread of about 1.7 on an average of about 3.0 says the estimate is rough, which is the correct thing to say about twelve flats. Reporting the average alone invites the false confidence that a single lucky split produces, and 0.52 is one fold rather than a result.

## Introduction to Artificial Intelligence - MCQ - 4.2.19

**description**
Which measure ignores true negatives entirely, and why is that usually the right behaviour?

- **option1** Both precision and recall, because on a rare-class problem the correctly cleared majority is the uninteresting part
- **option2** Specificity, because it concerns only the cases that were flagged
- **option3** Accuracy, because the majority class would otherwise dominate the figure
- **option4** F1, because it is derived from two measures that each consider only a portion of the confusion matrix and therefore cancels the remainder out

**answer** 1
**difficulty** medium
**bloomTaxonomy** understand
**topics** machine-learning-fundamentals
**subTopics** model-evaluation

**explanation**
Recall uses the cases found and missed; precision uses the cases found and the false alarms. Neither touches the correctly cleared majority, and letting that majority into the arithmetic is exactly what makes accuracy useless when one class is rare. Specificity is the measure that does consider true negatives.

## Introduction to Artificial Intelligence - MCQ - 4.2.20

**description**
A student claims that a model with 99 percent training accuracy and 97 percent test accuracy is well fitted. Which alternative explanation deserves checking first?

- **option1** That the model is underfitting, since both figures are close together
- **option2** That the test set is too large, which would make both figures converge artificially
- **option3** That information from the label has leaked into the features, making the task easier than it really is
- **option4** That the model has been trained for too many iterations, which would drive both figures upward at the same rate

**answer** 3
**difficulty** medium
**bloomTaxonomy** evaluate
**topics** machine-learning-fundamentals
**subTopics** model-generalization

**explanation**
Good and nearly equal scores usually mean the fit is about right, and the alarming alternative is that the same information appears in both the features and the label, which inflates both figures together. Checking whether any feature could only have been known after the outcome is the cheapest way to tell the two apart.

---

# Set 5

## Introduction to Artificial Intelligence - MCQ - 4.2.21

**description**
What does the `fit` and `predict` pairing offered by every estimator in scikit-learn actually buy a practitioner?

- **option1** Guaranteed correctness, since a uniform interface prevents a model from being used on unsuitable data
- **option2** Faster execution, since a shared interface allows the library to optimise across models
- **option3** Comparing several models becomes a loop rather than a project, because the surrounding code does not change
- **option4** Automatic selection of the best model for the data, since the library can try each estimator in turn once they all share the same two methods

**answer** 3
**difficulty** medium
**bloomTaxonomy** understand
**topics** machine-learning-fundamentals
**subTopics** machine-learning-with-scikit-learn

**explanation**
Uniformity is the library's real contribution: swapping a tree for a nearest-neighbour classifier is a one-line change and everything around it stays put. It offers no protection against using a model on unsuitable data, and choosing the model remains the practitioner's judgment.

## Introduction to Artificial Intelligence - MCQ - 4.2.22

**description**
Why does binding a scaler to a model inside a pipeline matter when cross-validating, rather than scaling the whole dataset once beforehand?

- **option1** Because a pipeline scales faster than a separate scaling step
- **option2** Because scaling the whole dataset first produces different numbers from scaling each fold, and the pipeline version is the one that matches what the model will see in production
- **option3** Because scikit-learn requires scaling to be inside a pipeline for cross-validation to run at all
- **option4** Because scaling the whole dataset first lets information from each held-out fold influence the scaler, quietly inflating every score

**answer** 4
**difficulty** hard
**bloomTaxonomy** evaluate
**topics** machine-learning-fundamentals
**subTopics** machine-learning-with-scikit-learn

**explanation**
The scaler learns the range from whatever it is fitted on, so fitting it on everything means each fold's held-out rows have already contributed to the transformation applied to them. A pipeline refits the scaler inside each fold using only that fold's training portion, which is the correct procedure and easy to get wrong by hand.

## Introduction to Artificial Intelligence - MCQ - 4.2.23

**description**
Which failure of a machine learning project is not addressed by choosing a better algorithm?

- **option1** The training set being too small for the chosen model's flexibility
- **option2** The hyperparameters having been left at their default values
- **option3** The evaluation having been carried out on a single split rather than by cross-validation
- **option4** The relevant information never having been recorded as a feature

**answer** 4
**difficulty** medium
**bloomTaxonomy** evaluate
**topics** machine-learning-fundamentals
**subTopics** data-for-machine-learning

**explanation**
The features set the limit and the algorithm determines how close to it you get, so a missing signal cannot be recovered by any model. The other three are all fixable by changing how the work is done: reduce flexibility, tune the settings, or measure properly.

## Introduction to Artificial Intelligence - MCQ - 4.2.24

**description**
Why does a time-ordered dataset call for a time-based split rather than a random one?

- **option1** Because random splits are computationally more expensive on ordered data
- **option2** Because a random split trains on later records and tests on earlier ones, flattering a model that will only ever face the future
- **option3** Because time-ordered data cannot be shuffled without corrupting the feature values
- **option4** Because a time-based split produces a larger training set, which is what a model needs when the relationship it is learning changes over the period covered

**answer** 2
**difficulty** medium
**bloomTaxonomy** understand
**topics** machine-learning-fundamentals
**subTopics** model-training

**explanation**
The split should imitate the situation the model will actually face. Prices and behaviour drift, so a model that has seen next quarter while being tested on last quarter has an advantage no deployed system gets. Training on the earliest data and testing on the most recent reproduces deployment honestly.

## Introduction to Artificial Intelligence - MCQ - 4.2.25

**description**
Macro averaging and micro averaging give very different figures on a three-class mail problem where the personal folder holds 90 percent of messages and the model is poor at promotions. Which is which?

- **option1** Macro drops because every class counts equally; micro looks fine because large classes dominate
- **option2** Macro looks fine because large classes dominate; micro drops because every class counts equally
- **option3** Both drop equally, since they differ only in the order in which the counts are combined
- **option4** Macro drops because it weights each class by its size, and micro looks fine because it discards the smallest class before computing the figure

**answer** 1
**difficulty** hard
**bloomTaxonomy** analyze
**topics** machine-learning-fundamentals
**subTopics** model-evaluation

**explanation**
Macro averaging takes the plain average across classes, so a small badly handled class drags it down. Micro averaging pools all the counts first, so every example counts equally and the dominant class carries the result. Neither is wrong, and stating which was used is part of reporting the number.

## Introduction to Artificial Intelligence - MCQ - 4.2.26

**description**
Which pair of terms correctly separates what is learned from what is chosen?

- **option1** A tree's thresholds are hyperparameters; its maximum depth is a parameter
- **option2** A line's slope is a hyperparameter; the number of neighbours is a parameter
- **option3** A tree's thresholds are parameters; its maximum depth is a hyperparameter
- **option4** Both thresholds and maximum depth are parameters, since a training run determines the value of each of them from the data supplied

**answer** 3
**difficulty** medium
**bloomTaxonomy** remember
**topics** machine-learning-fundamentals
**subTopics** model-training

**explanation**
Parameters are set by the training procedure from the data, and hyperparameters are set by you before training begins. Thresholds emerge from searching the data; maximum depth is a limit you impose. Getting these right matters because hyperparameters must be chosen by measuring, which requires held-out data of its own.

## Introduction to Artificial Intelligence - MCQ - 4.2.27

**description**
Why does regularisation scale to models that have no notion of degree, such as neural networks?

- **option1** Because it penalises the size of the coefficients, which every such model has, rather than a structural setting
- **option2** Because it reduces the number of layers required, which is the equivalent of degree in a network
- **option3** Because it operates on the training data rather than on the model
- **option4** Because networks are fitted by the same least-squares procedure as polynomials, so any technique applying to one applies to the other without adjustment

**answer** 1
**difficulty** hard
**bloomTaxonomy** understand
**topics** machine-learning-fundamentals
**subTopics** model-generalization

**explanation**
Adding a penalty proportional to the size of the weights makes each one earn its place, and weights exist whatever the architecture. Degree is a whole number and can only jump, whereas the penalty strength is continuous and can be tuned finely. Limiting a tree's depth and stopping training early are cruder members of the same family.

## Introduction to Artificial Intelligence - MCQ - 4.2.28

**description**
A team reports that their interpretable model was rejected because accuracy must not be sacrificed. What should be asked?

- **option1** Whether the interpretable model was actually measured, since on structured data it frequently performs comparably
- **option2** Whether the accuracy figure was computed on the training set
- **option3** Whether the opaque model could be made interpretable after the fact
- **option4** Whether the accuracy difference is large enough to matter given the number of decisions the system will make each year in production

**answer** 1
**difficulty** medium
**bloomTaxonomy** evaluate
**topics** machine-learning-fundamentals
**subTopics** decision-trees

**explanation**
The tradeoff between accuracy and interpretability is real in general and frequently asserted without ever testing a simpler model. Treating it as a hypothesis to be measured rather than an excuse offered in advance is the discipline. The size of any real difference matters too, but only once a difference has been established.

## Introduction to Artificial Intelligence - MCQ - 4.2.29

**description**
Two clusters of customers have nearly identical annual spend, 20,000 to 26,000 against 19,000 to 25,000, but differ more than twofold in visits. Before scaling, the algorithm merged them. Why?

- **option1** Because the two groups genuinely overlap and no algorithm could separate them
- **option2** Because distance was driven almost entirely by spend, on which the two groups agree
- **option3** Because k was set too high, splitting other groups and leaving too few clusters for these two
- **option4** Because visits and spend are correlated, so the algorithm treated them as a single combined feature during the distance calculation

**answer** 2
**difficulty** medium
**bloomTaxonomy** analyze
**topics** machine-learning-fundamentals
**subTopics** clustering

**explanation**
The unscaled distance was dominated by rupees, and on rupees the two groups are nearly the same, so they collapsed together. Scaling both features onto a comparable range separated them cleanly. The algorithm never combines features on its own, and the two groups are well separated once the right measure is used.

## Introduction to Artificial Intelligence - MCQ - 4.2.30

**description**
A model is trained to predict whether a patient will need follow-up, using historical spending as a stand-in for health need. What is the risk, and where does it sit in the machine learning workflow?

- **option1** A modelling risk, since spending is a numeric feature and needs scaling before use
- **option2** A data risk, since the proxy measures access to healthcare rather than need for it, and no algorithm recovers the difference
- **option3** An evaluation risk, since spending correlates with the label and will inflate the test score
- **option4** A deployment risk, since spending patterns change over time and the model will drift away from the population it was fitted to

**answer** 2
**difficulty** hard
**bloomTaxonomy** evaluate
**topics** machine-learning-fundamentals
**subTopics** data-for-machine-learning

**explanation**
Choosing what to measure happens before any model exists, and a proxy that tracks something subtly different bakes that difference into every prediction. Drift is a genuine additional concern and arrives later. The defining fault here is the substitution itself, which is why it belongs to the data stage rather than to modelling or evaluation.
