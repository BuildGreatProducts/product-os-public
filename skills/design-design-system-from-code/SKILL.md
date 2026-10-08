---
name: design-design-system-from-code
description: >-
  Reverse-engineers the design system already in a codebase — colors, type, spacing, radii,
  elevation, and components from CSS variables, Tailwind config, theme files, and components —
  resolves competing values with the user, and writes Google-format docs/DESIGN.md plus its
  docs/DESIGN.html style guide. Use when the app exists but has no DESIGN.md: "design system from
  code", "reverse-engineer my design system", "consolidate my design tokens". Not for deriving a
  system from an image or site — use design-design-system; not for reviewing changes — use
  develop-design-review.
---

# Design: Design System from Code (DESIGN.md)

The **reverse** of `design-design-system`: instead of Product Identity + a reference image → a new system, read the design system that already lives — implicitly and inconsistently — inside an existing codebase, and write it down as a single Google-format `docs/DESIGN.md` with the same `docs/DESIGN.html` mirror. Every shipping codebase has three blues that all mean "primary", button padding forked between components, cards rounded at 8, 12, and 14px, and a `--color-text` variable half the code ignores. The job: **find the de-facto system, surface every internal conflict, let the member pick the canonical value for each role, and document the result.**

The cardinal rule is **document reality, don't silently improve it.** Capture the real fonts, palette, and spacing scale. Don't invent an aesthetic, substitute "better" fonts, or quietly fix contrast. The only things you actively resolve are *internal inconsistency* and fonts on ProductOS's exclusion list — and only with the member. Quality issues (a pair failing WCAG AA, a non-free font, a sprawling type scale) are **advisory notes** delivered outside the file. A `DESIGN.md` that lies about the codebase is worse than none. No external research is needed — everything lives in the code.

## Inputs

Run in the app repo root — the repository that contains `productos/` (also works standalone in any codebase without ProductOS).

1. **The product codebase** — **required.** Identify the framework and styling approach first (step 2). If the repo has no UI code (pure backend, CLI, data pipeline), stop and say there's no design system to extract.
2. **The format** — **required**, embedded in "Output format" below so this skill works standalone. If `productos/skills/design-design-system/REFERENCE-DESIGN.md` exists, use it as the format exemplar. If `docs/DESIGN.md` already has tokens, read it first, treat its structure as the format reference, and run the session as a reconciliation. If it holds only a `## Product Identity` section (no token groups — written by `design-identity-creator`), it's still a from-scratch extraction; keep that section.
3. **The Product Identity** — the `## Product Identity` section of `docs/DESIGN.md` — **optional, tiebreaker only.** Its tone and named visual references break ties only when code evidence is genuinely ambiguous; they never override what the code does. If absent, resolve on code evidence alone.
4. **`docs/DEFINE.md`** — **optional, context only.** Its Summary, Offer → Customer and Persona help name the aesthetic in `Brand & Style` and show which surfaces matter most.

## Voice

A senior design systems engineer doing a brownfield audit:

- **Evidence-led.** "`#2563EB` appears in 34 places, `#2D6CDF` in 6, and `#3B82F6` in 2 — all used as the primary action color. I'm proposing `#2563EB` as canonical `primary`. Confirm or pick another."
- **Descriptive, not prescriptive.** Document the system; resist "improving" the palette or swapping fonts. The one exception is an excluded font (step 4).
- **Token-fluent and conflict-precise.** "Spacing clusters on a 4px base — `4 / 8 / 16 / 24 / 32 / 64` — except `13px`, `18px`, `25px`, which appear once or twice each. Snap them to the nearest step?" Never "there are some inconsistencies."
- **Honest about gaps.** If a category has no discernible system (elevation as a free-for-all of ad-hoc shadows), say so and propose the smallest defensible system — flagged as a proposal, not a discovery.

## Output format (Google DESIGN.md spec — embedded)

Two parts: YAML frontmatter (machine-readable tokens) and a Markdown body (eight sections, fixed order) — Google's open format ([github.com/google-labs-code/design.md](https://github.com/google-labs-code/design.md)), the same one `design-design-system` produces. In ProductOS the body may open with a `## Product Identity` section (from `design-identity-creator`); if present, it sits before the eight sections and is preserved verbatim — the spec preserves unknown sections. This is normative — don't improvise the schema, section set, or order.

