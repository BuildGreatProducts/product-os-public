# Shape: MCP server

*Slug: `mcp-server` · Family: AI-native*

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

A connector that gives AI agents tools and data from a system, over the Model Context Protocol: a CRM connector, a database MCP, an internal-API bridge, a data feed only the member has. The customer's agent (Claude, ChatGPT, Cursor, Codex, and other MCP clients) discovers the server's tools and calls them on the user's behalf — the "user interface" is the tool list and its descriptions, read by a model. Servers run locally (stdio, installed as a package or a one-click bundle) or remotely (a hosted URL over Streamable HTTP, with OAuth). Paid MCP servers are almost always remote, because the value — data, compute, or an account — lives on the member's side. A settings page doesn't change the shape: the value is delivered through the agent.

## Live means

A stranger can connect the server to a mainstream MCP client from its public listing or docs — adding the remote URL and completing auth, or installing the package — and a clean agent session calls the server's tools to complete the documented first task against production, on the first try.

## First sale means

A real customer (warm network counts; the member's own test purchase doesn't) pays for access — usually a subscription or usage plan through Stripe Checkout or a merchant of record, which provisions the account the OAuth flow or API key is tied to — and their agent makes authenticated tool calls on the paid plan. An enterprise or team deal paid by invoice also counts once paid.

## Define notes

- **Persona:** two layers — the person who connects it (a developer, an ops lead, a power user) and the job their agent does with it. Name the client they use; it decides the auth and install path.
- **Pricing models:** subscription tiers by call volume or seats; usage-based (per call, per record, per credit) metered through Stripe; free tier with a call cap; or free connector as a feature of a paid SaaS (then this is a secondary shape of `web-app` or `developer-tool`).
- **Who pays:** an individual by card for prosumer data and tools; a company for connectors to its own systems, where security review and SSO enter the sale.
- **Unit economics:** every tool call has a cost (upstream API, compute, data licence). The pricing unit should track the costly call, not the session.

### Fees — last reviewed October 2026 (re-verify before quoting)

- At the last review, MCP directories and the official MCP Registry charged no listing fee and didn't handle payments. Some hosted MCP platforms offer built-in monetisation for a share of revenue — check their current terms before relying on one.

## Design route

