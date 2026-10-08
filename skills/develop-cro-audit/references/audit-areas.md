# CRO audit areas (A–K)

The eleven areas the audit walks, in order. For each: what the area covers and the code patterns to scan for. The numbers each flag rests on (thresholds, lift figures, sources) live in [benchmarks.md](benchmarks.md) — cite from there in findings. Mark an area N/A with a one-line reason when it doesn't apply to the product type (no paywall for an open-source dev tool, no SEO for a browser extension, no pricing page for a commission-only marketplace).

## Contents

- [A. Performance & Core Web Vitals](#a-performance--core-web-vitals)
- [B. Above-the-Fold Hero & CTA (web only)](#b-above-the-fold-hero--cta-web-only)
- [C. Signup / Form Conversion](#c-signup--form-conversion)
- [D. Trust Signals & Social Proof](#d-trust-signals--social-proof)
- [E. Pricing Page Surface](#e-pricing-page-surface)
- [F. Mobile Responsiveness & Touch Targets](#f-mobile-responsiveness--touch-targets)
- [G. Paywall & Subscription Surfaces](#g-paywall--subscription-surfaces-mobile--consumer--subscription)
- [H. Analytics & Conversion Tracking](#h-analytics--conversion-tracking)
- [I. A/B Testing Infrastructure](#i-ab-testing-infrastructure)
- [J. Onboarding & First-Session Activation](#j-onboarding--first-session-activation)
- [K. SEO & Discoverability](#k-seo--discoverability)

## A. Performance & Core Web Vitals

The highest-leverage conversion lever. Estimate LCP, INP, and CLS against the Core Web Vitals thresholds in benchmarks.md.

**Code patterns to look for:**
- Unoptimized hero images (`<img>` without `loading="lazy"` for below-fold, no `width`/`height` causing CLS, no responsive `srcset`)
- Bundle bloat (`package.json` dependencies — flag `moment`, `lodash` full import, large chart/icon libraries)
- Render-blocking scripts (`<script>` without `defer`/`async` in `<head>`)
- No image format optimization (no WebP/AVIF; only JPG/PNG)
- Heavy hero animations / video without `preload="none"` or `autoplay`-on-scroll patterns
- No code splitting (single bundle > 500KB)
- Web fonts loaded with `<link>` blocking and no `font-display: swap`

## B. Above-the-Fold Hero & CTA (web only)

The highest-impact landing page conversion zone.

**Code patterns to look for:**
- Hero copy length (count words in `<h1>` — flag if >12)
- CTA button text (find the primary CTA — flag generic "Submit", "Click Here", "Sign Up"; prefer first-person, e.g. "Start my trial")
- Multiple competing CTAs above the fold (count `<button>` / `<a>` with primary styling in the hero — flag if >1)
- Stock illustration hero (search for `unsplash`, `stock`, `hero-illustration` references)
- Video hero with autoplay (flag — static heroes tend to outperform)
- Missing social proof above the fold (logos/testimonials in the hero section — flag if absent)

## C. Signup / Form Conversion

Forms are the most common conversion killer in B2B SaaS; every unnecessary field costs completions.

**Code patterns to look for:**
- Form field count (count `<input>` / `<select>` / `<textarea>` in primary signup forms — flag if >3)
- Required fields beyond email (flag every `required` attribute past email)
- SSO providers (Google/Apple/Microsoft/GitHub OAuth — flag if absent on primary signup)
- Inline validation (`onBlur`/`onChange` handlers tied to error display — flag if missing)
- Error message quality (flag generic "Invalid input" without specifics)
- CAPTCHA on signup (flag — reserve for abuse triggers)
- Password requirements visible upfront (flag if rules only show on error)
- Multi-step form without progress indicator (flag missing `<progress>` or step counter)
- Mobile keyboard hints (`inputMode="email"` / `autoComplete="email"` — flag if missing on the email field)

## D. Trust Signals & Social Proof

**Code patterns to look for:**
- Customer logos near hero / CTAs (flag if absent on landing pages)
- Testimonials near pricing tiers / CTAs (flag if the pricing page lacks per-tier testimonials)
- Star ratings + review count (flag if hidden in the footer; prefer above the primary CTA)
- Security/compliance badges in the footer (SOC 2, GDPR, ISO 27001 — flag if missing for B2B)
- Status page link (flag if missing for B2B)
- Privacy / terms / security pages linked from the footer
- Customer count / usage stats anywhere on the page

## E. Pricing Page Surface

For self-serve and low-ACV products, pricing hidden behind "Contact Us" loses most would-be buyers.

**Code patterns to look for:**
- Pricing page exists and is linked from nav (flag if "Contact Sales" only)
- Three tiers (flag if >3 — decision fatigue)
- One tier highlighted as "Most Popular" (flag if no visual anchor)
- Annual/monthly toggle (flag if missing)
- CTA on each tier matches the hero CTA (flag if inconsistent)
- Per-tier FAQ below the table (flag if missing — defuses objections)
- Free tier or free trial offered (flag if missing for self-serve products)

## F. Mobile Responsiveness & Touch Targets

**Code patterns to look for:**
- Viewport meta tag (`<meta name="viewport" content="width=device-width, initial-scale=1">` — flag if missing/malformed)
- Touch target sizes (Tailwind: `h-11`+ for buttons = 44px; flag any primary button at `h-8`/`h-9` = 32–36px)
- Mobile-first CSS (flag if base styles use desktop breakpoints)
- Tap-highlight states (flag absence of `:active`/`:focus-visible`)
- Fixed-position modals (flag absence of full-screen mobile modal handling)
- Forms zoom on iOS (flag any `font-size < 16px` on `<input>` — triggers zoom)

## G. Paywall & Subscription Surfaces (mobile / consumer / subscription)

**Code patterns to look for:**
- Hard paywall vs freemium (detect the paywall trigger — flag if absent on consumer mobile)
- Free trial toggle on the paywall (flag if missing)
- Annual + trial as default (flag if monthly is pre-selected)
- A 5-star review above the pricing on the paywall (flag if absent)
- Win-back / decline flow (flag if dismissing the paywall returns to no offer — it should fire an alternate offer)
- Usage meter / credit display (flag if usage-based pricing has no visible meter)

## H. Analytics & Conversion Tracking

Can't optimize what isn't measured — instrument every funnel step.

**Code patterns to look for:**
- Analytics library present (GA4, PostHog, Mixpanel, Amplitude, Plausible, Segment — flag if absent)
- Page view tracking
- CTA click events tracked (button onClick handlers with tracking calls)
- Form submission events
- Funnel events (signup_started, signup_completed, trial_started, paid_converted, etc.)
- Session recording / heatmap library (Hotjar, FullStory, LogRocket — flag if absent for landing pages)
- Server-side conversion events (for ad attribution where client-side tracking is blocked)
- Error / exception tracking (Sentry, Rollbar — flag if absent)

## I. A/B Testing Infrastructure

No infrastructure = no optimization velocity; strong teams keep at least one test running.

**Code patterns to look for:**
- Feature flag / experiment SDK (PostHog, GrowthBook, LaunchDarkly, Statsig, Optimizely, custom — flag if absent)
- Variant rendering pattern (`useFeatureFlag` / `useExperiment` hooks)
- Server-side experiments (for high-impact decisions where flicker is unacceptable)

## J. Onboarding & First-Session Activation

**Code patterns to look for:**
- Onboarding flow exists (`onboarding`, `welcome`, `getting-started` route/component)
- Magic moment timing (cross-reference `docs/MAGIC-MOMENT.md` if present — flag if the documented activation event isn't visibly engineered in the flow)
- Empty state handling (empty-state components — flag if the app opens to a blank dashboard)
- Pre-populated workspace (seed data, sample content — flag if absent for B2B SaaS)
- Progressive disclosure (flag if every feature shows in onboarding rather than just the first action)
- Skippable / non-blocking (flag forced 7+ screens with no skip)
- Upgrade nudges during onboarding (flag if the paywall fires before first value)

## K. SEO & Discoverability

The on-ramp to organic conversion.

**Code patterns to look for:**
- `<title>` tag present and ≤60 chars
- `<meta name="description">` present and ≤160 chars
- OG image set (`og:image`, `twitter:image`)
- Structured data (JSON-LD for Product / SoftwareApplication / FAQ)
- `robots.txt` and `sitemap.xml` present
- Canonical URLs (`<link rel="canonical">`)
- `llms.txt` for AI-assistant indexing (most relevant for developer tools and docs sites)
