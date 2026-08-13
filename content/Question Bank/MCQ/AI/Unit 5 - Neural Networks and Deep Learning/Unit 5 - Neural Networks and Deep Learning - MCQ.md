# Unit 5 - Neural Networks and Deep Learning - MCQ

**Course:** Introduction to Artificial Intelligence
**Title pattern:** `Introduction to Artificial Intelligence - MCQ - U.S.Q`
**Set 1 (questions 1 to 20) is the upload set.** It covers all 12 subtopics of this unit.
**Set 2 (questions 21 to 50) is the reserve bank.**

## Subtopic coverage in the upload set

| Subtopic | Covered by |
| --- | --- |
| `biological-inspiration` | 5.1.1 |
| `artificial-neurons` | 5.1.2, 5.1.11 |
| `perceptron` | 5.1.3 |
| `feedforward-neural-networks` | 5.1.4, 5.1.12 |
| `activation-functions` | 5.1.5, 5.1.13 |
| `training-neural-networks` | 5.1.6, 5.1.14 |
| `deep-learning` | 5.1.7, 5.1.15 |
| `convolutional-neural-networks` | 5.1.8, 5.1.16 |
| `recurrent-neural-networks` | 5.1.9, 5.1.17 |
| `attention-mechanism` | 5.1.10, 5.1.18 |
| `transformers` | 5.1.19 |
| `foundation-models` | 5.1.20 |

---

# Set 1

## Introduction to Artificial Intelligence - MCQ - 5.1.1

**description**
A neuron fires at most a few hundred times a second while a processor performs billions of operations in the same period, yet the brain recognises a face faster than most systems. Which property accounts for the difference?

- **option1** The brain stores its memories in a faster form of storage than a computer uses
- **option2** Neurons carry more information per firing than a processor carries per operation
- **option3** The brain works massively in parallel, with everything happening at once
- **option4** Neurons operate on continuous values rather than the discrete ones a processor manipulates, which allows a single neuron to represent many states simultaneously

**answer** 3
**difficulty** easy
**bloomTaxonomy** understand
**topics** neural-networks-and-deep-learning
**subTopics** biological-inspiration

**explanation**
Roughly 86 billion slow units working simultaneously beat a handful of fast cores working largely in sequence. Two further contrasts matter: the same connections do both memory and processing, and the brain degrades gradually rather than halting when a part fails. The capability lives in the connections, not in the units.

## Introduction to Artificial Intelligence - MCQ - 5.1.2

**description**
An irrigation neuron uses a weight of positive one on dry soil, negative one on rain forecast, positive one on water in the tank, and a bias of minus 1.5. Which part of the brief does the negative weight encode?

- **option1** The threshold, since a negative number sets how much evidence is demanded
- **option2** The relative importance of the rain sensor, since a negative weight indicates that this input should be consulted before the other two are considered
- **option3** The activation function, since a negative total produces a zero output
- **option4** The word "unless", since rain forecast argues against running the pump

**answer** 4
**difficulty** easy
**bloomTaxonomy** understand
**topics** neural-networks-and-deep-learning
**subTopics** artificial-neurons

**explanation**
Positive weights push towards firing and negative weights push against, so "do not run it if rain is forecast" becomes a weight of minus one. The bias of minus 1.5 is what sets how much total evidence is demanded, and the activation is the separate rule that turns the total into an output.

## Introduction to Artificial Intelligence - MCQ - 5.1.3

**description**
A perceptron is trained on data that no straight line can separate. What happens, and why is it dangerous in practice?

- **option1** It converges to the best available line, and the danger is that nobody checks whether a better one exists
- **option2** It stops immediately with an error, and the danger is that the error message is easy to overlook
- **option3** It converges to a curved boundary instead, and the danger is that the resulting model can no longer be described by a single set of weights
- **option4** It cycles indefinitely, and the danger is that this looks exactly like slow progress

**answer** 4
**difficulty** easy
**bloomTaxonomy** analyze
**topics** neural-networks-and-deep-learning
**subTopics** perceptron

**explanation**
The convergence theorem promises a solution in finite time when a separating line exists and says nothing when one does not, in which case the weights cycle without settling. A perceptron that has not converged looks identical to one needing more epochs, which is why the usual defence is to cap the epochs and keep the best weights seen.

## Introduction to Artificial Intelligence - MCQ - 5.1.4

**description**
Three neurons, each drawing one straight line, together compute XOR, which no single neuron can. What did the hidden layer actually do?

- **option1** It drew a curved boundary that a single neuron could not produce
- **option2** It applied a different activation function from the output neuron, and that difference is what makes the combination capable of representing XOR
- **option3** It re-described the inputs so that a straight line was enough for the remaining problem
- **option4** It averaged the two inputs, which removes the need for a boundary at all

**answer** 3
**difficulty** easy
**bloomTaxonomy** understand
**topics** neural-networks-and-deep-learning
**subTopics** feedforward-neural-networks

**explanation**
Every neuron still draws exactly one straight line. What changed is that the output neuron looks at the hidden values rather than the raw inputs, and in that space the four points are linearly separable. A hidden layer re-describes the input in terms that make the remaining problem easier, which is learning a representation at the smallest possible scale.

## Introduction to Artificial Intelligence - MCQ - 5.1.5

**description**
Sigmoid's slope is 0.25 at its steepest and 0.00034 at an input of 8. What is the practical consequence for a neuron operating at 8?

- **option1** It fires more strongly than a neuron at zero, so its influence on the next layer grows
- **option2** It produces an incorrect output, since the function has stopped responding to its input
- **option3** It still produces an output but has effectively stopped learning, because adjusting its weights barely changes anything
- **option4** It will produce an output of exactly 1, which removes it from the calculation performed by every neuron in the following layer

**answer** 3
**difficulty** easy
**bloomTaxonomy** understand
**topics** neural-networks-and-deep-learning
**subTopics** activation-functions

