---
name: develop-prd-roadmap
description: >-
  Scopes the MVP in a structured interview (core loop, feature cuts, tech stack) and writes the two
  documents a coding agent builds from: docs/PRD.md (technical spec) and docs/ROADMAP.md (phased
  checkbox plan). Develop phase Step 1. Use when the user says "create my PRD", "scope my MVP", or
  "I'm ready to build". Requires docs/DEFINE.md and docs/DESIGN.md; reads the magic moment,
  onboarding, and landing page or app listing. Not for an existing codebase — use
  develop-refactor-plan.
---

# Develop: MVP PRD & Roadmap

This skill takes everything the member has decided in the Define and Design phases and converts it into the two documents an AI coding agent (Claude Code, Codex, or Cursor — the tools `build-loop` supports) builds the product from: **`docs/PRD.md`** — the technical blueprint specific enough to implement without clarifying questions — and **`docs/ROADMAP.md`** — the phased build plan whose checkboxes the coding agent marks complete as it works.

The MVP is the smallest slice of the product's promise that delivers the magic moment and can be built in 4–8 weeks. The skill runs in two halves: a **scoping interview** that pins down exactly what's in and what's out, then **generation** of the PRD and roadmap from those decisions using the guides in `productos/develop/guides/`.

The voice is a senior technical product lead who ships MVPs with AI coding agents:

- **Warm and direct** — treats the member as capable.
- **Ruthless about cuts** — every feature that doesn't serve the magic moment is a candidate for Out of Scope.
- **Precise on the page** — concrete endpoint paths, real field names, specific files; the documents never hand-wave.

## Inputs

Read inputs from `docs/` and the guides from `productos/develop/guides/` at the app repo root:

**Required — stop if missing or thin:**

1. **DEFINE.md** — `docs/DEFINE.md`. The Define phase in one file. Its `## Summary` and `## 1. Product Offer` provide the customer, pain, mechanism, guarantee, and proof; `## 2. Customer Persona` and `## 3. Pricing Strategy` are read in step 3 below. If missing, or if Summary, Offer, Persona and Pricing are substantively empty, stop and tell the member to run the Define skills first (`define-offer-builder` → `define-customer-persona` → `define-pricing`), or `define-from-code` for an existing product.
2. **DESIGN.md** — usually `docs/DESIGN.md`. The Google-format design system with token YAML and component specs, opening with the `## Product Identity` section (name, worldview, tone of voice, visual style) — read the identity for naming and copy context. The PRD references its tokens and component names rather than redefining them. If missing, ask the member whether to proceed anyway — the PRD will then carry a note that `design-design-system` must be run before implementation begins — or pause and generate it first.

**Supporting context — read whichever exist:**

3. **The rest of DEFINE.md** — Offer → Guarantee and Proof (commitments the MVP must honour), `## 2. Customer Persona` (persona names and verbatim language for user stories), `## 3. Pricing Strategy` (who pays, the pricing model, billing unit, plans, entry route, and launch price — this determines whether the Payment Integration section exists, what it charges, and which plans and limits the MVP must enforce), and `## 4. Business Strategy` when filled (the north star the success criteria can point at).
4. **The Magic Moment** — `docs/MAGIC-MOMENT.md`. The single most important scoping input. The primary magic moment is the milestone the core MVP phases must reach; its instrumentation note becomes a PRD requirement.
5. **The Onboarding Flow** — `docs/ONBOARDING.md`. Every screen in the flow is a screen the MVP must ship. This is the backbone of the PRD's UI/UX Requirements section.
6. **The acquisition spec** — `docs/LANDING-PAGE.md` (web/desktop) or `docs/APP-LISTING.md` (mobile). Whichever exists confirms the platform, and every capability promised in its copy is a feature the MVP either ships or the copy must stop claiming. Harvest the promises.
7. **COPY.md** — `docs/COPY.md`. If present, the PRD's UI/UX requirements inherit its lexicon (features are named by their canonical nouns) and its error and empty-state patterns become named requirements rather than afterthoughts.

**Guides — read before the corresponding step:**

8. `productos/develop/guides/TECH-STACK-OPTIONS.md` — comparison data for the tech stack questions.
9. `productos/develop/guides/PRD-GENERATION.md` — section requirements and formats for the PRD.
10. `productos/develop/guides/ROADMAP-GENERATION.md` — phase design, task format, and the agent session guide for the roadmap.

## Workflow

### 1. Check state and pick the mode

This skill is resumable. Before anything else, check what exists:

