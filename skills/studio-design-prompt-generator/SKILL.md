---
name: studio-design-prompt-generator
description: >-
  Use when the user has a finished `productos/design/1-Product-Identity.md` and `docs/PRODUCT.md` and wants paste-ready prompts for AI design tools (Pencil, paper.design, Claude Design, or MagicPath) that produce on-brand designs immediately. Triggers on phrases like "generate design prompts", "create AI design prompts", "make screen prompts for my product", "give me prompts for Claude Design / Pencil / paper / MagicPath", "prompts to design my screens", "draft my screens with AI", "give me a design prompt for [screen]", "what should I prompt my AI design tool with", or any request to translate the Product Identity into design-tool prompts. Reads both source files and writes `productos/design/Design-Prompts.md` with three prompts: Prompt 1 is always a comprehensive UI design system foundation (colors, typography, components, layout, motion) so screens share a consistent component vocabulary; Prompts 2 and 3 are two priority screens for the product type.
---

# Design: Design Prompt Generator

This skill turns a finished Product Identity and Design System into **three paste-ready prompts for AI design tools** — Pencil (pencil.dev), paper.design, Claude Design, or MagicPath. The output is `productos/design/Design-Prompts.md` containing one prompt per priority screen for the user's specific product, with the full brand identity context (brand character, tone, visual style, type pairing, colour palette, what-to-avoid) embedded inside every prompt so the generated designs are on-brand from screen one.

The voice is a senior design strategist and prompt engineer with deep experience extracting brand context into compressed, AI-tool-ingestible format — and specifically with the 2026 generation of AI design tools (Pencil at pencil.dev, paper.design, Claude Design, MagicPath) that take 200–500 word prompts and produce usable screen drafts in seconds. The strategist's job is not to invent new design direction; it is to faithfully translate the documented Product Identity into the specific format AI design tools consume best, and to pick the three screens that produce the most useful drafts first.

A design prompt without brand context produces a generic AI-startup screen — purple gradient, Inter Display, abstract blob illustration. A design prompt with the full contrarian belief, tone, visual style, palette, and font pairing baked in produces a draft that's 80% on-brand on the first generation. This skill's job is to write prompts in that second category.

> **Session length:** Designed to be completable in 15–30 minutes of conversation. The skill reads two upstream documents, proposes three screens, composes the prompts, and writes the file. No external research is required — all category-specific patterns live in the Product Identity already.

## Inputs

Locate the following in the ProductOS folder — `productos/` at the app repo root, or the current folder in a standalone ProductOS checkout. Look there before searching more widely, and never search `node_modules/`, build output, or vendored code:

1. **PRODUCT.md** — usually `docs/PRODUCT.md`. **Required.** Provides the product type, customer, mechanism, and use context. The product type drives which three screens are most useful to design first. If PRODUCT.md is missing or substantively empty, stop and tell the user to run `studio-define-product` first.

2. **Product Identity** — usually `productos/design/1-Product-Identity.md`. **Required.** Provides the words: the Brand Card, worldview, contrarian belief, tone-of-voice attributes (the "X but not Y" phrases), no-go words, example sentence, and Visual Style (lane, notes, references). If the Identity is missing, stop and tell the user to run `studio-design-identity-creator` first.

3. **DESIGN.md** — usually `docs/DESIGN.md` (with its `docs/DESIGN.html` mirror). **Required — this is where the visuals live.** Produced by `studio-design-design-system` in Step 2: the palette hexes, font pairing, spacing, shapes, and component tokens every prompt embeds. If it's missing, stop and tell the user to run Step 2 first — prompts without tokens generate generic AI-startup screens.

## The strategist's voice

Adopt the voice of a senior design strategist and AI-design-tool prompt engineer:

- **Honor what's documented.** The Product Identity (words) and DESIGN.md (tokens) are the source of truth. Don't invent new tones, palettes, or type directions — translate the documented ones into the prompt format.
- **Compress without losing.** The brand-context block is 6–10 lines. Every line carries information the AI design tool needs to make a specific decision. Cut filler; keep specificity.
- **Paste-ready, always.** Every prompt is wrapped in a triple-backtick code block. Every value is filled with content derived from PRODUCT.md and the Identity — no `[bracketed]` placeholders left undefined.
- **Specific, not generic.** Never "modern and clean." Always the actual visual style ("warm-neutral palette with deep ink text; documentary photography of real users; generous negative space, type-led hierarchy").
- **Honor the font and copy bans.** DESIGN.md's typography tokens name the committed fonts. Inter, Instrument Serif, Outfit, and Plus Jakarta Sans are off-limits. Category-default copy ("AI-powered", "Easy to use") is off-limits.

