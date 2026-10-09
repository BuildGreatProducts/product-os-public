---
name: setup
description: >-
  Installs ProductOS into the product's project folder: checks productos/ sits inside one (making
  one for a standalone copy), wires the coding-agent guidelines into the root CLAUDE.md and
  AGENTS.md without overwriting, gitignores productos/, adopts a coach's plan into docs/PLAN.md,
  and asks where the member wants to start. At the start of Develop it turns on version history
  (git) for products built from code. Use first after receiving ProductOS, or when the user says
  "set up ProductOS", "install ProductOS", or "turn on version history". Safe to re-run. Not for
  upgrading an installed copy — use update.
---

# Setup — install ProductOS and adopt your plan

Install ProductOS into the product's project folder — the first thing to run after receiving a copy — and, if the copy came from the member's coach, move the custom programme plan it carries to `docs/PLAN.md`, where every ProductOS skill expects it. It takes minutes. The only files it writes are the root `CLAUDE.md`/`AGENTS.md`, `.gitignore`, and `docs/PLAN.md` (moved from the seed) — plus, at the start of Develop, the first commit of version history. Every check is idempotent — re-running costs seconds and fixes whatever drifted.

**No git yet.** Define and Design need only the project folder. Version history (git) goes on at the start of Develop, and only when the product is built from code in this folder — see [Version history](#version-history--at-the-start-of-develop) below. A folder that's already a git repository stays one.

## Workflow

### 1. Find the project folder

ProductOS lives as `productos/` inside the product's **project folder** — the folder that holds everything for the product: `docs/`, the root guidelines, and later any code. Check where this folder sits:

- **It's `productos/` inside a folder that's for this product** → that folder is the project folder. Carry on. (A general folder — the home folder, Desktop, Downloads, Documents — isn't one: treat that as standalone.) (Already a git repository? Then version history is already on — note it.)
- **It's standalone** — the folder you're working in is ProductOS itself (its `README.md`, `ROUTING.md`, and `skills/` at the top level), or it isn't named `productos` → set up the project folder *for* the member rather than handing them instructions. From scratch is no exception; the project folder exists before the product does.
  1. Ask only what you can't decide: does the product already have a folder (existing code, an export, a site's files)? If not, what should the new one be called (default: the product's working name, or `my-product`), next to where ProductOS sits now?
  2. Create the folder if new, and move this folder into it as `productos/` exactly.
  3. Tell the member in one plain line — *"I made a folder for your product; everything ProductOS writes for you goes in it."* — then name the folder and ask them to reopen their agent (or their Claude Desktop or Cowork project) in it, because this session started in the old location.

### 2. Wire the root guidelines

The project folder's root needs the coding-agent guidelines from `productos/setup/`:

- Root `CLAUDE.md`/`AGENTS.md` **don't exist** → copy them from `productos/setup/` whole.
- The folder **already has them** → **never overwrite** the member's content. Append the `<!-- BEGIN PRODUCTOS -->…<!-- END PRODUCTOS -->` block from the matching file in `productos/setup/`, and add one pointer line to `productos/setup/CLAUDE.md` (for the full guidelines) **inside** the markers, just before `<!-- END PRODUCTOS -->`. If the markers are already present (a re-run), replace everything between them — pointer line included — with the fresh block; never append a second block.

Wire whichever file(s) match the member's coding agent(s); default is both.

### 3. Gitignore the system

Ensure the project folder's `.gitignore` contains a `productos/` line (create or append; skip if present) — even before version history is on, so it's in place from the first save. If the folder is already a git repository, check it actually took effect: if `productos/` was committed before the line existed (`git ls-files productos | head -1` returns anything), untrack it with `git rm -r --cached productos/` and commit that change for them — an ignore line does nothing for files already tracked. ProductOS is licensed to the member, not the public — the materials stay uncommitted, while the member's outputs (`docs/`, the wired root files) are theirs and stay tracked as normal. Don't walk the member through the mechanics; one line covers it unless they ask: *"ProductOS's own files stay out of your project's history; everything it writes for you is saved as normal."*

### 4. Adopt the plan

If **`productos/PLAN.md`** exists (it ships inside coached copies), move it to **`docs/PLAN.md`** — create `docs/` first if needed (`mkdir -p docs`). Then a light verification pass:

1. Read the plan's **Inventory** and the *Check at setup* lines in its **Your Programme** list.
2. Check each item against the actual repo, now that it's readable — does the app run, does the core flow work, does the codebase match what the plan assumed?
3. Where reality matches, confirm and move on. Where it doesn't, apply the plan's own stated consequence ("if the core flow doesn't run end to end, Develop route becomes 3b") and **annotate** the affected step — a one-line note under the relevant programme step, dated.

Older plans may use retired names. Read them as follows, and don't rewrite the plan for a rename:

| The plan names | Read it as |
| --- | --- |
| `studio-<name>` (before 1.11.0, e.g. `studio-define-pricing`) | `<name>` — the prefix simply drops |
| `define-leverage-finder` / `studio-define-leverage-finder` (before 1.12.0) | `define-idea-finder` |
| `mini-launch` / `studio-launch` (before 1.14.0) | Retired — launches are no longer part of the system. Annotate the step as retired. |
| `define-product` / `studio-define-product` (before 1.14.0) | Retired — the Define skills write `docs/DEFINE.md` directly, so there's no synthesis step. Annotate the step as retired. |
| `docs/PRODUCT.md` | `docs/DEFINE.md` |
| `cc-build-loop` / `codex-build-loop` / `cursor-build-loop` (before 1.15.0) | `build-loop` |
| `develop-mvp-build` / `develop-refactor-build` (before 1.15.0) | `develop-build` |
| `develop-refactor-plan` (before 2.0.0) | `develop-prd-roadmap` in existing-codebase mode — it writes the gap into `docs/ROADMAP.md` |
| `docs/REFACTOR.md` | Still run by `develop-build` if it has unchecked tasks; new plans use `docs/ROADMAP.md` |
| A plan with no `define-product-shape` step (before 2.0.0) | Insert nothing — annotate the plan's first Design step: *"run `define-product-shape` first (added in ProductOS 2.0)"*. |

Annotate, don't recompose: this pass adjusts details the coach couldn't see, it does not redesign the programme. Anything bigger — the member's situation has genuinely changed, a phase no longer fits — goes back to the coach, who re-runs the intake and re-delivers an updated `PLAN.md` (replace `docs/PLAN.md` with it when it arrives).

### 5. Name the first action

Say it in plain words — what the first step does for the member, not its skill name — and end with the one thing to remember: saying **"continue"** starts it now, and picks up from wherever they stop in every later session (the `continue` skill).

- **Plan adopted** → read its **Your Programme** list and tell the member what their first step is and why, e.g. *"Your plan starts by pulling your offer and customer out of the app you've already built, so you don't start from a blank page. Say "continue" to start."*
- **No plan anywhere** (and no challenge already open in `docs/`) → one question decides the path. Ask it as a four-way choice (a multiple-choice prompt where the agent has one):

  > **Where would you like to start?**
  > 1. **Find a new idea** — you have a business, expertise, or a passion, but no product idea yet.
  > 2. **Start from an idea you have** — you know what you want to build, and nothing's built yet.
  > 3. **Start from an existing project** — code, a prototype, an app on a builder like Lovable or Bolt, or a live site, service, or listing.
  > 4. **Take on a challenge** — *Ship in 7*: your product live in seven sessions. *Sell in 30*: your first paying customer in thirty, for a product that's already live.

  Look before you ask: product code beyond `productos/` and `docs/`, a platform export, a live URL in a README. If the folder points to an answer, put it first and say why (*"There's an app in `src/`, so I'd start from your existing project — sound right?"*), but still let the member pick.

  - **Find a new idea** → **`define-phase`** on its idea-first route: `define-idea-finder` finds the idea, then the offer work begins.
  - **An idea they have** → **`define-phase`** on its new-idea route, starting with the offer.
  - **An existing project** → **`product-audit`**: it looks at what exists, scores it, and writes a plan in `docs/PLAN.md`, which `product-refactor` then works through.
  - **A challenge** → if the member didn't name one, pick by the folder: a product that's already live → **`sell-in-30`**; anything else, from an idea to a working prototype → **`ship-in-7`**. Say which and why in one line and let them switch. The challenge enrols them and takes it from there; its own checks route a not-yet-live product from Sell in 30 to Ship in 7.

  Tell `define-phase` which route the member chose, so it doesn't ask again.

  Ask nothing else here: no menu of skills. For a member who doesn't choose a challenge now, the challenges come up again when they fit — the audit can open its plan with one, `define-phase` offers Ship in 7 once Define is done, and `develop-phase` offers Sell in 30 once the product is live. A member who asks for a challenge by name, at any point, gets it straight away. (Custom programmes from a coach ship inside coached copies of ProductOS and replace an audit plan.)

Setup installs the copy the member already has; it doesn't fetch a newer one. Re-running setup to pick up a new release? Run **`update`** instead — it brings `productos/` up to the latest version, moves anything an older copy left inside `productos/` into `docs/`, and runs steps 2–3 of this skill itself.

## Version history — at the start of Develop

Run this section when Develop starts (`develop-phase` calls it first, and the skills that write or move code send the member here if it's missing), or any time the member asks to turn version history on. It's Develop Step 2 in [ROUTING.md](../../ROUTING.md) — hard rule 6.

1. **Read the shape's need.** The primary shape's Develop route row *2 — Verify setup* in `productos/shapes/<slug>.md` (from this skill's folder, `../../shapes/<slug>.md`) — or the `## Develop` row in `docs/PATH.md`, once it's set.
   - **Full** — the product is built from code in this folder — or **Full / Skip** with the Full condition holding → version history is needed.
   - **Skip**, or **Full / Skip** with the condition failing (everything lives in hosted or no-code tools) → not needed. Say so in one line, and offer it only as a way to keep drafts.
2. **Already a git repository?** Nothing to turn on — re-check step 3's untracked rule and go to 4.
3. **Turn it on.** `git init`; confirm `.gitignore` has `productos/` (step 3); then save everything else — `docs/`, the root guidelines, any existing code — as the first commit, *Start version history*. Tell the member in one plain line: *"I've turned on version history: from here every change to your product is saved and can be undone."* No git on the machine? Say so plainly and give the one thing to do — on a Mac, accept the "install developer tools" prompt that appears the first time git runs; on Windows, install Git from git-scm.com — then carry on.
4. **Check the guidelines.** The root `CLAUDE.md`/`AGENTS.md` carry the PRODUCTOS block (step 2). Backing the project up to GitHub comes later, when the build or go-live needs it; mention it then, not now.

## Verify before ending

- [ ] `productos/` sits inside the product's project folder.
- [ ] The root `CLAUDE.md`/`AGENTS.md` carry exactly one PRODUCTOS block.
- [ ] `.gitignore` excludes `productos/`, and — if version history is on — nothing under it is tracked.
- [ ] Version history is on wherever Develop has started on a product built from code here, and nowhere it isn't needed yet.
- [ ] Any shipped plan lives at `docs/PLAN.md` with its setup checks resolved or annotated.
- [ ] The member knows exactly what to do first, and that saying "continue" picks up from there — now and in every later session.

Anything less — name the gap and fix it before ending the session.
