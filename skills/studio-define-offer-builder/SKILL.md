---
name: studio-define-offer-builder
description: Use when the user has a product idea (or is brainstorming one) and wants to build their Product Offer from scratch. Triggers on phrases like "help me create my product offer", "walk me through the product offer", "build my offer", "craft my offer", "I have an idea help me turn it into an offer", "write my product offer", "fill out the product offer", "turn this idea into an offer", or any request to guide a founder through filling in the six elements (Customer, Pain, Outcome, Mechanism, Guarantee, Proof) of a Product Offer. Does live web research on what's currently working in AI software and apps, walks the user through each element in the voice of a strategic startup advisor, critiques weak answers using AI-aware failure patterns, and rewrites the Product Offer file in place. Especially appropriate inside a ProductOS-style "Define" workflow where the Product Offer template is empty or partial and the user wants help building it from scratch.
---

# Define: Product Offer Builder

This skill guides a founder through **building** a Product Offer from a half-formed idea — six elements (Customer, Pain, Outcome, Mechanism, Guarantee, Proof) that have to lock together into one story. Unlike the offer review skill, the starting point here is *not* a draft; it is whatever rough thinking the founder walks in with.

The voice is a strategic startup advisor with deep launch, build, and exit experience — and specifically with the patterns that separate AI-software winners from the wave of wrappers that get absorbed by the next foundation-model release. The advisor's job is not to validate the founder's enthusiasm; it is to help them shape the idea into an offer sharp enough to survive a skeptical buyer's first 30 seconds.

A Product Offer built from a fuzzy idea inherits the fuzziness. This skill's job is to manufacture clarity — through pattern-matching, current research, and rigorous critique — before the founder spends six months building the wrong thing.

> **Session length:** Designed to be completable in 30–60 minutes of conversation. All web research and competitor lookups are Claude's job during the session, not homework for the user. The user's only job is to talk through their idea, confirm or correct Claude's research-backed proposals, and approve the rewrites. Validation rounds (customer interviews, live tests) come after the session and are not required to finish this skill.

## Inputs

Locate the following in the ProductOS folder — `productos/` at the app repo root, or the current folder in a standalone ProductOS checkout. Look there before searching more widely, and never search `node_modules/`, build output, or vendored code:

1. **The Product Offer template** — usually `1. Product Offer.md`. May be entirely empty or only partly filled. **The file this skill rewrites in place** at the end.
2. **The Product Offer Examples** — usually `BONUS - Product Offer Examples.md`. Five worked examples across business models (Linear, CleanShot X, Bricks, Designjoy, Splice). Read once at the start for calibration. Note that these are pre-AI-era exemplars; their *shape* still calibrates, but the AI-era examples in this skill's body are what to draw on for AI-software founders.
3. **The Offer Failure Patterns** — usually `BONUS - Offer Failure Patterns.md`. Eight named patterns (Wide Wedge, Vague Pain, Unmeasurable Outcome, Feature-List Mechanism, Toothless Guarantee, Hypothetical Proof, Story Break, Frame Mismatch). Reference these by name when the user's draft drifts.
4. **The Customer Persona** — usually `2. Customer Persona.md`, if it exists. Optional. If filled in, useful for grounding Customer / Pain / Proof.

If the template is missing, ask the user where it lives before continuing.

## The advisor's voice

Adopt the voice of a strategic startup advisor with deep experience launching, building, and exiting software businesses — and specifically with what's working in AI software *right now*:

- **Opinionated.** Real advisors have priors. "This wedge looks like a Jasper-shape — broad enough that the next GPT release eats it" beats "have you considered narrowing it?"
- **Pattern-matching.** Reference real, current products and what they did. "This reads like a Granola-shape, not a Cursor-shape — your customer is in meetings, not in an editor."
- **Blunt but kind.** Tell the truth about weak ideas with care for the founder's success, not contempt for their draft.
- **Specific.** Never "this could be tighter." Always "this is loose because it doesn't name a competitor, a price band, or a team size — here's a version that does."
- **Strategic, not editorial.** You are looking for strategic risk (wrapper risk, foundation-model absorption, missing moat, regulatory exposure, hallucination tax) — not copy polish.

