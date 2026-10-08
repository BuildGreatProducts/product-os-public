---
name: develop-code-review
description: >-
  Runs the ProductOS pre-commit review of uncommitted changes (working tree, staged, and untracked
  files): states what the change is for, checks correctness, regressions, edge cases, a light
  security pass, and consistency, verifies every finding in the source, and ends with a
  ready-to-commit verdict. Use when the user says "review my changes before I commit" or "am I ready
  to commit". Works in any repo. Not for a pull request or branch — use a PR review tool; not for a
  full security audit — use develop-security-audit.
---

# Develop: Code Review

The deliberate pre-commit review. The build loops run their tool's `/review` in-flight, per task; this skill is the step back — a whole-diff pass over everything currently uncommitted, before it becomes a commit. The output is a conversation, not a file: findings with locations, and a verdict.

**Boundary with the sibling skills:** the build loops (`cc-build-loop` etc.) own in-flight, per-task review while building; `develop-design-review` owns design-system adherence (tokens, components, `docs/DESIGN.md`); `develop-security-audit` owns security depth. **This skill owns the pre-commit correctness pass** — it carries only a thin security check for the two commit-blockers (hardcoded secrets, missing auth on new routes) and hands anything deeper to the audit.

The voice is a senior engineer reviewing a teammate's diff — direct, specific, and calibrated. Not a gatekeeper: the job is to catch what would break, say what's genuinely good in one line, and give a clear verdict. Nitpicks are not findings. A clean small diff deserving "no issues — ready to commit" is a normal, expected outcome, not a failure to look hard enough.

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

### 3. Run the repo's own checks

If the repo defines typecheck, lint, or test commands (`package.json` scripts, a `Makefile`, `pyproject.toml`, the root `CLAUDE.md`/`AGENTS.md`), run them. A check that fails because of the diff is a must-fix; one that was already failing before the change is Pre-existing. If none exist, say so in one line and move on — don't invent a test suite.

### 4. Review across five lenses

One pass per lens over the scoped diff, gathering candidate findings before reporting anything:

1. **Correctness** — does the code do what step 2's stated intent says, on every path it touches?
2. **Regressions & contracts** — changed function signatures or return shapes with un-updated callers; removed or renamed exports still imported elsewhere; schema changes vs. the queries that hit them; API response changes vs. the frontend that consumes them.
3. **Edge cases & error handling** — including failure paths and missing loading/error states on new UI.
4. **Security (thin pass)** — two commit-blockers only: hardcoded secrets or keys anywhere in the diff or untracked files, and new routes/endpoints with no auth check. Anything subtler gets one line: "worth a `develop-security-audit` pass" — don't attempt depth here.
5. **Consistency & reuse** — re-implements an existing helper, deviates from the codebase's own patterns, leftover debug output, commented-out blocks, TODO stubs returning fake data.

### 5. Verify before reporting

Every finding earns its place or gets cut:

- **Behavioral claims need a `file:line` citation in actual source — never an inference from a name.** "This probably breaks the caller" is not a finding until you've read the caller.
- Confirm the broken consumer actually exists and is actually reached.
- Confirm the issue is **in the diff**. If it's real but pre-existing, re-label it Pre-existing — don't drop it, and don't blame today's change for it.
- Cut anything you wouldn't confidently raise reviewing a colleague's PR. Better to miss a theoretical issue than to bury the two real ones in noise.

### 6. Report and give the verdict

Deliver in conversation, in this shape:

- **One-line tally first** — *"2 must-fix, 1 consider, 1 pre-existing"* or *"No blocking issues."*
- **Must fix** — numbered; each with: what (one sentence), why it matters (the failure a user would hit), where it was verified (`file:line`), and the fix (specific, not "handle this better").
- **Consider** — capped at **five**; anything beyond that is a count ("…and 4 smaller nits — ask if you want them"). Never promote a nitpick to must-fix.
- **Pre-existing (not from this change)** — real issues noticed in touched code that today's diff didn't cause. The member should know about the landmine without being blamed for planting it.
- **One line of credit** — something genuinely done well. One line, not a paragraph.
- **Verdict, always explicit:** **Ready to commit** or **Not ready — fix the N must-fix items first.** Never end without one.

## Rules

- **Re-reviews converge.** After the user fixes findings and asks again, check the fixes and report must-fix items only — no new nits on a re-pass. The loop must end.
- **Don't duplicate the machines.** Never flag formatting, import order, or anything the repo's linter/CI already enforces. Don't flag missing tests, except for new logic on the core loop.
- **The spec wins.** If a finding contradicts `docs/PRD.md` or the task's intent, flag the disagreement instead of asserting the code is wrong.
- **Never say "looks good" without having read the code.** The credit line and the verdict are earned by the pass, not by politeness.

## Verify before delivering

- [ ] Every finding cites real source (`file:line`), and every must-fix has a specific fix.
- [ ] The repo's own checks ran (or their absence was stated), and any failure the diff caused is a must-fix.
- [ ] Consider items are capped at five; pre-existing issues are labelled, not blamed on today's change.
- [ ] A small clean diff got a fast, confident "ready."
- [ ] The member knows exactly three things: what must change before committing, what can wait, and whether they're ready to commit — the verdict is explicit.

**Next step:** after any auth, payments, or data-access work, follow this with `develop-security-audit`.
