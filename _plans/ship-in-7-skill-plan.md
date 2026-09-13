# Plan: `studio-ship-in-7`

*Working plan for a new cross-phase ProductOS skill. Lives in `_plans/` (never shipped, same convention as `_private/`). Sibling plan: `sell-in-30-skill-plan.md`. Delete or move both once the skills ship.*

**Status:** draft for review, reworked from the single 7-day-challenge plan. Decisions already taken in review are marked **(decided)**; everything else carries a recommended default.

---

## 1. What it is

The launch challenge. A member runs it in their app repo and gets a **custom 7-day plan that ends with their app live at a real URL**, with one task, one existing skill, and one piece of proof per day, a daily post in the Skool community, and a close that recommends joining Product Studio and booking a call.

**The bar (decided):** a live URL and a passed smoke test as a real customer. Not a beta user, not payments live. Announcing it (a launch post) is Day 7's stretch, never the bar.

**The promise the plan has to keep:** whatever the member arrives with, Day 7 is the same. The composition changes; the destination doesn't.

### Where members arrive from

The skill reads the repo and shows the member what it found, then **asks which starting point fits (decided: always ask, no recommendation)**:

| Starting point | Evidence in the repo | What the 7 days are mostly spent on |
| --- | --- | --- |
| **Idea only** | No app code beyond `productos/`, Define templates empty | Define fast → spec → build the magic moment only → ship |
| **AI-generated app, not live** | App code, no `docs/DESIGN.md`/`docs/COPY.md`, generated look | Backfill Define → identity, copy, design system → rebuild the core screens → gate → ship |
| **Local prototype** | App code, no deploy config, no `docs/DEPLOY.md`, no production URL | Backfill Define → quality gate → deploy guide → ship → polish |
| **Prompt-to-app platform** (Lovable, Bolt, v0, Base44) | Platform project, no owned repo | Migrate into an owned repo → gate → ship (see Q3) |

### How it fits the system

