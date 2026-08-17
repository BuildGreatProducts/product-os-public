---
name: studio-define-pricing
description: Use when the user has filled out their Product Offer (and ideally their Customer Persona) and needs one honest launch price fast — enough to make a real ask this week, with no heavyweight strategy work. Triggers on phrases like "what should I charge", "pick my launch price", "pricing strategy", "put a price on it", "how much is this worth", "what's my price line", "price for my mini-launch", or any request to fill in a four-section Pricing Strategy (Who Pays, Launch Price, Price Anchors, Your Price Line). Reads the Product Offer and Customer Persona, researches 2–3 real anchor prices, and produces a filled-in Pricing Strategy document in a 20–30 minute session. Deliberately the week-one slice of pricing — the full ladder, cost & margin, and revenue model live in the optional Business Strategy Deep Dive (studio-define-business-strategy). Especially appropriate in a ProductOS Define workflow, immediately before the Mini-Launch.
---

# Define: Pricing Strategy

This skill puts **one honest price** on the user's product — fast. It turns a filled-in Product Offer (and Persona, if available) into a four-section **Pricing Strategy**: who pays, one launch price said out loud, 2–3 real anchors, and the plain-English price line that carries the number into the Mini-Launch.

The goal is deliberately **not** a complete monetization model. That work — pricing ladder, tiers, cost & margin, revenue-model coherence — lives in the optional `BONUS-Business-Strategy-Deep-Dive.md` (filled by `studio-define-business-strategy`), which most people don't need until the money questions get real — typically before spending on paid channels in Distribute. This skill exists because the Mini-Launch (the next step in the Define checklist) needs a price to carry, and founders will happily spend three weeks "figuring out pricing" as a way of not talking to anyone. Twenty to thirty minutes, one number, done.

A price the founder has never said out loud is not a price — it's a guess hiding in a spreadsheet. The measure of success for this session is that the user can finish the sentence *"it'll be about ___"* to a stranger without flinching.

> **Session length:** 20–30 minutes. Claude does the anchor-price research live in the session; the user's job is to react and commit. Do not let this session expand into business-strategy territory — if the conversation drifts to tiers, margins, or freemium debates, park it: "that's the optional Business Strategy Deep Dive; right now we need one number you can say this week."

## Inputs

Before starting, locate the following in the ProductOS folder — `productos/` at the app repo root, or the current folder in a standalone ProductOS checkout. Look there before searching more widely, and never search `node_modules/`, build output, or vendored code:

1. **The Product Offer** — usually `1-Product-Offer.md`. The **required** input. The Customer, Outcome, and Mechanism sections drive who pays and what shape the price takes.
2. **The Pricing Strategy template** — usually `3-Pricing-Strategy.md`. Defines the exact output structure, *and is also the file the skill rewrites in place* at the end.
3. **The Customer Persona** — usually `2-Customer-Persona.md`, if filled in. Optional but the single most useful input: willingness-to-pay, anchor products, and budget bucket come from here.

If the Product Offer is missing or mostly empty, stop and point the user to `studio-define-offer-builder` first.

## Workflow

### 1. Form a price hypothesis from the offer

Read the offer (and persona). Extract: who the buyer is (and whether buyer = user), whether the outcome is **continuous** (points to monthly) or **bounded** (points to one-time or pilot), and any willingness-to-pay or anchor data the persona already names. State a one-paragraph hypothesis — buyer, billing shape, price band — and ask the user to confirm or correct before researching.

### 2. Research 2–3 real anchors

Use web search to pull today's actual prices for 2–3 products the persona already pays for or would compare this to. Real numbers from real pricing pages — anchors move, and an outdated anchor produces an outdated price. Note where the user's product should sit relative to each anchor *and why* (replaces it, does one slice of it better, serves a smaller buyer).

### 3. Walk the four sections, in order

**1 Who Pays → 2 Launch Price → 3 Price Anchors → 4 Your Price Line.** For each: propose a specific answer, ask one or two targeted questions, critique drift against the template's `> Good / Bad` lines, and lock it in. Watch for these failure patterns and name them when you see them:

- **The Blank Cheque.** "Everyone" as the buyer. A price needs a budget to come out of; force a named buyer and budget bucket.
- **The Negotiable Range.** "$20–50 depending" — a range is a price you've already agreed to lower. One number.
- **The Freemium Dodge.** "Free for now, we'll monetize later" is not a pricing strategy; it's a way to avoid the scary sentence. The Mini-Launch works *because* the ask is real.
- **The Unspoken Number.** A price the user has never said out loud. Make them type the price line and read it back in the session. If they flinch, that's the fear the Mini-Launch is designed to break — say so.
- **The Free-Tool Anchor.** Anchoring against free products guarantees a race to zero. Anchor against what the customer already *pays* for.

### 4. Rewrite the Pricing Strategy file in place

Rewrite `3-Pricing-Strategy.md` in place — same section headers, same italic prompts, same `> Good/Bad` lines, same shapes table — replacing each `**Your answer:**` block. Add a dated header ("Drafted: [month year]") and a one-line footer noting the anchors' source URLs and the reminder: *"First-pass price for the Mini-Launch — expand into the full ladder via `BONUS-Business-Strategy-Deep-Dive.md` when the money questions get real."* Read the existing file first to preserve any user notes.

### 5. Verify before delivering

Check: buyer is named with a budget bucket; the launch price is **one number** with a billing shape that matches the offer's value shape; anchors are named with current prices; the price line is one sentence a stranger would understand. Then hand off: the recommended next step is always the Mini-Launch (`studio-launch`) — within 48 hours, while the number is still warm.

## Tone and pacing

- **Fast and decisive.** This is the shortest Define session. Propose, confirm, move.
- **Push through the flinch.** Users will hedge on the number. Remind them: this price is a first pass that the market gets to argue with next week — but the argument only happens if there's a number on the table.
- **Park strategy questions.** Tiers, margins, annual discounts, freemium — all real, all later. Name where they live (the optional `studio-define-business-strategy` deep dive) and keep moving.

## What "done" looks like

A rewritten `3-Pricing-Strategy.md` where the buyer and budget are named, the launch price is one number the user has said out loud, the anchors are real and current, and the price line reads as one natural sentence — ready to be dropped into a mini-launch post or DM within 48 hours.
