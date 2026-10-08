---
name: distribute-activation-retention-audit
description: >-
  Audits a built product for activation and retention leaks — the path from signup or install to
  the first successful output and the loop that brings users back, adapted to the product shape —
  and writes a prioritized audit with a paste-ready fix prompt to docs/ACTIVATION-RETENTION-AUDIT.md.
  Use when the user asks "why do users churn", "users sign up but don't come back", or for an
  "activation audit", and before scaling acquisition. Not for conversion surfaces (signup, pricing, checkout) — use develop-cro-audit; not
  for designing a new onboarding — use design-onboarding-flow.
---

# Distribute: Activation & Retention Audit

Run in the **app repo** — the repository that contains `productos/` — and produce a prioritized audit of the leaks between "users arrive" and "users stay": a scored breakdown of the activation path (signup → magic moment) and the retention loop (what brings users back), each finding tagged by severity, file location, effort, impact, and the fix — ending in a paste-ready prompt the member can drop into their coding agent. The output is `docs/ACTIVATION-RETENTION-AUDIT.md` (create `docs/` if needed). It runs before `distribute-scale-automate`: scaling acquisition into a product that doesn't activate or retain pours water through the holes.

**Boundary with the other two codebase audits — keep them distinct:**

- **`develop-cro-audit`** covers *arrive → sign up / pay* (conversion surfaces: performance, forms, CTAs, pricing, trust). If a finding is about getting a visitor to convert, note it and defer there; don't double-count.
- **`develop-design-review`** covers *does the UI match `DESIGN.md`* (visual consistency).
- **This skill** covers *sign up → reach the magic moment → come back*. When in doubt: CRO ends at the signup/payment event; this skill begins there.

## The auditor's voice

A senior activation and lifecycle consultant. The job is not to reassure; it's to surface the specific code gaps bleeding activation and retention, ranked by effort × impact, pointed at the exact files.

- **Honest about severity.** A signup wall before any value is a P0; a missing milestone email is a P2. Don't conflate them.
- **Specific to the file.** Never "onboarding is too long." Always "`src/onboarding/Wizard.tsx` forces 7 screens with no skip before the first value; the benchmark is ≤3."
- **Effort × Impact aware.** Sort by effort × impact, not severity alone. A 2-hour dunning-email fix that recovers passive churn beats a 2-week gamification build.
- **Calibrated to the product type.** Don't demand daily push notifications from a tax-filing app; don't accept "no re-engagement at all" from a habit tracker. Penalizing a transactional product for lacking daily mechanics is the single most common mistake.
- **Code-review tone.** Give findings the member can implement, not advice they have to translate.

## Inputs

