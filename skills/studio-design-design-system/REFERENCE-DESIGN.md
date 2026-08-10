---
version: alpha
name: Editorial Calm
description: A light-mode, editorial-feeling design system anchored in warm neutrals, generous whitespace, and a refined serif/sans pairing. Reference example for the ProductOS Design System skill — illustrates the canonical Google DESIGN.md format with all eight markdown sections populated.
colors:
  primary: "#1A1A1A"
  secondary: "#6B6660"
  tertiary: "#B23A2E"
  neutral: "#F8F5F0"
  surface: "#FFFFFF"
  surface-container: "#F2EEE7"
  surface-container-high: "#E8E3D9"
  on-surface: "#1A1A1A"
  on-surface-variant: "#6B6660"
  outline: "#B8B0A4"
  outline-variant: "#E0D9CC"
  inverse-surface: "#1A1A1A"
  inverse-on-surface: "#F8F5F0"
  error: "#B23A2E"
  on-error: "#FFFFFF"
  error-container: "#F4DAD5"
  on-error-container: "#7A1F16"
typography:
  display-lg:
    fontFamily: Newsreader
    fontSize: 64px
    fontWeight: 500
    lineHeight: 1.05
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Newsreader
    fontSize: 40px
    fontWeight: 500
    lineHeight: 1.15
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Newsreader
    fontSize: 28px
    fontWeight: 500
    lineHeight: 1.25
  body-lg:
    fontFamily: Public Sans
    fontSize: 18px
    fontWeight: 400
    lineHeight: 1.55
  body-md:
    fontFamily: Public Sans
    fontSize: 16px
    fontWeight: 400
    lineHeight: 1.6
  body-sm:
    fontFamily: Public Sans
    fontSize: 14px
    fontWeight: 400
    lineHeight: 1.5
  label-md:
    fontFamily: Public Sans
    fontSize: 14px
    fontWeight: 500
    lineHeight: 1.4
  label-sm:
    fontFamily: Public Sans
    fontSize: 12px
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: 0.08em
rounded:
  none: 0
  sm: 2px
  md: 4px
  lg: 8px
  full: 9999px
spacing:
  xs: 4px
  sm: 8px
  md: 16px
  lg: 32px
  xl: 64px
  gutter: 24px
  margin: 48px
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.neutral}"
    typography: "{typography.label-md}"
    rounded: "{rounded.sm}"
    padding: 12px 24px
    height: 44px
  button-primary-hover:
    backgroundColor: "{colors.secondary}"
  button-ghost:
    backgroundColor: transparent
    textColor: "{colors.primary}"
    typography: "{typography.label-md}"
    rounded: "{rounded.sm}"
    padding: 12px 20px
    height: 44px
  button-ghost-hover:
    backgroundColor: "{colors.surface-container}"
  input-field:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    typography: "{typography.body-md}"
    rounded: "{rounded.sm}"
    padding: 12px 16px
    height: 44px
  input-field-focus:
    backgroundColor: "{colors.surface}"
  card-paper:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.on-surface}"
    rounded: "{rounded.md}"
    padding: 24px
  list-item:
    backgroundColor: transparent
    textColor: "{colors.on-surface}"
    typography: "{typography.body-md}"
    padding: 16px 0
  list-item-hover:
    backgroundColor: "{colors.surface-container}"
  chip:
    backgroundColor: "{colors.surface-container}"
    textColor: "{colors.on-surface-variant}"
    typography: "{typography.label-sm}"
    rounded: "{rounded.full}"
    padding: 6px 12px
---

# Editorial Calm

## Brand & Style

Editorial Calm is a long-form, type-led design system that draws from independent magazine layouts and contemporary book design. The visual personality is patient, considered, and quietly authoritative — the UI gets out of the reader's way and lets the content carry the experience.

The aesthetic intent is "read it twice." Pages should feel composed rather than packed. Negative space is doing structural work, not decorative work — the reader's eye lands on the content because nothing competes with it. Emotional response: an unhurried confidence, the feeling of opening a thoughtful magazine rather than scrolling a feed.

## Colors

The palette is a warm-neutral foundation with a single earthy accent.

