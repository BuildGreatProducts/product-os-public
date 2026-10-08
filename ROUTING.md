# Routing — which step runs next

The rulebook every ProductOS orchestrator follows: the four phase orchestrators (`define-phase`, `design-phase`, `develop-phase`, `distribute-phase`), `product-audit` (which composes a plan from it), `product-refactor` (which runs that plan), and the challenges. The phase checklists remain the source of truth for **how** each step runs; this file says **which** steps apply, **when**, and **how to tell a step is done**.

## Contents

- [Three layers decide the route](#three-layers-decide-the-route)
- [Modes](#modes)
- [Hard rules](#hard-rules)
- [The step catalog](#the-step-catalog)
- [Running a step](#running-a-step)
- [Reading progress](#reading-progress)

## Three layers decide the route

1. **`docs/PLAN.md`** — the member's programme, from their coach or from `product-audit`. It decides which steps apply to *this member* and in what order. It wins over the other two.
2. **The shape file** — `productos/shapes/<slug>.md`, for the primary shape named in `docs/DEFINE.md` → `## Product Shape`. It decides which steps apply to *this kind of product* and how each adapts.
3. **The phase checklists** — `productos/<phase>/<PHASE>-CHECKLIST.md`. The default order, and how each step runs.

No plan → follow the shape file's route through the checklist order. No shape yet → Define runs up to Step 1b (`define-product-shape`) before anything else is routed.

## Modes

**Plan modes** — set per member, in `docs/PLAN.md`:

- **Full** — run the step as its checklist describes.
- **Fast-track** — the same output file, extracted from what already exists and then sharpened, instead of built from scratch. Only steps the catalog below names a fast-track route for.
- **Already-done** — the output exists and is current. Point to the evidence and move on.
- **Skip** — the step doesn't apply to this member, with a one-line reason the catalog allows.

**Shape modes** — set per shape, in `shapes/<slug>.md`:

- **Full** — as the checklist runs it.
- **Adapted** — the skill runs on the shape's medium. The skill reads the shape file's note for how (onboarding as install → first output instead of screens; UX copy for commands and tool descriptions instead of buttons).
- **Lite** — a reduced output: the design system as brand tokens only (colour, type, logo use) for listings, landing pages, and docs.
- **Optional** — offer it; run it only if the member wants it.
- **Conditional** — written `Full / Skip` in a shape file, with the condition beside it (a security audit only where a service has custom code or customer data). Check the condition with the member, then treat the step as Full or Skip.
- **Skip** — doesn't apply to this shape.

When the plan and the shape disagree, the plan wins, but say so: a coach may have scheduled a step the shape usually skips for a reason.

## Hard rules

1. **Define is never skipped.** `docs/DEFINE.md` with Summary, Offer, Product Shape, Persona, and Pricing filled must exist before any Design, Develop, or Distribute step. New product → Full Define. Existing product → Fast-track (`define-from-code` → `define-offer-review` → `define-product-shape`, short session).
2. **Product Shape comes before Design.** Every later route depends on it.
3. **Distribute is never skipped.** Every programme ends in the Distribute loop; only its timing varies.
4. **Needs come first.** Every scheduled step's needed files come from an earlier scheduled step or are Already-done. If a plan skips a producer, it schedules the fast-track producer instead — never quietly un-skips half a phase.
5. **Security before go-live.** Any shape that ships code to customers runs `develop-security-audit` before `develop-golive`, and the audit's Critical and High findings are fixed first.

## The step catalog

"Done when" is what `scripts/status.py` checks. Step labels match the checklists.

### Define

| Step | Skill | Output | Needs | Done when | Plan modes |
| --- | --- | --- | --- | --- | --- |
| 0 — Idea *(only without one)* | `define-idea-finder` | `## Idea Audit` (optional section) | — | the member has one idea | Full · Skip (idea exists) |
| 1 — Product Offer | `define-offer-builder` (+ `define-offer-review`) | `## Summary`, `## 1. Product Offer` | — | Summary and all six Offer subsections filled | Full · Fast-track (`define-from-code` → `define-offer-review`; the review is not optional) · Already-done |
| 1b — Product Shape | `define-product-shape` | `## Product Shape` | Offer | Primary Shape names a slug from `shapes/SHAPES.md` | Full · Fast-track (short session confirming the shape the product already has) · Already-done |
| 2 — Customer Persona | `define-customer-persona` | `## 2. Customer Persona` | Offer | section filled | Full · Fast-track (`define-from-code`) · Already-done |
| 3 — Pricing Strategy | `define-pricing` | `## 3. Pricing Strategy` | Offer, Product Shape, Persona | section filled | Full · Fast-track (`define-from-code`) · Already-done |
| 4 — Business Strategy *(optional)* | `define-business-strategy` | `## 4. Business Strategy` | Offer, Pricing | section filled | Optional — schedule before paid acquisition or when investors ask |

### Design

| Step | Skill | Output | Needs | Done when | Plan modes |
| --- | --- | --- | --- | --- | --- |
| 1 — Product Identity | `design-identity-creator` | `docs/DESIGN.md` → `## Product Identity` (+ `docs/DESIGN.html`) | Define | the identity section exists in DESIGN.md | Full · Fast-track (capture an existing brand) · Already-done |
| 2 — UX Writing | `design-ux-writing` | `docs/COPY.md` | Identity | file exists | Full · Already-done |
| 3 — Design System | `design-design-system` or `design-design-system-from-code` | `docs/DESIGN.md` tokens + `docs/DESIGN.html` | Identity, or a codebase | DESIGN.md has YAML tokens | Full · Fast-track (= from-code) · Already-done. Required before any UI build or design review |
| 4 — Design Prompts | `design-prompt-generator` | `docs/DESIGN-PROMPTS.md` | Design System | file exists | Full · Skip (no new screens to generate) |
| 5 — Magic Moment | `design-magic-moment` | `docs/MAGIC-MOMENT.md` | Define | file exists | Full · Fast-track (name the moment the product already delivers) · Already-done. Required before onboarding, the activation audit, or scaling |
| 6 — Onboarding | `design-onboarding-flow` | `docs/ONBOARDING.md` (+ wireframe for screen shapes) | Magic Moment | file exists | Full · Skip (existing onboarding demonstrably activates) · Already-done |
| 7 — Acquisition surface(s) | `design-landing-page` · `design-app-listing` · `design-marketplace-listing` | `docs/LANDING-PAGE.md` · `docs/APP-LISTING.md` · `docs/MARKETPLACE-LISTING.md` | Define, Identity, Magic Moment | every surface the shape file names exists | Full · Skip (existing surface converts) · Already-done |

### Develop

| Step | Skill | Output | Needs | Done when | Plan modes |
| --- | --- | --- | --- | --- | --- |
| 0 — Migrate *(prompt-to-app platforms only)* | `develop-migrate` | `docs/MIGRATION.md` → the app in the member's own repo | an app on Lovable, Bolt, v0, Base44, Replit… | MIGRATION.md tasks all checked | Full when on such a platform · Skip otherwise |
| 1 — PRD & Roadmap | `develop-prd-roadmap` | `docs/PRD.md` + `docs/ROADMAP.md` | Define, Design (Lite is enough where the shape allows) | both files exist | Full (new build, or existing-codebase mode: a roadmap of the gap) · Already-done |
| 1b — Evals *(AI-native shapes and AI features)* | `develop-agent-evals` | `docs/EVALS.md` | PRD | file exists with at least three scenarios | Full for `agent-skill`, `agent-plugin`, `mcp-server`, `chat-assistant` · Optional for other shapes — recommended when the core output is AI-generated · Skip otherwise |
| 2 — Verify setup | `setup` | root guidelines wired | — | root CLAUDE.md/AGENTS.md carry the ProductOS block | Already-done (normally) |
| 3 — Build | `develop-build` | ROADMAP.md tasks checked | PRD, ROADMAP | ROADMAP status line reads Y/Y | Full · Already-done (codebase already matches the PRD) |
| 4 — Build loop | `build-loop` (+ `develop-feature-finder`) | shipped features | a codebase | ongoing | Full whenever post-MVP code work is scheduled |
| 5 — Code review | `develop-code-review` | verdict, in conversation | uncommitted changes | — | Full for changes made outside the build skills |
| 6 — Design changes | `develop-design-better` + `develop-design-review` | on-system UI | Design System | — | Full whenever UI work is scheduled |
| 7 — Conversion review | `develop-cro-audit` | `docs/CRO-AUDIT.md` | a usable product with a signup, pricing, or checkout surface | file exists | Full · Skip until usable end to end |
| 8 — Security audit | `develop-security-audit` | `docs/SECURITY-AUDIT.md` | code customers will run or reach | verdict is "Safe to launch" | Full before go-live; re-run after auth, payments, or data-access work |
| 9 — Go live | `develop-golive` | `docs/DEPLOY.md` | a shippable product; security audit cleared | the shape's "Live means" bar is met | Full · Already-done (already live) |

### Distribute

| Step | Skill | Output | Needs | Done when | Plan modes |
| --- | --- | --- | --- | --- | --- |
| 1 — Go-To-Market | `distribute-gtm-strategy` | `docs/GO-TO-MARKET.md` | Define | file exists | Full — never Skip |
| 2 — Growth Experiments | `distribute-growth-experiments` | `docs/GROWTH-EXPERIMENTS.md` + seeds `docs/GROWTH-TRACKER.md` | GTM | files exist | Full — never Skip |
| 3 — Run the cycle | the member, logging in `docs/GROWTH-TRACKER.md` | evidence | experiments | the tracker has logged results | Full — the loop itself |
| 4 — Scale & Automate | `distribute-scale-automate`, gated by `distribute-activation-retention-audit` | `docs/SCALE.md` (+ `docs/ACTIVATION-RETENTION-AUDIT.md`) | proven winners (Pass + double down), Magic Moment | file exists | Full · deferred until the tracker has winners |

## Running a step

Every orchestrator runs a step the same way:

1. **Name it.** "Next: Design Step 5 — Magic Moment (`design-magic-moment`). It writes `docs/MAGIC-MOMENT.md`. Your shape runs it in full." Say why it's next (plan, shape, or checklist order) and what it needs.
2. **Check the needs.** A missing upstream output means its producer runs first — never improvise the content.
3. **Confirm in one line**, then run the skill and follow its instructions. A challenge that is open (`docs/SHIP-IN-7.md` or `docs/SELL-IN-30.md` with `Status: Open`) owns the order instead: hand over to its check-in.
4. **Verify the output** against the step's "Done when" (re-run `scripts/status.py`).
5. **Name the next step**, or the hand-off to the next phase's orchestrator once the phase is done.

## Reading progress

Run the status script from the app repo root to see what's done:

```bash
python3 productos/scripts/status.py
```

(In a plugin install with no `productos/` folder, run it from this file's folder: `python3 scripts/status.py --repo <app-repo-root>`.) It prints every step above with `done`, `partial`, `missing`, or `n/a`, the primary shape, whether a plan or challenge is active, and the next step in checklist order. It reads files only; it never writes. Without Python, check the "Done when" column by hand.
