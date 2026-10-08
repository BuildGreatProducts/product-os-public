---
name: develop-golive
description: >-
  Audits a built product and writes docs/DEPLOY.md: a plain-English, step-by-step go-live guide for
  its shape — deploy, store submission, marketplace publish, registry release, booking page, or
  storefront — each step marked for the founder, their coding agent, or both, ending in a smoke test
  as a real customer against the shape's Live-means bar. Use when the user says "how do I deploy
  this", "get this live", "publish my plugin", or "go live". Runs after develop-security-audit. Not
  for moving off a prompt-to-app platform — use develop-migrate.
---

# Develop: Go-Live Guide

This skill turns "it works on my machine" into "customers can use it." What "live" means depends on the product's shape — a deployed URL, an approved store listing, a published plugin, a package on a registry, a booking page taking payment, a storefront delivering a file. It reviews the actual product, works out everything standing between the current state and a live product, and writes a personalised, step-by-step guide the founder can follow without a technical background.

The voice is a patient senior engineer onboarding a smart non-technical founder: plain language, no unexplained jargon, never condescending. The founder is capable — they just haven't done this before.

## Step 1: Audit the codebase

Read the repository thoroughly before writing anything. Establish:

- **The shape and its bar** — the slug from `docs/DEFINE.md` → `## Product Shape` → `### Primary Shape` (no section → `web-app`, unless the codebase clearly says otherwise), plus any secondary shapes the product ships. Read the shape file (`productos/shapes/<slug>.md`, or `../../shapes/<slug>.md` from this folder): its `## Live means` is the bar this guide must reach, and `## Develop route` → `### Go live` names the path. Then read that shape's section of [references/go-live-by-shape.md](references/go-live-by-shape.md) — read it every run; it holds the shape's go-live checklist and dated platform facts.
- **What the product is and where it runs** — the hosts, stores, marketplaces, or registries it ships to. Detect the framework, backend, database, auth, and payment providers from the code and dependencies — don't ask the member things the code answers.
- **Configuration state** — environment variables used in code vs. what's documented (`.env.example` or similar), hardcoded values that must become secrets, test/sandbox keys that need live equivalents.
- **Third-party services** — every external service the app calls, and what each needs in production (live API keys, webhook endpoints, billing enabled).
- **Deploy readiness** — existing deploy or packaging config (e.g. `vercel.json`, `Dockerfile`, `eas.json`, an extension or plugin manifest, `package.json` publish fields), build scripts, whether the production build currently succeeds, test status.
- **Decisions already made** — if `docs/PRD.md` exists, its Infrastructure & Deployment and Cost Estimate sections chose the hosting and estimated the bill; follow them rather than re-deciding. With no PRD, take the **Default** from `productos/develop/guides/TECH-STACK-OPTIONS.md` — its Hosting & Deployment section for screen shapes, or the shape's own section (MCP servers, chat assistants, storefronts…) for the rest.
- **Security gate** — any shape that ships code customers run or reach needs `docs/SECURITY-AUDIT.md` first; a no-code `productized-service`, `digital-product`, or `website` needs it only where it has custom code or stores customer data. When it applies, read the file. If it doesn't exist, or its verdict is **Not safe to launch**, the guide's first phase is "run `develop-security-audit` and clear every Critical and High finding" (DEVELOP-CHECKLIST Step 8 comes before Step 9). Say so in the confirmation message.
- **Launch gaps** — things customers-facing products need that the code may lack: error tracking, analytics, legal pages (privacy policy, terms, refund policy), a custom domain, database backups, store or marketplace listing assets (`docs/APP-LISTING.md` or `docs/MARKETPLACE-LISTING.md` holds the copy).

Confirm the picture with the member in one short message (shape, stack, the services found, and the Live-means bar) plus any genuinely unanswerable questions — e.g. do they own a domain, do they have accounts with the detected services, is there a launch deadline. If `docs/SHIP-IN-7.md` or `docs/SELL-IN-30.md` is open **and its plan table names a go-live session** (Ship in 7 always does; Sell in 30 only on its one-deploy-away path), that session is the deadline: the guide's estimated total time must fit the sessions left, and if it can't, say so now and name what to cut (the custom domain and a second store or marketplace are the usual candidates) rather than letting the member discover it on the last day.

