---
name: develop-feature-finder
description: >-
  Turns a business objective (activation, retention, conversion, revenue, referrals) into ranked
  feature recommendations for an existing app — reviewing the codebase, researching comparable
  products, and giving evidence, effort, and a metric for each — then offers to append the chosen
  ones to the build plan. Use when the user asks "what should I build next", "features to improve
  retention", or "what would increase activation". Not for finding a product idea — use
  define-idea-finder; not for channel or funnel experiments — use distribute-growth-experiments.
---

# Develop: Feature Finder

Turn a business objective into ranked, evidence-backed feature recommendations grounded in what the app actually is today — not generic growth advice.

## 1. Pin down the objective

Ask what the member wants to achieve. If they're vague, offer the common shapes: activation (more users reach the core value), retention (they come back), conversion (free → paid), revenue per user, referrals/virality, engagement depth, or reduced churn. Push until the objective is measurable — *"improve retention"* becomes *"more users return in week 2."* One objective per session; mixing goals produces mush.

## 2. Review the codebase

Read the repository to understand the product as built: what it does, the core user journey (entry → value → return), existing features, pricing/paywall surfaces, onboarding, notifications/emails, and what analytics or instrumentation exist. If product docs are present (e.g. `docs/DEFINE.md`, `docs/MAGIC-MOMENT.md`, a PRD, a roadmap), read them for the customer, magic moment, and what's already planned — don't recommend what's already on the roadmap. Note the stack, since it bounds what's cheap vs. expensive to build.

## 3. Research what works

Research the objective live — current best practices for this product category, and specifically what named comparable products have done with documented results (e.g. Duolingo's streaks for retention, Dropbox's referral storage, Superhuman's onboarding for activation). Prioritize documented outcomes over listicle advice. Map each pattern against this app: does the mechanism that made it work exist here? If web search isn't available, say so, ask the member for comparables they know, and mark those claims unverified.

## 4. Recommend

Present 5–8 candidates, ranked by expected impact against effort. For each:

- **The feature or change** — concrete enough to picture, specific to this app (name the screens/flows it touches).
- **Why it should work** — the mechanism, with the comparable product and its documented result.
- **Effort** — S/M/L given the actual stack and codebase.
- **How to measure** — the metric that proves it moved the objective, and whether the app can currently measure it (if not, instrumentation is part of the work).
- **Risk or trade-off** — honestly stated; e.g. notification fatigue, paywall friction, scope creep.

Lead with your top 3 in detail; list the rest briefly. Include at least one cheap, unglamorous option (copy, ordering, or friction-removal changes often beat new features) and flag any recommendation that's fashionable but a poor fit for this product.

## 5. Hand off

Discuss and let the member pick. For chosen recommendations, offer to add them as tasks ready for `build-loop` to execute:

- Append them to `docs/ROADMAP.md` — or `docs/REFACTOR.md` if that's the active plan — as `TASK-NNN` continuing from the last ID, in the three-line format from `productos/develop/guides/ROADMAP-GENERATION.md` (checkbox + ID + description, `Files:`, `Notes:` ending with `Verify:`), sized to one agent session and ordered.
- Update the plan's `**Status:** X/Y tasks complete` total to include them.
- Never write to `docs/PLAN.md` or the `productos/*-CHECKLIST.md` files — they are not build plans.

Outside ProductOS (no `docs/ROADMAP.md`), add them to the repo's existing task list if there is one; if no plan exists, offer to write the chosen recommendations up as one.

## Rules

- Every recommendation must trace to the stated objective — no pet features.
- Evidence over instinct: name the comparable, cite the documented result, and say when evidence is thin.
- Respect what exists: recommendations build on the current codebase and stack, not an imaginary rewrite.
- Be honest when the objective's biggest lever isn't a feature at all (pricing, positioning, distribution) — say so and point at the right phase instead of inventing product work.
