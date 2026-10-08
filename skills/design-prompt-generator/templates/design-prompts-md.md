# DESIGN-PROMPTS.md template

The structure written to `docs/DESIGN-PROMPTS.md` at Step 6. Wrap each prompt in a triple-backtick code block so it copies cleanly without surrounding markdown.

````markdown
# Design Prompts

*Drafted: [Month Year]. Generated from `docs/DEFINE.md`, `docs/DESIGN.md` (Product Identity + tokens), and `docs/COPY.md` where present. Paste each prompt into your AI design tool — the brand context and tokens are already in the prompt.*

## How to use this file

1. Open your AI design tool ([the tool the member chose — MagicPath by default]).
2. **Start with Prompt 1 (the design system).** It renders your `docs/DESIGN.md` tokens as a component library — the foundation the next two screens are built on.
3. Copy the entire prompt — from "Design a..." through the last line.
4. Paste into the tool. The brand identity and tokens are embedded in every prompt.
5. Run Prompts 2 and 3 against the same canvas so the screens reuse Prompt 1's components; iterate on layout, hierarchy, or content as needed.
6. `docs/DESIGN.md` stays the source of truth for exact tokens — if it changes, re-run `design-prompt-generator`.

---

## Brand identity context (embedded in every prompt below)

[The compressed 6–10 line brand context block from step 3, shown once so the member can see what's passed to each prompt.]

---

## Prompt 1: Design system foundation

**Purpose:** Render the full UI component library from the DESIGN.md tokens — Prompts 2 and 3 reuse it. Run this first.

### Prompt — paste this into your AI design tool

```
[The complete paste-ready design system prompt from step 4]
```

---

## Prompt 2: [Screen Name]

**Purpose:** [one sentence]
**Position in journey:** [pre-signup / first session / day 1 / etc.]

### Prompt — paste this into your AI design tool

```
[The complete paste-ready screen prompt — includes the "Reuse the components from Prompt 1" line]
```

---

## Prompt 3: [Screen Name]

**Purpose:** [one sentence]
**Position in journey:** [...]

### Prompt — paste this into your AI design tool

```
[The complete paste-ready screen prompt — includes the "Reuse the components from Prompt 1" line]
```

---

## Sources

- Product context: `docs/DEFINE.md`
- Brand strategy: `docs/DESIGN.md` → Product Identity
- Design tokens: `docs/DESIGN.md`
- Copy rules: `docs/COPY.md` (if present)
````
