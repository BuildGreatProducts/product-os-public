---
name: design-onboarding-flow
description: >-
  Designs the screen-by-screen onboarding flow that gets a new user to the magic moment, using the
  best-practice reference for the product type, and writes docs/ONBOARDING.md plus a clickable lo-fi
  wireframe at docs/ONBOARDING-WIREFRAME.html. Use when the user says "design my onboarding",
  "wireframe my onboarding", or "what screens do I need for the first session". Requires
  docs/DEFINE.md, the Product Identity, and docs/MAGIC-MOMENT.md. Not for auditing onboarding
  already built — use distribute-activation-retention-audit.
---

# Design: Onboarding Flow

Design the **concrete onboarding flow** — the screen-by-screen sequence that takes a new user from "I just installed this" to "I felt the magic moment and I'm in" — as two artifacts in lockstep: a spec at `docs/ONBOARDING.md` (every screen with goal, action, what it proves, copy, wireframe, drop-off risk, reference) and a self-contained clickable lo-fi wireframe at `docs/ONBOARDING-WIREFRAME.html` the member can click through to stress-test the flow before any code is written. A flow only in prose can't be stress-tested; a wireframe without a spec can't be handed off. No external research is needed — the category patterns live in `productos/design/onboarding/`.

## Inputs

Read inputs from `docs/` and the worksheets and BONUS docs from `productos/design/` at the app repo root.

1. **`docs/DEFINE.md`** — **required.** Customer and use context (Offer → Customer plus the Persona), pain, mechanism, and business model (Pricing Strategy). The mechanism drives which screens are needed (an AI generator needs a prompt input; a meeting tool needs a microphone permission; a marketplace needs a category browse). If it's missing or thin, stop: tell the member to run the Define skills first (`define-offer-builder` → `define-customer-persona` → `define-pricing`, or `define-from-code` for an existing product).
2. **Product Identity** — the `## Product Identity` section of `docs/DESIGN.md`. **Required.** The Tone of Voice sets the flow's emotional register (a dramatic reveal, a measured demonstration, a defiant confrontation — read off the tone attributes and contrarian belief) and constrains every headline, button label, error, and notification.
3. **`docs/MAGIC-MOMENT.md`** — **required.** The primary magic moment, its position, time-to-aha target, and success metric; the flow's single job is to engineer the user to it. If missing, stop and point to `design-magic-moment`.
4. **The onboarding best-practice doc** for the product type, auto-selected from `productos/design/onboarding/`:

| Product type (from DEFINE.md) | Reference file in `productos/design/onboarding/` |
| --- | --- |
| Mobile consumer AI app | `BONUS-Mobile-Onboarding-Best-Practice.md` |
| B2B AI SaaS / web app for teams | `BONUS-B2B-AI-SaaS-Onboarding-Best-Practice.md` |
| API / developer tool | `BONUS-API-and-Developer-Tool-Onboarding-Best-Practice.md` |
| Vertical SaaS (industry-specific) | `BONUS-Vertical-SaaS-Onboarding-Best-Practice.md` |
| Productized service | `BONUS-Productized-Service-Onboarding-Best-Practice.md` |
| Two-sided marketplace | `BONUS-Marketplace-Onboarding-Best-Practice.md` |
| Creator economy / community platform | `BONUS-Creator-Economy-Onboarding-Best-Practice.md` |
| Browser extension | `BONUS-Browser-Extension-Onboarding-Best-Practice.md` |
| Desktop / native app | `BONUS-Desktop-App-Onboarding-Best-Practice.md` |

   Each doc opens with a Contents list. Read its **Meta-Rule**, **Decision Tree**, **18 Tactics**, **Anti-Patterns**, and **Calibration** sections — they are the source of truth for the flow; dip into a Worked Example when a screen needs a concrete precedent.
5. **`productos/design/3-Onboarding-Flow.md`** — the worksheet holding the output structure. Read it; never write to it.
6. **[REFERENCE-WIREFRAME.html](REFERENCE-WIREFRAME.html)** in this skill's folder — the exact HTML structure to generate (device frame, sidebar, annotation panel, click-to-advance navigation, lo-fi greyscale styling). Structural template only — **never copy its content.**
7. **`docs/COPY.md`** — optional; read in full if present. Every headline, sub-head, button label, and error must conform to its lexicon, mechanical rules, and per-surface budgets. This skill decides *which* screens exist and *what* they say; COPY.md governs *how* it's said.

`docs/DESIGN.md`'s design-system tokens are deliberately **not** used — the wireframe stays neutral so flow problems aren't masked by polish.

