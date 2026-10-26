## Introduction

Some systems are best understood not as objects that call each other but as data flowing through a series of transformations. A compiler reads source text and passes it through stages that scan, parse, analyse, and generate code. A command typed at a terminal can chain simple programs so that the output of one becomes the input of the next. A nightly job might extract data from a store, clean it, combine it, and load it into a report. These are data-flow architectures, and the best known is pipes and filters.

**Definition:** Pipes and filters is an architectural style in which processing is divided into independent steps, called filters, each of which reads input, transforms it, and writes output, connected by pipes that carry the data from one filter to the next.

<!--
IMAGE PROMPT  ->  generate as images/09_intro_pipes_and_filters_and_data_flow_architectures.png   (16:9 cinematic hero image, place here, right after the Introduction)

CHARACTER & THEME: Software Engineering course introduction image based directly on the opening scene of this lesson. Show the core idea of the lesson visually, with no named characters.

STYLE: world-class high-end 3D render, cinematic and vibrant, glossy soft 3D forms, blue software forms, green positive accents, orange secondary accents, red warnings, soft studio-gradient backdrop, minimal large labels.

SCENE: A horizontal assembly line: a Source feeding a pipe into Filter A (clean), another pipe into Filter B (transform), another into Filter C (aggregate), and a final pipe into a Sink labelled Report, with data items shown moving along.

ON-IMAGE TEXT: show a short bold title "Pipes and Filters" plus only these few labels, large and legible: Source, Filter, Sink. Keep text minimal, no sentences.

GOAL: make the opening idea instantly clear and engaging while matching the existing reading-material image standards.
-->

## The Elements

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Element</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Role</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Example in a daily sales report</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data source</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Produces the input data</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The orders store</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Filter</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A processing step that transforms data; knows nothing about the other filters</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Remove cancelled orders; convert currencies; total sales per dish</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pipe</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A connector carrying data from one filter to the next</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A stream, file, or queue between the steps</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data sink</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Consumes the final output</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A report file or dashboard</td>
    </tr>
  </tbody>
</table>

## Properties of Filters

- **Independent.** Each filter works only with its input and output, sharing no hidden state with other filters.
- **Composable.** Filters can be combined in different orders and reused in different pipelines.
- **Replaceable.** A filter can be improved or substituted without changing others, as long as the data format matches.
- **Testable.** Each filter can be checked alone with sample input and expected output.
- **Parallelisable.** Different filters can work on different items at the same time, like stations on an assembly line.

## Familiar Examples

- **Command-line tools,** where small programs are chained, each doing one job.
- **Compilers,** with stages for scanning, parsing, checking, optimising, and generating code.
- **Data processing pipelines,** often called extract, transform, load (ETL), used to move and clean data for analysis.
- **Image and video processing,** where a series of operations is applied in turn.
- **Stream processing systems,** which process continuous flows of events through a chain of operations.
- **Build and delivery pipelines,** where stages build, test, and release software in sequence.

## Variants

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Variant</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Description</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Typical use</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Batch sequential</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Each stage processes all its input before the next begins</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Nightly reports, traditional data processing</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Pipeline (streaming)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Stages run concurrently, passing items along as they appear</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Real-time processing, streams</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Branching and merging</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Data is split into parallel paths and rejoined later</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Processing different categories separately</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Blackboard (related style)</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Independent specialists read and write a shared store, each contributing when it can</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Problems with no fixed order of solution, such as speech recognition</td>
    </tr>
  </tbody>
</table>

## Benefits

- **Simplicity of reasoning:** each step has a clear input and output.
- **Reuse:** filters can be used in several pipelines.
- **Flexibility:** pipelines are rearranged by reconnecting filters.
- **Natural performance gains:** concurrent execution of stages.
- **Maintainability:** a defect or change is confined to one filter.

## Drawbacks

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Problem</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Explanation</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Common data format</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Filters must agree on the format of data, and converting between formats costs effort and time</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Not suited to interaction</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The style fits transformations of data, not interactive applications driven by user events</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Error handling is difficult</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">A failure in the middle of a pipeline affects everything downstream, and recovery needs a design</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Sharing state is awkward</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Steps needing global context are hard to express</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Throughput limited by the slowest step</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">The slowest filter is the bottleneck, and buffering between stages adds delay</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Debugging</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Following one item through many stages needs tooling</td>
    </tr>
  </tbody>
</table>

## Designing a Good Pipeline

- Keep each filter **small and focused** on one transformation.
- Define the **data format between filters** clearly and keep it stable.
- Decide how **errors** are handled: stop, skip and record the item, or send it to a separate stream for later examination.
- Make filters **idempotent** where possible, so that a failed run can be repeated safely.
- Provide **monitoring** at each stage: counts, delays, and failures.
- Consider **back-pressure**, so that a fast producer does not overwhelm a slow consumer.

<!--
IMAGE PROMPT  ->  generate as images/02_data_pipeline_with_branch_and_error_stream.png   (16:9 explanatory diagram, place here)

A pipeline for a daily sales report: Orders store, Remove cancelled, Convert currency, Total per dish, Report. A branch after Remove cancelled sends bad records to an Error stream box in orange. Counters above each pipe show items flowing.

STYLE: clean flat-3D infographic, blue primary forms, green for correct or healthy, orange for caution, red for failure, large legible labels, minimal text.
-->

## Your Turn: Style Fit

1. A job that reads sales records, removes invalid ones, converts amounts to one currency, and totals them by dish.
2. A graphical editor in which the user clicks and drags objects and sees immediate results.
3. A compiler turning source text into runnable code in several stages.

Case 1 suits pipes and filters, or a batch pipeline. Case 2 does not: it is interactive and driven by user events, and an event-driven or layered style with MVC fits better. Case 3 is a classic pipes-and-filters design, with stages from scanning to code generation.

## Conclusion

Pipes and filters is an architectural style in which processing is divided into independent steps, called filters, each of which reads input, transforms it, and writes output, connected by pipes that carry the data from one filter to the next. It is simple, composable, and well suited to transformation of data.

The styles studied so far connect parts across machines and networks, and that raises problems that do not exist inside one process. The next chapter turns to the fundamentals of distributed systems.
