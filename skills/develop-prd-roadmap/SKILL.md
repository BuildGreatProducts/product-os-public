---
name: develop-prd-roadmap
description: >-
  Scopes the product in a structured interview (core loop, feature cuts, stack) and writes the two
  documents a coding agent builds from: docs/PRD.md, shaped by the product's shape, and
  docs/ROADMAP.md, a phased checkbox plan. In existing-codebase mode it baselines the repo, audits
  the code against the target PRD, takes keep-or-remove decisions, and writes a gap roadmap.
  Develop Step 1. Use when the user says "create my PRD", "scope my MVP", "plan the refactor", or
  "I'm ready to build". Not for leaving a prompt-to-app platform — use develop-migrate.
---

# Develop: PRD & Roadmap

This skill converts the member's Define and Design decisions into the two documents an AI coding agent (Claude Code, Codex, or Cursor — the tools `build-loop` supports) builds from: **`docs/PRD.md`** — the blueprint, specific enough to implement without clarifying questions — and **`docs/ROADMAP.md`** — the phased plan whose checkboxes the agent marks as it works.

It has two modes:

- **New build** — the MVP: the smallest slice of the promise that delivers the magic moment and can be built in 4–8 weeks. A **scoping interview** pins down what's in and out, then **generation** writes the PRD and roadmap from the guides in `productos/develop/guides/`.
- **Existing-codebase** — the repo already has a product. The PRD describes the target state, the code is audited against it, and the roadmap is a **gap roadmap** from today's code to that target.

