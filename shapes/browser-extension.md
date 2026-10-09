# Shape: Browser extension

*Slug: `browser-extension` · Family: Apps with a screen*

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

An add-on the customer installs from a browser's extension store that works on top of the websites they already use: AI reply helpers inside Gmail or LinkedIn, page summarisers, tab managers, research clippers. The value arrives in someone else's interface — a popup, a side panel, a button injected into a page — so the extension borrows the host site's context and must stay out of its way. It lives in the Chrome Web Store (which also serves most Chromium browsers), Microsoft Edge Add-ons, Firefox Add-ons (AMO), and Safari (packaged as an app through the App Store). Paid extensions usually pair with a small web backend for accounts and billing.

## Live means

The extension is approved and publicly installable from the Chrome Web Store (or the persona's main browser's store), and a smoke test passes as a real customer on a clean browser profile: install from the listing, pin it, grant permissions, reach the magic moment on a real target site, against the production backend.

## First sale means

A real customer (warm network counts; the member's own test purchase doesn't) pays for the paid tier through a checkout the member runs — a Stripe Checkout or Payment Link, a merchant of record, or an extension-payments service such as ExtensionPay — and the extension unlocks the paid features for that account. The Chrome Web Store does not process payments, so the checkout is always the member's own.

## Define notes

- **Persona:** defined by the site they live in (Gmail, LinkedIn, Salesforce, YouTube, Google Docs) and the repeated action on it. The persona names the host site; it decides the permissions, the listing keywords, and the communities.
- **Pricing models:** freemium with a monthly cap on the AI action is the norm; paid plans unlock volume or advanced actions. Usage credits suit generation-heavy extensions. One-time lifetime deals work for utilities without running costs.
- **Who pays:** usually the individual by card; team plans when the host site is a work tool. Upgrades happen on a web page the extension opens — design that hand-off.

### Fees — last reviewed October 2026 (re-verify before quoting)

- Chrome Web Store: one-time $5 developer registration fee; no revenue share, because the store no longer offers payments.
- Firefox Add-ons and Microsoft Edge Add-ons: no registration fee.
- Safari: the extension ships inside a Mac/iOS app through the App Store, which needs the $99/year Apple Developer Program; App Store commission applies if paid through Apple.

## Design route

| Step | Mode | How it adapts |
| --- | --- | --- |
| 1 — Identity | Full | The icon must read at 16px in the toolbar; the name must not imply endorsement by the host site (store policy). |
| 2 — UX Writing | Full | Popup and side-panel copy, injected-button labels, permission rationales, the upgrade prompt when the free cap is hit. |
| 3 — Design System | Adapted | Tokens scoped to the extension's own surfaces (popup, side panel, options page) and to injected UI, which must sit visibly but politely on top of host pages it doesn't control. |
| 4 — Design Prompts | Adapted | The popup or side panel and one injected-UI state on the main host site, instead of full app screens. |
| 5 — Magic Moment | Full | Happens on the host site — the first reply drafted in Gmail, the first page summarised — not in the extension's own UI. |
| 6 — Onboarding | Adapted | Uses `BONUS-Browser-Extension-Onboarding-Best-Practice.md`: install → welcome tab → pin prompt → open the host site → first action. The wireframe covers the welcome tab and first in-page state. |
| 7 — Acquisition surface | Full | `design-marketplace-listing` for Chrome Web Store (plus Edge Add-ons and Firefox AMO if shipped) — the primary surface. Add `design-landing-page` for pricing, the upgrade checkout, and search traffic the store doesn't capture. |

## Develop route

