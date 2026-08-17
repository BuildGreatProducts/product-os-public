---
name: studio-design-magic-moment
description: Use when the user has a finished `docs/PRODUCT.md` and wants to identify their product's aha moment — the specific instant the customer realizes the product is worth keeping. Triggers on phrases like "find my aha moment", "identify the magic moment", "what's my product's aha", "where should the wow happen", "design the activation moment", "what's the Facebook-7-friends moment for my product", "magic number for my product", "where does the customer first realize the value", or any request to recommend candidate aha moments for a product. Reads `docs/PRODUCT.md`, does live research on category-specific aha-moment patterns, recommends three candidate magic moments in the voice of a senior growth strategist, picks a primary, and writes the result to `productos/design/2-Magic-Moment.md`. Especially appropriate after the Product Identity is locked in and the user is ready to design onboarding around a specific activation event.
---

# Design: Magic Moment Identification

This skill guides a founder through identifying their product's **magic moment** — the specific user action that triggers the realization "this is worth keeping." The output is `productos/design/2-Magic-Moment.md` containing three evidence-backed candidate aha moments and a primary recommendation, drawn from `docs/PRODUCT.md` and live research into how comparable products in the same category have engineered activation.

The voice is a senior growth strategist with deep experience documenting and designing aha moments across consumer mobile, B2B SaaS, AI products, marketplaces, and productized services — the same lineage as Sean Ellis ("the moment the utility really clicks"), Brian Balfour and Andrew Chen's Reforge framework (setup → aha → habit), and Chamath Palihapitiya's documented Facebook north star (7 friends in 10 days). The strategist's job is not to invent a clever aha; it is to identify the *shape* of aha that fits this product's category, then propose three specific, testable candidates the founder can actually engineer into the first session.

A magic moment is not an opinion. It is the documented action that separates users who retain from users who churn — and in the absence of retention data (pre-launch or early-stage), it is the hypothesis grounded in named comparables that the team commits to testing first.

> **Session length:** Designed to be completable in 20–40 minutes of conversation. The user only needs to have a finished `PRODUCT.md`. All category research, comparable lookups, and candidate generation are Claude's job during the session. The output is a single decision document and a measurable hypothesis to test.

## Inputs

Locate the following in the ProductOS folder — `productos/` at the app repo root, or the current folder in a standalone ProductOS checkout. Look there before searching more widely, and never search `node_modules/`, build output, or vendored code:

1. **PRODUCT.md** — usually `docs/PRODUCT.md`. **Required.** The synthesised plain-English roll-up of the user's Define-phase work. The Customer section tells you who's experiencing the aha; the Problem section tells you what pain is being relieved; the Mechanism section tells you the action that delivers the relief; the Goal section tells you what success looks like. If PRODUCT.md doesn't exist or is substantively empty, stop and tell the user to run the `studio-define-product` skill first.

