---
name: ship-in-7
description: >-
  Runs the ProductOS Ship in 7 challenge — seven sessions to the product shape's Live-means bar,
  passed as a real customer. Reads the repo and shape, picks the plan for the shape and starting
  point (idea, AI-generated app, prototype, platform, agent product, service or digital product),
  logs each session's proof in docs/SHIP-IN-7.md, and closes with a Ship Report. Use for "ship in
  7", "launch in 7 days", "start the challenge", or when docs/SHIP-IN-7.md has Status: Open. Not
  for a live product that needs customers — use sell-in-30.
---

# Ship in 7 — the launch challenge

Ship in 7 takes a member from wherever they are to **their product live, in seven sessions** — live as its shape defines it. It is the first thing a community member runs after installing ProductOS, and it is an orchestrator: every session names one existing ProductOS skill to run, one artefact it produces, and one piece of proof. This skill owns the sequencing, the daily accountability loop, and the log in `docs/SHIP-IN-7.md`; it never teaches what the skills it runs already teach.

**The bar:** **the shape's Live-means bar, passed as a real customer.** It comes from `docs/DEFINE.md` → `## Product Shape` → `### Live Means`, which `define-product-shape` writes from the shape file's `## Live means` (`productos/shapes/<slug>.md`; from this skill's folder, `../../shapes/<slug>.md`); if the DEFINE section is missing that subsection, read the shape file's. For a web app: a live URL where a fresh account signs up, does the core thing, and sees it work. For an agent plugin: a stranger installs it from the public link and gets the first output on the first try. For a productized service: a stranger can buy it and receive the delivery. Passing that bar as a real customer is the **smoke test** everywhere below. Not a beta user, not a first sale, not a landing page alone. Announcing it is the Day 7 stretch, never the bar. Whatever the member arrives with, Day 7 is the same. The composition changes; the destination doesn't.

**Register:** coach at the moment of fear. The bar is visibly low and non-negotiable. Shipping is the achievement; silence is an entry; never shame a zero. Blunt about proof, warm about everything else.

**Days, misses and gaps.** Seven sessions, not seven calendar days: recommend consecutive days, but the counter advances by check-in. Day 0 is the enrol; Days 1–7 each open with a short check-in, then run the day's block; the close follows Day 7. A day is *assigned* at the check-in that names its block; the next check-in confirms its proof: present → done; partial → logged as partial; absent → a **miss**, logged as one, and its block re-planned under the compression list, never silently re-assigned. Calendar time between check-ins is a **gap**, noted with dates, never a miss. A second check-in on the same day, or a member saying the block is still in progress, *continues* the current day rather than advancing the counter.

## Inputs

Read inputs from `docs/` and the ProductOS folder (`productos/`) at the app repo root.

1. **The Product Shape** — `docs/DEFINE.md` → `## Product Shape` (`### Primary Shape` for the slug, `### Live Means` for the bar), then only the `## Live means` and `## Develop route` sections of the shape file. Missing → enrol step 3 runs `define-product-shape` first.
2. **The repo itself.** Whether app code exists beyond `productos/`; framework, deploy config (`vercel.json`, `Dockerfile`, `eas.json`, …), a production URL anywhere; whether the UI reads as generated (default component-library look, inconsistent spacing, marketing-voice copy); whether it is a prompt-to-app platform export (Lovable, Bolt, v0, Base44).
3. **The ProductOS documents**, if any: `docs/DEFINE.md`, `docs/COPY.md`, `docs/DESIGN.md`, `docs/PRD.md`, `docs/ROADMAP.md`, `docs/EVALS.md`, `docs/SECURITY-AUDIT.md`, `docs/LANDING-PAGE.md` / `docs/MARKETPLACE-LISTING.md` / `docs/APP-LISTING.md`, `docs/DEPLOY.md`.
4. **`docs/PLAN.md`**, if present (a coached copy). Compose from its Develop route and annotate it; never override it.
5. **`docs/SHIP-IN-7.md`**, if present: an open challenge means this is a check-in or a close, not an enrol. **`docs/SELL-IN-30.md`** open means stop: only one challenge runs at a time.
6. **The plan library in this folder:** [PLAN-idea-only.md](PLAN-idea-only.md), [PLAN-ai-generated-app.md](PLAN-ai-generated-app.md), [PLAN-local-prototype.md](PLAN-local-prototype.md), [PLAN-platform-migration.md](PLAN-platform-migration.md), [PLAN-agent-product.md](PLAN-agent-product.md), [PLAN-service-or-digital.md](PLAN-service-or-digital.md), and [SHIP-IN-7-TEMPLATE.md](SHIP-IN-7-TEMPLATE.md). Read only the plan file the shape and starting point select.

## Which mode is this?

Read the header's `Status:` line first.

- No `docs/SHIP-IN-7.md`, or the file's status is `Closed` → **Enrol** (Day 0). A closed file is a finished Ship Report: move it to `docs/SHIP-IN-7-<closed date>.md` before writing the new one, never overwrite it.
- Status `Open` and Day 7 not yet logged → **Daily check-in** (confirming Day 7's proof leads straight into the Close).
- Status `Open`, Day 7 logged (or the member says "close") → **Close**.

Confirm with the member in one line before proceeding.

---

## Mode 1 — Enrol (Day 0)

### 1. Setup check

Ship in 7 runs after `setup`, but the member may run it first. Check the four setup conditions: `productos/` sits inside a git repo; the root `CLAUDE.md`/`AGENTS.md` carry the `<!-- BEGIN PRODUCTOS -->` block; `.gitignore` excludes `productos/` *and* nothing under it is tracked (`git ls-files productos` is empty); any shipped `productos/PLAN.md` has been moved to `docs/PLAN.md`. **If any fails, run `setup` in full now** (it takes seconds and is idempotent), then continue. Don't send the member away.

### 2. Read the repo and show the evidence

One short block, facts only: what exists (code, framework, docs, deploy config, live URL, listing or package) and what's missing. No judgement yet, no recommendation.

### 3. Read the shape

Read `docs/DEFINE.md` → `## Product Shape`. **If it's missing** (no section, or no DEFINE.md at all), run `define-product-shape` now as a short fast-track session before composing anything: for an idea-only member it works from the idea in a sentence or two, and Day 1's Define re-confirms it. State the primary shape and its Live-means bar back in one line; the bar goes into the file verbatim.

### 4. Ask the starting point

The shape picks the plan family; the starting point picks the plan within it. Present the starting points the evidence fits, plus "none of these", and **ask**. Never recommend; the member knows things the repo doesn't.

| Shape | Starting point | Typical evidence | Plan file |
| --- | --- | --- | --- |
| Screen shapes and `developer-tool` | **Idea only** | No app code beyond `productos/`; no `docs/DEFINE.md` | `PLAN-idea-only.md` |
| | **AI-generated app, not live** | App code; no `docs/DESIGN.md` or `docs/COPY.md`; generated look | `PLAN-ai-generated-app.md` |
| | **Local prototype** | App code; no deploy config, no `docs/DEPLOY.md`, no production URL | `PLAN-local-prototype.md` |
| | **Prompt-to-app platform** | A Lovable / Bolt / v0 / Base44 project, no owned repo | `PLAN-platform-migration.md` |
| `agent-skill`, `agent-plugin`, `mcp-server`, `chat-assistant` | **Idea, or a working build** | A skill folder, plugin manifest, MCP server code, or assistant instructions — or nothing yet | `PLAN-agent-product.md` |
| `productized-service`, `digital-product`, `website` | **Idea, or partly built** | An offer, a draft page, a product file, a delivery process — or nothing yet | `PLAN-service-or-digital.md` |

**Plan-selection rule:** pick the plan family by the primary shape, never by the code alone. The two non-screen plans each cover both idea and existing-build starts: drop the blocks whose artefact already exists and is current. The four screen plans are written for a `web-app`; for `mobile-app`, `desktop-app`, `browser-extension`, and `developer-tool`, keep the plan and swap Go live's work and proof for the shape's (store submission, signed installer, extension store listing, published package), reading the shape file's `## Develop route` for the go-live step. Where go-live passes through a store review, submit by Day 5 so the review can land inside the week; a review still pending on Day 7 is logged honestly as the one thing between the member and the bar.

**App code that isn't live fits two rows** (AI-generated app, local prototype). The question that separates them is not the code, it's the look: *"Are you happy with how it looks, or do you want it to look designed by Day 7?"* Designed → AI-generated app (two rebuild days). Happy → local prototype (a fuller gate and a polish day). Ask it as a question, not a recommendation.

If they pick "none of these", compose from the block library directly (below) and say which plan file is closest.

### 5. Confirm the inputs

- **Start date.** Default tomorrow, so Day 1 is a full session.
- **Hours per session.** A number, not a tier. Say what that number means for this starting point: the plan is one plan scaled to their hours, never a "1h plan" and a "2h plan". Recommend more time where it changes the outcome. An **idea-only** member whose hours can't carry Define, spec, build, gate and deploy in seven sessions is told so plainly, before the plan is written — with the honest alternative (more hours, or a smaller magic moment).
- **Consecutive days.** Recommend them. Weekends and life will get in the way for some; that's a gap, not a miss.
- **The Skool community.** Ask whether they're in it. If not, skip every Skool post step and leave the post log out of the file.

### 6. Compose the seven sessions

Start from the `PLAN-*.md` file for the shape and starting point, then adjust using the block library and the composition rules below: drop a block only when its artefact exists **and is current and complete** (a `docs/DEFINE.md` that describes today's product; a `docs/SECURITY-AUDIT.md` whose verdict covers today's code with Critical/High fixed, not merely a file with that name); otherwise keep the block. Add the ones the evidence says are missing, fit to the hours. Show the plan as a table — session, block, skill, proof, hours — and let the member edit before anything is written.

### 7. Write `docs/SHIP-IN-7.md`

From `SHIP-IN-7-TEMPLATE.md` (create `docs/` if needed): the header (start date, hours, the shape, the bar verbatim, the starting point), the plan table, the empty session log, the Skool post log (only if the member is in the Skool community). The member's file, tracked in git.

### 8. Draft the Day-0 Skool post and name Day 1

Skip the post if the member isn't in the Skool community. Title `Ship in 7 - Day 0! [app name]`; body in the member's voice (see **The Skool post**). End by naming Day 1's literal first action: the skill to run and the proof that ends the session.

---

## Mode 2 — Daily check-in (Days 1–7)

Every session in the repo starts here while the challenge is open (the root guidelines say so). Five minutes of overhead, then the day's block.

1. **Find the day.** Read the log: the last assigned day is the one to confirm. If the member says its block is still in progress, continue it; don't advance. Note any gap since the last check-in with dates; a gap is not a miss.
2. **Confirm the last assigned day's proof first.** "Did it ship? Show me." A file that now exists in the repo, a screenshot saved to `docs/` (something the agent can open), a URL, a passing command. A draft is not proof; a description of what was planned is not proof; a screen recording the agent can't open is a claim, not proof.
3. **Log it.** Done / partial / missed, the proof, a one-line blocker. No proof → that day is a miss, logged as one. **Partial** (the artefact exists but the day's bar isn't met, e.g. the audit is written but Critical findings aren't fixed): log it as partial, carry the remainder into the next day as its first task, and apply the first compression action. Two partials in a row count as a miss.
4. **Missed?** Use the selected plan file's **Compression** list, in order, first action that fits; the list under *Compression* below applies only to custom compositions. Constraints ("never move Go live…") are rules, not steps — no compression action may break one. Two consecutive misses → shrink the scope of the MVP to the magic moment alone (every other roadmap item moves to `docs/ROADMAP.md`'s later phases), never the bar. If the MVP is already the magic moment alone, the next lever is hours: ask for more, or name the honest miss now rather than on Day 7.
5. **Assign today's one block**: the skill to run, the artefact, the proof. Update the header's status line to today's day (`Status: Open · Day 4 of 7`). Then either run that skill in this session or hand off ("run `develop-golive`; come back when `docs/DEPLOY.md` exists and the accounts are created"). Say what the member needs to bring (an image they love for the Look block, hosting account logins for Go live).
6. **Draft today's Skool post** if the member is in the Skool community (title from the house format, body in the member's voice). If the block is handed off, draft it with a `[proof]` slot and finish it at the next check-in when the proof lands; a post never claims proof that doesn't exist yet.
7. **End by saying exactly what returning next time looks like.**

### Compression (custom compositions only)

When the member picked "none of these", use these actions in order, first that fits:

1. Drop the stretch (Announce).
2. Merge the two build days into one, scoped tighter: the magic moment and the path to it, nothing else.
3. Merge Words into Look (identity in a paragraph, copy rules from `docs/COPY.md`'s defaults) when the app exists and the look is the priority.

**Constraints — every path, every plan file:**

- Never move Go live past Day 7. Never skip the quality gate, and never move it after Go live.
- If the gate surfaces Critical findings on Day 5, Day 6 fixes them and Day 7 goes live; if that still doesn't fit, the smoke test is the honest miss and the close says so.

---

## Mode 3 — Close (Day 7 or 8)

Read [CLOSE.md](CLOSE.md) and follow it: check the bar honestly and close the status line, write the Ship Report, draft the graduation post, give the Product Studio recommendation, and verify the log before handing over.

---

## The block library

Every block is an existing skill (or a plain action) with a proof. The composer picks from here; the plan files are worked compositions.

| Block | Skill(s) | Produces | Proof | Typical |
| --- | --- | --- | --- | --- |
| Setup check | `setup` | wired root files, gitignore | file diff | 10 min |
| Shape | `define-product-shape` (short fast-track) | `## Product Shape` in `docs/DEFINE.md` | Primary Shape names a slug; Live Means filled | 20 min |
| Define from idea | `define-offer-builder` → `define-customer-persona` → `define-pricing`, compressed into one sitting | `docs/DEFINE.md` | Summary, Offer, Persona and Pricing filled | 2.5 h |
| Define backfill | `define-from-code` | `docs/DEFINE.md` | Summary, Offer, Persona and Pricing filled | 1 h |
| Words | `design-identity-creator` → `design-ux-writing` | the Product Identity in `docs/DESIGN.md` (the Brand Card), `docs/COPY.md` | the Product Identity section and `COPY.md` exist; `COPY.md`'s audit fix list present | 1.5 h |
| Look | `design-design-system` (one image you love) or `design-design-system-from-code` | `docs/DESIGN.md` + `docs/DESIGN.html` | screenshot of `DESIGN.html` | 1 h |
| Magic moment + spec | `design-magic-moment` → `develop-prd-roadmap`, MVP scoped to the magic moment only | `docs/PRD.md`, `docs/ROADMAP.md` | roadmap of one phase | 1.5 h |
| Evals *(agent shapes, AI-output products)* | `develop-agent-evals` | `docs/EVALS.md` | at least three scenarios with pass criteria | 1 h |
| Build | `develop-build` (idea) · `develop-design-better` + `build-loop` + `develop-design-review` (rebuild) · `develop-prd-roadmap` in existing-codebase mode (a gap roadmap in `docs/ROADMAP.md`) → `develop-build` (messy code) | the working core flow | before/after screenshots saved to `docs/`, or a recording the agent can open | 4 h+ per day |
| Acquisition surface | `design-landing-page` · `design-marketplace-listing` · `design-app-listing` — whichever the shape file names | `docs/LANDING-PAGE.md` / `docs/MARKETPLACE-LISTING.md` / `docs/APP-LISTING.md` | the file, and the page or listing drafted in place | 1.5 h |
| Checkout *(service, digital product)* | a payment link or checkout wired to delivery; a real test purchase, refunded | a working checkout | the receipt and the refund; the delivery received | 1.5 h |
| Migrate | `develop-migrate` | `docs/MIGRATION.md`, an owned repo | the migration's verification gate green | 1–2 days |
| Quality gate | `develop-code-review` → `develop-security-audit` → Critical/High fixed via the build loop | `docs/SECURITY-AUDIT.md` | the verdict line; Fix plan Critical/High ticked | 2–3 h |
| Deploy guide | `develop-golive` | `docs/DEPLOY.md` | file exists; accounts created | 1 h |
| **Go live** | work `docs/DEPLOY.md` top to bottom | live URL, HTTPS, domain (web app) · published listing, package, or registry entry · public page and checkout | **the shape's Live-means bar, passed as a real customer** | 2–3 h |
| Announce *(stretch)* | no skill: post the live link where your customers are | the post | the post's link or screenshot | 30 min |

### Composition rules

1. **Go live sits on Day 5, 6 or 7**: Day 6 with Day 7 as buffer and smoke test is the default; Day 5 when the gate is done early (the local-prototype plan); Day 7 outright when hours are tight. Never before the quality gate.
2. **The quality gate is never skipped.** Every shape that ships code (an app, a plugin's scripts and hooks, an MCP server, a bot backend, a custom checkout or delivery automation) runs the security audit before anything is reachable; agent shapes add their evals passing to the gate. A shape that ships no code of its own (a service sold through a payment link, a file on a marketplace) has a checkout-and-delivery dry run as its gate: a real purchase, refunded, and the delivery reaching the buyer.
3. **Define backfill is never skipped when `docs/DEFINE.md` is missing.** The Skool posts draw on it and `sell-in-30` opens by reviewing its offer. Compressed, not dropped.
4. **Design blocks are included only when the app exists and looks generated**, or when the member asks. On the idea path, Look runs on Day 2 so the build is on tokens from the first screen. The agent and service plans carry Words instead of Look: their listing or landing page is the product's face, and the shape file's Design route says where a Lite design system (brand tokens only) is enough.
5. **Build days are capped at two.** The MVP is the magic moment and the path to it. Everything else moves to later roadmap phases.
6. **One plan, scaled to the hours the member gave.** Never present two named plans.
7. **`docs/PLAN.md` present:** compose from its Develop route (build, an existing-codebase roadmap, migrate), keep its fast-tracks, and annotate the plan with a dated one-liner. Never recompose it.

---

## The Skool post

Two accountability loops run through the week: this check-in inside the agent, and **one new post a day in the Skool community**. If the member isn't in the Skool community, skip the post. The skill drafts **title and body**; the member posts it and pastes the link into the Skool post log.

**Titles, house format:**

```
Ship in 7 - Day 0! [app name]
Ship in 7 - Day 3! [what shipped, five words]
Ship in 7 - Day 4! Missed it, here's the fix
Ship in 7 - It's live! 🚀
Ship in 7 completed! Here's what I learnt
```

The `It's live` post goes out the day the smoke test passes, whatever the day number. The `completed` post is the close. One post a day: if the smoke test passes on the same day as the close, combine them into one post titled `Ship in 7 completed! [app name] is live 🚀`.

**Body, in the member's own voice.** Build the voice from what they have actually written: their messages in this session, the Product Offer in `docs/DEFINE.md`, UI copy in the repo, their previous posts in the log. Short, first person, the proof (screenshot or link), the number if there is one, tomorrow's task in one line. No marketing register, no exclamation-mark stacking, no "excited to announce". If you can't hear the member's voice yet, ask for one previous post of theirs.

Missed days are posted too. Zero is an entry.

---

## Failure patterns to name

- **The Research Day.** A session spent reading, comparing stacks, watching tutorials; nothing produced. Every session ends with an artefact.
- **The Scope Creep.** A roadmap item added on Day 3 because it "has to be there for launch". It doesn't. Later phase.
- **The Polish Loop.** Day 6 spent on the landing page hero instead of DNS (or the listing's fourth screenshot instead of the submission). The Live-means bar is the bar; the hero isn't.
- **The Silent Skip.** A missed session that isn't logged. Log it, post it, compress, move on.
- **The Draft-as-Proof.** "I've planned the deploy" is not `docs/DEPLOY.md`. A file, a URL, a screenshot, or it didn't happen.
- **The Platform Optimism.** A migration "nearly done" on Day 5. The verification gate is green or it isn't.
- **The Gate Dodge.** Deploying or publishing before the security audit because "it's just a beta". Secrets, open tables, and over-permissioned tools don't know it's a beta.
- **The Works-On-My-Machine.** An agent product tested only in the member's own setup. The bar is a stranger's clean install, not the author's.

## Must-nots

- Never post to Skool, or anywhere, on the member's behalf.
- Never run paid tools or create accounts without the member; the deploy guide marks those steps 🧑 for a reason.
- Never touch production data.
- Never skip the quality gate or move Go live past Day 7 to "make room".
- Never write a proof artefact yourself to make a day "done". The skills the plan names produce the files; the member produces the screenshots and URLs. If the proof isn't there, the day is a miss.
