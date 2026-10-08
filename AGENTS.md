# ProductOS

ProductOS is a complete operating system for taking a product from idea to revenue with AI agents. It lives in the `productos/` folder of the app repository it serves — the surrounding repo **is** the product codebase, and ProductOS is set up in it before anything else, even the first line of code. It works in four phases, each with its own folder, checklist, templates, and skills:

1. **Define** (`productos/define/`) — nail the offer, customer, and pricing. Every Define skill writes its own section of one document, `docs/DEFINE.md`.
2. **Design** (`productos/design/`) — identity (the brand in words, written into `docs/DESIGN.md`), then the UX writing guide (`docs/COPY.md` — how the product speaks), then the design system derived from an image reference (the tokens in `docs/DESIGN.md` + its live `docs/DESIGN.html` style guide), design prompts, magic moment, onboarding, acquisition surface.
3. **Develop** (`productos/develop/`) — PRD, roadmap, the agent-driven build with code-review and security gates, go-live. Produces `docs/PRD.md`, `docs/ROADMAP.md`, `docs/SECURITY-AUDIT.md`, and `docs/DEPLOY.md`.
4. **Distribute** (`productos/distribute/`) — go-to-market, growth experiments, scaling. A loop, not a one-pass sequence. Produces `docs/GO-TO-MARKET.md`, `docs/GROWTH-EXPERIMENTS.md`, `docs/GROWTH-TRACKER.md`, and `docs/SCALE.md`.

One rule runs through all four phases: **`docs/` is the source of truth for everything ProductOS produces.** Every skill that produces a document writes it to `docs/` at the repo root; nothing a skill produces stays inside `productos/`.

## Where to start

Run `setup` — the installer. It verifies ProductOS is properly installed (sitting as `productos/` inside a git repo, root `CLAUDE.md`/`AGENTS.md` wired from `productos/setup/`, `productos/` gitignored), fixes what's missing, and — if the copy shipped with a programme plan at `productos/PLAN.md` — moves it to `docs/PLAN.md` and verifies it against the actual repo. Custom plans are composed by the user's coach from their onboarding call; plan revisions come from the coach too.

If ProductOS is checked out standalone (no surrounding app repo), run `setup` anyway — it walks the user through creating the app repo and moving ProductOS into it as `productos/`.

No plan in the copy? Setup offers two paths. A **new project** (nothing built yet) starts with `define-offer-builder`, Step 1 of `productos/define/DEFINE-CHECKLIST.md`, and works top to bottom, finishing each phase before the next — the standard programme. An **existing project** (app code, a prototype, an AI-generated app) starts `ship-in-7`, which gets it live at a real URL in seven sessions; `sell-in-30` follows once it's live. Each phase checklist names the exact skill to run at each step, the file it produces, and the reference docs it draws on.

## How this folder is organized

