# Start Here

ProductOS takes a product from idea to revenue with AI agents, in four phases — **Define → Design → Develop → Distribute** — each with a checklist, worksheets, and skills. Everything the skills produce lands in your repo's `docs/` folder. It lives **inside your app's repository**: setting up ProductOS is the first thing you do in the codebase, before there's any code.

## Set up (once, ~5 minutes)

1. **Create or open your app repo.** Building from scratch? Make an empty folder and `git init` it — the repo exists before the product does. Already have a codebase? That repo is the one.
2. **Put ProductOS in it as `productos/`** — clone this folder into the repo root, named exactly `productos`. Cursor's `/add-plugin` needs a git clone, not a GitHub ZIP extract — see `productos/README.md`.
3. **Run `setup`.** Just ask your agent: *"Set up ProductOS."* It wires the coding-agent guidelines into your repo root (`CLAUDE.md`/`AGENTS.md`, from `productos/setup/` — appended, never overwriting what's already there) and adds `productos/` to your `.gitignore` — ProductOS is licensed to you, not to the public, so the materials stay uncommitted while your outputs are tracked as normal.

If your copy came from your coach, your custom programme is already inside it: setup moves it to **`docs/PLAN.md`** and verifies it against your actual repo. The plan — composed from your onboarding call — says which steps of each phase you'll do in full, which are fast-tracked from what already exists, which you can skip and why, and the exact order to work in.

Two things are in every programme, whatever your stage, because they're where the value concentrates:

- **The Define work** — the product offer is what clarifies exactly what you're building. If you already have a product, you take the fast-track: `define-from-code` extracts the drafts from what exists into `docs/DEFINE.md`, then the review sharpens them. Arriving with a business, expertise, or a passion but no idea? `define-idea-finder` finds the idea first.
- **The Distribute loop** — everyone needs distribution. Only the timing varies.

## No plan? Two paths

After setup (steps 1–3 always apply), setup looks at your repo and recommends one of two paths:

- **New project — nothing built yet.** Ask your agent to *"build my product offer"*: `define-offer-builder` is Step 1 of **`productos/define/DEFINE-CHECKLIST.md`**. From there, work top to bottom, finishing each phase before the next — that's the standard programme. No idea yet? `define-idea-finder` finds one first.
- **Existing project — code, a prototype, or an AI-generated app.** Ask your agent to *"start ship in 7"*: seven sessions to your app live at a real URL. It reads your repo, asks where you're starting from, composes a session-by-session plan from the ProductOS skills, checks in with you every session, and ends with a report you can bring to a Product Studio call. Already live? Its follow-on, *"start sell in 30"*, takes you to your first paying customer. (If you start a challenge before setup, it runs setup for you.)

Custom plans ship with coached copies of ProductOS.

## Where things live

- **`productos/`** — the system: phase folders, checklists, worksheets, skills. Gitignored — never committed to your repo, and no skill writes your work into it.
- **`docs/`** (repo root) — the source of truth for everything ProductOS produces: `PLAN.md` (your programme), `DEFINE.md` (offer, customer, and pricing in one document), `DESIGN.md` + `DESIGN.html` (your identity and design system), `COPY.md`, `PRD.md`, `ROADMAP.md`, `GO-TO-MARKET.md`, and the rest accumulate here as the skills produce them. Tracked in git — these are yours, and they're what you share. If the repo already has a `docs/` folder, they live alongside what's there.
- **Root `CLAUDE.md` / `AGENTS.md`** — coding-agent guidelines wired at setup, so your agent behaves from day one of the build.
- **Phase checklists** (`productos/define/DEFINE-CHECKLIST.md` etc.) — how each step runs. Your plan says which steps apply to you; the checklists remain the source of truth for running them.

Plan revisions come from your coach — when circumstances change, they re-run the intake and send an updated `PLAN.md` (your agent replaces `docs/PLAN.md` with it). New versions of ProductOS itself: ask your agent to *"update ProductOS"* — it keeps everything you've written, and moves anything an older copy kept inside `productos/` into `docs/`. Installation options for each tool: see `productos/README.md`.
