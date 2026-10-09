#!/usr/bin/env python3
"""Report ProductOS progress for an app repo: which steps are done, the product's shape, the next step.

Run from the app repo root:   python3 productos/scripts/status.py
Or point it at a repo:        python3 <productos>/scripts/status.py --repo <app-repo-root>
With no flag it prints a short plain-English summary for the member. Add --detail for every step
(what the orchestrators read), --json for machine-readable output, or --greet for the
session-start hook's JSON (silent when the repo doesn't use ProductOS).

Read-only: it inspects docs/ and the root guidelines and never writes. ROUTING.md defines each
step and its "Done when"; this script checks exactly those conditions. The order it suggests is
the phase's route in docs/PATH.md when the phase orchestrator has set one, otherwise checklist
order filtered by the product's shape. A docs/PLAN.md, when present, overrides both.
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
    # Verify setup runs first in Develop: version history goes on before any code is written or moved
    ("Develop", "2 — Verify setup", "setup", ["verify setup", "setup"]),
    ("Develop", "0 — Migrate", "develop-migrate", ["migrate"]),
    ("Develop", "1 — PRD & Roadmap", "develop-prd-roadmap", ["prd"]),
    ("Develop", "1b — Evals", "develop-agent-evals", ["evals"]),
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
# A route in docs/PATH.md that runs one of them makes it count.
NOT_GATING = {"4 — Business Strategy (optional)", "0 — Migrate", "7 — Conversion review"}
PHASES = ["Define", "Design", "Develop", "Distribute"]
# Modes a docs/PATH.md row can carry; the run modes make a step count toward the next step.
PATH_MODES = {m.lower(): m for m in ("Full", "Fast-track", "Adapted", "Lite", "Optional", "Skip", "Already-done")}
RUN_MODES = {"Full", "Fast-track", "Adapted", "Lite"}
# What each step does for the member, in plain words, for the summary and the greeting.
PLAIN = {
    ("Define", "1"): "describe who your product is for, the problem it solves, and what it promises",
    ("Define", "1b"): "decide what form your product takes — an app, a plugin, a service, and so on",
    ("Define", "2"): "describe your ideal customer",
    ("Define", "3"): "set your price",
    ("Define", "4"): "check the numbers behind the business",
    ("Design", "1"): "name your product and set its personality",
    ("Design", "2"): "set the words your product uses with customers",
    ("Design", "3"): "choose your colours, fonts, and styles",
    ("Design", "4"): "write the prompts that generate your screens",
    ("Design", "5"): "pin down the moment customers first see the value",
    ("Design", "6"): "plan a new customer's first few minutes",
    ("Design", "7"): "write the page or listing that wins customers",
    ("Develop", "0"): "move your app off the app-builder platform into your own project",
    ("Develop", "1"): "turn your plans into a build spec and a task list",
    ("Develop", "1b"): "set the tests your product's AI must pass",
    ("Develop", "2"): "turn on version history, so every change to your product is saved and can be undone",
    ("Develop", "3"): "your coding agent builds the product, task by task",
    ("Develop", "7"): "check signup, pricing, and checkout for where people drop off",
    ("Develop", "8"): "check the product is safe for your customers and their data",
    ("Develop", "9"): "put the product in front of real customers",
    ("Distribute", "1"): "choose the channels where you'll find customers",
    ("Distribute", "2"): "design small experiments to grow",
    ("Distribute", "3"): "run the experiments and log what happened",
    ("Distribute", "4"): "double down on what works",
}
CHALLENGE_NAMES = {"SHIP-IN-7.md": "Ship in 7", "SELL-IN-30.md": "Sell in 30"}
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


def shape_names():
    """{slug: display name} from the shapes table in shapes/SHAPES.md."""
    text = read(os.path.join(PRODUCTOS, "shapes", "SHAPES.md")) or ""
    return dict(re.findall(r"^\|\s*`([a-z-]+)`\s*\|\s*([^|]+?)\s*\|", text, re.M))


def valid_slugs():
    return list(shape_names())


def wired_block(repo):
    """True if the root CLAUDE.md or AGENTS.md carries the ProductOS block (its BEGIN marker on a line of its own)."""
    return any(re.search(r"^<!-- BEGIN PRODUCTOS -->", read(os.path.join(repo, f)) or "", re.M)
               for f in ("CLAUDE.md", "AGENTS.md"))


def gitignored(repo):
    """True if the project's .gitignore has a line covering productos/."""
    lines = (read(os.path.join(repo, ".gitignore")) or "").split("\n")
    return any(l.strip() in ("productos", "productos/", "/productos", "/productos/") for l in lines)


def has_git(repo):
    """True if the project folder is under version history (in this folder or one above it)."""
    here = os.path.abspath(repo)
    while True:
        if os.path.exists(os.path.join(here, ".git")):
            return True
        parent = os.path.dirname(here)
        if parent == here:
            return False
        here = parent


def step_number(label):
    return label.split(" ")[0]


