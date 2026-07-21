## Introduction

Kabir joined Priya's admissions office as a scholarship coordinator three weeks ago, and his job so far has felt manageable: track every scholarship applicant across three spreadsheets, `applicants.xlsx` for personal details, `documents.xlsx` for uploaded certificates, and `interviews.xlsx` for the shortlist and interview slots. It worked fine when there were forty applicants. This year there are four thousand.

The trouble starts small. A candidate named Rohan Verma submits a corrected category certificate, moving him from the SC scholarship pool to the General merit pool.

Kabir updates `applicants.xlsx` the moment the certificate arrives. Nobody remembers to open `interviews.xlsx`, where Rohan's `row` still lists him under the SC panel three weeks later, on the day of his interview.

Then, on the morning the shortlist is finalized, two coordinators open `interviews.xlsx` at the same time from two different laptops, one adding a new interview slot, the other marking three candidates as confirmed. Both save their copies to the shared drive within a minute of each other.

Whichever file lands last on the server simply overwrites the other, and one coordinator's honest, correct work disappears without so much as an error message.

None of this happened because Kabir or his colleagues were careless. It happened because plain files were never built to hold shared, growing data safely, and the failure has three distinct, well-known faces: **redundancy, inconsistency, and `lost updates`**.

**Definition:** Redundancy creeps in because the same fact has to be retyped wherever it is needed, inconsistency follows because updating one copy never guarantees the others get updated too, and `lost updates` happen because a plain file cannot merge two people's honest changes into one.

<!--
IMAGE PROMPT  ->  generate as images/02_intro_the_problem_with_files.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: DBMS course introduction image based directly on the opening scene of this lesson. Use the named person, setting, and database problem from the Introduction.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue database forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A simple visual of the Introduction: Kabir joined Priya's admissions office as a scholarship coordinator three weeks ago, and his job so far has felt manageable: track every scholarship applicant across three spreadsheets, applicants.xlsx for personal details, documents.xlsx for uploaded.

ON-IMAGE TEXT: show a short bold title "The Problem With Files" plus only these few labels, large and legible: Problem, Files, Kabir. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing DBMS reading-material image standards.
-->

![Intro visual for the problem with files](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/02_intro_the_problem_with_files_matched_b8bd866d.png)

## Redundancy: The Same Fact, Typed More Than Once

Redundancy means a single fact gets stored in more than one place. Rohan's phone number is retyped into every file that needs to be read on its own, without anyone flipping between three tabs:

- `applicants.xlsx`, next to his personal details
- `documents.xlsx`, next to his certificate upload
- `interviews.xlsx`, next to his interview slot

By itself, that repetition causes no damage. It just means one true fact about Rohan now exists in three copies, quietly waiting for someone to update only one of them.

## Inconsistency: When the Copies Stop Agreeing

- That waiting ends the moment Rohan's category certificate is corrected.
- Kabir updates `applicants.xlsx`, the file he happened to have open, and moves on to the next candidate in the queue.
- Nobody touches `interviews.xlsx`, which still shows Rohan under the SC panel on interview day.

- Ask a simple question now: which category is Rohan actually in? `applicants.xlsx` says General merit. `interviews.xlsx` says SC.
- Both files claim to hold the truth, and they disagree, which is exactly what **inconsistency** means: redundant copies of the same fact, updated in one place and left untouched in another, until nobody can say with confidence which one is correct.

![Updating one of three redundant spreadsheet copies leaves the files in conflict](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/03_redundancy_creates_inconsistency.png)

## Lost Updates: When Two Changes Collide

The interview-day mix-up is the sharpest version of the same underlying problem. Two coordinators edit `interviews.xlsx` within the same minute, each making a genuine, correct change.

The shared drive has no way to merge their two edits into one file that reflects both. It keeps whichever file was saved last and quietly discards the other, along with every confirmed slot the discarded coordinator had just entered.

This is a **`lost update`**: two valid, simultaneous changes to the same shared file, where only one survives and the other vanishes with no warning at all.

![Two coordinators save valid changes to one spreadsheet, but the last save overwrites the first](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/04_lost_update_last_save_wins.png)

## The Three Symptoms at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Symptom</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What happens</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Admissions office example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Redundancy</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The same fact is stored in more than one file</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rohan&#x27;s phone number typed into applicants, documents, and interviews files</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Inconsistency</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Redundant copies disagree after only one is updated</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Rohan&#x27;s category shows General in one file, SC in another</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Lost updates</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Two simultaneous edits to the same file, only one survives</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A coordinator&#x27;s confirmed interview slots vanish when a second save overwrites the first</td>
    </tr>
  </tbody>
</table>

## Could More Discipline Fix This?

It is tempting to blame the people rather than the tool. Could Kabir's office simply agree on a rule: always update every file the moment anything changes, and never let two people open the same file at once?

For three files and two coordinators, that rule might survive a week. It will not survive:

- a busy interview season, with dozens of edits landing within minutes of each other
- a new volunteer who was never told the rule
- the ordinary human habit of updating the file already open and trusting that someone else will remember the rest

The moment shared data is written to and read from by more than one person, at any real scale, these three symptoms stop being rare accidents and become a routine, predictable cost of using plain files for something they were never designed to do: coordinate simultaneous, shared access to the same facts.

## Your Turn: Name the Symptom

A hostel warden keeps three spreadsheets: `residents.xlsx` (room assignments), `fees.xlsx` (who has paid), and `complaints.xlsx` (maintenance requests). A student's phone number is retyped into all three. Read each scenario below and name which of the three symptoms, redundancy, inconsistency, or a lost update, it illustrates.

1. The warden updates a student's phone number in `residents.xlsx` after she changes her number, but `fees.xlsx` and `complaints.xlsx` still show the old one.
2. Two wardens both open `fees.xlsx` on Monday morning; one marks Room 12 as paid, the other marks Room 14 as paid, and only the second save survives.
3. Every one of the three files stores the same student's phone number in its own column.

Scenario 1 is inconsistency: the same fact now disagrees across files because only one copy was updated. Scenario 2 is a lost update: two genuine, simultaneous edits collide, and one vanishes without warning. Scenario 3 is redundancy itself, the root cause sitting quietly before either of the other two symptoms even has a chance to appear: the same phone number typed three times is what makes disagreement and overwritten edits possible in the first place.

## Conclusion

Redundancy creeps in because the same fact has to be retyped wherever it is needed, inconsistency follows because updating one copy never guarantees the others get updated too, and `lost updates` happen because a plain file cannot merge two people's honest changes into one. None of this is a character flaw in Kabir's team, it is what plain files do, reliably, once real numbers and real deadlines arrive.

The natural next question is what kind of tool would actually solve all three problems at once, and what exactly it means to say that tool holds a single, organized body of data rather than just another file.
