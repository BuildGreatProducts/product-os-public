# Platform export notes

## Platform notes — last reviewed October 2026 (re-verify with web search before quoting)

Export mechanics on prompt-to-app platforms change fast. Use these as the starting point for step 3's live check, not as the answer; fold only what the live check confirms into the plan. If web search isn't available, say so, use these notes, and mark the affected Notes lines "unverified — confirm in the platform's docs before running."

### Lovable
- **GitHub sync** is a paid-plan feature — often the one platform charge the migration can't avoid. *(Source not recorded — check Lovable's pricing page.)*
- **Lovable Cloud** is the platform-managed backend (database, auth, storage, functions); an app on it is in the harder migration class than one wired to the member's own Supabase.
- **Official backend Export / Pause / Remove controls** shipped in mid-2026; before that the community relied on workarounds. *(Source not recorded — check Lovable's docs and changelog.)*
- **What the backend export includes:** a native `pg_dump` carrying schema, data, RLS policies, triggers, sequences, and auth users **with password hashes** — so existing logins survive the move.
- **What it excludes:** secrets, OAuth provider configs, and storage files (fetched separately).

### Bolt, v0, Base44
- No notes recorded yet — rely on the live check in step 3.
