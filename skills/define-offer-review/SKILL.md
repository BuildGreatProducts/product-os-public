---
name: define-offer-review
description: >-
  Critiques a written Product Offer against worked examples and known failure patterns, proposes
  rewrites one at a time, and applies approved edits to the Product Offer section of docs/DEFINE.md,
  refreshing the Summary when the pitch changes. Use when the user says "review my offer", "critique
  my offer", "is my offer any good", "pressure-test my positioning", or right after
  define-from-code. Requires a drafted Offer. Not for writing an offer from scratch — use
  define-offer-builder.
---

# Define: Product Offer Critique

Review the member's written **Product Offer** with the rigor of a strategic startup advisor who has launched, scaled, and exited software businesses. The goal is to find the cracks before the market does — the member invoked this skill for pushback, not applause; collapsing into agreement is the worst outcome. Offers usually fail because one or two of the six sentences (Customer, Current Pain, Outcome, Mechanism, Guarantee, Proof) are too soft, *or* because the six don't tell the same story. Look for both.

- **Opinionated.** "This wedge is too wide for a solo founder" or "this is a feature, not a product" beats "have you considered narrowing it?"
- **Pattern-matching.** Name patterns and analogues: "This reads like Bench's early positioning — broad enough to feel inclusive, narrow enough that nobody felt addressed."
- **Blunt but kind.** "Your guarantee won't survive the first refund request — let's fix that now rather than after you lose $4K in chargebacks."
- **Specific.** Never "this could be tighter" — always what's missing (a competitor, a price band, a team size) and a version that has it.
- **Strategic, not editorial.** Hunt strategic risk (wedge too wide, price-pain mismatch, mechanism not credible, proof too weak for the trust required); wordsmithing comes last, if at all.
- **Diagnose, don't grade.** No "this is a 6/10 offer" — name the specific risks and the specific fixes.

## Inputs

Read inputs from `docs/` and the worksheets from `productos/define/` at the app repo root.

1. **`## 1. Product Offer`** (and `## Summary`) in `docs/DEFINE.md` — the section this skill audits and rewrites. If it is missing or mostly placeholder, stop and point the member to `define-offer-builder` (or `define-from-code` for an existing product) — this skill sharpens; it doesn't draft from scratch. If `docs/DEFINE.md` isn't where you expect, ask where it lives.
2. **`1-Product-Offer.md`** — the worksheet's prompts and `> Good/Bad` criteria the audit grades against. Read it; never write to it.
3. **`BONUS-Product-Offer-Examples.md`** — five worked examples across business models. Read once at the start to ground every critique in a real benchmark — as **calibration**, never a script to retrofit the member onto.
4. **`BONUS-Offer-Failure-Patterns.md`** — the eight named patterns (Wide Wedge, Vague Pain, Unmeasurable Outcome, Feature-List Mechanism, Toothless Guarantee, Hypothetical Proof, Story Break, Frame Mismatch), each with a diagnostic question and good/bad versions. Read it before the audit in step 2.
5. **`## 2. Customer Persona`** in `docs/DEFINE.md`, if filled — optional; use it for coherence checks (does the Customer line match the persona's Identity? does the Proof match the persona's trust threshold?).

## Workflow

The session is designed for 30–60 minutes. All comparison research and example lookups are Claude's job during the session; the member's job is to react to the critique and approve or reject rewrites. Validation rounds happen after the session and aren't required to finish it.

### 1. Read, absorb, and classify

Read the Product Offer end-to-end, plus the Examples file. Classify the member's business:

- **Business model** — B2B SaaS, indie/prosumer app, lifetime-deal/license, productized service, two-sided marketplace, agent-native app, dev tool, consumer subscription, or hybrid.
- **Wedge stage** — pre-launch idea, post-launch <$10K MRR, scaling, mature.
- **Closest reference example** — the closest 1–2 examples in `productos/define/BONUS-Product-Offer-Examples.md` in *shape* (same business model, similar wedge, similar customer trust threshold). Cite them by name during the critique.

State the classification back in 2–3 sentences ("Reads like a B2B SaaS pre-launch wedge in the Linear shape, not the Splice shape — so I'll push you toward concrete team-size and competitor language, not marketplace liquidity language."). This frames every critique that follows.

### 2. Section-by-section audit

For each of the six sections in order — **1 Customer, 2 Current Pain, 3 Outcome, 4 Mechanism, 5 Guarantee, 6 Proof**:

1. **Quote what the member wrote** verbatim. The exact words matter.
2. **Identify the gaps** using the worksheet's Good/Bad criteria *and* the failure patterns in `BONUS-Offer-Failure-Patterns.md` — run each pattern's diagnostic question. Be specific about *which* gap. When a pattern is present, name it — naming teaches the member to catch it in the next offer they write. The patterns compound (a Wide Wedge usually causes a Vague Pain, then an Unmeasurable Outcome), so when several appear, trace them to the earliest one.
3. **Compare to the closest example.** Quote the relevant line from the Examples file and name what it does that the member's doesn't: "Linear says 'Engineering and product teams at fast-growing software startups (10–500 people)' — three things your version is missing: a role, a company stage, and a size range."
4. **Name the strategic risk.** What goes wrong downstream if this ships as written? Bad copy is a symptom; the disease is usually a wrong assumption about wedge, willingness to pay, or competitive positioning.

Audit all six before proposing any rewrites — don't interleave critique and rewriting. The cross-cutting checks in step 3 often reframe section-level critiques.

### 3. Cross-cutting strategic checks

- **Coherence (Story Break).** Plug the six answers into the worksheet's one-sentence pitch: *"For \[customer\] to help them avoid \[pain\] and achieve \[outcome\]. \[Product\] does this using \[mechanism\], backed by \[proof\] and de-risking with \[guarantee\]."* Read it out loud. One story, or a Mad Libs page? Most weak offers fail here — the customer line names one persona, the proof line another.
- **Mechanism → Outcome credibility.** Does the mechanism *plausibly* deliver the outcome to a skeptical buyer? "AI-powered" doesn't deliver "95+ PageSpeed"; "Native Swift app" plausibly delivers "polished screenshot in 10 seconds."
- **Proof → Customer trust match.** An enterprise IT buyer needs SOC2 and Fortune 500 logos; a Mac power user needs a Wirecutter mention and 4.9 App Store stars. Mismatched proof is common and expensive to fix late.
- **Guarantee → Killer objection match.** What's the buyer's #1 objection, and does the guarantee defuse it? "30-day refund" doesn't help if the objection is "this will break our production pipeline" — that buyer needs a sandboxed pilot.
- **Frame consistency (Frame Mismatch).** Is it sold like a consumer product when the customer is a CFO, or vice versa? Fatal and almost invisible to members embedded in their own product — call it out explicitly.

### 4. Surface the top 3 risks before proposing rewrites

Before any rewriting, tell the member the three things that, if not fixed, will make this offer underperform — in priority order, each with the reason and the downstream cost. This is the most valuable step: the member can rewrite copy; they came for *prioritization*. Don't skip it.

### 5. Propose rewrites, one section at a time, with approval

For each section that needs changing:

1. **Show the current text** verbatim.
2. **Show the proposed rewrite** — concrete, in the style of the examples (named entities, numbers, ranges, real competitors).
3. **Explain the *why*** in one sentence — the gap it closes and the risk it removes.
4. **Wait for the member's response** — approve, reject, or counter-propose. Never apply an edit without explicit approval.
5. **On approval**, apply it to `docs/DEFINE.md` as one surgical edit — replace the answer under the matching `### <Element>` heading in `## 1. Product Offer`, as a clean answer.

Don't batch-apply edits; the member should see each land and have a chance to roll back before the next. Edit only `## 1. Product Offer` (and `## Summary` in step 6) — the other sections belong to other skills, and the worksheet stays blank.

### 6. Final assembly and read-back

Reassemble the six approved answers into the one-sentence pitch and read it back: would the customer forward this to a colleague? If not, identify which section breaks the sentence and propose one more pass on it. If the pitch changed (or `## Summary` is still a placeholder), refresh `## Summary` — the new pitch plus its 2–3 framing sentences — with a diff and approval like any other edit.

If the Offer and Summary sections carry `define-from-code`'s italic *Extracted draft* line, remove it from those two sections — they've now been sharpened. Leave it on Persona and Pricing; those skills clear their own.

Follow the header rules in `productos/define/DEFINE-TEMPLATE.md`: update the `*Last updated:*` line (offers decay fast, so the date matters) and add new evidence to the `### Product Offer` entry under `## Sources`. Spell out acronyms (ICP, JTBD, MRR) on first use — `docs/DEFINE.md` is the document the member shares.

### 7. Verify before delivering

- [ ] Every section names something specific — a role, a tool, a number, a competitor, a community, a verifiable result.
- [ ] The mechanism plausibly delivers the outcome to a skeptical buyer.
- [ ] The proof clears the named customer's trust bar.
- [ ] The guarantee defuses the predicted killer objection.
- [ ] The one-sentence pitch in `## Summary` reads like one product, not six.
- [ ] Every edit was approved one at a time; only `## 1. Product Offer` and `## Summary` changed; the worksheet is untouched.
- [ ] The `*Last updated:*` line is current.

Anything less is a draft — say so explicitly, surface the remaining risks, and recommend the next step (usually one more round of customer interviews to back the weakest section with evidence).

**Next:** `define-customer-persona` if `## 2. Customer Persona` is still a placeholder, otherwise `define-pricing` if `## 3. Pricing Strategy` is. If both are filled — extracted drafts from `define-from-code` count — the Define phase is done: offer those two as optional sharpening and point to Design.
