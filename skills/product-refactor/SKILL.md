---
name: product-refactor
description: >-
  Runs an existing product's ProductOS programme across all four phases — the docs/PLAN.md that
  product-audit (or a coach) wrote — finding the next step that isn't done, running its skill in the
  plan's mode, checking the output, marking it done in the plan, and re-scoring the audit at each
  phase boundary. Use when the user says "continue my plan", "what's next in my plan", "run my
  audit plan", or after product-audit. Not for writing the plan — use product-audit; not for one
  phase only — use that phase's orchestrator.
---

# Product Refactor — run the plan

Work through `docs/PLAN.md` top to bottom, one step at a time, across phases. This skill routes; the step skills do the work. It's the cross-phase counterpart of the phase orchestrators: they walk one phase in checklist order, this walks the member's plan in its own order. (For a code-level refactor of an existing codebase, the plan schedules `develop-prd-roadmap` in existing-codebase mode — that's one of its steps, not this skill's job.)

Follow [ROUTING.md](../../ROUTING.md) — its *Modes*, *Hard rules*, step catalog, and *Running a step*.

## Workflow

### 1. Read the plan and the state

- **No `docs/PLAN.md`** → an existing product needs `product-audit` first; a new idea goes to `define-phase`.
- **A challenge is open** (`docs/SHIP-IN-7.md` or `docs/SELL-IN-30.md` with `Status: Open`) → its check-in owns today's step; hand over.
- Run `python3 productos/scripts/status.py` (in a plugin install: `<this skill's folder>/../../scripts/status.py --repo .`) and read `docs/PLAN.md` → **Your Programme**.

### 2. Find the next step

The first step in **Your Programme** that has no *Done* line and isn't satisfied by the status script's "Done when". Skip steps marked Already-done; never run a step listed under *Not scheduled*. If a step's needs are missing, the plan has a gap: run the producer and annotate why.

### 3. Run it

Name the step, its mode, and the plan's reason for it; confirm in one line; then run the skill. **Fast-track** runs the fast-track producer ROUTING.md names (e.g. `define-from-code` → `define-offer-review`). A step that opens a challenge (`ship-in-7`, `sell-in-30`) hands over to it until the challenge closes. Long-running steps (`develop-build`) can be started and resumed — re-read the plan and status when the member returns.

### 4. Mark it done

Confirm the step's "Done when" with the status script, then add one line under the step in `docs/PLAN.md`:

`*Done [YYYY-MM-DD] — [evidence: the file, verdict, or result].*`

Annotate, never recompose: don't reorder, add, or delete steps.

### 5. Re-score at phase boundaries

When the last scheduled step of a phase is done, re-score that phase with the scorecard in `productos/skills/product-audit/references/scorecard.md` (from this skill's folder, `../product-audit/references/scorecard.md`) and add a row to `docs/PRODUCT-AUDIT.md` → **Re-scores**: date, phase, before → after, what moved it. Tell the member in two lines.

### 6. When the plan drifts

Reality changes: a step no longer applies, a blocker appears, the shape's Sequence trigger fires. For a plan composed by `product-audit`, re-run `product-audit` to replan (it keeps finished steps as Already-done and bumps the revision). For a coach's plan, annotate the step with the problem and tell the member to take it to their coach — never rewrite a coach's plan.

### 7. When the plan is done

Every scheduled step has a *Done* line → the Distribute loop continues with `distribute-phase`. Say so, with the audit's before/after scores.

## Rules

- The plan's order wins over checklist order (ROUTING.md layer 1), but never over the hard rules — flag a plan that breaks one instead of following it.
- Route, don't author: the step skills write the documents and the code.
- One step at a time; the member can stop after any step.

## Verify after each step

- [ ] The step's "Done when" passes in the status script.
- [ ] Its *Done* line is in `docs/PLAN.md`, with evidence.
- [ ] At a phase boundary, `docs/PRODUCT-AUDIT.md` has a re-score row.
- [ ] The member knows the next step.