## Voice

A senior onboarding designer who translates activation strategy into the first 60–180 seconds of a real product:

- **Pattern-led.** Every screen is anchored in a documented tactic: "Screen 1 is *Open With a Question* — Mobile Onboarding Tactic #1; Cal AI, Noom, Rizz all open this way." No screen exists without a reference.
- **Speed-biased.** Every additional screen costs completion rate. The default question on every screen: "could this be removed or merged?"
- **Copy-specific.** Never "a welcome headline" — the actual headline, in the brand's voice, with character count and a one-line note on why it works.
- **Drop-off aware.** Every screen has a named drop-off risk and a mitigation; a screen without one hasn't been pressure-tested.

## Workflow

### 1. Read the inputs

Read in order: DEFINE.md, Product Identity, Magic Moment, the selected best-practice doc sections, COPY.md if present, and REFERENCE-WIREFRAME.html once. Extract:

- From DEFINE.md: product type, customer, mechanism, business model.
- From the Identity: contrarian belief, tone attributes (the actual "X but not Y" phrases), no-go words, example sentence.
- From Magic Moment: the primary, its position, time-to-aha target, success metric, and the three candidates (so alternates are known).
- From the best-practice doc: the relevant decision-tree pattern, the 6–10 most relevant tactics, the anti-patterns, the calibration values.

### 2. Classify the product and confirm the reference doc

*"Based on DEFINE.md, this looks like a [product type] with a [business model] business model — so I'm using `BONUS-[X]-Onboarding-Best-Practice.md` as the reference. Confirm or correct."* If the product blends categories ("it's a mobile app but the buyer is a business"), choose a primary reference and optionally pull specific tactics from a secondary doc.

### 3. Form the working hypothesis

In 3 sentences, confirmed before drafting screens:

- **Funnel shape** — the decision-tree pattern that applies (e.g., "Goal-First Quiz Funnel" from Mobile; "Try-Before-Signup" or "Workspace + Sample Data" from B2B AI SaaS).
- **Total screen count** — rough target (5–8 for aha-fast B2B SaaS; 15–25 for consumer mobile quiz flows; 3–4 for developer tools; 2–3 for browser extensions).
- **Magic-moment screen** — which screen number delivers it.

### 4. Draft the flow, one screen at a time

For each screen, propose the worksheet's fields:

- **Screen number and name** ("3. Personalized Plan Reveal")
- **Goal** — one sentence, anchored in a named tactic
- **User action** — the tap, type, swipe, or wait
- **What this screen proves** — one sentence: what the user now believes about the product ("The AI did real work on my data"). Feeds the wireframe annotation's `proves` field.
- **Copy** — actual headline (in the brand's voice, usually 4–8 words, matching the Identity's example sentence in cadence), sub-headline, CTA text, and any social-proof text
- **Wireframe** — 2–3 lines: "Full-bleed dark background, headline top-aligned, 3 large tappable goal options, primary CTA at bottom."
- **Drop-off risk** — what could go wrong here, with the mitigation
- **Reference** — the BONUS doc tactic this implements ("Mobile Onboarding Tactic #1 — Open With a Question")

Present each screen, get a confirm/correct, then move on — don't drop the whole flow at once. Fold in "merge 2 and 3" or "this needs an extra step" immediately.

### 5. Mark the magic-moment screen

Call it out explicitly: *"This is the magic moment. The user has now hit [the activation event from `docs/MAGIC-MOMENT.md`]. Every screen up to this point was preparation; every screen after is consolidation."* Its copy, wireframe, and timing get extra scrutiny — the most-polished elements in the flow.

### 6. Cross-cutting checks

Before writing:

- **Time-to-magic-moment.** Estimate total user time from screen 1 to the magic-moment screen. If it exceeds the Magic Moment doc's target by more than 20%, merge or remove screens.
- **Drop-off curve.** None of the best-practice doc's anti-patterns appear (no email-verification gate before a dev tool's test key; no empty workspace for B2B SaaS; no 12-field signup anywhere). Audit explicitly.
- **Tone consistency.** Read all copy aloud as one sequence. Any screen whose copy could come from a different brand gets rewritten; with COPY.md, every string conforms to its lexicon, budgets, and mechanical rules.
- **Magic-moment match.** The marked screen actually delivers the activation event in `docs/MAGIC-MOMENT.md`; surface any contradiction now.
- **Device frame.** Mobile is the default; web, desktop, and extension products get the matching frame (step 8).

### 7. Write `docs/ONBOARDING.md`

