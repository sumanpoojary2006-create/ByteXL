## Introduction

The usual order of work is to write code and then test it. Test-driven development reverses this: write a small failing test first, then write just enough code to make it pass, then clean up. It sounds like a minor change of sequence, yet practitioners report that it changes how they think about design, how confident they are in their code, and how much of it is tested. Kent Beck formalised it in the Extreme Programming community in the late 1990s and described it in *Test-Driven Development: By Example* (2002). It is one of the most discussed practices in software engineering, with enthusiastic advocates and thoughtful critics.

**Definition:** Test-driven development (TDD) is a way of working in which the developer repeatedly writes a small automated test that fails, writes the simplest code that makes it pass, and then improves the design while keeping all tests green, so that tests drive the development of the code in small, verified steps.

<!--
IMAGE PROMPT  ->  generate as images/08_intro_test_driven_development.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A circular three-step loop with a red node Red (write a failing test), a green node Green (make it pass), and a blue node Refactor (improve the code), arrows between them, and a small growing stack of passing tests on the side.

ON-IMAGE TEXT: show a short bold title "Test-Driven Development" plus only these few labels, large and legible: Red, Green, Refactor. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Cycle: Red, Green, Refactor

1. **Red.** Write a small test for a behaviour that does not yet exist. Run it and **watch it fail.** The failure proves that the test can fail, and that it checks something real.
2. **Green.** Write the **simplest code** that makes the test pass, even if crude or hard-coded. Run all the tests; they should be green.
3. **Refactor.** With the safety net of passing tests, **improve the design**: remove duplication, clarify names, restructure. Run the tests again after each small change.
4. **Repeat** with the next small behaviour.

Each cycle is short, a few minutes, so the code is never far from a working, tested state.

## An Example in Words

Suppose the task is a function that calculates the total of an order with a bulk discount.

- **Test 1 (red):** an order with no items has a total of zero. The test fails because the function does not exist. Write the minimum so that it passes, perhaps just returning zero. Green.
- **Test 2 (red):** an order with one item priced at 100 has a total of 100. Fails. Make it pass by adding up item prices. Green.
- **Test 3 (red):** an order with two items totals their sum. This probably passes already; the test confirms the behaviour.
- **Test 4 (red):** an order of ten or more items receives ten percent off. Fails. Add the discount rule. Green. Then refactor, perhaps naming the threshold and extracting the discount calculation.
- **Test 5 (red):** nine items receive no discount. This is a boundary test, and drives attention to the edge.

At each stage the behaviour grew by one small, tested step.

## The Three Laws

Robert C. Martin summarised the discipline as three rules.

1. Do not write production code unless it is to make a failing test pass.
2. Do not write more of a test than is sufficient to fail (and failing to compile counts as failing).
3. Do not write more production code than is sufficient to pass the one failing test.

These are meant as a strict training exercise that builds the habit, and practitioners often relax them in everyday work.

## Techniques Within TDD

- **Test list:** before starting, jot down the behaviours to be tested and the cases to remember, then work through them one at a time.
- **Fake it till you make it:** make a test pass first with a constant, then generalise when more tests demand it.
- **Triangulation:** add a second example to force the general solution to emerge from the specific ones.
- **Obvious implementation:** when the right code is clear, write it directly.
- **Baby steps:** if stuck, take smaller steps.

## Benefits

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Benefit</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Design feedback</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Writing the test first forces the developer to think about how the code will be used, producing simpler, more modular interfaces. Hard-to-write tests reveal poor design early</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Confidence and safety net</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A comprehensive suite grows with the code, enabling refactoring and change</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Focus and small steps</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One failing test at a time keeps attention on a single small goal</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">High coverage as a by-product</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Every behaviour has a test because it was written to justify the code</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Specification by example</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The tests document the intended behaviour</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fewer defects found later</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Problems are caught within minutes of being introduced</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Less debugging</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">When a test fails, the cause is in the last few lines written</td>
    </tr>
  </tbody>
</table>

Some empirical studies, including work at Microsoft and IBM by Nagappan and colleagues in 2008, reported markedly lower defect density in TDD projects, at the price of longer initial development time. Other studies found weaker or mixed effects. The evidence suggests benefit, but it depends on skill and context.

## Costs and Criticisms

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Concern</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Learning curve</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">It takes weeks of practice to feel natural, and early attempts can feel slow</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Slower at first</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">More effort is spent up front, repaid later in fewer defects and easier change</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Brittle tests</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">If tests are tied to implementation details, refactoring breaks them; tests should check behaviour</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Poor fit for some work</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Exploratory code, user interface layout, and research prototypes may not suit test-first</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Can encourage design from the bottom up only</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Without larger design thinking, small steps may wander; architecture still needs attention</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Misuse as a goal in itself</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Following the ritual without thinking, or demanding it dogmatically, produces poor results</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Needs testable design</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Legacy code with hidden dependencies is hard to drive with TDD without preparation</td>
    </tr>
  </tbody>
</table>

In 2014, David Heinemeier Hansson, creator of a well-known web framework, provoked a public debate by declaring that TDD was dead, arguing that it led to design damage for the sake of tests. Kent Beck and Martin Fowler replied in discussion that it remained useful when applied with judgement. The sensible reading is that TDD is a valuable tool for much logic-heavy code, not a religion.

## TDD and Related Practices

- **Unit tests first, then more:** TDD concerns mostly unit-level tests, written by developers. The integration and acceptance tests of the following topics complement it.
- **Acceptance test-driven development (ATDD)** applies the same idea at feature level: define the acceptance tests with stakeholders first, then build to pass them. Behaviour-driven development, the next topic, is a closely related form.
- **TDD and refactoring** are partners: the green tests make refactoring safe, and refactoring keeps the design healthy.
- **TDD and continuous integration:** the growing suite runs on every change.

## Getting Started

1. **Start with logic-rich code,** such as calculations and rules, where TDD is most natural.
2. **Practise on small exercises,** called code katas, to build the rhythm.
3. **Keep steps small** and tests fast.
4. **Test behaviour, not implementation.**
5. **Refactor every cycle,** not just now and then.
6. **Pair with an experienced practitioner,** if possible.
7. **Be pragmatic.** Use TDD where it helps, and write tests after for work where test-first is awkward.

<!--
IMAGE PROMPT  ->  generate as images/02_tdd_cycle_with_example_steps.png   (16:9 explanatory diagram, place here)

A red-green-refactor cycle diagram with three example turns beside it: Test 1 empty order totals zero, Test 2 one item totals its price, Test 4 ten items get ten percent off. A growing green bar of passing tests below shows increasing confidence, and a clock showing each cycle lasts minutes.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Which Step?

1. A developer writes a test for a new rule and runs it to see it fail.
2. A developer writes the simplest code that makes the failing test pass.
3. With all tests passing, a developer renames a confusing variable and removes duplicated logic.

Step 1 is red. Step 2 is green. Step 3 is refactor. Each step ends by running the tests.

## Conclusion

Test-driven development (TDD) is a way of working in which the developer repeatedly writes a small automated test that fails, writes the simplest code that makes it pass, and then improves the design while keeping all tests green, so that tests drive the development of the code in small, verified steps. It offers design feedback, a safety net, and focus, and it works best applied thoughtfully.

TDD is at heart a conversation about expected behaviour. The next topic extends that conversation to include the people who define the requirements: behaviour-driven development.
