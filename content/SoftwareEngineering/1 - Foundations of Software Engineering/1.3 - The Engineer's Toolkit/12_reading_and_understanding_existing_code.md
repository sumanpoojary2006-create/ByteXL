## Introduction

The payment failures traced back to a file called `discount.py`. It had been written eighteen months earlier by a developer who had since left the company. It had no comments, and the only documentation was a commit message that said "fix stuff".

Ananya felt her stomach drop. She had spent her whole education writing code from a blank file, with an assignment sheet telling her exactly what to build. Now she had to understand something that already existed, with its mistakes, history, and unstated assumptions.

Vikram reassured her: "Most of this job is reading. Studies of developers consistently find that they spend far more time understanding existing code than writing new code." He then taught her a method, so that reading code became a skill and not a guessing game.

**Definition:** Reading existing code is the disciplined process of building an accurate mental model of what a program does and why, by running it, tracing it, searching it, and reading its tests and history, before changing anything.

<!--
IMAGE PROMPT  ->  generate as images/12_intro_reading_and_understanding_existing_code.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Use the named person, setting, and engineering problem from the Introduction.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Ananya sits in front of a large unfamiliar code file with a magnifying glass and sticky notes, while a glowing trail of history commits stretches behind it and Vikram points at a map-like diagram.

ON-IMAGE TEXT: show a short bold title "Reading and Understanding Existing Code" plus only these few labels, large and legible: Read, Trace, Understand. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## A Method for Reading Unfamiliar Code

1. **Run it first.** Seeing the behaviour is faster than imagining it. Start the program or the tests and watch what happens.
2. **Find the entry point.** Where does execution begin? For a web app, it might be the route that handles a request. Start from there instead of reading files alphabetically.
3. **Read the tests.** Good tests are examples of intended behaviour. If there are none, that fact is itself information.
4. **Trace one concrete example.** Pick specific input values and follow them line by line, writing down the value of each variable. Concrete traces beat abstract reading.
5. **Search, do not scroll.** Use the editor's search or `grep` to find where a function is defined and where it is used.
6. **Use the history.** `git log` and `git blame` show who changed a line and the message that explains why.
7. **Take notes and draw.** A small diagram of what calls what is worth more than ten minutes of staring.
8. **Do not change anything until you understand it.** Premature fixes are how new bugs are born.

<!--
IMAGE PROMPT  ->  generate as images/02_reading_code_method.png   (16:9 explanatory diagram, place here)

A circular flow of eight small icons: Run, Entry point, Tests, Trace, Search, History, Notes, Then change. The final step Then change is drawn in green and is clearly last.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Tracing a Real Example

Here is the heart of `discount.py`:

```python
def final_price(price, quantity, is_member):
    total = price * quantity
    if quantity >= 10:
        total = total * 0.90
    if is_member:
        total = total - 20
    return max(total, 0)
```

Trace the call `final_price(50, 12, True)` by writing down each variable.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Step</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Line</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Value</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">total = price * quantity</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">50 * 12 = 600</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">quantity &gt;= 10 is true</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">total = 600 * 0.90 = 540.0</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">3</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">is_member is true</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">total = 540.0 - 20 = 520.0</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">4</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">return max(total, 0)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">max(520.0, 0) = 520.0</td>
    </tr>
  </tbody>
</table>

The result is `520.0`. Now trace `final_price(5, 2, True)`:

- `total = 5 * 2 = 10`
- `quantity >= 10` is false, so no bulk discount
- member discount: `10 - 20 = -10`
- `max(-10, 0)` returns `0`

A member buying 10 rupees of food pays zero. Is that intended? The code cannot tell us, but the trace tells us exactly what it does. This is where the history becomes valuable: running `git log` on the file shows a message "members get 20 off, never negative," which explains the `max` call and tells Ananya the behaviour is deliberate.

## Questions to Ask While Reading

- What are the **inputs** and **outputs** of this piece of code?
- What does it assume to be true that is not checked?
- What happens at the **edges**: zero, negative numbers, empty values, very large values?
- Does the order of operations matter? Here, applying the percentage discount before the flat 20 gives a different answer from the reverse.
- What else calls this, so what could break if I change it?

## Leave It Better Than You Found It

After understanding code, you often add something small that helps the next reader: a clarifying name, a short comment that explains **why** (not what), or a test that records the behaviour you just discovered. Ananya added a test for the zero-floor case so that the next person would not need to repeat her investigation.

## Your Turn: Trace It

Using the `final_price` function, work out the result of each call by hand.

1. `final_price(100, 10, False)`
2. `final_price(30, 3, True)`
3. `final_price(40, 10, True)`

Call 1: total is 1000, the bulk discount makes it 900.0, there is no member discount, so the result is `900.0`. Call 2: total is 90, there is no bulk discount because quantity is below 10, the member discount gives 70, so the result is `70`. Call 3: total is 400, the bulk discount makes it 360.0, the member discount makes it 340.0, so the result is `340.0`.

## Conclusion

Reading existing code is the disciplined process of building an accurate mental model of what a program does and why, by running it, tracing it, searching it, and reading its tests and history, before changing anything. It is a core professional skill, not a sign of weakness.

With this lesson, Unit 1 is complete. Ananya now knows what software engineering is, where its practices came from, how projects fail, what kinds of systems exist, how the work is organised, what makes software good, and how to use the tools and habits of a working engineer. Unit 2 takes the next step: given all that work to do, how should a team organise it over time? That is the question that process models and agile methods answer.
