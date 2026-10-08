# Product Shapes

A product's **shape** is how the customer receives and uses it: the surface it lives on, what "live" means, and what a first sale looks like. The shape decides which ProductOS steps apply and how each one adapts. A skill for an AI agent doesn't need a screen-by-screen design system; a productized service doesn't deploy to a server; a mobile app's acquisition surface is a store listing, not a landing page.

`define-product-shape` picks the shape (Define Step 1b) and writes it to the `## Product Shape` section of `docs/DEFINE.md`. Every phase orchestrator, `product-audit`, and the challenges read that section, then read the one shape file below for the route.

## Contents

- [The shapes](#the-shapes)
- [Picking a shape](#picking-a-shape)
- [Hybrid and sequenced products](#hybrid-and-sequenced-products)
- [Shape file format](#shape-file-format)

## The shapes

| Slug | Shape | What the customer gets | Examples |
| --- | --- | --- | --- |
| `web-app` | Web app | Software they sign in to in a browser | SaaS dashboards, AI writing tools, internal-tool builders |
| `mobile-app` | Mobile app | An app from the App Store or Google Play | AI photo apps, habit trackers, companion apps |
| `desktop-app` | Desktop app | An installed Mac/Windows/Linux application | Menu-bar utilities, AI meeting recorders, editors |
| `browser-extension` | Browser extension | An add-on from a browser's extension store | AI reply helpers, page summarizers, tab managers |
| `agent-plugin` | Agent plugin | A plugin for an AI agent or AI coding tool — bundled skills, commands, agents, hooks, or connectors | Claude Code / Cowork plugins, Codex plugins, Cursor plugins |
| `agent-skill` | Agent skill | One skill or a skill pack an agent loads to do a job well | A brand-voice skill, a financial-model skill, a code-review skill pack |
| `mcp-server` | MCP server | A connector that gives AI agents tools and data from a system | A CRM connector, a database MCP, an internal-API bridge |
| `chat-assistant` | Chat assistant | An assistant people talk to in a chat surface | Custom GPTs, Claude Projects, Slack/Discord/WhatsApp/Telegram bots |
| `developer-tool` | API, SDK, or CLI | Programmatic access other developers build on | A paid API, an SDK, a command-line tool |
| `productized-service` | Productized service | A fixed-scope outcome delivered for a fixed price, run with AI behind the scenes | AI-assisted bookkeeping, done-for-you SEO, a design subscription |
| `website` | Website | A site whose content, directory, or community is the product | A niche directory, a newsletter with a site, a resource library, a community |
| `digital-product` | Digital product | A file or package bought once and downloaded | Templates, prompt packs, Notion systems, courses, ebooks, presets |

## Picking a shape

Ask in this order, and stop at the first clear yes:

1. **Does the customer pay for an outcome someone (or something) delivers to them, rather than a tool they operate?** → `productized-service`.
2. **Do they buy it once and download it?** → `digital-product`.
3. **Does it run inside an AI agent or AI tool the customer already uses?** One capability → `agent-skill`; a bundle of skills, commands, agents, or hooks → `agent-plugin`; a connection to a system's tools and data → `mcp-server`; a conversation partner → `chat-assistant`.
4. **Do developers integrate it into their own code?** → `developer-tool`.
5. **Is the content, directory, or community the product?** → `website`.
6. **Otherwise it's software with a screen:** where does the customer use it — browser (`web-app`), phone (`mobile-app`), computer (`desktop-app`), or on top of other websites (`browser-extension`)?

Pick by **where the value is delivered**, not by how it's built: a web app with an AI agent behind it is still a `web-app`; an MCP server that also has a settings page is still an `mcp-server`.

## Hybrid and sequenced products

- **One primary shape, always.** It decides the route. The primary shape is where the first paying customer gets the value.
- **Secondary shapes** are surfaces that support the primary (a `web-app` with an `mcp-server` so agents can use it; a `mobile-app` with a companion `website`). Each secondary shape adds its own acquisition surface and go-live steps, but not a second Define or Design phase. Add one only when the MVP genuinely ships it.
- **Sequenced products** start as one shape and become another: the classic AI pattern is `productized-service` first (deliver the outcome by hand with AI help, learn what customers pay for), then `web-app` once the process is proven. Record the sequence and its trigger ("move to web-app once 10 clients are paying"); the route follows the current shape until the trigger fires, then `define-product-shape` re-runs.

## Shape file format

Each `shapes/<slug>.md` has the same sections, so orchestrators can read just the part they need:

- **What it is** — one paragraph, plus where it lives (store, marketplace, host).
- **Live means** — the bar for "live" for this shape. Ship in 7 uses it as its bar.
- **First sale means** — what a first paying customer looks like. Sell in 30 uses it as its bar.
- **Define notes** — what the shape changes in persona and pricing (typical pricing models, who pays, marketplace fees).
- **Design route** — a table: each Design step, its mode for this shape, and how it adapts.
- **Develop route** — the same for each Develop step, plus what the PRD must cover and what "go live" means.
- **Distribute notes** — the shape's native channels (stores, marketplaces, registries, directories) and first-100-users moves.
- **Watch-outs** — the shape's specific traps (platform review, policy, distribution dependency).

Route modes (defined in `ROUTING.md`): **Full** · **Adapted** (the skill runs on the shape's medium — e.g. onboarding as install → first output instead of screens) · **Lite** (a reduced output — e.g. brand tokens only) · **Optional** · **Skip** · **Conditional** (written `Full / Skip`, with the condition beside it).
