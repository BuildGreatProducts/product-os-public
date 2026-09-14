# Start Here

ProductOS takes a product from idea to revenue with AI agents, in four phases — **Define → Design → Develop → Distribute** — each with a checklist, templates, and skills that fill them in. It lives **inside your app's repository**: setting up ProductOS is the first thing you do in the codebase, before there's any code.

## Set up (once, ~5 minutes)

1. **Create or open your app repo.** Building from scratch? Make an empty folder and `git init` it — the repo exists before the product does. Already have a codebase? That repo is the one.
2. **Put ProductOS in it as `productos/`** — clone this folder into the repo root, named exactly `productos`. Cursor's `/add-plugin` needs a git clone, not a GitHub ZIP extract — see `productos/README.md`.
3. **Run `studio-setup`.** Just ask your agent: *"Set up ProductOS."* It wires the coding-agent guidelines into your repo root (`CLAUDE.md`/`AGENTS.md`, from `productos/setup/` — appended, never overwriting what's already there) and adds `productos/` to your `.gitignore` — ProductOS is licensed to you, not to the public, so the materials stay uncommitted while your outputs are tracked as normal.

If your copy came from your coach, your custom programme is already inside it: setup moves it to **`docs/PLAN.md`** and verifies it against your actual repo. The plan — composed from your onboarding call — says which steps of each phase you'll do in full, which are fast-tracked from what already exists, which you can skip and why, and the exact order to work in.

Two things are in every programme, whatever your stage, because they're where the value concentrates:

- **The Define work** — the product offer is what clarifies exactly what you're building. If you already have a product, you take the fast-track: `studio-define-from-code` extracts the drafts from what exists, then the review sharpens them. Arriving with a business but no idea? `studio-define-leverage-finder` finds the idea first.
- **The Distribute loop** — everyone needs distribution. Only the timing varies.

## Starting completely from scratch?

No plan in your copy? After setup (steps 1–3 always apply), run a **challenge**: ask your agent to *"start ship in 7"* if your app isn't live yet — seven sessions to a live URL — or *"start sell in 30"* if it's live and nobody has paid — thirty sessions to your first customer. Each reads your repo, asks where you're starting from, composes a day-by-day plan from the ProductOS skills, checks in with you every session, and ends with a report you can bring to a Product Studio call. (If you run a challenge before setup, it runs setup for you.)

Prefer the long way, or want the full programme after a challenge? Open **`productos/define/DEFINE-CHECKLIST.md`** and work top to bottom, finishing each phase before the next. That's the standard programme — custom plans ship with coached copies.

## Where things live

- **`productos/`** — the system: phase folders, checklists, templates, skills. Gitignored — never committed to your repo.
- **`docs/`** (repo root) — your product's canon: `PLAN.md` (your programme), `PRODUCT.md`, `DESIGN.md`, `PRD.md`, `ROADMAP.md`, `LAUNCHES.md`, and the rest accumulate here as the skills produce them. Tracked in git — these are yours. If the repo already has a `docs/` folder, they live alongside what's there.
- **Root `CLAUDE.md` / `AGENTS.md`** — coding-agent guidelines wired at setup, so your agent behaves from day one of the build.
- **Phase checklists** (`productos/define/DEFINE-CHECKLIST.md` etc.) — how each step runs. Your plan says which steps apply to you; the checklists remain the source of truth for running them.

Plan revisions come from your coach — when circumstances change, they re-run the intake and send an updated `PLAN.md` (your agent replaces `docs/PLAN.md` with it). Installation options for each tool: see `productos/README.md`.
