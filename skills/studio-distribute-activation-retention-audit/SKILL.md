---
name: studio-distribute-activation-retention-audit
description: Use when the user has a working product codebase and wants to find the activation and retention leaks — why new users don't reach the magic moment, and why existing users don't come back — and fix them. Triggers on phrases like "activation audit", "retention audit", "find my leaks", "why do users churn", "fix my onboarding", "users sign up but don't come back", "leaky bucket", or "audit my activation funnel". Runs in the app repo — the repository that contains `productos/`. Detects product type, maps the as-built activation funnel (signup to magic moment) and retention loop (what brings users back), checks instrumentation, and writes a prioritized audit to `docs/ACTIVATION-RETENTION-AUDIT.md` (or repo root if no `docs/`) with a paste-ready fix prompt. Optionally references ProductOS files (`docs/PRODUCT.md`, `productos/design/2-Magic-Moment.md`, `productos/design/3-Onboarding-Flow.md`, `productos/distribute/BONUS-Measurement-and-Attribution.md`) if present; works standalone.
---

# Distribute: Activation & Retention Audit

This skill runs in the **app repo** — the repository that contains `productos/` — and produces a prioritized **activation and retention audit** — the leaks between "users arrive" and "users stay." The output is `docs/ACTIVATION-RETENTION-AUDIT.md` (or `ACTIVATION-RETENTION-AUDIT.md` at the repo root): a scored breakdown of the activation path (signup → magic moment) and the retention loop (what brings users back), each finding tagged by severity, file location, and the fix — ending in a paste-ready prompt the user can drop into their coding agent to fix the top leaks in one pass.

This exists because of the **leaky bucket**: scaling acquisition into a product that doesn't activate or retain just pours water through the holes. Before a founder runs the Scale skill and pours traffic on, this audit finds the holes. Most products lose more users to three or four fixable code gaps — a signup wall before any value, a blank empty state, no re-engagement email at all, an activation event that isn't even tracked — than to anything wrong with their acquisition.

**Boundary with the other two codebase audits — keep them distinct:**

- **`studio-develop-cro-audit`** covers *arrive → sign up / pay* (conversion surfaces: performance, forms, CTAs, pricing, trust). If a finding is about getting a visitor to convert, it belongs there.
- **`studio-develop-design-review`** covers *does the UI match `DESIGN.md`* (visual consistency).
- **This skill** covers *sign up → reach the magic moment → come back* (everything after the conversion). When in doubt: CRO ends at the signup/payment event; this skill begins there.

The voice is a senior activation and lifecycle consultant who has audited hundreds of products and knows the 2026 patterns that separate products retaining 40%+ at Day 1 from products leaking 75% of signups in the first session. The job is not to reassure; it's to surface the specific code gaps bleeding activation and retention right now, ranked by effort × impact, pointed at the exact files where the fixes live.

## The auditor's voice

- **Honest about severity.** A signup wall before any value is a P0; a missing milestone email is a P2. Don't conflate them.
- **Specific to the file.** Never "onboarding is too long." Always "`src/onboarding/Wizard.tsx` forces 7 screens with no skip before the first value; the benchmark is ≤3."
- **Effort × Impact aware.** Sort by effort × impact, not severity alone. A 2-hour dunning-email fix that recovers passive churn beats a 2-week gamification build.
- **Calibrated to the product type.** Don't demand daily push notifications from a tax-filing app; don't accept "no re-engagement at all" from a habit tracker.
- **Code-review tone.** The user is a technical founder; give findings they can implement, not advice they have to translate.

## Inputs

1. **The user's product codebase** — **required**. Run in the repo root; detect the framework (Next.js, Vite/React, Vue/Nuxt, SvelteKit, Remix, native iOS/Android, Electron/Tauri, Expo/React Native, backend frameworks) before scanning so the file heuristics apply.

2. **Magic Moment** — at `productos/design/2-Magic-Moment.md`. **The most valuable input** — absent only in a repo without ProductOS — it names the activation event the whole audit measures against. If absent, ask: *"What's the one action that makes a user 'get it' — the moment they feel the product working?"*

3. **Onboarding Flow** — usually `productos/design/3-Onboarding-Flow.md`. **Optional.** The intended first-run path; lets the audit flag where shipped code drifted from the designed flow.

4. **PRODUCT.md** — usually `docs/PRODUCT.md`. **Optional.** Provides product type, north star, and business model — which set the retention bar (daily / weekly / occasional).

