# Design Better — the heuristics catalogue (H1–H50)

Each entry: number (cite in reviews) + short name + one-line rule + code action. Style-neutral throughout — defer every visual property to `docs/DESIGN.md`.

## Contents

- [Visual hierarchy & emphasis](#visual-hierarchy--emphasis) — H1–H6
- [Layout & alignment](#layout--alignment) — H7–H10
- [Typography craft](#typography-craft) — H11–H13
- [Color & contrast (non-stylistic)](#color--contrast-non-stylistic) — H14–H16
- [Interaction & feedback](#interaction--feedback) — H17–H22
- [Forms](#forms) — H23–H27
- [States: empty, loading, error, success](#states-empty-loading-error-success) — H28–H32
- [Motion](#motion) — H33–H36
- [Accessibility (WCAG 2.2 AA)](#accessibility-wcag-22-aa) — H37–H42
- [Mobile & touch](#mobile--touch) — H43–H46
- [Cognitive load & navigation](#cognitive-load--navigation) — H47–H48
- [AI-product specifics](#ai-product-specifics) — H49–H50

## Visual hierarchy & emphasis

**H1. One primary action per view (Von Restorff).** Make the primary CTA the single visually distinct element — use the most prominent DESIGN.md color and largest button size. Secondary actions use quieter tokens.

**H2. Hierarchy from size + weight + color, not size alone (Refactoring UI).** De-emphasize secondary text by reducing weight or shifting to a secondary text color token before reducing font size.

**H3. Proximity groups, white space separates (Gestalt).** Stack related fields with a small `gap`; separate unrelated groups with a larger spacing token.

**H4. Common Region bounds groups (Gestalt).** When proximity isn't enough, bound with a card, divider, or tinted surface — using DESIGN.md elevation/surface tokens.

**H5. White space is a tool — default to too much (Refactoring UI).** Generous padding reads as confident. Tightening should be deliberate, not default.

**H6. Snap to the spacing scale; nothing one pixel off (Polish).** Every margin/padding/gap is a DESIGN.md token. Alignment to the grid is the difference between "designed" and "drafted."

## Layout & alignment

**H7. Semantic HTML before divs + ARIA (WCAG 1.3.1).** Use `<main>`, `<nav>`, `<header>`, `<section>`, `<article>`, `<button>`, `<label>`. Reach for `role=` only when no native element fits.

**H8. Reading line length 50–75ch.** Cap prose containers with `max-width: 65ch` (or analogous).

**H9. Reflow at 320 CSS px (WCAG 1.4.10).** Every view works at 320 px wide with no horizontal scroll.

**H10. Text spacing tolerance (WCAG 1.4.12).** Layout survives user overrides of line-height (≥ 1.5×), letter-spacing (≥ 0.12em), word-spacing (≥ 0.16em).

## Typography craft

**H11. Use only documented type levels.** Every `font-size`/`font-weight` references a DESIGN.md typography token.

**H12. Tabular figures in data (`font-variant-numeric: tabular-nums`).** Numbers in tables, dashboards, and ledgers align vertically.

**H13. Modern text-wrap (`balance` on headlines, `pretty` on prose).** Headlines read more deliberately with `text-wrap: balance`; body paragraphs avoid orphans with `text-wrap: pretty`.

## Color & contrast (non-stylistic)

**H14. Body text contrast ≥ 4.5:1 (WCAG 1.4.3 AA).** Verify every body/background token pair. Large text (≥18.66 px bold or ≥24 px) needs ≥ 3:1.

**H15. UI component contrast ≥ 3:1 (WCAG 1.4.11).** Form borders, icon-only buttons, focus rings, chart strokes all need ≥ 3:1 vs adjacent color.

**H16. Color is never the sole signal.** Pair every color-encoded state with an icon, label, or pattern.

## Interaction & feedback

**H17. Feedback within 100 ms (Doherty / Norman).** Every action that triggers logic confirms visually within 100 ms (press state, ripple, optimistic update, skeleton).

**H18. Three-state minimum for interactive elements.** Default, hover or focus-visible, active, disabled. Loading is a fifth where async.

**H19. Affordances signal interactivity.** Buttons look pressable; links visibly differ from body text — use DESIGN.md tokens for the visual treatment.

**H20. Discoverability over hidden interactions (Norman).** Critical actions are visible by default — never hidden behind hover, long-press, or undisclosed gestures.

**H21. Easy reversal (Shneiderman).** Undo on destructive actions; Cancel on every modal; Back without data loss; soft-delete with restore.

**H22. Constraints prevent errors (Norman).** Disable invalid options; use `min`, `max`, `step`, `pattern`, `type` on inputs; gate submit on validity.

## Forms

**H23. Single-column layout, top-aligned labels.** Stack vertically; labels above inputs; never placeholder-as-label.

**H24. `inputmode` + `type` for mobile keyboards.** `type="email"`, `inputmode="numeric"`/`"decimal"`, `type="tel"`, `type="url"`.

**H25. `autocomplete` attributes.** `email`, `name`, `new-password`, `one-time-code`, `postal-code`, etc. Saves users 30 seconds and respects password managers.

**H26. Inline validation on blur, clear on change.** Validate `onBlur`; clear errors `onChange` once valid. Validating every keystroke punishes typos.

**H27. Smart defaults absorb complexity (Tesler).** Detect timezone, locale, currency; pre-select the safe option; parse natural language ("tomorrow 3 pm"); pre-fill from previous inputs.

## States: empty, loading, error, success

**H28. Four states, every data view.** Empty, loading, error, success — each designed and coded using DESIGN.md tokens.

**H29. Skeleton over spinner for content (NN/g).** Use shape-matching placeholders that match final layout dimensions (prevents CLS).

**H30. Optimistic UI for low-risk actions.** Likes, toggles, follows update immediately; reconcile silently; rollback with a toast on failure.

**H31. Empty states are first impressions.** Every empty list has a one-line explanation of what should be there + a primary CTA.

**H32. Errors say what / why / how to fix.** Never just "Something went wrong." Always offer a retry or recovery path.

## Motion

**H33. UI motion in the 150–400 ms band (NN/g, Material 3).** Micro 100–150 ms (hover, toggle); standard 200–300 ms (menu, modal); large 300–400 ms (page transition). Repeated UI never animates over 500 ms.

**H34. Easing matches direction.** Ease-out entering (`cubic-bezier(0, 0, 0.2, 1)`); ease-in exiting; ease-in-out for moves between two on-screen states.

**H35. Animate `transform` and `opacity` only.** GPU-accelerated. Never animate `width`/`height`/`top`/`left`.

**H36. Honor `prefers-reduced-motion`.** Wrap non-essential motion in `@media (prefers-reduced-motion: reduce)`. Replace transforms with instant changes or short opacity fades — never remove the feedback signal entirely.

## Accessibility (WCAG 2.2 AA)

**H37. Keyboard operability for everything (WCAG 2.1.1).** Every interactive element reachable via Tab / Shift+Tab / Enter / Space / Arrow. Focus traps in modals work.

**H38. Visible focus rings (WCAG 2.4.7).** Never `outline: none` without a `:focus-visible` equivalent — ≥ 2 px, ≥ 3:1 contrast. Use a DESIGN.md focus token if defined.

**H39. Pointer target size ≥ 24×24 (WCAG 2.5.8).** Every clickable element ≥ 24×24 CSS px. On touch, aim for 44×44 (Apple HIG) or 48×48 (Material 3).

**H40. Programmatically associated labels (WCAG 3.3.2).** Every input has a `<label htmlFor=id>` or wraps the input. `aria-label` only when the input is genuinely unlabeled visually.

**H41. Focus not obscured (WCAG 2.4.11).** Sticky headers/footers must not cover the focused element. Set `scroll-padding-top`/`-bottom` equal to sticky heights.

**H42. Accessible authentication (WCAG 3.3.8).** No cognitive puzzles for login. Allow paste in password fields. Pair OTP with `autocomplete="one-time-code"`.

## Mobile & touch

**H43. Thumb-zone primary CTAs.** On mobile, primary actions land in the bottom half. Avoid top corners for high-frequency actions.

**H44. Respect safe-area insets.** Use `env(safe-area-inset-*)` on fixed/sticky bottom bars and full-bleed headers.

**H45. No hover-only critical info.** Tooltips shown only on `:hover` are invisible on touch. Show critical content by default.

**H46. Drag has a tap alternative (WCAG 2.5.7).** Every drag-to-sort/delete/resize has a button or menu equivalent.

## Cognitive load & navigation

**H47. Navigation ≤ 5–9 items (Miller).** Top-level nav stays inside the magic number; push the rest into a menu, command palette, or settings.

**H48. Recognition over Recall (NN/g #6).** Surface selected filters, current page (active nav state), breadcrumbs, recent items. Never make the user remember a value from a previous screen.

## AI-product specifics

**H49. Stream + Stop is a primary control.** AI responses stream as they generate; a visible Stop button at primary affordance weight while streaming aborts the underlying request, not just the UI. Tool calls / thinking / searching surface as labeled steps.

**H50. AI output is an editable draft.** Treat model responses as drafts users can edit, accept partially, regenerate, or reject. Cite sources inline with one-click open. Distinguish error categories (network, rate limit, content filter, model error) so each has its own recovery path.
