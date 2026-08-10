# BONUS - Web Landing Page Best Practice

*A bonus asset for ProductOS — 12 principles, 18 tactics, and a decision tree pulled from teardowns of the highest-converting landing pages shipping today: Stripe (actual runnable code in the hero), Linear (minimalist confident editorial), Anthropic (quiet rigor against the AI noise floor), Notion (its own visual language as the design system), Lovable (prompt box hero / try-before-signup), Cursor (code-sample hero), Granola, Vercel, and the 2026 conversion datasets from HubSpot, Hotjar, AdEvolver, and the "2,000 pages tested in 2026" landing page study.*

---

## The Meta-Rule

> **A landing page has one job: convert a stranger who clicked a link into someone who took the next step. Every section, every word, every pixel either pulls the user toward that action or pulls them away. Above the fold is the entire fight — most visitors decide whether to scroll or close the tab in under 7 seconds, and 89% of clicks on the page come from above-the-fold CTAs. The rest of the page exists to recover the user who didn't convert above the fold, not to teach the user who did.**

Onboarding sells activation. Magic moments sell the wow. Product identity sells the brand. **Landing pages sell the next click.** Stripe became Stripe because the first thing a developer sees is runnable code — not an illustration of code, not a screenshot of code, runnable code with copyable cURL. Linear's marketing site refreshes incrementally several times a year because the team understands the landing page is the product's most-visited surface. Anthropic positions on safety and rigor and uses *quiet design* in a noisy AI category to make that positioning legible. Every winning landing page in 2026 makes one promise above the fold, demonstrates it visually, and gives the visitor one obvious next action.

---

## The Numbers That Set the Stakes

These are the 2026 benchmarks from the Landing Page Conversion Study (2,000 pages tested), HubSpot's Annual Marketing Benchmark Study, Hotjar's 2026 click analysis, AdEvolver's 90-CTA winner study, the SaaS Hero 2026 B2B SaaS Conversion Benchmarks, and Cristina Cordova's documented marketing-site teardowns of Stripe, Notion, and Linear.

| Metric | Number | Source |
| --- | --- | --- |
| B2B SaaS average visitor-to-lead conversion | **1.5–2.5%** | SaaS Hero 2026 |
| B2B SaaS top-10% visitor-to-lead conversion | **8–15%** | SaaS Hero 2026 |
| SaaS free-trial conversion (median) | **7.2%** | SaaS Hero 2026 |
| Single-goal landing page conversion | **13.5%** (vs 10.5% for multi-CTA pages) | Landing Page Conversion Study 2026 |
| Lift from above-fold CTA + 10-word value prop | **+96% engagement, 11.3% session-to-conversion** | Hotjar 2026 |
| Lift from above-fold CTA vs no above-fold CTA | **+89% more clicks** | Hotjar 2026 |
| Sticky CTA conversion lift | **+11%** (above-fold + sticky together: +12% — sticky absorbs most of the benefit) | LP Study |
| Lift from personalized CTAs vs generic | **+202%** | HubSpot 2026 |
| Lift from AI-driven dynamic CTAs vs static defaults (B2B SaaS) | **+231%** | HubSpot 2026 |
| Average word count of winning CTAs | **3.4 words** | AdEvolver (90 CTAs analyzed) |
| Lift from first-person CTA ("Start my trial") vs second-person ("Start your trial") | **+90% CTR** | ContentVerve |
| Lift from removing the hero entirely vs a stock-image hero | **+4%** | LP Study 2026 |
| Lift from a single-stat hero (one giant number) | **+18%** | LP Study 2026 |
| Hero video lift vs static hero (B2B SaaS) | **−7%** (video lost to static) | LP Study 2026 |
| Best-in-class heroes that show social proof above the fold | **81%** (vs 41% baseline) | LP Study 2026 |
| Best-in-class heroes that include a risk reducer near CTA | **65%** (vs 42% baseline) | LP Study 2026 |
| Lift from headline rewrites (outcome + timeframe vs feature-led) | **Up to +67.8%** | KlientBoost |
| Average days SaaS marketing teams refresh their landing page | **45 days** (top quartile) | SaaS Frame |

