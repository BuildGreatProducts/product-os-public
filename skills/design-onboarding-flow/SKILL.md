---
name: design-onboarding-flow
description: Use when the user has a finished `docs/DEFINE.md`, a Product Identity, and a Magic Moment hypothesis, and wants to design the onboarding flow that engineers the user toward that magic moment. Triggers on phrases like "design the onboarding flow", "create my onboarding", "build the activation flow", "wireframe my onboarding", "lay out the first-session experience", "what screens do I need for onboarding", "make the onboarding flow document", "click-through wireframe of my onboarding", or any request to translate the activation hypothesis into a screen-by-screen flow spec. Auto-selects the best-practice reference from `productos/design/onboarding/` based on product type, drafts a screen-by-screen flow in the voice of a senior onboarding designer, writes `docs/ONBOARDING.md`, and generates a clickable lo-fi HTML wireframe at `docs/ONBOARDING-WIREFRAME.html` the user can click through to feel the flow.
---

# Design: Onboarding Flow

This skill guides a founder through designing the **concrete onboarding flow** — the screen-by-screen sequence that engineers a new user from "I just installed this" to "I felt the magic moment and I'm in." The output is two artifacts in lockstep: a markdown specification at `docs/ONBOARDING.md` listing every screen with goal, copy, action, drop-off risk, and reference; and a self-contained clickable HTML wireframe at `docs/ONBOARDING-WIREFRAME.html` that lets the user feel the flow in their browser.

