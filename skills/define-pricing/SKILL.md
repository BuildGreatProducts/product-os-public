---
name: define-pricing
description: >-
  Decides how the product earns and what it costs — who pays, business model, pricing model, price
  anchors, one launch price, and a one-sentence price line — and writes the Pricing Strategy section
  of docs/DEFINE.md. Use when the user asks "what should I charge", "pick my launch price",
  "subscription or one-time", "freemium or trial", or "pricing strategy". Requires the Product Offer
  (ideally the Persona too). Not for margins, moats, or a north star metric — use
  define-business-strategy.
---

# Define: Pricing Strategy

Decide **how the product earns and what it costs** — fast — and write it as the six-section Pricing Strategy in `docs/DEFINE.md`: who pays, the business model that matches how the value arrives, what the price multiplies by and how people start, 2–3 real anchors, one launch price with the value, cost, and anchor lines behind it, and the plain-English price line. The model and the number are decided together, because a price without a unit is not a price: "$29" means nothing until it's "$29 per workspace per month, one plan, 14-day trial." Success is the member finishing *"it'll be about ___ per ___"* to a stranger without flinching.

Be fast and decisive: propose, confirm, move. Read the reference docs so the member doesn't have to, and bring the one paragraph that matters to their product, not the whole section.

## Inputs

Read inputs from `docs/` and the worksheets and references from `productos/define/` at the app repo root.

1. **`## 1. Product Offer`** in `docs/DEFINE.md` — **required**. Customer, Outcome, and Mechanism drive who pays, how the value arrives, and what the price multiplies by. If it is missing or mostly placeholder, stop and point the member to `define-offer-builder` first.
2. **`3-Pricing-Strategy.md`** — the worksheet's section structure, prompts, tables, and `> Good/Bad` criteria. Read it; never write to it.
3. **`BONUS-Business-Models.md`** — **required**, read selectively in step 3.
4. **`BONUS-Pricing-Models.md`** — **required**, read selectively in steps 4 and 6.
5. **`## 2. Customer Persona`** in `docs/DEFINE.md`, if filled — optional but the single most useful input: willingness-to-pay, anchor products, and budget bucket set the value ceiling.
6. **`BONUS-Real-Business-Strategy-Examples.md`** — calibration only: its How the Business Earns and Pricing Model rows show well-matched models and plan structures across six real businesses. Never retrofit the member onto one.

Ask, too, whether the member has had any real customer replies or conversations that touched on price — a stranger who asked about the price is worth more than any benchmark.

## Workflow

The session runs 30–45 minutes: ~30 on the fast path (step 2), closer to 50 on a full-path product once the live anchor research is counted. Claude does the reading and the anchor research live; the member's job is to react and commit.

Read [references/failure-patterns.md](references/failure-patterns.md) before step 3; name each pattern the moment it appears in steps 3–7, and re-check the draft against all twelve in step 9.

### 1. Form a hypothesis from the offer

Read the offer (and persona). Extract: who the buyer is (and whether buyer = user); whether the value is **one-off**, **recurring**, **linked to consumption**, or **linked to a transaction or result**; whether the mechanism has material per-unit cost (AI inference, storage, payouts, human time); and any willingness-to-pay or anchor data the persona names. State a one-paragraph hypothesis — buyer, value shape, candidate business model, candidate billing unit, candidate price band — and get it confirmed or corrected **before reading any BONUS sections or researching**. A wrong hypothesis wastes the whole session.

Stay out of the economics. Cost-per-user modelling, margin targets, the moat, and the north star belong to the optional `## 4. Business Strategy` section (`define-business-strategy`), which most members don't need until the money questions get real. If the conversation drifts there, park it: "that's the optional deep dive; right now we need a model and a number you can say this week." The one exception is the cost floor in step 6 — an order of magnitude, not a model.

### 2. Route: fast path or full path

- **Fast path** — a single continuous or bounded outcome sold to an individual or small team: subscription or one-time, one obvious unit (account or seat), one or two plans. Steps 3 and 4 become one-line confirmations ("subscription, per account, one plan, 14-day trial — agree?"), and the session runs ~30 minutes. Most solo and prosumer products take this path.
- **Full path** — anything usage- or AI-heavy, a marketplace, ads or affiliate, B2B with procurement, services, open-core, or outcome-based. Read the matching family and mechanic sections and walk steps 3 and 4 properly; the unit and the entry route are where these products win or lose money.

If any full-path trigger applies, take the full path — a product can fit every fast-path criterion and still lose money on its unit. Say which path you're on and why.

### 3. Pick the business model (section 2)

From `BONUS-Business-Models.md`, read the "Start from how the value arrives" table in full, then **only** the 1–2 family sections the hypothesis points at — never all sixteen. Present the family that fits how the value arrives, quote its *what tends to fail* line as it applies to this product (its worked economics example and first experiment are there to quote too), name the alternative you rejected and why, and lock it.

One primary model. A secondary model only if the offer genuinely has two kinds of value (a base product plus paid add-ons, say) — and name it as secondary. A usage overage on a subscription is not a second model: write "subscription" here and put the overage in the pricing model.

