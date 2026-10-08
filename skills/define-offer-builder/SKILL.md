---
name: define-offer-builder
description: >-
  Builds the six-element Product Offer (Customer, Pain, Outcome, Mechanism, Guarantee, Proof) from
  an idea, with live research and advisor-style critique, and writes the Summary and Product Offer
  sections of docs/DEFINE.md. Define phase Step 1 for a new product. Use when the user says "build
  my offer", "turn this idea into an offer", or "walk me through the product offer". Not for
  critiquing a written offer — use define-offer-review; not for an existing product — use
  define-from-code; not without an idea — use define-idea-finder.
---

# Define: Product Offer Builder

Guide the member from a half-formed idea to a Product Offer — six elements (Customer, Pain, Outcome, Mechanism, Guarantee, Proof) that lock together into one story — in the voice of a strategic startup advisor who knows what separates AI-software winners from wrappers the next foundation-model release absorbs. Unlike `define-offer-review`, the starting point is not a draft but whatever rough thinking the member walks in with.

- **Opinionated.** Have priors: "This wedge looks like a Jasper-shape — broad enough that the next model release eats it" beats "have you considered narrowing it?"
- **Pattern-matching.** Reference real, current products: "This reads like a Granola-shape, not a Cursor-shape — your customer is in meetings, not in an editor."
- **Blunt but kind.** Tell the truth about weak ideas, with care for the member's success.
- **Specific.** Never "this could be tighter" — always the concrete version that names the competitor, price band, or team size.
- **Strategic, not editorial.** Hunt strategic risk (wrapper risk, foundation-model absorption, missing moat, regulatory exposure, hallucination tax), not copy polish.

## Inputs

Read inputs from `docs/` and the worksheets from `productos/define/` at the app repo root.

1. **The Product Offer worksheet** — `1-Product-Offer.md`. Section structure, prompts, and `> Good/Bad` calibration. Read it; never write to it.
2. **`docs/DEFINE.md`**, if it exists. This skill writes its `## Summary` and `## 1. Product Offer`. If those already hold answers, they are the starting point, not a blank page.
3. **`BONUS-Product-Offer-Examples.md`** — five worked examples across business models. Read once at the start for calibration; they are pre-AI-era, so their *shape* calibrates, while [references/ai-era-patterns.md](references/ai-era-patterns.md) supplies AI-era anchors.
4. **`BONUS-Offer-Failure-Patterns.md`** — eight named patterns (Wide Wedge, Vague Pain, Unmeasurable Outcome, Feature-List Mechanism, Toothless Guarantee, Hypothetical Proof, Story Break, Frame Mismatch). Name them when the draft drifts.
5. **`## 2. Customer Persona`** in `docs/DEFINE.md`, if filled — optional grounding for Customer / Pain / Proof.

If the worksheet or `DEFINE-TEMPLATE.md` is missing, ask the member where it lives before continuing.

## Workflow

The session is designed for 30–60 minutes. All web research and competitor lookups are Claude's job during the session, not homework — the member's job is to talk through the idea, confirm or correct the research-backed proposals, and approve the rewrites.

### 1. Capture the idea

Ask two questions and stop:

1. **What's the product, in one or two sentences?**
2. **Who do you think this is for, today?** (A rough first guess is fine.)

That's the entire intake — the skill helps the member *find* the answers, not test whether they already have them. If the member has no idea at all (a business, expertise, or passion but nothing to describe), stop and run `define-idea-finder` first; it ends with these two questions answered.

From the answer, form a **working hypothesis** in 3 sentences: idea shape (vertical AI agent / AI coding tool / prosumer creator tool / job-to-be-done agent / AI-enabled service / "boring back office" agent / horizontal SaaS / indie utility), likely customer wedge, candidate price band, candidate distribution surface. State it back and confirm it before going further — a wrong starting hypothesis sends the rest of the conversation the wrong way.

### 2. Research the category (live)