Use the section structure of `productos/design/3-Onboarding-Flow.md` exactly — same headers and per-screen field labels (Goal / User action / What this screen proves / Copy / Wireframe / Drop-off risk / Reference; ★ and the **Magic moment** line on the magic-moment screen). Replace every `[placeholder]`, drop the worksheet's italic intro, and add a dated line under the title: *Drafted: [Month Year]. Generated from DEFINE.md, Product Identity, and Magic Moment.* Each screen is a bullet block, not paragraphs; the doc reads in 3–5 minutes. `mkdir -p docs` if needed; if the file exists, read it first, preserve the member's edits, and show a diff and get approval before overwriting.

### 8. Generate `docs/ONBOARDING-WIREFRAME.html`

Build one self-contained file by adapting `REFERENCE-WIREFRAME.html`:

1. **Keep the structural skeleton exactly** — header, sidebar, device frame, annotation panel, navigation script — and **pick the device frame class** for the product:

   | Product type (from DEFINE.md) | Device class | Size | Chrome markup |
   | --- | --- | --- | --- |
   | Consumer mobile AI app | `device-mobile` | 320×640 | `<div class="notch"></div>` |
   | iPad-first / tablet product | `device-tablet` | 480×680 | (none) |
   | B2B AI SaaS, marketplace, creator economy, vertical SaaS, productized service client portal, API/dev tool dashboard | `device-browser` | 800×500 | `<div class="browser-chrome"><div class="traffic-lights"><span></span><span></span><span></span></div><div class="url-bar">app.yourproduct.com</div></div>` |
   | Native desktop app (Granola / Raycast / Superhuman shape) | `device-desktop` | 720×480 | `<div class="title-bar"><div class="traffic-lights"><span></span><span></span><span></span></div><div class="title-text">Product Name</div></div>` |
   | Browser extension (Grammarly / Honey / Loom shape) | `device-extension` | 360×500 | `<div class="ext-arrow"></div>` |

   Replace `device-mobile` (the reference's active example) with the matching class and update the chrome markup inside the device div. Preserve the HTML comment block at the top of `<main class="canvas">` that documents the alternatives.
2. **Replace the sidebar list** with the actual screen names.
3. **Replace each `<section class="screen">`** with a wireframe of the actual screen, using the primitives (`.wire-progress`, `.wire-headline`, `.wire-sub`, `.wire-box`, `.wire-option`, `.wire-cta`, `.wire-back`, `.wire-loading`, `.wire-testimonial`); add a new primitive only when a screen genuinely needs one (`.wire-image`, `.wire-chat`).
4. **Wire up navigation** — each primary CTA's `data-next` points to the next screen number; each sidebar `data-jump` matches.
5. **Populate the `annotations` JS object** — one entry per screen with `title`, `goal`, `action`, `proves`, `risk`, `ref`, read directly from the spec's Goal / User action / What this screen proves / Drop-off risk / Reference fields so the two stay in sync.
6. **Keep it lo-fi.** Greyscale, dashed wireframe boxes, no real imagery, no imported fonts, no colour from `docs/DESIGN.md`.
7. **Single file, no dependencies.** No external CSS, CDN scripts, or images — it opens by double-clicking.

Walk it mentally before writing: every primary CTA advances to a real screen; the last screen's CTA loops to screen 1 or does nothing, with "[End of flow]" in its annotation.

## Verify before delivering

- [ ] Every screen in `docs/ONBOARDING.md` has goal, user action, what it proves, exact copy (headline / sub / CTA), wireframe description, drop-off risk, and a BONUS tactic reference.
- [ ] The magic-moment screen is marked ★ and matches `docs/MAGIC-MOMENT.md`; the time-to-magic-moment estimate is within 20% of its target.
- [ ] Anti-patterns avoided are listed, and none appear in the flow; the success metric is named.
- [ ] All copy is in the Identity's voice, reads as one brand aloud, and conforms to `docs/COPY.md` when present.
- [ ] The HTML opens without errors; every `data-next` resolves; the sidebar matches the screens; every annotation (including `proves`) is populated; the device frame matches the product type; screens 1 → N → loopback walk cleanly.
- [ ] Both files use the same screen names, screen count, and identical headlines — if they drift, the wireframe is stale.
- [ ] The spec reads in 3–5 minutes; the wireframe is lo-fi greyscale and clicks through in under 60 seconds.

Give the member both file paths and a tight recap: the funnel shape, the magic-moment screen, and confirmation that both the spec and the clickable wireframe are written.

**Next:** click through the wireframe three times — as the user, hunting drop-off risks, and reading the copy aloud — edit anything that trips, then instrument the success metric before any code is written.
