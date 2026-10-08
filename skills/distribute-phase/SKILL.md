---
name: distribute-phase
description: >-
  Guides the member through the Distribute loop for their product's shape — go-to-market with the
  shape's native channel, growth experiments, logging results, the activation check, and scaling
  proven winners — reading docs/DEFINE.md, the shape file, docs/PLAN.md, and the growth tracker to
  say where the loop stands and run the next step's skill. Use when the user says "start
  distribute", "what's next in growth", "how do I get users now", or "walk me through distribute".
  Not for one specific step — run that step's skill directly.
---

# Distribute phase

Run the Distribute loop: pick channels, run experiments, log what happened, fix activation, scale what works, repeat. Every visit says where the loop stands and runs the next step. This skill routes; the step skills do the work.

Follow [ROUTING.md](../../ROUTING.md) — its *Hard rules*, the Distribute table, and *Running a step*. The Distribute checklist (`productos/distribute/DISTRIBUTE-CHECKLIST.md`) is the source of truth for how each step runs.

## Workflow

### 1. Read the state and the needs

Run the status script from the app repo root: `python3 productos/scripts/status.py` (in a plugin install: `python3 <this skill's folder>/../../scripts/status.py --repo .`).

- **A challenge is open** → hand over to its check-in (`ship-in-7` / `sell-in-30`).
- **Define isn't done** → `define-phase` (an existing product takes the fast-track — hours, not weeks).
- **The product isn't live yet** (the shape's *Live means* bar hasn't passed) → say so. Go-To-Market can be planned now and a waitlist can start, but experiments need a reachable product: point to `develop-phase` for go-live.
- **`docs/PLAN.md` exists** → its Distribute timing wins.

Read the primary shape and the **Distribute notes** in `productos/shapes/<slug>.md` (from this skill's folder, `../../shapes/<slug>.md`): the native channels, and what "activated" and "returned" mean for this shape.

### 2. Say where the loop stands

From the status script and the files: which channels `docs/GO-TO-MARKET.md` chose, which experiments `docs/GROWTH-EXPERIMENTS.md` has running and their pass bars and dates, how many results `docs/GROWTH-TRACKER.md` has logged, and whether any winner (Pass + double down) exists. One short paragraph.

### 3. Run the next step

- **No GTM** → `distribute-gtm-strategy`. One of the three channels should be the shape's native channel (its store, marketplace, or registry) unless there's a stated reason not to.
- **No experiments, or the cycle ended** → `distribute-growth-experiments` for the next set.
- **Experiments running** → the cycle (Step 3). Ask the member for the numbers since last time and log each result in `docs/GROWTH-TRACKER.md` in the worksheet's columns — the number against the pass threshold, Pass or Fail, the learning, and the decision (`double down`, `iterate`, or `kill`). Then name the experiment's next "Do this" step.
- **Winners exist** → the activation check first: `distribute-activation-retention-audit` if `docs/ACTIVATION-RETENTION-AUDIT.md` doesn't exist or has open P0s (fix them via `build-loop`), then `distribute-scale-automate`.
- **Scale plan in place** → keep the loop going: the next experiment cycle, or bring the next channel from GO-TO-MARKET.md online when a channel maxes out.

For each step: name it, check its needs, confirm in one line, run the skill, and confirm "Done when" with the status script.

## Rules

- Route, don't author: the step skills write the plans; the member runs the experiments.
- Never post, send, or spend on the member's behalf — draft it for them.
- Distribute never finishes: end every visit by naming what to do before the next one and when the next result is due.

## Verify before ending the visit

- [ ] The member knows where the loop stands: channels, experiments running, results due.
- [ ] Every result the member shared is logged in the tracker with a decision.
- [ ] Scaling only follows a Pass + double down winner and a clean activation check.
- [ ] The next action and its date are named.
