import random
import openpyxl

random.seed(17)

# (description, explanation, difficulty, bloom, subtopic, correct, [distractors])
SET1 = [
    # 1.1.1 Easy — programming-fundamentals (what is programming)
    (
        "A warehouse robot's engineering team is deciding whether a task counts as 'programming' or just a one-time manual override. A technician walks up to the robot and manually pushes it three metres to the left, one time, to avoid a spill. Separately, another engineer writes a rule that runs every day: 'if a spill sensor reading exceeds 0.4, reverse the robot 3 metres and pause for 10 seconds.' Which of these is programming, and why?",
        "Programming is the act of specifying a repeatable, unambiguous set of instructions that a machine can carry out on its own, for any future situation matching the condition. The one-time manual push is a direct human action, not an instruction set the robot will reuse. The written rule is a program: precise, conditional, and repeatable — that's the definition of programming, and it doesn't require Python syntax specifically.",
        "easy", "understand", "programming-fundamentals",
        "Only the written rule — programming means giving a machine precise, repeatable instructions it can execute on its own",
        ["Only the manual push — programming refers to any physical, hands-on adjustment made directly to a machine's current behaviour", "Both — any action at all that changes what the robot does counts as programming, whether typed or done by hand", "Neither — programming only applies narrowly to writing Python syntax, not to general step-by-step instructions"],
    ),
    # 1.1.2 Medium — programming-fundamentals (IPO)
    (
        "A fitness wearable reads a wearer's heart rate every second from its sensor, runs it through a calibration formula that accounts for the wearer's age and weight to estimate calories burned, and updates the number shown on the wrist display. A firmware reviewer is labelling each part of this pipeline using the Input-Processing-Output model. Which part does the calibration formula belong to?",
        "The heart-rate reading from the sensor is the input. Applying the calibration formula to convert that raw reading into an estimated calorie count is processing — using input to derive a result. Updating the wrist display with that number is the output. The formula runs continuously each second here, not just once at setup, so it isn't outside the model.",
        "medium", "apply", "programming-fundamentals",
        "Processing — it transforms the raw sensor reading into a usable result before anything is shown",
        ["Input — the formula is where data first enters the system", "Output — the formula produces the final calorie number that matters to the user", "None of the three — calibration formulas sit outside the IPO model since they run only once at setup"],
    ),
    # 1.1.3 Medium — computational-thinking
    (
        "An airport is designing a new baggage-sorting system. The engineering lead breaks the problem into smaller pieces: scanning tags, routing bags to the correct carousel, and flagging bags with no readable tag. She does not, however, look at how the sorting logic for connecting flights is similar to the logic already used for direct flights, and ends up writing the connecting-flight sorter completely from scratch. Which computational thinking skill was skipped?",
        "Decomposition did happen — the problem was broken into scanning, routing, and flagging. Pattern recognition is about spotting similarities between problems so existing solutions can be reused; that step was skipped here, forcing the connecting-flight logic to be built from scratch rather than adapted from the direct-flight version. There's no indication abstraction or algorithm design were mishandled.",
        "medium", "analyze", "computational-thinking",
        "Pattern recognition — missed reusing similar connecting-flight and direct-flight logic",
        ["Decomposition — breaking the problem into scanning, routing, and flagging was never done", "Abstraction — she included too many low-level scanner details in the design", "Algorithm design — no step-by-step sorting procedure was ever created for any flight type"],
    ),
    # 1.1.4 Hard — computational-thinking (abstraction)
    (
        "A technician is designing a monitoring tool to flag underperforming solar panels. Instead of just checking a panel's power output against an expected range, the tool's first version tracks the exact wiring gauge, the manufacturer's internal cell layout, and the precise ambient dust particle count for every panel before deciding anything. The tool becomes too slow and complicated to run daily. What computational thinking principle is being violated?",
        "Abstraction means keeping only the details relevant to the problem and hiding the rest. Wiring gauge, internal cell layout, and precise dust counts are far more detail than needed to flag underperformance from power output alone. This over-inclusion of irrelevant detail — not a lack of decomposition or algorithm design — is what makes the tool slow and unwieldy.",
        "hard", "analyze", "computational-thinking",
        "Abstraction — tracking far more low-level detail than the problem actually needs",
        ["Decomposition — the problem has not been broken down into smaller sub-tasks at all", "Pattern recognition — the tool fails to notice that all panels behave identically", "Algorithm design — the tool has no defined sequence of steps to follow"],
    ),
    # 1.1.5 Medium — algorithms-and-pseudocode (problem solving stage)
    (
        "A vending-machine company's field technician has been asked to fix machines that are frequently running out of popular snacks. Before touching any restocking schedule, she spends a day pulling sales logs from every machine to see which items actually sell fastest at which locations. Which stage of the problem-solving approach is she in?",
        "Studying sales logs to understand what's actually happening — before designing any restocking schedule — is the 'understand the problem' stage. No plan has been devised yet, nothing is being executed, and there's no described prior solution being reviewed.",
        "medium", "understand", "algorithms-and-pseudocode",
        "Understand the problem — studying data before deciding on a solution",
        ["Devise a plan — she is already designing the new restocking schedule", "Carry out the plan — she is executing the fix by analysing the machines directly", "Review the solution — she is checking whether a previous fix worked"],
    ),
    # 1.1.6 Hard — algorithms-and-pseudocode (finiteness)
    (
        "An engineer writes the following steps for an elevator's dispatch algorithm:\n\n1. Wait for a floor request.\n2. Move toward the requested floor.\n3. If a new request comes in from a closer floor, switch to that floor instead.\n4. Go back to step 1.\n\nA reviewer flags this as not being a valid algorithm in the strict sense, even though it seems to describe reasonable elevator behaviour. What is the issue?",
        "One of the defining properties of an algorithm is finiteness — it must terminate after a finite number of steps. This description loops back to step 1 forever with no exit condition, so, strictly, it isn't finite. Real elevator control systems run as an ongoing service rather than a single terminating algorithm, but the reviewer is correctly pointing out that this doesn't meet the formal definition. It does have an input (the floor request), and conditional steps are completely normal in algorithms.",
        "hard", "analyze", "algorithms-and-pseudocode",
        "It never terminates — step 4 loops back to step 1 forever",
        ["It has no input, so it cannot be considered an algorithm", "Step 3 uses a condition, and algorithms cannot contain conditional steps", "There is no issue — this is a perfectly valid, finite algorithm as written"],
    ),
    # 1.1.7 Medium — flowcharts (shape swap)
    (
        "A ride-hailing app's surge-pricing logic is drawn as a flowchart. The diagram uses a rectangle to ask 'Is demand greater than supply?' and a diamond to perform the action 'Apply 1.5x surge multiplier.' A reviewer says the diagram is drawn incorrectly. What is wrong?",
        "In standard flowchart convention, a diamond represents a decision point (a yes/no or true/false question), and a rectangle represents a processing step or action. Here they've been swapped — the question is in a rectangle and the action is in a diamond. Ovals conventionally represent start/end points, and parallelograms represent input/output, not decisions.",
        "medium", "understand", "flowcharts",
        "The shapes are swapped — decisions need a diamond, actions need a rectangle",
        ["Nothing is wrong — rectangles and diamonds are interchangeable in flowcharts", "The surge multiplier should be an oval, since ovals represent all calculations", "The decision should be a parallelogram, since parallelograms represent all yes/no questions"],
    ),
    # 1.1.8 Hard — flowcharts (loop-back tracing)
    (
        "A parking garage's entry-barrier flowchart works as follows: a car approaches, the system checks if there's an available spot. If yes, it opens the barrier and lets the car in. If no, it displays 'Garage Full' and loops back to re-check availability every 10 seconds, repeating until a spot opens or the car leaves. A car arrives when the garage is full, and a spot opens up 30 seconds later, with the car still waiting. What does the flowchart do?",
        "The loop-back branch means the system doesn't just check once — it rechecks on a fixed interval as long as the car is still waiting, and proceeds to open the barrier as soon as a check finds an available spot. It isn't a dead end because of the loop back to the recheck step, and the barrier only opens based on an actual availability check, not merely because 30 seconds passed.",
        "hard", "apply", "flowcharts",
        "It keeps re-checking every 10 seconds and opens the barrier once a spot is found — no re-approach needed",
        ["It displays 'Garage Full' once and never rechecks, so the car is stuck until it manually retries", "It opens the barrier immediately once 30 seconds have passed, regardless of whether a spot is actually available", "The flowchart has no way to eventually let the car in, since 'Garage Full' is a dead end"],
    ),
    # 1.1.9 Hard — python-overview (trade-off)
    (
        "A team is choosing a language for two separate projects: (1) a data-analysis pipeline that cleans and summarizes millions of survey rows using well-supported libraries, and (2) firmware for a coin-sized heart-rate sensor with under 2KB of memory and no operating system. One engineer suggests using Python for both, citing its readability and huge ecosystem. Where does this reasoning break down?",
        "Python's readability and library ecosystem (pandas, etc.) make it a strong fit for the data pipeline. But Python requires an interpreter and a meaningful memory footprint to run — something a 2KB, no-OS embedded sensor cannot accommodate. This is precisely why languages like C are typically used for such firmware. Python is commonly and effectively used for large-scale data analysis, so rejecting it there is also incorrect, and readability doesn't change hardware memory constraints.",
        "hard", "analyze", "python-overview",
        "Python suits the data pipeline, but the 2KB sensor firmware can't support an interpreter",
        ["It doesn't break down — Python's interpreter can run on any device regardless of memory constraints", "Python is unsuitable for both, since data-analysis pipelines require a compiled language for acceptable performance", "Python is better suited to the firmware, since its readability makes it easier to debug on constrained hardware"],
    ),
    # 1.1.10 Medium — python-environment (syntax error, caught before running)
    (
        "A restaurant's self-order kiosk runs a small first-version Python script to display the daily order number. A junior developer writes:\n\n```python\norder_number = 42\nprint(\"Your order number is: + order_number)\n```\n\nWhen the kiosk starts up, nothing displays and the terminal shows an error before the program even begins running normally. What kind of problem is this, and when is it caught?",
        "The missing closing quote after `\"Your order number is: ` means Python cannot correctly parse the line at all — this is a syntax error, and syntax errors are caught before the program starts executing, not partway through. A runtime error would require the code to be syntactically valid and fail while running; a logic error would mean it runs and gives a wrong-but-plausible result. Neither applies here since the program never starts.",
        "medium", "apply", "python-environment",
        "A syntax error — the missing quote means Python can't parse the code at all",
        ["A runtime error — the code parses fine but crashes partway through execution when it tries to add a number to a string", "A logic error — the code runs completely and produces the wrong order number", "This is not an error at all — kiosks are expected to fail silently on their first run"],
    ),
]

