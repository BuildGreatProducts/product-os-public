---
name: develop-phase
description: >-
  Guides the member through the Develop phase for their product's shape — migrate if needed, PRD and
  roadmap (new build or existing codebase), evals for AI-native shapes, the build, design and
  conversion checks, the security audit, and go-live in the shape's form — reading docs/DEFINE.md,
  docs/DESIGN.md, the shape file, and docs/PLAN.md to set the route, then running each step's skill.
  Ends by handing off to distribute-phase. Use when the user says "start develop", "what's next in
  the build", or "walk me through develop". Not for building one feature — use build-loop.
---

# Develop phase

Walk the member from spec to a live product in the form their shape calls for, running each step's skill and checking its output. This skill routes; the step skills do the work.

Follow [ROUTING.md](../../ROUTING.md) — its *Three layers*, *Hard rules*, the Develop table, and *Running a step*. The Develop checklist (`productos/develop/DEVELOP-CHECKLIST.md`) is the source of truth for how each step runs.

## Workflow

### 1. Read the state and the needs

Run the status script from the app repo root: `python3 productos/scripts/status.py` (in a plugin install: `python3 <this skill's folder>/../../scripts/status.py --repo .`).

- **A challenge is open** → hand over to its check-in (`ship-in-7` / `sell-in-30`).
- **Define isn't done** → `define-phase`. **Design isn't done** → `design-phase`; the PRD needs the identity and, for anything with a UI or a listing, DESIGN.md tokens (Lite is enough where the shape says so).
- **`docs/PLAN.md` exists** → its Develop route, steps, and modes win.

### 2. Set the route

Read the primary shape (`docs/DEFINE.md` → `## Product Shape`) and the **Develop route** table plus *What the PRD must cover* and *Go live* in `productos/shapes/<slug>.md` (from this skill's folder, `../../shapes/<slug>.md`). Then pick the entry:

- **The app lives on a prompt-to-app platform** (Lovable, Bolt, v0, Base44, Replit…) → Step 0, `develop-migrate`, first.
- **Nothing built yet** → `develop-prd-roadmap` (new build).
- **A codebase exists** → `develop-prd-roadmap` in existing-codebase mode: the roadmap becomes the gap between the code and the target PRD.
- **The code already matches the spec** (the plan says so, or the member confirms after the PRD) → straight to the build loop.

Ask which coding agent builds it (Claude Code, Codex, or Cursor — `build-loop` works in all three). Show the route, one line per step with its shape mode, before starting.

### 3. Run each step

In order, skipping Skip steps:

1. **PRD & Roadmap** — `develop-prd-roadmap`. It covers the shape's PRD sections.
2. **Evals** — `develop-agent-evals`, when the shape route says Full (agent skills, plugins, MCP servers, chat assistants) or the product's core is an AI output. Evals come before the build so "done" has a bar.
3. **Verify setup** — the status script shows whether the root guidelines are wired; run `setup` if not.
4. **Build** — `develop-build` runs the whole roadmap, reviewing and committing at every phase boundary. It's a long run: the member can start it and come back. When they return, re-read the roadmap's status line.
5. **Design changes** — for screen shapes, `develop-design-review` before UI work is committed (`develop-design-better` while building it).
6. **Conversion review** — `develop-cro-audit` once the product is usable end to end and has a signup, pricing, or checkout surface.
7. **Security audit** — `develop-security-audit` for anything that ships code or holds customer data. Its Critical and High findings get fixed (hand the Fix plan to `build-loop`) before go-live.
8. **Go live** — `develop-golive`, in the shape's form (deploy, store submission, marketplace publish, package registry, booking page, storefront). Done when the shape's *Live means* bar passes as a real customer.

For each step: name it, check its needs, confirm in one line, run the skill, and confirm "Done when" with the status script.

### 4. After the MVP

Post-MVP features run through `build-loop` (`develop-feature-finder` when the member doesn't know what to build next); changes made outside the build skills get `develop-code-review` before commit; re-run the security audit after auth, payments, or data-access work.

### 5. Close the phase

When the product meets its *Live means* bar, tell the member what's live and where, then hand off: **next, `distribute-phase`** (Go-To-Market can start while the build runs, if the member wants).

## Rules

- Route, don't author: the step skills write the specs and the code.
- Security before go-live, always (ROUTING.md hard rule 5).
- Never improvise a missing PRD or roadmap — run the producer.

## Verify before handing off

- [ ] The roadmap status line reads Y/Y (or the plan routes straight to the build loop).
- [ ] Evals exist and pass where the shape requires them.
- [ ] The security audit's verdict is "Safe to launch", or every Critical and High finding is fixed.
- [ ] The shape's *Live means* bar passed as a real customer, and `docs/DEPLOY.md` records how.
