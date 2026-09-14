# Ship in 7 — plan: Local prototype

*The member has an app that runs on their machine. The code is reasonable, the core flow works locally, and nobody can reach it: no deploy config, no `docs/DEPLOY.md`, no production URL. Seven sessions to a live app, with the extra days spent on the gate and on polish.*

This is the least crowded path, so it carries the fullest quality gate and a real polish day.

## The seven sessions

| Day | Block | Skill(s) | Proof | Hours |
| --- | --- | --- | --- | --- |
| 1 | **Define backfill + baseline** | `define-from-code` → `define-product` (skip if current); `develop-code-review` over the working tree so the starting state is known | `docs/PRODUCT.md`; the review's verdict line | 2 |
| 2 | **Quality gate** | `develop-security-audit` → do the "Do this right now" items today | `docs/SECURITY-AUDIT.md` verdict; rotated keys if any were committed | 2 |
| 3 | **Fixes** | the build loop over the audit's Fix plan, Critical and High first | Fix plan Critical/High ticked; tests green | 3 |
| 4 | **Deploy guide** | `develop-golive` | `docs/DEPLOY.md`; hosting and service accounts created (🧑 steps) | 1.5 |
| 5 | **Go live** | work `docs/DEPLOY.md` top to bottom | live URL, HTTPS, custom domain if owned | 3 |
| 6 | **Polish** | `design-design-system-from-code` if `docs/DESIGN.md` is missing, then `develop-design-review` over the core flow; fix the inconsistencies it flags | before/after of the core flow; `docs/DESIGN.md` | 2.5 |
| 7 | **Smoke test, announce** | smoke test as a real customer on the live URL (fresh account, incognito); `mini-launch` (stretch) | **smoke test passed**; live post screenshot (stretch) | 2 |

## Notes for the composer

- **Go live is on Day 5 here, deliberately.** The gate and its fixes take Days 2–3 in full because this path has the time; that puts the app live with two sessions of buffer.
- **Polish uses the from-code design skill.** The code already has a de facto design system; `design-design-system-from-code` extracts it and flags inconsistencies, and `develop-design-review` fixes the ones on the core flow. If the member wants a *new* look, that's the AI-generated-app plan, not this one.
- **Day 1's code review is a baseline, not a rewrite.** Its job is to know the state before the audit and the deploy, and to catch leftover debug code and hardcoded values that become secrets in production.
- **If the audit finds nothing Critical or High**, Day 3 becomes a second polish day or brings go live forward to Day 4.

## Compression (a missed or short session)

1. Drop Announce, then Polish.
2. Merge Days 2–3: audit and fix the Critical/High only; Medium and Low go to the Fix plan for after launch.
3. Merge Days 4–5: the deploy guide is written and worked in one session on the simplest hosting path the guide names.
4. Never move the gate after go live; never move go live past Day 7.

## What Day 7 looks like

The app is live, the audit's Critical and High findings are closed, a real customer's path works at the real URL, and the core flow reads as one product. The launch post is a bonus.