SET2 = [
    # 1.2.1 Easy — programming-fundamentals (IPO, red herring)
    (
        "An ATM accepts a withdrawal amount typed by a customer, checks it against the account balance and note availability, dispenses the requested cash, and also prints a paper receipt showing the new balance — though the customer often doesn't take the receipt. In the Input-Processing-Output model, what is the output of this system?",
        "Output is whatever the system produces as a result after processing, regardless of whether the customer engages with all of it. Both the dispensed cash and the printed receipt are outputs. Whether a customer takes the receipt has no bearing on whether it counts as output. The typed amount is the input, and the balance/note check is processing, not output.",
        "easy", "understand", "programming-fundamentals",
        "The dispensed cash and the printed receipt — both are outputs of the system",
        ["Only the dispensed cash — the receipt does not count because customers frequently ignore it", "The typed withdrawal amount, since that is what triggers the entire transaction", "The balance check against note availability, since that is the final step before cash is released"],
    ),
    # 1.2.2 Medium — programming-fundamentals (missing input dependency)
    (
        "A logistics team builds a delivery-route planner that is supposed to calculate the shortest route using the current traffic conditions. A developer writes the processing logic to compute the shortest path, but never wires in a live traffic feed — the system just uses straight-line distance between stops. Deliveries keep getting routed through streets that are actually jammed. What is the root cause, described in Input-Processing-Output terms?",
        "Processing can only work with the inputs it's given. If live traffic was never captured as an input, no amount of correct routing logic can account for it — the shortest-path calculation is working exactly as designed, just on incomplete input. The output display isn't the problem, and traffic conditions being 'external' doesn't exempt them from needing to be captured as an input if the system depends on them.",
        "medium", "analyze", "programming-fundamentals",
        "A required input, live traffic data, was never captured, so processing can't account for it here",
        ["The processing logic itself is flawed and needs a different shortest-path algorithm", "The output display is not updating fast enough to reflect real traffic", "This is not an IPO problem at all here, since traffic is treated as an external factor outside the system"],
    ),
    # 1.2.3 Hard — programming-fundamentals (ambiguity in identifying the input)
    (
        "An e-commerce backend team is specifying a refund-processing feature. The requirement says: 'When an order is returned, calculate the refund amount and update the customer's payment method.' Two engineers disagree about what this system's input is. One says it's the returned order details; the other says it's the customer's original payment method. Which point of view correctly identifies the input, and why does the disagreement matter?",
        "The input is what triggers and initiates the process — here, the returned order details are what kick off refund processing. The payment method is data the processing step looks up and uses partway through, but it doesn't trigger the process; the return does. This distinction matters because misidentifying the trigger can lead to designing the system around the wrong event, e.g., waiting on payment-method data before a return has even been confirmed.",
        "hard", "analyze", "programming-fundamentals",
        "The returned order details — that's what triggers the process, not the payment method",
        ["The payment method is the input, since without it no refund could ever be issued", "Both are inputs of equal standing, since the system cannot function without either one", "Neither is the input — the refund amount itself is the true input to the system"],
    ),
    # 1.2.4 Easy — computational-thinking (decomposition, concept id)
    (
        "A city bike-sharing operator needs to redistribute bikes each night so no dock is completely empty or completely full the next morning. Before writing any code, the operations analyst breaks this large problem into three smaller ones: predicting demand per dock, calculating how many bikes to move between docks, and scheduling van routes to make the moves. Which computational thinking skill is being applied here?",
        "Breaking one large problem (nightly rebalancing) into smaller, self-contained sub-problems (demand prediction, quantity calculation, route scheduling) is decomposition. No comparison to a past problem, detail-hiding, or step-by-step procedure has been described yet — those would be separate steps that could follow.",
        "easy", "understand", "computational-thinking",
        "Decomposition — splitting one large problem into smaller sub-problems",
        ["Pattern recognition — noticing that this problem resembles a past one", "Abstraction — deciding which details of each dock to ignore", "Algorithm design — writing the exact step-by-step van routing procedure"],
    ),
    # 1.2.5 Medium — computational-thinking (pattern recognition applied correctly)
    (
        "A hospital's ER intake system currently has a queue for chest-pain patients that ranks them by symptom severity and vitals. The team is now building a queue for stroke-symptom patients. A developer notices the ranking logic — combine severity score with time since symptom onset — is structurally the same for both conditions, just with different scoring rules, so she reuses the same ranking engine with condition-specific scoring plugged in. What is she doing?",
        "Recognizing that the stroke queue shares the same underlying structure as the chest-pain queue, and reusing the ranking engine instead of rebuilding it, is exactly what pattern recognition looks like in practice. This isn't decomposition (no breaking-down described) or abstraction (no detail is being hidden) — and a new scoring rule plugged into an existing engine is the opposite of building from scratch.",
        "medium", "apply", "computational-thinking",
        "Applying pattern recognition — reusing a similar solution for a related problem",
        ["Applying decomposition — breaking the stroke queue into smaller pieces for the first time", "Applying abstraction — removing detail that isn't relevant to either queue", "Writing an algorithm from scratch, since a new scoring rule always requires a brand-new engine"],
    ),
    # 1.2.6 Hard — computational-thinking (ordering: abstraction before algorithm design)
    (
        "A city traffic engineer is redesigning signal timing at a busy intersection. Two colleagues disagree on the first step. One wants to immediately write the exact second-by-second timing algorithm for the lights. The other wants to first identify which factors actually matter — pedestrian volume, left-turn queue length, time of day — and ignore irrelevant ones like the intersection's paint colour or signpost material. Which approach follows sound computational thinking practice, and why?",
        "Deciding which factors are relevant (abstraction) before locking into a specific step-by-step timing algorithm avoids wasting effort building precise logic around the wrong variables. Jumping straight to algorithm design risks encoding irrelevant details or missing important ones. This ordering matters — it isn't interchangeable — because a flawed initial scope is hard to unwind once an algorithm is already built around it.",
        "hard", "analyze", "computational-thinking",
        "Abstraction first — decide what matters before committing to an algorithm",
        ["The first colleague's approach — algorithm design should always come first so there is something concrete to test", "Both approaches are equally valid, since abstraction and algorithm design can be done in any order without consequence", "Neither — traffic timing should be decided by decomposition alone, without abstraction or algorithm design"],
    ),
    # 1.2.7 Easy — algorithms-and-pseudocode (pseudocode vs code distinction)
    (
        "A smart-thermostat developer writes the following before touching any code:\n\n```\nIF room temperature > target temperature + 2\n    Turn on cooling\nELSE IF room temperature < target temperature - 2\n    Turn on heating\nELSE\n    Keep system idle\n```\n\nWhat is this an example of, and why would a developer write this before actual code?",
        "This is pseudocode: it expresses the logic in plain, structured language without committing to any specific programming language's exact syntax (no colons, no specific keyword casing, no indentation rules enforced). It is not valid Python as written, and it is not a flowchart, since flowcharts are diagrams with shapes and arrows, not text.",
        "easy", "understand", "algorithms-and-pseudocode",
        "Pseudocode — a language-independent outline written before actual code",
        ["Python code — this is valid, runnable Python exactly as written", "A flowchart — this is a diagram-based representation of the logic", "A finished algorithm ready for production, requiring no further translation"],
    ),
    # 1.2.8 Medium — algorithms-and-pseudocode (step ordering consequence)
    (
        "A food delivery app's ETA algorithm is written as:\n\n1. Add the restaurant's food-prep time to the current time.\n2. Look up current traffic conditions on the route.\n3. Add the estimated travel time to the result from step 1.\n\nA reviewer notices this occasionally produces stale ETAs during sudden traffic spikes. What is the issue with the step ordering?",
        "Because traffic is fetched after prep time is calculated, there's a small window where conditions could shift before that data is used, making the final ETA slightly stale in fast-changing traffic. Step order absolutely can affect real-world correctness or freshness of results even when every step eventually executes. Prep time is a legitimate part of ETA and shouldn't be removed, and there's no rule requiring a minimum of four steps.",
        "medium", "analyze", "algorithms-and-pseudocode",
        "Traffic is checked only after prep time is added, so conditions can shift before that data gets used",
        ["There is no issue — step order never affects an algorithm's correctness as long as all steps eventually run", "The algorithm is invalid because it has exactly three steps, and valid algorithms require at least four", "Step 1 should be removed entirely, since prep time is never relevant to ETA"],
    ),
    # 1.2.9 Medium — algorithms-and-pseudocode (devise a plan skipped)
    (
        "A municipal engineer is asked to reduce water pressure drops across a city's pipe network. Instead of first sketching how sensors, valves, and a control algorithm would work together, he immediately starts writing detailed control code for adjusting valve positions. Midway through, he realizes he never decided how the different sensor readings should be combined into one decision. What problem-solving stage did he skip?",
        "Devising a plan means deciding the overall approach — here, how sensor data should combine into a decision — before implementation begins. Skipping straight to writing control code without that design step is exactly why he got stuck midway through. He did understand the problem (pressure drops), so that stage wasn't skipped; and he can't be 'carrying out a plan' that was never devised in the first place.",
        "medium", "analyze", "algorithms-and-pseudocode",
        "Devise a plan — he moved straight to implementation without first designing the overall approach",
        ["Understand the problem — he clearly understood that pressure drops were the issue", "Carry out the plan — he is already deep into carrying out a plan, so this stage cannot have been skipped", "Review the solution — this stage only applies after a working system exists"],
    ),
    # 1.2.10 Hard — algorithms-and-pseudocode (definiteness)
    (
        "An agricultural drone operator manually adjusts a drone's spray nozzle angle by eye each time it flies over a slope, based on how the field looks that day. A software team wants to replace this with an algorithm. One engineer proposes: 'Whenever the field looks uneven, adjust the nozzle appropriately.' A colleague rejects this as not being a usable algorithm. Why?",
        "A valid algorithm requires definiteness — each step must be precise and unambiguous enough for the executor (here, a program) to carry out without guessing. 'Looks uneven' and 'adjust appropriately' rely on human judgment, not measurable, well-defined conditions like a specific slope-angle sensor reading. This is a definiteness problem, not a finiteness or decomposition one, and a program cannot infer human intent from vague phrasing.",
        "hard", "analyze", "algorithms-and-pseudocode",
        "It lacks definiteness — the steps are too vague for a program to execute",
        ["It lacks decomposition — the task has not been broken into the correct number of sub-tasks", "It lacks finiteness — this description would never terminate once running", "It is a perfectly usable algorithm, since the drone would understand the intent"],
    ),
    # 1.2.11 Easy — flowcharts (shape recall)
    (
        "A security-camera system's flowchart needs a shape to represent the very first step: 'System powers on.' Which flowchart shape is conventionally used for this?",
        "Ovals (also called terminal symbols) conventionally mark the start and end points of a flowchart. Rectangles represent processing steps, diamonds represent decisions, and parallelograms represent input or output operations — none of which fit a 'system powers on' starting point.",
        "easy", "understand", "flowcharts",
        "An oval (terminal/start-end symbol)",
        ["A rectangle (process symbol)", "A diamond (decision symbol)", "A parallelogram (input/output symbol)"],
    ),
    # 1.2.12 Medium — flowcharts (equivalence with pseudocode)
    (
        "A gym's equipment-maintenance flowchart reads: check usage hours, then a diamond asks 'Usage hours > 500?' — if yes, flag for servicing; if no, keep monitoring. A technician rewrites this same logic as pseudocode:\n\n```\nIF usage_hours > 500\n    Flag for servicing\nELSE\n    Keep monitoring\n```\n\nDo the flowchart and the pseudocode represent the same logic?",
        "A flowchart and pseudocode are simply two different ways of representing the exact same logic — diagram-based versus text-based. Here, both include the same condition (usage hours > 500) and both possible outcomes (flag vs monitor). Pseudocode can absolutely represent decisions using IF/ELSE, and this flowchart description already includes both branches, not just the 'yes' path.",
        "medium", "analyze", "flowcharts",
        "Yes — both represent the same decision and outcomes, just in two different notations",
        ["No — the flowchart has three steps total while the pseudocode has only two lines of logic here", "No — pseudocode is not capable of representing a decision the way a flowchart's diamond can here", "No — the flowchart only shows the 'yes' path here, while the pseudocode shows both branches clearly"],
    ),
    # 1.2.13 Hard — flowcharts (missing branch)
    (
        "A grid load-balancing flowchart checks: 'Is demand greater than supply?' If yes, it draws power from the battery reserve. The diagram has no 'No' branch drawn out of that decision diamond at all — the line simply stops. An engineer says this flowchart cannot be implemented as-is. Why?",
        "A decision diamond must define what happens for every possible outcome of its question — here, both when demand exceeds supply and when it doesn't. Leaving the 'No' path unspecified means there's no defined behaviour for that case, which makes the flowchart incomplete, not just stylistically odd. There's no universal convention that a missing branch silently means 'do nothing' — that would need to be explicitly drawn. Diamonds are correctly used here; the problem is the missing branch, not the shape choice.",
        "hard", "analyze", "flowcharts",
        "Every decision needs both outcomes defined — the missing 'No' path is undefined behaviour",
        ["It cannot be implemented because diamonds are only allowed to have one outgoing path in a flowchart", "It is actually fine, since a missing 'No' branch is silently treated as 'do nothing' by convention", "It cannot be implemented because the decision should have been a rectangle instead of a diamond"],
    ),
    # 1.2.14 Easy — python-overview (interpreted language, concept id)
    (
        "A game studio's scripting lead explains to a new hire that Python code is generally run by an interpreter that reads and executes it line by line, rather than being translated all at once into a standalone executable ahead of time, the way some other languages work. What category does this describe Python as?",
        "Running code line-by-line through an interpreter, rather than compiling the whole program into an executable ahead of time, is what defines an interpreted language. Compiled languages translate the entire program before it runs. Markup and query languages describe entirely different categories (structuring documents, and querying data, respectively), not execution models.",
        "easy", "understand", "python-overview",
        "An interpreted language",
        ["A compiled language (like C)", "A markup language (like HTML)", "A query language (like SQL)"],
    ),
    # 1.2.15 Medium — python-overview (readability trade-off)
    (
        "A call-center's engineering team is comparing two rewritten versions of their ticket-routing logic — one in Python, one in a lower-level language. The Python version runs measurably slower per ticket, but the team is still choosing it for this internal tool. Which of the following is the most defensible reason for that choice, given Python's known trade-offs?",
        "Python is genuinely slower per-operation than many lower-level languages — that trade-off is real, not a misconception to wave away. The defensible reasoning is that for a modest, well-within-range ticket volume, the readability and maintainability benefits outweigh a speed cost that doesn't actually bottleneck the system. Claiming Python is 'always faster' or that speed 'never matters' misrepresents the trade-off, and lower-level languages absolutely can express conditional logic.",
        "medium", "analyze", "python-overview",
        "The ticket volume is modest and within Python's range, so readability outweighs the speed cost",
        ["Python is always faster than lower-level languages once a program is fully written and tested", "The lower-level language cannot express conditional logic, so Python is the only valid option", "Speed differences between languages never matter for any production system, regardless of scale"],
    ),
    # 1.2.16 Hard — python-overview (ecosystem strength doesn't generalize)
    (
        "A telecom analytics team picked Python for anomaly detection largely because of its mature data-science library ecosystem (for statistics and machine learning). A new team member argues that since Python worked so well here, it must also be the best choice for writing the company's new high-frequency packet-inspection engine, which needs to process millions of packets per second with minimal latency. Is this reasoning sound?",
        "Python was a good fit for anomaly detection because of its specific strengths there — library support and readability for statistical work, where raw speed wasn't the bottleneck. A packet-inspection engine handling millions of packets per second is bottlenecked by raw execution speed, a different constraint entirely, so the earlier reasoning doesn't carry over. This isn't a blanket 'never use Python' rule either — it's about matching the language's strengths to each task's actual constraint.",
        "hard", "analyze", "python-overview",
        "No — the reason Python fit anomaly detection doesn't transfer to a latency-critical packet engine",
        ["Yes — a language performing well on one task within a company will perform equally well on any other task there", "Yes — Python's data-science libraries include everything needed for high-frequency packet inspection", "No — Python should never be used anywhere in a telecom company, regardless of the specific task"],
    ),
    # 1.2.17 Easy — python-environment (REPL vs script use case)
    (
        "A field engineer wants to quickly check what `humidity_reading * 1.8` evaluates to for a sample value, just once, without saving anything for later use. Which tool is most appropriate for this?",
        "The REPL (Read-Eval-Print Loop) is designed exactly for quick, throwaway checks — type an expression, see the result immediately, without creating or saving a file. A saved script is more appropriate when the code needs to be reused or shared later. Flowcharts and pseudocode are planning tools, not executable calculators — pseudocode in particular cannot be run directly by Python at all.",
        "easy", "understand", "python-environment",
        "The Python REPL — suited for quick one-off checks that don't need saving",
        ["A saved `.py` script file, since all Python code must be saved before it can run", "A flowchart diagram, since flowcharts are used for any quick calculation", "Pseudocode, since pseudocode can be directly executed by Python"],
    ),
    # 1.2.18 Medium — python-environment (script persistence)
    (
        "An engineer writes a short batch job that renames a folder of podcast audio files by episode number, tests it directly in the interactive REPL, and it works. The next morning, she wants to run the exact same renaming job on a new folder of files without retyping every line. What should she have done instead, and why?",
        "The REPL is meant for interactive, in-the-moment work and does not persist code between sessions — once it's closed, that history is gone. Saving the logic in a `.py` file means it can be reopened and re-run anytime without retyping it. Flowcharts are diagrams, not executable files, and retyping identical code every day is exactly the repetitive manual work that saving a script is meant to eliminate.",
        "medium", "apply", "python-environment",
        "Save the code in a `.py` script file so it can be reopened and rerun later",
        ["Nothing — the REPL automatically remembers and re-offers every command typed in any previous session", "Rewrite the logic as a flowchart, since flowcharts can be executed directly the next day", "Nothing needs to change — retyping the same lines each morning is the intended way to use Python"],
    ),
    # 1.2.19 Hard — python-environment (runtime error, minimal fix)
    (
        "A sports analytics team's first Python script for a live scoreboard runs fine during testing but crashes mid-broadcast the first time a match ends in a 0-0 draw:\n\n```python\nhome_goals = 0\naway_goals = 0\nratio = home_goals / away_goals\nprint(ratio)\n```\n\nWhat kind of error is this, and what is the minimal correct fix?",
        "This code is syntactically correct and runs successfully for nonzero values of `away_goals` — the failure only happens at runtime, specifically when dividing by zero, which is a `ZeroDivisionError`. The minimal fix is to add a check for zero before dividing (or handle the exception), not to rewrite the script's overall logic, since the ratio formula itself is fine for every other case. This is a completely normal, fixable situation in Python, not a language limitation.",
        "hard", "analyze", "python-environment",
        "A runtime error (`ZeroDivisionError`) — check for zero before dividing, don't rewrite everything",
        ["A syntax error — the division operator `/` is being used incorrectly and Python cannot parse this line", "A logic error — the ratio calculation itself is mathematically wrong regardless of the input values", "This cannot be fixed in Python; ratios involving zero must be computed in a different language"],
    ),
    # 1.2.20 Medium — python-environment (comments vs print)
    (
        "A developer testing a home-security alarm's Python script temporarily adds a line, `# print(sensor_reading)`, above the main logic while debugging, then removes the `#` when she wants to see the value again. What is she using this line for, and why does adding `#` change its behaviour?",
        "A `#` marks everything after it on that line as a comment, which Python skips entirely when running the file — it has zero effect on execution, not a partial or paused one. Removing the `#` restores it as a normal, executable `print()` statement. This is a common, deliberate technique for toggling debug output on and off without deleting code. Comments don't turn code into pseudocode, and they do change execution — the line runs or doesn't depending on the `#`.",
        "medium", "understand", "python-environment",
        "The `#` marks the line as a comment, so Python skips it; removing `#` restores the `print()` call",
        ["The `#` pauses the line's execution temporarily but still displays the sensor reading once per run", "The `#` converts the line into pseudocode, which Python still partially executes", "The `#` has no effect on execution; it only changes how the line looks in the editor"],
    ),
]

