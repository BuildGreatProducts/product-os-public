---
name: studio-define-product
description: Use when the user has filled in the Define-phase documents (Product Offer, Customer Persona, Pricing Strategy, Mini-Launch) and wants a single concise summary of the entire product strategy. Triggers on phrases like "create PRODUCT.md", "synthesise my define docs", "summarise my product", "roll up the define folder", "build my PRODUCT doc", "condense my strategy", "one-page product summary", "create a readable summary of my product", or any request to merge the Define documents into a single readable summary. Reads all the source documents, translates framework jargon into plain English, and produces an 8-section PRODUCT.md (Summary, Customer, Problem, Mechanism, Why, Business model, Proof, Goal) in the docs folder — readable in 4–6 minutes by a co-founder, designer, advisor, or new hire without context. Especially appropriate as the final step in a ProductOS-style Define workflow.
---

# Define: PRODUCT.md Synthesis

This skill takes the Define-phase documents — **Product Offer**, **Customer Persona**, **Pricing Strategy**, and **Mini-Launch** (plus the launch log and the optional Business Strategy Deep Dive, when they exist) — and synthesises them into a single readable **PRODUCT.md** that sits in `docs/` at the project root. The output is what a co-founder, designer, advisor, or first hire could read in 4–6 minutes and walk away knowing exactly what the product is, who it's for, why it wins, how it makes money, and how we'll know if it's working.

The source documents are deliberately rigorous — they hold the founder to specifics, named entities, and concrete numbers. They also lean on acronyms — *ICP, JTBD, MRR, ARR, GTM, RAG, BYOK, TAM/SAM/SOM* — that work fine inside the founder's working documents but quietly shut out anyone reading PRODUCT.md without that vocabulary. **This skill's job is to spell those acronyms out, not to strip wider framework language.** Terms like *wedge, anti-persona, north star, moat, freemium, willingness to pay* are well-understood in startup and design conversation and read more clearly than their long-form alternatives — those stay. The skill keeps every substantive fact (real numbers, named competitors, customer-voice quotes, concrete prices) and trims only the abbreviations and over-qualification.

The output is intentionally succinct without being shallow. Each of the eight sections is a focused paragraph that contains everything substantive from the source documents, written in plain English a smart friend at a dinner party could follow.

> **Session length:** Designed to be completable in 15–30 minutes of conversation. The skill reads the source documents, then drafts each of the eight sections one at a time — presenting the draft, asking for confirmation or amendments, folding the user's feedback in, and only then moving on to the next section. Once all eight are locked in, the assembled document gets one final look and then writes to file. No external research is required — all the input lives in the `productos/define/` folder.

## Inputs

Locate the source documents in `productos/define/` (or `define/` in a standalone ProductOS checkout). Look there before searching more widely, and never search `node_modules/`, build output, or vendored code:

1. **The Product Offer** — usually `1-Product-Offer.md`. The single most important input. Provides Customer, Pain, Outcome, Mechanism, Guarantee, Proof, and the assembled one-sentence pitch.
2. **The Customer Persona** — usually `2-Customer-Persona.md`. Provides the texture for the Customer and Problem sections — role, life context, the specific moment when the problem shows up, the customer's verbatim pain language, and the anti-persona for the *"Not for: ..."* closer.
3. **The Pricing Strategy** — usually `3-Pricing-Strategy.md`. Provides the Business model section: who pays, the launch price, and the anchors it sits against.
4. **The Mini-Launch** — usually `4-Mini-Launch.md`, plus **the Launch Log** at `docs/LAUNCHES.md` if it exists. Provides the Proof section's first-party evidence — real replies from potential customers, dated, warm/cold labelled, plus the believers list and the current rung on the signal ladder — and often the freshest customer-voice quotes in the folder. The Goal section's near-term bar is the ladder's next rung.
5. **The Business Strategy Deep Dive** — `BONUS-Business-Strategy-Deep-Dive.md`, *if the user has done the optional deep dive*. When filled, it upgrades the Business model section (revenue model, pricing ladder, cost & margin), the Why section (unfair advantage), and the Goal section (north star metric). When empty, skip it silently — the Pricing Strategy and launch log carry those sections.

If the Product Offer, Customer Persona, or Pricing Strategy is missing or substantively empty (still has `**Your answer:**` placeholders in most sections), stop and tell the user which one needs to be filled in first, and which sibling Define skill produces it (e.g., *"Customer Persona is mostly empty — run `studio-define-customer-persona` first"*). A synthesis is only as good as the documents it summarises; do not proceed with thin inputs.

**The Mini-Launch is recommended but not blocking.** If it's empty, note that the Proof section has no first-party signal yet, recommend running `studio-launch` (the whole point of the phase's quick win), and proceed if the user wants to. The Business Strategy Deep Dive is optional by design — never block on it or nag about it.

## Output

Write to **`docs/PRODUCT.md`** at the project root. If the `docs/` folder doesn't exist, create it. If `PRODUCT.md` already exists, read it first; build the new version; if there are meaningful differences from the existing file, show the user the diff in conversation; overwrite on the user's approval.

## Workflow

