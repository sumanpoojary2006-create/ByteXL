function apiBase() {
  const configured = location.protocol === "file:"
    ? "http://127.0.0.1:8000"
    : String(window.IMAGE_CONVERTER_CONFIG?.apiBase || location.origin).trim();
  const api = new URL(configured, location.href);
  const isVercel = api.hostname === "vercel.app" || api.hostname.endsWith(".vercel.app");
  if (isVercel) throw new Error("Configure the external content API before using this page.");
  return api.origin;
}

const API_BASE = apiBase();
const state = { plan: null, publish: null, loading: false, creating: false, publishing: false, collapsed: new Set() };
const $ = (id) => document.getElementById(id);

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

// The API can be a cold Render instance, so a first request that never lands is
// expected rather than a failure worth reporting.
const WAKE_UP_RETRY_DELAYS_MS = [4000, 10000, 20000];
const wait = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

async function request(path, options = {}) {
  for (let attempt = 0; ; attempt++) {
    let response;
    try {
      response = await fetch(`${API_BASE}${path}`, {
        ...options,
        headers: { "Content-Type": "application/json", ...(options.headers || {}) }
      });
    } catch (networkError) {
      if (attempt >= WAKE_UP_RETRY_DELAYS_MS.length) {
        throw new Error("Could not reach the content API after several attempts. The free Render instance may still be waking up — wait a moment and try again.");
      }
      showMessage(`The API service looks idle and is waking up — retrying in a few seconds (attempt ${attempt + 2} of ${WAKE_UP_RETRY_DELAYS_MS.length + 1})…`);
      await wait(WAKE_UP_RETRY_DELAYS_MS[attempt]);
      continue;
    }
    let body;
    try { body = await response.json(); } catch { body = {}; }
    if (!response.ok) throw new Error(body.detail || body.message || `Request failed (${response.status})`);
    return body;
  }
}

function showMessage(text, kind = "") {
  const node = $("message");
  node.hidden = !text;
  node.className = `message${kind ? ` ${kind}` : ""}`;
  node.textContent = text || "";
}

function statLabel(value, label, tone = "") {
  return `<div class="stat${tone ? ` ${tone}` : ""}"><strong>${escapeHtml(value)}</strong><span>${escapeHtml(label)}</span></div>`;
}

async function loadBlueprints() {
  const select = $("blueprint");
  try {
    const { items = [] } = await request("/course-builder/blueprints");
    if (!items.length) {
      select.innerHTML = `<option value="">No blueprints found</option>`;
      showMessage("No blueprints are installed on the server.", "error");
      return;
    }
    select.innerHTML = items
      .map((item) => {
        const code = item.courseCode ? `${item.courseCode} — ` : "";
        return `<option value="${escapeHtml(item.slug)}">${escapeHtml(code + item.title)} (${item.topics} topics)</option>`;
      })
      .join("");
    showMessage("");
  } catch (error) {
    select.innerHTML = `<option value="">Could not load blueprints</option>`;
    showMessage(error.message, "error");
  }
}

async function loadPlan(refresh = false) {
  const slug = $("blueprint").value;
  if (!slug || state.loading) return;
  state.loading = true;
  $("load").disabled = true;
  $("refresh").disabled = true;
  showMessage(refresh
    ? "Re-reading every donor page from ByteXL — this takes about a minute…"
    : "Resolving the blueprint against ByteXL…");
  try {
    const { plan } = await request(`/course-builder/plan?slug=${encodeURIComponent(slug)}${refresh ? "&refresh=true" : ""}`);
    state.plan = plan;
    state.collapsed = new Set();
    render();
    showMessage("");
  } catch (error) {
    state.plan = null;
    render();
    showMessage(error.message, "error");
  } finally {
    state.loading = false;
    $("load").disabled = false;
    $("refresh").disabled = false;
  }
}

