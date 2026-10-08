# Design — Checklist

Work top to bottom — or ask your agent to *"start design"*: `design-phase` sets your route from your product's shape and walks it with you. Requires `docs/DEFINE.md` to exist with its Summary, Offer, Product Shape, Persona and Pricing filled (run the Define phase first — or its fast-track via `define-from-code` if you already have a product). Each step runs a single skill and writes its output to `docs/` (Steps 1 and 3 write the mirrored `docs/DESIGN.md` + `docs/DESIGN.html` pair). The numbered files in this folder are worksheets — the skills read them for structure and guidance and never write into them. The order matters — every later skill reads the earlier outputs.

**Your shape decides which steps apply.** Each shape file (`productos/shapes/<slug>.md`, for the primary shape in `docs/DEFINE.md`) marks every step below Full, Adapted (runs on your shape's medium — e.g. onboarding as install → first output), Lite (brand tokens only), Optional, or Skip, and names your acquisition surfaces. A screen-based app runs every step; an agent skill skips the screen work but still needs its identity, copy, magic moment, and listing.

If `docs/PLAN.md` exists (your programme plan, from your coach or `product-audit`), it may mark steps below as fast-tracked or skipped for you — follow it; this checklist remains the source of truth for how each step runs.

Running a challenge (`docs/SHIP-IN-7.md` or `docs/SELL-IN-30.md` open)? It says which of these steps are this week's, and on which session; this checklist remains the source of truth for how each step runs.

---

## Step 1 — Product Identity

- **What to do:** Run `design-identity-creator`.
- **What it does:** Writes the `## Product Identity` section of `docs/DESIGN.md` (and its `docs/DESIGN.html` mirror), creating both files if they don't exist yet — the minimum viable brand in words, five decisions: **Name** (committed and availability-checked), **Worldview** (the conviction beyond your category), **Contrarian Belief** (what your category gets wrong), **Tone of Voice**, and **Visual Style** (imagery lane + references) — assembled into a one-glance Brand Card. Colours and fonts are deliberately *not* here; they come from Step 3. Uses `1-Product-Identity.md` as its worksheet and draws on `BONUS-Product-Identity-Deep-Dive.md`.

## Step 2 — UX Writing Guide (COPY.md)

- **What to do:** Run `design-ux-writing`.
- **What it does:** Produces `docs/COPY.md` — the in-product copy system: a voice chart that turns your Tone of Voice into followable rules, a terminology lexicon (one name per thing), per-surface rules with worked examples (buttons, errors, empty states, confirmations, toasts, notifications), a banned-word list, and a copy review rubric. DESIGN.md is how the product looks; COPY.md is how it speaks — and every later skill that writes copy reads it. If you already have a codebase, the skill also audits your real UI strings and appends a fix list. Draws on `BONUS-UX-Writing-Best-Practice.md`.

## Step 3 — Design System (DESIGN.md + DESIGN.html)

- **What to do:** Find **one image or website you love** — a screenshot of a product whose look fits your brand, a marketing site, a Figma file (your identity's Visual Style references are the natural hunting ground) — then run `design-design-system`.
- **No screens to design?** If your shape marks this step Lite (agent skills and plugins, MCP servers, developer tools, services, digital products), `design-design-system` runs in Lite mode: brand tokens only — colour, type, logo use — for your listing, landing page, and docs.
- **Already have a codebase?** Run `design-design-system-from-code` instead — it reverse-engineers the design system already in your code, flagging and resolving inconsistencies along the way.
- **What it does:** Translates the image into the rest of the two mirrored files, keeping the Product Identity section from Step 1: `docs/DESIGN.md` — Google-format YAML tokens (colors, typography, rounded, spacing, components) plus prose rationale, the source of truth your coding agent reads — and `docs/DESIGN.html` — a self-contained style guide that renders every token and component live in your browser, so you can *see* your design system. Your identity guides the strategy; the image supplies the tactics. Tokens pass WCAG AA contrast.

## Step 4 — Design Prompts for AI design tools *(screen shapes)*

- **What to do:** Run `design-prompt-generator`.
- **What it does:** Produces `docs/DESIGN-PROMPTS.md` — three paste-ready prompts (Prompt 1: the full UI component set; Prompts 2–3: two priority screens for your product type) for Pencil, paper.design, Claude Design, or MagicPath — with your DESIGN.md tokens, identity words, and COPY.md lexicon embedded, so generated screens are on-brand and copy-correct from the first pass.
- **How to use the prompts:** Read `BONUS-Design-Tool-Setup.md` to install and connect your AI design tool — **MagicPath is recommended**. Paste the prompts and generate your screens on top of the design system you locked in Step 3.

## Step 5 — Magic Moment

- **What to do:** Run `design-magic-moment`.
- **What it does:** Produces `docs/MAGIC-MOMENT.md` (worksheet: `2-Magic-Moment.md`) — one specific in-product event that makes users feel the product working, plus the activation hypothesis (what has to happen for a user to reach that moment).

## Step 6 — Onboarding Flow

- **What to do:** Run `design-onboarding-flow`.
- **What it does:** Produces `docs/ONBOARDING.md` (worksheet: `3-Onboarding-Flow.md`) plus, for screen shapes, a clickable lo-fi wireframe at `docs/ONBOARDING-WIREFRAME.html` — the screen-by-screen (or, for shapes without screens, step-by-step: install → first output, booking → first delivery) path from first-open to magic moment. Every screen has a purpose, a primary action, and a tie back to the activation hypothesis. Draws on the matching `productos/design/onboarding/BONUS-[product-type]-Onboarding-Best-Practice.md`.

## Step 7 — Acquisition surface(s) *(your shape file names which)*

*Many shapes need more than one: a browser extension has a store listing and a landing page; a web app with an MCP server adds a registry listing. Run each one your shape files name.*

### 7a — Landing Page *(any shape with a web presence)*

- **What to do:** Run `design-landing-page`.
- **What it does:** Produces `docs/LANDING-PAGE.md` (worksheet: `4a-Landing-Page.md`), and optionally a clickable wireframe at `docs/LANDING-PAGE-WIREFRAME.html` — hero, features-as-benefits, social proof, CTA closer. Draws on `BONUS-Web-Landing-Page-Best-Practice.md`.

### 7b — App Store Listing *(mobile app)*

- **What to do:** Run `design-app-listing`.
- **What it does:** Produces `docs/APP-LISTING.md` (worksheet: `4b-App-Store-Listing.md`) — name, subtitle, screenshots brief, description, keywords. Draws on `BONUS-App-Store-Listing-Best-Practice.md`.

### 7c — Marketplace Listing *(every other store, marketplace, registry, or directory)*

- **What to do:** Run `design-marketplace-listing`.
- **What it does:** Produces `docs/MARKETPLACE-LISTING.md` (worksheet: `4c-Marketplace-Listing.md`) — one listing per store your shape needs: browser extension stores, agent plugin marketplaces, MCP registries, chat-assistant directories, app directories, package registries, and digital-product storefronts. Name, pitch within each field limit, description, categories, assets brief, install and first-run instructions, and the store's review checklist. Draws on `BONUS-Marketplace-Listing-Best-Practice.md`.

---

## Next phase

Once `docs/DESIGN.md` carries its design system (Step 3, full or Lite) and every acquisition surface your shape needs exists, move to the Develop phase: ask your agent to *"start develop"* (`develop-phase`), or open `productos/develop/DEVELOP-CHECKLIST.md`. During the build, `docs/COPY.md` guides every user-facing string; use `develop-design-better` when generating UI, `develop-design-review` before commits, and `develop-cro-audit` once the product has traffic.
