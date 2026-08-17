---
name: studio-define-from-code
description: Use when the user already has a product — a codebase, live app, landing page, or app store listing — and needs the Define-phase documents extracted from it fast, instead of built from blank templates. Triggers on phrases like "extract my offer from my code", "fast-track define", "I already built it, backfill the strategy docs", "reverse-engineer my product offer", "define from my existing product", "my product exists but I have no PRODUCT.md", or any request to derive the Product Offer, Customer Persona, and Pricing Strategy from an existing product. Reads the evidence (repo, live site, listing, existing docs), infers draft answers for all six offer elements plus persona and observed pricing, pre-fills the three Define templates in place marked as extracted drafts, confirms the load-bearing inferences with the user, then hands off to studio-define-offer-review for sharpening and studio-define-product for synthesis. The Define fast-track for members who aren't starting from scratch.
---

# Define: From Code (the fast-track)

This skill is the Define-phase counterpart of `studio-design-design-system-from-code`. Instead of going *forward* — blank worksheet → interview → filled offer — it goes *backward*: it reads the product that already exists (the codebase, the live app, the landing page, the listing) and extracts the strategy that's already implicit in it into the three Define worksheets. The forward skills are for greenfield ideas. This one is for members who arrive with something built and shouldn't spend their first week pretending they don't.

**What this skill is not:** a way to skip the thinking. The offer work is the most valuable session in the programme precisely because it forces clarity — so the fast-track ends in a critique, not a shrug. Everything this skill writes is an **extracted draft**, and the handoff to `studio-define-offer-review` is mandatory, not optional. Extraction gets the member to the valuable conversation in hours instead of days; it doesn't replace it.

> **Session shape:** 45–60 minutes. Most of it is reading evidence and confirming inferences — short focused questions, never the full builder interview.

## Inputs

Whatever exists, in priority order — read everything available before drafting anything:

1. **The codebase** — the repository surrounding `productos/`; read it directly, no path to ask for. Structure, features that demonstrably work, the core flow, auth/payment integrations (a Stripe integration is pricing evidence), copy strings and empty states (offer language hides in UI copy).
2. **The live product / landing page / app store listing** (get URLs). The public surfaces are the strongest offer evidence there is — they show what the product *actually promises* today: which customer it addresses, which pain it names, what price it dares to show.
3. **Existing docs** — READMEs, pitch decks, specs, notes. Secondary to the artifacts: what the member wrote about the product and what the product does often disagree, and the product wins.
4. **The member.** Real usage (who uses it, how they found it, what they say) and anything paid. Ask; don't infer user counts from code.

This skill runs read-only against the product — it never modifies the app code. The only files it writes are the three Define templates in `productos/define/`.

## Workflow

### 1. Read the evidence

Read everything in Inputs end to end before drafting. As you read, collect: the customer the product implies, the pain its features attack, the outcome its copy promises, the mechanism it actually implements, any guarantee or trust language, any proof (testimonials, user numbers, reviews), any visible or implemented pricing, and any signal about who really uses it.

### 2. Draft the three documents

From the evidence, draft in one pass:

- **`productos/define/1-Product-Offer.md`** — all six elements (Customer, Pain, Outcome, Mechanism, Guarantee, Proof), each 1–2 sentences, each traceable to evidence. Where the evidence is silent (commonly Guarantee, often Proof), write the honest gap — *"No guarantee anywhere on the current site — decide one in the review"* — not an invention.
- **`productos/define/2-Customer-Persona.md`** — the persona the product is *actually built for*, per the evidence, flagging loudly where that differs from who the member says it's for. That gap is one of the most valuable things this skill can surface.
- **`productos/define/3-Pricing-Strategy.md`** — observed pricing (from the site, the Stripe products, or "currently free — no price has ever been asked"), a who-pays inference, and any anchors the evidence suggests.

### 3. Confirm the load-bearing inferences

Present the drafts **one document at a time**, leading each with the 2–3 inferences that would change everything downstream if wrong (who the customer is, what the core pain is, what the price is). Ask short, specific questions — *"The site sells to freelancers but the codebase's onboarding assumes a team — which is it?"* — fold in corrections, and move on. This is a fast confirmation pass, not the builder interview; resist expanding it.

### 4. Fill the templates in place

Rewrite the three numbered templates in `productos/define/`, preserving their structure and the `> Good/Bad` guidance scaffolding exactly (per the root `AGENTS.md` rules — never parallel copies). Directly under each file's title, add one italic line: *"Extracted draft — generated from the existing product by `studio-define-from-code` on [date]. Sharpen with `studio-define-offer-review` before relying on it."*

### 5. Verify and hand off

Re-read all three files: no `**Your answer:**` placeholder left empty without an explicit named gap, every answer either evidence-backed or flagged as a decision to make, scaffolding intact. This matters mechanically as well as honestly — `studio-define-product` refuses to synthesise placeholder-heavy documents.

Then hand off, in order:

1. **`studio-define-offer-review`** — the sharpening critique. Mandatory. This is where the fast-track earns its keep.
2. **`studio-define-product`** — synthesise `docs/PRODUCT.md` as normal once the review pass is done.
3. **The Mini-Launch question** — if the member has never put the product in front of strangers, recommend `studio-launch` next; if they already have real signal, note the current rung for `docs/LAUNCHES.md` to be backfilled at their first scheduled launch (their custom plan in `docs/PLAN.md`, if it exists, already says which).

## What "done" looks like

Three Define templates filled in place, every answer either traceable to named evidence or explicitly flagged as a gap, the extraction line dated at the top of each file, any customer/positioning contradictions between the artifacts and the member's self-description surfaced in conversation — and the member heading into `studio-define-offer-review` with hours saved and the valuable argument still ahead of them, not skipped.
