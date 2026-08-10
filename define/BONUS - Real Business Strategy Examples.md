# BONUS - Real Business Strategy Examples

Five filled-in canvases across real software businesses. Use them as reference when working through your own framework. Figures are drawn from public reporting and founder interviews where available; exact internals (margins, North Star targets) are reasonable estimates marked with \~.

---

## Example 1: Loom (B2B SaaS, acquired by Atlassian for \~$975M in 2023)

Async video messaging for distributed teams — screen, cam, and voice in one click.

| Component | Decision |
| --- | --- |
| Revenue Model | Recurring SaaS subscription, per-creator. Free tier seeds the team; paid converts the workspace once usage habits form. |
| Pricing Ladder | Free (25 videos/creator) / Business at $15 per creator/month ($12.50 annual) / Business + AI at \~$20 / Enterprise (custom). Business is the engineered default — unlimited recording, transcription, HD, and password-protected links. |
| Cost & Margin | Variable: video storage (cloud object storage) plus AI transcription per minute uploaded. Video-heavy SaaS typically lands in the 70–80% gross margin band; storage caps on lower tiers protect the unit economics. |
| Unfair Advantage | Switching costs — every team builds an internal library of hundreds of recorded explainers that don't migrate. Slack, Notion, Jira, and GitHub embeds make Loom load-bearing in daily workflows. |
| North Star | Weekly active creators per workspace. Workspaces with multiple creators in week one churn at a fraction of single-recorder accounts — the metric tracks team adoption, which is what makes the per-seat model expand. |

---

## Example 2: MacWhisper (Mac App, indie, by Jordi Bruin / Good Snooze)

Native macOS transcription app built on OpenAI's open-source Whisper models, running locally on the user's Mac.

| Component | Decision |
| --- | --- |
| Revenue Model | One-time license purchase, sold through Gumroad. Free version handles small Whisper models; Pro unlocks Large-v3, batch processing, longer files, and editor features. Optional API/BYOK for cloud-only features. |
| Pricing Ladder | Free / Pro at \~$69 / Pro+ at \~$149 one-time, with a discounted upgrade path. No subscription on the core product. Refunds handled inside Gumroad's window. |
| Cost & Margin | Near-zero variable cost — transcription runs on the user's Mac, so there's no per-minute API spend on the books. Fixed costs: Apple Developer Program, Gumroad fees (\~10% incl. processing), occasional contract work. Margin \~90%. |
| Unfair Advantage | Speed of shipping — Jordi shipped within days of Whisper's open-source release and has compounded a multi-year head start with native macOS polish, Apple Silicon optimization, and a steady cadence of model updates that Electron competitors can't match. |
| North Star | Weekly licenses sold. Indie Mac apps live and die on launch surges and steady distribution from Hacker News, podcaster mentions, and word-of-mouth in journalist and academic circles. |

---

## Example 3: FluentBooking (WordPress Plugin LTD, WPManageNinja)

Native WordPress appointment booking plugin from a portfolio shop, launched on AppSumo with a lifetime deal before transitioning to annual licensing.

| Component | Decision |
| --- | --- |
| Revenue Model | AppSumo LTD launch on day one, then annual license renewals for premium support and updates after the initial window. Cross-sells into sibling plugins drive the long tail. |
| Pricing Ladder | Three lifetime tiers, roughly $59 / $159 / $299, with each tier stacking site counts and feature unlocks (group bookings, payments, team scheduling). Tier 2 is the anchor. |
| Cost & Margin | Variable: AppSumo's revenue share is heavy on launch — typically a 70/30 split favoring AppSumo at the entry tier. Post-launch margin is &gt;90% on direct sales and renewals. The founder accepts the haircut for the email list and review volume. |
| Unfair Advantage | Cross-product portfolio — WPManageNinja already ships Fluent Forms, FluentCRM, FluentSMTP, and FluentSupport, with a combined install base in the hundreds of thousands. The owned email list converts at multiples of cold AppSumo traffic. |
| North Star | Launch period: daily code redemptions vs. seat caps. Post-launch: renewal rate at month 12 plus conversion of LTD buyers into paying users of sibling plugins. |

---

## Example 4: Designjoy (Productized Design Service, \~$1.5M ARR solo)

Unlimited design requests for startups and SaaS founders, run as a one-person business by Brett Williams.

