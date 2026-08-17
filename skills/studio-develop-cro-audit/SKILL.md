---
name: studio-develop-cro-audit
description: Use when the user has a working product codebase (web/mobile app, SaaS, marketplace, dev tool, extension, or landing page) and wants a conversion rate optimization audit of the code — what's slowing conversion, what's missing, what to fix first. Triggers on phrases like "audit my conversion rate", "CRO audit", "review my code for conversion", "what's hurting my signup rate", "find my conversion bottlenecks", "why aren't users converting", or "are my forms killing conversion". Runs in the app repo — the repository that contains `productos/`. Detects product type, scans for conversion-relevant patterns (forms, CTAs, Core Web Vitals, analytics, mobile, paywall placement, trust signals), and writes a prioritized audit to `docs/CRO-AUDIT.md` (or repo root if no `docs/`). Optionally references ProductOS files (`docs/PRODUCT.md`, `productos/design/1-Product-Identity.md`, `productos/design/2-Magic-Moment.md`) if present; works standalone.
---

# Develop: Conversion Rate Optimization Audit

This skill runs in the **app repo** — the repository that contains `productos/` — and produces a prioritized **conversion rate optimization audit** of the current state of the code. The output is `docs/CRO-AUDIT.md` (or `CRO-AUDIT.md` at the repo root) containing a scored breakdown of conversion-relevant surfaces — performance, forms, CTAs, trust signals, paywall placement, analytics tracking, mobile experience, and onboarding — with each issue tagged by severity, location in the codebase, and the fix.

The voice is a senior conversion rate optimization consultant with deep experience auditing thousands of product codebases across consumer mobile, B2B SaaS, marketplaces, developer tools, and landing pages — and specifically with the 2026 patterns that separate products converting at 8–15% (top-decile B2B SaaS) from products converting at 1.5–2.5% (category average). The consultant's job is not to tell the user their code is fine; it is to surface the specific high-impact issues that are bleeding conversion right now, prioritize them by effort × impact, and point the user to the exact files and lines where the fixes live.

Conversion rate is a downstream consequence of dozens of upstream code decisions. Most products lose 30–50% of potential conversion to four or five fixable code issues (slow LCP, too-long signup forms, missing trust signals above the fold, no mobile-specific paywall flow, no behavioral analytics on the funnel). This skill's job is to find those issues in the code and tell the user what to fix first.

> **Session length:** Designed to be completable in 30–60 minutes. The skill scans the codebase, runs the audit, drafts the report section by section with the user, and writes the file at the end. No external research or live A/B testing required during the session — the audit is a code review, not an experiment.

## Inputs

Locate the following:

1. **The user's product codebase** — **required**. The skill runs in the repository root and scans the source files. Detect the framework (Next.js, Vite/React, Vue, SvelteKit, Remix, native iOS/Android, Electron, browser extension manifest, plain HTML, etc.) before scanning so the file structure heuristics apply correctly.

2. **PRODUCT.md** — at `docs/PRODUCT.md`. **Recommended** — in a repo without ProductOS it's simply absent; proceed standalone. Provides the product type, customer, magic moment, and business model — which drives which audit areas are prioritized. If absent, ask the user one question: *"What kind of product is this — mobile app / B2B SaaS / marketplace / API or developer tool / landing page / browser extension / productized service portal? And what's the primary conversion event you care about — signup, free-trial start, paid conversion, first transaction, first AI output?"*

3. **The relevant BONUS reference** — in `productos/design/` or `productos/design/onboarding/`. **Optional** — absent in a repo without ProductOS. When present, the skill loads:
   - `productos/design/BONUS-Web-Landing-Page-Best-Practice.md` for web/desktop conversion patterns
   - `productos/design/BONUS-App-Store-Listing-Best-Practice.md` for mobile listing context
   - `productos/design/onboarding/BONUS-[Type]-Onboarding-Best-Practice.md` for in-product activation
   These supply the calibration tables and tactic numbers the audit cites.

4. **Magic Moment, Product Identity** — usually `productos/design/2-Magic-Moment.md` and `productos/design/1-Product-Identity.md` if present. **Optional.** Provides the activation event the audit measures against and the tone the audit applies to copy critiques.

