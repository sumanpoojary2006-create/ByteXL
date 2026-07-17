import random
import openpyxl

random.seed(41)

# (description, explanation, difficulty, bloom, subtopic, correct, [distractors])

ENTITIES_ATTRIBUTES_RELATIONSHIPS = [
    (
        "Kabir watches a student hand over two books and a library card. The librarian scans the card, scans each book, and notes the due date. Kabir jots down three words: student, book, librarian.\n\nWhat makes each of these worth calling an entity?",
        "Each is a distinct, real-world thing the library needs to remember details about over time, independently of anything else, and that can be told apart from every other instance of its own kind — exactly the definition of an entity.",
        "easy", "understand", "entities-attributes-relationships",
        "Each is a distinct real-world thing the system needs to track details about over time, independently and distinguishably from others of its kind",
        ["Each one appears somewhere in every sentence Kabir wrote down that afternoon", "Each one is a verb describing something happening in the library", "Each one is a property that describes some other, more important thing"],
    ),
    (
        "Kabir tests \"Reading\" as a candidate entity and rejects it, unlike Student, Book, and Librarian.\n\nWhy doesn't \"Reading\" qualify as its own entity?",
        "\"Reading\" is an activity a student does, not a distinct thing with its own identity worth tracking separately — it doesn't need its own set of facts remembered about it, separate from the things it involves, so it collapses into a relationship rather than standing alone as an entity.",
        "medium", "analyze", "entities-attributes-relationships",
        "It's an activity, not a distinct thing needing its own separately tracked facts — it collapses into a relationship instead",
        ["\"Reading\" is too short a word to qualify as an entity name", "The library has no interest in tracking reading habits at all", "Verbs can never appear anywhere in an ER model, under any role"],
    ),
    (
        "A Book entity has a title, an author, an ISBN, and a shelf location.\n\nWhat are these individual facts called, and what must always be true of one?",
        "These are attributes — individual facts that describe an entity. An attribute never floats free the way raw data can; it is always a property of some specific entity, which is exactly why the entity had to be identified first.",
        "easy", "remember", "entities-attributes-relationships",
        "Attributes — and each one must always be a property of some specific entity",
        ["Relationships — and each one must always connect two entities", "Constraints — and each one must always restrict a column's domain", "Cardinalities — and each one must always describe a count"],
    ),
    (
        "When Kabir watches the student borrow a book, he notices a fact — the borrow date — that belongs to neither the student alone nor the book alone, but ties one particular student to one particular book on one particular date.\n\nWhat does this borrowing connection, and the fact riding along with it, represent?",
        "This is a relationship — a meaningful association between two entities — and the borrow date is a fact that belongs to the relationship itself rather than to either entity alone, a distinction that matters once diagrams turn into working schemas.",
        "medium", "apply", "entities-attributes-relationships",
        "A relationship between Student and Book, with the borrow date as a fact belonging to that relationship itself",
        ["A third entity called Borrowing, with the borrow date as one of its ordinary attributes", "A composite attribute of the Book entity, describing when it was checked out", "A derived attribute of the Student entity, calculated from their membership date"],
    ),
    (
        "Kabir's rule of thumb for deciding whether a candidate noun deserves to be its own entity is a single question he asks about it.\n\nWhat is that question?",
        "He asks: does this need its own set of facts remembered about it, separate from the things it involves? If the answer is no, it usually collapses into an attribute or a relationship instead of standing on its own as an entity.",
        "medium", "understand", "entities-attributes-relationships",
        "Does this need its own set of facts remembered about it, separate from the things it involves?",
        ["Is this word a noun rather than a verb in the sentence describing it?", "Would drawing this as a rectangle look visually balanced on the page?", "Does the librarian mention this word more than once during a visit?"],
    ),
    (
        "Kabir's manager tells him the real work of database design happens before a single table gets created.\n\nIf Kabir's entity list is wrong from the start, what happens to everything built on top of it?",
        "Every attribute is always a property of some specific entity, so getting the entity list wrong means every attribute built on top of it inherits the same confusion — the whole design is only a faithful translation of the entities identified first.",
        "hard", "analyze", "entities-attributes-relationships",
        "Every attribute built on top of the wrong entities inherits the same confusion, since attributes are always properties of specific entities",
        ["Nothing changes; attributes can be freely reattached to any entity later at no cost", "Only the relationships are affected; attributes remain completely unaffected", "The database automatically corrects entity mistakes once real rows are inserted"],
    ),
]

