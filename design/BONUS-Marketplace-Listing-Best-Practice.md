# BONUS - Marketplace Listing Best Practice

*A bonus asset for ProductOS — principles, a decision tree, and field-by-field tactics for listings on every store, marketplace, registry, and directory that isn't the App Store or Google Play (those live in `BONUS-App-Store-Listing-Best-Practice.md`): browser extension stores, agent plugin marketplaces, skill and MCP directories, assistant stores, workplace app directories, editor marketplaces, package registries, API marketplaces, and digital-product storefronts. The tactics are timeless; every field limit, fee, and policy sits in the dated Store Reference at the end — re-verify before quoting.*

---

## Contents

- [The Meta-Rule](#the-meta-rule)
- [The 10 Principles](#the-10-principles)
- [The Decision Tree — Which Listings Does This Shape Need?](#the-decision-tree--which-listings-does-this-shape-need)
- [The 12 Tactics](#the-12-tactics)
- [Anti-Patterns — What Kills Marketplace Listings](#anti-patterns--what-kills-marketplace-listings)
- [Calibration — What Good Looks Like](#calibration--what-good-looks-like)
- [Store Reference — last reviewed October 2026](#store-reference--last-reviewed-october-2026-re-verify-before-quoting)
  - [Browser extension stores](#browser-extension-stores)
  - [Agent plugin marketplaces and directories](#agent-plugin-marketplaces-and-directories)
  - [Agent skills](#agent-skills)
  - [MCP registries and directories](#mcp-registries-and-directories)
  - [Assistant stores](#assistant-stores)
  - [Workplace and community app directories](#workplace-and-community-app-directories)
  - [Editor marketplaces](#editor-marketplaces)
  - [Package registries](#package-registries)
  - [API marketplaces](#api-marketplaces)
  - [Digital product storefronts](#digital-product-storefronts)
- [Closing — The One Mental Model That Beats Everything](#closing--the-one-mental-model-that-beats-everything)

---

## The Meta-Rule

> **A listing is read in a results list before it is read on its own page. The name, the icon, and the one-line pitch decide whether anyone clicks; the description, the visuals, and the install path decide whether they install; the store's reviewers decide whether the listing exists at all. Write for all three readers — the scanning shopper, the evaluating buyer, and the reviewer with a checklist — inside the store's exact limits.**

On many of these surfaces a fourth reader matters too: an AI agent or search index that matches the listing's text to a request. Clear, specific, honest text serves all four.

---

## The 10 Principles

### 1. The One-Liner Does the Selling

Most stores show a name, an icon, and one short line in search results and category pages. That line must say who it's for and what outcome it delivers — the magic moment as a benefit — within the field limit, without the product's name eating half of it.

### 2. Name for Recognition and Search

The name has to be memorable *and* findable. Where the store allows it and its rules permit, pair the brand with the job ("Clause — contract review for freelancers"). Never borrow the host platform's trademark in a way its rules forbid.

### 3. Show the Product Working in the Host

Screenshots and demos should show the product inside the surface the buyer already knows — the browser page with the extension's panel open, the terminal with the agent's output, the chat with the assistant's answer, the template with real data. A logo on a gradient proves nothing.

### 4. The Install Path Is Part of the Listing

For plugins, servers, packages, and templates, the listing usually carries the install instructions. A broken or ambiguous install line converts a willing buyer into a one-star review. Test it on a clean setup every release.

### 5. Every Store Has a Different Reader

A package registry's reader is a developer scanning a README; a template marketplace's reader is a buyer comparing preview images; an assistant store's reader is someone about to try a conversation. Same product, same voice — different emphasis per store.

### 6. Keywords Are Fields, Not Stuffing

Most stores index the name, the short description, tags, and categories; many penalize repetition. Put the buyer's own search words in the fields that are indexed, once each, in natural sentences.

### 7. The Reviewer Is a Customer Too

Store review rejects listings for missing privacy policies, unjustified permissions, misleading claims, and broken test accounts. Write the listing with the store's policy in hand, and give reviewers what they need — test credentials, a demo video, a clear permission rationale — before they ask.

### 8. Pricing Shows the Way the Store Shows It

Some stores display price natively; some can't take payment at all and the listing has to explain how paying works. Either way, the price, the plan, and what's free must mirror `docs/DEFINE.md` exactly — and the store's fee belongs in the pricing math.

### 9. Proof Is Real or Absent

Ratings, install counts, and testimonials build trust only if they're real. Pre-launch, lean on a clear demo, a guarantee, and the maker's credibility — never invented numbers.

### 10. The Listing Is a Living Asset

Stores reward recently updated, well-maintained listings, and buyers read changelogs. Revisit the listing every release: refresh screenshots, update the version notes, and test one change at a time when the store supports experiments.

---

## The Decision Tree — Which Listings Does This Shape Need?

Start from the primary shape in `docs/DEFINE.md`, then add the listings its secondary shapes need. The shape file's Design Step 7 row is the authority; this table is the default.

| Primary shape | Listings to write (primary first) |
| --- | --- |
| `browser-extension` | Chrome Web Store → Firefox Add-ons → Edge Add-ons (one section each; most text is shared, the limits differ) |
| `agent-plugin` | The host marketplace or directory for each host it supports (Claude Code / Cowork, Codex, Cursor) → the repository README → community directories |
| `agent-skill` | The plugin marketplace it ships in (skills usually travel inside a plugin) → the repository README → skill directories; a storefront if the skill is sold as a download |
| `mcp-server` | The official MCP Registry → the package registry it installs from (npm, PyPI, a container registry) → client directories (Claude connectors, ChatGPT apps) → community directories |
| `chat-assistant` | The host's store or directory (an assistant store, Slack Marketplace, Discord App Directory, Teams Store) |
| `developer-tool` | The package registry (npm, PyPI, crates.io, Homebrew) → editor marketplaces for any extension → API marketplaces for a paid API |
| `digital-product` | The storefront (Gumroad, Lemon Squeezy, Etsy) and/or the host's template marketplace (Notion, Framer) |
| `desktop-app` | Third-party desktop stores, if used — the Store Reference doesn't cover them; research their fields live |
| `mobile-app` | Not this doc — `design-app-listing` |
| `web-app`, `website`, `productized-service` | Usually none; a secondary shape (an MCP server, a Slack bot, a browser extension) brings its own listing |

**Prioritize.** Write the primary store in full first. Secondary stores reuse its copy, adapted to their limits and readers — never pasted unchanged when the limits or the reader differ.

---

## The 12 Tactics

Organized by the order a listing is read. Each listing in `docs/MARKETPLACE-LISTING.md` covers all twelve where the store has the field.

---

### Stage 1 — The Results List (the first second)

#### 1. The Name That Carries a Keyword

**Why:** In most stores the name is the most heavily indexed field and the first thing scanned. A brand plus a two- or three-word job, inside the limit and the store's naming rules, wins both recognition and search.

**Pass threshold:** Within the limit; contains the primary search term or sits beside it in the one-liner; passes the store's naming rules (no host trademarks where barred).

#### 2. The One-Line Pitch

**Why:** The summary or short description is the ad. It names the customer and the outcome — the magic moment as a benefit — and leaves features for the description.

**Pass threshold:** Within the field limit with the exact count shown; names who it's for and the outcome; no "AI-powered", "best", or "easy to use".

#### 3. The Icon That Survives Small Sizes

**Why:** Icons render tiny in results lists and sidebars. A single bold mark from the brand, readable at the smallest size the store shows, outperforms a detailed illustration.

**Pass threshold:** Recognizable at the store's smallest rendered size; follows the store's size, padding, and format rules.

---

### Stage 2 — The Listing Page (the next thirty seconds)

#### 4. The Description's First Lines

**Why:** Many stores truncate the description behind a "more" link, and buyers rarely click it. The first lines restate the outcome, name the mechanism, and say how fast the first result arrives.

**Pass threshold:** The first two or three lines stand alone as a complete pitch.

#### 5. The Scannable Body

**Why:** Buyers scan. Short sections — what it does, who it's for, how it works, what it accesses, pricing, support — beat paragraphs. Use the store's supported formatting and nothing it doesn't render.

**Pass threshold:** Every section has a heading or bullet structure the store renders; the body stays within the limit.

#### 6. Visuals in the Host

**Why:** Screenshots and demo videos are the strongest proof. Each shows the product working inside the host on realistic content, with a short benefit caption where the store allows overlays; the first visual shows the magic moment.

**Pass threshold:** The first visual shows the magic moment; every visual matches the store's sizes and count limits; captions are benefit-led and legible at thumbnail size.

#### 7. Categories, Tags, and Keywords

**Why:** Category placement decides which browse pages the listing appears on; tags and keywords decide which searches it matches. Choose the category buyers browse, not the broadest one, and use each tag slot for a distinct real search term.

**Pass threshold:** Category chosen from the store's fixed list; tags within the count and length limits; no repeated or irrelevant terms.

---

### Stage 3 — The Install (the next two minutes)

#### 8. The Install and First-Run Block

**Why:** For plugins, servers, packages, and templates the listing *is* the onboarding entry. Give the exact install action, the first thing to do after install, and what the buyer should see — matching `docs/ONBOARDING.md`.

**Pass threshold:** Exact install line or button text; one first-run action; the expected result; one troubleshooting line; all tested on a clean setup.

#### 9. The Access and Data Statement

**Why:** Buyers and reviewers both ask what the product can touch. State what it reads, writes, and sends, and why each permission is needed, in plain language — matching the store's privacy disclosure fields.

**Pass threshold:** Every permission or scope has a one-line justification; the statement matches the privacy policy and the store's disclosure form.

---

### Stage 4 — The Decision (pricing and trust)

#### 10. Pricing as the Store Shows It

**Why:** Buyers decide on price at the listing. Use the store's native pricing display where it exists; where it doesn't, say plainly what's free, what's paid, and where payment happens. Account for the store's fee in the price.

**Pass threshold:** Mirrors `docs/DEFINE.md` → Pricing Strategy exactly; the store's fee is noted; free-versus-paid is unambiguous.

#### 11. Real Proof and Real Support

**Why:** Ratings and installs accrue only to listings buyers trust. Use only real proof, link real support, and reply to early reviews — replies are visible proof of a maintained product.

**Pass threshold:** All proof is real or the slot says `[none yet — omit]`; a support link and a response commitment are listed.

---

### Stage 5 — The Review (before publishing)

#### 12. The Pre-Submission Checklist

**Why:** Rejections cost days or weeks. Every store has a policy set; a checklist built from the store's current rules — privacy policy, permission rationale, test account, demo video, naming rules, content rules — catches the common rejections before submission.

**Pass threshold:** A checklist per store, built from its current policy pages, every item checked or owned by the member with a date.

---

## Anti-Patterns — What Kills Marketplace Listings

### The Name-Only One-Liner

The summary repeats the name or says "The best tool for X." **Name the customer and the outcome.**

### The Pasted Listing

The same text pasted into every store, truncated mid-sentence where limits are shorter. **Adapt per store; count every field.**

### The Logo-on-Gradient Screenshot

Visuals that show branding instead of the product working. **Show the product in the host, on real content.**

### The Untested Install Line

An install command or config snippet that fails on a clean machine. **Test every release, on every host listed.**

### The Keyword Pile

Tags and descriptions stuffed with repeated search terms. Stores penalize it and buyers distrust it. **Each term once, where it's indexed.**

### The Permission Surprise

Broad permissions or scopes with no explanation. Reviewers reject it; buyers abandon at the prompt. **Least privilege, each justified.**

### The Invented Proof

Placeholder ratings, imaginary user counts, or logos of customers who never bought. **Real or absent.**

### The Policy Afterthought

No privacy policy, no test account, a missing demo video — discovered at rejection. **Build the checklist before writing the copy.**

### The Stale Listing

Screenshots from three versions ago and a changelog that stopped. **Refresh with every meaningful release.**

---

## Calibration — What Good Looks Like

*ProductOS design targets — not measured benchmarks. Stores report their own impression, view, and install numbers; replace these with yours once the listing is live.*

| Measure | Target |
| --- | --- |
| Every field within the store's current limit | 100%, counts shown in the spec |
| One-liner names the customer and the outcome | always |
| First visual shows the magic moment | always |
| Install line tested on a clean setup | every release, every host listed |
| Permissions with a written justification | all |
| Listing refresh | every meaningful release, and at least every 60–90 days |
| First experiment (where the store supports it) | the first visual or the one-liner |

---

## Store Reference — last reviewed October 2026 (re-verify before quoting)

Field limits, fees, and policies change without notice. Each fact below was checked against the platform's own documentation in October 2026 unless marked *(secondary source)* or *(unverified)*. Before writing a listing, re-check the store's current docs or submission form by web search; if you can't, say the limits are unverified. Read only the sections your listings need.

### Browser extension stores

**Chrome Web Store**

| Field | Limit or spec |
| --- | --- |
| Name (manifest `name`) | ≤75 characters |
| Summary (manifest `description`) | ≤132 characters, plain text |
| Detailed description | no limit documented *(16,000 is often cited — unverified)* |
| Icon | 128×128 PNG — 96×96 artwork with 16 px transparent padding |
| Screenshots | 1280×800 or 640×400, 1–5, full bleed, square corners |
| Promo tiles | small 440×280 (required); marquee 1400×560 (optional) |
| Fees | one-time developer registration fee *(amount commonly reported as $5 — secondary source)* |

Policy and review: single purpose; narrowest permissions; privacy policy and pre-install data disclosure; Limited Use (no selling data, no ad use of user data); Manifest V3 bans remotely hosted code; keyword spam is prohibited (repeating one keyword more than a handful of times). Review usually takes a few days and can take weeks — longer for new developers, broad host permissions, sensitive permissions, and large or minified code.

**Firefox Add-ons (AMO)**

| Field | Limit or spec |
| --- | --- |
| Name | ≤50 characters *(secondary source)* |
| Summary | ≤250 characters |
| Description | no practical limit |
| Screenshots | 1280×800 recommended (1.6:1), no count limit |
| Fees | none *(secondary source)* |

Policy and review: source code must be submitted when a minifier, bundler, or custom build step is used, with build instructions that reproduce the package exactly; obfuscation is banned. New extensions must declare data collection in the manifest (`data_collection_permissions`, `"none"` if nothing is collected) — required for new extensions since November 2025; extension to all extensions was planned for 2026 *(unverified)*.

**Microsoft Edge Add-ons**

| Field | Limit or spec |
| --- | --- |
| Short description | from the manifest `description` (the Chrome limit applies) |
| Description | 250–10,000 characters |
| Search terms | up to 7 terms, ≤30 characters each, ≤21 words total |
| Logo | 1:1, 300×300 recommended, 128×128 minimum |
| Tiles | small 440×280; large 1400×560 |
| Screenshots | up to 6, 640×480 or 1280×800 |
| Fees | registration is free |

Policy and review: a privacy tab with a single-purpose statement, a justification per permission, a remote-code declaration, data-use certification, and a privacy policy URL. Certification takes up to 7 business days.

### Agent plugin marketplaces and directories

**Claude Code / Cowork plugins**

- `plugin.json`: only `name` is required (kebab-case); optional `displayName`, `version`, `description`, `author`, `homepage`, `repository`, `license`, `keywords`, and component paths. Directory listings add an icon and documentation, support, privacy, and terms URLs. Names beginning `claude-` or `anthropic-` are rejected.
- A marketplace is a repository with `marketplace.json` (`name`, `owner`, `plugins[]`, each with `name` and `source`). Customers run `/plugin marketplace add owner/repo`, then `/plugin install plugin@marketplace` — print both lines in the listing.
- Anthropic's plugin directory: submit through the directory's management page and run its validator. Blocking checks have included a README of at least 40 words, a license, a unique name of ≤64 characters, exact version pins for `npx`/`uvx`, and no embedded credentials; large repositories and binaries are held for manual review, and every new version is security-scanned.

**Codex (and ChatGPT) plugins**

- `plugin.json` → `interface`: `displayName`, `shortDescription`, `longDescription`, `developerName`, `category`, `capabilities`, `defaultPrompt`, `brandColor`, logo and icons, screenshots, website/privacy/terms URLs.
- OpenAI's shared app and plugin review applies the same limits as ChatGPT apps (see Assistant stores): display name ≤30, subtitle ≤30, long description ≤4,000, up to 3 starter prompts of ≤128 characters. Plugins with lifecycle hooks can't go in the public directory.

**Cursor plugins**

- `.cursor-plugin/plugin.json` (only `name` required). Submit through Cursor's marketplace publishing page; plugins must be open source and every update is reviewed manually. Review has been reported at up to about two weeks *(secondary source)*.

**Community directories** list plugins from their repositories; the README is the listing. Write it with the Tactics above: install line and first prompt first.

### Agent skills

- Agent Skills format: `name` 1–64 characters (lowercase letters, digits, hyphens; matches the folder); `description` 1–1,024 characters; optional `license`, `compatibility` (≤500), `metadata`, `allowed-tools`. Keep the body under about 500 lines.
- The description is both the listing's one-liner and the text agents match to decide when to load the skill: what it does, when to use it, when not to.
- Skills are usually distributed inside a plugin marketplace or a repository; use the plugin sections above for the listing itself.

### MCP registries and directories

**Official MCP Registry**

| Field | Limit or spec |
| --- | --- |
| `name` | 3–200 characters, `namespace/server` form (e.g. `io.github.user/server`) |
| `description` | 1–100 characters |
| `title` | ≤100 characters |
| Other fields | `version` (required), `packages[]`, `remotes[]`, `repository`, `websiteUrl` |

Namespace proof: `io.github.<user-or-org>/*` via GitHub login in the `mcp-publisher` CLI; domain namespaces via a DNS TXT record or an HTTP well-known file. Package ownership is proven in the package itself (`mcpName` in `package.json` for npm; an `mcp-name:` line in the README for PyPI; a label for container images).

**Claude connectors directory**

Every tool needs a `title` and a `readOnlyHint` or `destructiveHint` annotation; read and write actions must be separate tools (no catch-all method parameter); tool names ≤64 characters; no prompt-injection patterns in descriptions. Submissions need test credentials for a fully populated account and public documentation by the publish date. Money transfer and AI image, video, or audio generation have not been accepted. Submissions are scanned automatically and listed as community connectors, with verification possible later.

**ChatGPT apps** — see Assistant stores. **Community directories** typically pull from the repository and the registry; keep the README and `server.json` description consistent.

### Assistant stores

**ChatGPT apps directory (OpenAI)**

Verified organization and domain; https privacy, terms, support, and website URLs; a square icon of at least 48 px; a test account without MFA; 5 positive and 3 negative test cases; a video walkthrough. Limits: display name ≤30, subtitle ≤30, long description ≤4,000, up to 3 starter prompts of ≤128 characters, up to 20 capabilities of ≤120 characters.

**GPT Store (custom GPTs)**

- Knowledge: up to 20 files, 512 MB each; instructions ≤8,000 characters *(secondary source)*. Description and conversation-starter limits are not documented — check the builder.
- Builder profiles are verified by billing name or domain *(secondary source)*.
- Reported in August 2026: personal accounts can no longer create or publish new GPTs; creation continues in Business, Enterprise, and Edu workspaces *(secondary source — confirm before planning a GPT Store launch)*. The builder revenue programme has been a limited pilot *(secondary source)*.
- Naming rules on OpenAI's marks: check the current brand guidelines *(unverified)*.

**Other assistant directories** (Poe, assistant hubs inside workplace tools) — research fields live.

### Workplace and community app directories

**Slack Marketplace**

| Field | Limit or spec |
| --- | --- |
| Short description | ≤10 words |
| Long description | no limit; keyword stuffing discouraged |
| Screenshots | 1600×1000 (8:5), JPG or PNG, under 2 MB |
| Video | 30–90 seconds, YouTube |
| Eligibility | at least 10 active workspaces or 10 weekly active users before submitting |

AI rules: say that LLM output may be inaccurate; disclose the model, data retention, and data residency; no training on Slack data; consequential decisions need human review; the assistant overview ≤25 words. Review timeline isn't published.

**Discord App Directory**

| Field | Limit or spec |
| --- | --- |
| Description | ≤400 characters |
| Summary | ≤200 characters |
| Expanded description | Markdown, no stated limit |
| Tags | 1–5 |

Listing requires a verified app with a privacy policy and terms. Unverified bots are capped at 100 servers, with verification open from 75 *(secondary source)*. Premium apps: 85% to the developer on the first $1M of gross sales, 70% after, in supported regions *(secondary source)*.

**Microsoft Teams Store**

Manifest limits: `name.short` ≤30, `name.full` ≤100, `description.short` ≤80, `description.full` ≤4,000, `developer.name` ≤32. Submission goes through Partner Center validation.

### Editor marketplaces

**VS Code Marketplace**

- `package.json`: `displayName` (unique on the Marketplace), `description`, `categories` (fixed list), `keywords` (≤30), `icon` (PNG ≥128×128, 256×256 for Retina; no SVG), `galleryBanner`. The README is the listing page and the CHANGELOG is shown beside it.
- README and CHANGELOG images must use https; SVG images only from trusted badge providers.
- Verified publisher badge: six months on the Marketplace, a domain registered six months, a DNS TXT record, and up to 5 business days of review.

**Open VSX** (the registry Cursor, VSCodium, and Windsurf install from): an Eclipse account linked to GitHub, the publisher agreement, an access token, then `ovsx create-namespace` and `ovsx publish`. Publish to both registries to reach every VS Code–based editor.

**JetBrains Marketplace**

- Name: Latin characters; no "Plugin", "IntelliJ", "JetBrains", or JetBrains product names. JetBrains' own docs disagree on length (≤30 in the approval guidelines; ≤60 hard limit with ≤20 recommended in the listing guide) — stay ≤30.
- Description: English first; the first 40 characters are an English summary shown on preview cards; no marketing adjectives or donation links.
- Logo: 40×40 SVG, not the template default. Every new plugin and update is reviewed manually.
- Paid plugins: 15% commission; no listing fees.

### Package registries

For packages the README is the listing; its first screen needs the one-liner, the install line, and a minimal working example.

**npm** — `name` ≤214 characters including scope, lowercase, URL-safe; `description` and `keywords` feed search. Unpublishing is restricted after 72 hours (no dependents, low downloads, single owner) and version numbers can never be reused — treat publishing as permanent and use `npm deprecate` instead. Trusted publishing from CI (OIDC) is the recommended path, with provenance attached automatically for public repositories; long-lived classic tokens were revoked in December 2025.

**PyPI** — summary ≤512 characters; the long description (README) has no size limit and renders as Markdown or reStructuredText per `Description-Content-Type`; classifiers come from the official list (`License ::` classifiers are deprecated in favor of a license expression). Trusted publishing is supported from major CI providers.

**crates.io** — required: `name` (≤64, ASCII), `version`, `description`, `license` or `license-file`. `keywords` ≤5, each ≤20 ASCII characters; `categories` ≤5, exact category slugs. Publishing is permanent; `cargo yank` blocks new dependents but deletes nothing.

**Homebrew** — homebrew-core requires notability (30 forks, 30 watchers, or 75 stars; triple that for self-submitted projects; repositories under 30 days old rarely qualify), a stable tagged release, an open license, and a source build passing CI. The `desc` field: under 80 characters, no leading article, starts with a capital, doesn't start with the formula name, no trailing period. Before notability, ship your own tap.

### API marketplaces

**RapidAPI Hub** — listing with name, descriptions, category, endpoint docs, and plan tiers; a 25% marketplace fee since November 2025 (up from 20%); payouts via PayPal. Price plans with the fee included.

**Postman API Network** — listing is a public workspace with collections and docs; a verified-publisher badge needs domain verification and a team with work emails on that domain.

### Digital product storefronts

**Gumroad** — 10% + $0.50 per direct sale; 30% on sales through its Discover marketplace; merchant of record for sales tax. Covers ≥1280×720, up to 8 per product; thumbnail 600×600 *(thumbnail size: secondary source)*.

**Lemon Squeezy** — 5% + 50¢ per sale, merchant of record. Sellers have been pointed toward Stripe's managed payments product *(secondary source — check current terms before choosing it)*.

**Etsy** *(all secondary sources — Etsy's pages weren't reachable at the last review)* — title ≤140 characters; 13 tags of ≤20 characters; up to 20 photos; $0.20 listing fee per four months; 6.5% transaction fee. AI use must be disclosed under its creativity standards, and selling AI prompts is banned.

**Notion Marketplace** — 8% + $0.40 per paid template sale (some localized pages still show 10%); sellers apply and are approved before onboarding payments.

**Framer Marketplace** — creators keep 100% of paid-template revenue; templates are reviewed manually for up to about 21 days and must be original.

---

## Closing — The One Mental Model That Beats Everything

> **Picture your listing as one row in the store's search results, between two competitors. In the space of a name, an icon, and one line, the buyer has to see who it's for and what they'll get. Everything else on the listing — the description, the visuals, the install line, the checklist that got it approved — exists to make good on that one line.**

Stores reward listings that convert and keep their buyers. Write the line, prove it in the host, make the install work the first time, and keep the listing as current as the product.