**explanation**
Such a neuron is saturated. The output is perfectly valid and close to 1, but the slope determines how much a weight change matters, and at 0.00034 the neuron is effectively frozen. ReLU avoids this on the positive side, since its slope is exactly 1 however large the input.

## Introduction to Artificial Intelligence - MCQ - 5.1.6

**description**
During gradient descent on a single weight, the slope starts at minus 322 and the first move is 1.611, while by step eight the slope is minus 0.70 and the move is 0.004. What produces the slowdown?

- **option1** A schedule that reduces the learning rate as training proceeds
- **option2** Numerical precision limits, which prevent very small differences in the loss from being represented once the weight approaches its optimal value
- **option3** The loss function switching to a flatter form once the error falls below a threshold
- **option4** The same formula that gives the direction also gives the magnitude, and the slope shrinks near the bottom

**answer** 4
**difficulty** easy
**bloomTaxonomy** understand
**topics** neural-networks-and-deep-learning
**subTopics** training-neural-networks

**explanation**
The step is the slope multiplied by the learning rate, and the slope flattens as the valley floor approaches, so the procedure decelerates without anyone scheduling it. The learning rate here is a fixed 0.005 throughout, which is what makes the automatic slowdown visible.

## Introduction to Artificial Intelligence - MCQ - 5.1.7

**description**
Before deep learning, a computer vision team spent months designing features by hand. What replaced that work, and what was surprising about the result?

- **option1** The training process learned the features, and the first layer rediscovered edge detectors much like the ones humans had designed
- **option2** A rule-based preprocessing stage, and the surprise was that it removed the need for a classifier
- **option3** A larger set of hand-designed features, and the surprise was how few of them turned out to matter
- **option4** A statistical summary of the pixel values, and the surprise was that this simple summary outperformed the features that experts had spent months constructing

**answer** 1
**difficulty** easy
**bloomTaxonomy** understand
**topics** neural-networks-and-deep-learning
**subTopics** deep-learning

**explanation**
Deep learning discovers the representation from data rather than receiving it from a person, and early layers converge on edge detectors similar to those designed by hand. The cost is that the learned features are largely unnamed, so explaining a decision becomes harder than with features somebody chose deliberately.

## Introduction to Artificial Intelligence - MCQ - 5.1.8

**description**
Looking for one 3 by 3 feature in a 6 by 6 image costs 10 parameters with a convolutional filter and 1,332 with a fully connected layer. What happens to that gap as the image grows?

- **option1** It narrows, since the filter must be applied at more positions
- **option2** It stays the same, since both counts scale with the number of pixels
- **option3** It widens at first and then narrows, since a larger image eventually requires additional filters to cover the greater variety of features present in it
- **option4** It widens sharply, since the filter's count is fixed while the fully connected count grows with the square of the pixel count

**answer** 4
**difficulty** easy
**bloomTaxonomy** analyze
**topics** neural-networks-and-deep-learning
**subTopics** convolutional-neural-networks

**explanation**
A filter's weight count is its width times its height times the number of input channels, plus a bias, and it is completely independent of image size. The image can double and the layer's parameter count does not change at all, which is the property no fully connected layer has and the reason convolution scales to real photographs.

## Introduction to Artificial Intelligence - MCQ - 5.1.9

**description**
A recurrent state carries a recurrent weight of 0.8. After twenty words, roughly how much of the first word's influence survives, and what is the bind?

- **option1** About 20 percent, and the bind is that the network cannot process sequences longer than its training examples
- **option2** About 80 percent, and the bind is that the state saturates once it approaches its maximum
- **option3** About 1 percent, and the bind is that a weight above 1 makes the state explode instead
- **option4** None at all, and the bind is that a recurrent network discards the previous state entirely each time a new word arrives at the input

**answer** 3
**difficulty** easy
**bloomTaxonomy** apply
**topics** neural-networks-and-deep-learning
**subTopics** recurrent-neural-networks

**explanation**
Each step multiplies the carried state by 0.8, so twenty steps leave about 1 percent. Below 1 the early information disappears exponentially; above 1 the state grows without limit. There is no setting that both remembers a long way back and stays stable, which is the bind LSTMs were built to break.

## Introduction to Artificial Intelligence - MCQ - 5.1.10

**description**
Attention returns a blend of all values rather than the single best match. Why does softness matter for learning?

- **option1** Because a blend is more accurate than any single value could be
- **option2** Because blending reduces the amount of computation required at each position
- **option3** Because a hard lookup has no useful notion of slightly better, leaving nothing for gradient descent to work with
- **option4** Because returning several values at once allows the network to keep more than one interpretation of the input available for later layers to choose between

**answer** 3
**difficulty** easy
**bloomTaxonomy** understand
**topics** neural-networks-and-deep-learning
**subTopics** attention-mechanism

**explanation**
Because the weights vary smoothly, a small change to a query produces a small change to the output, which is exactly what a gradient needs. A hard pick of the single best match is a step function with no gradient, so the network could never learn what to look for.

---

# Set 2

## Introduction to Artificial Intelligence - MCQ - 5.1.11

**description**
A neuron keeps weights of 1.0 and 1.0 while its bias moves from 0.5 to minus 0.5 to minus 1.5 to minus 2.5. Its behaviour changes from always firing, to OR, to AND, to never firing. What does the bias represent?

- **option1** The strength of the connection between the two inputs
- **option2** How much total evidence the neuron demands before it fires
- **option3** The steepness of the activation function at the firing point
- **option4** A correction applied after the activation, which shifts the output without changing the point at which the neuron begins to fire

**answer** 2
**difficulty** medium
**bloomTaxonomy** understand
**topics** neural-networks-and-deep-learning
**subTopics** artificial-neurons

**explanation**
At minus 0.5 the neuron needs one active input, at minus 1.5 it needs two, and beyond what any combination supplies it never fires. This is also why a neuron without a bias is crippled: with no bias the total is zero whenever every input is zero, so the boundary is forced through the origin.

## Introduction to Artificial Intelligence - MCQ - 5.1.12

