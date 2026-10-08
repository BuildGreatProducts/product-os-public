# Develop — Checklist

Work top to bottom. Requires `docs/DEFINE.md` and `docs/DESIGN.md` to exist (run the Define and Design phases first — or their fast-tracks: `define-from-code` for DEFINE.md, `design-design-system-from-code` for DESIGN.md). Steps 1–3 take you from spec to working MVP; steps 4–7 are the ongoing build rhythm; step 8 is the security gate; step 9 puts the product in front of customers.

If `docs/PLAN.md` exists (your programme plan, shipped with coached copies of ProductOS), it names your route through this phase (build from scratch, refactor, or straight to the build loop) and may mark steps as fast-tracked or skipped — follow it; this checklist remains the source of truth for how each step runs.

Running a challenge (`docs/SHIP-IN-7.md` or `docs/SELL-IN-30.md` open)? It says which of these steps are this week's, and on which session; this checklist remains the source of truth for how each step runs.

---

## Step 1 — PRD & Roadmap

- **What to do:** Run `develop-prd-roadmap`.
- **Refactoring an existing codebase (path 3b)?** This step is optional — `develop-refactor-plan` generates its own refactor-scoped PRD when `docs/PRD.md` doesn't exist, so you can go straight to Step 3b.
- **No `docs/DEFINE.md` yet?** Run the Define fast-track first — `define-from-code` extracts the Define work from your existing product into `docs/DEFINE.md`.
- **What it does:** Scopes your MVP through a structured interview (core loop, feature cuts, tech stack), then produces `docs/PRD.md` — the technical spec a coding agent builds from — and `docs/ROADMAP.md` — the phased build plan with task checkboxes. Draws on `productos/develop/guides/PRD-GENERATION.md`, `ROADMAP-GENERATION.md`, and `TECH-STACK-OPTIONS.md`.

## Step 2 — Verify your setup

- **What to do:** Nothing to create or copy — ProductOS already lives inside your app repo, and the specs are already at `docs/`. Just confirm the root `CLAUDE.md`/`AGENTS.md` carry the ProductOS guidelines (wired from `productos/setup/` at setup; if they're missing, `setup` fixes it in seconds).
- **Also recommended:** Push the repo to GitHub so your work is backed up and versioned. The agent builds straight through all phases in one go — there's no need to gate each phase behind a pull request. Code review is built in: `develop-build` reviews at every phase boundary, and `build-loop` reviews once its work is finished — no separate service needed.

## Step 3 — Build the MVP

Pick the path that matches your situation:

### 3a — Building from scratch

- **What to do:** Run `develop-build`.
- **What it does:** Works through every roadmap task in order — implementing, testing, and verifying each before moving on, with a code review and a commit at every phase boundary — until all tasks are checked off and the magic moment works end to end.

### 3b — Refactoring an existing codebase

- **What to do:** First protect your working code — work in a git worktree or duplicate the codebase folder before refactoring, so you can always get back to a working version. Then run `develop-refactor-plan`, review each difference it finds with you, and once `docs/REFACTOR.md` exists, run `develop-build`.
- **Coming from a prompt-to-app platform (Lovable, Bolt, v0, Base44)?** Run `develop-migrate` first — it inventories everything the platform manages, moves the app into your own repo, stack, and deployment via `docs/MIGRATION.md`, and gates decommissioning the old platform behind a full verification pass. Refactor after you fully own the codebase.
- **What it does:** The plan skill audits your code against the PRD (generating a refactor-scoped PRD first if `docs/PRD.md` doesn't exist) and turns your keep/remove decisions into `docs/REFACTOR.md`; the build skill executes it task by task until the codebase matches the PRD.
- **No `docs/DESIGN.md` yet?** Run `design-design-system-from-code` first — it reverse-engineers the design system already in your code into `docs/DESIGN.md`, so the refactor has real design tokens to converge on.

## Step 4 — Build new features with the build loop

- **What to do:** For every feature you add after the MVP, run `build-loop` — it works in Claude Code, Codex, and Cursor, and uses your tool's own review.
- **What it does:** Forces each task through build → end-to-end testing → fixes, then reviews the finished work (`/review`) before it counts as done — so quality doesn't drift as the app grows.
- **Not sure what to build next?** Run `develop-feature-finder` with a business goal (retention, activation, conversion, revenue) — it reviews your codebase, researches what comparable products do, and delivers ranked feature recommendations you can feed straight into the build loop.

## Step 5 — Code review for work outside the build skills

- **What to do:** Run `develop-code-review` on uncommitted changes you made outside the build loop or a full build (a hand edit, a quick fix). Work from `develop-build` or `build-loop` has already been reviewed.
- **What it does:** Reviews the whole uncommitted diff (including new untracked files) for correctness, regressions, edge cases, and leftover debug code, verifies every finding against the actual source, and ends with an explicit verdict: ready to commit, or the must-fix list first.

## Step 6 — Design changes

- **What to do:** Run `develop-design-better` whenever you're generating or changing UI, and `develop-design-review` before committing design work.
- **What it does:** Keeps every screen aligned with `docs/DESIGN.md` tokens — and, when `docs/COPY.md` exists, every user-facing string aligned with it — catching visual and copy drift before it ships.

## Step 7 — Conversion review

- **What to do:** Run `develop-cro-audit` once the product is usable end to end (and again once it has real traffic).
- **What it does:** Reviews your app against conversion best practices — onboarding friction, activation drop-off, pricing page, CTAs — and produces prioritized improvements.

## Step 8 — Security audit ★ *before you go live*

- **What to do:** Run `develop-security-audit` before Step 9 — and again after any significant auth, payments, or data-access work. Do the report's "Do this right now" and Human-only actions yourself; hand the Fix plan to your coding agent.
- **What it does:** Audits the codebase in the order that actually burns founder apps — committed secrets, database access control (RLS), unprotected routes, ownership checks, keys exposed to the browser — verifies every finding to a concrete exploit path, and produces `docs/SECURITY-AUDIT.md`: a one-line verdict plus a severity-ordered checkbox fix plan your agent can execute while you keep building.

## Step 9 — Deploy to customers

- **What to do:** Run `develop-golive` when you're ready to go live.
- **What it does:** Audits the codebase and produces `docs/DEPLOY.md` — a plain-English, step-by-step launch guide where every step is marked 🧑 you / 🤖 agent / 🤝 together. Work through it top to bottom; you're live when the final smoke test passes as a real customer.

---

## Next phase

Once customers can reach the product, move to the Distribute phase. Open `productos/distribute/DISTRIBUTE-CHECKLIST.md`.
