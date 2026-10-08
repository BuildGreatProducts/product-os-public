# ProductOS

**A complete operating system for taking a product from idea to revenue with AI agents.**

> **Want 1-1 support?** Join the **Product Studio** to get 1-1 support through this programme and a custom plan built for your app: **[go.buildgreatproducts.com](https://go.buildgreatproducts.com)**

ProductOS guides you through four phases. Each phase has a checklist that tells you exactly which skill to run at each step, the file it produces, and the reference playbook it draws on. Your AI agent does the heavy lifting; the system keeps it honest.

**ProductOS lives inside your app's repository** — it's the first thing you set up in the codebase, before there's any code. Even from scratch: create the app repo first, then put ProductOS in it as a `productos/` folder. The system stays in `productos/`; your product's canonical documents accumulate at the repo-root `docs/`.

Coached copies of ProductOS ship with your custom programme already inside: `docs/PLAN.md`, composed by your coach from your onboarding call — which steps of each phase you'll do in full, which are fast-tracked from what you've already built, which you can skip. No plan in your copy? Setup offers two paths: a new project starts with the offer builder and follows the checklists top to bottom (the standard programme); an existing project starts Ship in 7. See `productos/START-HERE.md`.

One rule runs through all four phases: **everything ProductOS produces lands in `docs/`.** The phase folders hold the worksheets and playbooks; the skills write the results to your repo, where they're committed, shared, and read by every later skill. Each phase gives you a small set of documents to read, not a folder of worksheets.

| Phase | Folder | What you end up with |
|---|---|---|
| 1. **Define** | `productos/define/` | Offer, persona, pricing — all in one document → `docs/DEFINE.md` |
| 2. **Design** | `productos/design/` | Identity (in words), UX writing guide, design system from an image you love, design prompts, magic moment, onboarding, landing page or app listing → `docs/DESIGN.md` + `docs/DESIGN.html` (identity + tokens), `docs/COPY.md`, `docs/DESIGN-PROMPTS.md`, `docs/MAGIC-MOMENT.md`, `docs/ONBOARDING.md`, `docs/LANDING-PAGE.md` / `docs/APP-LISTING.md` |
| 3. **Develop** | `productos/develop/` | PRD, roadmap, agent-built MVP, code review + security audit, go-live → `docs/PRD.md`, `docs/ROADMAP.md`, `docs/SECURITY-AUDIT.md`, `docs/DEPLOY.md` |
| 4. **Distribute** | `productos/distribute/` | Go-to-market, growth experiments, scaling — a loop, not a finish line → `docs/GO-TO-MARKET.md`, `docs/GROWTH-EXPERIMENTS.md`, `docs/GROWTH-TRACKER.md`, `docs/SCALE.md` |

## Installation

Three steps, the same for every tool and every stage:

1. **Create or open your app repo.** Starting from scratch? Make an empty folder and `git init` it — your product's repo exists before your product does.
2. **Put ProductOS in it as `productos/`** — clone this folder into the repo root, named exactly `productos`. A copy (or a GitHub ZIP extract) is fine for Claude Code and Codex; **Cursor's `/add-plugin` needs a real git clone** — see below.
3. **Run `setup`.** It wires the agent guidelines into your repo root (`CLAUDE.md`/`AGENTS.md`, from `productos/setup/`), adds `productos/` to your `.gitignore` (see the licence note below), and — if your copy shipped with a programme plan — moves it to `docs/PLAN.md` and verifies it against your actual repo.

ProductOS is also a plugin for **Claude Code**, **Codex**, and **Cursor** — one package, three manifests, the same 36 skills:

### Claude Code

From your app repo root:

```
claude plugin install ./productos
```

### Codex

From your app repo root, add the `productos/` folder as a marketplace (it ships with its own `.agents/plugins/marketplace.json`), then install:

```
codex plugin marketplace add ./productos
codex plugin add productos@productos
```

(See [developers.openai.com/codex/plugins](https://developers.openai.com/codex/plugins) for how Codex plugins and marketplaces work.)

### Cursor

`/add-plugin` clones the selected folder as a git remote (`file://…` + `git ls-remote HEAD`). That only works if the folder **is a git repository with at least one commit**. A GitHub ZIP extract (`product-os-public-main`, no `.git`) fails with:

> Failed to resolve git ref "HEAD" … does not appear to be a git repository

**Clone, don't unzip:**

```
git clone https://github.com/BuildGreatProducts/product-os-public productos
```

Then type `/add-plugin` and point it at that `productos/` folder. Cursor auto-discovers all skills from `productos/skills/`.

**Already unzipped?** Turn the folder into a git repo, then retry `/add-plugin`:

```
cd /path/to/product-os-public-main
git init
git add .
git commit -m "ProductOS"
```

(`git init` alone is not enough — Cursor needs a resolvable `HEAD`, which means one commit.)

**Without using git:** copy the folder to `~/.cursor/plugins/local/productos` (it must contain `.cursor-plugin/plugin.json`) and reload the window. See [Test plugins locally](https://cursor.com/docs/plugins.md#test-plugins-locally).

### Cowork / Claude Desktop (no install)

Add **your app repo** (not `productos/` itself) as the project folder. The root `CLAUDE.md`/`AGENTS.md` wired at setup orients your agent, and skills in `productos/skills/` are picked up from there. You can also copy individual skill folders into `~/.claude/skills/` (Claude) or `~/.agents/skills/` (Codex/Cursor, works across all your repos) for a manual install.

### Updating

When a new version ships (see `productos/CHANGELOG.md`), ask your agent to *"update ProductOS"*. The `update` skill fetches the latest release from the official repo and shows you what's new before changing anything. It replaces every file you never touched and keeps every file you changed. If your copy is older than 1.14.0 and kept your work inside `productos/` (filled templates, wireframes), it moves that work into `docs/`, never overwriting a file already there. It then re-wires your root guidelines and tells you how to refresh the plugin in your tool.

> **Licence note:** ProductOS is yours to use, not to redistribute — which is why setup gitignores `productos/`: the materials never get committed to your repo, so open-sourcing your product later is safe. Your outputs (`docs/`, the wired root guidelines) are yours and are tracked as normal. Collaborators install their own copy from the official repo into their clone. See `productos/LICENSE.md`.

Skill names follow the `<phase>-*` convention (e.g. `define-offer-builder`) in every tool; the four cross-phase skills are simply `setup` (the installer), `update` (brings your copy up to the latest version), and the two challenges, `ship-in-7` (your app live in seven sessions) and `sell-in-30` (your first paying customer in thirty, or your first activated user if the product stays free).

## Getting started

1. Run **`setup`** — ask your agent to *"set up ProductOS"*. It wires your repo and, if your copy came from your coach, adopts your custom programme: **`docs/PLAN.md`** says which steps of each phase you'll do in full, which are fast-tracked, which you can skip, and in what order. No plan in your copy? Setup ends by offering one of two paths:
   - **New project** (nothing built yet) → **`define-offer-builder`**, Step 1 of the Define checklist. From there, work down the checklists phase by phase — that's the standard programme. No idea yet? `define-idea-finder` comes first.
   - **Existing project** (code, a prototype, an AI-generated app) → **`ship-in-7`**, seven sessions to your app live at a real URL. It composes a session-by-session plan from the skills below, checks in with you every session, and ends with a report you can bring to a Product Studio call. Already live? Its follow-on, **`sell-in-30`**, takes you to your first paying customer.
2. **Already have a product?** Your plan fast-tracks the Define phase via `define-from-code` — it extracts your product offer, persona, and pricing drafts from your existing codebase or landing page into `docs/DEFINE.md`, then the review pass sharpens them. You skip the blank-template work, not the valuable thinking. **No software idea yet?** `define-idea-finder` audits your existing business, expertise, or passions and converges on the one MVP worth building, before the offer work begins.
3. Follow your plan's sequence; within it, finish each scheduled step before the next — later skills read earlier outputs.
4. Everything the skills produce lands in **`docs/`** at the repo root — `docs/PLAN.md` (your programme), `docs/DEFINE.md` (offer, customer, pricing in one document), `docs/DESIGN.md` (identity + design system), and the rest. That folder is the source of truth: share it, commit it, and point anyone new at it. If your repo already has a `docs/` folder, the ProductOS documents simply live alongside what's there.
5. When a checklist says "Run `define-offer-builder`", just ask your agent to do that — the skill triggers by name or by describing what you want ("help me build my product offer").

## How it's organized

- **`productos/START-HERE.md`** — the front door: setup in three steps, and how your programme plan works.
- **Checklists** (`*-CHECKLIST.md`) — the runbook for each phase. Source of truth for how each step runs; your plan says which steps apply to you.
- **Numbered worksheets** (`1-`–`4-` in each phase folder) — the structure and `> Good/Bad` calibration each skill follows. The skills read them and write your answers to `docs/`; the worksheets stay blank.
- **BONUS docs** — reference playbooks: worked examples, failure patterns, channel guides, best-practice libraries.
- **`productos/skills/`** — one flat folder per skill (36 total). Each contains a `SKILL.md` plus any bundled files it loads only when needed (`references/`, `templates/`).
- **`productos/scripts/`** — a maintainer tool: `lint-skills.py` checks every skill against Anthropic's skill-authoring rules. You don't need it to use ProductOS.
- **`productos/setup/CLAUDE.md` + `productos/setup/AGENTS.md`** — agent guidelines wired into your repo root at setup (by `setup`), so your coding agent behaves from day one.

## Requirements

- A Claude plan with access to Claude Code, Cowork, or Claude Desktop (or Cursor/Codex for the build phase).
- Web search enabled — the Define and Distribute skills do live market research.

## Version

**1.15.0** — see `productos/CHANGELOG.md`. Licensed for individual commercial use — see `productos/LICENSE.md`.