**description**
Removing the activation function from every neuron in a two-layer XOR network produces an output of minus 0.5 for all four inputs. What general result does this demonstrate?

- **option1** That the weights chosen for that network were unsuitable once thresholds were removed
- **option2** That removing the activation causes the outputs of the hidden layer to cancel, which is a property specific to networks whose weights include both positive and negative values
- **option3** That a weighted sum of weighted sums is itself just a weighted sum, so any depth of purely linear layers collapses into one
- **option4** That two layers are insufficient for XOR, and a third would have restored the correct behaviour

**answer** 3
**difficulty** medium
**bloomTaxonomy** analyze
**topics** neural-networks-and-deep-learning
**subTopics** feedforward-neural-networks

**explanation**
The algebra reduces the whole network to a constant here, and in general it reduces any stack of linear layers to a single layer. Stack a hundred with no activation between them and you have the capability of one neuron. The activation is what makes depth mean anything, so no third layer would have helped.

## Introduction to Artificial Intelligence - MCQ - 5.1.13

**description**
Why is ReLU the default choice for hidden layers, and what does it cost?

- **option1** Its slope is 1 wherever the neuron is active, at the cost that neurons can die permanently
- **option2** Its output reads as a probability, at the cost of saturating at both ends
- **option3** It is centred on zero, at the cost of being slower to compute than sigmoid
- **option4** It bounds its output between fixed limits, at the cost of requiring the inputs to be scaled onto the same range before they reach the layer

**answer** 1
**difficulty** medium
**bloomTaxonomy** understand
**topics** neural-networks-and-deep-learning
**subTopics** activation-functions

**explanation**
A slope of exactly 1 on the positive side means a correction passes back through undiminished however deep the network, and ReLU is very fast to compute. Its slope for negative inputs is exactly zero, so a neuron whose sum has gone negative for every example receives no correction and never recovers. Leaky ReLU keeps a small negative slope to address that.

## Introduction to Artificial Intelligence - MCQ - 5.1.14

**description**
Backpropagation is described as exact bookkeeping that goes wrong in itself under no circumstances. Where do training failures actually come from?

- **option1** From backpropagation accumulating rounding errors across many layers
- **option2** From the order in which training examples are presented, since backpropagation assumes the examples arrive independently and identically distributed
- **option3** From the network being too small to represent the function being learned, which is the only genuine cause of a failed training run
- **option4** From the loss function measuring the wrong thing, from vanishing gradients, from a badly chosen learning rate, and from an unlucky random start

**answer** 4
**difficulty** medium
**bloomTaxonomy** understand
**topics** neural-networks-and-deep-learning
**subTopics** training-neural-networks

**explanation**
Backpropagation distributes blame correctly by construction. What breaks is everything around it: a loss that measures something other than what you care about, saturated activations that make the gradient vanish before it reaches the early layers, a rate that crawls or diverges, and a random start that lands in a poor hollow.

## Introduction to Artificial Intelligence - MCQ - 5.1.15

**description**
A team has 800 rows of tabular loan data and must justify every decision to a regulator. Should they use a deep network?

- **option1** Yes, since deep networks outperform other approaches on any problem once they are trained properly
- **option2** No, since deep learning suits raw high-dimensional input and needs far more data, while this problem wants named features and justifiable decisions
- **option3** Yes, provided the early layers are reused from a model trained on a different domain
- **option4** No, since deep networks cannot process tabular data at all without first converting each row into an image or another high-dimensional representation

**answer** 2
**difficulty** medium
**bloomTaxonomy** evaluate
**topics** neural-networks-and-deep-learning
**subTopics** deep-learning

**explanation**
Hand-built features with a simpler classifier suit tabular data, small datasets and decisions needing justification, because the features are named and the reasoning can be described. Deep learning suits images, audio and text, wants hundreds of thousands of examples, and leaves the features learned and largely unnamed. Tabular data can be fed to a network; it is simply the wrong tool here.

## Introduction to Artificial Intelligence - MCQ - 5.1.16

**description**
A single filter detects the same bright bar with identical strength wherever it appears in the image. What is this property called, and what would a fully connected layer have needed instead?

- **option1** Translation invariance, and a fully connected layer would have needed to learn the pattern separately for every location
- **option2** Pooling, and a fully connected layer would have needed a larger input resolution
- **option3** Feature mapping, and a fully connected layer would have needed the image to be centred on the feature before the pattern could be recognised at all
- **option4** Weight sharing, and a fully connected layer would have needed the filter applied at a single fixed position

**answer** 1
**difficulty** medium
**bloomTaxonomy** understand
**topics** neural-networks-and-deep-learning
**subTopics** convolutional-neural-networks

**explanation**
Translation invariance is the outcome and weight sharing is the mechanism producing it, since the same nine weights are used at every position. A fully connected layer treats every pixel as unrelated to every other, so it would have to see the pattern in each location during training in order to recognise it there.

## Introduction to Artificial Intelligence - MCQ - 5.1.17

**description**
Why can a convolutional network be parallelised across positions while a recurrent network cannot be parallelised across time steps?

- **option1** Because a recurrent network shares its weights across time steps, and shared weights cannot be updated by two computations running at the same moment
- **option2** Because convolution uses fewer parameters, so more of the work fits in memory at once
- **option3** Because recurrent networks process continuous values while convolutional networks process discrete ones
- **option4** Because each recurrent step needs the state produced by the previous step, whereas each filter position depends only on the input

**answer** 4
**difficulty** medium
**bloomTaxonomy** analyze
**topics** neural-networks-and-deep-learning
**subTopics** recurrent-neural-networks

**explanation**
The recurrence is a genuine data dependency: step five cannot start until step four has produced its state. Convolution has no such chain, so every position can be computed at once. Both share weights, which shows that sharing is not the obstacle, and this dependency is one of the two problems attention removes.

## Introduction to Artificial Intelligence - MCQ - 5.1.18

**description**
Shuffling the words of a sentence leaves every self-attention weight unchanged. What does this show, and how is it fixed?