### 1. Locate and check the source documents

Verify the source files exist and have been filled in beyond template defaults — the Product Offer, Customer Persona, and Pricing Strategy are required; the Mini-Launch is recommended; the Business Strategy Deep Dive is optional (see Inputs). If any doc is thin or missing, name the gap and recommend the next step before continuing.

### 2. Read and absorb all the source documents end to end

Read every source document fully. Extract the substantive content from each section — the real numbers, the named entities (competitors, communities, tools, customers, podcasts, prices), the verbatim customer quotes, the specific moments and frequencies. These are the load-bearing facts that **cannot** be cut in synthesis.

Also extract the framework labels and internal jargon — these are the things that **will** be cut.

### 3. Draft and confirm each section, one at a time

Build the eight sections in order, drawing only from the source documents and translating into plain English using the table in step 4.

**Critical workflow note:** *do not* draft the whole document and then read it back at the end. Instead, draft one section, present it in the conversation, ask the user for confirmation or amendments, fold their feedback in, and only then move on to the next section. This keeps the user actively in the loop and surfaces translation issues — jargon that snuck through, content the user wants surfaced differently, a customer quote the user wants restored — one section at a time, when they're easy to fix. Doing all eight at once and presenting a wall of prose is the wrong shape for this skill; section-by-section is the point.

For each section:

1. **Draft** the paragraph from the relevant source-doc sections using the translation table in step 4 below.
2. **Present** it to the user, labelled clearly — e.g., *"Here's the draft **Customer** section: …"*
3. **Ask** one specific question: *"Does this read accurately? Anything to add, cut, or reword?"*
4. **Iterate** on user feedback until they approve. Terse approvals (*"looks good," "yes"*) count as approval — move on. If the user has specific edits, fold them in and re-present that section only.
5. **Lock it in.** Keep the approved text as the working version of that section. Move to the next.

The section definitions below describe what content each one pulls from where. Use them as the drafting recipe for each turn of the loop.

**Header.** Product name (pull from the Offer's *"Describe your product"* section if present; ask the user if it's not obvious). One-line tagline if available. *"Last updated: [today's date in plain format, e.g., May 2026]"*.

**Summary.** Open with the assembled elevator pitch from the Offer, rewritten if it reads stilted. Follow with 2–3 sentences that frame the product — what kind of thing it is, who broadly it's for, the headline outcome. Someone could read just this section and know what's being built.

**Customer.** A paragraph that names the customer's role and life context, the specific moment when the problem shows up (place, device, mood — from the Persona's Problem Context), what they currently do about it (Behaviors & Habits), and a short *"Not for: ..."* closer drawn from the Anti-Persona. Pull from Persona sections 1, 2, 3, and 12.

**Problem.** A paragraph that describes the pain in the customer's own words — pull verbatim language from the Persona's Pains & Frustrations if available. Name the trigger event (Persona section 6), how often it happens, and the concrete cost (time, money, emotional load). Note what the customer is doing today instead (Persona's Current Alternatives) and why that isn't enough.

**Mechanism.** A paragraph that explains how the product works in plain English. Translate the Offer's Mechanism out of jargon — RAG becomes *"uses your firm's documents to ground the AI's answers,"* fine-tuning becomes *"trained specifically on [the relevant domain],"* multi-model routing becomes *"automatically picks the best AI model for each task."* Describe what the customer actually does and sees when they use it. Call out what makes the approach win where others have failed.

**Why.** A paragraph on why this wins, in plain terms. If the Business Strategy Deep Dive is filled, pull its Unfair Advantage — distribution, audience, niche expertise, switching costs, integrations, counter-positioning, or a moat being deliberately built over the next 12 months. If not, build it from the Offer's Mechanism (what this approach does that alternatives don't) and any early edge visible in the launch log — a channel that already responds, believers who already lean in. Close with the Offer's Guarantee, framed as the specific risk the product takes off the buyer's table.

**Business model.** A short paragraph on how the product makes money. From the Pricing Strategy: who pays, the launch price and billing shape, and the anchors it sits against. If the Business Strategy Deep Dive is filled, add the revenue model, tiers, and cost-per-user where strategically interesting (e.g., AI-margin pressure shaping pricing structure) — otherwise one honest launch price, plainly stated, is the correct amount of business model at this stage.

**Proof.** A paragraph covering three beats. (1) What proves the market exists today — named competitors and the anchor products people already pay for, drawn from the Offer's Proof and the Pricing Strategy's anchors. (2) What proves this product specifically — testimonials, reviews, named customers from the Offer's Proof, plus the first-party signal from the Mini-Launch and launch log (dated replies, labelled warm or cold — "three strangers replied to the priced post in week two" is real proof at this stage, and the believers list is a named asset). (3) What we're testing next — the next launch on the ladder, its channel, and its pass bar (e.g., "next: the Design relaunch to the same thread; the bar is one 'can I try it?'").

**Goal.** A short paragraph on what we're tracking. The near-term bar is the signal ladder's next rung, from the launch log (*"next rung: one activated user, at the beta invite"*). If the Business Strategy Deep Dive is filled, add the north star metric in plain English with its 90-day target. Close with what would make us change course — the ladder's own rule: the same rung missed twice is a pivot conversation.

