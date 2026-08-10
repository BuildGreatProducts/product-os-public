---
name: studio-design-design-system-from-code
description: Use when the user already has a product codebase and wants to reverse-engineer the design system already in the code into a Google-format `docs/DESIGN.md` — extracting the colors, typography, spacing, radii, elevation, and components actually used, flagging internal inconsistencies (competing values for one role — several "primary" blues, forked paddings, mixed radii, stray hex), resolving each with the user, then writing the file. Triggers on "design system from code", "reverse-engineer my design system", "I have a codebase but no DESIGN.md", "audit my codebase for design tokens", "consolidate my design tokens". Runs in the app repo — the repository that contains `productos/` — and reads CSS variables, Tailwind config, theme files and components; surfaces inconsistencies to resolve interactively; writes `docs/DESIGN.md` in Google's exact format (YAML tokens + eight sections), matching `studio-design-design-system`, compatible with `studio-develop-design-review`.
---

# Design: Design System from Code (DESIGN.md)

This skill is the **reverse** of `studio-design-design-system`. Instead of going *forward* — Product Identity + a reference image → a brand-new `docs/DESIGN.md` — it goes *backward*: it reads the design system that already lives, implicitly and inconsistently, inside an existing product codebase, and turns it into a single documented, Google-format `docs/DESIGN.md`. The forward skill is for greenfield products with a brand but no code. This skill is for brownfield products with code but no documented system.

Every shipping codebase already *has* a design system — it's just undocumented, scattered across CSS files and component props, and almost always internally inconsistent. There are three blues that all mean "primary," button padding that's `12px 24px` in one component and `10px 20px` in another, cards rounded at 8px, 12px, and 14px depending on who wrote them, and a `--color-text` custom property that half the codebase ignores in favour of inline hex. The job of this skill is to **find the de-facto system, surface every internal conflict, let the user pick the canonical value for each role, and write the result down** in the exact format the rest of ProductOS consumes.

The cardinal rule is **document reality, don't silently improve it.** This skill captures what the code *actually does* — including the real fonts, the real palette, the real spacing scale. It does not invent a new aesthetic, substitute "better" fonts, or quietly fix contrast. The only thing it actively resolves is *internal inconsistency* — and even that it resolves *with the user*, never on its own. Quality issues (a pair that fails WCAG AA, a non-free font, a sprawling type scale) get **flagged as advisory notes** at the end, never silently changed. A `DESIGN.md` that lies about the codebase is worse than none.

The voice is a senior design systems engineer doing a brownfield audit — someone who has reverse-engineered token systems out of React, Vue, Svelte, SwiftUI, Android, and raw-CSS codebases, knows the difference between a deliberate variant and an accidental fork, and is allergic to documenting a system that doesn't match the code it claims to describe.

> **Session length:** Designed to be completable in 30–60 minutes. The skill scans the codebase, builds the token inventory, clusters the conflicts, walks the user through resolving each one, and writes the file. No external research required — everything needed lives in the code, with optional context from `productos/design/1. Product Identity.md` and `docs/PRODUCT.md` if they exist in the workspace.

## Inputs

Locate the following. The skill runs in the **app repo root** — the repository that contains `productos/` (it also works standalone in any codebase without ProductOS).

1. **The user's product codebase** — **required.** The repository whose UI you'll read. Identify the framework and styling approach before doing anything else (see Workflow step 2). If the repo has no UI code at all (pure backend, CLI, data pipeline), stop and tell the user there's no design system to extract.

2. **The Google DESIGN.md format spec** — **required, embedded below.** The output must conform exactly to Google's open-source DESIGN.md format (Google Labs, Apache 2.0, [github.com/google-labs-code/design.md](https://github.com/google-labs-code/design.md)) — the same format `studio-design-design-system` produces. If the `REFERENCE-DESIGN.md` bundled with the `studio-design-design-system` skill happens to be accessible, read it once as the structural blueprint. If you're running inside the product repo where it isn't present, use the embedded spec in the "Output format" section below. If a `docs/DESIGN.md` already exists, read it first and treat its structure as the format reference, and the session as a reconciliation rather than a from-scratch write.

