---
name: setup
description: >-
  Installs ProductOS into the app repo: checks productos/ sits in a git repo (walking a standalone
  checkout into one), wires the coding-agent guidelines into the root CLAUDE.md and AGENTS.md
  without overwriting, gitignores productos/, adopts a coach's plan from productos/PLAN.md into
  docs/PLAN.md, and names the first action. Use first after receiving ProductOS, or when the user
  says "set up ProductOS", "install ProductOS", or "wire my repo". Safe to re-run. Not for upgrading
  an installed copy — use update.
---

# Setup — install ProductOS and adopt your plan

Install ProductOS into the app repository — the first thing to run after receiving a copy — and, if the copy came from the member's coach, move the custom programme plan it carries to `docs/PLAN.md`, where every ProductOS skill expects it. It takes minutes. The only files it writes are the root `CLAUDE.md`/`AGENTS.md`, `.gitignore`, and `docs/PLAN.md` (moved from the seed). Every check is idempotent — re-running costs seconds and fixes whatever drifted.

## Workflow

### 1. Verify the repo

Check that this folder is `productos/` inside a git repository (`git rev-parse --is-inside-work-tree` from the parent). If ProductOS is checked out standalone — no surrounding repo — pause and set it up: help the member create (or pick) the app repo, `git init` it if new, and move this folder into it as `productos/` exactly. From scratch is no exception; the repo exists before the product does.

### 2. Wire the root guidelines

The app repo root needs the coding-agent guidelines from `productos/setup/`:

- Root `CLAUDE.md`/`AGENTS.md` **don't exist** → copy them from `productos/setup/` whole.
- The repo **already has them** → **never overwrite** the member's content. Append the `<!-- BEGIN PRODUCTOS -->…<!-- END PRODUCTOS -->` block from the matching file in `productos/setup/`, and add one pointer line to `productos/setup/CLAUDE.md` (for the full guidelines) **inside** the markers, just before `<!-- END PRODUCTOS -->`. If the markers are already present (a re-run), replace everything between them — pointer line included — with the fresh block; never append a second block.

Wire whichever file(s) match the member's coding agent(s); default is both.

### 3. Gitignore the system

Ensure the app repo's `.gitignore` contains a `productos/` line (create or append; skip if present). Then check it actually took effect: if `productos/` was committed before the line existed (`git ls-files productos | head -1` returns anything), untrack it with `git rm -r --cached productos/` and tell the member to commit — an ignore line does nothing for files already tracked. ProductOS is licensed to the member, not the public — the materials stay uncommitted, while the member's outputs (`docs/`, the wired root files) are theirs and stay tracked as normal.

### 4. Adopt the plan

If **`productos/PLAN.md`** exists (it ships inside coached copies), move it to **`docs/PLAN.md`** — create `docs/` first if needed (`mkdir -p docs`). Then a light verification pass:

1. Read the plan's **Inventory** and the *Check at setup* lines in its **Your Programme** list.
2. Check each item against the actual repo, now that it's readable — does the app run, does the core flow work, does the codebase match what the plan assumed?
3. Where reality matches, confirm and move on. Where it doesn't, apply the plan's own stated consequence ("if the core flow doesn't run end to end, Develop route becomes 3b") and **annotate** the affected step — a one-line note under the relevant programme step, dated.

Older plans may use retired names. Read them as follows, and don't rewrite the plan for a rename:

| The plan names | Read it as |
| --- | --- |
| `studio-<name>` (before 1.11.0, e.g. `studio-define-pricing`) | `<name>` — the prefix simply drops |
| `define-leverage-finder` / `studio-define-leverage-finder` (before 1.12.0) | `define-idea-finder` |
| `mini-launch` / `studio-launch` (before 1.14.0) | Retired — launches are no longer part of the system. Annotate the step as retired. |
| `define-product` / `studio-define-product` (before 1.14.0) | Retired — the Define skills write `docs/DEFINE.md` directly, so there's no synthesis step. Annotate the step as retired. |
| `docs/PRODUCT.md` | `docs/DEFINE.md` |
| `cc-build-loop` / `codex-build-loop` / `cursor-build-loop` (before 1.15.0) | `build-loop` |
| `develop-mvp-build` / `develop-refactor-build` (before 1.15.0) | `develop-build` |

Annotate, don't recompose: this pass adjusts details the coach couldn't see, it does not redesign the programme. Anything bigger — the member's situation has genuinely changed, a phase no longer fits — goes back to the coach, who re-runs the intake and re-delivers an updated `PLAN.md` (replace `docs/PLAN.md` with it when it arrives).

### 5. Name the first action

- **Plan adopted** → read its **Your Programme** list and tell the member their literal first action — the exact checklist to open or skill to run, e.g. *"Run `define-from-code` — your plan fast-tracks Define from your existing app."*
- **No plan anywhere** (and no challenge already open in `docs/`) → offer the two paths, and recommend the one the repo points to:
  - **New project** — nothing built yet (the repo holds little beyond `productos/`, `docs/`, and config files): run **`define-offer-builder`**, Step 1 of `productos/define/DEFINE-CHECKLIST.md`, then work down the checklists phase by phase. No idea yet? `define-idea-finder` runs first and hands straight into it.
  - **Existing project** — app code, a prototype, an AI-generated app, or an app on a prompt-to-app platform: run **`ship-in-7`** — seven sessions to the app live at a real URL, composed from the phase skills, with a check-in every session. (An app already live at a real URL has met Ship in 7's bar; offer its follow-on, **`sell-in-30`**, instead.)

  Say what you saw and which path it points to (*"There's a Next.js app in `src/`, so this is an existing project — start Ship in 7"*), and let the member pick the other if it fits better. (Custom programmes ship with coached copies of ProductOS.)

Setup installs the copy the member already has; it doesn't fetch a newer one. Re-running setup to pick up a new release? Run **`update`** instead — it brings `productos/` up to the latest version, moves anything an older copy left inside `productos/` into `docs/`, and runs steps 2–3 of this skill itself.

## Verify before ending

- [ ] `productos/` sits inside a git repo.
- [ ] The root `CLAUDE.md`/`AGENTS.md` carry exactly one PRODUCTOS block.
- [ ] `.gitignore` excludes `productos/` and nothing under it is tracked.
- [ ] Any shipped plan lives at `docs/PLAN.md` with its setup checks resolved or annotated.
- [ ] The member knows exactly what to do first.

Anything less — name the gap and fix it before ending the session.