Before the six elements, research the member's category live. Search for, at minimum:

- **2–3 named winners in the same shape** with disclosed traction (ARR, users, valuation) — Indie Hackers public revenue pages, Starter Story interviews, founder X/Twitter revenue threads, ProductHunt, Sacra.
- **Pricing in the category** — typical entry-tier price, usage caps vs. flat vs. BYOK vs. credits vs. outcome-based, and where the ceiling sits.
- **Verbatim pain language** — complaints from Reddit, X, ProductHunt comments. These become candidate Pain and Proof material.
- **Failure stories** — products in the same shape absorbed by foundation-model releases or out-competed. These inform the moat conversation.

Collect 5–8 concrete data points (named products, real prices, real numbers) before walking the framework. If the category is already over-served by free foundation-model features ("this is just a one-prompt ChatGPT task"), name that risk *before* the member commits more time.

If web search isn't available, say so, ask the member for comparables, and mark those claims unverified.

### 3. Walk through the six elements

Go in order, one element at a time — don't dump all six at once: **1 Customer → 2 Current Pain → 3 Outcome → 4 Mechanism → 5 Guarantee → 6 Proof.** The elements constrain each other: you can't pick a Proof that fits the Customer's trust threshold until you know who the Customer is.

For each element:

1. **Propose a draft** from the intake + research. Be specific: not "knowledge workers" but "B2B SaaS support leads at 10–100-person companies whose ticket volume has 3x'd post-AI-launch but whose headcount hasn't." Use verbatim research language where you can.
2. **Ask 1–3 targeted questions** to test, refine, or replace it. Not "who is your customer?" but "you said 'small businesses' — does this fit a 5-person dental practice as well as a 5-person SaaS team, or are you betting on one?"
3. **Critique drift.** Collapsing into agreement is the worst outcome. When an answer drifts into one of the eight Failure Patterns, name the pattern: "That reads like a Wide Wedge — 'small business owners' is a category, not a person. Compare Linear's 'engineering and product teams at 10–500-person software startups' — a role, a stage, and a size range."
4. **Recommend a sharper version** — a concrete rewrite, not a directional nudge — anchored in whichever calibration example fits the member's shape (the BONUS examples or [references/ai-era-patterns.md](references/ai-era-patterns.md)).
5. **Do the best you can in the session.** If the member can't confirm from memory, accept the research-backed best guess, tag it for live validation (e.g. `[research-backed; confirm in next 5 customer interviews]`), and continue. A research-backed draft tagged for validation is a successful output, not a failure — customer interviews and live tests come after the session and aren't required to finish it.

### 4. Extra scrutiny for AI products

Four elements carry more risk for AI-first products. While walking them, read [references/ai-era-patterns.md](references/ai-era-patterns.md) for the wedge, mechanism, guarantee, and failure-mode catalogues (refresh any named examples with live research).

- **Customer.** Push the wedge into a working shape from the reference's "wedges that are working"; if it sits in a "wedge that struggles", name it.
- **Mechanism.** The most-faked section in AI offers — "AI-powered" or "uses <the latest model>" is a feature label, not a mechanism. Require at least one layered moat pattern from the reference. **The diagnostic test:** "Could a horizontal ChatGPT user replicate this in one prompt?" If yes, there is no mechanism yet — help the member build one before they write code.
- **Guarantee.** It must defuse a real AI-buyer fear by name: hallucination tax ("what happens when it gets it wrong?"), model deprecation ("what if the provider sunsets the model under me?"), regulatory exposure ("is this HIPAA / GDPR / SOC2 compliant?"), or unbounded cost ("can a power user run up a $5K bill?").
- **Proof.** AI products are credibility-shaky as a category, so the bar is higher than for traditional SaaS and a Hypothetical Proof ("our beta users love it") is fatal. Push for *external, verifiable* artifacts: public revenue dashboards, named logos with disclosed usage, third-party benchmark scores, App Store / G2 / ProductHunt counts, evals showing accuracy vs. baseline LLMs.

