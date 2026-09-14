# Ship in 7 — plan: Idea only

*The member has an idea and an empty repo (or nothing but `productos/`). Seven sessions to a live app with one working core flow.*

**Honest note at enrol:** this is the path where hours matter most. As written below the week is roughly twenty hours, about three a session, with the build days carrying the most. At two hours a session it fits only with a smaller magic moment (sign up → do the one thing → see it work; no logo upload, no editing, no settings); at one hour it doesn't fit. Say so before writing the plan, and offer the two honest alternatives: more hours, or the smaller magic moment. Tell the member on Day 1 to bring **one image or website they love** for Day 2's design system.

## The seven sessions

| Day | Block | Skill(s) | Proof | Hours |
| --- | --- | --- | --- | --- |
| 1 | **Define from idea** | `studio-define-offer-builder` → `studio-define-customer-persona` → `studio-define-pricing` → `studio-define-product`, one sitting, no research rabbit holes | `docs/PRODUCT.md` exists, 8 sections filled; the offer read out loud | 3 |
| 2 | **Look + magic moment + spec** | `studio-design-design-system` from one image the member loves → `studio-design-magic-moment` → `studio-develop-prd-roadmap` with the MVP scoped to the magic moment only | `docs/DESIGN.html` screenshot; `docs/ROADMAP.md` with one phase | 2.5 |
| 3 | **Build, day one** | `studio-develop-mvp-build` (or the build loop task by task) | a screenshot of the first working screen, saved to `docs/` | 4 |
| 4 | **Build, day two** | continue; the core flow works end to end locally | screenshots of signup → magic moment, saved to `docs/`; the test suite passing | 4 |
| 5 | **Quality gate** | `studio-develop-code-review` → `studio-develop-security-audit` → Critical/High fixed via the build loop | `docs/SECURITY-AUDIT.md` verdict; Critical/High ticked | 2 |
| 6 | **Deploy guide + go live** | `studio-develop-golive` → work `docs/DEPLOY.md` top to bottom | live URL, HTTPS | 3 |
| 7 | **Smoke test, buffer, announce** | smoke test as a real customer; fix what it finds; `studio-launch` if there's time | **smoke test passed**; live post screenshot (stretch) | 2 |

## Notes for the composer

- **No Words block.** Identity and the copy guide are worth having, but not this week. The design system gives the build its tokens; `docs/COPY.md` can come after launch. If hours allow (4h+), add `studio-design-ux-writing` to Day 2 so the first screens are copy-correct.
- **The spec is the scope control.** `studio-develop-prd-roadmap` will want to scope a full MVP; brief it with the challenge: one phase, the magic moment and the path to it, everything else in "later". The roadmap must fit two build days.
- **Day 1 is the long one.** Four Define skills in one sitting is possible because the challenge sets the pace: the offer-builder's interview, then persona and pricing at their fastest, then the synthesis. No web-research spirals; the pricing skill's fast path (about thirty minutes: one model, one unit, one number) is the model.
- **Build days are the only days that can absorb more hours.** If the member has 4h+, Day 4 usually finishes early; pull the quality gate forward and give Day 6 a full buffer.

## Compression (a missed or short session)

1. Drop Announce.
2. Merge Days 3–4 into one build day: the magic moment screen only, no onboarding, no settings.
3. Shorten Day 2's Look: run `studio-design-design-system` with the framework's default component library as the reference instead of a chosen image, and move on to the spec.
4. Never move Day 5 (gate) after Day 6 (go live). Never move go live past Day 7.

## What Day 7 looks like

A real person (the member, in an incognito window, with a fresh account) signs up, does the one thing, and sees it work at a URL that isn't localhost. That's the bar. The launch post is a bonus.