5. **Measurement & Attribution** — usually `productos/distribute/BONUS-Measurement-and-Attribution.md`. **Optional.** The reference for the instrumentation check in Area H.

If the ProductOS docs are absent, the skill works standalone using the calibration benchmarks embedded below and one or two clarifying questions.

## Workflow

### 1. Detect the product type, framework, and retention model

Inspect the repo root and detect the framework and product type (mobile app, B2B SaaS, marketplace, dev tool, consumer web, extension, productized service). Then fix the **retention model** — how often *should* this product be used? — because it sets the bar:

- **Daily / habit** (social, habit, productivity, health) → needs an active return trigger (push, streaks, digests). Judge against Day 1/7/30 retention.
- **Weekly** (most B2B SaaS, creator tools) → needs lifecycle email + a recurring reason to log in. Judge against weekly active and feature adoption.
- **Occasional / transactional** (tax, travel, events, one-off utilities) → retention is *return-to-purchase*, not daily use; judge against repeat rate and reactivation, and don't penalize the absence of daily mechanics.

State it back: *"Detected: [framework] for [product type], retention model: [daily/weekly/occasional], magic moment: [event]. Confirm or correct."* Auditing a transactional product against daily-retention benchmarks produces a misleading report.

### 2. Map the as-built activation funnel and retention loop

Before scoring, trace two paths through the actual code:

- **Activation funnel:** from auth-complete to the magic moment — every screen, gate, and required action in between. Count the steps. This is the spine of the activation findings.
- **Retention loop:** what, if anything, brings a user back — emails, push, scheduled jobs, stored value. If nothing does, that *is* the headline finding.

### 3. Scan the eight audit areas

Walk these in order. For each, scan for the patterns, surface findings, and score them. **A–D are activation; E–H are retention.**

#### A. Time-to-Value & the Activation Path
Users who reach the "aha" in their first session (or within 48h) are ~3.4× more likely to convert to paid.
- Count actions from auth-complete to the magic moment (cross-ref `productos/design/2-Magic-Moment.md`) — flag if >3–5, or if it requires setup/config first.
- Is the magic moment engineered into the first-run path at all? Flag if the documented activation event isn't visibly built before the user hits the general UI.
- "Setup tax" before value — mandatory profile completion, workspace config, integration connection. Flag anything that delays the first win.
- A guided path to the first win vs. dumping the user into the full app.

#### B. Signup Gating & Friction Walls
The most common activation leak is a wall placed before any value.
- Auth wall before any value — flag forced signup before a demo/sample/try-it; prefer value-first or a guest mode.
- Permission prompts (push / location / contacts / camera) fired on first launch before value — flag (tanks opt-in and trust).
- Hard paywall before the magic moment — flag for products that should let users *feel* value first.
- Email-verification hard gate blocking first use — flag.
- SSO on signup — flag if absent (every extra signup step costs activation).

#### C. Empty States & First-Run Guidance
A new user in a blank screen with no next action is a silent killer.
- Empty-state handling — does the app open to a blank dashboard/list? Flag absence.
- Seed/sample data or templates for first-run — flag absence where a blank workspace = no value (B2B SaaS, tools).
- Getting-started checklist / first-action prompt / contextual tips — flag absence.
- Progressive disclosure — flag if the full UI dumps at once instead of guiding the first action.
- Every empty state has a primary CTA toward the magic moment — flag dead-end empty states.

#### D. Onboarding Flow Friction
- Onboarding step count (search `onboarding`/`welcome`/`getting-started` routes/components) — flag >3–5 screens. Benchmark: 3-step tours complete at ~72%, 7-step at ~16%.
- Skippable / non-blocking — flag forced tours with no skip.
- Required fields — flag every required field not essential to the first value.
- Progress indication — flag missing step counter/progress.
- Onboarding ends **at** the magic moment, not before it — flag flows that dump the user at a dashboard short of the aha. Cross-ref `productos/design/3-Onboarding-Flow.md` for drift.

#### E. Re-engagement Channels *(the #1 retention leak)*
The most common retention leak is *no mechanism to bring users back at all*.
- Lifecycle email infrastructure (Resend, Postmark, SendGrid, Loops, Customer.io, Klaviyo) — flag if only transactional email exists, or none.
- Welcome / onboarding email series — flag absence.
- Re-engagement / win-back emails for dormant users ("you left X unfinished," "we miss you") — flag absence.
- Milestone / triggered / behavioral emails — flag absence.
- Push notifications (mobile/PWA): SDK present, permission asked *after* first value, and actual triggered sends wired up — flag if a daily/weekly product has no push.
- Calibrate to the retention model: daily products need an active trigger; occasional products lean on email and can skip push.