def path_routes(text):
    """{phase: {"shape": slug or None, "rows": [{num, skill, mode, why}]}} from docs/PATH.md."""
    out = {}
    for heading, body in sections(text or "").items():
        m = re.match(r"(Define|Design|Develop|Distribute)\b(?:\s*[—–-]\s*`?([a-z-]+)`?)?", heading)
        if not m:
            continue
        rows = []
        for line in body.split("\n"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if not line.lstrip().startswith("|") or len(cells) < 3:
                continue
            num = re.match(r"\**(\d+[a-z]?)\b", cells[0])
            mode = re.match(r"\**([A-Za-z-]+)", cells[2])
            if num and mode and mode.group(1).lower() in PATH_MODES:
                rows.append({"num": num.group(1), "skill": ", ".join(re.findall(r"`([^`]+)`", cells[1])),
                             "mode": PATH_MODES[mode.group(1).lower()], "why": cells[3] if len(cells) > 3 else ""})
        out[m.group(1)] = {"shape": m.group(2), "rows": rows}
    return out


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

    # The route each phase orchestrator wrote down. A later phase's section written for another
    # shape is stale: ignore it until the orchestrator sets the route again.
    path = {}
    for phase, sec in path_routes(doc("PATH.md")).items():
        if phase != "Define" and sec["shape"] and primary and sec["shape"] != primary:
            result["notes"].append(f"docs/PATH.md's {phase} route was set for `{sec['shape']}`, not `{primary}` "
                                   f"— {phase.lower()}-phase sets it again.")
            continue
        path[phase] = sec
    result["path"] = sorted(path, key=PHASES.index)

    design = doc("DESIGN.md") or ""
    roadmap = doc("ROADMAP.md")
    refactor = doc("REFACTOR.md")
    tracker = doc("GROWTH-TRACKER.md") or ""
    wired = wired_block(repo)
    git = has_git(repo)
    result["setup"] = {"guidelines": wired, "gitignored": gitignored(repo), "version_history": git}

    def step_mode(phase, label, keywords):
        """(mode, path row or None): the route in docs/PATH.md wins over the shape file."""
        rows = path[phase]["rows"] if phase in path else []
        row = next((r for r in rows if r["num"] == step_number(label)), None)
        if row:
            return row["mode"], row
        route = route_for(routes, keywords)
        return (route[0] if route else ("Optional" if "optional" in label else "Full")), None

    def verify_setup():
        # Version history is needed when the route runs this step: the shape builds from code here
        mode = step_mode("Develop", "2 — Verify setup", ["verify setup", "setup"])[0]
        needed = mode in RUN_MODES
        history = "version history on" if git else (
            "version history off — goes on at the start of Develop" if needed
            else "version history off — not needed unless the product is built from code here")
        state = "done" if wired and (git or not needed) else "missing"
        return state, ("root guidelines wired" if wired else "root CLAUDE.md / AGENTS.md not wired") + "; " + history

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
    # the surfaces the member's Design route settled on win over the shape's defaults
    chosen = [r for r in path.get("Design", {}).get("rows", []) if r["num"] == "7"]
    chosen = [k for k in SURFACES if chosen and f"design-{k}" in chosen[0]["skill"]]
    wanted = chosen or wanted

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
        "2 — Verify setup": verify_setup,
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

    for i, (phase, label, skill, keywords) in enumerate(STEPS):
        state, evidence = checks[label]()
        mode, row = step_mode(phase, label, keywords)
        nums = [r["num"] for r in path[phase]["rows"]] if phase in path else []
        if row:
            skill = row["skill"] or skill
            if mode in RUN_MODES and state == "n/a":
                state = "missing"  # the route runs a step that is otherwise only for some members
            gating = mode in RUN_MODES
        else:
            gating = label not in NOT_GATING and mode not in ("Skip", "Optional", "Conditional")
        if mode == "Skip" and state != "done":
            state = "n/a"
        # path rows run in table order; steps the route doesn't list follow it
        order = (PHASES.index(phase), nums.index(step_number(label)) if row else len(nums) + i)
        result["steps"].append({"phase": phase, "step": label, "skill": skill, "status": state,
                                "shape_mode": mode, "route": "path" if row else "shape",
                                "gating": gating, "evidence": evidence, "_order": order})

    result["steps"].sort(key=lambda s: s.pop("_order"))
    nxt = next((s for s in result["steps"] if s["status"] in ("missing", "partial") and s["gating"]), None)
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
        result["notes"].append("docs/PLAN.md exists — it decides the order; product-refactor walks it.")
    if any(v == "open" for v in challenges.values()):
        result["notes"].append("A challenge is open — its check-in decides today's step.")
    return result


def render(r):
    lines = [f"ProductOS status — {r['repo']}",
             f"Shape: {r['shape']}  ({r['shape_source']})",
             f"Plan: {r['plan'] or 'none'}   Challenges: {', '.join(f'{k} {v}' for k, v in r['challenges'].items()) or 'none'}",
             f"Path: {', '.join(r['path']) + ' set in docs/PATH.md' if r['path'] else 'none set yet'}",
             f"Setup: root guidelines {'wired' if r['setup']['guidelines'] else 'NOT wired'} · "
             f"productos/ {'gitignored' if r['setup']['gitignored'] else 'NOT gitignored'} · "
             f"version history {'on' if r['setup']['version_history'] else 'off'}", ""]
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
    source = "your path" if n and n["route"] == "path" else "checklist order"
    lines.append(f"Next ({source}): {n['phase']} {n['step']} → {n['skill']}" if n else "Next: every gating step is done — keep running the Distribute loop.")
    lines += [f"Note: {x}" for x in r["notes"]]
    return "\n".join(lines)


def summary(r):
    """The plain-English version: where the member is, the next step in a sentence, what to say."""
    lines = []
    names = shape_names()
    if r["shape_source"] == "docs/DEFINE.md":
        lines.append(f"Product shape: {names.get(r['shape'], r['shape'])}.")
    progress = []
    for phase in PHASES:
        counted = [s for s in r["steps"] if s["phase"] == phase and s["status"] != "n/a"
                   and (s["gating"] or s["status"] == "done")]
        done = sum(s["status"] == "done" for s in counted)
        if counted and done == len(counted):
            progress.append(f"{phase} done")
        elif done:
            progress.append(f"{phase} {done} of {len(counted)} steps done")
        else:
            progress.append(f"{phase} not started")
    lines.append(" · ".join(progress))
    lines.append("")
    open_challenge = next((CHALLENGE_NAMES[k] for k, v in r["challenges"].items() if v == "open"), None)
    n = r["next"]
    if open_challenge:
        lines.append(f"You're in the {open_challenge} challenge, so today's check-in comes first.")
    elif r["plan"]:
        lines.append("Your programme plan sets the order of your steps, and your agent picks up the next one in it.")
    if n and not open_challenge and not r["plan"]:
        what = PLAIN.get((n["phase"], step_number(n["step"])), n["step"].split("— ")[-1].lower())
        lines.append(f"Next up, in {n['phase']}: {what}.")
    elif not n:
        lines.append("Every step is done. Keep the growth loop going: log your latest results and plan the next experiments.")
    lines.append('Say "continue" and your agent will take you through it. You can stop after any step.')
    return "\n".join(lines)


def uses_productos(repo):
    """True if this folder has ProductOS set up — the greeting stays silent everywhere else."""
    if os.path.isfile(os.path.join(repo, "ROUTING.md")) and os.path.isdir(os.path.join(repo, "shapes")):
        return False  # a checkout of ProductOS itself, not a product repo
    if os.path.isdir(os.path.join(repo, "productos")):
        return True
    if any(os.path.isfile(os.path.join(repo, "docs", f)) for f in ("DEFINE.md", "PLAN.md", "PATH.md")):
        return True
    return wired_block(repo)


def productos_root(start):
    """The project folder that uses ProductOS: `start` or the nearest folder above it, or None.

    Stops at the repository boundary (a folder with .git) and never climbs to the home folder or
    above — a general folder isn't a project folder.
    """
    here, home = os.path.abspath(start), os.path.abspath(os.path.expanduser("~"))
    while here != home and os.path.dirname(here) != here:
        if os.path.isfile(os.path.join(here, "ROUTING.md")) and os.path.isdir(os.path.join(here, "shapes")):
            return None  # inside a checkout of ProductOS itself
        if uses_productos(here):
            return here
        if os.path.exists(os.path.join(here, ".git")):
            return None
        here = os.path.dirname(here)
    return None


def greeting(r):
    """SessionStart hook output: the summary as context, with how to open the session."""
    context = ("ProductOS is set up in this repo. Where the member is right now:\n\n" + summary(r) + "\n\n"
               "If the member's first message doesn't already ask for something specific, open your reply "
               "with a short, plain-English welcome back (two or three lines): where they are and what saying "
               "\"continue\" will do next. Don't start a step until they say so. If they ask for something "
               "else, do that and skip the welcome.")
    return json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": context}})


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--repo", default=".", help="app repo root (default: current directory)")
    out = ap.add_mutually_exclusive_group()
    out.add_argument("--detail", action="store_true", help="print every step (what the orchestrators read)")
    out.add_argument("--json", action="store_true", help="print JSON instead of a table")
    out.add_argument("--greet", action="store_true", help="print the session-start hook's JSON; silent outside ProductOS repos")
    args = ap.parse_args()
    if not os.path.isdir(args.repo):
        sys.exit(f"Not a folder: {args.repo}")
    repo = args.repo
    if args.greet:
        repo = productos_root(repo)
        if repo is None:
            return
    r = status(repo)
    if args.json:
        print(json.dumps(r, indent=2))
    elif args.greet:
        print(greeting(r))
    else:
        print(render(r) if args.detail else summary(r))


if __name__ == "__main__":
    main()