If PRODUCT.md and the BONUS docs are missing, the skill works standalone using the calibration tables embedded in the workflow section below.

## The auditor's voice

Adopt the voice of a senior CRO consultant doing a technical code review:

- **Honest about severity.** Real auditors don't pad reports. A 3-second LCP is a P0 problem; a missing alt tag is a P3. Don't conflate them.
- **Specific to the file.** Never "the signup form has too many fields." Always "`src/components/SignupForm.tsx:42–67` has 8 required fields; the documented benchmark is 1–2."
- **Effort × Impact aware.** Sort findings by effort × impact, not by personal taste. A 4-hour fix that lifts conversion 8% beats a 40-hour fix that lifts it 12%.
- **Reference-anchored.** Every finding cites either the documented benchmark from the ProductOS BONUS docs (if present) or the inline calibration table below.
- **Code-review tone.** Not marketing fluff. The user is a developer or a technical founder; they want findings they can implement, not bullet points they have to translate.

## Workflow

### 1. Detect the product type and framework

Inspect the repository root. Look for canonical indicators:

- `package.json` with `next` → Next.js web/landing page
- `package.json` with `vite` + `react` → React SPA
- `vue.config.js` / `nuxt.config.*` → Vue/Nuxt
- `svelte.config.js` → SvelteKit
- `remix.config.js` → Remix
- `Info.plist` / `*.xcodeproj` → native iOS
- `AndroidManifest.xml` / `build.gradle` → native Android
- `Cargo.toml` + `tauri.conf.json` → Tauri desktop
- `package.json` with `electron` → Electron desktop
- `manifest.json` with `manifest_version` → browser extension
- Plain `*.html` + `*.css` + `*.js` → static landing page
- Backend frameworks (Rails, Django, Phoenix, Express) → server-rendered web

If PRODUCT.md is present, cross-reference its product type against the framework. If PRODUCT.md is absent, ask the user.

State the detected setup back: *"Detected: [framework] for [product type]. Auditing against the [BONUS reference] pattern, primary conversion event: [event]. Confirm or correct."*

### 2. Scan for the eleven audit areas

Walk through eleven audit areas in order. For each, scan the codebase for the specific patterns documented below, surface the findings, score them, and capture them for the report.

#### A. Performance & Core Web Vitals

The single highest-leverage conversion lever in 2026. Every 100ms of LCP delay correlates with ~1.11% conversion drop (Deloitte/eBay study). Sites meeting all three Core Web Vitals thresholds see ~24% fewer abandons.

**2026 thresholds:**
- **LCP** (Largest Contentful Paint) — good: <2.5s, poor: >4s
- **INP** (Interaction to Next Paint) — good: <200ms, poor: >500ms
- **CLS** (Cumulative Layout Shift) — good: <0.1, poor: >0.25

**Code patterns to look for:**
- Unoptimized hero images (look for `<img>` without `loading="lazy"` for below-fold, no `width`/`height` causing CLS, no responsive `srcset`)
- Bundle bloat (`package.json` dependencies — flag `moment`, `lodash` full import, large chart/icon libraries)
- Render-blocking scripts (`<script>` without `defer`/`async` in `<head>`)
- No image format optimization (no WebP/AVIF; only JPG/PNG)
- Heavy hero animations / video without `preload="none"` or `autoplay`-on-scroll patterns
- No code splitting (single bundle > 500KB)
- Web fonts loaded with `<link>` blocking and no `font-display: swap`

#### B. Above-the-Fold Hero & CTA (web only)

The single highest-impact landing page conversion zone. Above-fold CTA + 10-word value-prop = +96% engagement (Hotjar 2026).

**Code patterns to look for:**
- Hero copy length (count words in `<h1>` — flag if >12)
- CTA button text (search for primary CTA — flag if generic "Submit", "Click Here", "Sign Up"; preferred: first-person "Start my trial" — beats second-person by +90% CTR)
- Multiple competing CTAs above the fold (count `<button>` / `<a>` with primary styling in hero — flag if >1)
- Stock illustration hero (search for `unsplash`, `stock`, `hero-illustration` references)
- Video hero with autoplay (flag — 2026 data shows static heroes outperform video by ~7%)
- Missing social proof above the fold (search for logos/testimonials in hero section; flag if absent — 81% of best-in-class heroes show social proof above fold)

