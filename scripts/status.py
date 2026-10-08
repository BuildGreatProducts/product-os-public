#!/usr/bin/env python3
"""Report ProductOS progress for an app repo: which steps are done, the product's shape, the next step.

Run from the app repo root:   python3 productos/scripts/status.py
Or point it at a repo:        python3 <productos>/scripts/status.py --repo <app-repo-root>
Add --json for machine-readable output.

Read-only: it inspects docs/ and the root guidelines and never writes. ROUTING.md defines each
step and its "Done when"; this script checks exactly those conditions. The order it suggests is
checklist order filtered by the product's shape. A docs/PLAN.md, when present, overrides it.
"""
import argparse
import json
import os
import re
import sys

PRODUCTOS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_SHAPE = "web-app"  # repos from before 2.0 have no Product Shape section

# (phase, label, skill, keywords used to find the step's row in a shape file's route table)
STEPS = [
    ("Define", "1 — Product Offer", "define-offer-builder", None),
    ("Define", "1b — Product Shape", "define-product-shape", None),
    ("Define", "2 — Customer Persona", "define-customer-persona", None),
    ("Define", "3 — Pricing Strategy", "define-pricing", None),
    ("Define", "4 — Business Strategy (optional)", "define-business-strategy", None),
    ("Design", "1 — Product Identity", "design-identity-creator", ["identity"]),
    ("Design", "2 — UX Writing", "design-ux-writing", ["ux writing", "copy"]),
    ("Design", "3 — Design System", "design-design-system", ["design system"]),
    ("Design", "4 — Design Prompts", "design-prompt-generator", ["prompt"]),
    ("Design", "5 — Magic Moment", "design-magic-moment", ["magic moment"]),
    ("Design", "6 — Onboarding", "design-onboarding-flow", ["onboarding"]),
    ("Design", "7 — Acquisition surface(s)", "design-landing-page / design-app-listing / design-marketplace-listing", ["acquisition"]),
    ("Develop", "0 — Migrate", "develop-migrate", ["migrate"]),
    ("Develop", "1 — PRD & Roadmap", "develop-prd-roadmap", ["prd"]),
    ("Develop", "1b — Evals", "develop-agent-evals", ["evals"]),
    ("Develop", "2 — Verify setup", "setup", ["verify setup", "setup"]),
    ("Develop", "3 — Build", "develop-build", ["build"]),
    ("Develop", "7 — Conversion review", "develop-cro-audit", ["conversion"]),
    ("Develop", "8 — Security audit", "develop-security-audit", ["security"]),
    ("Develop", "9 — Go live", "develop-golive", ["go live", "go-live"]),
    ("Distribute", "1 — Go-To-Market", "distribute-gtm-strategy", None),
    ("Distribute", "2 — Growth Experiments", "distribute-growth-experiments", None),
    ("Distribute", "3 — Run the cycle", "the member, logging in docs/GROWTH-TRACKER.md", None),
    ("Distribute", "4 — Scale & Automate", "distribute-scale-automate", None),
]
# Steps the next-step suggestion skips over: optional, ongoing, or only for some members.
NOT_GATING = {"4 — Business Strategy (optional)", "0 — Migrate", "2 — Verify setup", "7 — Conversion review"}
SURFACES = {"landing-page": "LANDING-PAGE.md", "app-listing": "APP-LISTING.md",
            "marketplace-listing": "MARKETPLACE-LISTING.md"}


def read(path):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except OSError:
        return None


def sections(text, level="##"):
    """Split Markdown into {heading: body} at the given heading level."""
    out, name, buf = {}, None, []
    for line in text.split("\n"):
        m = re.match(rf"^{level} (?!#)(.+?)\s*$", line)
        if m:
            if name is not None:
                out[name] = "\n".join(buf)
            name, buf = m.group(1).strip(), []
        elif name is not None:
            buf.append(line)
    if name is not None:
        out[name] = "\n".join(buf)
    return out


