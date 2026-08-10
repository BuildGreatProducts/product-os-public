# Start Here

ProductOS takes a product from idea to revenue with AI agents, in four phases — **Define → Design → Develop → Distribute** — each with a checklist, templates, and skills that fill them in. It lives **inside your app's repository**: setting up ProductOS is the first thing you do in the codebase, before there's any code.

## Set up (once, ~5 minutes)

1. **Create or open your app repo.** Building from scratch? Make an empty folder and `git init` it — the repo exists before the product does. Already have a codebase? That repo is the one.
2. **Put ProductOS in it as `productos/`** — clone or copy this folder into the repo root, named exactly `productos`.
3. **Run `studio-setup`.** Just ask your agent: *"Set up ProductOS."* It wires the coding-agent guidelines into your repo root (`CLAUDE.md`/`AGENTS.md`, from `productos/setup/` — appended, never overwriting what's already there) and adds `productos/` to your `.gitignore` — ProductOS is licensed to you, not to the public, so the materials stay uncommitted while your outputs are tracked as normal.

If your copy came from your coach, your custom programme is already inside it: setup moves it to **`docs/PLAN.md`** and verifies it against your actual repo. The plan — composed from your onboarding call — says which steps of each phase you'll do in full, which are fast-tracked from what already exists, which you can skip and why, and the exact order to work in.

Two things are in every programme, whatever your stage, because they're where the value concentrates:

- **The Define work** — the product offer is what clarifies exactly what you're building. If you already have a product, you take the fast-track: `studio-define-from-code` extracts the drafts from what exists, then the review sharpens them.
- **The Distribute loop** — everyone needs distribution. Only the timing varies.

## Starting completely from scratch?

No plan in your copy, or just an idea and happy with the default path? After setup (steps 1–3 always apply), open **`productos/define/DEFINE-CHECKLIST.md`** and work top to bottom, finishing each phase before the next. That's the standard programme — custom plans ship with coached copies.

## Where things live

- **`productos/`** — the system: phase folders, checklists, templates, skills. Gitignored — never committed to your repo.
- **`docs/`** (repo root) — your product's canon: `PLAN.md` (your programme), `PRODUCT.md`, `DESIGN.md`, `PRD.md`, `ROADMAP.md`, `LAUNCHES.md`, and the rest accumulate here as the skills produce them. Tracked in git — these are yours. If the repo already has a `docs/` folder, they live alongside what's there.
- **Root `CLAUDE.md` / `AGENTS.md`** — coding-agent guidelines wired at setup, so your agent behaves from day one of the build.
- **Phase checklists** (`productos/define/DEFINE-CHECKLIST.md` etc.) — how each step runs. Your plan says which steps apply to you; the checklists remain the source of truth for running them.

Plan revisions come from your coach — when circumstances change, they re-run the intake and send an updated `PLAN.md` (your agent replaces `docs/PLAN.md` with it). Installation options for each tool: see `productos/README.md`.
