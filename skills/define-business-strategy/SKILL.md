---
name: define-business-strategy
description: >-
  Use for the optional deep dive into the economics behind the price — when the money questions get real: before paid channels in Distribute, at first revenue, or when an investor asks how the model works. Requires the Offer and Pricing sections of docs/DEFINE.md. Triggers on phrases like "build my business strategy", "what are my margins", "what does each customer cost me", "what's my unfair advantage", "what's my north star metric", "unit economics", "can I afford paid acquisition", or any request to fill in the three-section Business Strategy (Cost & Margin, Unfair Advantage, North Star Metric). Reads the Pricing Strategy's model, unit, plans, and price as given, researches cost benchmarks and category north stars, then walks the user section by section — building the cost-per-customer equation together, critiquing weak moats — and writes the Business Strategy section of docs/DEFINE.md. A BONUS deep dive, not a checklist step: the business model and price are decided in define-pricing.
---

# Define: Business Strategy Deep Dive (optional)

This skill is ProductOS's **optional deep dive** — most people run it when the money questions get real (before paid channels, at first revenue, or when an investor asks), not in week one. The Pricing Strategy has already decided how the business earns, what the price multiplies by, and the number. This skill adds the three things that make those decisions survivable: **Cost & Margin** (does the price survive the heaviest customer?), **Unfair Advantage** (why isn't this cloned in six months?), and the **North Star Metric** (the one number that says the engine is turning).

The goal is not to fill in three boxes. The goal is to make the three answers *lock together with the Pricing Strategy* — so the cost structure supports the price, the unfair advantage explains why the model holds, and the north star tracks the leading indicator of the chosen business model. Most first-draft strategies fail not because any single answer is wrong, but because the answers don't agree with each other or with the price already on the table.

A Business Strategy that contradicts itself silently is more dangerous than one that's obviously wrong, because the founder runs on it for a year before the math catches up. This skill's job is to surface the contradictions before they cost twelve months.

> **Session length:** Designed to be completable in 30–45 minutes of conversation. **All cost benchmarks and category research are Claude's job during the session**, not homework for the user. Cost-per-customer numbers don't need to be measured — Claude builds the estimate with the user from the delivery-cost cheat sheet in `productos/define/BONUS-Pricing-Models.md` and category benchmarks (SaaS 70–85% gross margin, AI apps 40–60%, productized service 40–60% unless solo, marketplaces 20–40% take-rate); the user signs off on the working assumption, which gets re-grounded post-launch with real usage data. Do not relitigate the business model or the launch price here — if the economics say the price is wrong, send the user back to `define-pricing` with the specific number that broke.

## Inputs

Before starting, locate the following. The member's answers live in `docs/DEFINE.md` at the app repo root; the worksheet and references live in the ProductOS folder — `productos/` at the app repo root, or the current folder in a standalone ProductOS checkout. Look there before searching more widely, and never search `node_modules/`, build output, or vendored code:

1. **The Product Offer** — `## 1. Product Offer` in `docs/DEFINE.md`. **Required.** The Mechanism tells you where the variable cost is (AI tokens, storage, payouts, human time); the Proof and Guarantee hint at distribution and the moat.
2. **The Pricing Strategy** — `## 3. Pricing Strategy` in `docs/DEFINE.md`, produced by `define-pricing`. **Required.** Read as given: the business model, billing unit, plans, entry route, cadence, launch price, and the cost-floor assumption behind it. This skill turns that one-line cost floor into a real per-customer equation at low, expected, and heavy use. If it's still a placeholder, stop and run `define-pricing` first — you cannot check economics against a price that doesn't exist.
3. **The Business Strategy worksheet** — usually `BONUS-Business-Strategy-Deep-Dive.md` in the `productos/define/` folder. Defines the section structure, prompts, tables, and `> Good/Bad` criteria. Read it; never write to it. The output goes to `## 4. Business Strategy` in `docs/DEFINE.md` (see step 5).
4. **The Business Strategy examples** — usually `BONUS-Real-Business-Strategy-Examples.md`. Six worked examples across business models (B2B SaaS, indie Mac app, WordPress LTD, productized service, marketplace, usage-based API). Read the Cost & Margin, Unfair Advantage, and North Star rows once at the start to internalize what "good" looks like across these shapes. Use as **calibration**, never as a script to retrofit the user onto.
5. **The Pricing Models reference** — usually `BONUS-Pricing-Models.md`. Read chapter 25's *Check delivery economics* and the delivery-cost cheat sheet; they supply the planning figures for the cost equation.
6. **The Customer Persona** — `## 2. Customer Persona` in `docs/DEFINE.md`, if filled in. Optional; the willingness-to-pay section is the check that the margin math and the buyer's budget agree.
7. **Real traction** — not a file: ask about any real customer replies, conversations, signups, or payments the member has had. Optional but gold. A channel that already pulled is often the unfair advantage; real usage is the north star's first data point.

If any of the required inputs are missing, ask the user where they live before continuing.

