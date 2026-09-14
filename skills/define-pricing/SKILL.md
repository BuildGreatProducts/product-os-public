---
name: define-pricing
description: >-
  Use when the user has a filled-in Product Offer (and ideally Customer Persona) and needs to decide how the product earns and what it costs — business model, pricing model, one launch price — in 30–45 minutes before the Mini-Launch. Triggers on "what should I charge", "pick my launch price", "pricing strategy", "business model for my app", "pricing model", "how should I charge", "subscription or one-time", "per seat or per usage", "should I have tiers", "freemium or trial", "put a price on it", "what's my price line", or any request to fill in the six-section Pricing Strategy (Who Pays, How the Business Earns, Pricing Model, Price Anchors, Launch Price, Your Price Line). Reads the Offer and Persona plus BONUS-Business-Models.md and BONUS-Pricing-Models.md, researches 2–3 anchor prices, triangulates the number from value, cost, and anchors, and rewrites 3-Pricing-Strategy.md in place. Cost & margin, unfair advantage, and north star live in the optional deep dive, define-business-strategy.
---

# Define: Pricing Strategy

This skill decides **how the product earns and what it costs** — fast. It turns a filled-in Product Offer (and Persona, if available) into a six-section **Pricing Strategy**: who pays, which business model matches how the value arrives, what the price multiplies by and how people start, 2–3 real anchors, one launch price with the value, cost, and anchor lines behind it, and the plain-English price line that carries the number into the Mini-Launch.

The model and the number are decided here, once, because a price without a unit is not a price. "$29" means nothing until it's "$29 per workspace per month, one plan, 14-day trial." What this skill deliberately does **not** do is the economics behind the number — cost-per-user modelling, margin targets, the moat, the north star. Those live in the optional `BONUS-Business-Strategy-Deep-Dive.md` (filled by `define-business-strategy`), which most people don't need until the money questions get real — typically before spending on paid channels in Distribute. This skill exists because the Mini-Launch (the next step in the Define checklist) needs a price to carry, and founders will happily spend three weeks "figuring out pricing" as a way of not talking to anyone.

A price the founder has never said out loud is not a price — it's a guess hiding in a spreadsheet. The measure of success for this session is that the user can finish the sentence *"it'll be about ___ per ___"* to a stranger without flinching.

> **Session length:** 30–45 minutes; ~30 on the fast path (see step 2), closer to 50 on a full-path product once the live anchor research is counted. Claude does the reading and the anchor research live in the session; the user's job is to react and commit. The sixteen business models and twenty-four pricing mechanics live in `productos/define/BONUS-Business-Models.md` and `productos/define/BONUS-Pricing-Models.md` — read the intro tables in full, then **only the sections that match the hypothesis**, never all forty. If the conversation drifts to margins, moats, or north stars, park it: "that's the optional deep dive; right now we need a model and a number you can say this week."

## Inputs

Before starting, locate the following in the ProductOS folder — `productos/` at the app repo root, or the current folder in a standalone ProductOS checkout. Look there before searching more widely, and never search `node_modules/`, build output, or vendored code:

1. **The Product Offer** — usually `1-Product-Offer.md`. The **required** input. Customer, Outcome, and Mechanism drive who pays, how the value arrives, and what the price should multiply by.
2. **The Pricing Strategy template** — usually `3-Pricing-Strategy.md`. Defines the exact output structure, *and is also the file the skill rewrites in place* at the end.
3. **The Business Models reference** — usually `BONUS-Business-Models.md`. **Required.** Read the "Start from how the value arrives" table in full; read only the 1–2 family sections the hypothesis points at. Each family carries what tends to fail, a worked economics example, and a first experiment — quote them for the user's product.
4. **The Pricing Models reference** — usually `BONUS-Pricing-Models.md`. **Required.** Read "Keep the layers separate" and the three worked combinations in full (they are shapes, not answers — never retrofit the user's product onto one); read only the mechanic sections matching the unit, plans, entry, and cadence under discussion; read chapter 25 (Setting your price) including the delivery-cost cheat sheet when building the launch price.
5. **The Customer Persona** — usually `2-Customer-Persona.md`, if filled in. Optional but the single most useful input: willingness-to-pay, anchor products, and budget bucket come from here and set the value ceiling.
6. **The Business Strategy examples** — usually `BONUS-Real-Business-Strategy-Examples.md`. Calibration only: the How the Business Earns and Pricing Model rows show what a well-matched model and plan structure look like across six real businesses. Never retrofit the user onto one.
7. **The Launch Log** — `docs/LAUNCHES.md`, if present. A stranger who asked about the price is worth more than any benchmark.

If the Product Offer is missing or mostly empty, stop and point the user to `define-offer-builder` first.

## Workflow

### 1. Form a hypothesis from the offer

Read the offer (and persona). Extract: who the buyer is (and whether buyer = user); whether the value is **one-off**, **recurring**, **linked to consumption**, or **linked to a transaction or result**; whether the mechanism has material per-unit cost (AI inference, storage, payouts, human time); and any willingness-to-pay or anchor data the persona already names. State a one-paragraph hypothesis — buyer, value shape, candidate business model, candidate billing unit, candidate price band — and ask the user to confirm or correct **before reading any BONUS sections or researching**. A wrong hypothesis wastes the whole session.

### 2. Route: fast path or full path

- **Fast path** — the offer is a single continuous or bounded outcome sold to an individual or small team: subscription or one-time, one obvious unit (account or seat), one or two plans. Sections 2 and 3 become one-line confirmations ("subscription, per account, one plan, 14-day trial — agree?"), and the session runs ~30 minutes. Most solo and prosumer products take this path.
- **Full path** — anything usage- or AI-heavy, a marketplace, ads or affiliate, B2B with procurement, services, open-core, or outcome-based. Read the matching family and mechanic sections and walk sections 2 and 3 properly; the unit and the entry route are where these products win or lose money.

If any full-path trigger applies, take the full path — a product can fit every fast-path criterion and still lose money on its unit. Say which path you're on and why.

### 3. Pick the business model (section 2)

Present the family that fits how the value arrives, quote its *what tends to fail* line as it applies to this product, name the alternative you rejected and why, and lock it. One primary model. A secondary model only if the offer genuinely has two kinds of value (a base product plus paid add-ons, say) — and name it as secondary. A usage overage on a subscription is not a second model: write "subscription" here and put the overage in the pricing model (section 3).

### 4. Design the pricing model (section 3)

Fill the five-row table — billing unit (and exclusions), plans, entry, cadence, extra use — reading the matching mechanic sections as you go. Test the unit: is it something the customer already counts in? Test the plans: does each have a real buyer, or is the third column there because pricing pages have three columns? Test the entry: why this route, and does a free tier actually introduce paying buyers? Then write the complete-offer sentence — *"For ___, [product] delivers ___ for $___ per ___, including ___; extra ___ costs ___"* — with the price blank, and read it back. If it doesn't parse as a sentence, the model is too complicated.

### 5. Research 2–3 real anchors (section 4)

Use web search to pull today's actual prices for 2–3 products the persona already pays for or would compare this to. Real numbers from real pricing pages — anchors move, and an outdated anchor produces an outdated price. Note where the user's product should sit relative to each anchor *and why* (replaces it, does one slice of it better, serves a smaller buyer).

### 6. Set the launch price (section 5)

Build three lines, then commit one number for the default plan:

- **Value ceiling** — the persona's willingness to pay, or an estimate from chapter 25: hours released × what their time is worth (halved if the time can't be redeployed), extra contribution, or a cost they can actually remove. Treat "10% of value" as a hypothesis.
- **Cost floor** — direct delivery cost per billing unit for a **heavy** customer, from the delivery-cost cheat sheet: platform fees, inference, failed attempts, storage, support. Tag it `[working assumption]` when unmeasured. Don't skip this because the user has no invoices yet; an order of magnitude is enough to catch a price that loses money on its best customers.
- **Anchor position** — where the number sits against section 4.