function renderSyllabus(plan) {
  const syllabus = plan.syllabus || {};
  const card = $("syllabus-card");
  if (!syllabus.courseCode && !syllabus.institution) { card.hidden = true; return; }
  card.hidden = false;
  $("syllabus-title").textContent = syllabus.courseTitle || plan.title || "Syllabus";
  $("syllabus-sub").textContent = [syllabus.institution, syllabus.textbook].filter(Boolean).join(" · ");
  const facts = [
    syllabus.courseCode && `Code ${syllabus.courseCode}`,
    syllabus.credits && `${syllabus.credits} credits`,
    syllabus.ltps && `L:T:P:S ${syllabus.ltps}`,
    syllabus.hoursPerWeek && `${syllabus.hoursPerWeek} hrs/week`,
    syllabus.cieMarks && `CIE ${syllabus.cieMarks}`,
    syllabus.seeMarks && `SEE ${syllabus.seeMarks}`
  ].filter(Boolean);
  $("syllabus-pills").innerHTML = facts.map((f) => `<span class="pill">${escapeHtml(f)}</span>`).join("");
  const outcomes = Object.entries(syllabus.outcomes || {});
  $("outcomes").innerHTML = outcomes
    .map(([key, text]) => `<div class="co"><b>${escapeHtml(key)}</b><div>${escapeHtml(text)}</div></div>`)
    .join("");
}

function renderCoverage(plan) {
  const t = plan.totals || {};
  $("plan-card").hidden = false;
  const covered = (t.reuse || 0) + (t.moved || 0) + (t.thin || 0);
  $("coverage-sub").textContent =
    `${covered} of ${t.topics} syllabus topics are already written somewhere on ByteXL `
    + `(${Math.round((t.coverage || 0) * 100)}% coverage, about ${(t.reusedWords || 0).toLocaleString()} words of reusable material).`;
  $("source-pills").innerHTML = (plan.sources || [])
    .map((s) => `<span class="pill">${escapeHtml(s.title)} · ${s.used} topics</span>`)
    .join("") || `<span class="pill">No donor products</span>`;

  $("stats").innerHTML = [
    statLabel(t.units, "Units"),
    statLabel(t.chapters, "Chapters"),
    statLabel(t.topics, "Topics"),
    statLabel(t.reuse, "Reused as-is", "good"),
    statLabel((t.thin || 0) + (t.moved || 0), "Needs a look", (t.thin || t.moved) ? "warn" : ""),
    statLabel(t.author, "To author", t.author ? "warn" : "good")
  ].join("");

  const blockers = plan.blockers || [];
  $("blockers").innerHTML = blockers.length
    ? `<div class="message error"><strong>${blockers.length} topic${blockers.length === 1 ? "" : "s"} cannot be resolved, so the course cannot be created yet.</strong><br>`
      + blockers.map((b) => `${escapeHtml(b.title)} — ${escapeHtml(b.detail)}`).join("<br>") + `</div>`
    : "";

  const gaps = plan.gaps || [];
  $("gaps").innerHTML = gaps.length
    ? `<div class="message warn">${gaps.length} topic${gaps.length === 1 ? "" : "s"} have no reading material anywhere in the ByteXL catalogue and must be written.</div>`
      + `<div class="gap-list">` + gaps.map((g) =>
        `<div class="gap"><strong>${escapeHtml(g.sectionTitle)} · ${escapeHtml(g.title)}</strong>`
        + (g.note ? `<span>${escapeHtml(g.note)}</span>` : "") + `</div>`).join("") + `</div>`
    : `<div class="message success">Every syllabus topic is covered by material that already exists.</div>`;
}

function renderTopic(topic) {
  const source = topic.source;
  const stats = topic.stats || {};
  const metrics = source
    ? [
        stats.words != null && `${Number(stats.words).toLocaleString()} words`,
        stats.images ? `${stats.images} img` : null,
        stats.codeBlocks ? `${stats.codeBlocks} code` : null
      ].filter(Boolean)
    : [];
  const sourceHtml = source
    ? `<span class="prod">${escapeHtml(source.productTitle)}</span> · ${escapeHtml(source.sectionTitle)}<br><b>${escapeHtml(source.pageTitle)}</b>`
    : `<i>No donor page — a placeholder will be created</i>`;
  return `<div class="topic">
    <div>
      <div class="topic-title">${escapeHtml(topic.title)}</div>
      ${topic.note ? `<div class="topic-note">${escapeHtml(topic.note)}</div>` : ""}
      ${topic.detail ? `<div class="topic-detail">${escapeHtml(topic.detail)}</div>` : ""}
    </div>
    <div class="src">${sourceHtml}</div>
    <div class="metrics">
      ${metrics.map((m) => `<span class="metric">${escapeHtml(m)}</span>`).join("")}
      <span class="status ${escapeHtml(topic.status)}">${escapeHtml(topic.status)}</span>
    </div>
  </div>`;
}

