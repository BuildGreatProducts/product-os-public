# Shape: Agent skill

*Slug: `agent-skill` · Family: AI-native*

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

One skill, or a small skill pack, that an AI agent loads to do a specific job well: a brand-voice skill, a financial-model skill, a code-review skill pack, a contract-redline skill. A skill is a folder with a `SKILL.md` (a name and a description that tell the agent when to use it, then instructions) plus optional reference files, templates, and scripts. The agent reads it on demand, so the customer gets expertise inside the tool they already use — Claude, Claude Code, Codex, Cursor, and other agents that support the shared skill format. Skills are distributed as Git repositories, inside plugins, through skill directories, or as downloadable folders. Where `agent-plugin` bundles a workflow, `agent-skill` sells one capability done well.

## Live means

The skill is installable by a stranger from a public link or marketplace, and a fresh install produces the documented first output on the first try — invoked by the documented request in a clean agent session, with no member-specific files or settings present.

## First sale means

A real customer (warm network counts; the member's own test purchase doesn't) pays for the skill or the access behind it — a Stripe Checkout or Payment Link, Gumroad / Lemon Squeezy download, or a merchant of record that grants a private-repo invite, a download, or an API key — and installs it. A skill sold as part of a service or team rollout, paid by invoice, also counts once paid.

## Define notes

- **Persona:** the person *and* the agent they use: "a fractional CFO who builds models in Claude", "a staff engineer whose team uses Codex for review". The persona must already be in the agent daily; a skill doesn't convert someone to agents.
- **Pricing models:** free skill as the top of a funnel (to a paid app, service, or community) is the most common; paid pack with updates (one-time or annual); team licence for an organisation rolling it out; a free skill that calls a paid API for the part that can't be copied (data, a model, a hosted tool).
- **Who pays:** an individual expert by card, or a team lead buying for many seats. Expertise-heavy skills (finance, legal, brand) carry higher prices than generic productivity skills because the instructions encode scarce judgement.

### Fees — last reviewed October 2026 (re-verify before quoting)

- At the last review, skill directories and agent marketplaces charged no listing fee and offered no paid checkout; sales go through the member's own checkout (Stripe, Gumroad, Lemon Squeezy — see `digital-product` for storefront fees). Check whether any directory has added paid listings.

## Design route

| Step | Mode | How it adapts |
| --- | --- | --- |
| 1 — Identity | Lite | Name (checked against the skill directories and the `name` field rules), worldview, and tone of voice. Visual Style only as far as the README and listing need. |
| 2 — UX Writing | Adapted | `docs/COPY.md` covers the skill's description (the triggering text), the structure and voice of every output it produces, its questions to the user, and its README. |
| 3 — Design System | Lite | Brand tokens for the README, listing, and any landing page. Full only if the skill outputs visual documents (decks, reports) — then the tokens style those outputs. |
| 4 — Design Prompts | Skip | No screens. |
| 5 — Magic Moment | Adapted | The first output that is clearly better than the agent without the skill — shown as a before/after on the same request. |
| 6 — Onboarding | Adapted | Install → first invocation (the exact sentence to type) → first output. `docs/ONBOARDING.md` is the README quickstart; no wireframe. Use `BONUS-Agent-Extension-Onboarding-Best-Practice.md`. |
| 7 — Acquisition surface | Full | `design-marketplace-listing` for the skill directories and plugin marketplaces it's listed in, plus the repository README. Add `design-landing-page` when the skill is paid or feeds a paid product. |

## Develop route

