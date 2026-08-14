## Introduction

The examination cell at a university in Pune runs on a set of rules that a clerk applies by hand, and Farida has been asked to encode them so a system can apply them instead.

She starts confidently. "A student with less than 75 percent attendance is barred from the examination" becomes a proposition, and she writes it down. Then she looks at the enrolment list. There are 4,200 students.

The rule is one sentence and it applies to every one of them. In propositional logic, "Ashwin is barred" and "Meera is barred" are entirely unrelated statements that happen to look similar; the language has no way to record that they are two instances of the same rule. Farida would need 4,200 propositions about attendance, 4,200 more about barring, and 4,200 separate implications linking them. Next year, when the intake changes, she would need to write them all again.

Something has gone badly wrong, and it is not Farida's method. It is the language. Propositional logic treats "Ashwin has low attendance" as one indivisible lump of truth, with no visible parts. It cannot see that the statement is about a *thing* called Ashwin, having a *property* called low attendance, and it therefore cannot say anything about all such things at once.

Fixing this requires a language that can talk about objects, the properties they have, the relations between them, and how many of them a statement covers. That language is **first-order predicate logic**.

**Definition:** `First-order predicate logic` extends propositional logic by breaking statements into `predicates` applied to `objects`, and by adding `quantifiers` that allow a single statement to assert something about all objects or about at least one object in a domain.

![Opening scene: The examination cell at a university in Pune runs on a set of rules that a clerk applies by hand, and Farida has been asked to encode them so a system can apply them instead.](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_section_introduction.png)

## Objects, Predicates, and Relations

Three new pieces of vocabulary carry almost all of the power.

**Objects** are the things being talked about, named by constants. `Ashwin`, `Meera`, `CS201`, `Pune`. In first-order logic, objects are whatever the domain contains: people, courses, rooms, numbers, events.

**Predicates** are properties that an object may or may not have. `Student(Ashwin)` says Ashwin is a student, and it is true or false. Written this way, the statement has visible parts: a predicate applied to an object. Propositional logic could only see "the whole thing".

**Relations** are predicates taking more than one object, which is where the language becomes genuinely expressive. `Enrolled(Ashwin, CS201)` says Ashwin is enrolled in CS201. `Teaches(ProfRao, CS201)`. `Attendance(Ashwin, 68)`. The number of objects a predicate takes is called its arity, and relations of arity two are by far the most common.

**Functions** complete the set. A function maps objects to objects rather than to truth values, so `Instructor(CS201)` refers to a person rather than asserting anything. This lets you write `Teaches(Instructor(CS201), CS201)` without knowing who that instructor is.

Notice what has been gained already, before any quantifier appears. `Enrolled(Ashwin, CS201)` and `Enrolled(Meera, CS201)` now visibly share structure. A system can look at them and see that they are the same relation applied to different students, which propositional logic could never do.

![Visual explanation of objects, predicates, and relations](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_section_objects_predicates_and_relations.png)

## Variables and Quantifiers

The pieces above still describe named individuals. The step that solves Farida's problem is the ability to say something about objects without naming them.

A **variable**, conventionally written x or y, stands for an unspecified object. `Barred(x)` on its own asserts nothing, because nobody has said which x. A `quantifier` fixes that by saying how many objects the statement is claimed for.

**The universal quantifier**, written for all x, claims the statement holds for every object in the domain. Farida's rule becomes:

> for all x: Student(x) and Attendance(x) < 75 implies Barred(x)

One statement, 4,200 students, and it stays correct when the intake changes. This is the whole reason the language exists.

**The existential quantifier**, written there exists x, claims the statement holds for at least one object.

> there exists x: Student(x) and Enrolled(x, CS201) and Barred(x)

That says at least one student enrolled in CS201 is barred, without naming them or claiming how many.

There is a pairing between the quantifiers and the operators that is worth memorising, because it explains a mistake beginners make constantly.

- **Universal statements normally use implication.** "All students with low attendance are barred" is written as for all x: Student(x) implies Barred(x). Writing for all x: Student(x) and Barred(x) instead claims that *everything in the entire domain* is a barred student, including the courses and the rooms.
- **Existential statements normally use conjunction.** "Some student is barred" is written as there exists x: Student(x) and Barred(x). Writing there exists x: Student(x) implies Barred(x) is almost worthless, because implication is vacuously true for any object that is not a student, so a single classroom in the domain makes the statement true.

Learning that universals take implication and existentials take conjunction saves more marks in examinations, and more bugs in real knowledge bases, than any other single rule in this lesson.

![Visual explanation of fol quantifiers](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_fol_quantifiers_context_v4.png)

## Negation and the Quantifier Swap

Negating a quantified statement flips the quantifier, in a pattern that is the exact analogue of De Morgan's law from propositional logic.

- **not (for all x: P(x))** is equivalent to **there exists x: not P(x)**. If it is not true that every student passed, then some student did not pass.
- **not (there exists x: P(x))** is equivalent to **for all x: not P(x)**. If no student is barred, then every student is not barred.

The practical use is that "no student has been marked absent" and "every student has not been marked absent" are the same claim, so a system can convert between them freely to match whichever form its rules are written in.

![Visual explanation of quantifier order and negation](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_quantifier_order_and_negation_context_v4.png)