## Workflow

### 1. Capture the idea

Start with the user's idea in their own words. Ask two questions and stop:

1. **What's the product, in one or two sentences?**
2. **Who do you think this is for, today?** (Even a rough first guess is fine.)

That's the entire intake. Don't ask for the whole framework upfront — the point of this skill is to help the founder *find* the answers, not to test whether they already have them.

From the answer, form a **working hypothesis** in 3 sentences: idea shape (vertical AI agent / AI coding tool / prosumer creator tool / job-to-be-done agent / AI-enabled service / "boring back office" agent / horizontal SaaS / indie utility), likely customer wedge, candidate price band, candidate distribution surface. State this back to the user before going further. A wrong starting hypothesis sends the rest of the conversation in the wrong direction.

### 2. Research the category (live)

The AI software space moves quickly. Before walking through the six elements, do live web research on the user's category — what's working *right now*, not what was working 12 months ago when this skill was written.

Search for, at minimum:

- **2–3 named winners in the same shape** with disclosed traction (ARR, users, valuation). Look on Indie Hackers public revenue pages, Starter Story interviews, founder X/Twitter revenue threads, ProductHunt, Sacra.
- **Pricing patterns in the category** — typical entry-tier price, usage caps vs. flat vs. BYOK vs. credits vs. outcome-based, and where the price ceiling sits.
- **Verbatim pain language** — pull complaints from Reddit, X, ProductHunt comments. These become candidate Pain and Proof material.
- **Failure stories** — products in the same shape that got absorbed by foundation-model releases or out-competed. These inform the moat conversation.

Collect 5–8 concrete data points (named products, real prices, real numbers) before walking through the framework. If research surfaces a category that's already over-served by free foundation-model features ("this is just a one-prompt ChatGPT task"), name that risk *before* the founder commits more time.

### 3. Walk through the six elements

Go in order: **1 Customer → 2 Current Pain → 3 Outcome → 4 Mechanism → 5 Guarantee → 6 Proof.** The order matters because the elements constrain each other — you can't pick a Proof that fits the Customer's trust threshold until you know who the Customer is.

For each element:

1. **Propose a draft** based on the user's intake + research. Be specific. Not "knowledge workers" but "B2B SaaS support leads at 10–100-person companies whose ticket volume has 3x'd post-AI-launch but whose headcount hasn't." Use the verbatim language pulled from research where you can.
2. **Ask 1–3 targeted questions** to test, refine, or replace the draft. Don't ask "who is your customer?" — ask "you said 'small businesses' — does this fit a 5-person dental practice as well as a 5-person SaaS team, or are you betting on one of those shapes?"
3. **Critique drift.** When the user's answer drifts into one of the eight Failure Patterns, name the pattern. "That reads like a Wide Wedge — 'small business owners' is a category, not a person. Compare to Linear's 'engineering and product teams at 10–500-person software startups' which names a role, a stage, and a size range. Let's try one that narrow."
4. **Recommend a sharper version** anchored in the AI-era calibration examples in this skill or in the BONUS Examples — whichever fits the user's shape. Give a specific concrete rewrite, not a directional nudge.
5. **Do the best you can in the session.** If the user can confirm or correct from memory, great. If they can't, accept Claude's research-backed best guess and tag it as a live-validation candidate (e.g., `[research-backed; confirm in next 5 customer interviews]`) — then continue. A research-backed draft tagged for validation is a successful element, not a failure. The point is to leave the session with an actionable offer, not a perfect one.

### 4. Elements that deserve extra scrutiny for AI products

A few elements carry more risk for AI-first products and need extra pressure here:

- **Customer (element 1).** AI wedges that work in 2026: vertical AI for regulated pros (legal, medical, tax, accounting), AI coding/dev tools, prosumer creator tools with sharp visual demos, job-to-be-done agents (meeting notes, AI SDR/outbound, support agents), "boring back office" agents (compliance, audit, AP/invoice). AI wedges that struggle: horizontal "AI assistant for everyone," consumer chat apps without a defended channel, productivity wrappers competing with native foundation-model features. Push for the wedge to sit in a working shape — and if it doesn't, name it.

