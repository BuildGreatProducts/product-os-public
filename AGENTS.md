# ProductOS

ProductOS is a complete operating system for taking a product from idea to revenue with AI agents. It lives in the `productos/` folder of the app repository it serves — the surrounding repo **is** the product codebase, and ProductOS is set up in it before anything else, even the first line of code. It works in four phases, each with its own folder, checklist, templates, and skills:

1. **Define** (`productos/define/`) — nail the offer, customer, and pricing, then ship the **mini-launch** (a small post or DM batch that gets the first real reply from a potential customer). Produces `docs/PRODUCT.md` and starts `docs/LAUNCHES.md`.
2. **Design** (`productos/design/`) — identity (the brand in words), then the design system derived from an image reference (`docs/DESIGN.md` + its live `docs/DESIGN.html` style guide), magic moment, onboarding, acquisition surface, then relaunch #2 ("here's what it looks like").
3. **Develop** (`productos/develop/`) — PRD, roadmap, the agent-driven build with code-review and security gates, then relaunch #3 (the beta invite). Produces `docs/PRD.md`, `docs/ROADMAP.md`, `docs/SECURITY-AUDIT.md`, and `docs/DEPLOY.md`.
4. **Distribute** (`productos/distribute/`) — go-to-market, relaunch #4 (the public launch), growth experiments, scaling. A loop, not a one-pass sequence.

One thread runs through all four phases: each closes with a launch, run by the cross-phase `studio-launch` skill, climbing the signal ladder (`reply → conversation → signup → activated user → payment`) and logged in `docs/LAUNCHES.md` alongside the believers list.

## Where to start

Run `studio-setup` — the installer. It verifies ProductOS is properly installed (sitting as `productos/` inside a git repo, root `CLAUDE.md`/`AGENTS.md` wired from `productos/setup/`, `productos/` gitignored), fixes what's missing, and — if the copy shipped with a programme plan at `productos/PLAN.md` — moves it to `docs/PLAN.md` and verifies it against the actual repo. Custom plans are composed by the user's coach from their onboarding call; plan revisions come from the coach too.

If ProductOS is checked out standalone (no surrounding app repo), run `studio-setup` anyway — it walks the user through creating the app repo and moving ProductOS into it as `productos/`.

No plan in the copy? The linear path is the standard programme: open `productos/define/DEFINE-CHECKLIST.md` and work top to bottom, finishing each phase before the next. Each phase checklist names the exact skill to run at each step, the file it produces, and the reference docs it draws on.

## How this folder is organized

- `productos/define/`, `productos/design/`, `productos/develop/`, `productos/distribute/` — one folder per phase: a `*-CHECKLIST.md` runbook, numbered templates (`1.`–`4.`) that skills fill in place, and `BONUS - *.md` reference playbooks.
- `productos/skills/<skill-name>/` — the Claude skills the checklists invoke, one flat folder per skill containing a `SKILL.md` (plus any bundled reference files). Names use the `studio-<phase>-*` convention (e.g. `studio-define-offer-builder`); the three tool-specific build loops (`claude-code-build-loop`, `codex-build-loop`, `cursor-build-loop`) are deliberately unprefixed so they work outside ProductOS, and the two cross-phase skills are `studio-setup` (the installer — it opens every programme) and `studio-launch` (the launch ritual — it closes every phase), no phase prefix on either.
- `productos/setup/` — the coding-agent guidelines (`CLAUDE.md`, `AGENTS.md`) that get wired into the app repo root at setup: copied whole if no root file exists, or appended as a marked `<!-- BEGIN PRODUCTOS -->…<!-- END PRODUCTOS -->` block if one does — never overwrite a repo's existing root files.
- `docs/` — the output directory at the **app repo root** (not inside `productos/`). ProductOS skills write the canonical product documents there (`PLAN.md`, `PRODUCT.md`, `DESIGN.md` + `DESIGN.html`, `PRD.md`, `ROADMAP.md`, `SECURITY-AUDIT.md`, `DEPLOY.md`, `LAUNCHES.md`), alongside whatever documentation the repo already has. Don't hand-create the canonical files; other files in `docs/` are the app's own — leave them alone.

## Rules for agents working in this folder

- Templates are filled **in place** — rewrite the numbered template files, preserving their structure and the `> Good/Bad` guidance scaffolding. Never create parallel copies.
- If `docs/PLAN.md` exists, consult it before opening any checklist — it says which steps are Full, Fast-tracked, Skipped, or Already-done for this user, and in what order. The plan governs *which steps apply*; the checklists remain the source of truth for *how each step runs*. If it doesn't exist, follow the checklists linearly from Define — custom plans ship with coached copies of ProductOS.
- Respect the dependency chain: if an upstream file (e.g. `docs/PRODUCT.md`) is missing, run the skill that produces it — or the fast-track producer the plan names (`studio-define-from-code` for the Define documents, `studio-design-design-system-from-code` for the design system) — rather than improvising content.
- The surrounding repo is the product codebase — build-phase skills operate on it directly. Build-loop plan files are `docs/ROADMAP.md` and `docs/REFACTOR.md`; `docs/PLAN.md` (the programme plan) and the `productos/*-CHECKLIST.md` files are never build plans, even though they contain lists.
- The checklists are the source of truth for sequence and skill names. If a checklist and a skill disagree, flag it rather than silently picking one.
