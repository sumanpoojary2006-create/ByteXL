## Introduction

Kavya translates equipment manuals from English into Tamil, and her new trainee notices a habit he finds inefficient: she keeps one finger resting on the source page the entire time she is typing, and her eyes go back to it every few words.

She is not reading a sentence once, compressing the whole thing into a single thought, and producing the translation from that compressed thought alone. She reads it, begins translating, and while producing each word looks back at the specific part of the original that word depends on. Getting the verb ending right means glancing back at the subject, which may be twenty words earlier.

A recurrent network is forced to work the other way. Everything it has read is squeezed into one fixed-size state and handed forward. By the time the last word arrives, the first word survives only as a faint residue in a handful of numbers, and if the first word was the one that mattered, it has been lost.

The alternative is to stop compressing. Keep every position available, and let each position look directly at whichever others are relevant to it, choosing for itself. Nothing has to survive a chain of handovers, because everything is one step away.

That mechanism is **attention**, and it is the idea modern language models are built on.

**Definition:** `Attention` computes, for a given position, a set of weights over all available positions and returns a weighted average of their values, so that the position draws information directly from wherever it is relevant rather than through a chain of intermediate steps.

![Kavya keeps a finger on an English equipment manual while linking each Tamil phrase to the relevant source words](images/10_section_introduction_v2.png)

## Attention Is a Soft Lookup

The mechanism is best understood as a lookup that returns a blend rather than a single match.

An ordinary dictionary lookup takes a key and returns exactly one value. Attention takes a `query`, compares it against every `key`, converts those comparisons into weights that sum to 1, and returns the correspondingly weighted mixture of all the `values`.

Three pieces, then:

- **Query:** what this position is looking for.
- **Keys:** what each available position offers, used for matching.
- **Values:** what each position actually contributes if selected.

Reading the code below: `attend` is four lines and is the whole mechanism. Compare the query with every key using `dot`, turn those scores into weights with `softmax`, and that is attention. `softmax` converts any list of numbers into positive numbers summing to 1; the `- biggest` inside it is only there to stop `math.exp` overflowing and changes nothing about the result.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjvmj" 
 width="100%"
></iframe>

```
Attention is a soft lookup: the query is compared with every key,
and the scores become weights that sum to 1.

query strongly matching 'capital city'  ->  [0.909, 0.045, 0.045]
       capital city  0.909 ####################################  (Delhi)
         main river  0.045 #  (Ganga)
       tallest peak  0.045 #  (Kanchenjunga)

query torn between two keys  ->  [0.44, 0.398, 0.162]
       capital city  0.440 #################  (Delhi)
         main river  0.398 ###############  (Ganga)
       tallest peak  0.162 ######  (Kanchenjunga)

query matching nothing in particular  ->  [0.333, 0.333, 0.333]
       capital city  0.333 #############  (Delhi)
         main river  0.333 #############  (Ganga)
       tallest peak  0.333 #############  (Kanchenjunga)

A sharp query picks out one entry. A vague query spreads its weight.
Nothing is ever fully discarded, which is why it is called soft.
```

| In the code | Which of the three pieces | What it does |
| --- | --- | --- |
| The argument to `attend` | Query | What this position is looking for |
| `[1.0, 0.0, 0.0]` in `ENTRIES` | Key | What an entry offers, used for matching |
| `"Delhi"` in `ENTRIES` | Value | What that entry contributes if selected |
| `dot(query, k)` | The comparison | One score per entry, larger for a better match |
| `softmax(scores)` | The blend | Scores become weights summing to 1 |
| Weights never reaching 0 | Softness | Nothing is fully discarded, so it stays trainable |

Three queries, three different behaviours from one mechanism.

The first query matches one key strongly and comes back with 0.909 of that entry's value. The second is genuinely torn and returns a blend. The third matches everything equally and returns the plain average, which is attention's way of saying it has no opinion.

The softness is the property that makes this trainable. A hard lookup, picking the single best match, has no useful notion of "slightly better", so there would be nothing for gradient descent to work with. **Because the weights vary smoothly, the network can learn what to look for**, adjusting queries and keys a little at a time.

![Visual explanation of attention soft lookup](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/10_attention_soft_lookup.png)

## Self-Attention

In `self-attention`, the sequence attends to itself. Every position produces a query, a key, and a value, and every position uses its query against all the keys, including its own.

