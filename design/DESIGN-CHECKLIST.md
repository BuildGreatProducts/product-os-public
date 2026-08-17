# Design — Checklist

Work top to bottom. Requires `docs/PRODUCT.md` to exist (run the Define phase first — or its fast-track via `studio-define-from-code` if you already have a product). Each step runs a single skill and produces a single file (Step 2 produces a mirrored pair). The order matters — every later skill reads the earlier outputs.

If `docs/PLAN.md` exists (your programme plan, shipped with coached copies of ProductOS), it may mark steps below as fast-tracked or skipped for you — follow it; this checklist remains the source of truth for how each step runs.

---

## Step 1 — Product Identity

- **What to do:** Run `studio-design-identity-creator`.
- **What it does:** Produces `productos/design/1-Product-Identity.md` — the minimum viable brand in words, five decisions: **Name** (committed and availability-checked), **Worldview** (the conviction beyond your category), **Contrarian Belief** (what your category gets wrong), **Tone of Voice**, and **Visual Style** (imagery lane + references) — assembled into a one-glance Brand Card. Colours and fonts are deliberately *not* here; they come from Step 2. Draws on `BONUS-Product-Identity-Deep-Dive.md`.

## Step 2 — Design System (DESIGN.md + DESIGN.html)

- **What to do:** Find **one image or website you love** — a screenshot of a product whose look fits your brand, a marketing site, a Figma file (your identity's Visual Style references are the natural hunting ground) — then run `studio-design-design-system`.
- **Already have a codebase?** Run `studio-design-design-system-from-code` instead — it reverse-engineers the design system already in your code, flagging and resolving inconsistencies along the way.
- **What it does:** Translates the image into two mirrored files: `docs/DESIGN.md` — Google-format YAML tokens (colors, typography, rounded, spacing, components) plus prose rationale, the source of truth your coding agent reads — and `docs/DESIGN.html` — a self-contained style guide that renders every token and component live in your browser, so you can *see* your design system. Your identity guides the strategy; the image supplies the tactics. Tokens pass WCAG AA contrast.

## Step 3 — Design Prompts for AI design tools

- **What to do:** Run `studio-design-prompt-generator`.
- **What it does:** Produces `productos/design/Design-Prompts.md` — three paste-ready prompts (Prompt 1: the full UI component set; Prompts 2–3: two priority screens for your product type) for Pencil, paper.design, Claude Design, or MagicPath — with your DESIGN.md tokens and identity words embedded, so generated screens are on-brand from the first pass.
- **How to use the prompts:** Read `BONUS-Design-Tool-Setup.md` to install and connect your AI design tool — **MagicPath is recommended**. Paste the prompts and generate your screens on top of the design system you locked in Step 2.

## Step 4 — Magic Moment

- **What to do:** Run `studio-design-magic-moment`.
- **What it does:** Produces `productos/design/2-Magic-Moment.md` — one specific in-product event that makes users feel the product working, plus the activation hypothesis (what has to happen for a user to reach that moment).

## Step 5 — Onboarding Flow

- **What to do:** Run `studio-design-onboarding-flow`.
- **What it does:** Produces `productos/design/3-Onboarding-Flow.md` — the screen-by-screen path from first-open to magic moment. Every screen has a purpose, a primary action, and a tie back to the activation hypothesis. Draws on the matching `productos/design/onboarding/BONUS-[product-type]-Onboarding-Best-Practice.md`.

## Step 6 — Acquisition surface *(pick one based on product type)*

*If your product ships both a web surface and a mobile app, run both — you'll end up with both `4a-Landing-Page.md` and `4b-App-Store-Listing.md`, and that's correct.*

### 6a — Landing Page *(web / SaaS / desktop / marketing site)*

- **What to do:** Run `studio-design-landing-page`.
- **What it does:** Produces `productos/design/4a-Landing-Page.md` — hero, features-as-benefits, social proof, CTA closer. Draws on `BONUS-Web-Landing-Page-Best-Practice.md`.

### 6b — App Store Listing *(mobile app)*

- **What to do:** Run `studio-design-app-listing`.
- **What it does:** Produces `productos/design/4b-App-Store-Listing.md` — name, subtitle, screenshots brief, description, keywords. Draws on `BONUS-App-Store-Listing-Best-Practice.md`.

## Step 7 — Relaunch: "here's what it looks like"

- **What to do:** Run `studio-launch`. Same ritual as your Mini-Launch: ship within 48 hours, share a screenshot of the live post with your cohort or accountability partner, log every response in `docs/LAUNCHES.md`.
- **What it does:** Sends the product's new face — the Brand Card, a landing-page draft, or screens generated from your design system — to your believers first, then back to the same channel as launch #1, as an update on the same thread. **The win is one "can I try it?" or signup** — the next rung on the signal ladder. Anyone who leans in goes on the beta list for the Develop relaunch.

---

## Next phase

Once `docs/DESIGN.md` and the acquisition surface exist, move to the Develop phase. Open `productos/develop/DEVELOP-CHECKLIST.md`. During the build, use `studio-develop-design-better` when generating UI, `studio-develop-design-review` before commits, and `studio-develop-cro-audit` once the product has traffic.
