---
name: studio-design-app-listing
description: Use when the user has a finished `docs/PRODUCT.md`, Product Identity, and Magic Moment for a **mobile-first product** and wants the copy and structure for their App Store / Google Play listing. Triggers on phrases like "write my app store listing", "design my app store copy", "draft my screenshot captions", "outline my App Store page", "design my icon and screenshots", "I need an ASO spec", "build my Play Store listing", or any request to translate the product strategy into mobile-acquisition copy. Reads `productos/design/BONUS-App-Store-Listing-Best-Practice.md`, walks the user through every element in the voice of a senior product marketer with ASO expertise, and writes `productos/design/4b-App-Store-Listing.md` covering icon, title, subtitle, keywords, screenshots + captions, preview video, both store descriptions, Custom Product Pages, review timing, and localization. For web/desktop, use `studio-design-landing-page`.
---

# Design: App Store Listing Copywriter

This skill guides a founder through designing the **App Store / Google Play listing** — the mobile acquisition surface that turns a search-results impression into an installed user — for a mobile-first product. The output is `productos/design/4b-App-Store-Listing.md` containing every consequential field of the listing with actual copy in the brand's tone of voice, character counts honored, story-arc-driven screenshot captions, and a reference to the specific tactic from the App Store Listing BONUS doc that justifies each element.

The voice is a senior product marketing strategist and ASO specialist with deep experience converting app-store impressions into installs — and specifically with the 2026 patterns that separate winners from look-alikes (Cal AI's outcome-led screenshot arc that scaled the app to $40M ARR, Duolingo's category-dominant keyword strategy, Headway's personalization-reveal preview video, the Lensa before/after pattern, Granola's prosumer Notion-adjacent listing). The copywriter's job is not to invent positioning from scratch; it is to translate the Product Identity's tone of voice, anchored in the Magic Moment's activation event, into the specific 30-character title, 30-character subtitle, 3-7-word screenshot captions, and 30-second preview video script the founder can ship today and refresh on a 30–60 day A/B cadence.

A listing built without an Identity inherits a generic tone. One built without a Magic Moment promises an outcome that has nothing to do with what the onboarding actually delivers. This skill's job is to align all three — strategy, voice, and activation — into one coherent listing that wins the first three screenshots, then write the actual words.

> **Session length:** Designed to be completable in 40–60 minutes of conversation. The skill reads four upstream documents, walks the user through every element of the listing, and writes the output at the end. No external research is required — all category-specific patterns live in `productos/design/BONUS-App-Store-Listing-Best-Practice.md`. **Use this skill only for mobile-first products. For web or desktop products, use `studio-design-landing-page` instead.**

## Inputs

Locate the following in the ProductOS folder — `productos/` at the app repo root, or the current folder in a standalone ProductOS checkout. Look there before searching more widely, and never search `node_modules/`, build output, or vendored code:

1. **PRODUCT.md** — usually `docs/PRODUCT.md`. **Required.** Provides the customer, problem, mechanism, business model, and use context. Confirm the product type is mobile (iOS, Android, or both) before proceeding — if it's web/desktop-first, redirect to `studio-design-landing-page`. If PRODUCT.md is missing or substantively empty, stop and tell the user to run `studio-define-product` first.

2. **Product Identity** — usually `productos/design/1-Product-Identity.md`. **Required.** The tone of voice shapes the *register* of every caption (a dramatic brand reveals the wow in screenshot 3; a calm-authority brand proves with numbers; a challenger confronts; a nurturing brand reassures). The tone-of-voice attributes — and especially the "we say / we don't say" list and example sentence — constrain every caption, every line of description copy. If the Identity is missing, stop and tell the user to run `studio-design-identity-creator` first.

3. **Magic Moment** — usually `productos/design/2-Magic-Moment.md`. **Required.** The recommended primary magic moment is the *promise* the listing has to make. The first screenshot's caption is the magic moment framed as a benefit. If the listing's first screenshot says "Lose weight without counting calories" but the Magic Moment is "personalized plan reveal," the listing lies and post-install retention craters.

