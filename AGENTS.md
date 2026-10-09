# ProductOS

ProductOS is a complete operating system for taking an AI product from idea to revenue with AI agents — whatever its shape: a web or mobile app, a desktop app or browser extension, an agent plugin, skill, or MCP server, a chat assistant, a developer tool, a productized service, a website, or a digital product. It lives in the `productos/` folder of the product's project folder — that folder **is** the product's home, and ProductOS is set up in it before anything else, even the first line of code. Define and Design need nothing more than the folder; it becomes a git repository at the start of Develop, and only for products built from code there (`ROUTING.md` hard rule 6). Skills call it "the app repo" either way. It works in four phases, each with its own folder, checklist, worksheets, skills, and an orchestrator skill that walks it:

1. **Define** (`productos/define/`, `define-phase`) — nail the offer, the product's **shape**, the customer, and pricing. Every Define skill writes its own section of one document, `docs/DEFINE.md`.
2. **Design** (`productos/design/`, `design-phase`) — identity (the brand in words, written into `docs/DESIGN.md`), the UX writing guide (`docs/COPY.md`), the design system from an image reference (full, or Lite brand tokens for shapes without screens), design prompts, magic moment, onboarding, and the acquisition surfaces the shape needs (landing page, app-store listing, marketplace listing).
3. **Develop** (`productos/develop/`, `develop-phase`) — PRD and roadmap (for a new build or an existing codebase), evals for AI-native shapes, the agent-driven build with code-review and security gates, go-live in the shape's form. Produces `docs/PRD.md`, `docs/ROADMAP.md`, `docs/EVALS.md`, `docs/SECURITY-AUDIT.md`, and `docs/DEPLOY.md`.
4. **Distribute** (`productos/distribute/`, `distribute-phase`) — go-to-market (including the shape's native channels), growth experiments, scaling. A loop, not a one-pass sequence. Produces `docs/GO-TO-MARKET.md`, `docs/GROWTH-EXPERIMENTS.md`, `docs/GROWTH-TRACKER.md`, and `docs/SCALE.md`.

One rule runs through all four phases: **`docs/` is the source of truth for everything ProductOS produces.** Every skill that produces a document writes it to `docs/` at the repo root; nothing a skill produces stays inside `productos/`.

## Where to start

Run `setup` — the installer. It verifies ProductOS is properly installed (sitting as `productos/` inside the product's project folder, root `CLAUDE.md`/`AGENTS.md` wired from `productos/setup/`, `productos/` gitignored), fixes what's missing, and — if the copy shipped with a programme plan at `productos/PLAN.md` — moves it to `docs/PLAN.md` and verifies it against the actual repo. Coached plans are composed by the member's coach from their onboarding call; plan revisions come from the coach too.

If ProductOS is checked out standalone (not inside a project folder), run `setup` anyway — it makes the project folder and moves ProductOS into it as `productos/`. No git needed until Develop.

No plan in the copy? Setup asks one question — *where would you like to start?* — suggesting an answer when the folder points to one:

- **Find a new idea** → `define-phase` on its idea-first route: `define-idea-finder`, then the offer.
- **Start from an idea you have** → `define-phase`, which walks Define step by step and hands on to each later phase's orchestrator — the standard programme.
- **Start from an existing project** (product code, a prototype, an AI-generated app, a live service or listing) → `product-audit`, which scores the product across all four phases and writes a programme for it to `docs/PLAN.md`; `product-refactor` then works through it.
- **Take on a challenge** → `ship-in-7` (live in seven sessions, from wherever the member is) or `sell-in-30` (a first paying customer, for a live product).

For members who don't pick a challenge at the start, the challenges come up again when they fit: `ship-in-7` once Define is done or as the opening block of an audit plan, and `sell-in-30` once the product is live. A member who asks for one by name gets it straight away. After the first session, the member only needs to say "continue".

Each phase checklist names the exact skill to run at each step, the file it produces, and the reference docs it draws on. `productos/ROUTING.md` says which step runs next; `python3 productos/scripts/status.py` shows what's done.

## How this folder is organized

- `productos/define/`, `productos/design/`, `productos/develop/`, `productos/distribute/` — one folder per phase: a `*-CHECKLIST.md` runbook, numbered worksheets (`1-`–`4-`, with `1b-`, `4a-`/`4b-`/`4c-` variants) that give each output its structure and `> Good/Bad` guidance, and `BONUS-*.md` reference playbooks.
- `productos/shapes/` — `SHAPES.md` (the twelve shapes and how to pick one) plus one file per shape: what "live" and "first sale" mean, how every Design and Develop step adapts (Full / Adapted / Lite / Optional / Skip), and the shape's native channels.
- `productos/ROUTING.md` — the step catalog every orchestrator follows: which steps apply (plan → shape → checklist), the hard rules, each step's needs and "Done when".
- `productos/skills/<skill-name>/` — the skills, one flat folder per skill containing a `SKILL.md` (plus any `references/` and `templates/` it loads when needed). Names use the `<phase>-*` convention (e.g. `define-offer-builder`), including the four phase orchestrators (`define-phase`, `design-phase`, `develop-phase`, `distribute-phase`). `build-loop` (the task-by-task loop for Claude Code, Codex, and Cursor) has no prefix so it works outside ProductOS. The seven cross-phase skills have no prefix either: `continue` (the one phrase a member needs — it reads where they are and hands over to whoever owns the next step), `setup` (the installer), `update` (the updater), `product-audit` and `product-refactor` (the existing-product path: audit → plan → run the plan), and the two challenges `ship-in-7` (seven sessions to a live product) and `sell-in-30` (thirty sessions to a first customer), which compose a session-by-session plan from the phase skills and log it in `docs/SHIP-IN-7.md` / `docs/SELL-IN-30.md`.
- `productos/scripts/` — `status.py` (the read-only progress report: a plain-English summary for the member by default, every step with `--detail` for the orchestrators) and `lint-skills.py` (the maintainer's skill lint).
- `productos/hooks/` — the plugin's session-start hook, which greets the member with where they are and what "continue" will do (silent in repos that don't use ProductOS).
- `productos/GLOSSARY.md` — plain-English meanings for the terms members meet; agents explain a term the first time it comes up.
- `productos/setup/` — the coding-agent guidelines (`CLAUDE.md`, `AGENTS.md`) that get wired into the repo root at setup: copied whole if no root file exists, or appended as a marked `<!-- BEGIN PRODUCTOS -->…<!-- END PRODUCTOS -->` block if one does — never overwrite a repo's existing root files.
- `docs/` — the output directory at the **repo root** (not inside `productos/`). ProductOS skills write every output there, alongside whatever documentation the repo already has:
  - **Programme:** `PLAN.md`, `PATH.md` (each phase's route, written by its orchestrator), `PRODUCT-AUDIT.md`, and the challenge logs `SHIP-IN-7.md` / `SELL-IN-30.md`.
  - **Define:** `DEFINE.md` (Summary, Product Offer, Product Shape, Customer Persona, Pricing Strategy, and the optional Business Strategy and Idea Audit sections).
  - **Design:** `DESIGN.md` + `DESIGN.html` (Product Identity, then the design-system tokens), `COPY.md`, `DESIGN-PROMPTS.md`, `MAGIC-MOMENT.md`, `ONBOARDING.md` + `ONBOARDING-WIREFRAME.html`, `LANDING-PAGE.md` + `LANDING-PAGE-WIREFRAME.html`, `APP-LISTING.md`, `MARKETPLACE-LISTING.md`.
  - **Develop:** `PRD.md`, `ROADMAP.md`, `EVALS.md`, `MIGRATION.md`, `SECURITY-AUDIT.md`, `DEPLOY.md`, `CRO-AUDIT.md`, and `design-reviews/` (plus a legacy `REFACTOR.md` in repos from before 2.0).
  - **Distribute:** `GO-TO-MARKET.md`, `GROWTH-EXPERIMENTS.md`, `GROWTH-TRACKER.md`, `SCALE.md`, `ACTIVATION-RETENTION-AUDIT.md`.

  Don't hand-create the canonical files; other files in `docs/` are the app's own — leave them alone.

## Rules for agents working in this folder

- Outputs go to `docs/`, never into `productos/`. The numbered templates in the phase folders are **worksheets**: read them for structure and the `> Good/Bad` calibration, write the answers to the skill's `docs/` file, and leave the worksheet blank. A skill that writes part of a shared document (`DEFINE.md`, the Product Identity section of `DESIGN.md`) writes only its own section.
- Repos set up before ProductOS 1.14.0 may still have `docs/PRODUCT.md` and filled templates inside `productos/`. Don't build on them silently — run `update`, which moves their content into the `docs/` files above.
- Three layers decide which step runs (`productos/ROUTING.md`): `docs/PLAN.md` when it exists (Full, Fast-tracked, Skipped, or Already-done for this member, in order), then the product's shape file, then the checklist order. The checklists remain the source of truth for *how* each step runs.
- The product's shape (`docs/DEFINE.md` → `## Product Shape`) decides which steps apply and what "live" means. Read `productos/shapes/<slug>.md` before any Design, Develop, or Distribute work. A repo from before 2.0 with no shape is treated as a `web-app` until `define-product-shape` runs.
- Respect the dependency chain: if an upstream file (e.g. `docs/DEFINE.md`) is missing, run the skill that produces it — or the fast-track producer the plan names (`define-from-code` for the Define documents, `design-design-system-from-code` for the design system) — rather than improvising content; if no product idea exists at all, `define-idea-finder` finds one first.
- The project folder is the product codebase — build-phase skills operate on it directly, and they need version history on first (`setup` → *Version history*). Which `docs/` files are build plans is defined once, in the root guidelines (`setup/CLAUDE.md` and its `setup/AGENTS.md` twin); `docs/PLAN.md` (the programme plan) and the `productos/*-CHECKLIST.md` files are never build plans, even though they contain lists.
- The checklists are the source of truth for sequence and skill names. If a checklist and a skill disagree, flag it rather than silently picking one.
- If `docs/SHIP-IN-7.md` or `docs/SELL-IN-30.md` exists with `Status: Open`, a challenge is running: start every session with that challenge's daily check-in (`ship-in-7` / `sell-in-30`) before any other work. Only one challenge is open at a time; the challenge composes *which* skills run on *which* day, and the checklists remain the source of truth for how each skill runs.
