## Introduction

Almost everything in code has a name: variables, functions, classes, files, modules, tests. A name is the first thing a reader sees and often the only documentation they will consult, so names carry a large share of the burden of understanding. A well-chosen name can make a comment unnecessary. A poorly chosen one can mislead a reader for hours. A saying attributed to Phil Karlton claims that the hardest problems in computing are cache invalidation and naming things. The humour contains a truth: naming is hard because it forces the author to understand exactly what the thing is.

**Definition:** Good naming is the practice of choosing identifiers that reveal the purpose and meaning of what they name, in the vocabulary of the problem, consistently and without misleading the reader, so that the code can be understood without extra explanation.

<!--
IMAGE PROMPT  ->  generate as images/02_intro_naming_things_well.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Three labelled boxes on a shelf: one with a vague label reading data2, one with a clear label reading unpaid order total, and one with a misleading label reading list that actually holds a single number.

ON-IMAGE TEXT: show a short bold title "Naming Things Well" plus only these few labels, large and legible: Reveal, Consistent, Honest. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Principles of Good Names

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Principle</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Meaning</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Weak example</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Better example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Reveal intent</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The name says why the thing exists and what it is</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">d for an elapsed time</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">elapsed days</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Be precise</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Choose the most accurate term, not a vague one</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">data, info, thing, handle, process</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">order summary, validate coupon</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Avoid disinformation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Do not suggest something false</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A variable called account list that holds one account</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">account</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Make distinctions meaningful</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Different names for different things, and with a real difference</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">customer info versus customer data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">customer profile and customer payment details</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Be pronounceable and searchable</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Names that can be spoken and found</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Single letters, strange abbreviations</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The full word, such as delivery address</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use the domain language</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Words the experts use</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Technical or invented terms</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The term the business uses, such as booking or invoice</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Match scope to length</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Short names for tiny scopes, descriptive for wide scopes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A one-letter name used across a whole module</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A short loop counter inside a three-line loop is acceptable</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Avoid encodings</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Do not embed type or prefixes in the name</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Hungarian-style prefixes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Let the type system say it</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Be consistent</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One word per concept</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">fetch, get, retrieve, and load all used for reading</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Choose one and use it everywhere</td>
    </tr>
  </tbody>
</table>

## Naming Different Kinds of Things

- **Variables and fields** are **nouns** or noun phrases describing the value they hold: total price, selected dish.
- **Booleans** read as **questions** or statements that are true or false: is paid, has coupon, can cancel. Avoid negatives that make conditions confusing, such as is not available, which becomes awkward when negated again.
- **Functions and methods** are **verbs** or verb phrases describing what they do: calculate total, send receipt. A function that answers a question may be named as one: is valid.
- **Classes and types** are **nouns** naming a concept: Order, Payment Method. Avoid vague words like Manager, Processor, or Helper, which often hide a poorly defined responsibility.
- **Interfaces** describe a capability or role: Payable, Notifier.
- **Constants** name the meaning of a value: maximum items per order.
- **Tests** describe the behaviour being checked: rejects an order with no items.
- **Files and modules** are named for their content and purpose.

## Conventions

Languages and teams follow conventions about the **form** of names, so that readers can recognise kinds of names at a glance.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Style</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Appearance</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical use</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">camelCase</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">First word lower case, later words capitalised</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Variables and functions in many languages</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">PascalCase</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Every word capitalised</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Classes and types</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">snake_case</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lower case words joined by underscores</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Variables and functions in several languages</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">UPPER_SNAKE_CASE</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Capitals joined by underscores</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Constants</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">kebab-case</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lower case words joined by hyphens</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">File names and web addresses</td>
    </tr>
  </tbody>
</table>

The particular convention matters less than following the one the team and language have chosen, consistently.

## Common Naming Mistakes

- **Meaningless names:** a, tmp, foo, data1, which force the reader to trace the code to learn what they mean.
- **Noise words:** adding words that add no meaning, such as the, my, or Object.
- **Over-abbreviation:** names such as cust_acct_bal that save typing at the reader expense. Standard abbreviations that everyone knows are fine.
- **Names that lie:** a function named check that also changes data, or a name that no longer matches what it does after the code changed.
- **Too long:** names so long they obscure the logic. The aim is a name that is as long as necessary and no longer.
- **Jokes and cleverness:** names that only the author understands.
- **Mixed vocabulary:** several words for one idea, or one word for several ideas.

## Renaming Is Cheap

Modern editors can rename a thing and every use of it safely and instantly. There is little excuse for keeping a poor name once a better one is found. A name should be changed as understanding improves, since code often starts with a vague name because the author did not yet understand its role. A good habit is to rename whenever you notice a name that made you pause.

## A Test for Names

- Can someone say what the thing is or does from the name alone?
- Would you need a comment to explain it? If so, can the name carry that meaning?
- Can you find it by searching?
- Does it agree with the vocabulary used elsewhere?
- Would the name still be accurate if the implementation changed?

<!--
IMAGE PROMPT  ->  generate as images/02_naming_kinds_and_conventions.png   (16:9 explanatory diagram, place here)

A table-like poster: rows labelled Variable (noun), Boolean (question), Function (verb), Class (noun), Constant (meaning), each with a short sample name and a tick. Beside it a small panel of style samples camelCase, PascalCase, snake_case, UPPER_SNAKE_CASE, kebab-case, and a note Follow the team convention.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Improve the Names

1. A boolean is named flag.
2. A function named process handles checking a coupon, applying a discount, and printing a receipt.
3. A class is named OrderManagerHelper.

Name 1 should say what is being flagged, such as is paid or has expired. Function 2 does three things; it should be split, with each part named for its action, for example validate coupon, apply discount, and print receipt. Class 3 uses vague words; the responsibility should be identified and named precisely, for example Order Pricing, or the class should be divided.

## Conclusion

Good naming is the practice of choosing identifiers that reveal the purpose and meaning of what they name, in the vocabulary of the problem, consistently and without misleading the reader, so that the code can be understood without extra explanation. Names are cheap to improve and powerful when right.

Names label the parts. The next topic looks at how the parts themselves, the functions, should be shaped.
