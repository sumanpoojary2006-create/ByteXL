## Introduction

A food delivery company receives about forty thousand written reviews a week, and until last year a team of six read a sample of them and wrote a summary every Friday.

The summary was always late, always partial, and always slightly wrong, because six people cannot read forty thousand reviews and because the ones they sampled were whichever happened to be near the top. Meanwhile a restaurant whose quality had collapsed on Tuesday would not appear in any report until the following week.

The company wants the reviews read automatically. Sorted by sentiment, grouped by complaint, and flagged when a particular restaurant's tone shifts.

This is a harder problem than it sounds, and the reason is worth stating precisely. Every technique in this course so far has operated on numbers: sensor readings, pixel values, prices in lakh. A review is a sequence of characters. Before any model can touch it, somebody has to decide what a review is made of, and there is no obvious answer.

Turning language into something a machine can compute over, and back again, is **natural language processing**.

**Definition:** `Natural language processing` is the field concerned with enabling machines to work with human language, covering the conversion of text into structured representations, the extraction of meaning from it, and the generation of language as output.

![Visual explanation of introduction](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_section_introduction.png)

## Three Things People Mean by NLP

The term covers work of three quite different kinds, and separating them prevents a good deal of confusion.

- **Text processing** turns raw characters into structured units. Splitting into words, normalising spelling and case, tagging parts of speech, identifying names. Largely mechanical, and the necessary first step for everything else.
- **Language understanding** extracts meaning. Sentiment, topic, intent, the answer to a question, what a pronoun refers to. This is where the difficulty lives.
- **Language generation** produces text. Translation, summarising, replying, writing code.

The delivery company needs the first two. A chatbot needs all three.

![Visual explanation of nlp pipeline](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_nlp_pipeline_context_v4.png)

## Text Processing

The first job is unglamorous and consequential: deciding what counts as a unit.

Reading the code below: three small functions applied one after another, each two or three lines. `tokenise` splits, `remove_stopwords` deletes, `crude_stem` chops endings. The `stages` list exists only so the output can show the text after each step, and the point is to watch the token count fall from 14 to 10.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjbsr" 
 width="100%"
></iframe>

```
Raw text:
   The delivery was LATE!! Food arrived cold, and the app crashed twice. Not happy.

lowercased and split into tokens (14 tokens)
   ['the', 'delivery', 'was', 'late', 'food', 'arrived', 'cold', 'and', 'the', 'app', 'crashed', 'twice', 'not', 'happy']

stopwords removed (10 tokens)
   ['delivery', 'late', 'food', 'arrived', 'cold', 'app', 'crashed', 'twice', 'not', 'happy']

crudely stemmed (10 tokens)
   ['delivery', 'late', 'food', 'arriv', 'cold', 'app', 'crash', 'twice', 'not', 'happy']

Word counts after processing:
     delivery 1
         late 1
         food 1
        arriv 1
         cold 1
```

| In the code | What it does | What it discards |
| --- | --- | --- |
| `text.lower()` | Case folding | "LATE" and "late" merge, and the shouting is gone |
| `re.findall(r"[a-z']+", ...)` | Tokenising | All punctuation, including the exclamation marks |
| `t not in STOPWORDS` | Stopword removal | Common words, and negations if the list includes them |
| `t[: -len(ending)]` | Stemming | Word endings, producing "arriv", which is not English |
| `len(t) - len(ending) >= 4` | A length guard | Stops short words being chopped to nothing |

Four operations, each of which discards something.

**Lowercasing** makes "LATE" and "late" the same token, which is usually right and occasionally destroys meaning, since the writer's capitals were carrying anger that is now gone.

**Tokenising** with a pattern for letters throws away the exclamation marks, which were also signal. It would also mishandle "don't" if the apostrophe were not explicitly kept, and it has no idea what to do with a hyphenated word or a URL.

**Stopword removal** deletes very common words. Notice what survived: "not" is still there, and it is a stopword in many standard lists. Removing it would turn "not happy" into "happy", which is the opposite of what the review says. **The most common stopword list mistake is deleting negations.**

**Stemming** chops endings so that "crashed" and "crashes" become one token. The crude version here produces "arriv", which is not a word, and that is normal: stems are matching keys rather than English.

Every step trades information for uniformity. The pipeline is a series of judgment calls, and getting them wrong is a far more common cause of a bad language system than choosing the wrong model.

