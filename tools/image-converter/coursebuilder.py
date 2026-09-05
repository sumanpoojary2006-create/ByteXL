"""Tactical course assembly from reading material that already exists on ByteXL.

A tactical course is a university-specific product (NHCE, Parul, St Mary's) whose
syllabus is fixed by the college but whose lessons should not be written again --
the strategic courses already carry them. This module turns a *blueprint* (the
syllabus expressed as Units -> Chapters -> Topics, with each topic pinned to a
donor page) into a plan that can be reviewed and then written to ByteXL.

The blueprint is the reviewable artefact and lives in ``blueprints/*.json``. Its
pins are page ids, so this module's real job is to keep telling the truth about
them: a donor page that was renamed, deleted or gutted since the blueprint was
authored has to surface as a blocked row rather than as a topic that quietly
ships empty. That failure has happened before on the upload path, so nothing
here trusts a pin without reading the page back.

ByteXL content is two levels deep -- ``contentSections`` holding
``contentPages`` -- so the three-level syllabus is flattened the same way the
FastAPI product does it: the section title carries "unit.chapter", the pages are
the topics.
"""

from __future__ import annotations

import json
import re
import time
from pathlib import Path
from typing import Any, Callable, Iterable, Optional

BLUEPRINT_DIR = Path(__file__).parent / "blueprints"
PAGE_CACHE_PATH = Path(__file__).parent / ".course-builder-cache.json"

# Donor pages below this are too thin to carry a syllabus topic on their own.
# The catalogue's own floor is ~590 words for a strategic lesson; the educator
# dumps that fail this check sit around 200-400.
THIN_WORD_COUNT = 450

# Page bodies change rarely and 90 reads take about a minute, so the cache is
# generous. The Refresh button on the page bypasses it.
PAGE_CACHE_TTL_SECONDS = 6 * 60 * 60

STATUS_REUSE = "reuse"
STATUS_MOVED = "moved"
STATUS_THIN = "thin"
STATUS_MISSING = "missing"
STATUS_AUTHOR = "author"

BLOCKING_STATUSES = {STATUS_MISSING}


def slugify(text: str) -> str:
    """Match ByteXL's own slug rule for reading-material URLs.

    Reverse-engineered by regenerating all 241 lesson links of two live courses
    and diffing against what the platform stores. The rule is narrower than the
    usual slugify:

    * every run of characters outside ``[a-z0-9_]`` becomes one hyphen, so
      apostrophes fold (``Python's`` -> ``python-s``) but **underscores survive**
      (``Python Variable_ Namespace`` -> ``python-variable_-namespace``, and
      ``the __init__ Constructor`` keeps its dunder);
    * only the *trailing* hyphen is stripped, so ``type()`` ends at ``type``
      while a title with a leading space keeps its leading hyphen
      (`` Branching and Merging`` -> ``-branching-and-merging``).

    Stripping both ends, or treating ``_`` as a separator, produces URLs that
    look right and resolve to nothing.
    """
    text = str(text or "").lower()
    text = re.sub(r"[^a-z0-9_]+", "-", text)
    return text.rstrip("-")


def reading_material_url(reading_id: str, reading_title: str, page_id: str,
                          section_title: str, page_title: str) -> str:
    return (
        f"https://app.bytexl.ai/reading/{reading_id}/{slugify(reading_title)}/"
        f"{page_id}/{slugify(section_title)}/{slugify(page_title)}"
    )


def normalize_title(text: str) -> str:
    """Fold a topic title to the form used for donor-page lookups."""
    text = str(text or "").lower()
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = text.replace("&", " and ")
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def section_title(unit: dict[str, Any], chapter: dict[str, Any]) -> str:
    """Flatten a unit and chapter into the one section title ByteXL can hold."""
    return f"{chapter.get('number') or unit.get('number')} - {chapter.get('title')}"


# --------------------------------------------------------------------------- #
# Blueprints
# --------------------------------------------------------------------------- #

