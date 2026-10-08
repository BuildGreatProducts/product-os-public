# Shape adaptations — the audit for products without screens

Read at step 1 when the primary shape is anything other than `web-app`, `mobile-app`, `desktop-app`, or `browser-extension`. The eight areas and the scoring stay the same; what counts as activation, retention, a "location", and the evidence changes. Where an area genuinely doesn't apply, write its table as a single row: `N/A — [one-line reason]` — never drop the area silently.

## Contents

- [Activation, retention, and evidence by shape](#activation-retention-and-evidence-by-shape)
- [The eight areas, adapted](#the-eight-areas-adapted)
- [Instrumentation options by shape](#instrumentation-options-by-shape)

## Activation, retention, and evidence by shape

The activation event is the shape's **first successful output**, as the shape file's `## Distribute notes` (and `docs/MAGIC-MOMENT.md`) name it. Retention is **repeat invocation or repeat purchase**, not logins.

| Shape | Activation (first successful output) | Retention (repeat use) | Where the evidence lives |
| --- | --- | --- | --- |
| `agent-plugin`, `agent-skill` | installed, triggered, and produced the output the member promised | invoked again in later sessions; still installed after 30 days | the plugin/skill files (descriptions, commands, hooks, README), any licence or telemetry code |
| `mcp-server` | a client connected and a tool call returned a useful result | tool calls per key or account, week over week | server code, auth, logs |
| `chat-assistant` | a conversation that completed the job | returning conversations or workspace users | the assistant's instructions, bot code, the platform's analytics |
| `developer-tool` | first successful API call, CLI command, or SDK integration | calls per key or active installs, week over week | code, docs, API logs |
| `productized-service` | the first deliverable accepted by the client | renewal or a repeat order | intake forms, delivery records, the CRM or sheet, the billing dashboard |
| `digital-product` | the buyer downloaded it and used it (opened the template, finished module one) | repeat purchases, updates opened, a low refund rate | checkout platform, delivery emails, the product's start-here page |
| `website` | the visitor got the value (found the resource, subscribed, joined) | return visits, newsletter opens | site code, analytics, newsletter platform |

**Retention model** (step 1): a plugin, skill, MCP server, or developer tool used in daily work is *daily/weekly*; a chat assistant follows its job's frequency; a productized service is *renewal-cycle* (judge against renewal rate, not visits); a digital product is *occasional* (judge against repeat purchase and refunds, never daily mechanics).

**Location** for a finding is a file and line where there is code (`README.md:12`, `skills/x/SKILL.md` description, `server/auth.ts:40`), otherwise the named system and setting (`Stripe → subscription settings → retries`, `intake form, question 6`, `Gumroad → delivery email`).

## The eight areas, adapted

| Area | Agent and developer shapes (`agent-plugin`, `agent-skill`, `mcp-server`, `chat-assistant`, `developer-tool`) | `productized-service` | `digital-product` | `website` |
| --- | --- | --- | --- | --- |
| **A. Time-to-Value** | count steps from install command to first successful output (install, account, key, config, first prompt); flag config before the first output | days from payment to the first deliverable; flag anything the client must do first | steps from purchase to first use; flag a product with no obvious first step | clicks from landing to the value; flag content buried behind navigation |
| **B. Gating** | an account, API key, licence key, or OAuth scope demanded before any output; broad permission or tool scopes requested up front | intake forms asking for more than the first deliverable needs; a mandatory kickoff call before work starts | account creation required to download | signup or cookie walls before any content |
| **C. Empty states** | what happens on first invocation with no config or data: does the error say exactly what to do next? Does the skill's description match how people ask, so it triggers at all? (A skill that never fires is the blank screen.) | N/A unless there is a client portal — the "empty state" is silence after payment, which belongs in A | the start-here page or first module: is there one? | empty search results, empty directory categories |
| **D. Onboarding** | the README quickstart, setup command, and first-run message: one copy-paste path to the first output | the welcome email and intake sequence | the welcome/delivery email and the start-here page | N/A for most sites — or the newsletter/community welcome |
| **E. Re-engagement** | usually no channel to the user: flag the absence of an owned contact (email at licence or download), release notes, and marketplace update notes. Chat assistants in workspaces can message — flag over-messaging as much as silence | status updates and a reporting cadence the client sees | buyer emails: updates, how-to tips, the next product | newsletter and its welcome series |
| **F. Return loop & stored value** | saved config, memory, files the tool writes into the project, hooks or scheduled tasks that make it part of the workflow | accumulated history, reports, assets the client would lose by leaving | updates and additions that keep the product current | saved lists, accounts, a reason to come back weekly |
| **G. Churn & win-back** | paid licence or subscription: cancel flow, failed-payment dunning, uninstall feedback. Free and open-source with no account: N/A — no churn surface to audit | renewal reminders, cancellation reason, failed-payment dunning, pause instead of cancel | refund flow and refund-reason capture | unsubscribe reason capture |
| **H. Instrumentation** | see below | see below | see below | see below |

## Instrumentation options by shape

Measure the activation event and repeat use with the least invasive option that answers the question. Anything that sends data from the customer's machine is **opt-in, disclosed in the README and listing, and never includes prompts, file contents, or customer data**. Flag hidden or default-on telemetry as a P0 trust finding, not a win.

- **`agent-plugin`, `agent-skill`:** opt-in telemetry (an anonymous "invoked / succeeded" event); usage logs the tool writes locally that the member can ask users to share; licence-check pings (count active installs per key); marketplace install counts; GitHub traffic and clone stats; feedback prompts after the first output.
- **`mcp-server`:** server-side logs per account or key: connections, tool calls, errors, and the first successful call per account; auth events. This is the richest instrumentation of any agent shape — use it.
- **`chat-assistant`:** the platform's own analytics (conversation counts, ratings, workspace installs and active users), plus server logs for any backend it calls.
- **`developer-tool`:** API logs per key (first successful call, calls per week, error rate); opt-in CLI telemetry; registry download counts as a weak signal only.
- **`productized-service`:** delivery records (date paid, date delivered, revisions, accepted), renewals and cancellations in the billing system, client satisfaction after each delivery — a sheet or CRM is enough.
- **`digital-product`:** downloads, refunds and refund reasons, repeat purchases, and delivery-email opens from the checkout platform's dashboard; a "start here" link click as the activation proxy.
- **`website`:** page analytics with return-visitor cohorts, newsletter opens and clicks, signups.
