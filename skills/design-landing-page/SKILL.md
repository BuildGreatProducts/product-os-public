---
name: design-landing-page
description: >-
  Writes the landing page spec — every headline, section, and visual direction mapped to a proven
  conversion tactic, with the CTA the shape calls for (sign up, install, add to Chrome, book a
  call, buy, API key) — to docs/LANDING-PAGE.md, plus an optional lo-fi wireframe. Use for
  any product with a web presence when the user says "write my landing page", "design my hero", or
  "outline my homepage". Requires docs/DEFINE.md, the Product Identity, and docs/MAGIC-MOMENT.md.
  Not for store listings — use design-app-listing or design-marketplace-listing; not for auditing a
  built page — use develop-cro-audit.
---

# Design: Landing Page Copywriter

Design the **landing page** for any product with a web presence — the marketing surface that turns a stranger into a user, installer, buyer, or client — as a spec at `docs/LANDING-PAGE.md`: every section with actual copy in the brand's voice, visual direction, what it proves, its drop-off risk, and the Web Landing Page BONUS tactic that justifies it. Optionally (step 8) also a clickable lo-fi wireframe at `docs/LANDING-PAGE-WIREFRAME.html` that stays in lockstep with the spec. The job is to align strategy (DEFINE.md), voice (the Identity), and activation (the Magic Moment) into one page: without the Identity the page inherits a generic tone; without the Magic Moment it promises an outcome onboarding doesn't deliver. No external research is needed — the patterns live in the BONUS doc. **Any shape with a web presence.** A mobile app whose only acquisition surface is the store uses `design-app-listing`; every other store, marketplace, or registry listing uses `design-marketplace-listing` — and a shape whose Step 7 names both runs both.

## Inputs

Read inputs from `docs/` and the worksheets and BONUS docs from `productos/design/` at the app repo root.

1. **`docs/DEFINE.md`** — **required.** Customer and use context (Offer → Customer plus the Persona, whose own words feed the Problem section), pain, mechanism, proof (Offer → Proof and Guarantee), and the business model and plans (Pricing Strategy). If it's missing or its Offer and Pricing are placeholders, stop: tell the member to run the Define skills first (`define-offer-builder` → `define-customer-persona` → `define-pricing`, or `define-from-code` for an existing product).
2. **Product Identity** — the `## Product Identity` section of `docs/DESIGN.md`. **Required.** The Tone of Voice sets each headline's register (a dramatic brand reveals; a calm-authority brand demonstrates with measured proof; a challenger confronts; a nurturing brand reassures); its "we say / we don't say" list and example sentence constrain every word. If missing, stop and point to `design-identity-creator`.
3. **`docs/MAGIC-MOMENT.md`** — **required.** The primary magic moment is the *promise* the page makes; the hero is the magic moment framed as a benefit headline.
4. **`productos/design/BONUS-Web-Landing-Page-Best-Practice.md`** — **required**; the source of truth. It opens with a Contents list: read **The Meta-Rule**, **The Decision Tree** (step 3), **The 18 Tactics** (steps 4–5, cited by number), **Anti-Patterns** (step 6), and **Calibration** (budgets); the Worked Examples (Stripe / Lovable / Linear) calibrate the hero. Benchmarks with sources are in its **Numbers That Set the Stakes** section — quote them from there, not from memory.
5. **`productos/design/4a-Landing-Page.md`** — the worksheet holding the output structure. Read it; never write to it.
6. **Product shape** — `docs/DEFINE.md` → `## Product Shape` → `### Primary Shape` names the slug; read only the Design route row for Step 7 in `productos/shapes/<slug>.md` (from this folder, `../../shapes/<slug>.md`) — it names which acquisition surfaces the shape needs. The shape sets the CTA and hero visual:

| Primary shape | Primary CTA (first person where it isn't a store badge) | Hero visual |
| --- | --- | --- |
| `web-app` | "Start my free trial" / "Try it free" | the product working, or a try-before-signup input |
| `mobile-app` | the official App Store / Google Play badges | the app in a phone frame on the magic moment |
| `desktop-app` | "Download for Mac" (detect the OS; link the others) | the app window mid-task |
| `browser-extension` | "Add to Chrome" (detect the browser; the store's own button wording) | the extension working on a real page |
| `agent-plugin`, `agent-skill` | "Install the plugin" + the copy-paste install command | a terminal or chat frame showing the first output |
| `mcp-server` | "Connect [Product]" + the one-click install or config snippet per client | a chat frame showing one tool call and its result |
| `chat-assistant` | "Start chatting" / "Open in [host]" / "Add to Slack" | a real conversation |
| `developer-tool` | "Get my API key" or the install command | a working code sample |
| `productized-service` | "Book my call" or "Start my project" | the deliverable the client receives |
| `website` | "Subscribe" / "Browse the [directory]" | the content itself |
| `digital-product` | "Get it for $[price]" | the product's inside, in use |

   No Product Shape section (a repo from before 2.0) → treat it as `web-app` unless the code or member clearly says otherwise, and suggest `define-product-shape`. If `docs/PLAN.md` schedules the step differently, the plan wins — say so.
7. **The design system in `docs/DESIGN.md`** — optional. If present, the hero visual direction can reference the brand's actual color/typography tokens.
8. **`docs/COPY.md`** — optional. The marketing register stays this skill's own, but product nouns and CTA verbs on the page must match the in-product lexicon.
9. **[REFERENCE-WIREFRAME.html](REFERENCE-WIREFRAME.html)** in this skill's folder — used only at step 8 if the member wants the wireframe.

## Voice

A senior product marketing strategist and brand copywriter:

- **Proof is real or absent.** Logos, ratings, review counts, user counts, testimonials, press, and compliance badges come only from `docs/DEFINE.md` → Offer → Proof or what the member tells you. Never invent a customer, a number, or a badge; a pre-launch product leaves those slots as `[none yet — omit this section]` and leans on a demonstrative visual, the guarantee, or the founder's story instead.
- **Conversion sets the structure; the voice writes the words.** The BONUS doc's patterns decide *what* each section does and in what order ("outcome + timeframe" headline, one CTA everywhere); the Identity's Tone of Voice governs *every word inside* that structure — no line may break it. If the Identity says "Smart, but not academic. Authentic, but not stuffy," that's the test for every headline.
- **Magic Moment honest.** Every promise is deliverable in the first session. If the Magic Moment is "first meeting transcribed in 60 seconds," the headline can promise "Notes ready in 60 seconds" — not "Your team's most productive year ever."
- **Specific and pattern-led.** Never "a benefit-led headline" — the actual headline with character count and a one-line note on why it works, citing its tactic: "Hero is Tactic #3 (the 10-word value-prop headline)."

## Workflow

### 1. Read the inputs

Read DEFINE.md, the Product Identity, the Magic Moment, the BONUS doc sections above, and COPY.md if present. Extract:

- From DEFINE.md: primary shape (and any secondary shapes with their own surfaces), customer, mechanism, business model, the Pricing Strategy's plans and price line, and the Offer's Proof.
- From the Identity: worldview, contrarian belief, tone attributes ("X but not Y"), we-say / we-don't-say list, example sentence, visual style (concrete tokens live in DESIGN.md).
- From Magic Moment: the primary, its position, time-to-aha target, success metric.
- From the BONUS doc: the decision-tree pattern, the 6–10 most relevant tactics, the anti-patterns, the calibration values.
- From COPY.md: the canonical nouns and verbs every product reference and CTA verb must match.

### 2. Confirm the shape and the CTA

*"DEFINE.md names this a `[slug]`, so the page's one CTA is "[CTA from the table]" and the hero shows [hero visual]. I'm using `BONUS-Web-Landing-Page-Best-Practice.md` as the reference; output goes to `docs/LANDING-PAGE.md`. Confirm or correct."* If the shape's Step 7 names no landing page (a mobile app selling only through the store), redirect: *"Your acquisition surface is the store listing — use `design-app-listing` (App Store / Google Play) or `design-marketplace-listing` (any other store or registry)."* If it names a listing as well, say it's next once this page is done.

Where the CTA leaves the page (a store's install button, a booking calendar, a checkout), the page's job ends at the click — name the destination in the CTA's notes so the hand-off copy matches. For install-command CTAs, the command is the CTA: it must be copy-paste correct, with a copy button.

### 3. Form the working hypothesis

In 3 sentences, confirmed before writing copy:

- **Pattern** — the decision-tree pattern (Try-Before-Signup / Code-in-Hero / Product-Visual / Outcome-First / Customer-Logo / Gallery+Price Hero).
- **Hero promise** — the Magic Moment framed as a one-sentence benefit headline.
- **Visual direction** — what the hero shows (runnable code / prompt box / product screenshot / before-after / gallery).

### 4. Draft the page, one section at a time

The canonical structure is 11 sections: Header → Hero → Social Proof Bar → Problem → Solution / How It Works → Features as Benefits → Deep Social Proof → Pricing → FAQ → Final CTA → Footer. For each, propose the worksheet's fields:

- **Goal** — one sentence, anchored in a named tactic
- **Copy** — actual headlines, sub-heads, CTAs, body, with the worksheet's budgets (headline ≤12 words, CTA 3–5 words first-person, step/benefit headlines ~5 words with ~20-word descriptions)
- **Visual direction** — 2–3 lines ("full-bleed dark background, real product UI screenshot with subtle motion looping every 4 seconds")
- **What this proves** — one sentence: what the visitor now believes after this section
- **Drop-off risk** — what makes a visitor leave or stall here
- **Reference** — the tactic number ("Landing Page Tactic #3 — The 10-word Value-Prop Headline")

Social proof sections use only real proof (see Voice); **Pricing mirrors `docs/DEFINE.md` → Pricing Strategy exactly** — each plan's name, price, inclusions, and CTA, highlighting the plan the strategy steers buyers to, never adding tiers it doesn't have; the footer lists only certifications actually held.

Present each section, get a confirm/correct, then move on — don't drop the whole page at once.

### 5. The Hero gets extra scrutiny

The hero is the disproportionate-impact zone — the headline, sub-head, CTA, and visual decide whether the visitor scrolls or closes (the BONUS doc's Numbers section has the above-the-fold data). Spend more time on it than on the rest of the page:

- **10-word value-prop headline** in the brand's voice
- **One-sentence sub-headline** that qualifies the customer or names the timeframe
- **3–5-word first-person CTA** ("Start my free trial", not "Start your free trial") — the shape's CTA from the table; a store badge or install command replaces it where the shape calls for one
- **Demonstrative hero visual** — the actual product working, not a stock illustration
- **Above-fold social proof** — logo bar OR testimonial fragment OR rating + count, real only

Test the headline by reading it to a stranger in the ICP and asking what the product does — if they can't answer in one sentence, rewrite.

### 6. Cross-cutting checks

Before writing the file:

- **Magic Moment match.** The hero promise is deliverable in the first session and matches the Magic Moment exactly.
- **Tone consistency.** Read all copy aloud, hero through footer; any section that could come from a different brand gets rewritten. The Identity's example sentence should fit naturally inside the page.
- **Anti-patterns.** Run the page against the BONUS doc's 12 anti-patterns (stock-illustration hero, multi-CTA above the fold, "Submit" button, hidden pricing, …) and remove any that appear.
- **Brand identity match.** Visual direction is consistent with the Identity's Visual Style and the DESIGN.md tokens — same imagery lane, composition principles, character.
- **Pattern match.** Every section maps to a tactic; a section without one doesn't belong on the page.

### 7. Write `docs/LANDING-PAGE.md`

Use the section structure of `productos/design/4a-Landing-Page.md` exactly — same headers and field labels, including What this proves / Drop-off risk on every section. Replace every `[placeholder]`, drop the worksheet's italic intro, and add a dated line under the title: *Drafted: [Month Year]. Generated from DEFINE.md, Product Identity, and Magic Moment.* Bullets with exact copy in quotes; the doc reads in 4–6 minutes. `mkdir -p docs` if needed; if the file exists, read it first, preserve the member's edits, and show a diff and get approval before overwriting.

### 8. Offer the wireframe (optional)

Ask one question:

> *"Want me to also generate a clickable lo-fi HTML wireframe of the page at `docs/LANDING-PAGE-WIREFRAME.html`? It's a scrollable browser-frame view with sidebar navigation and per-section annotations — useful for feeling the flow and pressure-testing copy before any code is written. Skip if you want to stay markdown-only."*

If the member declines, skip to Verify and note the skip in the recap so they can re-run this step later. If they accept, follow [references/wireframe-build.md](references/wireframe-build.md).

## Verify before delivering

- [ ] Every one of the 11 sections has goal, exact copy (headline / sub / CTA / body), visual direction, what it proves, drop-off risk, and a BONUS tactic reference.
- [ ] The hero promise matches the Magic Moment exactly and is deliverable in the first session.
- [ ] The CTA matches the shape's row (store badge, install command, booking, checkout, API key, or signup); one CTA repeated through the page — hero, sticky, and final CTA use the same first-person copy, 3–5 words; all headlines ≤12 words.
- [ ] All proof is real (from DEFINE.md's Proof or the member); empty slots say `[none yet — omit this section]`.
- [ ] Pricing mirrors DEFINE.md's Pricing Strategy exactly — no added tiers.
- [ ] Every line is in the Identity's voice, no category-default copy, and product nouns/CTA verbs match `docs/COPY.md` when present.
- [ ] Anti-patterns avoided are listed; refresh cadence is named (45 days, first A/B test specified); the doc is dated and sourced.
- [ ] If the wireframe was generated: it opens without errors, every sidebar item scrolls to a real section, the annotation panel updates on scroll, the browser chrome is sticky, the 11 sections render in order, and every headline, sub-head, CTA, testimonial, and FAQ matches the markdown exactly (if they drift, regenerate).

Give the member the file path(s) and a tight recap: the pattern, the hero promise, and whether the wireframe was generated or skipped.

**Next:** scroll the wireframe three times (as the visitor, hunting drop-off risks, reading the copy aloud), build the page with the `docs/DESIGN.md` tokens, instrument hero CTA click-through, sticky CTA engagement, and scroll depth from day one, and run the first A/B test within 45 days. With a store surface too, run `design-app-listing` (App Store / Google Play) or `design-marketplace-listing` (any other store or registry).