The voice is a senior technical product lead who ships with AI coding agents: warm and direct, ruthless about cuts (every feature that doesn't serve the magic moment is a candidate for Out of Scope), precise on the page (real endpoint paths, field names, files — never hand-waving).

## Inputs

Read inputs from `docs/` and the guides from `productos/develop/guides/` at the app repo root.

**Required — stop if missing or thin:**

1. **`docs/DEFINE.md`** — `## Summary` and `## 1. Product Offer` (customer, pain, mechanism, guarantee, proof), `## 2. Customer Persona`, `## 3. Pricing Strategy`. If Summary, Offer, Persona, or Pricing are substantively empty, stop: run the Define skills first (`define-offer-builder` → `define-customer-persona` → `define-pricing`), or `define-from-code` for an existing product.
2. **The product shape** — `docs/DEFINE.md` → `## Product Shape` → `### Primary Shape` gives the slug; then read `productos/shapes/<slug>.md` (from this folder, `../../shapes/<slug>.md`) — only its `## Develop route` section: the route table, `### What the PRD must cover`, and `### Go live`. No Product Shape section (repos from before 2.0) → treat the product as `web-app` unless the codebase or member clearly says otherwise, and suggest running `define-product-shape`. Secondary shapes in `### Secondary Shapes` that the MVP ships get their own PRD coverage.
3. **`docs/DESIGN.md`** — the design system, opening with `## Product Identity` (read it for naming and copy context). The PRD references its tokens and component names, never redefines them. Shapes whose route runs the design system Lite (brand tokens only) need only that. If missing, ask whether to proceed — the PRD then notes that `design-design-system` must run before implementation — or pause and generate it.

**Supporting context — read whichever exist:**

4. **The rest of `docs/DEFINE.md`** — Guarantee and Proof (commitments the MVP must honour), the persona's name and verbatim language (for user stories), the pricing model, billing unit, plans, and launch price (decides whether Payment Integration exists and what it enforces), and `## 4. Business Strategy` when filled (the north star).
5. **`docs/MAGIC-MOMENT.md`** — the most important scoping input. The primary magic moment is the milestone the core phases must reach; its instrumentation note becomes a PRD requirement.
6. **`docs/ONBOARDING.md`** — every step in the flow is something the MVP must ship; the backbone of the PRD's UI/UX section (or its shape variant).
7. **The acquisition spec** — `docs/LANDING-PAGE.md`, `docs/APP-LISTING.md`, or `docs/MARKETPLACE-LISTING.md`. Every capability promised in the copy is a feature the MVP ships or the copy stops claiming. Harvest the promises.
8. **`docs/COPY.md`** — if present, features take its lexicon's canonical nouns, and its error and empty-state patterns become named requirements.
9. **`docs/PLAN.md`** — if present, it may say which mode applies and whether Develop Step 1b (Evals) is scheduled.

**Guides — read before the step that uses them:** `TECH-STACK-OPTIONS.md` (interview C), `PRD-GENERATION.md` (step 4), `ROADMAP-GENERATION.md` (step 5).

## Workflow

### 1. Check state and pick the mode

**Existing-codebase mode** applies when the repo already has product code (source beyond `productos/` and `docs/`) that wasn't built from the current `docs/ROADMAP.md`, or when `docs/PLAN.md` or the member says so. Confirm it in one line, then read [references/existing-codebase.md](references/existing-codebase.md) and follow it. Its baseline needs version history: not a git repository yet → run `setup` → *Version history* first. Read that file whenever this mode applies — including to resume, when `docs/ROADMAP.md` holds a `## Decisions (draft)` table from an interrupted review. It reuses steps 2, 4, and 5 below for their formats.

Otherwise this is a **new build**. The skill is resumable:

- **Neither file exists** → run from step 2.
- **`docs/PRD.md` exists but is incomplete** (missing numbered sections) → confirm the decisions recorded in its Overview and Out of Scope still hold, then resume at the first missing section.
- **PRD complete, `docs/ROADMAP.md` missing** → skip to step 5.
- **Both exist** and the member asked to regenerate or update → re-read the source docs, regenerate only what was asked, and if the PRD changes materially, offer to regenerate the roadmap too.

### 2. Read every input and apply the shape

Read all available inputs in full before asking anything. Build a private working picture:

- **The core loop hypothesis** — from the Offer's Mechanism and the primary magic moment: the single journey, end to end, that delivers the aha.
- **The candidate feature list** — every concrete capability mentioned anywhere: acquisition-copy promises, onboarding steps and permissions, mechanism elements, the guarantee, the magic moment's instrumentation. Deduplicate into 10–25 candidates.
- **The shape's PRD** — the variant for this shape in `PRD-GENERATION.md` § Shape variants (which standard sections change, are replaced, or are added) plus every item in the shape file's `### What the PRD must cover`. Each item becomes a candidate feature or a PRD section; none may be dropped silently.
- **Evals** — when Develop Step 1b is scheduled (Full for `agent-skill`, `agent-plugin`, `mcp-server`, `chat-assistant`, or any product whose core is an AI output; or `docs/PLAN.md` schedules it), plan for it now: the PRD's Success Criteria include passing `docs/EVALS.md`, and the roadmap gets eval tasks per `ROADMAP-GENERATION.md` § Shape notes. `develop-agent-evals` runs next, before the build, and writes the scenarios those tasks run.
- **The business model facts** — model, billing unit, plans, entry route, trial mechanics. These set the payments scope.
- **What's already decided** — never re-ask what the docs answer; state it back and confirm.

### 3. The scoping interview

Five sections, in order, one question at a time — never a wall of questions. For each: one sentence on why it matters, suggestions grounded in the docs (if you can't ground one, ask open), and let the member pick, modify, or write their own. Terse approvals count — move on.

**A. The core loop.** Present the hypothesis: *"Reading your magic moment and onboarding, the journey that has to work flawlessly is: [first open → X → Y → aha]. Does that match how you see it?"* Iterate until the member owns one sentence describing the journey from first use to magic moment. It anchors every cut.

**B. Feature scope.** Sort the candidates into three buckets, pushing toward the smallest viable cut:

- **P0 — launches with this.** Broken without it. Everything on the core loop is P0.
- **P1 — feels incomplete without it.** Ships if time allows, first thing after if not.
- **P2 — post-launch.** Goes in Out of Scope with a reason and a reconsider-when trigger.

Challenge every P0 off the core loop: *"Does the magic moment happen without this? Then it's P1."* Flag acquisition-copy promises that land in P2 — the copy and the MVP must not contradict each other. If the P0 list isn't honestly buildable in 4–8 weeks of AI-assisted development, keep cutting.

**C. Platform and stack.** Confirm the platform (the shape usually decides it), then work through the stack layers from `TECH-STACK-OPTIONS.md`. App shapes take the five core layers — frontend, backend, database, auth, payments; every other shape takes the layers its own section there lists (an MCP server: SDK, transport, hosting, auth; a productized service: booking, payments, intake, CRM, delivery automation). For each layer: 2–3 options adapted to this product, one recommendation with a reason tied to its needs, and the member decides. App defaults unless the product clearly needs otherwise: **Convex** (backend + database); **Stripe Managed Payments** for web (merchant of record from day one; **Polar** when the member wants a simpler developer-first setup) or **RevenueCat** for mobile. **No database**, **no auth**, or **no payments** are legitimate answers — say so. If the Pricing Strategy says revenue starts later, payments may be P2; confirm rather than assume. Record a one-line rationale per choice; once chosen, the stack is settled.

Then the **supporting services** — recommend the default, confirm in one line, move on: **analytics** (PostHog, or Mixpanel for focused funnel reporting — for non-screen shapes, whatever the platform reports plus usage logging), **transactional email** (Resend, or Loops for drips and newsletters too; skip only if nothing sends email), and **error tracking** (Sentry, for anything that runs code in production). These are foundation-phase setup tasks, listed in the stack table and dependencies so they're wired in early.

**D. Constraints and tooling.** Which coding agent builds this? Realistic timeline and weekly time budget? Hard constraints — service budget, existing accounts, compliance?

**E. Success criteria.** 3–5 measurable criteria for "MVP done", led by the magic moment (the first real user reaching it is the bar) and the north star when Business Strategy is filled — e.g. *"signup to magic moment under 2 minutes"*, *"all P0 features pass their acceptance criteria"*, *"every EVALS.md scenario passes on the mid and large models"*.

**Close the interview** by presenting the complete outline in one compact block — core loop, P0/P1/P2, platform, stack table with rationales, constraints, success criteria — and get explicit approval. This outline is the contract for everything generated next.

### 4. Generate `docs/PRD.md`

Read `PRD-GENERATION.md` in full and follow it — critical rules, all 14 section requirements, formats, and this shape's variant. The approved outline supplies scope, stack, and success criteria; `docs/DEFINE.md` and the Design docs supply the foundation.

Write in four chunks, presenting each for approval before moving on:

1. **§1–2** Overview + Technical Architecture — success criteria, stack table, rationales.
2. **§3–4** Data Model + API Specification (or their shape replacements) — implementation-ready.
3. **§5–8** User Stories + Functional + Non-Functional + UI/UX Requirements (or its shape replacement) — stories use the persona's name; FR priorities mirror P0/P1; UI/UX covers every onboarding step and MVP screen, referencing `docs/DESIGN.md` component names.
4. **§9–14** Auth + Payments + Edge Cases + Dependencies + Out of Scope + Open Questions — Auth and Payments specific to the chosen providers (or skipped per the guide); Out of Scope is the P2 list with reconsider-when triggers.

Append each chunk as it's approved — this is what makes the session resumable. Don't ask permission between sections within a chunk. If the member changes an earlier decision mid-generation, update the outline first, then flag which written sections it affects and offer to revise them.

### 5. Generate `docs/ROADMAP.md`

Read `ROADMAP-GENERATION.md` in full and follow it — the three-line checkbox format is non-negotiable, task IDs run sequentially across all phases, every phase ships something demoable, the magic moment is reachable by the end of the core phases, and the shape's notes adjust the phases.

1. **Phase outline first** — count, titles, goals, rough task counts, sized per the guide (simple: 2–3 phases; medium: 4–5; complex: 5–8). Get approval. If the task count and the member's weekly budget don't fit 4–8 weeks, revisit scope now.
2. **Full roadmap** — header and status line, build philosophy, every phase with goal, reference sections, and tasks, then the Agent Session Guide. Summarize (phases, task totals, where the magic moment lands) rather than reading every task back.

### 6. Verify before delivering

- [ ] Every PRD heading from the guide's Output Structure is present, replaced per the shape variant, or marked not applicable with a reason; every "What the PRD must cover" item from the shape file is covered.
- [ ] No design tokens are duplicated in the PRD; the stack table matches the interview choices exactly, with rationales.
- [ ] Every roadmap task uses the exact `- [ ] **TASK-NNN**` three-line format, IDs are sequential with no gaps, and the status line reads `0/{total} tasks complete`.
- [ ] Every task traces to a PRD requirement; every P0 feature has tasks; no P2 feature does; the magic moment is reachable by the end of the core phases.
- [ ] Each phase's reference sections use real heading text from the generated PRD.
- [ ] Acquisition-copy promises and PRD scope don't contradict each other (any flagged in interview B are in Open Questions).
- [ ] When Develop Step 1b is scheduled, the success criteria name `docs/EVALS.md` and the roadmap has eval tasks.
- [ ] The roadmap ends with the Agent Session Guide and its prompt templates.
- [ ] The member can say in one sentence what the MVP is and what it is not.

**Next step:** `develop-agent-evals` when Develop Step 1b is scheduled; then `develop-build` to build straight through the roadmap (or phase by phase with the Agent Session Guide prompts).