- **Neither `docs/PRD.md` nor `docs/ROADMAP.md` exists** → run the full workflow from step 2.
- **`docs/PRD.md` exists but is incomplete** (missing numbered sections) → confirm the scoping decisions recorded in its Overview and Out of Scope sections still hold, then resume generation at the first missing section.
- **`docs/PRD.md` is complete but `docs/ROADMAP.md` is missing** → skip to step 5.
- **Both exist** and the member asked to "regenerate" or "update" → re-read the source docs (they may have changed), regenerate only what was asked, and if the PRD changes materially, flag that the roadmap depends on it and offer to regenerate that too.

### 2. Read and absorb every input

Read all available inputs in full before asking the member anything. Build a private working picture:

- **The core loop hypothesis** — from the Offer's Mechanism (DEFINE.md) and the primary magic moment: what single user journey, end to end, delivers the aha?
- **The candidate feature list** — harvest every concrete capability mentioned anywhere: each promise in the landing page / app listing copy, each screen and permission in the onboarding flow, each element of the mechanism, the guarantee from the Product Offer, the instrumentation the magic moment needs. Deduplicate into a flat list of 10–25 candidate features.
- **The platform** — usually evident: an App Store Listing means mobile, a Landing Page means web or desktop. Confirm rather than ask cold.
- **The business model facts** — business model, billing unit, plans, entry route, and trial mechanics from the Pricing Strategy. These determine the payments scope.
- **What's already decided** — the docs answer many scoping questions already. Never re-ask something the docs answer; state it back and confirm.

### 3. The scoping interview

