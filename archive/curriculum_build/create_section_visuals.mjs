import fs from "node:fs/promises";
import { existsSync } from "node:fs";
import path from "node:path";
import { chromium } from "playwright";

const outputDir = "/Users/suman/Desktop/ByteXL/Unit 1/section_images";
await fs.mkdir(outputDir, { recursive: true });

const W = 1200;
const H = 1600;

function esc(text) {
  return String(text)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function icon(label, emoji, color = "blue") {
  return `<div class="icon ${color}"><span>${emoji}</span><small>${esc(label)}</small></div>`;
}

function miniCard(title, body, emoji = "•", color = "blue") {
  return `<div class="mini-card ${color}"><div class="mini-emoji">${emoji}</div><div><h3>${esc(title)}</h3><p>${esc(body)}</p></div></div>`;
}

function step(label, title, body, color = "blue") {
  return `<div class="step ${color}"><b>${esc(label)}</b><h3>${esc(title)}</h3><p>${esc(body)}</p></div>`;
}

function flow(items) {
  return `<div class="flow">${items.map((item, i) => `
    <div class="flow-item ${item.color ?? "blue"}">
      <div class="flow-icon">${item.emoji}</div>
      <strong>${esc(item.title)}</strong>
      <span>${esc(item.body)}</span>
    </div>
    ${i < items.length - 1 ? `<div class="arrow">→</div>` : ""}
  `).join("")}</div>`;
}

const sections = [
  {
    file: "00_opening_learning_objectives.png",
    eyebrow: "SECTION 0",
    title: "Why Programming Matters",
    subtitle: "A visual roadmap for a first-time coder",
    visual: `
      <div class="hero-split">
        <div class="big-idea">
          <div class="code-mark">&lt;/&gt;</div>
          <h2>From using apps<br/>to building them</h2>
          <p>Students begin by seeing programming as a way to give clear instructions and create useful digital tools.</p>
        </div>
        <div class="learner-scene">
          <div class="student">👨‍💻</div>
          <div class="thought t1">Explain</div>
          <div class="thought t2">Recognise</div>
          <div class="thought t3">Describe</div>
          <div class="thought t4">Write</div>
          <div class="thought t5">Read Code</div>
        </div>
      </div>
      <div class="roadmap">
        ${step("1", "Notice technology", "Spot programs behind daily apps.", "blue")}
        ${step("2", "Think in steps", "Break tasks into clear instructions.", "green")}
        ${step("3", "Read first code", "Understand what print(...) does.", "purple")}
        ${step("4", "Feel ready", "Start coding without fear.", "orange")}
      </div>
      <div class="note-card"><b>Core message:</b> You do not need prior experience. Programming begins with clear thinking.</div>
    `,
  },
  {
    file: "01_simple_introduction.png",
    eyebrow: "SECTION 1",
    title: "A Simple Introduction",
    subtitle: "Programming is hidden inside ordinary moments",
    visual: `
      <div class="morning-map">
        ${icon("Alarm", "⏰", "blue")}
        ${icon("Chat", "💬", "green")}
        ${icon("Food", "🍽️", "orange")}
        ${icon("Maps", "🗺️", "purple")}
        ${icon("ATM", "🏧", "pink")}
        <div class="center-code"><span>&lt;/&gt;</span><b>Instructions</b><small>behind every app</small></div>
      </div>
      ${flow([
        { emoji: "👤", title: "Human goal", body: "I want something done", color: "blue" },
        { emoji: "📝", title: "Program", body: "Clear ordered instructions", color: "green" },
        { emoji: "💻", title: "Computer", body: "Runs the instructions", color: "purple" },
        { emoji: "✅", title: "Result", body: "Useful output appears", color: "orange" },
      ])}
      <div class="quote">Programming is how humans talk to computers and tell them what to do.</div>
    `,
  },
  {
    file: "02_what_is_programming.png",
    eyebrow: "SECTION 2",
    title: "What is Programming?",
    subtitle: "Clear steps turn intent into action",
    visual: `
      <div class="definition-board">
        <div class="def-left">
          <h2>Computer</h2>
          <p>Fast, powerful, literal.</p>
          <div class="machine">💻</div>
          <small>No guessing. No common sense. Only instructions.</small>
        </div>
        <div class="def-right">
          ${step("A", "Input", "What the user gives.", "blue")}
          ${step("B", "Processing", "Rules and steps the program follows.", "green")}
          ${step("C", "Output", "What the computer shows or does.", "orange")}
        </div>
      </div>
      <div class="examples-grid">
        ${miniCard("Making tea", "Water + steps → tea", "☕", "orange")}
        ${miniCard("Food order", "Cart + payment → order placed", "🛵", "green")}
        ${miniCard("Maps", "Location + destination → route", "🗺️", "purple")}
        ${miniCard("ATM", "Card + PIN + amount → cash", "💳", "blue")}
      </div>
    `,
  },
  {
    file: "03_literal_helper_analogy.png",
    eyebrow: "SECTION 3",
    title: "The Literal Helper",
    subtitle: "Computers follow exactly what we say",
    visual: `
      <div class="helper-scene">
        <div class="helper">🤖</div>
        <div class="speech">“I will do every step exactly. Please do not skip anything.”</div>
      </div>
      <div class="sandwich-flow">
        ${step("1", "Take bread", "Start with the first exact action.", "blue")}
        ${step("2", "Open jar", "Important hidden step.", "orange")}
        ${step("3", "Spread butter", "Now the action makes sense.", "green")}
        ${step("4", "Serve", "Finish only after all steps.", "purple")}
      </div>
      <div class="warning-card">If a step is missing, the computer does not “figure it out.” It simply follows the incomplete program.</div>
    `,
  },
  {
    file: "04_why_need_programming.png",
    eyebrow: "SECTION 4",
    title: "Why Do We Need Programming?",
    subtitle: "Programming turns problems into tools",
    visual: `
      <div class="impact-wheel">
        <div class="wheel-center">Solve<br/>Real<br/>Problems</div>
        ${icon("Apps", "📱", "blue")}
        ${icon("Web", "🌐", "green")}
        ${icon("Games", "🎮", "purple")}
        ${icon("Automation", "⚙️", "orange")}
        ${icon("Banking", "🏦", "pink")}
        ${icon("AI", "✨", "blue")}
      </div>
      <div class="creator-card">
        <h2>User → Creator</h2>
        <p>Learning programming means you can stop only consuming technology and start building it.</p>
      </div>
    `,
  },
  {
    file: "05_mini_case_studies.png",
    eyebrow: "SECTION 5",
    title: "Mini Case Studies",
    subtitle: "Apps are workflows made of decisions",
    visual: `
      <div class="case-columns">
        <div class="case-card food">
          <h2>Food Delivery</h2>
          <p>Location → restaurant → bill → partner → tracking</p>
          <div class="case-icon">🍱</div>
        </div>
        <div class="case-card maps">
          <h2>Maps</h2>
          <p>Current place → destination → traffic → fastest route</p>
          <div class="case-icon">🧭</div>
        </div>
        <div class="case-card atm">
          <h2>ATM</h2>
          <p>Card → PIN check → balance check → cash</p>
          <div class="case-icon">🏧</div>
        </div>
      </div>
      <div class="decision-strip">
        <span>If PIN is correct</span><b>→</b><span>continue</span><b>else</b><span>show error</span>
      </div>
    `,
  },
  {
    file: "06_english_to_code.png",
    eyebrow: "SECTION 6",
    title: "From English to Code",
    subtitle: "A recipe is already close to a program",
    visual: `
      ${flow([
        { emoji: "☕", title: "Plain task", body: "Make tea", color: "orange" },
        { emoji: "🪜", title: "Ordered steps", body: "Boil, add, wait, pour", color: "blue" },
        { emoji: "🧠", title: "Logic", body: "One clear action at a time", color: "green" },
        { emoji: "💻", title: "Code", body: "Computer-readable instructions", color: "purple" },
      ])}
      <div class="two-panel">
        <div><h3>English steps</h3><ol><li>Get water</li><li>Heat water</li><li>Add tea</li><li>Serve</li></ol></div>
        <div><h3>Programming thinking</h3><ol><li>Clear goal</li><li>Correct order</li><li>Simple actions</li><li>Expected result</li></ol></div>
      </div>
    `,
  },
  {
    file: "07_first_python.png",
    eyebrow: "SECTION 7",
    title: "Your First Look at Python",
    subtitle: "Python reads close to English",
    visual: `
      <div class="code-window">
        <div class="window-bar"><span></span><span></span><span></span></div>
        <pre><code>print("Hello, World!")</code></pre>
      </div>
      ${flow([
        { emoji: "print", title: "Command", body: "show something", color: "blue" },
        { emoji: "( )", title: "Brackets", body: "hold the message", color: "green" },
        { emoji: "“ ”", title: "Quotes", body: "text lives here", color: "purple" },
        { emoji: "📺", title: "Output", body: "Hello, World!", color: "orange" },
      ])}
      <div class="screen-output">Hello, World!</div>
    `,
  },
  {
    file: "08_common_misconceptions.png",
    eyebrow: "SECTION 8",
    title: "Common Misconceptions",
    subtitle: "Myths should not block the first step",
    visual: `
      <div class="myth-grid">
        ${miniCard("Myth", "Only geniuses can program.", "❌", "pink")}
        ${miniCard("Reality", "Programming is a learnable skill.", "✅", "green")}
        ${miniCard("Myth", "You must be great at maths.", "❌", "pink")}
        ${miniCard("Reality", "Logic and practice matter more at the start.", "✅", "green")}
        ${miniCard("Myth", "Errors mean failure.", "❌", "pink")}
        ${miniCard("Reality", "Errors are clues for learning.", "✅", "green")}
      </div>
      <div class="quote">“I’m not bad at programming — I’m just early in learning it.”</div>
    `,
  },
  {
    file: "09_student_reflection.png",
    eyebrow: "SECTION 9",
    title: "Student Reflection Activity",
    subtitle: "Connect programming to your own life",
    visual: `
      <div class="reflection-scene">
        <div class="student-large">🧑‍🎓</div>
        <div class="bubble b1">Which apps did I use today?</div>
        <div class="bubble b2">What happens when I tap a button?</div>
        <div class="bubble b3">Which boring task can be automated?</div>
        <div class="bubble b4">How do I feel about coding?</div>
      </div>
      <div class="activity-card">Reflection turns coding from an abstract subject into something connected to daily life.</div>
    `,
  },
  {
    file: "10_practice_exercise.png",
    eyebrow: "SECTION 10",
    title: "Small Practice Exercise",
    subtitle: "Think like a programmer before writing code",
    visual: `
      <div class="checklist-board">
        <h2>Choose one everyday task</h2>
        <div class="task-chips"><span>Brush teeth</span><span>Make toast</span><span>Send message</span><span>Pack bag</span></div>
        <div class="rules">
          ${step("1", "Number each step", "Keep order clear.", "blue")}
          ${step("2", "One action per line", "Avoid mixing actions.", "green")}
          ${step("3", "Do not skip hidden steps", "Remember the closed jar.", "orange")}
          ${step("4", "Read it aloud", "Would a literal helper succeed?", "purple")}
        </div>
      </div>
    `,
  },
  {
    file: "11_summary.png",
    eyebrow: "SECTION 11",
    title: "Summary",
    subtitle: "One clear idea everything builds on",
    visual: `
      <div class="summary-map">
        <div class="summary-center">Programming</div>
        <div class="node n1">Clear steps</div>
        <div class="node n2">No common sense</div>
        <div class="node n3">Daily apps</div>
        <div class="node n4">First Python line</div>
        <div class="node n5">Mistakes help</div>
      </div>
      ${flow([
        { emoji: "📥", title: "Input", body: "What goes in", color: "blue" },
        { emoji: "⚙️", title: "Processing", body: "What happens", color: "green" },
        { emoji: "📤", title: "Output", body: "What comes out", color: "orange" },
      ])}
      <div class="next-card">Next: Inputs, Processing, and Outputs</div>
    `,
  },
];

function htmlFor(section) {
  return `<!doctype html>
<html>
<head>
<meta charset="utf-8" />
<style>
  * { box-sizing: border-box; }
  body {
    margin: 0;
    width: ${W}px;
    height: ${H}px;
    font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    background:
      radial-gradient(circle at 80% 8%, #dce9ff 0, transparent 26%),
      radial-gradient(circle at 20% 92%, #e9ddff 0, transparent 24%),
      linear-gradient(135deg, #ffffff 0%, #f5f8ff 55%, #edf4ff 100%);
    color: #101b3d;
  }
  .page { width: ${W}px; height: ${H}px; padding: 58px 62px; position: relative; overflow: hidden; border: 1px solid #c7d4ed; }
  .page:before { content: "</>"; position: absolute; top: 30px; left: 44px; color: #9fb1f3; font-weight: 900; font-size: 42px; }
  .page:after { content: "+"; position: absolute; top: 78px; right: 64px; color: #9fb1f3; font-weight: 900; font-size: 34px; }
  .top { margin-top: 36px; }
  .eyebrow { color: #6a4bc3; font-size: 22px; font-weight: 900; letter-spacing: 2px; text-transform: uppercase; }
  h1 { font-size: 70px; line-height: 0.98; margin: 14px 0 18px; letter-spacing: -2px; color: #07165d; }
  .subtitle { font-size: 31px; line-height: 1.35; color: #2b2e43; max-width: 900px; font-weight: 600; font-style: italic; }
  .accent { width: 92px; height: 8px; border-radius: 99px; background: #f7b500; margin: 28px 0 42px; }
  .visual { position: relative; }
  .card, .note-card, .quote, .activity-card, .warning-card, .next-card, .creator-card {
    background: rgba(255,255,255,.86);
    border: 2px solid #cdbdf4;
    box-shadow: 0 18px 60px rgba(33,40,94,.08);
    border-radius: 28px;
    padding: 30px;
  }
  .hero-split { display: grid; grid-template-columns: 1fr 1fr; gap: 34px; align-items: center; }
  .big-idea { border-radius: 34px; padding: 38px; background: #f4edff; border: 2px solid #d9c9ff; min-height: 470px; }
  .big-idea h2 { font-size: 50px; line-height: 1.05; margin: 20px 0; color: #5b2bb8; }
  .big-idea p { font-size: 25px; line-height: 1.4; }
  .code-mark { font-size: 54px; font-weight: 900; color: #1a53bd; }
  .learner-scene { position: relative; height: 500px; border-radius: 34px; background: linear-gradient(160deg,#eaf3ff,#f6edff); border: 2px solid #d8e4ff; }
  .student { font-size: 210px; position: absolute; left: 118px; top: 120px; }
  .thought, .bubble { position: absolute; background: white; border: 2px dashed #bca9ee; border-radius: 999px; padding: 14px 20px; font-size: 22px; font-weight: 800; color: #5b2bb8; }
  .t1 { left: 40px; top: 35px; } .t2 { right: 30px; top: 68px; } .t3 { left: 30px; bottom: 110px; } .t4 { right: 45px; bottom: 55px; } .t5 { right: 18px; top: 210px; }
  .roadmap, .sandwich-flow, .rules { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin-top: 34px; }
  .step { border-radius: 24px; padding: 22px; background: white; border: 2px solid #d9e4fb; min-height: 178px; }
  .step b { width: 42px; height: 42px; display: grid; place-items: center; border-radius: 50%; color: white; background: #2563eb; font-size: 22px; }
  .step h3, .mini-card h3 { margin: 14px 0 8px; font-size: 24px; color: #07165d; }
  .step p, .mini-card p { margin: 0; font-size: 19px; line-height: 1.35; }
  .step.green b { background: #16a34a; } .step.orange b { background: #f97316; } .step.purple b { background: #6d3bc2; }
  .note-card, .warning-card, .activity-card, .next-card { margin-top: 34px; font-size: 27px; line-height: 1.35; background: #fff7d9; border-color: #f4c542; }
  .quote { margin-top: 38px; font-size: 38px; line-height: 1.25; color: #5b2bb8; font-weight: 900; text-align: center; background: #faf7ff; }
  .morning-map { position: relative; height: 560px; border-radius: 36px; border: 2px solid #d7e4ff; background: #f8fbff; }
  .icon { position: relative; display: inline-grid; place-items: center; width: 150px; height: 150px; border-radius: 34px; margin: 34px; color: white; font-weight: 900; box-shadow: 0 14px 30px rgba(0,0,0,.12); }
  .icon span { font-size: 56px; } .icon small { font-size: 18px; }
  .icon.blue { background: #2563eb; } .icon.green { background: #16a34a; } .icon.orange { background: #f97316; } .icon.purple { background: #6d3bc2; } .icon.pink { background: #db2777; }
  .center-code { position: absolute; left: 50%; top: 50%; transform: translate(-50%,-50%); width: 260px; height: 260px; background: #07165d; color: white; border-radius: 50%; display: grid; place-items: center; text-align: center; box-shadow: 0 20px 50px rgba(7,22,93,.24); }
  .center-code span { font-size: 58px; font-weight: 900; } .center-code b { font-size: 30px; } .center-code small { font-size: 18px; }
  .flow { display: flex; align-items: stretch; gap: 14px; margin: 36px 0; }
  .flow-item { flex: 1; min-height: 190px; border-radius: 26px; padding: 24px 18px; text-align: center; border: 2px solid #d7e4ff; background: white; }
  .flow-icon { font-size: 48px; margin-bottom: 12px; font-weight: 900; color: #5b2bb8; }
  .flow-item strong { display: block; font-size: 24px; color: #07165d; margin-bottom: 8px; }
  .flow-item span { font-size: 18px; line-height: 1.25; }
  .flow-item.blue { background:#e7f0ff; } .flow-item.green { background:#e7f6ea; } .flow-item.purple { background:#eee7ff; } .flow-item.orange { background:#fff2cc; }
  .arrow { display: grid; place-items: center; font-size: 42px; color: #6d3bc2; font-weight: 900; }
  .definition-board { display: grid; grid-template-columns: .9fr 1.1fr; gap: 26px; }
  .def-left { border-radius: 34px; padding: 34px; background:#07165d; color:white; min-height: 520px; }
  .def-left h2 { font-size: 42px; margin: 0 0 10px; } .def-left p { font-size: 26px; } .machine { font-size: 170px; text-align:center; margin: 50px 0; }
  .def-left small { font-size: 22px; line-height: 1.35; display: block; }
  .def-right { display: grid; gap: 18px; }
  .examples-grid, .myth-grid { display:grid; grid-template-columns: repeat(2, 1fr); gap: 20px; margin-top: 34px; }
  .mini-card { display:flex; gap: 18px; align-items: center; border-radius: 24px; padding: 22px; min-height: 140px; border: 2px solid #d7e4ff; }
  .mini-emoji { font-size: 46px; }
  .mini-card.blue { background:#e7f0ff; } .mini-card.green { background:#e7f6ea; } .mini-card.orange { background:#fff2cc; } .mini-card.purple { background:#eee7ff; } .mini-card.pink { background:#ffe4ef; }
  .helper-scene { position: relative; height: 480px; border-radius: 34px; background: linear-gradient(135deg,#eaf3ff,#fff7d9); border: 2px solid #d7e4ff; }
  .helper { font-size: 220px; position:absolute; left: 110px; top: 110px; }
  .speech { position:absolute; right:70px; top:100px; width: 480px; background:white; border: 3px solid #6d3bc2; border-radius: 34px; padding: 32px; font-size: 32px; line-height: 1.25; font-weight:900; color:#5b2bb8; }
  .impact-wheel { height: 650px; position: relative; border-radius: 34px; background:#f8fbff; border:2px solid #d7e4ff; }
  .wheel-center { position:absolute; left:50%; top:50%; transform:translate(-50%,-50%); width:260px; height:260px; border-radius:50%; background:#07165d; color:white; display:grid; place-items:center; text-align:center; font-size:34px; font-weight:900; line-height:1.05; }
  .impact-wheel .icon:nth-child(2){position:absolute;left:90px;top:60px}.impact-wheel .icon:nth-child(3){position:absolute;right:90px;top:60px}.impact-wheel .icon:nth-child(4){position:absolute;left:60px;bottom:75px}.impact-wheel .icon:nth-child(5){position:absolute;right:60px;bottom:75px}.impact-wheel .icon:nth-child(6){position:absolute;left:420px;top:20px}.impact-wheel .icon:nth-child(7){position:absolute;left:420px;bottom:30px}
  .creator-card h2 { font-size: 42px; margin:0 0 8px; color:#5b2bb8; } .creator-card p {font-size:26px; margin:0;}
  .case-columns { display:grid; grid-template-columns: repeat(3, 1fr); gap: 22px; }
  .case-card { min-height: 560px; border-radius: 32px; padding: 28px; border:2px solid #d7e4ff; display:flex; flex-direction:column; justify-content:space-between; }
  .case-card h2 { font-size: 34px; margin:0; color:#07165d; } .case-card p { font-size:25px; line-height:1.35; } .case-icon { font-size:130px; text-align:center; }
  .food {background:#fff2cc}.maps{background:#e7f0ff}.atm{background:#eee7ff}
  .decision-strip { margin-top:34px; display:flex; gap:18px; align-items:center; justify-content:center; background:#07165d; color:white; border-radius:28px; padding:30px; font-size:28px; font-weight:900; }
  .two-panel { display:grid; grid-template-columns:1fr 1fr; gap:24px; margin-top:38px; }
  .two-panel div { background:white; border:2px solid #d7e4ff; border-radius:28px; padding:28px; }
  .two-panel h3 { font-size:32px; margin:0 0 16px; color:#5b2bb8; } .two-panel li { font-size:25px; margin:12px 0; }
  .code-window { border-radius:32px; overflow:hidden; background:#07165d; color:white; box-shadow: 0 22px 55px rgba(7,22,93,.24); }
  .window-bar { height:58px; background:#172554; display:flex; gap:12px; align-items:center; padding:0 24px; }
  .window-bar span { width:18px; height:18px; border-radius:50%; background:#f87171; } .window-bar span:nth-child(2){background:#fbbf24}.window-bar span:nth-child(3){background:#34d399}
  pre { margin:0; padding:58px; font-size:58px; line-height:1.2; }
  .screen-output { margin-top:30px; background:#111827; color:#34d399; border-radius:24px; padding:28px; font-size:42px; text-align:center; font-family: ui-monospace, SFMono-Regular, Menlo, monospace; }
  .reflection-scene { position:relative; height:720px; border-radius:36px; background:#f8fbff; border:2px solid #d7e4ff; }
  .student-large { position:absolute; left:390px; top:250px; font-size:190px; }
  .bubble { font-size:27px; max-width:360px; white-space:normal; line-height:1.2; }
  .b1{left:70px;top:90px}.b2{right:70px;top:130px}.b3{left:90px;bottom:130px}.b4{right:85px;bottom:105px}
  .checklist-board { border-radius:36px; background:#f8fbff; border:2px solid #d7e4ff; padding:36px; }
  .checklist-board h2 { font-size:42px; color:#07165d; margin:0 0 24px; }
  .task-chips { display:flex; gap:14px; flex-wrap:wrap; margin-bottom:30px; }
  .task-chips span { background:#e7f0ff; border:2px solid #bdd3ff; border-radius:999px; padding:12px 20px; font-size:22px; font-weight:800; color:#1d4ed8; }
  .summary-map { position:relative; height:630px; border-radius:36px; background:#f8fbff; border:2px solid #d7e4ff; }
  .summary-center { position:absolute; left:50%; top:50%; transform:translate(-50%,-50%); width:250px; height:250px; border-radius:50%; background:#5b2bb8; color:white; display:grid; place-items:center; font-size:36px; font-weight:900; }
  .node { position:absolute; background:white; border:3px solid #cdbdf4; border-radius:999px; padding:20px 28px; font-size:26px; font-weight:900; color:#07165d; }
  .n1{left:85px;top:90px}.n2{right:85px;top:95px}.n3{left:70px;bottom:120px}.n4{right:70px;bottom:125px}.n5{left:410px;top:42px}
  .next-card { background:#e7f6ea; border-color:#47b881; color:#17613d; text-align:center; font-weight:900; }
</style>
</head>
<body>
<main class="page">
  <section class="top">
    <div class="eyebrow">${esc(section.eyebrow)}</div>
    <h1>${esc(section.title)}</h1>
    <div class="subtitle">${esc(section.subtitle)}</div>
    <div class="accent"></div>
  </section>
  <section class="visual">${section.visual}</section>
</main>
</body>
</html>`;
}

const chromePath = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const browser = await chromium.launch({
  headless: true,
  ...(existsSync(chromePath) ? { executablePath: chromePath } : {}),
});
const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 2 });

for (const section of sections) {
  await page.setContent(htmlFor(section), { waitUntil: "networkidle" });
  const out = path.join(outputDir, section.file);
  await page.screenshot({ path: out, fullPage: false });
  console.log(out);
}

await browser.close();

const index = sections
  .map((s, i) => `${String(i).padStart(2, "0")}. ${s.title} -> ${s.file}`)
  .join("\n");
await fs.writeFile(path.join(outputDir, "README.txt"), index + "\n");