TYPES_OF_ATTRIBUTES = [
    (
        "The gym's enrolment form asks for both \"age\" and \"date of birth.\" Whenever a member's birthday passes and nobody updates the age field by hand, the two values start contradicting each other.\n\nWhat attribute type should \"age\" actually be treated as, and why?",
        "Age is a derived attribute — it can always be computed from date of birth, so storing it separately as its own fact is not just unnecessary, it actively drifts out of truth every time a birthday passes without a manual update.",
        "easy", "understand", "types-of-attributes",
        "Derived — it can always be recalculated from date of birth rather than stored and maintained separately",
        ["Composite — it's built from smaller sub-parts like day, month, and year", "Multivalued — a member can have more than one age at once", "Simple — it's already as granular as the domain needs"],
    ),
    (
        "The gym's address field is squeezed into a single line, even though the gym genuinely needs to filter members by city separately for a new branch opening.\n\nWhat attribute type does this call for?",
        "Address is a composite attribute — built from smaller, meaningful sub-parts (street, city, pincode) that are each useful on their own, exactly why the gym needs city separately.",
        "easy", "understand", "types-of-attributes",
        "Composite — built from smaller meaningful sub-parts like street, city, and pincode",
        ["Derived — it can be calculated from a member's other stored facts", "Simple — it's already a single, indivisible value", "Multivalued — a member can have more than one address at once"],
    ),
    (
        "More than one gym member has written down two phone numbers in the margin, because the form only left room for one.\n\nWhat attribute type is phone number, given this behavior?",
        "Phone number is a multivalued attribute — a single entity instance (one member) can legitimately hold more than one value for this property at the same time, exactly what the cramped one-line form failed to accommodate.",
        "easy", "remember", "types-of-attributes",
        "Multivalued",
        ["Composite", "Derived", "Simple"],
    ),
    (
        "What test does Meera learn to apply for deciding whether an attribute like address should be treated as composite rather than left as one indivisible value?",
        "The test is whether the pieces are ever useful on their own — if the gym never once needs to query \"which members live in which city\" without also needing the full address, breaking it apart would be unnecessary detail.",
        "medium", "apply", "types-of-attributes",
        "Whether the sub-parts are ever needed on their own, independent of the whole attribute",
        ["Whether the attribute's value is longer than ten characters", "Whether the attribute appears in more than one entity", "Whether the attribute was originally entered by a human rather than a system"],
    ),
    (
        "A book having several authors, and a car being available in several colours, are both mentioned as examples of the same attribute type as a gym member's phone numbers.\n\nWhat is that shared attribute type?",
        "All of these are multivalued attributes — cases where a single entity instance can hold more than one value of the same property at the same time, breaking the usual \"one entity, one value\" assumption.",
        "medium", "apply", "types-of-attributes",
        "Multivalued attributes",
        ["Composite attributes", "Derived attributes", "Simple attributes"],
    ),
    (
        "Why is storing a derived attribute like age described as \"actively dangerous\" rather than merely \"unnecessary\"?",
        "Because the stored value slowly drifts out of truth every time the source fact changes (a birthday passes) without anyone remembering to update the derived copy — it doesn't just waste space, it silently becomes wrong over time.",
        "hard", "analyze", "types-of-attributes",
        "The stored value silently drifts out of truth over time whenever the source attribute changes and nobody updates it",
        ["It's dangerous only because it takes up more storage space than date of birth", "It's dangerous because derived attributes are always illegal in a relational database", "It's dangerous because it can never be recalculated once the source attribute is deleted"],
    ),
]

