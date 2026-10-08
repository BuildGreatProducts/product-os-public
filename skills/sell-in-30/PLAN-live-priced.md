# Sell in 30 — week one: Live, priced, nobody has paid

*The product is live with a price on the site or a payments integration in place, and nobody has paid yet. The bar is a payment.*

## Week one

| Day | Block | Skill(s) | Proof |
| --- | --- | --- | --- |
| 1 | **Define backfill + offer review** | `define-from-code` if `docs/DEFINE.md` is missing → `define-offer-review`; confirm the price line against the Pricing Strategy section of `docs/DEFINE.md` (run `define-pricing` if that section is missing or unfilled — a live price with no document behind it is a guess) | a sharpened offer, read out loud; the price line confirmed |
| 2 | **Messaging alignment** | `design-landing-page` (and/or `design-app-listing`) against the reviewed offer → ship the copy via the build loop, `develop-design-review` before commit | before/after of the live hero and the pricing section |
| 3 | **Checkout verified, or made live** | if Stripe is still in test mode (key prefix `sk_test_` rather than `sk_live_`, the dashboard's test-mode toggle, or `livemode: false` on the Price object; never inferred from a price ID's name), switch it to live per the payments section of `develop-golive` first; then a real purchase through the live checkout as a stranger would (fresh account, incognito), refunded; fix what breaks | the live receipt and its refund (the test purchase never counts toward the bar); screenshots of landing → paid saved to `docs/` |
| 4 | **Warm list + warm conversations** | write or update the warm list in `docs/SELL-IN-30.md`; the warm ask to each, personally, checkout link in hand; every response logged in the Experiment Log | sent-folder screenshot; the warm list |
| 5 | **Channel** | `distribute-gtm-strategy` | `docs/GO-TO-MARKET.md` |
| 6 | **Experiments + follow-ups** | `distribute-growth-experiments`, briefed with the bar and the clock; every open thread answered | `docs/GROWTH-EXPERIMENTS.md`; `docs/GROWTH-TRACKER.md` seeded |
| 7 | **Weekly read** | the signal read, applied to the week | the read; the Week 1 Skool post |

## Notes for the composer

- **Day 3 is a verification first, a setup only if test mode is found.** Priced products with no real payments are common: a Stripe integration in test mode, a checkout that 404s on mobile, a webhook pointing at a dead URL. Walk it as a stranger. Anything found is fixed the same day.
- **A conversion-path audit is a natural experiment 1** on this path (`develop-cro-audit` on landing, pricing, checkout, then the top three fixes). Let the growth experiments skill rank it against the channel experiments rather than fixing it blind on Day 3.
- **If the price has never been said out loud with reasoning**, `define-pricing` on Day 1 is thirty minutes well spent. A price that was guessed is a pricing experiment waiting to happen.

## Compression (a missed or short session)

Actions, in order — use the first that fits, within the week:

1. Merge Days 5–6.
2. Merge Day 2 into Day 1: draft the copy changes in the review session; ship them the same day.

**Constraints** (rules, not steps — no action above may break them):

- Never move the checkout verification after the warm asks.
- Never move the read.