Walk the member through five sections, in order, one question at a time — never a wall of questions. For each question: give one sentence of context on why it matters, offer suggestions grounded in the docs (not generic — if you can't ground a suggestion, ask an open question instead), and let them pick, modify, or write their own. Terse approvals ("yes", "looks good") count — move on. Carry every answer forward.

**A. The core loop.** Present your core loop hypothesis from step 2: *"Reading your magic moment and onboarding flow, the journey that has to work flawlessly is: [signup → X → Y → aha]. Everything else is secondary. Does that match how you see it?"* Iterate until the member owns one sentence describing the journey from first open to magic moment. This sentence anchors every cut that follows.

**B. Feature scope.** Present the harvested candidate feature list and sort it together into three buckets, pushing hard toward the smallest viable cut:

- **P0 — MVP launches with this.** The product is broken without it. Everything on the core loop is P0 by definition.
- **P1 — MVP feels incomplete without it.** Ships in the MVP if time allows, first thing after if not.
- **P2 — Post-launch.** Explicitly deferred. Goes in the PRD's Out of Scope section with a reason and a reconsider-when trigger.

Challenge every P0 that isn't on the core loop: *"Does the magic moment happen without this? Then it's P1."* Flag landing-page promises that land in P2 — the copy and the MVP must not contradict each other; one of them has to move. The MVP must be honestly buildable in 4–8 weeks of AI-assisted development; if the P0 list isn't, keep cutting.

**C. Platform and tech stack.** Confirm the platform, then work through the five core stack layers — frontend, backend, database, auth, payments — using the comparison data in `productos/develop/guides/TECH-STACK-OPTIONS.md`. For each layer: present 2–3 options as a short comparison (pros, cons, best-for) *adapted to this product*, recommend one with a reason tied to the product's actual needs, and let the member decide. Defaults to lean on unless the product clearly needs otherwise: **Convex** (backend + database); for payments, **Stripe Managed Payments** (web — Stripe as merchant of record, so tax compliance is handled from day one; **Polar** is the secondary when the member wants a simpler developer-first setup) or **RevenueCat** (mobile). For mobile utilities, **no database**, **no auth**, or **no payments** are legitimate answers — say so. If the Pricing Strategy says revenue starts later, payments may be P2; confirm rather than assume. Record a one-line rationale for every choice — the PRD's stack table needs it. Once chosen, the stack is settled: the PRD provides implementation guidance for these choices and never second-guesses them.

Then cover the **supporting services** — the tools that make a product observable and operable from launch, using the same comparison data. Don't over-deliberate these; recommend the default, confirm in one line, and move on:

- **Analytics** — instrument the activation funnel from day one. Default **PostHog** (analytics + session replay + feature flags), or **Mixpanel** for focused funnel/retention reporting.
- **Transactional email** — needed if the app sends sign-up, reset, receipt, or notification emails. Default **Resend** (developer-first, React Email), or **Loops** if the member also wants onboarding drips and newsletters from one tool. Skip only if the app sends no email.
- **Error tracking** — a launch essential, not optional. Default **Sentry** across frontend, backend, and mobile. Recommend it for every production app.

These are typically P1 setup tasks in the foundation phase, not features — but they belong in the PRD's stack table and dependencies so the coding agent wires them in early rather than retrofitting after launch.

**D. Constraints and tooling.** Three quick questions: Which coding agent will build this (Claude Code, Codex, Cursor — `build-loop` supports all three — or other)? What's the realistic timeline and weekly time budget? Any hard constraints — budget ceiling for services, existing accounts, compliance needs?

**E. Success criteria.** Define measurably what "MVP done" means, drawing from the Magic Moment metric (the first real user reaching the magic moment is the bar that matters) and DEFINE.md's north star when Business Strategy is filled. Aim for 3–5 criteria like *"time from signup to magic moment under 2 minutes"*, *"core loop completable on mobile Safari"*, *"all P0 features pass their acceptance criteria."*

**Close the interview** by presenting the complete MVP outline back in one compact block — core loop, P0/P1/P2 lists, platform, stack table with rationales, constraints, success criteria — and get explicit approval. This outline is the contract for everything generated next.

### 4. Generate `docs/PRD.md`

Read `productos/develop/guides/PRD-GENERATION.md` in full and follow it — critical rules, all 14 section requirements, and formats. The approved MVP outline from the interview supplies the scope, stack choices, and success criteria the guide expects; `docs/DEFINE.md` and the Design docs supply the strategic foundation.

Generate and write to file in four chunks, presenting each in conversation for approval before moving on (a 14-section read-back is the wrong shape; four checkpoints is right):

1. **§1–2** Overview + Technical Architecture — the outline's success criteria, stack table, and rationales land here.
2. **§3–4** Data Model + API Specification — implementation-ready, in the syntax of the chosen database per the guide.
3. **§5–8** User Stories + Functional Requirements + Non-Functional Requirements + UI/UX Requirements — stories use the Persona's named persona; FR priorities mirror the P0/P1 buckets; UI/UX covers every screen in the onboarding flow plus all MVP screens, referencing `docs/DESIGN.md` component names.
4. **§9–14** Auth + Payments + Edge Cases + Dependencies + Out of Scope + Open Questions — Auth and Payments are specific to the chosen providers (or skipped per the guide if "None"); Out of Scope is the P2 list with reasons and reconsider-when triggers.

Append the file as each chunk is approved — this is what makes the session resumable. After chunk 4, confirm the heading structure matches the guide's Output Structure Example exactly. These four checkpoints and the two roadmap checkpoints below are the only mandatory pauses; don't ask permission between sections within a chunk. If the member changes an earlier decision mid-generation, update the MVP outline first, then flag which already-written sections it affects and offer to revise them.

### 5. Generate `docs/ROADMAP.md`

Read `productos/develop/guides/ROADMAP-GENERATION.md` in full and follow it — the checkbox task format is non-negotiable, task IDs are sequential across all phases, every phase ships something demoable, and the magic moment must be achievable by the end of the core MVP phases.

Two-step approval:

1. **Phase outline first.** Propose the phase structure — count, titles, goals, rough task counts — sized to this product's actual complexity per the guide (simple: 2–3 phases; medium: 4–5; complex: 5–8). Get approval before writing tasks. Sanity-check against the member's timeline from interview section D; if the task count and their weekly budget don't fit 4–8 weeks, revisit scope or phasing now, not after generation.
2. **Full roadmap.** Write the complete file — header with status line, build philosophy, every phase with goal, reference sections, and tasks in the exact three-line format, then the agent session guide. Present a summary (phases, task totals, where the magic moment lands) rather than reading every task back.

### 6. Verify before delivering

Run this checklist against both files; fix anything that fails before handing over:

- [ ] Every PRD heading from the guide's Output Structure is present (or explicitly skipped per the guide's rules for "None" auth/payments).
- [ ] No design tokens are duplicated in the PRD — colors, type, spacing live only in `docs/DESIGN.md` references.
- [ ] The stack table matches the interview choices exactly, with rationales; nothing second-guesses them.
- [ ] Every roadmap task uses the exact `- [ ] **TASK-NNN**` three-line format; IDs are sequential with no gaps; status line reads `0/{total} tasks complete`.
- [ ] Every task traces to a PRD requirement; every P0 feature has tasks; no P2 feature does.
- [ ] The magic moment is reachable by the end of the core MVP phases.
- [ ] Each phase's reference sections use real heading text from the generated PRD.
- [ ] Landing-page promises and PRD scope don't contradict each other (any flagged in interview B are noted in Open Questions).
- [ ] The roadmap ends with the Agent Session Guide and its prompt templates, ready to paste into a coding agent.
- [ ] The member can say in one sentence what the MVP is and what it is not.

**Next step:** run `develop-build` to build straight through the roadmap (or go phase by phase with the roadmap's Agent Session Guide prompts).
