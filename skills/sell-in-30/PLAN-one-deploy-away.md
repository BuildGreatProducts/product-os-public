# Sell in 30 — week one: Not yet live, one deploy away

*The app runs locally, deploy config or `docs/DEPLOY.md` is in progress, and the member can be live within the first few days. Anyone further from live than that belongs in `ship-in-7`. The bar is a payment (or an activated user, if the product stays free this month).*

**Honest note at enrol:** this is the tightest week one in the challenge. Two sessions of deploy push the offer review, messaging, checkout, warm asks, strategy and experiments into five. Say so, and recommend more hours for this week than for the rest.

## Week one

| Day | Block | Skill(s) | Proof |
| --- | --- | --- | --- |
| 1 | **Go live: the guide** | `develop-security-audit` first unless `docs/SECURITY-AUDIT.md` exists, is current, and covers the code being deployed (absent, outdated, or narrower than today's scope → re-run it); Critical findings fixed before deploy; then `develop-golive` → work `docs/DEPLOY.md`: accounts, secrets, services | `docs/DEPLOY.md`; accounts created; production services configured |
| 2 | **Go live: the deploy + offer review** | finish `docs/DEPLOY.md`; smoke test as a real customer; then `define-from-code` if needed → `define-offer-review` → `define-product` | live URL, smoke test passed; a sharpened offer |
| 3 | **Messaging alignment + checkout live** | landing page / listing copy from the reviewed offer, shipped; `define-pricing` if there is no price; payments live and a real test purchase, refunded the same session and never counted toward the bar (skip the checkout half if staying free) | before/after of the live hero; the test-purchase receipt |
| 4 | **Believers backfill + warm conversations** | create `docs/LAUNCHES.md`; `mini-launch` sitting one, link in hand | sent-folder screenshot |
| 5 | **Channel** | `distribute-gtm-strategy` | `1-Go-To-Market-Strategy.md` |
| 6 | **Experiments + follow-ups** | `distribute-growth-experiments`, briefed with the bar and the clock | `2-Growth-Experiments.md`; tracker seeded |
| 7 | **Weekly read** | `mini-launch` sitting two | the read; the Week 1 Skool post |

## Notes for the composer

- **The security audit is not optional because the week is tight.** An existing `docs/SECURITY-AUDIT.md` counts only if it is current and covers what is being deployed; if it is absent, outdated, or narrower than today's scope, `develop-security-audit` runs again on Day 1 before the deploy guide. Critical findings are fixed before anything is reachable. Ship in 7's quality-gate rule applies here too.
- **If the deploy takes a third session**, it takes it: Day 3 becomes deploy, and Days 3–4 as written merge into Day 4 (messaging drafted from the review, checkout live, warm asks in one long session). The read stays on Day 7.
- **If the deploy can't be done in three sessions**, the honest move is to stop: log it, set `docs/SELL-IN-30.md`'s header to `Status: Closed — [date]` with a one-line reason, and only then route to `ship-in-7` (one challenge open at a time). The member restarts Sell in 30 the week the app is live, with the "after Ship in 7" plan; the closed file is moved aside at that enrol, not overwritten.

## Compression (a missed or short session)

1. Merge Days 5–6.
2. Merge Day 3's messaging into Day 2's review: draft and ship in one session.
3. Never move the checkout after the warm asks. Never move the read.
