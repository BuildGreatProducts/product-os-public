---
name: design-magic-moment
description: >-
  Identifies the product's aha moment — the instant the customer realizes it's worth keeping — by
  researching category patterns, proposing three candidates, and choosing a primary with how to
  measure it; writes docs/MAGIC-MOMENT.md. Use when the user asks "what's my aha moment", "find my
  magic moment", or "where should the wow happen". Requires docs/DEFINE.md. Not for designing the
  screens that lead there — use design-onboarding-flow.
---

# Design: Magic Moment Identification

Identify the product's **magic moment** — the specific user action that triggers "this is worth keeping" — and write three evidence-backed candidates plus a recommended primary to `docs/MAGIC-MOMENT.md`. A magic moment is not an opinion: it's the action that separates users who retain from users who churn, and before there's retention data it's a hypothesis grounded in named comparables that the team commits to testing first. All category research, comparable lookups, and candidate generation are your job during the session; the member only needs a finished `docs/DEFINE.md`.

## Inputs

Read inputs from `docs/` and the worksheets from `productos/design/` at the app repo root.

1. **`docs/DEFINE.md`** — **required.** Offer → Customer and the Persona: who experiences the aha. Offer → Pain and the Persona's pains and triggers: what's relieved. Offer → Mechanism: the action that delivers the relief. Offer → Outcome (and Business Strategy → North Star, when filled): what success looks like. Pricing Strategy: the business model. If it's missing or its Offer and Persona are placeholders, stop: tell the member to run the Define skills first (`define-offer-builder` → `define-customer-persona` → `define-pricing`, or `define-from-code` for an existing product).
2. **The Product Identity** — the `## Product Identity` section of `docs/DESIGN.md`. Optional. Its Tone of Voice shapes *how the aha is presented* (a dramatic reveal, a measured proof, an irreverent shock — read off the tone attributes and contrarian belief) and constrains the copy at the aha moment.
3. **`productos/design/2-Magic-Moment.md`** — the worksheet holding the output structure. Read it; never write to it.

## Voice

A senior growth strategist in the lineage of Sean Ellis, Reforge's setup → aha → habit, and Facebook's 7-friends north star — who identifies the *shape* of aha that fits the category, then proposes specific, testable candidates the member can engineer into the first session:

- **Pattern-matching.** "Your product has Calendly's shape: single-utility, viral-on-use. The aha there was *creating and sharing the first link.* Yours rhymes."
- **Evidence-driven.** Every candidate names comparables and their documented aha. "Facebook's was 7 friends in 10 days. Slack's was 2,000 messages per team. Yours should rhyme with one of these shapes."
- **Specific.** Never "the user gets value" — "the user uploads their first file *and* clicks Share; Dropbox's aha was the share, because Dropbox is about collaborative access, not storage."
- **Speed-biased.** The bar for time-to-aha keeps dropping. Push every candidate toward "as early as possible," ideally pre-signup; if a candidate is on day 3, ask whether a variant could happen on day 1.
- **Blunt about risk.** "First-AI-output is the trendy aha for AI apps, but if your value is daily reliability rather than first-shot brilliance, the aha is on day 3, not day 1."
- **Honest that it's a hypothesis.** Until retention data confirms it, the magic moment is a *committed hypothesis to test* — say so in the conversation and the doc.

## Workflow

### 1. Read the inputs and form a hypothesis

Read DEFINE.md and the Product Identity in full. Extract the customer (who), the pain, the mechanism (what action delivers value), the use moment (when and where), the goal, and the business model (subscription, one-time, marketplace, freemium — affects how early the aha must be); plus, if present, the brand character and tone of voice.

State a **working hypothesis** in 2 sentences — candidate aha *shape* (from the seven below) and candidate *position* (pre-signup, first 60 seconds, first session, day 1, day 7) — and confirm it before going further.

### 2. Identify the aha shape

The product will rhyme with one or two of seven documented shapes. Name which fit and why.

