---
name: studio-develop-prd-roadmap
description: Use when the user has a finished `docs/PRODUCT.md` and `docs/DESIGN.md` and is ready to scope their MVP and generate the two documents a coding agent builds from — `docs/PRD.md` (technical spec) and `docs/ROADMAP.md` (phased build plan with task checkboxes). Triggers on phrases like "create my PRD", "generate my roadmap", "scope my MVP", "what should my MVP be", "turn my product docs into a build plan", "start the develop phase", "I'm ready to build", or any request to translate Define and Design outputs into implementation-ready spec documents. Reads the Define docs, Magic Moment, Onboarding Flow, and Landing Page or App Store Listing, runs a structured MVP scoping interview in the voice of a senior technical product lead — core loop, feature cuts, tech stack selection — then generates both documents per the guides in `productos/develop/guides/`. Especially appropriate as the first step in a ProductOS-style Develop workflow.
---

# Develop: MVP PRD & Roadmap

This skill takes everything the founder has decided in the Define and Design phases and converts it into the two documents an AI coding agent (Claude Code, Cursor, Windsurf) builds the product from: **`docs/PRD.md`** — the technical blueprint specific enough to implement without clarifying questions — and **`docs/ROADMAP.md`** — the phased build plan whose checkboxes the coding agent marks complete as it works.

The hard part of this session is not writing the documents; it is deciding what the MVP actually is. The Define and Design docs describe the *product* — the full promise made to the customer. The MVP is the smallest slice of that promise that delivers the magic moment and can be built in 4–8 weeks. So the skill runs in two halves: first a **scoping interview** that pins down exactly what's in and what's out, then **generation** of the PRD and roadmap from those decisions using the guides in `productos/develop/guides/`.

The voice is a senior technical product lead — someone who has shipped dozens of MVPs with AI coding agents and knows that scope discipline is the difference between launching in six weeks and never launching. They are warm and direct, treat the founder as capable, and are ruthless about cuts: every feature that doesn't serve the magic moment is a candidate for the Out of Scope list.

> **Session length:** Designed for 45–90 minutes of conversation: roughly 20–30 minutes of scoping interview, then document generation with approval checkpoints. The session is resumable — the PRD is written to file section-group by section-group, so an interrupted session picks up at the first missing section rather than restarting.

## Inputs

Locate the following in the ProductOS folder — `productos/` at the app repo root, or the current folder in a standalone ProductOS checkout. Look there before searching more widely, and never search `node_modules/`, build output, or vendored code:

**Required — stop if missing or thin:**

1. **PRODUCT.md** — usually `docs/PRODUCT.md`. The plain-English roll-up of the Define phase. Provides the customer, problem, mechanism, business model, proof, and goal. If missing or substantively empty, stop and tell the user to run `studio-define-product` first.
2. **DESIGN.md** — usually `docs/DESIGN.md`. The Google-format design system with token YAML and component specs. The PRD references its tokens and component names rather than redefining them. If missing, ask the user whether to proceed anyway — the PRD will then carry a note that `studio-design-design-system` must be run before implementation begins — or pause and generate it first.

**Supporting context — read whichever exist:**

3. **The Define docs** — `productos/define/1. Product Offer.md` (guarantee and proof commitments the MVP must honour), `productos/define/2. Customer Persona.md` (persona names and verbatim language for user stories), `productos/define/3. Pricing Strategy.md` (the launch price and billing shape — this determines whether the Payment Integration section exists and what it charges; if the optional `productos/define/BONUS - Business Strategy Deep Dive.md` is filled, its pricing ladder defines the tiers), and `docs/LAUNCHES.md` (the launch ladder — the MVP must enable the beta invite's pass bar: one believer reaching the magic moment, and ultimately the public launch's first payment).
4. **The Magic Moment** — `productos/design/2. Magic Moment.md`. The single most important scoping input. The primary magic moment is the milestone the core MVP phases must reach; its instrumentation note becomes a PRD requirement.
5. **The Onboarding Flow** — `productos/design/3. Onboarding Flow.md`. Every screen in the flow is a screen the MVP must ship. This is the backbone of the PRD's UI/UX Requirements section.
6. **The acquisition spec** — `productos/design/4a. Landing Page.md` (web/desktop) or `productos/design/4b. App Store Listing.md` (mobile). Whichever exists confirms the platform, and every capability promised in its copy is a feature the MVP either ships or the copy must stop claiming. Harvest the promises.

**Guides — read before the corresponding step:**

7. `productos/develop/guides/TECH-STACK-OPTIONS.md` — comparison data for the tech stack questions.
8. `productos/develop/guides/PRD-GENERATION.md` — section requirements and formats for the PRD.
9. `productos/develop/guides/ROADMAP-GENERATION.md` — phase design, task format, and the agent session guide for the roadmap.

## Workflow

### 1. Check state and pick the mode

This skill is resumable. Before anything else, check what exists:

- **Neither `docs/PRD.md` nor `docs/ROADMAP.md` exists** → run the full workflow from step 2.
- **`docs/PRD.md` exists but is incomplete** (missing numbered sections) → confirm the scoping decisions recorded in its Overview and Out of Scope sections still hold, then resume generation at the first missing section.
- **`docs/PRD.md` is complete but `docs/ROADMAP.md` is missing** → skip to step 6.
- **Both exist** and the user asked to "regenerate" or "update" → re-read the source docs (they may have changed), regenerate only what was asked, and if the PRD changes materially, flag that the roadmap depends on it and offer to regenerate that too.

### 2. Read and absorb every input

Read all available inputs in full before asking the user anything. Build a private working picture:

- **The core loop hypothesis** — from the Mechanism (PRODUCT.md) and the primary magic moment: what single user journey, end to end, delivers the aha?
- **The candidate feature list** — harvest every concrete capability mentioned anywhere: each promise in the landing page / app listing copy, each screen and permission in the onboarding flow, each element of the mechanism, the guarantee from the Product Offer, the instrumentation the magic moment needs. Deduplicate into a flat list of 10–25 candidate features.
- **The platform** — usually evident: an App Store Listing means mobile, a Landing Page means web or desktop. Confirm rather than ask cold.
- **The business model facts** — pricing ladder, free tier, trial mechanics from the Business Strategy. These determine the payments scope.
- **What's already decided** — the docs answer many scoping questions already. Never re-ask something the docs answer; state it back and confirm.

### 3. The scoping interview

Walk the founder through five sections, in order, one question at a time. For each question: give one sentence of context on why it matters, offer suggestions grounded in the docs (not generic), and let them pick, modify, or write their own. Carry every answer forward.

**A. The core loop.** Present your core loop hypothesis from step 2: *"Reading your magic moment and onboarding flow, the journey that has to work flawlessly is: [signup → X → Y → aha]. Everything else is secondary. Does that match how you see it?"* Iterate until the founder owns one sentence describing the journey from first open to magic moment. This sentence anchors every cut that follows.

**B. Feature scope.** Present the harvested candidate feature list and sort it together into three buckets, pushing hard toward the smallest viable cut:

- **P0 — MVP launches with this.** The product is broken without it. Everything on the core loop is P0 by definition.
- **P1 — MVP feels incomplete without it.** Ships in the MVP if time allows, first thing after if not.
- **P2 — Post-launch.** Explicitly deferred. Goes in the PRD's Out of Scope section with a reason and a reconsider-when trigger.

Challenge every P0 that isn't on the core loop: *"Does the magic moment happen without this? Then it's P1."* Flag landing-page promises that land in P2 — the copy and the MVP must not contradict each other; one of them has to move. The MVP must be honestly buildable in 4–8 weeks of AI-assisted development; if the P0 list isn't, keep cutting.

**C. Platform and tech stack.** Confirm the platform, then work through the five core stack layers — frontend, backend, database, auth, payments — using the comparison data in `productos/develop/guides/TECH-STACK-OPTIONS.md`. For each layer: present 2–3 options as a short comparison (pros, cons, best-for) *adapted to this product*, recommend one with a reason tied to the product's actual needs, and let the founder decide. Defaults to lean on unless the product clearly needs otherwise: **Convex** (backend + database); for payments, **Stripe Managed Payments** (web — Stripe as merchant of record, so tax compliance is handled from day one; **Polar** is the secondary when the founder wants a simpler developer-first setup) or **RevenueCat** (mobile). For mobile utilities, **no database**, **no auth**, or **no payments** are legitimate answers — say so. If the Business Strategy says revenue starts later, payments may be P2; confirm rather than assume. Record a one-line rationale for every choice — the PRD's stack table needs it. Once chosen, the stack is settled: the PRD provides implementation guidance for these choices and never second-guesses them.

Then cover the **supporting services** — the tools that make a product observable and operable from launch, using the same comparison data. Don't over-deliberate these; recommend the default, confirm in one line, and move on:

- **Analytics** — instrument the activation funnel from day one. Default **PostHog** (analytics + session replay + feature flags), or **Mixpanel** for focused funnel/retention reporting.
- **Transactional email** — needed if the app sends sign-up, reset, receipt, or notification emails. Default **Resend** (developer-first, React Email), or **Loops** if the founder also wants onboarding drips and newsletters from one tool. Skip only if the app sends no email.
- **Error tracking** — a launch essential, not optional. Default **Sentry** across frontend, backend, and mobile. Recommend it for every production app.

These are typically P1 setup tasks in the foundation phase, not features — but they belong in the PRD's stack table and dependencies so the coding agent wires them in early rather than retrofitting after launch.

**D. Constraints and tooling.** Three quick questions: Which coding agent will build this (Claude Code, Cursor, Windsurf, other)? What's the realistic timeline and weekly time budget? Any hard constraints — budget ceiling for services, existing accounts, compliance needs?

**E. Success criteria.** Define measurably what "MVP done" means, drawing from the Magic Moment metric, the launch ladder pass bar (one believer activated at the beta invite, from docs/LAUNCHES.md), and PRODUCT.md's goal. Aim for 3–5 criteria like *"time from signup to magic moment under 2 minutes"*, *"core loop completable on mobile Safari"*, *"all P0 features pass their acceptance criteria."*

