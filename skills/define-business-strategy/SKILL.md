---
name: define-business-strategy
description: >-
  Works out the economics behind the price — cost per customer and gross margin, unfair advantage,
  north star metric — and writes the optional Business Strategy section of docs/DEFINE.md. Use when
  the money questions get real (before paid acquisition, at first revenue, when an investor asks):
  "what are my margins", "unit economics", "what does each customer cost me", "what's my north star
  metric". Requires the Offer and Pricing sections. Not for choosing the business model or price —
  use define-pricing.
---

# Define: Business Strategy Deep Dive (optional)

The optional deep dive — most members run it when the money questions get real (before paid channels, at first revenue, or when an investor asks), not in week one. The Pricing Strategy has already decided how the business earns, the billing unit, and the number; this skill adds what makes those decisions survivable: **Cost & Margin** (does the price survive the heaviest customer?), **Unfair Advantage** (why isn't this cloned in six months?), and the **North Star Metric** (the one number that says the engine is turning). The three answers must lock together with the Pricing Strategy — most first-draft strategies fail because the answers silently contradict each other or the price, and the member runs on that for a year before the math catches up.

Treat the member as a peer making real strategic decisions, and push back when answers are weak — collapsing into agreement is the worst outcome.

## Inputs

Read inputs from `docs/` and the worksheet and references from `productos/define/` at the app repo root.

1. **`## 1. Product Offer`** in `docs/DEFINE.md` — **required**. The Mechanism shows where the variable cost is (AI tokens, storage, payouts, human time); the Proof and Guarantee hint at distribution and the moat.
2. **`## 3. Pricing Strategy`** in `docs/DEFINE.md` (from `define-pricing`) — **required**, read as given: business model, billing unit, plans, entry route, cadence, launch price, and the cost-floor assumption. This skill turns that one-line cost floor into a per-customer equation at low, expected, and heavy use. If it's still a placeholder, stop and run `define-pricing` first — you can't check economics against a price that doesn't exist.
3. **`BONUS-Business-Strategy-Deep-Dive.md`** — the worksheet's section structure, prompts, tables, and `> Good/Bad` criteria. Read it; never write to it.
4. **`BONUS-Real-Business-Strategy-Examples.md`** — six worked examples across business models. Read the Cost & Margin, Unfair Advantage, and North Star rows once at the start as **calibration**, never a script to retrofit the member onto.
5. **`BONUS-Pricing-Models.md`** — read chapter 25's *Check delivery economics* and the delivery-cost cheat sheet; they supply the planning figures for the cost equation.
6. **`## 2. Customer Persona`** in `docs/DEFINE.md`, if filled — optional; its willingness-to-pay is the check that the margin math and the buyer's budget agree.
7. **Real traction** — not a file: ask about real customer replies, conversations, signups, or payments. Optional but gold — a channel that already pulled is often the unfair advantage; real usage is the north star's first data point.

If any required input is missing, ask the member where it lives before continuing.

## Failure patterns

Name these the moment they appear in step 3 (naming is half the cure), and re-check the draft against each in step 6:

- **The Unbounded-AI-Cost Margin.** AI app priced as if it had zero variable cost; the math collapses the day a power user runs 10x the average tokens. Fix with usage caps per plan, a metered component, BYOK (bring your own key) on the top plan, or a different unit — in the Pricing Strategy.
- **The Average Customer.** Margin computed on the average account. The heavy-use row decides whether the price works; fill it.
- **The "Our Team" Moat.** "We have a great team" or "we built it first." Neither survives one round of competitive cloning. If the member genuinely can't name a real moat, name one to **build**, not one to claim.
- **The Vanity North Star.** Signups, downloads, followers — leading indicators of *attention*, not revenue. A subscription business with "signups" as its north star doesn't yet know what it sells.
- **The Mismatched North Star.** MRR on a one-time-purchase Mac app; weekly buyers on a subscription SaaS; GMV on a productized service. Track the *engine* of the model chosen in the Pricing Strategy.
- **The Contradiction.** Answers that disagree with the price on the table: $29 flat with unlimited documents while heavy users cost $40; willingness-to-pay of $20/month while the margin only works above $50; a mechanism implying heavy AI cost while the margin assumes 85%. These ship silently and run for a year — catch them now and route the fix to the document that owns the decision.

## Workflow

The session is designed for 30–45 minutes. **All cost benchmarks and category research are Claude's job during the session**, not homework. Cost-per-customer numbers don't need to be measured: build the estimate with the member from the delivery-cost cheat sheet and category benchmarks; the member signs off on the working assumption, which gets re-grounded post-launch with real usage data.

### 1. Absorb the pricing decisions and form a working hypothesis

Read the Product Offer and Pricing Strategy end-to-end (and the Persona and any real traction). Extract:

- The business model, billing unit, plans, entry route, cadence, and launch price — as decided. These are inputs, not questions: don't relitigate the business model or the launch price here. If the economics say the price is wrong, send the member back to `define-pricing` with the specific number that broke.
- The mechanism's variable cost drivers — AI inference (and failed attempts), storage, payment or platform fees, payouts, human time.
- The Pricing Strategy's cost-floor assumption, and whether it was tagged `[working assumption]`.
- Any distribution edge visible in the proof, the persona's watering holes, or the traction so far.
- The category, which usually narrows the north star.

Form a **working hypothesis** in one paragraph — likely cost-per-customer shape and gross margin band, candidate unfair advantage, candidate north star — and get it confirmed or corrected before researching. A 30-second check saves a wrong-direction detour.

### 2. Research the economics

Spend real but focused effort. Use web search and any connected research tools to investigate:

- **Cost benchmarks for the category** — the typical gross margin range for the product shape (SaaS ~70–85%; AI apps with API costs often land at 40–60%, though anything under 50% is unhealthy; productized services 40–60% unless solo; for marketplaces the comparable figure is a 20–40% take-rate, not a margin), and current unit costs for the mechanism's expensive parts (model pricing per job, storage, platform fees).
- **The category's typical north star** — what successful companies in the category track publicly (e.g. Loom: weekly active creators; indie Mac apps: weekly licenses; marketplaces: GMV; usage-based APIs: paid units consumed).
- **Moat candidates** — a channel, community, data asset, or portfolio the member already has that comparable businesses built their advantage on.

Collect 4–6 concrete data points before walking the framework, noting which came from research and which still need the member's validation.

If web search isn't available, say so, ask the member for comparables, and mark those claims unverified.

### 3. Walk the strategy, section by section

Go through the worksheet in order — **1 Cost & Margin → 2 Unfair Advantage → 3 North Star Metric** — one section at a time; each constrains the next (the margin sets how much room there is to fund a moat; the moat often names the channel the north star tracks). If the member explicitly asks to batch, oblige, but warn that the coherence check usually needs a second pass.

For each section:

1. **Propose a hypothesis** from the offer, the Pricing Strategy, and research. Be specific — not "AI costs" but "about $0.02 per document at expected use, $0.035 at heavy use once retries are counted; at $29 for 500 documents the heaviest customer costs $17.50 to serve — a 40% margin, which is thin."
2. **Ask 1–3 targeted questions** to confirm, refine, or reject it.
3. **Critique weak answers.** Quote the worksheet's "bad" criteria when an answer drifts, and name any pattern from the Failure patterns section.
4. **Recommend a sharper version** anchored in the examples and research.
5. **Do the best you can in the session.** If the member can't confirm from memory (common for Cost & Margin pre-launch), accept the benchmark-based estimate, tag it `[working assumption — re-ground with real data post-launch]`, and continue. A research-backed strategy tagged for validation is a successful output.

### 4. Sections that deserve extra scrutiny

- **Cost & Margin (1).** Build the math together: write the per-customer equation explicitly, line by line — AI (including failed attempts) + storage + platform fees + email/auth + human time — with a planning figure on every line, then fill the low / expected / heavy-use table, not just the average. The non-negotiable is that the member understands the equation and signs off on the assumption, not that the inputs are measured. If the heavy-use row goes negative or an AI product's gross margin lands under 50%, surface it immediately: the fix is a cap, a metered component, or a different unit, and it belongs in the Pricing Strategy — send the member back to `define-pricing` with the specific number.
- **Unfair Advantage (2).** The most-faked section. "We built it first," "our AI is smarter," "better UX," "our team" are hopes, not moats. A real unfair advantage compounds with time and use: distribution density, niche expertise, audience, switching costs, cross-product portfolio, open-source community, or counter-positioning. **Naming a moat to *build* over the next 12 months is as valid an output as naming one already held** — tag it as a build commitment rather than a present-tense claim.
- **Cross-cutting coherence.** Read all three sections with the Pricing Strategy as one paragraph. Does the cost structure support the price? Does the persona's willingness to pay leave room for the margin? Does the north star track the engine of the business model (MRR for subscription, weekly buyers for one-time, paid units for usage, active retainers for services)? If any pair contradicts, fix the upstream one.

### 5. Write the Business Strategy section of `docs/DEFINE.md`

Write to `docs/DEFINE.md` (it exists — the Pricing Strategy is a required input) following the header rules in `productos/define/DEFINE-TEMPLATE.md`: write only `## 4. Business Strategy`, the `### Business Strategy` entry under `## Sources`, and the `*Last updated:*` line. If the economics say the price is wrong, the fix goes through `define-pricing`, not an edit here. If the section is already filled, show the member a diff and get approval before overwriting, surfacing any conflicts with their own edits.

- Use the worksheet's headings — `### Cost & Margin`, `### Unfair Advantage`, `### North Star Metric` — as clean answers. Keep the cost equation and the filled three-customer contribution table under Cost & Margin; drop the worksheet's option tables (Common unfair advantages, Common north stars by business model).
- Open the section with a 2–3 sentence **strategy summary** — the business model and price from the Pricing Strategy, then the gross margin, the moat, and the north star — so a co-founder gets it in 10 seconds. Close it with one short evidence line, e.g. "Based on: the Product Offer, the Pricing Strategy, 3 cost benchmarks, 0 actual usage data. Recommended next step: re-ground cost-per-customer with the first month of real invoices."
- The `### Business Strategy` sources entry lists the benchmark references, model and platform price pages, and other research used.

Spell out acronyms (MRR, GMV, LTD) on first use — `docs/DEFINE.md` is the document the member shares.

### 6. Verify before delivering

- [ ] **Cost & Margin** has an explicit per-customer equation, a filled low / expected / heavy-use table with a positive heavy-use contribution, and a named gross margin % above the category's floor (SaaS ~70%; AI apps 50%).
- [ ] Fixed monthly costs are covered by current or near-term MRR, and the member can recite cost-per-customer from memory.
- [ ] **Unfair Advantage** names a real, compounding moat — or honestly names one to build over the next 12 months — not "we built it first" with a thesaurus on top.
- [ ] **North Star** is **one** metric, with a 90-day target, matching the business model in the Pricing Strategy.
- [ ] The three answers and the Pricing Strategy read as **one** story in the strategy summary; no failure pattern survives.
- [ ] The `*Last updated:*` line and the `### Business Strategy` sources entry are current; the worksheet is untouched.

Give the member the file path (`docs/DEFINE.md`) and a one-paragraph summary of what is solid and what still needs validation.

**Next:** if the economics changed the price, re-run `define-pricing` for the section that broke; otherwise pick a tracker for the north star and re-run this skill once a month of real usage data is in.
