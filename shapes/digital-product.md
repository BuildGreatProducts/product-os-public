# Shape: Digital product

*Slug: `digital-product` · Family: Other*

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

A file or package the customer buys once and downloads or duplicates: templates (Notion, Figma, spreadsheet, slide), prompt packs, Notion systems, courses, ebooks, presets, code starters. The value is in the asset and what it saves the buyer — hours of setup, a proven structure, expertise packaged. It lives on a storefront (Gumroad, Lemon Squeezy, Payhip, Stan, the member's own site with Stripe) and often in marketplaces (Notion's template marketplace, Etsy, Creative Market, Figma Community, Framer's marketplace; Udemy or Teachable-style platforms for courses). Delivery is automatic after purchase, so the sales page and the first-use experience do the selling and the onboarding.

## Live means

A public sales page with the price is live, and a smoke test passes as a real buyer: pay through live checkout, receive the delivery email or download page automatically, open or duplicate the product, and reach the first win the quickstart promises — with no manual step by the member.

## First sale means

A real customer (warm network counts; the member's own test purchase doesn't) buys through the live checkout — a storefront (Gumroad, Lemon Squeezy, Payhip), a Stripe Payment Link or Checkout, or a marketplace order (Etsy, Notion's marketplace, Creative Market) — and the money lands in the member's balance (for marketplaces, as a pending or released payout).

## Define notes

- **Persona:** someone who wants a head start and will do the work themselves — a solo founder who wants the system, not a service. The persona names the tool they'll use the product in (Notion, Figma, Sheets, Claude) because it decides the format and the marketplace.
- **Pricing models:** one-time price (the default); tiered bundles (basic / pro / with extras); pay-what-you-want with a minimum (for audience building); a free lead-magnet version with a paid full version; a membership for an ongoing library of updates. Courses sometimes add cohorts or support tiers at higher prices.
- **Who pays:** the individual by card. Team or commercial licences are a higher tier for templates and code.
- **Tax:** digital goods sold to consumers abroad carry VAT/GST obligations in many countries. A merchant-of-record storefront handles this; plain Stripe leaves it to the member.

### Fees — last reviewed October 2026 (re-verify before quoting)

- Gumroad charged a flat 10% plus a per-transaction fee on direct sales, and 30% on sales through its Discover marketplace, at the last review — and acts as merchant of record. Lemon Squeezy (owned by Stripe) charged 5% plus a per-transaction fee as a merchant of record. Etsy charges a per-listing fee plus a transaction fee and payment processing. Notion's template marketplace and Creative Market take a share of paid sales. All of these change — check the current figure before setting the price.

## Design route

| Step | Mode | How it adapts |
| --- | --- | --- |
| 1 — Identity | Full | For a creator's product, the brand is often the creator — the worldview and contrarian belief sell the product. The name check covers the storefront and marketplace. |
| 2 — UX Writing | Adapted | `docs/COPY.md` covers the product's own instructions (the quickstart, in-template guidance, prompt-pack usage notes), the delivery and follow-up emails, and the naming of everything inside the product. |
| 3 — Design System | Lite | Brand tokens for the sales page, cover images, and the product's own styling. Full when the product is itself visual (a Figma kit, a Framer or slide template) — then the tokens are the product's styles. |
| 4 — Design Prompts | Optional | Only when the product is a visual template; the prompts generate its key pages. Skip for ebooks, prompt packs, and courses. |
| 5 — Magic Moment | Adapted | The first win after download — the template duplicated and the first entry working, the first prompt producing a great result, lesson one delivering a result. |
| 6 — Onboarding | Adapted | Purchase → delivery email → download or duplicate → a "start here" page → first win → follow-up email on day 3. `docs/ONBOARDING.md` covers that sequence; no wireframe. Use `BONUS-Digital-Product-Onboarding-Best-Practice.md`. |
| 7 — Acquisition surface | Full | `design-landing-page` — the sales page (the storefront page or the member's own). `design-marketplace-listing` for each marketplace used (Notion's template marketplace, Gumroad Discover, Etsy, Creative Market, Figma Community, Framer's marketplace; Udemy for courses). |

## Develop route

| Step | Mode | How it adapts |
| --- | --- | --- |
| 0 — Migrate | Skip | Not applicable. |
| 1 — PRD & Roadmap | Adapted | The PRD is the product spec (below); the roadmap is a production plan — outline, build the asset, test it with buyers, write the quickstart, set up the storefront. |
| 1b — Evals | Optional | Run it for prompt packs and AI-powered templates: each prompt scored on the outputs it produces across the models the buyer may use. Skip for non-AI products. |
| 2 — Verify setup | Full | The repo holds `docs/`, the source files, and the quickstart under version control. |
| 3 — Build | Adapted | Produce the asset against the roadmap: `develop-build` for code starters and scripted pieces; the member and agent together for templates, ebooks, and course material. |
| 4 — Build loop | Optional | For version updates driven by buyer feedback; announce updates to past buyers. |
| 5 — Code review | Optional | Full for code starters and anything with scripts; Skip otherwise. |
| 6 — Design changes | Optional | For the sales page, and for visual templates against the design system. |
| 7 — Conversion review | Adapted | Traffic → sales page → checkout → purchase, and the free-to-paid step if there's a lead magnet. Runs on the sales page and storefront checkout. |
| 8 — Security audit | Full / Skip | Full for code products (starters, boilerplates, scripts the buyer runs) and for a custom-built storefront handling payments or accounts. Skip for templates, ebooks, prompt packs, and courses sold through an established storefront — no code ships. |
| 9 — Go live | Adapted | Storefront and marketplace publishing (below). |

### What the PRD must cover

- **Contents:** exactly what's in the package — every file, page, prompt, lesson, or module — and the format of each.
- **Target tool and versions:** where the buyer uses it (Notion, Figma, Sheets, a model and app for prompts, a framework version for code).
- **The quickstart:** the "start here" steps from download to first win.
- **Delivery:** storefront, file hosting, duplicate links or access grants, and licence terms (personal vs commercial).
- **Updates:** how buyers get new versions and how they're notified.
- **Proof:** the examples, screenshots, or previews the sales page will show — produced from the real product.

### Go live

Final files packaged and tested by someone who didn't make them → storefront set up (🧑 the member: account, payout details, tax settings) → product uploaded with price, description, covers, and the licence → delivery email and "start here" page written → sales page live → marketplace listings submitted → a real test purchase run end to end, then refunded. `develop-golive` writes this as `docs/DEPLOY.md`.

#### Review and policy — last reviewed October 2026 (re-verify before quoting)

- Notion's template marketplace, Figma Community, and Framer's marketplace review submissions against their own guidelines; review times vary — check each one's current process.
- Etsy and other marketplaces have rules on AI-generated and digital items (disclosure, originality) — check before listing.
- Storefronts typically hold early payouts or verify new accounts; set up the account before launch week.

## Distribute notes

**Native channels:** the creator's own audience (X, LinkedIn, YouTube, newsletter), the marketplaces of the tool the product lives in (Notion, Figma, Framer), general marketplaces (Gumroad Discover, Etsy, Creative Market), SEO for "[tool] template for [job]" queries, communities around the tool, and affiliates (other creators selling it for a commission).

**First users:**

1. Give the product free to ten warm-network users in exchange for honest feedback and a testimonial; fix the quickstart from what they get stuck on.
2. Release a free lite version (one template, ten prompts, the first module) as a lead magnet that builds the email list.
3. Post a short video of the first win — the template in use, the prompt's output — on the channel where the persona follows creators.
4. Submit to the tool's own marketplace and two general marketplaces in the same week.
5. Run a launch-week price for the email list, with a clear end date.

**Activation and retention:** *activated* = a buyer opens or duplicates the product and reaches the first win (measured by delivery-page clicks, duplicate counts where the platform shows them, course progress, or a day-3 check-in email reply). *Returned* = the buyer comes back for an update, a second product, or the upgrade within 60 days. Refund rate is the honest retention signal for one-time products.

## Watch-outs

- **Thin product.** A prompt pack the buyer could generate with one prompt doesn't survive reviews. The value has to be curation, testing, structure, or expertise.
- **No audience, no sales.** Marketplaces reward products with early sales and reviews; launching to nobody stays at zero. Build the list while building the product.
- **Tax surprise.** Selling digital goods abroad through plain Stripe creates VAT obligations. Use a merchant of record, or handle registration knowingly.
- **Easy to share.** Files get passed around. Price for the buyer who wants updates, support, and a licence, and don't over-invest in DRM.
- **One-and-done revenue.** A single one-time product caps out. Plan the next product, the bundle, or the upgrade path before launch.
