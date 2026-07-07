const BACKEND_URL = "https://image-converter-pi-rouge.vercel.app";

const zipInput = document.getElementById("zipInput");
const fileName = document.getElementById("fileName");
const convertBtn = document.getElementById("convertBtn");
const statusEl = document.getElementById("status");
const statsEl = document.getElementById("stats");
const uploadedCount = document.getElementById("uploadedCount");
const failedCount = document.getElementById("failedCount");
const missingCount = document.getElementById("missingCount");

let selectedFile = null;

setStatus("Connected to the ByteXL team converter.");

zipInput.addEventListener("change", () => {
  selectedFile = zipInput.files?.[0] || null;
  fileName.textContent = selectedFile ? selectedFile.name : "No file selected";
  resetStats();
  updateConvertState();
});

convertBtn.addEventListener("click", async () => {
  if (!selectedFile) return;

  convertBtn.disabled = true;
  resetStats();

  try {
    await convertWithBackend(selectedFile);
  } catch (err) {
    setStatus(err.message || "Conversion failed.", "error");
  } finally {
    updateConvertState();
  }
});

async function convertWithBackend(file) {
  if (!file.name.toLowerCase().endsWith(".zip")) {
    throw new Error("Please choose a .zip file.");
  }

  setStatus("Uploading ZIP to ByteXL team converter...");
  const formData = new FormData();
  formData.append("file", file, file.name);

  const response = await fetch(`${BACKEND_URL}/convert`, {
    method: "POST",
    body: formData
  });

  if (!response.ok) {
    const detail = await response.json().then((body) => body.detail).catch(() => "");
    throw new Error(detail || `Converter failed with HTTP ${response.status}.`);
  }

  const stats = parseStats(response.headers.get("X-Stats") || "");
  renderStats(stats);

  setStatus("Downloading converted ZIP...");
  const blob = await response.blob();
  await downloadBlob(blob, responseFilename(response, file.name));
  setStatus("Done. Converted ZIP downloaded.", "success");
}

function parseStats(header) {
  const stats = { uploaded: 0, failed: 0, missing: 0 };
  for (const part of header.split(",")) {
    const [key, value] = part.split("=");
    if (key in stats) {
      stats[key] = Number(value) || 0;
    }
  }
  return stats;
}

function responseFilename(response, originalName) {
  const fallback = `${originalName.replace(/\.zip$/i, "")}_converted.zip`;
  const disposition = response.headers.get("Content-Disposition") || "";
  const match = disposition.match(/filename\*?=(?:UTF-8''|")?([^";]+)/i);
  return match ? decodeURIComponent(match[1].replace(/"/g, "")) : fallback;
}

async function downloadBlob(blob, filename) {
  const url = URL.createObjectURL(blob);
  try {
    await chrome.downloads.download({ url, filename, saveAs: true });
  } finally {
    setTimeout(() => URL.revokeObjectURL(url), 30_000);
  }
}

function updateConvertState() {
  convertBtn.disabled = !selectedFile;
}

function setStatus(message, type = "") {
  statusEl.textContent = message;
  statusEl.className = type ? `status ${type}` : "status";
}

function resetStats() {
  renderStats({ uploaded: 0, failed: 0, missing: 0 }, true);
}

function renderStats(stats, hide = false) {
  uploadedCount.textContent = stats.uploaded;
  failedCount.textContent = stats.failed;
  missingCount.textContent = stats.missing;
  statsEl.hidden = hide;
}