def has_content(body):
    """True if a section has real text beyond headings, placeholders, and HTML comments."""
    body = re.sub(r"<!--.*?-->", "", body or "", flags=re.S)
    for line in body.split("\n"):
        s = line.strip()
        if not s or s.startswith("#") or re.match(r"^\*Filled by", s) or s == "---":
            continue
        return True
    return False


def find_section(secs, *names):
    for key, body in secs.items():
        bare = re.sub(r"\s*\*\(optional\)\*", "", key).strip()
        if bare in names:
            return body
    return None


def subsection_state(body):
    """done if every ### subsection has content, partial if some do, missing if none."""
    if body is None:
        return "missing"
    subs = sections(body, "###")
    if not subs:
        return "done" if has_content(body) else "missing"
    filled = sum(has_content(b) for b in subs.values())
    if filled == len(subs):
        return "done"
    return "partial" if filled else "missing"


def valid_slugs():
    text = read(os.path.join(PRODUCTOS, "shapes", "SHAPES.md")) or ""
    return re.findall(r"^\|\s*`([a-z-]+)`\s*\|", text, re.M)


def shape_routes(slug):
    """{step keyword: (mode, how-it-adapts)} from the shape file's route tables."""
    text = read(os.path.join(PRODUCTOS, "shapes", f"{slug}.md")) or ""
    rows = {}
    for line in text.split("\n"):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2 or not line.lstrip().startswith("|") or set(cells[0]) <= set("-: "):
            continue
        mode = re.match(r"\**(Full|Adapted|Lite|Optional|Skip)\b", cells[1], re.I)
        if mode:
            name = mode.group(1).capitalize()
            if re.search(r"/\s*\**skip", cells[1], re.I):
                name = "Conditional"  # "Full / Skip" — the condition is in the next cell
            rows[cells[0].lower()] = (name, " | ".join(cells[2:]))
    return rows


def route_for(routes, keywords):
    if not keywords:
        return None
    for step, value in routes.items():
        # "build loop" must not match the Build step
        if any(k in step for k in keywords) and not (keywords == ["build"] and "loop" in step):
            return value
    return None


def checkbox_progress(text):
    done = len(re.findall(r"^\s*- \[[xX]\]", text, re.M))
    total = done + len(re.findall(r"^\s*- \[ \]", text, re.M))
    return done, total


