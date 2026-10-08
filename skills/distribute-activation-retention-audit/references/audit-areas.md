# Audit areas — the eight-area scan

Walk these in order at step 3. For each area, scan the codebase for the patterns, surface findings, and score them (step 4). **A–D are activation; E–H are retention.** Calibrate every check to the retention model fixed in step 1.

#### A. Time-to-Value & the Activation Path
Users who reach the "aha" in their first session (or within 48h) are far more likely to convert and retain.
- Count actions from auth-complete to the magic moment (cross-ref `docs/MAGIC-MOMENT.md`) — flag if >3–5, or if it requires setup/config first.
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
- Onboarding step count (search `onboarding`/`welcome`/`getting-started` routes/components) — flag >3–5 screens; completion falls steeply with each added step.
- Skippable / non-blocking — flag forced tours with no skip.
- Required fields — flag every required field not essential to the first value.
- Progress indication — flag missing step counter/progress.
- Onboarding ends **at** the magic moment, not before it — flag flows that dump the user at a dashboard short of the aha. Cross-ref `docs/ONBOARDING.md` for drift.

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
- Failed-payment dunning — Stripe smart retries + dunning emails. Flag absence: involuntary/passive churn is a large share of subscription churn and the cheapest to recover.
- Downgrade path vs. hard cancel for price-sensitive churners — flag if cancel is the only option.
- Exit survey / cancellation-reason capture — flag absence (silent churn teaches you nothing).
- Grace period / post-cancel win-back offer — flag absence.

#### H. Activation & Retention Instrumentation
You can't fix a leak you can't see. The checks below are complete on their own; if `productos/distribute/BONUS-Measurement-and-Attribution.md` exists, use it for the event-naming and funnel conventions.
- Is the magic-moment / activation event tracked? Flag if the activation event doesn't fire to analytics.
- Funnel events (signup → activated → retained) instrumented — flag gaps.
- Retention measurability — product analytics that can cut cohorts/returns (PostHog, Mixpanel, Amplitude). Flag if only page-view analytics exist (can't see retention).
- Churn events (cancel, payment_failed, reactivated) tracked — flag absence.
- A retention/north-star metric visible somewhere — flag if the team is flying blind.
