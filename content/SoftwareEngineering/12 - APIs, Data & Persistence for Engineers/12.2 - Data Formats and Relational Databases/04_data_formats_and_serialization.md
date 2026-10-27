## Introduction

Programs hold data as structures in memory: objects, lists, numbers, and text, arranged in ways that suit the language and the machine. These structures cannot be sent over a network or saved to a file as they are, because memory layouts differ between languages and systems and mean nothing outside the running program. Data must first be converted into a sequence of bytes or characters in an agreed format, and converted back by the receiver. This conversion is called serialisation, and the agreed formats are the common language of APIs, files, messages, and storage.

This topic explains serialisation, the main data formats and their trade-offs, the role of schemas, and the practical pitfalls of representing numbers, dates, and text.

**Definition:** Serialisation is the process of converting an in-memory data structure into a sequence of bytes or text in an agreed format so that it can be stored or transmitted, and deserialisation is the reverse process of reconstructing the structure from that representation.

<!--
IMAGE PROMPT  ->  generate as images/04_intro_data_formats_and_serialization.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based on the central concept of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: Left: a structured object in memory drawn as connected boxes; an arrow labelled Serialise leads to a linear strip of text or bytes in the centre; an arrow labelled Deserialise leads to a reconstructed object on a different machine on the right.

ON-IMAGE TEXT: show a short bold title "Data Formats and Serialization" plus only these few labels, large and legible: Structure, Bytes, Structure. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## Why Formats Matter

- **Interoperability:** the sender and receiver may be written in different languages, by different organisations, years apart. A shared format is the only thing they need to agree on.
- **Longevity:** stored data outlives the code that wrote it.
- **Performance:** the format affects size, speed of conversion, and network cost.
- **Evolvability:** formats must survive changes to the data they carry.
- **Security:** reading untrusted data is a classic source of vulnerabilities.

## Text and Binary Formats

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Kind</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Description</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Advantages</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Disadvantages</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Text formats</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data is written as readable characters</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Human-readable; easy to debug and to edit; independent of machine details</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Larger; slower to read and write; numbers and binary data are awkward</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Binary formats</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data is written as compact bytes</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Small and fast</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not readable without tools; need a schema or specification to interpret</td>
    </tr>
  </tbody>
</table>

## Common Formats

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Format</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Description</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical use</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">JSON (JavaScript Object Notation)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Text format built from objects (named values), arrays (ordered lists), strings, numbers, true, false, and null. Popularised by Douglas Crockford in the early 2000s and standardised as an internet standard</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The dominant format for web APIs and configuration</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Simple and readable; no comments; no native date type; limited number precision; no binary type</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">XML (extensible markup language)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Text format using nested tagged elements and attributes; a W3C standard from 1998</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Documents, older enterprise systems, SOAP</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Verbose but powerful, with schemas, namespaces, and transformation tools</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">YAML</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Text format that uses indentation for structure, designed for human readability</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Configuration files</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Readable, but subtle rules cause mistakes; richer features can be unsafe to read from untrusted sources</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">CSV (comma-separated values)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Text rows of values separated by commas</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tabular exports and imports; spreadsheets</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">No standard for types or for the treatment of commas, quotes, and line breaks within values; encoding issues</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Protocol buffers (Google)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Compact binary format defined by a schema, with generated code for many languages</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Internal service communication, gRPC</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Fast and small; needs the schema to read</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Avro and Thrift</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Schema-based binary formats with strong support for schema evolution</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data pipelines and streaming systems</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Schema travels with the data or is held in a registry</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">MessagePack, CBOR</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Binary encodings of the same data model as JSON</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Where JSON is wanted but smaller and faster</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not human-readable</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Parquet and ORC</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Columnar binary formats that store each column together</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Analytics and data warehouses</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Efficient to scan a few columns across many records; poor for single-record updates</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">HTML and form encodings</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Web page markup, form submissions</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Browsers</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Presentation-focused</td>
    </tr>
  </tbody>
</table>

No format is best for all purposes. A typical system uses JSON at its public API, a compact binary format between internal services, CSV for exports, and a columnar format for analytics.

## Schemas

A **schema** describes the structure of data: which fields exist, their types, which are required, and any constraints. Schemas make data self-describing or at least checkable.

- **Validation:** data can be checked automatically against its schema at the boundary, rejecting malformed input early.
- **Documentation:** the schema is a precise statement of the contract.
- **Code generation:** types and parsers can be generated in many languages.
- **Compatibility checking:** changes to a schema can be tested for compatibility before release.

Examples are JSON Schema for JSON, XML Schema for XML, and the definitions of protocol buffers and Avro, which are central to those formats. Some formats, such as plain JSON, are **schema-optional**, which gives flexibility but pushes responsibility for validation onto the application.

## Evolving Formats

