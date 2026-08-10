# CLAUDE.md

<!-- BEGIN PRODUCTOS -->
## This repo runs on ProductOS

- The product strategy system lives in `productos/` — checklists, templates, and skills. The strategy docs are the source of intent; don't guess at product decisions the docs already answer.
- The programme plan is `docs/PLAN.md`, when present (adopted at setup by `studio-setup`) — consult it before starting any phase work.
- The canonical product documents live in `docs/` at the repo root (`PRODUCT.md`, `DESIGN.md`, `PRD.md`, `ROADMAP.md`, `LAUNCHES.md`, `SECURITY-AUDIT.md`, …). ProductOS skills write them; they may sit alongside the repo's own docs.
- Build-loop plan files are `docs/ROADMAP.md` and `docs/REFACTOR.md` — never `docs/PLAN.md` (the programme plan, no checkboxes) and never `productos/*-CHECKLIST.md`.
- Full system orientation: `productos/AGENTS.md`.
<!-- END PRODUCTOS -->

Behavioral guidelines to reduce common LLM coding mistakes. Merge with project-specific instructions as needed.

**Tradeoff:** These guidelines bias toward caution over speed. For trivial tasks, use judgment.

## 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

Before implementing:
- State your assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them - don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

## 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If you write 200 lines and it could be 50, rewrite it.

Ask yourself: "Would a senior engineer say this is overcomplicated?" If yes, simplify.

## 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

When editing existing code:
- Don't "improve" adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- If you notice unrelated dead code, mention it - don't delete it.

When your changes create orphans:
- Remove imports/variables/functions that YOUR changes made unused.
- Don't remove pre-existing dead code unless asked.

The test: Every changed line should trace directly to the user's request.

## 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

Transform tasks into verifiable goals:
- "Add validation" → "Write tests for invalid inputs, then make them pass"
- "Fix the bug" → "Write a test that reproduces it, then make it pass"
- "Refactor X" → "Ensure tests pass before and after"

For multi-step tasks, state a brief plan:
```
1. [Step] → verify: [check]
2. [Step] → verify: [check]
3. [Step] → verify: [check]
```

Strong success criteria let you loop independently. Weak criteria ("make it work") require constant clarification.

## 5. Design Fidelity

**The design system is law. Reference `docs/DESIGN.md` for every frontend change.**

Before writing or changing any UI code:
- Read the relevant sections of `docs/DESIGN.md` — token YAML and component specs.
- Every color, font, size, spacing, and radius comes from a token. Never hardcode visual values.
- Reuse existing components before creating new ones. New components are built from the tokens.
- If a design need isn't covered by `docs/DESIGN.md`, flag the gap and ask - don't invent styling.

## 6. Secure by Default

**Insecure code that works is not done. These are not optional.**

- Never hardcode or commit secrets — environment variables only, and never behind a public prefix (`NEXT_PUBLIC_*`, `VITE_*`, `EXPO_PUBLIC_*` ship to every browser).
- Authorization lives server-side: check *ownership* of the resource, not just that someone is logged in. Client-side checks are UX, not security.
- Every database table gets access rules from day one — RLS policies scoped to the user in Supabase, auth-required rules in Firebase. A table without rules is public.
- Parameterized queries only — never build SQL from user input.
- Verify webhook signatures (Stripe, Clerk, GitHub) before trusting the payload.
- `service_role` and `sk_live_` keys never reach the client. The anon key / `pk_live_` are public by design — that's fine *because* the rules above hold.

---

**These guidelines are working if:** fewer unnecessary changes in diffs, fewer rewrites due to overcomplication, clarifying questions come before implementation rather than after mistakes, and no hardcoded style values appear in any diff.
