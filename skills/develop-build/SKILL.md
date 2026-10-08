---
name: develop-build
description: >-
  Builds a whole ProductOS roadmap in one run — docs/ROADMAP.md, whether a new build or an
  existing-codebase gap roadmap (or a legacy docs/REFACTOR.md) — every task in order, each
  implemented, tested, and verified, with a code review and a commit at every phase boundary, until
  the roadmap is complete. Use when the user says "build my MVP", "execute the roadmap", "run the
  refactor", or "build everything". Requires docs/PRD.md and the roadmap. Not for one task at a time
  or post-MVP features — use build-loop.
---

# Develop: Build

Execute every task in the roadmap, in order, until all tasks are checked off.

## Pick the plan

- The member named one → use it.
- Otherwise `docs/ROADMAP.md` with unchecked tasks. A legacy `docs/REFACTOR.md` with unchecked tasks (written by ProductOS versions before 2.0) is run exactly the same way, as an existing-codebase plan. Both with unchecked tasks → ask which.
- `docs/ROADMAP.md` holds a `## Decisions (draft)` table → the existing-codebase review was interrupted; stop and resume `develop-prd-roadmap`.
- No plan → stop and run `develop-prd-roadmap` (it writes a new-build or an existing-codebase roadmap).

**Existing-codebase rules** apply when the roadmap's header carries the `**Mode:** existing-codebase` line, or the plan is a legacy `docs/REFACTOR.md`.

## Setup

Read the plan first — it is the source of truth for what to build and in what order. An existing-codebase plan also encodes keep/remove decisions already made with the member; don't relitigate them. `docs/PRD.md` is the spec the plan builds toward (missing → stop and run `develop-prd-roadmap`); `docs/DESIGN.md` holds the visual tokens; `docs/DEFINE.md` holds the strategy; `docs/EVALS.md`, when it exists, holds the scenarios an AI-native product must pass. Don't load these wholesale — each phase lists its Reference sections, plus whatever a task's Notes line points to.

## Work loop

Repeat until every task is complete:

1. **Find the first unchecked task** (`- [ ]`). Tasks are ordered intentionally (removals and foundations before rebuilds) — never skip ahead.
2. **Read what the task needs** — its Files and Notes lines, plus the current phase's Reference sections if not yet read this session.
3. **Implement it** exactly as specified — file paths, package names, and config values are deliberate. Follow the repo's `CLAUDE.md`/`AGENTS.md`: simplest implementation that satisfies the task, surgical changes, no speculative features; remove any imports, variables, or files your change orphans.
4. **Test and verify before moving on.** Run the task's `Verify:` step, run the product, run the test suite, and add tests for new logic. "Run the product" means where the customer meets it — the app in a browser or simulator; for an `agent-skill`, `agent-plugin`, `mcp-server`, or `chat-assistant`, load it in its host and use it, and run the task's `docs/EVALS.md` scenarios when Notes name them. Under existing-codebase rules, existing tests passing is part of every task's definition of done; if a task changes behaviour on purpose, update the affected tests and say so. If verification fails, fix it first — never mark a failing task complete or start the next one with the product broken. A task Notes marks `Owner: member` (an account, a store form, a no-code tool): prepare what you can, ask the member to do it, and check it off once they confirm its Verify line.
5. **Mark it complete** — `- [ ]` to `- [x]`, and update the header (`**Status:** X/Y tasks complete`, `**Current Phase:** ...`).
6. **At each phase boundary:** run the product end to end and confirm the phase's Goal is true and demoable. **Review the phase** with the coding agent's built-in review over the phase's changes (`/review` in Claude Code, or the equivalent in Cursor or Codex; `develop-code-review` if none is available), plus a security-focused pass if the phase touched auth, payments, user input, data access, or agent tools and hooks. Fix the findings and re-run the affected tests. Then commit `Phase {N}: {Phase Title}` summarizing the goal and task range, push if a remote is configured, and keep going — no pull request between phases.

## Rules

- The PRD's stack choices are final — implement them, never substitute alternatives.
- Visual styling comes from `docs/DESIGN.md` tokens — never invent colors, type, or spacing.
- If a task is ambiguous or conflicts with the PRD, check the PRD section it references; if still unclear, ask one specific question rather than guessing.
- If necessary work isn't covered by any task (in existing-codebase work, often a hidden dependency on removed code), surface it and propose adding a task — don't silently expand scope.
- **Existing-codebase rules:** the plan's keep/remove decisions are final — remove a feature cleanly; don't preserve it "just in case". If a phase can't be made green, reset to the last phase commit (or the `pre-refactor-<date>` tag if no phase is committed yet) — tell the member first, and never leave the main branch broken.
- Keep going until `**Status:** Y/Y tasks complete`: every task checked, every phase reviewed and verified, all tests passing — and the magic moment working end to end (a new build) or the codebase fully aligned with the PRD (existing-codebase).
