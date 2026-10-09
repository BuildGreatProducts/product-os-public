# Shape: Agent plugin

*Slug: `agent-plugin` · Family: AI-native*

## Contents

- [What it is](#what-it-is)
- [Live means](#live-means)
- [First sale means](#first-sale-means)
- [Define notes](#define-notes)
- [Design route](#design-route)
- [Develop route](#develop-route)
  - [What the PRD must cover](#what-the-prd-must-cover)
  - [Go live](#go-live)
- [Distribute notes](#distribute-notes)
- [Watch-outs](#watch-outs)

## What it is

A bundle that extends an AI agent or AI coding tool: skills, slash commands, subagents, hooks, and connectors (MCP servers) packaged together and installed in one step. Examples: Claude Code and Cowork plugins, Codex plugins, Cursor plugins — ProductOS itself ships this way. The customer receives a workflow, not a single capability: several pieces that work together inside the tool they already use. Plugins are distributed through marketplaces — a Git repository with a marketplace manifest that users add, the agent vendors' official directories, and community directories. The "UI" is the agent's chat and terminal; the plugin's interface is its command names, descriptions, and outputs.

## Live means

A stranger can install the plugin from a public marketplace or repository link using the host tool's documented install command, and a fresh install — on a clean machine with no member-specific config — runs the documented first command and produces the documented first output on the first try.

## First sale means

A real customer (warm network counts; the member's own test purchase doesn't) pays for the plugin or for the service behind it — typically a Stripe Checkout or Payment Link, or a merchant of record, that issues an API key or grants access to a private marketplace repository — and uses that paid access in the agent. Agent marketplaces don't process payments, so the checkout is always the member's own.

## Define notes

- **Persona:** defined by the host tool *and* the job: "a solo founder in Claude Code who ships web apps", "a Cursor user on a team with a code-review policy". The tool sets the install path; the job sets the plugin's scope.
- **Pricing models:** free and open plugin as distribution for a paid product (most common); paid access to a private repo or marketplace (one-time or annual, with updates); a free plugin whose connectors call a paid hosted backend (subscription or usage); a plugin bundled into a coaching or service offer.
- **Who pays:** the individual developer or founder by card; a team lead for a team-wide licence. Price the *maintained workflow*, not the files — the files can be copied.

### Fees — last reviewed October 2026 (re-verify before quoting)

- At the last review, the main agent plugin marketplaces (Claude Code / Cowork, Codex, Cursor) charged no listing fee and offered no built-in paid checkout or revenue share; monetisation happens through the member's own checkout. Check whether any host has since added paid listings.

## Design route

| Step | Mode | How it adapts |
| --- | --- | --- |
| 1 — Identity | Full | The name becomes the plugin's install name and command namespace — check it's free in the target marketplaces and doesn't collide with common commands. |
| 2 — UX Writing | Adapted | `docs/COPY.md` covers command names, skill and agent descriptions (the text that decides when the agent triggers them), argument hints, hook and error messages, the shape of every output the plugin writes, and the README voice. |
| 3 — Design System | Lite | Brand tokens only (colour, type, logo use) for the README, marketplace listing, and landing page. |
| 4 — Design Prompts | Skip | No screens to generate. Optional only if the plugin ships a web dashboard. |
| 5 — Magic Moment | Adapted | The first command whose output makes the user feel the workflow working (a full PR review posted, a whole spec written), named as an observable output. |
| 6 — Onboarding | Adapted | Install → configure (any keys, MCP auth, required CLIs) → first command → magic moment. `docs/ONBOARDING.md` is the README quickstart and any setup command; no wireframe. Use `BONUS-Agent-Extension-Onboarding-Best-Practice.md`. |
| 7 — Acquisition surface | Full | `design-marketplace-listing` for each marketplace (the Claude Code / Cowork plugin directory, Codex, Cursor, community directories) and the repository README. Add `design-landing-page` when the plugin is paid or feeds a paid product. |

## Develop route

| Step | Mode | How it adapts |
| --- | --- | --- |
| 0 — Migrate | Skip | Not applicable. |
| 1 — PRD & Roadmap | Adapted | The PRD specifies components (below) instead of screens; the roadmap builds one component at a time, each with its eval scenarios. |
| 1b — Evals | Full | `develop-agent-evals` — trigger tests (the right skill or command fires, and the wrong ones don't) plus output-quality scenarios for each component. |
| 2 — Verify setup | Full | Turn on version history (git) if it isn't on yet — the build saves its work there at every phase — and check the guidelines `setup` wired. Runs first in Develop. |
| 3 — Build | Full | `develop-build` writes the manifests, skills, commands, agents, hooks, and connectors, running the evals as each component lands. |
| 4 — Build loop | Full | Each change re-runs the evals; host tools change their plugin formats, so re-test on new host versions. |
| 5 — Code review | Full | For hooks, scripts, and connector code changed outside the build skills; skill text gets the same review. |
| 6 — Design changes | Skip | No UI. Optional if a dashboard ships. |
| 7 — Conversion review | Adapted | README / listing → install → first command → magic moment → paid key or private access. Runs on the README, listing, and landing page instead of app screens. |
| 8 — Security audit | Full | Hooks and scripts execute on the customer's machine with their permissions. Audit for command injection, secrets in the repo, over-broad tool permissions, prompt-injection paths from untrusted content, and what data connectors send out. |
| 9 — Go live | Adapted | Marketplace publish rather than a deploy (below). |

### What the PRD must cover

- **Component list:** every skill, command, agent, hook, and connector, each with its job, its trigger (description or command name), and its inputs and outputs.
- **Host tools and formats:** which agents the plugin targets (Claude Code, Cowork, Codex, Cursor) and the manifest each needs; what's shared and what's host-specific.
- **Descriptions and triggering:** the description text for each skill and agent, written to trigger on the right requests and not on neighbouring ones.
- **Dependencies and configuration:** required CLIs, environment variables, MCP servers and their auth, and the first-run check that tells the user what's missing.
- **The eval set:** scenarios per component, with pass criteria, from `docs/EVALS.md`.
- **Paid access (if any):** how access is gated (private repo invites, API keys checked by a hosted backend), and how updates reach paying users.
- **Versioning:** version number in the manifest, changelog, and the update command users run.

### Go live

Public repository (or private, for paid access) with the plugin manifest and a marketplace manifest → install tested from the marketplace link on a clean machine → submitted to the official directory of each host tool where one accepts submissions → listed in community directories → any hosted backend deployed under its own `web-app` or `mcp-server` go-live. `develop-golive` writes this as `docs/DEPLOY.md`; live when a stranger's fresh install produces the first output.

#### Review and policy — last reviewed October 2026 (re-verify before quoting)

- Claude Code plugins install from any Git-hosted marketplace (`/plugin marketplace add`, then `/plugin install`) without review; Anthropic's official directory reviews submissions — check its current submission process and timeline.
- Codex and Cursor each have their own plugin manifest formats and directories; check the current docs for the manifest fields and whether listings are reviewed.
- Hooks run arbitrary commands; directories may reject or flag plugins whose hooks do more than they declare.

## Distribute notes

**Native channels:** the host tools' official plugin directories, community marketplaces and "awesome" lists on GitHub, the host tools' Discord servers and forums, developer communities on X, Reddit, and Hacker News, and YouTube walkthroughs of agent workflows.

**First users:**

1. Install it with ten warm-network users of the host tool on a call; time how long the first command takes from a clean start.
2. Post a screen recording of the magic-moment command running end to end, in the host tool's community channels.
3. Submit to the official directory and three community lists in the same week, with the README's one-line promise.
4. Write one build-in-public post per component explaining the workflow problem it solves, each linking the install command.

**Activation and retention:** *activated* = a fresh install runs the magic-moment command and produces its output (measured by a paid-backend call, an opt-in telemetry ping, or asking early users). *Returned* = the user invokes any plugin command again in week 2. GitHub stars and clones are vanity — they don't show use.

## Watch-outs

- **Too many pieces.** A plugin with fifteen skills and no clear first command doesn't activate. Lead with one workflow and its one command.
- **Triggers that collide.** Vague descriptions fire on the wrong requests or never fire. Trigger evals are not optional.
- **Copyable value.** Plugin files are plain text. Paid value has to live somewhere it can't be copied: a hosted backend, maintained updates, data, or support.
- **Host-format churn.** Plugin formats and install commands change between host releases. Pin the tested host version in the README and re-test on upgrades.
- **Hooks that surprise.** A hook that runs on every prompt or writes files unannounced gets the plugin uninstalled. Declare what each hook does.