![Visual explanation of text processing](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_section_text_processing_simple_v2.png)

## Finding What a Document Is About

Once text is tokens, the next question is which words matter. Counting is the obvious approach and it fails immediately, because the most frequent words in any English document are "the", "and", and "was".

The standard repair weighs each word by how rare it is across the whole collection. A word appearing in every document distinguishes nothing; a word appearing in one document is highly characteristic of it. Combining how often a word appears in this document with how rarely it appears in others gives `TF-IDF`.

Reading the code below: TF-IDF is a product of two numbers, and each is computed separately. `term_frequency` is the TF half, counting within one review. `inverse_doc_freq` is the IDF half, computed once across all four reviews. The line that multiplies them, `tf[w] * inverse_doc_freq[w]`, is the whole method.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjc7b" 
 width="100%"
></iframe>

```
Weight given to a word, by how many of the four reviews contain it:
   in 4 reviews: weight 0.000   ['and', 'the', 'was']
   in 3 reviews: weight 0.288   ['biryani']
   in 2 reviews: weight 0.693   ['cold', 'delivery', 'excellent', 'late']
   in 1 reviews: weight 1.386   ['again', 'arrived', 'food', 'hot', 'on', 'quick', 'service', 'terrible', 'time']

Most distinctive words in each review, by TF-IDF:
   r1: quick (0.154), service (0.154), excellent (0.077)
   r2: arrived (0.139), hot (0.139), on (0.139)
   r3: cold (0.077), delivery (0.077), late (0.077)
   r4: again (0.116), food (0.116), terrible (0.116)

Words in every review score exactly zero, however often they occur.
The measure finds what makes a document different, not what it contains.
```

| In the code | Which half | What it measures |
| --- | --- | --- |
| `c / len(tokens)` | TF | How much of this one review is this word |
| `appears_in[w]` | Input to IDF | How many reviews contain it at all |
| `math.log(len(docs) / appears_in[w])` | IDF | Rarity across the collection; 0 if in every review |
| `tf[w] * inverse_doc_freq[w]` | The score | Frequent here and rare elsewhere scores highest |
| No stopword list anywhere | The consequence | Common words zero themselves out |

The first table is the mechanism laid bare. A word in all four reviews gets a weight of exactly zero, so "the", "and", and "was" contribute nothing no matter how often they appear. A word in only one review gets 1.386, the highest available.

The result is that no stopword list was needed. **The common words suppressed themselves**, because being common is precisely what the measure penalises, and that is more robust than maintaining a list of words to delete.

Read the per-review results and the summary the delivery company wanted is already visible. Reviews r1 and r2 surface quick, service, excellent, arrived, hot. Reviews r3 and r4 surface cold, delivery, late, terrible. Nobody labelled these as positive or negative; the distinctive vocabulary separated them.

TF-IDF is decades old, takes twenty lines, and remains a sensible baseline for search and document classification. It is worth knowing before reaching for anything larger.

![Visual explanation of finding what a document is about](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_section_finding_what_a_document_is_about_simple_v2.png)

## Where Counting Words Breaks

The approach above treats a document as an unordered collection, and language is not unordered.

Reading the code below: two scorers on the same four sentences. `unigram_score` is two lines, counting positive words and subtracting negative ones. `bigram_score` walks the sentence in overlapping pairs so that a negation can flip whatever follows it, and the `skip` flag stops the flipped word being counted a second time on its own.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjcgs" 
 width="100%"
></iframe>

```
                            review  single words  word pairs
-------------------------------------------------------------
                 the food was good             1           1
             the food was not good             1          -1
        the service was never slow            -1           1
        not bad at all, quite good             0           2

Counting words one at a time cannot see 'not'. Looking at pairs can,
because the meaning of 'good' depends on the word immediately before it.

This is why 'n-grams', short runs of consecutive words, were the
standard fix for decades. They only reach as far as n words, though:
no fixed n handles 'the food, despite everything, was not good'.
```

| In the code | What it sees | Where it fails |
| --- | --- | --- |
| `unigram_score` | One word at a time | Cannot see "not", so it gets the sign wrong |
| `zip(tokens, tokens[1:])` | Overlapping pairs | The window is exactly two words wide |
| `first in ("not", "never", "no")` | A negation | Only flips the word immediately after it |
| `skip = True` | Bookkeeping | Stops the flipped word being counted twice |
| Anything beyond two words apart | Invisible to both | The limitation the whole section is building to |