RELATIONSHIP_CARDINALITY = [
    (
        "At Rohan's company, every employee is assigned exactly one desk, and every desk is assigned to exactly one employee. No desk is shared, and no employee has a second desk.\n\nWhat cardinality does the Employee-Desk relationship have?",
        "This is a one-to-one relationship: one instance of each entity is associated with exactly one instance of the other, and vice versa.",
        "easy", "remember", "relationship-cardinality",
        "One-to-one",
        ["One-to-many", "Many-to-many", "Zero-to-one"],
    ),
    (
        "One department can have many employees working in it, but any single employee belongs to exactly one department.\n\nWhat cardinality is this, and what asymmetry gives it away?",
        "This is one-to-many. Read from the department's side, the answer to \"how many employees\" is \"many\"; read from an employee's side, the answer to \"how many departments\" is \"exactly one\" — that asymmetry is the entire definition of one-to-many.",
        "medium", "understand", "relationship-cardinality",
        "One-to-many — the department side allows many, but the employee side is capped at exactly one",
        ["One-to-one — both sides are capped at exactly one", "Many-to-many — both sides allow many", "This relationship has no defined cardinality at all"],
    ),
    (
        "One student can enrol in several courses in a semester, and one course, naturally, has many students sitting in it.\n\nWhat cardinality is the Student-Course relationship, and what makes it the trickiest of the three shapes?",
        "This is many-to-many — unlike one-to-many, there is no side here that can be pinned down to \"exactly one\"; both directions genuinely allow more than one connection, which makes it harder to represent later as a table structure.",
        "medium", "apply", "relationship-cardinality",
        "Many-to-many — neither side can be pinned down to exactly one connection",
        ["One-to-many — only courses can have many students", "One-to-one — each student takes exactly one course per semester", "None of these; students and courses cannot have a defined cardinality"],
    ),
    (
        "Rohan's manager insists on never describing a relationship's cardinality from only one side, such as saying only \"a department has employees.\"\n\nWhy does stating both directions matter?",
        "Getting into the habit of stating both directions out loud, \"one department to many employees, one employee to one department,\" is what prevents a design from silently sliding into the wrong cardinality further down the line.",
        "medium", "analyze", "relationship-cardinality",
        "Stating both directions prevents a design from silently sliding into the wrong cardinality",
        ["It matters only for documentation style, with no effect on the actual design", "Describing only one side is always sufficient, since the other side is implied automatically", "It matters only for many-to-many relationships, never for one-to-many"],
    ),
    (
        "What goes wrong, concretely, if a one-to-many relationship like Department-Employees is mistakenly modeled as one-to-one?",
        "The finished system will reject a perfectly legitimate department that happens to have three employees rather than one, since a one-to-one model assumes only a single match is ever allowed on each side.",
        "hard", "analyze", "relationship-cardinality",
        "The system will reject a legitimate department that has more than one employee",
        ["The system will silently duplicate every employee row three times", "Nothing goes wrong; one-to-one and one-to-many behave identically in practice", "The system will allow a department to have unlimited employees instead of just one"],
    ),
    (
        "The lesson insists that cardinality \"is not a detail to sort out after the design is finished, it is a decision that shapes the design itself.\"\n\nWhat does this mean in practical terms?",
        "How a relationship eventually gets stored, a single reference, a foreign key on one side, or an entirely new table, depends directly on getting the cardinality right from the start; mislabeling it produces a system that rejects legitimate real-world data rather than a system that's merely inconvenient.",
        "hard", "understand", "relationship-cardinality",
        "How a relationship is eventually stored depends directly on its cardinality being identified correctly from the start",
        ["Cardinality only affects how a diagram looks visually, not how the database is actually built", "Cardinality can always be changed later with no consequences to the stored data", "Cardinality only matters for many-to-many relationships, never for the other two shapes"],
    ),
]