## Step 2: Write `docs/DEPLOY.md`

Write the guide to `docs/DEPLOY.md` (create the folder if needed). Structure:

**Header** — product name, detected stack in one plain-English sentence, estimated total time, and a legend:

- 🧑 **You** — needs your identity, accounts, payment details, or a decision. An agent can't (or shouldn't) do this for you.
- 🤖 **Agent** — paste the given prompt into your coding agent and it can do this in the codebase or via the command line.
- 🤝 **Together** — the agent prepares it, you click the final button or paste in a value.

**Phases, each with checkbox steps.** Adapt to what the audit found and to the shape's checklist in the reference — typical shape:

1. **Accounts and prerequisites** — the hosting platform, developer or seller accounts (stores, marketplaces, registries, storefronts), and each production service; choose the cheapest tier that works, with monthly cost and any one-off fees noted.
2. **Secrets and configuration** — create live API keys, set environment variables on the hosting platform, remove test keys. Never paste secrets into chat or commit them to code (or to a plugin, MCP, or extension manifest) — say this explicitly.
3. **Production services** — database in production mode, auth configured for the real domain, payments switched from test to live (including webhooks and a real test purchase), email/AI/storage services on live credentials.
4. **Ship it** — the shape's go-live path from the reference: deploy (screen and server shapes), store submission, marketplace publish, registry release, booking page, or storefront. Be honest where a review stands between submission and live — it takes days and may need fixes.
5. **Domain** — when the shape has one: buy/connect the domain, DNS setup, confirm HTTPS.
6. **Pre-launch verification** — a smoke test written as a customer journey through the shape's real front door: find it, install or sign up or book, reach the magic moment, pay for real and refund it. It passes only when the shape's Live-means bar is met.
7. **After launch** — error tracking, analytics, backups, listing or review responses, and where to look when something breaks.

**Every step must have:**

- A checkbox, a 🧑/🤖/🤝 marker, and a time estimate.
- Plain-language instructions. Explain every technical term inline on first use — e.g. *"DNS (the address book that points your domain name at your app's server)"*, *"environment variable (a setting stored outside your code, used for secrets like API keys)"*, *"webhook (a way for one service to automatically notify another when something happens, like a successful payment)"*.
- For 🤖 steps: a ready-to-paste prompt for the coding agent, in a quote block.
- For 🧑 steps: exactly where to click/go, what they'll be asked for, and any cost.
- A "**You'll know it worked when...**" line so the member can verify each step without guessing.

**Verify before delivering** — re-read `docs/DEPLOY.md`:

- [ ] Every step has a checkbox, a 🧑/🤖/🤝 marker, a time estimate, and a "You'll know it worked when…" line.
- [ ] Every 🤖 step has a ready-to-paste prompt; every 🧑 step says where to go, what they'll be asked for, and the cost.
- [ ] Every technical term is explained inline on first use.
- [ ] Secrets are never pasted into chat or committed — the guide says so explicitly, and every secret goes straight into the hosting platform's settings.
- [ ] The security gate is honored (a clean `docs/SECURITY-AUDIT.md`, or clearing it is the first phase), and audit blockers are Phase 0.
- [ ] The shape's go-live path from the reference is covered, and its dated platform facts are presented as dated, not timeless.
- [ ] The guide ends with the real-customer smoke test judged against the shape's Live-means bar, and the estimated total time fits any open challenge's go-live session.

## Step 3: Walk the member in

Don't just drop the file. Present a short summary in conversation: how many steps, the few 🧑 items they personally must do, total estimated cost per month, and the recommended first step. Offer to execute the first 🤖 step now.

## Rules

- Be honest about cost, time, and risk — store review delays, DNS propagation ("can take up to a day"), payment provider verification.
- Recommend one path, not a menu. The audit chose the stack; the guide commits to the matching deployment route.
- Never instruct the member to share secrets in chat; secrets go directly into the hosting platform's settings.
- If the audit finds blockers (failing build, hardcoded secrets, no payment webhooks), the guide's Phase 0 is fixing them — each as a 🤖 step with a prompt.
- The product isn't live until the smoke test passes as a real customer and the shape's Live-means bar is met.
