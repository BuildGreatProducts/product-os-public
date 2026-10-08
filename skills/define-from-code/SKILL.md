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

This skill is the Define-phase counterpart of `design-design-system-from-code`. Instead of going *forward* — blank worksheet → interview → filled offer — it goes *backward*: it reads the product that already exists (the codebase, the live app, the landing page, the listing) and extracts the strategy that's already implicit in it into `docs/DEFINE.md`, using the three Define worksheets for structure. The forward skills are for greenfield ideas. This one is for members who arrive with something built and shouldn't spend their first week pretending they don't.

**What this skill is not:** a way to skip the thinking. The offer work is the most valuable session in the programme precisely because it forces clarity — so the fast-track ends in a critique, not a shrug. Everything this skill writes is an **extracted draft**, and the handoff to `define-offer-review` is mandatory, not optional. Extraction gets the member to the valuable conversation in hours instead of days; it doesn't replace it.

> **Session shape:** 45–60 minutes. Most of it is reading evidence and confirming inferences — short focused questions, never the full builder interview.

## Inputs

Whatever exists, in priority order — read everything available before drafting anything:

1. **The codebase** — the repository surrounding `productos/`; read it directly, no path to ask for. Structure, features that demonstrably work, the core flow, auth/payment integrations (a Stripe integration is pricing evidence), copy strings and empty states (offer language hides in UI copy).
2. **The live product / landing page / app store listing** (get URLs). The public surfaces are the strongest offer evidence there is — they show what the product *actually promises* today: which customer it addresses, which pain it names, what price it dares to show.
3. **Existing docs** — READMEs, pitch decks, specs, notes. Secondary to the artifacts: what the member wrote about the product and what the product does often disagree, and the product wins.
4. **The member.** Real usage (who uses it, how they found it, what they say) and anything paid. Ask; don't infer user counts from code.

This skill runs read-only against the product — it never modifies the app code. The only file it writes is `docs/DEFINE.md`. The worksheets in `productos/define/` (`1-Product-Offer.md`, `2-Customer-Persona.md`, `3-Pricing-Strategy.md`) supply the structure and `> Good/Bad` criteria; they stay blank.

## Workflow

### 1. Read the evidence

Read everything in Inputs end to end before drafting. As you read, collect: the customer the product implies, the pain its features attack, the outcome its copy promises, the mechanism it actually implements, any guarantee or trust language, any proof (testimonials, user numbers, reviews), any visible or implemented pricing, and any signal about who really uses it.

### 2. Draft the four sections

From the evidence, draft in one pass, following each worksheet's headings:

- **`## 1. Product Offer`** (worksheet `1-Product-Offer.md`) — all six elements (Customer, Pain, Outcome, Mechanism, Guarantee, Proof), each 1–2 sentences, each traceable to evidence. Where the evidence is silent (commonly Guarantee, often Proof), write the honest gap — *"No guarantee anywhere on the current site — decide one in the review"* — not an invention.
- **`## Summary`** — the six elements assembled into the worksheet's one-sentence pitch, plus 2–3 framing sentences — who it's for, what it replaces, and why the approach is credible.
- **`## 2. Customer Persona`** (worksheet `2-Customer-Persona.md`) — the persona the product is *actually built for*, per the evidence, flagging loudly where that differs from who the member says it's for. That gap is one of the most valuable things this skill can surface.
- **`## 3. Pricing Strategy`** (worksheet `3-Pricing-Strategy.md`) — observed pricing (from the site, the Stripe products, the app-store listing, or "currently free — no price has ever been asked"), the business model and billing unit the evidence implies, a who-pays inference, and any anchors the evidence suggests.

### 3. Confirm the load-bearing inferences

Present the drafts **one section at a time**, leading each with the 2–3 inferences that would change everything downstream if wrong (who the customer is, what the core pain is, what the price is). Ask short, specific questions — *"The site sells to freelancers but the codebase's onboarding assumes a team — which is it?"* — fold in corrections, and move on. This is a fast confirmation pass, not the builder interview; resist expanding it.

### 4. Write the sections of `docs/DEFINE.md`

- **If `docs/DEFINE.md` doesn't exist**, create it (`mkdir -p docs`) from `productos/define/DEFINE-TEMPLATE.md`, with the product name in the title line.
- **If it exists**, read it first. Any of the four sections the member has already filled are theirs: show a diff of the proposed change and get approval before overwriting, and preserve their edits. Leave `## 4. Business Strategy` alone.

Write `## Summary`, `## 1. Product Offer`, `## 2. Customer Persona`, and `## 3. Pricing Strategy` under the worksheets' headings (`### Customer` … `### Proof`; one `###` per persona worksheet section; `### Who Pays` … `### Your Price Line`) as clean answers — no italic prompts, no `> Good/Bad` lines, no `**Your answer:**` labels. Directly under each of those four section headings, add one italic line: *"Extracted draft — generated from the existing product by `define-from-code` on [date]. Sharpen with `define-offer-review` before relying on it."*

Update the `*Last updated:*` line, and add `### Product Offer`, `### Customer Persona`, and `### Pricing Strategy` entries under `## Sources` naming the evidence each section came from (files, URLs, listings, what the member told you). Write for a reader without context: spell out acronyms like ICP, JTBD, and MRR on first use — `docs/DEFINE.md` is the document the member shares.

### 5. Verify and hand off

Re-read all four sections: no `###` heading left empty without an explicit named gap, every answer either evidence-backed or flagged as a decision to make, the extracted-draft line under each section heading, the other sections untouched. This matters mechanically as well as honestly — every downstream Design and Develop skill reads `docs/DEFINE.md`, and an empty heading becomes an invented answer there.

Then hand off to **`define-offer-review`** — the sharpening critique. Mandatory. This is where the fast-track earns its keep. After the review, the persona and pricing drafts can be sharpened with `define-customer-persona` and `define-pricing` where the member wants more than the extraction gave them; otherwise, with Summary, Offer, Persona, and Pricing filled, the Define phase is done and Design is next (their custom plan in `docs/PLAN.md`, if it exists, already says which).

## What "done" looks like

The Summary, Offer, Persona, and Pricing sections of `docs/DEFINE.md` filled, every answer either traceable to named evidence or explicitly flagged as a gap, the extraction line dated under each section heading, any customer/positioning contradictions between the artifacts and the member's self-description surfaced in conversation — and the member heading into `define-offer-review` with hours saved and the valuable argument still ahead of them, not skipped.