PARTICIPATION_CONSTRAINTS = [
    (
        "Aisha's manager asks: \"Can an order exist without a customer attached to it?\"\n\nWhat does Aisha conclude, and what participation type does this describe for Orders in the Customer-Orders relationship?",
        "No — every order in the system must belong to some customer, with no concept of an order floating free. This is total participation: every single instance of the Orders entity is required to take part in the relationship.",
        "easy", "understand", "participation-constraints",
        "No, an order cannot exist without a customer — this is total participation for Orders",
        ["Yes, orders can exist independently — this is partial participation for Orders", "No, but this describes cardinality, not participation, so the question doesn't apply", "Yes, but only if the order has already been shipped"],
    ),
    (
        "Can a customer exist who has never placed a single order? Aisha's manager confirms the answer is yes — someone who created an account, browsed a little, and never checked out.\n\nWhat participation type does this describe for Customers in the same relationship?",
        "This is partial participation: instances of the Customers entity are allowed to exist whether or not they take part in the Orders relationship, and a customer with zero orders is a perfectly valid, normal state.",
        "easy", "understand", "participation-constraints",
        "Partial participation — a customer may validly exist with zero orders",
        ["Total participation — every customer must place at least one order", "This describes cardinality, not participation", "This is undefined, since customers with no orders shouldn't be allowed in the system"],
    ),
    (
        "In a hospital's Doctors-Patients \"Admits\" relationship, every currently admitted patient must have been admitted by some doctor, but a doctor on staff might currently have zero admitted patients.\n\nWhich side has total participation, and which has partial?",
        "Patients has total participation (every admitted patient must have an admitting doctor), while Doctors has partial participation (a doctor may currently have zero admitted patients, perhaps between cases).",
        "medium", "apply", "participation-constraints",
        "Patients has total participation; Doctors has partial participation",
        ["Doctors has total participation; Patients has partial participation", "Both Doctors and Patients have total participation", "Both Doctors and Patients have partial participation"],
    ),
    (
        "Why does participation constraint deserve its own name and concept, rather than being folded directly into cardinality?",
        "Cardinality answers \"how many,\" while participation answers \"is it required at all\" — a relationship can be one-to-many with total participation on one side and partial on the other, exactly like Customers and Orders, meaning the two facts are genuinely separate and both are needed to fully describe a relationship.",
        "medium", "analyze", "participation-constraints",
        "Cardinality answers \"how many\"; participation answers \"is it required at all\" — two genuinely separate facts about a relationship",
        ["Participation is really just another name for cardinality, used interchangeably", "Participation only applies to many-to-many relationships, unlike cardinality", "Cardinality already fully determines participation, so tracking both is redundant"],
    ),
    (
        "What would it mean, in real business terms, if the store insisted that every customer must have at least one order — that is, if Customers had total participation in the Customer-Orders relationship?",
        "It would force every new signup to place an order the instant they register, which does not match how the business actually works, since browsing without buying is a completely normal customer state.",
        "medium", "apply", "participation-constraints",
        "It would force every new signup to place an order the instant they register, which doesn't match real business behavior",
        ["It would have no practical effect on how the business operates day to day", "It would mean customers could no longer be deleted from the database", "It would mean every order would need to reference more than one customer"],
    ),
    (
        "Aisha learns to check participation \"from both sides, separately,\" the same habit she learned for cardinality.\n\nWhy can't participation be assumed to be symmetrical across both sides of a relationship?",
        "The two sides are almost never symmetrical — every order needs a customer (total participation) but a customer doesn't need an order (partial participation). Mixing the two up leads directly to a design that is too strict on one side or too loose on the other.",
        "hard", "analyze", "participation-constraints",
        "The two sides are almost never symmetrical, and mixing them up produces a design that's too strict on one side or too loose on the other",
        ["Participation is always identical on both sides by mathematical necessity", "Only cardinality can differ between sides; participation is always fixed at total for both", "Checking both sides is only a documentation habit with no effect on the actual design"],
    ),
]

