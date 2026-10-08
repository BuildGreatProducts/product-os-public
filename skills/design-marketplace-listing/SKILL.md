---
name: design-marketplace-listing
description: >-
  Writes a listing for every store, marketplace, registry, or directory the product's shape needs —
  Chrome Web Store, plugin marketplaces, MCP registries, assistant and Slack directories, VS Code,
  npm, Gumroad and the like — with name, one-line pitch within the field limit, description, tags,
  visuals brief, install steps, pricing display, and the store's review checklist, to
  docs/MARKETPLACE-LISTING.md. Design phase Step 7. Use when the user says "write my store
  listing", "list my MCP server", or "write my plugin listing". Not for the App Store or Google Play
  — use design-app-listing.
---

# Design: Marketplace Listing

Write the **store, marketplace, registry, and directory listings** a product's shape needs — everywhere except the App Store and Google Play — as one spec at `docs/MARKETPLACE-LISTING.md`, with one section per listing, primary store first. Each section carries exact copy within the store's current limits, a visual brief sized to its specs, a tested install and first-run block, the pricing as that store displays it, and a pre-submission checklist built from the store's own policy. The job is to align strategy (DEFINE.md), voice (the Identity), and activation (the Magic Moment) inside each store's fields: without the Magic Moment the one-liner promises something the first run doesn't deliver; without current store facts the listing gets truncated or rejected.

## Inputs

Read inputs from `docs/` at the app repo root; the worksheet and BONUS doc are linked below.

1. **`docs/DEFINE.md`** — **required.** Offer (Customer, Pain, Mechanism, Guarantee, Proof), `## Product Shape` (Primary Shape and platform, Secondary Shapes, Live Means), and Pricing Strategy (model, plans, prices). If the Offer or Pricing is a placeholder, stop and point to the Define skills (`define-offer-builder` → `define-customer-persona` → `define-pricing`, or `define-from-code`). No Product Shape section (a repo from before 2.0) → ask which store the product ships to, and suggest `define-product-shape`.
2. **The shape file** — read only the Design route row for Step 7 in `productos/shapes/<slug>.md` (from this folder, `../../shapes/<slug>.md`), plus each secondary shape's row. It names the acquisition surfaces; if it names a landing page or app listing too, those come from `design-landing-page` and `design-app-listing`. If `docs/PLAN.md` schedules the step differently, the plan wins — say so.
3. **Product Identity** — `docs/DESIGN.md` → `## Product Identity`. **Required.** Tone of Voice governs every word; Visual Style and any tokens brief the icon and visuals. If missing, stop and point to `design-identity-creator`.
4. **`docs/MAGIC-MOMENT.md`** — **required.** The one-line pitch and the first visual are the magic moment framed as a benefit. If missing, stop and point to `design-magic-moment`.
5. **`docs/COPY.md`** — optional. Product nouns, command and tool names in the listing must match its lexicon.
6. **`docs/ONBOARDING.md`** — optional. The install and first-run block must match its first steps exactly.
7. **[BONUS-Marketplace-Listing-Best-Practice.md](../../design/BONUS-Marketplace-Listing-Best-Practice.md)** — **required.** Read **The Meta-Rule**, **The Decision Tree**, **The 12 Tactics** (cited by number), **Anti-Patterns**, and **Calibration** — then, from **Store Reference**, only the sections for the stores this product lists on.
8. **[4c-Marketplace-Listing.md](../../design/4c-Marketplace-Listing.md)** — the worksheet holding the output structure and Good/Bad calibration. Read it; never write to it.

## Voice

A senior product marketer who has shipped listings on many stores and been rejected by most of them once:

- **Limits are law.** Every field has its exact character count beside it; nothing is "about right".
- **Proof is real or absent.** Ratings, install counts, testimonials, and logos come only from DEFINE.md → Proof or the member. Pre-launch slots say `[none yet — omit]`.
- **Store-literate.** Each store has a different reader — a developer scanning a README, a buyer comparing preview images, a reviewer with a checklist. Adapt emphasis per store; never paste one listing everywhere.
- **Specific and pattern-led.** Never "a strong one-liner" — the actual line, its count, and the tactic it implements: "Pitch is Tactic #2 — 118/132."

## Workflow

### 1. Read the inputs

Read DEFINE.md (Offer, Product Shape, Pricing), the shape file's Step 7 rows, the Identity, the Magic Moment, COPY.md and ONBOARDING.md if present, and the BONUS doc's general sections. Extract the customer, outcome, mechanism, proof, pricing, the magic moment, the tone attributes and no-go words, and the lexicon.

### 2. Pick the listings