- **Third cross-phase skill**, next to `studio-setup` (opens every programme) and `studio-launch` (closes every phase); `studio-sell-in-30` is the fourth. For community members with no coached `docs/PLAN.md`, Ship in 7 is the first week of the programme.
- **Runs after `studio-setup` (decided).** Documented order is setup, then the challenge. Day 0 checks the four setup conditions (inside a git repo, root guidelines wired, `productos/` gitignored, plan adopted if shipped) and **runs `studio-setup` first if any is missing**, so "start ship in 7" works as a member's very first command.
- **Writes one new canonical doc: `docs/SHIP-IN-7.md`** (tracked, the member's, same precedent as `docs/LAUNCHES.md`). Everything else is written by the skills it runs.
- **Coached members** with a `docs/PLAN.md`: the challenge composes from the plan's Develop route and annotates the plan, never overrides it.
- **Only one challenge open at a time.** If `docs/SELL-IN-30.md` is open, the skill says so and stops.

---

## 2. The plan composer

The "custom plan" is composed, not picked from a fixed list. The skill carries a **block library**; enrol selects the blocks the evidence says are missing, orders them by dependency, and fits them to 7 days and the member's hours. The four starting points above are the worked examples that ship in the skill, not the only outcomes.

### Block library

| Block | Skill(s) | Produces | Proof | Typical |
| --- | --- | --- | --- | --- |
| Setup check | `studio-setup` | wired root files, gitignore | file diff | 10 min |
| Define from idea | `studio-define-offer-builder` → `studio-define-customer-persona` → `studio-define-pricing` → `studio-define-product` (compressed: one sitting) | `docs/PRODUCT.md` | file exists, 8 sections filled | 3 h |
| Define backfill | `studio-define-from-code` → `studio-define-product` | `docs/PRODUCT.md` | file exists | 1.5 h |
| Words | `studio-design-identity-creator` → `studio-design-ux-writing` | Brand Card, `docs/COPY.md` | files exist | 1.5 h |
| Look | `studio-design-design-system` (one image you love) or `studio-design-design-system-from-code` | `docs/DESIGN.md` + `DESIGN.html` | screenshot of `DESIGN.html` | 1 h |
| Magic moment + spec | `studio-design-magic-moment` → `studio-develop-prd-roadmap` (MVP scoped to the magic moment only) | `docs/PRD.md`, `docs/ROADMAP.md` | roadmap ≤ 1 phase | 1.5 h |
| Build | `studio-develop-mvp-build` (idea) · `studio-develop-design-better` + build loop + `studio-develop-design-review` (rebuild) · `studio-develop-refactor-plan/-build` (messy code) | working core flow | screen recording / before-after | 4 h+ per day |
| Migrate | `studio-develop-migrate` | `docs/MIGRATION.md`, owned repo | verification gate green | 1–2 days |
| Quality gate | `studio-develop-code-review` → `studio-develop-security-audit` → fix Critical/High via build loop | `docs/SECURITY-AUDIT.md` | verdict line, fix plan ticked | 2–3 h |
| Deploy guide | `studio-develop-golive` | `docs/DEPLOY.md` | file exists, accounts created | 1 h |
| **Go live** | work `docs/DEPLOY.md` top to bottom | live URL, HTTPS, domain | **smoke test as a real customer** | 2–3 h |
| Announce *(stretch)* | `studio-launch` | post + `docs/LAUNCHES.md` entry | live post screenshot | 1 h |

### Composition rules

1. **Go live sits on Day 6 with Day 7 as buffer and smoke test**, or Day 7 outright when the member's hours are tight. Never earlier than the quality gate.
2. **Quality gate is never skipped.** Every plan runs the security audit before anything is reachable.
3. **Define backfill is never skipped** when `docs/PRODUCT.md` is missing, because `golive` and the launch post read it. It is compressed, not dropped.
4. **Design blocks are included only when the app exists and looks generated** (the "AI slop" starting point) or when the member asks. On the idea path, the Look block runs on Day 2 so the build is on tokens from the first screen (decided: the rebuild happens in code, not just on paper).
5. **Build days are capped at two.** The MVP is the magic moment and the path to it, nothing else. Roadmap items beyond that are moved to `docs/ROADMAP.md`'s later phases, not built.
6. **Hours/day (Q2)** scale the plan: `1h` compresses Define to the fast-track only and drops Words; `4h+` may bring Announce inside the week.

### Worked examples (ship in the skill as `plans/`)

**Idea only** · D1 Define from idea · D2 Look + Magic moment + spec · D3–D4 Build · D5 Quality gate · D6 Deploy guide + Go live · D7 Smoke test, buffer, Announce.

**AI-generated app** · D1 Define backfill · D2 Words + Look · D3–D4 Build (rebuild the core screens) · D5 Quality gate · D6 Deploy guide + Go live · D7 Smoke test, buffer, Announce.

**Local prototype** · D1 Define backfill · D2 Quality gate · D3 Fixes · D4 Deploy guide · D5 Go live · D6 Domain, polish, `design-review` · D7 Smoke test, Announce.

**Prompt-to-app platform** · D1–D3 Migrate · D4 Quality gate · D5 Deploy guide · D6 Go live · D7 Smoke test, Announce. Flagged as the most ambitious path at enrol (Q3).

---

## 3. Skill design

### Files

```
skills/studio-ship-in-7/
  SKILL.md                three modes: enrol / daily check-in / close; the block library;
                          composition rules; Skool post format; failure patterns
  plans/idea-only.md
  plans/ai-generated-app.md   worked examples the composer starts from
  plans/local-prototype.md
  plans/platform-migration.md
  SHIP-IN-7-TEMPLATE.md   the docs/SHIP-IN-7.md skeleton the skill fills
```

Self-contained, like every other skill folder. The daily-loop mechanics are the same as in `studio-sell-in-30`; they are written once and kept identical in both SKILL.md files (Q10 asks whether to factor them out).

### Frontmatter

- `name`: `studio-ship-in-7` **(decided: `studio-` prefix)**.
- `description` ≤ 1024 characters and bytes. Triggers: "ship in 7", "ship in seven", "launch my app in 7 days", "7 day launch challenge", "start the challenge", "day 3 check-in", "what's my task today", "I missed a day", "I just installed ProductOS, what do I do".

### Mode 1 — Enrol (Day 0, ~20 min)

1. **Setup check.** Run `studio-setup` if any of its four conditions fail **(decided)**.
2. **Read the repo** and show the evidence in one short block: what exists (code, docs, deploy config, live URL), what's missing.
3. **Ask the starting point (decided: always ask).** Present the starting points that fit the evidence, plus "none of these". No recommendation.
4. **Confirm the plan's inputs:** start date (default tomorrow, so Day 1 is a full day) and honest hours per day (`1h` / `2h` / `4h+`).
5. **Compose the 7 days** from the block library and show the plan as a table: day, block, skill, proof, hours. The member edits before it's written.
6. **Write `docs/SHIP-IN-7.md`:** header (start/end dates, hours, the bar verbatim, starting point), the plan table, an empty daily log, the Skool post log.
7. **Draft the Day-0 Skool post** and end by naming Day 1's literal first action.

### Mode 2 — Daily check-in (Days 1–7)

Triggered by the member ("day 3", "check-in", "what's today"), and by every new session in the repo once the setup templates carry the line *"if `docs/SHIP-IN-7.md` or `docs/SELL-IN-30.md` is open, run its daily check-in first"*.

1. Work out the day **from the start date**, not from how many entries exist, so missed days stay visible.
2. **Confirm yesterday's proof first.** "Did it ship? Show me." A screenshot, a file that now exists, a URL. A draft is not proof (same rule as `studio-launch`).
3. Log yesterday: done / partial / missed, proof, one-line blocker.
4. **Missed a day?** Apply the compression rules: drop the stretch, merge the two build days into one scoped tighter, never move Go live past Day 7. Two consecutive misses → shrink the scope of the MVP, not the bar.
5. Name today's **one** block, the skill, the proof. Run it now or hand off ("run `studio-develop-golive`, come back when `docs/DEPLOY.md` exists").
6. **Draft today's Skool post** (see §4).
7. End by stating exactly what returning tomorrow looks like.

### Mode 3 — Close (Day 7 or 8)

1. **Check the bar honestly:** is the URL live, did the smoke test pass as a real customer? Hit, partly hit, or missed. A miss is logged and read, never reframed.
2. **Write the Ship Report** into `docs/SHIP-IN-7.md`: result vs bar, what shipped each day, what was cut to make the week, the biggest blocker, what the app can and can't do today. *Written so the member can bring it to a Product Studio call as-is*: it is the intake material a coach composes a custom plan from.
3. **Draft the graduation Skool post** (title format in §4; body in the member's voice; a link to the live app).
4. **The recommendation (decided):** join Product Studio and book a call. Framed by outcome, one paragraph, once, with the link (Q6). Hit the bar → "you've launched; a custom plan takes this to revenue." Missed → "this is exactly where a coach changes the outcome." Then name what to run meanwhile: `studio-sell-in-30` (Q5) or the Distribute checklist.

### Voice

The `studio-launch` register: coach at the moment of fear, bar visibly low, shipping is the achievement, silence is an entry, never shame a zero. Blunt about proof.

### Failure patterns (named in SKILL.md)

The Research Day (a day spent reading, nothing produced) · The Scope Creep (a roadmap item added on Day 3) · The Polish Loop (Day 6 spent on the landing page instead of DNS) · The Silent Skip (a missed day not logged) · The Draft-as-Proof · The Platform Optimism (a migration "nearly done" on Day 5).

---

## 4. Daily accountability

Two loops, because a plugin skill cannot message anyone on its own:

1. **Inside the agent (pull).** The daily check-in, reached by any of its triggers and by the setup-template line that makes every session in the repo start there.
2. **In the Skool community (push, social) (decided).** One **new post** a day, not a comment on a pinned thread. The skill drafts **title and body**; the member posts it and pastes the link into the log.
   - **Title, house format (Q7 to approve):** `Ship in 7 · Day 3/7 — [what shipped, five words]`. Day 0: `Ship in 7 · Day 0/7 — Starting: [app name]`. Day 7: `Ship in 7 · Shipped — [app name] is live`.
   - **Body, free-drafted in the member's own voice (decided).** The skill builds the voice from what the member has actually written: their messages in the session, the Product Offer and Mini-Launch drafts, UI copy in the repo, previous posts in the log. Short, first person, the proof (screenshot or link), the number if there is one, tomorrow's task in one line. No marketing register.
   - Missed days are posted too: `Ship in 7 · Day 4/7 — Missed it, here's the fix`. Zero is an entry.

No push reminders in v1 (Q8 default): the Skool feed carries the rhythm.

---

## 5. System changes (beyond the skill folder)

Shared with `studio-sell-in-30`; listed once here.

| File | Change |
| --- | --- |
| `README.md` | Skill count 38 → 40; "Getting started" gains the two challenges as the community entry points; cross-phase skills are now four. |
| `START-HERE.md` | "Starting completely from scratch?" → run `studio-setup`, then `studio-ship-in-7`. |
| `AGENTS.md` | Four cross-phase skills; dependency rule for `docs/SHIP-IN-7.md` / `docs/SELL-IN-30.md`; "only one challenge open at a time". |
| `setup/CLAUDE.md`, `setup/AGENTS.md` | `SHIP-IN-7.md`, `SELL-IN-30.md` in the canonical docs list; the "if a challenge is open, check in first" line inside the PRODUCTOS block. |
| `skills/studio-setup/SKILL.md` | Step 5, no plan → "Run `studio-ship-in-7` (not live yet) or `studio-sell-in-30` (live, no customer)" before the linear checklist. |
| `skills/studio-launch/SKILL.md` | Inputs read the open challenge file when present; the challenge day is the send deadline. |
| `skills/studio-develop-golive/SKILL.md` | One line: when `docs/SHIP-IN-7.md` is open, the guide's estimated time must fit the remaining days; say so if it can't. |
| Four `*-CHECKLIST.md` | One preamble line pointing challenge members at their open challenge file. |
| Five plugin manifests | Version 1.10.0; "38 skills" → "40 skills"; codex `defaultPrompt` gains "Start ship in 7". |
| `CHANGELOG.md` | 1.10.0 entry in the house style, covering both skills. |

---

## 6. Build sequence

1. Lock the answers to §7 (and the sibling plan's questions).
2. Write the block library and the four worked-example plans. They are the product.
3. Write `SHIP-IN-7-TEMPLATE.md`.
4. Write `SKILL.md`: the three modes, the composer, the Skool post format, failure patterns, "what done looks like".
5. Wire the system (§5), once, for both skills.
6. Validate: description length; the plugin loads in Claude Code, Codex, Cursor; the names pass each validator.
7. Dry-run all four starting points against fixture repos: an empty `git init`; a generated Next.js app with no design docs; a local app with no deploy config; a Lovable export. Walk Day 0, Day 1, a missed day, Day 7 in each.
8. Ship with `studio-sell-in-30` in 1.10.0.

Effort: two focused sessions for the skill and plans, one shared session for wiring and validation, one for the dry-runs.

---

## 7. Open questions

Already decided in review, carried forward: `studio-` prefix · setup runs first if missing · bar is live URL + smoke test · always ask the starting point · Skool: new post per day, house-format title, body in the member's voice · Product Studio + book a call at the close.

1. **Idea-only members.** In scope, with the MVP scoped to the magic moment only (default), or require existing code and send idea-stage members to the Define checklist first?
2. **Hours per day.** Offer the `1h` compressed plan (default) or state that Ship in 7 needs 2h+ and refuse to compose below it? An idea-only member at 1h/day cannot ship in 7; the honest move is to say so at enrol.
3. **Prompt-to-app platform arrivals.** In scope with the migration as Days 1–3 (default, flagged as ambitious), or out of scope ("run `studio-develop-migrate` first, then come back")?
4. **Announce.** Stretch only (default), or make a launch post part of the bar so the community sees every ship?
5. **Chain to Sell in 30.** Does the close name `studio-sell-in-30` as "what to run meanwhile" next to the Product Studio recommendation (default), or keep the close to Product Studio only?
6. **The Product Studio CTA.** The link (`go.buildgreatproducts.com`, as in the README, or a booking page?), the exact pitch line, and whether it appears in the graduation Skool post as well as in the closing message and the Ship Report (default: closing message and report; the post links the live app, not the programme).
7. **Skool title format.** Approve `Ship in 7 · Day N/7 — [what shipped]`, or give me the pattern you want.
8. **Reminders.** Skool feed only (default), or also a scheduled prompt where the tool supports it?
9. **Missed days.** Compress, never extend (default), or allow one pause day?
10. **Shared mechanics.** Keep the daily-loop text duplicated in both SKILL.md files (default: self-contained skills, house style), or factor it into a third, member-invisible reference file both skills read?
11. **Existing material.** Do you have a Ship in 7 doc, Skool post, or video script whose structure or language I should mirror? Drop it in `_private/`.
12. **Must-nots.** Anything the challenge must never do (never post on the member's behalf, never run paid tools, never touch production data)?

---

## 8. Risks

1. **Seven days is a real constraint for the idea path.** A magic-moment-only MVP is feasible with a coding agent at 2h+/day; at 1h/day it isn't. Mitigation: enrol says so and composes honestly (Q2).
2. **Quality gate vs. time.** A security audit on Day 5 can surface Critical findings that eat Day 6. Mitigation: the gate runs before deploy on every path, and the compression rules cut scope, never the gate.
3. **Detection false positives.** "Looks generated" is a judgement. Mitigation: the member picks the starting point (decided), the evidence is shown, the dry-runs test the read.
4. **Two skills, one loop.** Duplicated mechanics drift. Mitigation: Q10, and a CHANGELOG rule that a change to one loop is a change to both.
5. **Scope creep into a fifth phase.** If a day's instructions exceed "run X, produce Y, post Z", the content belongs in the skill being run, not here.