1. **The product codebase** — **required** for software shapes. Run in the repo root; detect the framework before scanning so the file heuristics apply. For a `productized-service` or `digital-product`, the evidence is mostly outside code — intake forms, delivery records, the checkout platform — so ask the member for exports or screenshots of those, and audit whatever code exists (site, checkout, delivery automation).
2. **The Product Shape** — `docs/DEFINE.md` → `## Product Shape` → `### Primary Shape` gives the slug; read only the `## Distribute notes` section of `productos/shapes/<slug>.md` (from this skill's folder, `../../shapes/<slug>.md`) for what the shape's activation (first successful output) and repeat use look like. No Product Shape section → treat it as `web-app` unless the codebase or member clearly says otherwise, and suggest `define-product-shape`.
3. **Magic Moment** — `docs/MAGIC-MOMENT.md`. **The most valuable input** — absent only in a repo without ProductOS — it names the activation event the whole audit measures against. If absent, ask: *"What's the one action that makes a user 'get it' — the moment they feel the product working?"*
4. **Onboarding Flow** — usually `docs/ONBOARDING.md`. **Optional.** The intended first-run path; lets the audit flag where shipped code drifted from the designed flow.
5. **DEFINE.md** — usually `docs/DEFINE.md`. **Optional.** Its Summary and Offer give the product type, its Pricing Strategy the business model, and Business Strategy → North Star (when filled) the north star — which set the retention bar (daily / weekly / occasional).
6. **Measurement & Attribution** — [BONUS-Measurement-and-Attribution.md](../../distribute/BONUS-Measurement-and-Attribution.md). Optional: the Area H checks are complete without it.

If the ProductOS docs are absent, the skill works standalone using [references/benchmarks.md](references/benchmarks.md) and one or two clarifying questions.

## Workflow

### 1. Detect the shape, framework, and retention model

Read the primary shape (Inputs), then inspect the repo root and detect the framework and product type (B2B SaaS, consumer, marketplace…). **If the shape is not `web-app`, `mobile-app`, `desktop-app`, or `browser-extension`**, read [references/shape-adaptations.md](references/shape-adaptations.md) now: it redefines activation as the shape's first successful output, retention as repeat invocation or repeat purchase, and says how each area adapts. (For a `browser-extension`, the audit runs as written: the funnel starts at install, and Area B's permission prompts are the extension's install-time permissions.) Then fix the **retention model** — how often *should* this product be used? — because it sets the bar:

- **Daily / habit** (social, habit, productivity, health) → needs an active return trigger (push, streaks, digests). Judge against Day 1/7/30 retention.
- **Weekly** (most B2B SaaS, creator tools) → needs lifecycle email + a recurring reason to log in. Judge against weekly active and feature adoption.
- **Occasional / transactional** (tax, travel, events, one-off utilities) → retention is *return-to-purchase*, not daily use; judge against repeat rate and reactivation, and don't penalize the absence of daily mechanics.

For no-screen shapes, the reference file's retention model replaces these three. State it back: *"Detected: [shape] · [framework] for [product type], retention model: [daily/weekly/occasional], magic moment: [event]. Confirm or correct."* Auditing a transactional product against daily-retention benchmarks produces a misleading report.

### 2. Map the as-built activation funnel and retention loop

Before scoring, trace two paths through the actual code:

- **Activation funnel:** from auth-complete (or install, or payment, for no-screen shapes) to the magic moment or first successful output — every screen, gate, and required action in between. Count the steps. This is the spine of the activation findings.
- **Retention loop:** what, if anything, brings a user back — emails, push, scheduled jobs, stored value. If nothing does, that *is* the headline finding.

### 3. Scan the eight audit areas

Read [references/audit-areas.md](references/audit-areas.md) and walk all eight areas in order — **A–D activation** (Time-to-Value, Signup Gating, Empty States, Onboarding Friction), **E–H retention** (Re-engagement Channels, Return Loop & Stored Value, Churn & Win-Back, Instrumentation). Scan every area before drafting anything: a partial audit produces a misleading priority order. For no-screen shapes, run each area as the shape-adaptations table says; an area that genuinely doesn't apply gets one row, `N/A — [reason]`, never a silent gap.

### 4. Score and prioritize each finding

Read [references/benchmarks.md](references/benchmarks.md) to calibrate. Capture for each finding: **Area** (A–H), **Finding** (one sentence), **Location** (file + line where applicable — cite the file for every finding; for evidence outside code, the named system and setting), **Severity** (P0–P3), **Effort** (`S` <4h / `M` 1–2d / `L` >2d), **Impact** (`L` / `M` / `H` — how much fixing it moves activation or retention for this retention model), **Fix** (one specific, code-level paragraph). Rank by effort × impact: `S`+`H` first.

**Severity rubric:**
- **P0** — structurally loses users now; fix this week (signup wall before any value, app opens to a dead-end blank screen, no re-engagement mechanism at all, activation event untracked).
- **P1** — meaningful leak; fix this month (7-step forced onboarding, no welcome series, no failed-payment dunning, magic moment reachable but buried).
- **P2** — moderate opportunity; fix this quarter (no milestone emails, no exit survey, weak empty-state CTA).
- **P3** — minor; fix when convenient (no streak mechanic on a weekly product, missing reactivation A/B hook).

### 5. Cross-cutting quick wins

Five gaps that almost always have a finding: (1) the **permission prompt on first launch** before the user feels anything; (2) the **blank dashboard** with no sample data or CTA; (3) the **welcome email that doesn't exist** (only a verification email); (4) **failed-payment dunning** left entirely to Stripe defaults; (5) the **magic moment that isn't tracked**, so activation can't be measured or improved. For no-screen shapes, the equivalents: setup or a key demanded before the first output; an error on first run that doesn't say what to do next; no owned contact with the user (no email at licence, download, or purchase); dunning missing on paid licences or retainers; the first successful output not counted anywhere.

### 6. Cross-reference ProductOS docs (strategy-code drift)

If `docs/MAGIC-MOMENT.md` or `docs/ONBOARDING.md` exist, check the shipped code against them: does the onboarding match the designed flow? Does the documented activation event actually fire and get tracked? Drift between documented strategy and shipped code is a P1 finding — the thinking was done but the code didn't follow.

### 7. Draft section-by-section, then write the audit

Build the audit one section at a time, confirming findings with the member as you go (the conversation about the leaks is the point). Then write `docs/ACTIVATION-RETENTION-AUDIT.md` (`mkdir -p docs` if needed) in the structure of [templates/audit-skeleton.md](templates/audit-skeleton.md). In *Sources & calibration*, keep each benchmark's source next to it. Keep prose tight; tables over paragraphs — it should read in 5–8 minutes for a developer skimming for fixes. The fix prompt is the payoff: concrete enough to paste and run.

### 8. Verify before delivering

- [ ] All eight areas (A–H) are covered — any that don't apply to the shape marked `N/A` with a reason — and the activation funnel and retention loop are mapped as-built.
- [ ] Activation and retention match the shape: first successful output and repeat use for no-screen shapes, and any telemetry recommended is opt-in and disclosed.
- [ ] Every finding has a file location where applicable, and an Effort (`S`/`M`/`L`) and Impact (`L`/`M`/`H`).
- [ ] Severities are honest (signup-wall-before-value = P0, missing streak = P3).
- [ ] The Top 5 are ranked by effort × impact.
- [ ] The audit honors the retention model (no daily-push findings for a transactional product).
- [ ] Conversion-surface findings are deferred to `develop-cro-audit`, not double-counted.
- [ ] Cross-cutting quick wins and (if ProductOS docs are present) strategy-code drift are surfaced.
- [ ] The fix prompt lists the P0/P1 leaks with their locations.

Give the member the file path and a tight summary — total findings, P0 count, the single biggest leak. Next step: implement the Top 5 (P0s and `S`/`M` effort first), instrument the magic-moment event if it isn't tracked, take a Day 1/Day 7 retention baseline, and re-run in 30 days; only once activation holds should the member return to `distribute-scale-automate` and pour traffic on.
