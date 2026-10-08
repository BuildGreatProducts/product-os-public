---
name: design-app-listing
description: >-
  Writes the App Store and Google Play listing spec — icon, title, subtitle, keywords, seven
  screenshot captions, preview video, both store descriptions, custom product pages, review timing,
  localization — to docs/APP-LISTING.md, in the brand's voice and within store character limits. Use
  for a mobile app when the user says "write my app store listing", "ASO", or "draft my screenshot
  captions". Requires docs/DEFINE.md, the Product Identity, and docs/MAGIC-MOMENT.md. Not for web
  pages — use design-landing-page; not for any other store, marketplace, or registry — use
  design-marketplace-listing.
---

# Design: App Store Listing Copywriter

Design the **App Store / Google Play listing** for a mobile-first product — the acquisition surface that turns a search-results impression into an install — as a spec at `docs/APP-LISTING.md`: every consequential field with actual copy in the brand's voice, character counts honored, a story-arc screenshot sequence, and the App Store Listing BONUS tactic that justifies each element. The job is to align strategy (DEFINE.md), voice (the Identity), and activation (the Magic Moment) into one listing that wins the first three screenshots: without the Identity it inherits a generic tone; without the Magic Moment it promises an outcome onboarding doesn't deliver. No external research is needed — the patterns live in the BONUS doc. **App Store and Google Play only** — the shape is `mobile-app` (primary, or secondary with its own store listing). For web pages use `design-landing-page`; for any other store, marketplace, or registry (browser extension stores, plugin marketplaces, MCP registries, the GPT Store, package registries, storefronts) use `design-marketplace-listing`.

## Inputs

Read inputs from `docs/` and the worksheets and BONUS docs from `productos/design/` at the app repo root.

1. **`docs/DEFINE.md`** — **required.** Customer and use context (Offer → Customer plus the Persona), pain, mechanism, proof (Offer → Proof), and the business model and price line (Pricing Strategy). If it's missing or its Offer and Pricing are placeholders, stop: tell the member to run the Define skills first (`define-offer-builder` → `define-customer-persona` → `define-pricing`, or `define-from-code` for an existing product).
2. **Product Identity** — the `## Product Identity` section of `docs/DESIGN.md`. **Required.** The Tone of Voice sets each caption's register (a dramatic brand reveals the wow in screenshot 3; a calm-authority brand proves with numbers; a challenger confronts; a nurturing brand reassures); its "we say / we don't say" list and example sentence constrain every caption and description line. If missing, stop and point to `design-identity-creator`.
3. **`docs/MAGIC-MOMENT.md`** — **required.** The primary magic moment is the *promise* the listing makes; screenshot 1's caption is the magic moment framed as a benefit. A first screenshot promising "Lose weight without counting calories" when the Magic Moment is "personalized plan reveal" is a lie that craters post-install retention.
4. **`productos/design/BONUS-App-Store-Listing-Best-Practice.md`** — **required**; the source of truth. It opens with a Contents list: read **The Meta-Rule**, **The Decision Tree** (step 3), **The 18 Tactics** (steps 4–5, cited by number), **Anti-Patterns** (step 6), and **Calibration**; the Worked Examples (Cal AI / Duolingo / CPP-driven subscription) calibrate screenshots 1–3 and CPPs.
5. **`productos/design/4b-App-Store-Listing.md`** — the worksheet holding the output structure. Read it; never write to it.
6. **[references/store-facts.md](references/store-facts.md)** — the store character limits and platform behaviour (description indexing, caption OCR, ranking signals), dated. Read at step 1.
7. **The design system in `docs/DESIGN.md`** — optional. If present, icon and screenshot direction can reference the brand's actual color/typography tokens.
8. **`docs/COPY.md`** — optional. The marketing register stays this skill's own, but product nouns in the subtitle, captions, and descriptions must match the in-product lexicon.

## Voice

A senior product marketing strategist and ASO specialist:

