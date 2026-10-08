---
name: design-prompt-generator
description: >-
  Writes three paste-ready prompts for AI design tools (MagicPath by default; Pencil, paper.design,
  or Claude Design also work) to docs/DESIGN-PROMPTS.md: a foundation prompt carrying the
  docs/DESIGN.md tokens, then two priority screens for the product — or, for a Lite shape, its
  listing and landing visuals. Use when the user says "generate design prompts", "prompts to design
  my screens", or "what should I prompt my design tool with". Requires the Product Identity and
  design system in docs/DESIGN.md, and docs/DEFINE.md. Not for building the design system — use
  design-design-system.
---

# Design: Design Prompt Generator

Turn the locked Product Identity and design system into **three paste-ready prompts for AI design tools** and write them to `docs/DESIGN-PROMPTS.md`: Prompt 1 renders the `docs/DESIGN.md` tokens as a full component library; Prompts 2 and 3 design the two priority screens for this product type, reusing those components. **MagicPath is the default tool** (per the Design checklist); Pencil (pencil.dev), paper.design, and Claude Design take the same prompts. A prompt without brand context produces a generic AI-startup screen (purple gradient, Inter Display, abstract blobs); one with the tokens, tone, and visual style baked in produces a draft that's mostly on-brand on the first generation. No external research is needed.

## Inputs

Read inputs from `docs/` at the app repo root.

1. **`docs/DEFINE.md`** — **required.** Product type and mechanism (Summary, Offer → Mechanism), customer and use context (Offer → Customer plus the Persona), business model (Pricing Strategy). The product type drives which screens to design first. If it's missing or its Summary and Offer are placeholders, stop: tell the member to run the Define skills first (`define-offer-builder` → `define-customer-persona` → `define-pricing`, or `define-from-code` for an existing product).
2. **Product Identity** — the `## Product Identity` section of `docs/DESIGN.md`. **Required.** The Brand Card, worldview, contrarian belief, tone attributes ("X but not Y"), no-go words, example sentence, and Visual Style (lane, notes, composition rules, references). If missing, stop and point to `design-identity-creator`.
3. **The design system in `docs/DESIGN.md`** — the YAML tokens and eight sections. **Required — this is where the visuals live.** If there are no tokens, stop and point to `design-design-system` (Step 3): prompts without tokens generate generic screens.
4. **Product shape** — `docs/DEFINE.md` → `## Product Shape` → `### Primary Shape` names the slug; read only the Design route row for Step 4 in `productos/shapes/<slug>.md` (from this folder, `../../shapes/<slug>.md`). **Full** → screens (step 2's first table); **Adapted** → the screens the row names (an extension's popup and injected UI); **Optional** → offer it and, on a yes, prompt only the screens the row names (a dashboard, a client portal, a visual template's pages); **Skip** → say so in one line. When Step 3 ran Lite and no screens are being prompted, offer the **listing and landing visuals** set (step 2's second table) instead — run it only if the member wants it, otherwise name the next step and stop. No Product Shape section (a repo from before 2.0) → treat it as `web-app` unless the code or member clearly says otherwise, and suggest `define-product-shape`. If `docs/PLAN.md` schedules the step differently, the plan wins — say so.
5. **`docs/COPY.md`** — optional (from `design-ux-writing`). If present, embed the lexicon's canonical nouns and verbs and the button/label rules in the prompts so generated screens are copy-correct — no "Submit" buttons, no synonyms for the product's concepts.

## Voice

A senior design strategist and AI-design-tool prompt engineer:

- **Honor what's documented.** The Identity (words) and DESIGN.md (tokens) are the source of truth — translate them; never invent tones, palettes, scales, or type directions.
- **Compress without losing.** Every line of the brand-context block carries information the tool needs for a specific decision.
- **Specific, not generic.** Never "modern and clean" — always the actual style ("warm-neutral palette with deep ink text; documentary photography of real users; generous negative space, type-led hierarchy").

## Workflow

### 1. Read DEFINE.md, DESIGN.md, and COPY.md

Read them in full before generating anything. Extract:

- From DEFINE.md: product type, customer, mechanism, business model, use context. The product type drives step 2.
- From the Product Identity: Brand Card, worldview, contrarian belief, tone attributes, no-go words, example sentence, visual style.
- From DESIGN.md's tokens: every `colors`, `typography`, `rounded`, `spacing`, and `components` entry with its exact value, plus the elevation model and layout grid from the prose — Prompt 1 carries these verbatim.
- From COPY.md (if present): the button/label rules and the core lexicon terms.