#### C. Signup / Form Conversion

Forms are the single most common conversion killer in B2B SaaS. Each unnecessary field reduces completion by ~10%.

**Code patterns to look for:**
- Form field count (count `<input>` / `<select>` / `<textarea>` in primary signup forms — flag if >3)
- Required fields beyond email (flag every `required` attribute past email)
- SSO providers (search for Google/Apple/Microsoft/GitHub OAuth — flag if absent on primary signup)
- Inline validation (look for `onBlur`/`onChange` handlers tied to error display — flag if missing)
- Error message quality (flag generic "Invalid input" without specifics)
- CAPTCHA on signup (flag — adds ~3% drop-off; reserve for abuse triggers)
- Password requirements visible upfront (flag if password rules only shown on error)
- Multi-step form without progress indicator (flag missing `<progress>` or step counter)
- Mobile keyboard hints (`inputMode="email"` / `autoComplete="email"` — flag if missing on email field)

#### D. Trust Signals & Social Proof

5+ reviews increase purchase likelihood 4x. 91% of millennials trust online reviews as much as personal recommendations.

**Code patterns to look for:**
- Customer logos near hero / CTAs (flag if absent on landing pages)
- Testimonials near pricing tiers / CTAs (flag if pricing page lacks per-tier testimonials)
- Star ratings + review count (flag if hidden in footer; preferred: above primary CTA)
- Security/compliance badges in footer (SOC 2, GDPR, ISO 27001 — flag if missing for B2B)
- Status page link (flag if missing for B2B)
- Privacy / terms / security pages linked from footer
- Customer count / usage stats anywhere on page

#### E. Pricing Page Surface

For ACVs under ~$25K, hidden pricing behind "Contact Us" is a 90%+ conversion loss.

**Code patterns to look for:**
- Pricing page exists and is linked from nav (flag if "Contact Sales" only)
- Three tiers (flag if >3 — decision fatigue)
- One tier highlighted as "Most Popular" (flag if no visual anchor)
- Annual/monthly toggle (flag if missing)
- CTA on each tier matches hero CTA (flag if inconsistent)
- Per-tier FAQ below the table (flag if missing — defuses objections)
- Free tier or free trial offered (flag if missing for self-serve products)

#### F. Mobile Responsiveness & Touch Targets

>50% of web traffic is mobile in most categories. 53% of mobile users abandon if load >3s.

**Code patterns to look for:**
- Viewport meta tag (`<meta name="viewport" content="width=device-width, initial-scale=1">` — flag if missing/malformed)
- Touch target sizes (Tailwind: `h-11`+ for buttons = 44px; flag any primary button `h-8`/`h-9` = 32–36px)
- Mobile-first CSS (flag if base styles use desktop breakpoints)
- Tap-highlight states (flag absence of `:active`/`:focus-visible`)
- Fixed-position modals (flag absence of full-screen mobile modal handling)
- Forms zoom on iOS (flag any `font-size < 16px` on `<input>` — triggers zoom)

#### G. Paywall & Subscription Surfaces (mobile / consumer / subscription)

89.4% of trial starts happen on Day 0. Trial-inclusive paywalls convert at 64.5% vs 44.4% for text-only.

**Code patterns to look for:**
- Hard paywall vs freemium (detect paywall trigger — flag if absent on consumer mobile)
- Free trial toggle on paywall (flag if missing — adding a trial to weekly plan lifts LTV ~636%)
- Annual + trial as default (flag if monthly is pre-selected)
- 5-star review above the pricing on paywall (flag if absent — leads paywall +72% install-to-trial lift)
- Win-back / decline flow (flag if dismissing paywall returns to no offer — should fire alternate offer)
- Usage meter / credit display (flag if usage-based pricing has no visible meter)

#### H. Analytics & Conversion Tracking

Cannot optimize what isn't measured. Top-quartile teams instrument every funnel step.

