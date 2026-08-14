## Introduction

Priya has nine minutes to file her match report from the press box in Chennai, and she needs one fact about a debutant she had not heard of before this morning. She types his name into a search engine, and down the right-hand side comes his date of birth, the teams he has played for, his batting style, a short list of records, and a row of other players underneath labelled as people also searched for.

Nobody wrote that panel. There is no page on the internet that happens to contain exactly those facts in exactly that arrangement, and no engineer at the search company assembled it for this particular player. The system built it, on request, out of stored knowledge about entities and the relationships between them.

Now ask what makes that possible. The system must know that this name refers to a person rather than a place. It must know that a person has a date of birth, that a cricketer has a batting style, and that a cricketer is a kind of sportsperson who is a kind of person. It must know which of its stored relationships are worth displaying and which are not.

That is not a list of facts. It is a **structure**, in which the arrangement of the knowledge carries information that no individual fact contains. Representations designed to make that structure explicit are the subject of this lesson.

**Definition:** `Semantic knowledge models` represent knowledge as a structured network of entities and the labelled relationships between them, so that the organisation itself supports inference, most notably by allowing properties to be inherited from general categories down to specific instances.

![Priya searches for a debutant cricketer as a right-hand knowledge panel assembles connected facts with nine minutes remaining](images/08_section_introduction_v2.png)

## Semantic Networks

A `semantic network` is the simplest of these. Entities are nodes, relationships are labelled arrows between them, and that is the entire notation.

Take a small library.

| From | Relationship | To |
| --- | --- | --- |
| Reference Book | is-a | Book |
| Book | is-a | Library Item |
| Library Item | has-property | catalogue number |
| Book | has-property | ISBN |
| Reference Book | has-property | cannot be borrowed |
| Midnight's Children | instance-of | Book |
| Midnight's Children | written-by | Salman Rushdie |
| Salman Rushdie | is-a | Author |

Two kinds of arrow are doing very different jobs, and confusing them is the commonest error in this material.

- **is-a** connects a category to a broader category. Reference Book is a kind of Book. It relates two classes.
- **instance-of** connects a specific individual to its category. Midnight's Children is one particular book, not a kind of book.

The distinction matters because "Book has an ISBN" means every book has one, whereas "Midnight's Children was written by Salman Rushdie" is a fact about one object and says nothing about books in general.

The payoff of the structure is `inheritance`. Ask whether a reference book has a catalogue number, and no stored fact says so. The system follows is-a upward, from Reference Book to Book to Library Item, finds the catalogue number property there, and answers yes. **The answer was derived from the shape of the network rather than retrieved from it**, and that is what separates a semantic network from a table of facts.

Inheritance also makes the knowledge base far smaller. State a property once at the most general category where it holds, and every specialisation below gets it without repetition. Correct it once, and every specialisation is corrected.

![Visual explanation of semantic networks frames](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/08_semantic_networks_frames_context_v4.png)

## The Inheritance Exception Problem

Inheritance has a famous difficulty, and meeting it now will save confusion later.

Birds fly. A penguin is a bird. Therefore a penguin flies, which is false.

The obvious repair is to attach a contradicting property to the more specific node: penguins do not fly. The system then has two answers available and needs a rule for choosing, and the rule everyone adopts is that **the most specific statement wins**. Penguin is more specific than Bird, so its property overrides the inherited one.

This works, and it costs something worth understanding. Once exceptions are allowed, the reasoning stops being deductive in the strict sense from the previous lessons. "Birds fly" no longer means every bird flies; it means birds typically fly, unless something more specific says otherwise. Adding the fact that Tweety is a penguin **retracts** the earlier conclusion that Tweety flies, and a logic in which new information can withdraw an old conclusion is called non-monotonic.

Ordinary first-order logic is monotonic: adding knowledge never removes a conclusion. Real-world knowledge is full of defaults and exceptions, so practical representations are non-monotonic and pay for it with a harder story about what their conclusions mean.

![Visual explanation of the inheritance exception problem](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/08_section_the_inheritance_exception_problem.png)

## Frames

A `frame` groups everything known about a concept into one named record with labelled `slots`, rather than scattering it across separate arrows.

```
Frame: Book
  is-a:            Library Item
  ISBN:            (required)
  author:          (required)
  loan period:     14 days        [default]
  renewable:       yes            [default]
  reservation fee: 0              [default]
```

```
Frame: Reference Book
  is-a:            Book
  loan period:     0 days         [overrides the default]
  renewable:       no             [overrides the default]
```

```
Frame: Midnight's Children
  instance-of:     Book
  ISBN:            978-0099578512
  author:          Salman Rushdie
```

Frames add three things beyond a plain semantic network.

1. **Grouping.** Everything about a book sits in one place, which matches how people actually think about categories and makes the knowledge far easier to maintain than arrows scattered across a graph.

2. **Defaults.** A slot can carry a typical value that applies unless overridden. A book is renewable unless it is a reference book. This is the exception mechanism from above, built into the representation rather than bolted on.

3. **Slots that trigger procedures.** A slot can hold code to run when its value is needed or changed, such as recalculating a due date whenever the loan period changes. This is exactly the declarative and procedural knowledge distinction from earlier in the unit, reconciled by letting one representation hold both.

Ask for the loan period of Midnight's Children and the system finds no value in the instance, follows instance-of to Book, and reports fourteen days. Ask the same of a reference book and the override answers zero. Nothing was stored twice.

