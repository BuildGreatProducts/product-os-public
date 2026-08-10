---
name: studio-develop-design-review
description: Use when the user has a `docs/DESIGN.md` and uncommitted changes in their product codebase (new components, modified styles, new screens) and wants a design-system adherence review before committing or merging. Triggers on phrases like "design review", "review my design system adherence", "check my changes against DESIGN.md", "design system check", "what design tokens am I missing", or "promote my new patterns to DESIGN.md". Runs in the app repo — the repository that contains `productos/`. Reads `docs/DESIGN.md`, inspects uncommitted git changes (working tree + staged), classifies each visual change as an Inconsistency, a New Pattern, or Already-Aligned, and writes a prioritized, timestamped report to `design-review/` (a new file per run): a fix to-do list, a promotion checklist for `docs/DESIGN.md`, and a paste-ready fix prompt for a coding agent. Optionally references `productos/design/1. Product Identity.md` for tone if present; works standalone.
---

# Develop: Design Review

This skill runs in the **app repo** — the repository that contains `productos/` — and produces a **design system adherence review** of uncommitted UI changes against the documented `docs/DESIGN.md`. The output is a timestamped report at `design-review/YYYY-MM-DD-HHMM-design-review.md` — a new file per run, never overwriting prior reviews — containing a structured report with three buckets — Inconsistencies (changes that violate documented tokens), New Patterns (changes that introduce something not yet in the design system), and Already-Aligned (changes that use tokens correctly) — plus a prioritized to-do list of fixes, a separate list of new patterns proposed for promotion into `DESIGN.md`, and a **paste-ready fix prompt** at the end of the Inconsistencies section that the user can copy directly into Claude Code, Cursor, or another coding agent to fix every issue in one pass.

The voice is a senior design systems engineer doing a pre-merge review with deep experience reading diffs across React, Vue, Svelte, native iOS, Android, and CSS-in-JS codebases — and specifically with the Google DESIGN.md format that the Design System skill produces. The engineer's job is not to gatekeep; it is to surface every drift between the code and the documented system, propose specific fixes that close the drift, and recognize when a new pattern in the code is good enough to promote into the design system rather than retro-fitting it to fit existing tokens.

Design systems decay one PR at a time. Most decay is invisible — a teammate hardcodes `#3B82F6` instead of using `{colors.primary}` because they couldn't remember the token name; a new dialog uses 14px radius instead of the documented `{rounded.md}` (12px); a hero section introduces a font weight that doesn't exist in the type scale. Each individual change is harmless. A hundred of them, and the design system is a relic. This skill's job is to catch the drift before it commits, fix what should be fixed, and promote what should be promoted.

> **Session length:** Designed to be completable in 15–30 minutes. The skill parses the design system, scans the diff, classifies each change, drafts the report section by section with the user, and writes the file. No external research required — everything needed lives in `DESIGN.md` and the working tree.

## Inputs

Locate the following:

1. **The user's product codebase** — **required**. The skill runs in the repository root. It must be a git repository with uncommitted changes (working tree + index). If there are no uncommitted changes, stop and tell the user there's nothing to review — suggest they either run this against a specific commit range (e.g., the last N commits on the current branch) or come back after they've made changes.

2. **`docs/DESIGN.md`** — **required**. The Google-format design system file produced by the `studio-design-design-system` skill. Provides the YAML frontmatter (machine-readable tokens) and the markdown body (eight sections of human-readable rationale and rules). If `DESIGN.md` is missing or substantively empty, stop and tell the user to run `studio-design-design-system` first.

3. **`productos/design/1. Product Identity.md`** — **optional** — absent in a repo without ProductOS. When present, the Identity supplies the tone-of-voice attributes for any copy critique in the review and the contrarian belief + visual style for calibrating "does this new pattern feel right for the brand?" judgments. If absent, the review focuses strictly on token-level adherence.

4. **`docs/PRODUCT.md`** — **optional**. If present, the product type contextualizes the review (a marketplace listing card has different conventions than a B2B dashboard card, even with the same tokens).

If `docs/DESIGN.md` does not exist, stop and tell the user which skill to run first. Do not improvise a review against an undocumented design system.

