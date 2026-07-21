## Introduction

Rohan manages the campus library's digitised catalogue, and this week two very different requests land on his desk within an hour of each other. The first is from a librarian who wants to see every book that costs less than 300 rupees, so she can plan a budget clearance shelf.

The second is from a student volunteer building a printed handout, who wants nothing but a plain list of book titles and authors, with no prices, no stock counts, and no genre codes cluttering the page.

Both requests sound like they want "a version of the catalogue," but they want completely different slices of it:

- The librarian wants fewer `rows`, all of the `columns`, but only the ones that meet her price condition.
- The volunteer wants every `row`, but only two of the `columns`. `Relational algebra` gives each of these two needs its own dedicated operation. Picking out `rows` that satisfy a condition is called **selection**, written with the Greek letter sigma, and picking out certain `columns` is called **projection**, written with the Greek letter pi. Learning to tell these two apart cleanly is the first real skill worth building here.

**Definition:** **Selection** chooses the rows of a relation that satisfy a condition, while **projection** chooses which columns appear in the result.

<!--
IMAGE PROMPT  ->  generate as images/02_intro_selection.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: DBMS course introduction image based directly on the opening scene of this lesson. Use the named person, setting, and database problem from the Introduction.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue database forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A simple visual of the Introduction: Rohan manages the campus library's digitised catalogue, and this week two very different requests land on his desk within an hour of each other. The first is from a librarian who wants to see every book that costs less than 300 rupees, so she can plan a.

ON-IMAGE TEXT: show a short bold title "Selection" plus only these few labels, large and legible: Selection, Rohan, Manages. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing DBMS reading-material image standards.
-->

![Intro visual for selection](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_intro_selection_matched_da5ec764.png)

## The Catalogue Rohan Is Working With

Everything that follows works off one small relation, a simplified slice of Rohan's Books `table`:

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">book_id</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">title</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">author</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">genre</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">price</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">201</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Silent Hills</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A. Menon</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Mystery</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">350</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">202</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Morning Light</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">R. Fernandes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Poetry</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">220</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">203</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The Long Wait</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A. Menon</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Mystery</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">410</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">204</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Coastal Roads</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">S. Iyer</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Travel</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">300</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">205</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Paper Boats</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">R. Fernandes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Poetry</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">180</td>
    </tr>
  </tbody>
</table>

Five `rows`, five `columns`. Selection and projection are really just two different ways of trimming this one small `table` down to exactly what someone asked for.

## Selection: Keeping the Rows That Match

- Selection, written sigma, picks out the `rows` of a relation that satisfy a given condition and discards the rest, while keeping every `column` untouched.
- The librarian's request, "every book under 300 rupees," is a selection on the Books relation with the condition price less than 300.
- Applying that selection produces:

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">book_id</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">title</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">author</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">genre</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">price</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">202</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Morning Light</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">R. Fernandes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Poetry</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">220</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">205</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Paper Boats</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">R. Fernandes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Poetry</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">180</td>
    </tr>
  </tbody>
</table>

- Notice what stayed the same and what changed.
- The shape of the `table` did not change at all, still five `columns`, still book_id through price.
- What changed is the `row` count: five `rows` narrowed down to two, because only two `rows` satisfy the condition.
- This is the defining habit of selection, it filters `rows` without ever touching `columns`.

Selection conditions can be as simple as a single comparison, or combined for something more specific. If Rohan instead needed "every mystery novel priced above 400," that is still a selection, just with a compound condition: genre equals Mystery and price is greater than 400.

Applied to the same Books relation, only one `row` survives:

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">book_id</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">title</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">author</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">genre</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">price</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">203</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The Long Wait</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A. Menon</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Mystery</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">410</td>
    </tr>
  </tbody>
</table>

Whether the condition is a single check or several joined together, the operation is still sigma, still working `row` by `row`, still leaving every `column` exactly as it was.

![Selection keeps matching rows while projection keeps chosen columns](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_selection_vs_projection.png)

## Projection: Keeping the Columns That Matter

