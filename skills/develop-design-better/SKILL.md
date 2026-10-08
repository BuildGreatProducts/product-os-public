---
name: develop-design-better
description: >-
  Applies UX/UI craft heuristics — hierarchy, interaction states, accessibility, motion, polish —
  while building or refactoring UI, using docs/DESIGN.md tokens for every visual value and flagging
  missing tokens as New Patterns instead of inventing them. Use when the user says "design better",
  "make this UI feel more designed", or "apply design polish". Not for checking changes against
  DESIGN.md — use develop-design-review; not for conversion — use develop-cro-audit.
---

# Develop: Design Better

A craft layer for any coding agent generating or reviewing UI. Style is owned by `docs/DESIGN.md`; this skill owns the timeless UX/UI craft heuristics — drawn from Nielsen Norman Group, Laws of UX, Shneiderman, Refactoring UI, WCAG 2.2, Don Norman, Apple HIG, Material 3, and established AI-product patterns — that separate "shipped" from "designed."

> **Boundary.** When a heuristic implies a visual property, reference a DESIGN.md token by name (`{colors.primary}`, `{rounded.md}`). If DESIGN.md doesn't have the token, flag as a New Pattern — never inline hex, font names, or arbitrary px.

## Inputs

- **`docs/DESIGN.md`** — required. If missing, stop and tell the member to run `design-design-system`.
- **The thing being built or refactored** — a brief, a file, or uncommitted diff.
- **The `## Product Identity` section of `docs/DESIGN.md`** and **`docs/DEFINE.md`** — optional. Identity informs microcopy tone; DEFINE.md helps weight which heuristic categories dominate.
- **`docs/COPY.md`** — optional. When present, it is the source of truth for all microcopy: lexicon nouns and verbs, per-surface budgets, mechanical rules, and the banned list. H31 and H32 apply per COPY.md's empty-state and error patterns.

## Workflow

1. **Read `docs/DESIGN.md`.** Parse the token catalogue (colors, typography, rounded, spacing, components) and the markdown rules (elevation, shape, Do's and Don'ts).

2. **Confirm scope and weight.** Restate the surface (signup / dashboard / chat / settings / detail / marketing) and which heuristic categories will dominate — a signup leans on Forms + States + Accessibility + Microcopy; a data dashboard leans on Hierarchy + IA + Cognitive Load; an AI chat leans on the AI-product subset.

3. **Generate or review using both layers.** Read [references/heuristics.md](references/heuristics.md) — the 50-item catalogue (H1–H50), grouped by category; use its Contents to go straight to the categories that dominate this surface. DESIGN.md tokens for every visual decision; the heuristics for every craft decision. Cite heuristics by number in reviews (*"H22 — disabled instead of erroring after submit"*).

4. **Verify before delivering** — the pre-flight checklist; every item passes:
   - [ ] Every interactive element has default, hover/focus-visible, active, disabled, and loading (where async) states.
   - [ ] Every async surface designs and codes all four states: empty, loading, error, success — and the success state is designed with care, not left as an afterthought (H28).
   - [ ] Every form input has a programmatically associated `<label>`, the correct `inputmode`/`type`, an `autocomplete` attribute, and `onBlur` validation.
   - [ ] Every motion is 150–400 ms, eases by direction (out entering / in exiting / in-out moving), animates `transform`/`opacity` only, and honors `prefers-reduced-motion`.
   - [ ] Body text contrast ≥ 4.5:1, UI components ≥ 3:1, focus rings ≥ 3:1 at ≥ 2 px.
   - [ ] Pointer targets ≥ 24×24 CSS px (≥ 44×44 on touch).
   - [ ] Layout works at 320 CSS px wide with no horizontal scroll.
   - [ ] The primary action is the single visually dominant element on the view (H1).
   - [ ] Microcopy is plain language (per `docs/COPY.md` when present); errors say what / why / how to fix (H32).
   - [ ] Every visual decision references a DESIGN.md token. Missing tokens are flagged as New Patterns for promotion via `develop-design-review`, not invented inline.

5. **Deliver.** Note which heuristic categories dominated and surface any trade-off where a heuristic was knowingly skipped.

**Next step:** run `develop-design-review` before committing UI work to catch token drift that slipped through.
