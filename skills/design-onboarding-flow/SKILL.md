---
name: design-onboarding-flow
description: >-
  Designs the onboarding flow to the magic moment — screen by screen for screen shapes, step by step
  for the rest (install to first output, purchase to first use, booking to first delivery) — from
  the best-practice reference for the product's shape, and writes docs/ONBOARDING.md plus, for
  screen shapes, a clickable lo-fi wireframe. Use when the user says "design my onboarding",
  "wireframe my onboarding", or "what happens in the first session". Requires docs/DEFINE.md, the
  Product Identity, and docs/MAGIC-MOMENT.md. Not for auditing built onboarding — use
  distribute-activation-retention-audit.
---

# Design: Onboarding Flow

Design the **concrete onboarding flow** — the sequence that takes a new user from "I just got this" to "I felt the magic moment and I'm in" — as a spec at `docs/ONBOARDING.md` (every screen or step with goal, action, what it proves, copy, wireframe or medium, drop-off risk, reference) and, for screen shapes, a self-contained clickable lo-fi wireframe at `docs/ONBOARDING-WIREFRAME.html` the member clicks through to stress-test the flow before any code is written. A flow only in prose can't be stress-tested; a wireframe without a spec can't be handed off. No external research is needed — the patterns live in `productos/design/onboarding/`.

**Screens or steps.** Screen shapes (`web-app`, `mobile-app`, `desktop-app`, `browser-extension`, `website`) get a screen-by-screen flow and the wireframe. Every other shape gets a **step-by-step** flow across the media the customer actually touches — install → configure → first command → first output; purchase → download → first use; booking → intake → kickoff → first delivery — where each step's "wireframe" field describes its medium (a terminal line, a chat turn, an email, a file, a call). A step flow gets a wireframe only for screens its shape row names (a developer tool's dashboard, a service's intake form); agent, chat, and developer shapes can add an optional transcript mock.

## Inputs

Read inputs from `docs/` and the worksheets and BONUS docs from `productos/design/` at the app repo root.

1. **`docs/DEFINE.md`** — **required.** Customer and use context (Offer → Customer plus the Persona), pain, mechanism, and business model (Pricing Strategy). The mechanism drives which screens are needed (an AI generator needs a prompt input; a meeting tool needs a microphone permission; a marketplace needs a category browse). If it's missing or thin, stop: tell the member to run the Define skills first (`define-offer-builder` → `define-customer-persona` → `define-pricing`, or `define-from-code` for an existing product).
2. **Product Identity** — the `## Product Identity` section of `docs/DESIGN.md`. **Required.** The Tone of Voice sets the flow's emotional register (a dramatic reveal, a measured demonstration, a defiant confrontation — read off the tone attributes and contrarian belief) and constrains every headline, button label, error, and notification.
3. **`docs/MAGIC-MOMENT.md`** — **required.** The primary magic moment, its position, time-to-aha target, and success metric; the flow's single job is to engineer the user to it. If missing, stop and point to `design-magic-moment`.
4. **Product shape** — `docs/DEFINE.md` → `## Product Shape` → `### Primary Shape` names the slug; read only the Design route row for Step 6 in `productos/shapes/<slug>.md` (from this folder, `../../shapes/<slug>.md`) — Full or Adapted, and how it adapts. No Product Shape section (a repo from before 2.0) → treat it as `web-app` unless the code or member clearly says otherwise, and suggest `define-product-shape`. If `docs/PLAN.md` schedules the step differently, the plan wins — say so.
5. **The onboarding best-practice doc** for the shape, from `productos/design/onboarding/` (from this folder, `../../design/onboarding/`):