**YAML frontmatter:**

```yaml
---
version: alpha
name: <Design System Name>
description: <one-sentence description>
colors:
  <token-name>: "<#hex>"
typography:
  <token-name>:
    fontFamily: <font name as used in the code>
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
    backgroundColor: "<hex or {colors.token-reference}>"
    textColor: "<hex or {colors.token-reference}>"
    typography: "{typography.token-reference}"
    rounded: "{rounded.token-reference}"
    padding: <dimension>
    height: <dimension>
---
```

**Token naming conventions** (map the code's de-facto values onto these names):

- Colors: `primary`, `secondary`, `tertiary`, `neutral`, `surface`, `surface-container`, `surface-container-high`, `on-surface`, `on-surface-variant`, `outline`, `outline-variant`, `error`, `on-error`. Add roles only when the code genuinely uses them (e.g., `success`, `warning`).
- Typography: `display-lg`, `headline-lg`, `headline-md`, `body-lg`, `body-md`, `body-sm`, `label-md`, `label-sm`. Aim for 6–10 levels; never exceed 15. If the code has 24 font sizes, that *is* the conflict — collapse them to a documented scale with the member.
- Rounded: `none`, `sm`, `md`, `lg`, `xl`, `full`.
- Spacing: `xs`, `sm`, `md`, `lg`, `xl`, plus named tokens like `gutter` and `margin` where the layout uses them repeatedly.

**Token-reference syntax:** components reference tokens with `"{colors.primary}"`, `"{typography.body-md}"`, `"{rounded.md}"` — braces, dot-path, exact token name, always in double quotes (unquoted, YAML reads `{…}` as a map).

**Markdown body — the eight canonical sections, in this order** (after the Product Identity section, if present), each **3–8 tight sentences** (bullets for per-role values don't count against it):

1. `## Brand & Style` — the aesthetic the code adds up to ("utilitarian dashboard," "consumer-playful," "editorial-minimal"), derived from the code and contextualized by `docs/DEFINE.md` if present.
2. `## Colors` — palette strategy, then a bullet per color role with hex and where it's used. Note any colors you consolidated.
3. `## Typography` — the type system (single family / pair / sprawl-collapsed-to-scale), then a bullet per level. Document the **real** font families as used in the code — except an excluded family, which is replaced by the substitute the member picked in step 5.
4. `## Layout & Spacing` — the base unit and scale, container widths, and grid/layout model as found in the code.
5. `## Elevation & Depth` — the depth model actually in use (shadows / borders / glass / tonal / flat), or the model you proposed to consolidate an ad-hoc one.
6. `## Shapes` — the corner-radius philosophy and how radius varies by component type.
7. `## Components` — style guidance per documented component (buttons, inputs, cards, list items, chips, plus product-specific ones). Every component here has a YAML entry and vice versa.
8. `## Do's and Don'ts` — 4–8 guardrails, biased toward this session's consolidation decisions ("Do use `{colors.primary}` (`#2563EB`) for primary actions — not the legacy `#3B82F6`").

## Workflow

### 1. Read context and set expectations

If `docs/DESIGN.md` exists, read it — this is a reconciliation (extend/correct) rather than a from-scratch write; tell the member. Read the Product Identity section and/or `docs/DEFINE.md` if present for tiebreaker and naming context. State the plan in one line: *"I'll scan the codebase, inventory the design tokens you're actually using, flag every internal inconsistency, we'll pick the canonical value for each together, then I'll write `docs/DESIGN.md` in the Google format. Starting the scan."*

### 2. Map the styling architecture

Before extracting any value, find *where* design decisions live — don't grep for hex until you know whether the source of truth is a Tailwind config, a theme file, or nothing. Use the checklist in [references/extraction-playbook.md](references/extraction-playbook.md) → Styling architectures (Tailwind, CSS custom properties, CSS-in-JS, token files, component-library themes, native, raw/scattered). State it back: *"Styling architecture: Tailwind config with a partial token theme, plus ~40 arbitrary-value escapes and a handful of inline hex in page components. Primary token source is `tailwind.config.ts`; the conflicts are mostly in the escapes. Scanning those now."*

In a **monorepo or multi-app** repository, ask which app/package to document before scanning — never blend two products' systems into one file.

### 3. Extract the de-facto token inventory

Sweep the code and collect every value actually used, grouped by category. **Count occurrences and note locations** — they're how conflicts get resolved. Capture reality fully, including the mess; don't clean up yet.

- **Colors:** every hex, `rgb()/rgba()`, `hsl()/hsla()`, named CSS color, Tailwind color (config + arbitrary), CSS variable value, and native color literal. Group by apparent role (background / text / border / accent / status).
- **Typography:** every `font-family`, `font-size`, `font-weight`, `line-height`, `letter-spacing`; Tailwind text/font classes; `@font-face`; native font calls. Note which families are actually loaded.
- **Spacing:** every `margin` / `padding` / `gap` / inset value and Tailwind spacing class. Detect the base unit (usually 4 or 8) and which values are on- vs off-grid.
- **Radius:** every `border-radius` value and radius class, grouped by the component type it's applied to.
- **Elevation:** every `box-shadow`, `drop-shadow`, `backdrop-filter`, and hairline-`border`-as-elevation. Note whether one model dominates or several coexist.
- **Components:** every recurring UI primitive (button, input, card, list item, chip, badge, modal) and its concrete style values — including duplicate/forked implementations.

### 4. Detect internal inconsistencies (the core of this skill)

Cluster the inventory into **conflicts** — competing values for what should be one role. Read [references/extraction-playbook.md](references/extraction-playbook.md) → Inconsistency patterns for how to detect each type: near-duplicate colors, token defined but bypassed, off-grid spacing, multiple radii per component type, mixed units, font sprawl, competing elevation models, forked components, dead tokens.

**Excluded fonts are always a conflict.** ProductOS avoids Inter, Instrument Serif, Outfit, and Plus Jakarta Sans. If the code uses one, add a typography conflict recommending the closest free substitute (Inter → Public Sans or Manrope; the full substitution list is in `design-design-system`'s font rule) and document the family the member picks. The excluded family left in the code becomes drift for `develop-design-review` to flag.

Build a **conflict list**: each entry is one role with its competing values, the occurrence count and representative locations for each, and your recommended canonical pick with the reason. De-duplicate (the same stray hex in 12 files is one conflict with 12 locations) and cluster forked components into one entry.

Summarize before resolving: *"Inventory done. Clean on radius and base spacing. [N] conflicts to resolve: 3 primary blues, 2 body-text greys, button padding forked 3 ways, 4 off-grid spacing values, and two Button components. Want to walk through them now?"*

### 5. Walk through the conflicts, one at a time

Present each conflict the same way and get a decision before moving on:

> **Role: `primary` (primary action color)** — 3 competing values:
> - `#2563EB` — 34 uses (Button, Link, theme config) ← **recommend canonical**
> - `#2D6CDF` — 6 uses (older marketing pages)
> - `#3B82F6` — 2 uses (one CTA, one icon)
> Recommend `#2563EB`: most-used, and it's the one defined in `tailwind.config.ts`. Keep it? (or pick another / I can show the swatches)

Form each recommendation with the **Resolution heuristics** in the playbook (frequency → source authority → location weight → identity tiebreaker → accessibility tiebreaker → recency), but the member decides — never resolve silently. Capture each decision tersely. Values the member didn't pick that remain in the code are now *drift* — documented as the wrong value, for `develop-design-review` to catch later. One conflict, one recommendation, one confirm, next.

Don't turn quality issues into conflicts. If `primary` on `surface` fails WCAG AA, that's an advisory for step 8, not a conflict.

### 6. Assemble the DESIGN.md

Map the canonical values onto the format above:

- **YAML frontmatter** — canonical colors under the standard role names, the consolidated type scale, spacing scale, radius scale, and a `components` entry for each documented primitive using `{token}` references.
- **`## Product Identity`** — kept verbatim right after the frontmatter and title if the existing file has one; never rewrite or drop it.
- **The eight sections** in order after it. Document the **real** fonts and values. In `Colors`, `Typography`, and `Do's and Don'ts`, briefly record the consolidation decisions ("consolidated three primary blues to `#2563EB`") so the file explains what the code should refactor toward.
- A `name` that describes what the code adds up to (use DEFINE.md / the Product Identity for flavour if present, else descriptive — "Acme Dashboard System").

### 7. Show the member and iterate

Two passes: **YAML frontmatter first** (confirm the canonical tokens and consolidated scales), then the **markdown body** (confirm tone and per-component prose). Fold in corrections; iterate once or twice. Don't dump the whole file at once.

### 8. Write `docs/DESIGN.md` and `docs/DESIGN.html`, then flag advisories

Write the approved file to `docs/DESIGN.md` (`mkdir -p docs` if needed). If it already exists, show the diff and overwrite only on the member's approval — carrying its `## Product Identity` section over untouched.

Then build the **`docs/DESIGN.html` mirror** from the approved markdown — the same twin `design-design-system` builds:

- **Self-contained and dependency-free.** One file: all CSS inline in a `<style>` block, no frameworks, no external JS. Web fonts may load via a Google Fonts `<link>` when a documented family needs it; otherwise fall back to the stack the code uses.
- **Token-driven.** Declare every YAML token as a CSS custom property in `:root` (`--color-primary`, `--type-body-md-size`, `--rounded-md`, `--space-md`) and style every swatch, specimen, and component from those variables — values must match the YAML exactly.
- **Sections, in order:** Header (name, description, "human-readable mirror of `docs/DESIGN.md`") → **Product Identity** (if the md has one) → Colors → Typography → Spacing → Radius → Elevation → Components (every YAML component rendered live, variants and states grouped) → Do's and Don'ts. Neutral style-guide chrome, not a marketing page.
- **Keep the Product Identity.** If the html already has that section, carry it over with content unchanged (restyling with the tokens is fine); otherwise render it from the md. Never drop it.
- **Never overwrite silently.** If `docs/DESIGN.html` exists, say what will change (new token sections, regenerated components, identity kept) and write only on approval.

Then, **separately from the file**, give the member the advisory notes you deliberately kept out of it:

- **Contrast:** every documented `backgroundColor` + `textColor` pair that fails WCAG AA (4.5:1 body, 3:1 large) — state the ratio, propose a fix, let the member decide whether to adjust the token or accept it.
- **Non-free fonts:** a documented family that isn't free for commercial use — note it, but **keep the real font in the file** unless the member explicitly asks to substitute. (Excluded fonts aren't advisories; they were resolved as conflicts in step 5.)
- **Residual sprawl:** anything collapsed aggressively (24 sizes → 8 levels) so the member knows what got rounded.

## Verify before delivering

Re-read both files:

- [ ] YAML parses — consistent indentation, hex and every `{…}` reference quoted, no trailing colons — with `version`, `name`, `description`, and populated `colors`, `typography`, `rounded`, `spacing`, `components`.
- [ ] The Product Identity section, if there was one, is intact right after the frontmatter — and right after the Header in `docs/DESIGN.html`.
- [ ] All eight sections are present, in order, each 3–8 tight sentences, with consolidation decisions recorded.
- [ ] Every YAML component has prose in `Components`, and vice versa; token references use exact `{colors.primary}` / `{typography.body-md}` / `{rounded.md}` syntax.
- [ ] Every canonical decision from step 5 is reflected — one value per role, the one the member picked.
- [ ] The file describes the code, not an idealized version — real fonts and values; advisories noted separately, not silently applied.
- [ ] No family on the exclusion list (Inter, Instrument Serif, Outfit, Plus Jakarta Sans) appears in the typography tokens.
- [ ] Contrast was computed for every documented component pair and reported (not necessarily fixed).
- [ ] The HTML mirrors the md — every custom property matches its YAML value, every YAML component renders, sections follow the md's order — and an existing html was overwritten only with approval.
- [ ] The md reads end to end in 4–6 minutes.

Give the member both file paths and a tight summary: one line per token group (colors, typography, spacing, shapes, components), one line on conflicts resolved ("9 conflicts consolidated"), and the advisory notes.

**Next:** run `develop-design-review` in this repo — it finds every place the code still uses non-canonical values and produces a paste-ready fix prompt to consolidate onto the documented tokens; `develop-design-better` then keeps new UI on-system.
