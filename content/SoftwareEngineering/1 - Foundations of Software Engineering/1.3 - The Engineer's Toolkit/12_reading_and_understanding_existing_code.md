## Introduction

Education tends to emphasise writing new programs from a blank file. Professional work looks different: most engineers spend far more time reading code that already exists, written by people who may have left, than writing code from scratch. The ability to understand unfamiliar software quickly and accurately is one of the most valuable practical skills.

This topic presents a disciplined method for building an accurate mental model of existing software before changing it, and explains why that discipline prevents new defects.

**Definition:** Reading existing code is the disciplined process of building an accurate mental model of what a program does and why, by running it, tracing it, searching it, and reading its tests and history, before changing anything.

<!--
IMAGE PROMPT  ->  generate as images/12_intro_reading_and_understanding_existing_code.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A magnifying glass over a large unfamiliar code file, with a trail of history commits stretching behind it and a small map-like diagram of connected parts.

ON-IMAGE TEXT: show a short bold title "Reading and Understanding Existing Code" plus only these few labels, large and legible: Read, Trace, Understand. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## A Method for Reading Unfamiliar Code

1. **Run it first.** Seeing behaviour is faster than imagining it. Start the program or its tests and watch what happens.
2. **Find the entry point.** Where does execution begin? Start from there instead of reading files in alphabetical order.
3. **Read the tests.** Good tests are examples of intended behaviour. The absence of tests is itself information about risk.
4. **Trace one concrete example.** Choose specific input values and follow them step by step, writing down what each value becomes. Concrete traces beat abstract reading.
5. **Search, do not scroll.** Use search tools to find where something is defined and everywhere it is used.
6. **Use the history.** Version control records who changed each part and the reason given, which often explains puzzling choices.
7. **Take notes and draw.** A small diagram of what depends on what is worth more than minutes of staring.
8. **Do not change anything until you understand it.** Premature fixes are how new defects are born.

## Tracing a Concrete Example

Suppose a pricing rule in an old module works like this: when the quantity is ten or more, the total receives a ten percent discount; then, if the buyer is a member, a flat amount is taken off; finally, the price can never fall below zero.

Trace a purchase of 12 items at 50 each by a member, and assuming the flat member amount is 20. The starting total is 600. The bulk rule applies, giving 540. The member amount reduces it to 520. The price is above zero, so the result is 520.

Now trace a member buying 2 items at 5 each. The total is 10, the bulk rule does not apply, and the member amount takes it to minus 10. The final rule lifts it to zero, so the member pays nothing. Is that intended? The tracing shows what the rule does, but not whether it is right. The history of the module may contain a note that members receive a flat reduction that is never negative, which tells you the behaviour is deliberate. Checking the history before "fixing" an apparent bug avoids breaking something intentional.

## Questions to Ask While Reading

- What are the **inputs** and **outputs** of this piece of the system?
- What does it assume to be true without checking?
- What happens at the **edges**: zero, negative values, empty values, very large values?
- Does the **order** of steps matter? In the pricing example, applying the percentage before the flat reduction gives a different answer from the reverse.
- What else depends on this, so what could break if it changes?

## Leave It Better Than You Found It

Once you understand code, you can leave a small improvement that helps the next reader: a clearer name, a note that explains **why** a choice was made, or a test that records the behaviour you discovered. Recording what you learned means the next person does not repeat your investigation.

## Your Turn: Trace It

Using the pricing rule described above (ten percent off for quantities of ten or more, then a flat 20 off for members, never below zero), work out the result for each purchase.

1. 10 items at 100 each, not a member.
2. 3 items at 30 each, a member.
3. 10 items at 40 each, a member.

Purchase 1: the total is 1000, the bulk rule makes it 900, there is no member reduction, so the result is 900. Purchase 2: the total is 90, the bulk rule does not apply because the quantity is below ten, the member reduction gives 70, so the result is 70. Purchase 3: the total is 400, the bulk rule makes it 360, the member reduction makes it 340, so the result is 340.

## Conclusion

Reading existing code is the disciplined process of building an accurate mental model of what a program does and why, by running it, tracing it, searching it, and reading its tests and history, before changing anything. It is a core professional skill, not a sign of weakness.

This completes Unit 1. You now have a picture of what software engineering is, where its practices came from, how projects fail, what kinds of systems exist, how the work is organised, what makes software good, and the habits and tools of a working engineer. Unit 2 turns to how a team organises all this work over time, through process models and agile methods.