def list_blueprints() -> list[dict[str, Any]]:
    """Summarise every blueprint on disk, cheapest-first for the picker."""
    summaries = []
    for path in sorted(BLUEPRINT_DIR.glob("*.json")):
        try:
            blueprint = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        units = blueprint.get("units") or []
        chapters = [chapter for unit in units for chapter in unit.get("chapters") or []]
        topics = [topic for chapter in chapters for topic in chapter.get("topics") or []]
        summaries.append(
            {
                "slug": blueprint.get("slug") or path.stem,
                "title": blueprint.get("title") or path.stem,
                "description": blueprint.get("description") or "",
                "courseCode": (blueprint.get("syllabus") or {}).get("courseCode") or "",
                "units": len(units),
                "chapters": len(chapters),
                "topics": len(topics),
                "authorNew": sum(1 for topic in topics if topic.get("authorNew")),
            }
        )
    return summaries


def load_blueprint(slug: str) -> dict[str, Any]:
    """Read one blueprint by slug, refusing anything that escapes the folder."""
    safe = re.sub(r"[^a-z0-9-]", "", str(slug or "").lower())
    if not safe:
        raise FileNotFoundError("A blueprint slug is required")
    path = BLUEPRINT_DIR / f"{safe}.json"
    if not path.is_file():
        raise FileNotFoundError(f"No blueprint named {safe}")
    return json.loads(path.read_text(encoding="utf-8"))


# --------------------------------------------------------------------------- #
# Donor catalogue
# --------------------------------------------------------------------------- #

def index_donor_pages(trees: dict[str, dict[str, Any]]) -> dict[str, dict[str, Any]]:
    """Build the by-id and by-title lookups a plan needs for one donor product."""
    index: dict[str, dict[str, Any]] = {}
    for product_id, tree in trees.items():
        by_id: dict[str, dict[str, str]] = {}
        by_title: dict[str, list[dict[str, str]]] = {}
        for section in tree.get("contentSections") or []:
            for page in section.get("contentPages") or []:
                page_id = page.get("_id")
                if not page_id:
                    continue
                entry = {
                    "pageId": page_id,
                    "pageTitle": page.get("title") or "",
                    "sectionTitle": section.get("title") or "",
                }
                by_id[page_id] = entry
                by_title.setdefault(normalize_title(entry["pageTitle"]), []).append(entry)
        index[product_id] = {
            "title": tree.get("title") or product_id,
            "byId": by_id,
            "byTitle": by_title,
        }
    return index


def resolve_source(
    source: dict[str, Any], index: dict[str, dict[str, Any]]
) -> tuple[Optional[dict[str, str]], str, str]:
    """Locate a pinned donor page, healing a moved id via its recorded title.

    Returns ``(entry, status, detail)``. A pin that resolves by id is ``reuse``;
    one that only resolves because the recorded title still exists elsewhere is
    ``moved`` and is surfaced for review rather than applied silently.
    """
    product_id = str(source.get("productId") or "")
    page_id = str(source.get("pageId") or "")
    product = index.get(product_id)
    if not product:
        return None, STATUS_MISSING, f"Donor product {product_id or '(none)'} was not loaded"

    entry = product["byId"].get(page_id)
    if entry:
        return entry, STATUS_REUSE, ""

    recorded_title = str(source.get("pageTitle") or "")
    candidates = product["byTitle"].get(normalize_title(recorded_title)) or []
    if len(candidates) == 1:
        moved = candidates[0]
        return (
            moved,
            STATUS_MOVED,
            f"Pinned page {page_id} is gone; matched '{moved['pageTitle']}' "
            f"({moved['pageId']}) by title instead",
        )
    if len(candidates) > 1:
        return None, STATUS_MISSING, (
            f"Pinned page {page_id} is gone and '{recorded_title}' is ambiguous "
            f"({len(candidates)} pages share it)"
        )
    return None, STATUS_MISSING, (
        f"Pinned page {page_id} no longer exists in {product['title']} and no page "
        f"is titled '{recorded_title}'"
    )


# --------------------------------------------------------------------------- #
# Page body stats
# --------------------------------------------------------------------------- #

