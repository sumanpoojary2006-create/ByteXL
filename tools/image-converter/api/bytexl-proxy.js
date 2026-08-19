import { timingSafeEqual } from "node:crypto";

const BYTEXL_ORIGIN = "https://app.bytexl.ai";

function tokenMatches(received, expected) {
  if (!received || !expected) return false;
  const left = Buffer.from(received);
  const right = Buffer.from(expected);
  return left.length === right.length && timingSafeEqual(left, right);
}

export default async function handler(request, response) {
  const authorization = String(request.headers.authorization || "");
  const receivedToken = authorization.replace(/^Bearer\s+/i, "");
  const acceptedTokens = [
    process.env.BYTEXL_CONTENT_TOKEN,
    process.env.BYTEXL_UPLOAD_TOKEN,
  ].filter(Boolean);

  if (!acceptedTokens.some((token) => tokenMatches(receivedToken, token))) {
    return response.status(401).json({ detail: "Unauthorized" });
  }

  const pathParts = String(request.query.path || "").split("/").filter(Boolean);
  if (!pathParts.length || pathParts.some((part) => part === "." || part === "..")) {
    return response.status(400).json({ detail: "Invalid ByteXL path" });
  }

  const target = new URL(`/${pathParts.map(encodeURIComponent).join("/")}`, BYTEXL_ORIGIN);
  for (const [key, value] of Object.entries(request.query)) {
    if (key === "path") continue;
    for (const item of Array.isArray(value) ? value : [value]) {
      if (item != null) target.searchParams.append(key, String(item));
    }
  }

  const method = String(request.method || "GET").toUpperCase();
  const headers = {
    Authorization: `Bearer ${receivedToken}`,
    Accept: "application/json",
  };
  const options = {
    method,
    headers,
    signal: AbortSignal.timeout(45000),
  };
  if (!new Set(["GET", "HEAD"]).has(method)) {
    headers["Content-Type"] = "application/json";
    options.body = JSON.stringify(request.body ?? {});
  }

  try {
    const upstream = await fetch(target, options);
    const body = await upstream.arrayBuffer();
    response.status(upstream.status);
    response.setHeader(
      "Content-Type",
      upstream.headers.get("content-type") || "application/json; charset=utf-8",
    );
    response.setHeader("Cache-Control", "private, no-store");
    return response.send(Buffer.from(body));
  } catch (error) {
    const timedOut = error && (error.name === "TimeoutError" || error.name === "AbortError");
    return response.status(502).json({
      detail: timedOut ? "ByteXL request timed out" : "ByteXL request failed",
    });
  }
}
