# Shape: API, SDK, or CLI

*Slug: `developer-tool` · Family: Other*

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

Programmatic access other developers build on: a paid API (an AI model behind an endpoint, a data API, a document-processing API), an SDK that wraps a service, or a command-line tool. The customer is a developer who integrates it into their own code; the value arrives as responses, packages, and commands, and the docs are the main interface. It lives on the member's domain (the API and docs site) and in package registries — npm, PyPI, crates.io, Go modules, Homebrew, Docker Hub, GitHub Releases — with an account dashboard for keys, usage, and billing. If AI agents are the main consumer of the tool, consider `mcp-server` as the primary shape or a secondary one.

## Live means

A stranger can sign up from the public docs or landing page, get an API key (or install the package from its public registry), and make the documented first call or run the documented first command from the quickstart — succeeding against production on the first try, in under the time the docs promise.

## First sale means

A real customer (warm network counts; the member's own test purchase doesn't) pays — a subscription or prepaid credits through Stripe Checkout, a usage-based invoice metered through Stripe Billing and actually paid, or a paid licence for a CLI or SDK — and their key makes calls on the paid plan. An API sold through a marketplace counts when the marketplace payout for a real customer's usage arrives.

## Define notes

- **Persona:** the developer who integrates it *and* who pays — often different at companies (the engineer chooses, the engineering lead approves spend). Name the language and stack they use; it decides which SDKs and examples ship first.
- **Pricing models:** usage-based (per call, per token, per record, per minute processed) with a free monthly allowance; prepaid credits; tiered subscriptions with included usage and overages; open-source core with a paid hosted service or paid features; per-seat licences for CLIs used by teams.
- **Who pays:** the developer by card for small usage; the company by invoice above a threshold. Self-serve card checkout must exist even if large deals are invoiced.
- **Unit economics:** price per unit must clear the cost per unit (model inference, upstream data, compute) with margin at the free-tier volume, too.

### Fees — last reviewed October 2026 (re-verify before quoting)

- Package registries (npm, PyPI, crates.io, Homebrew) are free to publish to and take no revenue; payment always runs through the member's own billing.
- API marketplaces (such as RapidAPI) and cloud marketplaces (AWS Marketplace, Azure Marketplace, Google Cloud Marketplace) take a percentage of sales and handle billing; percentages vary by marketplace and deal type — check the current figure before listing.

## Design route

| Step | Mode | How it adapts |
| --- | --- | --- |
| 1 — Identity | Full | The name check covers the package names on each registry, the CLI command name (short, unclaimed, not a common shell command), and the docs domain. |
| 2 — UX Writing | Adapted | `docs/COPY.md` covers error messages (what went wrong, why, how to fix — with a docs link), CLI help text, flag and command names, API field naming conventions, log output, and the docs voice. |
| 3 — Design System | Lite | Brand tokens for the docs site, landing page, and dashboard; terminal colour conventions for a CLI. |
| 4 — Design Prompts | Optional | For the dashboard (keys, usage, billing) and the docs site layout, when they're custom rather than a docs platform's theme. |
| 5 — Magic Moment | Adapted | The first successful call or command that returns something useful from the developer's own input — not a hello-world. Named with its expected time-to-first-call. |
| 6 — Onboarding | Adapted | Uses `BONUS-API-and-Developer-Tool-Onboarding-Best-Practice.md`: sign up → key shown once → copy-paste quickstart in the developer's language → first response → next step. The wireframe covers the dashboard's first-run state. |
| 7 — Acquisition surface | Full | `design-landing-page` — a docs-led page with a code sample above the fold and the pricing table. Add `design-marketplace-listing` for package registry pages (the README is the npm / PyPI listing), GitHub, and any API or cloud marketplace used. |

## Develop route

