from pathlib import Path
from html import escape
import textwrap


ROOT = Path("/Users/suman/Desktop/ByteXL/Unit 1/Chapter 5 - Conditional Logic in Python")
IMAGES = ROOT / "images"


STYLE = """
<style>
  .bg { fill: #f7fbff; }
  .card { fill: #ffffff; stroke: #cfe0ff; stroke-width: 2; rx: 18; }
  .blue { fill: #e9f2ff; stroke: #3b82f6; stroke-width: 2; rx: 16; }
  .green { fill: #eaf8ef; stroke: #22a35a; stroke-width: 2; rx: 16; }
  .yellow { fill: #fff7db; stroke: #f4b000; stroke-width: 2; rx: 16; }
  .purple { fill: #f3ecff; stroke: #7c3aed; stroke-width: 2; rx: 16; }
  .red { fill: #fff0f0; stroke: #ef4444; stroke-width: 2; rx: 16; }
  .ink { fill: #10204c; font-family: Arial, Helvetica, sans-serif; }
  .muted { fill: #41506f; font-family: Arial, Helvetica, sans-serif; }
  .label { fill: #10204c; font-family: Arial, Helvetica, sans-serif; font-size: 24px; font-weight: 700; }
  .small { fill: #41506f; font-family: Arial, Helvetica, sans-serif; font-size: 18px; }
  .tiny { fill: #41506f; font-family: Arial, Helvetica, sans-serif; font-size: 15px; }
  .mono { fill: #10204c; font-family: Menlo, Consolas, monospace; font-size: 18px; }
  .arrow { stroke: #2563eb; stroke-width: 4; fill: none; marker-end: url(#arrow); }
  .arrow-green { stroke: #16a34a; stroke-width: 4; fill: none; marker-end: url(#arrow-green); }
  .arrow-red { stroke: #ef4444; stroke-width: 4; fill: none; marker-end: url(#arrow-red); }
  .dash { stroke: #94a3b8; stroke-width: 3; stroke-dasharray: 8 8; fill: none; marker-end: url(#arrow-muted); }
  .diamond { fill: #fff7db; stroke: #f4b000; stroke-width: 2; }
</style>
<defs>
  <marker id="arrow" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto">
    <path d="M2,2 L10,6 L2,10 Z" fill="#2563eb" />
  </marker>
  <marker id="arrow-green" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto">
    <path d="M2,2 L10,6 L2,10 Z" fill="#16a34a" />
  </marker>
  <marker id="arrow-red" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto">
    <path d="M2,2 L10,6 L2,10 Z" fill="#ef4444" />
  </marker>
  <marker id="arrow-muted" markerWidth="12" markerHeight="12" refX="10" refY="6" orient="auto">
    <path d="M2,2 L10,6 L2,10 Z" fill="#94a3b8" />
  </marker>
</defs>
"""