Rows two and three are the ones that matter. "The food was not good" scores +1 by counting words, which is the wrong sign, and "the service was never slow" scores −1, also the wrong sign. Looking at pairs fixes both.

It fixes them within a window of two, and that is the limitation. The final line of output names the problem: a negation separated from its target by an intervening clause is invisible to bigrams, and extending to trigrams or four-grams only moves the boundary. There is no fixed window that handles arbitrary distance, and the number of possible n-grams explodes as n grows.

That difficulty, a relationship between two words that may be any distance apart, is precisely what the attention-based architectures were built to solve, and it is why modern language systems abandoned fixed windows entirely.

![Visual explanation of bow vs embeddings](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_bow_vs_embeddings_context_v4.png)

## Words as Positions Rather Than Symbols

Everything above treats a word as a symbol that either matches another word or does not. That is a second limitation, separate from word order, and it is arguably larger.

To a counting method, "excellent" and "superb" are as unrelated as "excellent" and "biryani". They are different strings, so they occupy different columns and share nothing. A review praising the food with one word contributes nothing to understanding a review praising it with the other, which means the system needs to see every synonym separately before it can learn anything about any of them.

The repair is to stop representing a word as a symbol and start representing it as a position. A `word embedding` gives each word a vector of perhaps 300 numbers, arranged so that words used in similar contexts sit near each other. "Excellent" and "superb" end up close together; "biryani" ends up somewhere else entirely, near "dosa" and "paratha".

The method for producing them is the self-supervised trick in miniature: train a model to predict a word from its neighbours, or its neighbours from it, across a very large quantity of text. Nothing is labelled, and the vectors that make that prediction work turn out to encode a great deal about meaning.

Two consequences follow, and the first is the practically important one.

**Similarity becomes computable.** A system can now recognise that two reviews say the same thing in different words, which is what makes search return relevant results that do not contain your exact search terms.

**Relationships appear as directions.** The often-quoted result is that the vector arithmetic for king minus man plus woman lands near queen, and similar patterns hold for country and capital, or singular and plural. This is genuinely surprising and it is also frequently overstated: the arithmetic works for some relationships and not others, and the neat examples are selected.

One limitation carried over into everything until quite recently. A single vector per word cannot handle a word with several meanings, so "bank" gets one position averaging the financial and the riverside senses, serving neither. Producing a different vector for a word depending on the sentence it appears in is exactly what the attention-based models later provided.

![Visual explanation of words as positions rather than symbols](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_section_words_as_positions_rather_than_symbols.png)

## What Makes Language Hard

Four difficulties recur across every language task, and they are worth naming because they explain why progress here lagged behind vision for so long.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Difficulty</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Why it resists a simple fix</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Ambiguity</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"The order was light" could praise or complain</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Resolving it needs knowledge outside the sentence</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Long-range dependence</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A negation twenty words from what it negates</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No fixed window is large enough</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Variation</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Spelling, slang, code-switching between languages mid-sentence</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The vocabulary is effectively unbounded</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Implication</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"I waited an hour for a dosa" contains no negative word</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The complaint is inferred, not stated</td>
    </tr>
  </tbody>
</table>

The last row is the one that defeats every word-counting method completely. There is nothing in that sentence to count. A person understands it because they know how long a dosa should take, and that knowledge is nowhere in the text.

![Visual explanation of what makes language hard](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/01_section_what_makes_language_hard.png)

## Your Turn

Break the stopword list deliberately.

Add "not" and "never" to `STOPWORDS` in the first program, then run the third program's reviews through the full pipeline before scoring them. Both negated reviews will now score positive. This is not a hypothetical: standard stopword lists in widely used libraries include negations, and a sentiment system built carelessly on top of one will confidently report the opposite of what customers wrote.

Then extend the TF-IDF program with a fifth review that is simply the word "biryani" repeated ten times. Look at what happens to its scores and to the weight of "biryani" across the collection. Term frequency rewards repetition, so a spam review can dominate, and you will see why real implementations dampen the frequency term rather than using it raw.

Finally, take the fourth row of the difficulty table seriously. Write five review sentences that are clearly complaints and contain no negative word at all. Then decide, for each one, what a system would need to know in order to understand it. If your answers involve expectations about time, portion size, or price, you have identified exactly the kind of world knowledge that word counting cannot supply and that large pre-trained models absorbed by accident.