### 4. Design the pricing model (section 3)

From `BONUS-Pricing-Models.md`, read "Keep the layers separate" and the three worked combinations in full (shapes, not answers — never retrofit the member's product onto one), then **only** the mechanic sections matching the unit, plans, entry, and cadence under discussion — never all twenty-four.

Fill the five-row table — billing unit (and exclusions), plans, entry, cadence, extra use. Test the unit: is it something the customer already counts in? Test the plans: does each have a real buyer, or is the third column there because pricing pages have three columns? Test the entry: why this route, and does a free tier actually introduce paying buyers? Then write the complete-offer sentence — *"For ___, [product] delivers ___ for $___ per ___, including ___; extra ___ costs ___"* — with the price blank, and read it back. If it doesn't parse as a sentence, the model is too complicated.

### 5. Research 2–3 real anchors (section 4)

Use web search to pull today's actual prices for 2–3 products the persona already pays for or would compare this to — real numbers from real pricing pages; an outdated anchor produces an outdated price. Note where the member's product should sit relative to each anchor *and why* (replaces it, does one slice of it better, serves a smaller buyer).

If web search isn't available, say so, ask the member for comparables, and mark those claims unverified.

### 6. Set the launch price (section 5)

Read chapter 25 of `BONUS-Pricing-Models.md` (Setting your price), including the delivery-cost cheat sheet. Build three lines, then commit one number for the default plan:

- **Value ceiling** — the persona's willingness to pay, or an estimate from chapter 25: hours released × what their time is worth (halved if the time can't be redeployed), extra contribution, or a cost they can actually remove. Treat "10% of value" as a hypothesis.
- **Cost floor** — direct delivery cost per billing unit for a **heavy** customer, from the delivery-cost cheat sheet: platform fees, inference, failed attempts, storage, support. Tag it `[working assumption]` when unmeasured. Don't skip it because the member has no invoices yet; an order of magnitude is enough to catch a price that loses money on its best customers.
- **Anchor position** — where the number sits against section 4.

Place the product in the starting-bands table (a base-plus-overage product straddles two rows: the base plan's band and the per-unit rule), pick **one number** for the default plan, and run the sanity line: plan price − total direct cost to serve a heavy customer for the billing period (per-unit cost × heavy-use quantity). For base-plus-overage, run it twice — at the included allowance and at heavy use with the overage counted in the price. If it's negative, change the unit, add a cap, or raise the price — now, not later.

### 7. Write the price line (section 6)

Make the member type the DM version and read it back in the session. Members will hedge on the number; if they flinch, say so — the flinch is normal, this price is a first pass the market gets to argue with next week, and the argument only happens if there's a number on the table. The full version is the section 3 sentence with the number filled in.

### 8. Write the Pricing Strategy section of `docs/DEFINE.md`

Write to `docs/DEFINE.md` following the header rules in `productos/define/DEFINE-TEMPLATE.md` (create it from the template only if the member pointed you to an offer held elsewhere; write only `## 3. Pricing Strategy`, the `### Pricing Strategy` entry under `## Sources`, and the `*Last updated:*` line). If the section is already filled, show the member a diff and get approval before overwriting. If it carries `define-from-code`'s italic *Extracted draft* line, remove that line once the member approves the rewrite.

- Use the worksheet's headings — `### Who Pays`, `### How the Business Earns`, `### Pricing Model`, `### Price Anchors`, `### Launch Price`, `### Your Price Line` — as clean answers. Keep the filled five-decision table under Pricing Model, and the value, cost, and anchor lines plus the sanity line under Launch Price; drop the worksheet's reference tables (the sixteen models, the starting bands).
- The `### Pricing Strategy` sources entry lists the anchor URLs, the BONUS sections cited (by anchor, e.g. `BONUS-Business-Models.md#business-03-usage-based`), and every cost-floor assumption.

Spell out acronyms (MRR, LTD, BYOK) on first use — `docs/DEFINE.md` is the document the member shares.

### 9. Verify before delivering

- [ ] The buyer is named with a budget bucket and a value shape.
- [ ] One business model, with the rejected alternative written down.
- [ ] A billing unit the customer already counts in; plans that each have a buyer; an entry route with a reason — reading back as one sentence.
- [ ] Anchors are named with current prices from real pricing pages.
- [ ] One launch price with value, cost, and anchor lines and a positive sanity line.
- [ ] The price line is one natural sentence a stranger would understand, and the member has said it out loud.
- [ ] None of the twelve failure patterns survives in the draft.
- [ ] The `*Last updated:*` line and the sources entry are current; `3-Pricing-Strategy.md` is untouched.

Give the member the file path (`docs/DEFINE.md`). Then close the phase: once Summary, Offer, Persona, and Pricing are filled (an extracted draft from `define-from-code` counts), the Define phase is done — next is Design (`productos/design/DESIGN-CHECKLIST.md`). If any of those is still a placeholder, name the skill that fills it first. Tell the member to say the price line to real potential customers while the number is still warm.