## The reviewer's voice

Adopt the voice of a senior design systems engineer doing a code review:

- **Specific to the diff.** Never "the new button doesn't match the design system." Always "`src/components/CTAButton.tsx:18` uses `backgroundColor: '#2563EB'`; `DESIGN.md` defines `{colors.primary}` as `#1A4D8C`. Either replace the hex with the token, or — if `#2563EB` is intentional — propose it as a new `primary-bright` token."
- **Three buckets, no fourth.** Every visual change lands in exactly one of: **Inconsistency**, **New Pattern**, or **Already-Aligned**. Don't invent "minor inconsistency" or "stylistic preference" — when in doubt, flag it as a new pattern and let the user decide.
- **Promote, don't punish.** A new pattern in the code isn't a failure of discipline — it's a signal that the design system has a gap. Frame promotion proposals as "the system was missing this; here's how to add it" rather than "you should have used what was there."
- **Token-fluent.** Speak in tokens. Not "this should be slightly darker," but "this should be `{colors.on-surface}` (`#1A1A1A`), not the inline `#2D2D2D`."
- **Effort-aware on fixes.** Order the to-do list by effort × impact. A find-and-replace across 12 files for a stale color token is a 10-minute fix that closes a hundred future inconsistencies. A bespoke component refactor is a half-day fix that closes one. Sort accordingly.

## Workflow

### 1. Read `docs/DESIGN.md` and parse the token catalogue

Read the file in full. Parse the YAML frontmatter into a structured token catalogue:

- **Colors:** every named color token and its hex value.
- **Typography:** every type level — `fontFamily`, `fontSize`, `fontWeight`, `lineHeight`, `letterSpacing`.
- **Rounded:** every named radius level and its dimension.
- **Spacing:** every named spacing token and its dimension.
- **Components:** every component definition and its referenced tokens.

Read the markdown body for the rules that aren't expressed as tokens — the elevation model (shadows / borders / glass / tonal / flat), the shape philosophy (which corners apply to which components), the Do's and Don'ts list, and any prose constraints in `Brand & Style` or `Components`.

State the parsed catalogue back to the user in one compact paragraph: *"Reviewing against `docs/DESIGN.md` — [N] color tokens, [N] type levels, [N] radius levels, [N] spacing tokens, [N] component definitions. Elevation model: [hairlines / shadows / glass / tonal / flat]. Excluded fonts (per identity): [list]. Confirm before I scan the diff."*