Propose the list from the shape file's Step 7 row and the BONUS **Decision Tree** — primary shape first, then secondary shapes — and confirm: *"Your shape is `mcp-server`, so I'll write the official MCP Registry entry first, then the npm README, then the Claude connectors directory submission. Add or drop any?"* A mobile app's store listing redirects to `design-app-listing`; a website goes to `design-landing-page`.

### 3. Verify the store facts

For each chosen store, read its Store Reference section, then re-check the limits, asset specs, fees, and policies against the store's current official docs by web search. Record what changed and the date checked in the file's Listings table. Without web search, use the reference's figures and mark every count *unverified*.

### 4. Form the working hypothesis

In 3 sentences, confirmed before drafting:

- **One-line pitch** — the magic moment as a benefit, inside the primary store's summary limit.
- **Primary keyword** — the buyer's own search term for this store.
- **First visual** — what the magic moment looks like inside the host (the extension's panel on a page, the agent's output in a terminal, the assistant's answer, the template filled in).

### 5. Draft each listing, one field at a time

Start with the primary store; work through the worksheet's fields in order — Name → One-line pitch → Icon → Description → Category, tags, and keywords → Visual assets brief → Install and first-run → Access and data statement → Pricing display → Proof and support → Review and policy checklist. For each field give the exact copy, its count against the limit, and the tactic number; present it and get a confirm or correct before moving on.

Then adapt each secondary store from the primary: keep the promise, re-fit the copy to that store's limits, reader, and formatting, and resize the visuals.

Per-shape emphasis:

- **Package registries, plugin and skill repositories:** the README is the listing — its first screen holds the one-liner, the install line, and a minimal working example; the registry `description` and `keywords` fields mirror it.
- **MCP servers and agent plugins:** the tool, skill, and command descriptions are listing copy too — agents read them to choose. Keep them consistent with COPY.md and the listing.
- **Assistant and workplace directories:** the starters or example commands double as the screenshots; reviewers need a test account and a demo video.
- **Storefronts:** the requirements box (tools, versions, plan level) and the inside preview carry the sale; the thank-you page and delivery email belong to `docs/ONBOARDING.md`.

### 6. Cross-cutting checks

- **Magic Moment match** — every pitch and every first visual delivers what the first run delivers.
- **Limits** — every field's count is within the verified (or flagged) limit.
- **Pricing** — mirrors `docs/DEFINE.md` → Pricing Strategy exactly, with the store's fee noted.
- **Policy** — every item in the store's checklist is covered or owned by the member with a date.
- **Voice and lexicon** — read every listing aloud; nothing generic ("AI-powered", "the best", "easy to use"); product nouns match COPY.md.
- **Anti-patterns** — none of the BONUS doc's anti-patterns appear.

### 7. Write `docs/MARKETPLACE-LISTING.md`

Use the worksheet's structure exactly — Summary, Magic Moment, Listings table, then one `## Listing — [Store]` section per store with the worksheet's field labels, then Cross-listing consistency, Anti-patterns avoided, Refresh cadence, and Sources. Replace every placeholder, drop the worksheet's italic intro, Good/Bad lines, and per-section instructions, and add under the title: *Drafted: [Month Year]. Generated from DEFINE.md, Product Identity, and Magic Moment. Store facts checked [date] — re-verify before submitting.* `mkdir -p docs` if needed; if the file exists, read it first, preserve the member's edits, and show a diff and get approval before overwriting.

## Verify before delivering

- [ ] Every listing the shape's Step 7 row names (and every secondary shape's) has a section, primary first, or the member chose to drop it.
- [ ] Every field has exact copy and a count against a limit checked on the store's current docs — or is marked unverified.
- [ ] Each one-line pitch names the customer and the outcome; the first visual shows the magic moment in the host.
- [ ] Install and first-run blocks are exact, match `docs/ONBOARDING.md`, and are tested or flagged "to test before submission".
- [ ] Every permission or scope has a justification; pricing mirrors DEFINE.md with the store's fee noted.
- [ ] All proof is real or `[none yet — omit]`; every store has a pre-submission checklist from its own policy.
- [ ] Copy is in the Identity's voice, adapted per store rather than pasted, with product nouns matching `docs/COPY.md` when present; the file is dated and sourced.

Give the member the file path and a tight recap: the listings written, the one-line pitch, and which store facts are unverified.

**Next:** produce the visuals — `design-prompt-generator`'s prompts carry the `docs/DESIGN.md` tokens, or hand the brief to a designer — test every install line on a clean setup, then submit the primary listing first. Store launch and ranking work continues in `distribute-gtm-strategy`.
