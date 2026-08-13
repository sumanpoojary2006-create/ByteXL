## Introduction

A streaming service in India carries about eight thousand titles. A subscriber opening the app has, in practice, about twelve seconds and one screen.

The catalogue is not a menu; it is a problem. Nobody browses eight thousand items, and a service that requires them to is a service people close. So the twelve titles on that screen have to be chosen, and choosing them well is worth more to the business than most of what else the engineering team does.

There is no obvious basis for choosing. The subscriber has not typed a query, has not stated a preference, and would struggle to describe their own taste if asked. What the service has is a record of what they watched, and a record of what several million other people watched.

Turning that into twelve titles is a **recommendation system**, and it is quietly the most commercially significant application of machine learning there is.

**Definition:** A `recommendation system` predicts which items a person will find relevant, using either the attributes of items the person already liked, called `content-based filtering`, or the behaviour of other people with similar histories, called `collaborative filtering`.

![Visual explanation of introduction](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_section_introduction.png)

## Content-Based Filtering

The first approach uses the items themselves. Describe each film by its attributes, build a profile of the attributes a viewer has liked, and score everything against that profile.

Reading the code below: two lines carry the method. `profile` averages the trait vectors of the films Meera liked, and `similarity` measures how closely two vectors point in the same direction, ignoring their length. That second property matters, since it means a film scoring 5, 0, 0, 5 and one scoring 2, 0, 0, 2 count as identical in taste.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjcwq" 
 width="100%"
></iframe>

```
Meera liked: Dhoom Chase, The Long Night
Her taste profile: [4.0, 0.5, 1.0, 4.5]
   action 4.0  romance 0.5  comedy 1.0  thriller 4.5

Every film scored against that profile:
        Dhoom Chase 0.975 #######################################  (already seen)
     The Long Night 0.966 ######################################  (already seen)
       Office Hours 0.298 ###########
     Wedding Season 0.179 #######
    Monsoon Letters 0.136 #####

Recommendation: Office Hours
It was chosen for resembling what she liked, using nothing about
any other viewer.
```

| In the code | What it is | Note |
| --- | --- | --- |
| `FILMS` | Trait vectors | Somebody had to write these by hand |
| `profile` | The average of what she liked | Four numbers standing in for a person's taste |
| `dot / (size_a * size_b)` | Cosine similarity | Compares direction, ignoring magnitude |
| `scores` | Every film against the profile | Including ones she has already seen |
| `f not in LIKED` | The filter | Recommending a film she just watched would be useless |

The profile is the whole method: Meera's two favourites average to high action, high thriller, low romance, and every film is then scored by how closely its trait vector points in that direction.

Notice the gap in the scores. The two films she has already seen score 0.97, and the best unseen candidate scores 0.298. **The system is confident about what she already likes and has very little to offer beyond it**, because the catalogue contains nothing else in that direction. That gap is the characteristic weakness of the approach.

Two strengths are worth naming. It works from the first rating, since a profile can be built from one film. And it can explain itself: the recommendation is because you liked action thrillers, which is a sentence a user will accept.

The weakness is `over-specialisation`. A profile built from action thrillers recommends action thrillers forever. It cannot discover that Meera would enjoy a documentary, because nothing in her profile points that way and nothing in the method looks outside it.

![Visual explanation of recommender methods](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_recommender_methods_context_v4.png)

## Collaborative Filtering

The second approach ignores the items entirely and uses other people.

Reading the code below: `similarity` now compares two people rather than two films, and the important line is the first one inside it, which keeps only films both viewers have rated. The prediction at the end is a weighted average, where each neighbour's opinion counts in proportion to how much their taste matches Meera's. There is no `FILMS` trait table anywhere in this program.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjd8g" 
 width="100%"
></iframe>

```
Which viewers resemble Meera?

     Arjun similarity 0.974   their rating of 'Office Hours': 3
     Priya similarity 0.467   their rating of 'Office Hours': 4
     Kabir similarity 0.987   their rating of 'Office Hours': 2
     Sneha similarity 0.599   their rating of 'Office Hours': 5

Predicted rating for Meera on 'Office Hours': 3.22

Nothing about the film itself was used. No genre, no cast, no plot.
The prediction comes entirely from who else liked what.
```

