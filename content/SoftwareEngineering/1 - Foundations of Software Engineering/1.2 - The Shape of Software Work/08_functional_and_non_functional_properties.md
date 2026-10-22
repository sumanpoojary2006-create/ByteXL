## Introduction

After the lunch-rush failure, Meera, the product owner, came to the retrospective with a one-line complaint written on a card: "The app should be fast."

Ananya read it twice. Fast compared to what? On which screen? With how many students? She could make the rating screen load in two seconds and Meera might still call that slow, or she could spend a week reaching half a second when two seconds would have been fine. A requirement that cannot be tested cannot be met, because nobody will agree when it has been.

Vikram used the moment to show the team how to write requirements that separate **what the system does** from **how well it does it**, and to make the second kind measurable.

**Definition:** A functional property describes what a system does, its features and behaviours, while a non-functional property describes how well it does them, such as how fast, how secure, how available, or how easy to use, and good requirements state both in a form that can be verified.

<!--
IMAGE PROMPT  ->  generate as images/08_intro_functional_and_non_functional_properties.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Use the named person, setting, and engineering problem from the Introduction.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Meera holds a card reading The app should be fast while Ananya holds a stopwatch and a crowd counter, and Vikram draws a split board with What it does on the left and How well on the right.

ON-IMAGE TEXT: show a short bold title "Functional and Non-Functional Properties" plus only these few labels, large and legible: What, How well, Measure. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Functional Requirements: What the System Does

Functional requirements describe features and behaviours: inputs, outputs, and business rules. They are phrased as things the system can do.

- A student can view the menu for any day in the current week.
- A student can rate a meal from 1 to 5 once after it is served.
- The mess manager can download a weekly report of average ratings per dish.

If a functional requirement is not met, a user can say, "It does not do X."

## Non-Functional Requirements: How Well It Does It

Non-functional requirements describe qualities and constraints. If one is not met, the user says, "It does X, but badly." They are also called **quality attributes**, and they often shape the architecture of a system more than any single feature does.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Category</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Vague version</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Measurable version</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Performance</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The app should be fast</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">95% of menu requests complete within 300 ms with 2,000 simultaneous users</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Availability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The app should always work</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Available 99.9% of the time during meal hours, measured monthly</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Security</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The app should be secure</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Passwords stored using a salted hash, accounts locked for 15 minutes after 5 failed logins</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Usability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The app should be easy to use</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A first-time user can place an order in under 60 seconds without help, in testing with 10 users</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Scalability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">It should handle growth</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The system supports 20,000 daily users without code changes, only added servers</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Maintainability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The code should be clean</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A new developer can build and run the tests locally within 30 minutes of cloning the repository</td>
    </tr>
  </tbody>
</table>

The measurable column has numbers, conditions, and a way to check. Those three things turn an opinion into a requirement.

<!--
IMAGE PROMPT  ->  generate as images/02_functional_vs_non_functional.png   (16:9 explanatory diagram, place here)

A split illustration: on the left a green checklist of features labelled What the system does; on the right a dial gauge, a shield, and a clock labelled How well it does it. A thin bridge connects them labelled Measurable.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Same Function, Different Quality

Here are two versions of the same function. Both return the correct average rating for a meal, so they satisfy the same functional requirement.

```python
# Version A: loads every rating into memory and averages in Python
def average_rating_a(meal_id, db):
    rows = db.query("SELECT stars FROM ratings WHERE meal_id = ?", meal_id)
    stars = [row.stars for row in rows]
    return sum(stars) / len(stars) if stars else None

# Version B: lets the database do the work
def average_rating_b(meal_id, db):
    row = db.query_one("SELECT AVG(stars) AS avg FROM ratings WHERE meal_id = ?", meal_id)
    return row.avg
```

With 20 ratings, nobody can tell them apart. With 200,000 ratings, version A moves 200,000 rows across the network and builds a list in memory, while version B sends back a single number. The function is identical in **what** it does and very different in **how well** it does it. Only a non-functional requirement, such as "the report must load in under one second with 200,000 ratings," would expose the gap before users do.

## Trade-offs and Conflicts

Non-functional requirements often conflict, and the team must decide which wins. Demanding very high security (long passwords, frequent re-login) can harm usability. Demanding the fastest possible response may increase cost. Writing each non-functional requirement with a number lets stakeholders argue about the number instead of arguing about adjectives.

## Your Turn: Classify and Sharpen

1. "Students can cancel an order up to 10 minutes before pickup." Functional or non-functional?
2. "Report generation must be quick." Rewrite it as a measurable requirement.
3. "Order data must survive a server crash." Which attribute does this concern?

Statement 1 is functional: it describes a behaviour and a rule. For statement 2, a good rewrite is: "The weekly ratings report is generated within 2 seconds for up to 100,000 ratings, measured on the production server." For statement 3, the attribute is dependability, specifically reliability and durability of data. A sound requirement might say: "No confirmed order is lost if a single server fails."

## Conclusion

A functional property describes what a system does, its features and behaviours, while a non-functional property describes how well it does them, such as how fast, how secure, how available, or how easy to use, and good requirements state both in a form that can be verified. Vague adjectives such as "fast" or "secure" are not requirements until they carry a number and a method of checking.

That finishes the chapter on how software work is shaped. The final chapter turns to the engineer's own skills and equipment, starting with the habits of mind that make an engineer different from a person who simply writes code.
