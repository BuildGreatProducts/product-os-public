---
name: define-product-shape
description: >-
  Decides the product's shape — web app, mobile app, desktop app, browser extension, agent plugin,
  agent skill, MCP server, chat assistant, developer tool, productized service, website, or digital
  product — and writes the Product Shape section of docs/DEFINE.md: primary and secondary shapes,
  why, what live and first sale mean, build implications. Define Step 1b, after the offer. Use when
  the user asks "what should my product be", "app or plugin", "what shape is my product". Not for
  the offer itself — use define-offer-builder.
---

# Define: Product Shape

Decide how the customer receives and uses the product, and write it to `## Product Shape` in `docs/DEFINE.md`. The shape routes everything after it: which Design steps apply, what the PRD covers, what "go live" means, which channels are native. Recommend firmly — a shape decided by default ("everything is a web app") is the most expensive mistake this step exists to prevent.

## Inputs

Read inputs from `docs/` and the worksheet from `productos/define/` at the app repo root.

1. **`## Summary` and `## 1. Product Offer`** in `docs/DEFINE.md` — **required**. If missing or a placeholder, stop and run `define-offer-builder` (or `define-from-code` for an existing product).
2. **[SHAPES.md](../../shapes/SHAPES.md)** — the twelve shapes, the picking questions, and the hybrid and sequence rules. Read it in full; it's short.
3. **`1b-Product-Shape.md`** — the worksheet: section structure and `> Good/Bad` calibration. Read it; never write to it.
4. **If they exist:** `## 2. Customer Persona` (where the customer already works), `## Idea Audit` (the route the member chose), and — for an existing product — the codebase, live URL, or store listing.

## Workflow

### 1. Form the hypothesis

Run the picking questions in SHAPES.md against the offer, in order, and stop at the first clear yes. Pick by **where the value is delivered**, not how it's built. For an existing product, the shape is usually what it already is — read the code or live product, name it, and only challenge it if the offer says the value lands somewhere else.

### 2. Check it against the customer

Research where the persona does this job today — the tools they already have open, where they buy software, whether they install things themselves. A shape that asks the customer to leave where they work needs a reason. Look at 2–3 competitors or comparables: what shape are they, and is there an opening in a different one (the same job as an agent skill when everyone else ships a web app)? Note any platform constraint that could kill a shape early: store review, marketplace rules, payment restrictions.

If web search isn't available, say so, ask the member for comparables, and mark those claims unverified.

### 3. Recommend

Present: the **primary shape** with its platform, **one rejected alternative** and why it lost, and any **secondary shape** the MVP genuinely needs. Then the consequence, in one line each from the shape file's routes: what Design will and won't include, what "go live" means, the native channel. Get a clear yes before writing. If the member wants two primary shapes, hold the line: one primary, the rest secondary or sequenced (SHAPES.md → Hybrid and sequenced products).

### 4. Fill the rest from the shape file

Read `productos/shapes/<slug>.md` (from this skill's folder, `../../shapes/<slug>.md`) — its *Live means*, *First sale means*, *Define notes*, and route tables. Walk the remaining worksheet sections one at a time, starting from the shape file's defaults and making each specific to this product: **Live Means**, **First Sale Means** (the payment event and how money is collected), **Build Implications** (UI or not, backend, auth, payments, hosting, store review, evals), **Sequence** (the next shape and its trigger, or none). Critique vague answers against the worksheet's Bad lines.

### 5. Write the section

If `docs/DEFINE.md` doesn't exist, create it from `productos/define/DEFINE-TEMPLATE.md` (follow its header rules: write only your section, replace its placeholder line, clean answers, show a diff before overwriting existing content). Write `### Primary Shape` as the slug in backticks plus the platform (`` `agent-skill` — a Claude skill pack installed from GitHub``), so `scripts/status.py` and every orchestrator can read it. Update *Last updated* and add a `### Product Shape` entry under `## Sources` (comparables checked, constraints found). Give the member the file path.

## Verify before delivering

- [ ] Primary Shape names exactly one slug from SHAPES.md, in backticks, plus its platform.
- [ ] Why This Shape names where the customer already works and one rejected alternative.
- [ ] Live Means and First Sale Means are concrete, checkable events — not "launched" or "people pay".
- [ ] Build Implications names anything that changes the build: UI or not, payments, hosting, store review, evals.
- [ ] Secondary shapes are MVP surfaces, not wishes; Sequence names a trigger or says none.
- [ ] Only `## Product Shape`, *Last updated*, and its Sources entry changed.

**Next step:** `define-customer-persona` (Define Step 2), or `define-pricing` if the persona is already filled — the shape's Define notes feed the pricing model. Re-run this skill when a Sequence trigger fires.
