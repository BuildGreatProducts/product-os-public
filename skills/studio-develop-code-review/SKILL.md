---
name: studio-develop-code-review
description: Use when the user has uncommitted changes and wants them reviewed before committing — the deliberate whole-diff correctness pass. Triggers on phrases like "review my changes", "code review", "check my work before I commit", "am I ready to commit", "review what we just built", "anything wrong with this diff", or any request to review uncommitted work. Runs in the app repo — the repository that contains `productos/`. Reads the working tree, staged changes, and new untracked files, states what the change is trying to do, reviews across five lenses (correctness, regressions, edge cases, a thin security pass, consistency), verifies every finding against the actual source before reporting, and delivers an in-conversation report — must-fix items, considerations, pre-existing issues — ending in an explicit verdict: ready to commit or not. Works standalone in any repo.
---

# Develop: Code Review

The deliberate pre-commit review. The build loops run their tool's `/review` in-flight, per task; this skill is the step back — a whole-diff pass over everything currently uncommitted, before it becomes a commit. The output is a conversation, not a file: findings with locations, and a verdict.

**Boundary with the sibling skills:** the build loops (`claude-code-build-loop` etc.) own in-flight, per-task review while building; `studio-develop-design-review` owns design-system adherence (tokens, components, `docs/DESIGN.md`); `studio-develop-security-audit` owns security depth. **This skill owns the pre-commit correctness pass** — it carries only a thin security check for the two commit-blockers (hardcoded secrets, missing auth on new routes) and hands anything deeper to the audit.

The voice is a senior engineer reviewing a teammate's diff — direct, specific, and calibrated. Not a gatekeeper: the job is to catch what would break, say what's genuinely good in one line, and give a clear verdict. Nitpicks are not findings. A clean small diff deserving "no issues — ready to commit" is a normal, expected outcome, not a failure to look hard enough.

> **Session length:** 5–15 minutes for a typical feature diff.

## Workflow

### 1. Establish the scope

Run and read:

- `git status --porcelain` — the overall picture.
- `git diff HEAD` — staged + unstaged changes against the last commit.
- `git diff --staged` — what's staged specifically, if the distinction matters to the user.
- `git ls-files --others --exclude-standard` — **new untracked files, read each in full.** Untracked files never appear in `git diff` and are the most commonly missed review surface — and exactly where stray `.env` files and secrets land.
- `git log --oneline -5` — what the recent work was about.

If there are no uncommitted changes, say so and stop — nothing to review. If the diff is large (>30 changed files), ask whether to scope down to the feature at hand — don't blanket-review a giant auto-formatter pass.

### 2. State the intent

Before judging anything, say in one or two sentences what these changes are trying to do — and confirm it if it's not obvious. Read enough surrounding context to review honestly: the callers of changed functions, the consumers of changed API responses, the tests that cover the touched paths, the types. Load the repo's root `CLAUDE.md`/`AGENTS.md` conventions — deviations from *this codebase's* established patterns are findings; deviations from generic best practice are not.

### 3. Review across five lenses

One pass per lens over the scoped diff, gathering candidate findings before reporting anything:

1. **Correctness** — logic errors, inverted conditions, off-by-one, wrong operator, unhandled null/undefined, unawaited promises, wrong branch on error.
2. **Regressions & contracts** — changed function signatures or return shapes with un-updated callers; removed or renamed exports still imported elsewhere; schema changes vs. the queries that hit them; API response changes vs. the frontend that consumes them.
3. **Edge cases & error handling** — empty/zero/negative inputs, network failure paths, swallowed exceptions, missing loading/error states on new UI.
4. **Security (thin pass)** — two commit-blockers only: hardcoded secrets or keys anywhere in the diff or untracked files, and new routes/endpoints with no auth check. Anything subtler gets one line: "worth a `studio-develop-security-audit` pass" — don't attempt depth here.
5. **Consistency & reuse** — re-implements an existing helper, deviates from the codebase's own patterns, leftover debug output, commented-out blocks, TODO stubs returning fake data.

### 4. Verify before reporting

Every finding earns its place or gets cut:

- **Behavioral claims need a `file:line` citation in actual source — never an inference from a name.** "This probably breaks the caller" is not a finding until you've read the caller.
- Confirm the broken consumer actually exists and is actually reached.
- Confirm the issue is **in the diff**. If it's real but pre-existing, re-label it Pre-existing — don't drop it, and don't blame today's change for it.
- Cut anything you wouldn't confidently raise reviewing a colleague's PR. Better to miss a theoretical issue than to bury the two real ones in noise.

### 5. Report and give the verdict

Deliver in conversation, in this shape:

- **One-line tally first** — *"2 must-fix, 1 consider, 1 pre-existing"* or *"No blocking issues."*
- **Must fix** — numbered; each with: what (one sentence), why it matters (the failure a user would hit), where it was verified (`file:line`), and the fix (specific, not "handle this better").
- **Consider** — capped at **five**; anything beyond that is a count ("…and 4 smaller nits — ask if you want them"). Never promote a nitpick to must-fix.
- **Pre-existing (not from this change)** — real issues noticed in touched code that today's diff didn't cause. The member should know about the landmine without being blamed for planting it.
- **One line of credit** — something genuinely done well. One line, not a paragraph.
- **Verdict, always explicit:** **Ready to commit** or **Not ready — fix the N must-fix items first.** Never end without one.

## Rules

- **Re-reviews converge.** After the user fixes findings and asks again, check the fixes and report must-fix items only — no new nits on a re-pass. The loop must end.
- **Don't duplicate the machines.** Never flag formatting, import order, missing tests, or anything the repo's linter/CI already enforces.
- **The spec wins.** If a finding contradicts `docs/PRD.md` or the task's intent, flag the disagreement instead of asserting the code is wrong.
- **Never say "looks good" without having read the code.** The credit line and the verdict are earned by the pass, not by politeness.

## What "done" looks like

The user knows exactly three things: what must change before committing (with locations and fixes), what can wait, and whether they're ready to commit. Every finding cites real source. Small clean diffs got a fast, confident "ready." Recommended rhythm: run this before every commit that closes a feature — and after any auth, payments, or data-access work, follow it with `studio-develop-security-audit`.