- Projection, written pi, works the opposite way.
- Instead of trimming `rows`, it trims `columns`, keeping every `row` but discarding any `column` not explicitly asked for.
- The volunteer's handout, wanting only titles and authors, is a projection of the Books relation onto just those two `columns`.
- Applying it produces:

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">title</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">author</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Silent Hills</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A. Menon</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Morning Light</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">R. Fernandes</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The Long Wait</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A. Menon</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Coastal Roads</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">S. Iyer</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Paper Boats</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">R. Fernandes</td>
    </tr>
  </tbody>
</table>

All five `rows` are still present, since projection does not filter anything out based on a condition. What disappeared is the shape of the `columns`, book_id, genre, and price are simply gone from the result, because nobody asked for them. This is projection's defining habit, it filters `columns` without ever touching which `rows` survive.

There is one subtlety worth noticing. If Rohan projected the Books relation down to just the genre `column`, the raw result would list Mystery, Poetry, Mystery, Travel, Poetry, five values with a repeat. Because a relation is meant to represent a set, `relational algebra`'s projection removes duplicate `rows` from its result, leaving just Mystery, Poetry, and Travel.

Projection is not simply "delete some `columns` and keep everything else identical," it is "keep some `columns`, and keep the result as a proper set of distinct `rows`."

## Combining Selection and Projection

Real requests rarely stop at only one operation. Suppose Rohan is asked for "the titles of every mystery novel," which combines both needs at once, filter to mystery `rows`, then keep only the title `column`.

Because `relational algebra` operations always produce a relation as output, the result of the selection can be fed straight into the projection as its input. First selection narrows Books down to the two mystery `rows`, Silent Hills and The Long Wait.

Then projection strips that narrowed relation down to just the title `column`:

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">title</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Silent Hills</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The Long Wait</td>
    </tr>
  </tbody>
</table>

This chaining is exactly the "closure" idea put to work: because sigma's output is a relation and pi's input is a relation, the two snap together cleanly, one operation feeding directly into the next, with no special glue code required in between.

![A selection for mystery books feeding into a projection of only the title column](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_selection_then_projection_chain.png)

## Selection and Projection at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Aspect</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Selection (sigma)</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Projection (pi)</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Trims</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rows</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Columns</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Keeps</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">All columns of matching rows</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">All rows, restricted to chosen columns</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Driven by</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A condition (for example, price less than 300)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A list of column names</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Removes duplicates?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Yes, in the formal definition</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rohan&#x27;s example</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">&quot;Books under 300 rupees&quot;</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">&quot;Only title and author&quot;</td>
    </tr>
  </tbody>
</table>

## Your Turn: Sigma or Pi?

A new request lands on Rohan's desk: "list just the author and genre for every book priced above 250 rupees." Break this into its component operations against the Books relation, and say what the final result contains.

This needs a selection first, sigma with the condition price greater than 250, which narrows the five `rows` down to Silent Hills, The Long Wait, and Coastal Roads. Then it needs a projection, pi onto just author and genre, which strips away book_id, title, and price from those three surviving `rows`. Silent Hills and The Long Wait both reduce to the identical pair A. Menon and Mystery, and because projection keeps its result as a proper set of distinct `rows`, that repeated pair collapses into one, leaving just two `rows` in the final answer: A. Menon with Mystery, and S. Iyer with Travel.

## Conclusion

Selection and projection are the two simplest, most frequently used tools in `relational algebra`, and they solve two genuinely different problems. Selection, sigma, narrows a relation down to the `rows` that satisfy a condition. Projection, pi, narrows it down to the `columns` that were actually asked for, folding away any duplicate `rows` that survive.

Once a request needs both, the two chain together naturally, because each one hands back a proper relation the other can work on. Rohan can now answer both requests on his desk without confusion, a selection on price gives the librarian her budget shelf, and a projection onto title and author gives the volunteer a clean handout with nothing else cluttering the page.

These two operations answer questions about a single `table`. The next natural question is what happens when a request involves comparing two relations against each other rather than trimming just one, which is exactly where set operations come in.
