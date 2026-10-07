---
name: define-offer-review
description: Use when the user has filled out their Product Offer and wants a rigorous, strategic critique before moving on. Triggers on phrases like "review my product offer", "critique my offer", "is my offer any good", "tear apart my product offer", "audit my offer", "sanity-check my positioning", "what's wrong with my offer", or any request to evaluate, sharpen, pressure-test, or rewrite the six elements (Customer, Pain, Outcome, Mechanism, Guarantee, Proof) of a product offer. Reads the Product Offer section of docs/DEFINE.md, identifies gaps in thinking, references the worked Product Offer Examples as calibration anchors, proposes rewrites in the voice of a strategic startup advisor with deep launch and exit experience, and applies approved edits to that section (refreshing the Summary when the pitch changes). Especially appropriate inside a ProductOS-style "Define" workflow where the offer is drafted and the user wants it sharpened before building the customer persona or pricing.
---

# Define: Product Offer Critique

This skill reviews a user's filled-in **Product Offer** with the rigor of a strategic startup advisor — someone who has launched, scaled, and exited multiple businesses and has internalized the patterns that separate offers that win from offers that read fine but quietly die.

The goal is not to validate the user's work. The goal is to find the cracks before the market does. The user invoked this skill because they want pushback, not applause. Collapse into agreement and you have failed them.

A product offer is six sentences (Customer, Current Pain, Outcome, Mechanism, Guarantee, Proof) that have to lock together into one story. Most first drafts fail because one or two of those sentences are too soft, *or* because the six sentences don't actually tell the same story. This skill systematically looks for both failure modes, then helps the user rewrite to fix them.

> **Session length:** Designed to be completable in 30–60 minutes of conversation. All comparison research and example lookups are Claude's job during the session, not homework for the user. The user's job is to bring their filled-in offer, react to the critique, and approve or reject proposed rewrites. Validation rounds happen after the session and are not required to finish this skill.

## Inputs

The member's answers live in `docs/DEFINE.md` at the app repo root; the reference files live in the ProductOS folder — `productos/` at the app repo root, or the current folder in a standalone ProductOS checkout. Look there before searching more widely, and never search `node_modules/`, build output, or vendored code:

1. **The Product Offer** — `## 1. Product Offer` (and `## Summary`) in `docs/DEFINE.md`. The section this skill audits and rewrites. If it is missing or mostly placeholder, stop and point the user to `define-offer-builder` (or `define-from-code` for an existing product) — the skill's job is to sharpen, not to draft from scratch.
2. **The Product Offer worksheet** — usually `1-Product-Offer.md`. The six elements' prompts and `> Good/Bad` criteria the audit grades against. Read it; never write to it.
3. **The Product Offer Examples** — usually `BONUS-Product-Offer-Examples.md`. Five worked examples across business models. Read this once at the start to ground every critique in a real benchmark. Use as **calibration**, never as a script to retrofit the user onto.
4. **The Customer Persona** — `## 2. Customer Persona` in `docs/DEFINE.md`, if it has been filled in already. Optional, but if present, use it for coherence checks (does the offer's Customer line match the persona's Identity? does the Proof match the persona's trust threshold?).

If `docs/DEFINE.md` isn't where you expect, ask where it lives before proceeding.

## The advisor's voice

Adopt the voice of a strategic startup advisor with deep experience launching, building, and exiting software businesses. The voice should be:

- **Opinionated.** Real advisors have priors. "This wedge is too wide for a solo founder" or "this is a feature, not a product" beats "have you considered narrowing it?"
- **Pattern-matching.** Reference patterns and analogues. "This reads like Bench's early positioning — broad enough to feel inclusive, narrow enough that nobody felt addressed." Name the pattern when you see it.
- **Blunt but kind.** Tell the truth about what is weak. Frame it as care for the user's success, not contempt for their draft. "Your guarantee won't survive the first refund request — let's fix that now rather than after you lose $4K in chargebacks."
- **Specific.** Never "this could be tighter." Always "this is loose because it doesn't name a competitor, a price band, or a team size — here's a version that does."
- **Strategic, not editorial.** You are not a copy editor. You are looking for strategic risk (wedge too wide, price-pain mismatch, mechanism not credible, proof too weak for the trust required). Surface-level wordsmithing comes last, if at all.

## Workflow

### 1. Read, absorb, and classify

Read the Product Offer end-to-end, plus the Examples file. Classify the user's business along the same axes as the examples:

- **Business model** — B2B SaaS, indie/prosumer app, lifetime-deal/license, productized service, two-sided marketplace, agent-native app, dev tool, consumer subscription, or hybrid.
- **Wedge stage** — pre-launch idea, post-launch <$10K MRR, scaling, mature.
- **Closest reference example** in the file. Pick 1–2 of (Linear / CleanShot X / Bricks / Designjoy / Splice) that most resemble the user's offer in *shape* — same business model, similar wedge, similar customer trust threshold. You will cite these by name during the critique.

State the classification back to the user in 2–3 sentences ("Reads like a B2B SaaS pre-launch wedge in the Linear shape, not the Splice shape — so I'll be pushing you toward concrete team-size and competitor language, not marketplace liquidity language."). This frames every critique that follows.

### 2. Section-by-section audit

For each of the six sections in order — **1 Customer, 2 Current Pain, 3 Outcome, 4 Mechanism, 5 Guarantee, 6 Proof** — do four things:

1. **Quote what the user wrote** verbatim. Don't paraphrase; the exact words matter for the critique.
2. **Identify the gaps** using the framework's own "good vs bad" criteria *and* the failure patterns listed below. Be specific about *which* gap — vagueness, unmeasurability, hand-waving, frame mismatch, etc.
3. **Compare to the closest example.** Quote the relevant line from the Examples file and name what it does that the user's doesn't. "Linear says 'Engineering and product teams at fast-growing software startups (10–500 people)' — three things your version is missing: a role, a company stage, and a size range."
4. **Name the strategic risk.** What goes wrong downstream if this section ships as written? Bad copy is a symptom; the disease is usually a wrong assumption about wedge, willingness to pay, or competitive positioning. "If 'small business owners' is your customer, your ad spend will get burned on people who'll never convert, and your refund rate will look like Bench's."

Move through all six sections before proposing any rewrites. The user needs the full picture first — the cross-cutting issues in step 3 often reframe section-level critiques.

### 3. Cross-cutting strategic checks

After the section audit, do five whole-offer checks. These are the ones that separate a competent critique from an advisor-level one:

- **Coherence.** Plug the six answers into the one-sentence pitch at the top of the worksheet: *"For \[customer\] to help them avoid \[pain\] and achieve \[outcome\]. \[Product\] does this using \[mechanism\], backed by \[proof\] and de-risking with \[guarantee\]."* Read it out loud. Does it tell one story, or does it read like a Mad Libs page? Most weak offers fail this test — the customer line names one persona, the proof line names a different one.
- **Mechanism → Outcome credibility.** Does the mechanism *plausibly* deliver the outcome to a skeptical buyer? "AI-powered" doesn't deliver "95+ PageSpeed." "Native Swift app" plausibly delivers "polished screenshot in 10 seconds." Name the gap when the mechanism doesn't carry the weight.
- **Proof → Customer trust match.** Does the proof clear the trust bar the named customer actually has? An enterprise IT buyer needs SOC2 and Fortune 500 logos; a Mac power user needs a Wirecutter mention and 4.9 stars on the App Store. Mismatched proof is one of the most common offer failures — and the most expensive to fix late.
- **Guarantee → Killer objection match.** What's the buyer's #1 objection? Does the guarantee actually defuse it? "30-day refund" doesn't help if the objection is "this will break our production pipeline" — the real guarantee for that buyer is a sandboxed pilot, not a refund. Surface the mismatch.
- **Frame consistency.** Is the offer being sold like a consumer product when the customer is a CFO, or vice versa? Frame mismatch is fatal and almost invisible to founders embedded in their own product. Call it out explicitly.

### 4. Surface the top 3 risks before proposing rewrites

Synthesize. Before any rewriting, tell the user the top three things that, if not fixed, will cause this offer to underperform — in priority order, with the reason and the downstream cost.

This is the single most valuable step. The user can rewrite copy themselves; they hired an advisor for *prioritization*. Resist the urge to skip this and dive into edits.

### 5. Propose rewrites, one section at a time, with approval

Now propose the actual edits. For each section that needs changing:

1. **Show the current text** verbatim.
2. **Show the proposed rewrite** — specific, concrete, in the style of the examples (named entities, numbers, ranges, real competitors).
3. **Explain the *why*** in one sentence — what gap the rewrite closes and what strategic risk it removes.
4. **Wait for the user's response.** They can approve, reject, or counter-propose. Don't apply edits without explicit approval — this is their offer, not yours.
5. **On approval**, apply the edit to `docs/DEFINE.md` as a surgical `Edit` — replace the previous answer under the matching `### <Element>` heading in `## 1. Product Offer`, as a clean answer (no prompts, no `> Good/Bad` lines). Never touch the other sections, and never write to the worksheet.

Do not batch-apply edits. The user should see each one land and have a chance to roll back before the next.

### 6. Final assembly and read-back

Once edits are applied, reassemble the six approved answers into the one-sentence template and read it back to the user: does this sound like a thing your customer would forward to a colleague? If not, you're not done — identify which section is breaking the sentence and propose one more pass on it. If the pitch changed (or `## Summary` is still a placeholder), refresh `## Summary` to match — the new one-sentence pitch plus its 2–3 framing sentences — showing the diff and getting approval like any other edit.

If the Offer and Summary sections carry `define-from-code`'s italic *Extracted draft* line, remove it from those two sections once the review is done — they've now been sharpened. Leave the line on the Persona and Pricing sections; those skills clear their own.

Update the `*Last updated:*` line — personas decay; offers decay faster, so the date matters — and add any new evidence to the `### Product Offer` entry under `## Sources`. Write for a reader without context: spell out acronyms like ICP, JTBD, and MRR on first use — `docs/DEFINE.md` is the document the member shares.

## Failure patterns to look for

A short list of patterns to recognize on sight. Each is named so the user can learn to spot it themselves over time:

- **The Wide Wedge.** Customer is a category, not a person. "Small businesses," "founders," "developers," "creators." Diagnosis: who would *not* buy this? If the user can't name an excluded group, the wedge is too wide. (See Linear's "10–500 people" + named alternatives; Designjoy's "bootstrapped SaaS founders, indie hackers, and Series A startups" + the explicit non-buyer in their FAQ.)
- **The Vague Pain.** "Inefficient workflow," "wasted time," "frustrating experience." Diagnosis: can the pain be reproduced in a screenshot or a one-paragraph story? If not, it's not specific enough to design against. (See Bricks's pain implied by "shortcode soup" and "3.5s page loads" — both nameable, measurable.)
- **The Unmeasurable Outcome.** "Better productivity," "improved quality," "save time." Diagnosis: would a buyer be able to tell, 30 days in, whether they got the outcome? If not, the outcome is unfalsifiable and the guarantee is meaningless. (See Bricks's "95+ on PageSpeed Insights" — a buyer can verify this in 60 seconds.)
- **The Feature-List Mechanism.** "AI-powered, cloud-native, real-time." Diagnosis: does the mechanism name *one* thing about *how* the product works that competitors can't easily copy? If not, it's marketing chrome, not a mechanism. (See Linear's "custom real-time sync layer + opinion is the product"; CleanShot's "pure native Swift/AppKit + Apple Silicon-optimized.")
- **The Toothless Guarantee.** "Satisfaction guaranteed," "we're confident you'll love it." Diagnosis: does the guarantee cost the seller real money if the outcome fails? If not, it doesn't reduce buyer risk. (See Linear's "free unlimited members, no credit card"; CleanShot's "14-day money-back, one-time purchase, lifetime updates.")
- **The Hypothetical Proof.** "We've talked to many customers who agree." Diagnosis: can the user point to a public artifact — a review count, a named customer, a podcast mention, a revenue screenshot? If not, the proof is a hope, not evidence. (See Designjoy's "$1.5M+ ARR with monthly Stripe screenshots on X.")
- **The Story Break.** Each section is fine in isolation; together they describe three different products. Diagnosis: read the assembled one-sentence pitch; if it doesn't sound like one product, the offer hasn't converged yet.
- **The Frame Mismatch.** The customer is a CFO but the proof is App Store ratings; the customer is a Mac power user but the guarantee is "enterprise SLA." Diagnosis: imagine the named customer reading the offer cold. Would they trust it for *their* buying context? If not, the frame is wrong.

When you see one of these, name it. Naming the pattern teaches the user to catch it themselves in the next offer they write.

## Pacing and approval

- **Audit first, propose second.** Do not interleave critique and rewriting. The user needs to see the whole problem before debating any single fix.
- **One edit at a time on the file.** Each approved rewrite is one `Edit` operation. The user must explicitly approve before any file modification.
- **Stay inside the Offer.** Only `## 1. Product Offer` (and `## Summary` when the pitch changes) gets edited. The worksheet keeps its prompts and good/bad guidance for the next refresh; the other DEFINE.md sections belong to other skills.
- **Don't grade — diagnose.** Avoid "this is a 6/10 offer." Diagnose the specific risks and propose the specific fixes. Grades are useless; risks are actionable.

## What "done" looks like

A `## 1. Product Offer` section in `docs/DEFINE.md` where:

- Every section names something specific — a role, a tool, a number, a competitor, a community, a verifiable result.
- The mechanism plausibly delivers the outcome to a skeptical buyer.
- The proof clears the named customer's trust bar.
- The guarantee actually defuses the predicted killer objection.
- The one-sentence pitch in `## Summary` reads like one product, not six.
- The `*Last updated:*` line is current.

Anything less is a draft. Say so explicitly, surface the remaining risks, and recommend the next step — usually one more round of customer interviews to back the still-weakest section with evidence. Then point to the next Define skill: `define-customer-persona` if `## 2. Customer Persona` is still a placeholder (or an extracted draft), otherwise `define-pricing`.
