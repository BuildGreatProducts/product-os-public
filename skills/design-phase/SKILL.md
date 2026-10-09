---
name: design-phase
description: >-
  Guides the member through the Design phase for their product's shape — identity, UX writing,
  design system (full, lite, or from code), design prompts, magic moment, onboarding, and the
  acquisition surfaces the shape needs — reading docs/DEFINE.md, the shape file, and docs/PLAN.md to
  set the route, then running each step's skill and checking its output. Ends by handing off to
  develop-phase. Use when the user says "start design", "what's next in design", or "walk me through
  design". Not for one specific step — run that step's skill directly.
---

# Design phase

Walk the member through Design in the order and modes their product's shape calls for, running each step's skill and checking its output. This skill routes; the step skills do the work.

Follow [ROUTING.md](../../ROUTING.md) — its *Three layers*, *Modes*, the Design table, and *Running a step*. The Design checklist (`productos/design/DESIGN-CHECKLIST.md`) is the source of truth for how each step runs.

## Workflow

### 1. Read the state and the needs

Run the status script from the app repo root: `python3 productos/scripts/status.py --detail` (in a plugin install: `python3 <this skill's folder>/../../scripts/status.py --detail --repo .`).

- **A challenge is open** → hand over to its check-in (`ship-in-7` / `sell-in-30`).
- **Define isn't done** (Offer, Product Shape, Persona, Pricing) → stop and run `define-phase`. Design needs the shape above all.
- **`docs/PLAN.md` exists** → its Design steps, modes, and order win.
- **`docs/PATH.md` has a `## Design` section for the current primary shape** → the route is already set, with the member's choices: show it, say where they are on it, and go to step 3 at its first step that isn't done. A section for a different shape is stale — set the route again (step 2) and say why.

### 2. Set the route

Read the primary shape from `docs/DEFINE.md` → `## Product Shape`, then the **Design route** table in `productos/shapes/<slug>.md` (from this skill's folder, `../../shapes/<slug>.md`). Each secondary shape adds its acquisition surface from its own shape file. Show the member the route before starting — one line per step with its mode:

> Your Design phase as an `agent-skill`: Identity (full) → UX writing (adapted: skill names, descriptions, output formats) → Design system (lite: brand tokens for the listing) → Prompts (skip) → Magic moment (full) → Onboarding (adapted: install → first output) → Marketplace listing + landing page.

Settle the two choices that need the member:

- **Design System route** — an existing codebase with UI → `design-design-system-from-code`; otherwise `design-design-system`, which needs **one image or site the member loves**: ask for it now so it's ready by Step 3. A Lite shape runs `design-design-system` in Lite mode.
- **Acquisition surfaces** — exactly the ones the shape files name: `design-landing-page`, `design-app-listing` (App Store / Google Play), `design-marketplace-listing` (every other store, marketplace, registry, or directory).

Then write the route down in `docs/PATH.md` → `## Design — `<slug>``, in the format in ROUTING.md → *Your path*: one row per step in route order with its mode and why (Skips included, with their reason), the Design System row naming the skill that will run, the acquisition row naming every surface, and the italic line recording the design-system source.

### 3. Run each step

In route order, skipping Skip steps and offering Optional ones. When the member accepts or declines an Optional step, or a choice changes (a different design-system source, another surface), update that row in `docs/PATH.md`. For each: name it with its mode, check its needs, confirm in one line, run the skill — telling it the mode and the shape file's adaptation note for an Adapted or Lite step — then re-run the status script to confirm "Done when". Between steps, recap in one line what the next step will use: the identity's tone feeds COPY.md; the magic moment is the onboarding's destination; the onboarding's first output is the landing page's promise.

### 4. Close the phase

When every non-Skip step is done, list the files that now exist in `docs/` and give the paths. Then hand off: **next, `develop-phase`**. During the build, `docs/COPY.md` and `docs/DESIGN.md` bind every user-facing string and visual; `develop-design-better` and `develop-design-review` apply them to screen shapes.

## Rules

- Route, don't author: the step skills write the documents.
- A plan or shape Skip is a decision, not an omission — say it out loud with its reason.
- Never run onboarding before the magic moment, or an acquisition surface before the identity — ROUTING.md's needs order holds.

## Verify before handing off

- [ ] Every step in the shape's route is done, skipped with a stated reason, or declined (Optional).
- [ ] DESIGN.md has tokens (full or Lite) whenever any UI build or acquisition surface is coming.
- [ ] Every acquisition surface the shape files name exists in `docs/`.
- [ ] `docs/PATH.md` → `## Design` matches the route that ran.
- [ ] The member has the list of new files and their paths.
