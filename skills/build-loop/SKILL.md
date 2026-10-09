---
name: build-loop
description: >-
  Builds plan tasks or a feature prompt in Claude Code, Codex, or Cursor through a build → test →
  fix loop per task, then one review pass with the tool's own /review (plus a security pass for
  sensitive surfaces) once the work is finished. Use when the user says "run the build loop", "build
  the next task", "continue the plan", or asks to implement work from a plan file or a direct prompt.
  Works in any repo. Not for running a whole roadmap in one go — use develop-build.
---

# Build Loop

Quality-gated feature work: nothing ships on "it compiles" — every task is built, tested end to end, and fixed, and the finished work is reviewed before the user hears "done."

## Source of work

- **A plan file exists** (task list with `- [ ]` checkboxes): work the first unchecked task. In a ProductOS repo, work only the build plans the root `CLAUDE.md`/`AGENTS.md` name — never `docs/PLAN.md` or the `productos/*-CHECKLIST.md` files, even though they contain lists. Elsewhere, search the repo for the plan. Tasks are ordered intentionally — never skip ahead. If the plan references spec docs, read only the sections relevant to the current task.
- **No plan (or the request is outside it):** build from the user's prompt. Restate it as a verifiable goal with 2–4 success criteria and confirm scope in one message before building.

**Version history must be on** — the review reads the uncommitted changes, and the work is committed when it's done. Not a git repository yet? In a ProductOS project run `setup` → *Version history* first; elsewhere, ask the user before running `git init`.

## The loop

Steps 1–4 run per task (or per prompted feature) — do not advance until each passes. Step 5 runs once, when the requested scope is complete.

1. **Build.** Implement exactly what the task specifies. Simplest implementation that satisfies it, surgical changes, no speculative scope. Match existing project conventions.

2. **Test end to end.** Run the task's verification step (or the success criteria). Run the full test suite — everything that passed before must still pass. Add tests for new logic. Then exercise the feature as a user would: run the app, walk the real flow including empty, loading, and error states.

3. **Fix.** Anything testing finds goes back through the loop: fix → re-test. Never mark a failing task complete; never start the next task with the app broken.

4. **Continue.** Mark the task `- [x]`, update any progress/status line in the plan, and loop to the next task until the requested scope is complete.

5. **Review the finished work.** Once every task in the requested scope is checked off, run your tool's review over all the changes made in this run, plus the security pass if the work touches auth, payments, user input, or data access:

   | Tool | Review | Security pass |
   | --- | --- | --- |
   | Claude Code | `/review` | `/security-review` |
   | Codex | `/review` against the uncommitted changes | a second `/review` with custom instructions focused on security ("Focus on security vulnerabilities and unvalidated input") |
   | Cursor | `/review` | a second review prompted for vulnerabilities (injection, authorization gaps, secrets exposure, unsafe input handling), or Bugbot on the PR if it's configured |

   If your tool's review isn't available, run `develop-code-review` on the uncommitted changes instead. Fix all findings in scope — bugs, security issues, edge cases, performance, style in files you touched. If the project has a design system spec (design tokens file, DESIGN.md, theme config), check UI changes against it — no hardcoded colors, type, or spacing that bypass tokens. Note pre-existing issues in untouched code for the report instead of fixing silently. Re-run the review until clean, then re-run the tests the fixes touched. If a finding contradicts the task or spec, the spec wins — flag the disagreement.

6. **Report.** When done, tell the user: what was built and plan progress, review findings fixed and anything deferred, how it was verified (tests + flow walked), and what needs their attention next. Be honest about anything flaky or partially verified.

## Rules

- Skipped review or untested work = unfinished work.
- Don't relitigate plan decisions; if a task seems wrong, ask one specific question rather than guessing.
- Discovered work no task covers? Surface it and propose a task — never silently expand scope.
