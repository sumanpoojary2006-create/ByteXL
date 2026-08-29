/* ByteXL Question Bank Intelligence.
 *
 * The server ships one dictionary-encoded fact table; every panel here is a
 * pivot over it, so filters never round-trip. Charts are hand-built SVG to keep
 * the page dependency-free and on the app's own design tokens.
 */
(function () {
  "use strict";

  /* Vercel serves this page statically and has no backend, so in production the
   * snapshot comes from the separately hosted API named in config.js. Running
   * `python run.py` serves the page and the API from one origin, so localhost
   * stays local rather than reaching out to the deployed backend. */
  function apiBase() {
    if (location.protocol === "file:") return "http://127.0.0.1:8000";
    if (location.hostname === "localhost" || location.hostname === "127.0.0.1") return "";
    var configured = String((window.IMAGE_CONVERTER_CONFIG && window.IMAGE_CONVERTER_CONFIG.apiBase) || "").trim();
    if (!configured) throw new Error("The analytics API is not configured in config.js.");
    var api = new URL(configured, location.href);
    if (api.hostname === "vercel.app" || api.hostname.endsWith(".vercel.app")) {
      throw new Error("Analytics cannot read from Vercel — configure an external API host in config.js.");
    }
    return api.origin;
  }
  var SERIES = ["--series-1", "--series-2", "--series-3", "--series-4", "--series-5", "--series-6", "--series-7", "--series-8"];
  var ORD = ["--ord-1", "--ord-2", "--ord-3", "--ord-0"]; // easy, medium, hard, unspecified
  // Sequential cyan ramp tuned for the graphite command-center surface.
  var HEAT = ["#171a2b", "#1b2440", "#203258", "#244773", "#285c8f", "#2c72a7", "#3189ba", "#37a0c9", "#43b7d6", "#59cbdf", "#7edce7", "#a9ebef"];
  var TYPE_LABEL = ["MCQ", "Coding", "Descriptive"];
  var DIFF_LABEL = ["Easy", "Medium", "Hard", "Unspecified"];
  var ROSTER_KEY = "bytexl.analytics.roster.v1";

  var DATA = null;      // raw snapshot
  var ROLES = {};       // author name -> lead | support | manager | system
  // months/tracks/subjects/authors are checkbox multi-selects: an empty Set means
  // "no filter" (show everything), same convention across all four. type stays a
  // single-select segmented control.
  var VIEW = { months: new Set(), tracks: new Set(), subjects: new Set(), authors: new Set(), type: "" };
  var initialMonthScope = true;
  var matrixType = 1;
  var rows = [];        // filtered row indices
  var months = [];      // month keys in the active window
  var bound = false;    // controls are bound once, not on every snapshot load
  var lastGeneratedAtMs = null; // for the ticking "Updated Xs ago" label
  var POLL_MS = 60000;  // how often the browser checks for a newer snapshot
  var FORCE_REFRESH_MS = 5 * 60000; // how often an open dashboard rebuilds from ByteXL
  var lastForcedRefreshMs = 0;
  var loadInFlight = false;
  var metricHistory = {};
  var resilienceScoreHistory = 0;
  var motionOK = !window.matchMedia || !window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var activeDashboard = "overview";
  var DASHBOARDS = {
    overview: { title: "Decision overview", description: "The signals that need attention now." },
    production: { title: "Production performance", description: "Growth, contribution, and bank movement over time." },
    coverage: { title: "Coverage & readiness", description: "Subject, track, company, and assessment readiness." },
    quality: { title: "Quality control", description: "Blueprint balance and metadata health." },
    team: { title: "Team & ownership", description: "Roles, contribution ownership, and curation rules." }
  };
  var ANALYTICS_INDEX = [
    { title: "Decision overview", view: "overview", target: "tiles", tags: "summary kpi total questions mcq coding growth net change executive pulse" },
    { title: "Knowledge resilience", view: "overview", target: "metric-resilience", tags: "fragile subjects risk concentration single author exposed ownership continuity hidden signal" },
    { title: "Monthly production", view: "production", target: "metric-monthly", tags: "monthly trend volume added questions growth output over time" },
    { title: "Curated vs uploaded", view: "production", target: "metric-curated", tags: "content leads support engineers role curated share uploaded" },
    { title: "Bank churn", view: "production", target: "metric-churn", tags: "archived deleted additions net change shrinking growing" },
    { title: "Weekly movement", view: "production", target: "metric-weekly", tags: "week over week weekly added archived net movement trend" },
    { title: "Content Lead output", view: "production", target: "metric-lead", tags: "who authored most top author contributor people leader productivity" },
    { title: "Subject coverage", view: "coverage", target: "metric-subject", tags: "subjects monthly gaps volume curriculum" },
    { title: "Track coverage", view: "coverage", target: "metric-track", tags: "tracks programming fundamentals tactical drills categories monthly content lead ownership" },
    { title: "Company mock coverage", view: "coverage", target: "metric-company", tags: "company hiring mock tests employers tagged readiness" },
    { title: "Akila company-specific output", view: "coverage", target: "metric-akila-company", tags: "Akila company specific questions author special category monthly" },
    { title: "Standardized assessments", view: "coverage", target: "metric-standard", tags: "standard tests papers ready assign assessment coverage" },
    { title: "Difficulty matrix", view: "quality", target: "metric-matrix", tags: "easy medium hard topic balance blueprint difficulty unspecified" },
    { title: "Data quality & risk", view: "quality", target: "metric-quality", tags: "missing subject topic explanation difficulty gaps metadata quality reusable" },
    { title: "Author roster", view: "team", target: "metric-roster", tags: "team people roles author ownership content lead support manager" }
  ];

  function css(name) { return getComputedStyle(document.body).getPropertyValue(name).trim(); }
  function $(id) { return document.getElementById(id); }
  function fmt(n) { return (n === null || n === undefined) ? "–" : n.toLocaleString("en-IN"); }
  function pct(a, b) { return b ? Math.round((a / b) * 1000) / 10 : 0; }
  function monthLabel(key) {
    if (!key) return "";
    var p = key.split("-");
    return ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"][+p[1] - 1] + " " + p[0].slice(2);
  }

  /* -------------------------------------------------------------- motion */
  function animateBars(svg, axis) {
    if (!motionOK || !svg || !svg.animate) return;
    Array.prototype.forEach.call(svg.querySelectorAll(".chart-bar"), function (node, i) {
      node.style.transformBox = "fill-box";
      node.style.transformOrigin = axis === "x" ? "left center" : "center bottom";
      node.animate([
        { transform: axis === "x" ? "scaleX(.04)" : "scaleY(.04)", opacity: .18 },
        { transform: "scale(1)", opacity: 1 }
      ], { duration: 520, delay: Math.min(i * 22, 180), easing: "cubic-bezier(.2,.75,.25,1)", fill: "both" });
    });
    Array.prototype.forEach.call(svg.querySelectorAll(".dlabel"), function (node, i) {
      node.animate([{ opacity: 0 }, { opacity: 1 }], { duration: 300, delay: 300 + Math.min(i * 18, 160), fill: "both" });
    });
  }
  function animateHeat(svg) {
    if (!motionOK || !svg || !svg.animate) return;
    Array.prototype.forEach.call(svg.querySelectorAll(".heat-cell"), function (node, i) {
      node.style.transformBox = "fill-box"; node.style.transformOrigin = "center";
      node.animate([{ transform: "scale(.72)", opacity: 0 }, { transform: "scale(1)", opacity: 1 }],
        { duration: 360, delay: Math.min(i * 7, 260), easing: "cubic-bezier(.2,.8,.25,1)", fill: "both" });
    });
  }
  function parseMetric(raw) {
    var clean = String(raw || "").replace(/,/g, "").replace(/[^0-9+\-.]/g, "");
    var n = Number(clean); return isFinite(n) ? n : null;
  }
  function metricText(raw, value) {
    var decimals = ((String(raw).match(/\.(\d+)/) || ["", ""])[1] || "").length;
    var out = value.toLocaleString("en-IN", { minimumFractionDigits: decimals, maximumFractionDigits: decimals });
    if (String(raw).trim().charAt(0) === "+" && value >= 0) out = "+" + out;
    if (/%\s*$/.test(String(raw))) out += "%";
    return out;
  }
  function animateMetrics(scope) {
    if (!motionOK) return;
    Array.prototype.forEach.call((scope || document).querySelectorAll(".tile .v,.score-value,.operating-value"), function (node) {
      var raw = node.childNodes.length ? node.childNodes[0].nodeValue || node.textContent : node.textContent;
      var target = parseMetric(raw); if (target === null) return;
      var labelNode = node.closest(".tile") && node.closest(".tile").querySelector(".k");
      var owner = node.closest("[id]");
      var key = (owner ? owner.id : "dashboard") + "|" + (labelNode ? labelNode.textContent : "resilience-score");
      var start = Object.prototype.hasOwnProperty.call(metricHistory, key) ? metricHistory[key] : 0;
      metricHistory[key] = target;
      var began = performance.now(), duration = 560;
      function tick(now) {
        var p = Math.min(1, (now - began) / duration), eased = 1 - Math.pow(1 - p, 3);
        var display = start + (target - start) * eased;
        node.childNodes[0].nodeValue = metricText(raw, display);
        if (p < 1 && node.isConnected) requestAnimationFrame(tick);
      }
      requestAnimationFrame(tick);
    });
  }

  /* ---------------------------------------------------------------- tooltip */
  var tip = null;
  function tipShow(evt, title, rowsIn) {
    if (!tip) tip = $("tooltip");
    var html = '<div class="tt-t">' + esc(title) + "</div>";
    rowsIn.forEach(function (r) {
      html += '<div class="tt-r">' + (r.color ? '<span class="sw" style="background:' + r.color + '"></span>' : "") +
        "<span>" + esc(r.label) + "</span><b>" + (typeof r.value === "number" ? fmt(r.value) : esc(r.value)) + "</b></div>";
    });
    tip.innerHTML = html;
    tip.style.opacity = "1";
    tipMove(evt);
  }
  function tipMove(evt) {
    if (!tip) return;
    var w = tip.offsetWidth, h = tip.offsetHeight;
    var x = evt.clientX + 14, y = evt.clientY + 14;
    if (x + w > innerWidth - 10) x = evt.clientX - w - 14;
    if (y + h > innerHeight - 10) y = evt.clientY - h - 14;
    tip.style.left = x + "px"; tip.style.top = y + "px";
  }
  function tipHide() { if (tip) tip.style.opacity = "0"; }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  /* ------------------------------------------------------------ svg helpers */
  function el(tag, attrs) {
    var n = document.createElementNS("http://www.w3.org/2000/svg", tag);
    for (var k in attrs) if (attrs[k] !== null && attrs[k] !== undefined) n.setAttribute(k, attrs[k]);
    return n;
  }
  /** Root <svg> that scales down to fit but never blows a small chart up. */
  function svgRoot(W, H, aria) {
    var s = el("svg", { viewBox: "0 0 " + W + " " + H, width: W, height: H, role: "img", "aria-label": aria || "" });
    s.style.maxWidth = "100%";
    s.style.height = "auto";
    return s;
  }
  /** Bar with 4px rounded data-end, square where it meets the baseline. */
  function barPath(x, y, w, h, vertical) {
    var r = Math.min(4, w / 2, h);
    if (h <= 0.5) return "";
    if (vertical) {
      return "M" + x + "," + (y + h) + "V" + (y + r) + "a" + r + "," + r + " 0 0 1 " + r + ",-" + r +
        "h" + (w - 2 * r) + "a" + r + "," + r + " 0 0 1 " + r + "," + r + "V" + (y + h) + "Z";
    }
    r = Math.min(4, h / 2, w);
    return "M" + x + "," + y + "h" + (w - r) + "a" + r + "," + r + " 0 0 1 " + r + "," + r +
      "v" + (h - 2 * r) + "a" + r + "," + r + " 0 0 1 -" + r + "," + r + "H" + x + "Z";
  }
  function niceTicks(max, count) {
    if (max <= 0) return [0];
    var raw = max / (count || 5), mag = Math.pow(10, Math.floor(Math.log10(raw)));
    var step = [1, 2, 2.5, 5, 10].map(function (m) { return m * mag; }).find(function (s) { return s >= raw; }) || 10 * mag;
    // The top tick must reach at least `max`, not just get close to it: rounding
    // the axis ceiling up to the next step can leave the last tick below the
    // real data max, which then draws the tallest bar taller than the plot area
    // and overflows into whatever sits below the chart.
    var top = Math.ceil(max / step) * step;
    var out = [];
    for (var v = 0; v <= top + step * 0.001; v += step) out.push(v);
    return out;
  }
  function legend(host, items) {
    var d = document.createElement("div");
    d.className = "legend";
    items.forEach(function (i) {
      d.innerHTML += '<span class="item"><span class="sw" style="background:' + i.color + '"></span>' + esc(i.label) + "</span>";
    });
    host.appendChild(d);
  }
  function caption(host, text) {
    var c = document.createElement("figcaption");
    c.textContent = text;
    host.appendChild(c);
  }

  /** Vertical grouped or stacked column chart. */
  function columns(host, opts) {
    host.innerHTML = "";
    var cats = opts.categories, series = opts.series, stacked = !!opts.stacked;
    if (!cats.length) { host.innerHTML = '<p class="muted">No data in this selection.</p>'; return; }
    legend(host, series.map(function (s) { return { label: s.label, color: s.color }; }));

    // Leave room for a total label when a bar lands exactly on the top tick.
    var W = 980, H = opts.height || 300, m = { t: 30, r: 14, b: 42, l: 58 };
    var pw = W - m.l - m.r, ph = H - m.t - m.b;
    var totals = cats.map(function (_, i) {
      return stacked ? series.reduce(function (a, s) { return a + (s.values[i] || 0); }, 0)
        : Math.max.apply(null, series.map(function (s) { return s.values[i] || 0; }));
    });
    var max = Math.max.apply(null, totals.concat([1]));
    var ticks = niceTicks(max, 5);
    max = ticks[ticks.length - 1] || max;
    var y = function (v) { return m.t + ph - (v / max) * ph; };

    var svg = svgRoot(W, H, opts.aria);
    ticks.forEach(function (t) {
      svg.appendChild(el("line", { x1: m.l, x2: m.l + pw, y1: y(t), y2: y(t), stroke: css("--grid"), "stroke-width": 1 }));
      var lb = el("text", { x: m.l - 9, y: y(t) + 4, "text-anchor": "end", class: "axs" });
      lb.textContent = t >= 1000 ? (t / 1000) + "k" : t;
      svg.appendChild(lb);
    });

    var band = pw / cats.length, inner = Math.min(band * 0.68, stacked ? 46 : 78);
    cats.forEach(function (cat, i) {
      var cx = m.l + band * i + band / 2;
      if (stacked) {
        var acc = 0;
        series.forEach(function (s) {
          var v = s.values[i] || 0; if (!v) return;
          var h = (v / max) * ph, yy = y(acc + v);
          // 2px surface gap between adjacent segments rather than a stroke.
          var seg = el("path", { d: barPath(cx - inner / 2, yy, inner, Math.max(h - 2, 0.6), true), fill: s.color, class: "chart-bar" });
          bindTip(seg, cat, series.map(function (t) { return { label: t.label, value: t.values[i] || 0, color: t.color }; }));
          svg.appendChild(seg);
          acc += v;
        });
        var tot = el("text", { x: cx, y: y(acc) - 7, "text-anchor": "middle", class: "dlabel" });
        tot.textContent = fmt(acc); svg.appendChild(tot);
      } else {
        var bw = (inner - 2 * (series.length - 1)) / series.length;
        series.forEach(function (s, si) {
          var v = s.values[i] || 0;
          var h = (v / max) * ph, bx = cx - inner / 2 + si * (bw + 2);
          if (v > 0) {
            var b = el("path", { d: barPath(bx, y(v), bw, h, true), fill: s.color, class: "chart-bar" });
            bindTip(b, cat, series.map(function (t) { return { label: t.label, value: t.values[i] || 0, color: t.color }; }));
            svg.appendChild(b);
          }
        });
        // Direct-label the leading series only; the axis and tooltip carry the rest.
        var lead = el("text", { x: cx, y: y(series[0].values[i] || 0) - 7, "text-anchor": "middle", class: "dlabel" });
        lead.textContent = fmt(series[0].values[i] || 0); svg.appendChild(lead);
      }
      var xl = el("text", { x: cx, y: H - m.b + 20, "text-anchor": "middle", class: "ax" });
      xl.textContent = cat; svg.appendChild(xl);
    });
    svg.appendChild(el("line", { x1: m.l, x2: m.l + pw, y1: m.t + ph, y2: m.t + ph, stroke: css("--line-hi"), "stroke-width": 1 }));
    host.appendChild(svg);
    animateBars(svg, "y");
    if (opts.caption) caption(host, opts.caption);
  }

  /** Horizontal bars — one series, ranked. */
  function hbars(host, opts) {
    host.innerHTML = "";
    var items = opts.items;
    if (!items.length) { host.innerHTML = '<p class="muted">No data in this selection.</p>'; return; }
    var rowH = 30, W = 620, m = { t: 6, r: 74, b: 24, l: opts.labelWidth || 168 };
    var H = m.t + items.length * rowH + m.b;
    var pw = W - m.l - m.r;
    var max = Math.max.apply(null, items.map(function (i) { return i.value; }).concat([1]));
    var svg = svgRoot(W, H, opts.aria);
    items.forEach(function (it, i) {
      var yy = m.t + i * rowH;
      var lb = el("text", { x: m.l - 10, y: yy + rowH / 2 + 4, "text-anchor": "end", class: "ax" });
      lb.textContent = it.label.length > 26 ? it.label.slice(0, 25) + "…" : it.label;
      svg.appendChild(lb);
      var w = (it.value / max) * pw;
      var b = el("path", { d: barPath(m.l, yy + 6, Math.max(w, 1), rowH - 14, false), fill: it.color || css("--series-1"), class: "chart-bar" });
      bindTip(b, it.label, (it.detail || []).concat([{ label: opts.valueLabel || "Questions", value: it.value }]));
      svg.appendChild(b);
      var vl = el("text", { x: m.l + w + 9, y: yy + rowH / 2 + 4, class: "dlabel" });
      vl.textContent = fmt(it.value) + (opts.suffix || ""); svg.appendChild(vl);
    });
    host.appendChild(svg);
    animateBars(svg, "x");
    if (opts.caption) caption(host, opts.caption);
  }

  /** 100% stacked horizontal bars — composition, not magnitude. */
  function pctBars(host, opts) {
    host.innerHTML = "";
    var items = opts.items;
    if (!items.length) { host.innerHTML = '<p class="muted">No data in this selection.</p>'; return; }
    legend(host, opts.series);
    var rowH = 30, W = 900, m = { t: 6, r: 78, b: 8, l: 206 };
    var H = m.t + items.length * rowH + m.b, pw = W - m.l - m.r;
    var svg = svgRoot(W, H, opts.aria);
    items.forEach(function (it, i) {
      var yy = m.t + i * rowH, total = it.values.reduce(function (a, b) { return a + b; }, 0) || 1;
      var lb = el("text", { x: m.l - 10, y: yy + rowH / 2 + 4, "text-anchor": "end", class: "ax" });
      lb.textContent = it.label.length > 30 ? it.label.slice(0, 29) + "…" : it.label;
      svg.appendChild(lb);
      var acc = 0;
      it.values.forEach(function (v, si) {
        if (!v) return;
        var w = (v / total) * pw;
        var seg = el("path", { d: barPath(m.l + acc, yy + 6, Math.max(w - 2, 1), rowH - 14, false), fill: opts.series[si].color, class: "chart-bar" });
        bindTip(seg, it.label, opts.series.map(function (s, k) {
          return { label: s.label, value: it.values[k] + " (" + pct(it.values[k], total) + "%)", color: s.color };
        }));
        svg.appendChild(seg);
        acc += w;
      });
      var vl = el("text", { x: m.l + pw + 9, y: yy + rowH / 2 + 4, class: "dlabel" });
      vl.textContent = fmt(total); svg.appendChild(vl);
    });
    host.appendChild(svg);
    animateBars(svg, "x");
    if (opts.caption) caption(host, opts.caption);
  }

  /** Matrix heatmap with a scale legend. */
  function heatmap(host, opts) {
    host.innerHTML = "";
    if (!opts.rows.length) { host.innerHTML = '<p class="muted">No data in this selection.</p>'; return; }
    var cols = opts.columns, cellW = 74, cellH = 27, m = { t: 30, r: 10, b: 6, l: 224 };
    var W = m.l + cols.length * cellW + m.r, H = m.t + opts.rows.length * cellH + m.b;
    var max = Math.max.apply(null, opts.rows.map(function (r) { return Math.max.apply(null, r.values); }).concat([1]));
    var svg = svgRoot(W, H, opts.aria);
    cols.forEach(function (c, j) {
      var t = el("text", { x: m.l + j * cellW + cellW / 2, y: m.t - 11, "text-anchor": "middle", class: "ax" });
      t.textContent = c; svg.appendChild(t);
    });
    opts.rows.forEach(function (r, i) {
      var t = el("text", { x: m.l - 10, y: m.t + i * cellH + cellH / 2 + 4, "text-anchor": "end", class: "ax" });
      t.textContent = r.label.length > 32 ? r.label.slice(0, 31) + "…" : r.label;
      svg.appendChild(t);
      r.values.forEach(function (v, j) {
        var idx = v <= 0 ? -1 : Math.min(HEAT.length - 1, Math.floor(Math.sqrt(v / max) * (HEAT.length - 1)));
        var fill = idx < 0 ? "rgba(255,255,255,.025)" : HEAT[idx];
        var cell = el("rect", { x: m.l + j * cellW + 1, y: m.t + i * cellH + 1, width: cellW - 3, height: cellH - 3, rx: 4, fill: fill, class: "heat-cell" });
        bindTip(cell, r.label + " · " + cols[j], (r.detail && r.detail[j]) || [{ label: "Questions", value: v }]);
        svg.appendChild(cell);
        if (v > 0) {
          var lb = el("text", {
            x: m.l + j * cellW + cellW / 2, y: m.t + i * cellH + cellH / 2 + 4, "text-anchor": "middle",
            // White on the darker ramp; dark ink only on the palest top cells.
            fill: idx >= 10 ? "#081018" : "#ffffff", "font-size": 10.5, "font-weight": 700
          });
          lb.textContent = fmt(v); svg.appendChild(lb);
        }
      });
    });
    host.appendChild(svg);
    animateHeat(svg);
    var sc = document.createElement("div");
    sc.className = "legend";
    sc.innerHTML = '<span class="item">Fewer</span>' + HEAT.map(function (c) {
      return '<span class="sw" style="background:' + c + ';width:20px;height:11px;border-radius:2px"></span>';
    }).join("") + '<span class="item">More</span>';
    host.appendChild(sc);
    if (opts.caption) caption(host, opts.caption);
  }

  function bindTip(node, title, rowsIn) {
    node.style.cursor = "pointer";
    node.addEventListener("mouseenter", function (e) { tipShow(e, title, rowsIn); });
    node.addEventListener("mousemove", tipMove);
    node.addEventListener("mouseleave", tipHide);
  }

  function table(host, head, body, note) {
    var h = '<div class="scroll"><table><thead><tr>' +
      head.map(function (c) { return "<th>" + esc(c) + "</th>"; }).join("") + "</tr></thead><tbody>" +
      body.map(function (r) {
        return "<tr>" + r.map(function (c, i) {
          return '<td class="' + (i ? "num" : "") + '">' + (c && c.html ? c.html : esc(c === null || c === undefined ? "" : c)) + "</td>";
        }).join("") + "</tr>";
      }).join("") + "</tbody></table></div>";
    host.innerHTML = h + (note ? '<p class="muted" style="font-size:11.5px;margin-top:9px">' + esc(note) + "</p>" : "");
  }

  /* ------------------------------------------------------------ aggregation */
  function roleOf(authorIdx) {
    return ROLES[DATA.dims.authors[authorIdx]] || "support";
  }

  function activeMonths() {
    var all = DATA.dims.months.slice().filter(Boolean).sort();
    if (!VIEW.months.size) return all; // empty selection = no filter, same as every other dimension
    return all.filter(function (m) { return VIEW.months.has(m); });
  }

  /** Row indices matching the current filters, by creation month. */
  function computeRows() {
    var c = DATA.cols, dims = DATA.dims;
    var monthSet = {};
    months.forEach(function (m) { monthSet[dims.months.indexOf(m)] = 1; });
    var trackOf = DATA.tracks;
    var out = [];
    for (var i = 0; i < c.cm.length; i++) {
      if (!monthSet[c.cm[i]]) continue;
      if (VIEW.type !== "" && c.ty[i] !== +VIEW.type) continue;
      if (VIEW.authors.size && !VIEW.authors.has(dims.authors[c.au[i]])) continue;
      var subj = dims.subjects[c.su[i]];
      if (VIEW.subjects.size && !VIEW.subjects.has(subj)) continue;
      if (VIEW.tracks.size && !VIEW.tracks.has(trackOf[subj])) continue;
      out.push(i);
    }
    return out;
  }

  /** Rows archived within the window, filtered the same way (archival is its own event). */
  function archivedRows() {
    var c = DATA.cols, dims = DATA.dims;
    var monthSet = {};
    months.forEach(function (m) { monthSet[dims.months.indexOf(m)] = 1; });
    var out = [];
    for (var i = 0; i < c.am.length; i++) {
      if (c.am[i] < 0 || !monthSet[c.am[i]]) continue;
      if (VIEW.type !== "" && c.ty[i] !== +VIEW.type) continue;
      if (VIEW.authors.size && !VIEW.authors.has(dims.authors[c.au[i]])) continue;
      var subj = dims.subjects[c.su[i]];
      if (VIEW.subjects.size && !VIEW.subjects.has(subj)) continue;
      if (VIEW.tracks.size && !VIEW.tracks.has(DATA.tracks[subj])) continue;
      out.push(i);
    }
    return out;
  }

  function byMonthType() {
    var c = DATA.cols, idx = {};
    months.forEach(function (m, i) { idx[DATA.dims.months.indexOf(m)] = i; });
    var mcq = months.map(function () { return 0; }), cod = months.map(function () { return 0; }), desc = months.map(function () { return 0; });
    rows.forEach(function (i) {
      var k = idx[c.cm[i]];
      if (k === undefined) return;
      if (c.ty[i] === 1) cod[k]++; else if (c.ty[i] === 2) desc[k]++; else mcq[k]++;
    });
    return { mcq: mcq, coding: cod, desc: desc };
  }

  /* --------------------------------------------------------------- panels */
  function renderTiles() {
    var t = byMonthType();
    var total = rows.length;
    var mcq = t.mcq.reduce(add, 0), cod = t.coding.reduce(add, 0);
    var arch = archivedRows().length;
    var leadN = 0;
    rows.forEach(function (i) { if (roleOf(DATA.cols.au[i]) === "lead") leadN++; });
    var net = total - arch;
    var last = months[months.length - 1], prev = months[months.length - 2];
    var lastN = t.mcq[months.length - 1] + t.coding[months.length - 1] + t.desc[months.length - 1];
    var prevN = months.length > 1 ? t.mcq[months.length - 2] + t.coding[months.length - 2] + t.desc[months.length - 2] : 0;
    var delta = prevN ? Math.round(((lastN - prevN) / prevN) * 100) : 0;

    var tiles = [
      { k: "Questions added", v: fmt(total), d: months.length + " month" + (months.length > 1 ? "s" : "") + " in view" },
      { k: "MCQs", v: fmt(mcq), d: pct(mcq, total) + "% of additions" },
      { k: "Coding questions", v: fmt(cod), d: pct(cod, total) + "% of additions" },
      { k: "Curated by Content Leads", v: pct(leadN, total) + "%", d: fmt(leadN) + " of " + fmt(total) + " questions" },
      { k: "Archived in window", v: fmt(arch), d: arch > total ? "Exceeds additions" : pct(arch, total) + "% of additions", cls: arch > total ? "down" : "" },
      { k: "Net bank change", v: (net >= 0 ? "+" : "") + fmt(net), d: net >= 0 ? "Bank grew" : "Bank shrank", cls: net >= 0 ? "up" : "down" },
      { k: monthLabel(last) + " vs " + monthLabel(prev), v: (delta >= 0 ? "+" : "") + delta + "%", d: fmt(prevN) + " → " + fmt(lastN), cls: delta >= 0 ? "up" : "down" }
    ];
    $("tiles").innerHTML = tiles.map(function (x) {
      return '<div class="tile"><div class="k">' + esc(x.k) + '</div><div class="v">' + x.v +
        '</div><div class="d ' + (x.cls || "") + '">' + esc(x.d) + "</div></div>";
    }).join("");
  }
  function add(a, b) { return a + b; }

  function executiveSignals() {
    var c = DATA.cols, dims = DATA.dims, selected = rows.length, total = selected || 1;
    var latestKey = months[months.length - 1], previousKey = months[months.length - 2];
    var latestIndex = dims.months.indexOf(latestKey), previousIndex = dims.months.indexOf(previousKey);
    var latest = 0, previous = 0, qualityDebt = 0, subjects = {};
    rows.forEach(function (i) {
      if (c.cm[i] === latestIndex) latest++;
      if (c.cm[i] === previousIndex) previous++;
      var subject = dims.subjects[c.su[i]], topic = dims.topics[c.tp[i]];
      if (!c.ex[i] || c.df[i] === 3 || subject === "(no subject)" || topic === "(no topic)") qualityDebt++;
      if (!subject || subject === "(no subject)") return;
      if (!subjects[subject]) subjects[subject] = { n: 0, authors: {} };
      subjects[subject].n++;
      var author = dims.authors[c.au[i]];
      subjects[subject].authors[author] = (subjects[subject].authors[author] || 0) + 1;
    });
    var concentrated = [], exposed = 0;
    Object.keys(subjects).forEach(function (subject) {
      var pool = subjects[subject]; if (pool.n < 25) return;
      var counts = Object.keys(pool.authors).map(function (author) { return pool.authors[author]; });
      var topShare = Math.max.apply(null, counts) / pool.n;
      if (topShare >= .7) { concentrated.push(subject); exposed += pool.n; }
    });
    var archived = archivedRows().length;
    var momentum = previous ? Math.round(((latest - previous) / previous) * 100) : 0;
    var debtPct = pct(qualityDebt, total), exposedPct = pct(exposed, total), archivePct = pct(archived, total);
    var risk = .5 * exposedPct + .28 * debtPct + .12 * Math.min(100, archivePct) + .1 * Math.max(0, -momentum);
    var score = selected ? Math.max(0, Math.min(100, Math.round(100 - risk))) : 0;
    return {
      total: selected, latest: latest, previous: previous, latestKey: latestKey, momentum: momentum,
      archived: archived, net: rows.length - archived, archivePct: archivePct,
      qualityDebt: qualityDebt, debtPct: debtPct,
      concentrated: concentrated.length, exposed: exposed, exposedPct: exposedPct,
      score: score, state: !selected ? "No data in this scope" : score >= 72 ? "Strong operating position" : score >= 55 ? "Guarded — intervention needed" : "Exposed — act now"
    };
  }

  function renderExecutiveBrief() {
    var s = executiveSignals(), headline;
    if (!s.total) headline = 'This scope has no questions; <em>widen the filters to restore the decision model.</em>';
    else if (s.exposedPct >= 45) headline = 'The bank is growing, but its knowledge base is <em>too concentrated to scale safely.</em>';
    else if (s.debtPct >= 25) headline = 'Production is healthy; <em>metadata debt is now the constraint.</em>';
    else if (s.momentum < 0) headline = 'Question-bank momentum has turned; <em>protect the next production cycle.</em>';
    else headline = 'The bank is expanding with <em>manageable operating risk.</em>';

    var host = $("executive-brief");
    host.innerHTML = '<div class="executive-hero"><div class="executive-copy">' +
      '<div class="signal-label">Executive readout</div><div class="executive-headline">' + headline + '</div>' +
      '<p class="executive-summary">' + monthLabel(s.latestKey) + ' production is <b>' + (s.momentum >= 0 ? "+" : "") + s.momentum +
      '%</b> versus the prior month. At the same time, <b>' + s.exposedPct + '%</b> of questions in view sit in concentrated subject pools and <b>' +
      s.debtPct + '%</b> carry at least one reuse-blocking metadata gap.</p>' +
      '<div class="hero-facts"><span class="hero-fact"><b>' + fmt(s.net) + '</b> net bank movement</span>' +
      '<span class="hero-fact"><b>' + s.concentrated + '</b> concentrated subjects</span>' +
      '<span class="hero-fact"><b>' + fmt(s.qualityDebt) + '</b> questions need enrichment</span></div></div>' +
      '<div class="operating-score"><div class="score-orbit" style="--operating:0"><div class="operating-value">' + s.score +
      '<small>Operating score</small></div></div><div class="operating-state">' + esc(s.state) + '</div>' +
      '<div class="operating-note">Weighted from concentration, metadata debt, archive pressure, and negative momentum.</div></div></div>';
    requestAnimationFrame(function () {
      var orbit = host.querySelector(".score-orbit"); if (orbit) orbit.style.setProperty("--operating", s.score);
    });

    var priorities = [
      { severity: s.exposedPct, metric: s.exposedPct + "%", title: "Diversify knowledge ownership", copy: fmt(s.exposed) + " questions depend on subject pools where one author supplied at least 70%.", view: "overview", target: "metric-resilience", action: "Inspect resilience", color: "#55dfe4", glow: "rgba(53,215,232,.2)" },
      { severity: s.debtPct, metric: s.debtPct + "%", title: "Pay down metadata debt", copy: fmt(s.qualityDebt) + " questions have a missing subject, topic, difficulty, or explanation.", view: "quality", target: "metric-quality", action: "Open quality control", color: "#a78bfa", glow: "rgba(139,92,246,.22)" },
      { severity: Math.max(5, s.archivePct - 40, -s.momentum), metric: (s.momentum >= 0 ? "+" : "") + s.momentum + "%", title: s.momentum >= 0 ? "Protect production momentum" : "Reverse the production decline", copy: fmt(s.archived) + " questions were archived in the selected window; net movement is " + (s.net >= 0 ? "+" : "") + fmt(s.net) + ".", view: "production", target: "metric-churn", action: "Review production", color: "#f27bcc", glow: "rgba(232,70,199,.2)" }
    ].sort(function (a, b) { return b.severity - a.severity; });
    $("priority-actions").innerHTML = '<div class="priority-grid">' + priorities.map(function (p, i) {
      return '<article class="priority-card" style="--priority-color:' + p.color + ';--priority-glow:' + p.glow + '">' +
        '<div class="priority-top"><span class="priority-rank">Priority ' + (i + 1) + '</span><span class="priority-metric">' + esc(p.metric) + '</span></div>' +
        '<div class="priority-title">' + esc(p.title) + '</div><div class="priority-copy">' + esc(p.copy) + '</div>' +
        '<button class="brief-jump" data-view="' + p.view + '" data-target="' + p.target + '">' + esc(p.action) + ' →</button></article>';
    }).join("") + '</div>';
    Array.prototype.forEach.call($("priority-actions").querySelectorAll(".brief-jump"), function (button) {
      button.addEventListener("click", function () { setDashboard(button.dataset.view, button.dataset.target, false); });
    });
  }

  /**
   * Hidden operational signal: a bank can have thousands of questions and
   * still be a single point of failure if one author owns a subject, or if the
   * pool is hard to review and rebalance. This turns those latent weaknesses
   * into one resilience score and a ranked intervention list.
   */
  function renderResilience() {
    var c = DATA.cols, dims = DATA.dims, agg = {};
    rows.forEach(function (i) {
      var subject = dims.subjects[c.su[i]];
      if (!subject || subject === "(no subject)") return;
      if (!agg[subject]) agg[subject] = { n: 0, authors: {}, noExpl: 0, noDiff: 0, mcq: 0, coding: 0 };
      var a = agg[subject], author = dims.authors[c.au[i]];
      a.n++; a.authors[author] = (a.authors[author] || 0) + 1;
      if (!c.ex[i]) a.noExpl++;
      if (c.df[i] === 3) a.noDiff++;
      if (c.ty[i] === 1) a.coding++; else if (c.ty[i] === 0) a.mcq++;
    });

    var scored = Object.keys(agg).filter(function (s) { return agg[s].n >= 25; }).map(function (subject) {
      var a = agg[subject], counts = Object.keys(a.authors).map(function (k) { return a.authors[k]; });
      var top = Math.max.apply(null, counts), topShare = top / a.n;
      var hhi = counts.reduce(function (sum, n) { var share = n / a.n; return sum + share * share; }, 0);
      var effective = hhi ? 1 / hhi : 0;
      var qualityGap = ((a.noExpl / a.n) + (a.noDiff / a.n)) / 2;
      var inventoryGap = Math.max(0, (120 - a.n) / 120);
      var formatGap = (!a.mcq || !a.coding) ? 1 : 0;
      var risk = Math.round(100 * (.55 * topShare + .25 * qualityGap + .12 * inventoryGap + .08 * formatGap));
      return { subject: subject, n: a.n, risk: risk, topShare: topShare, effective: effective, noExpl: a.noExpl, noDiff: a.noDiff, formatGap: formatGap };
    }).sort(function (a, b) { return b.risk - a.risk || b.n - a.n; });

    var host = $("c-resilience");
    if (!scored.length) {
      host.innerHTML = '<p class="muted">Select a wider period to calculate resilience; a subject needs at least 25 questions in view.</p>';
      return;
    }
    var weight = scored.reduce(function (sum, x) { return sum + x.n; }, 0) || 1;
    var weightedRisk = scored.reduce(function (sum, x) { return sum + x.risk * x.n; }, 0) / weight;
    var score = Math.max(0, Math.round(100 - weightedRisk));
    var concentrated = scored.filter(function (x) { return x.topShare >= .7; });
    var exposed = concentrated.reduce(function (sum, x) { return sum + x.n; }, 0);
    var effectiveAvg = scored.reduce(function (sum, x) { return sum + x.effective * x.n; }, 0) / weight;
    var state = score >= 65 ? "Resilient" : score >= 45 ? "Needs attention" : "Fragile";
    var color = score >= 65 ? css("--green") : score >= 45 ? css("--amber") : css("--red");
    var previous = resilienceScoreHistory; resilienceScoreHistory = score;

    host.innerHTML = '<div class="insight-grid"><div class="score-wrap">' +
      '<div class="score-ring" style="--score:' + previous + ';--ring-color:' + color + '"><div class="score-value">' + score + '<small>Resilience / 100</small></div></div>' +
      '<div class="score-state">' + state + '</div></div><div class="insight-side">' +
      '<div class="tiles"><div class="tile"><div class="k">Concentrated subjects</div><div class="v">' + concentrated.length + '</div><div class="d down">One author supplied at least 70%</div></div>' +
      '<div class="tile"><div class="k">Questions exposed</div><div class="v">' + pct(exposed, weight) + '%</div><div class="d">' + fmt(exposed) + ' questions in concentrated pools</div></div>' +
      '<div class="tile"><div class="k">Effective contributors</div><div class="v">' + effectiveAvg.toFixed(1) + '</div><div class="d">Average independent author strength</div></div></div>' +
      '<div id="c-resilience-bars"></div>' +
      '<p class="metric-note"><b>How it works:</b> risk blends dominant-author concentration (55%), missing explanations and difficulty (25%), thin inventory (12%), and missing MCQ/coding variety (8%). Subjects below 25 questions are excluded to avoid noisy small-sample alarms.</p>' +
      '</div></div>';
    requestAnimationFrame(function () {
      var ring = host.querySelector(".score-ring"); if (ring) ring.style.setProperty("--score", score);
    });
    hbars($("c-resilience-bars"), {
      labelWidth: 182, valueLabel: "Risk score", suffix: "%",
      items: scored.slice(0, 10).map(function (x) {
        return {
          label: x.subject, value: x.risk,
          color: x.risk >= 65 ? css("--series-8") : x.risk >= 50 ? css("--series-4") : css("--series-7"),
          detail: [
            { label: "Dominant author", value: Math.round(x.topShare * 100) + "%" },
            { label: "Effective contributors", value: x.effective.toFixed(1) },
            { label: "Questions", value: x.n },
            { label: "Missing explanation", value: x.noExpl },
            { label: "Missing difficulty", value: x.noDiff }
          ]
        };
      }),
      aria: "Subjects with the highest knowledge concentration risk",
      caption: "Highest-risk subject pools in the current filter selection. Lower is safer."
    });
  }

  function renderMonthly() {
    var t = byMonthType();
    var cats = months.map(monthLabel);
    columns($("c-monthly"), {
      categories: cats, height: 320,
      series: [
        { label: "MCQ", color: css("--series-1"), values: t.mcq },
        { label: "Coding", color: css("--series-2"), values: t.coding }
      ],
      aria: "Questions added per month by format",
      caption: "Labelled values are MCQ counts; hover any bar for the full split."
    });
    table($("tb-monthly"), ["Month", "MCQ", "Coding", "Descriptive", "Total", "Coding %"],
      months.map(function (m, i) {
        var tot = t.mcq[i] + t.coding[i] + t.desc[i];
        return [monthLabel(m), fmt(t.mcq[i]), fmt(t.coding[i]), fmt(t.desc[i]), fmt(tot), pct(t.coding[i], tot) + "%"];
      }));
  }

  function renderCurated() {
    var c = DATA.cols, idx = {};
    months.forEach(function (m, i) { idx[DATA.dims.months.indexOf(m)] = i; });
    var lead = months.map(function () { return 0; }), sup = months.map(function () { return 0; }), other = months.map(function () { return 0; });
    rows.forEach(function (i) {
      var k = idx[c.cm[i]]; if (k === undefined) return;
      var r = roleOf(c.au[i]);
      if (r === "lead") lead[k]++; else if (r === "support") sup[k]++; else other[k]++;
    });
    var host = $("c-curated");
    host.innerHTML = '<div class="role-share-grid">' + months.map(function (m, i) {
      var total = lead[i] + sup[i] + other[i], leadPct = pct(lead[i], total), supPct = pct(sup[i], total);
      return '<div class="role-share"><div class="role-share-month">' + esc(monthLabel(m)) + '</div>' +
        '<div class="role-share-values"><b>' + leadPct + '% <small>Lead</small></b><b>' + supPct + '% <small>Support</small></b></div>' +
        '<div class="share-bar"><i style="width:' + leadPct + '%"></i><i style="width:' + supPct + '%"></i></div>' +
        '<div class="role-share-counts">' + fmt(lead[i]) + ' curated · ' + fmt(sup[i]) + ' uploaded · ' + pct(other[i], total) + '% other</div></div>';
    }).join("") + '</div><div id="c-curated-chart"></div>';
    columns($("c-curated-chart"), {
      categories: months.map(monthLabel), stacked: true, height: 290,
      series: [
        { label: "Content Leads", color: css("--series-1"), values: lead },
        { label: "Platform Support", color: css("--series-2"), values: sup },
        { label: "Manager / system", color: css("--series-7"), values: other }
      ],
      aria: "Questions by author role per month",
      caption: "Counts behind the monthly proportions shown above. Manager and system activity stays visible rather than being reassigned."
    });
  }

  function renderWeekly() {
    var c = DATA.cols, dims = DATA.dims, host = $("c-weekly"), tableHost = $("tb-weekly");
    if (!c.cw || !c.aw || !dims.weeks) {
      host.innerHTML = '<div class="warn">Week-level history is being prepared. Refresh after the analytics service has rebuilt its snapshot.</div>';
      tableHost.innerHTML = ""; return;
    }
    var weekSet = {}, added = {}, archived = {};
    rows.forEach(function (i) { var w = dims.weeks[c.cw[i]]; if (w) { weekSet[w] = 1; added[w] = (added[w] || 0) + 1; } });
    archivedRows().forEach(function (i) { var w = dims.weeks[c.aw[i]]; if (w) { weekSet[w] = 1; archived[w] = (archived[w] || 0) + 1; } });
    var weeks = Object.keys(weekSet).sort().slice(-14);
    function label(w) { var d = new Date(w + "T00:00:00"); return d.toLocaleDateString("en-IN", { day: "2-digit", month: "short" }); }
    if (!weeks.length) { host.innerHTML = '<p class="muted">No weekly activity in this selection.</p>'; tableHost.innerHTML = ""; return; }
    columns(host, {
      categories: weeks.map(label), height: 310,
      series: [
        { label: "Added", color: css("--series-3"), values: weeks.map(function (w) { return added[w] || 0; }) },
        { label: "Archived", color: css("--series-8"), values: weeks.map(function (w) { return archived[w] || 0; }) }
      ],
      aria: "Week over week questions added and archived",
      caption: "Monday-starting weeks. The latest 14 active weeks are shown when a wide period is selected."
    });
    table(tableHost, ["Week starting", "Added", "Archived", "Net"], weeks.map(function (w) {
      var a = added[w] || 0, r = archived[w] || 0;
      return [label(w) + " " + w.slice(0, 4), fmt(a), fmt(r), (a - r >= 0 ? "+" : "") + fmt(a - r)];
    }));
  }

  function renderChurn() {
    var c = DATA.cols, idx = {};
    months.forEach(function (m, i) { idx[DATA.dims.months.indexOf(m)] = i; });
    var added = months.map(function () { return 0; }), arch = months.map(function () { return 0; });
    rows.forEach(function (i) { var k = idx[c.cm[i]]; if (k !== undefined) added[k]++; });
    archivedRows().forEach(function (i) { var k = idx[c.am[i]]; if (k !== undefined) arch[k]++; });
    columns($("c-churn"), {
      categories: months.map(monthLabel), height: 290,
      series: [
        { label: "Added", color: css("--series-3"), values: added },
        { label: "Archived", color: css("--series-8"), values: arch }
      ],
      aria: "Questions added versus archived per month",
      caption: "Net: " + months.map(function (m, i) {
        var n = added[i] - arch[i];
        return monthLabel(m) + " " + (n >= 0 ? "+" : "") + fmt(n);
      }).join(" · ")
    });
  }

  function renderSubject() {
    var c = DATA.cols, dims = DATA.dims, idx = {};
    months.forEach(function (m, i) { idx[dims.months.indexOf(m)] = i; });
    var agg = {};
    rows.forEach(function (i) {
      var k = idx[c.cm[i]]; if (k === undefined) return;
      var s = dims.subjects[c.su[i]];
      if (!agg[s]) agg[s] = { total: 0, cells: months.map(function () { return { t: 0, m: 0, c: 0 }; }) };
      agg[s].total++;
      var cell = agg[s].cells[k];
      cell.t++; if (c.ty[i] === 1) cell.c++; else cell.m++;
    });
    var top = Object.keys(agg).sort(function (a, b) { return agg[b].total - agg[a].total; }).slice(0, 18);
    heatmap($("c-subject"), {
      columns: months.map(monthLabel),
      rows: top.map(function (s) {
        return {
          label: s, values: agg[s].cells.map(function (x) { return x.t; }),
          detail: agg[s].cells.map(function (x) {
            return [{ label: "MCQ", value: x.m, color: css("--series-1") }, { label: "Coding", value: x.c, color: css("--series-2") }, { label: "Total", value: x.t }];
          })
        };
      }),
      aria: "Questions per subject per month",
      caption: "Top 18 subjects by volume" + (Object.keys(agg).length > 18 ? " of " + Object.keys(agg).length + " active in this period." : ".")
    });
    var all = Object.keys(agg).sort(function (a, b) { return agg[b].total - agg[a].total; });
    table($("tb-subject"), ["Subject", "Track"].concat(months.map(monthLabel)).concat(["Total", "MCQ", "Coding"]),
      all.map(function (s) {
        var mcq = 0, cod = 0;
        agg[s].cells.forEach(function (x) { mcq += x.m; cod += x.c; });
        return [s, DATA.tracks[s] || "–"].concat(agg[s].cells.map(function (x) { return fmt(x.t); }))
          .concat([fmt(agg[s].total), fmt(mcq), fmt(cod)]);
      }), "All " + all.length + " subjects active in the selected period.");
  }

  function renderLead() {
    var c = DATA.cols, dims = DATA.dims, idx = {};
    months.forEach(function (m, i) { idx[dims.months.indexOf(m)] = i; });
    var agg = {};
    rows.forEach(function (i) {
      var name = dims.authors[c.au[i]];
      if (roleOf(c.au[i]) !== "lead") return;
      var k = idx[c.cm[i]]; if (k === undefined) return;
      if (!agg[name]) agg[name] = { total: 0, mcq: 0, cod: 0, cells: months.map(function () { return { t: 0, m: 0, c: 0 }; }) };
      agg[name].total++;
      var cell = agg[name].cells[k]; cell.t++;
      if (c.ty[i] === 1) { cell.c++; agg[name].cod++; } else { cell.m++; agg[name].mcq++; }
    });
    var names = Object.keys(agg).sort(function (a, b) { return agg[b].total - agg[a].total; });
    if (!names.length) { $("c-lead").innerHTML = '<p class="muted">No Content Lead output in this selection.</p>'; $("tb-lead").innerHTML = ""; return; }
    // One segment per month and format makes both dimensions explicit at once.
    var shown = months.slice(-4), leadSeries = [];
    shown.forEach(function (m, mi) {
      var ix = months.indexOf(m);
      leadSeries.push({ label: monthLabel(m) + " MCQ", color: css(SERIES[(mi * 2) % SERIES.length]), values: names.map(function (n) { return agg[n].cells[ix].m; }) });
      leadSeries.push({ label: monthLabel(m) + " Coding", color: css(SERIES[(mi * 2 + 1) % SERIES.length]), values: names.map(function (n) { return agg[n].cells[ix].c; }) });
    });
    columns($("c-lead"), {
      categories: names.map(function (n) { return n.split(" ")[0]; }), height: 330,
      stacked: true,
      series: leadSeries,
      aria: "Content Lead output per month split by MCQ and coding",
      caption: "Each lead is split simultaneously by month and question format. Up to the latest four selected months are charted."
    });
    var detailRows = [];
    names.forEach(function (n) { months.forEach(function (m, i) {
      var x = agg[n].cells[i]; detailRows.push([n, monthLabel(m), fmt(x.m), fmt(x.c), fmt(x.t), pct(x.c, x.t) + "%"]);
    }); });
    table($("tb-lead"), ["Content Lead", "Month", "MCQ", "Coding", "Total", "Coding %"], detailRows);
  }

  function renderTrack() {
    var c = DATA.cols, dims = DATA.dims, monthIndex = {}, agg = {};
    months.forEach(function (m, i) { monthIndex[dims.months.indexOf(m)] = i; });
    rows.forEach(function (i) {
      var t = DATA.tracks[dims.subjects[c.su[i]]] || "Other / Unclassified";
      var k = monthIndex[c.cm[i]]; if (k === undefined) return;
      if (!agg[t]) agg[t] = { n: 0, cells: months.map(function () { return { n: 0, m: 0, c: 0, leads: {} }; }) };
      var cell = agg[t].cells[k], author = dims.authors[c.au[i]];
      agg[t].n++; cell.n++; if (c.ty[i] === 1) cell.c++; else cell.m++;
      if (roleOf(c.au[i]) === "lead") cell.leads[author] = (cell.leads[author] || 0) + 1;
    });
    var keys = Object.keys(agg).sort(function (a, b) { return agg[b].n - agg[a].n; });
    heatmap($("c-track"), {
      columns: months.map(monthLabel),
      rows: keys.map(function (k) { return { label: k, values: agg[k].cells.map(function (x) { return x.n; }), detail: agg[k].cells.map(function (x) {
        var details = [{ label: "MCQ", value: x.m, color: css("--series-1") }, { label: "Coding", value: x.c, color: css("--series-2") }];
        Object.keys(x.leads).sort(function (a, b) { return x.leads[b] - x.leads[a]; }).forEach(function (lead) { details.push({ label: lead, value: x.leads[lead] }); });
        return details;
      }) }; }),
      aria: "Questions per track per month linked to Content Leads",
      caption: "Hover a month to see format and Content Lead ownership. Tracks are derived from the subject field."
    });
    var trackRows = [];
    keys.forEach(function (k) { months.forEach(function (m, i) {
      var x = agg[k].cells[i], mix = Object.keys(x.leads).sort(function (a, b) { return x.leads[b] - x.leads[a]; })
        .map(function (lead) { return lead.split(" ")[0] + " " + fmt(x.leads[lead]); }).join(" · ") || "–";
      trackRows.push([k, monthLabel(m), fmt(x.n), fmt(x.m), fmt(x.c), mix]);
    }); });
    var tableHost = $("tb-track"); if (tableHost) table(tableHost, ["Track", "Month", "Questions", "MCQ", "Coding", "Content Lead mix"], trackRows);
  }

  function renderCompany() {
    var c = DATA.cols, dims = DATA.dims, agg = {}, mockTotal = 0;
    rows.forEach(function (i) {
      if (c.mk[i]) mockTotal++;
      if (c.co[i] < 0) return;
      var name = dims.companies[c.co[i]];
      if (!agg[name]) agg[name] = { n: 0, m: 0, c: 0 };
      agg[name].n++; if (c.ty[i] === 1) agg[name].c++; else agg[name].m++;
    });
    var keys = Object.keys(agg).sort(function (a, b) { return agg[b].n - agg[a].n; }).slice(0, 12);
    var monthSet = {}; months.forEach(function (m) { monthSet[m] = 1; });
    var mockTests = DATA.tests.rows.filter(function (t) { return t.mock && monthSet[t.month]; });
    var host = $("c-company");
    host.innerHTML = '<div class="tiles" style="margin-bottom:14px">' +
      '<div class="tile"><div class="k">Company-linked questions</div><div class="v">' + fmt(mockTotal) + '</div><div class="d">' + pct(mockTotal, rows.length) + "% of additions</div></div>" +
      '<div class="tile"><div class="k">Mock tests built</div><div class="v">' + fmt(mockTests.length) + '</div><div class="d">In the selected period</div></div>' +
      '<div class="tile"><div class="k">Companies covered</div><div class="v">' + fmt(Object.keys(agg).length) + '</div><div class="d">With named questions</div></div></div>' +
      '<div id="c-company-bars"></div>';
    hbars($("c-company-bars"), {
      labelWidth: 132,
      items: keys.map(function (k) {
        return {
          label: k, value: agg[k].n, color: css("--series-2"),
          detail: [{ label: "MCQ", value: agg[k].m, color: css("--series-1") }, { label: "Coding", value: agg[k].c, color: css("--series-2") }]
        };
      }),
      aria: "Questions per hiring company",
      caption: keys.length ? "Top " + keys.length + " companies by tagged question volume." : ""
    });
  }

  function renderAkilaCompany() {
    var c = DATA.cols, dims = DATA.dims, monthIndex = {}, mcq = months.map(function () { return 0; }), coding = months.map(function () { return 0; }), companies = {};
    months.forEach(function (m, i) { monthIndex[dims.months.indexOf(m)] = i; });
    for (var i = 0; i < c.cm.length; i++) {
      if (dims.authors[c.au[i]] !== "Akila Rengarajan" || !c.mk[i]) continue;
      var k = monthIndex[c.cm[i]]; if (k === undefined) continue;
      var subject = dims.subjects[c.su[i]];
      if (VIEW.type !== "" && c.ty[i] !== +VIEW.type) continue;
      if (VIEW.subjects.size && !VIEW.subjects.has(subject)) continue;
      if (VIEW.tracks.size && !VIEW.tracks.has(DATA.tracks[subject])) continue;
      if (c.ty[i] === 1) coding[k]++; else mcq[k]++;
      if (c.co[i] >= 0) companies[dims.companies[c.co[i]]] = 1;
    }
    var total = mcq.reduce(add, 0) + coding.reduce(add, 0), host = $("c-akila-company");
    host.innerHTML = '<div class="tiles" style="margin-bottom:14px"><div class="tile"><div class="k">Company-specific by Akila</div><div class="v">' + fmt(total) + '</div><div class="d">Fixed-author metric for the selected period</div></div>' +
      '<div class="tile"><div class="k">MCQ</div><div class="v">' + fmt(mcq.reduce(add, 0)) + '</div><div class="d">' + pct(mcq.reduce(add, 0), total) + '% of her company output</div></div>' +
      '<div class="tile"><div class="k">Coding</div><div class="v">' + fmt(coding.reduce(add, 0)) + '</div><div class="d">' + pct(coding.reduce(add, 0), total) + '% of her company output</div></div>' +
      '<div class="tile"><div class="k">Named companies</div><div class="v">' + fmt(Object.keys(companies).length) + '</div><div class="d">Company field populated</div></div></div><div id="c-akila-company-chart"></div>';
    columns($("c-akila-company-chart"), {
      categories: months.map(monthLabel), height: 280,
      series: [{ label: "MCQ", color: css("--series-1"), values: mcq }, { label: "Coding", color: css("--series-2"), values: coding }],
      aria: "Akila Rengarajan company-specific questions by month and type",
      caption: "This special category intentionally stays fixed to Akila even when the global Author filter changes. Other filters still apply."
    });
  }

  function renderMatrix() {
    var subject = $("f-matrix").value;
    var c = DATA.cols, dims = DATA.dims, agg = {};
    // The matrix reads the whole bank for the chosen subject, not just the period —
    // difficulty balance is a property of the bank as it stands today.
    for (var i = 0; i < c.su.length; i++) {
      if (dims.subjects[c.su[i]] !== subject) continue;
      if (c.st[i] === 1) continue; // archived questions are not part of the live matrix
      if (c.ty[i] !== matrixType) continue;
      var t = dims.topics[c.tp[i]];
      if (!agg[t]) agg[t] = [0, 0, 0, 0];
      agg[t][c.df[i]]++;
    }
    var keys = Object.keys(agg).sort(function (a, b) {
      return agg[b].reduce(add, 0) - agg[a].reduce(add, 0);
    }).slice(0, 22);
    pctBars($("c-matrix"), {
      series: DIFF_LABEL.map(function (l, i) { return { label: l, color: css(ORD[i]) }; }),
      items: keys.map(function (k) { return { label: k, values: agg[k] }; }),
      aria: TYPE_LABEL[matrixType] + " difficulty mix per topic for " + subject,
      caption: "Live " + TYPE_LABEL[matrixType] + " questions in " + subject + ". Row totals are on the right; hover for exact counts and shares."
    });
  }

  function renderStandard() {
    var monthSet = {}; months.forEach(function (m) { monthSet[m] = 1; });
    var all = DATA.tests.rows.filter(function (t) { return t.standardized; });
    var bySubject = {};
    all.forEach(function (t) {
      if (!bySubject[t.subject]) bySubject[t.subject] = { n: 0, q: 0, empty: 0, months: {} };
      var b = bySubject[t.subject];
      b.n++; b.q += t.questions; if (!t.questions) b.empty++; b.months[t.month] = 1;
    });
    var keys = Object.keys(bySubject).sort(function (a, b) { return bySubject[b].n - bySubject[a].n; });
    var host = $("c-standard");
    var inWindow = all.filter(function (t) { return monthSet[t.month]; }).length;
    host.innerHTML = '<div class="tiles" style="margin-bottom:14px">' +
      '<div class="tile"><div class="k">Subjects with a standardized assessment</div><div class="v">' + fmt(keys.length) + '</div><div class="d">All-time coverage</div></div>' +
      '<div class="tile"><div class="k">Assessment papers</div><div class="v">' + fmt(all.length) + '</div><div class="d">' + fmt(inWindow) + " created in the selected period</div></div>" +
      '<div class="tile"><div class="k">Papers with no questions</div><div class="v">' + fmt(all.filter(function (t) { return !t.questions; }).length) +
      '</div><div class="d">Shells that cannot be assigned</div></div></div><div id="c-standard-bars"></div><div id="tb-standard" style="margin-top:14px"></div>';
    hbars($("c-standard-bars"), {
      labelWidth: 224, valueLabel: "Papers", labelWidthNote: 1,
      items: keys.map(function (k) {
        return {
          label: k, value: bySubject[k].n, color: css("--series-3"),
          detail: [{ label: "Total questions", value: bySubject[k].q },
          { label: "Empty papers", value: bySubject[k].empty }]
        };
      }),
      aria: "Standardized assessment papers per subject",
      caption: "Counts every test flagged as a standardized assessment, whether by test intent or tag."
    });
    table($("tb-standard"), ["Subject", "Papers", "Questions", "Empty papers", "First built", "Latest"],
      keys.map(function (k) {
        var ms = Object.keys(bySubject[k].months).filter(Boolean).sort();
        return [k, fmt(bySubject[k].n), fmt(bySubject[k].q), fmt(bySubject[k].empty),
          monthLabel(ms[0]), monthLabel(ms[ms.length - 1])];
      }));
  }

  function renderQuality() {
    var c = DATA.cols, dims = DATA.dims;
    var noSubject = 0, noDiff = 0, noExpl = 0, noTopic = 0;
    rows.forEach(function (i) {
      if (dims.subjects[c.su[i]] === "(no subject)") noSubject++;
      if (c.df[i] === 3) noDiff++;
      if (!c.ex[i]) noExpl++;
      if (dims.topics[c.tp[i]] === "(no topic)") noTopic++;
    });
    var n = rows.length || 1;
    var items = [
      { label: "No subject assigned", v: noSubject, why: "Invisible to subject filters and the Test Builder." },
      { label: "No topic assigned", v: noTopic, why: "Cannot be placed in a difficulty matrix or blueprint." },
      { label: "No difficulty set", v: noDiff, why: "Breaks difficulty-balanced paper generation." },
      { label: "No explanation", v: noExpl, why: "Weak review value for students after an attempt." }
    ];
    var host = $("c-quality");
    host.innerHTML = '<div class="tiles" style="margin-bottom:6px">' + items.map(function (x) {
      var p = pct(x.v, n);
      return '<div class="tile"><div class="k">' + esc(x.label) + '</div><div class="v">' + p + '%</div><div class="d ' +
        (p > 25 ? "down" : "") + '">' + fmt(x.v) + " of " + fmt(n) + " · " + esc(x.why) + "</div></div>";
    }).join("") + "</div>";
    if (noSubject / n > 0.2) {
      var w = document.createElement("div");
      w.className = "warn";
      w.textContent = "A third of the questions in view carry no subject. Until they are tagged, subject, track and difficulty-matrix panels understate real coverage — the questions exist but cannot be found or reused.";
      host.appendChild(w);
    }
  }

  function renderRoster() {
    var c = DATA.cols, dims = DATA.dims, counts = {};
    rows.forEach(function (i) { var n = dims.authors[c.au[i]]; counts[n] = (counts[n] || 0) + 1; });
    var names = dims.authors.slice().sort(function (a, b) { return (counts[b] || 0) - (counts[a] || 0); })
      .filter(function (n) { return counts[n] || ROLES[n] === "lead"; });
    $("c-roster").innerHTML = names.map(function (n) {
      var r = ROLES[n] || "support";
      return '<div class="rrow"><span class="pill ' + r + '">' + r[0].toUpperCase() + '</span><span class="nm" title="' + esc(n) + '">' + esc(n) +
        '</span><span class="ct">' + fmt(counts[n] || 0) + "</span>" +
        '<select data-author="' + esc(n) + '">' +
        ["lead", "support", "manager", "system"].map(function (o) {
          return '<option value="' + o + '"' + (o === r ? " selected" : "") + ">" +
            { lead: "Content Lead", support: "Support Eng", manager: "Manager", system: "System" }[o] + "</option>";
        }).join("") + "</select></div>";
    }).join("");
    Array.prototype.forEach.call($("c-roster").querySelectorAll("select"), function (s) {
      s.addEventListener("change", function () {
        ROLES[s.dataset.author] = s.value;
        localStorage.setItem(ROSTER_KEY, JSON.stringify(ROLES));
        renderAll();
      });
    });
  }

  /* --------------------------------------------------------------- wiring */
  function renderAll() {
    months = activeMonths();
    rows = computeRows();
    renderExecutiveBrief(); renderTiles(); renderResilience(); renderMonthly(); renderCurated(); renderChurn(); renderWeekly();
    renderSubject(); renderLead(); renderTrack(); renderCompany(); renderAkilaCompany();
    renderMatrix(); renderStandard(); renderQuality(); renderRoster();
    animateMetrics($("app"));
  }

  /* ------------------------------------------------ dashboard navigation / finder */
  function setDashboard(view, target, fromSearch) {
    if (!DASHBOARDS[view]) return;
    activeDashboard = view;
    Array.prototype.forEach.call(document.querySelectorAll(".dashboard-view"), function (section) {
      section.classList.toggle("active", section.dataset.dashboard === view);
    });
    Array.prototype.forEach.call(document.querySelectorAll(".dash-nav-btn"), function (button) {
      button.classList.toggle("active", button.dataset.view === view);
      button.setAttribute("aria-current", button.dataset.view === view ? "page" : "false");
    });
    $("view-title").textContent = DASHBOARDS[view].title;
    $("view-description").textContent = DASHBOARDS[view].description;
    if (DATA) renderAll();
    if (fromSearch) {
      var search = $("analytics-search"), results = $("finder-results");
      search.value = ""; results.classList.remove("open"); results.innerHTML = "";
    }
    requestAnimationFrame(function () {
      var node = target && $(target);
      if (node) {
        node.classList.remove("metric-flash");
        void node.offsetWidth;
        node.classList.add("metric-flash");
        node.scrollIntoView({ behavior: motionOK ? "smooth" : "auto", block: "center" });
      } else if (window.innerWidth < 761) {
        window.scrollTo({ top: 0, behavior: motionOK ? "smooth" : "auto" });
      }
    });
  }

  function finderMatches(query) {
    var q = query.trim().toLowerCase();
    if (!q) return ANALYTICS_INDEX.slice(0, 6);
    var stop = { the: 1, and: 1, are: 1, for: 1, who: 1, what: 1, where: 1, which: 1, most: 1, show: 1, find: 1, need: 1 };
    var words = q.split(/\s+/).filter(function (word) { return word.length > 2 && !stop[word]; });
    return ANALYTICS_INDEX.map(function (item) {
      var title = item.title.toLowerCase(), haystack = title + " " + item.tags;
      var score = title.indexOf(q) >= 0 ? 12 : 0;
      words.forEach(function (word) {
        if (title.indexOf(word) >= 0) score += 4;
        else if (haystack.indexOf(word) >= 0) score += 2;
      });
      return { item: item, score: score };
    }).filter(function (result) { return result.score > 0; })
      .sort(function (a, b) { return b.score - a.score; })
      .slice(0, 6).map(function (result) { return result.item; });
  }

  function renderFinder(query) {
    var results = $("finder-results"), matches = finderMatches(query);
    results.innerHTML = matches.length ? matches.map(function (item, i) {
      return '<button class="finder-result' + (i === 0 ? " focused" : "") + '" role="option" data-view="' + item.view + '" data-target="' + item.target + '">' +
        '<strong>' + esc(item.title) + '</strong><span>' + esc(DASHBOARDS[item.view].title) + '</span></button>';
    }).join("") : '<div class="finder-empty">No exact match. Try “authors”, “quality”, “difficulty”, or “company”.</div>';
    results.classList.add("open");
    Array.prototype.forEach.call(results.querySelectorAll(".finder-result"), function (button) {
      button.addEventListener("click", function () { setDashboard(button.dataset.view, button.dataset.target, true); });
    });
  }

  function bindWorkspaceNavigation() {
    Array.prototype.forEach.call(document.querySelectorAll(".dash-nav-btn"), function (button) {
      button.addEventListener("click", function () { setDashboard(button.dataset.view); });
    });
    var search = $("analytics-search"), results = $("finder-results");
    search.addEventListener("focus", function () { renderFinder(search.value); });
    search.addEventListener("input", function () { renderFinder(search.value); });
    search.addEventListener("keydown", function (event) {
      if (event.key === "Enter") {
        var first = results.querySelector(".finder-result");
        if (first) { event.preventDefault(); setDashboard(first.dataset.view, first.dataset.target, true); }
      } else if (event.key === "Escape") {
        results.classList.remove("open"); search.blur();
      }
    });
    document.addEventListener("keydown", function (event) {
      if ((event.metaKey || event.ctrlKey) && event.key.toLowerCase() === "k") {
        event.preventDefault(); search.focus(); search.select();
      }
    });
    document.addEventListener("click", function (event) {
      if (!event.target.closest(".analytics-finder")) results.classList.remove("open");
    });
    Array.prototype.forEach.call(document.querySelectorAll(".quick-prompt"), function (button) {
      button.addEventListener("click", function () {
        search.value = button.dataset.query; renderFinder(search.value); search.focus();
      });
    });
  }

  /* --------------------------------------------------------- multi-select filter */
  var ALL_MULTISELECTS = [];
  function closeAllMultiSelects() {
    ALL_MULTISELECTS.forEach(function (m) { m.panel.classList.remove("open"); m.btn.classList.remove("open"); });
  }
  document.addEventListener("click", closeAllMultiSelects);
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") closeAllMultiSelects(); });

  /**
   * A checkbox dropdown bound to a Set in VIEW[opts.key]. Empty set = no filter,
   * matching the convention used everywhere the fact table is queried.
   *
   * The search box and the checkbox list are separate persistent DOM nodes —
   * typing only re-renders `.msel-list`, never the input itself, so a keystroke
   * never steals its own focus.
   */
  function mountMultiSelect(hostId, opts) {
    var host = $(hostId);
    host.className = "msel";
    host.innerHTML = "";
    var btn = document.createElement("button");
    btn.type = "button"; btn.className = "msel-btn";
    var panel = document.createElement("div"); panel.className = "msel-panel";

    var searchEl = null;
    if (opts.searchable) {
      searchEl = document.createElement("input");
      searchEl.type = "text"; searchEl.className = "msel-search"; searchEl.placeholder = "Search…";
      panel.appendChild(searchEl);
    }
    if (opts.presets && opts.presets.length) {
      var presetsEl = document.createElement("div"); presetsEl.className = "msel-presets";
      opts.presets.forEach(function (p) {
        var chip = document.createElement("button");
        chip.type = "button"; chip.className = "msel-chip"; chip.textContent = p.label;
        chip.addEventListener("click", function () {
          p.apply(VIEW[opts.key], optionsList());
          renderList(); updateButton(); renderAll();
        });
        presetsEl.appendChild(chip);
      });
      panel.appendChild(presetsEl);
    }
    var listEl = document.createElement("div"); listEl.className = "msel-list";
    panel.appendChild(listEl);
    var footer = document.createElement("div"); footer.className = "msel-footer";
    var allBtn = document.createElement("button"); allBtn.type = "button"; allBtn.className = "msel-link"; allBtn.textContent = "Select all";
    var noneBtn = document.createElement("button"); noneBtn.type = "button"; noneBtn.className = "msel-link"; noneBtn.textContent = "Clear";
    footer.appendChild(allBtn); footer.appendChild(noneBtn);
    panel.appendChild(footer);
    host.appendChild(btn); host.appendChild(panel);

    function optionsList() { return opts.getOptions(); }
    function visibleOptions() {
      var q = searchEl ? searchEl.value.trim().toLowerCase() : "";
      var all = optionsList();
      return q ? all.filter(function (o) { return o.label.toLowerCase().indexOf(q) >= 0; }) : all;
    }
    function updateButton() {
      var set = VIEW[opts.key];
      if (!set.size) { btn.textContent = opts.allLabel; return; }
      var all = optionsList();
      var names = all.filter(function (o) { return set.has(o.value); }).map(function (o) { return o.label; });
      btn.textContent = (names.length && names.length === set.size && set.size <= 2) ? names.join(", ") : set.size + " selected";
    }
    function renderList() {
      var vis = visibleOptions();
      listEl.innerHTML = vis.length ? vis.map(function (o) {
        var checked = VIEW[opts.key].has(o.value);
        return '<label class="msel-row"><input type="checkbox" data-v="' + esc(o.value) + '"' + (checked ? " checked" : "") +
          '><span class="lb">' + esc(o.label) + '</span>' + (o.count != null ? '<span class="ct">' + fmt(o.count) + "</span>" : "") + "</label>";
      }).join("") : '<div class="msel-empty">No matches</div>';
      Array.prototype.forEach.call(listEl.querySelectorAll("input[type=checkbox]"), function (cb) {
        cb.addEventListener("change", function () {
          if (cb.checked) VIEW[opts.key].add(cb.dataset.v); else VIEW[opts.key].delete(cb.dataset.v);
          updateButton(); renderAll();
        });
      });
    }
    if (searchEl) searchEl.addEventListener("input", renderList);
    allBtn.addEventListener("click", function () {
      visibleOptions().forEach(function (o) { VIEW[opts.key].add(o.value); });
      renderList(); updateButton(); renderAll();
    });
    noneBtn.addEventListener("click", function () {
      // Under an active search, "Clear" only drops what's visible so a filtered
      // search can't silently wipe out selections the user can't currently see.
      var vis = visibleOptions();
      if (searchEl && searchEl.value.trim()) vis.forEach(function (o) { VIEW[opts.key].delete(o.value); });
      else VIEW[opts.key].clear();
      renderList(); updateButton(); renderAll();
    });
    btn.addEventListener("click", function (e) {
      e.stopPropagation();
      var willOpen = !panel.classList.contains("open");
      closeAllMultiSelects();
      if (willOpen) {
        renderList();
        panel.classList.add("open"); btn.classList.add("open");
        if (searchEl) { searchEl.value = ""; searchEl.focus(); }
      }
    });
    panel.addEventListener("click", function (e) { e.stopPropagation(); });

    updateButton();
    var handle = { panel: panel, btn: btn, refresh: function () { updateButton(); if (panel.classList.contains("open")) renderList(); } };
    ALL_MULTISELECTS.push(handle);
    return handle;
  }

  function monthOptions() {
    var counts = {};
    for (var i = 0; i < DATA.cols.cm.length; i++) { var m = DATA.dims.months[DATA.cols.cm[i]]; if (m) counts[m] = (counts[m] || 0) + 1; }
    return Object.keys(counts).sort().map(function (m) { return { value: m, label: monthLabel(m), count: counts[m] }; });
  }
  function trackOptions() {
    var counts = {};
    for (var i = 0; i < DATA.cols.su.length; i++) { var t = DATA.tracks[DATA.dims.subjects[DATA.cols.su[i]]]; counts[t] = (counts[t] || 0) + 1; }
    return Object.keys(counts).sort(function (a, b) { return counts[b] - counts[a]; }).map(function (t) { return { value: t, label: t, count: counts[t] }; });
  }
  function subjectOptions() {
    var counts = {};
    for (var i = 0; i < DATA.cols.su.length; i++) { var s = DATA.dims.subjects[DATA.cols.su[i]]; counts[s] = (counts[s] || 0) + 1; }
    return Object.keys(counts).sort(function (a, b) { return counts[b] - counts[a]; }).map(function (s) { return { value: s, label: s, count: counts[s] }; });
  }
  function authorOptions() {
    var counts = {};
    for (var i = 0; i < DATA.cols.au.length; i++) { var a = DATA.dims.authors[DATA.cols.au[i]]; counts[a] = (counts[a] || 0) + 1; }
    return Object.keys(counts).sort(function (a, b) { return counts[b] - counts[a]; }).map(function (a) { return { value: a, label: a, count: counts[a] }; });
  }

  var monthsMsel, tracksMsel, subjectsMsel, authorsMsel;
  function mountFilters() {
    monthsMsel = mountMultiSelect("f-months", {
      key: "months", allLabel: "All time", getOptions: monthOptions,
      presets: [
        { label: "Latest 3", apply: function (set, opts) { set.clear(); opts.slice(-3).forEach(function (o) { set.add(o.value); }); } },
        { label: "Last 6", apply: function (set, opts) { set.clear(); opts.slice(-6).forEach(function (o) { set.add(o.value); }); } },
        { label: "Last 12", apply: function (set, opts) { set.clear(); opts.slice(-12).forEach(function (o) { set.add(o.value); }); } },
        { label: "All time", apply: function (set) { set.clear(); } }
      ]
    });
    tracksMsel = mountMultiSelect("f-track", { key: "tracks", allLabel: "All tracks", getOptions: trackOptions });
    subjectsMsel = mountMultiSelect("f-subject", { key: "subjects", allLabel: "All subjects", searchable: true, getOptions: subjectOptions });
    authorsMsel = mountMultiSelect("f-author", { key: "authors", allLabel: "All authors", searchable: true, getOptions: authorOptions });
  }
  function refreshFilters() {
    [monthsMsel, tracksMsel, subjectsMsel, authorsMsel].forEach(function (m) { m.refresh(); });
  }

  function refreshMatrixSelect() {
    var dims = DATA.dims, counts = {};
    for (var j = 0; j < DATA.cols.su.length; j++) counts[dims.subjects[DATA.cols.su[j]]] = (counts[dims.subjects[DATA.cols.su[j]]] || 0) + 1;
    // The difficulty matrix defaults to the subjects the brief named.
    var preferred = ["c-programming", "python", "algorithm-design", "java", "rdbms"];
    var matrixSubjects = dims.subjects.slice().filter(function (s) { return counts[s] >= 40 && s !== "(no subject)"; })
      .sort(function (a, b) { return counts[b] - counts[a]; });
    var sel = $("f-matrix");
    var prevValue = sel.value;
    sel.innerHTML = matrixSubjects.map(function (s) { return '<option value="' + esc(s) + '">' + esc(s) + " (" + fmt(counts[s]) + ")</option>"; }).join("");
    if (matrixSubjects.indexOf(prevValue) >= 0) { sel.value = prevValue; return; }
    var first = preferred.find(function (p) { return matrixSubjects.indexOf(p) >= 0; });
    if (first) sel.value = first;
  }

  function bindControls() {
    bindWorkspaceNavigation();
    $("f-matrix").addEventListener("change", renderMatrix);
    Array.prototype.forEach.call($("f-matrix-type").children, function (b) {
      b.addEventListener("click", function () {
        Array.prototype.forEach.call($("f-matrix-type").children, function (o) { o.classList.remove("on"); });
        b.classList.add("on"); matrixType = +b.dataset.v; renderMatrix();
      });
    });
    Array.prototype.forEach.call($("f-type").children, function (b) {
      b.addEventListener("click", function () {
        Array.prototype.forEach.call($("f-type").children, function (o) { o.classList.remove("on"); });
        b.classList.add("on"); VIEW.type = b.dataset.v; renderAll();
      });
    });
    [["t-monthly", "c-monthly", "tb-monthly"], ["t-weekly", "c-weekly", "tb-weekly"], ["t-subject", "c-subject", "tb-subject"], ["t-lead", "c-lead", "tb-lead"]]
      .forEach(function (p) {
        $(p[0]).addEventListener("change", function () {
          $(p[1]).classList.toggle("hidden", $(p[0]).checked);
          $(p[2]).classList.toggle("hidden", !$(p[0]).checked);
        });
      });
    $("btn-reset").addEventListener("click", function () {
      VIEW.months.clear(); monthOptions().slice(-3).forEach(function (o) { VIEW.months.add(o.value); });
      VIEW.tracks.clear(); VIEW.subjects.clear(); VIEW.authors.clear(); VIEW.type = "";
      Array.prototype.forEach.call($("f-type").children, function (o, i) { o.classList.toggle("on", i === 0); });
      refreshFilters();
      renderAll();
    });
    $("btn-refresh").addEventListener("click", function () { load(true, false); });
    $("btn-roster-reset").addEventListener("click", function () {
      localStorage.removeItem(ROSTER_KEY);
      ROLES = Object.assign({}, DATA.roles);
      renderAll();
    });
  }

  /* ----------------------------------------------------------- freshness / polling */
  function startFreshnessTicker() {
    setInterval(function () {
      if (!lastGeneratedAtMs) return;
      var el = $("meta-fresh");
      if (!el) return;
      var secs = Math.max(0, Math.round((Date.now() - lastGeneratedAtMs) / 1000));
      el.textContent = "Updated " + (secs < 60 ? secs + "s ago" : Math.round(secs / 60) + " min ago");
    }, 1000);
  }
  function startPolling() {
    // ByteXL has no change webhook, so "live" means the server keeps a warm
    // snapshot refreshed on its own schedule and the browser checks in
    // periodically for a newer one — not a push, but close for a dashboard
    // someone leaves open during the day.
    setInterval(function () {
      var force = Date.now() - lastForcedRefreshMs >= FORCE_REFRESH_MS;
      if (force) lastForcedRefreshMs = Date.now();
      load(force, true);
    }, POLL_MS);
  }

  function load(force, silent) {
    if (loadInFlight) return;
    loadInFlight = true;
    var btn = $("btn-refresh");
    if (!silent) {
      if (btn) { btn.disabled = true; btn.textContent = "Refreshing…"; }
      if (force) { $("app").classList.add("hidden"); $("loader").classList.remove("hidden"); }
      $("error").classList.add("hidden");
    }

    // Resolved here rather than at load time so a misconfigured host surfaces in
    // the error panel instead of leaving the spinner running forever.
    var API;
    try {
      API = apiBase();
    } catch (e) {
      if (!silent) {
        $("loader").classList.add("hidden");
        $("error").classList.remove("hidden");
        $("error").textContent = e.message;
        if (btn) { btn.disabled = false; btn.textContent = "Refresh data"; }
      }
      loadInFlight = false;
      return;
    }

    fetch(API + "/analytics/snapshot" + (force ? "?refresh=true" : ""))
      .then(function (r) {
        if (!r.ok) return r.text().then(function (t) { throw new Error("HTTP " + r.status + " — " + t.slice(0, 300)); });
        return r.json();
      })
      .then(function (d) {
        var changed = !DATA || DATA.generatedAt !== d.generatedAt;
        DATA = d;
        if (initialMonthScope) {
          VIEW.months.clear(); monthOptions().slice(-3).forEach(function (o) { VIEW.months.add(o.value); });
          initialMonthScope = false;
        }
        var saved = null;
        try { saved = JSON.parse(localStorage.getItem(ROSTER_KEY) || "null"); } catch (e) { saved = null; }
        ROLES = Object.assign({}, d.roles, saved || {});
        lastGeneratedAtMs = d.generatedAt ? Date.parse(d.generatedAt) : Date.now();
        if (force) lastForcedRefreshMs = Date.now();
        var restEl = $("meta-rest");
        if (restEl) {
          restEl.textContent = " · " + fmt(d.counts.live) + " live and " + fmt(d.counts.archived) + " archived questions · " +
            fmt(d.tests.rows.length) + " tests · checks every " + Math.round(POLL_MS / 60000) + " min and syncs ByteXL every " + Math.round(FORCE_REFRESH_MS / 60000) + " min" +
            (d.refreshing ? " · a background refresh is in progress" : "");
        }
        if (!bound) {
          mountFilters(); refreshMatrixSelect(); bindControls(); bound = true;
          startFreshnessTicker(); startPolling();
        } else if (changed) {
          refreshFilters(); refreshMatrixSelect();
        }
        $("loader").classList.add("hidden");
        $("app").classList.remove("hidden");
        if (!silent || changed) renderAll();
      })
      .catch(function (e) {
        if (silent) { window.console && console.warn && console.warn("Analytics poll failed:", e.message); return; }
        $("loader").classList.add("hidden");
        $("error").classList.remove("hidden");
        $("error").textContent = "Could not load the question bank: " + e.message;
      })
      .finally(function () {
        loadInFlight = false;
        if (!silent && btn) { btn.disabled = false; btn.textContent = "Refresh data"; }
      });
  }

  load(false, false);
})();