## Nested Quantifiers, Where Order Decides Everything

Statements with two quantifiers are where first-order logic becomes genuinely subtle, and where careless reading produces claims nobody intended.

Compare these two, which use identical symbols in a different order.

> for all x, there exists y: Student(x) implies Advises(y, x)

> there exists y, for all x: Student(x) implies Advises(y, x)

The first says every student has an advisor, and different students may have different advisors. The second says there is one particular person who advises every student in the university. The first is a reasonable policy. The second describes an impossible workload.

**With mixed quantifiers, order changes the meaning.** The rule is that the inner quantifier is evaluated within the scope of the outer one, so a "there exists" inside a "for all" may pick a different object for each case, while a "there exists" outside must pick one object that works for all cases.

Two quantifiers of the same type can be swapped freely, because "for all x, for all y" and "for all y, for all x" say the same thing, and likewise for two existentials. It is only the mixture that is order-sensitive.

![Visual explanation of nested quantifiers, where order decides everything](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_section_nested_quantifiers_where_order_decides_everything.png)

## Representing the University

Farida's whole examination-cell rulebook fits in a handful of statements.

| English | First-order logic |
| --- | --- |
| Ashwin is a student | Student(Ashwin) |
| Ashwin is enrolled in CS201 | Enrolled(Ashwin, CS201) |
| Every student enrolled in a course must be assigned a seat | for all x, for all c: Enrolled(x, c) implies there exists s: Seat(x, c, s) |
| No student may sit two examinations at once | not there exists x, e1, e2: Sitting(x, e1) and Sitting(x, e2) and e1 is not e2 and SameTime(e1, e2) |
| Some course has no students enrolled | there exists c: Course(c) and not there exists x: Enrolled(x, c) |
| Every course has exactly one instructor | for all c: Course(c) implies there exists t: Teaches(t, c) and for all u: Teaches(u, c) implies u is t |

The last row shows how "exactly one" is expressed, since no quantifier means it directly. You assert that at least one exists, and then that anything with the same property must be identical to it. That pattern, existence plus uniqueness, appears constantly in real knowledge bases.

Read the whole table and notice what has happened to Farida's problem. Six statements now cover every student, every course, and every examination, and none of them mentions a specific person except where a specific person is genuinely meant.

![Visual explanation of representing the university](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_section_representing_the_university.png)

## What First-Order Logic Costs

The expressive gain is not free, and being honest about the price is what distinguishes understanding this material from memorising it.

1. **Checking is no longer exhaustive.** Propositional logic could enumerate all 2 to the power n situations. A universally quantified statement over an infinite domain has infinitely many cases, so the truth-table method simply does not apply.

2. **Inference becomes semi-decidable.** For first-order logic there are procedures that will eventually confirm any statement that genuinely follows from the knowledge base. There is no procedure guaranteed to tell you, in finite time, that a statement does *not* follow. A system can be left running forever on a question whose answer is no.

3. **It still cannot quantify over predicates.** The word "first-order" means quantifiers range over objects only. "Every property that holds of Ashwin also holds of Meera" quantifies over properties, not objects, and needs a higher-order logic, which is more expressive and considerably worse behaved.

That second point is the deep one, and it is a genuine result rather than a limitation of current technology. It is also why practical systems almost never use full first-order logic, preferring restricted fragments where inference is guaranteed to terminate.

![Visual explanation of what first-order logic costs](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_section_what_first_order_logic_costs.png)

## First-Order Logic at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Element</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it does</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Constant</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Names one specific object</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Ashwin, CS201</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Predicate</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A property, true or false of an object</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Student(Ashwin)</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Relation</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A predicate over two or more objects</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Enrolled(Ashwin, CS201)</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Function</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Maps objects to objects, not to truth values</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Instructor(CS201)</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Universal quantifier</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Claims the statement for every object; pairs with implication</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">for all x: Student(x) implies Enrolled(x, someCourse)</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Existential quantifier</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Claims the statement for at least one object; pairs with conjunction</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">there exists x: Student(x) and Barred(x)</td>
    </tr>
  </tbody>
</table>

![Visual explanation of first-order logic at a glance](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_section_first_order_logic_at_a_glance.png)

## Your Turn

Represent your own family in first-order logic, then discover where it breaks.

Start with the relations `Parent(x, y)`, `Male(x)`, and `Female(x)`, and nothing else. Define these in terms of them: mother, sibling, grandparent, aunt, and cousin. Sibling is the interesting one, because a first attempt usually says two people are siblings if they share a parent, and that makes everybody their own sibling. Work out what has to be added.

Then translate these three sentences and pay close attention to the difference between the second and the third.

1. Everyone has a mother.
2. There is someone who is everyone's ancestor.
3. Everyone has an ancestor.

Sentences 2 and 3 use the same predicates and differ only in quantifier order, and one of them is a far stronger claim than the other. Say which, and describe a family in which the weaker one is true and the stronger one is false.

Finally, attempt "Ashwin and Meera have exactly two children in common" and notice how much work "exactly two" requires. If you find yourself asserting two children, then asserting they are different, then asserting that any third is equal to one of the first two, you have arrived at the standard pattern, and you will understand why real systems usually add counting to the language rather than expressing it this way.