## Workflow

### 1. Absorb the pricing decisions and form a working hypothesis

Read the Product Offer and the Pricing Strategy end-to-end (and the Persona and any real traction if available). Extract:

- The business model, billing unit, plans, entry route, cadence, and launch price — as decided. These are inputs, not questions.
- The mechanism's variable cost drivers — AI inference (and failed attempts), storage, payment or platform fees, payouts, human time.
- The cost-floor assumption already in the Pricing Strategy, and whether it was tagged `[working assumption]`.
- Any distribution edge visible in the proof, the persona's watering holes, or the traction so far.
- The category, which usually narrows the north star for you.

From this, form a **working hypothesis** in one paragraph: likely cost-per-customer shape and gross margin band, candidate unfair advantage, candidate north star. State it back to the user and ask them to confirm or correct before doing research.

### 2. Research the economics

Spend real but focused effort here. Use web search and any connected research tools to investigate:

- **Cost benchmarks for the category** — typical gross margin range for the product shape (SaaS ~70–85%, AI apps with API costs often land at 40–60%, though anything under 50% is unhealthy; productized services 40–60% unless solo; for marketplaces the comparable figure is a 20–40% take-rate, not a margin), and current unit costs for the mechanism's expensive parts (model pricing per job, storage, platform fees).
- **The category's typical north star** — what metric do successful companies in this category track publicly? Loom tracks weekly active creators; indie Mac apps track weekly licenses; marketplaces track GMV; usage-based APIs track paid units consumed.
- **The moat candidates** — is there a channel, a community, a data asset, or a portfolio the user already has that comparable businesses built their advantage on?

Collect 4–6 concrete data points before walking the user through the framework. Note explicitly which came from research and which still need user validation.

### 3. Walk the user through the strategy, section by section

Go through the worksheet in order: **1 Cost & Margin → 2 Unfair Advantage → 3 North Star Metric.** Each answer constrains the next: the margin tells you how much room there is to fund a moat, and the moat often names the channel the north star should track.

For each section:

1. **Propose a hypothesis** based on the offer, the Pricing Strategy, and research. Be specific — not "AI costs" but "about $0.02 per document at expected use, $0.035 at heavy use once retries are counted; at $29 for 500 documents the heaviest customer costs $17.50 to serve — a 40% margin, which is thin."
2. **Ask 1–3 targeted questions** to confirm, refine, or reject the hypothesis.
3. **Critique weak answers.** Each section in the worksheet has explicit "good vs bad" criteria — quote them when the user's answer drifts. Also watch for the failure patterns below.
4. **Recommend a sharper version** anchored in the BONUS examples and in research.
5. **Do the best you can in the session.** If the user can't confirm from memory (especially common for Cost & Margin pre-launch), accept Claude's benchmark-based estimate and tag it `[working assumption — re-ground with real data post-launch]` — then continue. A research-backed strategy tagged for validation is a successful output.

### 4. Sections that deserve extra scrutiny

- **Cost & Margin (section 1).** Fill the low / expected / heavy-use table, not just the average. Write the per-customer equation explicitly — AI (including failed attempts) + storage + platform fees + email/auth + human time — with a planning figure on every line. If the heavy-use row goes negative or the gross margin lands under 50% on an AI product, surface it immediately: the fix is a cap, a metered component, or a different unit, and it belongs in the Pricing Strategy — send the user back to `define-pricing` with the specific number.
- **Unfair Advantage (section 2).** The single most-faked section. "We built it first," "our AI is smarter," "we have better UX," "our team" — none of these are moats; they're hopes. A real unfair advantage compounds with time and use. Push for distribution density, niche expertise, audience, switching costs, cross-product portfolio, open-source community, or counter-positioning. **Naming a moat to *build* over the next 12 months is just as valid a session output as naming one you already have** — it just gets tagged as a build commitment rather than a present-tense claim.
- **Cross-cutting coherence.** After all three sections are drafted, read them together with the Pricing Strategy as one paragraph. Does the cost structure support the price? Does the persona's willingness to pay leave room for the margin? Does the north star track the engine of the chosen business model (MRR for subscription, weekly buyers for one-time, paid units for usage, active retainers for services)? If any pair contradicts, fix the upstream one.

### 5. Write the Business Strategy section of `docs/DEFINE.md`

Output: `## 4. Business Strategy` in `docs/DEFINE.md`. The worksheet `BONUS-Business-Strategy-Deep-Dive.md` stays blank; never write answers back into `productos/`.

Read `docs/DEFINE.md` first (it exists — the Pricing Strategy is a required input). Write only `## 4. Business Strategy`; never touch the other sections — if the economics say the price is wrong, the fix goes through `define-pricing`, not an edit here. If the section is already filled, show the user a diff of the proposed change and get approval before overwriting — preserve the member's own edits and surface any conflicts.