function renderTree(plan) {
  $("tree-card").hidden = false;
  $("tree").innerHTML = (plan.units || []).map((unit) => {
    const topicCount = (unit.chapters || []).reduce((sum, c) => sum + (c.topics || []).length, 0);
    const collapsed = state.collapsed.has(String(unit.number));
    const meta = [
      unit.courseOutcome,
      unit.hours ? `${unit.hours} hours` : null,
      `${(unit.chapters || []).length} chapters`,
      `${topicCount} topics`
    ].filter(Boolean).join(" · ");
    return `<div class="unit${collapsed ? " collapsed" : ""}" style="margin-bottom:14px">
      <div class="unit-head" data-unit="${escapeHtml(unit.number)}">
        <h3>Unit ${escapeHtml(unit.number)} &mdash; ${escapeHtml(unit.title)}</h3>
        <span class="meta">${escapeHtml(meta)}</span>
      </div>
      ${unit.syllabus ? `<div class="unit-syllabus">${escapeHtml(unit.syllabus)}</div>` : ""}
      ${(unit.chapters || []).map((chapter) => `<div class="chapter">
        <div class="chapter-head"><code>${escapeHtml(chapter.sectionTitle)}</code><strong>${escapeHtml(chapter.title)}</strong></div>
        ${(chapter.topics || []).map(renderTopic).join("")}
      </div>`).join("")}
    </div>`;
  }).join("") || `<div class="empty">This blueprint has no units.</div>`;

  $("tree").querySelectorAll(".unit-head").forEach((head) => {
    head.addEventListener("click", () => {
      const key = head.dataset.unit;
      if (state.collapsed.has(key)) state.collapsed.delete(key);
      else state.collapsed.add(key);
      renderTree(state.plan);
    });
  });
}

function renderCreate(plan) {
  const t = plan.totals || {};
  $("create-card").hidden = false;
  $("course-title").value = plan.title || "";
  $("course-description").value = plan.description || "";
  $("create-summary").textContent =
    `${t.chapters} sections · ${t.topics - (t.author || 0)} cloned · ${t.author || 0} placeholder`;

  const warnings = [];
  if (plan.existingProduct) {
    warnings.push(`A product titled “${plan.existingProduct.title}” already exists on ByteXL `
      + `(${plan.existingProduct._id}, ${plan.existingProduct.topicCount} topics). `
      + `Creating this course would make a second one — rename it first.`);
  }
  if (!plan.canCreate) warnings.push("Creation is blocked until every topic resolves to a readable donor page.");
  $("create-warning").innerHTML = warnings.length
    ? `<div class="message warn">${warnings.map(escapeHtml).join("<br><br>")}</div>` : "";
  $("create").disabled = !plan.canCreate || Boolean(plan.existingProduct) || state.creating;
  $("create-result").innerHTML = "";
}

function render() {
  const plan = state.plan;
  if (!plan) {
    ["syllabus-card", "plan-card", "tree-card", "create-card"].forEach((id) => { $(id).hidden = true; });
    return;
  }
  renderSyllabus(plan);
  renderCoverage(plan);
  renderTree(plan);
  renderCreate(plan);
}

