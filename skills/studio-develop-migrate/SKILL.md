---
name: studio-develop-migrate
description: Use inside (or alongside) an app built on a prompt-to-app platform — Lovable, Bolt, v0, Base44, Replit Agent, and similar — when the user wants to move it into their own repository and a developer agent tool like Claude Code, Codex, or Cursor. Triggers on phrases like "migrate from Lovable", "get my app out of Lovable", "move my project to Claude Code", "leave Bolt/v0/Base44", "own my codebase", "migration plan", or any request to take a platform-built app to a self-owned repo, stack, and deployment. Inventories everything the platform manages (hosting, database, auth, secrets, storage, functions, webhooks, domains), recommends the target stack, researches the platform's current export mechanics live, and writes `docs/MIGRATION.md` — a phased, checkbox-tracked plan the coding agent executes, ending with a verification gate before the old platform is decommissioned. Migration moves and rewires; it does not improve code — run `studio-develop-refactor-plan` afterwards for that.
---

# Develop: Migrate

Move an app off a prompt-to-app platform and into the member's own repo, stack, and coding agent — completely, safely, and once. The output is **`docs/MIGRATION.md`**: a phased plan in the standard ProductOS task format, executable by the coding agent, that ends with a verification gate. Nothing on the old platform is paused or deleted until that gate passes.

Two rules frame the whole session:

1. **Migration is not refactoring.** This skill moves and rewires what exists; it does not restructure or improve it. Code-quality work (service layers, dead platform shims, prop drilling, styling convergence) belongs to `studio-develop-refactor-plan`, run after the app is living safely in its new home. Keeping the two separate keeps both plans small and verifiable.
2. **Clean break.** The moment export happens, the old platform's editor is retired — the repo becomes the single source of truth. Editing in both places loses work silently: platform exports are point-in-time snapshots, and changes made platform-side after export are gone.

> **Session shape:** one sitting to inventory, decide the stack, and write the plan (45–60 min); the coding agent then executes the plan over one to a few sessions depending on how much backend the platform owned. Small frontend-only apps migrate in an hour or two; apps where the platform owns the database, auth, and functions are a half-day of careful work.

## Inputs

Locate in the ProductOS folder (`productos/` at the app repo root, or the current folder in a standalone checkout) and the repo-root `docs/`:

1. **`docs/PRODUCT.md`** — if present, the canon for what the app is; useful for the verification gate's core-flow list. Not required.
2. **`productos/develop/guides/TECH-STACK-OPTIONS.md`** — the stack recommendations the target should be chosen from.
3. **The platform project itself** — the user demonstrates or describes it; if a repo export already exists, read it directly.

Standalone fallback: with no ProductOS folder, run the same session and write `docs/MIGRATION.md` at the repo root.

## Workflow

### 1. Inventory the platform wiring

Before anything moves, build the complete picture of what the platform currently does for this app. Work through this list with the user, checking each concretely — "sort of" answers hide the thing that breaks in production:

- **Code & export path** — is there GitHub sync (Lovable: a paid-plan feature, and the one platform charge the migration can't avoid) or a zip export? Is the synced repo current?
- **Hosting & deploys** — platform-hosted URL, build pipeline, preview environments.
- **Database** — platform-managed cloud (e.g. Lovable Cloud) vs an external service the user owns (e.g. their own Supabase). This single answer sets the migration's difficulty class.
- **Auth** — platform-managed users? External provider (Clerk, Supabase Auth)? OAuth providers configured platform-side (client IDs, secrets, redirect URLs)?
- **Environment variables & secrets** — API keys the platform injects. **Secrets never export**; every one must be inventoried by name now and re-entered (or better, rotated) at the destination.
- **Storage** — buckets, uploaded files, and anywhere the app stores **signed URLs** — those URLs change after migration and stale ones break silently.
- **Server functions & scheduled jobs** — edge functions, cron jobs, and the URLs they call (platform-era URLs become zombies that must be hunted down and re-pointed).
- **Webhooks pointing IN** — Stripe endpoints, OAuth callbacks, email provider callbacks that currently target platform URLs. These break the moment the platform is paused, not the moment code moves — easy to miss, expensive to discover.
- **Custom domain & DNS** — where DNS points today; SSL. Cutover is the last step, never an early one.
- **Everything else** — email sending, analytics, error tracking, payment providers.

Record the inventory as a table: *item → where it lives now → where it's going → migration action → how we verify it*. This table becomes the skeleton of the plan.

### 2. Recommend the target stack

One rule: **keep what the user already owns; replace only what the platform owns.** An external Supabase, Stripe, or Clerk account migrates by re-pointing, not rebuilding. For each platform-owned piece, recommend the standard equivalent from `productos/develop/guides/TECH-STACK-OPTIONS.md` — the common shape is: GitHub repo as source of truth, Vercel (or similar) for hosting and previews, the platform's managed database moved to the user's own Supabase project, and the user's coding agent (Claude Code / Codex / Cursor) as the development tool. Present the recommendation with the one-line reason per piece, and let the user decide anything contested.

### 3. Research the platform's current export mechanics — live

Export paths change fast (Lovable shipped official backend **Export / Pause / Remove** controls in mid-2026; before that the community relied on workarounds). Do a quick, current web check on the specific platform's export mechanics before writing the plan: what the official export includes (Lovable's backend export is a native `pg_dump` carrying schema, data, RLS policies, triggers, sequences, and auth users **with password hashes** — logins survive), what it excludes (secrets, OAuth provider configs, storage files fetched separately), and any documented traps. Fold what's found into the plan's Notes lines — the plan should read as current, not as folklore.

### 4. Write `docs/MIGRATION.md`

Same format discipline as `docs/ROADMAP.md` and `docs/REFACTOR.md`: a header with the generated-by note and a `**Status:** 0/{total} tasks complete` line, phases with a one-sentence Goal, and tasks in the three-line checkbox format (`- [ ] **TASK-001** — … / Files: / Notes: … Verify: …`), sized to one agent session and ordered for sequential execution. The canonical phase shape — adapt to the inventory, cut phases that don't apply:

1. **Export & baseline** — GitHub sync/export; tag the commit as the migration baseline; capture a baseline inventory of the working app (core flows, screenshots, user count, storage file list) that the gate will compare against. From here: clean break.
2. **Environment & secrets** — `.env.example` documenting every variable by name; secrets re-entered at the destination and **rotated where the platform held them**; nothing committed.
3. **Backend move** *(only when the platform owns it)* — database dump/restore into the user's own project; auth users restored (verify a real login with an original password); storage files transferred and re-uploaded; edge functions redeployed from the repo; cron jobs recreated with fresh URLs and the old zombie URLs hunted out of the codebase; OAuth providers recreated (client ID, secret, redirect URLs).
4. **Re-point the world** — every webhook and callback that targeted platform URLs (Stripe first), API base URLs in the client, stored signed URLs regenerated.
5. **Deploy target** — hosting project created, env vars set, build green, preview and production deploys working. DNS cutover staged but **not executed yet**.
6. **Agent workflow** — root `CLAUDE.md`/`AGENTS.md` wired from `productos/setup/` (via `studio-setup` if not already done), platform compat shims and platform-only files removed, lockfile and dependency sanity pass.
7. **The gate, then goodbye** — walk every core flow against the phase-1 baseline: login with a pre-migration account, the payment path in test mode, uploads and stored-file URLs, each scheduled job fired once. **All green → DNS cutover → run the old platform in parallel for a few quiet days → pause, then remove it.** Anything red → stop; the old platform stays untouched until it's green.

### 5. Hand off

Summarize in conversation: what moved, what was rotated, what was decommissioned, and the baseline tag to roll back to. Then point forward: `studio-develop-refactor-plan` for the code-quality pass the platform's generated code almost certainly needs (it generates its own refactor-scoped PRD if none exists), and the member's build loop for everything after.

## What "done" looks like

The app runs entirely from the member's repo, stack, and agent; every inventory row shows its Verify pass; secrets the platform ever held are rotated; `docs/MIGRATION.md` shows all tasks checked with the gate green; and the old platform is paused or removed — in that order, never the reverse. Anything less: the old platform stays alive and the gap is named in the plan.
