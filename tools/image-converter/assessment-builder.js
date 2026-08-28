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
const state = { loading: false, creating: false, discovery: null, selected: new Set(), overrides: new Map() };
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

function renderRows() {
  const tbody = $("candidateRows");
  const candidates = state.discovery?.candidates || [];
  if (!candidates.length) {
    tbody.innerHTML = `<tr><td class="empty" colspan="8">${state.loading ? "Loading…" : "No Set 2 assessment groups were detected."}</td></tr>`;
    return;
  }
  tbody.innerHTML = candidates.map((candidate) => {
    const status = candidateStatus(candidate);
    const selectable = status === "ready";
    const checked = state.selected.has(candidate.groupKey);
    const override = overrideFor(candidate);
    const titleValue = override.title ?? candidate.title;
    const durationValue = override.duration ?? candidate.duration;
    const notes = [];
    if (candidate.issues?.length) notes.push(...candidate.issues);
    if (candidate.existingTest) {
      notes.push(`Test already exists${candidate.existingTest.title ? `: ${candidate.existingTest.title}` : ""}.`);
    }
    const existingLink = candidate.existingTest?.editUrl
      ? `<a href="${escapeHtml(candidate.existingTest.editUrl)}" target="_blank" rel="noopener">Open existing test</a>`
      : "";
    const titleCell = selectable
      ? `<input class="edit-title" type="text" maxlength="180" data-key="${escapeHtml(candidate.groupKey)}" data-field="title" value="${escapeHtml(titleValue)}">`
      : `<strong>${escapeHtml(titleValue)}</strong>${existingLink}`;
    const durationCell = selectable
      ? `<span class="duration-cell"><input class="edit-duration" type="number" min="0" max="1440" step="1" data-key="${escapeHtml(candidate.groupKey)}" data-field="duration" value="${escapeHtml(durationValue)}"> min</span>`
      : `${escapeHtml(durationValue)} min`;
    return `<tr>
      <td class="check"><input type="checkbox" data-key="${escapeHtml(candidate.groupKey)}" ${checked ? "checked" : ""} ${selectable ? "" : "disabled"}></td>
      <td>${escapeHtml(candidate.course)}</td>
      <td>${escapeHtml(candidate.unit)}</td>
      <td class="title-cell">${titleCell}</td>
      <td>${escapeHtml(candidate.questionCount)} (${escapeHtml((candidate.questionTypes || []).join(", "))})</td>
      <td>${durationCell}</td>
      <td><span class="status ${status}">${status}</span></td>
      <td>${escapeHtml(notes.join(" ")) || "&mdash;"}</td>
    </tr>`;
  }).join("");

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
      current[field] = field === "duration" ? input.value : input.value;
      state.overrides.set(key, current);
      renderControls();
    });
  });
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
  renderRows();
  const discovery = state.discovery;
  if (state.loading) {
    $("previewSub").textContent = "Scanning ByteXL for Set 2 questions…";
    $("previewPill").textContent = "Loading";
  } else if (discovery) {
    $("headSub").textContent = `${discovery.candidateCount} group(s) detected from ${discovery.setTwoQuestionCount} Set 2 question(s).`;
    $("previewSub").textContent = `${discovery.readyCount} ready to create, ${discovery.existingCount} already have a test.`;
    $("previewPill").textContent = discovery.readyCount ? "Ready" : "No new groups";
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
    if (candidateStatus(candidate) === "ready") state.selected.add(candidate.groupKey);
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

function init() {
  $("refreshBtn").addEventListener("click", loadCandidates);
  $("selectAllBtn").addEventListener("click", selectAllReady);
  $("clearBtn").addEventListener("click", clearSelection);
  $("createBtn").addEventListener("click", createSelected);
  render();
  loadCandidates();
}

init();