assert len(SET1) == 10, len(SET1)
assert len(SET2) == 20, len(SET2)


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
            "tags": f"python - {set_label}",
            "subjects": "python",
            "topics": "introduction-to-programming",
            "subTopics": subtopic,
            "companies": None,
            "option1": options[0],
            "option2": options[1],
            "option3": options[2],
            "option4": options[3],
            "answer": pos,
        })
    return rows


rows1 = build_rows(SET1, "Set 1", "Python - MCQ - 1.1")
rows2 = build_rows(SET2, "Set 2", "Python - MCQ - 1.2")
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

# SOP: the correct answer must never be the single longest option
for r in all_rows:
    opts = [r["option1"], r["option2"], r["option3"], r["option4"]]
    lengths = [len(o) for o in opts]
    correct_idx = r["answer"] - 1
    max_len = max(lengths)
    if lengths[correct_idx] == max_len and lengths.count(max_len) == 1:
        raise AssertionError(f"{r['title']}: correct option is the strict longest — {opts}")

# SOP: no single scenario domain (education-sector) should dominate the set
edu_words = ["college", "student", "hostel", "university", "school", "campus", "exam hall"]
edu_count = sum(1 for r in all_rows if any(w in r["description"].lower() for w in edu_words))
print("education-domain scenario count:", edu_count, "/", len(all_rows))
assert edu_count <= len(all_rows) * 0.2, "too many education-domain scenarios"

headers = ["title", "description", "explanation", "score", "status", "difficulty", "bloomTaxonomy",
           "tags", "subjects", "topics", "subTopics", "companies",
           "option1", "option2", "option3", "option4", "answer"]

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Python - MCQ - Unit 1"
ws.append(headers)
for r in all_rows:
    ws.append([r[h] for h in headers])

out_path = "content/Question Bank/MCQ/Unit 1 - Introduction to Programming/Unit 1 - Introduction to Programming - MCQ.xlsx"
wb.save(out_path)
print("Saved", out_path, "with", len(all_rows), "questions")
