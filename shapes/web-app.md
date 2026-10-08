# Shape: Web app

*Slug: `web-app` · Family: Apps with a screen*

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

Software the customer signs in to in a browser: a SaaS dashboard, an AI writing or analysis tool, an internal-tool builder. The value arrives on screens the member designs and hosts. It lives on the member's own domain, deployed to a host such as Vercel, Netlify, Render, Railway, or Fly, with its own auth, database, and checkout. This is the shape the ProductOS checklists were written for, so nearly every step runs as the checklist describes. It is also the usual landing point of a sequenced product (`productized-service` first, then `web-app` once the process is proven).

## Live means

The app is deployed on the member's own domain over HTTPS, and a smoke test passes on production as a real customer: a fresh account signs up, does the core thing, and reaches the magic moment, with no local services, test keys, or seeded data behind it.

## First sale means

A real customer (warm network counts; the member's own test purchase doesn't) pays through the app's live checkout — Stripe Checkout or a Stripe Payment Link, or a merchant of record such as Paddle or Lemon Squeezy, in live mode — the money lands in the member's account, and the paid plan unlocks in the app. A B2B annual deal paid by invoice also counts once the invoice is paid.

## Define notes

- **Persona:** separate the **user** (who signs up and does the work) from the **buyer** (who owns the budget) for anything sold to teams. Prosumer tools usually have one person in both roles; B2B tools rarely do, and the persona must say whose pain the first screen answers.
- **Pricing models:** monthly/annual subscription tiers are the default; seats for team tools; usage or credits when each AI action has a real cost; free trial or reverse trial over a permanent free plan unless the product spreads by sharing. `define-pricing` should price against the cost per active user of the AI calls, not just the hosting bill.
- **Who pays:** an individual on a card (self-serve checkout) or a company (card for small teams, invoice for larger ones). Decide which before the PRD — it decides whether checkout or a sales call is the first-sale path.

### Fees — last reviewed October 2026 (re-verify before quoting)

- Card processing (Stripe and similar) is a percentage plus a fixed fee per charge, varying by country and card type — check the provider's current pricing page.
- A merchant of record (Paddle, Lemon Squeezy, Polar) charges a higher percentage but collects and remits sales tax and VAT for the member. With Stripe alone, tax registration and remittance stay the member's job (Stripe Tax calculates it; it doesn't make the member the non-seller).

## Design route

| Step | Mode | How it adapts |
| --- | --- | --- |
| 1 — Identity | Full | As the checklist runs it. The name check includes the `.com` or category domain the app will live on. |
| 2 — UX Writing | Full | Buttons, errors, empty states, toasts, emails: the whole in-app copy system. |
| 3 — Design System | Full | From an image reference, or `design-design-system-from-code` for an existing codebase. Required before any UI build. |
| 4 — Design Prompts | Full | Component set plus the two priority screens: usually the core-loop screen and the first-run (empty) state. |
| 5 — Magic Moment | Full | One in-app event that can be logged as an analytics event. |
| 6 — Onboarding | Full | Signup → first screen → magic moment, with the clickable wireframe. Pick the B2B AI SaaS or Vertical SaaS onboarding reference. |
| 7 — Acquisition surface | Full | `design-landing-page` — the marketing site that carries the price and the signup CTA. Add `design-marketplace-listing` only if the app also lists inside a host marketplace (Shopify App Store, Slack Marketplace, Notion integrations) or ships a secondary shape. |

## Develop route

| Step | Mode | How it adapts |
| --- | --- | --- |
| 0 — Migrate | Full / Skip | Full when the app lives on a prompt-to-app platform (Lovable, Bolt, v0, Base44, Replit); Skip otherwise. |
| 1 — PRD & Roadmap | Full | New build, or existing-codebase mode for a gap roadmap. |
| 1b — Evals | Optional | Run it when the magic moment is an AI output (a generated draft, an analysis, a classification); skip for a CRUD tool with incidental AI. |
| 2 — Verify setup | Full | Normally already done by `setup`. |
| 3 — Build | Full | `develop-build` through the roadmap until the magic moment works end to end. |
| 4 — Build loop | Full | `build-loop` for every post-MVP feature; `develop-feature-finder` when unsure what's next. |
| 5 — Code review | Full | For changes made outside the build skills. |
| 6 — Design changes | Full | `develop-design-better` while building UI, `develop-design-review` before committing it. |
| 7 — Conversion review | Full | Landing page → signup → activation → pricing page → checkout, once usable end to end. |
| 8 — Security audit | Full | Before go-live; re-run after auth, payments, or data-access work. Access control on every table and route is the top risk. |
| 9 — Go live | Full | `develop-golive` writes `docs/DEPLOY.md`; live when the production smoke test passes. |

