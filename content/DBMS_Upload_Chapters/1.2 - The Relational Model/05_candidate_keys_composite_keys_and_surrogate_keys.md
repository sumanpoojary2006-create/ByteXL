## Introduction

Aisha is designing a `table` for her college library's book collection, and she quickly notices something curious. Both the ISBN and the Accession Number in her draft `table` are unique for every single book, no two books ever share either value. Only one of them can become the actual `primary key`, but both were, technically, good enough to have been chosen.

That realisation sends her down a rabbit hole of similar questions about keys that a simple "pick one unique `column`" story never quite answered.

What about her second draft `table`, Book Loans, where no single `column` is unique on its own, a student can borrow many books, and a book can be borrowed by many students over the year, but the pairing of "this student, this book, this exact loan date" never repeats?.

And what about a completely different `table`, Feedback Forms, submitted anonymously, where absolutely nothing about a form is naturally guaranteed to be unique, not the comments, not the date, nothing at all?

These three situations turn out to be common enough that the relational model gives each one its own name:

- A `column` that could have served as the `primary key`, even though it was not the one chosen, is a **`candidate key`**.
- A key that only becomes unique once two or more `columns` are combined together is a **`composite key`**.
- An artificial, invented `column` added purely to give a `table` a reliable identity, when nothing natural exists, is a **`surrogate key`**.

**Definition:** Candidate keys widen the lens from "the one `primary key`" to every `column` that honestly could have filled that `role`.

![Intro visual for candidate keys composite keys and surrogate keys](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/05_intro_candidate_keys_composite_keys_and_surrogate_keys.png)

## Candidate Keys: The Ones That Could Have Been Chosen

Look at Aisha's Books `table`.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">ISBN</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Accession No</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Title</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Author</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">978-93-5118-500-2</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">ACC10234</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data Structures Simplified</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">R. Sundaram</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">978-93-5118-611-0</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">ACC10235</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Introduction to Algorithms</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Meera Krishnan</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">978-93-5118-702-4</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">ACC10236</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Database Design Basics</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Farah Sheikh</td>
    </tr>
  </tbody>
</table>

Both ISBN and Accession No satisfy every requirement a `primary key` demands: each is unique across every `row`, and neither is ever left blank. Either one, alone, could have been chosen as the `table`'s official `primary key`. Any `column`, or minimal combination of `columns`, that meets those requirements is called a **`candidate key`**, precisely because it is a genuine candidate for the job, whether or not it ends up getting picked.

Once Aisha settles on ISBN as her actual `primary key`, Accession No does not disappear or stop being useful, it simply becomes what is often called an alternate key: a `candidate key` that lost the selection but is still perfectly capable of identifying a `row` on its own.

## Composite Keys: Unique Only Together

Now look at Aisha's Book Loans `table`, where no single `column` is unique by itself.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Roll No</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">ISBN</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Loan Date</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Due Date</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">20456</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">978-93-5118-500-2</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2026-06-01</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2026-06-15</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">20456</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">978-93-5118-611-0</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2026-06-01</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2026-06-15</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">20789</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">978-93-5118-500-2</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2026-06-02</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2026-06-16</td>
    </tr>
  </tbody>
</table>

Roll No 20456 repeats across two `rows`, because the same student borrowed two different books on the same day. ISBN 978-93-5118-500-2 also repeats, because that same title was borrowed by two different students.

Neither `column`, alone, can uniquely identify a loan record, and even Roll No and ISBN together are not quite safe: nothing stops the same student from borrowing the same book again on a later date, once it has been returned, which would repeat that same pair.

Add Loan Date into the mix, though, and the combination becomes genuinely unique, since a student is not expected to borrow the exact same book twice on the exact same day. A `primary key` formed by combining two or more `columns`, where the full combination is unique even though no individual `column`, or smaller subset of them, is, is called a **`composite key`**.

## Surrogate Keys: An Identity Invented on Purpose