- **option1** That the attention weights were computed incorrectly, fixed by normalising them again after the shuffle
- **option2** That attention discards order deliberately in order to remain parallelisable, and the loss is accepted as the price of computing all positions simultaneously
- **option3** That word order carries no meaning in the sentences used, fixed by choosing a more varied set of examples
- **option4** That attention is permutation invariant, fixed by adding position information to each word's vector before attention runs

**answer** 4
**difficulty** medium
**bloomTaxonomy** analyze
**topics** neural-networks-and-deep-learning
**subTopics** attention-mechanism

**explanation**
A score is a comparison between two vectors and nothing in that comparison mentions where either sat, so attention sees a bag of vectors rather than a sequence. Positional encoding adds a vector representing each position, so the same word at position 1 and position 4 arrives as two different vectors. The loss is not accepted; it is repaired.

## Introduction to Artificial Intelligence - MCQ - 5.1.19

**description**
A team needs a model that classifies whole documents, with each word able to draw on words both before and after it. Which transformer family fits?

- **option1** Encoder only
- **option2** Encoder-decoder
- **option3** Decoder only
- **option4** Decoder only, with positional encoding removed so that no direction is privileged over the other

**answer** 1
**difficulty** medium
**bloomTaxonomy** apply
**topics** neural-networks-and-deep-learning
**subTopics** transformers

**explanation**
An encoder sees the whole input in both directions, which suits classification, search and understanding a fixed text. A decoder sees only what precedes each position, which is what makes it suitable for generation and is the shape of most large language models. Encoder-decoder suits translation and summarising, where input and output are distinct sequences.

## Introduction to Artificial Intelligence - MCQ - 5.1.20

**description**
A startup wants to adapt a foundation model to its support domain and has around fifty worked examples and no budget for training. Which adaptation method fits?

- **option1** Full fine-tuning, since fifty examples is enough to continue training every weight
- **option2** Zero-shot prompting, since the task can simply be described and the fifty examples set aside for evaluating the result afterwards
- **option3** Partial fine-tuning, since freezing most weights reduces the requirement to a few dozen examples
- **option4** Few-shot prompting, since a handful of examples can be placed in the input with no weights changed

**answer** 4
**difficulty** medium
**bloomTaxonomy** apply
**topics** neural-networks-and-deep-learning
**subTopics** foundation-models

**explanation**
Few-shot prompting needs a handful of examples and costs nothing, since no weights change. Zero-shot would work with no examples at all, and holding fifty back for evaluation is reasonable practice, but with examples available and free to use, putting them in the input is the stronger choice. Both fine-tuning methods want hundreds to thousands of examples and real compute.

---

# Set 3

---

# Set 2

## Introduction to Artificial Intelligence - MCQ - 5.2.1

**description**
Which contrast between brains and conventional computers is stated correctly?

- **option1** The brain separates memory from processing, while a computer combines them in the same circuits
- **option2** The brain uses about 20 watts, while training a large model draws many kilowatts
- **option3** The brain halts when a small number of cells fail, while a computer degrades gradually
- **option4** The brain performs billions of operations a second across a handful of highly specialised regions, while a computer spreads the same work across many slower cores

**answer** 2
**difficulty** medium
**bloomTaxonomy** remember
**topics** neural-networks-and-deep-learning
**subTopics** biological-inspiration

**explanation**
The power gap is one of the starkest contrasts in the comparison. The other three invert real differences: the brain's connections do memory and processing together, it degrades gradually rather than halting, and an individual neuron fires only a few hundred times a second.

## Introduction to Artificial Intelligence - MCQ - 5.2.2

**description**
A neuron is given a weight of zero on one of its inputs. What does that express?

- **option1** That the input must be zero for the neuron to fire
- **option2** That the input has not yet been trained and will acquire a weight later
- **option3** That the input is irrelevant to this neuron's decision
- **option4** That the input contributes only when the other inputs are also zero, since the weighted sum then depends on the bias alone

**answer** 3
**difficulty** easy
**bloomTaxonomy** understand
**topics** neural-networks-and-deep-learning
**subTopics** artificial-neurons

**explanation**
A weight of zero removes the input from the weighted sum entirely, whatever value it takes. This is how a neuron says an input does not matter, and a trained network that drives many weights near zero is telling you which of your features carried no information.

## Introduction to Artificial Intelligence - MCQ - 5.2.3

**description**
The perceptron learning rule multiplies each weight update by the value of the corresponding input. What behaviour does that produce?

- **option1** All weights are adjusted equally, since the multiplication normalises the update
- **option2** Larger inputs receive smaller corrections, which keeps the weights balanced
- **option3** Weights on inputs of zero are left unchanged, so only connections that contributed to the mistake are adjusted
- **option4** Weights are adjusted in proportion to how wrong the prediction was, since the input value stands in for the size of the error made on that example

**answer** 3
**difficulty** medium
**bloomTaxonomy** understand
**topics** neural-networks-and-deep-learning
**subTopics** perceptron

**explanation**
An input of zero makes its update zero, so the neuron adjusts only the connections that actually took part. Larger inputs receive larger corrections rather than smaller ones. The size of the error is carried by the error term, which is plus one or minus one, not by the input value.

## Introduction to Artificial Intelligence - MCQ - 5.2.4

**description**
Why is it significant that a feedforward network is described as data rather than code?

- **option1** Because a nested list of numbers can be stored more compactly than a program
- **option2** Because learning then means altering that list of numbers, which is what makes training possible
- **option3** Because data can be inspected while code cannot
- **option4** Because a network stored as data can be executed on hardware that has no capacity to run arbitrary programs, which is what allows models to be deployed on small devices

**answer** 2
**difficulty** medium
**bloomTaxonomy** understand
**topics** neural-networks-and-deep-learning
**subTopics** feedforward-neural-networks

**explanation**
The forward pass function knows nothing about the problem and would run any network unchanged, because the network is a nested list of weights and biases. Behaviour living in numbers rather than in structure is exactly what lets a system change what it does by being nudged rather than rewritten.