ER_DIAGRAM_NOTATION = [
    (
        "In Vivek's ER diagram, a rectangle is labelled \"Patient,\" ovals hang off it labelled \"Patient ID\" and \"Name,\" and a diamond labelled \"Admits\" sits between Patient and a second rectangle labelled \"Doctor.\"\n\nWhat does each of these three shapes represent?",
        "A rectangle represents an entity, an oval represents an attribute describing the entity it's attached to, and a diamond represents a relationship, the meaningful connection between the two entities it touches.",
        "easy", "remember", "er-diagram-notation",
        "Rectangle = entity, oval = attribute, diamond = relationship",
        ["Rectangle = attribute, oval = entity, diamond = relationship", "Rectangle = relationship, oval = entity, diamond = attribute", "Rectangle = entity, oval = relationship, diamond = attribute"],
    ),
    (
        "\"Patient ID\" appears underlined inside its oval, while \"Name\" does not.\n\nWhat does the underline signify?",
        "The underlined label marks the identifying attribute, the one that plays the role of uniquely picking out one instance of the entity.",
        "easy", "understand", "er-diagram-notation",
        "It marks the identifying attribute of the entity",
        ["It marks an attribute that is currently empty for every row", "It marks a derived attribute calculated from another value", "It marks an attribute that belongs to more than one entity at once"],
    ),
    (
        "A dashed oval outline and a double-lined oval outline mean two different things in an ER diagram.\n\nWhich is which, and why does each get its own distinct visual treatment?",
        "A dashed outline marks a derived attribute, a quiet visual reminder that the value is calculated rather than stored. A double-lined outline marks a multivalued attribute, signalling that a single entity instance can carry more than one value there.",
        "medium", "apply", "er-diagram-notation",
        "Dashed = derived attribute (calculated, not stored); double-lined = multivalued attribute (can hold more than one value)",
        ["Dashed = multivalued attribute; double-lined = derived attribute", "Both symbols mean the same thing: an optional attribute that may be left blank", "Dashed = composite attribute; double-lined = the primary key"],
    ),
    (
        "In Vivek's hospital diagram, the line between Patient and the Admits diamond is doubled, while the line between Doctor and the same diamond stays single.\n\nWhat does this specific pair of lines communicate?",
        "The doubled line shows total participation for Patient (every admitted patient must have an admitting doctor), while the single line shows partial participation for Doctor (a doctor may currently have zero admitted patients).",
        "medium", "analyze", "er-diagram-notation",
        "Total participation for Patient (doubled line) and partial participation for Doctor (single line)",
        ["Total participation for Doctor and partial participation for Patient", "One-to-many cardinality, with Patient on the \"many\" side", "A composite relationship formed from two separate sub-relationships"],
    ),
    (
        "Two different conventions exist for showing cardinality on the lines connecting an entity to a relationship diamond.\n\nWhat are they?",
        "The first labels the line directly with \"1\" or \"N\" (sometimes \"M\") at each end. The second, popular in more polished diagramming tools, uses a crow's foot mark to mean \"many\" and a single tick mark to mean \"one.\"",
        "medium", "remember", "er-diagram-notation",
        "The \"1\"/\"N\" label convention, and the crow's-foot convention",
        ["The dashed-line convention, and the double-oval convention", "The rectangle-color convention, and the diamond-size convention", "The underline convention, and the bold-text convention"],
    ),
    (
        "Vivek's manager insists on a small, fixed set of shapes used the exact same way every time, rather than letting each diagram improvise its own symbols.\n\nWhy does this discipline matter?",
        "Reusing the same shape for the same kind of idea every single time is what makes a diagram readable to a stranger — a rectangle always means the same thing no matter who drew it, letting a trained reader understand a design without the original designer narrating it.",
        "hard", "analyze", "er-diagram-notation",
        "Reusing the same shape consistently for the same idea is what makes the diagram readable to anyone trained in the notation, without narration",
        ["It matters only for aesthetic consistency across a company's internal documents", "It matters because diagramming software cannot render more than three distinct shapes", "It has no real benefit; each designer's personal notation works just as well"],
    ),
]