- `productos/define/`, `productos/design/`, `productos/develop/`, `productos/distribute/` — one folder per phase: a `*-CHECKLIST.md` runbook, numbered worksheets (`1-`–`4-`) that give each output its structure and `> Good/Bad` guidance, and `BONUS-*.md` reference playbooks.
- `productos/skills/<skill-name>/` — the Claude skills the checklists invoke, one flat folder per skill containing a `SKILL.md` (plus any bundled reference files). Names use the `<phase>-*` convention (e.g. `define-offer-builder`); the three tool-specific build loops (`cc-build-loop`, `codex-build-loop`, `cursor-build-loop`) carry their tool's name instead so they work outside ProductOS, and the four cross-phase skills are `setup` (the installer — it opens every programme), `update` (the updater — it moves an installed copy to the latest release), and the two challenges `ship-in-7` (seven sessions to a live app) and `sell-in-30` (thirty sessions to a first customer) — orchestrators that compose a session-by-session plan from the phase skills and log it in `docs/SHIP-IN-7.md` / `docs/SELL-IN-30.md`; no phase prefix on any of the four.
- `productos/setup/` — the coding-agent guidelines (`CLAUDE.md`, `AGENTS.md`) that get wired into the app repo root at setup: copied whole if no root file exists, or appended as a marked `<!-- BEGIN PRODUCTOS -->…<!-- END PRODUCTOS -->` block if one does — never overwrite a repo's existing root files.
- `docs/` — the output directory at the **app repo root** (not inside `productos/`). ProductOS skills write every output there, alongside whatever documentation the repo already has:
  - **Programme:** `PLAN.md`, and the challenge logs `SHIP-IN-7.md` / `SELL-IN-30.md`.
  - **Define:** `DEFINE.md` (Summary, Product Offer, Customer Persona, Pricing Strategy, and the optional Business Strategy and Idea Audit sections).
  - **Design:** `DESIGN.md` + `DESIGN.html` (Product Identity, then the design-system tokens), `COPY.md`, `DESIGN-PROMPTS.md`, `MAGIC-MOMENT.md`, `ONBOARDING.md` + `ONBOARDING-WIREFRAME.html`, `LANDING-PAGE.md` + `LANDING-PAGE-WIREFRAME.html` and/or `APP-LISTING.md`.
  - **Develop:** `PRD.md`, `ROADMAP.md`, `REFACTOR.md`, `MIGRATION.md`, `SECURITY-AUDIT.md`, `DEPLOY.md`, `CRO-AUDIT.md`, and `design-reviews/`.
  - **Distribute:** `GO-TO-MARKET.md`, `GROWTH-EXPERIMENTS.md`, `GROWTH-TRACKER.md`, `SCALE.md`, `ACTIVATION-RETENTION-AUDIT.md`.

  Don't hand-create the canonical files; other files in `docs/` are the app's own — leave them alone.

## Rules for agents working in this folder

- Outputs go to `docs/`, never into `productos/`. The numbered templates in the phase folders are **worksheets**: read them for structure and the `> Good/Bad` calibration, write the answers to the skill's `docs/` file, and leave the worksheet blank. A skill that writes part of a shared document (`DEFINE.md`, the Product Identity section of `DESIGN.md`) writes only its own section.
- Repos set up before ProductOS 1.14.0 may still have `docs/PRODUCT.md` and filled templates inside `productos/`. Don't build on them silently — run `update`, which moves their content into the `docs/` files above.
- If `docs/PLAN.md` exists, consult it before opening any checklist — it says which steps are Full, Fast-tracked, Skipped, or Already-done for this user, and in what order. The plan governs *which steps apply*; the checklists remain the source of truth for *how each step runs*. If it doesn't exist, follow the checklists linearly from Define — custom plans ship with coached copies of ProductOS.
- Respect the dependency chain: if an upstream file (e.g. `docs/DEFINE.md`) is missing, run the skill that produces it — or the fast-track producer the plan names (`define-from-code` for the Define documents, `design-design-system-from-code` for the design system) — rather than improvising content; if no product idea exists at all, `define-idea-finder` finds one first.
- The surrounding repo is the product codebase — build-phase skills operate on it directly. Build-loop plan files are `docs/ROADMAP.md`, `docs/REFACTOR.md`, and `docs/MIGRATION.md` (plus the Fix plan in `docs/SECURITY-AUDIT.md` when asked for security fixes); `docs/PLAN.md` (the programme plan) and the `productos/*-CHECKLIST.md` files are never build plans, even though they contain lists.
- The checklists are the source of truth for sequence and skill names. If a checklist and a skill disagree, flag it rather than silently picking one.
- If `docs/SHIP-IN-7.md` or `docs/SELL-IN-30.md` exists with `Status: Open`, a challenge is running: start every session with that challenge's daily check-in (`ship-in-7` / `sell-in-30`) before any other work. Only one challenge is open at a time; the challenge composes *which* skills run on *which* day, and the checklists remain the source of truth for how each skill runs.