def svg(width, height, body):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img">
{STYLE}
<rect width="{width}" height="{height}" class="bg"/>
{body}
</svg>
"""


def text(x, y, value, cls="label", anchor="middle"):
    value = escape(value)
    return f'<text x="{x}" y="{y}" class="{cls}" text-anchor="{anchor}">{value}</text>'


def rect(x, y, w, h, cls="card"):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" ry="16" class="{cls}"/>'


def line(x1, y1, x2, y2, cls="arrow"):
    return f'<path d="M{x1},{y1} L{x2},{y2}" class="{cls}"/>'


def diamond(cx, cy, w, h):
    pts = f"{cx},{cy-h/2} {cx+w/2},{cy} {cx},{cy+h/2} {cx-w/2},{cy}"
    return f'<polygon points="{pts}" class="diamond"/>'


def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(textwrap.dedent(content).strip() + "\n", encoding="utf-8")


def write_svg(name, body, width=1400, height=620):
    (IMAGES / name).write_text(svg(width, height, body), encoding="utf-8")


def build_svgs():
    write_svg("01-branching-flow.svg", f"""
{rect(40, 60, 220, 90, "blue")}{text(150, 115, "Input / state")}
{diamond(430, 105, 210, 120)}{text(430, 100, "First test?", "label")}{text(430, 130, "True or false", "small")}
{rect(650, 40, 230, 80, "green")}{text(765, 90, "Run if block")}
{diamond(650, 260, 210, 120)}{text(650, 255, "Next test?", "label")}{text(650, 285, "elif", "small")}
{rect(910, 205, 230, 80, "green")}{text(1025, 255, "Run elif block")}
{rect(910, 380, 230, 80, "yellow")}{text(1025, 430, "Run else block")}
{rect(1190, 245, 170, 80, "purple")}{text(1275, 295, "Continue")}
{line(260, 105, 325, 105)}
{line(535, 105, 650, 80, "arrow-green")}{text(595, 72, "True", "tiny")}
{line(430, 165, 575, 250)}{text(505, 215, "False", "tiny")}
{line(880, 80, 1190, 260)}
{line(755, 260, 910, 245, "arrow-green")}{text(835, 232, "True", "tiny")}
{line(650, 320, 910, 420, "arrow-red")}{text(780, 385, "False", "tiny")}
{line(1140, 245, 1190, 275)}
{line(1140, 420, 1190, 300)}
{text(700, 555, "Only one branch runs: Python checks from top to bottom and stops at the first True condition.", "muted")}
""")

    write_svg("01-shopping-discount-tree.svg", f"""
{rect(50, 55, 250, 95, "blue")}{text(175, 105, "Cart total")}{text(175, 132, "membership status", "small")}
{diamond(455, 105, 230, 130)}{text(455, 100, ">= 5000?", "label")}
{rect(705, 50, 230, 90, "green")}{text(820, 102, "20% discount")}
{diamond(455, 315, 230, 130)}{text(455, 310, ">= 2000?", "label")}
{rect(705, 270, 230, 90, "yellow")}{text(820, 322, "10% discount")}
{rect(705, 450, 230, 90, "purple")}{text(820, 502, "No discount")}
{rect(1050, 245, 260, 105, "card")}{text(1180, 295, "Show final bill")}{text(1180, 322, "with message", "small")}
{line(300, 105, 340, 105)}
{line(570, 105, 705, 95, "arrow-green")}{text(640, 82, "yes", "tiny")}
{line(455, 170, 455, 250, "arrow-red")}{text(480, 215, "no", "tiny")}
{line(570, 315, 705, 315, "arrow-green")}{text(640, 300, "yes", "tiny")}
{line(455, 380, 705, 485, "arrow-red")}{text(575, 450, "no", "tiny")}
{line(935, 95, 1050, 270)}
{line(935, 315, 1050, 295)}
{line(935, 495, 1050, 320)}
{text(700, 585, "Useful for pricing, grading, eligibility, alerts, and any feature with ranked rules.", "muted")}
""")

    write_svg("01-branch-order.svg", f"""
{rect(60, 65, 570, 410, "red")}
{text(345, 115, "Risky order", "label")}
{text(110, 165, "if score >= 50:", "mono", "start")}
{text(140, 200, "grade = 'Pass'", "mono", "start")}
{text(110, 240, "elif score >= 90:", "mono", "start")}
{text(140, 275, "grade = 'Excellent'", "mono", "start")}
{rect(105, 335, 450, 70, "yellow")}{text(330, 378, "90 also passes the first test", "small")}
{rect(770, 65, 570, 410, "green")}
{text(1055, 115, "Better order", "label")}
{text(820, 165, "if score >= 90:", "mono", "start")}
{text(850, 200, "grade = 'Excellent'", "mono", "start")}
{text(820, 240, "elif score >= 50:", "mono", "start")}
{text(850, 275, "grade = 'Pass'", "mono", "start")}
{rect(815, 335, 450, 70, "blue")}{text(1040, 378, "Most specific rule first", "small")}
{text(700, 555, "When conditions overlap, place the narrowest or highest-priority rule first.", "muted")}
""")

    write_svg("01-login-case-study.svg", f"""
{rect(50, 70, 220, 90, "blue")}{text(160, 122, "User submits")}{text(160, 148, "email + password", "small")}
{diamond(430, 115, 220, 120)}{text(430, 110, "Fields filled?", "label")}
{diamond(670, 115, 220, 120)}{text(670, 110, "Account exists?", "label")}
{diamond(910, 115, 220, 120)}{text(910, 110, "Password ok?", "label")}
{rect(1155, 70, 190, 90, "green")}{text(1250, 122, "Login success")}
{rect(330, 330, 220, 80, "red")}{text(440, 380, "Ask for input")}
{rect(570, 330, 220, 80, "red")}{text(680, 380, "Show generic error")}
{rect(810, 330, 220, 80, "red")}{text(920, 380, "Show generic error")}
{line(270, 115, 320, 115)}
{line(540, 115, 560, 115, "arrow-green")}
{line(780, 115, 800, 115, "arrow-green")}
{line(1020, 115, 1155, 115, "arrow-green")}
{line(430, 175, 430, 330, "arrow-red")}
{line(670, 175, 670, 330, "arrow-red")}
{line(910, 175, 910, 330, "arrow-red")}
{text(700, 515, "A real login system makes clear decisions but avoids leaking private security details.", "muted")}
""")

    write_svg("02-nested-vs-guard.svg", f"""
{rect(50, 50, 580, 450, "red")}
{text(340, 95, "Deep nesting", "label")}
{text(105, 150, "if user_exists:", "mono", "start")}
{text(145, 185, "if password_ok:", "mono", "start")}
{text(185, 220, "if account_active:", "mono", "start")}
{text(225, 255, "allow_login()", "mono", "start")}
{text(185, 315, "else: show locked", "mono", "start")}
{text(145, 350, "else: show error", "mono", "start")}
{text(105, 385, "else: show error", "mono", "start")}
{rect(95, 425, 450, 45, "yellow")}{text(320, 454, "Harder to scan as rules grow", "small")}
{rect(770, 50, 580, 450, "green")}
{text(1060, 95, "Guard clauses", "label")}
{text(825, 150, "if not user_exists: stop", "mono", "start")}
{text(825, 190, "if not password_ok: stop", "mono", "start")}
{text(825, 230, "if not account_active: stop", "mono", "start")}
{text(825, 290, "allow_login()", "mono", "start")}
{rect(815, 425, 450, 45, "blue")}{text(1040, 454, "Handle invalid cases early", "small")}
{text(700, 570, "Nested conditions are useful, but guard clauses keep the main path visible.", "muted")}
""")

    write_svg("02-atm-nested.svg", f"""
{rect(50, 70, 190, 80, "blue")}{text(145, 120, "Insert card")}
{diamond(380, 110, 210, 120)}{text(380, 105, "PIN ok?", "label")}
{diamond(650, 110, 230, 120)}{text(650, 105, "Enough balance?", "label")}
{diamond(935, 110, 230, 120)}{text(935, 105, "ATM has cash?", "label")}
{rect(1190, 70, 160, 80, "green")}{text(1270, 120, "Dispense")}
{rect(300, 330, 190, 80, "red")}{text(395, 380, "Wrong PIN")}
{rect(570, 330, 190, 80, "red")}{text(665, 380, "Insufficient")}
{rect(855, 330, 190, 80, "red")}{text(950, 380, "Try later")}
{line(240, 110, 275, 110)}
{line(485, 110, 535, 110, "arrow-green")}
{line(765, 110, 820, 110, "arrow-green")}
{line(1050, 110, 1190, 110, "arrow-green")}
{line(380, 170, 380, 330, "arrow-red")}
{line(650, 170, 650, 330, "arrow-red")}
{line(935, 170, 935, 330, "arrow-red")}
{text(700, 530, "A nested decision tree is useful when one question only matters after another question passes.", "muted")}
""")

    write_svg("02-guard-validation.svg", f"""
{rect(70, 60, 230, 80, "blue")}{text(185, 110, "Request arrives")}
{rect(405, 50, 250, 95, "red")}{text(530, 95, "Missing input?")}{text(530, 122, "Return early", "small")}
{rect(405, 190, 250, 95, "red")}{text(530, 235, "Invalid format?")}{text(530, 262, "Return early", "small")}
{rect(405, 330, 250, 95, "red")}{text(530, 375, "Not allowed?")}{text(530, 402, "Return early", "small")}
{rect(820, 190, 260, 95, "green")}{text(950, 235, "Main action")}{text(950, 262, "Clear happy path", "small")}
{rect(1160, 190, 170, 95, "purple")}{text(1245, 245, "Response")}
{line(300, 100, 405, 95)}
{line(655, 95, 820, 220, "dash")}
{line(655, 235, 820, 235, "dash")}
{line(655, 375, 820, 250, "dash")}
{line(1080, 235, 1160, 235)}
{text(700, 545, "Guard clauses protect the main logic by rejecting bad cases before the main work starts.", "muted")}
""")

    write_svg("02-ticket-case.svg", f"""
{rect(55, 70, 250, 90, "blue")}{text(180, 120, "Ticket request")}{text(180, 148, "age, seat, payment", "small")}
{diamond(460, 115, 220, 120)}{text(460, 110, "Age valid?", "label")}
{diamond(715, 115, 220, 120)}{text(715, 110, "Seat open?", "label")}
{diamond(970, 115, 220, 120)}{text(970, 110, "Payment ok?", "label")}
{rect(1210, 75, 140, 80, "green")}{text(1280, 125, "Book")}
{rect(365, 340, 190, 75, "red")}{text(460, 386, "Fix age")}
{rect(620, 340, 190, 75, "red")}{text(715, 386, "Pick seat")}
{rect(875, 340, 190, 75, "red")}{text(970, 386, "Retry pay")}
{line(305, 115, 350, 115)}
{line(570, 115, 605, 115, "arrow-green")}
{line(825, 115, 860, 115, "arrow-green")}
{line(1080, 115, 1210, 115, "arrow-green")}
{line(460, 175, 460, 340, "arrow-red")}
{line(715, 175, 715, 340, "arrow-red")}
{line(970, 175, 970, 340, "arrow-red")}
{text(700, 520, "Ticket systems often combine nested eligibility with early exits for invalid requests.", "muted")}
""")

    write_svg("03-match-selection.svg", f"""
{rect(55, 70, 250, 90, "blue")}{text(180, 122, "One value")}{text(180, 150, "command / status / role", "small")}
{rect(440, 45, 230, 70, "green")}{text(555, 90, "case 'start'")}
{rect(440, 145, 230, 70, "green")}{text(555, 190, "case 'pause'")}
{rect(440, 245, 230, 70, "green")}{text(555, 290, "case 'cancel'")}
{rect(440, 345, 230, 70, "yellow")}{text(555, 390, "case _")}
{rect(870, 45, 320, 70, "card")}{text(1030, 90, "Run selected action")}
{rect(870, 345, 320, 70, "card")}{text(1030, 390, "Fallback action")}
{line(305, 115, 440, 80)}
{line(305, 115, 440, 180)}
{line(305, 115, 440, 280)}
{line(305, 115, 440, 380)}
{line(670, 80, 870, 80, "arrow-green")}
{line(670, 180, 870, 80, "arrow-green")}
{line(670, 280, 870, 80, "arrow-green")}
{line(670, 380, 870, 380)}
{text(700, 535, "match-case is best when one value chooses among several clear options.", "muted")}
""")

    write_svg("03-food-order-match.svg", f"""
{rect(65, 70, 230, 90, "blue")}{text(180, 120, "Menu choice")}
{rect(420, 45, 230, 70, "green")}{text(535, 90, "1 -> Pizza")}
{rect(420, 145, 230, 70, "green")}{text(535, 190, "2 -> Burger")}
{rect(420, 245, 230, 70, "green")}{text(535, 290, "3 -> Salad")}
{rect(420, 345, 230, 70, "yellow")}{text(535, 390, "_ -> Help")}
{rect(820, 40, 250, 90, "card")}{text(945, 92, "Build order")}
{rect(1120, 40, 210, 90, "purple")}{text(1225, 92, "Show total")}
{line(295, 115, 420, 80)}
{line(295, 115, 420, 180)}
{line(295, 115, 420, 280)}
{line(295, 115, 420, 380)}
{line(650, 80, 820, 85, "arrow-green")}
{line(650, 180, 820, 85, "arrow-green")}
{line(650, 280, 820, 85, "arrow-green")}
{line(1070, 85, 1120, 85)}
{text(700, 535, "Readable menu logic helps users choose and helps developers add new options later.", "muted")}
""")

    write_svg("03-match-vs-elif.svg", f"""
{rect(60, 65, 560, 410, "yellow")}
{text(340, 115, "Many elif checks", "label")}
{text(115, 170, "if command == 'start':", "mono", "start")}
{text(115, 215, "elif command == 'pause':", "mono", "start")}
{text(115, 260, "elif command == 'stop':", "mono", "start")}
{text(115, 305, "else:", "mono", "start")}
{rect(105, 380, 420, 55, "card")}{text(315, 415, "Good, but can feel repetitive", "small")}
{rect(780, 65, 560, 410, "green")}
{text(1060, 115, "One value, clear cases", "label")}
{text(835, 170, "match command:", "mono", "start")}
{text(875, 215, "case 'start':", "mono", "start")}
{text(875, 260, "case 'pause':", "mono", "start")}
{text(875, 305, "case _:", "mono", "start")}
{rect(825, 380, 420, 55, "card")}{text(1035, 415, "Cleaner for menu-like choices", "small")}
{text(700, 555, "Use match-case for readable multi-way choices around one main value.", "muted")}
""")

    write_svg("03-support-case.svg", f"""
{rect(50, 75, 220, 85, "blue")}{text(160, 125, "Ticket type")}
{rect(390, 45, 230, 70, "green")}{text(505, 90, "billing")}
{rect(390, 145, 230, 70, "green")}{text(505, 190, "technical")}
{rect(390, 245, 230, 70, "green")}{text(505, 290, "account")}
{rect(390, 345, 230, 70, "yellow")}{text(505, 390, "other")}
{rect(780, 45, 260, 70, "card")}{text(910, 90, "Billing team")}
{rect(780, 145, 260, 70, "card")}{text(910, 190, "Tech team")}
{rect(780, 245, 260, 70, "card")}{text(910, 290, "Account team")}
{rect(780, 345, 260, 70, "card")}{text(910, 390, "Triage queue")}
{rect(1140, 190, 200, 90, "purple")}{text(1240, 242, "Route ticket")}
{line(270, 115, 390, 80)}
{line(270, 115, 390, 180)}
{line(270, 115, 390, 280)}
{line(270, 115, 390, 380)}
{line(620, 80, 780, 80, "arrow-green")}
{line(620, 180, 780, 180, "arrow-green")}
{line(620, 280, 780, 280, "arrow-green")}
{line(620, 380, 780, 380)}
{line(1040, 80, 1140, 220)}
{line(1040, 180, 1140, 230)}
{line(1040, 280, 1140, 245)}
{line(1040, 380, 1140, 260)}
{text(700, 535, "Support software often routes one category value to one destination.", "muted")}
""")

    write_svg("04-validation-pipeline.svg", f"""
{rect(50, 70, 190, 80, "blue")}{text(145, 120, "Raw input")}
{rect(330, 45, 230, 70, "yellow")}{text(445, 90, "Clean spaces")}
{rect(330, 165, 230, 70, "yellow")}{text(445, 210, "Check empty")}
{rect(330, 285, 230, 70, "yellow")}{text(445, 330, "Check type")}
{rect(330, 405, 230, 70, "yellow")}{text(445, 450, "Check range")}
{rect(735, 165, 260, 90, "green")}{text(865, 215, "Safe value")}
{rect(1100, 165, 220, 90, "purple")}{text(1210, 215, "Use in logic")}
{line(240, 110, 330, 80)}
{line(240, 110, 330, 200)}
{line(240, 110, 330, 320)}
{line(240, 110, 330, 440)}
{line(560, 80, 735, 190, "dash")}
{line(560, 200, 735, 200, "dash")}
{line(560, 320, 735, 215, "dash")}
{line(560, 440, 735, 230, "dash")}
{line(995, 210, 1100, 210)}
{text(700, 545, "Defensive programs convert uncertain user input into safe, predictable data before making decisions.", "muted")}
""")

    write_svg("04-form-validation.svg", f"""
{rect(55, 70, 230, 90, "blue")}{text(170, 120, "Signup form")}
{diamond(445, 115, 220, 120)}{text(445, 110, "Email valid?", "label")}
{diamond(705, 115, 220, 120)}{text(705, 110, "Age >= 13?", "label")}
{diamond(965, 115, 220, 120)}{text(965, 110, "Password strong?", "label")}
{rect(1210, 75, 140, 80, "green")}{text(1280, 125, "Create")}
{rect(350, 340, 190, 75, "red")}{text(445, 386, "Fix email")}
{rect(610, 340, 190, 75, "red")}{text(705, 386, "Age rule")}
{rect(870, 340, 190, 75, "red")}{text(965, 386, "Improve pass")}
{line(285, 115, 335, 115)}
{line(555, 115, 595, 115, "arrow-green")}
{line(815, 115, 855, 115, "arrow-green")}
{line(1075, 115, 1210, 115, "arrow-green")}
{line(445, 175, 445, 340, "arrow-red")}
{line(705, 175, 705, 340, "arrow-red")}
{line(965, 175, 965, 340, "arrow-red")}
{text(700, 520, "Good validation gives specific, helpful feedback before data reaches the important system.", "muted")}
""")

    write_svg("04-try-except-flow.svg", f"""
{rect(65, 70, 230, 90, "blue")}{text(180, 122, "User types")}{text(180, 148, "amount text", "small")}
{rect(405, 70, 230, 90, "yellow")}{text(520, 122, "Try convert")}{text(520, 148, "int or float", "small")}
{diamond(800, 115, 220, 120)}{text(800, 110, "Converted?", "label")}
{rect(1060, 55, 240, 90, "green")}{text(1180, 107, "Check rules")}{text(1180, 133, "positive, limit", "small")}
{rect(1060, 285, 240, 90, "red")}{text(1180, 337, "Ask again")}
{line(295, 115, 405, 115)}
{line(635, 115, 690, 115)}
{line(910, 115, 1060, 100, "arrow-green")}{text(980, 85, "yes", "tiny")}
{line(800, 175, 1060, 330, "arrow-red")}{text(930, 265, "no", "tiny")}
{text(700, 520, "Conversion can fail. Handle it deliberately instead of letting the program crash.", "muted")}
""")

    write_svg("04-atm-defensive-case.svg", f"""
{rect(45, 75, 190, 80, "blue")}{text(140, 125, "Amount")}
{rect(330, 45, 230, 70, "yellow")}{text(445, 90, "Number?")}
{rect(330, 145, 230, 70, "yellow")}{text(445, 190, "> 0?")}
{rect(330, 245, 230, 70, "yellow")}{text(445, 290, "Multiple of 100?")}
{rect(330, 345, 230, 70, "yellow")}{text(445, 390, "<= balance?")}
{rect(760, 175, 230, 95, "green")}{text(875, 225, "Allow withdrawal")}
{rect(1090, 175, 230, 95, "purple")}{text(1205, 225, "Print receipt")}
{rect(760, 355, 230, 75, "red")}{text(875, 402, "Helpful message")}
{line(235, 115, 330, 80)}
{line(560, 80, 760, 200, "dash")}
{line(560, 180, 760, 210, "dash")}
{line(560, 280, 760, 220, "dash")}
{line(560, 380, 760, 230, "dash")}
{line(990, 220, 1090, 220)}
{line(445, 415, 760, 390, "arrow-red")}
{text(700, 535, "Defensive ATM logic protects money, users, and the system from invalid requests.", "muted")}
""")


def chapter_readme():
    write(ROOT / "README.md", """
    # Chapter 5: Conditional Logic in Python

    This folder contains four standalone Markdown learning resources and SVG diagrams for a premium Python curriculum chapter.

    ## Files

    | File | Topic |
    | --- | --- |
    | `01-if-elif-else-branching.md` | `if`, `elif`, and `else` for branching |
    | `02-nested-conditions-and-guard-clauses.md` | Nested conditions and guard clauses |
    | `03-match-case-readable-multi-way-choices.md` | `match-case` for readable multi-way choices |
    | `04-input-validation-and-defensive-decisions.md` | Input validation and defensive decision-making |

    ## Images

    All diagrams are stored in the `images/` folder as editable SVG files. The images avoid repeating long section titles and focus on visual understanding: flow, branching, validation paths, and decision structure.
    """)


def lesson_01():
    write(ROOT / "01-if-elif-else-branching.md", r"""
    # Chapter 5.1: `if`, `elif`, and `else` for Branching

    Conditional logic lets a program choose what to do next. In real software, almost every useful feature contains decisions: logging in, applying a discount, showing a warning, calculating a grade, or deciding whether a user is allowed to continue.

    ![Branching flow diagram](images/01-branching-flow.svg)

    ## Learning Objectives

    By the end of this section, you will be able to:

    - Explain how `if`, `elif`, and `else` let Python choose between paths.
    - Write simple and readable branching logic.
    - Understand why Python checks conditions from top to bottom.
    - Use `elif` when several related choices are possible.
    - Use `else` as a safe fallback when no previous condition is true.
    - Avoid common ordering and indentation mistakes.

    ## Simple Conceptual Explanation

    Think of a program like a person standing at a set of doors.

    - If the first door is open, the person enters that door.
    - Otherwise, they check the next door.
    - If no special door is open, they use the default door.

    In Python:

    - `if` asks the first question.
    - `elif` asks another question only if the earlier question was false.
    - `else` runs when none of the earlier conditions were true.

    The important rule is this:

    > In an `if` / `elif` / `else` chain, Python runs only one branch: the first branch whose condition is true.

    ## The Basic Shape

    ```python
    if condition:
        # run this when condition is True
    elif another_condition:
        # run this when the first condition is False
        # and this condition is True
    else:
        # run this when nothing above was True
    ```

    The colon `:` starts the branch. The indentation tells Python which lines belong inside that branch.

    ## Step-by-Step Python Examples

    ### Example 1: A Simple Age Check

    ```python
    age = 20

    if age >= 18:
        print("You are eligible to vote.")
    else:
        print("You are not eligible yet.")
    ```

    What happens:

    - Python checks `age >= 18`.
    - Since `20 >= 18` is true, Python prints the first message.
    - The `else` branch is skipped.

    ### Example 2: Weather Advice

    ```python
    weather = "rainy"

    if weather == "rainy":
        print("Carry an umbrella.")
    elif weather == "sunny":
        print("Wear sunglasses.")
    elif weather == "cold":
        print("Take a jacket.")
    else:
        print("Check the weather again before leaving.")
    ```

    This is useful because the choices are related. The program is deciding one kind of advice based on one weather condition.

    ### Example 3: Grading System

    ```python
    score = 86

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "Needs improvement"

    print("Grade:", grade)
    ```

    Notice the order. The highest score range appears first. That matters because Python stops at the first true condition.

    ![Branch order diagram](images/01-branch-order.svg)

    ### Example 4: Shopping Discount

    ![Shopping discount decision tree](images/01-shopping-discount-tree.svg)

    ```python
    cart_total = 3200
    is_member = True

    if cart_total >= 5000:
        discount = 0.20
    elif cart_total >= 2000 and is_member:
        discount = 0.10
    elif cart_total >= 1000:
        discount = 0.05
    else:
        discount = 0

    final_total = cart_total - (cart_total * discount)
    print("Final total:", final_total)
    ```

    This feels like a real ecommerce rule:

    - Very large purchases get the best discount.
    - Medium purchases may need membership.
    - Small purchases get a smaller offer.
    - Anything else gets no discount.

    ## Real-World Examples

    Conditional branching is used in:

    - Login systems: allow access or show an error.
    - Ticket booking: adult, child, senior citizen, or student pricing.
    - Food apps: free delivery, discount, or full delivery fee.
    - Banking apps: approve or reject a transaction.
    - Learning platforms: show beginner, intermediate, or advanced content.

    ## Mini Case Study: Login Decision Flow

    A login system does not simply check one thing. It often checks whether the user filled the form, whether the account exists, and whether the password is correct.

    ![Login case study decision flow](images/01-login-case-study.svg)

    ```python
    email = "student@example.com"
    password = "python123"

    stored_email = "student@example.com"
    stored_password = "python123"

    if email == "" or password == "":
        print("Please enter both email and password.")
    elif email != stored_email:
        print("Invalid email or password.")
    elif password != stored_password:
        print("Invalid email or password.")
    else:
        print("Login successful.")
    ```

    Professional note: real systems usually avoid saying exactly whether the email or password was wrong. A generic message is safer because it does not reveal which accounts exist.

    ## Common Mistakes

    ### Mistake 1: Forgetting the colon

    ```python
    if age >= 18
        print("Allowed")
    ```

    Correct:

    ```python
    if age >= 18:
        print("Allowed")
    ```

    ### Mistake 2: Wrong indentation

    ```python
    if age >= 18:
    print("Allowed")
    ```

    Correct:

    ```python
    if age >= 18:
        print("Allowed")
    ```

    ### Mistake 3: Checking broad rules before specific rules

    ```python
    score = 95

    if score >= 50:
        print("Pass")
    elif score >= 90:
        print("Excellent")
    ```

    The second branch never runs for `95`, because `score >= 50` is already true. Put the more specific or higher-priority rule first.

    ## Best Practices

    - Use clear condition names when possible.
    - Keep related choices in one `if` / `elif` / `else` chain.
    - Put the most specific conditions before broader conditions.
    - Use `else` for a meaningful fallback.
    - Do not make one condition do too many jobs.
    - Prefer readable logic over clever logic.

    ## Practice Exercises

    ### Beginner

    1. Ask for a user's age and print whether they are a child, teenager, or adult.
    2. Create a simple temperature checker:
       - below 18: cold
       - 18 to 30: pleasant
       - above 30: hot
    3. Write a program that checks whether a number is positive, negative, or zero.

    ### Intermediate

    1. Build a grading system with `A`, `B`, `C`, `D`, and `Needs improvement`.
    2. Create a ticket price calculator for child, adult, and senior citizen categories.
    3. Build a shopping discount calculator using cart total and membership status.

    ### Challenge

    Build a delivery fee calculator:

    - If order total is at least 1000, delivery is free.
    - If the user is a premium member, delivery is free.
    - If distance is more than 10 km, delivery is 120.
    - Otherwise, delivery is 50.

    Then print the final amount including delivery.

    ## Key Takeaways

    - `if` starts a decision.
    - `elif` adds another related option.
    - `else` handles the fallback case.
    - Python checks conditions from top to bottom.
    - Only the first true branch in a chain runs.
    - Good branching logic is ordered, readable, and easy to explain.
    """)


def lesson_02():
    write(ROOT / "02-nested-conditions-and-guard-clauses.md", r"""
    # Chapter 5.2: Nested Conditions and Guard Clauses

    Some decisions depend on earlier decisions. For example, an ATM should check your PIN before checking whether you have enough balance. A ticket booking system should check whether a seat is available before accepting payment. This is where nested conditions and guard clauses become useful.

    ![Nested conditions and guard clauses comparison](images/02-nested-vs-guard.svg)

    ## Learning Objectives

    By the end of this section, you will be able to:

    - Explain what nested conditions are.
    - Use nested `if` statements when one decision depends on another.
    - Recognize when nesting becomes hard to read.
    - Use guard clauses to handle invalid cases early.
    - Refactor deeply nested logic into cleaner code.
    - Choose between nesting and guard clauses thoughtfully.

    ## Simple Conceptual Explanation

    A nested condition is an `if` statement inside another `if` statement.

    Real-world comparison:

    - You first check if a shop is open.
    - If it is open, you check if the item is available.
    - If the item is available, you check if you have enough money.

    Each question only matters if the previous question passed.

    A guard clause is different. It says:

    > If something is wrong, stop early. Otherwise, continue with the main logic.

    Guard clauses are useful because they keep the normal path easier to read.

    ## Nested Conditions: Basic Example

    ```python
    has_ticket = True
    has_id = True

    if has_ticket:
        if has_id:
            print("You may enter.")
        else:
            print("Please show your ID.")
    else:
        print("Please buy a ticket first.")
    ```

    This is nested because the ID check happens only after the ticket check passes.

    ## Real-World Example: ATM Withdrawal

    ![ATM nested decision flow](images/02-atm-nested.svg)

    ```python
    pin_correct = True
    balance = 5000
    amount = 2000
    atm_has_cash = True

    if pin_correct:
        if balance >= amount:
            if atm_has_cash:
                print("Please collect your cash.")
            else:
                print("This ATM is temporarily out of cash.")
        else:
            print("Insufficient balance.")
    else:
        print("Incorrect PIN.")
    ```

    This structure matches the real process:

    1. No correct PIN means no withdrawal.
    2. No balance means no cash.
    3. No ATM cash means the transaction cannot continue.

    Nested logic is natural here because each later question depends on an earlier answer.

    ## The Problem with Deep Nesting

    Deep nesting can become hard to read:

    ```python
    if user_exists:
        if password_correct:
            if account_active:
                if not account_locked:
                    print("Login successful")
                else:
                    print("Account locked")
            else:
                print("Account inactive")
        else:
            print("Wrong password")
    else:
        print("User not found")
    ```

    The main success path is buried inside many levels. This makes the code harder to scan, test, and maintain.

    ## Guard Clauses

    A guard clause checks for a problem early and exits early.

    ```python
    user_exists = True
    password_correct = True
    account_active = True
    account_locked = False

    if not user_exists:
        print("Invalid login.")
    elif not password_correct:
        print("Invalid login.")
    elif not account_active:
        print("Account inactive.")
    elif account_locked:
        print("Account locked.")
    else:
        print("Login successful.")
    ```

    This version is flatter. The invalid cases are handled first, and the success case is easy to find.

    In functions, guard clauses become even cleaner because we can `return` early:

    ```python
    def can_login(user_exists, password_correct, account_active, account_locked):
        if not user_exists:
            return "Invalid login."
        if not password_correct:
            return "Invalid login."
        if not account_active:
            return "Account inactive."
        if account_locked:
            return "Account locked."

        return "Login successful."

    print(can_login(True, True, True, False))
    ```

    ![Guard clause validation flow](images/02-guard-validation.svg)

    ## When to Use Nested Conditions

    Use nesting when:

    - A later question truly depends on an earlier answer.
    - The logic forms a natural decision tree.
    - The nesting is shallow and still readable.

    Example:

    ```python
    is_logged_in = True
    role = "admin"

    if is_logged_in:
        if role == "admin":
            print("Show admin dashboard.")
        else:
            print("Show user dashboard.")
    else:
        print("Please log in.")
    ```

    ## When to Use Guard Clauses

    Use guard clauses when:

    - You want to reject invalid cases early.
    - Many conditions must be true before the main action.
    - Deep nesting makes the code difficult to read.
    - You are writing a function that can return early.

    Example:

    ```python
    def withdraw(balance, amount, pin_correct):
        if not pin_correct:
            return "Incorrect PIN."
        if amount <= 0:
            return "Amount must be positive."
        if amount > balance:
            return "Insufficient balance."

        return "Withdrawal approved."

    print(withdraw(5000, 2000, True))
    ```

    ## Mini Case Study: Ticket Booking

    A ticket booking system must protect the booking process from bad states:

    - The age must be valid.
    - The seat must be available.
    - Payment must succeed.
    - Only then should the ticket be booked.

    ![Ticket booking decision case study](images/02-ticket-case.svg)

    ```python
    def book_ticket(age, seat_available, payment_successful):
        if age < 0:
            return "Invalid age."
        if not seat_available:
            return "Please choose another seat."
        if not payment_successful:
            return "Payment failed. Try again."

        return "Ticket booked successfully."

    print(book_ticket(21, True, True))
    ```

    This is professional because invalid cases are handled before the success path.

    ## Common Mistakes

    ### Mistake 1: Nesting everything

    Beginners often write nested code even when each condition can be checked independently. This makes code harder to read.

    ### Mistake 2: Repeating the same error message everywhere

    If many branches print the same message, consider simplifying the logic.

    ### Mistake 3: Hiding the main action too deeply

    If the important action is far to the right because of indentation, the code may need guard clauses.

    ### Mistake 4: Using guard clauses without clear return or stop behavior

    A guard clause should actually stop the invalid path. In a function, that usually means `return`.

    ## Best Practices

    - Keep nesting shallow whenever possible.
    - Use functions when logic becomes large.
    - Use guard clauses for invalid or exceptional cases.
    - Make the main success path easy to see.
    - Do not combine unrelated decisions into one large condition.
    - Prefer clear messages and predictable behavior.

    ## Practice Exercises

    ### Beginner

    1. Write nested logic for entering a cinema:
       - The user must have a ticket.
       - If they have a ticket, check if they have an ID.
    2. Write a nested condition for a student:
       - If attendance is at least 75, check if assignment is submitted.
    3. Write a guard clause function that rejects a negative number.

    ### Intermediate

    1. Refactor a deeply nested login check into guard clauses.
    2. Build an ATM withdrawal function with checks for PIN, amount, balance, and daily limit.
    3. Create a course enrollment function:
       - reject if seats are full
       - reject if prerequisites are missing
       - approve otherwise

    ### Challenge

    Build a function called `approve_loan(age, income, credit_score, existing_debt)`:

    - Reject age below 18.
    - Reject income below 25000.
    - Reject credit score below 650.
    - Reject if existing debt is more than half the income.
    - Otherwise return `"Loan approved"`.

    Try one version with nested conditions and one version with guard clauses. Compare which one is easier to read.

    ## Key Takeaways

    - Nested conditions are useful when decisions depend on earlier decisions.
    - Too much nesting makes code harder to read.
    - Guard clauses handle invalid cases early.
    - Guard clauses make the main path easier to see.
    - Professional code is not just correct; it is readable and maintainable.
    """)


def lesson_03():
    write(ROOT / "03-match-case-readable-multi-way-choices.md", r"""
    # Chapter 5.3: `match-case` for Readable Multi-Way Choices

    Python's `match-case` statement helps you write clear code when one value can lead to many possible actions. It is especially helpful for menu choices, commands, roles, statuses, and categories.

    ![Match-case selection flow](images/03-match-selection.svg)

    ## Learning Objectives

    By the end of this section, you will be able to:

    - Explain what `match-case` does.
    - Use `match` to compare one value against several possible cases.
    - Use `case _` as a fallback.
    - Decide when `match-case` is cleaner than many `elif` statements.
    - Write readable menu-style and command-style logic.

    ## Simple Conceptual Explanation

    Imagine a food counter where you say one menu number:

    - `1` means pizza.
    - `2` means burger.
    - `3` means salad.
    - Anything else means "please choose again."

    That is a multi-way choice. One value points to one action.

    In Python, `match-case` lets us write this kind of logic in a clean structure.

    Important: `match-case` was introduced in Python 3.10. Use Python 3.10 or newer.

    ## Basic Syntax

    ```python
    command = "start"

    match command:
        case "start":
            print("Starting...")
        case "pause":
            print("Pausing...")
        case "stop":
            print("Stopping...")
        case _:
            print("Unknown command.")
    ```

    The underscore `_` means "anything else." It is the fallback case.

    ## Step-by-Step Python Examples

    ### Example 1: Simple Menu Choice

    ![Food order match-case flow](images/03-food-order-match.svg)

    ```python
    choice = 2

    match choice:
        case 1:
            print("You selected pizza.")
        case 2:
            print("You selected burger.")
        case 3:
            print("You selected salad.")
        case _:
            print("Invalid choice.")
    ```

    Python compares `choice` with each case. Since `choice` is `2`, it runs the burger branch.

    ### Example 2: User Role

    ```python
    role = "editor"

    match role:
        case "admin":
            print("Full access")
        case "editor":
            print("Can edit content")
        case "viewer":
            print("Can view content")
        case _:
            print("Unknown role")
    ```

    This is easier to scan than a long chain of equality checks.

    ### Example 3: Order Status

    ```python
    status = "shipped"

    match status:
        case "placed":
            message = "Your order has been placed."
        case "packed":
            message = "Your order is being packed."
        case "shipped":
            message = "Your order is on the way."
        case "delivered":
            message = "Your order has been delivered."
        case _:
            message = "Status unavailable."

    print(message)
    ```

    This kind of code appears in shopping apps, ticket systems, delivery apps, and dashboards.

    ## `match-case` vs `elif`

    ![Match-case versus elif comparison](images/03-match-vs-elif.svg)

    You can write the same idea using `elif`:

    ```python
    command = "pause"

    if command == "start":
        print("Starting")
    elif command == "pause":
        print("Pausing")
    elif command == "stop":
        print("Stopping")
    else:
        print("Unknown command")
    ```

    This is correct. But when there are many choices based on the same value, `match-case` can be easier to read:

    ```python
    command = "pause"

    match command:
        case "start":
            print("Starting")
        case "pause":
            print("Pausing")
        case "stop":
            print("Stopping")
        case _:
            print("Unknown command")
    ```

    Use `match-case` when one main value is being compared against many clear options.

    ## Real-World Examples

    `match-case` is useful for:

    - App navigation commands.
    - Food ordering menu choices.
    - Ticket categories.
    - User roles.
    - Payment status messages.
    - Customer support ticket routing.
    - Game controls such as move, jump, pause, or quit.

    ## Mini Case Study: Customer Support Routing

    A support system receives a ticket category and routes it to the right team.

    ![Support routing match-case case study](images/03-support-case.svg)

    ```python
    ticket_type = "technical"

    match ticket_type:
        case "billing":
            team = "Billing Support"
        case "technical":
            team = "Technical Support"
        case "account":
            team = "Account Support"
        case "feedback":
            team = "Customer Experience"
        case _:
            team = "General Triage"

    print("Route to:", team)
    ```

    This is realistic because many systems route work based on a category. If the category is unknown, the fallback prevents the system from failing silently.

    ## Common Mistakes

    ### Mistake 1: Forgetting `case _`

    Without a fallback, unexpected values may do nothing.

    ### Mistake 2: Using `match-case` for unrelated conditions

    This is not a good fit:

    ```python
    # Better with if/elif, not match-case
    if age >= 18 and has_id:
        print("Allowed")
    ```

    `match-case` is best when one value is being matched against options.

    ### Mistake 3: Using Python older than 3.10

    `match-case` will not work in Python 3.9 or older.

    ### Mistake 4: Making each case too large

    If a case has many lines, consider moving the work into a function.

    ## Best Practices

    - Use `match-case` for menu-like choices.
    - Include a `case _` fallback.
    - Keep each case short and focused.
    - Use clear values such as strings, numbers, or named constants.
    - Use `if` when conditions are range-based or involve multiple unrelated checks.
    - Use functions if each case performs a larger action.

    ## Practice Exercises

    ### Beginner

    1. Write a program that matches a traffic light color:
       - red -> stop
       - yellow -> wait
       - green -> go
       - anything else -> invalid color
    2. Match a day number from 1 to 7 and print the weekday name.
    3. Match a simple calculator operation: `+`, `-`, `*`, `/`.

    ### Intermediate

    1. Create a food menu using `match-case`.
    2. Build a help desk router for ticket types: billing, technical, account, feedback.
    3. Create a game command handler for: start, pause, resume, quit.

    ### Challenge

    Build a command-line banking menu:

    - `1` -> check balance
    - `2` -> deposit
    - `3` -> withdraw
    - `4` -> show last transaction
    - any other option -> show help

    Use `match-case`, and keep each case readable.

    ## Key Takeaways

    - `match-case` is for readable multi-way choices.
    - It works best when one value controls the decision.
    - `case _` is the fallback.
    - Use `if` / `elif` for ranges or complex logical conditions.
    - `match-case` can make menus, commands, roles, and statuses easier to maintain.
    """)


def lesson_04():
    write(ROOT / "04-input-validation-and-defensive-decisions.md", r"""
    # Chapter 5.4: Input Validation and Defensive Decision-Making

    User input is uncertain. A user may type letters when you expect numbers, leave fields empty, enter impossible values, or try something your program was not designed for. Defensive decision-making means writing code that expects problems and handles them calmly.

    ![Input validation pipeline](images/04-validation-pipeline.svg)

    ## Learning Objectives

    By the end of this section, you will be able to:

    - Explain why input validation is necessary.
    - Check for empty, invalid, or out-of-range input.
    - Convert input safely before using it.
    - Use conditions to protect important program logic.
    - Write helpful error messages.
    - Build defensive decision flows for realistic programs.

    ## Simple Conceptual Explanation

    Think of input validation like a security check at an airport.

    Before a person boards a flight:

    - The ticket is checked.
    - The ID is checked.
    - The baggage is checked.
    - Only then can the person board.

    A program should do the same with input:

    - Is it present?
    - Is it the right type?
    - Is it in the allowed range?
    - Is it safe to use?

    Defensive code does not trust input blindly. It checks first, then acts.

    ## Why Input Needs Validation

    In Python, `input()` always gives you a string.

    ```python
    age = input("Enter your age: ")
    print(type(age))
    ```

    Even if the user types `21`, Python receives `"21"` as text. If you want to compare it as a number, you must convert it first.

    ## Step-by-Step Python Examples

    ### Example 1: Empty Input

    ```python
    name = input("Enter your name: ").strip()

    if name == "":
        print("Name cannot be empty.")
    else:
        print("Welcome,", name)
    ```

    `.strip()` removes extra spaces from the beginning and end. This prevents `"   "` from being accepted as a real name.

    ### Example 2: Safe Number Conversion

    ![Try except conversion flow](images/04-try-except-flow.svg)

    ```python
    age_text = input("Enter your age: ")

    try:
        age = int(age_text)
        print("Age entered:", age)
    except ValueError:
        print("Please enter a whole number.")
    ```

    Without `try` / `except`, the program would crash if the user typed `"twenty"`.

    ### Example 3: Range Validation

    ```python
    age_text = input("Enter your age: ")

    try:
        age = int(age_text)

        if age < 0:
            print("Age cannot be negative.")
        elif age > 120:
            print("Please enter a realistic age.")
        elif age >= 18:
            print("You are eligible.")
        else:
            print("You are not eligible yet.")

    except ValueError:
        print("Please enter a valid number.")
    ```

    This example validates type and range before making the final eligibility decision.

    ### Example 4: Form Validation

    ![Form validation decision flow](images/04-form-validation.svg)

    ```python
    email = input("Email: ").strip()
    password = input("Password: ").strip()

    if "@" not in email:
        print("Please enter a valid email address.")
    elif len(password) < 8:
        print("Password must be at least 8 characters.")
    else:
        print("Account can be created.")
    ```

    This is simple, but it shows the idea: reject bad input before saving or using it.

    ## Defensive Decision-Making

    Defensive decision-making means asking:

    > What could go wrong, and how should the program respond?

    Example:

    ```python
    def calculate_discount(cart_total):
        if cart_total < 0:
            return "Cart total cannot be negative."
        if cart_total == 0:
            return "Cart is empty."
        if cart_total >= 5000:
            return "Apply 20% discount."
        if cart_total >= 2000:
            return "Apply 10% discount."

        return "No discount."

    print(calculate_discount(3200))
    ```

    The function handles invalid and unusual values before applying business rules.

    ## Real-World Examples

    Input validation appears in:

    - Signup forms.
    - ATM withdrawal screens.
    - Payment forms.
    - Ticket booking systems.
    - Online exam submissions.
    - Search boxes.
    - Food delivery address forms.

    ## Mini Case Study: Defensive ATM Withdrawal

    An ATM cannot simply accept any amount. It must check whether the input is a number, positive, available in valid note multiples, and within the user's balance.

    ![Defensive ATM validation case study](images/04-atm-defensive-case.svg)

    ```python
    def validate_withdrawal(amount_text, balance):
        try:
            amount = int(amount_text)
        except ValueError:
            return "Please enter a valid number."

        if amount <= 0:
            return "Amount must be greater than zero."
        if amount % 100 != 0:
            return "Amount must be in multiples of 100."
        if amount > balance:
            return "Insufficient balance."

        return "Withdrawal approved."

    print(validate_withdrawal("2000", 5000))
    print(validate_withdrawal("abc", 5000))
    ```

    This is defensive because the function expects bad input and handles it safely.

    ## Common Mistakes

    ### Mistake 1: Trusting input too early

    ```python
    age = int(input("Age: "))
    ```

    This crashes if the user types non-numeric text.

    ### Mistake 2: Checking range before conversion

    ```python
    age = input("Age: ")

    if age > 18:
        print("Adult")
    ```

    `age` is text here, not a number.

    ### Mistake 3: Giving vague error messages

    Bad:

    ```python
    print("Error")
    ```

    Better:

    ```python
    print("Password must be at least 8 characters.")
    ```

    ### Mistake 4: Mixing validation and main logic too much

    If validation becomes long, move it into a function.

    ## Best Practices

    - Validate before processing.
    - Convert input safely using `try` / `except`.
    - Use `.strip()` for text fields.
    - Give helpful error messages.
    - Keep validation rules close to the input they protect.
    - Use functions for repeated validation.
    - Handle invalid, empty, and extreme values.
    - Never assume the user will type exactly what you expect.

    ## Practice Exercises

    ### Beginner

    1. Ask for a name and reject empty input.
    2. Ask for an age and reject negative values.
    3. Ask for a password and check that it has at least 8 characters.

    ### Intermediate

    1. Build a marks validator:
       - input must be a number
       - marks must be between 0 and 100
    2. Build an email checker that verifies the email contains `@` and `.`.
    3. Build a withdrawal validator that rejects negative amounts and amounts greater than balance.

    ### Challenge

    Build a signup validator function:

    - Name cannot be empty.
    - Email must contain `@`.
    - Password must be at least 8 characters.
    - Age must be a valid integer.
    - Age must be 13 or above.

    Return a helpful message for the first failed rule. If all rules pass, return `"Signup successful"`.

    ## Key Takeaways

    - User input is always uncertain.
    - `input()` returns text, even when the user types a number.
    - Validate before using input in important decisions.
    - Use `try` / `except` for safe conversion.
    - Defensive code prevents crashes and improves user experience.
    - Professional programs respond clearly when input is invalid.
    """)


def main():
    ROOT.mkdir(parents=True, exist_ok=True)
    IMAGES.mkdir(parents=True, exist_ok=True)
    build_svgs()
    chapter_readme()
    lesson_01()
    lesson_02()
    lesson_03()
    lesson_04()


if __name__ == "__main__":
    main()
