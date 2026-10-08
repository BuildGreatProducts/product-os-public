---
name: develop-build
description: >-
  Builds a whole ProductOS plan in one run — docs/ROADMAP.md for a new MVP, or docs/REFACTOR.md for
  an existing codebase — every task in order, each implemented, tested, and verified, with a code
  review and a commit at every phase boundary, until the plan is complete. Use when the user says
  "build my MVP", "execute the roadmap", "run the refactor", or "work through REFACTOR.md". Requires
  docs/PRD.md and the plan. Not for one task at a time or post-MVP features — use build-loop.
---

# Develop: Build

Execute every task in the build plan, in order, until all tasks are checked off.

## Pick the plan

- The member named one → use it.
- Otherwise: `docs/REFACTOR.md` with unchecked tasks → **refactor mode**; `docs/ROADMAP.md` with unchecked tasks → **MVP mode**; both → ask which.
- Neither exists → stop. A new MVP needs `develop-prd-roadmap`; an existing codebase needs `develop-refactor-plan`.

## Setup

Read the plan first — it is the source of truth for what to build and in what order. In refactor mode it also encodes keep/remove decisions already made with the member; don't relitigate them. `docs/PRD.md` is the spec the plan builds toward (stop and run `develop-prd-roadmap` if it's missing in MVP mode); `docs/DESIGN.md` holds the visual design tokens; `docs/DEFINE.md` holds the product strategy. Don't load these wholesale — each phase lists the Reference sections to read, plus whatever a task's Notes line points to.

## Work loop

Repeat until every task in the plan is complete:

1. **Find the first unchecked task** (`- [ ]`). Tasks are ordered intentionally (in a refactor, removals and foundations come before rebuilds) — never skip ahead.
2. **Read what the task needs** — its Files and Notes lines, plus the current phase's Reference sections if not yet read this session.
3. **Implement the task** exactly as specified — file paths, package names, and config values are deliberate. Follow the repo's `CLAUDE.md`/`AGENTS.md` guidelines: simplest implementation that satisfies the task, surgical changes only, no speculative features; remove any imports, variables, or files your change orphans.
4. **Test and verify before moving on.** Run the verification step at the end of the task's Notes, run the app, run the test suite, and add tests for new logic. In refactor mode, existing tests passing is part of every task's definition of done; if a task changes behaviour on purpose, update the affected tests and say so. If verification fails, fix it first — never mark a failing task complete or start the next task with the app broken.
5. **Mark the task complete** — change `- [ ]` to `- [x]` and update the header status line (`**Status:** X/Y tasks complete`, `**Current Phase:** ...`).
6. **At each phase boundary:** run the app end to end and confirm the phase's Goal is true (and demoable, in MVP mode). **Review the phase:** run the coding agent's built-in review over the phase's changes (`/review` in Claude Code, or the equivalent in Cursor or Codex; `develop-code-review` if none is available), plus a security-focused pass if the phase touched auth, payments, user input, or data access. Fix the findings and re-run the affected tests. Then commit — `Phase {N}: {Phase Title}` in MVP mode, `Refactor Phase {N}: {Phase Title}` in refactor mode — summarizing the goal and completed task range, push if a remote is configured, and keep going. There's no need to open a pull request between phases.

## Rules

- The PRD's stack choices are final — implement them, never substitute alternatives.
- Visual styling comes from `docs/DESIGN.md` tokens — never invent colors, type, or spacing.
- If a task is ambiguous or conflicts with the PRD, check the PRD section it references; if still unclear, ask one specific question rather than guessing.
- If necessary work isn't covered by any task (in a refactor, often a hidden dependency on removed code), surface it and propose adding a task — don't silently expand scope.
- **Refactor mode:** the plan's keep/remove decisions are final — if a task removes a feature, remove it cleanly; don't preserve it "just in case". If a phase can't be made green, reset to the last phase commit (or the `pre-refactor-<date>` tag if no phase has been committed yet) — tell the member first, and never leave the main branch broken.
- Keep going until `**Status:** Y/Y tasks complete`: every task checked, every phase reviewed and verified, all tests passing — and the magic moment working end to end (MVP mode) or the codebase fully aligned with the PRD (refactor mode).