ER_TO_RELATIONAL_MAPPING = [
    (
        "Naina's ER diagram has a rectangle labelled \"Student\" with attributes Roll Number (underlined), Name, and Date of Birth.\n\nWhat does this rectangle become in the relational design, and what becomes of the underlined attribute?",
        "The rectangle becomes a Students table, and every simple attribute becomes a column. The underlined (identifying) attribute, Roll Number, becomes the table's primary key.",
        "easy", "understand", "er-to-relational-mapping",
        "A Students table, with Roll Number as its primary key",
        ["A Students table, with Name as its primary key", "A junction table linking Students to Courses", "No table at all; rectangles only describe relationships, not entities"],
    ),
    (
        "The Instructor-teaches-Course relationship is one-to-many: one instructor teaches several courses, but each course has exactly one instructor.\n\nHow does this relationship get represented in the relational tables?",
        "A foreign key column (Instructor ID) is added to the Courses table, the \"many\" side of the relationship — the entity on the \"many\" side always carries the foreign key pointing at the \"one\" side, never the other way round.",
        "medium", "apply", "er-to-relational-mapping",
        "A foreign key column is added to Courses (the \"many\" side), pointing back to Instructors (the \"one\" side)",
        ["A foreign key column is added to Instructors, pointing back to Courses", "A brand new junction table is created to link Instructors and Courses", "No new column is needed; the relationship is left implicit"],
    ),
    (
        "Why would placing the foreign key on the \"one\" side (Instructors) instead of the \"many\" side (Courses) fail to represent an instructor teaching more than one course?",
        "A single column can only ever hold one value per row, so an Instructors row could only reference a single course — it could never represent an instructor connected to several courses at once, which is exactly what the one-to-many relationship requires.",
        "hard", "analyze", "er-to-relational-mapping",
        "A single column in a single row can only hold one value, so it couldn't represent an instructor linked to multiple courses",
        ["It would fail because Instructors already has too many columns to add one more", "It would actually work fine; either side could hold the foreign key with identical results", "It would fail because foreign keys are never allowed to point from a \"one\" side table"],
    ),
    (
        "The Student-enrols-in-Course relationship is many-to-many.\n\nWhat does this become in the relational design, and why can't a single foreign key column in either Students or Courses handle it?",
        "It becomes a brand new junction (associative) table holding a foreign key pointing to Students and another pointing to Courses. Neither the Students table nor the Courses table can hold a single foreign key column for this relationship, because a single column in a single row cannot represent \"several\" values at once.",
        "medium", "understand", "er-to-relational-mapping",
        "A new junction table with a foreign key to each side, since a single column can't represent multiple connections in either direction",
        ["A single new column added to whichever table has fewer rows", "A foreign key added to both Students and Courses, each pointing at the other", "Nothing new; many-to-many relationships require no additional structure"],
    ),
    (
        "For a one-to-one relationship, such as an employee and their assigned desk, where does the lesson say the foreign key is usually placed, and what extra constraint does it typically need?",
        "The usual choice is to place the foreign key on whichever side has total participation, and to mark that column unique, so the database itself refuses to let the same desk end up assigned to two different employees.",
        "medium", "apply", "er-to-relational-mapping",
        "On the side with total participation, marked unique so the database prevents the same value being reused",
        ["On the side with the most rows, with no additional constraint needed", "On both sides simultaneously, each marked as a primary key", "It's placed randomly, since either side works identically for one-to-one relationships"],
    ),
    (
        "Naina's finished conversion produces four tables (Students, Courses, Instructors, Enrolments) from three rectangles and two diamonds in her original diagram.\n\nWhich table exists that never corresponded to a rectangle at all, and why does it exist?",
        "The Enrolments table exists purely because the many-to-many Student-enrols-in-Course diamond needed somewhere to live — unlike the one-to-many Instructor-teaches-Course relationship, which only added an extra column rather than a whole new table.",
        "hard", "analyze", "er-to-relational-mapping",
        "The Enrolments table — it exists purely because a many-to-many relationship needed a junction table to hold it",
        ["The Courses table — it exists purely because of the Instructor-teaches-Course relationship", "The Students table — it exists purely to hold the Roll Number attribute", "No table exists without a corresponding rectangle; every table traces back to an entity"],
    ),
]