### What the PRD must cover

- **Accounts and access:** auth method, roles (if teams), and the ownership rule for every table — who can read and write each row.
- **The core loop screens** from `docs/ONBOARDING.md`, in build order, ending at the magic moment.
- **Payments:** plans and prices from `docs/DEFINE.md`, checkout, webhooks, how entitlements are stored and checked, what happens on failed payment or cancellation.
- **AI calls (if any):** provider and model, cost per core action, per-plan quotas or credits, timeouts and the fallback when the call fails.
- **Email:** transactional email provider, sending domain, the emails the MVP sends (verify, reset, receipt, the activation nudge).
- **Analytics:** the magic-moment event and the funnel events before it, named exactly.

### Go live

Hosting deploy, custom domain and DNS, HTTPS, production environment variables, a production database with access rules on, Stripe (or the merchant of record) switched to live mode with its webhook pointed at production, the sending domain verified for email, error tracking, privacy policy and terms pages, then the smoke test as a real customer. No platform review stands between the member and launch — the gate is the security audit.

#### Review and policy — last reviewed October 2026 (re-verify before quoting)

- "Sign in with Google" with basic profile and email scopes needs only a configured OAuth consent screen. Requesting sensitive or restricted scopes (Gmail, Drive contents) triggers Google's app verification, which can take weeks — scope the MVP to avoid it unless the product depends on it.
- Payment providers can hold or review new accounts on their first live charges; activate live mode before launch day, not on it.

## Distribute notes

**Native channels:** search (SEO and GEO — the product's job as a query), communities where the persona asks the problem question (subreddits, Slack and Discord groups, niche forums), launch platforms (Product Hunt, Hacker News "Show HN"), AI tool directories (There's An AI For That, Futurepedia), software review and alternatives sites (G2, Capterra, AlternativeTo, SaaSHub), and the integration marketplaces of the tools the persona already uses.

**First users:**

1. Personally invite 20 people from the warm network who match the persona, and set up the first five accounts with them on a call — watch where they stall.
2. Answer five live threads where the persona describes the problem, with a short demo clip of the magic moment, not a pitch.
3. Ship one free single-purpose page (a calculator, a generator, a checker) that delivers a slice of the magic moment without signup, and link it to the app.
4. Submit to the AI directories and alternatives sites in the same week, using the landing page's one-line promise.
5. Launch on Product Hunt only once ten real users can vouch for it.

**Activation and retention:** *activated* = a new account fires the magic-moment event from `docs/MAGIC-MOMENT.md`, ideally in the first session. *Returned* = the account repeats the core action in its second week (for a daily tool, on a later day in week one). Instrument both events in product analytics before launch; `distribute-activation-retention-audit` reads them.

## Watch-outs

- **Settings before the core loop.** Account pages, team invites, and billing portals built before the magic moment works end to end. The roadmap's first phases end at the magic moment.
- **Unbounded AI cost on a free plan.** One heavy free user can cost more than ten paying ones. Quotas per plan go in the PRD, not after the first bill.
- **Verification emails in spam.** An unverified sending domain silently kills signups. Verify SPF/DKIM before the smoke test.
- **"It's just a ChatGPT wrapper."** If the mechanism is a prompt the persona could type themselves, the landing page can't defend the price. The offer's mechanism must name what the app does that a chat window doesn't.
- **Launching blind.** No magic-moment event in analytics means no activation number, and the Distribute loop has nothing to read.
- **Test keys in production.** Stripe test mode on the live site passes the smoke test and takes no money. Check the mode on the first real purchase.
