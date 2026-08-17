---
name: studio-setup
description: Use as the first thing after receiving ProductOS — it installs the system into the app repo and adopts the custom programme plan when one shipped with the copy. Triggers on phrases like "set up ProductOS", "install ProductOS", "studio setup", "wire my repo", "adopt my plan", "get ProductOS working in this repo", or any request to install or initialise ProductOS in a codebase. Verifies productos/ sits inside a git repo (and walks a standalone checkout through creating the app repo and moving in), wires the coding-agent guidelines from productos/setup/ into the repo root (copy whole, or append the marked block — never overwriting), adds productos/ to .gitignore, and — if the copy shipped with a plan at productos/PLAN.md — moves it to docs/PLAN.md and runs a light verification pass against the actual repo. Ends by naming the member's literal first action. Run once at install; safe to re-run any time.
---

# Setup — install ProductOS and adopt your plan

ProductOS lives inside your app's repository, and this skill is how it gets installed there — the first thing to run after receiving your copy. It wires the repo, and if your copy came from your coach it carries your custom programme inside: setup moves that plan to `docs/PLAN.md`, where every ProductOS skill expects it.

> **Session shape:** minutes, not a meeting. The only files this skill writes are the root `CLAUDE.md`/`AGENTS.md`, `.gitignore`, and `docs/PLAN.md` (moved from the seed). All checks are idempotent — re-running costs seconds and fixes whatever drifted.

## Workflow

### 1. Verify the repo

Check that this folder is `productos/` inside a git repository (`git rev-parse --is-inside-work-tree` from the parent). If ProductOS is checked out standalone — no surrounding repo — pause and set it up: help the user create (or pick) the app repo, `git init` it if new, and move this folder into it as `productos/` exactly. From scratch is no exception; the repo exists before the product does.

### 2. Wire the root guidelines

The app repo root needs the coding-agent guidelines from `productos/setup/`:

- Root `CLAUDE.md`/`AGENTS.md` **don't exist** → copy them from `productos/setup/` whole.
- The repo **already has them** → **never overwrite.** Append only the `<!-- BEGIN PRODUCTOS -->…<!-- END PRODUCTOS -->` block from the setup templates, plus one pointer line to `productos/setup/CLAUDE.md` for the full guidelines. If the markers are already present, replace the block between them.

Wire whichever file(s) match the user's coding agent(s); default is both.

### 3. Gitignore the system

Ensure the app repo's `.gitignore` contains a `productos/` line (create or append; skip if present). ProductOS is licensed to the member, not the public — the materials stay uncommitted, while the member's outputs (`docs/`, the wired root files) are theirs and stay tracked as normal.

### 4. Adopt the plan

If **`productos/PLAN.md`** exists (it ships inside coached copies), move it to **`docs/PLAN.md`** — create `docs/` first if needed (`mkdir -p docs`). Then a light verification pass:

1. Read the plan's **Inventory** and the *Check at setup* lines in its **Your Programme** list.
2. Check each item against the actual repo, now that it's readable — does the app run, does the core flow work, does the codebase match what the plan assumed?
3. Where reality matches, confirm and move on. Where it doesn't, apply the plan's own stated consequence ("if the core flow doesn't run end to end, Develop route becomes 3b") and **annotate** the affected step — a one-line note under the relevant programme step, dated.

Annotate, don't recompose: this pass adjusts details the coach couldn't see, it does not redesign the programme. Anything bigger — the member's situation has genuinely changed, a phase no longer fits — goes back to the coach, who re-runs the intake and re-delivers an updated `PLAN.md` (replace `docs/PLAN.md` with it when it arrives).

### 5. Name the first action

- **Plan adopted** → read its **Your Programme** list and tell the member their literal first action — the exact checklist to open or skill to run, e.g. *"Run `studio-define-from-code` — your plan fast-tracks Define from your existing app."*
- **No plan anywhere** → the linear path: open **`productos/define/DEFINE-CHECKLIST.md`** and work top to bottom, finishing each phase before the next. (Custom programmes ship with coached copies of ProductOS.)

## What "done" looks like

`productos/` sits inside a git repo; the root `CLAUDE.md`/`AGENTS.md` carry the PRODUCTOS block; `.gitignore` excludes `productos/`; any shipped plan now lives at `docs/PLAN.md` with its setup checks resolved or annotated; and the member knows exactly what to do first. Anything less — name the gap and fix it before ending the session.
