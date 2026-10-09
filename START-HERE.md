# Start Here

ProductOS takes an AI product from idea to revenue with AI agents — an app, an extension, an agent plugin or skill, an MCP server, a chat assistant, a developer tool, a productized service, a website, or a digital product — in four phases: **Define → Design → Develop → Distribute**, each with a checklist, worksheets, skills, and an orchestrator that walks it with you. Everything the skills produce lands in a `docs/` folder in your product's folder. It lives **inside your product's folder**: setting up ProductOS is the first thing you do there, before there's any code.

## Set up (once, ~5 minutes)

1. **Make or open your product's folder.** Building from scratch? An empty folder is all you need — no git, no terminal. Already have a codebase? That folder is the one.
2. **Put ProductOS in it as `productos/`** — copy this folder in, named exactly `productos`. (Or skip this: open ProductOS on its own, run setup, and it makes your product's folder and moves itself in.) Cursor's `/add-plugin` needs a git clone, not a GitHub ZIP extract — see `productos/README.md`.
3. **Run `setup`.** Just ask your agent: *"Set up ProductOS."* It wires the coding-agent guidelines into your folder (`CLAUDE.md`/`AGENTS.md`, from `productos/setup/` — appended, never overwriting what's already there) and adds `productos/` to your `.gitignore`, so ProductOS's own files never end up in your product's history.

Version history (git) comes later: at the start of Develop, if your product is built from code, your agent turns it on for you. Define and Design run in the plain folder.

If your copy came from your coach, your custom programme is already inside it: setup moves it to **`docs/PLAN.md`** and verifies it against what's actually in your folder. The plan — composed from your onboarding call — says which steps of each phase you'll do in full, which are fast-tracked from what already exists, which you can skip and why, and the exact order to work in.

Two things are in every programme, whatever your stage, because they're where the value concentrates:

- **The Define work** — the product offer and its shape are what clarify exactly what you're building. If you already have a product, you take the fast-track: `define-from-code` extracts the drafts from what exists into `docs/DEFINE.md`, then the review sharpens them. Arriving with a business, expertise, or a passion but no idea? `define-idea-finder` finds the idea first.
- **The Distribute loop** — everyone needs distribution. Only the timing varies.

## No plan? One question

After setup (steps 1–3 always apply), setup asks one question — **where would you like to start?** — and suggests an answer if your folder points to one:

- **Find a new idea.** You have a business, expertise, or a passion, but no product idea yet: `define-idea-finder` finds the one worth building, then the Define phase carries on from it.
- **Start from an idea you have.** `define-phase` walks the Define phase step by step — your offer, your product's **shape** (web app, mobile app, agent skill or plugin, MCP server, chat assistant, developer tool, productized service, website, digital product…), your customer, your price — then hands on to `design-phase`, `develop-phase`, and `distribute-phase`. Your shape decides which steps you run and what "live" means for you.
- **Start from an existing project — code, a prototype, an AI-generated app, a live service or listing.** `product-audit` scores what you have across all four phases, names your shape and stage, and writes a programme to `docs/PLAN.md`; `product-refactor` then works through it step by step.

- **Take on a challenge.** You want a deadline: *Ship in 7* gets your product live in seven sessions, from wherever you are; *Sell in 30* takes a live product to its first paying customer in thirty.

Whichever you pick, from then on you only need to say **"continue"**. Didn't pick a challenge? Your agent offers them again when they fit — *Ship in 7* once Define is done, *Sell in 30* once you're live — and you can ask for either by name any time. (If you start a challenge before setup, it runs setup for you.)

Coached copies of ProductOS ship with a custom plan from your coach, which replaces an audit plan.

Lost your place, or back after a break? Just tell your agent **"continue"** — it works out where you are, tells you in plain words, and picks up the next step. (`python3 productos/scripts/status.py` prints the same summary.) Unfamiliar word? `productos/GLOSSARY.md` explains it.

## Where things live

- **`productos/`** — the system: phase folders, checklists, worksheets, skills, and the shape files (`productos/shapes/`). Gitignored — never committed to your repo, and no skill writes your work into it.
- **`docs/`** (repo root) — the source of truth for everything ProductOS produces: `PLAN.md` (your programme), `DEFINE.md` (offer, shape, customer, and pricing in one document), `DESIGN.md` + `DESIGN.html` (your identity and design system), `COPY.md`, `PRD.md`, `ROADMAP.md`, `GO-TO-MARKET.md`, and the rest accumulate here as the skills produce them. Tracked in git — these are yours, and they're what you share. If the repo already has a `docs/` folder, they live alongside what's there.
- **Root `CLAUDE.md` / `AGENTS.md`** — coding-agent guidelines wired at setup, so your agent behaves from day one of the build.
- **Phase checklists** (`productos/define/DEFINE-CHECKLIST.md` etc.) — how each step runs. Your plan says which steps apply to you; the checklists remain the source of truth for running them.

Plan revisions come from your coach — when circumstances change, they re-run the intake and send an updated `PLAN.md` (your agent replaces `docs/PLAN.md` with it). An audit plan is revised by re-running `product-audit`. New versions of ProductOS itself: ask your agent to *"update ProductOS"* — it keeps everything you've written, and moves anything an older copy kept inside `productos/` into `docs/`. Installation options for each tool: see `productos/README.md`.
