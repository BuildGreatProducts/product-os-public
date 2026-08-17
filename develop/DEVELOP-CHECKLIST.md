# Develop — Checklist

Work top to bottom. Requires `docs/PRODUCT.md` and `docs/DESIGN.md` to exist (run the Define and Design phases first — or their fast-tracks: `studio-define-from-code` for PRODUCT.md's inputs, `studio-design-design-system-from-code` for DESIGN.md). Steps 1–3 take you from spec to working MVP; step 4 puts that MVP in your believers' hands; steps 5–8 are the ongoing build rhythm; step 9 is the security gate; step 10 puts the product in front of customers.

If `docs/PLAN.md` exists (your programme plan, shipped with coached copies of ProductOS), it names your route through this phase (build from scratch, refactor, or straight to the build loop) and may mark steps as fast-tracked or skipped — follow it; this checklist remains the source of truth for how each step runs.

---

## Step 1 — PRD & Roadmap

- **What to do:** Run `studio-develop-prd-roadmap`.
- **Refactoring an existing codebase (path 3b)?** This step is optional — `studio-develop-refactor-plan` generates its own refactor-scoped PRD when `docs/PRD.md` doesn't exist, so you can go straight to Step 3b.
- **No `docs/PRODUCT.md` yet?** Run the Define fast-track first — `studio-define-from-code` extracts the Define documents from your existing product, then `studio-define-product` synthesises PRODUCT.md.
- **What it does:** Scopes your MVP through a structured interview (core loop, feature cuts, tech stack), then produces `docs/PRD.md` — the technical spec a coding agent builds from — and `docs/ROADMAP.md` — the phased build plan with task checkboxes. Draws on `productos/develop/guides/PRD-GENERATION.md`, `ROADMAP-GENERATION.md`, and `TECH-STACK-OPTIONS.md`.

## Step 2 — Verify your setup

- **What to do:** Nothing to create or copy — ProductOS already lives inside your app repo, and the specs are already at `docs/`. Just confirm the root `CLAUDE.md`/`AGENTS.md` carry the ProductOS guidelines (wired from `productos/setup/` at setup; if they're missing, `studio-setup` fixes it in seconds).
- **Also recommended:** Push the repo to GitHub so your work is backed up and versioned. The agent builds straight through all phases in one go — there's no need to gate each phase behind a pull request. For code review, the build loop runs your coding agent's built-in review per task, and Step 6's `studio-develop-code-review` is the deliberate pass before each commit — no separate service needed.

## Step 3 — Build the MVP

Pick the path that matches your situation:

### 3a — Building from scratch

- **What to do:** Run `studio-develop-mvp-build`.
- **What it does:** Works through every roadmap task in order — implementing, testing, and verifying each before moving on — until all tasks are checked off and the magic moment works end to end.

### 3b — Refactoring an existing codebase

- **What to do:** First protect your working code — work in a git worktree or duplicate the codebase folder before refactoring, so you can always get back to a working version. Then run `studio-develop-refactor-plan`, review each difference it finds with you, and once `docs/REFACTOR.md` exists, run `studio-develop-refactor-build`.
- **Coming from a prompt-to-app platform (Lovable, Bolt, v0, Base44)?** Run `studio-develop-migrate` first — it inventories everything the platform manages, moves the app into your own repo, stack, and deployment via `docs/MIGRATION.md`, and gates decommissioning the old platform behind a full verification pass. Refactor after you fully own the codebase.
- **What it does:** The plan skill audits your code against the PRD (generating a refactor-scoped PRD first if `docs/PRD.md` doesn't exist) and turns your keep/remove decisions into `docs/REFACTOR.md`; the build skill executes it task by task until the codebase matches the PRD.
- **No `docs/DESIGN.md` yet?** Run `studio-design-design-system-from-code` first — it reverse-engineers the design system already in your code into `docs/DESIGN.md`, so the refactor has real design tokens to converge on.

## Step 4 — Relaunch: the beta invite

- **What to do:** As soon as the magic moment works end to end, run `studio-launch`. Same ritual: ship within 48 hours, share a screenshot of the live message with your cohort or accountability partner, log every response in `docs/LAUNCHES.md`.
- **What it does:** Puts the working MVP in your believers' hands — a personal invite to everyone who replied or signed up at the earlier launches, then an update on the same public thread. **The win is one activated user** — a real person reaching the magic moment (`productos/design/2-Magic-Moment.md`). Their first-session feedback is the best feature-finder you'll ever get; feed it into Step 5.

## Step 5 — Build new features with the build loop

- **What to do:** For every feature you add after the MVP, run the build-loop skill matching your tool: `cursor-build-loop`, `claude-code-build-loop`, or `codex-build-loop`.
- **What it does:** Forces each feature through build → in-flight review (`/review`) → end-to-end testing → fixes before it counts as done — so quality doesn't drift as the app grows. When the feature is finished, Step 6 is the deliberate pre-commit pass.
- **Not sure what to build next?** Run `studio-develop-feature-finder` with a business goal (retention, activation, conversion, revenue) — it reviews your codebase, researches what comparable products do, and delivers ranked feature recommendations you can feed straight into the build loop.

## Step 6 — Code review before commit

- **What to do:** Run `studio-develop-code-review` whenever you have uncommitted changes that are about to become a commit — the step back after the build loop's in-flight reviews.
- **What it does:** Reviews the whole uncommitted diff (including new untracked files) for correctness, regressions, edge cases, and leftover debug code, verifies every finding against the actual source, and ends with an explicit verdict: ready to commit, or the must-fix list first.

## Step 7 — Design changes

- **What to do:** Run `studio-develop-design-better` whenever you're generating or changing UI, and `studio-develop-design-review` before committing design work.
- **What it does:** Keeps every screen aligned with `docs/DESIGN.md` tokens and catches visual drift before it ships.

## Step 8 — Conversion review

- **What to do:** Run `studio-develop-cro-audit` once the product is usable end to end (and again once it has real traffic).
- **What it does:** Reviews your app against conversion best practices — onboarding friction, activation drop-off, pricing page, CTAs — and produces prioritized improvements.

## Step 9 — Security audit ★ *before you go live*

- **What to do:** Run `studio-develop-security-audit` before Step 10 — and again after any significant auth, payments, or data-access work. Do the report's "Do this right now" and Human-only actions yourself; hand the Fix plan to your coding agent.
- **What it does:** Audits the codebase in the order that actually burns founder apps — committed secrets, database access control (RLS), unprotected routes, ownership checks, keys exposed to the browser — verifies every finding to a concrete exploit path, and produces `docs/SECURITY-AUDIT.md`: a one-line verdict plus a severity-ordered checkbox fix plan your agent can execute while you keep building.

## Step 10 — Deploy to customers

- **What to do:** Run `studio-develop-golive` when you're ready to go live.
- **What it does:** Audits the codebase and produces `docs/DEPLOY.md` — a plain-English, step-by-step launch guide where every step is marked 🧑 you / 🤖 agent / 🤝 together. Work through it top to bottom; you're live when the final smoke test passes as a real customer.

---

## Next phase

Once customers can reach the product, move to the Distribute phase. Open `productos/distribute/DISTRIBUTE-CHECKLIST.md`.
