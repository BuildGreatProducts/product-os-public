# Tech Stack Options

Default comparison data for ProductOS's Develop-phase tech stack questions. Use these as a baseline and adapt recommendations based on the specific product’s needs. The comparison format and pros/cons should be adjusted to reflect how each option fits the founder’s particular product.

## Contents

- [Frontend Frameworks](#frontend-frameworks)
- [Backend](#backend)
- [Database](#database)
- [Auth Providers](#auth-providers)
- [Payment Providers](#payment-providers)
- [Analytics](#analytics)
- [Transactional Email](#transactional-email)
- [Error Tracking & Monitoring](#error-tracking--monitoring)
- [Hosting & Deployment](#hosting--deployment)
- [Non-App Shapes](#non-app-shapes)
- [Agent Skills & Plugins](#agent-skills--plugins)
- [MCP Servers](#mcp-servers)
- [Chat Assistants](#chat-assistants)
- [Developer Tools](#developer-tools)
- [Websites](#websites)
- [Digital Product Storefronts](#digital-product-storefronts)
- [Productized-Service Tooling](#productized-service-tooling)

-----

## Frontend Frameworks

### Web Apps

**Next.js** — React framework with server-side rendering, file-based routing, and excellent deployment options.

- ✓ Largest React ecosystem, huge community, extensive documentation
- ✓ App Router with server components for performance
- ✓ Excellent integration with Vercel, Convex, Clerk, and most services
- ✓ Best-supported by AI coding tools (most training data)
- ✗ Can be complex — many ways to do things (server vs client components)
- ✗ Opinionated about project structure
- **Best for:** Most web apps. Default recommendation unless there’s a specific reason not to.

**Remix** — Full-stack React framework focused on web standards and progressive enhancement.

- ✓ Excellent form handling and data loading patterns
- ✓ Progressive enhancement — works without JavaScript
- ✓ Simpler mental model than Next.js (loaders + actions)
- ✗ Smaller ecosystem than Next.js
- ✗ Less AI coding tool familiarity
- **Best for:** Form-heavy apps, content-heavy sites, apps that need to work without JS.

**SvelteKit** — Svelte framework with file-based routing and server-side rendering.

- ✓ Significantly less boilerplate than React
- ✓ Excellent performance — smaller bundle sizes
- ✓ Built-in state management (no Redux/Zustand needed)
- ✗ Smaller ecosystem and community than React
- ✗ Fewer component libraries available
- ✗ Less AI coding tool support
- **Best for:** Performance-critical apps, developers who prefer less boilerplate.

### Mobile Apps

**Expo / React Native** — Cross-platform mobile framework with managed workflow.

- ✓ Write once, run on iOS and Android
- ✓ Expo managed workflow eliminates native build complexity
- ✓ React knowledge transfers directly
- ✓ Over-the-air updates
- ✗ Performance can lag behind native for graphics-heavy apps
- ✗ Some native APIs require ejecting from managed workflow
- **Best for:** Most mobile apps. Default recommendation for mobile.

**Flutter** — Google's cross-platform UI toolkit using Dart.

- ✓ Excellent performance — compiles to native
- ✓ Beautiful, customizable UI components
- ✓ Single codebase for iOS, Android, web, desktop
- ✗ Dart is a separate language to learn
- ✗ Less ecosystem integration with JS/TS backends
- ✗ Less AI coding tool support than React Native
- **Best for:** Apps needing pixel-perfect custom UI or very high performance.

### Desktop Apps

**Electron** — Build cross-platform desktop apps with Chromium and Node.js. Powers VS Code, Slack, Discord, Figma, and Notion.

- ✓ Most mature desktop framework — battle-tested at massive scale
- ✓ Full web technology stack (HTML, CSS, JS/TS) — no new language to learn
- ✓ Largest ecosystem of plugins, tools, and community resources
- ✓ Excellent AI coding tool support (most training data)
- ✗ Heavy memory footprint — each app bundles its own Chromium instance
- ✗ Large bundle sizes (100MB+ minimum)
- ✗ Can feel non-native on macOS — requires extra work to match platform conventions
- **Best for:** Most desktop apps. Default recommendation for desktop. Especially strong when the team already knows web technologies.

**Tauri** — Lightweight desktop framework using the OS's native webview and a Rust backend.

- ✓ Dramatically smaller bundles than Electron (often 5-10MB vs 100MB+)
- ✓ Lower memory usage — uses the OS webview instead of bundling Chromium
- ✓ Rust backend for performance-critical operations and system access
- ✓ Strong security model — fine-grained permission system for system APIs
- ✗ Younger ecosystem — fewer community resources and plugins than Electron
- ✗ Rust knowledge needed for backend plugins and system integrations
- ✗ OS webview inconsistencies can cause cross-platform rendering differences
- **Best for:** Desktop apps where bundle size and memory matter, or when deep system integration is needed. Good for developers comfortable with Rust.

**Flutter (Desktop)** — The same Flutter framework listed under Mobile, with support for macOS, Windows, and Linux.

- ✓ Single codebase across mobile, web, and desktop — true cross-platform
- ✓ Compiles to native — good performance without a webview
- ✓ Consistent UI across all platforms
- ✗ Desktop support is less mature than mobile — some platform APIs are missing
- ✗ Dart ecosystem is smaller than JS/TS for desktop-specific needs
- ✗ Apps don't follow native platform UI conventions by default
- **Best for:** Projects that need a single codebase across mobile AND desktop. Not recommended for desktop-only apps — Electron or Tauri are better choices there.

-----

## Backend

**Convex** — Reactive backend-as-a-service with built-in database, real-time sync, and TypeScript-native functions.

- ✓ Real-time data sync out of the box — no WebSocket setup
- ✓ Zero backend boilerplate — define functions, they just work
- ✓ Built-in auth, file storage, scheduling, search
- ✓ TypeScript end-to-end with full type safety
- ✓ Excellent DX for solo developers — fast iteration
- ✓ ACID transactions on the database
- ✗ Newer ecosystem — fewer community resources
- ✗ Vendor dependency — data lives on Convex Cloud
- ✗ Different mental model from traditional REST APIs
- **Best for:** Most products, especially real-time apps, solo developers, MVPs. Default recommendation.

**Supabase** — Open-source Firebase alternative built on PostgreSQL.

- ✓ PostgreSQL under the hood — full SQL power, relational data
- ✓ Real-time subscriptions, auth, storage, edge functions
- ✓ Open source — can self-host if needed
- ✓ Large and growing community
- ✗ More setup than Convex — manual schema migrations
- ✗ Real-time requires explicit subscription setup
- ✗ Edge functions are less integrated than Convex functions
- **Best for:** Products with complex relational data, teams that want SQL and open-source.

**Node.js + Express + PostgreSQL** — Traditional server setup with full control.

- ✓ Maximum flexibility — build exactly what you need
- ✓ Largest ecosystem of packages and middleware
- ✓ Full control over infrastructure and hosting
- ✗ Significant boilerplate — auth, validation, error handling, CORS, etc.
- ✗ You manage everything: database migrations, deployment, scaling
- ✗ Slower to iterate as a solo developer
- **Best for:** Experienced backend developers who want full control, or products with unusual requirements.

-----

## Database

**Convex Database** — Document-relational database built into the Convex platform.

- ✓ Automatic reactive queries — UI updates when data changes
- ✓ ACID transactions with optimistic concurrency
- ✓ Automatic indexing — define indexes in schema, they just work
- ✓ TypeScript schema validation built-in
- ✗ Only available with Convex backend
- ✗ Document-oriented — different from SQL thinking
- **Best for:** Any product using Convex backend. Use this — it’s part of the package.

**PostgreSQL** — The gold-standard open-source relational database.

- ✓ Rock-solid reliability and ACID compliance
- ✓ Full SQL power — complex queries, joins, aggregations
- ✓ Excellent for relational data with complex relationships
- ✓ Massive ecosystem of tools and extensions
- ✗ Requires migrations for schema changes
- ✗ No built-in real-time — need separate pub/sub
- **Best for:** Products with complex relational data. Pairs with Supabase or traditional backends.

**Supabase Database (PostgreSQL)** — Managed PostgreSQL via the Supabase platform with a dashboard, auto-generated APIs, and real-time subscriptions.

- ✓ Full PostgreSQL — complex queries, joins, extensions, relational power
- ✓ Auto-generated REST and GraphQL APIs from your schema
- ✓ Real-time subscriptions built in
- ✓ Row Level Security for fine-grained access control
- ✓ Dashboard with table editor — visual schema management
- ✗ Only makes sense with Supabase backend
- ✗ Migrations still needed for production schema changes
- **Best for:** Supabase backends — use this, it’s part of the package. Excellent for relational data.

**None (local-only / no database)** — The app stores data on-device only (AsyncStorage, SQLite, UserDefaults, local files).

- ✓ Zero infrastructure — no backend costs, no latency
- ✓ Works offline by default
- ✓ Simpler architecture — no sync, no API calls
- ✗ Data is lost if the user deletes the app (unless backed up)
- ✗ No cross-device sync
- ✗ No server-side logic or shared data
- **Best for:** Mobile apps that are primarily tools (calculators, trackers, utilities), offline-first apps, or MVPs that don’t need shared data. Consider adding a backend later if the product grows.

-----

## Auth Providers

**Convex Auth** — Native auth built into the Convex platform.

- ✓ Zero-config integration with Convex backend
- ✓ Supports email/password, OAuth providers, magic links
- ✓ User data lives in Convex — no external service calls
- ✗ Only works with Convex backend
- ✗ Fewer pre-built UI components than Clerk
- **Best for:** Convex backends where simplicity is priority.

**Clerk** — Drop-in auth with pre-built UI components.

- ✓ Beautiful, pre-built sign-in/sign-up components
- ✓ Social login, MFA, organization management out of the box
- ✓ Excellent React/Next.js integration
- ✓ Generous free tier (10,000 MAUs)
- ✗ External service dependency
- ✗ Monthly cost at scale
- **Best for:** Products that want polished auth UI fast. Works with any backend.

**Auth.js (NextAuth)** — Open-source auth for Next.js.

- ✓ Open source — no vendor dependency
- ✓ Supports many OAuth providers
- ✓ Database adapters for most databases
- ✗ More setup and configuration than Clerk
- ✗ Less polished UI — you build your own forms
- ✗ Session management can be tricky
- **Best for:** Developers who want open-source auth with full control.

**Supabase Auth** — Auth built into the Supabase platform.

- ✓ Integrated with Supabase — Row Level Security uses auth
- ✓ Email/password, magic links, OAuth providers
- ✓ Free with Supabase
- ✗ Only makes sense with Supabase backend
- ✗ Less polished than Clerk’s UI components
- **Best for:** Supabase backends — use this, it’s part of the package.

**None (no auth needed)** — The app doesn’t require user accounts or sign-in.

- ✓ Simpler UX — no sign-up friction, instant access
- ✓ Less infrastructure to manage
- ✓ Better for tools, utilities, and single-player experiences
- ✗ No personalization or saved preferences across devices
- ✗ Can’t gate features behind subscription tiers (without device-level checks)
- **Best for:** Mobile utility apps, offline tools, calculators, single-player experiences, or MVPs testing core value before adding accounts. Can always add auth later.

-----

## Payment Providers

### Web / SaaS Payments

**Stripe Managed Payments** — Stripe's merchant of record service ([stripe.com/managed-payments](https://stripe.com/gb/managed-payments)). Stripe becomes the merchant of record for your digital sales, handling tax calculation, collection, and remittance in 80+ countries, plus fraud prevention, dispute handling, and customer support.

- ✓ Merchant of record — tax compliance shifts to Stripe entirely (no registrations, filings, or audits on your end)
- ✓ Full Stripe platform underneath — supports virtually any payment model
- ✓ Largest ecosystem — extensive documentation, libraries, integrations
- ✓ One-line enablement on Stripe Checkout (`managed_payments: { enabled: true }`)
- ✓ Fraud prevention, dispute handling, and 24/7 customer support included
- ✓ Transaction-level control — apply it to all sales or only specific markets/products
- ✓ Best-supported by AI coding tools (most training data and examples)
- ✗ Higher per-transaction fees than standard Stripe processing (Stripe takes on the tax liability)
- ✗ Stripe's underlying concepts (Products, Prices, Subscriptions) still need learning
- ✗ Digital goods only — not for physical products
- **Best for:** Most web/SaaS products. Default recommendation for web — managed tax compliance from day one on the most battle-tested platform.

**Polar** — Developer-first payment platform for SaaS and digital products, also acting as merchant of record.

- ✓ Built specifically for developers and SaaS products
- ✓ Merchant of record — global tax compliance handled entirely for you
- ✓ Handles subscriptions, one-time payments, and licensing
- ✓ Excellent API and webhook support
- ✓ Generous free tier — no monthly fee, only transaction fees
- ✓ Built-in customer portal
- ✗ Newer platform — smaller community and ecosystem than Stripe
- ✗ Less suitable for physical goods or complex billing
- **Best for:** Solo founders who want the simplest possible developer-first billing setup. Strong secondary choice when the full Stripe platform isn't needed.

**Lemon Squeezy** — Merchant of record for digital products.

- ✓ Handles global tax compliance — they’re the merchant of record
- ✓ Simple setup for subscriptions and one-time payments
- ✓ Built-in affiliate program
- ✓ No need to register for tax in different jurisdictions
- ✗ Higher fees than Stripe (they handle tax liability)
- ✗ Less flexible than Stripe for complex billing
- ✗ Smaller ecosystem
- **Best for:** Solo founders selling internationally who don’t want to deal with tax compliance.

### Mobile In-App Payments

For mobile apps distributed through the App Store or Google Play, in-app purchases (IAP) are often required by platform policies. These tools manage subscriptions and purchases through the native store billing systems.

**RevenueCat** — Cross-platform in-app subscription management.

- ✓ Abstracts Apple and Google billing APIs into one SDK
- ✓ Handles receipt validation, entitlements, and subscription status server-side
- ✓ Excellent dashboard with analytics, cohorts, and churn tracking
- ✓ Generous free tier — free up to $2,500/month in tracked revenue
- ✓ Works with React Native/Expo, Flutter, Swift, Kotlin
- ✓ Webhook support for backend integration
- ✗ Another dependency and point of failure in the payment flow
- ✗ Paid tiers add up as revenue grows (1% of tracked revenue after free tier)
- **Best for:** Any mobile app with subscriptions or one-time IAP. Default recommendation for mobile payments.

**Superwall** — Paywall A/B testing and management platform.

- ✓ Build and deploy paywalls remotely — no app update needed to change pricing UI
- ✓ Built-in A/B testing for paywall designs, pricing, and placement
- ✓ Pre-built paywall templates that convert well
- ✓ Analytics on conversion, trial starts, and revenue per paywall
- ✓ Works with RevenueCat or handles purchases directly via StoreKit/Billing
- ✗ Focused on paywall presentation — not a full subscription backend (pair with RevenueCat for that)
- ✗ Adds SDK overhead to your app
- ✗ Free tier is limited — paid plans required for A/B testing
- **Best for:** Mobile apps that want to optimize subscription conversion through paywall experimentation. Best paired with RevenueCat for the full billing stack.

**None (no payments needed)** — The app is free with no monetization, or monetization will be added later.

- ✓ Ship faster — no payment integration complexity
- ✓ No App Store commission considerations
- ✓ Focus entirely on core product value
- ✗ No revenue from day one
- ✗ Adding payments later requires an app update and review
- **Best for:** Free utility apps, apps exploring product-market fit before monetizing, or apps monetized through other channels (ads, enterprise contracts, etc.).

-----

## Analytics

Product analytics tells you whether users reach the magic moment, where they drop off, and which features get used. Instrument this from day one — retrofitting events after launch means flying blind through the most important early weeks.

**PostHog** — All-in-one product analytics, session replay, feature flags, and A/B testing.

- ✓ Product analytics, funnels, session replay, feature flags, and experiments in one platform
- ✓ Generous free tier (1M events/month) — enough for most early-stage products
- ✓ Open source, can self-host if data residency matters
- ✓ Autocapture — start getting data before you've defined every event
- ✓ Excellent for tracking activation and the magic moment funnel
- ✗ Broad surface area — can feel heavy if you only want simple analytics
- ✗ Self-hosting is real infrastructure work — most should use cloud
- **Best for:** Most products. Default recommendation — the funnel + replay + flags combination is ideal for understanding and improving activation.

**Mixpanel** — Event-based product analytics focused on funnels, retention, and cohorts.

- ✓ Best-in-class funnel and retention analysis
- ✓ Clean, fast UI that non-technical founders navigate easily
- ✓ Strong cohort and segmentation tools
- ✓ Free tier up to 1M events/month
- ✗ Analytics only — no session replay or feature flags (need separate tools)
- ✗ Event taxonomy needs upfront planning to stay useful
- **Best for:** Teams that want focused, polished analytics and don't need replay or flags. Strong choice when reporting clarity matters most.

-----

## Transactional Email

Transactional email covers the messages your app sends automatically — sign-up confirmations, password resets, receipts, notifications. Almost every product with auth or payments needs this. (Auth providers like Clerk and Supabase send their own auth emails, but you'll still want this for product and billing emails.)

**Resend** — Developer-first email API built for transactional and product email.

- ✓ Built for developers — clean API, excellent DX, fast setup
- ✓ Write emails as React components with React Email
- ✓ Generous free tier (3,000 emails/month, 100/day)
- ✓ Great deliverability and simple domain verification
- ✓ Pairs naturally with Next.js/React stacks
- ✗ Newer platform — smaller feature set than legacy providers
- ✗ Not built for marketing campaigns or audience management
- **Best for:** Most products. Default recommendation for transactional email, especially on React/Next.js stacks.

**Loops** — Email platform combining transactional and lifecycle/marketing email.

- ✓ Transactional email AND marketing/lifecycle campaigns in one tool
- ✓ Visual editor — non-technical founders can write and edit emails
- ✓ Built-in drip campaigns and audience segmentation
- ✓ Simple API for transactional sends
- ✗ Less developer-focused than Resend for purely transactional needs
- ✗ Marketing features add surface area you may not need at MVP
- **Best for:** Founders who want transactional email plus onboarding drips and newsletters from one tool, without wiring up a separate marketing platform.

-----

## Error Tracking & Monitoring

Error tracking catches the bugs your users hit but never report. Without it, you only hear about crashes when someone complains — and most just churn silently. This is a launch essential, not a nice-to-have.

**Sentry** — Error tracking and performance monitoring across frontend, backend, and mobile.

- ✓ Captures errors with full stack traces, breadcrumbs, and the user actions that led to them
- ✓ Works across web, mobile (React Native, Flutter, Swift, Kotlin), and backend
- ✓ Performance monitoring and (with session replay) the ability to watch what the user saw when it broke
- ✓ Generous free tier — enough for early-stage error volume
- ✓ Alerts to Slack/email so you hear about issues before users complain
- ✗ Source map and SDK configuration takes some initial setup
- ✗ Event volume on noisy apps can push you off the free tier
- **Best for:** Every production app. Default recommendation — set it up before launch so the first real users' errors are visible.

-----

## Hosting & Deployment

Hosting is where the built app runs and where customers reach it. Pick the platform that matches the frontend and backend choices above; most MVPs need exactly one. Free tiers and limits change — check the provider's current pricing page before quoting a monthly cost.

**Vercel** — Managed hosting for web frontends and serverless functions, made by the Next.js team.

- ✓ Deploys from GitHub on every push, with a preview URL per branch
- ✓ First-class Next.js support; zero-config for most React, Svelte, and Astro apps
- ✓ Environment variables, custom domains, and SSL in one dashboard
- ✗ Serverless functions have execution time limits — not for long-running jobs or always-on workers
- ✗ Commercial use requires the paid plan
- **Best for:** Most web apps. Default recommendation, especially on Next.js with a managed backend (Supabase, Convex, Firebase).

**Netlify** — Managed hosting for static sites and web frontends with serverless functions.

- ✓ Same Git-push deploys and preview URLs as Vercel
- ✓ Strong for static and content-heavy sites (Astro, plain HTML)
- ✗ Less tightly integrated with Next.js than Vercel
- **Best for:** Static or content-led products, or founders who already use it.

**Railway** (or **Render**) — Managed hosting for always-on servers, workers, and databases.

- ✓ Runs a long-lived Node/Python/Go server, background workers, and cron jobs
- ✓ Can host Postgres or Redis next to the app
- ✗ More to configure than Vercel; you own the server process
- **Best for:** Products with a custom backend (Express, FastAPI, Rails) or work that outlives a serverless request — queues, scheduled jobs, websockets.

**Expo EAS + the app stores** — Build and submission pipeline for React Native/Expo apps.

- ✓ Cloud builds for iOS and Android without a local Xcode or Android Studio setup
- ✓ Submits builds to App Store Connect and Google Play; over-the-air updates for JS changes
- ✗ App Store review adds days to every release; Apple and Google developer accounts are required
- **Best for:** Every Expo mobile app. Pair it with the backend's own hosting (Supabase, Convex, Firebase are already hosted).

**Default:** a web app on a managed backend → **Vercel**. A custom server or background workers → **Railway**. A mobile app → **Expo EAS**, with the backend where it already lives.

-----

## Non-App Shapes

The sections above cover the screen shapes (`web-app`, `mobile-app`, `desktop-app`, `browser-extension`). Every other shape picks its stack from its own section below — the layers differ, so the interview asks about these instead of frontend, backend, and database. A shape that also runs code on a server (a remote MCP server, a bot backend, a paid API) takes its backend, database, analytics, and error tracking from the sections above too.

Each section ends with dated platform facts. Platforms, fees, and policies in these markets change monthly — re-verify any fact before quoting it to the member or putting it in a PRD.

-----

## Agent Skills & Plugins

For `agent-skill` and `agent-plugin`. The layers: the skill format, the plugin packaging per host, and distribution.

- **Agent Skills format (SKILL.md folders)** — a folder with a `SKILL.md` (YAML frontmatter `name` + `description`, then instructions) plus optional references, scripts, and assets. Write every skill in this format; it is the portable unit across hosts.
- **Host plugin packaging** — a plugin bundles skills with commands, subagents, hooks, and MCP servers behind a manifest. Each host has its own manifest folder (e.g. `.claude-plugin/`, `.codex-plugin/`, `.cursor-plugin/`); one repo can carry several, so one codebase reaches several hosts. ProductOS itself is packaged this way.
- **Distribution** — a plugin marketplace (a manifest in a Git repo that customers add once, then install from and update through), a host's official directory, or a direct download (zip). Paid products usually gate a private repo or deliver a license, since marketplaces rarely handle payment.

**Default:** write skills in the SKILL.md format; package them as a plugin with a manifest for each host the persona uses; distribute through a marketplace in a GitHub repo (private and access-granted on purchase for a paid product); submit to the hosts' official directories once it has users.

#### Platform facts — last reviewed October 2026 — re-verify before quoting

- The SKILL.md format began as Anthropic's Agent Skills and was published as an open standard; Claude's apps, Claude Code, and the API support it, and other coding agents (Codex and Cursor among them) read the same format. Check each target host's docs for its current skill and plugin support.
- Claude Code installs plugins from marketplaces defined by `.claude-plugin/marketplace.json` in a Git repository; a plugin's own manifest is `.claude-plugin/plugin.json`.
- Host marketplaces and directories have their own review and listing rules — check them before promising a launch date.

-----

## MCP Servers

For `mcp-server`. The layers: SDK, transport, hosting, auth, and distribution.

- **Official TypeScript SDK** — the most widely used SDK, with examples for every transport. Best for most servers, and for remote servers on JavaScript hosts.
- **Official Python SDK (with FastMCP)** — decorator-style tool definitions, fast to write. Best when the upstream system or the member's code is Python.
- **Transport** — **stdio** for a local server the host launches on the user's machine (needs local files, local apps, or local credentials); **Streamable HTTP** for a remote server customers connect to by URL (no install, easier to charge for, works in web and mobile clients).
- **Hosting (remote)** — Cloudflare Workers (MCP-specific tooling, OAuth helper libraries) or Vercel (fits alongside a Next.js app); Railway for long-running work.
- **Auth (remote)** — OAuth, per the MCP authorization spec, so each user connects their own account; an API key in a header is simpler but works in fewer clients.

**Default:** a remote server on the TypeScript SDK over Streamable HTTP, hosted on Cloudflare Workers or Vercel, with OAuth. Choose a local stdio server, published as an npm or PyPI package, only when it needs the user's machine.

#### Platform facts — last reviewed October 2026 — re-verify before quoting

- Current spec transports are stdio and Streamable HTTP; the older HTTP+SSE transport is deprecated.
- An official MCP Registry lists public servers; hosts also run their own connector directories with separate submission and review (e.g. Claude's connectors directory). Desktop hosts may support one-click packaged installs (e.g. MCP bundles for Claude Desktop).
- Client support for remote OAuth, resources, and prompts varies by host — test in every host the PRD names.

-----

## Chat Assistants

For `chat-assistant`. The layers: platform, model, backend, knowledge, and payments.

- **Custom GPT (ChatGPT)** — no code, built in the GPT editor with instructions, knowledge files, and actions (OpenAPI). Best for prototyping the conversation in days; weak on billing, analytics, and owning the customer.
- **Claude Project** — instructions plus knowledge inside Claude. Best for internal or team assistants; not a public product surface.
- **Slack app** — a bot in the customer's workspace, built with Slack's Bolt SDK on your own backend. Best for B2B assistants used at work.
- **Telegram or Discord bot** — your own backend behind the platform's bot API. Best for consumer and community assistants.
- **WhatsApp (Business Platform)** — the widest consumer reach in many countries, with business verification and per-message pricing. Best for a business-specific assistant (bookings, support) in WhatsApp-first markets.

**Default:** a bot on the platform the persona already uses every day — Slack for work, Telegram for consumers — backed by your own server calling the model API, so you own the users, the billing, and the logs. Prototype the conversation as a Custom GPT or Claude Project first if the member wants to test it before building.

#### Platform facts — last reviewed October 2026 — re-verify before quoting

- Custom GPTs and Claude Projects can't take payment from users directly; a paid assistant there needs an external checkout and access control.
- WhatsApp's business terms restrict general-purpose AI assistants on the Business Platform; a business-specific assistant is the safe pattern. Check the current policy before choosing WhatsApp.
- Slack Marketplace, Discord's App Directory, and Telegram each have their own listing, review, and monetization rules (Telegram supports in-bot payments for digital goods through its own currency).
- ChatGPT also supports apps built on MCP — a route for an assistant that is really an `mcp-server` with a UI.

-----

## Developer Tools

For `developer-tool`. The layers: language and registry, release pipeline, docs, API keys and billing.

- **npm** — JavaScript and TypeScript SDKs and CLIs (run with `npx`). Default for JS/TS.
- **PyPI** — Python SDKs and CLIs (run with `pipx` or `uvx`). Default when the users write Python.
- **Homebrew tap** — a second install path for a CLI aimed at macOS developers. Add after launch.
- **Release pipeline** — GitHub Actions publishing on a version tag, using the registry's trusted publishing (no long-lived tokens), with a changelog per release.
- **Docs** — Mintlify (hosted, generates API reference from OpenAPI, fast to polish) or Docusaurus (open source, self-hosted).
- **API keys and billing (paid APIs)** — keys issued and checked by your backend (or a key service such as Unkey); usage metered into Stripe's usage-based billing.

**Default:** TypeScript published to npm (PyPI if the users are Python developers), released from GitHub Actions with trusted publishing, docs on Mintlify, and Stripe usage-based billing for a paid API.

#### Platform facts — last reviewed October 2026 — re-verify before quoting

- npm and PyPI both support trusted publishing from CI and encourage or require two-factor auth for publishers; check current requirements before the first release.
- Package names are first-come — reserve the name in each registry early.

-----

## Websites

For `website`. The layers: builder or framework, content source, hosting, and memberships if any.

- **Astro** — a content-first framework a coding agent builds well; content in Markdown or JSON in the repo, fast static pages, good SEO defaults. Best for directories, resource libraries, and content sites the member builds with their agent.
- **Next.js** — when the site needs app-like features (accounts, search over a database, submissions).
- **Framer or Webflow** — visual builders with a built-in CMS. Best when the member wants to design and edit without code.
- **Ghost** — publishing with newsletters and paid memberships built in. Best when the newsletter is the product.
- **Community platforms** (Circle, Skool, Discourse) — when the community is the product and the site is its front door.
- **Headless CMS** (Sanity, or a Git-based CMS) — add one to Astro or Next.js when non-developers edit content often.

**Default:** Astro with content in the repo, hosted on Netlify or Vercel; Ghost instead when the site is a newsletter with paid memberships.

#### Platform facts — last reviewed October 2026 — re-verify before quoting

- Builder and community-platform plans change often, and custom domains, CMS item limits, and member features sit on paid tiers — check current pricing before quoting a monthly cost.

-----

## Digital Product Storefronts

For `digital-product`. The layers: where it's made, where it's sold, how it's delivered.

- **Gumroad** — a storefront, checkout, file delivery, and updates to past buyers in minutes; some marketplace discovery. Best for a first digital product.
- **Lemon Squeezy or Polar** — merchant-of-record checkouts with license keys and APIs. Best for software-like products (plugins, code templates) or developer audiences.
- **Stripe Payment Links** — when the member already has Stripe (with Managed Payments for tax); delivery needs its own step (an automation emailing the file).
- **Marketplaces** (Etsy, Notion's template gallery, Figma and Framer communities) — discovery inside an existing audience, in exchange for fees and less control. Best as a second channel.
- **Course platforms** (Podia, Teachable, Kajabi) — hosted lessons, drip, and student accounts. Best when the product is a course.

**Default:** Gumroad for the storefront and delivery; Lemon Squeezy or Polar when the product needs license keys; a course platform when it's a course.

#### Platform facts — last reviewed October 2026 — re-verify before quoting

- Check whether each storefront acts as merchant of record (collecting and remitting sales tax and VAT) and what it charges per sale — both differ by platform and change.
- Marketplace fees, payout schedules, and listing rules vary widely; read the current seller terms before listing.

-----

## Productized-Service Tooling

For `productized-service`. The layers: booking, payments, intake, client records, delivery automation, and the AI tools the work runs on.

- **Booking** — Cal.com (open source, can take payment at booking) or Calendly (most familiar to clients).
- **Payments** — Stripe Payment Links or Checkout for fixed-price packages and subscriptions; Stripe Invoicing for deposits and custom quotes.
- **Intake** — Tally (fast to build, conditional logic) or Typeform; the form collects everything the SOP needs before work starts.
- **Client records** — a Notion or Airtable board (one row per client and order, with status) until volume justifies a CRM such as Attio or HubSpot.
- **Delivery automation** — Zapier (easiest), Make (more control over complex flows), or n8n (self-hostable, code-friendly) to connect intake → records → AI steps → delivery messages.
- **AI tools** — the SOP's prompts and templates live in a Claude Project or skills, versioned in the repo with the rest of the SOP.

**Default:** Cal.com + Stripe Payment Links + Tally + a Notion client board + Zapier, with the SOP's prompts in the repo.

#### Platform facts — last reviewed October 2026 — re-verify before quoting

- Free tiers on booking, form, and automation tools cap usage (bookings, responses, tasks per month) and change often — check limits against the capacity in the PRD.
