function apiBase() {
  const configured = location.protocol === "file:"
    ? "http://127.0.0.1:8000"
    : String(window.IMAGE_CONVERTER_CONFIG?.apiBase || location.origin).trim();
  const api = new URL(configured, location.href);
  const isVercel = api.hostname === "vercel.app" || api.hostname.endsWith(".vercel.app");
  if (isVercel) throw new Error("Configure the external assessment API before using this page.");
  return api.origin;
}

const API_BASE = apiBase();
const state = { loading: false, creating: false, discovery: null, selected: new Set(), overrides: new Map(), search: "" };
const $ = (id) => document.getElementById(id);

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

const WAKE_UP_RETRY_DELAYS_MS = [4000, 10000, 20000];

function wait(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

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
        throw new Error("Could not reach the assessment API after several attempts. The free Render instance may still be waking up — wait a moment and click Refresh.");
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

function showMessage(text, tone = "") {
  const message = $("message");
  message.hidden = !text;
  message.className = `message ${tone}`.trim();
  message.textContent = text;
}

function candidateStatus(candidate) {
  if (candidate.existingTest) return "exists";
  if (!candidate.ready) return "blocked";
  return "ready";
}

function renderStats() {
  const discovery = state.discovery;
  $("setTwoCount").textContent = discovery?.setTwoQuestionCount ?? 0;
  $("structuredCount").textContent = discovery?.structuredQuestionCount ?? 0;
  $("unstructuredCount").textContent = discovery?.unstructuredQuestionCount ?? 0;
  $("readyCount").textContent = discovery?.readyCount ?? 0;
  $("existingCount").textContent = discovery?.existingCount ?? 0;
}

function overrideFor(candidate) {
  return state.overrides.get(candidate.groupKey) || {};
}

function matchesSearch(candidate) {
  const query = state.search.trim().toLowerCase();
  if (!query) return true;
  return `${candidate.course} ${candidate.title}`.toLowerCase().includes(query);
}

function bindRowInteractions(tbody) {
  tbody.querySelectorAll("input[type=checkbox]").forEach((box) => {
    box.addEventListener("change", () => {
      const key = box.dataset.key;
      if (box.checked) state.selected.add(key);
      else state.selected.delete(key);
      renderControls();
    });
  });
  tbody.querySelectorAll("input.edit-title, input.edit-duration").forEach((input) => {
    input.addEventListener("input", () => {
      const key = input.dataset.key;
      const field = input.dataset.field;
      const current = state.overrides.get(key) || {};
      current[field] = input.value;
      state.overrides.set(key, current);
      renderControls();
    });
  });
}

function renderReadyRows(rows) {
  const tbody = $("readyRows");
  if (!rows.length) {
    tbody.innerHTML = `<tr><td class="empty" colspan="7">${state.loading ? "Loading…" : "No ready groups match."}</td></tr>`;
    return;
  }
  tbody.innerHTML = rows.map((candidate) => {
    const checked = state.selected.has(candidate.groupKey);
    const override = overrideFor(candidate);
    const titleValue = override.title ?? candidate.title;
    const durationValue = override.duration ?? candidate.duration;
    return `<tr>
      <td class="check"><input type="checkbox" data-key="${escapeHtml(candidate.groupKey)}" ${checked ? "checked" : ""}></td>
      <td>${escapeHtml(candidate.course)}</td>
      <td>${escapeHtml(candidate.unit)}</td>
      <td class="title-cell"><input class="edit-title" type="text" maxlength="180" data-key="${escapeHtml(candidate.groupKey)}" data-field="title" value="${escapeHtml(titleValue)}"></td>
      <td>${escapeHtml(candidate.questionCount)} (${escapeHtml((candidate.questionTypes || []).join(", "))})</td>
      <td><span class="duration-cell"><input class="edit-duration" type="number" min="0" max="1440" step="1" data-key="${escapeHtml(candidate.groupKey)}" data-field="duration" value="${escapeHtml(durationValue)}"> min</span></td>
      <td>&mdash;</td>
    </tr>`;
  }).join("");
  bindRowInteractions(tbody);
}

function renderExistingRows(rows) {
  const tbody = $("existingRows");
  if (!rows.length) {
    tbody.innerHTML = `<tr><td class="empty" colspan="5">${state.loading ? "Loading…" : "No matches."}</td></tr>`;
    return;
  }
  tbody.innerHTML = rows.map((candidate) => {
    const editUrl = candidate.existingTest?.editUrl;
    const link = editUrl
      ? `<div class="link-row">
          <a href="${escapeHtml(editUrl)}" target="_blank" rel="noopener">${escapeHtml(candidate.existingTest.title || "Open existing test")}</a>
          <button type="button" class="copy-btn" data-url="${escapeHtml(editUrl)}">Copy link</button>
        </div>`
      : escapeHtml(candidate.existingTest?.title || "—");
    return `<tr>
      <td>${escapeHtml(candidate.course)}</td>
      <td>${escapeHtml(candidate.unit)}</td>
      <td>${escapeHtml(candidate.title)}</td>
      <td class="title-cell">${link}</td>
      <td>${escapeHtml(candidate.questionCount)} (${escapeHtml((candidate.questionTypes || []).join(", "))})</td>
    </tr>`;
  }).join("");
}

function renderBlockedRows(rows) {
  const panel = $("blockedPanel");
  const tbody = $("blockedRows");
  panel.hidden = !rows.length;
  if (!rows.length) {
    tbody.innerHTML = "";
    return;
  }
  $("blockedSub").textContent = `${rows.length} group(s) need fixing before they can be created.`;
  tbody.innerHTML = rows.map((candidate) => `<tr>
      <td>${escapeHtml(candidate.course)}</td>
      <td>${escapeHtml(candidate.unit)}</td>
      <td>${escapeHtml(candidate.title)}</td>
      <td>${escapeHtml(candidate.questionCount)}</td>
      <td>${escapeHtml((candidate.issues || []).join(" ")) || "&mdash;"}</td>
    </tr>`).join("");
}

function renderTables() {
  const all = state.discovery?.candidates || [];
  const filtered = all.filter(matchesSearch);
  const ready = filtered.filter((candidate) => candidateStatus(candidate) === "ready");
  const existing = filtered.filter((candidate) => candidateStatus(candidate) === "exists");
  const blocked = filtered.filter((candidate) => candidateStatus(candidate) === "blocked");

  renderReadyRows(ready);
  renderExistingRows(existing);
  renderBlockedRows(blocked);

  const filterNote = state.search.trim() ? " matching your search" : "";
  $("readySub").textContent = state.loading ? "Scanning…" : `${ready.length} ready group(s)${filterNote}.`;
  $("readyPill").textContent = state.loading ? "Loading" : ready.length ? "Ready" : "None";
  $("existingSub").textContent = state.loading ? "Scanning…" : `${existing.length} group(s) already have a test${filterNote}.`;
  $("existingPill").textContent = state.loading ? "Loading" : existing.length ? "On file" : "None";
}

function selectionIsValid() {
  if (!state.selected.size) return false;
  for (const candidate of state.discovery?.candidates || []) {
    if (!state.selected.has(candidate.groupKey)) continue;
    const override = overrideFor(candidate);
    const title = String(override.title ?? candidate.title).trim();
    if (!title || title.length > 180) return false;
    const duration = Number(override.duration ?? candidate.duration);
    if (!Number.isInteger(duration) || duration < 0 || duration > 1440) return false;
  }
  return true;
}

function renderControls() {
  const busy = state.loading || state.creating;
  const valid = selectionIsValid();
  $("refreshBtn").disabled = busy;
  $("selectAllBtn").disabled = busy || !state.discovery?.candidates?.length;
  $("clearBtn").disabled = busy || !state.selected.size;
  $("createBtn").disabled = busy || !valid;
  $("createBtn").title = !busy && state.selected.size && !valid
    ? "Fix the highlighted title/duration values before creating."
    : "";
  $("createBtn").textContent = state.creating
    ? "Creating assessments…"
    : `Create selected assessments${state.selected.size ? ` (${state.selected.size})` : ""}`;
}

function render() {
  renderStats();
  renderTables();
  const discovery = state.discovery;
  if (state.loading) {
    $("headSub").textContent = "Scanning ByteXL for Set 2 questions…";
  } else if (discovery) {
    $("headSub").textContent = `${discovery.candidateCount} group(s) detected from ${discovery.setTwoQuestionCount} Set 2 question(s).`;
  }
  renderControls();
}

async function loadCandidates() {
  if (state.loading) return;
  state.loading = true;
  state.selected.clear();
  state.overrides.clear();
  render();
  try {
    const result = await request("/test-assessment/candidates");
    state.discovery = result;
    showMessage("");
  } catch (error) {
    state.discovery = null;
    showMessage(error.message || "Could not load Set 2 assessment candidates.", "error");
  } finally {
    state.loading = false;
    render();
  }
}

function selectAllReady() {
  for (const candidate of state.discovery?.candidates || []) {
    if (candidateStatus(candidate) === "ready" && matchesSearch(candidate)) state.selected.add(candidate.groupKey);
  }
  render();
}

function clearSelection() {
  state.selected.clear();
  render();
}

function renderResults(result) {
  const panel = $("resultsPanel");
  panel.hidden = false;
  $("resultsPill").textContent = `${result.createdCount} created · ${result.failedCount} failed`;
  $("resultsBody").innerHTML = (result.results || []).map((row) => {
    if (row.status === "created") {
      return `<div class="result-row">
        <div><span class="status created">created</span> <strong>${escapeHtml(row.title)}</strong> · ${escapeHtml(row.questionCount)} questions</div>
        <div class="links">
          <a href="${escapeHtml(row.editUrl)}" target="_blank" rel="noopener">Open Test Builder</a>
          <button type="button" class="copy-btn" data-url="${escapeHtml(row.editUrl)}">Copy link</button>
          <a href="${escapeHtml(row.previewUrl)}" target="_blank" rel="noopener">Preview</a>
        </div>
      </div>`;
    }
    return `<div class="result-row">
      <div><span class="status failed">failed</span> <strong>${escapeHtml(row.title)}</strong></div>
      <div>${escapeHtml(row.message || "Creation failed.")}</div>
    </div>`;
  }).join("");
}

function buildOverridesPayload() {
  const overrides = {};
  for (const key of state.selected) {
    const edited = state.overrides.get(key);
    if (!edited) continue;
    const entry = {};
    if ("title" in edited) entry.title = String(edited.title).trim();
    if ("duration" in edited) entry.duration = Number(edited.duration);
    if (Object.keys(entry).length) overrides[key] = entry;
  }
  return overrides;
}

async function createSelected() {
  if (!state.selected.size || state.creating || !selectionIsValid()) return;
  state.creating = true;
  render();
  try {
    const result = await request("/test-assessment/create", {
      method: "POST",
      body: JSON.stringify({ confirm: true, groupKeys: Array.from(state.selected), overrides: buildOverridesPayload() })
    });
    showMessage(`${result.createdCount} assessment(s) created, ${result.failedCount} failed.`, result.failedCount ? "error" : "success");
    renderResults(result);
    await loadCandidates();
  } catch (error) {
    showMessage(error.message || "Assessment creation failed.", "error");
  } finally {
    state.creating = false;
    render();
  }
}

async function copyText(text) {
  try {
    await navigator.clipboard.writeText(text);
    return true;
  } catch {
    try {
      const textarea = document.createElement("textarea");
      textarea.value = text;
      textarea.style.position = "fixed";
      textarea.style.opacity = "0";
      document.body.appendChild(textarea);
      textarea.focus();
      textarea.select();
      const ok = document.execCommand("copy");
      document.body.removeChild(textarea);
      return ok;
    } catch {
      return false;
    }
  }
}

function handleCopyClick(event) {
  const button = event.target.closest(".copy-btn");
  if (!button) return;
  const url = button.dataset.url;
  if (!url) return;
  copyText(url).then((ok) => {
    const original = button.textContent;
    button.textContent = ok ? "Copied!" : "Copy failed";
    button.classList.toggle("copied", ok);
    setTimeout(() => {
      button.textContent = original;
      button.classList.remove("copied");
    }, 1500);
  });
}

const blueprintState = { previewing: false, creating: false, preview: null };

function showBlueprintMessage(text, tone = "") {
  const message = $("blueprintMessage");
  message.hidden = !text;
  message.className = `message ${tone}`.trim();
  message.textContent = text;
}

function blueprintRowStatus(row) {
  if (row.existingTest) return "exists";
  if (row.issues?.length) return "blocked";
  return "ready";
}

function renderBlueprintRows() {
  const panel = $("blueprintPanel");
  const tbody = $("blueprintRowsBody");
  const preview = blueprintState.preview;
  panel.hidden = !preview;
  if (!preview) return;

  tbody.innerHTML = preview.rows.map((row) => {
    const status = blueprintRowStatus(row);
    const notes = [];
    if (row.issues?.length) notes.push(...row.issues);
    if (row.existingTest) {
      notes.push(`Already exists${row.existingTest.title ? `: ${row.existingTest.title}` : ""}.`);
      const link = row.existingTest.editUrl
        ? `<a href="${escapeHtml(row.existingTest.editUrl)}" target="_blank" rel="noopener">Open</a>`
        : "";
      if (link) notes.push(link);
    }
    return `<tr>
      <td><strong>${escapeHtml(row.title)}</strong></td>
      <td>${escapeHtml((row.topics || []).join(", "))}</td>
      <td>${escapeHtml((row.difficulty || []).join(", ")) || "&mdash;"}</td>
      <td>${escapeHtml(row.mcqSelectedCount)} / ${escapeHtml(row.mcqRequested)} <span style="color:var(--faint)">(avail ${escapeHtml(row.mcqAvailable)})</span></td>
      <td>${escapeHtml(row.codingSelectedCount)} / ${escapeHtml(row.codingRequested)} <span style="color:var(--faint)">(avail ${escapeHtml(row.codingAvailable)})</span></td>
      <td>${escapeHtml(row.duration)} min</td>
      <td><span class="status ${status}">${status}</span></td>
      <td>${notes.join(" ") || "&mdash;"}</td>
    </tr>`;
  }).join("");

  $("blueprintSub").textContent = `${preview.readyCount} of ${preview.rows.length} row(s) ready · ${preview.poolSize} Set 2 questions found for "${preview.subject}".`;
  $("blueprintPill").textContent = preview.readyCount === preview.rows.length ? "All ready" : "Needs attention";
  $("blueprintCreateBtn").disabled = blueprintState.previewing || blueprintState.creating || preview.readyCount !== preview.rows.length;
  $("blueprintCreateBtn").textContent = blueprintState.creating
    ? "Creating assessments…"
    : `Create blueprint assessments${preview.rows.length ? ` (${preview.rows.length})` : ""}`;
}

function parseBlueprintRows() {
  const raw = $("blueprintRows").value.trim();
  if (!raw) throw new Error("Paste at least one blueprint row as a JSON array.");
  let rows;
  try {
    rows = JSON.parse(raw);
  } catch (error) {
    throw new Error(`Blueprint JSON is invalid: ${error.message}`);
  }
  if (!Array.isArray(rows) || !rows.length) throw new Error("Blueprint must be a non-empty JSON array of rows.");
  return rows;
}

async function previewBlueprint() {
  if (blueprintState.previewing || blueprintState.creating) return;
  const subject = $("blueprintSubject").value.trim();
  if (!subject) return showBlueprintMessage("Enter a subject (e.g. python).", "error");

  let rows;
  try {
    rows = parseBlueprintRows();
  } catch (error) {
    return showBlueprintMessage(error.message, "error");
  }

  blueprintState.previewing = true;
  blueprintState.preview = null;
  $("blueprintCreateBtn").disabled = true;
  $("blueprintResultsPanel").hidden = true;
  showBlueprintMessage("");
  renderBlueprintRows();
  try {
    const result = await request("/test-assessment/blueprint/preview", {
      method: "POST",
      body: JSON.stringify({ subject, rows })
    });
    blueprintState.preview = { ...result, subject };
    showBlueprintMessage(
      result.readyCount === rows.length
        ? `All ${rows.length} row(s) are ready to create.`
        : `${rows.length - result.readyCount} of ${rows.length} row(s) need attention before creating.`,
      result.readyCount === rows.length ? "success" : "error"
    );
  } catch (error) {
    showBlueprintMessage(error.message || "Could not preview the blueprint.", "error");
  } finally {
    blueprintState.previewing = false;
    renderBlueprintRows();
  }
}

function renderBlueprintResults(result) {
  const panel = $("blueprintResultsPanel");
  panel.hidden = false;
  $("blueprintResultsPill").textContent = `${result.createdCount} created · ${result.failedCount} failed`;
  $("blueprintResultsBody").innerHTML = (result.results || []).map((row) => {
    if (row.status === "created") {
      return `<div class="result-row">
        <div><span class="status created">created</span> <strong>${escapeHtml(row.title)}</strong> · ${escapeHtml(row.questionCount)} questions</div>
        <div class="links">
          <a href="${escapeHtml(row.editUrl)}" target="_blank" rel="noopener">Open Test Builder</a>
          <button type="button" class="copy-btn" data-url="${escapeHtml(row.editUrl)}">Copy link</button>
          <a href="${escapeHtml(row.previewUrl)}" target="_blank" rel="noopener">Preview</a>
        </div>
      </div>`;
    }
    return `<div class="result-row">
      <div><span class="status failed">failed</span> <strong>${escapeHtml(row.title)}</strong></div>
      <div>${escapeHtml(row.message || "Creation failed.")}</div>
    </div>`;
  }).join("");
}

async function createBlueprint() {
  const preview = blueprintState.preview;
  if (!preview || blueprintState.creating || preview.readyCount !== preview.rows.length) return;
  blueprintState.creating = true;
  renderBlueprintRows();
  try {
    const rows = parseBlueprintRows();
    const result = await request("/test-assessment/blueprint/create", {
      method: "POST",
      body: JSON.stringify({ confirm: true, subject: preview.subject, rows })
    });
    showBlueprintMessage(`${result.createdCount} assessment(s) created, ${result.failedCount} failed.`, result.failedCount ? "error" : "success");
    renderBlueprintResults(result);
    await previewBlueprint();
  } catch (error) {
    showBlueprintMessage(error.message || "Blueprint creation failed.", "error");
  } finally {
    blueprintState.creating = false;
    renderBlueprintRows();
  }
}

function clearBlueprint() {
  $("blueprintSubject").value = "";
  $("blueprintRows").value = "";
  blueprintState.preview = null;
  $("blueprintResultsPanel").hidden = true;
  showBlueprintMessage("");
  renderBlueprintRows();
}

function init() {
  $("refreshBtn").addEventListener("click", loadCandidates);
  $("selectAllBtn").addEventListener("click", selectAllReady);
  $("clearBtn").addEventListener("click", clearSelection);
  $("createBtn").addEventListener("click", createSelected);
  $("searchInput").addEventListener("input", (event) => {
    state.search = event.target.value;
    render();
  });
  $("blueprintPreviewBtn").addEventListener("click", previewBlueprint);
  $("blueprintClearBtn").addEventListener("click", clearBlueprint);
  $("blueprintCreateBtn").addEventListener("click", createBlueprint);
  document.addEventListener("click", handleCopyClick);
  render();
  loadCandidates();
}

init();