**Footer.** *"Based on: Product Offer (dated [date]), Customer Persona (dated [date]), Pricing Strategy (dated [date]), Mini-Launch (shipped [date])."* — listing whichever source docs are filled in, including the Launch Log and the Business Strategy Deep Dive when present. Add relative links to each source doc so any reader can drill down.

### 4. Spell out acronyms

Expand the acronyms below — they shut out any reader who hasn't memorised the abbreviation. Wider framework terms (*wedge, anti-persona, north star, moat, freemium, willingness to pay, pivot criteria, proven demand, fine-tuning, agent loop*) are fine to leave in place; they read more clearly than their long-form alternatives and a reader working on a product strategy will recognise them. Stripping every framework term would make the document feel watered down.

| Acronym | Expand to |
| --- | --- |
| ICP | "ideal customer" or just "the customer" |
| JTBD | "job-to-be-done" |
| GTM | "go-to-market" |
| TAM / SAM / SOM | describe the market in concrete terms (size, who's in it, who you can reach) |
| MRR / ARR | "monthly revenue" / "yearly revenue" |
| BYOK | "bring-your-own-key" (or describe: *"users connect their own AI account"*) |
| RAG | "retrieval-augmented generation" (or describe: *"uses your documents to ground the AI's answers"*) |

For domain-specific acronyms that appear in the source docs but aren't on this list (e.g., SOC2, HIPAA, SaaS, SDK), use judgement: expand on first use if there's any chance a non-startup reader wouldn't know it, then use the acronym thereafter.

Also strip:

- Repeated qualifiers (*specific*, *concrete*, *named*) — let the specifics themselves do the work.
- Process language (*we surveyed*, *based on research*) unless it's load-bearing for credibility.
- Hedging that doesn't add information (*broadly speaking*, *generally*).
- Section labels from the source docs (*Section 1 says*, *In the Persona*).

Keep:

- Real numbers — prices, frequencies, costs, targets, revenue figures.
- Named entities — competitors, tools, communities, customers, podcasts.
- Customer-voice quotes — the most credible artefact in the document.
- Specifics that make the document feel tangible (a moment, a device, a place).
- Well-understood framework terms (*wedge, anti-persona, north star, moat, freemium, willingness to pay, pivot criteria, proven demand*) — these are clearer in context than the long-form alternatives.

### 5. Final assembly look

Each section has already been approved individually in step 3, so this step is a quick final look at the full document — header, the eight locked-in sections in order, and the footer — to catch any cross-section issues: repetition between sections, abrupt transitions, the same number cited three different ways, or anything that reads off when stitched together. Ask one question: *"Anything that reads off across the whole thing?"* Iterate once if needed; the heavy lifting was done section by section in step 3.

### 6. Write the file

Once the user approves, write to `docs/PRODUCT.md`. Create the `docs/` folder if it doesn't exist (using a bash `mkdir -p` if necessary). If `PRODUCT.md` already exists, the read-back step in section 5 is the user's approval to overwrite.

### 7. Verify before delivering

Re-read the rewritten file and check:

- Every section is a focused paragraph (not a single sentence, not a bullet list).
- No unexpanded acronyms survived (search for *ICP, JTBD, GTM, TAM, SAM, SOM, MRR, ARR, BYOK, RAG*) — except where they appear inside a "Acronym (expanded form)" parenthetical.
- Real numbers, named entities, and customer-voice quotes are preserved from the source docs.
- The footer is dated and links to each filled-in source doc.
- The whole document reads end-to-end in 4–6 minutes.

Deliver via a `computer://` link.

## Tone and pacing

- **Plain English throughout.** If you wouldn't say it to a smart friend at a dinner party, rewrite it.
- **One paragraph per section.** Not bullet lists. Not single sentences. A focused paragraph that contains everything substantive from the corresponding source-doc sections.
- **Specific over abstract.** *"$49/month, paid quarterly"* beats *"flexible pricing options."* *"3:17am with a baby on his chest"* beats *"frustrating moments."*
- **No cutting of facts.** The skill summarises *language*, not *content*. Every real number, named entity, and customer-voice quote in the source docs should survive into PRODUCT.md.
- **Read the whole thing aloud before delivering.** If a section trips the tongue, rewrite it.

## What "done" looks like

A `docs/PRODUCT.md` that:

- Has eight focused paragraphs (Summary, Customer, Problem, Mechanism, Why, Business model, Proof, Goal) plus a dated header and a sources footer.
- Reads end-to-end in 4–6 minutes by someone with zero prior context.
- Contains no unexpanded acronyms — a non-startup reader would not feel they're missing terminology. (Well-understood framework terms like *wedge, north star, moat* stay, per step 4.)
- Preserves every real number, named entity, and customer-voice quote from the source documents.
- Is dated and links to the source documents in the footer.

Anything less is a draft. Surface the gap — usually that one of the source documents is thin and the corresponding section is correspondingly thin — and recommend the next step: run the relevant sibling Define skill to sharpen the source doc, then re-run this synthesis.