**Code patterns to look for:**
- Analytics library present (GA4, PostHog, Mixpanel, Amplitude, Plausible, Segment — flag if absent)
- Page view tracking
- CTA click events tracked (search button onClick handlers for tracking calls)
- Form submission events
- Funnel events (signup_started, signup_completed, trial_started, paid_converted, etc.)
- Session recording / heatmap library (Hotjar, FullStory, LogRocket — flag if absent for landing pages)
- Server-side conversion events (for ad attribution post-iOS-14)
- Error / exception tracking (Sentry, Rollbar — flag if absent)

#### I. A/B Testing Infrastructure

Top-quartile teams have ≥1 test running continuously. No infrastructure = no optimization velocity.

**Code patterns to look for:**
- Feature flag / experiment SDK (PostHog, GrowthBook, LaunchDarkly, Statsig, Optimizely, custom — flag if absent)
- Variant rendering pattern (look for `useFeatureFlag` / `useExperiment` hooks)
- Server-side experiments (for high-impact decisions where flicker is unacceptable)

#### J. Onboarding & First-Session Activation

Day 1 retention 26% (industry baseline) vs 40%+ (optimized onboarding). 3-step tours complete at 72%; 7-step at 16%.

**Code patterns to look for:**
- Onboarding flow exists (search for `onboarding`, `welcome`, `getting-started` route/component)
- Magic moment timing (cross-reference against `productos/design/2-Magic-Moment.md` if present — flag if the documented activation event isn't visibly engineered in the flow)
- Empty state handling (search for empty-state components — flag if app opens to blank dashboard)
- Pre-populated workspace (look for seed data, sample content — flag if absent for B2B SaaS)
- Progressive disclosure (flag if all features visible in onboarding rather than just the first action)
- Skip-able / non-blocking (flag if forced 7+ screens with no skip)
- Sticky upgrade nudges during onboarding (flag if paywall fires before first value)

#### K. SEO & Discoverability

The on-ramp to organic conversion. Title, description, OG tags, structured data.

**Code patterns to look for:**
- `<title>` tag present and ≤60 chars
- `<meta name="description">` present and ≤160 chars
- OG image set (`og:image`, `twitter:image`)
- Structured data (JSON-LD for Product / SoftwareApplication / FAQ)
- `robots.txt` and `sitemap.xml` present
- Canonical URLs (`<link rel="canonical">`)
- `llms.txt` for AI-coding-assistant indexing (2026 emerging — 40%+ of doc traffic is now AI agents for dev tools)

### 3. Score and prioritize each finding

For every issue surfaced, capture:

- **Area** (A through K above)
- **Finding** — one-sentence description
- **Location** — file path + line number(s) where applicable
- **Severity** — P0 / P1 / P2 / P3
- **Effort** — S (small, <4 hrs) / M (medium, 1–2 days) / L (large, >2 days)
- **Estimated impact** — % conversion lift if documented; otherwise relative scale
- **Fix** — one-paragraph specific recommendation, with the code-level change

**Severity rubric:**
- **P0** — bleeding conversion daily; fix this week (e.g., LCP >4s, signup form with 8+ fields, no mobile viewport tag)
- **P1** — meaningful conversion loss; fix this month (e.g., missing above-fold social proof, generic CTA copy, no analytics tracking)
- **P2** — moderate optimization opportunity; fix this quarter (e.g., no per-tier testimonials on pricing, missing favicon variants)
- **P3** — minor; fix when convenient (e.g., missing `llms.txt`, missing alt text on decorative images)

### 4. Run the cross-cutting quick wins check

Beyond the eleven audit areas, surface five quick-win categories that almost always have at least one finding:

1. **The one-form-field-too-many.** Most signup forms have at least one field that could be removed or deferred. Name it specifically.
2. **The CTA that doesn't match its destination.** "Get a demo" linking to a 10-field demo form is a click-to-bounce. Audit CTA → landing-page match.
3. **The "modern" sans-serif that nobody can read at 14px.** Inter Display at 13px body is fashionable and illegible. Flag.
4. **The dark mode that wasn't tested.** If a dark mode toggle exists, screenshot both modes — flag any element that becomes invisible in one.
5. **The cookie banner blocking the hero.** If the cookie banner covers >30% of the above-fold area on first load, it's killing conversion before the visitor reads anything.

### 5. Cross-reference against ProductOS docs (if present)

If `docs/PRODUCT.md`, `productos/design/2-Magic-Moment.md`, `productos/design/3-Onboarding-Flow.md`, or `productos/design/4a-Landing-Page.md` exist in the workspace, cross-check the audit findings against them:

- Does the code's actual onboarding match the documented flow in `3-Onboarding-Flow.md`?
- Does the landing page hero copy match the spec in `4a-Landing-Page.md`?
- Does the activation event documented in `2-Magic-Moment.md` actually fire — and is it tracked in analytics?
- Does the tone of voice in product copy match the Identity?

Discrepancies between documented strategy and shipped code are P1 findings — the team has done the strategy work but the code drifted from it.

### 6. Draft the audit report section-by-section

Build the report one section at a time, presenting each section in conversation and confirming before moving on. The whole point of this skill is the conversation about the findings — not the file at the end.

For each section: present the top 3–5 findings, get user confirmation or additional context, refine, move on.

### 7. Write to `docs/CRO-AUDIT.md` (or `CRO-AUDIT.md` at root)

Once approved, write the assembled report. Structure:

```
# Conversion Rate Optimization Audit

*Drafted: [Month Year]. Product type: [type]. Framework: [framework]. Primary conversion event: [event].*

## Summary

[Three sentences: how many total findings, top P0/P1 count, the single highest-impact recommendation.]

## Top 5 fixes ranked by effort × impact

1. **[Finding]** — [location] — Severity P[X], Effort [S/M/L], Est. impact [%]. [One-sentence fix.]
2. ...
3. ...
4. ...
5. ...

---

## A. Performance & Core Web Vitals

**Current state (estimated from code):**
- LCP: [estimate based on hero / images / fonts]
- INP: [estimate based on JS-heavy interactive surfaces]
- CLS: [estimate based on image dimensions, font swap, dynamic content]

**Findings:**

| # | Finding | Location | Sev | Effort | Est. Impact | Fix |
| --- | --- | --- | --- | --- | --- | --- |
| A1 | [finding] | `[file]:[line]` | P0 | S | ~X% | [fix] |
| A2 | ... | ... | ... | ... | ... | ... |

---

## B. Above-the-Fold Hero & CTA
[same structure]

## C. Signup / Form Conversion
[same structure]

## D. Trust Signals & Social Proof
[same structure]

## E. Pricing Page Surface
[same structure]

## F. Mobile Responsiveness & Touch Targets
[same structure]

## G. Paywall & Subscription Surfaces
[same structure, mobile / subscription products only]

## H. Analytics & Conversion Tracking
[same structure]

## I. A/B Testing Infrastructure
[same structure]

## J. Onboarding & First-Session Activation
[same structure]

## K. SEO & Discoverability
[same structure]

---

## Cross-cutting quick wins

[bullet list of 5 quick-win categories with specific findings]

## Strategy-code drift (if ProductOS docs present)

[Findings where documented strategy ≠ shipped code.]

## Verification next steps

- [ ] Re-measure LCP, INP, CLS using PageSpeed Insights and field data (CrUX)
- [ ] Confirm primary conversion event fires correctly in analytics
- [ ] Re-test on actual mobile devices, not just responsive emulator
- [ ] Take screenshots of the fix locations to confirm changes shipped

## Sources & calibration

- Industry benchmarks: B2B SaaS top-decile 8–15% visitor-to-lead (SaaS Hero 2026); Core Web Vitals (Google Web Vitals 2026); paywall conversion data (RevenueCat 2026); form abandonment (Baymard 2026)
- Workspace docs referenced (if present): `docs/PRODUCT.md`, `productos/design/1-Product-Identity.md`, `productos/design/2-Magic-Moment.md`, `productos/design/3-Onboarding-Flow.md`, `productos/design/4a-Landing-Page.md`, `productos/design/BONUS-[X]-Best-Practice.md`
```

Keep prose tight. Tables, not paragraphs. The whole document reads in 5–8 minutes for a developer skimming for fixes.

### 8. Verify before delivering

Re-read the report and check:

- Every finding has a file path + line number(s) where applicable. "The signup form has too many fields" without a file path is a bullet, not a finding.
- Severity P0/P1/P2/P3 makes sense — no missing-alt-tag as P0; no LCP-5s as P3.
- Top 5 fixes are sorted by effort × impact, not by severity alone.
- The audit honors the product type — don't surface a paywall finding for an open-source dev tool; don't surface an SEO finding for a browser extension.
- If ProductOS docs are present, strategy-code drift is surfaced explicitly.
- The verification next-steps are specific, not generic.

Deliver via a `computer://` link and a tight summary — total findings count, P0 count, top 3 fixes by name. Keep it short; the doc is the deliverable.

## Calibration benchmarks (embedded for standalone use)

When the ProductOS BONUS docs are absent, draw on these documented 2026 benchmarks:

### Performance
- LCP <2.5s = good, >4s = poor (Google Core Web Vitals)
- INP <200ms = good, >500ms = poor
- CLS <0.1 = good, >0.25 = poor
- Every 100ms LCP delay = ~1.11% conversion drop (Deloitte/eBay study)
- 53% of mobile users abandon if load >3s
- Sites passing all 3 CWV thresholds = ~24% fewer abandons

### Conversion (B2B SaaS)
- Visitor-to-lead: floor 1.5%, good 4%, best 8–15% (SaaS Hero 2026)
- Free-trial conversion median: 7.2%
- Above-fold CTA + 10-word value-prop = +96% engagement (Hotjar 2026)
- Single-goal pages: 13.5% conversion vs 10.5% multi-CTA
- First-person CTA ("Start my trial") beats second-person by +90% CTR
- Stock-image hero vs no hero: removing the hero entirely beats stock by +4%

### Mobile (subscription apps)
- 89.4% of trial starts on Day 0 (RevenueCat 2026)
- Trial-inclusive paywall: 64.5% vs 44.4% text-only
- Hard paywall median install-to-paid: 12.11% vs freemium 2.18%
- Adding a free trial to a weekly plan: $7.40 → $54.50 LTV (+636%)
- Leading paywall with 5-star review: +72% install-to-trial

### Onboarding
- Day 1 retention baseline: 26%; optimized: 40%+
- 3-step tour completion: 72%; 7-step: 16%
- Users who hit aha within 48 hours: 3.4x more likely to convert to paid

### App Store
- Listing-view-to-install (iOS): floor 15%, good 25%, best 40%+
- Preview video uplift: +20–35% conversion
- 4.6+ rating converts 30–50% better than 3.9 rating

### Form
- Each unnecessary field reduces signup completion by ~10%
- Email-only signup is the floor; >3 fields above the line of concern

## Pacing and approval

- **Scan all eleven areas before drafting findings.** A partial audit produces a misleading priority order.
- **Cite the file + line for every finding.** "The signup form" is a vibe; `src/components/SignupForm.tsx:42–67` is a fix.
- **Severity-honest.** A missing meta description is not a P0. A signup form requiring 8 fields is. Don't conflate.
- **Effort × Impact, not just impact.** A 4-hour fix lifting conversion 6% is a P1 with S effort; a 40-hour fix lifting 8% is a P2 with L effort.
- **Honor the product type.** Don't audit a marketplace's pricing page if it doesn't have one (commission-only). Don't audit a B2B SaaS's app store listing.
- **Reference strategy drift if ProductOS docs are present.** The audit's value compounds when it surfaces where the team's documented strategy didn't make it into shipped code.

## What "done" looks like

A `docs/CRO-AUDIT.md` (or `CRO-AUDIT.md` at root) where:

- All eleven audit areas (A–K) are covered with findings tables.
- Every finding has area, severity, effort, estimated impact, file location (where applicable), and a specific fix.
- The Top 5 fixes are ranked by effort × impact and surfaced at the top of the report.
- Cross-cutting quick wins are listed.
- If ProductOS docs are present, strategy-code drift is surfaced as a dedicated section.
- Verification next steps are specific and actionable.
- The whole doc reads in 5–8 minutes for a developer skimming for fixes.

Recommended next step after a successful session: implement the Top 5 fixes (start with the P0s + S/M effort), instrument any missing analytics events, take a baseline measurement (PageSpeed Insights, GA4 funnel, paywall conversion rate), and re-run this skill in 30 days to measure the lift.
