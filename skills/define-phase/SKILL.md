---
name: define-phase
description: >-
  Guides the member through the whole Define phase, one step at a time — idea if needed, product
  offer, product shape, customer persona, pricing, and the optional business strategy — reading
  docs/DEFINE.md and docs/PLAN.md to name the next step, running that step's skill, and checking its
  output before moving on. Ends by handing off to design-phase. Use when the user says "start
  define", "walk me through define", "what's next in define", or "help me define my product". Not
  for one specific step — run that step's skill directly.
---

# Define phase

Walk the member through Define in order, running each step's skill and checking its output, until `docs/DEFINE.md` has its Summary, Offer, Product Shape, Persona, and Pricing filled. This skill routes; the step skills do the work and write the document.

Follow [ROUTING.md](../../ROUTING.md) — its *Three layers*, *Hard rules*, the Define table, and *Running a step*. The Define checklist (`productos/define/DEFINE-CHECKLIST.md`) is the source of truth for how each step runs.

## Workflow

### 1. Read the state

Run the status script from the app repo root: `python3 productos/scripts/status.py --detail` (in a plugin install: `python3 <this skill's folder>/../../scripts/status.py --detail --repo .`). Then:

- **A challenge is open** (`docs/SHIP-IN-7.md` or `docs/SELL-IN-30.md` with `Status: Open`) → hand over to its check-in (`ship-in-7` / `sell-in-30`); it decides today's step.
- **`docs/PLAN.md` exists** → its Define steps, modes, and order win. Fast-track steps run their fast-track producer.
- **`docs/PATH.md` has a `## Define` section** → the route is already set: say where the member is on it and go to step 3 at its first step that isn't done.

### 2. Pick the entry route

If the member already chose where to start — at setup's or `continue`'s question — take that route without asking again.

- **No idea yet** → `define-idea-finder` (Step 0), which hands into the offer.
- **An idea, no product** → the full route: `define-offer-builder` → `define-product-shape` → `define-customer-persona` → `define-pricing`. Offer `define-offer-review` once after the offer if the member wants a critique pass.
- **An existing product** (app code, a live URL, a store listing) and no DEFINE.md → the fast-track: `define-from-code` → `define-offer-review` (not optional here) → `define-product-shape` (a short session confirming the shape the product already has). The persona and pricing drafts from `define-from-code` count as filled; offer `define-customer-persona` and `define-pricing` as optional sharpening.
- **Resuming** → the first step the status script shows as missing or partial.

Say which route and why in one line, and list the steps ahead. Then write it down in `docs/PATH.md` → `## Define`, in the format in ROUTING.md → *Your path*: the italic line names the entry route (new idea, idea first, or fast-track from code); one row per step in the order it runs — Step 0 only when the idea finder runs, Business Strategy as Optional unless the plan schedules it.

### 3. Run each step

For each step: name it, check its needs, confirm in one line, run the skill, then re-run the status script to confirm the step's "Done when" (ROUTING.md). Between steps, recap in one line what the step added to DEFINE.md and what the next step uses from it — the shape feeds pricing; the persona feeds pricing's who-pays.

Never skip **Product Shape**: every later phase routes on it. **Business Strategy** (Step 4) is optional — offer it only when the plan schedules it or money questions are live (paid acquisition, investors, margins). When the member accepts or declines it — or any other decision on the route changes — update that row in `docs/PATH.md`.

### 4. Close the phase

When Steps 1, 1b, 2, and 3 are done, read DEFINE.md and give the member a five-line summary: the one-sentence offer, the shape and what "live" means for it, the persona in one line, and the price line. Give them the file path, then hand off: **next, `design-phase`**. This is the moment to offer **Ship in 7** in one line — seven sessions to a live product, with a daily check-in — as the alternative for a member who wants a deadline; run `ship-in-7` if they take it.

## Rules

- Route, don't author: never write DEFINE.md content yourself — the step skills own their sections.
- Never run a step whose needs are missing; run the producer first (ROUTING.md hard rule 4).
- The member can stop after any step; the status script picks up where they left off.

## Verify before handing off

- [ ] Status script shows Define 1, 1b, 2, and 3 as done.
- [ ] Primary Shape names a valid slug — the Design route depends on it.
- [ ] On the fast-track, `define-offer-review` ran.
- [ ] `docs/PATH.md` → `## Define` matches the route that ran.
- [ ] The member has the five-line summary and the path to `docs/DEFINE.md`.
