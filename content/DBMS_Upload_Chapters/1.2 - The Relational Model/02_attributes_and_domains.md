## Introduction

Kabir runs a small gym membership desk in Bengaluru and keeps a signup register for new members. One afternoon a new member fills in the form: name, phone number, and age.

Under "Age," the member, in a hurry, writes "twenty-five." Under "Phone," someone else once wrote "call my brother instead." Kabir stares at both entries and realises his register has a problem that has nothing to do with the people filling it in. The register never told anyone what kind of answer belonged in each box.

He redraws the form. Next to "Age," he now prints a small note: "whole number, 10 to 90." Next to "Phone," he prints: "10 digit mobile number, digits only." Suddenly the boxes are no longer just blank spaces waiting for whatever someone feels like writing. Each box has a personality of its own: a set of answers that are acceptable, and everything else that simply is not.

That personality is exactly what a database means by a column's **domain**. Every column, or **attribute**, in a table has a name, and behind that name sits a domain, the complete set of legal values that column is ever allowed to hold. An "Age" column's domain might be whole non-negative numbers within a sensible range.

An "Email" column's domain is the set of text values shaped like a valid email address. Understanding attributes and domains is what lets a database catch a nonsense entry before it ever becomes a row.

![Kabir adding domain gates so only valid age, phone, and email values enter the Members table](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_attribute_domain_entry_gates.png)

**Definition:** An attribute is a column's name, but its domain is the promise behind that name, the exact boundary of values the column will ever legitimately hold.

## An Attribute Is More Than Just a Label

A column is a named attribute every row has, but that name alone is only half the story. Consider Kabir's Members table.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Member ID</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Name</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Age</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Phone</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Email</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">1</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Farah Sheikh</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">25</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">9845012233</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">farah.sheikh@example.com</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">2</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Vivek Iyer</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">31</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">9900112244</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">vivek.iyer@example.com</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">3</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Naina Kapoor</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">19</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">9811223344</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">naina.kapoor@example.com</td>
    </tr>
  </tbody>
</table>

The column named "Age" is not just a label sitting at the top of the grid. It is a promise about every single value underneath it: each one will be a whole number, it will never be negative, and it will realistically fall somewhere a human lifespan makes sense, say 10 to 90.

The column named "Email" carries a different promise entirely: every value underneath it will look like text with an "@" symbol and a domain name, never a bare number, never a sentence, never someone's phone number typed into the wrong box.

## Domain: The Set of Legal Values

A **domain** is the complete set of values a given attribute is permitted to hold. Age's domain is not "any number at all," it deliberately excludes -5, 400, and "twenty-five" written as words. Phone's domain is not "any text," it excludes "call my brother instead" just as firmly as it excludes a five-digit number.

Defining a domain is really answering one question in advance, for every future value that column will ever receive: what does a correct answer here actually look like?

A few everyday examples make this concrete.

A column for **age** should only ever hold whole, non-negative numbers, realistically bounded, since nobody's age is -5 or 3.7. A column for **email** should only hold text shaped like a valid email address, containing an "@" and a domain part, not a phone number and not a random sentence.

A column for **date of birth** should only hold values that are genuine calendar dates, and never a date sitting in the future. A column for **gender** at many organisations is restricted to a short, fixed list of allowed labels, rather than accepting any free text a person types in.

A column for **marks out of 100** should only hold numbers from 0 to 100, since 105 or -10 cannot be a real score on that scale.

Notice that a domain is not just about the type of value, whole number versus text, it is also about which values within that type actually make sense. Both -5 and 25 are whole numbers, but only one of them belongs in Age.

![Whole-number values filtered by narrower age and marks domains](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_type_vs_domain_boundaries.png)

## Why Domains Matter Before a Single Row Is Ever Entered

Kabir's original, undefined register let anyone write anything, and the result was chaos: an age written as a word, a phone number that was not a phone number at all. The moment he wrote down a domain for each box, the boxes themselves started doing part of his job for him.

A person filling the age box now knows, before writing anything, that the expected answer is a small whole number, not a sentence.

This matters even more inside an actual database, because a database is meant to answer questions reliably at scale. If even a handful of rows in a million-row Members table have "Age" values like "young" or "N/A" or "25 years," any calculation that tries to find the average age, or list members between 20 and 30, either breaks outright or quietly produces a wrong answer.

Defining a strict domain for every attribute, before data starts arriving, is what keeps a table trustworthy as it grows from four rows to four million.

## Attributes and Domains at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Attribute</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it represents</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">A sensible domain</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Age</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A member&#x27;s age in completed years</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Whole numbers, roughly 10 to 90</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Email</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A member&#x27;s contact email address</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Text shaped like name@domain, containing an &quot;@&quot;</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Phone</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A member&#x27;s mobile number</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Exactly 10 digits, digits only</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Gender</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A member&#x27;s recorded gender</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">One of a short fixed list of allowed labels</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Marks</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A score out of 100 on an exam</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Whole numbers from 0 to 100</td>
    </tr>
  </tbody>
</table>

- A useful habit, whenever you meet a new column in any table for the rest of this course, is to pause and ask two questions: what kind of value is this attribute meant to hold, and what values, even though they might technically be the same type, would actually be nonsense here.
- That second question is usually the more revealing one.

## Your Turn: Set the Boundaries

Kabir wants to add two more columns to his Members table: "Membership Plan" (Monthly, Quarterly, or Annual) and "Joining Date." For each, decide what the domain should be, and name one value that looks technically valid but should still be rejected.

Membership Plan's domain is a short fixed list: only "Monthly," "Quarterly," or "Annual" are legal, so a value like "Yearly" would be rejected even though it is ordinary text, because it does not match any of the three allowed labels. Joining Date's domain is genuine calendar dates that are not in the future, so "2027-01-01" would technically be a valid date but should still be rejected, since nobody can join Kabir's gym tomorrow's yesterday.

## Conclusion

An attribute is a column's name, but its domain is the promise behind that name, the exact boundary of values the column will ever legitimately hold. Fixing that boundary in advance, before a single row exists, is what stops a database from quietly filling up with entries that look like data but mean nothing, an age written as a word, a phone number that is really a sentence.

Kabir's redrawn signup form is really an early, informal version of exactly this idea, the moment he wrote "whole number, 10 to 90" next to Age, he was defining a domain, and no new member will ever again be able to write "twenty-five" in that box.

Once a table's attributes and their domains are settled, a sharper question naturally follows: among all these columns, which one, or which combination of them, can be trusted to tell two rows apart with total certainty, even when every other value in those rows happens to match.