SYNTHESIS = [
    (
        "The Customer-Orders relationship is one-to-many (a customer can place many orders, each order has exactly one customer). Separately, every order must have a customer, but a customer may have zero orders.\n\nWhich combination correctly describes both the cardinality and the participation of this relationship?",
        "Cardinality is one-to-many. Participation is total for Orders (every order must have a customer) and partial for Customers (a customer may have zero orders) — cardinality and participation are two separate facts that must each be checked.",
        "medium", "analyze", "participation-constraints",
        "One-to-many cardinality; Orders has total participation, Customers has partial participation",
        ["Many-to-many cardinality; both sides have total participation", "One-to-one cardinality; Orders has partial participation, Customers has total participation", "One-to-many cardinality; both sides have partial participation"],
    ),
    (
        "An Address attribute is drawn in an ER diagram as an oval with three smaller ovals branching off it: Street, City, and Pincode.\n\nWhen this diagram is converted into relational tables, what does this composite attribute become?",
        "A composite attribute becomes several separate columns in the entity's table, one per component part — Street, City, and Pincode each become their own column, rather than one combined field.",
        "medium", "apply", "er-to-relational-mapping",
        "Three separate columns in the table: Street, City, and Pincode",
        ["A single column holding all three values separated by commas", "A brand new junction table linking the entity to each address component", "No column at all, since composite attributes are always derived and never stored"],
    ),
    (
        "In the ER diagram legend, total participation is shown with a double line from an entity to a diamond, and a multivalued attribute is shown with a double-lined oval outline.\n\nEven though both use \"doubling\" as a visual cue, what different underlying ideas do they represent?",
        "A double line between entity and diamond represents total participation — every instance must take part in the relationship. A double-lined oval represents a multivalued attribute — a single instance can hold more than one value for that attribute. Same visual device, two unrelated concepts.",
        "hard", "analyze", "er-diagram-notation",
        "Double line to a diamond means total participation; a double-lined oval means a multivalued attribute — same visual style, different meanings",
        ["Both symbols mean exactly the same thing: an attribute that is required for every row", "The double line always refers to cardinality, and the double oval always refers to participation", "Neither symbol has any defined meaning; doubling is purely decorative in ER notation"],
    ),
    (
        "Kabir identifies \"Student borrows Book\" as involving two entities and a relationship. Suppose that relationship turns out to be many-to-many, since a student can borrow many books over time and a book can be borrowed by many different students over time.\n\nWhat would the relational mapping ultimately require?",
        "A many-to-many relationship always requires a new junction table, here perhaps BorrowRecords, holding a foreign key pointing to Student and another pointing to Book, since neither entity's table alone can hold a single foreign key column representing multiple connections.",
        "hard", "apply", "er-to-relational-mapping",
        "A new junction table (e.g. BorrowRecords) with a foreign key to Student and a foreign key to Book",
        ["A single new column added directly to the Book table pointing at Student", "A single new column added directly to the Student table pointing at Book", "No new table; the borrow date attribute alone is sufficient to represent the relationship"],
    ),
]