Use the worksheet's headings — `### Cost & Margin`, `### Unfair Advantage`, `### North Star Metric` — with clean answers: no italic prompts, no `> Good/Bad` lines, no `**Your answer:**` labels. Keep the cost equation and the filled three-customer contribution table under Cost & Margin; drop the worksheet's option tables (Common unfair advantages, Common north stars by business model).

Open the section with a short **strategy summary** — 2–3 sentences that restate the business model and price from the Pricing Strategy, then the gross margin, the moat, and the north star, so a co-founder can read it in 10 seconds — and close it with one short evidence line — e.g., "Based on: the Product Offer, the Pricing Strategy, 3 cost benchmarks, 0 actual usage data. Recommended next step: re-ground cost-per-customer with the first month of real invoices."

Update the `*Last updated:*` line, and add a `### Business Strategy` entry under `## Sources` listing the benchmark references, model and platform price pages, and any other research used — so the user can re-verify later. Write for a reader without context: spell out acronyms like MRR, GMV, and LTD on first use — `docs/DEFINE.md` is the document the member shares.

### 6. Verify before delivering

Re-read the written strategy against the framework's "good vs bad" criteria and the failure patterns below. Specifically check:

- Does the heavy-use row stay positive, and is gross margin above the category's floor (SaaS ~70%, AI apps 50%)? Can the user recite cost-per-customer from memory?
- Is the Unfair Advantage a real moat (distribution, switching costs, audience, niche expertise, counter-positioning) — or is it "we built it first" with a thesaurus on top?
- Is the North Star **one** metric, with a 90-day target, that matches the business model in the Pricing Strategy?
- Do the three answers and the Pricing Strategy tell **one** story when read in sequence?

Deliver `docs/DEFINE.md` via a `computer://` link and a one-paragraph summary of what is solid and what still needs validation.

## Failure patterns to look for

Common ways a Business Strategy underperforms. Name them when you see them — naming compounds learning:

- **The Unbounded-AI-Cost Margin.** AI app priced as if it had zero variable cost. Margin math collapses the day a power user runs 10x the average tokens. Fix with usage caps per plan, a metered component, BYOK on the top plan, or a different unit — in the Pricing Strategy.
- **The Average Customer.** Margin computed on the average account. The heavy-use row is the one that decides whether the price works; fill it.
- **The "Our Team" Moat.** Unfair Advantage is "we have a great team" or "we built it first." Neither survives a single round of competitive cloning. If the user genuinely can't name a real moat, the right answer is to name one to **build**, not one to claim.
- **The Vanity North Star.** Signups, downloads, social followers. These are leading indicators of *attention*, not of revenue. A subscription business with "signups" as a north star is one that doesn't yet know what it sells.
- **The Mismatched North Star.** North star metric doesn't match the business model. MRR on a one-time-purchase indie Mac app; weekly buyers on a subscription SaaS; GMV on a productized service. Pick a metric that tracks the *engine* of the model chosen in the Pricing Strategy.
- **The Contradiction.** Answers that don't agree with the price already on the table. The Pricing Strategy says $29 flat with unlimited documents; Cost & Margin shows heavy users cost $40. The Persona's willingness-to-pay is $20/month but the margin only works above $50. Mechanism implies heavy AI cost but the margin assumes 85%. These contradictions are silent — they ship and run for a year before the math surfaces. Catch them now, and route the fix to the document that owns the decision.

When you spot one of these, name it. Naming is half the cure.

## Tone and pacing

- **Conversational, not robotic.** The user is making real strategic decisions; treat them like a peer working through a hard problem, not a form to fill in.
- **Push back when answers are weak.** The user invoked this skill to be rigorous; collapsing into agreement is the worst possible outcome. Quote the framework's "bad" criteria, name the failure pattern, and propose a sharper version.
- **One section at a time by default.** The order matters. If the user explicitly asks to batch, oblige — but warn that the coherence check usually needs a second pass.
- **Confirm the working hypothesis before researching deeply.** A 30-second hypothesis check saves a 10-minute wrong-direction detour.
- **Build the math together.** Write the cost-per-customer equation explicitly, line by line, with Claude supplying planning figures where the user has none. The non-negotiable is that the user understands the equation and signs off on the working assumption; it is *not* that the inputs are measured.

## What "done" looks like

A filled `## 4. Business Strategy` in `docs/DEFINE.md` where:

- **Cost & Margin** has an explicit per-customer cost equation, a filled low / expected / heavy-use table with a positive heavy-use contribution, a named gross margin %, and fixed monthly costs covered by current or near-term MRR.
- **Unfair Advantage** names a real, compounding moat — or honestly names one to build over the next 12 months. Both count as done.
- **North Star** is one metric, with a 90-day target, that matches the business model in the Pricing Strategy.
- The three answers and the Pricing Strategy read as **one** story in the strategy summary at the top of the section.
- The `*Last updated:*` line is current and the `### Business Strategy` sources entry is filled.

Recommended next step after a successful session: if the economics changed the price, re-run `define-pricing` for the specific section that broke; otherwise live with the strategy, pick a tracker for the north star, and re-run this skill once a month of real usage data is in.
