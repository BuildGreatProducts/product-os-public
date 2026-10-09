# ProductOS

**A complete operating system for taking an AI product from idea to revenue with AI agents — whatever its shape.**

> **Want 1-1 support?** Join the **Product Studio** to get 1-1 support through this programme and a custom plan built for your app: **[go.buildgreatproducts.com](https://go.buildgreatproducts.com)**

ProductOS guides you through four phases. Each phase has a checklist that tells you exactly which skill to run at each step, the file it produces, and the reference playbook it draws on — and an orchestrator skill that walks it with you. Your AI agent does the heavy lifting; the system keeps it honest.

**It's built for every shape of AI product**, not just apps: web, mobile, and desktop apps, browser extensions, agent plugins, agent skills, MCP servers, chat assistants, developer tools (APIs, SDKs, CLIs), productized services, websites, and digital products. In the Define phase you choose your product's shape, and from then on every step adapts to it: an agent skill skips the screen-by-screen design work but gets an eval set and a marketplace listing; a productized service designs its delivery process instead of a database; a mobile app goes live through the App Store, not a deploy.

**ProductOS lives inside your product's project folder** — it's the first thing you set up, before there's any code. Even from scratch: make the folder first, then put ProductOS in it as a `productos/` folder. The system stays in `productos/`; your product's canonical documents accumulate in `docs/` at the folder's root. Define and Design need nothing more — no git, no terminal. Version history (git) goes on at the start of Develop, and only if your product is built from code; your agent does it for you.

Coached copies of ProductOS ship with your custom programme already inside: `docs/PLAN.md`, composed by your coach from your onboarding call — which steps of each phase you'll do in full, which are fast-tracked from what you've already built, which you can skip. No plan in your copy? Setup asks where you'd like to start, with four paths: find a new idea (`define-idea-finder`, then the Define phase); start from an idea you have (`define-phase`, following the phases top to bottom — the standard programme); start from an existing project (`product-audit`, which scores what you have and writes a programme for it); or take on a challenge (`ship-in-7` or `sell-in-30`). See `productos/START-HERE.md`.

One rule runs through all four phases: **everything ProductOS produces lands in `docs/`.** The phase folders hold the worksheets and playbooks; the skills write the results to your repo, where they're committed, shared, and read by every later skill. Each phase gives you a small set of documents to read, not a folder of worksheets.

| Phase | Folder | What you end up with |
|---|---|---|
| 1. **Define** | `productos/define/` | Offer, product shape, persona, pricing — all in one document → `docs/DEFINE.md` |
| 2. **Design** | `productos/design/` | Identity (in words), UX writing guide, design system from an image you love, design prompts, magic moment, onboarding, and the acquisition surfaces your shape needs (landing page, app-store listing, marketplace listing) → `docs/DESIGN.md` + `docs/DESIGN.html` (identity + tokens), `docs/COPY.md`, `docs/DESIGN-PROMPTS.md`, `docs/MAGIC-MOMENT.md`, `docs/ONBOARDING.md`, `docs/LANDING-PAGE.md` / `docs/APP-LISTING.md` / `docs/MARKETPLACE-LISTING.md` |
| 3. **Develop** | `productos/develop/` | PRD, roadmap (new build or existing codebase), evals for AI-native shapes, agent-built MVP, code review + security audit, go-live in your shape's form → `docs/PRD.md`, `docs/ROADMAP.md`, `docs/EVALS.md`, `docs/SECURITY-AUDIT.md`, `docs/DEPLOY.md` |
| 4. **Distribute** | `productos/distribute/` | Go-to-market, growth experiments, scaling — a loop, not a finish line → `docs/GO-TO-MARKET.md`, `docs/GROWTH-EXPERIMENTS.md`, `docs/GROWTH-TRACKER.md`, `docs/SCALE.md` |

## Installation

Three steps, the same for every tool and every stage:

1. **Make or open your product's folder.** Starting from scratch? An empty folder is all you need. Already have a codebase? That folder is the one.
2. **Put ProductOS in it as `productos/`** — copy or clone this folder into it, named exactly `productos`. A copy (or a GitHub ZIP extract) is fine for Claude Code, Codex, and Claude Desktop; **Cursor's `/add-plugin` needs a real git clone** — see below. (Skip both steps if you like: run `setup` from the ProductOS folder itself and it makes your product's folder and moves ProductOS in.)
3. **Run `setup`.** It wires the agent guidelines into your folder's root (`CLAUDE.md`/`AGENTS.md`, from `productos/setup/`), adds `productos/` to your `.gitignore` (see the licence note below), and — if your copy shipped with a programme plan — moves it to `docs/PLAN.md` and verifies it against what's actually there.

ProductOS is also a plugin for **Claude Code**, **Codex**, and **Cursor** — one package, three manifests, the same 45 skills:

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

Add **your product's folder** (not `productos/` itself) as the project folder — the easiest way to run Define and Design, with no terminal at all. The root `CLAUDE.md`/`AGENTS.md` wired at setup orients your agent, and skills in `productos/skills/` are picked up from there. You can also copy individual skill folders into `~/.claude/skills/` (Claude) or `~/.agents/skills/` (Codex/Cursor, works across all your repos) for a manual install.

### Updating

When a new version ships (see `productos/CHANGELOG.md`), ask your agent to *"update ProductOS"*. The `update` skill fetches the latest release from the official repo and shows you what's new before changing anything. It replaces every file you never touched and keeps every file you changed. If your copy is older than 1.14.0 and kept your work inside `productos/` (filled templates, wireframes), it moves that work into `docs/`, never overwriting a file already there. It then re-wires your root guidelines and tells you how to refresh the plugin in your tool.

