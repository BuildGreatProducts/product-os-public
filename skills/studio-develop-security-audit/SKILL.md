---
name: studio-develop-security-audit
description: Use for a full security audit of the app — the whole codebase or just uncommitted changes — producing docs/SECURITY-AUDIT.md, a verdict-first report with a checkbox fix plan a coding agent can execute. Triggers on phrases like "security audit", "is my app secure", "check for vulnerabilities", "audit my code for security", "am I safe to launch", "security review of my codebase", or any request to find security problems before or after launch. Runs in the app repo — the repository that contains `productos/`. Detects the stack (framework, database, auth, payments), maps the attack surface, audits by severity tier (secrets, database access control, unprotected routes, IDOR, exposed keys first), verifies every finding to a concrete exploit path before reporting, and separates agent-executable fixes from human-only actions like key rotation. Never auto-fixes. Works standalone in any repo.
---

# Develop: Security Audit

A full security audit of the member's app, built for how these apps are actually built — fast, with AI agents, by founders who are not security engineers. The research is blunt: most AI-generated code is functionally correct and insecure, and the incidents that killed real founder apps came from a short list — committed secrets, databases without row-level security, unprotected API routes, missing ownership checks, and secret keys shipped to the browser. This skill audits that list first, verifies every finding to a concrete exploit path, and writes **`docs/SECURITY-AUDIT.md`**: a verdict, the findings, and a fix plan a coding agent can execute while the member keeps building.

**Boundary with the sibling skills:** the build loops run their tool's security pass per task on sensitive surfaces; `studio-develop-code-review` carries only a thin pre-commit check (secrets, missing auth). **This skill owns depth**: the whole attack surface, the full category list, and the durable report. Run it before go-live, and again after any significant auth, payments, or data-access work.

**This skill never auto-fixes.** A wrong "fix" to auth middleware can lock a founder out of their own app. It reports; execution is a separate, explicit step the member chooses.

The voice is a senior application-security engineer auditing a small production app — precise about exploitability, allergic to theater. Every finding must name what an attacker can actually do. Findings that amount to "this isn't best practice" don't ship; a report full of noise teaches the member to ignore reports.

> **Session length:** 30–60 minutes for a full-codebase audit; 10–20 for uncommitted-changes scope.

## Workflow

### 1. Scope and stack

Ask one question: **whole codebase, or just the uncommitted changes?** (Default whole codebase; uncommitted-only uses the same `git diff HEAD` + untracked-files scoping as `studio-develop-code-review`.)

Then detect the stack before judging anything — framework, database layer (Supabase / Firebase / Prisma / raw SQL), auth provider (Clerk / Auth0 / NextAuth / Supabase Auth / custom), payment provider, hosting config. **The stack decides which categories apply.** Managed providers make whole categories N/A — "weak password hashing: N/A, Clerk manages credentials" is a correct and required audit line, not a gap. Auditing for problems the stack can't have is the fastest way to a noise report.

### 2. Map the attack surface

Enumerate before judging — the map is the audit's evidence base and goes in the report:

- Every **route/endpoint**: method, whether auth runs before the handler, whether it takes a resource ID.
- Every **database table/collection** and its RLS / rules status.
- Every **environment variable** and where it's referenced — especially anything behind a public prefix (`NEXT_PUBLIC_*`, `VITE_*`, `REACT_APP_*`, `EXPO_PUBLIC_*`).
- Every **webhook receiver**, and whether it verifies signatures.
- Every **user-input entry point** and **file-upload path**.

### 3. Audit by tier, one category at a time

Work the tiers in order — never batched, never sampled. Classify each category **CRITICAL / HIGH / MEDIUM / LOW / PASS / N/A**, and for every N/A state why.

**Tier 1 — the five that took down real apps. Audit these first, always:**

1. **Secrets exposure** — `.env` tracked in git (`git ls-files` + history), keys hardcoded in source, secrets placed behind public env prefixes (a `NEXT_PUBLIC_` secret ships to every browser).
2. **Database access control** — Supabase: RLS enabled on *every* table, policies scoped to `auth.uid()`, no `USING (true)`; Firebase: rules require auth, no open reads/writes; self-hosted DBs not bound to `0.0.0.0` without auth.
3. **Unprotected API routes** — from the surface map: every route where auth doesn't demonstrably run before the handler; admin routes that check login but not role.
4. **Broken object-level authorization (IDOR)** — routes taking a resource ID must verify *ownership*, separately from authentication, on reads **and** writes. This is the most common real vulnerability in AI-built apps: logged-in user A editing user B's data by changing an ID.
5. **Secret keys reachable by the browser** — see the key-identity rules below; `service_role` / `sk_live_` anywhere client-reachable is Critical.