Place the product in the starting-bands table (a base-plus-overage product straddles two rows: the base plan's band and the per-unit rule), pick **one number** for the default plan, and run the sanity line: plan price − total direct cost to serve a heavy customer for the billing period (per-unit cost × heavy-use quantity). For base-plus-overage, run it twice — at the included allowance and at heavy use with the overage counted in the price. If it's negative, change the unit, add a cap, or raise the price — not later, now.

### 7. Write the price line (section 6)

Make the user type the DM version and read it back in the session. If they flinch, that's the fear the Mini-Launch is designed to break — say so. The full version is the section 3 sentence with the number filled in.

### 8. Rewrite the Pricing Strategy file in place

Rewrite `3-Pricing-Strategy.md` in place — same section headers, same italic prompts, same `> Good/Bad` lines, same tables — replacing each `**Your answer:**` block and filling the section 3 table. Add a dated header ("Drafted: [month year]") and a **Sources** footer listing the anchor URLs, the BONUS sections cited (by anchor, e.g. `BONUS-Business-Models.md#business-03-usage-based`), and every cost-floor assumption. Read the existing file first to preserve any user notes.

### 9. Verify before delivering

Check: buyer is named with a budget bucket and a value shape; one business model with a rejected alternative written down; a billing unit the customer already counts in, with plans that each have a buyer and an entry route with a reason; anchors named with current prices; one launch price with value, cost, and anchor lines and a positive sanity line; the price line is one sentence a stranger would understand. Then hand off: the recommended next step is always the Mini-Launch (`mini-launch`) — within 48 hours, while the number is still warm.

## Failure patterns to look for

Name them when you see them — naming compounds learning:

- **The Blank Cheque.** "Everyone" as the buyer. A price needs a budget to come out of; force a named buyer and budget bucket.
- **The Layer Blur.** "Freemium", "annual", "AI-powered", or "with a guarantee" offered as the business model. Freemium is an entry route, annual is a cadence, AI is a capability, a guarantee reduces risk — none of them says who pays for what.
- **The Two-Model Trap.** Subscription *and* one-time *and* services, in parallel, "to maximise revenue." Two models means two cost structures, two sales motions, two churn dynamics. Pick one as primary.
- **The Invisible Unit.** Billing in tokens, API calls, or compute-seconds when the buyer thinks in documents, minutes, or clients. Choose a unit they can explain to their own boss.
- **The Unlimited Promise.** "Unlimited" AI, storage, or support on a low fixed fee. The heaviest customer sets your cost, not the average one; add a meaningful limit or a metered component.
- **The Unexamined Flat Price.** One plan chosen without checking whether a second plan has a real buyer. One or two clear plans can beat three — but decide it, don't default to it. (The reverse, three columns because pricing pages have three columns, is the same failure.)
- **The Freemium Dodge.** "Free for now, we'll monetize later" is not a pricing strategy; it's a way to avoid the scary sentence. A free tier is fine when it introduces paying buyers the paid tier never could — write down why, or don't do it.
- **The Ten-Percent Rule.** "The outcome is worth $1,000 so we'll charge $100." A value estimate finds a ceiling; it doesn't prove anyone will pay a fixed share of it.
- **The Negotiable Range.** "$20–50 depending" — a range is a price you've already agreed to lower. One number.
- **The Free-Tool Anchor.** Anchoring against free products guarantees a race to zero. Anchor against what the customer already *pays* for.
- **The Launch-Cash Mirage.** Lifetime-deal or annual-prepay revenue treated as recurring. Cash collected now is a delivery obligation later; model heavy use over years before selling forever.
- **The Unspoken Number.** A price the user has never said out loud. Make them type the price line and read it back in the session.

## Tone and pacing

- **Fast and decisive.** Propose, confirm, move. Read the reference docs so the user doesn't have to; bring the one paragraph that matters to their product, not the whole section.
- **Push through the flinch.** Users will hedge on the number. Remind them: this price is a first pass that the market gets to argue with next week — but the argument only happens if there's a number on the table.
- **Park economics questions.** Cost-per-user modelling, margin targets, the moat, the north star — all real, all later. Name where they live (the optional `define-business-strategy` deep dive) and keep moving. The one exception is the cost floor in step 6, which is an order of magnitude, not a model.

## What "done" looks like

A rewritten `3-Pricing-Strategy.md` where the buyer, budget, and value shape are named; one business model is chosen with its rejected alternative; the billing unit, plans, entry, and cadence are filled in and read as one sentence; the anchors are real and current; the launch price is one number with value, cost, and anchor lines behind it and a positive sanity line; and the price line reads as one natural sentence — ready to be dropped into a mini-launch post or DM within 48 hours.
