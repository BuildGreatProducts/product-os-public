# Ship in 7 — plan: Prompt-to-app platform

*The member built the app on Lovable, Bolt, v0, Base44 or similar. It may even be reachable on the platform's URL, but they don't own the repo, the stack, or the deployment. Seven sessions to the app live on their own hosting, in their own repo.*

**Honest note at enrol:** this is the most ambitious path. `studio-develop-migrate` is deliberately a full inventory-and-verification process because migrations that skip it lose data, break auth, or leave Stripe webhooks pointing at a dead URL. Three sessions is realistic for a small app at a couple of hours each; a large app with many platform-managed services may not fit, and the skill says so at the end of Day 1's inventory. Say this before writing the plan.

## The seven sessions

| Day | Block | Skill(s) | Proof | Hours |
| --- | --- | --- | --- | --- |
| 1 | **Migrate: inventory + plan** | `studio-setup` (the app repo may be brand new) → `studio-develop-migrate` through its inventory and `docs/MIGRATION.md` | `docs/MIGRATION.md` with the full inventory; a stack decision; the honest "does this fit in three days?" answer | 2.5 |
| 2 | **Migrate: move** | work `docs/MIGRATION.md`: export, repo, database, auth, storage, secrets rotated | the app runs locally from the owned repo with real data | 4+ |
| 3 | **Migrate: verify** | the migration's verification gate: real login with a pre-migration password, test payment, storage URLs, webhooks re-pointed | **verification gate green** (the platform is not yet paused) | 3 |
| 4 | **Define backfill + quality gate** | `studio-define-from-code` → `studio-define-product` (fast); `studio-develop-security-audit` → Critical/High fixed | `docs/PRODUCT.md`; `docs/SECURITY-AUDIT.md` verdict; Critical/High ticked | 3 |
| 5 | **Deploy guide** | `studio-develop-golive` | `docs/DEPLOY.md`; hosting accounts created | 1.5 |
| 6 | **Go live** | work `docs/DEPLOY.md`; DNS cutover last | live URL on the member's own hosting | 3 |
| 7 | **Smoke test, decommission, announce** | smoke test as a real customer on the new URL; only then pause the platform per `docs/MIGRATION.md`; `studio-launch` (stretch) | **smoke test passed**; platform paused; live post (stretch) | 2 |

## Notes for the composer

- **The migration skill's rules are the plan's rules.** Secrets never export and are rotated; exports are point-in-time so the plan enforces a clean break; DNS cutover comes last; the old platform is paused only after the verification gate and the smoke test are both green. Don't compress any of that.
- **Migration moves and rewires; it never improves.** No refactor, no redesign this week. `studio-develop-refactor-plan` is for after the app is live and owned.
- **Define backfill is short here.** `studio-define-from-code` reads the live platform URL and the migrated code; the offer is already implicit in a product people may be using.
- **If Day 1's inventory says it doesn't fit**, the honest composition is: Days 1–5 migrate and verify, Day 6 quality gate, Day 7 go live and smoke test, no buffer, announce dropped. Say so, and offer the alternative of running `studio-develop-migrate` first and starting Ship in 7 once the app is owned.

## Compression (a missed or short session)

1. Drop Announce.
2. Merge Days 4 and 5: the audit's Critical/High and the deploy guide in one session; Define backfill becomes a 30-minute extraction.
3. Never skip the verification gate; never pause the platform before the smoke test; never move go live past Day 7.

## What Day 7 looks like

The app is live at a URL the member owns, from a repo the member owns, with real users' data intact, the old platform paused, and a real customer's path working end to end.