The result is that each word's new representation is a blend of all the words, weighted by relevance to it.

Reading the code below: `self_attention` is five lines. The word "self" is visible in one detail, that `vectors` supplies the queries and the keys, so each word is compared against every word including itself. The result is a square matrix, one row per word, each row summing to 1.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjw2k" 
 width="100%"
></iframe>

```
Every word looks at every word. Each row sums to 1.

               the      cat    drank     milk  quickly
------------------------------------------------------
      the    0.185    0.205    0.211    0.203    0.197
      cat    0.141    0.354    0.192    0.154    0.159
    drank    0.119    0.157    0.336    0.170    0.217
     milk    0.140    0.155    0.210    0.346    0.149
  quickly    0.148    0.174    0.290    0.162    0.226

  'the' attends most to drank (0.21) and cat (0.20)
  'cat' attends most to drank (0.19) and quickly (0.16)
  'drank' attends most to quickly (0.22) and milk (0.17)
  'milk' attends most to drank (0.21) and cat (0.16)
  'quickly' attends most to drank (0.29) and cat (0.17)
```

| In the code | What it is | Note |
| --- | --- | --- |
| `vectors` used as both queries and keys | The "self" in self-attention | Each word is compared with every word, itself included |
| One `rows.append(...)` per word | One row of the matrix | How that word distributes its attention |
| Each row sums to 1 | The softmax guarantee | Attention is a blend, not a score |
| The diagonal | A word attending to itself | Usually the largest entry, and reasonably so |
| Any row entry | Reaches any distance in one step | No decay between position 1 and position 50 |
| Rows are independent | Parallelism | All rows can be computed at once |

The matrix is the whole picture. Row "drank" says how much the word "drank" draws from each word in the sentence when building its updated representation.

Two patterns are visible and both are typical of real attention. Every word attends most strongly to itself, which is sensible since its own meaning is the largest part of what it should carry forward. And the off-diagonal weights are not uniform: "quickly" gives 0.29 to "drank", the word it modifies, and "milk" gives 0.21 to "drank", the verb acting on it.

Be careful about how much to read into this. These vectors were chosen by hand to have interpretable dimensions, and in a trained network the vectors are learned and mostly not interpretable. What the example establishes is the mechanism and its shape, not that attention discovers grammar.

The critical structural property is what the matrix implies about distance. **Every word reaches every other word in one step.** The weight from position 1 to position 50 is computed exactly like the weight from position 1 to position 2, with no decay in between. The exponential forgetting of a recurrent state simply does not arise.

And every row can be computed independently, so a sequence of 2,000 words is 2,000 rows calculated simultaneously rather than 2,000 dependent steps. Attention solves the memory problem and the parallelism problem with one mechanism, which is why it displaced recurrence rather than supplementing it.

![Visual explanation of self attention positions](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/10_self_attention_positions.png)

## What Attention Does Not Know

There is a catch, and it is large enough that attention is unusable without a fix.

Reading the code below: `attention_for` returns a dictionary rather than a list, which is the trick that makes the comparison readable. The same word maps to the same weight in both runs, so the two dictionaries can be compared directly with `==` despite the words being printed in a different order.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjwcj" 
 width="100%"
></iframe>

```
What 'drank' pays attention to, in two different word orders

  original: the cat drank milk quickly
            {'the': 0.1189, 'cat': 0.1574, 'drank': 0.3365, 'milk': 0.1705, 'quickly': 0.2167}

  shuffled: milk quickly the drank cat
            {'milk': 0.1705, 'quickly': 0.2167, 'the': 0.1189, 'drank': 0.3365, 'cat': 0.1574}

Identical attention to every word: True

Self-attention has no idea what order the words came in. It sees a
bag of vectors, not a sequence. 'cat drank milk' and 'milk drank cat'
would produce exactly the same attention weights.

The fix is to add position information into each word's vector before
attention runs, so that a word at position 1 and the same word at
position 4 arrive as different vectors.
```

| In the code | What it is | Why it matters |
| --- | --- | --- |
| `dot(query, WORDS[other])` | The score | Mentions the two vectors and nothing about position |
| `shuffled` | Same words, new order | The only difference between the two runs |
| The returned dictionary | Word to weight | Lets the two runs be compared regardless of print order |
| `same` is `True` | Permutation invariance | Order has no effect on the mechanism at all |

