# Shape: Website

*Slug: `website` · Family: Other*

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

A site whose content, directory, or community is the product: a niche directory (AI tools for lawyers, remote jobs for designers), a newsletter with a site, a resource library, a paid community. Visitors get value by browsing, reading, searching, or belonging — not by operating software. AI often powers the content pipeline (curating, summarising, enriching listings). It lives on the member's domain, built in code or on a site builder (Framer, Webflow, WordPress, Ghost) or a newsletter/community platform (beehiiv, Substack, Ghost, Circle, Skool). Revenue comes from members, sponsors, featured listings, or affiliates — so traffic and trust are the core assets.

## Live means

The site is public on the member's domain over HTTPS with its core content in place (enough listings, issues, or resources to deliver the promise on day one), and a smoke test passes as a real visitor: arrive on the homepage, find the thing they came for, and complete the main action — subscribe, join, submit a listing, or reach the paid offer.

## First sale means

A real customer (warm network counts; the member's own test purchase doesn't) pays — a paid membership or subscription (Stripe, or the platform's billing on Ghost, beehiiv, Substack, Circle, Skool), a featured or sponsored listing bought through a Stripe Payment Link, a newsletter sponsorship invoice that's paid, or the first affiliate commission actually paid out.

## Define notes

- **Persona:** the visitor (who gets the value) and, for sponsor- or listing-funded sites, the payer (vendors, employers, advertisers who want that audience). Define both — a directory's first sale usually comes from the listed side, not the readers.
- **Pricing models:** paid membership or subscription (communities, premium newsletters, resource libraries); featured, sponsored, or paid-submission listings (directories); sponsorships and ads (newsletters, once there's an audience); affiliate commissions; a one-time lifetime access fee. Many sites combine a free audience with one paid layer.
- **Who pays:** readers by card for memberships; businesses by card or invoice for listings and sponsorships.
- **The audience is the asset:** sponsorship pricing is set per send or per thousand readers, so the pricing section should name the audience size at which sponsorship turns on.

### Fees — last reviewed October 2026 (re-verify before quoting)

- Substack takes 10% of paid subscription revenue (plus card processing). Ghost(Pro) and beehiiv charge platform plans rather than a revenue share on paid subscriptions, at the last review. Community platforms (Circle, Skool) combine monthly plans with transaction fees that vary by tier — check the current figures before choosing.

## Design route

| Step | Mode | How it adapts |
| --- | --- | --- |
| 1 — Identity | Full | For content and community the brand *is* the product — worldview and contrarian belief set the editorial line. |
| 2 — UX Writing | Adapted | `docs/COPY.md` covers navigation, search and filter labels, listing and submission forms, subscribe and join prompts, welcome emails, and an editorial style guide for the content itself. |
| 3 — Design System | Full | The site is the product surface; the system covers content templates (article, listing card, directory filters). Skip only the parts a site builder's theme already fixes. |
| 4 — Design Prompts | Full | The homepage and the core template (a listing page, an issue, a resource page). |
| 5 — Magic Moment | Adapted | The first time a visitor finds exactly what they came for (the right tool, the right job, the answer) — or, for a newsletter or community, the first issue or thread that delivers. |
| 6 — Onboarding | Adapted | Visitor → find value → subscribe or join → welcome email or welcome post → first return visit. `docs/ONBOARDING.md` covers the welcome sequence; the wireframe covers the subscribe/join path. |
| 7 — Acquisition surface | Adapted | `design-landing-page`, applied to the homepage and the subscribe, join, or "list your product" page (the site is its own landing page). `design-marketplace-listing` is Optional, for platform discovery (Substack's network, beehiiv's recommendations, Skool's discovery). |

## Develop route

| Step | Mode | How it adapts |
| --- | --- | --- |
| 0 — Migrate | Full / Skip | Full when the site was generated on a prompt-to-app platform and needs to move; Skip when it's on a site builder or publishing platform the member intends to keep — those are legitimate homes. |
| 1 — PRD & Roadmap | Adapted | The PRD centres on the content model and pipeline (below); on a site builder, the roadmap is mostly configuration and content tasks. |
| 1b — Evals | Optional | Run it when AI generates or enriches content (listing summaries, auto-categorisation, AI search) — the evals check accuracy before it publishes. |
| 2 — Verify setup | Full | The repo holds `docs/`, content scripts, and the site code if custom. |
| 3 — Build | Full | Code-built sites: `develop-build`. Site-builder sites: configured against the same roadmap; the content seed is a roadmap phase of its own. |
| 4 — Build loop | Full | New templates, filters, and member features; on a builder, it's mostly content and integrations. |
| 5 — Code review | Optional | Full for a code-built site; Skip for a builder with no custom code. |
| 6 — Design changes | Full | Every new template and page type stays on the design system. |
| 7 — Conversion review | Full | Visitor → subscribe/join → paid member, and for listing-funded sites, vendor → submission → paid listing. |
| 8 — Security audit | Full / Skip | Full when the site has custom code with accounts, payments, user submissions, or member data. Skip when it runs entirely on a hosted platform (Ghost(Pro), beehiiv, Substack, Circle, Skool, Framer) with no custom backend — the platform carries that risk. |
| 9 — Go live | Adapted | Domain, platform or host, payments, and the content seed (below). |

### What the PRD must cover

- **Content model:** the content types (listing, article, issue, resource, thread), their fields, categories, and tags.
- **Content pipeline:** where content comes from (the member, submissions, scraping, AI enrichment), the editorial check before publish, and the update cadence.
- **The seed:** how much content must exist on launch day to deliver the promise.
- **Search and SEO:** URL structure, page titles and descriptions, structured data, sitemap, internal linking — for directories, one indexable page per listing and category.
- **Members and payments:** which platform or code handles subscribe, join, paid tiers, and gated content.
- **Monetisation surfaces:** sponsor slots, featured listings, affiliate links — where they appear and how they're bought.
- **Analytics:** traffic sources, subscribe/join conversion, and the return-visit metric.

### Go live

Domain connected over HTTPS → platform or host configured → content seed published → subscribe, join, or listing purchase working in live mode → welcome email set up and the sending domain verified → analytics and Google Search Console connected, sitemap submitted → privacy policy and terms → smoke test as a real visitor. `develop-golive` writes this as `docs/DEPLOY.md`.

#### Review and policy — last reviewed October 2026 (re-verify before quoting)

- Search engines index new sites over days to weeks; Search Console speeds discovery but doesn't guarantee ranking. Thin, auto-generated pages at scale risk search penalties — AI-enriched listings need real, unique value per page.
- Affiliate programmes have their own approval and disclosure rules; disclose affiliate links on the page.

## Distribute notes

**Native channels:** search (SEO for directories and resources; GEO so AI answers cite the site), the communities where the persona already asks the questions the site answers, newsletter cross-recommendations (beehiiv and Substack recommendation networks, swaps with similar newsletters), social posts repurposing the content, and the listed vendors themselves (they share their listing).

**First users:**

1. Send the launch to the warm network with one specific reason the persona will care, and ask each person to forward it to one peer.
2. Email every vendor listed in the directory that they're featured — many will share it; offer an upgraded listing.
3. Post one useful piece of the content (a ranked list, a finding) natively in three communities, linking to the site for the rest.
4. Swap recommendations with three newsletters that serve the same persona at a similar size.
5. Build one category or topic page per high-intent search query the persona types.

**Activation and retention:** *activated* = a visitor subscribes or joins after finding value (or, for directories, clicks through to a listing from search or filters). *Returned* = they come back in week 2 — opening an issue, visiting the site again, or posting in the community. For paid members, track month-2 renewal.

## Watch-outs

- **The empty room.** A directory with 30 listings or a community with no posts fails the first visit. The content seed is part of the build, not an afterthought.
- **Rented audience.** A platform's discovery feed can change. Own the email list from day one.
- **AI content at scale.** Thousands of auto-generated pages without unique value attract search penalties and lose trust. Enrich, don't fabricate.
- **Monetising too early.** Sponsors and ads on a tiny audience earn little and cost credibility; a small paid layer for the most engaged readers usually comes first.
- **No maintenance plan.** Stale listings and dead links erode a directory's value. The pipeline needs an update cadence the member can sustain.
