# Pricing Strategy Framework

A worksheet for deciding how your product earns and what it costs — filled in by `studio-define-pricing` in a 30–45 minute session. Keep each answer to 1-2 sentences; the tables in sections 3 and 5 are the exception.

This is the canonical pricing document. It answers, in order: who pays, how the business earns, what the price multiplies by and how people start, what the price sits against, one launch price, and the sentence that carries it into your Mini-Launch (`4-Mini-Launch.md`). The economics behind the price — what each customer costs to serve, why a clone doesn't kill you, the one number to watch — are the optional deep dive (`BONUS-Business-Strategy-Deep-Dive.md`) for when the money questions get real.

Two reference docs sit behind this worksheet: `BONUS-Business-Models.md` (the sixteen ways an app earns) and `BONUS-Pricing-Models.md` (the twenty-four ways to shape a price, plus how to set the number). Read the sections that match your pick, not all forty.

---

## 1. Who Pays

*Who actually hands over the money — out of which budget — and how does the value arrive?*

> Good: a named buyer, a budget bucket, and the shape of the value — "solo consultant, personal software budget under $100/mo, the value recurs every week they use it", "head of ops, team-tooling budget, no sign-off needed under $50/seat, the value is one migration done once"
> Bad: "everyone", "users", a buyer who is a different person from the user with no note on how that gets bridged, no idea whether the value is one-off or continuous

Say whether the buyer is also the user, and whether the value is **one-off**, **recurring**, **linked to consumption**, or **linked to a transaction or result**. That last answer picks your business model in the next section.

**Your answer:**

---

## 2. How the Business Earns

*Which one business model matches how the value arrives?*