| In the code | What changed from the content-based version | Note |
| --- | --- | --- |
| `RATINGS` replaces `FILMS` | People, not traits | No genre, cast, or plot anywhere |
| `similarity(a, b)` | Compares two viewers | Same cosine formula, different inputs |
| `if x is not None and y is not None` | Handles gaps | Only films both people rated can be compared |
| `sum(s * r) / sum(s)` | The prediction | A weighted average of neighbours' ratings |
| `s` as the weight | Trust | Kabir at 0.987 counts far more than Sneha at 0.599 |

Read the similarity column and the logic is visible. Kabir at 0.987 and Arjun at 0.974 have taste close to Meera's, and both rated Office Hours low. Sneha at 0.599 loved it, and her opinion is discounted accordingly. The weighted average lands at 3.22.

The remarkable thing is what the program never knew. It has no idea that Office Hours is a comedy, who is in it, or what it is about. **The prediction is derived entirely from the pattern of who liked what**, and this is why collaborative filtering routinely outperforms content-based methods in practice: patterns of taste capture things no attribute list contains.

This is also why recommendations sometimes surprise people usefully. A content-based system cannot suggest something unlike what you have watched. A collaborative one can, if people resembling you liked it, and no explanation in terms of genre is needed or available.

![Visual explanation of collaborative filtering](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_section_collaborative_filtering.png)

## Cold Start

Collaborative filtering has one structural failure, and every service has to plan for it.

Reading the code below: `similarity` is unchanged and `predict` is the previous block's weighted average packaged into a function. What is new is in the data. A sixth film has `None` from everybody and a sixth viewer has `None` for everything, and the `return ... if total_weight else None` at the end of `predict` is what turns both into a refusal rather than a crash.

<iframe
 frameBorder="0"
 height="350px"  
 src="https://onecompiler.com/embed/python/44xvzjdnw" 
 width="100%"
></iframe>

```
Two things collaborative filtering cannot do

1. A brand new film, 'Quiet Harvest', that nobody has rated:
   predicted rating for Meera: None
   No ratings exist, so there is nothing to base a prediction on.

2. A brand new viewer, Rohan, who has rated nothing:
   predicted rating for 'Dhoom Chase': None
   predicted rating for 'Monsoon Letters': None
   He resembles nobody, because similarity needs shared ratings.

This is the cold start problem. Content-based methods handle both
cases, because a film's traits and a stated preference exist even
when no ratings do. Real systems therefore use both approaches.
```

| In the code | The cold start case | Why it fails |
| --- | --- | --- |
| `"Quiet Harvest"` with `None` from everyone | A new item | `ratings[film_index] is None` skips every neighbour |
| `"Rohan"` with `None` for everything | A new user | `len(shared) < 2` makes every similarity 0.0 |
| `total_weight` stays at 0 | Both cases | Nothing to divide by, so no prediction exists |
| `else None` | The honest answer | Better than inventing a number from no evidence |

Two `None` values where a recommendation should be, and neither is a bug.

A new title has no ratings, so nothing supports a prediction, and the service's newest and most heavily promoted content is exactly what the recommender cannot recommend. A new subscriber has rated nothing, so no similarity can be computed with anyone, and the first session is when they decide whether to keep the subscription.

Both are addressed by combining the approaches. Content-based methods work from attributes that exist before any rating does, so a new film can be recommended on its genre and cast, and a new subscriber can be asked to pick three favourite titles at signup, which is what that onboarding screen is for. **The two methods fail in different places, which is why production systems are hybrids rather than one or the other.**

![Visual explanation of cold start objectives](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_cold_start_objectives_context_v4.png)

## Nobody Rates Anything

The programs above assume a table of ratings out of five. Real services largely do not have one.

Asking people to rate things produces very little data, because rating is effort with no immediate reward, and the little it produces is skewed: people rate what they loved and what they hated, and almost nothing in between. A service with ten million subscribers may have ratings from a small fraction of them.

