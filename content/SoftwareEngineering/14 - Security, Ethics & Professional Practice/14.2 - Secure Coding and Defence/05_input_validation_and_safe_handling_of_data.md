## Introduction

Every program receives data from outside: form fields, uploaded files, query strings, messages from other services, command-line arguments, even values in a database that were originally entered by someone. Any of it may be malformed by accident or crafted by an attacker. A large share of vulnerabilities arise at one point: the program treats such data as if it were safe. Safe handling of data rests on three practices applied at different moments: checking data when it enters (validation), keeping data from being mistaken for instructions when it is passed on (separation and parameterisation), and making data harmless when it is shown or used in another context (output encoding).

This topic explains the principle of distrusting input, the difference between validation and sanitisation, the ways of passing data safely to interpreters, how to handle the output side, and special cases such as files and web requests.

**Definition:** Safe data handling is the set of practices by which a program treats all data crossing a trust boundary as untrusted, verifying that it has the expected form before accepting it, keeping it distinct from commands when passing it to other components, and encoding it appropriately for the context in which it is used or displayed.

<!--
IMAGE PROMPT  ->  generate as images/05_intro_input_validation_and_safe_handling_of_data.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A funnel-shaped gate on the left labelled Validate admitting only shaped blocks while rejecting odd ones, a middle panel with data and command shown as two separate lanes, and a right panel with a speech-bubble labelled Encode for output.

ON-IMAGE TEXT: show a short bold title "Input Validation and Safe Handling of Data" plus only these few labels, large and legible: Validate, Separate, Encode. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Never Trust Input

Data from outside a trust boundary must always be treated as untrusted. This includes:

- direct user input in forms and URLs;
- information in requests that the user can change: headers, cookies, hidden fields, and any value computed in the browser;
- files and their names, types, and contents;
- data from other systems and third-party services;
- environment values, configuration from untrusted locations;
- data previously stored that originated outside the system.

**Client-side checks do not count as security.** Browser or mobile-app validation is useful for usability, giving fast feedback, but an attacker can bypass the client entirely and send requests directly. The server must check everything again.

## Validation

**Validation** is checking that data meets the expectations of the application before it is used.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Kind of check</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">What it verifies</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Type</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The value is of the expected kind</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A quantity is a whole number</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Length and size</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Within limits</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Name no longer than a set length; upload no larger than a limit</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Range</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Within allowed bounds</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Quantity between 1 and 20</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Format</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Matches the expected pattern</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">An email address, a postal code, a date</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Allowed values</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Belongs to a fixed set</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Order status is one of the known states</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Presence</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Required values are supplied</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Delivery address</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Consistency</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fields agree with each other</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">End date after start date</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Business rules</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Meets domain constraints</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Discount code valid for this customer and date</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Authorisation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The user may use this value</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The order belongs to the user</td>
    </tr>
  </tbody>
</table>

### Principles

- **Allow-list (positive validation) over deny-list.** Define what is acceptable and reject everything else. Lists of bad inputs are always incomplete, because attackers find variants.
- **Validate early, at the boundary,** so that the rest of the code can rely on well-formed data. Defining types that can only hold valid values (for example, a type for an email address that is validated when created) keeps checks in one place.
- **Validate on the server,** and again in each service that receives data, as services should not assume others have checked.
- **Reject, do not repair, where possible.** Silently altering input may produce unexpected results.
- **Normalise before validating:** convert to a canonical form (character encoding, case, path form) so that equivalent forms cannot slip past a check.
- **Limit size and complexity** to prevent resource exhaustion.
- **Give useful but not revealing error messages.** Tell the user what is wrong with their input, without exposing internals.
- **Validation is not a substitute for the other two practices.** Some valid data, such as a surname with an apostrophe, is legitimately dangerous in certain contexts and still needs separation and encoding.

## Sanitisation

**Sanitisation** modifies input to remove or neutralise dangerous parts, for example by stripping markup from user-supplied text. It is sometimes necessary, such as when allowing limited formatting in comments, but it is error-prone: it depends on predicting every harmful form. Prefer, in order: reject invalid data; separate data from commands; encode for the context; and sanitise using a well-maintained library only when richer input must be accepted. Never write an ad hoc cleaning routine from scratch.

## Keeping Data Away from Commands

The most important defence against injection is structural: never build a command by joining strings that include untrusted data.

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Interpreter</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Danger</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Safe approach</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Database (SQL)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data altering the meaning of a query, exposing or destroying data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">**Parameterised queries** (prepared statements), in which the query structure is fixed and values are supplied separately as data; stored procedures that use parameters safely; object-relational mappers that parameterise by default (Unit 12)</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Operating system shell</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data run as commands</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Avoid calling the shell; use library functions for the task; if unavoidable, pass arguments as separate items, not one text string; validate against allow-lists</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Directory services, XML processors, template engines, expression languages</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data interpreted as directives</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use safe configuration; disable dangerous features; use parameterised or escaped interfaces</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">File system paths</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data like "go up one folder" reaching unintended files (**path traversal**)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Do not build paths from user input; map identifiers to files through a lookup; resolve and verify the final path stays within an allowed folder</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Web pages (HTML, scripts)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data run as script in another user's browser (**cross-site scripting**)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Output encoding; frameworks that escape automatically; content security policies</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Deserialisation</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Crafted data triggering behaviour while being reconstructed</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use data-only formats; do not deserialise untrusted objects; verify integrity (Unit 12)</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Outgoing requests</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data controlling where the server connects (server-side request forgery)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Allow-lists of destinations; block internal ranges</td>
    </tr>
  </tbody>