> Good: one primary model that matches how the value arrives, with the alternative you rejected written down — "subscription, because the reports are worth paying for again every month; rejected one-time because the data goes stale in weeks"
> Bad: two models in parallel "to maximise revenue", freemium named as the model (it's an entry route, see section 3), a mobile app on subscription because mobile apps are

**The sixteen models — pick one.** Each links to its full section (how it works, what tends to fail, a worked economics example, a first experiment) in `BONUS-Business-Models.md`:

| Model | Usually a good fit when… |
| --- | --- |
| [Subscription](BONUS-Business-Models.md#business-01-subscription) | Value recurs and customers can recognise it at renewal. |
| [One-time purchase](BONUS-Business-Models.md#business-02-one-time-purchase) | A defined product or result has low continuing delivery costs. |
| [Usage-based](BONUS-Business-Models.md#business-03-usage-based) | Workloads vary and consumption is understandable. |
| [Credits / consumables](BONUS-Business-Models.md#business-04-credits-consumables) | Customers want occasional jobs with controlled spending. |
| [Paid content / add-ons](BONUS-Business-Models.md#business-05-paid-content-add-ons) | Different customers need valuable optional extensions. |
| [Transaction / commission](BONUS-Business-Models.md#business-06-transaction-commission) | The app enables successful exchanges between buyers and sellers. |
| [Ads / sponsorship](BONUS-Business-Models.md#business-07-ads-sponsorship) | Repeat attention is valuable to relevant advertisers. |
| [Affiliate / lead generation](BONUS-Business-Models.md#business-08-affiliate-lead-generation) | The app helps users choose an external provider. |
| [Enterprise contracts](BONUS-Business-Models.md#business-09-enterprise-contracts) | Organisations need governance, deployment, and purchasing support. |
| [White-label / OEM](BONUS-Business-Models.md#business-10-white-label-oem) | Partners can brand or embed a shared capability. |
| [Open-core / hosting](BONUS-Business-Models.md#business-11-open-core-hosting) | Users value inspectability and some buyers pay for convenience or support. |
| [Software + services](BONUS-Business-Models.md#business-12-software-services) | Expert implementation helps customers achieve the app's result. |
| [Outcome-based](BONUS-Business-Models.md#business-13-outcome-based) | Success can be defined, verified, and attributed. |
| [Donations / patronage](BONUS-Business-Models.md#business-14-donations-patronage) | A committed community voluntarily funds useful work. |
| [Supports another business](BONUS-Business-Models.md#business-15-supports-another-business) | The app increases value in a wider paid business. |
| [Lifetime offers](BONUS-Business-Models.md#business-16-lifetime-offers) | A one-off payment can sustainably fund the full promised entitlement. |

Write the model, why it fits the outcome, the alternative you rejected and why, and a secondary model only if it earns its place.

**Your answer:**

---

## 3. Pricing Model

*What does the price multiply by, what's included, how does someone start, and when do they pay?*

> Good: a unit the customer already counts in, one or two plans with a real buyer each, an entry route with a reason — "per location, unlimited staff; one plan; 14-day trial because the value shows in the first week; monthly"
> Bad: charging in tokens when the buyer thinks in documents, three columns because pricing pages have three columns, "unlimited" on a low fixed fee, "most popular" with no purchase data, a free tier with no reason it introduces paying buyers

**Five decisions — fill the table** (each row links to the matching layer in `BONUS-Pricing-Models.md`):

| Decision | Your choice |
| --- | --- |
| **Billing unit** — what the price multiplies by (account, seat, resource, usage unit, transaction, outcome) and what is excluded. *[Units 01–06, 13; advertiser, partner, service, and outcome units 17–20](BONUS-Pricing-Models.md#pricing-01-flat-rate-per-account)* | |
| **Plans** — one plan, 2–3 plans with a named default, or add-ons; what each includes. *[Packaging 07, 11; capacity blocks 10](BONUS-Pricing-Models.md#pricing-07-feature-tiers)* | |
| **Entry** — upfront, free tier, trial, demo, or paid pilot, and why. *[Entry 21, 23, 24](BONUS-Pricing-Models.md#pricing-23-free-entry-freemium)* | |
| **Cadence** — monthly, annual, one-time, per job; renewal terms. *[Timing 15, 16; commitments and minimums 14](BONUS-Pricing-Models.md#pricing-16-billing-cadence)* | |
| **Extra use** — charge, top-up, pause, or upgrade at the limit. *[Quantity bands 08, 09; base plus overage 12](BONUS-Pricing-Models.md#pricing-12-hybrid-base-plus-overage)* | |

Then say the whole offer in one sentence:

*"For ___, [product] delivers ___ for $___ per ___, including ___; extra ___ costs ___."*

**Your answer:**

---

## 4. Price Anchors

*Which 2–3 products does your customer already pay for that set their expectation of what this should cost?*

> Good: named products with today's real prices — "Notion $12/seat, Calendly $12/mo — we sit just above, at $19, because we replace both"
> Bad: no anchors, anchoring against free tools, anchors you haven't checked the current price of

For each anchor, note where you sit relative to it *and why* — replaces it, does one slice of it better, serves a smaller buyer.

**Your answer:**

---

## 5. Launch Price

*One price for your default plan that you would say out loud to a stranger this week — and the three lines that justify it.*

> Good: one number with a billing shape, and a value line, a cost line, and an anchor line behind it — "$29/month per workspace; the persona pays $60+/mo for the two tools it replaces; heavy use costs us about $6/mo; sits under Anchor A and above Anchor B"
> Bad: a range you'd negotiate down from, "free for now, we'll monetize later", a price you have never said out loud, a number copied from a competitor's page with nothing behind it

**Triangulate from three lines:**

- **Value ceiling.** What the outcome is worth to this buyer — the persona's willingness to pay, or an estimate (hours released × what their time is worth, extra contribution, a cost they can actually remove). "Customers pay 10% of the value" is a hypothesis to test, not a formula. *(`BONUS-Pricing-Models.md` chapter 25.)*
- **Cost floor.** What it costs you to deliver one billing unit to a **heavy** customer — hosting, AI inference, failed attempts, storage, support, platform fees. Use the delivery-cost cheat sheet in chapter 25 and tag it `[working assumption]` until real invoices replace it.
- **Anchor position.** Where the number sits against section 4, and why.

**Starting bands** — starting hypotheses the market argues with next week, not benchmarks:

| Shape | Starting band | Typical ladder |
| --- | --- | --- |
| Consumer mobile subscription | $5–15/mo | Free → $9.99/mo or $59.99/yr |
| Prosumer / solo tool | $9–29/mo | one plan, or $9 / $19 |
| B2B starter SaaS | $19–99/mo | $19 / $49 / $99 |
| Team / agency SaaS | $99–700/mo | $99 / $299 / $700 |
| One-time / perpetual licence | $29–199 | Free → $69 → $149 |
| Lifetime deal launch | $59–299, seats capped | $79 / $199 / $299 |
| Usage / credits | per-unit at 3–5× your delivery cost | base plan + overage |
| Paid pilot / productised service | $500–5,000 fixed scope | pilot → retainer |

Close with the sanity line: **price − direct cost per unit at heavy use = $___** (it must be positive; if it isn't, change the unit, the cap, or the price before you launch). A base-plus-overage product straddles two rows above and runs the line twice: at the included allowance, and at heavy use with the overage counted in the price.

**Your answer:**

---

## 6. Your Price Line

*The one plain-English sentence that carries the price into your Mini-Launch.*

> Good: "I'm building X for Y — it'll be around $29/month, about half what [anchor] charges. Would that be worth it for you?"
> Bad: a paragraph of hedging, apologizing for the price, hiding the number behind "affordable"

Two lengths. The DM version above is what goes in the Mini-Launch. The full version is the one-sentence offer from section 3 — use it on a pricing page, a one-pager, or when someone asks "so how does it work?"

Including the price in your mini-launch message is **optional — but recommended.** A post with a price gets you a dramatically more honest signal than one without: "sounds cool" is free, "I'd pay $29 for that" is data. If saying the number out loud feels scary, that's normal — it's also exactly the fear the mini-launch is designed to break.

**Your answer:**