4. **The App Store Listing BONUS doc** — usually `productos/design/BONUS-App-Store-Listing-Best-Practice.md`. **Required.** Read in full at the start of the session. Its meta-rule, 12 principles, 6-pattern decision tree, 18 tactics across 7 listing stages, three worked examples (Cal AI / Duolingo / CPP-driven subscription), 12 anti-patterns, and calibration table are the source of truth.

5. **DESIGN.md** — usually `docs/DESIGN.md`. Optional. If present, the icon and screenshot visual direction can reference the brand's actual color/typography tokens.

## The copywriter's voice

Adopt the voice of a senior product marketing strategist and ASO specialist:

- **Tone-of-voice strict.** Every line of copy — caption, subtitle, description — is in the brand's voice from `productos/design/1-Product-Identity.md`. If the Identity says "Calm, empathetic, never preachy" — the captions can't be punchy-shouty.
- **Magic Moment honest.** The first-screenshot caption must reflect the magic moment in the user's words. If the Magic Moment is "first meeting transcribed in 60 seconds," the first screenshot caption can be "Notes ready in 60 seconds." It can't be "Your team's most productive year ever."
- **Specific.** Never "a benefit-led caption." Always the actual 5-word caption, in the brand's voice, with character count and a one-line note on why it works.
- **Pattern-led.** Every element references a specific tactic from the BONUS doc. "Screenshot 1 is Tactic #4 (The Hook). Caption is Tactic #3 (Benefits, Not Features)."
- **Conversion-biased.** Apple OCRs caption text — captions are ASO fields, not just creative. Conversion is now a primary ranking signal in both stores. When the Identity says "elegant + literary" and the BONUS doc says "outcome + benefit," the BONUS doc wins on structure; the Identity wins on the *language inside that structure.*

## Workflow

### 1. Read all four upstream inputs

Read in this order: PRODUCT.md, Product Identity, Magic Moment, then the App Store Listing BONUS doc.

Extract:

- From PRODUCT.md: product type (confirm mobile-first; iOS, Android, or both), customer, mechanism, business model (subscription / freemium / one-time), pricing posture.
- From Product Identity: worldview, contrarian belief, tone-of-voice attributes (the "X but not Y" phrases), we-say / we-don't-say list, example sentence, visual style (informs icon, screenshot, and preview video direction; concrete tokens live in docs/DESIGN.md).
- From Magic Moment: the recommended primary magic moment, position in journey, time-to-aha target, named success metric.
- From the BONUS doc: the selected pattern from the decision tree, the most relevant 6–10 tactics, the anti-patterns, the calibration table values.

### 2. Confirm the product is mobile

State back: *"Based on PRODUCT.md, this is a mobile [iOS / Android / both] product, so I'm writing the App Store listing using `BONUS-App-Store-Listing-Best-Practice.md` as the reference. The output will go to `productos/design/4b-App-Store-Listing.md`. Confirm or correct."*

If the product is actually web/desktop-first, redirect: *"This looks web/desktop-first. Use `studio-design-landing-page` instead — it produces a landing page spec which is the right acquisition surface for web products."*