## Introduction to Artificial Intelligence - MCQ - 5.2.5

**description**
A correction travelling back through ten sigmoid layers is multiplied by at most 0.25 at each one. What is left when it reaches the first layer, and what is the name of the problem?

- **option1** About one tenth, and the problem is called slow convergence, which is addressed by increasing the learning rate to compensate for the reduced signal
- **option2** About 2.5 percent, and the problem is called saturation
- **option3** About one thousandth, and the problem is called dead units
- **option4** About one millionth, and the problem is called the vanishing gradient

**answer** 4
**difficulty** medium
**bloomTaxonomy** apply
**topics** neural-networks-and-deep-learning
**subTopics** activation-functions

**explanation**
0.25 raised to the tenth power is about 9.5 times ten to the minus seven, so under one millionth, and 0.25 is the most optimistic figure since it requires every neuron to sit exactly at its steepest point. This is the vanishing gradient problem, and ReLU's slope of exactly 1 is what lets depth stop being self-defeating.

## Introduction to Artificial Intelligence - MCQ - 5.2.6

**description**
Why must the weights of a network be initialised randomly rather than all set to zero?

- **option1** Because identical weights make every neuron in a layer compute the same thing and receive the same correction forever
- **option2** Because zero weights make the loss function undefined at the first step
- **option3** Because random values reach the minimum faster than any fixed starting point
- **option4** Because a zero weight is interpreted as an absent connection, so a network initialised to zero would have no connections between its layers at all

**answer** 1
**difficulty** medium
**bloomTaxonomy** analyze
**topics** neural-networks-and-deep-learning
**subTopics** training-neural-networks

**explanation**
Random initialisation breaks symmetry. With identical weights, two neurons in the same layer produce identical outputs, receive identical blame, and update identically, so they remain duplicates however long training runs. The layer then has the capacity of a single neuron regardless of its width.

## Introduction to Artificial Intelligence - MCQ - 5.2.7

**description**
Deep learning is said to change what has to be designed. Under the older approach a domain expert spent months on features. What replaces that cost?

- **option1** Nothing, since learned features are obtained without additional cost of any kind
- **option2** A requirement for more powerful classifiers, since learned features are harder to separate
- **option3** A larger requirement for data and compute, since the representation is now learned rather than designed
- **option4** A requirement for a second expert, since somebody must interpret the learned features before the model can be deployed in a regulated setting

**answer** 3
**difficulty** medium
**bloomTaxonomy** understand
**topics** neural-networks-and-deep-learning
**subTopics** deep-learning

**explanation**
The expense moves rather than disappearing: often hundreds of thousands of examples and large compute, against thousands of examples and modest compute for the hand-built route. Explaining a decision also becomes harder, since the learned features are largely unnamed, but that is a consequence rather than a substitute cost.

## Introduction to Artificial Intelligence - MCQ - 5.2.8

**description**
Max pooling reduces a 6 by 6 feature map to 3 by 3, discarding three quarters of the values. What is deliberately thrown away, and why is that acceptable?

- **option1** The weakest responses, acceptable because they contribute little to the classification
- **option2** The precise position of a response within each block, acceptable because whether a feature was found nearby usually matters more than exactly where
- **option3** Every second row and column, acceptable because neighbouring pixels are nearly identical
- **option4** The sign of each response, acceptable because a feature map records the strength of a match and the direction of the change is not needed downstream

**answer** 2
**difficulty** medium
**bloomTaxonomy** understand
**topics** neural-networks-and-deep-learning
**subTopics** convolutional-neural-networks

**explanation**
Keeping only the strongest value in each block preserves the answer to whether the feature was found nearby while discarding exactly where within the block. For recognising a cat, whether the ear was at pixel 41 or 42 is noise, and a representation tolerant of small shifts is more robust than one that is not.

## Introduction to Artificial Intelligence - MCQ - 5.2.9

**description**
Which arrangement is a many-to-many unaligned sequence problem?

- **option1** Tagging each word of a sentence with its part of speech
- **option2** Classifying a spoken command into one of a fixed set of intents
- **option3** Translating a seven-word English sentence into a nine-word Hindi one
- **option4** Generating a caption from a single image, where one input produces a sequence of words as output

**answer** 3
**difficulty** medium
**bloomTaxonomy** remember
**topics** neural-networks-and-deep-learning
**subTopics** recurrent-neural-networks

**explanation**
Translation takes a sequence in and produces a sequence out of a different length, with the words not lining up. Part of speech tagging is many to many but aligned, one output per input. Intent classification is many to one, and captioning is one to many.

## Introduction to Artificial Intelligence - MCQ - 5.2.10

**description**
Attention lets any position reach any other in one step. What does it cost as sequences get longer?

- **option1** Cost grows linearly with length, as it does for recurrence
- **option2** Cost grows with the square of the length, since every pair of positions is compared
- **option3** Cost is unchanged, since all positions are processed simultaneously
- **option4** Cost grows with the square of the length, and also with the depth of the network, since each layer must recompute the comparisons made by the layer beneath it

**answer** 2
**difficulty** medium
**bloomTaxonomy** understand
**topics** neural-networks-and-deep-learning
**subTopics** attention-mechanism

**explanation**
Every position compares itself with every other, so the number of comparisons is the square of the sequence length. Recurrence grows linearly but pays in sequential execution and exponential information loss with distance. Layers do stack, but that multiplies by a constant rather than changing the growth in sequence length.

---

# Set 4

## Introduction to Artificial Intelligence - MCQ - 5.2.11

**description**
Which single principle borrowed from biology does the artificial neuron actually implement?

- **option1** That the number of units must approach the scale found in a human brain before useful behaviour appears
- **option2** That intelligence emerges from many simple units, each combining weighted signals and passing on a result
- **option3** That units communicate using electrical spikes timed to the millisecond
- **option4** That each unit maintains its own local memory of the signals it has previously received, which it consults before deciding whether to pass anything on