## Workflow

### 1. Read PRODUCT.md and Product Identity

Read both files in full before generating anything. Extract:

- From PRODUCT.md: product type, customer, mechanism, business model, and use context. The product type is the load-bearing input — it drives the screen selection in step 2.
- From Product Identity: the Brand Card, worldview, contrarian belief, tone-of-voice attributes, no-go words, example sentence, visual style (lane, style notes, composition rules, named references).
- From DESIGN.md: the colour tokens (with hexes), the typography tokens (families, sizes, weights), spacing and rounded scales, elevation model, and the component list — the concrete values every prompt embeds.

### 2. Pick the three prompts (one design system + two priority screens)

The three generated prompts always follow the same structure:

- **Prompt 1 — Full UI design system component set.** *Always this — no product-type variation.* This is the foundation the screens are built on: color palette, typography scale, button variants, form elements, cards, navigation, modals, lists, tables, badges, avatars, tooltips, toasts, empty/loading/error states, icons, spacing scale, border radius, shadow/elevation, motion principles. The AI design tool generates the entire component library in one pass, anchored to the brand's palette, fonts, and visual style. Generating this first means the next two screen prompts inherit a consistent component vocabulary rather than each making up their own buttons and cards.

- **Prompts 2 and 3 — Two priority screens.** The two most important screens for the user's specific product, picked from the product-type mapping below.

Use this product-type → priority-screen mapping for prompts 2 and 3 (pick the top two; the third option in each cell is an alternate if the user prefers it):

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
| Landing page / static site | Hero section / Features-as-benefits section *(alt: Pricing or CTA closer)* |

State the three proposed prompts back to the user — Prompt 1 (design system) is fixed; for Prompts 2 and 3, give a one-sentence rationale per screen and the alternate option from the table. Get a confirm/correct before composing. If the user wants different priority screens, accept their choices. If the user wants to skip the design system prompt entirely (rare), accept that too — but note that the screens will be less coherent without it.

### 3. Compose the brand context block

Build a 6–10 line compressed summary of the brand identity that any AI design tool can ingest as design direction. This block is used at the top of the Design Prompts file *and* embedded inside every per-screen prompt. Include:

- **Brand character** (contrarian belief + tone in one line) — e.g., *"opinion-is-the-product; precise, calm, opinionated"*
- **Tone** (the 3–5 voice attributes from the Identity, ideally in the Mailchimp "X but not Y" form) — e.g., *"Smart, but not academic. Authentic, but not stuffy. Helpful, but not bossy."*
- **Visual style** (one sentence pulled from the Visual Style section — imagery lane + composition rules) — e.g., *"Documentary photography of real users in natural light; generous negative space, type-led hierarchy, hairline borders instead of shadows."*
- **Type pairing** (the two typefaces from DESIGN.md's typography tokens — both must be free for commercial use and outside the exclusion list) — e.g., *"Newsreader for headlines, Public Sans for body."*
- **Color direction** (one sentence — mood + 2–3 hex values where decisive; do not prescribe a full token system, the Design System skill handles that) — e.g., *"Warm-neutral foundation with terracotta accent: cream surface (#F8F5F0), deep ink text (#1A1A1A), terracotta accent (#B23A2E)."*
- **What to avoid** (1–2 specific things, drawn from the Identity's no-go words and the global AI-startup defaults) — e.g., *"No purple gradients, no abstract AI blobs, no Inter or Instrument Serif, never say 'AI-powered' or 'Easy to use'."*

### 4. Compose the three prompts

#### Prompt 1 — Design system foundation (always this; goes first)

This prompt asks the AI design tool to generate a comprehensive UI component library before any specific screens. Use this structure:

```
Design a complete UI design system foundation for [product description in one sentence].

Brand identity:
[paste the brand context block from step 3]

What to design:
A comprehensive component library covering everything needed to build the product's screens consistently. Output the full set, organised by category:

Foundations
- Color palette: primary, secondary, accent, neutral scale (5–9 steps from light to dark), and semantic colors (success, warning, error, info). Include hex values for each.
- Typography scale: display, h1, h2, h3, body large, body, body small, caption, label. Use the type pairing from the Brand identity block above. Show font family, size (px), weight, line-height, letter-spacing for each.
- Spacing scale: 4 / 8 / 12 / 16 / 24 / 32 / 48 / 64 px (or a documented variant).
- Border radius scale: none / sm / md / lg / pill.
- Shadow / elevation scale: 0 (flat) through 4 (high). Soft shadows or hairline borders — choose one based on the tone and visual style.
- Motion: standard easing curve, standard duration (e.g., 200ms), entrance vs interaction.

Components
- Buttons: primary, secondary, tertiary/ghost, destructive. Sizes (sm, md, lg). States (default, hover, active, focus, disabled, loading).
- Form elements: text input, textarea, select, checkbox, radio, toggle/switch, slider, file upload, search. With label, helper text, error state.
- Cards: default, elevated, interactive (hover). With optional header, body, footer.
- Modal / dialog: with overlay, header, body, footer, close.
- Navigation: top nav, side nav, breadcrumbs, tabs, pagination, dropdown menu.
- Lists & tables: list item with avatar / leading icon / trailing action; table with header row, sortable columns, row hover.
- Badges, tags, chips: solid / outlined / removable.
- Avatar: image, initials, group / stack. Sizes.
- Tooltips & popovers.
- Toasts, alerts, banners: info, success, warning, error.
- Icons: line vs filled, stroke weight, corner style — choose one based on the tone and visual style. Show ~10 representative icons in the style.
- Empty states, loading states (skeletons), error states.
- Progress indicators: bar, circular, stepper.

Layout
- Grid: column count, gutter width, max content width.
- Responsive breakpoints (mobile, tablet, desktop) if the product is web/desktop; mobile sizing if mobile-first.

Visual notes:
- [specific compositional rule from Visual Style — e.g., "generous negative space, type-led hierarchy, hairline borders instead of shadows"]
- [accessibility note — e.g., "maintain WCAG AA contrast for all text-on-color pairings; never rely on color alone to convey state"]
- [overall feel anchored in the tone of voice — e.g., "Calm, precise, considered — every component reads as quietly competent, never showy"]

Present the design system as a tidy sticker sheet or single canvas, grouped by category, with clear section headings.
```

Like the screen prompts, this must be **paste-ready** — every `[bracketed]` placeholder filled with content derived from PRODUCT.md and the Identity. The brand identity block is the same one used in Prompts 2 and 3, ensuring consistency across the trio.

#### Prompts 2 and 3 — Priority screens

For each of the two priority screens, build a paste-ready prompt with this structure:

```
Design a [screen type] for [product description in one sentence].

Brand identity:
[paste the brand context block from step 3]

Screen purpose:
[1-2 sentence description of what this screen does and where it sits in the user journey]

Layout (top to bottom):
- [section 1 — what it contains, key elements]
- [section 2 — what it contains, key elements]
- [section 3 — what it contains, key elements]
- [section 4 — what it contains, key elements if applicable]

Content / copy hints:
- Headline: "[exact headline in the brand voice]"
- Sub-headline / supporting copy: "[exact copy]"
- CTAs: "[exact CTA text, 3-5 words, first-person where applicable]"
- Other key labels: "[as needed]"

Visual notes:
- [device frame: mobile / tablet / desktop / responsive]
- [specific compositional rule from Visual Style — e.g., "generous negative space, type-led hierarchy"]
- [accessibility note — e.g., "maintain WCAG AA contrast for body text"]
- Reuse the components from the design system prompt (Prompt 1) — same buttons, same form elements, same cards.

What this screen should feel like:
- [one sentence anchored in the tone of voice — e.g., "Calm and considered — the user should feel the AI is doing thoughtful work on their behalf, not racing them"]
```

The "reuse the components from the design system prompt" line is the load-bearing addition compared to a generic screen prompt — it tells the AI design tool that the screens should pull from the just-generated design system rather than inventing new component styles.

Both screen prompts must be **paste-ready** — no markdown placeholders the user has to fill in, no `[bracketed]` notes left undefined. Every value is filled with the actual content derived from the Product Identity and PRODUCT.md.

**Hard constraints on every prompt:**

- **Font constraint.** The two recommended typefaces must be free for commercial use (Google Fonts, Fontshare, or open source like Vercel's Geist) and **must not** include Inter, Instrument Serif, Outfit, or Plus Jakarta Sans. Default to DESIGN.md's typography tokens; if a substitute is needed, acceptable picks: Newsreader, Fraunces, Bricolage Grotesque, Source Serif 4, Schibsted Grotesk, Public Sans, Manrope, Hanken Grotesk, Cormorant Garamond, DM Serif Display, Spectral, Albert Sans, Onest, Funnel Sans/Display, JetBrains Mono, DM Mono (all Google Fonts), Geist / Geist Mono (Vercel, open source), Satoshi, General Sans, Switzer (all Fontshare).
- **Character constraint.** A calm-authority brand's screens don't read like a punk brand's. The tone words and contrarian belief constrain every visual decision in the prompts.
- **No-go words.** Every copy hint must pass the tone-of-voice test from the Identity. No category-default copy ("AI-powered", "Easy to use", "The best app for X", "Built for teams", "Modern and intuitive").
- **DESIGN.md reference.** Add a line at the end of each prompt: *"Use tokens from `docs/DESIGN.md` where applicable for exact colors, type, spacing, and component styling."*

### 5. Show the user and iterate

Present the three composed prompts in conversation. Ask one question: *"Do these read as on-brand? Any prompt I should rework before writing the file?"* Iterate once if needed — usually the user spots something specific about screen layout or copy that needs adjustment.

### 6. Write `productos/design/Design-Prompts.md`

Once approved, write the assembled file. If the file already exists, read it first, surface the diff in conversation, overwrite on the user's approval.

Structure:

```
# Design Prompts

*Drafted: [Month Year]. Generated from `docs/PRODUCT.md` and `productos/design/1-Product-Identity.md`. Paste each prompt below into Pencil (pencil.dev), paper.design, Claude Design, or MagicPath to generate that screen's design — the brand context is already in the prompt so the output is on-brand.*

## How to use this file

1. Open your AI design tool — Pencil (pencil.dev), paper.design, Claude Design, or MagicPath.
2. **Start with Prompt 1 (the design system).** Generate the component library first; it becomes the visual foundation the next two screens are built on.
3. Copy the entire prompt for what you want to design — from "Design a..." through the last line of the prompt.
4. Paste into the tool. The brand identity is embedded in every prompt.
5. Iterate with the AI tool on layout, hierarchy, or content as needed.
6. `docs/DESIGN.md` (produced in Step 2) is the source of truth for exact tokens — but these prompts will still produce on-brand drafts.

---

## Brand identity context (embedded in every prompt below)

[The compressed 6-10 line brand context block from step 3, surfaced once at the top of the file so the user can see what's being passed to each prompt.]

---

## Prompt 1: Design system foundation

**Purpose:** Generate the full UI component library that Prompts 2 and 3 will reuse — colors, typography, components, layout, motion. Run this first.

### Prompt — paste this into your AI design tool

\`\`\`
[The complete paste-ready design system prompt from step 4]
\`\`\`

---

## Prompt 2: [Screen Name]

**Purpose:** [one sentence]
**Position in journey:** [pre-signup / first session / day 1 / etc.]

### Prompt — paste this into your AI design tool

\`\`\`
[The complete paste-ready screen prompt — includes the "Reuse the components from Prompt 1" line]
\`\`\`

---

## Prompt 3: [Screen Name]

**Purpose:** [one sentence]
**Position in journey:** [...]

### Prompt — paste this into your AI design tool

\`\`\`
[The complete paste-ready screen prompt — includes the "Reuse the components from Prompt 1" line]
\`\`\`

---

## Sources

- Product context: `docs/PRODUCT.md`
- Brand strategy: `productos/design/1-Product-Identity.md`
- Design tokens: `docs/DESIGN.md`
```

Use code blocks (triple-backtick) around each prompt so the user can click-to-copy in markdown viewers without picking up the surrounding markdown formatting.

### 7. Verify before delivering

Re-read the written file and check:

- **Prompt 1 is the design system foundation** — covers colors, typography, foundations (spacing, radius, elevation, motion), components (buttons, forms, cards, modals, navigation, lists/tables, badges, avatars, tooltips, toasts, icons, states, progress), and layout. Anchored in the brand's palette, fonts, and visual style.
- **Prompts 2 and 3 are priority screens** for the user's specific product type, each with a one-sentence purpose and journey position. Both include the "Reuse the components from the design system prompt (Prompt 1)" line so the screens inherit the just-generated component vocabulary.
- The brand context block (brand character, tone, visual style, type pairing, color direction, what-to-avoid) is consistent across all three prompts and consistent with the Product Identity file.
- The two recommended typefaces in every prompt are free for commercial use and outside the exclusion list (no Inter, Instrument Serif, Outfit, or Plus Jakarta Sans).
- Every prompt is paste-ready — no leftover `[bracketed]` placeholders, no unfilled values, no markdown formatting that breaks when pasted into an AI design tool.
- Every copy hint passes the tone-of-voice test from the Identity — no category-default copy.
- The prompts are wrapped in triple-backtick code blocks so the user can copy-paste cleanly.
- Each prompt references `docs/DESIGN.md` for token specifics.

Deliver via a `computer://` link and a short summary — one line for the brand context (character + tone + type pairing), one line confirming the design system prompt, and two lines naming the two priority screens. Keep the summary tight: this is a recap, not a re-pitch.

## Pacing and approval

- **Read both upstream inputs before composing anything.** PRODUCT.md drives screen selection; the Identity drives every line of every prompt.
- **One screen at a time when composing.** Don't dump all three prompts at once. The conversation about the layout and copy is the value.
- **Honor the font ban, the brand character, and the no-go words.** Three hard constraints that catch most failure modes.
- **Compress the brand context block, don't summarize.** Every line carries information the AI design tool will use to make a specific visual decision.
- **Write the final document concisely.** Bullets, code blocks, exact copy in quotes. The whole doc reads in under 3 minutes.

## What "done" looks like

A `productos/design/Design-Prompts.md` where:

- **Prompt 1 is the design system foundation** — a paste-ready prompt covering colors, typography, foundations (spacing, radius, elevation, motion), components (buttons, forms, cards, modals, navigation, lists/tables, badges, avatars, tooltips, toasts, icons, empty/loading/error states, progress), and layout. Always this; no product-type variation.
- **Prompts 2 and 3 are two priority screens** for the user's specific product type, each with a one-sentence purpose and a journey position. Both prompts explicitly tell the AI design tool to **reuse the components from Prompt 1** so the screens inherit a coherent component vocabulary.
- **A compressed brand-context block** (brand character, tone, visual style, type pairing, color direction, what-to-avoid) appears once at the top of the file and is embedded inside all three prompts.
- **Every prompt is paste-ready** — wrapped in a triple-backtick code block, no `[bracketed]` placeholders left undefined, no markdown formatting that breaks on paste, every value filled with content derived from PRODUCT.md and the Product Identity.
- **The two recommended typefaces** in every prompt are free for commercial use and outside the exclusion list (no Inter, Instrument Serif, Outfit, or Plus Jakarta Sans).
- **Every copy hint** in every prompt passes the tone-of-voice test from the Identity.
- **The "How to use this file" section** tells the user to start with Prompt 1 (design system) before generating the screens.
- **The file references `docs/DESIGN.md`** as the source of truth for tokens, but stands alone if that file doesn't exist yet.
- **The file is dated** and sources are listed at the bottom.

Recommended next step after a successful session: paste **Prompt 1 (the design system)** into Pencil (pencil.dev), paper.design, Claude Design, or MagicPath first — generate the component library, then run Prompts 2 and 3 against the same canvas so the screens pull from the just-generated components. The brand identity is already embedded in every prompt, so the output should be immediately on-brand. After generating initial drafts, run the **`studio-design-design-system`** skill to produce a `docs/DESIGN.md` file with exact tokens — once that's in place, re-running this skill will produce prompts that reference the tokens directly, yielding even more accurate token-aligned output from AI design tools.
