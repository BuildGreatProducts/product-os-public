# Prompt templates

The two prompt shapes composed at Step 4. Fill every `[bracketed]` slot with real content from `docs/DEFINE.md`, `docs/DESIGN.md`, and `docs/COPY.md` — the finished prompts contain no brackets.

## Contents

- [Prompt 1 — Design system foundation](#prompt-1--design-system-foundation)
- [Prompts 2 and 3 — Priority screens](#prompts-2-and-3--priority-screens)

## Prompt 1 — Design system foundation

Asks the AI design tool to render the component library **from the tokens already locked in `docs/DESIGN.md`** — it renders the system, it does not invent one. Paste the actual YAML values into the Foundations slots (token names exactly as DESIGN.md has them: `primary`, `on-surface`, `display-lg`, `headline-lg`, `body-md`, `label-md`, …). Only motion and icon style, which DESIGN.md doesn't tokenize, are left for the tool to choose — anchored in the tone.

```
Design a complete UI design system foundation for [product description in one sentence].

Brand identity:
[paste the brand context block from step 3]

Use these design tokens exactly — do not invent new colors, sizes, or radii:

Colors (token: hex)
[every entry under DESIGN.md `colors:`, one per line — e.g. "primary: #1A1A1A", "surface: #FFFFFF", "on-surface: #1A1A1A", "error: #B23A2E"]

Typography (level: family / size / weight / line-height / letter-spacing)
[every entry under DESIGN.md `typography:`, one per line — e.g. "display-lg: Newsreader / 56px / 500 / 1.1 / -0.02em", "body-md: Public Sans / 16px / 400 / 1.5"]

Spacing
[every entry under DESIGN.md `spacing:` — e.g. "xs 4px, sm 8px, md 16px, lg 24px, xl 48px, gutter 24px"]

Corner radius
[every entry under DESIGN.md `rounded:` — e.g. "none 0, sm 4px, md 8px, lg 12px, full 9999px"]

Elevation
[the depth model from DESIGN.md's Elevation & Depth section in one line — e.g. "hairline borders (outline-variant) and tonal layering; no drop shadows"]

Components already defined (render these first, with exactly these token values)
[every entry under DESIGN.md `components:` — e.g. "button-primary: background primary, text on-primary, typography label-md, radius md, padding 12px 20px, height 44px"; "button-primary-hover: background …"]

What to design:
Render the tokens above as a foundations sheet (color swatches with token names and hexes, a live specimen of every typography level, spacing and radius scales, elevation levels). Then build the full component library from those tokens only, organised by category. Extend the defined components to the rest of the set in the same style:

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
- Icons: line vs filled, stroke weight, corner style — choose one consistent with the tone and visual style. Show ~10 representative icons.
- Empty states, loading states (skeletons), error states.
- Progress indicators: bar, circular, stepper.
- Motion: one standard easing curve and duration (e.g., 200ms), entrance vs interaction — consistent with the tone.

Layout
- Grid: [column count, gutter, max content width from DESIGN.md's Layout & Spacing section]
- [Responsive breakpoints (mobile, tablet, desktop) if the product is web/desktop; mobile sizing if mobile-first]

Button and label text follows: [COPY.md's button/label rules and 4–6 canonical nouns/verbs from its lexicon, if COPY.md exists]

Visual notes:
- [specific compositional rule from Visual Style — e.g., "generous negative space, type-led hierarchy, hairline borders instead of shadows"]
- Maintain WCAG AA contrast for all text-on-color pairings; never rely on color alone to convey state.
- [overall feel anchored in the tone of voice — e.g., "Calm, precise, considered — every component reads as quietly competent, never showy"]

Present the design system as a tidy sticker sheet or single canvas, grouped by category, with clear section headings.

Use tokens from docs/DESIGN.md where applicable for exact colors, type, spacing, and component styling.
```

## Prompts 2 and 3 — Priority screens

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
- CTAs and buttons: "[exact text — in-product buttons verb-first {Verb} {noun}, 1-3 words, per docs/COPY.md when present; conversion CTAs 3-5 words, first-person where applicable]"
- Other key labels: "[as needed]"

Visual notes:
- [device frame: mobile / tablet / desktop / responsive]
- [specific compositional rule from Visual Style — e.g., "generous negative space, type-led hierarchy"]
- [accessibility note — e.g., "maintain WCAG AA contrast for body text"]
- Reuse the components from the design system prompt (Prompt 1) — same buttons, same form elements, same cards.

What this screen should feel like:
- [one sentence anchored in the tone of voice — e.g., "Calm and considered — the user should feel the AI is doing thoughtful work on their behalf, not racing them"]

Use tokens from docs/DESIGN.md where applicable for exact colors, type, spacing, and component styling.
```

The "Reuse the components from the design system prompt (Prompt 1)" line is load-bearing: it tells the tool to pull from the just-generated system rather than inventing new component styles.
