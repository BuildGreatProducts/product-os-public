---
name: define-from-code
description: >-
  Extracts draft Define answers — Summary, Product Offer, Customer Persona, Pricing Strategy — from
  an existing product (codebase, live app, landing page, or store listing), writes them to
  docs/DEFINE.md marked as extracted drafts, confirms the load-bearing inferences, then hands off to
  define-offer-review. Use when the product already exists but DEFINE.md doesn't: "fast-track
  define", "extract my offer from my code", "backfill the strategy docs". Not for a product that is
  still an idea — use define-offer-builder.
---

# Define: From Code (the fast-track)

The Define-phase counterpart of `design-design-system-from-code`: instead of going forward (blank worksheet → interview → filled offer), go *backward* — read the product that already exists (codebase, live app, landing page, listing) and extract the strategy already implicit in it into `docs/DEFINE.md`, using the three Define worksheets for structure. It is not a way to skip the thinking: everything this skill writes is an **extracted draft**, and the handoff to `define-offer-review` is mandatory. Extraction gets the member to the valuable conversation in hours instead of days; it doesn't replace it.

## Inputs

Whatever exists, in priority order — read everything available before drafting anything:

1. **The codebase** — the repository surrounding `productos/`; read it directly. Structure, features that demonstrably work, the core flow, auth/payment integrations (a Stripe integration is pricing evidence), copy strings and empty states (offer language hides in UI copy).
2. **The live product / landing page / app store listing** (ask for URLs). The strongest offer evidence there is — what the product *actually promises* today: which customer it addresses, which pain it names, what price it dares to show. Read them with a web fetch or browser tool if one is connected; otherwise ask the member to paste the page copy and pricing.
3. **Existing docs** — READMEs, pitch decks, specs, notes. Secondary to the artifacts: when what the member wrote and what the product does disagree, the product wins.
4. **The member.** Real usage (who uses it, how they found it, what they say) and anything paid. Ask; don't infer user counts from code.

Run read-only against the product — never modify the app code. The only file this skill writes is `docs/DEFINE.md`. The worksheets in `productos/define/` (`1-Product-Offer.md`, `2-Customer-Persona.md`, `3-Pricing-Strategy.md`) supply the structure and `> Good/Bad` criteria; they stay blank.

## Workflow

The session runs 45–60 minutes — mostly reading evidence and confirming inferences with short, focused questions, never the full builder interview.

### 1. Read the evidence

Read everything in Inputs end to end before drafting. Collect: the customer the product implies, the pain its features attack, the outcome its copy promises, the mechanism it actually implements, any guarantee or trust language, any proof (testimonials, user numbers, reviews), any visible or implemented pricing, and any signal about who really uses it.

### 2. Draft the four sections

Draft in one pass, following each worksheet's headings:

- **`## 1. Product Offer`** (`1-Product-Offer.md`) — all six elements (Customer, Pain, Outcome, Mechanism, Guarantee, Proof), each 1–2 sentences, each traceable to evidence. Where the evidence is silent (commonly Guarantee, often Proof), write the honest gap — *"No guarantee anywhere on the current site — decide one in the review"* — not an invention.
- **`## Summary`** — the six elements assembled into the worksheet's one-sentence pitch, plus 2–3 framing sentences: who it's for, what it replaces, why the approach is credible.
- **`## 2. Customer Persona`** (`2-Customer-Persona.md`) — the persona the product is *actually built for*, per the evidence, flagging loudly where that differs from who the member says it's for. That gap is one of the most valuable things this skill surfaces.
- **`## 3. Pricing Strategy`** (`3-Pricing-Strategy.md`) — observed pricing (from the site, the Stripe products, the store listing, or "currently free — no price has ever been asked"), the business model and billing unit the evidence implies, a who-pays inference, and any anchors the evidence suggests.

### 3. Confirm the load-bearing inferences

Present the drafts **one section at a time**, leading each with the 2–3 inferences that would change everything downstream if wrong (who the customer is, what the core pain is, what the price is). Ask short, specific questions — *"The site sells to freelancers but the codebase's onboarding assumes a team — which is it?"* — fold in corrections, and move on. This is a fast confirmation pass, not the builder interview; resist expanding it.

### 4. Write the sections of `docs/DEFINE.md`

Write to `docs/DEFINE.md` following the header rules in `productos/define/DEFINE-TEMPLATE.md` (create it from the template if it's missing, with the product name in the title line; write only `## Summary`, `## 1. Product Offer`, `## 2. Customer Persona`, `## 3. Pricing Strategy`, their three entries under `## Sources`, and the `*Last updated:*` line — leave `## 4. Business Strategy` alone). Any of the four sections the member has already filled are theirs: show a diff and get approval before overwriting.

- Use the worksheets' headings (`### Customer` … `### Proof`; one `###` per persona worksheet section; `### Who Pays` … `### Your Price Line`) as clean answers.
- In each of the four sections, replace the template's `*Filled by …*` placeholder line with: *"Extracted draft — generated from the existing product by `define-from-code` in Month YYYY. Sharpen with `define-offer-review` before relying on it."* (the current month and year, matching the `*Last updated:*` format). The downstream skills remove this line when they sharpen a section.
- Add `### Product Offer`, `### Customer Persona`, and `### Pricing Strategy` entries under `## Sources` naming the evidence each section came from (files, URLs, listings, what the member told you).

Spell out acronyms (ICP, JTBD, MRR) on first use — `docs/DEFINE.md` is the document the member shares.

### 5. Verify and hand off

Every downstream Design and Develop skill reads `docs/DEFINE.md`, and an empty heading becomes an invented answer there — so check:

- [ ] Summary, Offer, Persona, and Pricing are filled; no `###` heading is left empty without an explicit named gap.
- [ ] Every answer is traceable to named evidence or flagged as a decision to make.
- [ ] The dated extracted-draft line has replaced the placeholder in each of the four sections.
- [ ] Contradictions between the artifacts and the member's self-description (customer, positioning) were surfaced in conversation.
- [ ] `## 4. Business Strategy`, the app code, and the worksheets are untouched.

Then hand off to **`define-offer-review`** — mandatory; this is where the fast-track earns its keep. After the review, the member can sharpen the persona and pricing drafts with `define-customer-persona` and `define-pricing`; otherwise, with Summary, Offer, Persona, and Pricing filled, the Define phase is done and Design is next (`docs/PLAN.md`, if it exists, already says which).