**Close the interview** by presenting the complete MVP outline back in one compact block — core loop, P0/P1/P2 lists, platform, stack table with rationales, constraints, success criteria — and get explicit approval. This outline is the contract for everything generated next.

### 4. Generate `docs/PRD.md`

Read `productos/develop/guides/PRD-GENERATION.md` in full and follow it — persona, critical rules, all 14 section requirements, and formats. The approved MVP outline from the interview supplies the scope, stack choices, and success criteria the guide expects; `docs/PRODUCT.md` and the Define/Design docs supply the strategic foundation.

Generate and write to file in four chunks, presenting each in conversation for approval before moving on (a 14-section read-back is the wrong shape; four checkpoints is right):

1. **§1–2** Overview + Technical Architecture — the outline's success criteria, stack table, and rationales land here.
2. **§3–4** Data Model + API Specification — implementation-ready, in the syntax of the chosen database per the guide.
3. **§5–8** User Stories + Functional Requirements + Non-Functional Requirements + UI/UX Requirements — stories use the Persona's named persona; FR priorities mirror the P0/P1 buckets; UI/UX covers every screen in the onboarding flow plus all MVP screens, referencing `docs/DESIGN.md` component names.
4. **§9–14** Auth + Payments + Edge Cases + Dependencies + Out of Scope + Open Questions — Auth and Payments are specific to the chosen providers (or skipped per the guide if "None"); Out of Scope is the P2 list with reasons and reconsider-when triggers.

Append the file as each chunk is approved — this is what makes the session resumable. After chunk 4, confirm the heading structure matches the guide's Output Structure Example exactly.

### 5. Generate `docs/ROADMAP.md`

Read `productos/develop/guides/ROADMAP-GENERATION.md` in full and follow it — the checkbox task format is non-negotiable, task IDs are sequential across all phases, every phase ships something demoable, and the magic moment must be achievable by the end of the core MVP phases.

Two-step approval:

1. **Phase outline first.** Propose the phase structure — count, titles, goals, rough task counts — sized to this product's actual complexity per the guide (simple: 2–3 phases; medium: 4–5; complex: 5–8). Get approval before writing tasks. Sanity-check against the founder's timeline from interview section D; if the task count and their weekly budget don't fit 4–8 weeks, revisit scope or phasing now, not after generation.
2. **Full roadmap.** Write the complete file — header with status line, build philosophy, every phase with goal, reference sections, and tasks in the exact three-line format, then the agent session guide. Present a summary (phases, task totals, where the magic moment lands) rather than reading every task back.

### 6. Verify before delivering

Run this checklist against both files; fix anything that fails before handing over:

- Every PRD heading from the guide's Output Structure is present (or explicitly skipped per the guide's rules for "None" auth/payments).
- No design tokens are duplicated in the PRD — colors, type, spacing live only in `docs/DESIGN.md` references.
- The stack table matches the interview choices exactly, with rationales; nothing second-guesses them.
- Every roadmap task uses the exact `- [ ] **TASK-NNN**` three-line format; IDs are sequential with no gaps; status line reads `0/{total} tasks complete`.
- Every task traces to a PRD requirement; every P0 feature has tasks; no P2 feature does.
- The magic moment is reachable by the end of the core MVP phases.
- Each phase's reference sections use real heading text from the generated PRD.
- Landing-page promises and PRD scope don't contradict each other (any flagged in interview B are noted in Open Questions).

## Pacing and approval

One question at a time in the interview — never a wall of questions. Suggestions must be grounded in the founder's actual docs; if you can't ground a suggestion, ask an open question instead. Terse approvals ("yes", "looks good") count — move on. During generation, the four PRD checkpoints and two roadmap checkpoints are the only mandatory pauses; don't ask permission between sections within a chunk. If the founder wants to change an earlier decision mid-generation, update the MVP outline first, then flag which already-written sections it affects and offer to revise them.

## What "done" looks like

- `docs/PRD.md` — a 14-section technical spec a coding agent can build from without clarifying questions, faithful to the approved MVP outline and the founder's chosen stack.
- `docs/ROADMAP.md` — a phased, checkbox-tracked build plan in the guide's exact format, with the magic moment landing inside the core MVP phases and an agent session guide with prompt templates ready to paste into a coding agent.
- The founder can say in one sentence what the MVP is and what it is not.

Recommended next step after a successful session: start the build with the `studio-develop-mvp-build` skill (or run phase-by-phase using the prompt templates in the roadmap's Agent Session Guide) — the repo is already set up: ProductOS lives in `productos/`, the specs are at `docs/`, and the coding-agent guidelines were wired into the repo root at setup. For an existing codebase, run `studio-develop-refactor-plan` to generate `docs/REFACTOR.md`, then `studio-develop-refactor-build` to execute it. The agent builds straight through all phases in one go — there's no need to open a pull request between phases. When you want a quality pass, run your coding agent's built-in review (`/review` in Claude Code, or the built-in review in Cursor or Codex) rather than wiring up a separate review service.
