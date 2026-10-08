# Shape: Mobile app

*Slug: `mobile-app` · Family: Apps with a screen*

## Contents

- [What it is](#what-it-is)
- [Live means](#live-means)
- [First sale means](#first-sale-means)
- [Define notes](#define-notes)
- [Design route](#design-route)
- [Develop route](#develop-route)
  - [What the PRD must cover](#what-the-prd-must-cover)
  - [Go live](#go-live)
- [Distribute notes](#distribute-notes)
- [Watch-outs](#watch-outs)

## What it is

An app the customer installs from the Apple App Store or Google Play and uses on their phone: AI photo and video apps, habit and health trackers, companion and coaching apps. The value arrives on a small screen, often in short sessions, and the store sits between the member and every customer — it hosts the listing, reviews each release, and (for digital goods) takes the payment. Typically built with React Native/Expo, Flutter, or native Swift/Kotlin, with a hosted backend for accounts and AI calls.

## Live means

The app is approved and publicly downloadable from the App Store and/or Google Play (on at least one store; a TestFlight build or a closed test doesn't count), and a smoke test passes on a real phone as a real customer: install from the store listing, sign up, reach the magic moment, against the production backend.

## First sale means

A real customer (warm network counts; the member's sandbox purchase doesn't) completes an in-app purchase or subscription through Apple's or Google's billing — usually via StoreKit / Play Billing, often wrapped by RevenueCat — and it shows in App Store Connect or the Play Console as a real transaction. Where store rules allow a web checkout instead (see the dated note), a Stripe payment from a customer who then unlocks the app also counts.

## Define notes

- **Persona:** mobile personas are defined by *moment of use* as much as job: where they are, how long they have, one-handed or not. The persona must name the trigger that makes them open the app.
- **Pricing models:** subscription with a free trial behind a paywall shown during onboarding is the dominant model for AI mobile apps; weekly plans are common in consumer AI; lifetime unlocks and consumable credits (for generation-heavy apps) are alternatives. Freemium with ads rarely funds AI costs.
- **Who pays:** the individual, through their store account. The store is the seller of record — it handles tax and refunds, and the member never sees the card.
- **Price points** are chosen from each store's price tiers, set per country.

### Fees — last reviewed October 2026 (re-verify before quoting)

- Apple Developer Program: $99/year. Google Play developer registration: $25 one-time.
- Apple's standard commission is 30% on digital goods, 15% for members of the Small Business Program (under $1M in proceeds the prior year) and for subscriptions after the subscriber's first year. Google Play charges 15% on the first $1M of annual revenue and 15% on subscriptions. Both have regional variations — check the current figure.
- Rules on linking out to a web checkout have changed by region (the EU under the Digital Markets Act; the US after 2025 court rulings against Apple). Whether a web checkout is allowed, and on what terms, differs per storefront — check the current guidelines before designing around it.

## Design route

| Step | Mode | How it adapts |
| --- | --- | --- |
| 1 — Identity | Full | The name check includes store search (no near-duplicate app names) and the 30-character store title. The icon direction comes from Visual Style. |
| 2 — UX Writing | Full | Short-form copy: tab labels, permission-prompt pre-screens, push notifications, paywall copy. |
| 3 — Design System | Full | Tokens for iOS and Android: touch targets, safe areas, dynamic type, dark mode. |
| 4 — Design Prompts | Full | Component set plus the two priority screens: the core-loop screen and the paywall. |
| 5 — Magic Moment | Full | Must land inside the first session — mobile users rarely come back to finish setup. |
| 6 — Onboarding | Full | Uses `BONUS-Mobile-Onboarding-Best-Practice.md`: value screens, personalisation questions, permission pre-prompts, the paywall placement, then the magic moment. |
| 7 — Acquisition surface | Full | `design-app-listing` (App Store and Google Play) is the primary surface. Add `design-landing-page` as a Lite one-pager: store badges, the promise, and the privacy-policy and support URLs both stores require. |

## Develop route

| Step | Mode | How it adapts |
| --- | --- | --- |
| 0 — Migrate | Full / Skip | Full when the app was generated on a prompt-to-app platform the member doesn't control the code of; Skip otherwise. |
| 1 — PRD & Roadmap | Full | Stack choice (Expo / Flutter / native) and the store-billing approach are decided here. |
| 1b — Evals | Optional | Run it when the magic moment is an AI output (a generated image, a plan, a transcript summary). |
| 2 — Verify setup | Full | Normally already done by `setup`. |
| 3 — Build | Full | The roadmap must include store accounts, bundle IDs, signing, and a TestFlight / internal-testing build before the final phase. |
| 4 — Build loop | Full | Every release after launch goes through store review — batch changes into releases. |
| 5 — Code review | Full | For changes made outside the build skills. |
| 6 — Design changes | Full | Review on device sizes (smallest supported phone and a large one), not just a simulator default. |
| 7 — Conversion review | Adapted | Store listing → install → onboarding → paywall → trial start → paid conversion. The paywall is the main surface. |
| 8 — Security audit | Full | Plus mobile specifics: no secret API keys in the app bundle (they're extractable), backend access rules, receipt validation server-side. |
| 9 — Go live | Adapted | Store submission rather than a deploy (below). |

### What the PRD must cover

- **Platforms and stack:** iOS, Android, or both at launch; framework; minimum OS versions.
- **Backend:** auth, database access rules, and an API proxy for every AI call so no provider key ships in the app.
- **Monetisation:** products and subscription groups as configured in each store, trial length, paywall placement, entitlement checks, restore purchases, server-side receipt validation (or RevenueCat).
- **Permissions:** each OS permission (camera, photos, notifications, health, location), when it's asked, and the pre-prompt copy explaining why.
- **Store compliance:** in-app account deletion if accounts exist, privacy-policy URL, the data the app collects (for Apple's privacy labels and Google's Data safety form), content moderation for user-generated or AI-generated content.
- **Analytics:** the magic-moment event, paywall view, trial start, and conversion — with attribution set up so installs can be traced to campaigns.

### Go live

Production backend deployed → store developer accounts created (🧑 the member, with identity verification) → app records, bundle IDs, and in-app products configured → privacy labels / Data safety form completed → screenshots and listing copy from `docs/APP-LISTING.md` uploaded → build submitted for review → on approval, release (manual release lets the member time the launch). `develop-golive` writes this as `docs/DEPLOY.md`; live when the store-installed build passes the smoke test.

#### Review and policy — last reviewed October 2026 (re-verify before quoting)

- Apple App Review typically completes within a day or two; rejections add a round trip each. Common rejection causes: crashes on review, broken login (supply a demo account), missing account deletion, paywall terms unclear, minimal functionality ("a website in a wrapper").
- If the app offers third-party social login, Apple's guidelines require an equivalent privacy-focused login option (Sign in with Apple satisfies it) — check the current guideline 4.8 wording.
- New personal Google Play developer accounts must run a closed test with a minimum number of testers for a minimum number of days before production access (12 testers for 14 days at the last review — check the current figure). Plan for it: it can add two weeks to the first launch.
- Each update goes through review again on both stores.

## Distribute notes

**Native channels:** App Store and Google Play search (ASO — keywords, screenshots, ratings), store featuring (Apple's editorial "Today" and nomination form), short-form video (TikTok, Reels, Shorts — the dominant channel for consumer AI apps), creators and UGC, Apple Search Ads and other paid install channels once unit economics are known.

**First users:**

1. Put the build in 20 warm-network hands through TestFlight / a closed test before launch, and ask each for a store rating on release day.
2. Post three short videos a week showing the magic moment on a real phone screen — the before/after or the reveal, not the feature list.
3. Seed the first ratings with a review prompt (`SKStoreReviewController` / In-App Review API) fired right after the magic moment, never on first open.
4. Submit the app to Apple's featuring nomination form ahead of launch.
5. Run a custom product page (or store listing experiment) per traffic source once installs arrive.

**Activation and retention:** *activated* = an install reaches the magic-moment event in the first session. *Returned* = the user opens the app and repeats the core action on day 7 (D7 retention); for subscription apps, also track trial → paid conversion and month-2 renewal.

## Watch-outs

- **Review as a launch-day surprise.** A first submission can be rejected for reasons unrelated to code (metadata, demo access, missing deletion). Submit two or three days before the planned launch, with manual release.
- **API keys in the bundle.** Anything in the app can be extracted. Every AI and paid-API call goes through the member's backend.
- **The Google closed-test wait.** A new personal Play account can't go straight to production. Start the closed test early or launch iOS first.
- **The paywall that comes before the value.** A hard paywall on screen one converts the curious and refunds the rest; place it after a taste of the magic moment unless the listing already sold it.
- **Store fees missing from the pricing math.** Price minus the store's cut minus AI cost per user is the real margin.
- **"Web view in a wrapper."** An app that's just the website loses on review and on ratings — the app must use the phone (camera, notifications, offline, widgets).
