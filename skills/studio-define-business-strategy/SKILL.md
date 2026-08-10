---
name: studio-define-business-strategy
description: >-
  Use for the optional deep dive into how the product makes money — when the money questions get real: before paid channels in Distribute, at first revenue, or when an investor asks how the model works. Requires a filled-in Product Offer. Triggers on phrases like "build my business strategy", "what's my revenue model", "what are my margins", "what's my unfair advantage", "what's my north star metric", "pricing ladder", "monetization strategy", "business model for my app", or any request to translate a product offer into the five-section Business Strategy (Revenue Model, Pricing Ladder, Cost & Margin, Unfair Advantage, North Star Metric). Reads the Product Offer, researches competitive pricing and benchmarks, then walks the user section by section — proposing hypotheses, critiquing weak choices — and fills in BONUS - Business Strategy Deep Dive.md. A BONUS deep dive, not a checklist step: the week-one pricing pass (studio-define-pricing) covers most people until scaling.
---

# Define: Business Strategy Deep Dive (optional)

This skill is ProductOS's **optional deep dive** — most people run it when the money questions get real (before paid channels, at first revenue, or when an investor asks), not in week one. It turns a filled-in **Product Offer** into a coherent **Business Strategy** by guiding the user, section by section, through the five-element framework — pulling the Revenue Model, Pricing Ladder, Cost & Margin, Unfair Advantage, and North Star Metric out of the offer, researching comparable businesses for calibration, critiquing weak choices against the framework's own "good vs bad" criteria, and producing a finished strategy document.

The goal is not to fill in five boxes. The goal is to make the five answers *lock together* — so the revenue model fits the product's shape, the price reflects the named customer's willingness to pay, the cost structure supports the price, the unfair advantage explains why this isn't cloned in six months, and the north star tracks the leading indicator of all of it. Most first-draft strategies fail not because any single answer is wrong, but because the five don't agree with each other.

A Business Strategy that contradicts itself silently is more dangerous than one that's obviously wrong, because the founder runs on it for a year before the math catches up. This skill's job is to surface the contradictions before they cost twelve months.

> **Session length:** Designed to be completable in 45–60 minutes of conversation. **All competitor pricing research and category benchmarks are Claude's job during the session**, not homework for the user. Cost-per-user numbers don't need to be measured — Claude builds the estimate with the user using category benchmarks (SaaS 70–85% margin, AI apps 40–60%, productized service 40–60% unless solo, marketplaces 20–40% take-rate); the user signs off on the working assumption, which gets re-grounded post-launch with real usage data. Pricing validation conversations are a normal next phase, not a precondition for finishing this skill.

## Inputs

Before starting, locate the following in the ProductOS folder — `productos/` at the app repo root, or the current folder in a standalone ProductOS checkout. Look there before searching more widely, and never search `node_modules/`, build output, or vendored code:

1. **The Product Offer** — usually `1. Product Offer.md`. The **required** input. If sections are blank or vague, stop and ask the user to tighten the offer before proceeding; a business strategy built on a fuzzy offer inherits the fuzziness, and you will spend the whole conversation re-deriving the offer instead of building the strategy.
2. **The Business Strategy Deep Dive template** — usually `BONUS - Business Strategy Deep Dive.md` in the `productos/define/` folder. Defines the exact output structure to follow, *and is also the file the skill rewrites in place* at the end (see step 5).
3. **The Business Strategy examples** — usually `BONUS - Real Business Strategy Examples.md`. Five worked examples across business models (B2B SaaS, indie Mac app, WordPress LTD, productized service, marketplace). Read this once at the start to internalize what "good" looks like across these shapes. Use as **calibration**, never as a script to retrofit the user onto.
4. **The Customer Persona** — usually `2. Customer Persona.md`, if it has been filled in already. Optional, but if present, it is the single most useful input for the Pricing Ladder section — willingness-to-pay, anchor products, and budget bucket all come from here. If it isn't filled in, note that the pricing answers will need extra validation later.
5. **The Pricing Strategy** — usually `3. Pricing Strategy.md`, if filled in (produced by `studio-define-pricing`). The week-one first pass: named buyer, one launch price, real anchors. If present, the Pricing Ladder section *expands* this rather than starting from scratch — the launch price becomes the candidate default tier, and the anchors carry over. Don't relitigate the number unless research or the mini-launch signal argues against it.
6. **The Launch Log** — `docs/LAUNCHES.md` and `productos/define/4. Mini-Launch.md`, if present. Optional but gold: real replies, signups, activated users, and payments from every launch so far, warm/cold labelled. A cold stranger who asked about the price is worth more than any benchmark — read the launch entries before proposing the Pricing Ladder, and cite them when they support (or contradict) a choice.