Aisha's third case, the anonymous Feedback Forms `table`, is different again. Nothing about a submitted form is guaranteed to be unique.

Two students might leave identical comments on the same date, with no roll number recorded at all, since the whole point of the form is anonymity.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Feedback ID</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Comment</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Date</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Please extend library hours during exams</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2026-06-10</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">More seating needed on the ground floor</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2026-06-10</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">3</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Please extend library hours during exams</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2026-06-11</td>
    </tr>
  </tbody>
</table>

Here, Feedback ID is not a natural attribute of the feedback itself, nobody wrote "Feedback ID 1" on their form. It is a plain, ever-increasing number the `table` invents and assigns automatically the moment each new `row` is added, purely to give that `row` a reliable identity when nothing genuinely unique exists in the real-world data.

A `column` like this, an artificial identifier created solely to serve as a `primary key`, is called a **`surrogate key`**. Surrogate keys are extremely common in practice, not only when nothing unique exists, but also when the natural `candidate keys` available are inconvenient, unstable, or unpleasant to work with as an identifier.

![Candidate, composite, and surrogate keys solving three different identity problems in a library database](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/09_candidate_composite_surrogate_keys.png)

## Choosing Among the Three

These three ideas answer three different design questions, and it helps to keep them clearly separate in your mind.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Kind of key</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">The question it answers</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example from Aisha&#x27;s library</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Candidate key</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Which columns could each, alone, have served as the primary key</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">ISBN and Accession No, in the Books table</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Composite key</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What combination of columns becomes unique only when taken together</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Roll No plus ISBN plus Loan Date, in Book Loans</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Surrogate key</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What artificial ID do we invent when nothing natural is reliably unique</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Feedback ID, in the anonymous Feedback Forms</td>
    </tr>
  </tbody>
</table>

A practical habit worth building is to look at any new `table` and ask, in order: is there already a single `column` here that is naturally unique? If there are several, they are all `candidate keys`, and one becomes primary. If none is unique alone but some combination is, that combination becomes a `composite key`.

And if truly nothing in the real-world data can be trusted to stay unique, inventing a `surrogate key` is often the simplest, safest way forward.

![A key-selection decision path from natural unique columns to composite or surrogate keys](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/10_key_selection_decision_path.png)

## Your Turn: Classify the Keys

Aisha adds a fourth `table`, Reading Room Bookings, with `columns` for Roll No, Seat Number, Booking Date, and an auto-generated Booking ID that the `table` assigns to every new `row`. A student can book different seats on different days, and the same seat gets booked by different students on different days, but a given seat can never be double-booked on the same date. Identify the `candidate key`, the `composite key`, and the `surrogate key` in this `table`.

Seat Number plus Booking Date together form the `composite key`, since neither `column` alone is unique, a seat repeats across many dates and a date repeats across many seats, but the pairing of one seat on one date never repeats. Booking ID is the `surrogate key`, an artificial number invented purely to give each booking a reliable identity. Because that composite pairing could itself have served as the `primary key` instead of Booking ID, it also qualifies as a `candidate key`, exactly as Accession No did for Aisha's Books `table`.

## Conclusion

Candidate keys widen the lens from "the one `primary key`" to every `column` that honestly could have filled that `role`. Composite keys show that uniqueness sometimes only emerges once several `columns` are considered together, rather than any one of them alone. And surrogate keys reveal that a `database` is perfectly willing to manufacture an identity out of nothing when the real world simply refuses to offer one naturally.

Aisha's rabbit hole ends with all three of her library `tables` settled: ISBN as the chosen `primary key` with Accession No standing by as its candidate, Roll No plus ISBN plus Loan Date as the `composite key` for Book Loans, and an invented Feedback ID giving her anonymous forms an identity they could never have found on their own.

With a `table`'s identity settled, whether natural, composite, or invented, a `database` still needs a way to enforce everyday rules about the values sitting inside every other `column`, rules like a value that must never be left blank or a value that must always stay one of a kind, and that is exactly the territory worth exploring next.