**Tier 2 — High:** SQL/NoSQL injection (raw queries built from input — f-strings, template literals); XSS *only* via the framework escape hatches (`dangerouslySetInnerHTML`, `innerHTML`, `v-html` — React/Vue/Angular are otherwise safe by default); unverified webhooks (Stripe/Clerk/GitHub signature checks + idempotency); wildcard or reflected CORS, especially with `credentials: true`; SSRF where user input controls the **host or protocol** (path-only is not a finding); command injection / `eval` / unsafe deserialization; dependency risk — packages that don't exist on the registry (AI-hallucinated names) or carry known critical vulns (`npm audit` / `pip audit`); **missing rate limiting on auth endpoints** (login, register, password reset — credential stuffing is script-kiddie easy); JWT flaws (`algorithm: none`, unverified signatures, no expiry).

**Tier 3 — Medium/Low:** CSRF protection / `SameSite` cookie config; security headers (CSP, HSTS, X-Frame-Options, X-Content-Type-Options); insecure file uploads (extension-only validation, no server-side size limit, uploads served from the app domain); verbose errors / stack traces / debug mode reachable in production; PII in logs.

Tag each finding with its OWASP Top 10 (2025) ID for reference — but the tiers, not OWASP, order the report; the tiers are ordered by what actually burns founders.

**Key identity — the rules that prevent both the worst false positive and the worst miss:**

- `SUPABASE_ANON_KEY` / `NEXT_PUBLIC_SUPABASE_ANON_KEY` in frontend code is **correct and intended** — it is not a secret, and flagging it is a false positive. Same for Stripe `pk_live_*` and the Firebase web `apiKey`.
- `SUPABASE_SERVICE_ROLE_KEY` or Stripe `sk_live_*` anywhere the browser can reach — client bundles, public env prefixes, frontend fetch headers — is **Critical**: it bypasses all access control.
- The anon key is only safe **because of RLS**. So when RLS is off, the finding is never "anon key exposed" — it is *"RLS disabled on table X; the (correctly public) anon key therefore grants anyone read/write on it."* Name the real problem.

### 4. Verify every finding

Detection is generous; the report is not. Before a finding ships, re-examine it against the code and demand a **concrete exploit path** — who the attacker is, what they send, what they get. Drop anything below roughly 8/10 confidence. Judge new code against *this codebase's* existing security patterns, not an abstract ideal.

**Never report** (noise, not findings): denial-of-service or resource-exhaustion scenarios; theoretical race conditions; missing hardening without a concrete exploit ("should add a CSP" is a Tier-3 *category check*, not a per-file finding); missing auth checks in *client-side* code (the server owns authorization — client checks are UX); XSS in React/Angular/Vue outside the escape hatches; attacks requiring control of env vars or CLI flags (those are trusted); missing audit logs; findings in documentation or test-only files.

**Always report** (commonly excluded by enterprise tools only because enterprises have separate systems for them — founders don't): committed or exposed secrets, missing rate limiting on auth endpoints, and vulnerable or hallucinated dependencies.

### 5. Write `docs/SECURITY-AUDIT.md`

One canonical file at the app repo root, overwritten each run (create `docs/` if needed), in exactly this shape:

```markdown
# Security Audit — [app name]

*Audited [date] by studio-develop-security-audit. Scope: [whole codebase | uncommitted changes]. Stack: [detected].*

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

Every fix task's **Verify** line is a falsifiable assertion an agent can mechanically confirm — never "improve validation." The **Do this right now** section outranks everything: rotating a leaked key comes before fixing the code that leaked it.

### 6. Hand off execution

Close the session with the verdict, the finding count by severity, and the one instruction: *"To execute the fixes, tell your coding agent to work through the Fix plan in `docs/SECURITY-AUDIT.md` top to bottom, marking tasks complete — or point your build loop at it. The Human-only actions are yours; do the 'right now' section first."* After the fixes land, offer a re-audit of the changed surface to confirm the Verify lines pass.

## What "done" looks like

A `docs/SECURITY-AUDIT.md` where the verdict is one honest line; every finding has a location and a named attacker capability; the anon-key/service-role distinction was applied correctly; every N/A says why; the fix plan is severity-ordered checkbox tasks with falsifiable Verify lines an agent can execute unattended; human actions (rotation first) are separate and specific; and the excluded list shows the omissions were deliberate. A member who reads only the verdict and the "Do this right now" section already knows the two things that matter most.