async function createCourse() {
  const plan = state.plan;
  if (!plan || state.creating) return;
  const title = $("course-title").value.trim();
  if (!title) { showMessage("A course title is required.", "error"); return; }
  const t = plan.totals || {};
  const skipAuthorNew = $("skip-author").checked;
  const written = t.topics - (skipAuthorNew ? (t.author || 0) : 0);
  const confirmed = window.confirm(
    `Create “${title}” on ByteXL?\n\n`
    + `${written} topics will be written: ${t.topics - (t.author || 0)} cloned from existing lessons`
    + (skipAuthorNew
      ? `. The ${t.author || 0} unwritten topics will be left out.`
      : ` and ${t.author || 0} placeholders.`)
    + `\n\nThis publishes a new product on the platform.`
  );
  if (!confirmed) return;

  state.creating = true;
  $("create").disabled = true;
  showMessage("Creating the course — cloning every donor page, this takes a minute…");
  try {
    const result = await request("/course-builder/create", {
      method: "POST",
      body: JSON.stringify({
        slug: plan.slug,
        title,
        description: $("course-description").value.trim(),
        skipAuthorNew,
        confirm: true
      })
    });
    showMessage("");
    const skipped = result.skippedTopics || [];
    $("create-result").innerHTML = `<div class="message success">
      Created <strong>${escapeHtml(result.title)}</strong> — reading id <code>${escapeHtml(result.readingId)}</code>.<br>
      ${result.createdSections} sections, ${result.clonedTopics} cloned topics, ${result.placeholderTopics} placeholders to write.
      ${skipped.length ? `<br>Left out for you to add later:<br>${skipped.map((s) => `· ${escapeHtml(s)}`).join("<br>")}` : ""}
    </div>`;
  } catch (error) {
    showMessage(error.message, "error");
    $("create").disabled = false;
  } finally {
    state.creating = false;
  }
}

// --------------------------------------------------------------------------
// Step 5 — the platform course object. Independent of steps 1-4: it needs only
// a blueprint, because every lesson links into the donor course that already
// holds it rather than into anything this page created.
// --------------------------------------------------------------------------

function showPublishMessage(text, kind = "") {
  const node = $("publish-message");
  node.hidden = !text;
  node.className = text ? `message${kind ? ` ${kind}` : ""}` : "";
  node.textContent = text || "";
}

function renderPublish(plan) {
  const t = plan.totals || {};
  $("publish-sources").textContent = (plan.sources || [])
    .map((s) => `${s.title} · ${s.used}`).join("   |   ") || "no donors";

  const stats = $("publish-stats");
  stats.hidden = false;
  stats.innerHTML = [
    statLabel(t.modules, "Units"),
    statLabel(t.chapters, "Chapters"),
    statLabel(t.lessons, "Lesson links", "good"),
    statLabel(t.excluded, "Not written", t.excluded ? "warn" : "good"),
    statLabel(t.blocked, "Blocked", t.blocked ? "bad" : "good"),
    statLabel(plan.existingCourse ? "rebuild" : "new", "Action")
  ].join("");

  $("publish-excluded").innerHTML = (plan.blocked || []).length
    ? `<div class="message error"><strong>${plan.blocked.length} lesson(s) could not be resolved:</strong><br>`
      + plan.blocked.map((b) => `${escapeHtml(b.title)} — ${escapeHtml(b.detail)}`).join("<br>") + `</div>`
    : ((plan.excluded || []).length
      ? `<div class="message warn">${plan.excluded.length} syllabus topic(s) have no reading material and are left out of the course:<br>`
        + plan.excluded.map((e) => `· ${escapeHtml(e.chapter)} — ${escapeHtml(e.title)}`).join("<br>") + `</div>`
      : "");

  $("publish-tree").innerHTML = (plan.modules || []).map((m) => `<div class="unit" style="margin-bottom:10px">
      <div class="unit-head"><h3>${escapeHtml(m.title)}</h3>
        <span class="meta">${m.topics.length} chapters · ${m.topics.reduce((n, t2) => n + t2.subTopics.length, 0)} lessons</span></div>
      ${m.topics.map((t2) => `<div class="chapter"><div class="chapter-head">
          <strong>${escapeHtml(t2.title)}</strong><code>${t2.subTopics.length} lessons</code></div>
        ${t2.subTopics.map((s) => `<div class="topic"><div class="topic-title">${escapeHtml(s.title)}</div>
          <div class="src"><a href="${escapeHtml(s.data)}" target="_blank" rel="noopener">${escapeHtml(s.data.replace("https://app.bytexl.ai/reading/", ""))}</a></div>
          <div class="metrics"><span class="status reuse">link</span></div></div>`).join("")}
      </div>`).join("")}
    </div>`).join("");

  $("publish-title").value = plan.title || "";
  $("publish-description").value = plan.courseDescription || "";
  $("publish-warning").innerHTML = plan.existingCourse
    ? `<div class="message warn">A course titled “${escapeHtml(plan.existingCourse.title)}” already exists (<code>${escapeHtml(plan.existingCourse._id)}</code>). Publishing will rebuild that course in place — its module tree is replaced, and batch assignments, grading and FAQs are preserved.</div>`
    : "";
  $("publish-create").disabled = !plan.canCreate;
  $("publish-create").textContent = plan.existingCourse ? "Rebuild course on ByteXL" : "Publish course on ByteXL";
  $("publish-result").innerHTML = "";
}