- **Primary (#1A1A1A):** A deep ink — used for headlines, body text, and primary buttons. Sets the editorial baseline.
- **Secondary (#6B6660):** A warm grey — used for metadata, captions, secondary interactive states, and supporting text.
- **Tertiary (#B23A2E):** A terracotta accent — used sparingly for the single most important action on a screen, key highlights, and editorial flourishes (drop caps, inline marks). Never used for ambient elements.
- **Neutral (#F8F5F0):** A warm cream — the foundational page background. Reads softer and more organic than pure white without losing brightness.
- **Surface (#FFFFFF):** Paper white — used for elevated content surfaces (cards, modals, input fields) that sit on top of the neutral page.
- **Outline / Outline-variant:** Used for 1px hairline rules and divider lines. Variant is the lower-contrast option used inside content; the standard outline reserves itself for component boundaries.

## Typography

The system pairs **Newsreader** (a contemporary variable serif from Production Type) for narrative and **Public Sans** (the US Web Design System workhorse) for interface text. Both are free on Google Fonts.

- **Display & headlines** are set in Newsreader Medium with negative tracking to create the gravitational pull of an editorial cover line. Italics are encouraged for headlines where character is wanted.
- **Body copy** is Public Sans 400 at 16–18px with a 1.55–1.6 line-height for comfortable long-form reading.
- **Labels** are Public Sans 500–600. The smallest label size uses uppercase and 0.08em letter-spacing for metadata, timestamps, and category tags — a deliberate echo of magazine masthead conventions.
- **Numbers** in tabular contexts should use `font-variant-numeric: tabular-nums` for alignment.

## Layout & Spacing

The layout follows a measured-prose model: long, narrow text columns inside a generous canvas.

- **Content width:** Body text columns max at 680px. UI components extend to a 1080px content frame. Outer page margins start at 48px and scale up at larger viewports.
- **Vertical rhythm:** An 8px base unit governs all spacing decisions. Standard sequence is `xs (4) — sm (8) — md (16) — lg (32) — xl (64)` with `gutter: 24` and `margin: 48` as named tokens for repeated layout patterns.
- **Grouping:** Related content is housed in cards with 24px internal padding. Vertical gaps between cards default to 32px (`lg`). Section breaks use 64px (`xl`) margins to create deliberate breathing room.
- **Containment:** Editorial Calm is structurally biased toward density-restrained columns over dashboard grids. If a layout starts to feel like a dashboard, return to single-column.

## Elevation & Depth

Depth is implied through paper-on-paper layering and hairline borders, not shadows.

- **Level 1 (Page):** The warm cream neutral. No shadow, no border — this is the canvas.
- **Level 2 (Cards & modals):** Paper white surface sitting on the neutral page. A single 1px outline-variant border defines the edge. No drop shadow.
- **Level 3 (Floating, exceptional):** A very soft `box-shadow: 0 1px 3px rgba(26, 26, 26, 0.06)` reserved for hover and dropdown menus — always paired with the outline border, never replacing it.

The absence of dramatic shadows is a deliberate identity choice. Anything more aggressive breaks the editorial calm.

## Shapes

The shape language is restrained and precise — buttons and inputs use `rounded-sm (2px)`, cards use `rounded-md (4px)`. Pills and chips use `rounded-full` to mark them as a distinct typological category (tags, statuses, filters).

The 2–4px corner radius family is small enough to feel architectural and not toy-like, while still being visible. Sharp corners (0px) are reserved for rule lines and full-width image edges.

## Components

### Buttons

Primary buttons are solid `primary` ink on neutral text, used once per screen for the dominant action. Hover state shifts the background to `secondary` (the warm grey). Ghost buttons are transparent with primary text and a subtle `surface-container` hover — used for secondary, tertiary, and destructive-confirm actions.

All buttons are 44px tall to comfortably meet touch-target accessibility. Padding is asymmetric (12px vertical, 24px horizontal on primary, 20px horizontal on ghost) to honour the label-md text proportions.

### Inputs & Forms

Input fields are paper white sitting on the neutral page, with a 1px outline-variant border that becomes `outline` on focus. Label-above is the default arrangement; helper text sits below in `body-sm` `on-surface-variant`. Error states swap the border to `error` and surface helper text in `error` on `error-container`.

### Cards & Lists

Cards are paper white with 24px internal padding and `rounded-md`. They contain a body of editorial content and an optional metadata strip (`label-sm` uppercase). List items are borderless by default with hairline `outline-variant` dividers between rows — hover surfaces a subtle `surface-container` background to indicate interactivity.

### Chips

Chips use `rounded-full` to distinguish them from buttons. They carry `label-sm` text on `surface-container` background and are used for tags, filters, and statuses — never for primary actions.

### Typography Application

Headlines use Newsreader Medium with italic accents for editorial character. Body copy stays in Public Sans for legibility. The `label-sm` uppercase treatment is reserved for metadata, section eyebrows, and timestamps — never for body copy.

## Do's and Don'ts

- **Do** reserve `tertiary` (the terracotta accent) for one element per screen. Two accents kills the editorial calm.
- **Don't** use shadows for visual hierarchy when a hairline border will do. The system is paper-on-paper, not card-stack.
- **Do** let body text columns breathe — max 680px wide, never edge-to-edge on desktop.
- **Don't** mix Newsreader and Public Sans within the same headline or sentence. The pairing works section-to-section, not character-to-character.
- **Do** use italic Newsreader for emphasis in headlines — it's the system's character moment.
- **Don't** use drop shadows on buttons or input fields. Borders and weight changes carry interaction state.
- **Do** maintain WCAG AA contrast (4.5:1 for body, 3:1 for large text) — the primary/neutral pairing meets this comfortably; the secondary/neutral pairing is body-text-only.
- **Don't** introduce additional accent colors. The system is deliberately mono-accent.