![Visual explanation of frames](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/08_section_frames.png)

## Ontologies

An `ontology` goes further and specifies the vocabulary itself: what classes exist, what relationships are allowed between them, and what constraints must hold.

The difference from the previous two is a difference in ambition. A semantic network records what is true in one system. An ontology defines what it is possible to say, and is meant to be shared between systems.

A library ontology would state things like these.

- **Class hierarchy.** LibraryItem, with subclasses Book, Journal, and AudioVisual, and Book with subclass ReferenceBook.
- **Properties with types.** `writtenBy` connects a Book to an Author and to nothing else, so `writtenBy(Book, Shelf)` is not merely false, it is meaningless.
- **Cardinality constraints.** A Book has exactly one ISBN. A Loan has exactly one Borrower.
- **Axioms.** Every ReferenceBook has a loan period of zero. No item may be on loan to two borrowers at once.

Two consequences follow, and both are the point of the exercise.

**Consistency becomes checkable.** With constraints stated formally, a reasoner can detect that a record giving a book two ISBNs violates the ontology, without anyone writing a validation rule for that specific case.

**Systems can share meaning.** If the college library and the university library both use the same ontology, then `writtenBy` means the same thing in both, and their catalogues can be merged without a human deciding field by field what each column meant. This is the real motivation, and it is why ontologies matter far more in practice than their reputation as an academic exercise suggests.

![Visual explanation of ontology knowledge graph](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/08_ontology_knowledge_graph_context_v4.png)

## Knowledge Graphs

A `knowledge graph` is what these ideas became at industrial scale, and it is what produced the panel at the start of this lesson.

The representation is deliberately simple: everything is a `triple` of subject, predicate, object.

| Subject | Predicate | Object |
| --- | --- | --- |
| Sachin Tendulkar | instance-of | Cricketer |
| Cricketer | subclass-of | Sportsperson |
| Sportsperson | subclass-of | Person |
| Person | has-property | date of birth |
| Sachin Tendulkar | played-for | India |
| India | instance-of | Country |

Billions of such triples, and the same inheritance from before answers questions nobody stored directly. Asked for a cricketer's date of birth, the system follows the subclass chain to Person, finds that Persons have dates of birth, and looks for the value.

Three properties made this form win at scale.

- **Uniform shape.** Every fact is a triple, so one storage and query mechanism handles everything, and new relationship types need no schema change.
- **Merge by identity.** Two sources describing the same entity combine simply by agreeing on its identifier, which is how a knowledge graph is assembled from many databases.
- **Multi-hop queries.** Questions such as which players in this team were born in this state are answered by following two arrows, without a table having been designed in advance to support that particular question.

It is worth being honest about what knowledge graphs do not solve. They are populated by extracting facts from text and structured sources, and that extraction makes mistakes, so a large graph reliably contains a quantity of confident nonsense. Nothing in the representation detects a fact that is well-formed and untrue.

![Visual explanation of knowledge graphs](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/08_section_knowledge_graphs.png)

## The Three Models at a Glance

<table style="border-collapse: collapse; width: 100%; margin: 1rem 0; font-size: 0.95rem;">
  <thead>
    <tr>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Model</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Organised as</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Adds</th>
      <th style="border: 1px solid #c8d7ea; padding: 10px 12px; text-align: left; background-color: #dceeff; color: #102a43; font-weight: 700;">Best for</th>
    </tr>
  </thead>
  <tbody>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Semantic network</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Nodes joined by labelled arrows</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Inheritance along is-a links</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Showing how concepts relate</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Frames</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Named records of slots</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Grouping, defaults, and attached procedures</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Describing structured objects with typical values</td>
    </tr>
    <tr style="background-color: #ffffff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Ontology</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Formal classes, properties, and axioms</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Constraints, consistency checking, shared meaning</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Agreeing vocabulary across systems</td>
    </tr>
    <tr style="background-color: #f7fbff;">
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;"><strong>Knowledge graph</strong></td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Billions of subject-predicate-object triples</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Scale, easy merging, multi-hop queries</td>
      <td style="border: 1px solid #d8e2ef; padding: 9px 12px; vertical-align: top;">Search panels, assistants, recommendations</td>
    </tr>
  </tbody>
</table>

![Visual explanation of the three models at a glance](https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/images/08_section_the_three_models_at_a_glance.png)

## Your Turn

Build a semantic network for the vehicles in your neighbourhood, on paper, with at least twelve nodes.

Include the classes Vehicle, TwoWheeler, FourWheeler, Scooter, Motorcycle, Car, and Truck, and at least three specific vehicles you actually know as instances. Attach properties at the most general node where they belong: number of wheels, requires a licence, fuel type, whether a helmet is required. Then answer, by tracing arrows rather than by looking anything up, whether your neighbour's specific scooter requires a helmet.

Now find the exception. Put an electric scooter in your network and attach fuel type at the Vehicle node as petrol. Something is now wrong, and there are two ways to repair it: override fuel type at the electric scooter, or move the property to a lower node in the hierarchy. Do both, and write down which you prefer and why. There is no universally correct answer, and articulating the trade-off between a default with exceptions and a more precisely placed property is the actual skill.

Finally, convert five of your arrows into triples of subject, predicate, object, and then write in plain English a question that requires following two of your triples in sequence to answer. That two-hop question is what a knowledge graph does that a table of facts does not, and constructing one yourself is the fastest way to see why the search panel could exist at all.
