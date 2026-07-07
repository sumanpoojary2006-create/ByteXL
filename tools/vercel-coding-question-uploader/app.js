const fs = require("fs");
const path = require("path");
const bytexlHandler = require("./api/bytexl");

const root = __dirname;

const mimeTypes = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".js": "application/javascript; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".svg": "image/svg+xml",
  ".png": "image/png"
};

const staticFiles = new Set(["/index.html", "/styles.css"]);
const staticPrefixes = ["/assets/", "/vendor/"];

function send(res, statusCode, body, contentType = "text/plain; charset=utf-8") {
  res.statusCode = statusCode;
  res.setHeader("Content-Type", contentType);
  res.end(body);
}

function isStaticPath(pathname) {
  return staticFiles.has(pathname) || staticPrefixes.some((prefix) => pathname.startsWith(prefix));
}

function serveStatic(req, res) {
  const requestUrl = new URL(req.url, `http://${req.headers.host || "localhost"}`);
  const pathname = requestUrl.pathname === "/" ? "/index.html" : decodeURIComponent(requestUrl.pathname);

  if (!isStaticPath(pathname)) {
    send(res, 404, "Not found");
    return;
  }

  const filePath = path.normalize(path.join(root, pathname));
  if (!filePath.startsWith(`${root}${path.sep}`)) {
    send(res, 403, "Forbidden");
    return;
  }

  fs.readFile(filePath, (error, data) => {
    if (error) {
      send(res, 404, "Not found");
      return;
    }

    const contentType = mimeTypes[path.extname(filePath)] || "application/octet-stream";
    res.writeHead(200, { "Content-Type": contentType });
    res.end(data);
  });
}

module.exports = function handler(req, res) {
  if (req.url.startsWith("/api/bytexl")) {
    bytexlHandler(req, res);
    return;
  }

  serveStatic(req, res);
};