**answer** 2
**difficulty** medium
**bloomTaxonomy** understand
**topics** neural-networks-and-deep-learning
**subTopics** biological-inspiration

**explanation**
The borrowing is deliberately shallow: weighted combination, a threshold-like response, and capability residing in the connections rather than the units. Spike timing is not reproduced, scale is not a precondition for usefulness, and a plain artificial neuron holds no memory of past inputs at all.

## Introduction to Artificial Intelligence - MCQ - 5.2.12

**description**
The same six-line neuron function produces AND, OR, NAND, and a rule that ignores one input. What does that demonstrate about where behaviour lives?

- **option1** That the structure is fixed and the behaviour is entirely in the weights and bias
- **option2** That four separate neurons are required, one for each gate, and the shared function merely provides a convenient way of writing them all down
- **option3** That logical gates are a special case not representative of real neural computation
- **option4** That the function is being recompiled with different logic for each gate

**answer** 1
**difficulty** medium
**bloomTaxonomy** understand
**topics** neural-networks-and-deep-learning
**subTopics** artificial-neurons

**explanation**
Nothing about the unit changes; only what is passed to it does. That separation is what makes learning possible, because numbers can be nudged in response to a mistake while a structure cannot. One function serves all four gates precisely because the behaviour is not in the function.

## Introduction to Artificial Intelligence - MCQ - 5.2.13

**description**
Why does a perceptron require its features to be on comparable scales?

- **option1** Because it sums the features directly, so one measured in larger numbers dominates the weighted total
- **option2** Because the learning rule cannot process values above a fixed maximum
- **option3** Because unscaled features prevent the convergence theorem from applying
- **option4** Because the bias is a single number, and it cannot offset features whose magnitudes differ from one another by more than an order of magnitude

**answer** 1
**difficulty** medium
**bloomTaxonomy** understand
**topics** neural-networks-and-deep-learning
**subTopics** perceptron

**explanation**
Attendance running from 40 to 95 would swamp study hours running from 1 to 10 in the weighted sum, exactly as annual spend swamped monthly visits in the clustering lesson. Convergence still holds for separable data whatever the scaling; the practical problem is that learning becomes slow and lopsided.

## Introduction to Artificial Intelligence - MCQ - 5.2.14

**description**
A network of two layers and a network of two hundred run the same three lines of code a different number of times. Which statement explains why?

- **option1** Because deeper networks reuse the weights of earlier layers rather than holding their own
- **option2** Because each layer performs a slightly different operation, and the three lines contain a branch that selects the correct one according to the layer's depth
- **option3** Because the number of layers is a parameter of the operation rather than a count of how many times it runs
- **option4** Because every layer performs the same operation, weighted sums followed by an activation, on whatever signal it receives

**answer** 4
**difficulty** medium
**bloomTaxonomy** understand
**topics** neural-networks-and-deep-learning
**subTopics** feedforward-neural-networks

**explanation**
Forward propagation is one operation applied repeatedly, with each layer's output becoming the next layer's input. Nothing distinguishes the tenth layer from the first except what arrives at it. Each layer holds its own weights, which is why depth costs parameters as well as computation.

## Introduction to Artificial Intelligence - MCQ - 5.2.15

**description**
Which activation would you choose for the final layer of a model that must output the probability of a single yes-or-no outcome, and why?

- **option1** Sigmoid, because its output lies between 0 and 1 and reads as a probability
- **option2** Tanh, because it is centred on zero and steeper than the alternatives
- **option3** ReLU, because its output is unbounded and can represent any level of confidence
- **option4** Leaky ReLU, because it keeps a small slope for negative inputs and therefore never produces a completely uninformative output

**answer** 1
**difficulty** medium
**bloomTaxonomy** apply
**topics** neural-networks-and-deep-learning
**subTopics** activation-functions

**explanation**
Sigmoid's saturation makes it a poor choice deep inside a network and its range makes it the natural choice at the output of a binary classifier. Tanh suits hidden layers in shallow networks and recurrent cells, and the ReLU family suits hidden layers, where an unbounded output is a virtue rather than a problem.

## Introduction to Artificial Intelligence - MCQ - 5.2.16

**description**
Training the same XOR network from two different random seeds gives a loss of 0.00013 in one case and about 0.125 in the other, with one of the four cases wrong. What has happened, and what is the standard response?

- **option1** The second run was stopped too early, and the response is to increase the number of epochs until the loss falls to match the first run
- **option2** The second run found a local hollow in the loss landscape, and the response is to train several times and keep the best
- **option3** The second run overfitted the four examples, and the response is to add more data
- **option4** The second run used a different learning rate, and the response is to standardise it

**answer** 2
**difficulty** medium
**bloomTaxonomy** analyze
**topics** neural-networks-and-deep-learning
**subTopics** training-neural-networks

**explanation**
A real network's loss landscape has many hollows, and where the random weights start decides which one is found. Gradient descent has no way to climb out. Training repeatedly and keeping the best result is what practitioners do, and the proportion of seeds that succeed is the honest answer to whether the approach works.

## Introduction to Artificial Intelligence - MCQ - 5.2.17

**description**
Which problem is best suited to reusing the early layers of an already trained deep network rather than training from scratch?

- **option1** Grouping two lakh customer records into segments where no labels exist and the useful number of groups is not known in advance
- **option2** Predicting loan default from twelve columns of tabular financial data
- **option3** Computing income tax from published slabs
- **option4** Classifying a new set of product photographs with only a few thousand labelled images

**answer** 4
**difficulty** medium
**bloomTaxonomy** apply
**topics** neural-networks-and-deep-learning
**subTopics** deep-learning

**explanation**
Early layers of a vision network learn edges and textures that transfer across image tasks, so reusing them and retraining the later layers works well when labelled images are scarce. Tabular data does not benefit in the same way, tax needs rules rather than learning, and the clustering problem is unsupervised.

## Introduction to Artificial Intelligence - MCQ - 5.2.18