| Step | Mode | How it adapts |
| --- | --- | --- |
| 1 — Identity | Lite | Name (checked against the MCP Registry and package registries), worldview, and tone of voice for docs and listings. |
| 2 — UX Writing | Adapted | `docs/COPY.md` covers the server's name and instructions, every tool name, tool description, and parameter description (the model reads these to decide what to call), error messages written so the agent can recover, and the docs voice. |
| 3 — Design System | Lite | Brand tokens for the docs site, landing page, OAuth consent screen, and account/settings page. |
| 4 — Design Prompts | Optional | Only for the account dashboard (keys, usage, billing) if one ships. |
| 5 — Magic Moment | Adapted | The first agent task that's impossible without the server — the user asks their agent a real question and gets an answer from the member's system. Named as the prompt and the expected result. |
| 6 — Onboarding | Adapted | Sign up → connect (paste the URL or install, then authorise) → the first prompt to try → magic moment. `docs/ONBOARDING.md` is per-client setup instructions plus the starter prompts; no wireframe unless a dashboard ships. Use `BONUS-Agent-Extension-Onboarding-Best-Practice.md` (and the API onboarding reference for the key and dashboard steps). |
| 7 — Acquisition surface | Full | `design-marketplace-listing` for the MCP Registry, client directories (Anthropic's connectors directory, ChatGPT's app directory, Cursor's), and community directories (Smithery, Glama, PulseMCP, mcp.so, Docker MCP Catalog). Plus `design-landing-page` — the docs-led page with pricing and signup. |

## Develop route

| Step | Mode | How it adapts |
| --- | --- | --- |
| 0 — Migrate | Skip | Not applicable. |
| 1 — PRD & Roadmap | Adapted | The PRD centres on the tool list, auth, and transports (below); the roadmap builds tools in order of the magic-moment task. |
| 1b — Evals | Full | `develop-agent-evals` — agent-in-the-loop scenarios: given a realistic prompt, does the agent pick the right tool, fill parameters correctly, and recover from errors? Run on at least two clients' models. |
| 2 — Verify setup | Full | Normally already done by `setup`. |
| 3 — Build | Full | `develop-build`, testing each tool with the MCP Inspector and the evals as it lands. |
| 4 — Build loop | Full | Tool description changes are behaviour changes — re-run the evals for them like code changes. |
| 5 — Code review | Full | For changes made outside the build skills. |
| 6 — Design changes | Optional | Only for the dashboard and OAuth screens. |
| 7 — Conversion review | Adapted | Landing page / directory listing → signup → connect → first successful tool call → paid plan. The connect step is the main drop-off. |
| 8 — Security audit | Full | Plus MCP specifics: OAuth implementation, per-user data isolation, no token passthrough to upstream APIs, least-privilege tool scopes, confirmation for destructive tools, prompt-injection paths through returned data, rate limiting. |
| 9 — Go live | Adapted | Hosted endpoint plus registry and directory publishing (below). |

### What the PRD must cover

- **Tool list with schemas:** every tool's name, description, input schema, output shape, side effects (read-only vs destructive), and the errors it returns. Keep the list short — fewer, well-described tools beat many overlapping ones.
- **Resources and prompts** (if any): what data is exposed as resources, and any prompt templates offered.
- **Auth:** OAuth for remote servers (the provider, scopes, token storage, refresh) or API keys; how a user's identity maps to their data upstream.
- **Transports:** Streamable HTTP for remote, stdio for local packages, and which clients each serves.
- **Rate limits and quotas:** per user and per plan, and what the agent sees when one is hit.
- **Metering and billing:** what's counted, where usage is recorded, how plans are enforced.
- **Observability:** per-tool call logs (without logging sensitive payloads), error rates, latency.
- **The eval set:** from `docs/EVALS.md`.

### Go live

Remote server deployed on the member's domain over HTTPS with OAuth working → account signup, billing, and usage limits live → tested in at least two clients from a clean account → published to the official MCP Registry → submitted to client directories that accept submissions → listed in community directories → a local package published to npm or PyPI (or a one-click bundle) if local install is supported. `develop-golive` writes this as `docs/DEPLOY.md`; live when a stranger connects and completes the first task.

#### Review and policy — last reviewed October 2026 (re-verify before quoting)

- The official MCP Registry (launched in preview in September 2025) lists metadata, not code: servers publish a `server.json` with the `mcp-publisher` CLI and verify their namespace via GitHub or a domain. Check the current process.
- Client directories (Anthropic's connectors directory, ChatGPT's app directory) review submissions against their own policies — expect requirements on OAuth, tool annotations (read-only / destructive), privacy policy, and test credentials for reviewers. Review timelines aren't published as fixed figures; check current guidance.
- Remote MCP auth follows the protocol's authorization spec (OAuth 2.1-based); the older HTTP+SSE transport is deprecated in favour of Streamable HTTP.

## Distribute notes

**Native channels:** the official MCP Registry, client directories (Claude, ChatGPT, Cursor), community directories (Smithery, Glama, PulseMCP, mcp.so, Docker MCP Catalog), GitHub, the communities of the system being connected (its user forums, admin communities, partner ecosystem), and developer channels (Hacker News, X, dev newsletters).

**First users:**

1. Connect it for ten warm-network users of the underlying system on a call, and give each three starter prompts — record the first answers as demos.
2. Post a short clip of an agent answering a real question from the system ("which deals stalled this month?") in that system's user community.
3. Publish to the MCP Registry and four directories in the same week.
4. Write one docs page per use case ("[system] + Claude for [job]") with copy-paste setup per client — these rank and get cited by AI search.
5. Offer the vendor of the underlying system a co-marketing slot if it fills a gap in their own AI story.

**Activation and retention:** *activated* = a new account's agent makes its first successful tool call that returns real data (the server sees it). *Returned* = that account makes tool calls on at least two days in week 2. Track signup → connected → first successful call — most loss is at connect.

## Watch-outs

- **Too many tools.** Wrapping every API endpoint floods the agent's context and confuses selection. Design tools around the user's tasks, not the upstream API.
- **Descriptions are the interface.** Vague tool descriptions mean wrong calls. Write and eval them like UX copy.
- **Prompt injection through returned data.** Content from emails, tickets, or web pages can carry instructions. Never let returned data trigger destructive tools without confirmation.
- **Client differences.** Auth flows, transport support, and tool limits vary by client. Test on every client the listing names.
- **Platform absorption.** If the system's vendor ships an official MCP server, a thin wrapper loses. The defensible value is data, workflow, or cross-system joins the vendor won't build.
