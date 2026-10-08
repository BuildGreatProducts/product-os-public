---
name: develop-design-review
description: >-
  Reviews uncommitted UI changes against docs/DESIGN.md, classifies each visual change as an
  Inconsistency, a New Pattern, or Already-Aligned, and writes a timestamped report to
  docs/design-reviews/ with a fix list, a promotion checklist for DESIGN.md, and a paste-ready fix
  prompt. Use when the user says "design review", "check my changes against DESIGN.md", or "promote
  my new patterns". Not for improving UI craft while building — use develop-design-better; not for
  creating DESIGN.md — use design-design-system or design-design-system-from-code.
---

# Develop: Design Review

This skill runs in the **app repo** — the repository that contains `productos/` — and produces a **design system adherence review** of uncommitted UI changes against `docs/DESIGN.md`. Each run writes a new timestamped report at `docs/design-reviews/YYYY-MM-DD-HHMM-design-review.md` (never overwriting prior reviews) with three buckets — **Inconsistencies** (changes that violate documented tokens or rules), **New Patterns** (changes that introduce something not yet in the design system), and **Already-Aligned** (changes that use tokens correctly) — plus a prioritized fix list, a promotion checklist for `DESIGN.md`, and a **paste-ready fix prompt** the member can copy into their coding agent to fix every issue in one pass.

**Shapes:** for products with screens — `web-app`, `mobile-app`, `desktop-app`, `browser-extension`, `website` — and for any landing page, settings screen, or portal another shape ships. Shapes without a UI have nothing for it to review.

## Inputs

Read inputs from `docs/` at the app repo root.

1. **The product codebase** — **required**. A git repository with uncommitted changes (working tree + index). If there are none, stop and tell the member there's nothing to review — suggest running against a specific commit range (e.g., `git diff main...HEAD` for a branch) or coming back after they've made changes.
2. **`docs/DESIGN.md`** — **required**. The Google-format design system from `design-design-system` (or `design-design-system-from-code`): YAML frontmatter tokens plus the markdown body's sections (after `## Product Identity` when ProductOS wrote one). If it's missing or substantively empty, stop and tell the member to run `design-design-system` first. Don't improvise a review against an undocumented design system.
3. **`docs/DESIGN.md` → `## Product Identity`** — optional (absent without ProductOS). Supplies tone of voice for any copy critique, and the contrarian belief + visual style for judging whether a new pattern feels right for the brand. If absent, review strictly at token level.
4. **`docs/COPY.md`** — optional. When present, check new or changed user-facing strings against its review rubric — lexicon, mechanical rules, banned words — and report violations as Inconsistencies alongside the token findings.
5. **`docs/DEFINE.md`** — optional. The product type (from the Summary and Offer) contextualizes the review — a marketplace listing card has different conventions than a B2B dashboard card, even with the same tokens.

## The reviewer's voice

A senior design systems engineer doing a pre-commit review — surfacing every drift between code and the documented system, not gatekeeping.

- **Specific to the diff.** Never "the new button doesn't match the design system." Always "`src/components/CTAButton.tsx:18` uses `backgroundColor: '#2563EB'`; `DESIGN.md` defines `{colors.primary}` as `#1A4D8C`. Either replace the hex with the token, or — if `#2563EB` is intentional — propose it as a new `primary-bright` token."
- **Three buckets, no fourth.** Every visual change lands in exactly one of Inconsistency, New Pattern, or Already-Aligned. Don't invent "minor inconsistency" or "stylistic preference" — when in doubt, flag it as a New Pattern and let the member decide.
- **Promote, don't punish.** A new pattern signals a gap in the design system, not a failure of discipline. Frame proposals as "the system was missing this; here's how to add it."
- **Token-fluent.** Not "this should be slightly darker," but "this should be `{colors.on-surface}` (`#1A1A1A`), not the inline `#2D2D2D`."

## Workflow

### 1. Read `docs/DESIGN.md` and parse the token catalogue

Read the file in full before looking at the diff. Parse the YAML frontmatter into a catalogue: every color token and hex; every type level (`fontFamily`, `fontSize`, `fontWeight`, `lineHeight`, `letterSpacing`); every radius level; every spacing token; every component definition and the tokens it references. Read the markdown body for rules that aren't tokens — the elevation model (shadows / borders / glass / tonal / flat), the shape philosophy, the Do's and Don'ts, and prose constraints in `Brand & Style` or `Components`.