| Step | Mode | How it adapts |
| --- | --- | --- |
| 0 — Migrate | Skip | Prompt-to-app platforms don't produce developer tools; Skip unless the dashboard came from one. |
| 1 — PRD & Roadmap | Adapted | The PRD centres on the interface contract (below); the roadmap builds the core endpoint or command first, then keys, metering, billing, SDKs, and docs. |
| 1b — Evals | Optional | Run it when the API's core output is AI-generated (extraction, generation, classification) — evals become the quality bar the docs can quote. |
| 2 — Verify setup | Full | Turn on version history (git) if it isn't on yet — the build saves its work there at every phase — and check the guidelines `setup` wired. Runs first in Develop. |
| 3 — Build | Full | `develop-build`, with contract tests for every endpoint or command and the quickstart run as an end-to-end test. |
| 4 — Build loop | Full | Every change checks backwards compatibility; breaking changes need a new version and a deprecation notice. |
| 5 — Code review | Full | For changes made outside the build skills. |
| 6 — Design changes | Optional | For the dashboard and docs site when custom. |
| 7 — Conversion review | Adapted | Landing / docs → signup → key → first successful call → free-allowance limit → paid plan. Time-to-first-call is the headline metric. |
| 8 — Security audit | Full | Plus API specifics: key hashing and rotation, per-key rate limits, tenant isolation, input validation and size limits, abuse of free tiers, supply-chain hygiene for published packages (provenance, no secrets in the package). |
| 9 — Go live | Adapted | API deploy plus package publish (below). |

### What the PRD must cover

- **The interface contract:** endpoints (method, path, request and response schemas, error codes) as an OpenAPI spec, or commands and flags for a CLI, or the public SDK surface.
- **Auth:** API keys (scopes, rotation, how they're shown once and stored hashed) or OAuth for user-delegated access.
- **Rate limits and quotas:** per key and per plan; response headers and errors when a limit is hit.
- **Metering and billing:** the billed unit, where usage is recorded, how it reaches Stripe, how overages and hard caps work.
- **Versioning:** the versioning scheme, compatibility promise, and deprecation policy.
- **SDKs and packages:** which languages at launch, registry names, and how they're generated or maintained.
- **Docs:** quickstart, reference, examples per use case, and changelog — the docs are part of the MVP, not after it.
- **Observability:** per-key request logs, error rates, latency, a public status page.

### Go live

API deployed on the member's domain over HTTPS → dashboard with signup, keys, usage, and billing live → docs site published → packages published to their registries from CI (🧑 the member creates registry accounts with two-factor auth) → the quickstart run from a clean machine by someone who didn't build it → status page live. `develop-golive` writes this as `docs/DEPLOY.md`.

#### Review and policy — last reviewed October 2026 (re-verify before quoting)

- npm and PyPI support trusted publishing from CI (short-lived tokens instead of stored secrets) and package provenance; registries increasingly require two-factor auth for maintainers. Check each registry's current requirements.
- Homebrew's core repository has notability criteria; a new tool usually starts in the member's own tap. Check the current acceptance rules.
- Registry names are first-come and hard to reclaim — claim them in the first build phase.

## Distribute notes

**Native channels:** Hacker News ("Show HN"), GitHub (README, topics, stars, "awesome" lists), developer communities (language-specific subreddits, Discord servers, Dev.to), technical SEO (docs and "how to [task] in [language]" tutorials), package registry search, API and cloud marketplaces for enterprise buyers, and AI search (docs that get cited by coding agents).

**First users:**

1. Pair with ten warm-network developers as they integrate it, without helping — note every place they open the docs twice.
2. Post a "Show HN" or community launch with a working code sample and honest pricing.
3. Publish three tutorials that solve a real task end to end in the persona's main language, each ending in signup.
4. Open-source a useful piece (a CLI, an SDK, an example app) that pulls developers to the paid API.
5. Make the docs easy for coding agents to read (clean markdown, an `llms.txt`, an MCP server if fitting) so agents recommend and integrate it.

**Activation and retention:** *activated* = a new account's key makes its first successful production call (or the CLI completes its first real command). *Returned* = the key makes calls on at least three days in week 2 — real integrations call daily. Track signup → key created → first call → tenth call; the drop between first and tenth shows integrations that stalled.

## Watch-outs

- **Docs as an afterthought.** For developers the docs are the product. A quickstart that fails once loses the developer.
- **Breaking changes.** A changed response field breaks customers' production code. Version from day one.
- **Free-tier abuse.** Signups made to farm free AI calls can cost real money. Card on file or tight limits for expensive endpoints.
- **Building SDKs for every language.** Launch with the persona's language and a clean HTTP API; add SDKs as paying users ask.
- **Unclaimed names.** A squatted package or CLI name forces a rename after launch. Claim registry names at the start.
