# Sell in 30 — week one: Live, priced, nobody has paid

*The product is live with a price on the site or a payments integration in place, and the launch log's rung is below `payment` (or there is no launch log). The bar is a payment.*

## Week one

| Day | Block | Skill(s) | Proof |
| --- | --- | --- | --- |
| 1 | **Define backfill + offer review** | `studio-define-from-code` if the Define docs are missing → `studio-define-offer-review` → `studio-define-product`; confirm the price line against `3-Pricing-Strategy.md` (run `studio-define-pricing` only if the current price has no reasoning behind it) | a sharpened offer, read out loud; `docs/PRODUCT.md`; the price line confirmed |
| 2 | **Messaging alignment** | `studio-design-landing-page` (and/or `studio-design-app-listing`) against the reviewed offer → ship the copy via the build loop, `studio-develop-design-review` before commit | before/after of the live hero and the pricing section |
| 3 | **Checkout verified, or made live** | if Stripe is still in test mode (key prefix `sk_test_` rather than `sk_live_`, the dashboard's test-mode toggle, or `livemode: false` on the Price object; never inferred from a price ID's name), switch it to live per the payments section of `studio-develop-golive` first; then a real purchase through the live checkout as a stranger would (fresh account, incognito), refunded; fix what breaks | the live receipt and its refund (the test purchase never counts toward the bar); screenshots of landing → paid saved to `docs/` |
| 4 | **Believers backfill + warm conversations** | create or update `docs/LAUNCHES.md`; `studio-launch` sitting one to believers and named warm contacts, checkout link in hand | sent-folder screenshot |
| 5 | **Channel** | `studio-distribute-gtm-strategy` | `1-Go-To-Market-Strategy.md` |
| 6 | **Experiments + follow-ups** | `studio-distribute-growth-experiments`, briefed with the bar and the clock; every open thread answered | `2-Growth-Experiments.md`; tracker seeded |
| 7 | **Weekly read** | `studio-launch` sitting two | the read; the Week 1 Skool post |

## Notes for the composer

- **Day 3 is a verification first, a setup only if test mode is found.** Priced products with no real payments are common: a Stripe integration in test mode, a checkout that 404s on mobile, a webhook pointing at a dead URL. Walk it as a stranger. Anything found is fixed the same day.
- **A conversion-path audit is a natural experiment 1** on this path (`studio-develop-cro-audit` on landing, pricing, checkout, then the top three fixes). Let the growth experiments skill rank it against the channel experiments rather than fixing it blind on Day 3.
- **If the price has never been said out loud with reasoning**, `studio-define-pricing` on Day 1 is twenty minutes well spent. A price that was guessed is a pricing experiment waiting to happen.

## Compression (a missed or short session)

1. Merge Days 5–6.
2. Merge Day 2 into Day 1: draft the copy changes in the review session; ship them the same day.
3. Never move the checkout verification after the warm asks. Never move the read.