**description**
As a convolutional network gets deeper, what happens to the spatial size and the number of feature maps, and what is being traded?

- **option1** Spatial size grows and the number of maps shrinks, trading breadth of features for resolution
- **option2** Spatial size shrinks and the number of maps grows, trading knowing precisely where things are for knowing more about what they are
- **option3** Both shrink, trading total capacity for speed
- **option4** Spatial size shrinks while the number of maps stays constant, trading resolution for the ability to process larger images within the same memory budget

**answer** 2
**difficulty** medium
**bloomTaxonomy** understand
**topics** neural-networks-and-deep-learning
**subTopics** convolutional-neural-networks

**explanation**
Pooling halves the spatial size at each stage while later stages apply more filters, so the network progressively knows less about location and more about content. This produces the edges to textures to parts to objects hierarchy, with fully connected layers at the end turning parts into a verdict.

## Introduction to Artificial Intelligence - MCQ - 5.2.19

**description**
An encoder-decoder recurrent model translates well on short sentences and degrades sharply on long ones. What is the structural cause?

- **option1** The entire meaning of the source must pass through one fixed-size vector, so the longer the input the more is lost
- **option2** Longer sentences contain more rare words, which the model has seen less often
- **option3** The decoder runs out of vocabulary on longer sentences
- **option4** The encoder and decoder are trained separately, and the mismatch between them grows in proportion to the length of the sequence being processed

**answer** 1
**difficulty** medium
**bloomTaxonomy** analyze
**topics** neural-networks-and-deep-learning
**subTopics** recurrent-neural-networks

**explanation**
A four-word sentence and a forty-word paragraph are compressed into the same number of values, which is the bottleneck. Rare words are a genuine and separate difficulty. This specific failure is what attention was originally invented to fix, before it was ever proposed as a replacement for recurrence itself.

## Introduction to Artificial Intelligence - MCQ - 5.2.20

**description**
In self-attention over a sentence, why does each word usually attend most strongly to itself?

- **option1** Because a word's own meaning is the largest part of what it should carry forward
- **option2** Because the mechanism is required to include the current position in the average
- **option3** Because the softmax always assigns its largest weight to the first position examined
- **option4** Because a word's query and key are derived from the same vector, which forces the comparison of a word with itself to return the maximum possible score

**answer** 1
**difficulty** medium
**bloomTaxonomy** understand
**topics** neural-networks-and-deep-learning
**subTopics** attention-mechanism

**explanation**
The diagonal is usually the largest entry and that is sensible rather than a quirk, since the updated representation of a word should be mostly about that word. In a trained network the queries and keys are produced by separate learned projections, so a high self-score is a learned outcome rather than something forced by construction.

---

# Set 5

## Introduction to Artificial Intelligence - MCQ - 5.2.21

**description**
Which three components make up one transformer layer?

- **option1** Convolution, pooling, and a fully connected classifier
- **option2** Multi-head self-attention, a residual connection with normalisation, and a position-wise feedforward network
- **option3** An encoder, a decoder, and a positional encoding stage
- **option4** Self-attention, a recurrent cell to supply order, and a feedforward network applied to the sequence as a whole

**answer** 2
**difficulty** medium
**bloomTaxonomy** remember
**topics** neural-networks-and-deep-learning
**subTopics** transformers

**explanation**
Attention mixes information across positions, the feedforward network processes each position independently, and the residual connections with normalisation are what make a deep stack trainable at all. Positional encoding is added once at the input rather than being a component of every layer, and no recurrence appears anywhere.

## Introduction to Artificial Intelligence - MCQ - 5.2.22

**description**
What does using several attention heads rather than one buy a transformer layer?

- **option1** Faster computation, since the heads run in parallel and each handles a shorter sequence
- **option2** Redundancy, so the layer still works when one head fails
- **option3** Several different relationships can be attended to at once, since each head learns its own projections
- **option4** A larger effective context window, since each head attends to a different portion of the input and their outputs are concatenated to cover the whole of it

**answer** 3
**difficulty** hard
**bloomTaxonomy** understand
**topics** neural-networks-and-deep-learning
**subTopics** transformers

**explanation**
One head can express one pattern of attention per position. Several let a layer track, for instance, a grammatical dependency and a topical link simultaneously. Every head sees the full sequence, so the context window is unchanged, and heads are not a fault-tolerance mechanism.

## Introduction to Artificial Intelligence - MCQ - 5.2.23

**description**
Why is a decoder-only architecture the shape of most large language models?

- **option1** Because it sees only what precedes each position, which matches the task of predicting the next token
- **option2** Because it requires no positional encoding, unlike the other two families
- **option3** Because it processes the input in both directions, which gives a fuller picture of context
- **option4** Because it uses fewer parameters than an encoder for the same sequence length, which is what makes training at very large scale affordable

**answer** 1
**difficulty** medium
**bloomTaxonomy** understand
**topics** neural-networks-and-deep-learning
**subTopics** transformers

**explanation**
Restricting each position to what came before it is exactly the next-token prediction objective, and generation then proceeds one token at a time. Seeing both directions describes an encoder, which suits classification instead. All three families need positional encoding.

## Introduction to Artificial Intelligence - MCQ - 5.2.24

**description**
Foundation models are described as producing capability as a by-product of a simple objective pursued at enormous scale. What is that objective, and why is the phrasing significant?

- **option1** Reconstructing corrupted inputs, and it matters because the corruption process had to be tuned carefully for each type of data the model was trained on
- **option2** Minimising classification error across many labelled tasks, and it matters because the labels were expensive
- **option3** Predicting the next token, and it matters because nobody specified the individual capabilities that emerged
- **option4** Maximising a reward from human feedback, and it matters because the reward was designed deliberately

**answer** 3
**difficulty** medium
**bloomTaxonomy** understand
**topics** neural-networks-and-deep-learning
**subTopics** foundation-models

**explanation**
Training on unlabelled text to predict what comes next produced translation, summarising and code writing without any of them being targeted. Reinforcement from human feedback is applied afterwards to shape behaviour, and it is not the objective that produced the underlying capability.

