# Shape: Chat assistant

*Slug: `chat-assistant` · Family: AI-native*

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

An assistant people talk to in a chat surface they already use: a custom GPT, a Claude Project, or a bot in Slack, Discord, WhatsApp, Telegram, or Microsoft Teams — a coach, a support agent, a niche expert, a team helper. The conversation is the whole interface: the value arrives as replies, and the product is the assistant's knowledge, behaviour, and actions. There are two families. **Hosted-builder assistants** (custom GPTs, Claude Projects) need no code but can't be charged for directly and live on someone else's platform. **Bot assistants** (Slack, Discord, WhatsApp, Telegram, Teams, or an embedded web chat) are code the member runs: a backend that receives messages, calls a model, and replies — with real accounts and billing. Choose the family in the PRD; it decides most of the route.

## Live means

A stranger can start a conversation with the assistant from its public link, store listing, or bot handle — install the Slack/Discord/Teams app, message the WhatsApp/Telegram bot, open the GPT — and a fresh conversation reaches the magic moment on the production configuration, on the first try, with no member-only setup.

## First sale means

A real customer (warm network counts; the member's own test purchase doesn't) pays for access and keeps using the assistant on the paid plan: through the member's Stripe Checkout or Payment Link (unlocking the bot for their account or workspace), through the platform's own payments where it requires them (Discord's premium app subscriptions, Telegram Stars for digital goods), or as a paid setup for a client (then it may really be a `productized-service`). A free GPT that sends a user to a paid product counts only when that product's payment lands.

## Define notes

- **Persona:** name the chat surface they already spend the day in — the team in Slack, the community in Discord, the customer on WhatsApp — and the questions they keep asking. If they'd have to adopt a new chat app to use it, the shape is wrong.
- **Pricing models:** subscription per person (consumer coaches, expert assistants); per workspace or seat (Slack/Teams team assistants); per conversation or message volume (support bots, where message costs pass through); a setup fee plus monthly for an assistant built on a client's knowledge.
- **Who pays:** the individual by card, or the workspace admin for team bots. For business-messaging bots (WhatsApp), the business pays and its customers chat free.

### Fees — last reviewed October 2026 (re-verify before quoting)

- Custom GPTs can't be sold per user; OpenAI has run a usage-based builder payout programme in limited markets — check its current status before planning revenue on it. Claude Projects are shared within a Claude Team or Enterprise organisation, not sold publicly.
- WhatsApp Business Platform messages are billed by Meta per message, by category and country — check the current rate card.
- Telegram requires digital goods and services sold inside bots to be paid in Telegram Stars; Discord's premium app monetisation is available in supported regions with a platform revenue share. Check the current terms.

## Design route

| Step | Mode | How it adapts |
| --- | --- | --- |
| 1 — Identity | Full | The assistant's name, personality, and tone of voice *are* the product's interface. The name check includes the platform's bot or GPT name. |
| 2 — UX Writing | Adapted | `docs/COPY.md` covers the greeting, conversation starters, how it asks clarifying questions, refusals and out-of-scope replies, error and limit messages, slash commands, and the upgrade prompt — the assistant's voice rules, written to go into its system prompt. |
| 3 — Design System | Lite | Brand tokens for the avatar, landing page, and listing. Full only for an embedded web chat widget the member styles. |
| 4 — Design Prompts | Skip | No screens. Optional for an embedded web chat or an admin dashboard. |
| 5 — Magic Moment | Adapted | The first reply that's clearly better than asking a general chatbot — specific to the user's situation, using knowledge or actions only this assistant has. Named as the opening exchange. |
| 6 — Onboarding | Adapted | Install or open → greeting → two or three questions that collect the context the first great answer needs → magic moment. `docs/ONBOARDING.md` is a sample conversation script; no wireframe. Use `BONUS-Chat-Assistant-Onboarding-Best-Practice.md`. |
| 7 — Acquisition surface | Full | `design-marketplace-listing` for the platform's directory (GPT Store, Slack Marketplace, Discord App Directory, Microsoft Teams store; for Telegram and WhatsApp there is no official store — the listing is the bot profile and any community bot directory). Plus `design-landing-page` for pricing and checkout. |

## Develop route

| Step | Mode | How it adapts |
| --- | --- | --- |
| 0 — Migrate | Skip | Not applicable. (A hosted-builder assistant that outgrows its builder becomes a bot build — PRD & Roadmap, not Migrate.) |
| 1 — PRD & Roadmap | Adapted | The PRD centres on the conversation design, knowledge, and actions (below). For a hosted-builder assistant, the "build" is configuration and the roadmap is short. |
| 1b — Evals | Full | `develop-agent-evals` — conversation scenarios: typical questions, edge cases, out-of-scope requests, attempts to extract the system prompt or knowledge, and the magic-moment exchange, with pass criteria. |
| 2 — Verify setup | Full | Normally already done by `setup`; for a hosted-builder assistant the repo holds the system prompt, knowledge files, and evals under version control. |
| 3 — Build | Full | Bot assistants: `develop-build` for the backend, platform integration, billing, and memory. Hosted builders: write the instructions and knowledge files, configure actions, run the evals. |
| 4 — Build loop | Full | Every prompt or knowledge change re-runs the evals. |
| 5 — Code review | Full | For bot code changed outside the build skills; Skip for a configuration-only assistant. |
| 6 — Design changes | Skip | No UI. Optional for an embedded widget or dashboard. |
| 7 — Conversion review | Adapted | Listing / landing page → install or open → first exchange → free-limit message → upgrade checkout. Runs on the listing, landing page, and the upgrade conversation. |
| 8 — Security audit | Full | For bot assistants: webhook signature verification, per-user and per-workspace data isolation, secrets, rate limits, prompt injection, what conversation data is stored. For hosted builders: what the knowledge files and actions expose — assume the instructions can be extracted. |
| 9 — Go live | Adapted | Platform app publish or bot registration (below). |

### What the PRD must cover

- **Family and platforms:** hosted builder or bot; which chat platforms at launch.
- **Conversation design:** the system prompt's structure, persona, scope, and what it refuses; the magic-moment exchange as a script.
- **Knowledge:** the sources (files, a database, retrieval), how they're kept current, and what must never be quoted verbatim.
- **Actions:** tools or API calls the assistant can take, with confirmation rules for anything that changes data.
- **Memory and identity:** what's remembered per user or workspace, for how long, and how a user is identified on each platform.
- **Billing and limits:** free allowance, plan limits, how the bot checks entitlement, the upgrade link.
- **Moderation and handoff:** harmful-content handling, and when a human takes over (support bots).
- **The eval set:** from `docs/EVALS.md`.

### Go live

Bot assistants: backend deployed over HTTPS → platform app or bot registered (🧑 the member: Slack/Discord/Teams developer accounts, a Meta business account and verified number for WhatsApp, BotFather for Telegram) → webhooks pointed at production → billing live → install tested from a clean account → directory submission where one exists. Hosted builders: published with public visibility, actions pointed at production, listed in the GPT Store. `develop-golive` writes this as `docs/DEPLOY.md`.

#### Review and policy — last reviewed October 2026 (re-verify before quoting)

- Slack Marketplace and the Microsoft Teams store review apps before listing; Slack has tightened API limits and data-use terms for apps distributed outside its Marketplace — check the current rules before relying on message-history access.
- Meta's WhatsApp Business terms restrict general-purpose AI assistants (from early 2026 at the last review); a business-specific assistant serving that business's customers is the allowed pattern. Check the current policy before building a WhatsApp-first product.
- Discord requires verification for bots in many servers; the App Directory has its own listing review.

## Distribute notes

**Native channels:** the platform's directory (GPT Store, Slack Marketplace, Discord App Directory, Teams store), communities that already live on the platform (Discord servers, Slack communities, Telegram groups), the persona's professional communities, and short-form video of real exchanges.

**First users:**

1. Put the assistant in front of ten warm-network users in the chat app they already use, and read every transcript from the first week (with consent).
2. Offer it free to the admins of three communities or workspaces where the persona gathers, in exchange for feedback and a mention.
3. Post screenshots of real magic-moment exchanges (anonymised) as the core content.
4. Use a free GPT or public demo bot as the top of the funnel, linking to the paid bot.

**Activation and retention:** *activated* = a new user or workspace completes the magic-moment exchange (the first reply that used their context or the assistant's private knowledge or actions). *Returned* = they start a new conversation on at least two days in week 2. For team bots, also track how many people in the workspace use it.

## Watch-outs

- **No moat in the prompt.** Instructions in a GPT or bot can be extracted and copied. The value has to be knowledge, actions, data, or distribution the member owns.
- **Building on a builder you can't charge through.** A custom GPT or Claude Project is a demo or a delivery format, not a business on its own.
- **Platform policy risk.** Chat platforms change API terms, rate limits, and AI policies; WhatsApp and Slack both did recently. Keep users reachable outside the platform.
- **Message costs.** Model calls plus per-message platform fees can exceed revenue on a flat plan. Price against cost per active user.
- **Confidently wrong.** An assistant answering outside its knowledge does more damage than one that says it doesn't know. Out-of-scope scenarios belong in the evals.