SET1_SOURCES = [
    (ENTITIES_ATTRIBUTES_RELATIONSHIPS, 0),
    (TYPES_OF_ATTRIBUTES, 0),
    (RELATIONSHIP_CARDINALITY, 0),
    (PARTICIPATION_CONSTRAINTS, 0),
    (ER_DIAGRAM_NOTATION, 0),
    (ER_TO_RELATIONAL_MAPPING, 0),
]

SET1 = [src[idx] for src, idx in SET1_SOURCES]
SET1.extend(SYNTHESIS)

SET2 = (
    ENTITIES_ATTRIBUTES_RELATIONSHIPS[1:]
    + TYPES_OF_ATTRIBUTES[1:]
    + RELATIONSHIP_CARDINALITY[1:]
    + PARTICIPATION_CONSTRAINTS[1:]
    + ER_DIAGRAM_NOTATION[1:]
    + ER_TO_RELATIONAL_MAPPING[1:]
)

assert len(SET1) == 10, len(SET1)
assert len(SET2) == 30, len(SET2)


def build_rows(items, set_label, title_prefix):
    positions = [(i % 4) + 1 for i in range(len(items))]
    random.shuffle(positions)

    rows = []
    for idx, (desc, expl, diff, bloom, subtopic, correct, distractors) in enumerate(items, start=1):
        pos = positions[idx - 1]
        options = distractors[:]
        options.insert(pos - 1, correct)
        rows.append({
            "title": f"{title_prefix}.{idx}",
            "description": desc,
            "explanation": expl,
            "score": 1,
            "status": "published",
            "difficulty": diff,
            "bloomTaxonomy": bloom,
            "tags": f"dbms - {set_label}",
            "subjects": "dbms",
            "topics": "database-design-and-modeling",
            "subTopics": subtopic,
            "companies": None,
            "option1": options[0],
            "option2": options[1],
            "option3": options[2],
            "option4": options[3],
            "answer": pos,
        })
    return rows


rows1 = build_rows(SET1, "Set 1", "DBMS - MCQ - 2.1.1")
rows2 = build_rows(SET2, "Set 2", "DBMS - MCQ - 2.1.2")
all_rows = rows1 + rows2


def summarize(name, rs):
    diff, bloom, sub, ans = {}, {}, {}, {1: 0, 2: 0, 3: 0, 4: 0}
    for r in rs:
        diff[r["difficulty"]] = diff.get(r["difficulty"], 0) + 1
        bloom[r["bloomTaxonomy"]] = bloom.get(r["bloomTaxonomy"], 0) + 1
        sub[r["subTopics"]] = sub.get(r["subTopics"], 0) + 1
        ans[r["answer"]] += 1
    print(name, "diff:", diff)
    print(name, "bloom:", bloom)
    print(name, "subtopics:", sub)
    print(name, "answers:", ans)


summarize("SET1", rows1)
summarize("SET2", rows2)

descs = [r["description"] for r in all_rows]
assert len(descs) == len(set(descs)), "duplicate description found"
for r in all_rows:
    opts = [r["option1"], r["option2"], r["option3"], r["option4"]]
    assert len(set(opts)) == 4, f"duplicate option in {r['title']}: {opts}"

headers = ["title", "description", "explanation", "score", "status", "difficulty", "bloomTaxonomy",
           "tags", "subjects", "topics", "subTopics", "companies",
           "option1", "option2", "option3", "option4", "answer"]

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "DBMS - MCQ - Unit 2.1"
ws.append(headers)
for r in all_rows:
    ws.append([r[h] for h in headers])

out_path = "content/Question Bank/MCQ/DBMS/Unit 2 - Database Design and Modeling/2.1 - Entity-Relationship Modeling - MCQ.xlsx"
wb.save(out_path)
print("Saved", out_path, "with", len(all_rows), "questions")