The two numbers that should change how you build: **above-the-fold CTA + 10-word value-prop = +96% engagement** (Hotjar 2026 — the single highest-leverage combination in landing page design), and **video heroes lost to static heroes by 7 percentage points** in the 2,000-page 2026 study. The 2022–2023 instinct that "video is always better" has been measurably wrong for B2B SaaS for two years — clarity beats motion, especially above the fold.

---

## The 12 Principles

These are the mental models that show up across every winning landing page teardown.

### 1. One Promise, Above the Fold, Stated in Plain English

The single most important thing on the page is the headline. A B2B visitor decides in under 7 seconds whether to scroll. The headline must state — in the user's words, not the company's words — the outcome they will get. "Generate 50% more leads in 30 days" beats "Modern AI-powered lead intelligence platform" on every test, every time. **If a stranger can't tell what your product does from the headline alone, the page is broken.**

### 2. Show, Don't Describe

Stripe's hero is *actual cURL code, copyable, runnable.* Lovable's hero is *a prompt box that builds a working app before signup.* Cursor's hero is *a code sample showing AI completing real code.* Notion's hero is *a working Notion page on the page itself.* The 2026 winners demonstrate the product *in the hero*, not in a video below the hero, not in a screenshot — in the actual hero zone. Static hero illustration is the lowest-converting hero pattern in the 2026 dataset.

### 3. One CTA Above the Fold, Same CTA Everywhere

Multi-CTA pages convert at 10.5%; single-goal pages convert at 13.5%. The difference is decision fatigue. Pick the one CTA — *Start free trial / Try the demo / Get a quote* — and use the same CTA copy, same button, same destination throughout the page. "Schedule a demo" in the header and "Talk to sales" in the footer feel like two products. **One product, one promise, one CTA.**

### 4. Sticky CTA Beats Hero CTA Alone

The above-fold CTA on its own lifts conversion +6%. The sticky CTA (one that follows the user as they scroll) lifts +11%. Both together = +12% — the sticky absorbs most of the above-fold's benefit. The implication: if you only build one, build the sticky. It catches the user at the moment they're convinced, wherever that moment is on the page.

### 5. Social Proof Above the Fold, Not Below

81% of best-in-class heroes show social proof — customer logos, trust bars, or testimonial fragments — *before the user scrolls*. The baseline pattern (social proof in a dedicated section below the hero) converts meaningfully worse. The user needs evidence they're not the first person taking the product seriously *while they're still deciding to read further.*

### 6. The Value Proposition Is Outcome × Timeframe

The winning headline formula: **[Desired outcome] + [Timeframe or ease]**. "Generate 50% more leads in 30 days." "Ship a feature in one afternoon." "Get your team to inbox zero by Friday." Headlines that name a feature ("AI-powered analytics dashboard") underperform headlines that name a result ("Cut your reporting time by 80%") by double-digit percentages on every documented test.

### 7. CTA Copy Is the Most-Read Word on the Page

The average winning CTA in AdEvolver's 90-CTA analysis is 3.4 words. Generic single-word commands ("Submit," "Continue," "Click Here") lose to benefit-driven copy by up to 60%. First-person framing ("Start *my* trial") beats second-person ("Start *your* trial") by 90% click-through lift. **Spend more time writing the CTA than the hero illustration.**

### 8. Demonstrate the Product on the Page, Not in a Video