- **Volume-of-use.** A usage threshold flips "I'm trying this" to "I live in this." Slack — 2,000 messages per team; Facebook — 7 friends in 10 days; Twitter — 30 follows. Fits habit-forming products with social, communication, or content cores.
- **Collaboration trigger.** Sharing, inviting, or co-creating reveals multi-player value. Dropbox — first file uploaded *and shared*; Notion — first page shared with a collaborator; Calendly — first link shared. Fits collaborative tools, sharing-driven products, marketplaces.
- **First-output.** The product produces a real artifact the user can keep, share, or build on. Lovable — first working app from a prompt; Cursor — first AI-completed line accepted; Granola — first meeting transcribed; Cal AI — personalized plan revealed; ChatGPT — first useful answer. Fits AI products, creative tools, generators.
- **Time-saved.** A task that took minutes or hours takes seconds. Superhuman — Inbox Zero in the first session; Calendly — first meeting booked without email back-and-forth; Stripe — first test payment in 7 lines of code. Fits productivity tools, infrastructure, replacement-for-X products.
- **Personalization-reveal.** The product analyses the user's input and returns a result that feels custom-built. Spotify — Discover Weekly; Cal AI — personalized calorie plan; Headway — personalized reading queue; Headspace — personalized meditation track. Fits content discovery, health/wellness, recommendation-driven products.
- **First-win.** One specific outcome the user can point to and feel good about. Duolingo — first lesson with streak started; Strava — first run logged; Whoop — first sleep score; Apple Fitness — first ring closed. Fits goal-oriented, tracking, fitness, learning products.
- **Pre-signup.** Real value *before* an account — signup becomes saving what they already made. Lovable — homepage prompt box builds an app before signup; Airbnb — browse without login; Spotify — guest play; Perplexity — search without an account. Fits high-friction-to-signup products, viral utilities, products with a strong demo wow.

### 3. Live research on the category

Read [references/benchmarks.md](references/benchmarks.md) for documented comparables and time-to-aha benchmarks, then search live for:

- **2–3 named comparable products** in the same category — each one's documented aha if public, or the most credible inferred one.
- **The category's activation benchmarks** — typical time-to-aha, first-session conversion, day-1 retention bar.
- **AI-specific patterns in this category** — most categories now have an AI-augmented incumbent whose aha is faster and earlier than the pre-AI norm.

Collect 4–6 concrete data points (named products with their aha + sources) before generating candidates. If web search isn't available, say so, ask the member for comparables, and mark those claims unverified.

### 4. Generate three candidate magic moments

Each candidate is specific, evidence-backed, and placed at a real position in the journey. For each, define the seven worksheet fields:

- **Action** — what the user does, in 5–10 words.
- **Wow** — what they see, feel, or unlock in that instant.
- **Where** — pre-signup / first 60 seconds / first session / day 1 / day 3 / day 7 — the earliest position the action can realistically happen, not where it's convenient to build.
- **Time-to-aha** — a concrete bound in seconds, minutes, hours, or session number ("<60 seconds from landing on the homepage"), never "as fast as possible."
- **Comparable evidence** — at least two named products (where possible) whose documented aha rhymes with this candidate. "Other products do this" is not evidence.
- **Risk** — what could go wrong. A candidate without a named risk hasn't been pressure-tested.
- **Metric** — a threshold measurable in product analytics ("X% of new accounts complete Y within Z minutes", "session length ≥ N seconds on session 1").

The three must be **distinct bets**, not three flavours of one idea — pull from different shapes where the product supports it (e.g., for a B2B AI product: one Volume-of-use, one First-output, one Collaboration trigger).

### 5. Recommend a primary

Pick one, weighing in order: **(1) Speed** — fastest to aha from first contact; **(2) Evidence** — strongest comparable evidence in the same category; **(3) Fit** — most consistent with the Offer's Mechanism. State it in one sentence with two sentences of reasoning. The other two stay in the document as alternates if the primary fails its test in 4–6 weeks.

### 6. Show the member and iterate

Present the three with the primary clearly marked and ask: *"Does the recommended primary feel like the right first bet, or does one of the other two fit better for reasons I haven't captured?"* Fold in pushback; iterate once if needed — the member often knows something about the first session that changes the order.

### 7. Write `docs/MAGIC-MOMENT.md`

Use the section structure of `productos/design/2-Magic-Moment.md` exactly — same headers and field labels (Where it sits / Time-to-aha target / Success metric for the primary; the seven fields per candidate; Sources with 3–6 cited references). Replace every `[placeholder]`, drop the worksheet's italic intro, and add a dated line under the title: *Drafted: [Month Year]. Generated from DEFINE.md.* Candidates are bullets, not paragraphs. `mkdir -p docs` if needed; if the file exists, read it first, preserve the member's edits, and show a diff and get approval before overwriting.

## Verify before delivering

- [ ] The primary is one sentence naming a specific action, with position, time-to-aha target, and success metric — no vagueness.
- [ ] Three distinct candidates, each with all seven fields.
- [ ] Comparable evidence cites real named products — at least two per candidate where possible — not generic categories.
- [ ] Time-to-aha targets are concrete; positions are the earliest realistic placement, biased toward pre-signup or first session.
- [ ] Every metric is measurable in product analytics, not vibes.
- [ ] The doc frames the primary as a committed hypothesis to test.
- [ ] Sources cite 3–6 named references; the file is dated and reads in under 3 minutes.

Give the member the file path and a tight recap: one line for the primary, one per candidate, one confirming where in the journey it sits.

**Next:** `design-onboarding-flow` designs the screen-by-screen route that engineers this moment into the first session.
