# Develop — Checklist

Work top to bottom — or ask your agent to *"start develop"*: `develop-phase` sets your route from your product's shape and walks it with you. Requires `docs/DEFINE.md` and `docs/DESIGN.md` to exist (run the Define and Design phases first — or their fast-tracks: `define-from-code` for DEFINE.md, `design-design-system-from-code` for DESIGN.md; a Lite DESIGN.md is enough where your shape allows). Steps 0–3 take you from spec to a working MVP; steps 4–7 are the ongoing build rhythm; step 8 is the security gate; step 9 puts the product in front of customers.

**Your shape decides what each step means.** Your shape file (`productos/shapes/<slug>.md`) marks which steps apply, what the PRD must cover — an agent skill's PRD specifies its SKILL.md, triggers, and eval set; an MCP server's specifies its tools and auth; a productized service's specifies its delivery process — and what "go live" means: a deploy, a store submission, a marketplace publish, a package release, a booking page, or a storefront.

If `docs/PLAN.md` exists (your programme plan, from your coach or `product-audit`), it names your route through this phase (build from scratch, rework an existing codebase, or straight to the build loop) and may mark steps as fast-tracked or skipped — follow it; this checklist remains the source of truth for how each step runs.

Running a challenge (`docs/SHIP-IN-7.md` or `docs/SELL-IN-30.md` open)? It says which of these steps are this week's, and on which session; this checklist remains the source of truth for how each step runs.

---

## Step 0 — Migrate *(apps on a prompt-to-app platform only)*

- **What to do:** Coming from Lovable, Bolt, v0, Base44, Replit, or similar? Run `develop-migrate` before anything else.
- **What it does:** Inventories everything the platform manages, moves the app into your own repo, stack, and deployment via `docs/MIGRATION.md`, and gates decommissioning the old platform behind a full verification pass. Run `build-loop` on `docs/MIGRATION.md` to execute it. Plan the rest of the build (Step 1) once you fully own the codebase.

## Step 1 — PRD & Roadmap

