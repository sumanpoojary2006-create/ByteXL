const ALLOWED_PATHS = new Set([
  "/api/questions/batch-validate",
  "/api/questions/batch",
  "/api/questions/get-filter-options",
  "/api/getId"
]);

const BASE_URL = "https://bytexl.app";

function setCors(res) {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "POST, OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Content-Type, X-ByteXL-Token");
}

function send(res, statusCode, body, contentType = "application/json") {
  res.statusCode = statusCode;
  res.setHeader("Content-Type", contentType);
  res.end(body);
}

function readBody(req) {
  return new Promise((resolve, reject) => {
    if (req.body && typeof req.body === "object") {
      resolve(req.body);
      return;
    }

    let raw = "";
    req.on("data", (chunk) => {
      raw += chunk;
      if (raw.length > 6_000_000) {
        reject(new Error("Request body is too large"));
        req.destroy();
      }
    });
    req.on("end", () => {
      if (!raw) {
        resolve({});
        return;
      }
      try {
        resolve(JSON.parse(raw));
      } catch {
        reject(new Error("Invalid JSON body"));
      }
    });
    req.on("error", reject);
  });
}

module.exports = async function handler(req, res) {
  setCors(res);

  if (req.method === "OPTIONS") {
    send(res, 204, "");
    return;
  }

  if (req.method !== "POST") {
    send(res, 405, JSON.stringify({ message: "Method not allowed" }));
    return;
  }

  try {
    const request = await readBody(req);
    const path = String(request.path || "");
    const method = String(request.method || "POST").toUpperCase();
    const token = String(req.headers["x-bytexl-token"] || "").trim();

    if (!ALLOWED_PATHS.has(path)) {
      send(res, 400, JSON.stringify({ message: "ByteXL endpoint is not allowed" }));
      return;
    }

    if (path !== "/api/getId" && !token) {
      send(res, 401, JSON.stringify({ message: "ByteXL token is required" }));
      return;
    }

    const headers = { "Content-Type": "application/json" };
    if (token) {
      headers.Authorization = `Bearer ${token}`;
    }

    const upstream = await fetch(`${BASE_URL}${path}`, {
      method,
      headers,
      body: method === "GET" ? undefined : JSON.stringify(request.body ?? null)
    });

    const contentType = upstream.headers.get("content-type") || "text/plain";
    const text = await upstream.text();
    send(res, upstream.status, text, contentType);
  } catch (error) {
    send(res, 500, JSON.stringify({ message: error.message || "Proxy request failed" }));
  }
};
