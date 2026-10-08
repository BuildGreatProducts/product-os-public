# Image analysis and calibration patterns

Read at Step 1 (image analysis) to map what you see onto tokens, and at Step 3 when the reference needs an anchor shape.

## Colour extraction

- Dominant background → likely `surface` (or `neutral`). Dominant text → `on-surface`.
- The single non-neutral colour that draws the eye → the accent. If there are two strong accents, ask which is hero.
- Muted/secondary text → `on-surface-variant`. Multi-tone neutrals → `surface-container`, `surface-container-high`.
- Flag colours that may be rendering artifacts rather than intentional palette.

## Typography extraction

- Largest text → `display` or `headline-lg`. Body text → `body-md`. Small all-caps → `label-sm`.
- A serif in the reference is almost certainly for headlines, not body. Two distinct typefaces → the system is a pair.

## Spacing, elevation, shape extraction

- Smallest consistent gap → `xs`/`sm`; gap between unrelated blocks → `lg`/`xl`; button padding usually 12–16px vertical, 16–24px horizontal.
- Soft large shadows → shadow elevation; backdrop-blur → glass; stacked tints → tonal layering; 1px hairlines → border elevation; colour-contrast only → flat.
- 0–2px corners → architectural/brutalist; 4–8px → modern professional; 12–16px → consumer/friendly; 24px+ → playful; pills on small interactive elements → contemporary consumer.

## Calibration shapes

When the reference needs an anchor, draw on these recognized shapes:

- **Editorial Calm.** Warm neutrals + serif/sans pair + hairline borders + paper-on-paper. Fits calm-authority, editorial brands. (See `REFERENCE-DESIGN.md` in this skill's folder.)
- **Atmospheric Glass.** Dark surface + vibrant gradient + backdrop-blur cards. Fits dramatic, transformative brands.
- **Dashboard Precision.** Cool neutrals + geometric sans + sharp 2–4px corners + flat tonal layering. Linear/Vercel-shape.
- **Notion-Adjacent Friendly.** Warm whites + humanist sans + medium rounding + soft hairlines. Warm tool-for-thinking brands.
- **Brutalist Editorial.** High-contrast monochrome + serif display + sharp corners + heavy weights. Defiant or authority-led brands.