If the file is malformed (YAML doesn't parse, sections missing), surface the specific problem and ask the user whether to proceed with a partial catalogue or fix the file first. Don't silently work around malformed source-of-truth.

### 2. Detect uncommitted changes and scope the review

Run `git status --porcelain` and `git diff` against the working tree + index to detect what's changed. Default scope: every modified, added, or staged file in the working tree.

Filter to **UI-relevant files** by extension and path:

- React / Vue / Svelte components: `.tsx`, `.jsx`, `.ts`, `.js`, `.vue`, `.svelte`
- Style files: `.css`, `.scss`, `.sass`, `.less`, `.styl`, CSS-in-JS in component files
- Native: `.swift`, `.kt`, `.kotlin`, `.dart`, `.xml` (Android layouts), `.storyboard`, `.xib`
- Tailwind config: `tailwind.config.*`, `tailwind.config.ts`
- Design token files: `tokens.*`, `theme.*`, `colors.*`, `typography.*`
- Static markup: `.html`, `.htm`, `.mdx`

Skip files that are clearly out of scope: server routes without JSX, schema files, migrations, fixtures, lockfiles, tests with no visual assertions, generated build output.

If the diff is large (>30 changed files), ask the user whether to scope down: *"Detected [N] changed files. Want me to review all of them, or scope to a folder (e.g., `src/components/`) or to a single feature?"* Don't blanket-review a thousand-line auto-formatter pass.

State the scope back: *"Scope: [N] UI files across [folders]. About to scan for design system adherence — confirm."*

### 3. Scan each changed file and classify every visual decision

Walk through the diff hunk by hunk. For every line that touches a visual property, classify it into one of three buckets.

**Visual properties to inspect:**

- **Color values.** Hex (`#RRGGBB`, `#RGB`), `rgb()`, `rgba()`, `hsl()`, `hsla()`, named CSS colors (`white`, `black`, `gray`, etc.), Tailwind color classes (`bg-blue-500`, `text-red-600`), CSS variables (`var(--color-primary)`), native color literals (`UIColor`, `Color.parse`).
- **Typography.** `font-family`, `font-size`, `font-weight`, `line-height`, `letter-spacing`, Tailwind text classes (`text-xl`, `font-bold`), `@font-face` declarations, native font calls (`UIFont`, `TextStyle`).
- **Spacing.** `margin`, `padding`, `gap`, `top/right/bottom/left`, Tailwind spacing classes (`p-4`, `gap-8`, `space-y-2`), inline `style={{ padding: 16 }}`.
- **Radius.** `border-radius`, Tailwind radius classes (`rounded-md`, `rounded-2xl`), inline `style={{ borderRadius: 12 }}`.
- **Elevation.** `box-shadow`, `filter: drop-shadow`, `backdrop-filter`, Tailwind shadow classes (`shadow-lg`, `shadow-xl`), `border` declarations used for hairline elevation.
- **Component shape.** Newly introduced component types (a new `<Dialog>` variant, a new `<Card>` shape, a new `<Button>` size) — even if every token used is correct, the *component* may be a new pattern not yet documented in DESIGN.md's Components section.

For each hit, decide the bucket:

#### Inconsistency

The change uses a hardcoded value where a documented token exists, OR uses a documented token but applies it to a role the design system explicitly forbids, OR violates a documented rule from the Do's and Don'ts or Brand & Style section.

Examples:
- `backgroundColor: '#1A4D8C'` where `{colors.primary}` exists with that exact hex.
- `font-family: 'Inter'` where the design system uses Public Sans (and Inter is in the exclusion list).
- `border-radius: 14px` where the system documents only `none / 4px / 8px / 12px / 16px / full`.
- `box-shadow: 0 4px 12px rgba(0,0,0,0.15)` in a system documented as hairline-borders-only.
- A primary CTA using `{colors.secondary}` when the Do's-and-Don'ts say "primary CTAs always use `{colors.primary}`."

For each Inconsistency, capture:
1. **Location:** file path + line number + hunk header.
2. **The offending value:** the literal as it appears in the diff.
3. **The documented alternative:** the exact token reference or rule it should follow.
4. **Severity:** P0 (breaks brand or accessibility — e.g., primary CTA wrong color, contrast failure, banned font), P1 (wrong token in a high-visibility surface), P2 (wrong token in a low-visibility surface or a debatable case), P3 (cosmetic — e.g., 14px radius vs documented 12px on a single tooltip).
5. **The fix:** the literal replacement to make.

#### New Pattern

The change introduces a visual decision that isn't documented in `DESIGN.md` but isn't clearly wrong — a new color shade, a new type level, a new component variant, a new motion curve, a new spacing value. The right resolution may be to *promote* it into the design system rather than retro-fit it to existing tokens.

Examples:
- A new `colors.success-bright: #2DC07A` that doesn't exist in the system but is used as a confirmation toast accent.
- A new `body-xs` type level (12px) needed for dense data tables.
- A new component — `<Banner>` — with its own padding/radius/elevation rules.
- A `motion.easing.spring` curve used on a new bottom-sheet, where the system only documents standard ease-in-out.

For each New Pattern, capture:
1. **Location:** file path + line number(s) where it's used.
2. **The new value(s):** the literal(s) being introduced.
3. **Proposed token:** the suggested token name and placement in the DESIGN.md YAML (e.g., `colors.success-bright`, `typography.body-xs`, `components.banner`).
4. **Proposed DESIGN.md prose:** one or two sentences for the relevant markdown section explaining the role and when to use it.
5. **Promotion verdict — Claude's recommendation:** *Promote* (this fills a real gap and should be added), *Refactor* (the gap is real but the proposed value is wrong — propose a different value), or *Defer* (single-use case, not yet worth a token — leave inline for now and revisit if it recurs).

#### Already-Aligned

The change uses a documented token correctly. No action required. Capture briefly (a one-line count by file) so the report can credit the user without padding the document with hundreds of bullets.

### 4. Reconcile and rank

Before drafting the report, reconcile across findings:

- **De-duplicate.** If the same hardcoded color appears in 12 files, it's one finding with 12 locations, not 12 findings.
- **Cluster New Patterns.** If a new component appears in three files, it's one New Pattern entry, not three.
- **Resolve Inconsistency-vs-New-Pattern ambiguity.** A `border-radius: 14px` is an Inconsistency if 14px clearly should be 12px (the documented `md`). It's a New Pattern if there's an argument the system needs a `rounded.lg-tight` token between `md` (12) and `lg` (16). Lean Inconsistency unless the user's diff shows the value is used systematically — one-off use is rarely worth a new token.
- **Rank Inconsistencies by effort × impact.** P0s first regardless of effort. Within each severity, prefer find-and-replace fixes that close many instances over bespoke single-file refactors.
- **Rank New Patterns by Promote → Refactor → Defer.** Within "Promote," prefer additions that close repeated gaps over one-off patterns.

State the reconciled summary back to the user: *"Found [N] Inconsistencies (P0: [n], P1: [n], P2: [n], P3: [n]) across [N] files, [N] New Patterns proposed for promotion, and [M] aligned changes. Want me to walk through them before I write the report, or write it now and you'll review the file?"* Default to writing the report unless the user wants a guided walkthrough.

### 5. Draft the timestamped review file

Determine the output path. Each run produces a **new file** named with the current date and time so prior reviews are preserved:

```
design-review/YYYY-MM-DD-HHMM-design-review.md
```

Where `YYYY-MM-DD` is the current date and `HHMM` is the current 24-hour time. Example: `design-review/2026-06-03-1430-design-review.md` for a review run at 14:30 on June 3, 2026.

Get the current date and time programmatically (e.g., `date "+%Y-%m-%d-%H%M"` in bash) — do **not** hardcode or guess. If the `design-review/` folder doesn't exist at the repo root, create it (`mkdir -p design-review`). Never overwrite an existing review — if by some collision the same filename already exists, append `-2`, `-3`, etc. to the filename until it's unique.

Structure of the file:

```
# Design Review

*Reviewed: [Month Day, Year at HH:MM]. Scope: uncommitted changes in [N] UI files against `docs/DESIGN.md`. Generated by `studio-develop-design-review`.*

## Summary

- **Scope:** [N] UI files modified or added on the working tree.
- **Inconsistencies:** [N] total — P0: [n], P1: [n], P2: [n], P3: [n].
- **New Patterns proposed:** [N] — Promote: [n], Refactor: [n], Defer: [n].
- **Already-aligned changes:** [N] visual decisions used documented tokens correctly.
- **Top three things to do before commit:** [one-line each, the highest-leverage fixes].

---

## Inconsistencies

Sorted by severity, then by effort × impact.

### P0 — Breaks brand or accessibility

#### [Finding title — e.g., "Primary CTA uses wrong color"]

- **Locations:** `src/components/CTAButton.tsx:18`, `src/sections/Hero.tsx:42` ([N] total)
- **Offending value:** `backgroundColor: '#2563EB'`
- **Documented alternative:** `{colors.primary}` (`#1A4D8C`)
- **Why it matters:** [one sentence anchored in DESIGN.md prose — e.g., "Primary CTAs are the brand's single most visible color surface. Drifting them off-token shifts the entire brand perception two clicks at a time."]
- **Fix:** Replace `'#2563EB'` with `colors.primary` (or the framework's token-reference syntax — `var(--color-primary)`, `theme.colors.primary`, `Tailwind: bg-primary`).
- **To-do:** [ ] Replace `#2563EB` → `{colors.primary}` across [N] files. *(~10 min)*

[…repeat per P0 finding…]

### P1 — Wrong token in high-visibility surface

[…same structure…]

### P2 — Wrong token in low-visibility surface

[…same structure…]

### P3 — Cosmetic

[…same structure, may be a single grouped bullet list rather than per-finding sections…]

### Paste-ready fix prompt for your coding agent

Copy the block below and paste it into Claude Code, Cursor, Codex, or whichever coding agent you use. It contains every Inconsistency above with file paths, line numbers, the offending value, and the documented replacement — sorted by severity — plus the constraints the agent should respect. The agent should be able to action the entire list in one pass.

\`\`\`
You are working in this repository. I just ran a design system adherence review against `docs/DESIGN.md` on my uncommitted changes. Your job is to fix every Inconsistency listed below — nothing else. Do not reformat unrelated code. Do not touch files that aren't named here. Do not change any value that's already aligned with `docs/DESIGN.md`. Preserve all existing comments.

Work top to bottom (P0 → P3). For each item:
1. Open the listed file.
2. Locate the offending value at the listed line (line numbers may have shifted slightly — use the offending value as the anchor).
3. Replace it with the documented alternative, using the project's token-reference convention (e.g., the framework's theme accessor, CSS variable, or Tailwind class — match the surrounding code).
4. Move to the next item.

Constraints:
- Reference `docs/DESIGN.md` as the source of truth. If a token name has multiple resolution paths in the codebase (e.g., a CSS variable AND a Tailwind class), match the convention used elsewhere in the same file.
- Do not introduce new tokens — that's a separate step (see the Promotion checklist in the review file). If a fix seems to require a new token, leave the value as-is and add `// TODO design-review: needs new token` next to it.
- Do not modify accessibility attributes, ARIA labels, or test IDs.
- Do not change file imports unless a documented token requires importing a new theme module.

Inconsistencies to fix:

P0:
- [file:line] — Replace `<offending value>` with `<documented alternative>` (token: `{tokens.path}`). Reason: <one short phrase>.
- [file:line] — Replace `<offending value>` with `<documented alternative>` (token: `{tokens.path}`). Reason: <one short phrase>.

P1:
- [file:line] — Replace `<offending value>` with `<documented alternative>` (token: `{tokens.path}`).
- [file:line] — Replace `<offending value>` with `<documented alternative>` (token: `{tokens.path}`).

P2:
- [file:line] — Replace `<offending value>` with `<documented alternative>` (token: `{tokens.path}`).

P3:
- [file:line] — Replace `<offending value>` with `<documented alternative>` (token: `{tokens.path}`).

When you're done:
1. Run the project's typecheck and linter. Fix any errors introduced by the changes.
2. Re-run any unit tests that touch the modified files.
3. Report back: which files you changed, which items you couldn't fix and why, and whether tests pass.

Do not commit. The user wants to review the diff before committing.
\`\`\`

Populate every `<offending value>` and `<documented alternative>` literal with the exact values from the Inconsistency findings above — no `<placeholders>` left in the rendered file. The user should be able to copy the block and paste it without editing.

---

## New Patterns

Patterns introduced by the diff that aren't yet in `docs/DESIGN.md`. Each has a recommended verdict.

### Promote — fills a real gap; add to DESIGN.md

#### [Pattern title — e.g., "Compact body type level (`body-xs`)"]

- **Locations used:** `src/components/DataTable.tsx:88`, `src/components/CompactList.tsx:34`
- **New value:** `fontSize: 12px`, `lineHeight: 1.5`, family `Public Sans`, weight `400`.
- **Proposed token:**
  ```yaml
  typography:
    body-xs:
      fontFamily: Public Sans
      fontSize: 12
      fontWeight: 400
      lineHeight: 1.5
  ```
- **Proposed prose for `## Typography`:** "*`body-xs` — Use only inside dense data surfaces (tables, compact lists) where `body-sm` (14px) would compromise row density. Never use for primary reading content.*"
- **To-do:** [ ] Add `typography.body-xs` to `docs/DESIGN.md` YAML. [ ] Add the prose line above to the `## Typography` section. [ ] Update component usage to reference `{typography.body-xs}` instead of inline `fontSize: 12`.

[…repeat per Promote finding…]

### Refactor — gap is real, but the proposed value is wrong

#### [Pattern title]

- **Locations used:** […]
- **New value introduced:** […]
- **Why "refactor" not "promote":** [one sentence — e.g., "The system already has `colors.tertiary` (`#B23A2E`) for accents. The new `#D14638` is 8% lighter; it should use the documented token, not introduce a competing one."]
- **Proposed alternative:** Replace the new value with `{colors.tertiary}`.
- **To-do:** [ ] Replace `#D14638` with `{colors.tertiary}` in [N] files.

### Defer — single-use, not worth a token yet

#### [Pattern title]

- **Locations used:** [one location]
- **New value:** […]
- **Why "defer":** [one sentence — e.g., "Single-use today, used once on a marketing splash. If it recurs, propose it as a token then."]
- **To-do:** [ ] Leave inline. Add comment `// one-off — see design-review/ for context` so the next reviewer recognizes it.

---

## Already-aligned

[N] visual decisions across [N] files used documented tokens correctly. No action.

Notable wins:
- [file path]: [N] correct token references — e.g., uses `{colors.primary}`, `{typography.body-md}`, `{rounded.md}`.

---

## Promotion checklist for `docs/DESIGN.md`

Group all "Promote" verdicts above into a single ordered checklist the user can work through in one sitting:

- [ ] Add `typography.body-xs` token + prose to `## Typography`.
- [ ] Add `colors.success-bright` token + prose to `## Colors`.
- [ ] Add `components.banner` token + prose to `## Components`.
- [ ] After tokens land, run this skill again to confirm the new patterns are now classified as Already-aligned.

## Fix checklist for the working tree

Group all Inconsistency To-dos into a single ordered checklist:

- [ ] [P0] Replace `#2563EB` → `{colors.primary}` across [N] files. *(~10 min)*
- [ ] [P0] Replace `'Inter'` → `'Public Sans'` in `src/styles/globals.css`. *(~2 min)*
- [ ] [P1] [...]
- [ ] [P2] [...]
- [ ] [P3] [...]

---

## Sources

- Design system: `docs/DESIGN.md`
- Brand strategy (optional context): `productos/design/1. Product Identity.md`
- Product context (optional): `docs/PRODUCT.md`
- Diff scope: working tree + index at [commit SHA] on [branch name]
```

Write the report concisely. Bullets are tight. The whole document should be readable end-to-end in 5–8 minutes. Padding, meta-commentary, and re-pitching the design system are the enemy.

### 6. Verify before delivering

Re-read the written file and check:

- **File path is correct.** The file is at `design-review/YYYY-MM-DD-HHMM-design-review.md` with the actual current date and time — not hardcoded, not a guess, not a placeholder. The `design-review/` folder exists. No prior review was overwritten.
- **Every finding has a location.** No bullet says "the buttons" — every bullet has a file path and line number (or a hunk range).
- **Every Inconsistency has a fix.** No bullet says "review and decide" — every bullet has a literal replacement or a clear action.
- **Every New Pattern has a verdict.** No bullet leaves the user to invent the resolution — each is tagged Promote / Refactor / Defer with reasoning.
- **The paste-ready fix prompt exists** at the end of the Inconsistencies section, wrapped in a triple-backtick code block, with every `<offending value>` and `<documented alternative>` populated literally — no `<placeholder>` text left behind. Every Inconsistency above appears in the prompt, sorted by severity.
- **The Promotion checklist and Fix checklist exist** at the bottom and contain every finding's to-do, grouped and ordered.
- **The summary at the top is accurate** — the counts match the body.
- **No copy-paste of `DESIGN.md` content.** The review references DESIGN.md by section and token name; it does not duplicate the design system prose.
- **The file is readable end-to-end in 5–8 minutes.**

Deliver via a `computer://` link and a short summary — one line for the scope (files scanned, branch), one line for the counts (P0/P1/P2/P3 inconsistencies, N new patterns), the **top three to-dos** for the user to action first, and a line pointing the user to the paste-ready fix prompt: *"Scroll to 'Paste-ready fix prompt for your coding agent' to action everything in one pass."* Keep the summary tight: this is a recap, not a re-explanation of the report.

## Edge cases

- **No uncommitted changes.** Stop early. Suggest the user either make changes first or run against a specific commit range (e.g., `git diff main...HEAD` if reviewing a branch).
- **`docs/DESIGN.md` missing or unparseable.** Stop. Tell the user to run `studio-design-design-system` to create the file, or to fix the YAML errors before re-running.
- **Diff is entirely non-UI.** State explicitly: "No UI-relevant files in the diff. Nothing to review against the design system." Don't manufacture findings.
- **Diff is enormous (auto-formatter pass, dependency upgrade).** Ask the user to scope down before scanning. A 5000-line review report is worse than no review.
- **Pre-existing inconsistencies in unchanged code.** Out of scope by default — the skill reviews uncommitted changes, not the whole codebase. If the user wants a full-codebase audit, suggest expanding scope explicitly in a follow-up run; otherwise mention pre-existing issues only when they're adjacent to a current finding (e.g., "the line above this one also hardcodes the color — fix together or leave for a separate pass?").
- **DESIGN.md is partial.** If the design system covers colors and typography but not, e.g., motion or icons, classify motion/icon changes as New Patterns even when they look reasonable — the absence of documentation is itself the gap to surface.

## Pacing and approval

- **Parse DESIGN.md before scanning the diff.** Don't classify changes against a design system you haven't fully read.
- **State the scope back before scanning.** Confirm the file scope and the design system catalogue with the user in one paragraph. A misunderstood scope produces a useless report.
- **Three buckets, no fourth.** Every visual change is Inconsistency, New Pattern, or Already-Aligned. Resist the urge to invent categories.
- **Promote, don't punish.** New Patterns are signals of design system gaps, not failures of discipline. Frame promotion proposals as additions to the system.
- **Effort × Impact on Inconsistencies.** Within severity, sort by effort × impact. Find-and-replace fixes that close many instances win over bespoke single-file refactors.
- **Concise final document.** Tight bullets, exact file paths and line numbers, literal fixes. The report reads in 5–8 minutes.

## What "done" looks like

A timestamped file at `design-review/YYYY-MM-DD-HHMM-design-review.md` (a new file per run, prior reviews preserved) where:

- **A summary block** at the top names the scope, the counts (by severity and by verdict), and the top three to-dos to action first.
- **An Inconsistencies section** lists every visual change that violates `docs/DESIGN.md`, sorted by severity (P0 → P3) and grouped by finding. Each finding has file paths, line numbers, the offending literal, the documented alternative, why it matters in one sentence, the literal fix, and a to-do checkbox.
- **A paste-ready fix prompt for the user's coding agent** sits at the end of the Inconsistencies section, wrapped in a triple-backtick code block. Every Inconsistency above appears in the prompt with its literal offending value and documented replacement — no `<placeholder>` text left behind. The user copies the entire block once and pastes it into Claude Code, Cursor, or Codex to action every fix in one pass.
- **A New Patterns section** lists every visual change that introduces something not in `docs/DESIGN.md`, grouped by verdict (Promote / Refactor / Defer). Each Promote entry includes a proposed YAML addition and proposed prose for the relevant DESIGN.md markdown section.
- **An Already-aligned section** credits correctly-tokenized changes with a count by file. No padding bullets.
- **A Promotion checklist** at the bottom consolidates every "Promote" verdict into a single ordered to-do list the user can work through to update `docs/DESIGN.md`.
- **A Fix checklist** at the bottom consolidates every Inconsistency to-do into a single ordered list, sorted by severity and effort.
- **A Sources block** names the design system file, the optional context files, and the diff scope (branch + commit SHA).
- **Every finding has a location and a fix.** No vague bullets. No "review and decide" hand-offs.
- **The file is readable end-to-end in 5–8 minutes** by a developer or technical founder ready to action it.

Recommended next step after a successful session: copy the **paste-ready fix prompt** from the end of the Inconsistencies section into Claude Code, Cursor, or Codex to action every P0 → P3 fix in one pass. Then work through the **Promotion checklist** to update `docs/DESIGN.md` with the new tokens and prose. Once promotions land, re-run this skill — a new dated file lands in `design-review/`, and the previously-flagged New Patterns should now classify as Already-aligned, confirming the design system has absorbed the new vocabulary. Pair this skill with `studio-develop-cro-audit` for a complete pre-merge review (design adherence + conversion performance), or run it on every PR as a lightweight design system maintenance loop. Over time, the `design-review/` folder becomes a chronological audit trail of how the design system has evolved with the product.
