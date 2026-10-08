---
name: design-design-system
description: >-
  Derives a design system from an image reference — screenshot, mockup, Figma frame, or live site
  the user admires — reconciles it with the Product Identity, and writes Google-format
  docs/DESIGN.md (YAML tokens plus prose) and a live docs/DESIGN.html style guide; Lite mode writes
  brand tokens only for screenless shapes. Design phase Step 3. Use when the user says "build my
  design system", "create my DESIGN.md", or shares an image whose look they want. Not for tokens
  from existing code — use design-design-system-from-code; not for reviewing UI changes — use
  develop-design-review.
---

# Design: Design System (image → DESIGN.md + DESIGN.html)

Translate an **image reference the member loves** — a screenshot, mockup, Figma file, or live website — into a design system captured as **two mirrored files**:

- **`docs/DESIGN.md`** — YAML tokens in [Google's open design.md format](https://github.com/google-labs-code/design.md) plus prose rationale. The **source of truth** coding agents build from.
- **`docs/DESIGN.html`** — a self-contained style guide that renders every token and component live in a browser, styled from the same token values. The **mirror** the human opens.

They are always written and updated together so they never drift.

This is **Design phase Step 3**. The identity already lives in `docs/DESIGN.md` as its `## Product Identity` section (Step 1 created the file); this skill adds the tokens and the eight design-system sections around it. The identity supplies the *words* and deliberately leaves the *visuals* undecided — this skill derives colours, fonts, spacing, shapes, and components from a real image, guided by those words. The member supplies the image; you do the analysis, extraction, reconciliation, and both writes. Already have a codebase instead of an image? Use `design-design-system-from-code`.

## Modes

- **No image provided yet:** ask for one (Step 0) before doing anything else. Don't draft from imagination. If the member has no image after one prompt, offer the weak fallback: *"I can draft a starter system from your Product Identity's words alone and we'll refine it — but it will be far weaker than working from an image you love. Want to proceed that way, or grab a reference first?"*
- **`docs/DESIGN.md` holds only the Product Identity** (frontmatter with no token groups — the usual state after Step 1): a first run. Build the system around the identity; no overwrite question beyond the diff in Step 6.
- **`docs/DESIGN.md` already has tokens:** read it (and `docs/DESIGN.html`) and ask what the member wants — refine specific tokens, replace with a fresh analysis from new imagery, or merge. Confirm before destructive overwrites, and regenerate `docs/DESIGN.html` whatever changes.
- **Partial conversation:** if the session was interrupted mid-flow, resume from where it left off. Don't restart.
- **Lite:** the shape's Design route marks Step 3 **Lite** (typical for shapes without screens of their own — skills, MCP servers, services, digital products), or the member asks for brand tokens only. Run [Lite mode](#lite-mode-brand-tokens-only) instead of the full token set.

### Lite mode (brand tokens only)

A Lite system serves the surfaces a screenless product still has: its listing, landing page, docs, README, social images, and deliverables. Same two files, same Google format, same image-first intake (the identity-words fallback is more acceptable here) — less of it:

- **Tokens:** `colors` limited to `primary`, `on-primary`, `surface`, `on-surface`, `on-surface-variant`, `outline`, and at most one accent (add `error`/`success` only if docs or output show states); 4–6 `typography` levels (`display-lg`, `headline-md`, `body-md`, `label-md`, plus `code-md` in a mono family for developer-facing shapes); `rounded` and `spacing` of 3–4 steps each.
- **Components:** only what listings, landing, and docs visuals need — `button-primary`, `link`, `card`, `badge`, and `code-block` (agent and developer shapes) or `screenshot-frame` (when listings show a host app, chat, or terminal). Five or six entries, variants included.
- **Logo use:** a `### Logo use` subsection inside `## Brand & Style` — the mark's light and dark variants, clear space, minimum size, the square avatar/icon crop listings require, and two don'ts. No logo yet → say so, record the wordmark rule (name set in `display-lg`), and point to `../../design/logo-references/BONUS-Logo-Types-and-Best-Practice.md` → **Monochrome and Variant Rules**.
- **Prose:** all eight sections stay, in order (the format requires them); Layout & Spacing, Elevation & Depth, and Shapes may be one or two sentences each.
- **Marked Lite:** the YAML `description` ends "(Lite — brand tokens for listings, landing pages, and docs)", an italic line under the title reads *Lite design system — run the full Design Step 3 before building any product screens*, and DESIGN.html's Header carries the same note.

Steps 0–7 below run as written, scoped to this set; Step 2 asks only questions 1, 2, and 7. If the product later gains screens, re-run in full and extend — never discard — the Lite tokens.

## Inputs

Read inputs from `docs/` at the app repo root.

1. **An image reference (or several).** **Required — the primary anchor.** Accepted forms:
   - **Local image paths** (PNG / JPG / WebP / screenshots) — read with the Read tool, which renders images visually.
   - **Figma URLs** (`figma.com/design/...`, `/board/...`, `/make/...`) — if the Figma MCP server is connected, use it (`get_design_context`, `get_screenshot`, `get_metadata`); otherwise ask for a screenshot of the frame.
   - **Live website URLs** — if a browser/screenshot tool is connected, use it to capture the page; otherwise ask the member to paste a screenshot. Use WebFetch on the URL only as a supplementary signal (font names, colour values in CSS) — never as the primary visual source.
   - **A mix.** Ask which is the **primary anchor** and which are mood references — the primary drives the token decisions.
2. **The Product Identity** — the `## Product Identity` section of `docs/DESIGN.md`. **Required.** If it's missing or substantively empty, stop and point to `design-identity-creator` first.
3. **`docs/DEFINE.md`** — **required.** What the product is (Summary, Offer → Mechanism) and who uses it in what context (Offer → Customer plus the Persona) — a productivity tool's system differs structurally from a consumer app's even with the same brand character. If it's missing, stop and point to the Define skills (or `define-from-code`).
4. **Product shape** — `docs/DEFINE.md` → `## Product Shape` → `### Primary Shape` names the slug; read only the Design route row for Step 3 in `productos/shapes/<slug>.md` (from this folder, `../../shapes/<slug>.md`). **Full** → the standard run; **Lite** → Lite mode; **Adapted** → the standard run scoped to the surfaces the row names (a browser extension's popup, side panel, options page, and injected UI). The row's note wins where it says when to go Full (a skill that outputs visual documents, a visual template, an embedded chat widget). No Product Shape section (a repo from before 2.0) → treat it as `web-app` unless the code or member clearly says otherwise, and suggest `define-product-shape`. If `docs/PLAN.md` schedules the step differently, the plan wins — say so.
5. **[REFERENCE-DESIGN.md](REFERENCE-DESIGN.md)** in this skill's folder. Read once at the start for the exact format, YAML schema, section order, and `{path.to.token}` conventions. Structural template only — **never copy its design choices.**

## Voice

A senior design director and systems engineer with strong taste. **Observant** — describe what you actually see, not what you assume. **Decisive** — when the member is uncertain, recommend a direction with a one-line rationale. **Token-fluent** — every recommendation lands as a token: not "a soft red," but `error: "#B23A2E"`. **Strict to the spec** — section order, YAML schema, and token-reference syntax are fixed. Don't flatter weak references: if the imagery is conflicting or thin, say so and ask which direction to anchor on.

## Workflow

### 0. Image intake

Read the identity and DEFINE.md first, then open with:

> *"Share the image (or images) you want me to translate — a screenshot of a product you love, a marketing site capture, a Figma link, or a mix. If you have several, tell me which is the primary anchor. Your identity's Visual Style references are a good place to hunt."*

### 1. Image analysis

Read every image carefully before asking anything, using [references/image-analysis-patterns.md](references/image-analysis-patterns.md) to map what you see onto token roles. Extract per image:

- **Colours** — approximate hexes for backgrounds, surfaces, primary/secondary text, accents, borders, semantic states. Dominant vs accent. Light or dark mode.
- **Typography** — typeface character (geometric sans / humanist sans / serif / slab / display / mono), hierarchy levels, approximate sizes and weights, letter-spacing tendencies, uppercase usage.
- **Spacing & density** — tight, comfortable, or generous; visible scale (4/8/16/24/32).
- **Shapes** — corner-radius philosophy, and whether it varies by component class.
- **Elevation** — soft shadows, hard shadows, hairline borders, glass/blur, tonal layering, or flat.
- **Components** — visible atoms (buttons, inputs, chips, cards, nav, tables, modals, toasts), variants, states.
- **Mood** — two or three concrete adjectives.

Summarize back in 5–8 tight bullets, mirroring the imagery's actual character. If two references conflict, name the conflict.

### 2. Context questions — only the ones ProductOS hasn't answered

Ask one at a time, offering 3 tailored suggestions drawn from the analysis. **Skip everything the docs already answer** (product, audience, and context from DEFINE.md; tone, worldview, belief, and imagery lane from the identity) — acknowledge what's known instead of re-asking. What's left:

1. **Colour role assignments** — which spotted colour is `primary`, which is the accent, which carry semantic meaning? Light, dark, or both? Suggest a mapping.
2. **Typography confirmation** — the typeface direction and the scale levels the product needs (free-fonts rule in Step 4 applies).
3. **Spacing density** — tight / comfortable / generous; suggest from what you observed.
4. **Shape language** — sharp / soft / fully rounded / mixed, and what that signals.
5. **Elevation philosophy** — shadows / borders / glass / flat; recommend from the image and the identity's visual style.
6. **Component priorities** — which components matter for the MVP; cap at 6–10 (variants/states count).
7. **Anti-patterns** — three things this design must never become; these feed the Don'ts.

If an answer is vague, push back with a recommendation rather than another open question.

### 3. Reconcile the image with the Product Identity

The identity is the strategic anchor; the image is the aesthetic anchor. On conflict: **identity wins on strategy** (worldview, belief, tone, visual lane), **image wins on tactics** (hexes, radii, component rhythm) — unless the image violates a documented Visual Style rule. Common conflicts:

- **Image is dark mode, identity is calm/editorial** → propose dual-mode (light primary, dark variant) or treat the image as moodboard-not-blueprint.
- **Image uses a banned or paid font** → substitute a free equivalent (Step 4) and surface it.
- **Image has heavy shadows, identity tone is "calm + precise"** → hairline borders + tonal layering.
- **Image palette is over-saturated for the brand's tone** → de-saturate extracted hexes 10–20%.

Surface every conflict, propose the resolution, get a one-sentence confirm, move on. Silent reconciliation is how design systems drift.

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
- Every component's `backgroundColor`+`textColor` pair meets WCAG AA (4.5:1 body, 3:1 large).
- No duplicate `##` headings in the prose (the spec rejects them).

**Fonts must be free for commercial use** (Google Fonts, Fontshare, Vercel's Geist) and **never** the vibe-coded defaults: **Inter, Instrument Serif, Outfit, Plus Jakarta Sans**. If the image clearly uses a banned or paid font, substitute the closest free equivalent and surface it. Common substitutions: Söhne → Public Sans or Hanken Grotesk; GT America → Schibsted Grotesk; Tiempos → Newsreader; Inter → Public Sans or Manrope; Suisse Int'l → Public Sans; Helvetica Now → Public Sans. Distinctive free picks: Fraunces, Newsreader, Bricolage Grotesque, Source Serif 4, Schibsted Grotesk, Public Sans, Manrope, Hanken Grotesk, Cormorant Garamond, DM Serif Display, Spectral, Albert Sans, Onest, Funnel Sans/Display, JetBrains Mono, DM Mono, Geist/Geist Mono, Satoshi, General Sans, Switzer.

### 5. Prose drafting

Draft the eight canonical sections, in this exact order after the Product Identity section, each 3–8 tight sentences. Don't restate the YAML — explain the *why*, so a coding agent can make sound choices where the tokens are silent:

1. **`## Brand & Style`** — the look-and-feel north star, from DEFINE.md (what it is) + the identity (worldview, belief, tone, visual style). The aesthetic intent in one phrase, the emotional response the UI should evoke, and one or two anti-patterns.
2. **`## Colors`** — palette strategy: what `primary`, accent, `surface`, and semantic colours do and why those values. Note WCAG AA contrast intent.
3. **`## Typography`** — the pairing's character and what each scale level is for. Treatment rules (uppercase labels, tabular numerals).
4. **`## Layout & Spacing`** — grid model, max content widths, density philosophy, how spacing tokens map to layout.
5. **`## Elevation & Depth`** — the depth model and why it fits this brand.
6. **`## Shapes`** — corner-radius philosophy; intentional differences by component class.
7. **`## Components`** — how buttons, inputs, chips, cards behave; variant and state rules. Every YAML component explained here, and vice versa.
8. **`## Do's and Don'ts`** — 4–6 do's and 4–6 don'ts, specific and enforceable, from the anti-patterns answer and the identity.

### 6. Confirm and write `docs/DESIGN.md`

Show the member a brief outline first — the token names chosen (colour tokens, type levels, rounded/spacing scales, component list) and a one-line summary per prose section. Fold in last edits. Then write `docs/DESIGN.md` (create `docs/` if needed; if the file exists, show the diff and get approval). File order: the YAML frontmatter, the `# <Name>` title, the **`## Product Identity` section carried over verbatim** (it belongs to `design-identity-creator` — never rewrite or drop it), then the eight canonical sections. Drop the italic placeholder line saying tokens arrive at Step 3.

Verify the write succeeded before confirming. On failure, surface a clear message by cause: permission denied ("the directory isn't writable — check folder permissions"), disk full ("free up space and I'll retry"), existing-file conflict ("want me to save under a different name or overwrite?"), anything else (report verbatim and ask). Only say "saved" after verification — then build the mirror.

### 7. Build the `docs/DESIGN.html` mirror

Generate it **from the tokens just written**, not from a fresh interpretation of the imagery:

- **Self-contained and dependency-free.** One file that opens in any browser: all CSS inline in a `<style>` block, no frameworks, no external JS. Web fonts may load via a Google Fonts `<link>`.
- **Token-driven.** Declare every YAML token as a CSS custom property in `:root` (`--color-primary`, `--type-headline-lg-size`, `--rounded-md`, `--space-md`); every swatch, specimen, and component styles itself from those variables — never hardcode a value that exists as a token.
- **Mirrors the md's section order**, so the two files read side by side.
- If the system defines **both light and dark modes**, include a small vanilla-JS theme toggle flipping a `data-theme` attribute and define both token sets.

Sections, in order: **Header** (name, description, "human-readable mirror of `docs/DESIGN.md`") → **Product Identity** (carried over from the existing html — the Brand Card as a card plus the five elements, restyled with the new tokens if you like but content unchanged; rebuild it from the md section if the html is missing) → **Colors** (a swatch per token: block, name, hex, and a line of text in the paired `on-` colour) → **Typography** (each level as a live specimen at its real family/size/weight, spec beside it) → **Spacing** (labeled bars) → **Radius** (sample boxes per `rounded` value) → **Elevation** (a card per level) → **Components** (every `components:` entry rendered live, variants and states grouped; un-triggerable states like hover as labeled static copies) → **Do's and Don'ts** (two columns, ✓/✗, small visual examples where they help).

Keep the page's chrome neutral — a reference style guide, not a marketing page. Write `docs/DESIGN.html` with the same write-error handling.

## Editing the design system later

`docs/DESIGN.md` is canonical; `docs/DESIGN.html` is its mirror. **Any change to one is reflected in the other in the same edit** — md first, then the matching CSS custom property / component in the html (or regenerate it). If the member hand-edits the html, fold the change back into the md tokens.

- **Change a single token** — update YAML + any prose referencing the old value + the CSS custom property and affected components in the html.
- **Reanalyze with a new image** — summarize what changed, ask replace-or-merge, regenerate the html from the result.
- **Rewrite a prose section** — update only that section; leave YAML and html untouched unless tokens change too.
- **Add a component** — YAML entry + Components prose paragraph + live rendering (with variants/states) in the html.

Preserve section order — Product Identity first, then the eight — and never create duplicate `##` headings. Identity changes go through `design-identity-creator`, which rewrites that section in both files.

## Verify before delivering

Re-read both files:

- [ ] YAML parses (consistent indentation, quoted hexes) and matches the schema exactly.
- [ ] The Product Identity section is intact right after the frontmatter and title (md) and the Header (html).
- [ ] All eight canonical sections are present, in order, after it — each 3–8 tight sentences, no duplicate `##` headings.
- [ ] Every YAML component is explained in prose, and vice versa; token references use exact `{colors.primary}` syntax.
- [ ] All fonts are free for commercial use and off the banned list; substitutions were surfaced.
- [ ] Every component's `backgroundColor`+`textColor` pair meets WCAG AA (4.5:1 body, 3:1 large) — flag and fix failures before delivering.
- [ ] Every image-vs-identity conflict was surfaced and confirmed, and the system coheres with the identity's words.
- [ ] The HTML's custom properties match the YAML values exactly and it renders every token and component live, in the md's section order.
- [ ] Both files were written in the same pass; the md reads end to end in 4–6 minutes.
- [ ] Lite mode only: the token and component sets stay within the Lite limits, `### Logo use` is filled, and both files are marked Lite.

Give the member both file paths: `docs/DESIGN.md` is the source of truth any coding agent implements from; `docs/DESIGN.html` opens in a browser to show every token and component live; when tokens change, both update together.

**Next:** `design-prompt-generator` (Step 4) embeds these tokens plus the identity's words into paste-ready prompts for AI design tools. After a Lite run, follow the shape's route: Step 4 runs for listing and landing visuals only, or is skipped.