Data formats must change over time, as APIs do. Two directions of compatibility matter.

- **Backward compatibility:** new code can read data written by old code.
- **Forward compatibility:** old code can read data written by new code, by ignoring what it does not understand.

Practices that support both:

- **Add optional fields** with defaults, and do not remove or repurpose existing ones.
- **Identify fields stably.** Binary formats use numbers or names that must never be reused for a different meaning.
- **Ignore unknown fields** when reading.
- **Include a version** where changes cannot be compatible.
- **Use a schema registry** in systems that exchange many messages, to manage and check changes.

This is particularly important for stored data and for messages in queues, which may be read long after they were written, by software of a different version.

## Representing Values Correctly

Many defects arise from how particular kinds of value are represented.

### Numbers

- **Floating-point numbers** are approximate: some decimal fractions, such as one tenth, cannot be represented exactly, so sums can be slightly off. They are suitable for measurements and unsuitable for **money.**
- **Money** should be held as whole numbers of the smallest unit (for example, the smallest coin) or in an exact decimal type, together with a **currency code.**
- **Large integers** may exceed the range of the receiver's number type. Some systems send them as text.
- **Precision and rounding rules** should be stated.

### Dates and Times

Dates and times are an enormous source of error.

- Use a standard format, **ISO 8601**, for text representations, for example year, month, day, then time.
- Store and exchange times in **UTC** (coordinated universal time), and convert to local time only for display.
- Include the **time zone or offset** where local time matters.
- Remember that **daylight saving changes,** leap years, and different calendars exist.
- Distinguish a **date** (a calendar day), a **point in time**, and a **duration**.

### Text

- Use **Unicode** with the **UTF-8** encoding, which can represent text in all languages and is the dominant standard.
- Be careful with **length**: the number of bytes, characters, and visible symbols can differ.
- Expect **special characters,** very long strings, and empty text.
- **Escape** or encode text properly when embedding it in other formats.

### Absence

Formats differ in how they express **missing** data: an absent field, an explicit null, an empty string, and zero are different things. An API should state which it uses and treat them consistently.

### Binary Data

Text formats cannot hold raw bytes, so binary content such as images is encoded as text, commonly with **Base64**, which increases size by about a third, or sent separately as a file with its own address.

### Identifiers

Use identifiers that are **opaque and stable.** Large numeric identifiers can lose precision in some receivers; unique text identifiers avoid that.

## Security of Deserialisation

Reading data from outside is risky.

- **Treat all incoming data as untrusted:** validate type, size, range, and structure before use.
- **Limit sizes and depth** to avoid exhaustion of memory and processing time.
- **Beware of formats and libraries that can create arbitrary objects or run code during reading.** Insecure deserialisation, in which crafted data causes a program to execute attacker-chosen behaviour, is a well-known class of vulnerability. Prefer simple data-only formats and libraries configured safely.
- **Do not trust declared types or lengths.**
- **Protect sensitive fields** and avoid logging them.

## Choosing a Format

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Question</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Guidance</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Who reads it?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">People and diverse external consumers favour readable text formats, JSON in particular</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How much data and how fast?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">High volume or low latency favour compact binary formats</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">How long will it live?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Long-lived data needs a schema and a plan for evolution</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What tools exist?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Choose a format with good libraries in your languages</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">What is the shape of the data?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Tabular analytics suit columnar formats; nested documents suit JSON or XML</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Does it need validation?</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A schema-based format makes the contract explicit</td>
    </tr>
  </tbody>
</table>

<!--
IMAGE PROMPT  ->  generate as images/02_text_vs_binary_and_schema_evolution.png   (16:9 explanatory diagram, place here)

Left: the same order record drawn as a readable text block (large) and a compact binary strip (small), with size labels. Right: two versions of a schema, old reader and new writer, with an added optional field marked green and a removed field marked red, illustrating backward and forward compatibility.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Represent It Well

1. A shop stores prices as decimal numbers with fractions in a floating-point type and finds that totals are occasionally a fraction off. What is the remedy?
2. A system exchanges times in each user's local time with no zone information. What problem will arise?
3. An old program receives data from a newer program that has added a field. What property lets it carry on working?

For case 1, hold money as whole units of the smallest denomination, or an exact decimal type, with a currency code. For case 2, times will be ambiguous across zones and daylight saving changes; use UTC with an explicit offset. For case 3, forward compatibility, achieved by ignoring unknown fields.

## Conclusion

Serialisation is the process of converting an in-memory data structure into a sequence of bytes or text in an agreed format so that it can be stored or transmitted, and deserialisation is the reverse process of reconstructing the structure from that representation. Choosing a suitable format, describing it with a schema, planning for its evolution, and representing numbers, times, and text with care prevent a large class of defects.

The place where most application data finally rests is a database. The next topic introduces relational databases and the SQL language for developers.