State the catalogue back in one compact paragraph: *"Reviewing against `docs/DESIGN.md` — [N] color tokens, [N] type levels, [N] radius levels, [N] spacing tokens, [N] component definitions. Elevation model: [hairlines / shadows / glass / tonal / flat]. Excluded fonts (per identity): [list]. Confirm before I scan the diff."*

If the file is malformed (YAML doesn't parse, sections missing), surface the specific problem and ask whether to proceed with a partial catalogue or fix the file first. Don't silently work around a malformed source of truth.

### 2. Detect uncommitted changes and scope the review

Run `git status --porcelain`, `git diff HEAD` (working tree + index), and `git ls-files --others --exclude-standard`. Untracked files never appear in `git diff`, and new component files are where most New Patterns live — read each one in full. Default scope: every modified, added, staged, or untracked file.

Filter to UI-relevant files — components, stylesheets, native views/layouts, Tailwind config, token/theme files, static markup. Skip server routes without JSX, schemas, migrations, fixtures, lockfiles, tests with no visual assertions, and generated build output. If the diff is entirely non-UI, say so — "No UI-relevant files in the diff. Nothing to review against the design system." — and stop. Don't manufacture findings.

If the diff is large (>30 changed files, an auto-formatter pass, a dependency upgrade), ask the member to scope down first: *"Detected [N] changed files. Want me to review all of them, or scope to a folder (e.g., `src/components/`) or to a single feature?"* A 5000-line review is worse than no review.

State the scope back: *"Scope: [N] UI files across [folders]. About to scan for design system adherence — confirm."*

### 3. Scan each changed file and classify every visual decision

Walk the diff hunk by hunk. Inspect every line that touches a visual property — color, typography, spacing, radius, elevation — in whatever form the codebase expresses it (literals, CSS variables, Tailwind classes, inline styles, native color/font calls). Also inspect **component shape**: a newly introduced component type or variant (a new `<Dialog>` variant, `<Card>` shape, `<Button>` size) may be a New Pattern even if every token it uses is correct, because DESIGN.md's Components section doesn't document it yet.

Classify each hit:

#### Inconsistency

A hardcoded value where a documented token exists, a documented token applied to a role the system forbids, or a violation of a documented rule (Do's and Don'ts, Brand & Style). Examples:
- `backgroundColor: '#1A4D8C'` where `{colors.primary}` exists with that exact hex.
- `font-family: 'Inter'` where the system uses Public Sans (and Inter is in the exclusion list).
- `border-radius: 14px` where the system documents only `none / 4px / 8px / 12px / 16px / full`.
- `box-shadow: 0 4px 12px rgba(0,0,0,0.15)` in a system documented as hairline-borders-only.
- A primary CTA using `{colors.secondary}` when the Do's and Don'ts say primary CTAs always use `{colors.primary}`.

Capture for each: (1) **location** — file path + line number + hunk header; (2) **the offending value** as it appears in the diff; (3) **the documented alternative** — exact token reference or rule; (4) **severity** — P0 (breaks brand or accessibility: wrong primary CTA color, contrast failure, banned font), P1 (wrong token on a high-visibility surface), P2 (wrong token on a low-visibility surface, or a debatable case), P3 (cosmetic, e.g., 14px vs 12px radius on a single tooltip); (5) **the fix** — the literal replacement.

#### New Pattern

A visual decision not documented in `DESIGN.md` but not clearly wrong — a new color shade, type level, component variant, motion curve, or spacing value. The right resolution may be to *promote* it into the system rather than retro-fit it. Examples: a `colors.success-bright: #2DC07A` used as a confirmation-toast accent; a 12px `body-xs` level for dense tables; a new `<Banner>` with its own padding/radius/elevation; a `motion.easing.spring` curve where the system only documents ease-in-out. If DESIGN.md is partial (say, no motion or icon section), classify changes in the undocumented area as New Patterns even when they look reasonable — the missing documentation is the gap to surface.

Capture for each: (1) **location(s)**; (2) **the new value(s)**; (3) **proposed token** name and YAML placement (e.g., `typography.body-xs`, `components.banner`); (4) **proposed DESIGN.md prose** — one or two sentences on the role and when to use it; (5) **verdict** — *Promote* (fills a real gap), *Refactor* (the gap is real but the value is wrong — propose a different one), or *Defer* (single use, leave inline and revisit if it recurs).

#### Already-Aligned

Uses a documented token correctly. No action — capture a one-line count by file so the report credits the work without padding.

**Pre-existing issues in unchanged code** are out of scope. Mention one only when it's adjacent to a current finding ("the line above this one also hardcodes the color — fix together or leave for a separate pass?"); if the member wants a whole-codebase audit, suggest a separate, explicitly scoped run.

### 4. Reconcile and rank

- **De-duplicate.** The same hardcoded color in 12 files is one finding with 12 locations.
- **Cluster New Patterns.** A new component in three files is one entry.
- **Resolve Inconsistency-vs-New-Pattern ambiguity.** `border-radius: 14px` is an Inconsistency if it clearly should be the documented 12px; a New Pattern if there's a case for a token between `md` (12) and `lg` (16). Lean Inconsistency unless the diff shows the value used systematically — one-off use is rarely worth a token.
- **Rank Inconsistencies by effort × impact.** P0s first regardless of effort. Within each severity, a find-and-replace that closes many instances (a 10-minute fix closing a hundred future drifts) beats a bespoke single-file refactor (a half-day fix closing one).
- **Rank New Patterns Promote → Refactor → Defer.** Within Promote, prefer additions that close repeated gaps.

State the reconciled summary: *"Found [N] Inconsistencies (P0: [n], P1: [n], P2: [n], P3: [n]) across [N] files, [N] New Patterns proposed for promotion, and [M] aligned changes. Want me to walk through them before I write the report, or write it now and you'll review the file?"* Default to writing the report unless the member wants a guided walkthrough.

### 5. Write the timestamped review file

Get the timestamp programmatically — `date "+%Y-%m-%d-%H%M"` — never hardcode or guess it. Create the folder if needed (`mkdir -p docs/design-reviews`). Write to `docs/design-reviews/YYYY-MM-DD-HHMM-design-review.md`; if that filename already exists, append `-2`, `-3`, … until it's unique. Never overwrite a prior review.

Read [templates/design-review-report.md](templates/design-review-report.md) for the report structure and [templates/fix-prompt.md](templates/fix-prompt.md) for the paste-ready prompt that closes the Inconsistencies section. Fill both with real values — every bracket and `<placeholder>` replaced. Reference DESIGN.md by section and token name; don't copy its prose into the review. Tight bullets, no meta-commentary or re-pitching of the design system.

### 6. Verify before delivering

Re-read the written file and check:

- [ ] Path is `docs/design-reviews/YYYY-MM-DD-HHMM-design-review.md` with the real current date and time; no prior review overwritten.
- [ ] Every finding has a location — a file path and line number (or hunk range), never "the buttons."
- [ ] Every Inconsistency has a literal fix or clear action — never "review and decide."
- [ ] Every New Pattern has a Promote / Refactor / Defer verdict with reasoning; every Promote entry has proposed YAML and proposed prose for the relevant DESIGN.md section.
- [ ] The paste-ready fix prompt sits at the end of the Inconsistencies section in a triple-backtick block, contains every Inconsistency sorted by severity, with every offending value and documented alternative populated literally — no `<placeholder>` text.
- [ ] The Already-aligned section credits correct token use with a count by file — no padding bullets.
- [ ] The Promotion checklist and Fix checklist at the bottom contain every finding's to-do, grouped and ordered (fixes by severity, then effort).
- [ ] The Sources block names the design system file, optional context files, and the diff scope (branch + commit SHA).
- [ ] The summary counts match the body, and the top three to-dos are the highest-leverage fixes.
- [ ] No DESIGN.md prose duplicated; the file reads end to end in 5–8 minutes.

Deliver the file path and a short recap — one line for scope (files scanned, branch), one line for counts (P0/P1/P2/P3, N new patterns), the **top three to-dos**, and: *"Scroll to 'Paste-ready fix prompt for your coding agent' to action everything in one pass."*

**Next step:** paste the fix prompt into the coding agent, work the Promotion checklist into `docs/DESIGN.md`, then re-run this skill before committing UI work — promoted patterns should now classify as Already-aligned.