def status(repo):
    docs = os.path.join(repo, "docs")
    doc = lambda name: read(os.path.join(docs, name))  # noqa: E731
    result = {"repo": os.path.abspath(repo), "steps": [], "notes": []}

    define = doc("DEFINE.md")
    secs = sections(define) if define else {}
    slugs = valid_slugs()
    shape_body = find_section(secs, "Product Shape")
    primary = None
    if shape_body:
        prim = sections(shape_body, "###").get("Primary Shape", "")
        found = [s for s in re.findall(r"`([a-z-]+)`", prim) if s in slugs]
        primary = found[0] if found else None
    result["shape"] = primary or DEFAULT_SHAPE
    result["shape_source"] = "docs/DEFINE.md" if primary else f"default ({DEFAULT_SHAPE}) — no Product Shape yet"
    routes = shape_routes(result["shape"])

    design = doc("DESIGN.md") or ""
    roadmap = doc("ROADMAP.md")
    refactor = doc("REFACTOR.md")
    tracker = doc("GROWTH-TRACKER.md") or ""
    root_rules = (read(os.path.join(repo, "CLAUDE.md")) or "") + (read(os.path.join(repo, "AGENTS.md")) or "")

    def exists(name):
        return "done" if doc(name) is not None else "missing"

    def evidence_roadmap():
        if roadmap is None:
            return "missing", "no docs/ROADMAP.md"
        m = re.search(r"\*\*Status:\*\*\s*(\d+)\s*/\s*(\d+)", roadmap)
        d, t = (int(m.group(1)), int(m.group(2))) if m else checkbox_progress(roadmap)
        legacy = ""
        if refactor:
            rd, rt = checkbox_progress(refactor)
            legacy = f"; legacy docs/REFACTOR.md {rd}/{rt}"
            if rd < rt:
                return "partial", f"ROADMAP {d}/{t}{legacy}"
        return ("done" if t and d >= t else "partial"), f"ROADMAP {d}/{t}{legacy}"

    def security():
        text = doc("SECURITY-AUDIT.md")
        if text is None:
            return "missing", "no docs/SECURITY-AUDIT.md"
        if re.search(r"not safe to launch", text, re.I):
            return "partial", "verdict: Not safe to launch"
        if re.search(r"safe to launch", text, re.I):
            return "done", "verdict: Safe to launch"
        return "partial", "no verdict line found"

    def tracker_rows():
        rows = [l for l in tracker.split("\n") if l.startswith("|") and not re.match(r"^\|\s*(\*|-|Date\b)", l)]
        winners = [r for r in rows if re.search(r"\bPass\b", r) and re.search(r"double down", r, re.I)]
        return rows, winners

    surface_route = route_for(routes, ["acquisition"])
    wanted = []
    for sentence in re.split(r"(?<=[.;])\s+", surface_route[1] if surface_route else ""):
        # a surface named in a conditional sentence ("Add X when…", "X is Optional") isn't required
        if re.search(r"\b(when|if|only|optional|used|is for|not)\b", re.sub(r"\([^)]*\)", "", sentence), re.I):
            continue
        wanted += [k for k in SURFACES if f"design-{k}" in sentence and k not in wanted]
    wanted = wanted or ["landing-page"]

    checks = {
        "1 — Product Offer": lambda: (
            "done" if has_content(find_section(secs, "Summary")) and subsection_state(find_section(secs, "1. Product Offer")) == "done"
            else ("partial" if define and has_content(find_section(secs, "1. Product Offer")) else "missing"),
            "docs/DEFINE.md" if define else "no docs/DEFINE.md"),
        "1b — Product Shape": lambda: ("done" if primary else ("partial" if shape_body and has_content(shape_body) else "missing"),
                                      f"primary shape `{primary}`" if primary else "no valid Primary Shape slug"),
        "2 — Customer Persona": lambda: (subsection_state(find_section(secs, "2. Customer Persona")), ""),
        "3 — Pricing Strategy": lambda: (subsection_state(find_section(secs, "3. Pricing Strategy")), ""),
        "4 — Business Strategy (optional)": lambda: (subsection_state(find_section(secs, "4. Business Strategy")), ""),
        "1 — Product Identity": lambda: ("done" if has_content(sections(design).get("Product Identity")) else "missing", ""),
        "2 — UX Writing": lambda: (exists("COPY.md"), ""),
        "3 — Design System": lambda: ("done" if re.search(r"\A---\n.*?^colors:", design, re.S | re.M) else "missing",
                                      "YAML tokens in docs/DESIGN.md" if design else "no docs/DESIGN.md"),
        "4 — Design Prompts": lambda: (exists("DESIGN-PROMPTS.md"), ""),
        "5 — Magic Moment": lambda: (exists("MAGIC-MOMENT.md"), ""),
        "6 — Onboarding": lambda: (exists("ONBOARDING.md"), ""),
        "7 — Acquisition surface(s)": lambda: (
            "done" if all(doc(SURFACES[k]) is not None for k in wanted)
            else ("partial" if any(doc(SURFACES[k]) is not None for k in wanted) else "missing"),
            "needs " + ", ".join(f"docs/{SURFACES[k]}" for k in wanted)),
        "0 — Migrate": lambda: (("done" if checkbox_progress(doc("MIGRATION.md"))[0] == checkbox_progress(doc("MIGRATION.md"))[1] else "partial")
                                if doc("MIGRATION.md") is not None else "n/a", "only for apps on a prompt-to-app platform"),
        "1 — PRD & Roadmap": lambda: (
            "partial" if roadmap is not None and "## Decisions (draft)" in roadmap
            else "done" if doc("PRD.md") is not None and roadmap is not None
            else ("partial" if doc("PRD.md") is not None or roadmap is not None else "missing"),
            "keep-or-remove decisions still in draft" if roadmap and "## Decisions (draft)" in roadmap else ""),
        "1b — Evals": lambda: (exists("EVALS.md"), ""),
        "2 — Verify setup": lambda: ("done" if "BEGIN PRODUCTOS" in root_rules or "ProductOS" in root_rules else "missing",
                                     "root CLAUDE.md / AGENTS.md"),
        "3 — Build": evidence_roadmap,
        "7 — Conversion review": lambda: (exists("CRO-AUDIT.md"), ""),
        "8 — Security audit": security,
        "9 — Go live": lambda: (exists("DEPLOY.md"), "the shape's Live-means bar decides when it's live"),
        "1 — Go-To-Market": lambda: (exists("GO-TO-MARKET.md"), ""),
        "2 — Growth Experiments": lambda: (exists("GROWTH-EXPERIMENTS.md"), ""),
        "3 — Run the cycle": lambda: (("done" if tracker_rows()[0] else "missing") if tracker else "missing",
                                     f"{len(tracker_rows()[0])} logged result(s), {len(tracker_rows()[1])} winner(s)"),
        "4 — Scale & Automate": lambda: (exists("SCALE.md"),
                                        "activation audit " + ("done" if doc("ACTIVATION-RETENTION-AUDIT.md") is not None else "not run")),
    }

    for phase, label, skill, keywords in STEPS:
        state, evidence = checks[label]()
        route = route_for(routes, keywords)
        mode = route[0] if route else ("Optional" if "optional" in label else "Full")
        if mode == "Skip" and state != "done":
            state = "n/a"
        result["steps"].append({"phase": phase, "step": label, "skill": skill, "status": state,
                                "shape_mode": mode, "evidence": evidence})

    nxt = next((s for s in result["steps"]
                if s["status"] in ("missing", "partial") and s["step"] not in NOT_GATING
                and s["shape_mode"] not in ("Skip", "Optional", "Conditional")), None)
    result["next"] = nxt

    plan = doc("PLAN.md")
    result["plan"] = None if plan is None else ("product-audit" if "product-audit" in plan else "coach")
    challenges = {}
    for name in ("SHIP-IN-7.md", "SELL-IN-30.md"):
        text = doc(name)
        if text is not None:
            challenges[name] = "open" if re.search(r"^\**Status:?\**:?\s*Open", text, re.M) else "closed"
    result["challenges"] = challenges
    if not define:
        result["notes"].append("No docs/DEFINE.md — start with define-offer-builder (or define-from-code for an existing product).")
    if define and not primary:
        result["notes"].append(f"No Product Shape yet — routes assume `{DEFAULT_SHAPE}` until define-product-shape runs.")
    if plan is not None:
        result["notes"].append("docs/PLAN.md exists — it decides the order; the next step below is checklist order only.")
    if any(v == "open" for v in challenges.values()):
        result["notes"].append("A challenge is open — its check-in decides today's step.")
    return result


