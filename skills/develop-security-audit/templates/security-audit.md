# Security audit report template

The exact shape of `docs/SECURITY-AUDIT.md` — one canonical file, overwritten each run. Fill every bracket; omit **Do this right now** when no credential leaked. Every fix task's **Verify** line is a falsifiable assertion an agent can mechanically confirm — never "improve validation."

```markdown
# Security Audit — [app name]

*Audited [YYYY-MM-DD, from `date`] by develop-security-audit. Scope: [whole codebase | uncommitted changes]. Stack: [detected].*

## Verdict
[One line a founder can act on: "**Not safe to launch** — 2 critical issues let any visitor read every user's data."
 or "**Safe to launch** — no critical or high findings; 3 medium items below."]

## Do this right now
[Only when credentials leaked: rotation steps FIRST — the key is in git history and is compromised
 no matter what the code says. Omit the section when clean.]

## Findings
| # | Severity | Category (OWASP) | Location | What an attacker can do |
[one row per verified finding, severity-ordered]

## What's already secure
[Evidence-backed credit: "Auth: Clerk with server-side session checks (`middleware.ts:8`)."
 Proves coverage; the audit checked it, it passed.]

## Fix plan — agent-executable

> Work top to bottom. Mark tasks `[x]` as completed. Each Verify line must pass before the task counts.

- [ ] **SEC-001 — [Fix title]** ([SEVERITY])
  Files: `path/to/file.ts`
  Notes: [the specific change and why]. Verify: [a falsifiable assertion — "unauthenticated GET /api/orders returns 401", "`git ls-files .env` returns nothing"].

[…severity-ordered; one concern per task; sized to one agent session]

## Human-only actions
- [ ] [Dashboard/hosting/key-rotation steps an agent cannot perform, each with where and how]
- [ ] Manual test: log in as user A, take a resource ID, log in as user B, try to read and delete it. Expect 403 on both.

## Excluded from this audit
[What wasn't in scope (infrastructure, third-party provider internals) and what was deliberately
 not reported (DoS, theoretical races, hardening-without-exploit) — omissions are decisions, not gaps.]
```