If any of the required files are missing, ask the user where they live before continuing.

## Workflow

### 1. Absorb the offer and form a working hypothesis

Read the Product Offer end-to-end (and the Customer Persona, Pricing Strategy, and Mini-Launch if available). Extract:

- The customer description and business model implication — B2B SaaS, indie/prosumer app, lifetime-deal/license, productized service, two-sided marketplace, agent-native app, dev tool, consumer subscription, hybrid. The model is the single biggest constraint on every downstream answer.
- The outcome — does it produce **continuous** value (suggests subscription) or **bounded** value (suggests one-time / LTD)?
- The mechanism — does it have **per-user variable cost** (AI tokens, storage, payouts) that has to be priced into the margin?
- The guarantee — does it imply free seats, refunds, or pause-anytime mechanics that shape the pricing ladder?
- The proof — does it imply a distribution channel (audience, App Store, Product Hunt, AppSumo) that becomes part of the unfair advantage?
- (From the Persona, if available) The willingness-to-pay section — acceptable monthly price, ceiling, anchor products, budget bucket.
- (From the Pricing Strategy and Mini-Launch, if available) The launch price already committed to, and any real replies to it — the strongest calibration data in the folder.

From this, form a **working strategy hypothesis** in one paragraph: business model, likely revenue model, likely price band, likely cost-per-user shape, candidate unfair advantage, candidate north star. State this back to the user and ask them to confirm or correct before doing research. A wrong starting hypothesis (e.g., pitching subscription on a bounded-utility product) wastes the entire conversation.

### 2. Research the market shape

Spend real but focused effort here. The Business Strategy's job is to name *real* prices, *real* margins, and *real* moats — and those facts come from comparable businesses, not from the user's gut. Use web search and any connected research tools to investigate:

- **Comparable businesses** — find 3–5 products in the user's category and pull their pricing pages. Note their tiers, their default-tier price point, their annual discount, their free-tier scope. The user's pricing ladder should sit *intentionally* relative to these, not accidentally.
- **Cost benchmarks for the category** — typical gross margin range for the product shape (SaaS ~70–85%, AI apps with API costs often 40–60%, productized services 40–60% unless solo, marketplaces 20–40% take-rate).
- **The named anchor products from the offer or persona** — verify their current prices. Anchors move; an outdated anchor produces an outdated price ceiling.
- **The category's typical north star** — what metric do successful companies in this category track publicly? Loom tracks weekly active creators; indie Mac apps track weekly licenses; marketplaces track GMV. The category usually narrows the choice for you.

Collect 5–8 concrete data points — competitor prices, margin ranges, anchor prices, category-typical north stars — before walking the user through the framework. Note explicitly which points came from research and which still need user validation.

### 3. Walk the user through the strategy, section by section

Go through the template in order: **1 Revenue Model → 2 Pricing Ladder → 3 Cost & Margin → 4 Unfair Advantage → 5 North Star Metric.** The order matters: each answer constrains the next. Pricing a tier above your cost-per-user is impossible if you don't know cost-per-user; picking a north star is meaningless before the revenue model decides what "growth" even means.

For each section:

1. **Propose a hypothesis** based on the offer + persona + research. Be specific — not "subscription" but "recurring SaaS subscription at $19/$49/$99 per month, with the middle tier engineered as the default, modeled on the Linear/Loom shape rather than the MacWhisper one."
2. **Ask 1–3 targeted questions** to confirm, refine, or reject the hypothesis. Don't ask "what's your revenue model" — ask "your outcome reads as continuous value (every-month-better books), which points to subscription rather than one-time. Does that match how you imagine the customer paying, or is there a reason a one-time license fits better?"
3. **Critique weak answers.** Each section in the template has explicit "good vs bad" criteria — quote them when the user's answer drifts. Also watch for the failure patterns below, which are the most common ones across these five sections.
4. **Recommend a sharper version** anchored in the BONUS examples and in research. "Your draft says '$29/month flat.' Compare to FluentBooking's three-tier LTD ladder or Loom's free/$15/~$20/enterprise — both are doing real work that a single flat price isn't. Here's a sharper version: ..."
5. **Do the best you can in the session.** If the user can confirm or correct from memory, great. If they can't (especially common for Cost & Margin pre-launch), accept Claude's research-backed or benchmark-based estimate and tag it `[working assumption — re-ground with real data post-launch]` — then continue. A research-backed strategy tagged for validation is a successful output; the conversation should not stall on data the user can't reasonably have yet.