def render(r):
    lines = [f"ProductOS status — {r['repo']}",
             f"Shape: {r['shape']}  ({r['shape_source']})",
             f"Plan: {r['plan'] or 'none'}   Challenges: {', '.join(f'{k} {v}' for k, v in r['challenges'].items()) or 'none'}", ""]
    phase = None
    for s in r["steps"]:
        if s["phase"] != phase:
            phase = s["phase"]
            lines.append(phase)
        mode = "" if s["shape_mode"] == "Full" else f" [{s['shape_mode']}]"
        ev = f" — {s['evidence']}" if s["evidence"] else ""
        lines.append(f"  {s['status']:<8} {s['step']}{mode}{ev}")
    lines.append("")
    n = r["next"]
    lines.append(f"Next (checklist order): {n['phase']} {n['step']} → {n['skill']}" if n else "Next: every gating step is done — keep running the Distribute loop.")
    lines += [f"Note: {x}" for x in r["notes"]]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--repo", default=".", help="app repo root (default: current directory)")
    ap.add_argument("--json", action="store_true", help="print JSON instead of a table")
    args = ap.parse_args()
    if not os.path.isdir(args.repo):
        sys.exit(f"Not a folder: {args.repo}")
    r = status(args.repo)
    print(json.dumps(r, indent=2) if args.json else render(r))


if __name__ == "__main__":
    main()