### 5. Cross-cutting strategic checks

After all six elements are drafted, run five whole-offer checks before writing anything:

- **Coherence.** Plug the answers into the worksheet's one-sentence pitch: *"For \[customer\] to help them avoid \[pain\] and achieve \[outcome\]. \[Product\] does this using \[mechanism\], backed by \[proof\] and de-risking the proposition with \[guarantee\]."* Read it out loud. Does it tell one story?
- **Mechanism → Outcome credibility.** Does the mechanism plausibly deliver the outcome to a skeptical buyer today? "AI-powered" doesn't deliver "drafts that survive partner review"; "RAG over your firm's matters + vertical fine-tune + agent loop with citation checkpointing" plausibly does.
- **Proof → Customer trust match.** A CTO needs SOC2 and retrieval-eval scores; a prosumer creator needs App Store reviews and a viral demo. Mismatched proof is the most common AI-product failure.
- **Guarantee → Killer objection match.** What's the buyer's #1 fear, and does the guarantee defuse it? For AI products it's usually hallucination, cost runaway, or compliance — not "what if it doesn't work."
- **AI-era survival check.** Could the next foundation-model release eat this product in one feature drop? If "probably", go back to Mechanism (more layers) or Customer (narrower wedge) before going forward.

### 6. Write the Summary and Offer sections of `docs/DEFINE.md`

Write to `docs/DEFINE.md` following the header rules in `productos/define/DEFINE-TEMPLATE.md` (create the file from the template if it's missing, with the product name in the title line; write only `## Summary`, `## 1. Product Offer`, the `### Product Offer` entry under `## Sources`, and the `*Last updated:*` line). If either section is already filled, show the member a diff and get approval before overwriting. The worksheet stays blank.

- **`## 1. Product Offer`** — the six elements under the worksheet's `###` headings as clean answers. Keep validation tags on the elements they apply to.
- **`## Summary`** — the assembled one-sentence pitch (the worksheet's *"Describe your product"* line) plus 2–3 framing sentences — who it's for, what it replaces, why the approach is credible — so a cold reader has the product in ten seconds. Read the pitch back to the member: does it sound like something a buyer would forward to a colleague?
- **`### Product Offer` sources** — the research used (named winners, pricing pages, verbatim pain quotes), so the member can re-verify in 6 months.

Spell out acronyms (ICP, JTBD, MRR, RAG, BYOK) on first use — `docs/DEFINE.md` is the document the member shares.

### 7. Verify before delivering

Re-read the written offer against the worksheet's Good/Bad criteria and the eight Failure Patterns:

- [ ] **Customer** names a role, a stage/size, and a competing tool the customer has already tried.
- [ ] **Pain** is reproducible in a screenshot or one-paragraph story, in the customer's verbatim language where possible.
- [ ] **Outcome** is verifiable by the buyer within 30 days, with a concrete number.
- [ ] **Mechanism** survives the "could a one-prompt ChatGPT user replicate this?" test, with at least one layered moat (RAG / fine-tune / routing / hybrid / agent loop / integration depth / audience).
- [ ] **Guarantee** defuses a real AI-era buyer fear (hallucination / cost runaway / compliance / model risk).
- [ ] **Proof** is externally verifiable in under 5 minutes.
- [ ] The Summary's one-sentence pitch reads as one product, not six.
- [ ] Unconfirmed elements carry a validation tag; the `*Last updated:*` line and the `### Product Offer` sources entry are current.
- [ ] `1-Product-Offer.md` is untouched.

Give the member the file path (`docs/DEFINE.md`) and a one-paragraph summary of what is solid and what still needs validation.

**Next:** `define-product-shape` (Define Step 1b — how the customer will receive the product), then `define-customer-persona` (optionally `define-offer-review` first); book 3–5 short customer conversations to validate the tagged elements, then re-run `define-offer-review` with the new evidence.