def _load_page_cache() -> dict[str, Any]:
    try:
        cached = json.loads(PAGE_CACHE_PATH.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}
    return cached if isinstance(cached, dict) else {}


def _save_page_cache(cache: dict[str, Any]) -> None:
    try:
        PAGE_CACHE_PATH.write_text(json.dumps(cache), encoding="utf-8")
    except OSError:
        # A read-only deploy target just loses the cache, not the feature.
        pass


def measure_markdown(markdown: str) -> dict[str, int]:
    body = str(markdown or "")
    return {
        "words": len(body.split()),
        "chars": len(body),
        "images": body.count("!["),
        "codeBlocks": body.count("```") // 2,
    }


def collect_page_stats(
    page_ids: Iterable[str],
    fetch_page: Callable[[str], dict[str, Any]],
    *,
    refresh: bool = False,
    now: Optional[float] = None,
) -> dict[str, dict[str, Any]]:
    """Read each donor body once, caching the measurements but never the text."""
    now = time.time() if now is None else now
    cache = {} if refresh else _load_page_cache()
    stats: dict[str, dict[str, Any]] = {}
    dirty = False

    for page_id in dict.fromkeys(pid for pid in page_ids if pid):
        cached = cache.get(page_id)
        if isinstance(cached, dict) and now - float(cached.get("fetchedAt") or 0) < PAGE_CACHE_TTL_SECONDS:
            stats[page_id] = cached
            continue
        try:
            page = fetch_page(page_id)
            measured = measure_markdown(page.get("markdown"))
            measured["title"] = page.get("title") or ""
            measured["ok"] = True
        except Exception as exc:  # a dead donor must not abort the whole plan
            measured = {"words": 0, "chars": 0, "images": 0, "codeBlocks": 0,
                        "title": "", "ok": False, "error": str(exc)}
        measured["fetchedAt"] = now
        cache[page_id] = measured
        stats[page_id] = measured
        dirty = True

    if dirty:
        _save_page_cache(cache)
    return stats


# --------------------------------------------------------------------------- #
# Plan
# --------------------------------------------------------------------------- #