### 4. Sections that deserve extra scrutiny

A handful of sections do disproportionate damage when they're weak:

- **Revenue Model (section 1).** The single highest-leverage decision in the document. Subscription on a one-shot product, freemium-by-default, or two revenue models in parallel are the usual catastrophes — each costs months of motion before the math catches up. Push hard until the model **matches the product's shape**: continuous value → subscription, bounded utility → one-time, AI-heavy → BYOK or usage cap, network effect → take-rate, human-in-the-loop → productized service.
- **Cost & Margin (section 3).** Especially for AI apps. Pre-launch founders won't have measured cost-per-user yet — that's fine. Claude builds the estimate with the user from category benchmarks (typical AI token cost per active user, per-user storage, payment processing ~3%, email/auth), the user signs off on the working assumption, and the skill flags it for re-grounding post-launch. The non-negotiable is that the user *understands* the equation — what each input is and roughly what it costs. If the resulting gross margin lands under 50% on an AI product, surface this immediately: they're funding the user's foundation-model bill, and no amount of growth fixes that.
- **Unfair Advantage (section 4).** The single most-faked section. "We built it first," "our AI is smarter," "we have better UX," "our team" — none of these are moats; they're hopes. A real unfair advantage compounds with time and use. Push for distribution density, niche expertise, audience, switching costs, cross-product portfolio, open-source community, or counter-positioning. **Naming a moat to *build* over the next 12 months is just as valid a session output as naming one you already have** — it just gets tagged as a build commitment rather than a present-tense claim. Either way, the conversation does not stall; the user leaves with an honest strategic position.
- **Cross-cutting coherence.** After all five sections are drafted, read them as one paragraph. Does the price match the persona's willingness to pay? Does the cost structure support the price? Does the north star track the leading indicator of the revenue model (MRR for subscription, weekly buyers for LTD, active retainers for productized service)? If any pair contradicts, fix the upstream one and rerun the downstream sections.

### 5. Rewrite the Business Strategy file in place

Output: **rewrite `BONUS - Business Strategy Deep Dive.md` in place** with the filled-in answers. Do not create a new file — the user wants the strategy document to be the canonical, living version, not a sibling draft.

Match the template's structure exactly: same section headers, same italic prompts, same `> Good: ... / Bad: ...` guidance lines, same option tables. Replace each `**Your answer:**` block with the filled-in answer. Keep the option tables (Common models, Common shapes, Common unfair advantages, Common north stars by business type) intact — they remain useful when the user revisits the document in three months.

At the top of the rewritten file, add:

- A short **strategy summary** — 2–3 sentences that state the chosen business model, revenue model, default price point, and north star, so a co-founder can read it in 10 seconds.
- A **dated header** — e.g., "Drafted: May 2026"
- A short **evidence footer** — e.g., "Based on: 1 Product Offer, 1 Customer Persona, 4 competitor pricing pages, 0 actual revenue data. Recommended next step: validate price band with 5 customer pricing conversations before launching paid tier."

At the bottom of the rewritten file, add a **Sources** section listing the competitor pricing URLs, margin benchmark references, and any other research used — so the user can re-verify and re-research later. Pricing pages decay; sources let you re-date them.

Because this overwrites the template, **read the existing file first** to preserve any user notes or modifications they have already made to it, and surface any conflicts to the user before writing.

### 6. Verify before delivering

Re-read the rewritten strategy against the framework's "good vs bad" criteria and the failure patterns below. Specifically check:

- Does Revenue Model match the product's shape, or is the user about to sell a subscription on a one-shot product?
- Is the Pricing Ladder anchored on real competitors with real prices? Is the middle tier engineered as the default?
- Can the user recite cost-per-user from memory? Is gross margin in the healthy band for the category?
- Is the Unfair Advantage a real moat (distribution, switching costs, audience, niche expertise, counter-positioning) — or is it "we built it first" with a thesaurus on top?
- Is the North Star **one** metric, with a 90-day target, that the user knows off the top of their head?
- Do the five answers tell **one** story when read in sequence?

Deliver the rewritten file via a `computer://` link and a one-paragraph summary of what is solid and what still needs validation.

## Failure patterns to look for

Common ways a Business Strategy underperforms. Name them when you see them — naming compounds learning:

- **The Freemium Reflex.** "We'll do freemium" picked without a deliberate reason. Freemium is a *distribution mechanic*, not a default; it works when the free tier reaches users the paid tier never could (Loom inside companies, Linear inside teams). If the free tier doesn't introduce paid buyers, it's just a money leak.
- **The Two-Model Trap.** Subscription *and* one-time *and* services, in parallel, "to maximize revenue." Two revenue models means two cost structures, two sales motions, two churn dynamics, and twice the cognitive load. Pick one as primary; the others are at best opportunistic.
- **The Flat-Price Anchor.** A single price point with no tiers. Loses both the price-sensitive buyer (no entry tier) and the high-willingness-to-pay buyer (no expansion tier). The middle-tier-as-default shape exists because it works.
- **The Unbounded-AI-Cost Margin.** AI app priced as if it had zero variable cost. Margin math collapses the day a power user runs 10x the average tokens. Fix with usage caps per tier, BYOK on the top tier, or both.
- **The "Our Team" Moat.** Unfair Advantage is "we have a great team" or "we built it first." Neither survives a single round of competitive cloning. If the user genuinely can't name a real moat, the right answer is to name one to **build**, not one to claim.
- **The Vanity North Star.** Signups, downloads, social followers. These are leading indicators of *attention*, not of revenue. A subscription business with "signups" as a north star is one that doesn't yet know what it sells.
- **The Mismatched North Star.** North star metric doesn't match the revenue model. MRR on a one-time-purchase indie Mac app; weekly buyers on a subscription SaaS; GMV on a productized service. Pick a metric that tracks the *engine* of the chosen revenue model, not a generic growth proxy.
- **The Contradiction.** Five answers that don't agree. The Persona's willingness-to-pay is $20/month but the Pricing Ladder defaults to $99. Revenue model is subscription but North Star is "active users" (with no payment dimension). Mechanism implies heavy AI cost but Cost & Margin assumes 85% gross margin. These contradictions are silent — they ship and run for a year before the math surfaces. Catch them now.

When you spot one of these, name it. Naming is half the cure, and the user will catch them earlier next time.

## Tone and pacing

- **Conversational, not robotic.** The user is making real strategic decisions; treat them like a peer working through a hard problem, not a form to fill in.
- **Push back when answers are weak.** The user invoked this skill to be rigorous; collapsing into agreement is the worst possible outcome. Quote the framework's "bad" criteria, name the failure pattern, and propose a sharper version every time the answer drifts.
- **One section at a time by default.** Don't dump all five sections at once. The order matters and each section constrains the next. If the user explicitly asks to batch, oblige — but warn that the contradictions step (the most valuable one) usually needs a second pass.
- **Confirm the working hypothesis before researching deeply.** Research takes time and tokens. A 30-second hypothesis check saves a 10-minute wrong-direction pricing-page detour.
- **Build the math together.** For Cost & Margin specifically, write the cost-per-user equation explicitly (AI + storage + processing + email + auth) — but Claude supplies category benchmarks where the user doesn't have real numbers. The non-negotiable is the user understands the equation and signs off on the working assumption; the non-negotiable is *not* that the inputs are measured. Founders who skip the equation entirely are the ones who are surprised when the bank account empties at month 18 — but a benchmark-based estimate is a perfectly good starting point.

## What "done" looks like

A rewritten Business Strategy file where:

- **Revenue Model** names one primary model that matches the product's shape, with the reasoning written down.
- **Pricing Ladder** names 2–3 tiers with a named default tier, an annual discount of 20–30%, and explicit anchor prices from named competitors.
- **Cost & Margin** has an explicit per-user cost equation, a named gross margin %, and fixed monthly costs covered by current or near-term MRR.
- **Unfair Advantage** names a real, compounding moat (distribution, niche expertise, audience, switching costs, cross-product portfolio, open-source community, counter-positioning) — or honestly names one to build over the next 12 months. Both count as done.
- **North Star** is one metric, with a 90-day target, that matches the revenue model.
- The five answers read as **one** story when assembled in the strategy summary at the top of the file.
- The file is dated and sourced.

A research-backed strategy with cost-per-user as a working assumption and any tagged validation items is a *successful* session output, not a failure. The goal is a strategy the user can act on this week — set a launch price, build the right cost model into the product, pick a tracker for the north star. Validation (5 pricing conversations, real cost-per-user data post-launch) is a normal next phase that happens after the session.

Recommended next step after a successful session: live with the strategy for 2–3 days, then run 3–5 pricing conversations with strangers in the ICP to validate the price band, and re-run this skill once usage data is in.