| Step | Mode | How it adapts |
| --- | --- | --- |
| 0 — Migrate | Skip | Not applicable. |
| 1 — PRD & Roadmap | Adapted | The PRD specifies the skill's structure, triggering, and eval set (below); the roadmap builds the core instructions first, then references, scripts, and evals. |
| 1b — Evals | Full | `develop-agent-evals` — trigger scenarios (fires when it should, stays quiet on neighbours) and output-quality scenarios with pass criteria, run with and without the skill. |
| 2 — Verify setup | Full | Turn on version history (git) if it isn't on yet — the build saves its work there at every phase — and check the guidelines `setup` wired. Runs first in Develop. |
| 3 — Build | Adapted | `develop-build` writes `SKILL.md`, reference files, templates, and scripts, running the evals after each task. The bar is the eval set passing, not features shipped. |
| 4 — Build loop | Full | Every change re-runs the evals; re-test when the target agents release new models. |
| 5 — Code review | Adapted | Review bundled scripts as code and the skill text for contradictions, stale facts, and instructions the agent can't follow. |
| 6 — Design changes | Skip | No UI. |
| 7 — Conversion review | Adapted | Listing / README → install → first invocation → magic moment → paid upgrade. Runs on the README, listing, and landing page. |
| 8 — Security audit | Full | A skill directs an agent with the user's permissions. Audit bundled scripts, commands the skill tells the agent to run, secrets, external URLs it fetches, and how it treats untrusted input (prompt injection). Lighter when the skill is instructions only — but still run it. |
| 9 — Go live | Adapted | Publish to a repository and directories rather than deploy (below). |

### What the PRD must cover

- **SKILL.md structure:** frontmatter (`name`, `description`), the workflow the agent follows, inputs it asks for, the output format, and a verify step.
- **Description and triggering:** the exact description, the requests it must trigger on, and the neighbouring requests it must not.
- **Bundled references:** each reference file, what it holds, and when the skill tells the agent to read it (progressive disclosure keeps the main file short).
- **Scripts and tools:** any bundled scripts, their dependencies, and what tools or MCP servers the skill expects the agent to have.
- **Target agents:** which agents it's tested on, and any per-agent differences in install path or capabilities.
- **The eval set:** scenarios from `docs/EVALS.md`, with pass criteria and a with/without-skill baseline.
- **Paid access (if any):** how buyers get it and how they receive updates.

### Go live

Skill folder in a public repository (private for paid access, with access granted on purchase) → README with the install command for each target agent and the first request to type → fresh-install test in a clean session of each target agent → listed in skill directories and, optionally, wrapped in a plugin marketplace entry for one-command install. `develop-golive` writes this as `docs/DEPLOY.md`; live when a stranger's fresh install produces the first output.

#### Review and policy — last reviewed October 2026 (re-verify before quoting)

- The skill format (a folder with `SKILL.md` and YAML frontmatter) is shared across several agents; frontmatter rules include a lowercase-hyphenated `name` and a length-limited `description` (64 and 1,024 characters respectively in Claude's documentation at the last review — check the current limits).
- Community skill directories (for example skills.sh and Anthropic's public skills repository) differ in whether they review submissions; most index public GitHub repositories. Check each directory's current submission process.

## Distribute notes

**Native channels:** skill directories and plugin marketplaces, GitHub (README, topics, "awesome" lists), the target agents' communities (Discord servers, forums, subreddits), the persona's professional communities (where finance or legal or design practitioners talk about using AI), and X / LinkedIn posts showing before/after outputs.

**First users:**

1. Run the skill live with ten warm-network practitioners on their own real task; keep their before/after outputs as proof (with permission).
2. Publish the before/after side by side — same request, agent without the skill vs with it — in the persona's professional community.
3. List in two skill directories and one plugin marketplace in the same week.
4. Offer a free version that solves one narrow job completely, with the paid pack covering the adjacent jobs.

**Activation and retention:** *activated* = the first successful invocation that produces the documented output (measured by a paid-backend call, opt-in telemetry, or asking every early user). *Returned* = the skill is invoked again in week 2. Track installs separately from invocations — a skill that's installed but never triggers is a description problem.

## Watch-outs

- **The description is the product.** If it doesn't trigger on the persona's real phrasing, the skill never runs. Test triggering before polishing instructions.
- **Copyable by design.** A skill is plain text. Price updates, bundled data, a hosted backend, or the expert's ongoing judgement — not the file.
- **Model drift.** A new model can make instructions redundant or change behaviour. Re-run evals on every major model release.
- **Too long, too generic.** Instructions the agent already follows ("be thorough") waste context; the value is the specific judgement only the expert has.
- **Facts that age.** Skills that quote prices, limits, or laws need dated notes and a review cadence.
