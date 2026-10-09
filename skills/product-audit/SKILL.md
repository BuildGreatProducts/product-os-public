---
name: product-audit
description: >-
  Audits an existing product — codebase, docs, live product, listings — across Define, Design,
  Develop, and Distribute, scores each phase with cited evidence, names its stage and shape, and
  composes a ProductOS programme for it: docs/PRODUCT-AUDIT.md (the scorecard) and docs/PLAN.md (every
  step Full, Fast-track, Already-done, or Skip, in working order). Use when the user says "audit my
  product", "where is my product weak", "make me a plan for my existing app", or after setup on an
  existing project. Not for a new idea — use define-phase; to run the plan, use product-refactor.
---

# Product Audit

Read everything that exists, score where the product is strong and weak, and compose the programme that fixes the weakest load-bearing links first. The output is a plan in the same format a ProductOS coach writes, so setup, the orchestrators, and `product-refactor` all run it the same way. A coach-composed plan is more tailored than this one; this skill never overwrites one.

Follow [ROUTING.md](../../ROUTING.md): its modes, hard rules, and step catalog are the rulebook the plan is composed from.

## Workflow

### 1. Check the install

Confirm ProductOS is set up (root guidelines wired, `productos/` gitignored); if not, run `setup` first. If `docs/PLAN.md` already exists and came from a coach (its header doesn't say "product-audit"), don't replace it: run the audit, write `docs/PRODUCT-AUDIT.md` only, and suggest the member shares it with their coach.

### 2. Inventory the evidence

Run `python3 productos/scripts/status.py --detail` (in a plugin install: `<this skill's folder>/../../scripts/status.py --detail --repo .`) for the docs picture. Then read the product itself, each item with a one-phrase assessment:

- **Code** — stack, size, structure, tests and whether they pass, deploy config, payments, analytics, error tracking, obvious security smells (committed secrets, open database rules).
- **Docs** — every `docs/` file and the README; how current each is.
- **Live product** — the URL, store listing, or marketplace page, if one exists (a fetch or browser tool if connected; otherwise ask the member for a screenshot or the copy).
- **Platform** — whether the app lives on a prompt-to-app platform (Lovable, Bolt, v0, Base44, Replit…).

### 3. Settle the shape

If `## Product Shape` is missing from `docs/DEFINE.md`, the plan can't be routed: run `define-product-shape` as a short fast-track session (it reads what the product already is). If DEFINE.md doesn't exist at all, note it — the plan's first block will be the Define fast-track — and confirm the shape with the member from the evidence, recording it in the audit.

### 4. Ask only what the evidence can't answer

At most five questions, in one message: users and revenue (numbers), the goal for the next 90 days, hours per week, which coding agent they build with, and any deadline or constraint.

### 5. Score and stage

Score each phase against [references/scorecard.md](references/scorecard.md) — every score cites its evidence, and a missing artefact scores 0, not a guess. Name the **stage**: idea → prototype → live, no users → users, no revenue → revenue. The stage decides where the leverage is.

### 6. Compose the plan

Walk ROUTING.md's step catalog phase by phase, filtered by the shape file's routes (`productos/shapes/<slug>.md`; skip what the shape skips). Give every remaining step a plan mode — **Full**, **Fast-track**, **Already-done** (with the evidence), or **Skip** (with a reason the catalog allows) — then order the steps:

1. The hard rules first: Define is never skipped (an existing product takes the fast-track), Product Shape before Design, needs before the steps that read them, security before go-live, Distribute always.
2. Then by leverage for the stage, using [references/scorecard.md](references/scorecard.md) → *Leverage by stage*: a prototype that isn't live puts go-live early (Ship in 7 can be its first block); a live product with no users starts Go-To-Market in week one, in parallel with the Define fast-track; users without revenue puts pricing, checkout, and activation first.

Lint the draft against ROUTING.md's hard rules and fix violations by scheduling the fast-track producer, never by un-skipping half a phase.

### 7. Review with the member

Present the scorecard in five lines (one per phase plus the stage), then the plan's first five steps with their reasons. Fold in their corrections; hold the hard rules.

### 8. Write both files

- `docs/PRODUCT-AUDIT.md` from [templates/product-audit.md](templates/product-audit.md).
- `docs/PLAN.md` from [templates/plan.md](templates/plan.md) — unless a coach's plan exists (step 1). Replacing an earlier product-audit plan: keep completed steps as Already-done, bump the revision, and show the diff before writing.

Give the member both paths and their literal first action: **run `product-refactor`** to work through the plan (or the challenge the plan opens with).

## Verify before delivering

- [ ] Every score cites evidence; nothing scored from assumption.
- [ ] The shape is a valid slug, confirmed with the member.
- [ ] Every scheduled step's needs come from an earlier step or are Already-done.
- [ ] Every Skip has a catalog-legal reason; Define and Distribute are scheduled.
- [ ] A coach's plan was not overwritten.
- [ ] The plan's first step is something the member can start today.