def build_plan(
    blueprint: dict[str, Any],
    trees: dict[str, dict[str, Any]],
    page_stats: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    """Resolve every blueprint topic against the donor catalogue."""
    index = index_donor_pages(trees)
    units: list[dict[str, Any]] = []
    counts = {STATUS_REUSE: 0, STATUS_MOVED: 0, STATUS_THIN: 0,
              STATUS_MISSING: 0, STATUS_AUTHOR: 0}
    gaps: list[dict[str, Any]] = []
    blockers: list[dict[str, Any]] = []
    position = 0
    reused_words = 0
    seen_page_ids: dict[str, str] = {}

    for unit in blueprint.get("units") or []:
        planned_chapters = []
        for chapter in unit.get("chapters") or []:
            planned_topics = []
            for topic in chapter.get("topics") or []:
                position += 1
                title = topic.get("title") or ""
                row: dict[str, Any] = {
                    "position": position,
                    "unitNumber": unit.get("number"),
                    "unitTitle": unit.get("title"),
                    "chapterNumber": chapter.get("number"),
                    "chapterTitle": chapter.get("title"),
                    "sectionTitle": section_title(unit, chapter),
                    "title": title,
                    "note": topic.get("note") or "",
                }

                if topic.get("authorNew") or not topic.get("source"):
                    row.update({"status": STATUS_AUTHOR, "detail": "", "source": None,
                                "stats": None})
                    counts[STATUS_AUTHOR] += 1
                    gaps.append({"position": position, "title": title,
                                 "sectionTitle": row["sectionTitle"],
                                 "note": row["note"]})
                    planned_topics.append(row)
                    continue

                entry, status, detail = resolve_source(topic["source"], index)
                if entry is None:
                    row.update({"status": STATUS_MISSING, "detail": detail,
                                "source": topic["source"], "stats": None})
                    counts[STATUS_MISSING] += 1
                    blockers.append({"position": position, "title": title, "detail": detail})
                    planned_topics.append(row)
                    continue

                product_id = topic["source"].get("productId")
                stats = page_stats.get(entry["pageId"]) or {}
                if not stats.get("ok", True):
                    detail = f"Could not read the donor page: {stats.get('error')}"
                    row.update({"status": STATUS_MISSING, "detail": detail,
                                "source": topic["source"], "stats": stats})
                    counts[STATUS_MISSING] += 1
                    blockers.append({"position": position, "title": title, "detail": detail})
                    planned_topics.append(row)
                    continue

                words = int(stats.get("words") or 0)
                if status == STATUS_REUSE and words < THIN_WORD_COUNT:
                    status = STATUS_THIN
                    detail = (f"Donor page is {words} words, under the {THIN_WORD_COUNT}-word "
                              f"floor for a syllabus topic")

                duplicate_of = seen_page_ids.get(entry["pageId"])
                if duplicate_of:
                    detail = ((detail + " ") if detail else "") + (
                        f"Same donor page already fills '{duplicate_of}'")
                seen_page_ids[entry["pageId"]] = title

                counts[status] += 1
                reused_words += words
                row.update({
                    "status": status,
                    "detail": detail,
                    "source": {
                        "productId": product_id,
                        "productTitle": index[product_id]["title"],
                        "sectionTitle": entry["sectionTitle"],
                        "pageId": entry["pageId"],
                        "pageTitle": entry["pageTitle"],
                    },
                    "stats": {k: stats.get(k) for k in ("words", "images", "codeBlocks")},
                })
                planned_topics.append(row)

            planned_chapters.append({
                "number": chapter.get("number"),
                "title": chapter.get("title"),
                "sectionTitle": section_title(unit, chapter),
                "topics": planned_topics,
            })

        units.append({
            "number": unit.get("number"),
            "title": unit.get("title"),
            "courseOutcome": unit.get("courseOutcome"),
            "hours": unit.get("hours"),
            "syllabus": unit.get("syllabus"),
            "chapters": planned_chapters,
        })

    total = position
    return {
        "slug": blueprint.get("slug"),
        "title": blueprint.get("title"),
        "description": blueprint.get("description"),
        "syllabus": blueprint.get("syllabus") or {},
        "sources": [
            {
                "productId": source.get("productId"),
                "title": index.get(source.get("productId"), {}).get("title") or source.get("title"),
                "used": sum(
                    1
                    for unit in units
                    for chapter in unit["chapters"]
                    for topic in chapter["topics"]
                    if (topic.get("source") or {}).get("productId") == source.get("productId")
                ),
            }
            for source in blueprint.get("sources") or []
        ],
        "units": units,
        "totals": {
            "units": len(units),
            "chapters": sum(len(unit["chapters"]) for unit in units),
            "topics": total,
            "reuse": counts[STATUS_REUSE],
            "moved": counts[STATUS_MOVED],
            "thin": counts[STATUS_THIN],
            "missing": counts[STATUS_MISSING],
            "author": counts[STATUS_AUTHOR],
            "reusedWords": reused_words,
            "coverage": round(
                (counts[STATUS_REUSE] + counts[STATUS_MOVED] + counts[STATUS_THIN]) / total, 4
            ) if total else 0.0,
        },
        "gaps": gaps,
        "blockers": blockers,
        "canCreate": total > 0 and not blockers,
    }


def creation_steps(plan: dict[str, Any]) -> list[dict[str, Any]]:
    """The per-section write list, in the order the product will hold it."""
    steps: list[dict[str, Any]] = []
    for unit in plan.get("units") or []:
        for chapter in unit.get("chapters") or []:
            steps.append({
                "sectionTitle": chapter["sectionTitle"],
                "topics": [
                    {
                        "title": topic["title"],
                        "sourcePageId": (topic.get("source") or {}).get("pageId"),
                        "authorNew": topic["status"] == STATUS_AUTHOR,
                    }
                    for topic in chapter.get("topics") or []
                ],
            })
    return steps


# --------------------------------------------------------------------------- #
# Courses (the platform's own Course Builder, distinct from reading material)
# --------------------------------------------------------------------------- #
#
# A ByteXL "course" (``/api/courses``) is not the lesson content itself -- it is
# a Module -> Topic -> SubTopic tree of deep links into a reading-material
# product. This is what shows under the platform's own Course Builder screen;
# the reading material created by ``build_plan``/the create route above is the
# backing content it links to. Module = the syllabus Unit, Topic = the Chapter,
# SubTopic = one lesson link (``topicType: "readingMaterial"``) whose ``data``
# field is a URL of the shape
# ``https://app.bytexl.ai/reading/{readingId}/{reading-slug}/{pageId}/{section-slug}/{page-slug}``.
#
# The link is built by cross-referencing the *live* reading-material tree
# against the plan by title within each section, not by trusting page ids
# recorded anywhere -- a lesson dropped via ``skipAuthorNew`` at creation time
# simply will not be found and is reported back as excluded, the same way a
# gap is reported in the reading-material plan.


def blueprint_skeleton(blueprint: dict[str, Any]) -> dict[str, Any]:
    """The unit/chapter/topic titles from a blueprint, with no donor resolution.

    ``build_course_structure`` only needs titles and section names to cross-
    reference against a *live* reading-material tree -- it does not care which
    donor a topic came from or whether it resolved. Running the full
    ``build_plan`` machinery here would need a fabricated ``trees`` dict keyed
    by the wrong ids and would silently mark every topic ``missing``, which is
    harmless but misleading. This is the direct, honest version.
    """
    return {
        "units": [
            {
                "number": unit.get("number"),
                "title": unit.get("title"),
                "chapters": [
                    {
                        "sectionTitle": section_title(unit, chapter),
                        "title": chapter.get("title"),
                        # Where the client-facing course should file this
                        # chapter. Several reading-material chapters can share
                        # one, which merges them in the course.
                        "courseChapter": chapter.get("courseChapter") or chapter.get("title"),
                        "topics": [{"title": t.get("title")} for t in chapter.get("topics") or []],
                    }
                    for chapter in unit.get("chapters") or []
                ],
            }
            for unit in blueprint.get("units") or []
        ]
    }


def build_course_structure(
    plan: dict[str, Any],
    reading: dict[str, Any],
    make_id: Callable[[], str],
) -> dict[str, Any]:
    reading_id = reading.get("_id") or ""
    reading_title = reading.get("title") or ""
    pages_by_section: dict[str, dict[str, tuple[str, str]]] = {}
    for section in reading.get("contentSections") or []:
        pages_by_section[section.get("title") or ""] = {
            normalize_title(page.get("title") or ""): (page.get("_id"), page.get("title") or "")
            for page in section.get("contentPages") or []
            if page.get("_id")
        }

    modules: list[dict[str, Any]] = []
    included: list[dict[str, str]] = []
    excluded: list[dict[str, str]] = []

    for unit in plan.get("units") or []:
        module_title = f"Unit {unit.get('number')} - {unit.get('title')}"
        # Chapters that name the same courseChapter collapse into one course
        # chapter, in blueprint order, keeping their lessons contiguous.
        merged: dict[str, list[dict[str, Any]]] = {}
        order: list[str] = []
        for chapter in unit.get("chapters") or []:
            section = chapter.get("sectionTitle") or ""
            available = pages_by_section.get(section, {})
            course_chapter = chapter.get("courseChapter") or chapter.get("title") or ""
            if course_chapter not in merged:
                merged[course_chapter] = []
                order.append(course_chapter)
            for topic in chapter.get("topics") or []:
                title = topic.get("title") or ""
                match = available.get(normalize_title(title))
                if not match:
                    excluded.append({"sectionTitle": section, "title": title})
                    continue
                page_id, page_title = match
                merged[course_chapter].append({
                    "_id": make_id(),
                    "title": title,
                    "topicType": "readingMaterial",
                    "data": reading_material_url(
                        reading_id, reading_title, page_id, section, page_title
                    ),
                    "time": 0,
                })
                included.append({"sectionTitle": section, "title": title})

        module_topics = [
            {"_id": make_id(), "title": name, "subTopics": merged[name]}
            for name in order
            if merged[name]
        ]
        if not module_topics:
            continue
        modules.append({
            "_id": make_id(),
            "title": module_title,
            "topics": module_topics,
        })

    return {
        "modules": modules,
        "included": included,
        "excluded": excluded,
        "totals": {
            "modules": len(modules),
            "topics": sum(len(m["topics"]) for m in modules),
            "subTopics": len(included),
            "excluded": len(excluded),
        },
    }


def build_course_from_donors(
    blueprint: dict[str, Any],
    trees: dict[str, dict[str, Any]],
    make_id: Callable[[], str],
) -> dict[str, Any]:
    """Build the course tree linking straight into the donor products.

    The alternative -- cloning every lesson into a per-college reading-material
    product and pointing the course at that -- duplicates content and leaves two
    copies to maintain. Linking to the strategic courses instead means an edit to
    a Modern Python lesson reaches every tactical course built on it. Nineteen
    live courses already link across more than one reading product, so this is
    the platform's own pattern rather than a workaround.

    Each pin is re-resolved against the live donor tree, so the section and page
    titles baked into the URL are the current ones. A pin that no longer
    resolves is reported as ``blocked`` and must stop the write: a lesson link
    built from a stale page id renders as a working row and opens nothing.
    """
    index = index_donor_pages(trees)
    modules: list[dict[str, Any]] = []
    included: list[dict[str, Any]] = []
    excluded: list[dict[str, Any]] = []
    blocked: list[dict[str, Any]] = []
    attached: list[dict[str, Any]] = []
    unattached: list[dict[str, Any]] = []
    used_products: dict[str, int] = {}

    for unit in blueprint.get("units") or []:
        module_title = f"Unit {unit.get('number')} - {unit.get('title')}"
        merged: dict[str, list[dict[str, Any]]] = {}
        order: list[str] = []

        for chapter in unit.get("chapters") or []:
            course_chapter = chapter.get("courseChapter") or chapter.get("title") or ""
            reading_chapter = section_title(unit, chapter)
            if course_chapter not in merged:
                merged[course_chapter] = []
                order.append(course_chapter)

            for topic in chapter.get("topics") or []:
                title = topic.get("title") or ""
                source = topic.get("source")
                if topic.get("authorNew") or not source:
                    excluded.append({
                        "chapter": course_chapter,
                        "readingChapter": reading_chapter,
                        "title": title,
                        "note": topic.get("note") or "",
                    })
                    continue

                entry, status, detail = resolve_source(source, index)
                if entry is None:
                    blocked.append({"chapter": course_chapter, "title": title, "detail": detail})
                    continue

                product_id = str(source.get("productId"))
                product = index[product_id]
                merged[course_chapter].append({
                    "_id": make_id(),
                    "title": title,
                    "topicType": "readingMaterial",
                    "data": reading_material_url(
                        product_id, product["title"], entry["pageId"],
                        entry["sectionTitle"], entry["pageTitle"],
                    ),
                    "time": 0,
                })
                used_products[product_id] = used_products.get(product_id, 0) + 1
                included.append({
                    "chapter": course_chapter,
                    "title": title,
                    "productId": product_id,
                    "productTitle": product["title"],
                    "pageId": entry["pageId"],
                    "pageTitle": entry["pageTitle"],
                    "status": status,
                    "detail": detail,
                })

        # Labs and quizzes are platform assets referenced by test id, appended
        # after the readings of the chapter they belong to.
        extras_map = blueprint.get("courseExtras") or {}
        for name in order:
            # Only attach to a chapter that actually materialised. A lab must not
            # be the sole reason a chapter exists -- if every reading in it was
            # unwritten, the chapter is not ready to ship.
            if not merged[name]:
                for extra in extras_map.get(f"{unit.get('number')}|{name}") or []:
                    unattached.append({"chapter": name, "title": extra.get("title") or "",
                                       "reason": "chapter has no lessons"})
                continue
            for extra in extras_map.get(f"{unit.get('number')}|{name}") or []:
                merged[name].append({
                    "_id": make_id(),
                    "title": extra.get("title") or "",
                    "topicType": extra.get("topicType") or "challenge",
                    "data": extra.get("data") or "",
                    "time": 0,
                })
                attached.append({"chapter": name, "title": extra.get("title") or "",
                                 "topicType": extra.get("topicType") or "challenge"})

        module_topics = [
            {"_id": make_id(), "title": name, "subTopics": merged[name]}
            for name in order
            if merged[name]
        ]
        if not module_topics:
            continue
        modules.append({"_id": make_id(), "title": module_title, "topics": module_topics})

    return {
        "modules": modules,
        "included": included,
        "excluded": excluded,
        "blocked": blocked,
        "attached": attached,
        "unattached": unattached,
        "sources": [
            {"productId": pid, "title": index[pid]["title"], "used": count}
            for pid, count in sorted(used_products.items(), key=lambda kv: -kv[1])
        ],
        "totals": {
            "modules": len(modules),
            "chapters": sum(len(m["topics"]) for m in modules),
            "lessons": len(included),
            "extras": len(attached),
            "unattachedExtras": len(unattached),
            "excluded": len(excluded),
            "blocked": len(blocked),
        },
        "canCreate": bool(modules) and not blocked,
    }


def carry_over_manual_items(
    modules: list[dict[str, Any]], existing_modules: list[dict[str, Any]]
) -> dict[str, Any]:
    """Re-attach anything hand-added to the course that the blueprint does not own.

    A rebuild replaces the module tree wholesale, which is how a set of labs
    added by hand in the ByteXL UI was destroyed once. The blueprint owns the
    reading links and its declared ``courseExtras``; **everything else in the
    live course was put there by a person and must survive.** Items are matched
    back by chapter title and de-duplicated on ``data``, so re-running is safe.

    Anything whose chapter no longer exists is returned in ``orphaned`` rather
    than dropped quietly, so the caller can refuse the write and say what would
    have been lost.
    """
    # Ownership is keyed on the referenced asset alone, not on chapter+asset. A
    # quiz the blueprint moves to a merged chapter is still the blueprint's, so
    # it must not be re-attached to its old home or reported as stranded.
    owned_keys = {
        sub.get("data")
        for module in modules
        for topic in module.get("topics") or []
        for sub in topic.get("subTopics") or []
    }
    chapters_by_title = {
        topic.get("title"): topic
        for module in modules
        for topic in module.get("topics") or []
    }

    carried: list[dict[str, Any]] = []
    orphaned: list[dict[str, Any]] = []

    for module in existing_modules or []:
        for topic in module.get("topics") or []:
            chapter_title = topic.get("title")
            for sub in topic.get("subTopics") or []:
                # Reading links are rebuilt from the blueprint every time, so an
                # old one is stale by definition, not manual work.
                if sub.get("topicType") == "readingMaterial":
                    continue
                if sub.get("data") in owned_keys:
                    continue
                target = chapters_by_title.get(chapter_title)
                record = {
                    "chapter": chapter_title,
                    "title": sub.get("title"),
                    "topicType": sub.get("topicType"),
                    "data": sub.get("data"),
                }
                if target is None:
                    orphaned.append(record)
                    continue
                target.setdefault("subTopics", []).append(sub)
                carried.append(record)

    return {"carried": carried, "orphaned": orphaned}


def placeholder_markdown(topic_title: str, plan: dict[str, Any], note: str) -> str:
    """The stub written for a topic with no donor, so the gap is visible in-product."""
    course = plan.get("title") or "this course"
    lines = [
        f"# {topic_title}",
        "",
        "> **This lesson has not been written yet.**",
        "",
        f"The syllabus for {course} requires this topic, and no reading material "
        "covering it exists anywhere in the ByteXL catalogue, so it could not be "
        "reused from another course.",
    ]
    if note:
        lines += ["", f"**Why it is missing:** {note}"]
    lines += [
        "",
        "Replace this page with the full lesson before the course is handed to "
        "the college.",
        "",
    ]
    return "\n".join(lines)
