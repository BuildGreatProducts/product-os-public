# Sell in 30 — week one: Live, free, staying free for now

*The product is live and free, and the member has said it will not charge within the thirty days. The bar is one activated user: a real person reaching the magic moment. The price and checkout blocks drop out; activation takes their place.*

## Week one

| Day | Block | Skill(s) | Proof |
| --- | --- | --- | --- |
| 1 | **Define backfill + offer review** | `define-from-code` if `docs/DEFINE.md` is missing → `define-offer-review`; confirm `docs/MAGIC-MOMENT.md` exists (run `design-magic-moment` if not — the bar is defined there) | a sharpened offer in `docs/DEFINE.md`; the magic moment named in one sentence |
| 2 | **Messaging alignment** | `design-landing-page`, `design-app-listing`, and/or `design-marketplace-listing` (whichever surfaces the shape uses) against the reviewed offer → ship the copy (pages via the build loop, `develop-design-review` before commit; listings through the store's console) | before/after of the live hero or listing |
| 3 | **Warm list + activation check** | the warm list written in `docs/SELL-IN-30.md` (everyone who has used it or responded, then named people who match the persona); **the member** walks the live product as a stranger, from signup (or install, or connect) to the magic moment, with a fresh test account (never a real user's), and times it; note every wall. The agent reads the result; it never creates or touches production records | the warm list; screenshots of the stranger's path saved to `docs/`, with the walls listed |
| 4 | **Warm conversations** | the warm ask to everyone on the warm list, personally; the ask is "try it", with the link; every response logged in the Experiment Log | sent-folder screenshot |
| 5 | **Channel** | `distribute-gtm-strategy` | `docs/GO-TO-MARKET.md` |
| 6 | **Experiments + follow-ups** | `distribute-growth-experiments`, briefed with the bar (activated user) and the clock; the backlog leans on activation (`distribute-activation-retention-audit` as a candidate experiment) | `docs/GROWTH-EXPERIMENTS.md`; `docs/GROWTH-TRACKER.md` seeded |
| 7 | **Weekly read** | the signal read, applied to the week | the read; the Week 1 Skool post |

## Notes for the composer

- **The bar has to be observable.** "Reached the magic moment" needs an event the member can see: an analytics event, a database row, a server log of the first successful tool call, a screenshot the user sends. For shapes without screens, the shape file's Distribute notes name how activation is measured. Day 3 establishes how activation will be seen before anyone is asked to try it.
- **Day 3's stranger walk is the cheapest activation audit there is.** The walls it finds usually become experiment 1. The full `distribute-activation-retention-audit` is a candidate experiment, not a Day 3 block.
- **The pivot review's mapping shifts** on this path: no replies → persona; replies but no signup → messaging or offer; signups that don't activate → product (or execution: the wall). Pricing doesn't enter it.
- **If the member changes their mind and wants to charge**, switch the bar and add Price it and Checkout live as the next two sessions. Log the change, dated.

## Compression (a missed or short session)

Actions, in order — use the first that fits, within the week:

1. Merge Days 5–6.
2. Merge Day 2 into Day 1.
3. Merge Day 3 into Day 4: the stranger walk in the morning, the asks in the afternoon.

**Constraints** (rules, not steps — no action above may break them):

- Never move the read.