async function loadPublishPlan() {
  const slug = $("blueprint").value;
  if (!slug) return;
  $("publish-load").disabled = true;
  showPublishMessage("Resolving every syllabus topic against the donor courses…");
  try {
    const plan = await request(`/course-builder/course-plan?slug=${encodeURIComponent(slug)}`);
    state.publish = plan;
    renderPublish(plan);
    showPublishMessage("");
  } catch (error) {
    state.publish = null;
    showPublishMessage(error.message, "error");
  } finally {
    $("publish-load").disabled = false;
  }
}

async function publishCourse() {
  const plan = state.publish;
  if (!plan || state.publishing) return;
  const title = $("publish-title").value.trim();
  if (!title) { showPublishMessage("A course title is required.", "error"); return; }
  const t = plan.totals || {};
  const rebuilding = Boolean(plan.existingCourse);
  const confirmed = window.confirm(
    `${rebuilding ? "Rebuild" : "Publish"} “${title}” on ByteXL?\n\n`
    + `${t.modules} units, ${t.chapters} chapters, ${t.lessons} lesson links.\n`
    + (t.excluded ? `${t.excluded} unwritten topic(s) will be left out.\n` : "")
    + (rebuilding
      ? `\nThis replaces the module tree of the existing course ${plan.existingCourse._id}.`
      : `\nThis publishes a new course on the platform.`)
  );
  if (!confirmed) return;

  state.publishing = true;
  $("publish-create").disabled = true;
  showPublishMessage("Writing the course…");
  try {
    const result = await request("/course-builder/create-course", {
      method: "POST",
      body: JSON.stringify({
        slug: plan.slug,
        title,
        description: $("publish-description").value.trim(),
        courseType: $("publish-course-type").value,
        programLevel: $("publish-program-level").value.trim(),
        courseId: plan.existingCourse ? plan.existingCourse._id : undefined,
        confirm: true
      })
    });
    showPublishMessage("");
    $("publish-result").innerHTML = `<div class="message success">
      Course ${escapeHtml(result.action)} — <strong>${escapeHtml(result.title)}</strong>, id <code>${escapeHtml(result.courseId)}</code>.<br>
      ${result.modules} units, ${result.chapters} chapters, ${result.lessons} lesson links, verified by reading the course back.
    </div>`;
  } catch (error) {
    showPublishMessage(error.message, "error");
    $("publish-create").disabled = false;
  } finally {
    state.publishing = false;
  }
}

$("load").addEventListener("click", () => loadPlan(false));
$("refresh").addEventListener("click", () => loadPlan(true));
$("create").addEventListener("click", createCourse);
$("publish-load").addEventListener("click", loadPublishPlan);
$("publish-create").addEventListener("click", publishCourse);
$("blueprint").addEventListener("change", () => {
  state.plan = null;
  state.publish = null;
  $("publish-stats").hidden = true;
  $("publish-tree").innerHTML = "";
  $("publish-excluded").innerHTML = "";
  $("publish-create").disabled = true;
  render();
});
loadBlueprints();