What every service does have is behaviour. Whether a title was opened, how far into it the viewer got, whether they finished it, whether they came back the next day, whether they abandoned it after ninety seconds. This is `implicit feedback`, and it is abundant where ratings are scarce.

It also behaves quite differently, in ways worth knowing.

- **There are no negatives.** A rating of 1 says "I disliked this". Not watching something says nothing at all, since the viewer may never have seen it exist. Most of the matrix is not missing data, it is unobserved, and treating unwatched titles as dislikes is a common and damaging error.
- **The signal is noisy.** A title watched to the end may have been playing while somebody cooked. A title abandoned at ten minutes may have been interrupted.
- **Confidence varies with quantity.** One click means little; twelve visits to the same series means a great deal. Implicit methods therefore weight observations by how much evidence they represent, rather than treating each as a rating.

Alongside this, the technique that actually powers large recommenders is not the neighbour-by-neighbour comparison above, which does not scale to millions of users. It is `matrix factorisation`: representing each viewer and each item as a short vector of learned numbers, chosen so that the dot product of a viewer's vector with an item's vector reproduces the observed behaviour.

Those learned dimensions are not genre labels and nobody names them. They emerge as whatever best explains the data, and they often correspond loosely to things a person might recognise, such as a preference for long-running series or for regional-language content. The important property is practical: once every viewer and item is a short vector, scoring the entire catalogue for one person is a few thousand multiplications rather than a comparison against every other subscriber.

![Visual explanation of nobody rates anything](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_section_nobody_rates_anything.png)

## What Recommenders Optimise, and Why It Matters

The mechanics are the easy part. The consequential question is what the system is told to maximise.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Optimising for</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Behaviour it produces</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Failure it invites</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Clicks</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Surfaces whatever attracts attention</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rewards misleading titles and thumbnails</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Watch time</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Favours long and absorbing content</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Optimises for time spent, not time well spent</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Predicted rating</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Suggests things you will approve of</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Recommends the safe and familiar; narrows over time</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Long-term retention</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Closest to what the business actually wants</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Feedback arrives months later, so it is hard to train on</td>
    </tr>
  </tbody>
</table>

The bottom row states the real difficulty. The thing worth maximising is slow to measure, and the things easy to measure are proxies that diverge from it. A system trained on clicks will find that outrage attracts clicks, and nothing in the training objective knows that is a problem.

Two further effects deserve naming because they are properties of the system rather than of any model.

**Feedback loops.** A recommender shapes what people see, which shapes what they watch, which becomes the training data for the next version. A title never recommended is never watched and therefore never learns that anyone would have liked it.

**Popularity bias.** Items with many ratings are easier to predict confidently, so they get recommended more, gathering more ratings. The catalogue's long tail stays invisible unless something deliberately counteracts this.

Both are reasons real systems inject deliberate exploration, showing things the model is unsure about, accepting a small immediate cost for information and variety.

![Visual explanation of what recommenders optimise, and why it matters](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_section_what_recommenders_optimise_and_why_it_matters.png)

## Your Turn

Give Meera a third favourite that breaks her profile, such as `Monsoon Letters`, and rerun the content-based program.

Watch what happens to the profile and to the ranking. Averaging a romance into an action-thriller profile produces a middling vector that resembles nothing strongly, and the top recommendation may become a film matching neither taste. This is a real weakness of representing a person as one average: people have several distinct tastes, and a single profile blends them into a compromise nobody wanted.

Then make the two methods disagree. Using the collaborative program, find a film where the content-based score and the collaborative prediction point in opposite directions. Then decide which you would show, and write the rule a production system should follow when its two components disagree. There is no single right answer, and having a stated rule is better than whichever component happens to run last.

Finally, take the feedback loop seriously. Suppose a new documentary is added and, by chance, is never in the first twelve titles for anyone in its first month. Describe what happens to it over the following six months under a purely collaborative system. Then propose a concrete mechanism to prevent it, and state what that mechanism costs in the short term. If your answer involves deliberately showing some users something the model is unsure about, you have arrived at the exploration and exploitation trade in a new setting.
