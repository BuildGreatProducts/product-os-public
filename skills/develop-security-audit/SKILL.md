---
name: develop-security-audit
description: >-
  Audits the whole app (or uncommitted changes) for security problems — secrets, database access
  control, unprotected routes, IDOR, exposed keys first, then agent-tool risks such as prompt
  injection for AI-native products — verifies each finding to a concrete exploit path, and writes docs/SECURITY-AUDIT.md with a launch verdict and a checkbox fix plan that
  separates agent fixes from human-only actions like key rotation. Never auto-fixes. Use when the
  user asks for a "security audit", "is my app secure", or "am I safe to launch". Not for a general
  pre-commit review — use develop-code-review.
---

# Develop: Security Audit

A full security audit of the member's app, built for apps made fast with AI agents by founders who are not security engineers. It audits the short list that burns real founder apps first — committed secrets, databases without row-level security, unprotected API routes, missing ownership checks, secret keys shipped to the browser — verifies every finding to a concrete exploit path, and writes **`docs/SECURITY-AUDIT.md`**: a verdict, the findings, and a fix plan a coding agent can execute while the member keeps building.

**Boundary with the sibling skills:** `build-loop` and `develop-build` run the tool's security pass on sensitive surfaces when they review (`build-loop` once the work is finished, `develop-build` at each phase boundary); `develop-code-review` carries only a thin pre-commit check (secrets, missing auth). **This skill owns depth**: the whole attack surface, the full category list, and the durable report. Run it before go-live, and again after any significant auth, payments, or data-access work.

**This skill never auto-fixes.** A wrong "fix" to auth middleware can lock a founder out of their own app. It reports; execution is a separate, explicit step the member chooses.

The voice is a senior application-security engineer auditing a small production app — precise about exploitability, allergic to theater. Every finding must name what an attacker can actually do; "this isn't best practice" doesn't ship — a noisy report teaches the member to ignore reports.

## Workflow

### 1. Scope and stack

Ask one question: **whole codebase, or just the uncommitted changes?** (Default whole codebase; uncommitted-only uses the same `git diff HEAD` + untracked-files scoping as `develop-code-review`.)

Then read the shape (`docs/DEFINE.md` → `## Product Shape` → `### Primary Shape`; no section → `web-app`) and detect the stack before judging anything — framework, database layer (Supabase / Firebase / Prisma / raw SQL), auth provider (Clerk / Auth0 / NextAuth / Supabase Auth / custom), payment provider, hosting config. **The stack decides which categories apply.** Managed providers make whole categories N/A — "weak password hashing: N/A, Clerk manages credentials" is a correct and required audit line, not a gap. Auditing for problems the stack can't have is the fastest way to a noise report.

**No-code shapes** (`productized-service`, `digital-product`, `website` built in a hosted builder) need this audit only where there is custom code or stored customer data — scripts and automations that touch client files, a custom intake or portal, a database of buyers or members. Audit just that surface; if there is none, say so in one line and stop: the tools' own security is out of scope.

### 2. Map the attack surface

Enumerate before judging — the map is the audit's evidence base and goes in the report:

- Every **route/endpoint**: method, whether auth runs before the handler, whether it takes a resource ID.
- Every **database table/collection** and its RLS / rules status.
- Every **environment variable** and where it's referenced — especially anything behind a public prefix (`NEXT_PUBLIC_*`, `VITE_*`, `REACT_APP_*`, `EXPO_PUBLIC_*`).
- Every **webhook receiver**, and whether it verifies signatures.
- Every **user-input entry point** and **file-upload path**.
- **Agent tools** (when Tier 4 applies) — every tool a model can call (MCP tools, function-calling tools, GPT actions, bot commands) with its permissions and whether it changes or deletes anything; every hook and bundled script; every plugin, MCP, and extension manifest or config; every point where fetched or tool-returned content enters a prompt; every place model output is rendered as links or images.

### 3. Audit by tier, one category at a time

Work the tiers in order — never batched, never sampled. Classify each category **CRITICAL / HIGH / MEDIUM / LOW / PASS / N/A**, and for every N/A state why.

**Tier 1 — the five that took down real apps. Audit these first, always:**

1. **Secrets exposure** — `.env` tracked in git (`git ls-files` + history), keys hardcoded in source, secrets placed behind public env prefixes (a `NEXT_PUBLIC_` secret ships to every browser).
2. **Database access control** — Supabase: RLS enabled on *every* table, policies scoped to `auth.uid()`, no `USING (true)`; Firebase: rules require auth, no open reads/writes; self-hosted DBs not bound to `0.0.0.0` without auth.
3. **Unprotected API routes** — from the surface map: every route where auth doesn't demonstrably run before the handler; admin routes that check login but not role.
4. **Broken object-level authorization (IDOR)** — routes taking a resource ID must verify *ownership*, separately from authentication, on reads **and** writes. This is the most common real vulnerability in AI-built apps: logged-in user A editing user B's data by changing an ID.
5. **Secret keys reachable by the browser** — see the key-identity rules below; `service_role` / `sk_live_` anywhere client-reachable is Critical.

