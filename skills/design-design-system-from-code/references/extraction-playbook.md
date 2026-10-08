# Extraction playbook

Where design decisions hide in a codebase, how each kind of internal inconsistency shows up, and how to recommend a canonical value. Read the section named in each workflow step.

## Styling architectures (step 2)

Identify every approach in use — there are often several layered together:

- **Tailwind:** `tailwind.config.{js,ts,cjs,mjs}` — read `theme` and `theme.extend` (colors, fontFamily, fontSize, spacing, borderRadius, boxShadow). Then grep for arbitrary values (`bg-[#...]`, `p-[13px]`, `rounded-[14px]`) which are the off-system escapes.
- **CSS custom properties:** `:root { --color-...: ... }` in global CSS, plus any `[data-theme]` / `.dark` overrides. Then grep for raw hex / px used directly instead of the variables.
- **CSS-in-JS:** styled-components / emotion / vanilla-extract — theme objects (`theme.colors.*`), `styled.button\`...\``, and inline `style={{ }}` props.
- **Design-token files:** `tokens.json` (Style Dictionary / W3C DTCG), `theme.ts`, `tokens.ts`, `colors.ts`, `typography.ts`, `design-tokens/*`.
- **Component-library theme overrides:** MUI `createTheme`, Chakra `extendTheme`, Mantine theme, shadcn `globals.css` variables.
- **Native:** SwiftUI `Color`/`Font` extensions and asset catalogs; Android `colors.xml` / `themes.xml` / Compose `Theme.kt`; Flutter `ThemeData`.
- **Raw / scattered:** SCSS `$variables`, plain CSS, and the hardest case — values hardcoded inline throughout components with no central source.

## Inconsistency patterns (step 4 detection, step 5 recommendation)

### Near-duplicate colors

Multiple hex values within a small perceptual distance, all used for the same role. **Detect:** cluster colors by role and by closeness (e.g., values within ~ΔE 5, or that round to the same name). **Resolve:** recommend the most-used; break ties with the value defined in the central token source, then the Identity's temperature hint, then the one meeting AA. Document the chosen value; the others become drift.

### Token defined but bypassed

A CSS variable / theme token exists, but raw literals of (nearly) the same value appear directly in components. **Detect:** for each token, grep for its literal value used outside the token. **Resolve:** the token wins by definition — document it, and note the inline literals as drift to replace with the token reference.

### Off-grid spacing

An otherwise-clean base scale (4 or 8) polluted by stray values (`13px`, `18px`, `25px`). **Detect:** infer the base unit from the modal spacing values; flag anything not a clean multiple. **Resolve:** snap each off-grid value to the nearest scale step unless the member says it's intentional (e.g., an optical-alignment nudge).

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

Tokens defined but never referenced. **Detect:** tokens with zero usages. **Resolve:** low priority — mention them, but don't document unused tokens in the file unless the member wants them retained for a known upcoming use.

## Resolution heuristics (step 5)

When recommending a canonical value, weigh these in order — but always present the recommendation and let the member decide; never resolve silently:

1. **Frequency.** The most-used value is the default canonical pick. Production usage is the strongest evidence of intent.
2. **Source authority.** A value defined in the central token source (Tailwind config, `:root`, theme file, token JSON) outranks scattered inline literals, even if the inline ones are individually more numerous.
3. **Location weight.** Values in shared / design-system / component-library folders outrank values in one-off pages or marketing routes.
4. **Identity tiebreaker.** Only when code evidence is genuinely tied: use the Product Identity section of `docs/DESIGN.md` (tone, visual style references) to break the tie. Never to override clear code evidence.
5. **Accessibility tiebreaker.** Among otherwise-equal candidates, prefer the one meeting WCAG AA. (A *tiebreaker*, not a mandate to change a clear winner — AA failures of a clear winner are advisories in step 8 of the skill.)
6. **Recency.** Newer code may reflect the current direction; use git history sparingly as a final tiebreaker, not a primary signal.