Video heroes lost to static heroes in the 2026 dataset (−7%). The reason is that motion delays comprehension — the user has to wait for the video to make its point. Interactive demos *in the page* (Lovable's prompt box, Stripe's runnable code, Linear's product-screenshot animation that loops in under 4 seconds) win because they let the user *see the product working* without waiting. If you must use video, embed it below the hero, make it under 30 seconds, and let the page tell the story without it.

### 9. Pricing Is the Most-Visited Page After the Homepage

Hide your pricing and the user assumes it's expensive. Show it and you filter out poor-fit leads before they touch sales. The 2026 best-in-class SaaS pattern: pricing on the marketing site, three tiers max, one "most popular" tier highlighted, an annual/monthly toggle, and a clear answer to "what's included" in plain English. **For ACVs under ~$25K, hiding pricing behind "Contact Sales" is a 90%+ conversion loss.**

### 10. The FAQ Defuses Objections, Doesn't List Features

The FAQ section's job is to handle the specific concerns that stop a high-intent visitor from clicking the CTA: pricing structure, implementation time, security/compliance, data export, switching costs. Generic FAQs ("How does it work?") add length without lift. **Write the FAQ by answering the actual questions your sales team gets, then putting those answers on the page so sales doesn't have to.**

### 11. Animation Teaches or It Gets Cut

The 2022–2023 pattern of animating everything on scroll is over. The 2026 winning style is "surgical" — one or two tuned reveals per page, measured easing curves, no bounce. Motion that explains a transition is valuable; motion that decorates is friction. **The rule: if the animation does not teach or reassure, remove it.** Linear, Anthropic, and Vercel all converged on quiet, restrained motion in 2025–2026.

### 12. The Landing Page Is a Living Document

Top-quartile SaaS marketing teams refresh their landing page on a 45-day cadence — copy, hero, screenshots, testimonials, headlines. The landing page is your highest-leverage marketing surface; treating it as a one-time launch project is how landing pages get stale. **Plan to refresh the hero copy at least quarterly; plan to A/B test the CTA monthly.**

---

## The Decision Tree — Which Landing Page Pattern Should You Build?

Start at the top. Stop at the first "yes."

**Is your product something a visitor can experience in 30 seconds inside the browser (AI app builder, image generator, code completion, design tool)?**
→ Run **#1 The Try-Before-Signup Hero** (Lovable / Cursor / v0 pattern). Hero = a working interactive surface. Signup gate is "save what you just built."

**Is your product a developer API or SDK (Stripe, Twilio, Anthropic, Resend)?**
→ Run **#2 The Code-in-the-Hero Pattern** (Stripe / Resend / Anthropic pattern). Hero = runnable code with multi-language tabs. CTA = "Get API keys" or "Read the docs."

**Is your product a collaborative B2B SaaS (Linear, Notion, Slack-shape)?**
→ Run **#3 The Product-Visual Hero** (Linear / Notion pattern). Hero = real product screenshot or short looping animation showing the product working. CTA = "Start free."

**Is your product a consumer subscription where the value is the AI's output on the user's data (Cal AI, Headway, Headspace)?**
→ Run **#4 The Outcome-First Hero** with App Store badges. Hero = the outcome the user wants. CTA = App Store / Play Store badges, app sign-up if web-first.

**Is your product enterprise / vertical / sales-led (ServiceTitan, Toast, Harvey)?**
→ Run **#5 The Customer-Logo Hero**. Hero = customer outcomes with named logos. CTA = "Book a demo." Pricing is hidden by design; the page is a sales-enablement surface.

**Is your product a productized service (Designjoy, Penji, MarketerHire)?**
→ Run **#6 The Gallery + Price Hero** (Designjoy pattern). Hero = gallery of delivered work. Pricing visible on the page. CTA = self-serve Stripe Checkout.

**None of the above and you're stuck?**
→ Default to **#3 Product-Visual Hero** if you have a UI; **#4 Outcome-First Hero** if you don't. Iterate.

---

## The 18 Tactics

Organized by page section. Build top-to-bottom.

---

### Stage 1 — The Header / Nav (the first 1 second)

#### 1. The Sticky Header With CTA

**Why:** The sticky header is the first thing the user sees and the one element that stays visible during the entire scroll. Best-in-class headers include: logo (left), 3–5 nav links (Product / Pricing / Customers / Resources / Login), CTA button (right). The CTA in the header is the sticky CTA — same copy, same destination, same color as everything else.

**Pass threshold:** Header is sticky on scroll. CTA in header is the same copy as the hero CTA. Nav has ≤5 items.

#### 2. The Pricing Link in the Nav

**Why:** Users who click "Pricing" first are the highest-intent users on the page. Hiding pricing behind "Contact us" makes them bounce. Showing pricing in the nav signals "self-serve is available" — even if some plans require sales contact.

**Pass threshold:** Pricing is a top-level nav link. The pricing page lists at least one self-serve tier visibly.

---

### Stage 2 — The Hero (the next 5 seconds)

#### 3. The 10-Word Value-Prop Headline

**Why:** The Hotjar 2026 finding is decisive: 10-word value-prop + above-fold CTA = +96% engagement and 11.3% session-to-conversion. The headline says the outcome in the user's words. The 10-word target is a ceiling, not a floor — Linear's "Linear is a purpose-built tool for planning and building products" is 11 words and exceptional; Lovable's "Build software products, using only a chat interface" is 9 words and exceptional. Anything over 15 words is too much.

**Pass threshold:** Hero headline is ≤12 words, names a specific outcome, reads naturally aloud.

#### 4. The Specific Sub-Headline

**Why:** The sub-headline (one sentence under the headline) does what the headline can't fit. Most often: who it's for, what specifically it does, or how fast. "For engineering teams at fast-growing software startups" reads as a sub-headline; the headline is "The issue tracking tool you'll enjoy using." Together they qualify, focus, and concretize.

**Pass threshold:** Sub-headline names the customer, the specific outcome, or the specific time — not all three. One sentence.

#### 5. The First-Person CTA

**Why:** "Start my free trial" beats "Start your free trial" by 90% CTR. "Get my pricing" beats "Get pricing." First-person framing makes the visitor mentally claim the action. The CTA copy should be 3–4 words, name the benefit, and use first person.

**Pass threshold:** Hero CTA is 3–5 words, names the benefit, uses first-person framing ("my" or "I").

#### 6. The Hero Demonstration

**Why:** The hero must show the product working — runnable code (Stripe), interactive prompt box (Lovable), product screenshot or looping micro-animation (Linear, Vercel, Notion). Stock illustration of "AI brain on a gradient" is the lowest-converting hero pattern in the 2026 dataset. The hero demo is the visual proof the headline isn't marketing-speak.

**Pass threshold:** Hero visual shows the actual product in actual use. No stock photography, no abstract gradients, no "AI brain" illustrations.

---

### Stage 3 — Social Proof (the next 3 seconds — still above the fold)

#### 7. The Logo Bar Below the Hero

**Why:** A row of 5–8 customer logos directly below the hero — preferably above the fold or just at the fold — is the canonical "this product is taken seriously" signal. Best-in-class: 5–8 logos, recognizable brands, the same visual weight, no tagline above ("Trusted by leaders" adds nothing).

**Pass threshold:** Logo bar visible without scrolling on a 1366×768 viewport. 5–8 named logos. No "trusted by" tagline above them.

#### 8. The Hero Testimonial Fragment

**Why:** Best-in-class heroes (81% of them) include a testimonial fragment *above the fold* — a one-line quote with the name, role, and company. Not a full testimonial section; a single sentence that confirms the headline. "We shipped 3x faster — Lara, eng lead at Acme" goes a long way.

**Pass threshold:** A one-line testimonial visible above the fold, with named source and role.

---

### Stage 4 — The Problem and Solution (scroll 1–2)

#### 9. The Problem Statement

**Why:** Before features, name the problem in the user's own language. "Your team spends 15 hours a week in status meetings" beats "Communication challenges in modern teams." The problem section sets up the solution; without it, the solution feels like a feature list with no anchor.

**Pass threshold:** Problem section uses verbatim user language. Names a specific cost (hours, dollars, missed opportunities).

#### 10. The Solution / How It Works

**Why:** Three steps, three sentences, three visual fragments. "Connect your data → AI generates a draft → You ship in minutes." The user has to be able to mentally simulate using the product after this section. If they can't, the section is too abstract — replace concepts with verbs.

**Pass threshold:** Three numbered steps. Each step ≤15 words. Each step has a visual fragment showing the action.

#### 11. The Features-as-Benefits Section

**Why:** Don't list features; list outcomes the features unlock. "Slack integration" is a feature; "Get notified the moment a customer churns" is a benefit. The 2026 winning pattern uses 4–6 benefit blocks, each with: a 5-word headline, a 20-word description, and a small visual (icon or product fragment).

**Pass threshold:** ≤6 benefit blocks. Each headline is benefit-led, not feature-led. Each has a small concrete visual.

---

### Stage 5 — Deep Social Proof (scroll 2–3)

#### 12. The Case Study Pull-Quotes

**Why:** Three case study fragments with named customer + specific result + photo or logo. "Acme cut their customer support costs by 40% in 90 days." Each pull-quote links to a deeper case study page. Specific revenue / outcome numbers ("$504k Net New ARR") beat generic praise by an order of magnitude on conversion lift.

**Pass threshold:** ≥3 case study pull-quotes. Each names a specific outcome with a number. Each links to a deeper case study.

#### 13. The Star Rating + Review Count

**Why:** "4.8 ★ from 12,400 reviews" — with the source (G2, Capterra, Product Hunt, App Store) — is one of the most efficient trust signals on the page. Best placement: just above the second CTA, where the user's deciding whether to click.

**Pass threshold:** Star rating + review count + named source visible above at least one repeated CTA.

---

### Stage 6 — Pricing (scroll 3–4)

#### 14. The Three-Tier Pricing Table

**Why:** Three tiers, one highlighted as "most popular," annual/monthly toggle, "what's included" list per tier, single CTA per tier. Best practice for B2B SaaS: name the tiers by use case (Starter / Growth / Enterprise) and include a free tier or free trial. For consumer subscription: 1 tier, 1 annual/monthly toggle, App Store badges.

**Pass threshold:** Three pricing tiers visible without scrolling. Most-popular tier highlighted. Toggle for annual/monthly visible.

#### 15. The Pricing FAQ

**Why:** Below the pricing table, a 4–6 question FAQ that handles the actual objections: "Can I change plans?" "What happens at the end of trial?" "Do you offer refunds?" "How does the seat count work?" These questions cost sales time when they go unanswered on the page.

**Pass threshold:** ≥4 FAQ items below pricing. Each addresses a real objection sales gets.

---

### Stage 7 — The Final CTA and Footer (scroll 4–5)

#### 16. The Repeated CTA Block

**Why:** A final CTA block before the footer — large headline, same CTA copy as the hero, single button. The user who's scrolled this far is high-intent; give them the same easy out as the visitor who converted at the hero. Add a low-friction alternative (newsletter signup, "see live demo") for the not-yet-ready visitor.

**Pass threshold:** Repeated CTA block before the footer. Same CTA copy as the hero. Low-friction alternative for non-converters.

#### 17. The Footer With Trust Signals

**Why:** SOC 2, GDPR, ISO 27001, HIPAA badges in the footer — not advertised as features, just present. Customer service hours. Status page link. Privacy policy. The footer is where compliance/procurement teams check before forwarding to legal.

**Pass threshold:** Compliance badges visible in footer. Status page linked. Privacy / terms / GDPR / security pages linked.

---

### Stage 8 — The Long Game

#### 18. The 45-Day Refresh Cadence

**Why:** Top-quartile SaaS teams refresh their landing page every 45 days. Hero copy, testimonials, screenshots, features highlighted. Linear refreshes incrementally several times per year. The landing page is not a launch artifact; it is the company's most-visited surface and the highest-leverage marketing asset.

**Pass threshold:** Documented refresh cadence ≤60 days. A/B test running on at least one variable continuously.

---

## Worked Example 1 — The Stripe Hero

Stripe is the canonical "show, don't tell" landing page. The hero contains *actual cURL code* the developer can copy and run against Stripe's API.

| Element | What Stripe does |
| --- | --- |
| Headline | "Financial infrastructure for the internet" — confident, plain English, 6 words |
| Sub-headline | "Millions of businesses of all sizes use Stripe online and in person to accept payments, send payouts, automate financial processes, and ultimately grow revenue." |
| Hero visual | Runnable cURL code with copy button. Multi-language tabs (cURL / Node / Python / Ruby / Go). |
| CTA | "Start now" (3 words) |
| Social proof | Logo bar with Amazon, Google, Shopify, Salesforce within 2 scrolls |
| Pricing | Linked from nav. Public, transparent, no contact-sales gate for self-serve |

**Result:** The category-defining payments API by every metric. The "code as hero" pattern is now the canonical reference for API products.

---

## Worked Example 2 — The Lovable Try-Before-Signup Hero

Lovable's homepage is a prompt box. The user types an app idea, the AI generates a working web app inside ~60 seconds, and signup fires when the user wants to save what they built.

| Element | What Lovable does |
| --- | --- |
| Headline | "Build software products, using only a chat interface" — 9 words |
| Sub-headline | One sentence on what gets built |
| Hero visual | A prompt box (the actual product surface) |
| Pre-signup wow | A working app is generated before the signup gate |
| CTA | The send button on the prompt box (no separate "sign up" CTA) |
| Social proof | Community gallery of user-built apps |

**Result:** $200M ARR in 12 months with zero paid acquisition. The "prompt box as hero" pattern is now the AI-app reference.

---

## Worked Example 3 — The Linear Product-Visual Hero

Linear's hero is a real product screenshot, looping subtly to show the issue tracker actively in use. The site refreshes incrementally several times per year and is widely regarded as the canonical B2B SaaS marketing surface.

| Element | What Linear does |
| --- | --- |
| Headline | "The issue tracking tool you'll enjoy using" |
| Sub-headline | "Linear is a purpose-built tool for planning and building products" |
| Hero visual | Real Linear UI screenshot with subtle motion |
| CTA | "Start building" (2 words) |
| Social proof | Customer logos (Vercel, Ramp, Mercury, Cash App, Loom, Scale AI) within first scroll |
| Pricing | Visible, three tiers, free for unlimited members on Standard |

**Result:** Linear is the category-defining issue tracker; the marketing site is the most-imitated B2B SaaS reference of 2025–2026.

---

## Anti-Patterns — What Kills Landing Page Conversion

### The Stock Illustration Hero

An "AI brain on a gradient" or "abstract glowing orb" hero. Lowest-converting hero pattern in the 2026 dataset. **Replace with the actual product working.**

### The Multi-CTA Hero

Three CTAs above the fold ("Start free trial," "Book a demo," "Talk to sales"). Decision fatigue. Single-goal pages convert at 13.5%; multi-CTA at 10.5%. **Pick one. Repeat it.**

### The "Submit" Button

Generic single-word CTAs lose to benefit-driven CTAs by up to 60%. **"Submit" → "Get my pricing."**

### The Hidden Pricing

Pricing page that only shows "Contact us." 90%+ conversion loss for ACVs under $25K. **Show the price.**

### The Hero Video That Plays on Load

Auto-playing video heroes lost to static heroes by 7% in the 2026 study. **Static screenshot or interactive demo beats video on B2B SaaS.**

### The Animation-Everything Scroll

Every section reveals with a fade-and-slide. The 2022–2023 over-animation pattern is dead. **Surgical motion only — one or two tuned reveals per page.**

### The Wall of Logos

A logo bar with 30 customers. Reads as desperate. **5–8 named logos, same weight, no tagline.**

### The Feature List

Six bullet points starting with the product name. ("Linear is fast. Linear is opinionated. Linear has keyboard shortcuts...") **Lead with benefits the user wants, not features the product has.**

### The Form Wall

Email + name + company + phone + role + team size before the user can see anything. Conversion craters. **Email-only signup. Capture the rest through behavior.**

### The "Trusted By" Section With No Logos

The tagline without the proof. **Either show the logos or remove the section.**

### The Below-the-Fold-Only Social Proof

All social proof saved for the testimonials section. 81% of best-in-class heroes show social proof above the fold. **Move at least one logo bar and one testimonial fragment above the fold.**

### The 30-Section Page

A 30-screen scroll covering every possible objection. The user is gone by section 8. **Cut to 6–8 sections. The visitor who needs more goes to the case studies page.**

---

## Calibration — What Good Looks Like

| Metric | Floor | Good | Best-in-class |
| --- | --- | --- | --- |
| Visitor → next-action conversion (B2B SaaS) | 1.5% | 4% | 8–15% |
| Visitor → free-trial signup (SaaS) | 3% | 7% | 15%+ |
| Above-fold engagement (% who scroll past hero) | 50% | 70% | 85%+ |
| Time to first CTA click | 30 sec | 12 sec | <7 sec |
| Hero CTA click-through rate | 3% | 8% | 15%+ |
| Sticky CTA click-through rate | 1% | 3% | 6%+ |
| Bounce rate | 60% | 40% | <30% |
| Refresh cadence (days between hero copy changes) | 90 days | 45 days | 30 days |
| A/B tests running concurrently | 0 | 2 | 5+ |
| Page load time (LCP) | <3 sec | <2 sec | <1 sec |

If you are below the floor on visitor → next-action or above-fold engagement, the fix is almost never the design — it is the hero headline, the CTA copy, or the visual. Re-read principles #1, #2, and #6.

---

## The Landing Page Operating Model

Four functions running continuously:

**1. Hero copy on a 45-day refresh cycle.** The hero headline, sub-headline, and CTA are A/B tested on a documented cadence. Top-quartile teams refresh the hero copy every 45 days even when current performance is acceptable.

**2. Pricing page as a first-class surface.** The pricing page is the second most-visited page after the homepage. Treat it with the same craft — testimonials per tier, FAQ below, comparison table for B2B SaaS.

**3. Case study production cadence.** A new case study every 30 days, replacing the oldest pull-quote in the hero. Specific revenue / outcome numbers per case study.

**4. Sticky-CTA A/B testing.** The sticky CTA absorbs most of the conversion lift. Test its copy, color, and position monthly.

---

## Closing — The One Mental Model That Beats Everything

> **A landing page is a 7-second sales pitch with a 7-minute follow-up attached. The first 7 seconds — the headline, the visual, the CTA above the fold — decide whether the visitor scrolls or closes the tab. The remaining 7 minutes of page exist to recover the visitor who didn't convert in the first 7 seconds. Your only job is to make the first 7 seconds inevitable, and to give the recovering visitor the same easy out as the first-time converter.**

Stripe became Stripe because the first thing a developer sees is runnable code. Lovable became Lovable because the prompt box on the homepage delivered a working app before the user signed up. Linear became Linear because the marketing site refreshes incrementally and the hero shows the actual product working. The 2026 winners don't have more sections, more animations, or more clever copy than the losers — they have one promise above the fold, demonstrated visually, with one obvious next action.

Build for the 7 seconds. Refresh for the 45 days. Test the CTA monthly. That is how landing pages compound.

---

*Sources & teardowns this guide draws from: the Landing Page Conversion Study (2,000 pages tested in 2026); Hotjar's 2026 click analysis; HubSpot's 2026 Annual Marketing Benchmark Study; AdEvolver's 90-CTA winner analysis; ContentVerve's first-person CTA test; KlientBoost's headline rewrite study; SaaS Hero's 2026 B2B SaaS Conversion Benchmarks; the "Why Most SaaS Landing Pages Fail" Webflow analysis; Cristina Cordova's Stripe / Notion / Linear marketing-site teardowns; the Stripe, Linear, Anthropic, Lovable, Cursor, Notion, and Vercel marketing-site analyses from GridRebels, SaaSFrame, Ebaqdesign, and StartDesigns; Demand Curve's "Anatomy of a High-Converting Landing Page"; Unbounce's landing page anatomy reference.*