| Primary shape | Reference file | Flow unit | Wireframe |
| --- | --- | --- | --- |
| `web-app` | B2B AI SaaS (teams) · Vertical SaaS (one industry) · Marketplace (two-sided) · Creator Economy (creators, communities) — pick by DEFINE.md | screens | `device-browser` |
| `mobile-app` | `BONUS-Mobile-Onboarding-Best-Practice.md` | screens | `device-mobile` / `device-tablet` |
| `desktop-app` | `BONUS-Desktop-App-Onboarding-Best-Practice.md` | screens | `device-desktop` |
| `browser-extension` | `BONUS-Browser-Extension-Onboarding-Best-Practice.md` | screens | `device-extension` |
| `website` | `BONUS-Website-Onboarding-Best-Practice.md` | screens | `device-browser` |
| `agent-plugin`, `agent-skill`, `mcp-server` | `BONUS-Agent-Extension-Onboarding-Best-Practice.md` | steps | optional `device-transcript` |
| `chat-assistant` | `BONUS-Chat-Assistant-Onboarding-Best-Practice.md` | steps (conversation turns) | optional `device-transcript` |
| `developer-tool` | `BONUS-API-and-Developer-Tool-Onboarding-Best-Practice.md` | steps | `device-browser` for the dashboard's first run; optional `device-transcript` |
| `productized-service` | `BONUS-Productized-Service-Onboarding-Best-Practice.md` | steps | optional `device-browser` (intake form and portal only) |
| `digital-product` | `BONUS-Digital-Product-Onboarding-Best-Practice.md` | steps | none |

   The shape row's note wins over this table — it names exactly which screens, if any, get a wireframe. The web-app references are `BONUS-B2B-AI-SaaS-…`, `BONUS-Vertical-SaaS-…`, `BONUS-Marketplace-…`, and `BONUS-Creator-Economy-Onboarding-Best-Practice.md`. Each doc opens with a Contents list. Read its **Meta-Rule**, **Decision Tree**, **Tactics**, **Anti-Patterns**, and **Calibration** sections — they are the source of truth for the flow; dip into a Worked Example when a screen or step needs a concrete precedent. A secondary shape with its own first-run (a `web-app` with an `mcp-server`) can borrow tactics from that shape's doc.
6. **`productos/design/3-Onboarding-Flow.md`** — the worksheet holding the output structure. Read it; never write to it.
7. **[REFERENCE-WIREFRAME.html](REFERENCE-WIREFRAME.html)** in this skill's folder — the exact HTML structure to generate (device frame, sidebar, annotation panel, click-to-advance navigation, lo-fi greyscale styling). Structural template only — **never copy its content.**
8. **`docs/COPY.md`** — optional; read in full if present. Every headline, sub-head, button label, command, tool message, email, and error must conform to its lexicon, mechanical rules, and per-surface budgets. This skill decides *which* screens or steps exist and *what* they say; COPY.md governs *how* it's said.

`docs/DESIGN.md`'s design-system tokens are deliberately **not** used — the wireframe stays neutral so flow problems aren't masked by polish.

## Voice

A senior onboarding designer who translates activation strategy into the first 60–180 seconds of a real product:

- **Pattern-led.** Every screen or step is anchored in a documented tactic: "Screen 1 is *Open With a Question* — Mobile Onboarding Tactic #1; Cal AI, Noom, Rizz all open this way." No screen exists without a reference.
- **Speed-biased.** Every additional screen or step costs completion rate. The default question on every one: "could this be removed or merged?"
- **Copy-specific.** Never "a welcome headline" — the actual headline, in the brand's voice, with character count and a one-line note on why it works.
- **Drop-off aware.** Every screen or step has a named drop-off risk and a mitigation; one without hasn't been pressure-tested. Off-screen steps leak hardest at the hand-offs — the install command that fails, the download email in spam, the intake form nobody returns.

## Workflow

### 1. Read the inputs

Read in order: DEFINE.md (with its Product Shape), the shape file's Step 6 row, Product Identity, Magic Moment, the selected best-practice doc sections, COPY.md if present, and — for screen shapes or a transcript mock — REFERENCE-WIREFRAME.html once. Extract:

- From DEFINE.md: primary shape and platform, customer, mechanism, business model.
- From the Identity: contrarian belief, tone attributes (the actual "X but not Y" phrases), no-go words, example sentence.
- From Magic Moment: the primary, its position, time-to-aha target, success metric, and the three candidates (so alternates are known).
- From the best-practice doc: the relevant decision-tree pattern, the 6–10 most relevant tactics, the anti-patterns, the calibration values.

### 2. Confirm the shape, the flow unit, and the reference doc

*"DEFINE.md names this a `[slug]` with a [business model] model — so the flow is [screens / steps], the reference is `BONUS-[X]-Onboarding-Best-Practice.md`, and [the wireframe is / there's no wireframe; I can add a transcript mock]. Confirm or correct."* If the product blends categories ("it's a mobile app but the buyer is a business"), choose a primary reference and optionally pull specific tactics from a secondary doc.

### 3. Form the working hypothesis

In 3 sentences, confirmed before drafting screens:

- **Funnel shape** — the decision-tree pattern that applies (e.g., "Goal-First Quiz Funnel" from Mobile; "Try-Before-Signup" or "Workspace + Sample Data" from B2B AI SaaS).
- **Total screen or step count** — rough target (5–8 for aha-fast B2B SaaS; 15–25 for consumer mobile quiz flows; 3–4 for developer tools; 2–3 for browser extensions; 3–5 steps for agent extensions, chat assistants, and digital products; 4–6 for productized services — the reference's Calibration section has the shape's number).
- **Magic-moment screen or step** — which number delivers it.

### 4. Draft the flow, one screen or step at a time

For each screen or step, propose the worksheet's fields (a step's "screen" is whatever the customer is looking at — a terminal, a chat, an inbox, a file, a call):

- **Number and name** ("3. Personalized Plan Reveal"; "2. First command")
- **Goal** — one sentence, anchored in a named tactic
- **User action** — the tap, type, swipe, or wait (steps: the command run, message sent, file opened, form returned)
- **What this screen proves** — one sentence: what the user now believes about the product ("The AI did real work on my data"). Feeds the wireframe annotation's `proves` field.
- **Copy** — screens: actual headline (in the brand's voice, usually 4–8 words, matching the Identity's example sentence in cadence), sub-headline, CTA text, and any social-proof text; steps: the exact words the customer meets there — the install command and its success line, the agent's first reply, the email subject and first line, the "start here" page's heading
- **Wireframe** — screens: 2–3 lines ("Full-bleed dark background, headline top-aligned, 3 large tappable goal options, primary CTA at bottom."); steps: the **medium** and what's in it ("Terminal: one-line install, then a three-line success message naming the first command to run.")
- **Drop-off risk** — what could go wrong here, with the mitigation
- **Reference** — the BONUS doc tactic this implements ("Mobile Onboarding Tactic #1 — Open With a Question")

Present each one, get a confirm/correct, then move on — don't drop the whole flow at once. Fold in "merge 2 and 3" or "this needs an extra step" immediately.

### 5. Mark the magic-moment screen or step

Call it out explicitly: *"This is the magic moment. The user has now hit [the activation event from `docs/MAGIC-MOMENT.md`]. Everything up to this point was preparation; everything after is consolidation."* Its copy, wireframe, and timing get extra scrutiny — the most-polished elements in the flow.

### 6. Cross-cutting checks

Before writing:

- **Time-to-magic-moment.** Estimate total user time from the first screen or step to the magic moment — for steps, include waits the customer doesn't control (review queues, delivery turnaround, email arrival). If it exceeds the Magic Moment doc's target by more than 20%, merge or remove screens.
- **Drop-off curve.** None of the best-practice doc's anti-patterns appear (no email-verification gate before a dev tool's test key; no empty workspace for B2B SaaS; no 12-field signup anywhere). Audit explicitly.
- **Tone consistency.** Read all copy aloud as one sequence. Any screen whose copy could come from a different brand gets rewritten; with COPY.md, every string conforms to its lexicon, budgets, and mechanical rules.
- **Magic-moment match.** The marked screen actually delivers the activation event in `docs/MAGIC-MOMENT.md`; surface any contradiction now.
- **Device frame.** Screen shapes get the frame from the step 4 table (step 8); step flows get none, or `device-transcript` if the member wants the mock.

### 7. Write `docs/ONBOARDING.md`

Use the section structure of `productos/design/3-Onboarding-Flow.md` exactly — same headers and per-screen field labels (Goal / User action / What this screen proves / Copy / Wireframe / Drop-off risk / Reference; ★ and the **Magic moment** line on the magic-moment screen). Step flows title each block `### Step N — [Name]`, read "What this step proves", and label the wireframe field **Medium**; the `## Wireframe` section names the transcript mock or says there is none. Replace every `[placeholder]`, drop the worksheet's italic intro, and add a dated line under the title: *Drafted: [Month Year]. Generated from DEFINE.md, Product Identity, and Magic Moment.* Each screen or step is a bullet block, not paragraphs; the doc reads in 3–5 minutes. `mkdir -p docs` if needed; if the file exists, read it first, preserve the member's edits, and show a diff and get approval before overwriting.

### 8. Generate `docs/ONBOARDING-WIREFRAME.html` (screen shapes; optional transcript mock otherwise)

Screen shapes always get the wireframe. A step flow gets one only for the screens its shape row names (a developer tool's dashboard first run; a service's intake form or portal, optional), built from those steps alone. For agent, chat, and developer shapes, also offer one question — *"Want a click-through transcript mock of these steps at `docs/ONBOARDING-WIREFRAME.html`? Each step renders as a terminal or chat frame."* — and build it only on a yes, using the `device-transcript` frame and the `.wire-turn` primitives. Otherwise skip to Verify.