### 2. Propose the three prompts as a set

The structure is always the same:

- **Prompt 1 — Design system foundation.** *Always this, no product-type variation.* Renders the DESIGN.md tokens as a full component library first, so the two screens inherit one component vocabulary instead of each inventing its own buttons and cards.
- **Prompts 2 and 3 — Two priority screens** for this product, from the mapping below (pick the top two; the italic alternate is offered if the member prefers it). Lite shapes use the second table instead:

| Product type | Two priority screens (alternate in italics) |
| --- | --- |
| Consumer mobile AI app | Onboarding personalization screen / Plan reveal or main feature *(alt: Paywall)* |
| B2B AI SaaS / web app | Signup or workspace creation / Dashboard or main work surface *(alt: Pricing page)* |
| Marketplace | Browse or search results / Listing detail *(alt: Checkout or booking)* |
| API / Developer tool | Marketing homepage with hero code sample / Dashboard with API keys *(alt: Pricing page)* |
| Vertical SaaS | Role-specific dashboard / Settings or admin *(alt: Login)* |
| Productized service portal | Intake form / Request queue or board *(alt: Delivery view)* |
| Browser extension | Popup (in-context) / Post-install welcome tab *(alt: Settings)* |
| Desktop / native app | Onboarding first-run / Main work surface *(alt: Preferences)* |
| Creator economy / community platform | Editor or post creation / Feed or browse *(alt: Profile or dashboard)* |
| Landing page / static site / `website` | Hero section / Features-as-benefits section *(alt: Pricing or CTA closer)* |

**Lite — listing and landing visuals only.** Prompt 1 becomes a **brand kit** (the Lite tokens rendered as logo lockups and the square icon crop, type specimens, colour swatches, buttons, and the code-block or screenshot-frame component); Prompts 2 and 3 are the two visuals the shape's acquisition surfaces need first:

| Primary shape | Two priority visuals (alternate in italics) |
| --- | --- |
| `agent-skill`, `agent-plugin` | Listing or README banner / Output showcase — the skill's real output in a terminal or chat frame *(alt: marketplace icon set)* |
| `mcp-server` | Directory icon and listing card / Landing hero showing one tool call and its result in a chat frame *(alt: README banner)* |
| `chat-assistant` | Avatar and profile card / Conversation showcase with the starters *(alt: landing hero)* |
| `developer-tool` | Landing hero with a working code sample / Docs header and quickstart page *(alt: README banner)* |
| `productized-service` | Landing hero / Deliverable showcase — a sample of what the client receives *(alt: proposal or one-pager cover)* |
| `digital-product` | Storefront cover and thumbnail / Inside-preview set — 3–4 mockups of the product in use *(alt: social preview image)* |

Size every Lite visual to the store's asset spec from `docs/MARKETPLACE-LISTING.md` or `docs/LANDING-PAGE.md` when they exist; otherwise state the size in the prompt and flag it for checking.

Present the three together as a set — Prompt 1 fixed; for Prompts 2 and 3, a one-sentence rationale per screen and the alternate — and get a confirm/correct before composing. Accept the member's own screen choices. If they want to skip Prompt 1 (rare), accept it but note the screens will be less coherent.

### 3. Compose the brand context block

A 6–10 line compressed brand summary, shown once at the top of the file *and* embedded in every prompt:

- **Brand character** (contrarian belief + tone in one line) — *"opinion-is-the-product; precise, calm, opinionated"*
- **Tone** (the 3–5 Identity attributes, ideally "X but not Y") — *"Smart, but not academic. Authentic, but not stuffy. Helpful, but not bossy."*
- **Visual style** (lane + composition rules in one sentence) — *"Documentary photography of real users in natural light; generous negative space, type-led hierarchy, hairline borders instead of shadows."*
- **Type pairing** (the families in DESIGN.md's typography tokens) — *"Newsreader for headlines, Public Sans for body."*
- **Color direction** (mood + the 2–3 decisive hexes; the full palette lives in Prompt 1) — *"Warm-neutral foundation with terracotta accent: cream surface (#F8F5F0), deep ink text (#1A1A1A), terracotta accent (#B23A2E)."*
- **What to avoid** (1–2 specifics from the Identity's no-go words and the AI-startup defaults) — *"No purple gradients, no abstract AI blobs, no Inter or Instrument Serif, never say 'AI-powered' or 'Easy to use'."*

### 4. Compose the prompts, walking them one at a time

Use the two shapes in [templates/prompts.md](templates/prompts.md): Prompt 1 carries the DESIGN.md YAML tokens verbatim (every color, typography level by its DESIGN.md name — `display-lg`, `headline-lg`, `body-md`, `label-md`…, spacing, rounded, components) and asks the tool to render and extend them, never to invent a palette or scale; Prompts 2 and 3 use the screen shape, including the "Reuse the components from the design system prompt (Prompt 1)" line.

Compose Prompt 1, show it, get a confirm or a fix, then Prompt 2, then Prompt 3 — the layout and copy conversation per screen is the value. Ask per prompt: *"Does this read as on-brand? Anything to rework?"*

**Hard constraints on every prompt:**

- **Paste-ready.** Every `[bracketed]` slot filled with real content; nothing left for the member to fill; no markdown that breaks on paste.
- **Fonts.** The families come from DESIGN.md's typography tokens. They must be free for commercial use and never Inter, Instrument Serif, Outfit, or Plus Jakarta Sans. If a substitute is needed (DESIGN.md names a banned or paid family), surface it to the member and use an acceptable free pick: Newsreader, Fraunces, Bricolage Grotesque, Source Serif 4, Schibsted Grotesk, Public Sans, Manrope, Hanken Grotesk, Cormorant Garamond, DM Serif Display, Spectral, Albert Sans, Onest, Funnel Sans/Display, JetBrains Mono, DM Mono, Geist / Geist Mono, Satoshi, General Sans, Switzer.
- **Character.** The tone words and contrarian belief constrain every visual decision — a calm-authority brand's screens don't read like a punk brand's.
- **No-go words.** Every copy hint passes the Identity's tone test and COPY.md's rules — no category-default copy ("AI-powered", "Easy to use", "The best app for X", "Built for teams", "Modern and intuitive").
- **DESIGN.md reference.** Each prompt ends: *"Use tokens from docs/DESIGN.md where applicable for exact colors, type, spacing, and component styling."*

### 5. Write `docs/DESIGN-PROMPTS.md`

Once all three are approved, write the file using [templates/design-prompts-md.md](templates/design-prompts-md.md) (`mkdir -p docs` if needed). If it already exists, read it first, preserve the member's edits, show the diff, and overwrite only on approval. Bullets, code blocks, exact copy in quotes — the doc reads in under 3 minutes.

## Verify before delivering

- [ ] **Prompt 1** carries every DESIGN.md color, typography level (by its DESIGN.md name), spacing, rounded, and component token verbatim, and covers foundations, the full component set (buttons, forms, cards, modals, navigation, lists/tables, badges, avatars, tooltips, toasts, icons, empty/loading/error states, progress), motion, and layout — without inventing tokens. Lite: the brand kit covers every Lite token plus logo lockups and the square icon crop.
- [ ] **Prompts 2 and 3** are priority screens for this product type (Lite: the shape's two priority visuals, with sizes stated), each with a one-sentence purpose and journey position, and both include the "Reuse the components from Prompt 1" line.
- [ ] The brand context block appears once at the top and is embedded, identical, in all three prompts — consistent with the Product Identity.
- [ ] Fonts are DESIGN.md's, free for commercial use, and off the exclusion list.
- [ ] Every prompt is paste-ready: in a triple-backtick block, no leftover brackets, no paste-breaking markdown.
- [ ] Every copy hint passes the tone-of-voice test (and COPY.md's rules when present) — no category-default copy.
- [ ] Every prompt ends with the `docs/DESIGN.md` token reference line.
- [ ] "How to use this file" says to start with Prompt 1; the file is dated and sources are listed.

Give the member the file path and a tight recap: one line for the brand context (character + tone + type pairing), one confirming the design system prompt, and two naming the priority screens.

**Next:** set up the design tool with `productos/design/BONUS-Design-Tool-Setup.md`, paste Prompt 1 first, then Prompts 2 and 3 on the same canvas. If the design system changes, update it via `design-design-system` and re-run this skill.
