---
name: develop-migrate
description: >-
  Plans the move of an app off a prompt-to-app platform (Lovable, Bolt, v0, Base44, Replit Agent)
  into the user's own repo, stack, and coding agent: inventories what the platform owns, checks
  current export mechanics, and writes docs/MIGRATION.md, a phased checkbox plan ending in a
  verification gate before the old platform is decommissioned. Use when the user says "migrate from
  Lovable", "leave Bolt", or "own my codebase". Not for improving the code — use
  develop-refactor-plan afterwards.
---

# Develop: Migrate

Move an app off a prompt-to-app platform and into the member's own repo, stack, and coding agent — completely, safely, and once. The output is **`docs/MIGRATION.md`**: a phased plan in the standard ProductOS task format, executable by the coding agent, that ends with a verification gate. Nothing on the old platform is paused or deleted until that gate passes.

Two rules frame the whole session:

1. **Migration is not refactoring.** This skill moves and rewires what exists; it does not restructure or improve it. Code-quality work (service layers, dead platform shims, prop drilling, styling convergence) belongs to `develop-refactor-plan`, run after the app is living safely in its new home. Keeping the two separate keeps both plans small and verifiable.
2. **Clean break.** The moment export happens, the old platform's editor is retired — the repo becomes the single source of truth. Editing in both places loses work silently: platform exports are point-in-time snapshots, and changes made platform-side after export are gone.

## Inputs

Read inputs from `docs/` and the guides from `productos/develop/` at the app repo root:

1. **`docs/DEFINE.md`** — if present, the canon for what the app is; useful for the verification gate's core-flow list. Not required.
2. **`productos/develop/guides/TECH-STACK-OPTIONS.md`** — the stack recommendations the target should be chosen from.
3. **The platform project itself** — the member demonstrates or describes it; if a repo export already exists, read it directly.

Standalone fallback: with no ProductOS folder, run the same session and write `docs/MIGRATION.md` at the repo root.

## Workflow

### 1. Inventory the platform wiring

Before anything moves, build the complete picture of what the platform currently does for this app. Work through this list with the member, checking each concretely — "sort of" answers hide the thing that breaks in production:

