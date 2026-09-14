# Ship in 7 — plan: AI-generated app, not live

*The member has an app that a coding agent or a prompt-to-app tool built. It runs, but it looks generated: the default component-library look, inconsistent spacing, marketing-voice copy, no design system behind it. It has never been deployed. Seven sessions to a live app that looks designed.*

## The seven sessions

| Day | Block | Skill(s) | Proof | Hours |
| --- | --- | --- | --- | --- |
| 1 | **Define backfill** | `define-from-code` → `define-product` (skip if `docs/PRODUCT.md` exists and is current) | `docs/PRODUCT.md` exists; the extracted offer confirmed by the member | 1.5 |
| 2 | **Words + Look** | `design-identity-creator` → `design-ux-writing` (with its audit of the real UI strings) → `design-design-system` from one image the member loves | Brand Card; `docs/COPY.md` with the fix list; `docs/DESIGN.html` screenshot | 3 |
| 3 | **Rebuild, day one** | `develop-design-better` + the build loop on the highest-traffic screen; `develop-design-review` before commit | before/after of that screen | 4+ |
| 4 | **Rebuild, day two** | same, on the onboarding-to-magic-moment screens; apply `docs/COPY.md`'s fix list | before/after of the core flow | 4+ |
| 5 | **Quality gate** | `develop-code-review` → `develop-security-audit` → Critical/High fixed | `docs/SECURITY-AUDIT.md` verdict; Critical/High ticked | 2 |
| 6 | **Deploy guide + go live** | `develop-golive` → work `docs/DEPLOY.md` | live URL, HTTPS | 3 |
| 7 | **Smoke test, buffer, announce** | smoke test as a real customer; `develop-design-review` over the whole app if there's time; `mini-launch` (stretch) | **smoke test passed**; live post screenshot (stretch) | 2 |

## Notes for the composer

- **`design-design-system-from-code` is the wrong tool here.** It reverse-engineers the system already in the code; on this path the code has no system worth keeping. Use `design-design-system` from an image the member picks, so the rebuild has a look to converge on.
- **Rebuild, don't refactor.** `develop-refactor-plan` audits code against a PRD; this path has no PRD and the problem is the surface, not the structure. `develop-design-better` plus the build loop, screen by screen, is the mechanism. If the code is genuinely a mess underneath (the security audit or the code review says so), the local-prototype plan's Day 3 fixes apply and one rebuild day is dropped.
- **Two rebuild days cover the core flow, not the app.** Signup, onboarding, the magic moment screen, and whatever the highest-traffic screen is. Settings pages, admin screens, and edge states are later.
- **The copy fix list is part of the rebuild.** `design-ux-writing`'s audit produces an executable fix list for the real UI strings; Day 4 applies it alongside the visual rebuild so the app stops speaking in marketing English too.

## Compression (a missed or short session)

1. Drop Announce.
2. Merge Days 3–4 into one: the magic moment screen and the screen before it, nothing else.
3. Merge Words into Look: identity in a paragraph from `docs/PRODUCT.md`, `docs/COPY.md` from the ux-writing skill's defaults without the audit pass.
4. Never move the gate after go live; never move go live past Day 7.

## What Day 7 looks like

The app is live at a real URL, a real customer's path through it works, and the core screens look like they belong to one product. Not every screen — the core ones.
