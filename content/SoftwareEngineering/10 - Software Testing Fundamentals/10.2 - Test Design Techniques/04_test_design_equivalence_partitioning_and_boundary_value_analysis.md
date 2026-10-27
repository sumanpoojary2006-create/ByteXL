## Introduction

A function that accepts a whole number from one to a million has a million valid inputs and an effectively infinite number of invalid ones. Nobody can test them all, and nobody needs to. The craft of test design is choosing a small set of cases that is likely to find most of the defects. Two techniques, equivalence partitioning and boundary value analysis, do this for the common situation of inputs with ranges and rules. They are among the most useful ideas in testing, and they work with no knowledge of the code.

**Definition:** Equivalence partitioning divides the possible inputs into groups that the software should treat in the same way and tests one representative of each group, while boundary value analysis adds tests at the edges of those groups, where defects are most likely to occur.

<!--
IMAGE PROMPT  ->  generate as images/04_intro_test_design_equivalence_partitioning_and_boundary_value_analysis.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A number line from 0 to 15 divided into three coloured zones: Invalid (below 1), Valid (1 to 10), Invalid (above 10), with one dot in the middle of each zone and extra marked dots at the edges 0, 1, 2, 9, 10, 11.

ON-IMAGE TEXT: show a short bold title "Equivalence Partitioning and Boundary Value Analysis" plus only these few labels, large and legible: Partitions, Edges, Few tests. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Equivalence Partitioning

The idea is that inputs fall into **classes** within which the software behaves alike. If one value in a class works, the others probably do too, and if one fails, the others probably fail. So a test with a single representative of each class gives much of the benefit of testing all of them.

### Steps

1. Identify the **inputs** and the rules that govern them.
2. Divide each input into **valid classes** (accepted) and **invalid classes** (rejected).
3. Choose **one value from each class** as a test case.
4. State the **expected result** for each.

### Example: Quantity of a Dish in an Order

The rule: a customer may order from 1 to 10 portions of a dish.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Class</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Range</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Representative value</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Expected result</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Invalid: too low</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Below 1 (zero and negatives)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">0</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rejected with a message</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Valid</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1 to 10</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">5</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Accepted</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Invalid: too high</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Above 10</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">11 (or 50)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rejected with a message</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Invalid: wrong kind of input</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not a whole number, such as text, a decimal, or empty</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">"abc", 2.5, empty</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rejected with a message</td>
    </tr>
  </tbody>
</table>

Four tests cover the main behaviours instead of testing thousands of numbers.

### Partitioning Other Kinds of Input

Partitions are not only numeric ranges.

- **Sets of values:** payment method is card, wallet, or cash: each is a class, and a value outside the set is an invalid class.
- **Text:** empty, normal length, too long, containing special characters, containing only spaces.
- **Dates:** past, today, future, invalid dates, the end of a month or year.
- **States of data:** the list is empty, has one item, has many items.
- **Outputs:** classes of result the software can produce, such as no discount, standard discount, and maximum discount.

## Boundary Value Analysis

Experience shows that defects cluster at **boundaries**: the points where behaviour changes. Programmers often make off-by-one mistakes, such as using "less than" where "less than or equal" was meant. Boundary value analysis, a technique described by Glenford Myers in *The Art of Software Testing* (1979), tests at and next to every boundary.

For the range 1 to 10:

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Boundary</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Values to test</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Expected result</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lower boundary</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">0 (just below), 1 (on the boundary), 2 (just above)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rejected, accepted, accepted</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Upper boundary</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">9 (just below), 10 (on the boundary), 11 (just above)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Accepted, accepted, rejected</td>
    </tr>
  </tbody>
</table>

The common variants are **two-value** boundary testing (the boundary and the nearest value on the other side) and **three-value** testing (just below, on, and just above), which is more thorough.

### Why It Works

Take the rule "orders of ten or more items receive a discount." A boundary test with nine, ten, and eleven items checks exactly the condition a careless programmer might get wrong. A test with an input of 500 would pass even if the code said "greater than ten" instead of "ten or more." The boundary test would reveal the difference.

## Combining the Techniques

Equivalence partitioning gives the **classes**; boundary value analysis adds the **edges** of ordered classes. Together they yield a compact, high-value set.

For the quantity rule, a combined set might be: empty, text, 0, 1, 2, 5, 9, 10, 11, and a very large number. That is ten tests, each with a reason.

## Several Inputs

Real functions take several inputs, and the number of combinations grows quickly.

- **Test each input's classes in turn** while holding the others at normal, valid values. This isolates which input causes a failure.
- Test **selected combinations** where inputs interact, such as a member status together with quantity.
- For many inputs, **pairwise (combinatorial) testing** chooses a small set of cases so that every pair of values from different inputs appears together at least once. Research suggests that most defects involve the interaction of only a few inputs, so this reduces tests greatly while retaining effectiveness. Tools generate the sets.

## Error Guessing

Systematic techniques are complemented by **error guessing**, using experience of where defects tend to hide: empty or missing inputs, very large values, special characters, duplicate submissions, time zones and leap years, concurrent access, and the things that have gone wrong in similar software before. Keeping a checklist of past failures improves it.

## Limits

- The techniques assume that the **specification states the rules** clearly. Vague requirements make partitions hard to find, which is itself a useful finding.
- Classes may be wrong if the software contains **hidden special cases**, such as a particular value treated differently.
- They address **single inputs and rules**, and need to be supplemented by other techniques for complex logic and sequences, which the next topic covers.

<!--
IMAGE PROMPT  ->  generate as images/02_partitions_and_boundaries_quantity.png   (16:9 explanatory diagram, place here)

A number line for the quantity rule 1 to 10 with three zones (too low, valid, too high), a representative dot in each, and boundary markers at 0, 1, 2 and 9, 10, 11. A table below lists each test value with expected Accepted or Rejected.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Design the Tests

A booking form accepts a guest count from 2 to 8 inclusive.

1. List the equivalence classes.
2. List the boundary values to test.

The classes are: below 2 (invalid), 2 to 8 (valid), above 8 (invalid), and non-numeric or empty input (invalid). Boundary values are 1, 2, 3 and 7, 8, 9. A typical complete set adds a representative from the middle, such as 5, and the invalid kinds of input. Expected results: 1 rejected, 2 to 8 accepted, 9 rejected.

## Conclusion

Equivalence partitioning divides the possible inputs into groups that the software should treat in the same way and tests one representative of each group, while boundary value analysis adds tests at the edges of those groups, where defects are most likely to occur. They produce a small, justified set of test cases from the rules of the specification.

Some behaviour depends on combinations of conditions or on a sequence of events. The next topic describes techniques for those: decision tables and state-based testing.