2. **The Product Identity** — usually `productos/design/1-Product-Identity.md`. Optional but useful. The tone of voice influences *how the aha is presented* (a Magician's reveal vs. a Sage's measured proof vs. an Outlaw's irreverent shock), and the tone of voice constrains the copy used at the aha moment.

If PRODUCT.md is missing or thin, stop and surface the gap before continuing — an aha hypothesis built on a thin product strategy inherits the thinness.

## The strategist's voice

Adopt the voice of a senior growth strategist with deep experience documenting activation across consumer apps, B2B SaaS, AI products, and marketplaces:

- **Pattern-matching.** Real strategists don't invent aha moments — they map the product against documented patterns. "Your product has Calendly's shape: single-utility, viral-on-use. The aha there was *creating and sharing the first link.* Yours rhymes."
- **Evidence-driven.** Every candidate names comparable products and what their documented aha was. "Facebook's was 7 friends in 10 days (Palihapitiya's documented north star). Slack's was 2,000 messages per team (Brian Balfour). Yours should rhyme with one of these shapes."
- **Specific.** Never "the user gets value." Always "the user uploads their first file *and* clicks Share — Dropbox's aha was the share, not the upload, because Dropbox isn't about storage, it's about collaborative access."
- **Speed-biased.** The bar for time-to-aha has dropped sharply. Mobile: under 5 minutes. B2B SaaS: under 24 hours, ideally under 5 minutes. AI products: under 60 seconds (Lovable's documented first-app-from-prompt). Push every candidate toward "as early as possible," ideally pre-signup.
- **Blunt about risk.** When a candidate aha is fashionable but unlikely to predict retention for *this* product, surface the risk. "First-AI-output is the trendy aha for AI apps, but if your product's value is daily reliability not first-shot brilliance, the aha is on day 3, not day 1."

## Workflow

### 1. Read PRODUCT.md and Product Identity

Read both files in full before forming any hypothesis. Extract:

- From PRODUCT.md: the customer (who), the problem (what pain), the mechanism (what action delivers value), the use moment (when and where the product is used), the goal (what success looks like), the business model (subscription, one-time, marketplace, freemium — affects how early the aha needs to be).
- From Product Identity (if present): the brand character (a dramatic reveal, a measured proof, a defiant shock — read it off the tone words and contrarian belief), the tone of voice (how copy at the aha moment should sound).

Form a **working hypothesis** in 2 sentences: candidate aha *shape* (one of the seven shapes below) and candidate *position* in the journey (pre-signup, first 60 seconds, first session, day 1, day 7). State this back to the user before going further.

### 2. Identify the aha shape

The product is going to rhyme with one of seven well-documented aha-moment shapes. Identify which one or two fit before proposing specific candidates.

- **Volume-of-use aha.** The user crosses a usage threshold and the product transitions from "I'm trying this" to "I live in this." Documented examples: Slack — 2,000 messages per team (93% retention at threshold, per Brian Balfour); Facebook — 7 friends in 10 days (Palihapitiya's documented north star); Twitter — 30 follows. Best fit for: habit-forming products with social, communication, or content-consumption cores.

- **Collaboration trigger aha.** The user shares, invites, or co-creates with someone else and the product reveals its multi-player value. Documented examples: Dropbox — first file uploaded *and shared*; Notion — first page created and shared with a collaborator; Calendly — first scheduling link created and shared. Best fit for: collaborative tools, sharing-driven products, marketplaces.

- **First-output aha.** The product produces a real artifact for the user — code, design, doc, transcript, image, plan — that the user can keep, share, or build on. Documented examples: Lovable — first working app generated from prompt (~60 seconds); Cursor — first AI-completed line of code accepted; Granola — first meeting transcribed; Cal AI — personalized plan revealed; ChatGPT — first useful answer to a real question. Best fit for: AI products, creative tools, generators.

- **Time-saved aha.** The user finishes a task in seconds that used to take minutes or hours. Documented examples: Superhuman — Inbox Zero in the first session; Calendly — first booked meeting without email back-and-forth; Stripe — first test payment processed in 7 lines of code. Best fit for: productivity tools, infrastructure, replacement-for-X products.

- **Personalization-reveal aha.** The product analyses the user's input and presents a tailored result that feels custom-built. Documented examples: Spotify — Discover Weekly; Cal AI — personalized calorie plan; Headway — personalized reading queue; Headspace — personalized meditation track. Best fit for: content discovery, health/wellness, recommendation-driven products.

- **First-win aha.** A single specific outcome the user can point to and feel good about. Documented examples: Duolingo — first lesson completed (with streak started); Strava — first run logged; Whoop — first sleep score; Apple Fitness — first ring closed. Best fit for: goal-oriented products, tracking, fitness, learning.

- **Pre-signup aha.** The user experiences real value *before* creating an account — signup becomes the act of saving what they already produced. Documented examples: Lovable — prompt box on the homepage builds a real app before signup; Airbnb — browse and view homes without login; Spotify — guest play; Perplexity — search without account. Best fit for: high-friction-to-signup products, viral utility products, products with a strong demo wow.

Most products map cleanly to one or two shapes. Name which one(s) fit and why.

### 3. Live research on the category

Search live for:

- **2–3 named comparable products** in the same category as the user's PRODUCT.md. For each, identify the documented aha moment if public, or the most credible inferred one if not.
- **The activation benchmarks for the category** — what's the typical time-to-aha, what's the typical first-session conversion, what's the typical day-1 retention bar.
- **Any documented patterns specific to AI products in this category** — most categories now have an AI-augmented incumbent whose aha is faster and earlier than the pre-AI norm.

Collect 4–6 concrete data points (named products with their aha + sources) before generating candidates. This evidence is the load-bearing layer under the three options.

### 4. Generate three candidate magic moments

Each candidate must be specific, evidence-backed, and engineered against a real position in the user journey. For each, define:

- **The action** — what the user does (in 5–10 words).
- **The wow** — what they see, feel, or unlock in that instant.
- **Where it sits** — pre-signup / first 60 seconds / first session / day 1 / day 3 / day 7. Push toward the earliest position the action can realistically happen.
- **Time-to-aha target** — a specific time bound (e.g., "<60 seconds from landing on the homepage" or "within the first session, before the user closes the app").
- **Comparable evidence** — 1–3 named products whose documented aha rhymes with this candidate.
- **Risk** — what could go wrong with this candidate. A candidate without a named risk hasn't been pressure-tested.
- **Metric** — the specific measurable threshold that confirms the user hit it (e.g., "X% of new accounts complete Y within Z minutes" or "session length ≥ N seconds on session 1").

The three candidates should be **distinct**, not three flavours of the same idea. Pull from different aha shapes where the product supports it. For example, a B2B AI product might have one Volume-of-use candidate, one First-output candidate, and one Collaboration trigger candidate — three genuinely different bets the team could test against each other.

### 5. Recommend a primary

After all three candidates are drafted, pick one as the **recommended primary**. The recommendation is based on three criteria, weighted in this order:

1. **Speed.** Which candidate gets the user to aha fastest from first contact?
2. **Evidence.** Which candidate has the strongest comparable evidence in the same category?
3. **Fit with the product's mechanism.** Which candidate is most consistent with the Mechanism described in PRODUCT.md?

State the recommendation in one sentence with reasoning in two sentences. The other two candidates remain in the document as alternates — useful if the primary hypothesis fails its test in 4–6 weeks.

### 6. Show the user and iterate

Present the three candidates in conversation with the recommended primary clearly marked. Ask one question: *"Does the recommended primary feel like the right first bet, or does one of the other two candidates fit better for reasons I haven't captured?"* Fold any user pushback in. Iterate once if needed — usually the user knows something about the customer's first session that adjusts the ordering.

### 7. Rewrite `productos/design/2-Magic-Moment.md` in place

A template file already exists at `productos/design/2-Magic-Moment.md` with the canonical structure (recommended magic moment + three candidates + sources). **Rewrite the existing file in place** — do not create a sibling file. Read the existing file first to preserve any user notes or modifications they have already made (e.g., if the file has been previously populated and they're refining it).

Match the template's structure exactly: same section headers, same field labels (Action / Wow / Where / Time-to-aha / Comparable evidence / Risk / Metric for each candidate; Where it sits / Time-to-aha target / Success metric for the primary). Replace the `[placeholder]` markers with the filled-in content. Keep the document scaffolding intact so the user can re-run the skill later and the file remains canonical.

**Structure of the output file:**

```
# Magic Moment

*Drafted: [Month Year]. Generated from PRODUCT.md.*

## The recommended magic moment

> [One sentence: when the user does X, they experience Y. That is the moment they realize this product is worth keeping.]

**Where it sits:** [position in journey]
**Time-to-aha target:** [specific time bound]
**Success metric:** [measurable threshold]

## Why this is the primary

[2–3 sentences pulling from category evidence and product fit.]

---

## Three candidates considered

### Candidate 1: [Name — one phrase]

- **Action:** [what the user does]
- **Wow:** [what they see / feel / unlock]
- **Where:** [position in journey]
- **Time-to-aha:** [target]
- **Comparable evidence:** [1–3 named products with their documented ahas]
- **Risk:** [what could go wrong]
- **Metric:** [measurable threshold]

### Candidate 2: [Name — one phrase]

[same structure]

### Candidate 3: [Name — one phrase]

[same structure]

## Sources

[3–6 cited sources from the live research — comparable product teardowns, named frameworks (Sean Ellis, Reforge, Brian Balfour), industry benchmarks.]
```

Keep the prose tight — each candidate is bullets, not paragraphs. The whole document should be readable end-to-end in under 3 minutes.

### 8. Verify before delivering

Re-read the written file and check:

- The recommended primary names a specific action, position, time-to-aha, and metric — no vagueness.
- Each of the three candidates has all seven fields (action, wow, where, time, comparable, risk, metric).
- Comparable evidence cites real named products, not generic categories.
- Time-to-aha targets are concrete (in seconds, minutes, hours, or session-number) — not "as fast as possible."
- The metric is measurable in product analytics, not vibes.
- The position-in-journey is the earliest realistic placement, not where it's convenient to build.
- The file is readable end-to-end in under 3 minutes.

Deliver via a `computer://` link and a short summary of what has been defined — one line for the primary, one line for each candidate, one line confirming where in the journey it sits. Keep the summary tight: this is a recap, not a re-pitch.

## Calibration: documented aha moments to draw on

These are publicly documented or widely-attributed aha moments to use as comparables. Refresh via live research at invocation time — the AI-products landscape moves fast.

### Consumer / mobile

- **Facebook** — 7 friends in 10 days. Documented by Chamath Palihapitiya as the company's north star to 1B users.
- **Twitter** — 30 follows. The threshold at which a feed starts feeling alive.
- **Snap** — 3 snaps to 3 friends in the first week. The reciprocal-action loop.
- **WhatsApp** — first message sent and replied to. The two-way confirmation.
- **Duolingo** — first lesson completed, streak started. The gamified habit hook.
- **Strava** — first run logged. The single-act validation.
- **Cal AI** — personalized plan revealed at end of onboarding quiz.
- **Spotify** — guest play, then Discover Weekly in the first week.

### B2B SaaS

- **Slack** — 2,000 messages sent across a team (93% retention rate at threshold; Brian Balfour).
- **Dropbox** — first file uploaded *and shared* (the share is the aha, not the upload).
- **Notion** — first page created and shared with a collaborator.
- **Calendly** — first scheduling link created and shared externally.
- **Stripe** — first test payment processed (the 7-line cURL aha).
- **Linear** — first issue created with keyboard shortcut (the speed reveal).
- **Superhuman** — Inbox Zero in the first session (concierge onboarding made the aha mandatory).
- **HubSpot** — segmented by JTBD; aha varies per segment (sales reps: first deal logged; marketers: first form built).

### AI products

- **Lovable** — first working app generated from prompt (~60 seconds; pre-signup).
- **Cursor** — first AI-completed line of code accepted in the user's existing repo.
- **Granola** — first meeting transcribed with no bot in the call.
- **ChatGPT** — first useful answer to a real question the user already had.
- **Perplexity** — first cited answer to a real question (no login required).
- **Claude** — first long-form task completed correctly.
- **Cal AI** — personalized calorie/macro plan reveal at end of onboarding.
- **Headway** — personalized book queue at end of onboarding.

### Marketplaces

- **Airbnb** — first booking (pre-launch hosts: first listing receiving a booking inquiry within 2 weeks).
- **Etsy** — first sale (sellers); first favorited listing (buyers).
- **Fiverr** — first gig sold (sellers); first gig delivered to expectation (buyers).
- **Uber** — first ride completed within 5 minutes of request.

### Productized services

- **Designjoy** — first deliverable returned in <48 hours (Brett Williams' documented ops benchmark).
- **Penji / ManyPixels** — first design request fulfilled within SLA on day 1.

### Frameworks

- **Sean Ellis** — "moment the utility of the product really clicks." Pair with the PMF survey ("how would you feel if you could no longer use this product?" — 40%+ "very disappointed" = initial PMF).
- **Reforge (Brian Balfour, Andrew Chen, Sean Clowes)** — setup moment → aha moment → habit moment. The aha is the wedge between setup and habit.
- **Time-to-aha benchmarks (2026):** mobile <5 min; B2B SaaS median 1d 12h, top-quartile <5 min; AI products <60 sec.
- **Speed-to-aha lift:** users who hit aha within 48 hours are 3.4x more likely to convert to paid.
- **Onboarding length:** 3-step tours complete at 72%; 7-step tours complete at 16%.

## Pacing and approval

- **Hypothesis first, research second, candidates third.** Don't generate candidates before confirming the aha-shape hypothesis and showing it back to the user.
- **Three distinct candidates, not three flavours of one.** If the three options are too similar, the recommendation isn't a real decision.
- **Push toward the earliest possible position.** The bias is always "could this happen sooner?" If a candidate is on day 3, ask whether a variant of it could happen on day 1.
- **Cite named comparables.** Every candidate must reference at least one real named product. "Other products do this" is not evidence.
- **Acknowledge that this is a hypothesis.** This is the team's first bet, not a proven truth. Until retention data confirms it, the magic moment is a *committed hypothesis to test* — that framing belongs in the doc and in the conversation.
- **Write the final document concisely.** Each candidate is a tight bullet structure, not paragraphs. The whole doc reads in under 3 minutes.

## What "done" looks like

A `productos/design/2-Magic-Moment.md` where:

- **A recommended primary magic moment** is stated in one sentence, with position-in-journey, time-to-aha target, and success metric.
- **Three distinct candidates** are documented, each with action, wow, where, time-to-aha, comparable evidence, risk, and metric.
- **Comparable evidence** cites real named products — at least two per candidate where possible.
- **The position-in-journey** is the earliest realistic placement, with a bias toward pre-signup or first-session.
- **The success metric** is measurable in product analytics — not "users feel the value" but "X% of new accounts complete Y within Z minutes."
- **Sources** cite 3–6 named references from the live research.
- **The file is readable in under 3 minutes** and dated.

Recommended next step after a successful session: run the **Onboarding Flow** skill (`studio-design-onboarding-flow`) to design the concrete onboarding flow that engineers the recommended magic moment into the first session. The Magic Moment skill defines *what* the activation event is; the Onboarding Flow skill defines *how* the user is routed to it screen by screen.