The voice is a senior onboarding designer with deep experience translating activation strategy into the first 60–180 seconds of an actual product — and specifically with the AI-era patterns that separate winners from look-alikes (Cal AI's 33-screen quiz, Cursor's first-completion-in-the-real-repo, Lovable's prompt-box-before-signup, Granola's microphone-only ask, Linear's pre-populated workspace). The designer's job is not to invent a flow from first principles; it is to translate the Magic Moment hypothesis, anchored in the Product Identity's tone and the right category-specific best practice doc, into screens the user can click through *today* and stress-test before any code is written.

A flow defined only in prose is a flow nobody can stress-test. A wireframe without a flow doc is a sketch nobody can hand off. This skill produces both, lockstep, so the founder leaves the session with something to ship and something to critique.

> **Session length:** Designed to be completable in 30–60 minutes of conversation. The skill reads four upstream documents, auto-selects the right best-practice reference, drafts the flow screen by screen with the user, and writes both outputs at the end. No external research is required — all category-specific patterns live in `productos/design/onboarding/`.

## Inputs

Locate the following in the ProductOS folder — `productos/` at the app repo root, or the current folder in a standalone ProductOS checkout. Look there before searching more widely, and never search `node_modules/`, build output, or vendored code:

1. **DEFINE.md** — usually `docs/DEFINE.md`. **Required.** Provides the customer and use context (Offer → Customer plus the Customer Persona), the problem (Offer → Pain), the mechanism (Offer → Mechanism), and the business model (`## 3. Pricing Strategy`). The mechanism in particular drives what screens are needed (an AI-generation product needs a prompt input; a meeting tool needs a microphone permission; a marketplace needs a category browse). If DEFINE.md is missing or thin, stop and tell the user to run the Define skills first (`define-offer-builder` → `define-customer-persona` → `define-pricing`), or `define-from-code` for an existing product.

2. **Product Identity** — the `## Product Identity` section of `docs/DESIGN.md`. **Required.** The tone of voice shapes the *emotional register* of the flow (a Magician reveals; a Sage demonstrates; an Outlaw confronts). The tone of voice attributes constrain every piece of copy — every headline, button label, error message, push notification. The visual style informs the wireframe's general direction.

3. **Magic Moment** — usually `docs/MAGIC-MOMENT.md`. **Required.** Names the recommended primary magic moment, its position in the journey, time-to-aha target, and success metric. The flow's single job is to engineer the user to this moment. If the Magic Moment document is missing, stop and tell the user to run `design-magic-moment` first.

4. **The appropriate Onboarding Best Practice reference** — auto-selected from `productos/design/onboarding/` based on the product type. Mapping table:

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

Read the selected best-practice doc in full at the start of the session. Its decision tree, 18 tactics, worked examples, and anti-patterns are the source of truth for what the flow should look like. State the selected doc back to the user and ask them to confirm (or correct, if the product blends categories) before proceeding.

5. **The Reference Wireframe** — `REFERENCE-WIREFRAME.html` in this skill's folder. Read this once at the start. It demonstrates the exact HTML structure the skill will generate — device frame, sidebar, annotation panel, click-to-advance navigation, lo-fi greyscale wireframe styling. Use it as the structural template. **Do not copy its content** — its purpose is to show the *shape* of a correct wireframe, not the screens for the user's product.

6. **DESIGN.md** — usually `docs/DESIGN.md`. Optional. If present, the wireframe can subtly hint at the brand's color/typography direction without becoming a hi-fi mock. The wireframe stays lo-fi — its purpose is flow testing, not visual evaluation.

7. **COPY.md** — usually `docs/COPY.md`. Optional — read in full if present. Produced by `design-ux-writing` (Design checklist Step 2). Every screen's headline, sub-head, button label, and error message must conform to its lexicon, mechanical rules, and per-surface budgets. This skill decides *which* screens exist and *what* they say; COPY.md governs *how* anything is said.

## The designer's voice

Adopt the voice of a senior onboarding designer with deep experience designing first-session flows across consumer AI, B2B SaaS, marketplaces, and developer tools:

- **Pattern-led.** Every screen the designer proposes is anchored in a documented tactic from the selected best-practice doc. "Screen 1 is the *Open With a Question* pattern from Mobile Onboarding Tactic #1 — Cal AI, Noom, Rizz all open this way."
- **Speed-biased.** Every additional screen costs completion rate. The default question is "could this be removed or merged?" — push for the minimum-viable flow toward the Magic Moment.
- **Copy-specific.** Never "a welcome headline." Always the actual headline, in the brand's tone of voice, with character count and a one-line note on why it works.
- **Drop-off aware.** Every screen has a named drop-off risk and a mitigation. Screens without a documented risk haven't been pressure-tested.
- **Wireframe-pragmatic.** The wireframe is lo-fi on purpose. Greyscale boxes, simple typography, no real imagery. The point is testing flow, not visual polish.

## Workflow

### 1. Read all four upstream inputs

Read in this order: DEFINE.md, Product Identity, Magic Moment, then the appropriate onboarding best-practice doc from `productos/design/onboarding/`. Also read the REFERENCE-WIREFRAME.html once to internalize the output format.

Extract:

- From DEFINE.md: product type, customer, mechanism, business model.
- From Product Identity: contrarian belief, tone-of-voice attributes (the actual "X but not Y" phrases), no-go words, example sentence.
- From Magic Moment: the recommended primary magic moment, position in journey, time-to-aha target, success metric, the three candidates (so alternates are known).
- From the best-practice doc: the relevant decision-tree pattern, the most relevant 6–10 tactics, the anti-patterns, the calibration table values.

### 2. Classify the product and confirm the reference doc

State back to the user: *"Based on DEFINE.md, this looks like a [product type] with a [business model] business model — so I'm using `BONUS-[X]-Onboarding-Best-Practice.md` as the reference. Confirm or correct."*

If the user pushes back (e.g., "it's a mobile app but the buyer is a business"), reconcile and choose the primary reference, optionally pulling specific tactics from a secondary doc. Most products map cleanly; some blend.

### 3. Form the working hypothesis

In 3 sentences:

- **Funnel shape:** which decision-tree pattern from the best-practice doc applies (e.g., "Goal-First Quiz Funnel" from Mobile, "Try-Before-Signup Funnel" from B2B AI SaaS, "Workspace + Sample Data Funnel" from B2B AI SaaS, etc.).
- **Total screen count:** rough target (5–8 for B2B SaaS aha-fast flows; 15–25 for consumer mobile quiz flows; 3–4 for developer tools; 2–3 for browser extensions).
- **Magic-moment screen:** which screen in the flow is the magic moment, with the screen number named.

State this back to the user and get a confirm before drafting screens.

### 4. Draft the flow screen by screen

Walk through the proposed flow one screen at a time. For each screen, propose:

- **Screen number and name** (e.g., "3. Personalized Plan Reveal")
- **Goal of this screen** — one sentence, anchored in a named tactic from the best-practice doc
- **User action expected** — what tap, type, swipe, or wait the user does
- **Copy** — actual headline (in the brand's tone of voice), sub-headline, CTA text, and any social-proof text. Aim for short — most onboarding headlines are 4–8 words. Match the Product Identity's example sentence in cadence.
- **Wireframe sketch** — described in 2–3 lines: "Full-bleed dark background, headline top-aligned, 3 large tappable goal options, primary CTA at bottom." The wireframe HTML will visualize this — the prose is the spec.
- **Drop-off risk** — what could go wrong on this screen
- **Reference** — the specific BONUS doc tactic this implements (e.g., "Mobile Onboarding Tactic #1 — Open With a Question")

Present each screen in conversation, get a confirm/correct, then move to the next. Don't drop the entire flow at once; the conversation *is* the value. If the user says "merge screens 2 and 3" or "this needs an extra step," fold it in immediately.

### 5. Mark the magic-moment screen

When the flow reaches the magic-moment screen, **call it out explicitly**: *"This is the magic moment. The user has now hit [the activation event from `docs/MAGIC-MOMENT.md`]. Every screen up to this point was preparation; every screen after this point is consolidation."* The magic-moment screen gets extra scrutiny — its copy, wireframe, and timing should be the most-polished elements in the flow.

### 6. Cross-cutting checks

Before writing the files, run five checks:

- **Time-to-magic-moment.** Estimate the total user time from screen 1 to the magic-moment screen. Compare to the Magic Moment doc's stated time-to-aha target. If the estimate exceeds the target by more than 20%, the flow has too many screens — go back and merge or remove.
- **Drop-off curve.** Anti-patterns from the best-practice doc should not appear (e.g., no email-verification gate before the test key for a dev tool; no empty workspace for B2B SaaS; no 12-field signup form anywhere). Audit explicitly.
- **Tone-of-voice consistency.** Read all the copy aloud as one sequence. Does it sound like the same brand from screen 1 to the last? Any screen whose copy could come from a different brand needs a rewrite.
- **Magic-moment match.** The magic-moment screen actually delivers the activation event described in `docs/MAGIC-MOMENT.md`. If the flow's named magic-moment screen doesn't match the Magic Moment doc, surface the contradiction now.
- **Mobile vs web vs desktop.** The wireframe defaults to a mobile phone frame. If the product is web/desktop/extension, change the device frame in the wireframe to match (a browser frame, a desktop window, a chrome extension popup).

### 7. Write `docs/ONBOARDING.md`

The worksheet at `productos/design/3-Onboarding-Flow.md` holds the canonical structure (summary + magic-moment-we're-engineering-toward + the flow + anti-patterns + success metric + wireframe + sources) — read it for structure, but never write to it. Write the filled version to `docs/ONBOARDING.md` (`mkdir -p docs` if needed). If that file already exists, read it first, preserve the member's edits, and show a diff and get approval before overwriting.

Match the worksheet's structure exactly: same section headers, same field labels (Goal / User action / Copy / Wireframe / Drop-off risk / Reference per screen; ★ marker on the magic-moment screen). Replace the `[placeholder]` markers with the filled-in content and drop the worksheet's italic intro, so the doc reads clean and the user can re-run the skill later against the same structure.

The full structure to populate:

```
# Onboarding Flow

*Drafted: [Month Year]. Generated from DEFINE.md, Product Identity, and Magic Moment.*

## Summary

[Two sentences: funnel shape, total screen count, estimated time-to-magic-moment, the named magic-moment screen number.]

## The magic moment we're engineering toward

> [One sentence from `docs/MAGIC-MOMENT.md`'s recommended primary.]

**Position:** Screen [N] of [total].
**Time-to-aha target:** [from Magic Moment doc].
**Success metric:** [from Magic Moment doc].

---

## The flow

### Screen 1 — [Name]

- **Goal:** [one sentence]
- **User action:** [tap/type/wait]
- **Copy:**
  - Headline: "[exact headline]"
  - Sub: "[exact sub]"
  - CTA: "[exact CTA text]"
- **Wireframe:** [2–3 line description]
- **Drop-off risk:** [named risk]
- **Reference:** [BONUS doc + tactic number]

### Screen 2 — [Name]
[same structure]

[...]

### Screen [N] — [Magic moment screen name] ★

[same structure, plus:]
- **Magic moment:** This is where the user hits [the activation event].

[remaining screens...]

---

## Anti-patterns avoided

[3–5 bullet list of anti-patterns from the BONUS doc that this flow specifically avoids and why.]

## Success metric

[From Magic Moment doc, plus 1–2 supporting funnel metrics worth instrumenting — e.g., screen-by-screen drop-off, completion rate to magic moment, signup conversion.]

## Wireframe

A clickable HTML wireframe is at `docs/ONBOARDING-WIREFRAME.html` — open in any browser and click through to feel the flow.

## Sources

- Reference: `productos/design/onboarding/BONUS-[X]-Onboarding-Best-Practice.md` ([selected pattern])
- Tone of voice: `docs/DESIGN.md` → Product Identity
- Magic moment: `docs/MAGIC-MOMENT.md`
- Product context: `docs/DEFINE.md`
```

Keep prose tight — each screen is a bullet block, not paragraphs. The whole doc should be readable end-to-end in 3–5 minutes.

### 8. Generate `docs/ONBOARDING-WIREFRAME.html`

Build a single self-contained HTML file by adapting `REFERENCE-WIREFRAME.html` from this skill's folder:

1. **Keep the structural skeleton exactly** — header, sidebar, device frame, annotation panel, navigation script. **Pick the right device frame class** for the user's product. The reference HTML defines five device frame classes; the CSS sizes them to fit the canvas; the device chrome markup differs per class:

   | Product type (from DEFINE.md) | Device class | Size | Chrome markup |
   | --- | --- | --- | --- |
   | Consumer mobile AI app | `device-mobile` | 320×640 | `<div class="notch"></div>` |
   | iPad-first / tablet product | `device-tablet` | 480×680 | (none) |
   | B2B AI SaaS, marketplace, creator economy, vertical SaaS, productized service client portal, API/dev tool dashboard | `device-browser` | 800×500 | `<div class="browser-chrome"><div class="traffic-lights"><span></span><span></span><span></span></div><div class="url-bar">app.yourproduct.com</div></div>` |
   | Native desktop app (Granola / Raycast / Superhuman shape) | `device-desktop` | 720×480 | `<div class="title-bar"><div class="traffic-lights"><span></span><span></span><span></span></div><div class="title-text">Product Name</div></div>` |
   | Browser extension (Grammarly / Honey / Loom shape) | `device-extension` | 360×500 | `<div class="ext-arrow"></div>` |

   Replace `device-mobile` (the reference's active example) with the class that matches the product. Update the chrome markup inside the device div accordingly. The HTML comment block at the top of the `<main class="canvas">` section in the reference HTML documents the full set — preserve that comment in the generated file so the user can see the alternatives.
2. **Replace the sidebar list** with the user's actual screen names.
3. **Replace each `<section class="screen">`** with a wireframe of the user's actual screen. Use the wireframe primitives (`.wire-progress`, `.wire-headline`, `.wire-sub`, `.wire-box`, `.wire-option`, `.wire-cta`, `.wire-back`, `.wire-loading`, `.wire-testimonial`) — extend with new primitives only if a screen genuinely needs one (e.g., `.wire-image` for image-upload screens, `.wire-chat` for chat-style screens).
4. **Wire up navigation** — each primary CTA's `data-next` attribute points to the next screen number. Each `data-jump` in the sidebar matches.
5. **Populate the `annotations` JS object** with one entry per screen, each containing `title`, `goal`, `action`, `proves`, `risk`, `ref`. These read directly from the Goal / User action / Drop-off risk / Reference fields of the markdown spec, so the wireframe and the doc stay in sync.
6. **Keep the styling lo-fi.** Greyscale palette, dashed wireframe boxes, no real imagery. The wireframe's job is flow critique, not visual evaluation. Do not import fonts. Do not use color from `docs/DESIGN.md` (the wireframe is intentionally neutral so flow problems aren't masked by polish).
7. **Single file, no dependencies.** No external CSS, no CDN scripts, no images. The user double-clicks the file and it opens in any browser.

Test the file mentally before writing — every primary CTA must advance to a real next screen; the last screen's CTA can either loop to screen 1 or do nothing (with a note in the annotation that says "[End of flow]").

### 9. Verify before delivering

Re-read both files and check:

- **Markdown file:** every screen has goal, user action, copy (with exact headline / sub / CTA), wireframe description, drop-off risk, and reference. The magic-moment screen is marked. Anti-patterns avoided are listed. Time-to-magic-moment estimate aligns with the Magic Moment doc's target.
- **HTML file:** opens without errors, every CTA's `data-next` resolves to a real screen, the annotation for each screen is populated, the sidebar matches the screens, the device frame matches the product type. Mentally walk through screens 1 → N → loopback to verify navigation works.
- **Copy match:** the headlines in the markdown match the headlines in the HTML wireframe exactly. If they drift, the wireframe is stale.

Deliver via `computer://` links to both files and a short summary — one line for the funnel shape, one line for the magic-moment screen, one line confirming both the markdown spec and the clickable wireframe are written. Keep the summary tight: this is a recap, not a re-pitch.

## Pacing and approval

- **Read all four inputs before drafting anything.** DEFINE.md, Product Identity, Magic Moment, BONUS doc.
- **One screen at a time.** Don't dump the whole flow at once. The conversation *is* the value.
- **Push toward minimum viable screens.** The default question on every screen is "could this be removed or merged?" — every additional screen costs completion rate.
- **Tone of voice on every piece of copy.** Headlines, sub-heads, CTAs, error messages, push notifications. Each one is in the brand's voice from the Product Identity in `docs/DESIGN.md` — and, when `docs/COPY.md` exists, conforms to its lexicon, budgets, and mechanical rules.
- **Cite the BONUS doc tactic by number for every screen.** No screen exists without a reference.
- **Write both outputs concisely.** Markdown bullets, not paragraphs. Wireframe lo-fi greyscale, not branded. Readable in 3–5 minutes; clickable in under 60 seconds.

## What "done" looks like

Two files in `docs/`:

- **`docs/ONBOARDING.md`** — a screen-by-screen spec where every screen has goal, user action, exact copy, wireframe description, drop-off risk, and BONUS doc reference. The magic-moment screen is marked. Anti-patterns avoided are listed. Success metric is named.
- **`docs/ONBOARDING-WIREFRAME.html`** — a single-file clickable lo-fi wireframe with sidebar navigation, device frame, primary-CTA-advances-flow, annotation panel per screen, no external dependencies. Opens by double-clicking.

Both files use the same screen names, the same copy, and the same screen count. If they drift, the spec is stale — re-run the skill to re-sync.

Recommended next step after a successful session: open the HTML wireframe and click through it three times — once as the user, once looking for drop-off risks, once reading the copy aloud. Edit anything that trips. Then instrument the named success metric in product analytics before any code is written.