## Introduction to Artificial Intelligence - MCQ - 5.2.25

**description**
A team has 5,000 labelled examples, a modest GPU budget, and needs a model specialised to its domain. Which adaptation method is the best fit?

- **option1** Few-shot prompting, since 5,000 examples can be summarised into a handful of representative cases and placed directly in the input
- **option2** Full fine-tuning, since 5,000 examples is enough to continue training every weight
- **option3** Zero-shot prompting, since describing the task avoids any training cost at all
- **option4** Partial fine-tuning, since freezing most weights and training a small added set suits this quantity of data and budget

**answer** 4
**difficulty** medium
**bloomTaxonomy** apply
**topics** neural-networks-and-deep-learning
**subTopics** foundation-models

**explanation**
Partial fine-tuning wants hundreds to thousands of examples and runs in minutes to hours, which matches both constraints. Full fine-tuning is affordable at this data volume but takes hours to days and more compute. Discarding 4,990 examples to fit a prompt throws away the specialisation the team is paying for.

## Introduction to Artificial Intelligence - MCQ - 5.2.26

**description**
A network is trained with a loss that measures mean squared error, while the business cares about catching rare fraudulent transactions. Where does this go wrong, and which part of the training machinery is at fault?

- **option1** The gradient, because rare cases produce small gradients that vanish before reaching the early layers
- **option2** The loss function, because it measures something other than what is actually cared about
- **option3** The learning rate, because rare cases require smaller steps to be learned properly
- **option4** Backpropagation, because it distributes blame evenly across examples regardless of how important each one is to the business

**answer** 2
**difficulty** medium
**bloomTaxonomy** evaluate
**topics** neural-networks-and-deep-learning
**subTopics** training-neural-networks

**explanation**
Everything downstream optimises whatever the loss states, so a loss that treats a missed fraud like any other small error will produce a model that ignores fraud and scores well. Backpropagation is exact bookkeeping and does its job faithfully, which is precisely why a badly chosen objective is pursued so efficiently.

## Introduction to Artificial Intelligence - MCQ - 5.2.27

**description**
Why does a filter applied to a colour image have three dimensions rather than two, and what does it produce at each position?

- **option1** Three dimensions because the filter slides in three directions, producing a volume of responses
- **option2** Three dimensions because it spans width, height and the colour channels, producing one number per position
- **option3** Three dimensions because a separate filter is needed for each colour, producing three feature maps
- **option4** Three dimensions because the third dimension holds the bias terms, producing one number per position for each of the biases stored in it

**answer** 2
**difficulty** hard
**bloomTaxonomy** understand
**topics** neural-networks-and-deep-learning
**subTopics** convolutional-neural-networks

**explanation**
A 3 by 3 filter on a colour image is really 3 by 3 by 3, covering all channels at once and summing to a single number per position. Deeper in the network the same idea scales: a layer receiving 64 feature maps uses filters of 3 by 3 by 64. The filter does not slide through the channel dimension.

## Introduction to Artificial Intelligence - MCQ - 5.2.28

**description**
Padding is described as treating the edges of an image more evenly. What is the uneven treatment it corrects?

- **option1** Edge pixels fall inside fewer filter positions than central ones, so they are examined less often
- **option2** Edge pixels are usually darker, which biases the filter response
- **option3** Edge pixels cannot be assigned a colour channel, so they are excluded from the calculation
- **option4** Edge pixels are shared between adjacent filter positions, so their contribution is counted more than once in the resulting feature map

**answer** 1
**difficulty** hard
**bloomTaxonomy** understand
**topics** neural-networks-and-deep-learning
**subTopics** convolutional-neural-networks

**explanation**
A 3 by 3 filter cannot be centred on the outermost row or column, so those pixels participate in fewer computations and the output shrinks each layer. Adding a border of zeros keeps the output the same size as the input and gives edge pixels a fairer share of the filter's attention.

## Introduction to Artificial Intelligence - MCQ - 5.2.29

**description**
Which failure would a recurrent weight above 1 produce, and how does it differ from the vanishing case?

- **option1** The state explodes without limit, whereas below 1 the early information disappears
- **option2** The state oscillates between two values, whereas below 1 it converges on a single one
- **option3** The state is unaffected, since the activation bounds it whatever the weight
- **option4** The state loses its sensitivity to new input, whereas below 1 it loses its memory of old input, so the two failures are mirror images with the same practical consequence

**answer** 1
**difficulty** medium
**bloomTaxonomy** analyze
**topics** neural-networks-and-deep-learning
**subTopics** recurrent-neural-networks

**explanation**
Repeated multiplication by a number above 1 grows without bound, so 1.05 raised to the fiftieth power is already about 11.5 and climbing. Below 1 the trace of early words decays exponentially. There is no setting that both remembers a long way back and stays stable, which is the bind, and a squashing activation limits the state without removing the underlying instability in the gradients.

## Introduction to Artificial Intelligence - MCQ - 5.2.30

**description**
A student concludes from a self-attention matrix that the model has discovered English grammar, because "quickly" attends most strongly to "drank". What is the flaw in that inference?

- **option1** There is no flaw, since a high attention weight between a verb and its adverb is direct evidence of learned grammar
- **option2** The vectors in the example were chosen by hand to have interpretable dimensions, so the pattern was built in rather than discovered
- **option3** Attention weights are normalised, so no individual weight can be interpreted
- **option4** The matrix shows only one layer, and grammatical structure emerges only once the outputs of several attention layers have been combined together

**answer** 2
**difficulty** hard
**bloomTaxonomy** evaluate
**topics** neural-networks-and-deep-learning
**subTopics** attention-mechanism

**explanation**
In the worked example the meaning vectors were hand-built with interpretable dimensions, so the sensible-looking pattern follows from how the numbers were chosen. In a trained network the vectors are learned and mostly not interpretable. What the example establishes is the mechanism and its shape, not that attention discovers grammar.