- **Code & export path** — is there GitHub sync (some platforms put it behind a paid plan — check, since it may be the one platform charge the migration can't avoid) or a zip export? Is the synced repo current?
- **Hosting & deploys** — platform-hosted URL, build pipeline, preview environments.
- **Database** — platform-managed cloud (e.g. Lovable Cloud) vs an external service the member owns (e.g. their own Supabase). This single answer sets the migration's difficulty class.
- **Auth** — platform-managed users? External provider (Clerk, Supabase Auth)? OAuth providers configured platform-side (client IDs, secrets, redirect URLs)?
- **Environment variables & secrets** — API keys the platform injects. **Secrets never export**; every one must be inventoried by name now and re-entered (or better, rotated) at the destination.
- **Storage** — buckets, uploaded files, and anywhere the app stores **signed URLs** — those URLs change after migration and stale ones break silently.
- **Server functions & scheduled jobs** — edge functions, cron jobs, and the URLs they call (platform-era URLs become zombies that must be hunted down and re-pointed).
- **Webhooks pointing IN** — Stripe endpoints, OAuth callbacks, email provider callbacks that currently target platform URLs. These break the moment the platform is paused, not the moment code moves — easy to miss, expensive to discover.
- **Custom domain & DNS** — where DNS points today; SSL. Cutover is the last step, never an early one.
- **Everything else** — email sending, analytics, error tracking, payment providers.

Record the inventory as a table: *item → where it lives now → where it's going → migration action → how we verify it*. This table becomes the skeleton of the plan.

### 2. Recommend the target stack

One rule: **keep what the member already owns; replace only what the platform owns.** An external Supabase, Stripe, or Clerk account migrates by re-pointing, not rebuilding. For each platform-owned piece, recommend the standard equivalent from `productos/develop/guides/TECH-STACK-OPTIONS.md` (hosting: its Hosting & Deployment section's **Default**) — the common shape is: GitHub repo as source of truth, Vercel (or similar) for hosting and previews, the platform's managed database moved to the member's own Supabase project, and the member's coding agent (Claude Code / Codex / Cursor) as the development tool. Present the recommendation with the one-line reason per piece, and let the member decide anything contested.

### 3. Research the platform's export mechanics — live

Export paths change fast. Read [references/platform-notes.md](references/platform-notes.md) for what's known per platform, then do a quick web check on this platform's export mechanics before writing the plan: what the official export includes (database schema, data, access policies, auth users — and whether password hashes come along so logins survive), what it excludes (typically secrets, OAuth provider configs, storage files), and any documented traps. If web search isn't available, say so, ask the member what their platform's export screen offers, and mark those Notes lines unverified. Fold what's found into the plan's Notes lines — the plan should read as current, not as folklore.

### 4. Write `docs/MIGRATION.md`

First show the member the phase outline — which of the phases below apply, each with its Goal and a rough task count — and get approval. Then write the plan with the same format discipline as `docs/ROADMAP.md` and `docs/REFACTOR.md`: a header with the generated-by note and a `**Status:** 0/{total} tasks complete` line, phases with a one-sentence Goal, and tasks in the canonical three-line checkbox format from `productos/develop/guides/ROADMAP-GENERATION.md` (Notes ending with `Verify:`), sized to one agent session and ordered for sequential execution. The canonical phase shape — adapt to the inventory, cut phases that don't apply:

1. **Export & baseline** — GitHub sync/export; tag the commit as the migration baseline; capture a baseline inventory of the working app (core flows, screenshots, user count, storage file list) that the gate will compare against. From here: clean break.
2. **Environment & secrets** — `.env.example` documenting every variable by name; secrets re-entered at the destination and **rotated where the platform held them**; nothing committed.
3. **Backend move** *(only when the platform owns it)* — database dump/restore into the member's own project; auth users restored (verify a real login with an original password); storage files transferred and re-uploaded; edge functions redeployed from the repo; cron jobs recreated with fresh URLs and the old zombie URLs hunted out of the codebase; OAuth providers recreated (client ID, secret, redirect URLs).
4. **Re-point the world** — every webhook and callback that targeted platform URLs (Stripe first), API base URLs in the client, stored signed URLs regenerated.
5. **Deploy target** — hosting project created, env vars set, build green, preview and production deploys working. DNS cutover staged but **not executed yet**.
6. **Agent workflow** — root `CLAUDE.md`/`AGENTS.md` wired from `productos/setup/` (via `setup` if not already done), platform compat shims and platform-only files removed, lockfile and dependency sanity pass.
7. **The gate, then goodbye** — walk every core flow against the phase-1 baseline: login with a pre-migration account, the payment path in test mode, uploads and stored-file URLs, each scheduled job fired once. **All green → DNS cutover → run the old platform in parallel for a few quiet days → pause, then remove it.** Anything red → stop; the old platform stays untouched until it's green.

### 5. Verify before delivering

Re-read `docs/MIGRATION.md` and check:

- [ ] Every inventory row (item → now → going → action → verify) maps to at least one task, and every secret is listed by name with a re-enter-or-rotate task.
- [ ] Webhooks and callbacks pointing at platform URLs each have a re-point task.
- [ ] The plan migrates only — no refactoring tasks crept in.
- [ ] Export-mechanics Notes lines reflect the live check, or are marked unverified.
- [ ] DNS cutover and decommissioning sit behind phase 7's gate; nothing on the old platform is paused or removed before every flow is green.
- [ ] The status line total matches the task count.

### 6. Hand off

To execute the plan, the member tells `build-loop` to work through `docs/MIGRATION.md` top to bottom; it is a build-loop plan file like `docs/ROADMAP.md`. Phase 7's gate needs the member present for the real login, DNS cutover, and decommission.

Summarize in conversation: what moved, what was rotated, what was decommissioned, and the baseline tag to roll back to. Then point forward: `develop-refactor-plan` for the code-quality pass the platform's generated code almost certainly needs (it generates its own refactor-scoped PRD if none exists), and the member's build loop for everything after.

Done means the app runs entirely from the member's repo, stack, and agent; every inventory row shows its Verify pass; secrets the platform ever held are rotated; `docs/MIGRATION.md` shows all tasks checked with the gate green; and the old platform is paused or removed — in that order, never the reverse. Anything less: the old platform stays alive and the gap is named in the plan.