3. **`productos/design/1. Product Identity.md`** — **optional, tiebreaker only** — absent in a repo without ProductOS. When present, the Identity's tone and named visual references are used *only* as a tiebreaker when the code is genuinely ambiguous (e.g., two blues are used equally often and you need a reason to pick one). It does **not** override what the code does — this skill documents the implementation, not the aspiration. If absent, resolve conflicts purely on code evidence.

4. **`docs/PRODUCT.md`** — **optional, context only.** If present, it tells you what the product is and who uses it — useful for naming the aesthetic in the `Brand & Style` section and for sanity-checking which surfaces matter most. Not required.

## The engineer's voice

Adopt the voice of a senior design systems engineer reverse-engineering a system from code:

- **Evidence-led.** Every claim is anchored in the code. Not "your primary color is blue," but "`#2563EB` appears in 34 places, `#2D6CDF` in 6, and `#3B82F6` in 2 — all used as the primary action color. I'm proposing `#2563EB` as canonical `primary`. Confirm or pick another."
- **Descriptive, not prescriptive.** The system already exists; your job is to *document* it, not redesign it. Resist the urge to "improve" the palette or swap the fonts. The one thing you actively fix is internal inconsistency — and only with the user's sign-off.
- **Token-fluent.** Speak in tokens and exact values. Not "the spacing is a bit irregular," but "spacing clusters cleanly on a 4px base — `4 / 8 / 16 / 24 / 32 / 64` — except for `13px`, `18px`, and `25px`, which appear once or twice each and look like off-grid one-offs. Snap them to the nearest scale step?"
- **Conflict-precise.** Never "there are some inconsistencies." Always the specific cluster: the competing values, where each is used, and the occurrence count, with a recommended canonical pick and the reason.
- **Honest about gaps.** If a category has no discernible system (e.g., elevation is a free-for-all of ad-hoc shadows), say so plainly and propose the smallest defensible system that fits what's there — flagged as a proposal, not a discovery.

## Output format (Google DESIGN.md spec — embedded)

The file is two parts: YAML frontmatter (machine-readable tokens) and a Markdown body (eight sections, fixed order). This is normative — do not improvise the schema, the section set, or the section order.

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
    backgroundColor: <hex or {colors.token-reference}>
    textColor: <hex or {colors.token-reference}>
    typography: <{typography.token-reference}>
    rounded: <{rounded.token-reference}>
    padding: <dimension>
    height: <dimension>
---
```

**Token naming conventions** (map the code's de-facto values onto these names):

- Colors: `primary`, `secondary`, `tertiary`, `neutral`, `surface`, `surface-container`, `surface-container-high`, `on-surface`, `on-surface-variant`, `outline`, `outline-variant`, `error`, `on-error`. Add roles only when the code genuinely uses them (e.g., `success`, `warning` if the product has status colors).
- Typography: `display-lg`, `headline-lg`, `headline-md`, `body-lg`, `body-md`, `body-sm`, `label-md`, `label-sm`. Aim for 6–10 levels; never exceed 15. If the code has 24 font sizes, that *is* the conflict — collapse them to a documented scale with the user.
- Rounded: `none`, `sm`, `md`, `lg`, `xl`, `full`.
- Spacing: `xs`, `sm`, `md`, `lg`, `xl`, plus named tokens like `gutter` and `margin` where the layout uses them repeatedly.

**Token-reference syntax:** components reference tokens with `{colors.primary}`, `{typography.body-md}`, `{rounded.md}` — braces, dot-path, exact token name.

**Markdown body — exactly eight sections, in this order:**

1. `## Brand & Style` — 2 paragraphs naming the aesthetic the code adds up to (e.g., "utilitarian dashboard," "consumer-playful," "editorial-minimal"). Derived from the code, contextualized by `docs/PRODUCT.md` if present.
2. `## Colors` — palette strategy in prose, then a named bullet per color role with hex and where it's used in the code. End noting any colors you consolidated.
3. `## Typography` — the type system in prose (single family / pair / sprawl-collapsed-to-scale), then a bullet per level. Document the **real** font families as used in the code.
4. `## Layout & Spacing` — the spacing base unit and scale, container widths, and grid/layout model as found in the code.
5. `## Elevation & Depth` — the depth model actually in use (shadows / borders / glass / tonal / flat), or the model you proposed to consolidate an ad-hoc one.
6. `## Shapes` — the corner-radius philosophy and how radius varies by component type.
7. `## Components` — style guidance per documented component (buttons, inputs, cards, list items, chips, plus product-specific ones). Every component here has a YAML entry and vice versa.
8. `## Do's and Don'ts` — 4–8 guardrails, biased toward the consolidation decisions made this session ("Do use `{colors.primary}` (`#2563EB`) for primary actions — not the legacy `#3B82F6`").

