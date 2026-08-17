# ProductOS

**A complete operating system for taking a product from idea to revenue with AI agents.**

> **Want 1-1 support?** Join the **Product Studio** to get 1-1 support through this programme and a custom plan built for your app: **[go.buildgreatproducts.com](https://go.buildgreatproducts.com)**

ProductOS guides you through four phases. Each phase has a checklist that tells you exactly which skill to run at each step, the file it produces, and the reference playbook it draws on. Your AI agent does the heavy lifting; the system keeps it honest.

**ProductOS lives inside your app's repository** — it's the first thing you set up in the codebase, before there's any code. Even from scratch: create the app repo first, then put ProductOS in it as a `productos/` folder. The system stays in `productos/`; your product's canonical documents accumulate at the repo-root `docs/`.

Coached copies of ProductOS ship with your custom programme already inside: `docs/PLAN.md`, composed by your coach from your onboarding call — which steps of each phase you'll do in full, which are fast-tracked from what you've already built, which you can skip. No plan in your copy? Follow the checklists top to bottom — that's the standard programme. See `productos/START-HERE.md`.

One thread runs through all four phases: **the launch ladder.** Each phase closes with a launch (run by `studio-launch`) that climbs one rung of the signal ladder — `reply → conversation → signup → activated user → payment` — starting with the Define phase's **Mini-Launch** in week one or two, where the win is one real person replying. Everyone who responds joins your believers list in `docs/LAUNCHES.md`; they're your preview readers, beta users, and first customers.

| Phase | Folder | What you end up with |
|---|---|---|
| 1. **Define** | `productos/define/` | Offer, persona, pricing, mini-launch (your first real customer signal) → `docs/PRODUCT.md` |
| 2. **Design** | `productos/design/` | Identity (in words), design system from an image you love, magic moment, onboarding, relaunch #2 → `docs/DESIGN.md` + `docs/DESIGN.html` |
| 3. **Develop** | `productos/develop/` | PRD, roadmap, agent-built MVP, code review + security audit, the beta invite → `docs/PRD.md`, `docs/ROADMAP.md`, `docs/SECURITY-AUDIT.md`, `docs/DEPLOY.md` |
| 4. **Distribute** | `productos/distribute/` | Go-to-market, the public launch, growth experiments, scaling — a loop, not a finish line |

## Installation

Three steps, the same for every tool and every stage:

1. **Create or open your app repo.** Starting from scratch? Make an empty folder and `git init` it — your product's repo exists before your product does.
2. **Put ProductOS in it as `productos/`** — clone this folder into the repo root, named exactly `productos`. A copy (or a GitHub ZIP extract) is fine for Claude Code and Codex; **Cursor's `/add-plugin` needs a real git clone** — see below.
3. **Run `studio-setup`.** It wires the agent guidelines into your repo root (`CLAUDE.md`/`AGENTS.md`, from `productos/setup/`), adds `productos/` to your `.gitignore` (see the licence note below), and — if your copy shipped with a programme plan — moves it to `docs/PLAN.md` and verifies it against your actual repo.

ProductOS is also a plugin for **Claude Code**, **Codex**, and **Cursor** — one package, three manifests, the same 35 skills:

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

> **Licence note:** ProductOS is yours to use, not to redistribute — which is why setup gitignores `productos/`: the materials never get committed to your repo, so open-sourcing your product later is safe. Your outputs (`docs/`, the wired root guidelines) are yours and are tracked as normal. Collaborators install their own copy from the official repo into their clone. See `productos/LICENSE.md`.

Skill names follow the `studio-<phase>-*` convention (e.g. `studio-define-offer-builder`) in every tool; the two cross-phase skills are simply `studio-setup` (the installer) and `studio-launch` (the launch ritual).

## Getting started

1. Run **`studio-setup`** — ask your agent to *"set up ProductOS"*. It wires your repo and, if your copy came from your coach, adopts your custom programme: **`docs/PLAN.md`** says which steps of each phase you'll do in full, which are fast-tracked, which you can skip, and in what order. (No plan in your copy? Open **`productos/define/DEFINE-CHECKLIST.md`** and work top to bottom — that's the standard programme.)
2. **Not starting from scratch?** Your plan fast-tracks the Define phase via `studio-define-from-code` — it extracts your product offer, persona, and pricing drafts from your existing codebase or landing page, then the review pass sharpens them. You skip the blank-template work, not the valuable thinking.
3. Follow your plan's sequence; within it, finish each scheduled step before the next — later skills read earlier outputs.
4. Your product's canonical documents accumulate in **`docs/`** at the repo root — including `docs/PLAN.md`, your programme, and `docs/LAUNCHES.md`, the launch log that tracks your believers and your rung on the signal ladder. If your repo already has a `docs/` folder, the ProductOS documents simply live alongside what's there.
5. When a checklist says "Run `studio-define-offer-builder`", just ask your agent to do that — the skill triggers by name or by describing what you want ("help me build my product offer").

## How it's organized

- **`productos/START-HERE.md`** — the front door: setup in three steps, and how your programme plan works.
- **Checklists** (`*-CHECKLIST.md`) — the runbook for each phase. Source of truth for how each step runs; your plan says which steps apply to you.
- **Numbered templates** (`1-`–`4-` in each phase folder) — worksheets the skills fill in place, with `> Good/Bad` calibration examples throughout.
- **BONUS docs** — reference playbooks: worked examples, failure patterns, channel guides, best-practice libraries.
- **`productos/skills/`** — one flat folder per skill (35 total). Each contains a `SKILL.md` plus any bundled reference files.
- **`productos/setup/CLAUDE.md` + `productos/setup/AGENTS.md`** — agent guidelines wired into your repo root at setup (by `studio-setup`), so your coding agent behaves from day one.

## Requirements

- A Claude plan with access to Claude Code, Cowork, or Claude Desktop (or Cursor/Codex for the build phase).
- Web search enabled — the Define and Distribute skills do live market research.

## Version

**1.6.0** — see `productos/CHANGELOG.md`. Licensed for individual commercial use — see `productos/LICENSE.md`.