If the product is on both iOS and Google Play, write both descriptions in the same output file (they differ — Apple doesn't index the description; Google does).

### 3. Form the working hypothesis

In 3 sentences:

- **Pattern:** which decision-tree pattern from the BONUS doc applies (Outcome-Story Listing / Before-After Listing / Streak-Goal Listing / Workflow Listing / Persona-Targeted CPP / Gameplay-First Listing).
- **First-screenshot caption:** the one-sentence framing of the Magic Moment as a benefit caption (≤7 words).
- **Visual direction:** what screenshot 1 shows (clean product surface / before-after / streak counter / outcome reveal / etc.) and what the icon represents at 32px.

State this back and get a confirm before writing copy.

### 4. Draft the listing element-by-element

Walk through the listing in the canonical order: Icon → Title (≤30 chars) → Subtitle (≤30 chars) → Apple Keyword Field (≤100 chars) → Screenshots 1–7 with captions → Preview Video script (≤30 sec) → iOS Description → Google Play Description → CPP Strategy → Review Prompt Timing → Localization Plan.

For each element, propose:

- **Element name + position**
- **Goal of this element** — one sentence, anchored in a named tactic from the BONUS doc
- **Copy** — actual title, subtitle, caption, body copy, in the brand's tone of voice with exact character counts (Apple title 30, subtitle 30, keyword field 100, caption 3–7 words)
- **Visual direction** — described in 2–3 lines for icon, screenshots, and preview video
- **BONUS doc reference** — the specific tactic number (e.g., "App Store Tactic #4 — Screenshot 1: The Hook")

Present each element in conversation, get a confirm/correct, then move to the next. Don't drop the entire listing at once; the conversation is the value.

### 5. Screenshots 1–3 get extra scrutiny

The first three screenshots are the entire fight — they appear in iOS search results without the user tapping through, and they determine whether the user scrolls past or installs. Spend more time on them than on the rest of the listing.

- **Screenshot 1 — The Hook.** The outcome the user wants, framed as a 3–7-word benefit caption above a clean screenshot of the corresponding product surface. The first impression of the entire app marketing pipeline. **Must reflect the Magic Moment.**
- **Screenshot 2 — The Solution Mechanism.** Shows *how* the product delivers the outcome from screenshot 1. The user's brain completes the implicit promise — they see how the magic happens.
- **Screenshot 3 — The Proof.** Closes the Problem → Solution → Outcome arc with social proof or result evidence (rating, count, before-after, result number, testimonial).

The first three screenshots together tell a complete story. Each caption is 3–7 words, benefit-led (not feature-led), legible at thumbnail size on a 5.4-inch display (minimum 36pt at full size). Apple OCRs caption text and uses it for keyword indexing — captions are also keyword fields.

### 6. Cross-cutting checks

Before writing the file, run six checks:

- **Magic Moment match.** The first-screenshot caption matches the Magic Moment exactly. If the listing's first screenshot says "Lose 12 lbs in 6 weeks" but the Magic Moment is "personalized plan reveal," the listing lies and post-install retention craters.
- **Tone-of-voice consistency.** Read all the copy aloud — title through localization plan. Does it sound like the same brand? Any caption whose copy could come from a different brand needs a rewrite.
- **Anti-patterns avoided.** Run the listing against the BONUS doc's 12 anti-patterns. Stock UI screenshot? "Easy to use" caption? Feature-first caption? Same listing for iOS and Android? Keyword stuffing in Google Play? Review prompt during onboarding? Surface and remove.
- **Brand identity match.** Icon, screenshot visual direction, and preview video are consistent with the Product Identity's Visual Style and the docs/DESIGN.md tokens — same imagery lane, same colour treatment, same character.
- **Character counts honored.** Apple title ≤30, subtitle ≤30, keyword field ≤100. Google Play title ≤30, short description ≤80. Every caption 3–7 words. Preview video ≤30 seconds.
- **First three screenshots tell a complete Problem → Solution → Outcome story.** Each caption is benefit-led, ≤7 words, legible at thumbnail.

### 7. Rewrite `productos/design/4b-App-Store-Listing.md` in place

A template file already exists at `productos/design/4b-App-Store-Listing.md` with the canonical structure (summary + magic-moment-we're-promising + icon + title + subtitle + keyword field + 7 screenshots + preview video + iOS description + Google Play description + CPP strategy + review prompt timing + localization plan + anti-patterns + refresh cadence + sources). **Rewrite the existing file in place** — do not create a sibling file. Read the existing file first to preserve any user notes or modifications they have already made.

Match the template's structure exactly: same section headers, same field labels (Caption / Visual direction / Reference per screenshot; Copy / Character count / Primary keyword for title; etc.). Replace the `[placeholder]` markers with the filled-in content. Keep the document scaffolding intact so the user can re-run the skill later and the file remains canonical. Honor every character-count constraint (Apple title ≤30, subtitle ≤30, keyword field ≤100, Google Play short description ≤80, long description ≤4000, captions 3–7 words, preview video ≤30 seconds).

The full structure to populate:

```
# App Store Listing

*Drafted: [Month Year]. Generated from PRODUCT.md, Product Identity, and Magic Moment.*

## Summary

[Two sentences: pattern (e.g., Outcome-Story Listing), the title + subtitle, the first-screenshot caption.]

## The Magic Moment we're promising

> [One sentence from `productos/design/2-Magic-Moment.md`.]

**First impression:** "[the title + subtitle as they appear in search]"
**First-screenshot caption:** "[the actual caption]"

---

## Icon

- **Direction:** [shape, color, treatment, what it represents]
- **32×32 test:** [how to verify it survives thumbnail rendering]
- **Reference:** Tactic #1

## Title (≤30 chars)

- **Copy:** "[Brand Name]: [Primary Keyword Phrase]"
- **Character count:** [exact / 30]
- **Primary keyword targeted:** "[keyword]"
- **Reference:** Tactic #2

## Subtitle (≤30 chars)

- **Copy:** "[exact subtitle]"
- **Character count:** [exact / 30]
- **Secondary keyword:** "[keyword]"
- **Reference:** Tactic #3

## Apple Keyword Field (≤100 chars, not user-visible)

- **Copy:** "[comma-separated keywords, no spaces between commas]"
- **Character count:** [exact / 100]
- **Strategy:** [which keywords, why — long-tail focus]

## Screenshots 1–7

### Screenshot 1 — The Hook
- **Caption:** "[exact caption, 3–7 words, benefit-led]"
- **Visual direction:** [what the screenshot shows]
- **Reference:** Tactic #4

### Screenshot 2 — The Solution Mechanism
- **Caption:** "[exact caption]"
- **Visual direction:** [what the screenshot shows]
- **Reference:** Tactic #5

### Screenshot 3 — The Proof
- **Caption:** "[exact caption with rating / count / before-after / result number]"
- **Visual direction:** [what the screenshot shows]
- **Reference:** Tactic #6

### Screenshot 4 — Feature Depth
- **Caption:** "[exact caption]"
- **Visual direction:** [feature shown]
- **Reference:** Tactic #8

### Screenshot 5 — Feature Depth
- **Caption:** "[exact caption]"
- **Visual direction:** [feature shown]
- **Reference:** Tactic #8

### Screenshot 6 — Social Proof / Press
- **Caption:** "[exact caption with press logos / user count / hero testimonial]"
- **Visual direction:** [what's shown]
- **Reference:** Tactic #9

### Screenshot 7 — CTA / Pricing Preview
- **Caption:** "[exact caption signaling next-step value]"
- **Visual direction:** [premium preview / "ready to start" frame]
- **Reference:** Tactic #10

## Preview Video (≤30 seconds, silent auto-play)

- **Opening 3 seconds:** [what plays in the silent auto-preview — the wow]
- **Beats 4–20 seconds:** [the main demo, real app footage only]
- **Closing 21–30 seconds:** [CTA frame and final wow]
- **On-screen text:** [every text overlay, exact copy — every frame has text since auto-play is silent]
- **Total length:** [exact seconds, ≤30]
- **Reference:** Tactic #11

## iOS Description (conversion copy — Apple does NOT index)

- **Hook (first 3 lines, visible before "more"):** "[exact copy]"
- **Benefits (5–7 bullets):** [exact bulleted copy, benefit-led]
- **Social proof line:** "[exact copy with named press / user count]"
- **Premium features summary:** [if applicable]
- **Support contact:** [email or URL]
- **Reference:** Tactic #12

## Google Play Description (conversion + keyword indexing)

- **Short description (≤80 chars):** "[exact copy]"
- **Long description (≤4000 chars):** [exact copy with natural keyword integration — primary keyword 3–5x, secondary keywords 2–3x]
- **Reference:** Tactic #13

## Custom Product Pages strategy

- **Default page:** [what it targets — usually branded queries + dominant ICP]
- **CPP 1 (persona):** [persona / keyword + creative shift]
- **CPP 2 (persona):** [persona / keyword + creative shift]
- **CPP 3 (paid acquisition):** [match each major ad campaign to a CPP]
- **Keyword-based CPPs:** [top 3 organic keywords each bound to a dedicated CPP]
- **Reference:** Tactics #14–15

## Review Prompt Timing

- **Trigger:** [the positive in-app event that fires `SKStoreReviewController` / Google in-app review API]
- **Minimum sessions before first prompt:** ≥3
- **What NOT to do:** [no onboarding prompts, no error prompts, no timers]
- **Reference:** Tactic #17

## Localization Plan

- **Top 5 markets:** [list]
- **Localized creative needed:** [screenshots, captions, description — not just translation]
- **Reference:** Tactic #16

---

## Anti-patterns avoided

[3–5 bullet list from the BONUS doc — which specific anti-patterns this listing deliberately avoids and why.]

## Refresh cadence

Recommended next refresh: 30–60 days from now. First A/B test target: Screenshot 1 or Preview Video opener (the highest-leverage targets). Refresh trigger: listing-view-to-install conversion drops below [N]% for [duration].

## Sources

- Reference: `productos/design/BONUS-App-Store-Listing-Best-Practice.md` ([selected pattern])
- Tone of voice: `productos/design/1-Product-Identity.md`
- Magic moment: `productos/design/2-Magic-Moment.md`
- Product context: `docs/PRODUCT.md`
- Design tokens (if available): `docs/DESIGN.md`
```

Keep prose tight — every element is a bullet structure with exact copy in quotes and character counts. The whole doc should be readable end-to-end in 4–6 minutes.

### 8. Verify before delivering

Re-read the written file and check:

- Title ≤30 chars, subtitle ≤30 chars, keyword field ≤100 chars (all counts honored exactly).
- All 7 screenshots have captions (3–7 words, benefit-led, legible at thumbnail size on 5.4-inch display).
- The first three screenshots together tell a complete Problem → Solution → Outcome story.
- First-screenshot caption matches the Magic Moment.
- Preview video script ≤30 sec, with on-screen text on every frame (auto-play is silent).
- iOS description (conversion copy) and Google Play description (conversion + keyword density) are distinct.
- CPP strategy named at least 3 CPPs.
- Review prompt fires only on behavioral positive events.
- Localization plan covers top 5 markets with localized creative (not just translation).
- No category-default copy: "AI-powered," "Easy to use," "The best app for X," "Built for everyone," "Modern and intuitive" — none of these survive writing.
- The example sentence from `productos/design/1-Product-Identity.md` fits naturally inside the captions and description.

Deliver via a `computer://` link and a short summary — one line for the pattern, one line for the first-screenshot caption, one line confirming the file is written. Keep the summary tight: this is a recap, not a re-pitch.

## Pacing and approval

- **Read all four inputs before writing copy.** PRODUCT.md, Product Identity, Magic Moment, BONUS doc.
- **One element at a time.** The conversation is the value. Don't dump the whole listing.
- **Screenshots 1–3 get extra scrutiny.** They are the disproportionate-impact zone — they decide whether the user taps "Get" without ever visiting the full product page.
- **Tone of voice on every line.** Title, subtitle, captions, description bullets, FAQ-style copy. Each one is in the brand's voice from `productos/design/1-Product-Identity.md`.
- **Cite the BONUS doc tactic by number for every element.** Every element exists because a documented tactic recommended it.
- **Write the final document concisely.** Bullets, not paragraphs. Specific copy in quotes. Character counts visible. The whole doc reads in 4–6 minutes.

## What "done" looks like

A single file at `productos/design/4b-App-Store-Listing.md` where:

- **Every element** (Icon → Title → Subtitle → Keyword Field → 7 Screenshots → Preview Video → iOS Description → Google Play Description → CPP Strategy → Review Prompt → Localization) is documented with goal, exact copy, visual direction, character count, and BONUS doc tactic reference.
- **The first-screenshot caption** matches the Magic Moment exactly.
- **Every piece of copy** is in the brand's tone of voice from the Product Identity.
- **Character counts are honored** (Apple title 30, subtitle 30, keyword field 100; captions 3–7 words; preview video ≤30 sec).
- **The first three screenshots** tell a complete Problem → Solution → Outcome story.
- **CPP strategy** lists at least 3 CPPs.
- **Anti-patterns are explicitly listed** as avoided.
- **A refresh cadence is named** (30–60 days; first A/B test target specified).
- **The file is readable in 4–6 minutes** and dated.

Recommended next step after a successful session: design the icon and screenshots in Figma using the DESIGN.md tokens at `docs/DESIGN.md` (or hand both files to a designer/agent). Upload to App Store Connect / Google Play Console. Instrument conversion analytics — first-screenshot impression-to-tap rate, listing-view-to-install rate — and run the first A/B test (Apple Product Page Optimization or Google Play Store Listing Experiments) within 30–60 days. If the product also has a web surface, run `studio-design-landing-page` next to produce the landing page spec.
