# BONUS - Agent Extension Onboarding Best Practice

*A bonus asset for ProductOS — principles, a decision tree, and staged tactics for onboarding the three shapes that live inside an AI agent the customer already uses: agent skills (one capability an agent loads), agent plugins (a bundle of skills, commands, agents, hooks, or connectors), and MCP servers (a connector that gives agents tools and data). The patterns are drawn from how the best developer tools and agent extensions get from install to first useful output; platform specifics that change are kept in one dated section at the end.*

---

## Contents

- [The Meta-Rule](#the-meta-rule)
- [The 10 Principles](#the-10-principles)
- [The Decision Tree — Which Onboarding Pattern Should You Build?](#the-decision-tree--which-onboarding-pattern-should-you-build)
- [The 12 Tactics](#the-12-tactics)
- [Worked Example — A Brand-Voice Skill and a CRM MCP Server](#worked-example--a-brand-voice-skill-and-a-crm-mcp-server)
- [Anti-Patterns — What Kills Agent Extension Onboarding](#anti-patterns--what-kills-agent-extension-onboarding)
- [Calibration — What Good Looks Like](#calibration--what-good-looks-like)
- [Platform Notes — last reviewed October 2026](#platform-notes--last-reviewed-october-2026-re-verify-before-quoting)
- [Closing — The One Mental Model That Beats Everything](#closing--the-one-mental-model-that-beats-everything)

---

## The Meta-Rule

> **An agent extension is onboarded twice: once for the human, who has to install it, configure it, and trust it — and once for the agent, which has to discover it and choose it at the right moment from its name and description alone. The magic moment is the first useful output on the customer's own work. Everything before it is plumbing the customer didn't ask for; everything the agent can't understand is a feature that doesn't exist.**

There are no screens to design. The onboarding surfaces are an install line, a config snippet, a post-install message, the descriptions an agent reads, and the first output. Each of them is copy, and each of them is product.

---

## The 10 Principles

### 1. Two Readers, One Flow

The human reads the README, the listing, and the install message. The agent reads the skill description, the command names, and the tool schemas. A flawless install is wasted if the agent never loads the skill; a perfect description is wasted if the install fails. Design both paths and test both.

### 2. Install Is One Line or One Click

Every extra step between "I want this" and "it's installed" loses people. A single copy-paste command per host, or a one-click install where the host supports it, is the bar. If the extension needs a runtime (Node, Python, Docker), say so before the install line, not in an error after it.

### 3. Zero Configuration Before the First Output

Ship defaults that work. Ask for an API key, a workspace ID, or a path only at the moment the extension genuinely needs it — and when it does, ask in the agent's own conversation ("I need your CRM API key — here's where to find it") rather than in a config file the customer has to edit blind.

### 4. The First Output Lands on Their Work

A canned demo proves the extension runs; it doesn't prove it's worth keeping. The first prompt should point at something the customer already has — their repo, their document, their account — so the first output is something they would have had to produce themselves.

### 5. Tell Them Exactly What to Type

After install, the customer is looking at a blank prompt. The single most effective onboarding line is the first prompt, written out: "Try: `/brand-check README.md`" or "Ask: *which deals closed last week?*". One prompt, copy-paste ready, that reliably triggers the magic moment.

### 6. Descriptions Are the Agent's Onboarding

Agents choose skills and tools from their descriptions. A description must say what it does, when to use it, when not to, and what comes back — in the words customers actually use. Vague descriptions mean the agent never reaches for the extension; overlapping descriptions mean it reaches for the wrong one.

### 7. Least Privilege Earns Trust

An extension runs with the agent's access to the customer's files, accounts, or systems. Say what it reads and writes before install, start read-only where possible, and make destructive actions explicit and confirmable. Trust lost on the first run doesn't come back.

### 8. Make It Visible That It Worked

Agents blend outputs into the conversation. Make the extension's contribution legible: the agent names the skill or tool it used, outputs land in a file the customer can open, results cite where the data came from. Invisible value is unattributed value.

### 9. Work With the Host's Grain

The host decides the UX: its command syntax, its permission prompts, its output rendering. Extensions that fight the host — custom pseudo-UIs, walls of formatted text, instructions to change host settings — feel broken. Fit the host's conventions so the extension feels native.

### 10. Every Update Is a Re-Onboarding

Agent extensions update quietly. A renamed command or changed tool schema silently breaks the customer's habits — and the agent's. Keep names stable, version deliberately, and announce changes in a changelog the customer can find from the README.

---

## The Decision Tree — Which Onboarding Pattern Should You Build?

Start at the top. Stop at the first "yes."

**Is it a single skill (or small skill pack) the agent loads by itself when relevant?**
→ Run **#1 The Drop-In Skill.** Install → the customer says a natural trigger phrase → the agent loads the skill → first output on their work. Onboarding effort goes into the description and the first-prompt line.

**Is it a plugin whose value starts from a command the customer runs?**
→ Run **#2 The Starter Command.** Install → the post-install message names one starter command → first output → a help command lists the rest. Never lead with the full command list.

**Is it a local MCP server the customer adds to their client's config?**
→ Run **#3 The Config Snippet.** One tested snippet per client (tabs) → restart or reload → a first prompt that calls one read-only tool → first result on their data.

**Is it a remote MCP server that needs the customer's account?**
→ Run **#4 Connect and Authorize.** Add the server URL → OAuth in the browser → the first tool call returns something real from their account. No API-key copy-paste if OAuth is available.

**Is the extension a companion to a product the customer already uses (a web app's MCP server, an app's plugin)?**
→ Run **#5 Account-Linked.** Install from inside the product ("Connect to your agent") with credentials pre-filled → first output references their workspace by name.

**None of the above and you're stuck?**
→ Default to **#2 The Starter Command.** It gives the customer one obvious thing to do and the agent one unambiguous trigger.

---

## The 12 Tactics

Organized by stage. Build top to bottom.

---

### Stage 1 — Before Install (the README or listing)

#### 1. The Install Line Above the Fold

**Why:** The README or listing is the landing page. The install command — tested, copy-paste ready, with a copy button where the surface allows — belongs in the first screenful, beside a one-sentence promise of the first output.

**Pass threshold:** The install line is visible without scrolling, works on a clean machine, and has one variant per supported host.

#### 2. The Before-and-After Output

**Why:** Customers can't picture what a skill changes. Show the same request with and without the extension — the generic answer and the extension's answer — as text or a screenshot of the host. This is the agent-extension equivalent of a product screenshot.

**Pass threshold:** One real before/after pair near the top, using a realistic input.

#### 3. The Access Statement

**Why:** Customers are installing something that acts with their agent's permissions. A short list of what it reads, what it writes, what leaves the machine, and what it never does removes the main reason careful buyers hesitate.

**Pass threshold:** Read / write / network access stated in plain language before the install line or directly under it.

---

### Stage 2 — Install and Configure (the first two minutes)

#### 4. One Tested Path Per Host

**Why:** Each host installs extensions differently. A generic "add this to your config" leaves the customer to translate. Tabs or headed blocks per host, each tested, each ending in how to confirm it worked.

**Pass threshold:** Every host the listing names has its own install block, verified on a clean setup in the last release cycle.

#### 5. Defaults That Run

**Why:** Every required setting before the first output is a drop-off point. Pick sensible defaults, infer what you can (the repo's language, the workspace's timezone), and defer the rest.

**Pass threshold:** Zero required settings before the first output, or exactly one (the credential) requested in-conversation.

#### 6. The Self-Check

**Why:** When an install half-works, the customer can't tell whether the extension, the host, or their machine is at fault. A status command or a `health` tool that reports "installed, connected, credentials OK, ready" turns a support ticket into a ten-second fix.

**Pass threshold:** One command or tool that confirms readiness and names the fix for each failure it detects.

---

### Stage 3 — The First Command (the next minute)

#### 7. The First Prompt, Printed

**Why:** The post-install moment is the highest-intent moment in the whole flow and the most commonly wasted. Print the exact first prompt — in the install success message, the README, and the listing — and make sure it reliably triggers the magic moment.

**Pass threshold:** One copy-paste first prompt appears at the end of the install path and produces the magic moment in your own testing every time.

#### 8. Trigger-Tested Descriptions

**Why:** A skill that doesn't load when the customer asks naturally looks broken. Test descriptions against the phrasings real customers use — including near-misses that should *not* trigger it — and rewrite until the agent picks correctly. This is what `develop-agent-evals` formalizes.

**Pass threshold:** The starter prompt and at least five natural variants trigger the right skill or tool; near-misses don't.

#### 9. Sample Data for Empty Systems

**Why:** An MCP server pointed at an empty account returns nothing, and nothing feels like failure. Offer a demo dataset, a sandbox workspace, or a prompt that works on public data so the first call returns something meaningful.

**Pass threshold:** The first suggested prompt returns a non-empty, realistic result even on a fresh account.

---

### Stage 4 — The First Output (the magic moment)

#### 10. Output That Shows Its Work

**Why:** The customer needs to see that *the extension* did this, not the agent alone. Name the skill or tool used, cite sources or records touched, and write substantial outputs to a file the customer can open, share, and keep.

**Pass threshold:** The first output is attributable (the extension is named) and keepable (a file, a link, or a clearly delimited block).

#### 11. The Next-Step Line

**Why:** One output is a trial; three are a habit. End each output with one suggested follow-up that uses another capability — the second command, a deeper tool, a scheduled run.

**Pass threshold:** Every first-run output ends with one specific, runnable next step.

---

### Stage 5 — The Habit (the first week)

#### 12. Slot Into an Existing Loop

**Why:** Extensions that need remembering get forgotten. Attach to something the customer already does: a hook that runs on commit, a command that fits the end-of-day review, a scheduled report, a skill that triggers inside work they do daily. Pair it with a visible changelog so updates bring them back rather than break them.

**Pass threshold:** The extension has one recurring trigger in the customer's existing workflow, and a changelog linked from the README.

---

## Worked Example — A Brand-Voice Skill and a CRM MCP Server

*Composite examples to illustrate the patterns — not real products.*

**The brand-voice skill (Pattern #1, Drop-In Skill).** The README opens with one line — the host's install command — then a before/after: a product announcement drafted by the agent alone (generic, exclamation-heavy) beside the same draft with the skill loaded (the brand's cadence, banned words gone). The access statement says it reads files the customer points it at and writes nothing without being asked. The install success message ends: *Try: "rewrite docs/launch.md in our voice."* The description is tested against "make this sound like us", "brand voice check", and "tone pass", and does *not* trigger on "translate this". The first output is a rewritten file with a three-line summary of what changed and why, and a next-step line: *"Run a voice check on your landing page next?"*

**The CRM MCP server (Pattern #4, Connect and Authorize).** The listing shows three client tabs, each with a tested one-click install or config snippet. Connecting opens OAuth; read-only scopes are requested first, with write tools disabled until the customer enables them. The first suggested prompt is *"Which of my deals haven't been touched in 14 days?"* — read-only, guaranteed to return results on any active account, and the answer cites deal names and links back to the CRM. On an empty account, the server answers from a labeled demo dataset and says so. A `crm_status` tool reports connection, scopes, and rate-limit headroom.

---

## Anti-Patterns — What Kills Agent Extension Onboarding

### The README Novel

Twelve sections of architecture before the install line. Customers skim for the command; bury it and they leave. **Install line and first prompt first; architecture last.**

### The Config Maze

Five environment variables, a JSON file to hand-edit, and a restart before anything happens. **Defaults that run; one credential, asked for in conversation.**

### The Silent Install

The install succeeds and nothing tells the customer what to do next. They type something vague, the agent doesn't use the extension, and they conclude it doesn't work. **Print the first prompt.**

### The Invisible Skill

A description so generic ("helps with writing") that the agent never chooses it — or so broad that it hijacks unrelated requests. **Say what, when, when not, and what it returns; test the triggers.**

### The Tool Soup

Twenty tools with overlapping names and descriptions. The agent picks the wrong one, or calls three to do one job. **Fewer, distinct tools with one naming pattern; merge near-duplicates.**

### The Over-Permissioned First Run

Write and delete access requested before the customer has seen a single useful read. **Read-only first; escalate when the customer asks for an action.**

### The Demo-Only First Run

The suggested first prompt runs on bundled sample text, so the customer sees the extension work on nothing of theirs. **Point the first prompt at their own files, repo, or account.**

### The Raw Stack Trace

An error that surfaces as a stack trace in the agent's context. The agent can't recover, and the customer can't either. **Errors state what failed, why, and what to try — readable by both.**

### The Host Fight

Instructions to disable host safety prompts, custom ASCII interfaces, or output that ignores how the host renders text. **Work with the host's conventions.**

### The Breaking Update

A renamed command or changed tool schema ships without notice; the customer's muscle memory and the agent's learned usage both break. **Stable names, versioned changes, a changelog.**

---

## Calibration — What Good Looks Like

*ProductOS design targets — not measured industry benchmarks. Replace them with your own numbers once you have usage data.*

| Measure | Floor | Good | Best |
| --- | --- | --- | --- |
| Install to first useful output (local skill or plugin) | 10 min | 3 min | under 1 min |
| Install to first useful output (remote MCP with OAuth) | 15 min | 5 min | under 2 min |
| Steps from install to magic moment | 6 | 4 | 2–3 |
| Required settings before first output | 3 | 1 (the credential) | 0 |
| Starter prompt triggers the right skill or tool in your evals | 7 of 10 runs | 9 of 10 | 10 of 10 |
| Hosts with a tested install path | the primary host | all named hosts | all named hosts, tested every release |

If the first output takes too long or the starter prompt misfires, the fix is almost never more documentation — it's fewer steps, better defaults, and a sharper description. Re-read principles #3, #5, and #6.

---

## Platform Notes — last reviewed October 2026 (re-verify before quoting)

Install mechanics move fast; confirm each against the host's current docs before writing them into a README or listing.

- **Claude Code plugins** are distributed through marketplaces (a git repository with a marketplace manifest); customers add the marketplace, then install the plugin from it, using the host's `/plugin` commands. Skills can also be dropped into a user or project skills folder.
- **Skill descriptions** are capped in length by the Agent Skills format (a name of up to 64 characters and a description of up to 1,024 at the last review) — the cap is the budget for the agent's onboarding copy.
- **MCP servers** are added per client: some clients offer one-click install links or bundle formats; others take a JSON config entry. Remote servers increasingly use OAuth rather than pasted keys.
- **Codex and Cursor** each have their own plugin manifests and install paths; check each host's current documentation for the exact commands.
- **Directory review shapes onboarding.** Curated connector directories have asked for read and write actions to be separate tools, each annotated as read-only or destructive — which is also the least-privilege first run this doc recommends. `design-marketplace-listing` holds the per-store requirements.

---

## Closing — The One Mental Model That Beats Everything

> **Count the steps between "install" and "that's the output I'd have spent an hour on." Then count the words the agent needs to choose your extension at the right moment. Drive the first number toward two and make the second set of words impossible to misread.**

The best agent extensions feel like the agent got better, not like the customer adopted a new tool. That's the bar: one line to install, one prompt to try, one output worth keeping.