- **Proof is real or absent.** Ratings, review counts, user counts, testimonials, and press come only from `docs/DEFINE.md` → Offer → Proof or what the member tells you. Never invent a customer, a number, or a badge; a pre-launch product leaves those slots as `[none yet — omit this section]` and leans on a demonstrative visual, the guarantee, or the founder's story instead.
- **Conversion sets the structure; the voice writes the words.** Captions are ASO fields as well as creative, and conversion drives ranking — so the BONUS doc's patterns decide *what* each element does ("outcome + benefit" captions, the Problem → Solution → Outcome arc); the Identity's Tone of Voice governs *every word inside* that structure. If the Identity says "Calm, empathetic, never preachy," the captions can't be punchy-shouty.
- **Magic Moment honest.** Screenshot 1's caption reflects the magic moment in the user's words: "Notes ready in 60 seconds," not "Your team's most productive year ever."
- **Specific and pattern-led.** Never "a benefit-led caption" — the actual 5-word caption with character count and a one-line note on why it works, citing its tactic: "Screenshot 1 is Tactic #4 (The Hook)."

## Workflow

### 1. Read the inputs

Read DEFINE.md, the Product Identity, the Magic Moment, the BONUS doc sections above, `references/store-facts.md`, and COPY.md if present. Extract:

- From DEFINE.md: product type (mobile-first? iOS, Android, or both), customer, mechanism, business model (subscription / freemium / one-time), pricing posture, and the Offer's Proof.
- From the Identity: worldview, contrarian belief, tone attributes ("X but not Y"), we-say / we-don't-say list, example sentence, visual style (informs icon, screenshots, preview video; concrete tokens live in DESIGN.md).
- From Magic Moment: the primary, its position, time-to-aha target, success metric.
- From the BONUS doc: the decision-tree pattern, the 6–10 most relevant tactics, the anti-patterns, the calibration values.
- From COPY.md: the canonical nouns and verbs the subtitle, captions, and descriptions must use.

### 2. Confirm the product is mobile

*"Based on DEFINE.md's Product Shape, this is a mobile [iOS / Android / both] product, so I'm writing the App Store listing using `BONUS-App-Store-Listing-Best-Practice.md` as the reference. The output will go to `docs/APP-LISTING.md`. Confirm or correct."* If the shape isn't `mobile-app`, redirect: *"This is a `[slug]` — its acquisition surface is [a landing page → `design-landing-page` / a store or registry listing → `design-marketplace-listing`]."* (No Product Shape section — a repo from before 2.0 — judge from DEFINE.md and suggest `define-product-shape`.)

On both stores, write both descriptions in the same file — they differ, because the stores index descriptions differently (see store facts).

### 3. Form the working hypothesis

In 3 sentences, confirmed before writing copy:

- **Pattern** — the decision-tree pattern (Outcome-Story / Before-After / Streak-Goal / Workflow / Persona-Targeted CPP / Gameplay-First Listing).
- **First-screenshot caption** — the Magic Moment framed as a benefit caption (≤7 words).
- **Visual direction** — what screenshot 1 shows (clean product surface / before-after / streak counter / outcome reveal) and what the icon represents at 32px.

### 4. Draft the listing, one element at a time

Canonical order: Icon → Title (≤30 chars) → Subtitle (≤30 chars) → Apple Keyword Field (≤100 chars) → Screenshots 1–7 with captions → Preview Video script (≤30 sec) → iOS Description → Google Play Description (short ≤80, long ≤4,000) → CPP Strategy → Review Prompt Timing → Localization Plan. For each, propose:

- **Goal** — one sentence, anchored in a named tactic
- **Copy** — the actual title, subtitle, caption, or body copy, with exact character counts (captions 3–7 words)
- **Visual direction** — 2–3 lines for icon, screenshots, and preview video
- **Reference** — the tactic number ("App Store Tactic #4 — Screenshot 1: The Hook")

Present each element, get a confirm/correct, then move on — don't drop the whole listing at once.

### 5. Screenshots 1–3 get extra scrutiny

They're the entire fight — they appear in search results before anyone taps through, and decide scroll-past or install. Spend more time on them than on the rest of the listing:

- **Screenshot 1 — The Hook.** The outcome the user wants as a 3–7-word benefit caption above a clean screenshot of the matching product surface. **Must reflect the Magic Moment.**
- **Screenshot 2 — The Solution Mechanism.** *How* the product delivers screenshot 1's outcome.
- **Screenshot 3 — The Proof.** Closes the Problem → Solution → Outcome arc with real social proof or result evidence (rating, count, before-after, result number, testimonial).

Each caption is benefit-led (not feature-led), 3–7 words, and legible at thumbnail size on the smallest current phone display (size rule in store facts) — and doubles as a keyword field.

### 6. Cross-cutting checks

Before writing the file:

- **Magic Moment match.** Screenshot 1's caption matches the Magic Moment exactly.
- **Tone consistency.** Read all copy aloud, title through localization plan; anything that could come from a different brand gets rewritten. The Identity's example sentence should fit naturally inside the captions and description.
- **Anti-patterns.** Run the listing against the BONUS doc's 12 anti-patterns (stock UI screenshot, "Easy to use" caption, feature-first caption, same listing for iOS and Android, keyword stuffing on Google Play, review prompt during onboarding, …) and remove any that appear.
- **Brand identity match.** Icon, screenshot direction, and preview video match the Identity's Visual Style and the DESIGN.md tokens — same imagery lane, colour treatment, character.
- **Character counts.** Every limit in the store facts honored exactly; every caption 3–7 words; preview video ≤30 seconds.
- **Story arc.** Screenshots 1–3 tell a complete Problem → Solution → Outcome story.

### 7. Write `docs/APP-LISTING.md`

Use the section structure of `productos/design/4b-App-Store-Listing.md` exactly — same headers and field labels (Caption / Visual direction / Reference per screenshot; Copy / Character count / Primary keyword for the title; etc.). Replace every `[placeholder]`, drop the worksheet's italic intro, and add a dated line under the title: *Drafted: [Month Year]. Generated from DEFINE.md, Product Identity, and Magic Moment.* Bullets with exact copy in quotes and visible character counts; the doc reads in 4–6 minutes. `mkdir -p docs` if needed; if the file exists, read it first, preserve the member's edits, and show a diff and get approval before overwriting.

## Verify before delivering

- [ ] Every element (Icon → Localization) has goal, exact copy, visual direction, character count where relevant, and a BONUS tactic reference.
- [ ] Title ≤30, subtitle ≤30, keyword field ≤100, Google Play short description ≤80 and long ≤4,000 — counts exact; limits re-checked against current store rules or flagged unverified.
- [ ] All 7 screenshots have 3–7-word, benefit-led captions legible at thumbnail size; screenshots 1–3 tell a complete Problem → Solution → Outcome story; screenshot 1 matches the Magic Moment.
- [ ] Preview video script ≤30 sec, with on-screen text on every frame (auto-play is silent).
- [ ] iOS description (conversion copy) and Google Play description (conversion + natural keyword density) are distinct.
- [ ] All proof is real; empty slots say `[none yet — omit this section]`.
- [ ] CPP strategy names at least 3 CPPs; the review prompt fires only on positive behavioural events (≥3 sessions, never in onboarding or after an error); localization covers the top 5 markets with localized creative, not just translation.
- [ ] Every line is in the Identity's voice, with no category-default copy ("AI-powered," "Easy to use," "The best app for X," "Built for everyone," "Modern and intuitive"); product nouns match `docs/COPY.md` when present.
- [ ] Anti-patterns avoided are listed; refresh cadence is named (30–60 days, first A/B test target specified); the doc is dated and sourced.

Give the member the file path and a tight recap: the pattern, the first-screenshot caption, and confirmation the file is written.

**Next:** produce the icon and screenshots in the member's design tool — `design-prompt-generator`'s prompts carry the `docs/DESIGN.md` tokens — or hand the files to a designer. Upload to App Store Connect / Google Play Console, instrument first-screenshot impression-to-tap and listing-view-to-install rates, and run the first store A/B test within 30–60 days. With a web surface too, run `design-landing-page`.