Build one self-contained file by adapting `REFERENCE-WIREFRAME.html`:

1. **Keep the structural skeleton exactly** — header, sidebar, device frame, annotation panel, navigation script — and **pick the device frame class** for the product:

   | Product type (from DEFINE.md) | Device class | Size | Chrome markup |
   | --- | --- | --- | --- |
   | Consumer mobile AI app | `device-mobile` | 320×640 | `<div class="notch"></div>` |
   | iPad-first / tablet product | `device-tablet` | 480×680 | (none) |
   | B2B AI SaaS, marketplace, creator economy, vertical SaaS, productized service client portal, API/dev tool dashboard | `device-browser` | 800×500 | `<div class="browser-chrome"><div class="traffic-lights"><span></span><span></span><span></span></div><div class="url-bar">app.yourproduct.com</div></div>` |
   | Native desktop app (Granola / Raycast / Superhuman shape) | `device-desktop` | 720×480 | `<div class="title-bar"><div class="traffic-lights"><span></span><span></span><span></span></div><div class="title-text">Product Name</div></div>` |
   | Browser extension (Grammarly / Honey / Loom shape) | `device-extension` | 360×500 | `<div class="ext-arrow"></div>` |
   | Transcript mock (agent, chat, or developer shape — optional) | `device-transcript` | 720×480 | `<div class="title-bar"><div class="traffic-lights"><span></span><span></span><span></span></div><div class="title-text">Terminal</div></div>` |

   Replace `device-mobile` (the reference's active example) with the matching class and update the chrome markup inside the device div. Preserve the HTML comment block at the top of `<main class="canvas">` that documents the alternatives.
2. **Replace the sidebar list** with the actual screen names.
3. **Replace each `<section class="screen">`** with a wireframe of the actual screen, using the primitives (`.wire-progress`, `.wire-headline`, `.wire-sub`, `.wire-box`, `.wire-option`, `.wire-cta`, `.wire-back`, `.wire-loading`, `.wire-testimonial`); add a new primitive only when a screen genuinely needs one (`.wire-image`, `.wire-chat`).
4. **Wire up navigation** — each primary CTA's `data-next` points to the next screen number; each sidebar `data-jump` matches.
5. **Populate the `annotations` JS object** — one entry per screen with `title`, `goal`, `action`, `proves`, `risk`, `ref`, read directly from the spec's Goal / User action / What this screen proves / Drop-off risk / Reference fields so the two stay in sync.
6. **Keep it lo-fi.** Greyscale, dashed wireframe boxes, no real imagery, no imported fonts, no colour from `docs/DESIGN.md`.
7. **Single file, no dependencies.** No external CSS, CDN scripts, or images — it opens by double-clicking.

Walk it mentally before writing: every primary CTA advances to a real screen; the last screen's CTA loops to screen 1 or does nothing, with "[End of flow]" in its annotation.

## Verify before delivering

- [ ] The flow unit matches the shape (screens for screen shapes, steps otherwise) and the reference doc matches the shape table.
- [ ] Every screen or step in `docs/ONBOARDING.md` has goal, user action, what it proves, exact copy, wireframe or medium, drop-off risk, and a BONUS tactic reference.
- [ ] The magic-moment screen or step is marked ★ and matches `docs/MAGIC-MOMENT.md`; the time-to-magic-moment estimate is within 20% of its target.
- [ ] Anti-patterns avoided are listed, and none appear in the flow; the success metric is named.
- [ ] All copy is in the Identity's voice, reads as one brand aloud, and conforms to `docs/COPY.md` when present.
- [ ] If a wireframe or transcript mock was built: the HTML opens without errors; every `data-next` resolves; the sidebar matches the screens; every annotation (including `proves`) is populated; the device frame matches the product type; screens 1 → N → loopback walk cleanly.
- [ ] Both files use the same screen or step names, count, and identical copy — if they drift, the wireframe is stale.
- [ ] The spec reads in 3–5 minutes; any wireframe is lo-fi greyscale and clicks through in under 60 seconds.

Give the member the file path(s) and a tight recap: the funnel shape, the magic-moment screen or step, and which files were written.

**Next:** click through the wireframe (or walk the steps for real — run the install on a clean machine, buy your own product, book yourself) three times — as the user, hunting drop-off risks, and reading the copy aloud — edit anything that trips, then instrument the success metric before any code is written.