- **What to do:** Run `develop-prd-roadmap`.
- **Already have a codebase?** The same skill runs in existing-codebase mode: it protects your working code with a baseline branch and tag, writes the target PRD, audits your code against it, walks you through every keep-or-remove decision, and writes `docs/ROADMAP.md` as the gap between the code and the spec. (This replaces the old refactor plan — there's no separate `docs/REFACTOR.md`.)
- **No `docs/DEFINE.md` yet?** Run the Define fast-track first — `define-from-code` extracts the Define work from your existing product into `docs/DEFINE.md`.
- **What it does:** Scopes your MVP through a structured interview (core loop, feature cuts, tech stack), then produces `docs/PRD.md` — the technical spec a coding agent builds from, covering your shape's sections — and `docs/ROADMAP.md` — the phased build plan with task checkboxes. Draws on `productos/develop/guides/PRD-GENERATION.md`, `ROADMAP-GENERATION.md`, and `TECH-STACK-OPTIONS.md`.

## Step 1b — Evals *(agent skills, plugins, MCP servers, chat assistants, and any product whose core is an AI output)*

- **What to do:** Run `develop-agent-evals` before the build.
- **What it does:** Produces `docs/EVALS.md` — at least three scenarios per core job, each with the request, the inputs, and the expected behaviour as a checkable rubric, plus a baseline without your product and runs across the models your customers use. It's the bar "done" is measured against: the build isn't finished until the evals pass.

## Step 2 — Verify your setup

- **What to do:** Nothing to create or copy — ProductOS already lives inside your app repo, and the specs are already at `docs/`. Just confirm the root `CLAUDE.md`/`AGENTS.md` carry the ProductOS guidelines (wired from `productos/setup/` at setup; if they're missing, `setup` fixes it in seconds).
- **Also recommended:** Push the repo to GitHub so your work is backed up and versioned. The agent builds straight through all phases in one go — there's no need to gate each phase behind a pull request. Code review is built in: `develop-build` reviews at every phase boundary, and `build-loop` reviews once its work is finished — no separate service needed.

## Step 3 — Build the MVP

- **What to do:** Run `develop-build`.
- **What it does:** Works through every roadmap task in order — implementing, testing, and verifying each before moving on, with a code review and a commit at every phase boundary — until all tasks are checked off and the magic moment works end to end. On an existing codebase it works the gap roadmap the same way, keeping the app runnable after every phase, and resets to the last phase commit rather than leave the main branch broken. *(A `docs/REFACTOR.md` from an older version of ProductOS still runs the same way.)*

## Step 4 — Build new features with the build loop

- **What to do:** For every feature you add after the MVP, run `build-loop` — it works in Claude Code, Codex, and Cursor, and uses your tool's own review.
- **What it does:** Forces each task through build → end-to-end testing → fixes, then reviews the finished work (`/review`) before it counts as done — so quality doesn't drift as the app grows.
- **Not sure what to build next?** Run `develop-feature-finder` with a business goal (retention, activation, conversion, revenue) — it reviews your codebase, researches what comparable products do, and delivers ranked feature recommendations you can feed straight into the build loop.

## Step 5 — Code review for work outside the build skills

- **What to do:** Run `develop-code-review` on uncommitted changes you made outside the build loop or a full build (a hand edit, a quick fix). Work from `develop-build` or `build-loop` has already been reviewed.
- **What it does:** Reviews the whole uncommitted diff (including new untracked files) for correctness, regressions, edge cases, and leftover debug code, verifies every finding against the actual source, and ends with an explicit verdict: ready to commit, or the must-fix list first.

## Step 6 — Design changes *(screen shapes)*

- **What to do:** Run `develop-design-better` whenever you're generating or changing UI, and `develop-design-review` before committing design work.
- **What it does:** Keeps every screen aligned with `docs/DESIGN.md` tokens — and, when `docs/COPY.md` exists, every user-facing string aligned with it — catching visual and copy drift before it ships.

## Step 7 — Conversion review

- **What to do:** Run `develop-cro-audit` once the product is usable end to end (and again once it has real traffic). It applies wherever there's a signup, pricing, or checkout surface — including the landing page of a shape without screens.
- **What it does:** Reviews your app against conversion best practices — onboarding friction, activation drop-off, pricing page, CTAs — and produces prioritized improvements.

## Step 8 — Security audit ★ *before you go live*

- **What to do:** Run `develop-security-audit` before Step 9 — and again after any significant auth, payments, or data-access work. Agent plugins, skills, MCP servers, and chat assistants also get its agent-tools tier (prompt injection, tool permissions, secrets in configs). Services, websites, and digital products need it only where there's custom code or customer data. Do the report's "Do this right now" and Human-only actions yourself; hand the Fix plan to your coding agent.
- **What it does:** Audits the codebase in the order that actually burns founder apps — committed secrets, database access control (RLS), unprotected routes, ownership checks, keys exposed to the browser — verifies every finding to a concrete exploit path, and produces `docs/SECURITY-AUDIT.md`: a one-line verdict plus a severity-ordered checkbox fix plan your agent can execute while you keep building.

## Step 9 — Go live

- **What to do:** Run `develop-golive` when you're ready to go live.
- **What it does:** Produces `docs/DEPLOY.md` — a plain-English, step-by-step go-live guide in your shape's form (deploy, store submission, marketplace publish, package release, booking page, or storefront), where every step is marked 🧑 you / 🤖 agent / 🤝 together. Work through it top to bottom; you're live when your shape's *Live means* bar passes as a real customer.

---

## Next phase

Once customers can reach the product, move to the Distribute phase: ask your agent to *"start distribute"* (`distribute-phase`), or open `productos/distribute/DISTRIBUTE-CHECKLIST.md`.