| Component | Decision |
| --- | --- |
| Revenue Model | Productized service — flat monthly retainer, pause anytime, no contracts. One active request at a time, delivered next-business-day. |
| Pricing Ladder | Single tier at $4,995/month (raised from $3,995 then $4,995 as demand outpaced capacity). No annual discount — the product is explicitly designed to be paused, not committed to. Anchored against $8K+ traditional agency retainers. |
| Cost & Margin | Variable: software stack (Figma, Webflow, Notion), occasional contractor help during peak weeks. Brett famously runs this solo, which is what makes the margin work — north of 80% at scale, vs. the 40–50% typical of agency models that have to carry payroll. |
| Unfair Advantage | Audience — Brett built a public X/Twitter following of 100K+ by documenting Designjoy's growth in real time before and during scale. Inbound covers essentially all pipeline; zero paid acquisition. |
| North Star | Active retainers. Capacity-bound by a single designer — the constraint isn't sales, it's queue length. Above the cap, either quality drops or hiring becomes necessary and the margin math resets entirely. |

---

## Example 5: Splice (Two-Sided Marketplace, music samples)

Marketplace for royalty-free music samples, loops, and producer packs, with a subscription overlay on top of direct sales.

| Component | Decision |
| --- | --- |
| Revenue Model | Hybrid: producers list sample packs on the platform and earn per-download; users access the catalog via a credit-based subscription ("Sounds") or buy packs outright. Splice takes a margin on both sides. |
| Pricing Ladder | Sounds subscription tiered around $9.99 / $13.99 / $19.99/month for escalating monthly credit allocations and feature access (stems, AI-assisted Search). Direct pack sales priced by the producer, typically $20–$60. |
| Cost & Margin | Variable: payment processing, cloud storage for a 2M+ sample catalog, and producer royalty payouts — a meaningful share of each credit flows back to the rights holder. Gross margin lower than pure SaaS, but volume and renewal rates are strong. |
| Unfair Advantage | Producer default status — for a generation of bedroom producers, Splice *is* sampling the way Photoshop is image editing. The verb shows up in YouTube tutorials, beat-breakdowns, and music school curricula, which makes acquisition essentially passive and habit-locked. Competitors like LANDR Samples, Loopcloud, and Tracklib have shipped comparable catalogs and pricing for years without dislodging that default — the lead is behavioral, not contractual, which is why it survives even when individual producer partnerships churn. |
| North Star | Active subscribers × monthly downloads. Both sides of the marketplace track to one number — more downloads mean more producer earnings, which keeps supply pipeline healthy and renewal rates up. |

---

## Example 6: Resend (Developer API, usage-based)

Transactional email API for developers — React-based templates, modern dashboard, built by Zeno Rocha and team after years inside the developer-tools ecosystem.

| Component | Decision |
| --- | --- |
| Revenue Model | Usage-based SaaS with tiered subscription floors. Free tier seeds individual developers and side projects; paid plans gate higher send volumes, longer log retention, and dedicated IPs. Most expansion is automatic as customer apps grow. |
| Pricing Ladder | Free (3K emails/month, 100/day, 1 domain) / Pro at $20/month (50K emails, 10 domains, 7-day retention) / Scale at $90/month (100K emails, custom domains, 30-day retention) / Enterprise (custom, dedicated IPs, SOC 2). Overages priced per thousand emails on top of each tier. |
| Cost & Margin | Variable: underlying delivery infrastructure (AWS SES and equivalents wholesale at fractions of a cent per email), bandwidth, deliverability engineering, and IP warm-up. Markup is the design, DX, and reputation premium rather than infrastructure rent — gross margin lands in the \~80% band at scale, comparable to other developer-tool resellers. |
| Unfair Advantage | Developer experience as moat. The open-source React Email component library doubles as a distribution wedge — developers compose templates in JSX before they've picked a sending provider, and Resend is the default destination. Combined with Vercel/Next.js community proximity, the "what do you use for email?" answer inside YC and indie-hacker circles defaults to Resend before SendGrid or Postmark enter the conversation. |
| North Star | Monthly emails sent across paying accounts. Captures acquisition, expansion, and retention in one number — usage rarely shrinks once a production app integrates, so growth in send volume is the cleanest signal that the business compounds. |