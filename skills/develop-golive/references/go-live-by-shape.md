# Go live by shape

The go-live path, the checklist, and the smoke test for each shape. Read the section for the primary shape, plus any secondary shape the product ships. The shape file's **Live means** is always the bar; these checklists are how to reach it. Platform fees, review rules, and limits are in the dated section at the end — never quote them as timeless.

## Contents

- [Every shape](#every-shape)
- [web-app](#web-app)
- [mobile-app](#mobile-app)
- [desktop-app](#desktop-app)
- [browser-extension](#browser-extension)
- [agent-skill](#agent-skill)
- [agent-plugin](#agent-plugin)
- [mcp-server](#mcp-server)
- [chat-assistant](#chat-assistant)
- [developer-tool](#developer-tool)
- [productized-service](#productized-service)
- [website](#website)
- [digital-product](#digital-product)
- [Platform facts — last reviewed October 2026 — re-verify before quoting](#platform-facts--last-reviewed-october-2026--re-verify-before-quoting)

## Every shape

- Payments live, with a real purchase made and refunded.
- Legal pages the shape needs: privacy policy, terms, refund policy.
- The acquisition surface live and pointing at the real front door (install link, store page, booking page, checkout).
- Someone is notified when it breaks: error tracking for code, an inbox the member watches for no-code shapes.

## web-app

**Path:** deploy to the host the PRD chose (default from `TECH-STACK-OPTIONS.md` § Hosting & Deployment), connect the domain.

- Production build green; environment variables set on the host; database and auth on production settings; auth redirect URLs on the real domain.
- Payment webhooks pointed at the production URL; analytics and error tracking receiving events.
- **Smoke test:** from a phone and a laptop, a stranger's path — land on the page, sign up, reach the magic moment, pay, refund.

## mobile-app

**Path:** developer accounts → store listings → builds submitted (EAS or native) → review → release.

- Bundle ID, app icons, screenshots, and listing copy from `docs/APP-LISTING.md`; privacy disclosures (App Store privacy labels, Play data safety form) matching what the app actually collects.
- In-app purchase products created and approved alongside the build; a sandbox purchase tested.
- Pre-release testing track (TestFlight, Play testing tracks) used before submission; a reviewer account with demo data if the app needs a login.
- **Smoke test:** install from the live store listing on a real device, sign up, reach the magic moment, buy and restore a purchase.

## desktop-app

**Path:** signed builds → download page (or app store) → auto-update channel live.

- macOS: signed with a Developer ID and notarized; Windows: code-signed so installers don't trigger scary warnings; Linux packages if the PRD names them.
- Auto-update tested from one version to the next; licensing or account check working against production.
- **Smoke test:** download from the live page on a clean machine, install without warnings, reach the magic moment, buy, update to a newer build.

## browser-extension

**Path:** store developer account → listing → package upload → review → published (Chrome Web Store first; Firefox Add-ons and Edge Add-ons when the PRD names them).

- Every permission justified in the listing; the narrowest host permissions that work; a privacy policy URL; the store's privacy and data-use declarations filled honestly.
- Any backend on production settings; payments gated server-side, never only in the extension.
- **Smoke test:** install from the live store page into a fresh browser profile, reach the magic moment on a real site, pay, confirm the paid features unlock.

## agent-skill

**Path:** package (a plugin wrapping the skill, or a zip) → publish where customers install it (a marketplace repo, a host directory, or a private repo for buyers).

- Frontmatter final; the description tuned against `docs/EVALS.md`'s triggering table; no secrets, absolute paths, or personal data in the skill files.
- Install instructions for each target host; a version number and changelog.
- **Smoke test:** in a fresh environment, install it the way a customer would, give a should-trigger request from `docs/EVALS.md` in the customer's words, and get the job done on the mid model.

## agent-plugin

**Path:** manifests final → marketplace published → install from the marketplace → submit to the hosts' official directories once it has users.

- Each host's manifest valid (name, version, description, author, homepage, license); components load without errors; hooks fail safe.
- Credentials for bundled connectors come from the user's environment or the host's secret store — none in manifests or committed config.
- Paid plugin: access granted on purchase (private repo invite, license key) and revoked on refund.
- **Smoke test:** add the marketplace and install the plugin in a fresh environment on each target host, run the magic-moment job end to end, update to a new version.

## mcp-server

**Path:** remote — deploy over HTTPS with OAuth, then list it; local — publish the package (npm or PyPI), then list it.

- Remote: production URL on HTTPS; OAuth flow working with every client the PRD names; rate limits and per-user token storage in place; logs and error tracking on.
- Local: the package installs and runs with the one-line config in the README; credentials from environment variables.
- Tool descriptions and errors final against `docs/EVALS.md`; destructive tools marked and confirmed.
- Listed in the MCP registry and the host directories the persona uses.
- **Smoke test:** connect from each named client as a new user, authorize, and have an agent complete the magic-moment job from a plain request.

## chat-assistant

**Path:** publish on the platform (public GPT, Slack or Discord app, Telegram or WhatsApp bot) → access gating and payment → listing.

- System prompt, knowledge, and actions final against `docs/EVALS.md`; action endpoints on production with auth.
- Payment and access gating working (an external checkout that unlocks access, or the platform's own monetization).
- Platform review or verification passed where required (app directories, WhatsApp business verification).
- **Smoke test:** as a new user, find it through its public link or directory, start a conversation, reach the magic moment, pay, and confirm paid access works.

## developer-tool

**Path:** release the package (npm, PyPI, or another registry) and/or deploy the API → docs live → keys and billing live.

- Release from CI with trusted publishing, a version tag, and a changelog; the README quickstart matches the docs.
- API: production deploy, key issuance and revocation, rate limits, usage metering into billing.
- Docs site live with the quickstart, reference, and errors.
- **Smoke test:** on a clean machine, follow the public quickstart from zero — install, get a key, make the first successful call — then upgrade to a paid plan.

## productized-service

**Path:** booking page → payment → intake → delivery pipeline, run end to end once.

- Booking page live with real availability; payment link or checkout live (deposit or full); intake form collecting everything the SOP needs.
- Confirmation and onboarding messages sent automatically; the client record created; terms and refund policy linked at checkout.
- Security audit only if there is custom code or stored customer data beyond the tools' own.
- **Smoke test:** a friend books, pays full price, submits intake, and receives the delivery on time through the real pipeline; then refund them if agreed.

## website

**Path:** deploy (or publish from the builder) → domain → search and analytics.

- Domain with HTTPS; analytics on; forms delivering to a watched inbox; sitemap submitted to search engines; titles, meta, and structured data per template.
- Memberships or paid listings: checkout live and access gated.
- **Smoke test:** from a phone, find a page through search or a shared link, use the core content (search the directory, read the resource), subscribe or pay, and confirm the welcome email arrives.

## digital-product

**Path:** storefront → product page → delivery → a real purchase.

- Product page copy and preview assets live; files final and versioned; delivery email and download (or duplicate link, or course access) working; license keys issued if used.
- Refund policy stated; tax handled (a merchant-of-record storefront, or the member's own setup).
- **Smoke test:** buy it at full price from a separate account, receive and open the files, reach the first result the product promises, then refund.

## Platform facts — last reviewed October 2026 — re-verify before quoting

- **Apple App Store** — an Apple Developer Program membership (annual fee, US$99 at last review) is required; review can take days and may come back with fixes to make before approval. Apps sold outside the Mac App Store need Developer ID signing and notarization.
- **Google Play** — a one-time registration fee (US$25 at last review); new personal developer accounts must run a closed test with a minimum number of testers for a minimum period before production access — check the current numbers.
- **Chrome Web Store** — a one-time developer registration fee (US$5 at last review); review time varies with the permissions requested. Firefox Add-ons and Edge Add-ons have no registration fee at last review.
- **Windows code signing** — unsigned installers trigger SmartScreen warnings; certificate options and prices change often.
- **Agent hosts** — plugin marketplaces and official directories for Claude Code, Codex, and Cursor each have their own submission and review process; check each before promising a listing date.
- **MCP** — an official MCP Registry lists public servers; host connector directories (e.g. Claude's) review submissions separately and may require OAuth for remote servers.
- **Chat platforms** — a public GPT needs a verified builder profile; the Slack Marketplace reviews apps before listing; WhatsApp requires business verification and restricts general-purpose AI assistants.
- **Package registries** — npm and PyPI support trusted publishing from CI and require or encourage two-factor auth for publishers.
- **Storefronts** — merchant-of-record status and per-sale fees differ by storefront and change; read the current seller terms.