**Tier 2 — High:** SQL/NoSQL injection (raw queries built from input — f-strings, template literals); XSS *only* via the framework escape hatches (`dangerouslySetInnerHTML`, `innerHTML`, `v-html` — React/Vue/Angular are otherwise safe by default); unverified webhooks (Stripe/Clerk/GitHub signature checks + idempotency); wildcard or reflected CORS, especially with `credentials: true`; SSRF where user input controls the **host or protocol** (path-only is not a finding); command injection / `eval` / unsafe deserialization; dependency risk — packages that don't exist on the registry (AI-hallucinated names) or carry known critical vulns (run the ecosystem's audit tool — `npm audit`, `pip-audit` — if available; otherwise check the lockfile against known advisories and say the check was manual); **missing rate limiting on auth endpoints** (login, register, password reset — credential stuffing is script-kiddie easy); JWT flaws (`algorithm: none`, unverified signatures, no expiry).

**Tier 3 — Medium/Low:** CSRF protection / `SameSite` cookie config; security headers (CSP, HSTS, X-Frame-Options, X-Content-Type-Options); insecure file uploads (extension-only validation, no server-side size limit, uploads served from the app domain); verbose errors / stack traces / debug mode reachable in production; PII in logs.

**Tier 4 — Agent tools.** Applies to `agent-plugin`, `agent-skill`, `mcp-server`, and `chat-assistant`, and to any app where a model calls tools — audit it right after Tier 1 for those shapes. Six categories: prompt injection through tool outputs and fetched content; over-broad tool permissions and scopes; secrets in plugin, MCP, and extension configs and manifests; data exfiltration via links and images; unsafe shell in hooks and scripts; missing confirmation on destructive tools. Read [references/agent-tools-tier.md](references/agent-tools-tier.md) whenever Tier 4 applies — it holds each category's checks, severity rules, and the agent-specific never-report list. Severity follows what an injected instruction can make the agent *do*: Critical when untrusted content, private data, and an outbound channel or destructive tool meet in one session.

Tag each finding with its OWASP Top 10 (latest edition) ID for reference (Tier 4 findings: the OWASP Top 10 for LLM Applications ID) — but the tiers, not OWASP, order the report; the tiers are ordered by what actually burns founders.

**Key identity — the rules that prevent both the worst false positive and the worst miss:**

- `SUPABASE_ANON_KEY` / `NEXT_PUBLIC_SUPABASE_ANON_KEY` in frontend code is **correct and intended** — it is not a secret, and flagging it is a false positive. Same for Stripe `pk_live_*` and the Firebase web `apiKey`.
- `SUPABASE_SERVICE_ROLE_KEY` or Stripe `sk_live_*` anywhere the browser can reach — client bundles, public env prefixes, frontend fetch headers — is **Critical**: it bypasses all access control.
- The anon key is only safe **because of RLS**. So when RLS is off, the finding is never "anon key exposed" — it is *"RLS disabled on table X; the (correctly public) anon key therefore grants anyone read/write on it."* Name the real problem.

### 4. Verify every finding

Detection is generous; the report is not. Before a finding ships, re-examine it against the code and demand a **concrete exploit path** — who the attacker is, what they send, what they get. Drop anything below roughly 8/10 confidence. Judge new code against *this codebase's* existing security patterns, not an abstract ideal.

**Never report** (noise, not findings): denial-of-service or resource-exhaustion scenarios; theoretical race conditions; missing hardening without a concrete exploit ("should add a CSP" is a Tier-3 *category check*, not a per-file finding); missing auth checks in *client-side* code (the server owns authorization — client checks are UX); XSS in React/Angular/Vue outside the escape hatches; attacks requiring control of env vars or CLI flags (those are trusted); missing audit logs; findings in documentation or test-only files (for skills and plugins, SKILL.md files, references, and prompts are product code, not documentation).

**Always report** (commonly excluded by enterprise tools only because enterprises have separate systems for them — founders don't): committed or exposed secrets, missing rate limiting on auth endpoints, and vulnerable or hallucinated dependencies.

### 5. Write `docs/SECURITY-AUDIT.md`

One canonical file at the app repo root, overwritten each run (create `docs/` if needed). Get the audit date with `date +%Y-%m-%d` — never guess it. Read [templates/security-audit.md](templates/security-audit.md) and write the report in exactly that shape: Verdict, Do this right now (only when credentials leaked), Findings, What's already secure, Fix plan, Human-only actions, Excluded from this audit.

Every fix task's **Verify** line is a falsifiable assertion an agent can mechanically confirm — never "improve validation." The **Do this right now** section outranks everything: rotating a leaked key comes before fixing the code that leaked it — the key is in git history and is compromised no matter what the code says.

### 6. Verify before delivering

Re-read the written report and check:

- [ ] The verdict is one honest line a founder can act on.
- [ ] Every Tier 1–3 category — and every Tier 4 category when it applies — is classified, and every N/A says why.
- [ ] Every finding has a location, a named attacker capability, and passed the exploit-path check; nothing from the never-report list made it in.
- [ ] The anon-key / service-role distinction was applied correctly.
- [ ] The fix plan is severity-ordered checkbox tasks, one concern each, with falsifiable Verify lines an agent can execute unattended.
- [ ] Human-only actions (rotation first) are separate and specific, and include the user-A / user-B manual ownership test.
- [ ] The excluded list shows the omissions were deliberate.
- [ ] Nothing was auto-fixed.
- [ ] A member who reads only the verdict and the "Do this right now" section already knows the two things that matter most.

### 7. Hand off execution

Close the session with the verdict, the finding count by severity, and the one instruction: *"To execute the fixes, tell your coding agent to work through the Fix plan in `docs/SECURITY-AUDIT.md` top to bottom, marking tasks complete — or point your build loop at it. The Human-only actions are yours; do the 'right now' section first."* After the fixes land, offer a re-audit of the changed surface to confirm the Verify lines pass.