## Workflow

### 1. Read context and set expectations

If `docs/DESIGN.md` already exists, read it — this becomes a reconciliation session (extend/correct the existing file) rather than a from-scratch write; tell the user. If `productos/design/1. Product Identity.md` and/or `docs/PRODUCT.md` exist, read them for tiebreaker and naming context. State the plan back in one line: *"I'll scan the codebase, inventory the design tokens you're actually using, flag every internal inconsistency, we'll pick the canonical value for each together, then I'll write `docs/DESIGN.md` in the Google format. Starting the scan."*

### 2. Map the styling architecture

Before extracting values, find *where* design decisions live. Identify the framework and the styling approach(es) in use — there are often several layered together:

- **Tailwind:** `tailwind.config.{js,ts,cjs,mjs}` — read `theme` and `theme.extend` (colors, fontFamily, fontSize, spacing, borderRadius, boxShadow). Then grep for arbitrary values (`bg-[#...]`, `p-[13px]`, `rounded-[14px]`) which are the off-system escapes.
- **CSS custom properties:** `:root { --color-...: ... }` in global CSS, plus any `[data-theme]` / `.dark` overrides. Then grep for raw hex / px used directly instead of the variables.
- **CSS-in-JS:** styled-components / emotion / vanilla-extract — theme objects (`theme.colors.*`), `styled.button\`...\``, and inline `style={{ }}` props.
- **Design-token files:** `tokens.json` (Style Dictionary / W3C DTCG), `theme.ts`, `tokens.ts`, `colors.ts`, `typography.ts`, `design-tokens/*`.
- **Component-library theme overrides:** MUI `createTheme`, Chakra `extendTheme`, Mantine theme, shadcn `globals.css` variables.
- **Native:** SwiftUI `Color`/`Font` extensions and asset catalogs; Android `colors.xml` / `themes.xml` / Compose `Theme.kt`; Flutter `ThemeData`.
- **Raw / scattered:** SCSS `$variables`, plain CSS, and the hardest case — values hardcoded inline throughout components with no central source.

State the architecture back: *"Styling architecture: Tailwind config with a partial token theme, plus ~40 arbitrary-value escapes and a handful of inline hex in page components. Primary token source is `tailwind.config.ts`; the conflicts are mostly in the escapes. Scanning those now."*

If it's a **monorepo or multi-app** repository, ask which app/package to document before scanning — don't blend two products' systems into one file.

### 3. Extract the de-facto token inventory

Sweep the code and collect every value actually used, grouped by category. **Count occurrences and note locations** — frequency and location are how conflicts get resolved later. Capture reality, including the mess; do not clean up yet.

