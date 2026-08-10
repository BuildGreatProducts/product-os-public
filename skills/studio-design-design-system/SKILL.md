---
name: studio-design-design-system
description: >-
  Use when the user wants to turn an image reference — a screenshot, mockup, Figma URL, or live website they love — into their Design System. Triggers on phrases like "build my design system", "create my DESIGN.md", "design from image", "image to design system", "translate this screenshot into a design system", "extract design tokens", "make my design.md", "here's a site I love, capture its design", or when the user shares an image/URL in a design context with no other clear intent. Produces two mirrored artifacts: docs/DESIGN.md (Google-format YAML tokens + prose, the source of truth coding agents read) and docs/DESIGN.html (a self-contained live style guide for the human). Reads the image(s), asks only the context questions the ProductOS docs don't already answer, derives the tokens, reconciles them with the Product Identity, and writes both files together. Design phase Step 2 — runs right after the Product Identity and supplies the colours, fonts, and tokens the identity leaves undecided.
---

# Design: Design System (image → DESIGN.md + DESIGN.html)

This skill takes an **image reference the user loves** — a screenshot, mockup, Figma file, or live website — and translates it into a design system captured as **two mirrored files**:

- **`docs/DESIGN.md`** — YAML tokens in [Google's open design.md format](https://github.com/google-labs-code/design.md) plus prose rationale. The **source of truth** — AI coding agents (Claude Code, Cursor, Kiro, Stitch) read it automatically to make brand-consistent decisions.
- **`docs/DESIGN.html`** — a self-contained, human-readable style guide that renders every token and component live in a browser, styled directly from the same token values. The **mirror** the human opens.

Same system, two audiences: the agent reads the `.md`, the human opens the `.html`. They are always written and updated together so they never drift.

In ProductOS this is **Design phase Step 2**, immediately after the Product Identity. The identity supplies the *words* (name, worldview, contrarian belief, tone, visual style direction) and deliberately leaves the *visuals* undecided — this skill derives the colours, fonts, spacing, shapes, and components from a real image, guided by those words. The user's job before this session: find one image or site that looks the way the brand *feels*. The Visual Style references in the identity are the natural hunting ground.

> **Session length:** 30–60 minutes. The user supplies the image; Claude does the visual analysis, the token extraction, the identity reconciliation, and both file writes. Already have a codebase instead of an image? `studio-design-design-system-from-code` reverse-engineers the system from the code.

## Modes

- **No image provided yet:** ask for one (Step 0) before doing anything else. Don't draft a DESIGN.md from imagination. If the user has no image after one prompt, offer the weak fallback: *"I can draft a starter system from your Product Identity's words alone and we'll refine it — but it will be far weaker than working from an image you love. Want to proceed that way, or grab a reference first?"*
- **`docs/DESIGN.md` already exists:** read it (and `docs/DESIGN.html` if present) and ask what they want — refine specific tokens, replace with a fresh analysis from new imagery, or merge. Confirm before destructive overwrites. Whatever changes, regenerate `docs/DESIGN.html` so it stays in sync.
- **Partial conversation:** if the session was interrupted mid-flow, note where it left off and resume from that step. Don't restart.

## Inputs

1. **An image reference (or several).** **Required — the primary anchor.** Accepted forms:
   - **Local image paths** (PNG / JPG / WebP / screenshots) — read with the Read tool, which renders images visually.
   - **Figma URLs** (`figma.com/design/...`, `/board/...`, `/make/...`) — use the Figma MCP tools (`get_design_context`, `get_screenshot`, `get_metadata`) if connected.
   - **Live website URLs** — you can't screenshot arbitrary URLs without browser tooling; ask the user to paste a screenshot of the site, and use WebFetch on the URL only as a supplementary signal (font names, colour values in CSS) — never as the primary visual source.
   - **A mix.** If multiple, ask which is the **primary anchor** and which are mood references — the primary drives the token decisions.
2. **The Product Identity** — usually `productos/design/1. Product Identity.md`. **Required.** Supplies the words: name, worldview, contrarian belief, tone of voice, visual style (lane, style notes, composition rules, references). If missing or substantively empty, stop and point to `studio-design-identity-creator` first.
3. **PRODUCT.md** — usually `docs/PRODUCT.md`. **Required.** What the product is, who uses it, in what context — a productivity tool's system differs structurally from a consumer app's even with the same brand character.
4. **The Reference DESIGN.md** — `REFERENCE-DESIGN.md` in this skill's folder. Read once at the start: it demonstrates the exact format, YAML schema, and `{path.to.token}` conventions. Use it as the structural template only — **never copy its design choices.**

## The engineer's voice

A senior design director and systems engineer with strong taste. **Observant** — describe what you actually see in the imagery, not what you assume. **Decisive** — when the user is uncertain, recommend a direction with a one-line rationale. **Token-fluent** — every recommendation lands as a token: not "a soft red," but `error: "#B23A2E"`. **Strict to the spec** — section order, YAML schema, and token-reference syntax are fixed; do not improvise the format. And don't flatter weak references: if the imagery is conflicting or thin, say so and ask which direction to anchor on.

## Workflow

### 0. Image intake

Read the identity and PRODUCT.md first, then open with:

> *"Share the image (or images) you want me to translate — a screenshot of a product you love, a marketing site capture, a Figma link, or a mix. If you have several, tell me which is the primary anchor. Your identity's Visual Style references are a good place to hunt."*

### 1. Image analysis

Read every image carefully before asking anything. Don't generalize — describe what you actually see. Extract per image:

- **Colours** — approximate hexes for backgrounds, surfaces, primary/secondary text, accents, borders, semantic states. Dominant vs accent. Light or dark mode. (Extraction patterns below.)
- **Typography** — typeface character (geometric sans / humanist sans / serif / slab / display / mono), hierarchy levels, approximate sizes and weights, letter-spacing tendencies, uppercase usage.
- **Spacing & density** — tight, comfortable, or generous; visible scale (4/8/16/24/32).
- **Shapes** — corner-radius philosophy, and whether it varies by component class.
- **Elevation** — soft shadows, hard shadows, hairline borders, glass/blur, tonal layering, or flat.
- **Components** — visible atoms (buttons, inputs, chips, cards, nav, tables, modals, toasts), variants, states.
- **Mood** — two or three concrete adjectives.

Summarize back in 5–8 tight bullets, mirroring the imagery's actual character. If two references conflict, name the conflict.

### 2. Context questions — only the ones ProductOS hasn't answered

Ask one at a time, offering 3 tailored suggestions drawn from the analysis. **Skip everything the docs already answer:** the product, audience, and use context come from PRODUCT.md; the emotional tone, worldview, belief, and imagery lane come from the Product Identity — acknowledge what's known instead of re-asking. What's left:

1. **Colour role assignments** — from the colours spotted: which is `primary`, which is the accent, which carry semantic meaning? Light, dark, or both? Suggest a mapping.
2. **Typography confirmation** — confirm the typeface direction and the scale levels the product needs. (Free-fonts rule below applies.)
3. **Spacing density** — tight / comfortable / generous; suggest from what you observed.
4. **Shape language** — sharp / soft / fully rounded / mixed, and what that signals.
5. **Elevation philosophy** — shadows / borders / glass / flat; recommend based on the image and the identity's visual style.
6. **Component priorities** — which components matter for the MVP; cap at 6–10 (variants/states count).
7. **Anti-patterns** — three things this design must never become; these feed the Don'ts and protect the system over time.

If an answer is vague, push back with a recommendation rather than another open-ended question.

### 3. Reconcile the image with the Product Identity

The identity is the strategic anchor; the image is the aesthetic anchor. On conflict: **identity wins on strategy** (worldview, belief, tone, visual lane), **image wins on tactics** (hexes, radii, component rhythm) — unless the image violates a Visual Style rule already documented. Common conflicts:

- **Image is dark mode, identity is calm/editorial** → propose dual-mode (light primary, dark variant) or treat the image as moodboard-not-blueprint.
- **Image uses a banned or paid font** → substitute a free equivalent (rules below) and surface the substitution.
- **Image has heavy shadows, identity tone is "calm + precise"** → hairline borders + tonal layering.
- **Image palette is over-saturated for the brand's tone** → de-saturate extracted hexes 10–20%.

Surface every conflict explicitly, propose the resolution, get a one-sentence confirm, move on. Silent reconciliation is how design systems drift.

### 4. Token derivation

Compose the YAML frontmatter to the spec exactly:

```yaml
---
version: alpha
name: <Design System Name>
description: <one-sentence description>
colors:
  <token-name>: "<#hex>"
typography:
  <token-name>:
    fontFamily: <family>
    fontSize: <px>
    fontWeight: <number>
    lineHeight: <number-or-px>
    letterSpacing: <em>  # optional
rounded:
  <scale-level>: <dimension>
spacing:
  <scale-level>: <dimension>
components:
  <component-name>:
    backgroundColor: "{colors.<token>}"
    textColor: "{colors.<token>}"
    typography: "{typography.<token>}"
    rounded: "{rounded.<token>}"
    padding: <dimension>
    height: <dimension>  # optional
---
```

**Rules:**

- Hex colours are quoted `"#RRGGBB"` strings. Dimensions use `px`/`em`/`rem`; letter-spacing may be negative em.
- **Semantic names beat appearance names:** `primary`, `on-primary`, `surface`, `surface-container`, `on-surface`, `on-surface-variant`, `outline`, `outline-variant`, `error`, `success`, `warning`, `info` — never `blue`, `lightGray`.
- Typography levels: `display-lg`, `headline-lg/md`, `body-lg/md/sm`, `label-md/sm` — aim for 6–10, never exceed 15. Rounded: `none/sm/md/lg/xl/full`. Spacing: `xs/sm/md/lg/xl` plus `gutter`/`margin` where used repeatedly.
- Component values **reference tokens** with `{path.to.token}` syntax wherever a token exists; inline literals only when nothing matches.
- **Variants are sibling entries** — `button-primary` and `button-primary-hover`, never nested children.
- Valid component properties: `backgroundColor`, `textColor`, `typography`, `rounded`, `padding`, `size`, `height`, `width`. Others trigger parser warnings — avoid unless deliberate.
- No duplicate `##` headings in the prose (the spec rejects them).

**Fonts must be free for commercial use** (Google Fonts, Fontshare, Vercel's Geist) and **never** the vibe-coded defaults: **Inter, Instrument Serif, Outfit, Plus Jakarta Sans**. If the image clearly uses a banned or paid font, substitute the closest free equivalent and surface it. Common substitutions: Söhne → Public Sans or Hanken Grotesk; GT America → Schibsted Grotesk; Tiempos → Newsreader; Inter → Public Sans or Manrope; Suisse Int'l → Public Sans; Helvetica Now → Public Sans. Distinctive free picks: Fraunces, Newsreader, Bricolage Grotesque, Source Serif 4, Schibsted Grotesk, Public Sans, Manrope, Hanken Grotesk, Cormorant Garamond, DM Serif Display, Spectral, Albert Sans, Onest, Funnel Sans/Display, JetBrains Mono, DM Mono, Geist/Geist Mono, Satoshi, General Sans, Switzer.

### 5. Prose drafting

Draft the eight canonical sections, in this exact order, each 3–8 tight sentences. Don't restate the YAML — explain the *why*, so a coding agent can make sound choices in cases the tokens don't cover:

1. **`## Brand & Style`** — the look-and-feel north star. Pulls from PRODUCT.md (what it is) + the identity (worldview, belief, tone, visual style). Names the aesthetic intent in one phrase and the emotional response the UI should evoke, plus one or two anti-patterns.
2. **`## Colors`** — palette strategy: what `primary`, accent, `surface`, and semantic colours do and why those values. Note WCAG AA contrast intent.
3. **`## Typography`** — the pairing's character and what each scale level is for. Treatment rules (uppercase labels, tabular numerals).
4. **`## Layout & Spacing`** — grid model, max content widths, density philosophy, how spacing tokens map to layout.
5. **`## Elevation & Depth`** — the depth model (shadows / borders / glass / tonal / flat) and why it fits this brand.
6. **`## Shapes`** — corner-radius philosophy; intentional differences by component class.
7. **`## Components`** — how buttons, inputs, chips, cards behave; variant and state rules. Every YAML component explained here, and vice versa.
8. **`## Do's and Don'ts`** — 4–6 do's and 4–6 don'ts, specific and enforceable, drawn from the anti-patterns answer and the identity.

### 6. Confirm and write `docs/DESIGN.md`

Show the user a brief outline first — the token names chosen (colour tokens, type levels, rounded/spacing scales, component list) and a one-line summary per prose section. Fold in last edits. Then write to `docs/DESIGN.md` (create `docs/` if needed; if the file exists, show the diff and get approval to overwrite).

Verify the write succeeded before confirming. On failure, surface a clear message by cause: permission denied ("the directory isn't writable — check folder permissions"), disk full ("free up space and I'll retry"), existing-file conflict ("want me to save under a different name or overwrite?"), anything else (report verbatim and ask). Only say "saved" after verification — then build the mirror.

### 7. Build the `docs/DESIGN.html` mirror

The HTML is the human-readable twin — generated **from the tokens just written**, not from a fresh interpretation of the imagery. Requirements:

- **Self-contained and dependency-free.** One file that opens in any browser: all CSS inline in a `<style>` block, no frameworks, no external JS. Web fonts may load via a Google Fonts `<link>` when the typeface needs it.
- **Token-driven.** Declare every YAML token as a CSS custom property in `:root` (`--color-primary`, `--type-headline-lg-size`, `--rounded-md`, `--space-md`). Every swatch, specimen, and component styles itself from those variables — never hardcode a value that exists as a token.
- **Mirrors the md's section order**, so the two files read side by side.
- If the system defines **both light and dark modes**, include a small vanilla-JS theme toggle flipping a `data-theme` attribute and define both token sets.

Sections, in order: **Header** (name, description, "human-readable mirror of `docs/DESIGN.md`") → **Colors** (a swatch per token: block, name, hex, and a line of text in the paired `on-` colour) → **Typography** (each level as a live specimen at its real family/size/weight, spec beside it) → **Spacing** (labeled bars showing the rhythm) → **Radius** (sample boxes per `rounded` value) → **Elevation** (a card per level) → **Components** (every `components:` entry built and rendered live, variants and states grouped; render un-triggerable states like hover as labeled static copies) → **Do's and Don'ts** (two columns, ✓/✗, small visual examples where they help).

Keep the page's own chrome neutral — it's a reference style guide, not a marketing page. Write to `docs/DESIGN.html` with the same write-error handling. **The `.md` and `.html` are always written together — never leave one updated and the other stale.**

### 8. Verify and hand off

Re-read both files and check: YAML parses (consistent indentation, quoted hexes); all eight sections present in order; every YAML component explained in prose and vice versa; token references use exact `{colors.primary}` syntax; all fonts free and off the banned list; every component's `backgroundColor`+`textColor` pair meets WCAG AA (4.5:1 body, 3:1 large — flag and fix failures before delivering); the HTML's custom properties match the YAML values exactly; the md reads end-to-end in 4–6 minutes.

Then deliver both via `computer://` links:

> *"Your design system is captured in two mirrored files: **`docs/DESIGN.md`** — tokens + rationale for any coding agent to implement from (the source of truth) — and **`docs/DESIGN.html`** — open it in a browser to see every token and component rendered live. When tokens change, both update together."*

Recommended next step: run **`studio-design-prompt-generator`** (Step 3) — it embeds these tokens plus the identity's words into paste-ready prompts for AI design tools, so the first generated screens are on-brand.

## Image analysis patterns

Apply at Step 1.

### Colour extraction

- Dominant background → likely `surface` (or `neutral`). Dominant text → `on-surface`.
- The single non-neutral colour that draws the eye → the accent. If there are two strong accents, ask which is hero.
- Muted/secondary text → `on-surface-variant`. Multi-tone neutrals → `surface-container`, `surface-container-high`.
- Flag colours that may be rendering artifacts rather than intentional palette.

### Typography extraction

- Largest text → `display` or `headline-lg`. Body text → `body-md`. Small all-caps → `label-sm`.
- A serif in the reference is almost certainly for headlines, not body. Two distinct typefaces → the system is a pair.

### Spacing, elevation, shape extraction

- Smallest consistent gap → `xs`/`sm`; gap between unrelated blocks → `lg`/`xl`; button padding usually 12–16px vertical, 16–24px horizontal.
- Soft large shadows → shadow elevation; backdrop-blur → glass; stacked tints → tonal layering; 1px hairlines → border elevation; colour-contrast only → flat.
- 0–2px corners → architectural/brutalist; 4–8px → modern professional; 12–16px → consumer/friendly; 24px+ → playful; pills on small interactive elements → contemporary consumer.

## Calibration patterns

When the reference needs an anchor, draw on these recognized shapes:

- **Editorial Calm.** Warm neutrals + serif/sans pair + hairline borders + paper-on-paper. Fits calm-authority, editorial brands. (See `REFERENCE-DESIGN.md`.)
- **Atmospheric Glass.** Dark surface + vibrant gradient + backdrop-blur cards. Fits dramatic, transformative brands.
- **Dashboard Precision.** Cool neutrals + geometric sans + sharp 2–4px corners + flat tonal layering. Linear/Vercel-shape.
- **Notion-Adjacent Friendly.** Warm whites + humanist sans + medium rounding + soft hairlines. Warm tool-for-thinking brands.
- **Brutalist Editorial.** High-contrast monochrome + serif display + sharp corners + heavy weights. Defiant or authority-led brands.

## Editing the design system

`docs/DESIGN.md` is canonical; `docs/DESIGN.html` is its rendered mirror. **Any change to one is reflected in the other in the same edit.** Md first, then the matching CSS custom property / component in the html (or regenerate it). If the user hand-edits the html, fold the change back into the md tokens.

- **Change a single token** — update YAML + any prose referencing the old value + the CSS custom property and affected components in the html.
- **Reanalyze with a new image** — summarize what changed, ask replace-or-merge, regenerate the html from the result.
- **Rewrite a prose section** — update only that section; leave YAML and html untouched unless tokens change too.
- **Add a component** — YAML entry + Components prose paragraph + live rendering (with variants/states) in the html.

Preserve canonical section order and never create duplicate `##` headings.

## What "done" looks like

Two files, written together: a `docs/DESIGN.md` whose YAML matches the schema exactly, whose eight prose sections are tight and in order, whose fonts are free and off the banned list, whose component contrast pairs pass WCAG AA, and which coheres with the Product Identity's words — plus a `docs/DESIGN.html` that opens in a browser and renders every one of those tokens and components live, from the same values, in the same order. A founder can look at the html and *see* their brand; an agent can read the md and *build* it.