Shuffle the sentence and every attention weight is preserved exactly. Attention is `permutation invariant`: it treats the input as an unordered collection.

This is a direct consequence of how the weights are computed. A score is a comparison between two vectors, and nothing in that comparison mentions where either vector sat. The mechanism that freed us from processing in order also lost all knowledge of order, and "the cat drank the milk" and "the milk drank the cat" become indistinguishable.

The remedy is `positional encoding`: before attention runs, a vector representing each position is added to each word's vector. The same word at position 1 and position 4 then arrives as two different vectors, so scores computed from them differ, and order re-enters the calculation.

It is worth appreciating how much this admits. Recurrence got order for free, as an unavoidable consequence of processing one step at a time, and paid for it in forgetting and slowness. Attention gets speed and reach for free and has to add order back in by hand.

![Visual explanation of what attention does not know](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/10_section_what_attention_does_not_know_simple_v2.png)

## Why the Scores Are Divided

There is one detail in every real implementation that looks arbitrary and is not. Before the softmax, the scores are divided by the square root of the vector dimension.

The reason connects directly to saturation. A dot product is a sum of products across dimensions, so the more dimensions there are, the larger the sums get. In 4 dimensions the scores across a handful of random vectors might span a range of about 3. In 512 dimensions the same comparison spans a range closer to 89.

Now recall what softmax does with large gaps. It exponentiates, so a score 89 higher than its neighbours produces a weight indistinguishable from 1.0000, with everything else rounding to zero. The attention has become a hard selection: one position takes everything and the rest are ignored entirely.

That is a disaster for training rather than merely for accuracy. A softmax pinned at 1 and 0 is flat, its slope is essentially zero, and the correction passing back through it vanishes. **The attention layer saturates in exactly the way sigmoid saturates**, and for exactly the same reason.

Dividing by the square root of the dimension counteracts the growth, because that is roughly how fast the spread grows with dimension. The scores return to a range where softmax produces a genuine distribution rather than a hard pick, and gradients survive.

It is worth noticing what this says about the design as a whole. Attention was presented as a clean idea about direct access between positions, and making it work at realistic scale required a correction factor derived from how random sums behave. Most of the difference between an idea that works on a toy and one that trains on billions of words is made of details like this.

![Visual explanation of why the scores are divided](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/10_section_why_the_scores_are_divided.png)

## Attention at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Aspect</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Recurrence</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Attention</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reaching a distant word</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Through every step in between</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Directly, in one step</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Information loss with distance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Exponential decay</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">None</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Computation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sequential; cannot be parallelised</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">All positions at once</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Knows the order</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Inherently</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No; must be added as positional encoding</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Cost with sequence length</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Grows linearly</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Grows with the square, since every pair is compared</td>
    </tr>
  </tbody>
</table>

The last row is attention's own limitation and the reason long contexts are expensive. A thousand words means a million pairwise comparisons; ten thousand words means a hundred million. Reducing that cost is an active area of research and the practical reason context windows have limits.

![Visual explanation of attention at a glance](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/10_section_attention_at_a_glance.png)

## Your Turn

Change one word's vector and watch the whole matrix move.

In the self-attention program, give "milk" the vector `[0.9, 0.9, 0.1]`, making it partly animate. Rerun and compare the row for "drank". A single changed vector alters what every word attends to, because every weight is computed against every other. That interdependence is why attention is powerful and why it is hard to reason about one weight at a time.

Then fix the position problem yourself. Before computing attention, add a small position vector to each word: `[0.0, 0.0, 0.1 * index]`, so the first word gets nothing added and later words get progressively more in the third dimension. Rerun the permutation test and confirm the two orderings now differ. Then consider what you have broken: your encoding makes later words look more like action words, since you added to the dimension that means action. Designing a positional encoding that carries position without corrupting meaning is a genuine problem, and real systems use carefully constructed patterns for exactly this reason.

Finally, do the cost arithmetic. Attention compares every position with every other, so a sequence of length n needs n squared comparisons. Compute the number for 100, 1,000, and 100,000 words. Then work out how many times more expensive a 100,000-word context is than a 1,000-word one, and you will understand why context length is quoted as a headline specification rather than assumed to be unlimited.
