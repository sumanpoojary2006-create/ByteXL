const BYTEXL_API_BASE = (process.env.BYTEXL_API_BASE || "https://app.bytexl.ai").replace(/\/$/, "");

export default async function handler(request, response) {
  if (request.method !== "GET") {
    response.setHeader("Allow", "GET");
    return response.status(405).json({ detail: "Method not allowed" });
  }

  const token = process.env.BYTEXL_CONTENT_TOKEN || process.env.BYTEXL_UPLOAD_TOKEN;
  if (!token) {
    return response.status(500).json({ detail: "ByteXL token is not configured" });
  }

  try {
    const upstream = await fetch(`${BYTEXL_API_BASE}/api/content/v2/list?pageSize=10000`, {
      headers: { Authorization: `Bearer ${token}` },
      signal: AbortSignal.timeout(25000),
    });
    const body = await upstream.text();
    if (!upstream.ok) {
      return response.status(502).json({
        detail: `ByteXL product list returned ${upstream.status}`,
      });
    }

    const result = JSON.parse(body);
    const items = result.items || result.data || [];
    response.setHeader("Cache-Control", "private, no-store");
    return response.status(200).json({
      status: "success",
      defaultReadingId: process.env.BYTEXL_READING_ID || "44sqshkgw",
      items: items
        .filter((item) => item && item._id && item.title)
        .map((item) => ({
          _id: item._id,
          title: item.title,
          chapterCount: item.chapterCount,
          topicCount: item.topicCount,
        })),
    });
  } catch (error) {
    const timedOut = error && (error.name === "TimeoutError" || error.name === "AbortError");
    return response.status(502).json({
      detail: timedOut
        ? "ByteXL product list timed out. Please try refresh."
        : "ByteXL product list is temporarily unavailable.",
    });
  }
}