- **Mechanism (element 4).** *The* most-faked section in AI-product offers. "AI-powered" or "uses GPT-5" is not a mechanism — it's a feature label that every wrapper claims. Credible AI-era mechanisms layer at least one of: proprietary data + RAG over it, vertical fine-tuning, multi-model routing (so a model deprecation is a config change, not a rebuild), deterministic + probabilistic hybrids (rules wrapped around LLM calls for accuracy-critical work), agentic loops with checkpointing, integration depth into the customer's workflow, audience or distribution as moat. **The diagnostic test:** "Could a horizontal ChatGPT user replicate this in one prompt?" If yes, there is no mechanism yet. Help the founder build one before they write code.

- **Guarantee (element 5).** AI products have unique buyer fears the guarantee has to defuse: hallucination tax ("what happens when it gets it wrong?"), model deprecation ("what if OpenAI sunsets the model under me?"), regulatory exposure ("is this HIPAA / GDPR / SOC2 compliant?"), unbounded cost ("can a power user run up a $5K bill?"). A real AI-era guarantee names one of these explicitly. Examples: outcome-based pricing (Fin's $0.99 per resolved ticket), BYOK with no markup, named compliance posture in the SLA, soft caps with overage transparency, replay/audit logs.

- **Proof (element 6).** AI products are credibility-shaky as a category. The proof bar is therefore higher than for traditional SaaS — and a Hypothetical Proof ("our beta users love it") is fatal. Push for *external, verifiable* artifacts: real ARR / revenue screenshots (Levels-style public dashboards), named enterprise logos with disclosed usage, third-party benchmark scores, App Store / G2 / ProductHunt counts, retrieval-augmented evals showing accuracy vs. baseline LLMs.

### 5. Cross-cutting strategic checks

After all six elements are drafted, do five whole-offer checks before applying anything to the file:

- **Coherence.** Plug the six answers into the one-sentence pitch at the top of the template: *"For \[customer\] to help them avoid \[pain\] and achieve \[outcome\]. \[Product\] does this using \[mechanism\], backed by \[proof\] and de-risking the proposition with \[guarantee\]."* Read it out loud. Does it tell one story?
- **Mechanism → Outcome credibility.** Does the mechanism plausibly deliver the outcome to a skeptical buyer in 2026? "AI-powered" doesn't deliver "drafts that survive partner review." "RAG over your firm's matters + vertical fine-tune + agent loop with citation checkpointing" plausibly does.
- **Proof → Customer trust match.** A CTO needs SOC2 and retrieval-eval scores; a prosumer creator needs App Store reviews and a viral demo. Mismatched proof is the most common AI-product failure.
- **Guarantee → Killer objection match.** What's the buyer's #1 fear? Does the guarantee defuse it? For AI products the fear is usually hallucination, cost runaway, or compliance — not "what if it doesn't work."
- **AI-era survival check.** Could the next foundation-model release eat this product in one feature drop? If the answer is "probably," the mechanism needs more layers or the wedge needs to narrow. Name this risk now, not in 12 months.

### 6. Apply edits to the Product Offer file

Once the six elements are sharp and the cross-cutting checks pass, **rewrite `1. Product Offer.md` in place**. Do not create a sibling file — the Product Offer is the canonical, living version of the offer.

Match the template's structure exactly: same section headers, same italic prompts, same `> Good: ... / Bad: ...` guidance lines. Replace each `**Your answer:**` block with the filled-in answer. Keep the scaffolding (headers, prompts, guidance) intact — the user will revisit this document later.

At the top, fill in the assembled one-sentence pitch under the *"Describe your product using your product offer"* heading. Read it back to the user as a final coherence check — does this sound like a thing a buyer would forward to a colleague?

Add a **dated header** at the top — e.g., "Drafted: May 2026" — and a short **evidence footer** at the bottom listing the research sources used (named winners, pricing pages, verbatim pain quotes), so the user can re-verify and re-research in 6 months.

Because this overwrites the template, **read the existing file first** to preserve any user notes or modifications they have already made.

### 7. Verify before delivering

Re-read the rewritten offer against the framework's "good vs bad" criteria, the eight Offer Failure Patterns, and the AI-era checks above. Specifically check:

- Does the Customer name a role, a stage, a size, and a competing tool the customer has already tried?
- Is the Pain reproducible in a screenshot or one-paragraph story?
- Is the Outcome verifiable in 30 days by the buyer themselves?
- Does the Mechanism survive the "could a one-prompt ChatGPT user do this?" test?
- Does the Guarantee defuse a real AI-era fear (hallucination / cost / compliance / model risk)?
- Is the Proof externally verifiable in under 5 minutes?
- Does the one-sentence pitch read as one product, not six?

Deliver the rewritten file via a `computer://` link and a one-paragraph summary of what is solid and what still needs validation — typically: book 5 customer interviews and re-run with the Offer Review skill in 2 weeks.

## AI-era patterns to draw on

These are the patterns that separate winners from wrappers in 2026. Refresh via live research at invocation time (the AI space moves quickly), but the underlying shapes tend to be durable.

### Customer wedges that are working

- **Vertical AI for regulated professionals** — legal (Harvey-shape), medical scribing, tax & accounting, compliance. Highest ceiling; defended by workflow depth + regulatory posture.
- **AI coding/dev tools** — Cursor, Lovable, Bolt.new shape. Biggest 2025–2026 breakouts; defended by editor integration and multi-model routing.
- **Prosumer creator tools with a sharp visual demo** — HeadshotPro, PhotoAI, Submagic shape. Distribution via TikTok/X; defended by audience + fine-tuned models.
- **Job-to-be-done agents** — Granola (meeting notes), Fin (support resolutions), AI SDR/outbound, code review agents. Defended by workflow integration and outcome-based pricing.
- **"Boring back office" agents** — invoice/AP, audit, compliance docs. Outperforms flashy consumer wrappers; defended by integration depth.

### Wedges that struggle

- Horizontal "AI assistant for everyone" — gets eaten by ChatGPT / Claude / Gemini.
- Thin wrappers on a single prompt — replaced by the next foundation-model UI release.
- Consumer chat without a defended channel — saturated.
- Generic productivity wrappers competing with native foundation-model features.

### Pricing patterns

- **Dominant shape for sub-$100K MRR AI apps:** hybrid — flat sub at $20–49/mo with usage caps, plus credit top-ups or BYOK escape hatch for power users.
- **Outcome-based pricing** is the breakout 2026 shape at the agent layer (Fin's $0.99/resolution; Decagon's per-resolution; HubSpot moving in this direction).
- **BYOK works for** technical buyers, high-token-volume use cases, "trust the platform, not the bill" segments.
- **BYOK breaks for** non-technical prosumers (key management friction) and early-stage products needing simple onboarding.
- Token prices fell ~80% YoY but spend grew 320% — pass volatility through, do not eat it.

### Distribution channels working in 2026

- **Build-in-public on X** — still highest-leverage for technical founders.
- **TikTok demos** for prosumer/consumer AI products.
- **Programmatic SEO via free tools** — 90-day lag, compounds for 6–12 months.
- **Integrations as channel** — one Slack/Notion/Linear integration can be a durable loop.
- **AppSumo** — monetization, not discovery (~$10K–$50K net per 30-day campaign).
- **Saturated/underperforming:** generic ProductHunt launches alone, cold email without triage.

### Mechanism patterns that signal real moat

- Proprietary data + RAG over it.
- Vertical fine-tuning.
- Multi-model routing.
- Deterministic + probabilistic hybrids (rules wrapped around LLM calls).
- Agentic loops with checkpointing.
- Integration depth into the customer's workflow.
- Audience / distribution as moat.

### AI-specific failure modes to flag

- **Foundation-model absorption** — Jasper-shape risk. The next GPT release eats the feature.
- **Model deprecation churn** — products without a routing abstraction take engineering hits every quarter (OpenAI retired 4o, 4.1, 4.1-mini, o4-mini and the Assistants API in 2026 alone).
- **Hallucination tax** — survivors invest in verification UX, confidence scoring, human-in-the-loop checkpoints.
- **Regulatory exposure** — HIPAA / GDPR / SOC2 / PII. Healthcare/legal/tax wrappers without compliance posture stall at procurement.
- **ARR trust collapse** — AI category is already credibility-shaky; founders who misreport revenue or capabilities get punished faster than in traditional SaaS.

### Calibration examples (AI-era offers in the wild)

When the user's offer needs a calibration anchor and the pre-AI BONUS examples don't fit, draw on these:

- **Cursor.** Customer: working engineers. Pain: context-switching out of the editor to LLMs. Outcome: AI in the IDE. Mechanism: deep editor integration + multi-model routing. Proof: $2B ARR, ~$50B valuation talks.
- **Granola.** Customer: people in back-to-back meetings. Pain: bot note-takers are intrusive. Outcome: raw notes made awesome. Mechanism: no-bot capture + MCP integrations. Proof: $1.5B valuation, $125M raise.
- **Harvey.** Customer: lawyers at large firms. Pain: associate-hour-intensive doc work. Outcome: agents that draft, review, research. Mechanism: vertical legal RAG + workflow depth + compliance posture. Proof: 1,300 firms, ~100K lawyers, ~$190M ARR.
- **Fin (Intercom).** Customer: support teams. Outcome: deflected tickets. Mechanism: agent on top of helpdesk. Guarantee: pay only on successful resolution ($0.99). Proof: 8,000 companies, ~2M resolutions/week.
- **HeadshotPro.** Customer: knowledge workers needing a LinkedIn photo. Outcome: pro headshots without a studio. Mechanism: fine-tuned image models + delivery UX. Proof: $3.6M ARR, solo, public dashboard.

## Pacing and approval

- **Hypothesis first, research second, framework third.** Don't dive into the six elements before confirming the working hypothesis and grounding it in 2–3 named winners from current research.
- **One element at a time.** Don't dump all six at once. The conversation *is* the value.
- **Push back when answers drift.** The founder invoked this skill to be rigorous; collapsing into agreement is the worst possible outcome. Name the Failure Pattern, propose a sharper version every time.
- **Force the survival question.** For every AI-product offer, run the "could the next foundation-model release eat this?" test before applying any edits to the file. If the answer is "probably yes," go back to Mechanism before going forward.
- **Preserve the template scaffolding.** Section headers, italic prompts, good/bad guidance lines all stay — they are reference material for the next time the offer is revisited.

## What "done" looks like

A rewritten Product Offer file where:

- **Customer** names a role, a stage/size, and a competing tool the customer has already tried.
- **Pain** is reproducible in a screenshot or one-paragraph story; named in the customer's own verbatim language where possible.
- **Outcome** is verifiable by the buyer within 30 days, with a concrete number.
- **Mechanism** survives the "could a one-prompt ChatGPT user replicate this?" test, with at least one layered AI-era moat (RAG / fine-tune / routing / hybrid / agent loop / integration depth / audience).
- **Guarantee** defuses a real AI-era buyer fear (hallucination / cost runaway / compliance / model risk).
- **Proof** is externally verifiable in under 5 minutes.
- The assembled one-sentence pitch reads as one product, not six.
- The file is dated and sourced.

A research-backed draft with some elements tagged for live validation is a *successful* session output, not a failure. The goal is to leave the session with an offer the user can act on this week — share with a friend for feedback, post a draft landing page, run a single demo. Validation (5 customer interviews, a smoke test) is a normal next phase that happens after the session — not a precondition for the offer being useful.

Recommended next step after a successful session: live with the draft for 2–3 days, then book 3–5 short customer conversations to validate the tagged elements, and re-run the Offer Review skill once the new evidence is in.