</table>

The common idea is **separating the code channel from the data channel.** Parameterised interfaces ensure that whatever the user types is only ever data, no matter what characters it contains.

## Encoding Output

Data that is safe in one place can be dangerous in another. A piece of text containing angle brackets is harmless in a database but can inject script when placed in a web page. **Output encoding** transforms data so that it is displayed literally in the target context.

- Encoding depends on the **context:** the body of an HTML page, an HTML attribute, a script, a style sheet, a web address, a JSON document, and a log file each have different special characters.
- Use the **encoding facility of the framework** or a reputable library, and prefer templating systems that escape by default.
- Encode **at the point of output,** not on input, because the same stored data may be used in several contexts.
- **Content Security Policy** (a browser feature controlled by a response header) limits which scripts a page may run, giving a second layer of defence against cross-site scripting.
- **Log injection** is prevented by encoding line breaks and control characters in anything written to logs.

## Web Request Forgery and Related Protections

- **Cross-site request forgery (CSRF)** tricks a logged-in user's browser into sending an unwanted request to a site that trusts it. Defences are anti-forgery tokens, same-site cookie settings, and requiring re-authentication for sensitive actions.
- **Clickjacking** hides a site inside another to trick clicks. Defence: instruct browsers not to allow framing by other sites.
- **Open redirects** let attackers use a trusted site to send users to a malicious one. Defence: allow-list redirect targets.
- **Mass assignment** occurs when a framework copies all submitted fields into an object, so a user can set fields they should not, such as a role. Defence: explicitly list the fields that may be set.
- **HTTP security headers** instruct browsers to enable protections; set them as part of default configuration.

## Files and Uploads

Uploaded files are a rich source of risk.

- Limit **size** and **number.**
- Check the **actual type** of content, not just the file name or the claimed type.
- Store uploads **outside** the area served directly, with generated names; never trust the supplied name.
- **Scan** for malware where appropriate.
- Serve with the right content type and, for downloads, as attachments.
- Process images and documents in **isolated** environments, since parsers have had many flaws.

## Special Cases

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Case</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Care needed</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Numbers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Check ranges; beware of overflow and negative values; use exact types for money (Unit 12)</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Dates and times</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Use standard formats; check that dates are real</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Text and character sets</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Normalise; beware of look-alike characters and unusually long text; use UTF-8 consistently</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Regular expressions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Patterns can be written to take very long on crafted input (**ReDoS**); use simple patterns and limits</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Email addresses and names</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Do not over-restrict: real names include apostrophes, hyphens, and many scripts; verify addresses by sending a message, not by clever patterns</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Serialised and structured data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Limit size and nesting; validate against a schema (Unit 12)</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Machine-generated input</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Other services also fail or are compromised; validate their data too</td>
    </tr>
  </tbody>
</table>

## A Layered View

No single technique suffices. A robust application layers them: validate on entry; use safe interfaces for passing data on; encode on output; run with least privilege so that a mistake has limited effect; log suspicious input; and test with deliberately malformed input, including **fuzzing,** which feeds large numbers of random or mutated inputs to find crashes and failures.

<!--
IMAGE PROMPT  ->  generate as images/05_validate_separate_encode.png   (16:9 explanatory diagram, place here)

Left to right: Untrusted input passing a Validate gate (allow-list), then a Parameterised interface where data and command travel in separate lanes into a database, then an Encode step before a browser page. Red crossed-out arrow shows string-joining being rejected.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Handle the Data

1. A developer checks that a quantity field is a number in the browser only. What is missing?
2. A comment field allows users to post text that is shown to others. Which two practices protect other users?
3. Why is an allow-list better than a list of forbidden characters?

For case 1, server-side validation, since the browser can be bypassed. For case 2, output encoding for the page (or a safe framework that escapes by default), and where formatting is allowed, a well-maintained sanitisation library plus a content security policy. For case 3, an allow-list defines exactly what is acceptable, whereas a deny-list must foresee every harmful variant and is bypassed by one it missed.

## Conclusion

Safe data handling is the set of practices by which a program treats all data crossing a trust boundary as untrusted, verifying that it has the expected form before accepting it, keeping it distinct from commands when passing it to other components, and encoding it appropriately for the context in which it is used or displayed. Validation, parameterisation, and encoding together close off the most common route into software.

Even perfectly validated data must come from someone, and the system must know who that someone is and what they may do. The next topic covers authentication and authorisation.
