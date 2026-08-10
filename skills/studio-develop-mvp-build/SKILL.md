---
name: studio-develop-mvp-build
description: Use in the app repo — the repository that contains `productos/` — when the user wants the full MVP built from their ProductOS spec documents. Triggers on phrases like "build my MVP", "build the app", "execute the roadmap", "start the build", "work through the whole roadmap", "build everything", or any request to implement the entire plan rather than a single task or phase. Requires `docs/PRD.md` and `docs/ROADMAP.md` (plus `docs/PRODUCT.md` and `docs/DESIGN.md` for context). Works through every roadmap task in order — implementing, testing, and verifying each before moving on, marking checkboxes and updating the status line, committing at each phase boundary — and runs until all tasks are complete and the magic moment works end to end.
---

# Develop: MVP Build

Build the complete app by executing every task in `docs/ROADMAP.md`, in order, until all tasks are checked off.

## Setup

Read `docs/ROADMAP.md` first — it is the source of truth for what to build and in what order. `docs/PRD.md` is the technical spec behind it; `docs/DESIGN.md` holds the visual design tokens; `docs/PRODUCT.md` holds the product strategy. Do not load these documents wholesale — each phase lists the specific Reference sections to read, plus whatever a task's Notes line points to. If `docs/ROADMAP.md` or `docs/PRD.md` is missing, stop and tell the user to run `studio-develop-prd-roadmap` first.

## Work loop

Repeat until every task in the roadmap is complete:

1. **Find the first unchecked task** (`- [ ]`). Tasks are ordered intentionally — never skip ahead.
2. **Read what the task needs** — its Files and Notes lines, plus the current phase's Reference sections if not yet read this session.
3. **Implement the task** exactly as specified — file paths, package names, and config values are deliberate. Follow the repo's `CLAUDE.md`/`AGENTS.md` guidelines: simplest implementation that satisfies the task, no speculative features, surgical changes only.
4. **Test and verify before moving on.** Run the verification step at the end of the task's Notes, run the app, run existing tests, and add tests for new logic. If verification fails, fix it first — never mark a failing task complete or start the next task with the app broken.
5. **Mark the task complete** — change `- [ ]` to `- [x]` and update the header status line (`**Status:** X/Y tasks complete`, `**Current Phase:** ...`).
6. **At each phase boundary:** run the app end to end and confirm the phase's Goal is true and demoable. Commit with a message `Phase {N}: {Phase Title}` summarizing the goal and completed task range, then push and keep building — there's no need to open a pull request or pause for review between phases. If the phase touched auth, payments, user input, or data access, run the coding agent's built-in review (`/review` in Claude Code, or the equivalent in Cursor or Codex) and address the findings before continuing.

## Rules

- The PRD's stack choices are final — implement them, never substitute alternatives.
- Visual styling comes from `docs/DESIGN.md` tokens — never invent colors, type, or spacing.
- If a task is ambiguous or conflicts with the PRD, check the PRD section it references; if still unclear, ask one specific question rather than guessing.
- If necessary work isn't covered by any task, surface it and propose adding a task — don't silently expand scope.
- Keep going until `**Status:** Y/Y tasks complete`: every task checked, every phase verified, the magic moment working end to end.