#### F. The Return Loop & Stored Value
Is there a reason *and* a trigger to come back?
- A recurring trigger — scheduled digests, reminders, streaks, cron jobs that nudge users back. Flag absence for habit/daily products.
- Stored value / saved state — does use accumulate data, history, or config that creates switching cost? Flag "stateless" products that reset each session.
- Progress / streaks / personalization that improves with use — flag if the product is identical on day 30 as day 1 (calibrate to type).

#### G. Churn & Win-Back Surfaces
Where users leave, and whether anything catches them.
- Cancel flow — a save offer / pause / downgrade step, or one-click cancel into the void? Flag the absence of any retention step.
- Failed-payment dunning — Stripe smart retries + dunning emails. Flag absence: involuntary/passive churn is a large share of subscription churn (often ~20–40%) and the cheapest to recover.
- Downgrade path vs. hard cancel for price-sensitive churners — flag if cancel is the only option.
- Exit survey / cancellation-reason capture — flag absence (silent churn teaches you nothing).
- Grace period / post-cancel win-back offer — flag absence.

#### H. Activation & Retention Instrumentation
You can't fix a leak you can't see (cross-ref `productos/distribute/BONUS-Measurement-and-Attribution.md`).
- Is the magic-moment / activation event tracked? Flag if the activation event doesn't fire to analytics.
- Funnel events (signup → activated → retained) instrumented — flag gaps.
- Retention measurability — product analytics that can cut cohorts/returns (PostHog, Mixpanel, Amplitude). Flag if only page-view analytics exist (can't see retention).
- Churn events (cancel, payment_failed, reactivated) tracked — flag absence.
- A retention/north-star metric visible somewhere — flag if the team is flying blind.

### 4. Score and prioritize each finding

Capture for each: **Area** (A–H), **Finding** (one sentence), **Location** (file + line where applicable), **Severity** (P0–P3), **Effort** (S <4h / M 1–2d / L >2d), **Estimated impact**, **Fix** (one specific, code-level paragraph).

**Severity rubric:**
- **P0** — structurally loses users now; fix this week (signup wall before any value, app opens to a dead-end blank screen, no re-engagement mechanism at all, activation event untracked).
- **P1** — meaningful leak; fix this month (7-step forced onboarding, no welcome series, no failed-payment dunning, magic moment reachable but buried).
- **P2** — moderate opportunity; fix this quarter (no milestone emails, no exit survey, weak empty-state CTA).
- **P3** — minor; fix when convenient (no streak mechanic on a weekly product, missing reactivation A/B hook).

### 5. Cross-cutting quick wins

Five gaps that almost always have a finding: (1) the **permission prompt on first launch** before the user feels anything; (2) the **blank dashboard** with no sample data or CTA; (3) the **welcome email that doesn't exist** (only a verification email); (4) **failed-payment dunning** left entirely to Stripe defaults; (5) the **magic moment that isn't tracked**, so activation can't be measured or improved.

### 6. Cross-reference ProductOS docs (strategy-code drift)

If `productos/design/2-Magic-Moment.md` or `productos/design/3-Onboarding-Flow.md` exist, check the shipped code against them: does the onboarding match the designed flow? Does the documented activation event actually fire and get tracked? Drift between documented strategy and shipped code is a P1 finding — the thinking was done but the code didn't follow.

### 7. Draft section-by-section, then write the report

Build the report one section at a time, confirming findings with the user as you go (the conversation about the leaks is the point). Then write `docs/ACTIVATION-RETENTION-AUDIT.md` (or `ACTIVATION-RETENTION-AUDIT.md` at root):

```
# Activation & Retention Audit

*Drafted: [Month Year]. Product type: [type]. Framework: [framework]. Retention model: [daily/weekly/occasional]. Magic moment: [event].*

## Summary
[Three sentences: total findings, P0/P1 count, the single biggest leak and its headline fix.]

## Top 5 fixes ranked by effort × impact
1. **[Finding]** — `[location]` — P[X], Effort [S/M/L], Est. impact [x]. [One-sentence fix.]
2. … 3. … 4. … 5. …

## The activation funnel as-built
[The steps from signup to magic moment, friction flagged. Name the step count and the drop points.]

---
## A. Time-to-Value & the Activation Path
| # | Finding | Location | Sev | Effort | Impact | Fix |
| --- | --- | --- | --- | --- | --- | --- |
| A1 | … | `[file]:[line]` | P0 | S | … | … |
## B. Signup Gating & Friction Walls
## C. Empty States & First-Run Guidance
## D. Onboarding Flow Friction
[same table structure for B–D]

## The retention loop as-built
[What brings users back — or "nothing currently does."]

## E. Re-engagement Channels
## F. The Return Loop & Stored Value
## G. Churn & Win-Back Surfaces
## H. Activation & Retention Instrumentation
[same table structure for E–H]

---
## Cross-cutting quick wins
[the 5, with specific findings]

## Strategy-code drift (if ProductOS docs present)
[where documented magic moment / onboarding ≠ shipped code]

## Fix prompt (paste into your coding agent)
> Fix the following activation and retention leaks in this codebase. For each, the file and the change:
> 1. [P0 finding] — `[file:line]` — [the change].
> 2. …
> Work through them top to bottom; after each, confirm the activation event fires and is tracked.

## Verification next steps
- [ ] Confirm the magic-moment event fires and is tracked in analytics
- [ ] Measure Day 1 / Day 7 retention as a baseline
- [ ] Send a test through each lifecycle email / push trigger
- [ ] Re-run this audit in 30 days to measure the lift

## Sources & calibration
[benchmarks used + workspace docs referenced if present]
```

Keep prose tight; tables over paragraphs. Reads in 5–8 minutes for a developer skimming for fixes.

### 8. Verify before delivering

Check: every finding has a file location where applicable; severities are honest (signup-wall-before-value = P0, missing streak = P3); the Top 5 are ranked by effort × impact; the audit honors the retention model (no daily-push findings for a transactional product); strategy-code drift is surfaced if ProductOS docs are present; the fix prompt lists the P0/P1 leaks with their locations. Deliver via a `computer://` link with a tight summary — total findings, P0 count, the single biggest leak.

## Calibration benchmarks (embedded for standalone use)

Directional 2026 figures — verify before quoting externally:
- **Activation:** reaching the aha within the first session (or 48h) → ~3.4× more likely to convert to paid. A large share of signups never reach first value when a setup wall precedes it.
- **Onboarding:** 3-step tours complete at ~72%, 7-step at ~16%. Day 1 retention baseline ~26%, optimized 40%+.
- **Retention curves:** most consumer apps lose the majority of users in the first week; the curve should *flatten* (a stable returning core), not trend to zero. B2B SaaS healthy logo retention is high (90%+ annual); consumer varies widely by category.
- **Re-engagement:** lifecycle email and (where it fits) push meaningfully lift retention vs. transactional-only; a welcome series is the highest-leverage first send.
- **Passive churn:** involuntary/failed-payment churn is often ~20–40% of total subscription churn and is the cheapest to recover with smart retries + dunning emails.
- Calibrate all of the above to the product's retention model before scoring.

## Pacing and approval

- **Scan all eight areas before drafting.** A partial audit produces a misleading priority order.
- **Cite the file for every finding.** "Onboarding is long" is a vibe; `src/onboarding/Wizard.tsx` with 7 forced screens is a fix.
- **Severity-honest, and calibrated to the retention model.** The single most common mistake is penalizing a transactional product for lacking daily mechanics.
- **Boundary discipline.** If a finding is really about signup/payment conversion, note it and defer to `studio-develop-cro-audit`; don't double-count.
- **The fix prompt is the deliverable's payoff.** Make it concrete enough to paste and run.

## What "done" looks like

A `docs/ACTIVATION-RETENTION-AUDIT.md` where all eight areas (A–H) are covered with file-located findings; the activation funnel and retention loop are mapped as-built; the Top 5 fixes are ranked by effort × impact; cross-cutting quick wins and (if ProductOS docs are present) strategy-code drift are surfaced; and a paste-ready fix prompt lists the P0/P1 leaks with their locations. The whole doc reads in 5–8 minutes.

Recommended next step after a successful session: implement the Top 5 (start with P0s + S/M effort), instrument the magic-moment event if it isn't tracked, take a Day 1/Day 7 retention baseline, and re-run in 30 days. Only once activation holds should the user return to `studio-distribute-scale-automate` and pour traffic on.
