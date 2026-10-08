# Define — Checklist

Work top to bottom — or ask your agent to *"start define"*: `define-phase` walks these steps with you, one at a time, and checks each output. Each step runs a single skill and fills one section of a single file: `docs/DEFINE.md`, your product definition. The whole phase fits in the first two weeks — offer, shape, persona, pricing. `docs/DEFINE.md` is the one document you share with a co-founder, designer, or advisor, and the one every downstream Design and Develop skill reads.

The numbered files in this folder (`1-Product-Offer.md`, `1b-Product-Shape.md`, `2-Customer-Persona.md`, `3-Pricing-Strategy.md`) are **worksheets**: the structure and `> Good/Bad` guidance each skill reads. Your answers land in `docs/DEFINE.md` — the first skill to run creates it from `DEFINE-TEMPLATE.md`, and each skill writes only its own section.

If `docs/PLAN.md` exists (your programme plan, from your coach or `product-audit`), it may mark steps below as fast-tracked or skipped for you — follow it; this checklist remains the source of truth for how each step runs.

Running a challenge (`docs/SHIP-IN-7.md` or `docs/SELL-IN-30.md` open)? It says which of these steps are this week's, and on which session; this checklist remains the source of truth for how each step runs.

---

## Step 1 — Product Offer

- **What to do:** Run `define-offer-builder`, then optionally `define-offer-review` for a critique pass.
- **Already have a product?** Run `define-from-code` instead — it extracts draft Summary, Offer, Persona, and Pricing sections of `docs/DEFINE.md` from your existing codebase, live app, or landing page (covering Steps 1–3 in one pass), then `define-offer-review` sharpens them and `define-product-shape` confirms the shape the product already has (Step 1b, a short session). You skip the blank worksheets, not the thinking.
- **No idea yet?** Run `define-idea-finder` first — it audits your existing business, expertise, or passions for the point software can multiply, routes between building for yourself first and building for the people around you, and converges on one idea, then asks which parts to keep in the `## Idea Audit` section of `docs/DEFINE.md`. You arrive back at this step with the offer-builder's two intake questions already answered.
- **What it does:** Fills `## Summary` and `## 1. Product Offer` in `docs/DEFINE.md` — the six elements (Customer, Pain, Outcome, Mechanism, Guarantee, Proof), assembled into a one-sentence offer. Worksheet: `1-Product-Offer.md`. Draws on `BONUS-Product-Offer-Examples.md` and `BONUS-Offer-Failure-Patterns.md`.

## Step 1b — Product Shape

- **What to do:** Run `define-product-shape`.
- **What it does:** Fills `## Product Shape` in `docs/DEFINE.md` — how the customer receives and uses the product: web app, mobile app, desktop app, browser extension, agent plugin, agent skill, MCP server, chat assistant, developer tool, productized service, website, or digital product. One primary shape (plus any secondary surface the MVP genuinely ships), why it fits where your customer already works, and what "live" and "first sale" mean for it. The shape routes everything after it — which Design steps apply, what the PRD covers, what going live means, which channels are native. Worksheet: `1b-Product-Shape.md`. Draws on `productos/shapes/` (one file per shape).

## Step 2 — Customer Persona

- **What to do:** Run `define-customer-persona`.
- **What it does:** Fills `## 2. Customer Persona` in `docs/DEFINE.md` — one specific person, what they want, what they currently do, what makes them switch. Worksheet: `2-Customer-Persona.md`. Draws on `BONUS-Customer-Persona-Examples.md`.

## Step 3 — Pricing Strategy

- **What to do:** Run `define-pricing`. A 30–45 minute session — how the product earns and what it costs, decided once.
- **What it does:** Fills `## 3. Pricing Strategy` in `docs/DEFINE.md` — who pays, which business model matches how the value arrives, the pricing model (billing unit, plans, entry, cadence), 2–3 real anchors, one launch price with the value, cost, and anchor lines behind it, and the plain-English price line your landing page and first sales conversations will carry. Worksheet: `3-Pricing-Strategy.md`. Draws on `BONUS-Business-Models.md` and `BONUS-Pricing-Models.md`. *(Want the economics — cost & margin, moat, north star? That's `## 4. Business Strategy`, filled by `define-business-strategy` from the worksheet `BONUS-Business-Strategy-Deep-Dive.md`. Most people don't need it until money questions get real — typically before spending on paid channels in Distribute.)*

---

## Next phase

Once `docs/DEFINE.md` has its Summary, Offer, Product Shape, Persona and Pricing filled, move to the Design phase: ask your agent to *"start design"* (`design-phase`), or open `productos/design/DESIGN-CHECKLIST.md`.
