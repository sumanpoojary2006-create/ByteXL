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
  // Blue ramp, dark (near the surface = near zero) to light as magnitude rises.
  // Inverted from the light-surface convention because this dashboard is dark.
  var HEAT = ["#0d366b", "#184f95", "#1c5cab", "#256abf", "#2a78d6", "#3987e5", "#5598e7", "#6da7ec", "#86b6ef", "#9ec5f4", "#b7d3f6", "#cde2fb"];
  var TYPE_LABEL = ["MCQ", "Coding", "Descriptive"];
  var DIFF_LABEL = ["Easy", "Medium", "Hard", "Unspecified"];
  var ROSTER_KEY = "bytexl.analytics.roster.v1";

  var DATA = null;      // raw snapshot
  var ROLES = {};       // author name -> lead | support | manager | system
  // months/tracks/subjects/authors are checkbox multi-selects: an empty Set means
  // "no filter" (show everything), same convention across all four. type stays a
  // single-select segmented control.
  var VIEW = { months: new Set(["2026-06", "2026-07", "2026-08"]), tracks: new Set(), subjects: new Set(), authors: new Set(), type: "" };
  var rows = [];        // filtered row indices
  var months = [];      // month keys in the active window
  var bound = false;    // controls are bound once, not on every snapshot load
  var lastGeneratedAtMs = null; // for the ticking "Updated Xs ago" label
  var POLL_MS = 60000;  // how often the browser checks for a newer snapshot
  var FORCE_REFRESH_MS = 5 * 60000; // how often an open dashboard rebuilds from ByteXL
  var lastForcedRefreshMs = 0;
  var loadInFlight = false;

  function css(name) { return getComputedStyle(document.body).getPropertyValue(name).trim(); }
  function $(id) { return document.getElementById(id); }
  function fmt(n) { return (n === null || n === undefined) ? "–" : n.toLocaleString("en-IN"); }
  function pct(a, b) { return b ? Math.round((a / b) * 1000) / 10 : 0; }
  function monthLabel(key) {
    if (!key) return "";
    var p = key.split("-");
    return ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"][+p[1] - 1] + " " + p[0].slice(2);
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
          var seg = el("path", { d: barPath(cx - inner / 2, yy, inner, Math.max(h - 2, 0.6), true), fill: s.color });
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
            var b = el("path", { d: barPath(bx, y(v), bw, h, true), fill: s.color });
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
      var b = el("path", { d: barPath(m.l, yy + 6, Math.max(w, 1), rowH - 14, false), fill: it.color || css("--series-1") });
      bindTip(b, it.label, (it.detail || []).concat([{ label: opts.valueLabel || "Questions", value: it.value }]));
      svg.appendChild(b);
      var vl = el("text", { x: m.l + w + 9, y: yy + rowH / 2 + 4, class: "dlabel" });
      vl.textContent = fmt(it.value) + (opts.suffix || ""); svg.appendChild(vl);
    });
    host.appendChild(svg);
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
        var seg = el("path", { d: barPath(m.l + acc, yy + 6, Math.max(w - 2, 1), rowH - 14, false), fill: opts.series[si].color });
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
        var fill = idx < 0 ? "rgba(255,255,255,.035)" : HEAT[idx];
        var cell = el("rect", { x: m.l + j * cellW + 1, y: m.t + i * cellH + 1, width: cellW - 3, height: cellH - 3, rx: 4, fill: fill });
        bindTip(cell, r.label + " · " + cols[j], (r.detail && r.detail[j]) || [{ label: "Questions", value: v }]);
        svg.appendChild(cell);
        if (v > 0) {
          var lb = el("text", {
            x: m.l + j * cellW + cellW / 2, y: m.t + i * cellH + cellH / 2 + 4, "text-anchor": "middle",
            // Ink token, not the series colour; flipped for contrast on light cells.
            fill: idx >= 7 ? "#0b1020" : css("--ink"), "font-size": 10.5, "font-weight": 700
          });
          lb.textContent = fmt(v); svg.appendChild(lb);
        }
      });
    });
    host.appendChild(svg);
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
    columns($("c-curated"), {
      categories: months.map(monthLabel), stacked: true, height: 290,
      series: [
        { label: "Content Leads", color: css("--series-1"), values: lead },
        { label: "Platform Support", color: css("--series-2"), values: sup },
        { label: "Manager / system", color: css("--series-7"), values: other }
      ],
      aria: "Questions by author role per month",
      caption: "Curated share: " + months.map(function (m, i) {
        return monthLabel(m) + " " + pct(lead[i], lead[i] + sup[i] + other[i]) + "%";
      }).join(" · ")
    });
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
    // One column per month, capped at the palette's 8 slots.
    var shown = months.slice(-8);
    columns($("c-lead"), {
      categories: names.map(function (n) { return n.split(" ")[0]; }), height: 330,
      stacked: true,
      series: shown.map(function (m, i) {
        var mi = months.indexOf(m);
        return {
          label: monthLabel(m), color: css(SERIES[i % SERIES.length]),
          values: names.map(function (n) { return agg[n].cells[mi].t; })
        };
      }),
      aria: "Content Lead output per month",
      caption: "Stacked by month; hover a bar for the month-by-month split."
    });
    table($("tb-lead"), ["Content Lead"].concat(months.map(monthLabel)).concat(["Total", "MCQ", "Coding", "Coding %"]),
      names.map(function (n) {
        return [n].concat(agg[n].cells.map(function (x) { return fmt(x.t); }))
          .concat([fmt(agg[n].total), fmt(agg[n].mcq), fmt(agg[n].cod), pct(agg[n].cod, agg[n].total) + "%"]);
      }));
  }

  function renderTrack() {
    var c = DATA.cols, dims = DATA.dims, agg = {};
    rows.forEach(function (i) {
      var t = DATA.tracks[dims.subjects[c.su[i]]] || "Other / Unclassified";
      if (!agg[t]) agg[t] = { n: 0, m: 0, c: 0, subs: {} };
      agg[t].n++; if (c.ty[i] === 1) agg[t].c++; else agg[t].m++;
      agg[t].subs[dims.subjects[c.su[i]]] = 1;
    });
    var keys = Object.keys(agg).sort(function (a, b) { return agg[b].n - agg[a].n; });
    hbars($("c-track"), {
      labelWidth: 176,
      items: keys.map(function (k) {
        return {
          label: k, value: agg[k].n, color: css("--series-1"),
          detail: [{ label: "MCQ", value: agg[k].m, color: css("--series-1") },
          { label: "Coding", value: agg[k].c, color: css("--series-2") },
          { label: "Distinct subjects", value: Object.keys(agg[k].subs).length }]
        };
      }),
      aria: "Questions per track",
      caption: "Tracks are grouped from the subject field, which the platform does not model directly."
    });
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

  function renderMatrix() {
    var subject = $("f-matrix").value;
    var c = DATA.cols, dims = DATA.dims, agg = {};
    // The matrix reads the whole bank for the chosen subject, not just the period —
    // difficulty balance is a property of the bank as it stands today.
    for (var i = 0; i < c.su.length; i++) {
      if (dims.subjects[c.su[i]] !== subject) continue;
      if (c.st[i] === 1) continue; // archived questions are not part of the live matrix
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
      aria: "Difficulty mix per topic for " + subject,
      caption: "Live (non-archived) questions in " + subject + ". Row totals are on the right; hover for exact counts and shares."
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
    renderTiles(); renderMonthly(); renderCurated(); renderChurn();
    renderSubject(); renderLead(); renderTrack(); renderCompany();
    renderMatrix(); renderStandard(); renderQuality(); renderRoster();
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
        { label: "Jun–Aug 26", apply: function (set) { set.clear(); ["2026-06", "2026-07", "2026-08"].forEach(function (m) { set.add(m); }); } },
        { label: "Last 3", apply: function (set, opts) { set.clear(); opts.slice(-3).forEach(function (o) { set.add(o.value); }); } },
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
    $("f-matrix").addEventListener("change", renderMatrix);
    Array.prototype.forEach.call($("f-type").children, function (b) {
      b.addEventListener("click", function () {
        Array.prototype.forEach.call($("f-type").children, function (o) { o.classList.remove("on"); });
        b.classList.add("on"); VIEW.type = b.dataset.v; renderAll();
      });
    });
    [["t-monthly", "c-monthly", "tb-monthly"], ["t-subject", "c-subject", "tb-subject"], ["t-lead", "c-lead", "tb-lead"]]
      .forEach(function (p) {
        $(p[0]).addEventListener("change", function () {
          $(p[1]).classList.toggle("hidden", $(p[0]).checked);
          $(p[2]).classList.toggle("hidden", !$(p[0]).checked);
        });
      });
    $("btn-reset").addEventListener("click", function () {
      VIEW.months = new Set(["2026-06", "2026-07", "2026-08"]);
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