| Step | Mode | How it adapts |
| --- | --- | --- |
| 0 — Migrate | Skip | Not applicable to extensions; a companion web app migrates under its own `web-app` route. |
| 1 — PRD & Roadmap | Full | Manifest V3 architecture, permissions, and target browsers are decided here. |
| 1b — Evals | Optional | Run it when the magic moment is an AI output (a drafted reply, a summary). |
| 2 — Verify setup | Full | Turn on version history (git) if it isn't on yet — the build saves its work there at every phase — and check the guidelines `setup` wired. Runs first in Develop. |
| 3 — Build | Full | The roadmap includes the backend (auth, billing, AI proxy) and a store-ready packaged build. |
| 4 — Build loop | Full | Host sites change their markup without warning — budget loop time for selector breakage. |
| 5 — Code review | Full | For changes made outside the build skills. |
| 6 — Design changes | Full | Review injected UI on the real host site in light and dark themes. |
| 7 — Conversion review | Adapted | Store listing → install → pin → first action → free cap → upgrade page → checkout. |
| 8 — Security audit | Full | Plus extension specifics: minimum permissions, no remote code, no secrets in the package, message-passing validation, what page data leaves the browser. |
| 9 — Go live | Adapted | Store submission rather than a deploy (below). |

### What the PRD must cover

- **Target browsers and manifest:** Chrome (MV3) first; Edge, Firefox, Safari later or at launch.
- **Permissions:** each permission and host permission, why it's needed, and whether it can be optional (requested at the moment of use) — narrow host lists over `<all_urls>`.
- **Surfaces:** popup, side panel, options page, content scripts, and exactly which sites and DOM elements the content scripts touch.
- **Backend:** auth (and how the extension shares a session with the web app), billing and entitlement checks, an AI proxy so no key ships in the package.
- **Data handling:** what page content is read, what is sent to the server, what is stored — this becomes the store's privacy disclosure.
- **Breakage plan:** how host-site DOM changes are detected and fixed fast.

### Go live

Production backend live → Chrome Web Store developer account (🧑 the member) → packaged build uploaded with the listing from `docs/MARKETPLACE-LISTING.md`, privacy-practices disclosures, and a privacy-policy URL → submitted for review → published (public, or unlisted for a soft launch) → repeat for Edge and Firefox. `develop-golive` writes this as `docs/DEPLOY.md`; live when the store-installed build passes the smoke test on a clean profile.

#### Review and policy — last reviewed October 2026 (re-verify before quoting)

- Chrome Web Store reviews usually take days; extensions requesting broad host permissions or sensitive APIs get more scrutiny and can take longer. Every update is reviewed again.
- Manifest V3 is required for Chrome; remotely hosted code is not allowed — all logic ships in the package.
- Chrome's single-purpose policy requires one narrow, clearly described purpose; the listing must not use a host site's brand in a way that implies affiliation.
- The privacy-practices tab must match what the code actually does; mismatches are a common takedown cause.

## Distribute notes

**Native channels:** Chrome Web Store search (keywords in title and description, ratings, the Featured badge), the host site's own communities (Gmail power users, LinkedIn creators, Salesforce admins), "best Chrome extensions for X" roundups and YouTube tutorials, Product Hunt, and SEO for "[host site] + [task]" queries.

**First users:**

1. Install it on 20 warm-network browsers yourself, on a call, and watch the first in-page action — pinning and permissions are where they stall.
2. Record a 20-second clip of the magic moment happening inside the host site and post it where the persona discusses that site.
3. Ask every early user who hit the magic moment for a store rating — the first ten ratings decide store ranking.
4. Write one "how to [task] in [host site]" article per core use case, each ending in the install link.
5. Pitch the YouTubers and newsletters that publish extension roundups for this persona.

**Activation and retention:** *activated* = a new install performs the first in-page action that produces the magic moment (logged from the extension, with consent). *Returned* = the user performs the core action again on at least two days in week 2. Also watch the uninstall rate — Chrome lets the member set an uninstall URL for a one-question exit survey.

## Watch-outs

- **Permission creep.** Asking for "read and change all your data on all websites" lowers install conversion and lengthens review. Request the narrowest hosts, and optional permissions at the moment of use.
- **The host site changes.** A redesign of Gmail or LinkedIn can break the extension overnight. Monitor the core flow and keep releases quick.
- **No checkout in the store.** Billing, accounts, and entitlement checks are the member's build — scope them in the PRD.
- **Platform dependency.** The store can delist, and the host site can block the integration. Collect emails on install so users can be reached outside the store.
- **Privacy disclosure drift.** New features that read more page data must update the store's privacy disclosures in the same release.