- **Colors:** every hex, `rgb()/rgba()`, `hsl()/hsla()`, named CSS color, Tailwind color (config + arbitrary), CSS variable value, and native color literal. Group by apparent role (background / text / border / accent / status).
- **Typography:** every `font-family`, `font-size`, `font-weight`, `line-height`, `letter-spacing`; Tailwind text/font classes; `@font-face`; native font calls. Note which families are actually loaded.
- **Spacing:** every `margin` / `padding` / `gap` / inset value and Tailwind spacing class. Detect the base unit (usually 4 or 8) and which values are on- vs off-grid.
- **Radius:** every `border-radius` value and radius class, grouped by the component type it's applied to.
- **Elevation:** every `box-shadow`, `drop-shadow`, `backdrop-filter`, and hairline-`border`-as-elevation. Note whether one model dominates or several coexist.
- **Components:** every recurring UI primitive (button, input, card, list item, chip, badge, modal) and its concrete style values — including duplicate/forked implementations of the same primitive.

### 4. Detect internal inconsistencies (the core of this skill)

Cluster the inventory into **conflicts** — places where the code uses competing values for what should be a single role. This is the only thing the skill actively resolves, and it resolves it *with* the user. Look for these patterns (see "Inconsistency patterns" below for detail):

- Near-duplicate colors mapped to one role (multiple "primary" blues).
- Token defined but bypassed (a `--color-primary` exists, yet raw hex of ~the same color is used directly elsewhere).
- Off-grid spacing values breaking an otherwise clean scale.
- Multiple radii for the same component category.
- Mixed units for the same property (`rem` vs `px` vs `em`).
- Font sprawl (multiple sans families; a weight set that isn't a scale; 20+ font sizes).
- Competing elevation models for the same elevation level (shadow here, border there).
- Forked components (two `Button` implementations with divergent padding/radius/states).

Build a **conflict list**: each entry is one role with its competing values, the occurrence count and representative locations for each, and your recommended canonical pick with the reason. De-duplicate (the same stray hex in 12 files is one conflict with 12 locations) and cluster forked components into one entry.

Summarize before resolving: *"Inventory done. Clean on radius and base spacing. [N] conflicts to resolve: 3 primary blues, 2 body-text greys, button padding forked 3 ways, 4 off-grid spacing values, and two Button components. Want to walk through them now?"*

### 5. Walk through the conflicts interactively

For **each conflict**, present it the same way and get a decision before moving on:

> **Role: `primary` (primary action color)** — 3 competing values:
> - `#2563EB` — 34 uses (Button, Link, theme config) ← **recommend canonical**
> - `#2D6CDF` — 6 uses (older marketing pages)
> - `#3B82F6` — 2 uses (one CTA, one icon)
> Recommend `#2563EB`: most-used, and it's the one defined in `tailwind.config.ts`. Keep it? (or pick another / I can show the swatches)

Apply the **resolution heuristics** (below) to form the recommendation, but the user decides. Capture each decision tersely. Where the user picks a canonical value that differs from values still in the code, note that those are now *drift* — they'll be documented as "the wrong value" and `studio-develop-design-review` will catch them later. Keep momentum: one conflict, one recommendation, one confirm, next.

Do **not** turn quality issues into conflicts here. If `primary` on `surface` fails WCAG AA, that's not a conflict to resolve — it's an advisory note for step 8. Stay focused on internal inconsistency.

### 6. Assemble the DESIGN.md

With every conflict resolved, map the canonical values onto the Google format:

- Write the **YAML frontmatter** — canonical colors under the standard role names, the consolidated type scale, the spacing scale, the radius scale, and a `components` entry for each documented primitive using `{token}` references.
- Write the **eight markdown sections** in order, in tight prose. Document the **real** fonts and values. In `Colors`, `Typography`, and `Do's and Don'ts`, briefly record the consolidation decisions ("consolidated three primary blues to `#2563EB`") so the file explains *why* it looks the way it does and what the code should refactor toward.
- Pick a `name` for the system that describes what the code adds up to (use `docs/PRODUCT.md` / Identity for flavour if present, else descriptive — "Acme Dashboard System").

### 7. Show the user and iterate

Present in two passes: **YAML frontmatter first** (confirm the canonical tokens and the consolidated scales), then the **markdown body** (confirm tone and the per-component prose). Fold in corrections. Iterate once or twice. Keep each section to 2–4 short paragraphs — this is a reference doc, not an essay.

### 8. Write to `docs/DESIGN.md`, then flag advisories

Write the approved file to `docs/DESIGN.md` (`mkdir -p docs` if needed). If the file already exists, show the diff in conversation and overwrite only on the user's approval.

Then, **separately from the file**, surface the advisory notes you deliberately kept out of it — the quality issues you found but didn't silently fix:

- **Contrast:** any documented `backgroundColor` + `textColor` pair that fails WCAG AA (4.5:1 body, 3:1 large). State the ratio; propose a fix; let the user decide whether to adjust the token or accept it.
- **Non-free / excluded fonts:** if a documented family isn't free for commercial use, or is on ProductOS's exclusion list (Inter, Instrument Serif, Outfit, Plus Jakarta Sans), note it — but **keep the real font in the file** unless the user explicitly asks to substitute. The file documents the code; substitution is a separate decision.
- **Residual sprawl:** anything you collapsed aggressively (24 sizes → 8 levels) so the user knows what got rounded.

### 9. Verify before delivering

Re-read the written file and check:

- **YAML parses** — consistent indentation, hex quoted, no trailing colons.
- **All eight sections present, in order** — Brand & Style, Colors, Typography, Layout & Spacing, Elevation & Depth, Shapes, Components, Do's and Don'ts.
- **Every component in YAML has prose in `Components`, and vice versa.**
- **Token references use exact `{colors.primary}` / `{typography.body-md}` / `{rounded.md}` syntax.**
- **Every canonical decision from step 5 is reflected** — the documented value is the one the user picked, not a competing one.
- **The file describes the code, not an idealized version** — fonts and values match what's actually in the repo (advisories noted separately, not silently applied).
- **Contrast advisories computed** for every documented component pair and reported to the user (not necessarily fixed).
- **Readable end-to-end in 4–6 minutes.**

Deliver via a `computer://` link and a tight summary: one line per token group (colors, typography, spacing, shapes, components), one line on conflicts resolved (e.g., "9 conflicts consolidated"), and the advisory notes. Then point to the natural next step: run `studio-develop-design-review` in this repo to find every place the code still uses the now-non-canonical values, and use its paste-ready fix prompt to consolidate the codebase onto the documented tokens in one pass.

## Inconsistency patterns

How to detect and resolve each conflict type. Apply detection at step 4, resolution-recommendation at step 5.

### Near-duplicate colors

Multiple hex values within a small perceptual distance, all used for the same role. **Detect:** cluster colors by role and by closeness (e.g., values within ~ΔE 5, or that round to the same name). **Resolve:** recommend the most-used; break ties with the value defined in the central token source, then the Identity's temperature hint, then the one meeting AA. Document the chosen value; the others become drift.

### Token defined but bypassed

A CSS variable / theme token exists, but raw literals of (nearly) the same value appear directly in components. **Detect:** for each token, grep for its literal value used outside the token. **Resolve:** the token wins by definition — document it, and note the inline literals as drift to replace with the token reference.

### Off-grid spacing

An otherwise-clean base scale (4 or 8) polluted by stray values (`13px`, `18px`, `25px`). **Detect:** infer the base unit from the modal spacing values; flag anything not a clean multiple. **Resolve:** snap each off-grid value to the nearest scale step unless the user says it's intentional (e.g., an optical-alignment nudge).

### Multiple radii per component type

Cards (or buttons, or inputs) rounded at several different values. **Detect:** group radius values by the component type they're applied to. **Resolve:** one radius per component category; recommend the most-used, mapped to the nearest `rounded` scale level.

### Mixed units

The same property expressed in `rem`, `px`, and `em` across the codebase. **Detect:** per property, list the units in use. **Resolve:** pick the dominant unit for the documented token (note: the file records one canonical unit; the code can keep computing in others as long as the value matches).

### Font sprawl

More sans/serif families than the system needs, a weight set that doesn't form a scale, or an explosion of font sizes. **Detect:** list distinct families, weights, and sizes with counts. **Resolve:** collapse to a documented scale (6–10 type levels); recommend keeping the families that are actually loaded and most-used; flag any extra family as a candidate to drop (advisory, not a silent removal).

### Competing elevation models

Some surfaces use `box-shadow`, others use a hairline `border`, for the same elevation level. **Detect:** group elevation treatments by the elevation level they represent (resting card vs. floating menu). **Resolve:** recommend one model per level based on what dominates and what fits the product type; document it explicitly.

### Forked components

Two or more implementations of the same primitive (e.g., `Button` and `LegacyButton`) with divergent values. **Detect:** find duplicate primitives by name and by shape. **Resolve:** document one canonical definition (recommend the newer/more-used), and note the fork so review can reconcile usages.

### Dead tokens

Tokens defined but never referenced. **Detect:** tokens with zero usages. **Resolve:** low priority — mention them, but don't document unused tokens in the file unless the user wants them retained for a known upcoming use.

## Resolution heuristics

When recommending a canonical value, weigh these in order — but always present the recommendation and let the user decide; never resolve silently:

1. **Frequency.** The most-used value is the default canonical pick. Production usage is the strongest evidence of intent.
2. **Source authority.** A value defined in the central token source (Tailwind config, `:root`, theme file, token JSON) outranks scattered inline literals, even if the inline ones are individually more numerous.
3. **Location weight.** Values in shared / design-system / component-library folders outrank values in one-off pages or marketing routes.
4. **Identity tiebreaker.** Only when code evidence is genuinely tied: use `productos/design/1. Product Identity.md` (tone, visual style references) to break the tie. Never to override clear code evidence.
5. **Accessibility tiebreaker.** Among otherwise-equal candidates, prefer the one meeting WCAG AA. (Note: this is a *tiebreaker*, not a mandate to change a clear winner — AA failures of a clear winner are advisories in step 8.)
6. **Recency.** Newer code may reflect the current direction; use git history sparingly as a final tiebreaker, not a primary signal.

## Pacing and approval

- **Map the architecture before extracting.** Don't grep for hex until you know whether the source of truth is a Tailwind config, a theme file, or nothing.
- **Inventory before conflicts.** Capture reality fully — including the mess — before you start consolidating.
- **One conflict at a time.** Present the competing values, the counts, a recommendation, and the reason. Get a one-word confirm. Move on. Silent consolidation is how a documented system ends up not matching the code.
- **Document reality, don't redesign.** The only thing you actively resolve is internal inconsistency, and only with the user. Quality issues are advisories, not silent edits.
- **Two-pass review.** YAML tokens first, markdown prose second. Don't dump the whole file at once.
- **Strict to the spec.** Eight sections, fixed order, fixed YAML schema, `{token}` reference syntax. The Google format is normative.

## What "done" looks like

A `docs/DESIGN.md` file where:

- **YAML frontmatter** contains `version: alpha`, `name`, `description`, and populated `colors`, `typography`, `rounded`, `spacing`, and `components` — matching Google's schema exactly.
- **The documented values are the canonical ones the user chose** during conflict resolution — one value per role, no competing duplicates.
- **The file matches the code's reality** — real fonts, real palette, real scales — with quality concerns recorded as advisories *outside* the file rather than silently applied.
- **Markdown body** has all eight sections in the prescribed order, each a focused 2–4 paragraph explanation, with consolidation decisions briefly recorded.
- **Every component** in the YAML has prose in `Components`, and vice versa; **token references** use exact `{path.to.token}` syntax.
- **An advisory summary** was delivered in conversation: contrast pairs that fail AA, non-free/excluded fonts left in place, and anything aggressively collapsed.
- **The file is readable end-to-end in 4–6 minutes** by a human and parseable as YAML by a coding agent.

Recommended next step after a successful session: run `studio-develop-design-review` inside this same repo. It will compare the codebase against the freshly-documented `docs/DESIGN.md` and produce a prioritized, paste-ready fix prompt to migrate every non-canonical value (the "drift" you identified during conflict resolution) onto the documented tokens — turning the newly-written system into the one the code actually follows. From there, `studio-develop-design-better` will keep new UI on-system as it's built.