> **Licence note:** ProductOS is yours to use, not to redistribute — which is why setup gitignores `productos/`: the materials never get committed to your repo, so open-sourcing your product later is safe. Your outputs (`docs/`, the wired root guidelines) are yours and are tracked as normal. Collaborators install their own copy from the official repo into their clone. See `productos/LICENSE.md`.

Skill names follow the `<phase>-*` convention (e.g. `define-offer-builder`) in every tool, including the four phase orchestrators (`define-phase`, `design-phase`, `develop-phase`, `distribute-phase`). The cross-phase skills are simply `continue` (say it any time — it works out where you are and picks up the next step), `setup` (the installer), `update` (brings your copy up to the latest version), `product-audit` and `product-refactor` (the path for an existing product: score it, plan it, work the plan), the two challenges, `ship-in-7` (your product live in seven sessions) and `sell-in-30` (your first paying customer in thirty, or your first activated user if the product stays free), and `build-loop` (the build loop for Claude Code, Codex, and Cursor).

## Getting started

1. Run **`setup`** — ask your agent to *"set up ProductOS"*. It wires your folder and, if your copy came from your coach, adopts your custom programme: **`docs/PLAN.md`** says which steps of each phase you'll do in full, which are fast-tracked, which you can skip, and in what order. No plan in your copy? Setup asks one question — **where would you like to start?**
   - **Find a new idea** → **`define-idea-finder`** audits your business, expertise, or passions and converges on the one product worth building, then hands into the offer.
   - **Start from an idea you have** → **`define-phase`**. It walks Define step by step: your offer, your product's shape, your customer, your price. Then `design-phase`, `develop-phase`, and `distribute-phase` take over in turn.
   - **Start from an existing project** (code, a prototype, an AI-generated app, a live service or listing) → **`product-audit`**. It scores your product across all four phases with evidence, names your shape and stage, and writes a programme to `docs/PLAN.md`; **`product-refactor`** then works through it step by step.
   - **Take on a challenge** → **`ship-in-7`** gets you live in seven sessions, from wherever you are; already live, **`sell-in-30`** takes you to your first paying customer in thirty.

   Didn't pick a challenge at the start? They come up again when they fit: Ship in 7 once Define is done, or as the opening block of an audit plan; Sell in 30 once you're live. Ask for either by name at any time.
2. **Already have a product?** The audit's plan fast-tracks the Define phase via `define-from-code` — it extracts your product offer, persona, and pricing drafts from your existing codebase or landing page into `docs/DEFINE.md`, then the review pass sharpens them. You skip the blank-template work, not the valuable thinking. **No software idea yet?** `define-idea-finder` audits your existing business, expertise, or passions and converges on the one product worth building, before the offer work begins.
3. Follow your plan's sequence; within it, finish each scheduled step before the next — later skills read earlier outputs.
4. Everything the skills produce lands in **`docs/`** at your folder's root — `docs/PLAN.md` (your programme), `docs/DEFINE.md` (offer, shape, customer, pricing in one document), `docs/DESIGN.md` (identity + design system), and the rest. That folder is the source of truth: share it, commit it, and point anyone new at it. If your repo already has a `docs/` folder, the ProductOS documents simply live alongside what's there.
5. When a checklist says "Run `define-offer-builder`", just ask your agent to do that — the skill triggers by name or by describing what you want ("help me build my product offer").
6. **Lost your place, or back after a break?** Just tell your agent *"continue"*. It works out where you are — your plan, your phase, and the route each phase saved in `docs/PATH.md` — tells you in plain words, and picks up the next step. The Claude Code plugin greets you with the same summary when a session starts; in other agents, the guidelines setup wires in have your agent do the same when you open a session.

## How it's organized

- **`productos/START-HERE.md`** — the front door: setup in three steps, and how your programme plan works.
- **Checklists** (`*-CHECKLIST.md`) — the runbook for each phase. Source of truth for how each step runs; your plan and your shape say which steps apply to you. The phase orchestrators (`define-phase` … `distribute-phase`) walk them with you.
- **`productos/shapes/`** — the twelve product shapes, one file each: what "live" and "first sale" mean, and how every step adapts.
- **`productos/ROUTING.md`** — which step runs next: your plan, then your shape, then the checklist order.
- **Numbered worksheets** (`1-`–`4-` in each phase folder) — the structure and `> Good/Bad` calibration each skill follows. The skills read them and write your answers to `docs/`; the worksheets stay blank.
- **BONUS docs** — reference playbooks: worked examples, failure patterns, channel guides, best-practice libraries.
- **`productos/skills/`** — one flat folder per skill (45 total). Each contains a `SKILL.md` plus any bundled files it loads only when needed (`references/`, `templates/`).
- **`productos/scripts/`** — `status.py` shows where you are and what's next in plain English (*"python3 productos/scripts/status.py"*; add `--detail` for every step — the orchestrators run it for you), and `lint-skills.py` is the maintainer's check of every skill against Anthropic's skill-authoring rules.
- **`productos/setup/CLAUDE.md` + `productos/setup/AGENTS.md`** — agent guidelines wired into your repo root at setup (by `setup`), so your coding agent behaves from day one.

## Requirements

- A Claude plan with access to Claude Code, Cowork, or Claude Desktop (or Cursor/Codex for the build phase).
- Web search enabled — the Define and Distribute skills do live market research.

## Version

**2.0.0** — see `productos/CHANGELOG.md`. Licensed for individual commercial use — see `productos/LICENSE.md`.
