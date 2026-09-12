# Plan: the `7-day-challenge` skill

*Working plan for a new cross-phase ProductOS skill. Lives in `_plans/` (never shipped — same convention as `_private/`). Delete or move once the skill ships.*

**Status:** draft for review. Every open decision below carries a recommended default so the answer can be "defaults, except …".

---

## 1. What it is

The first thing a community member runs after installing ProductOS. It reads the repo, works out which of four situations the member is in, and enrols them in a 7-day challenge with **one task, one existing skill, and one piece of proof per day**, ending in a concrete, public win:

| Track | Who it's for | The win on Day 7 |
| --- | --- | --- |
| **A — Idea → Offer → Validated** | No product yet (idea, or not even that) | Offer + persona + price written, Mini-Launch shipped, ≥1 real reply logged, `docs/PRODUCT.md` exists |
| **B — AI slop → Professional design** | An app exists but looks generated | Identity + `docs/COPY.md` + `docs/DESIGN.md` exist, the core screens rebuilt on the tokens, before/after posted, relaunch #2 shipped |
| **C — Prototype/local → Launched** | It runs on their machine, nobody can reach it | Security audit passed, `docs/DEPLOY.md` done, live URL, beta invite shipped, ≥1 real person used it |
| **D — First real customer** | Live product, nobody has paid | Price live at checkout, public launch shipped, ≥1 payment (or the honest pivot read) |

It is an **orchestrator**: every day names the existing skill to run (`studio-define-offer-builder`, `studio-launch`, `studio-develop-golive`, …). It owns the sequencing, the daily accountability loop, and the log — nothing else. That keeps it small and means it never drifts from the checklists.

### How it fits the system

- **Third cross-phase skill**, alongside `studio-setup` (opens every programme) and `studio-launch` (closes every phase). The challenge is *the first week of* the programme for public-copy members who have no coached `docs/PLAN.md`.
- **Runs setup inline.** `studio-setup` is idempotent and takes seconds, so Day 0 verifies it rather than sending the member elsewhere first. `studio-setup`'s closing step gains a branch: no plan in the copy → "start the 7-day challenge".
- **Writes one new canonical doc: `docs/CHALLENGE.md`** (tracked, the member's, same precedent as `docs/LAUNCHES.md`). Launch days write to `docs/LAUNCHES.md` through `studio-launch` as they already do.
- **Coached members** (a `docs/PLAN.md` exists): the challenge picks the track that matches the plan's first phase and annotates, never overrides, the plan.

---

## 2. Skill design

### Files

```
skills/studio-7-day-challenge/
  SKILL.md                     frontmatter + the three modes (enrol / daily check-in / close)
  tracks/A-idea-to-validated.md
  tracks/B-slop-to-design.md   one file per track: day-by-day plan, proof per day,
  tracks/C-local-to-launched.md compression rules for missed days, the Day-7 pass bar
  tracks/D-first-customer.md
  CHALLENGE-TEMPLATE.md        the docs/CHALLENGE.md skeleton the skill fills
```

Bundled reference files inside the skill folder is the existing pattern ("each contains a SKILL.md plus any bundled reference files"). No new phase folder, no new numbered template.

### Frontmatter

- `name`: `studio-7-day-challenge` (see Q1 — the user asked for `7-day-challenge`; both spellings become trigger phrases either way).
- `description`: ≤ 1024 characters **and** bytes (the 1.7.1 lesson). Triggers: "7 day challenge", "seven day challenge", "start the challenge", "day 3 check-in", "daily check-in", "what's my task today", "I just installed ProductOS, what do I do", "where am I in the challenge", "I missed a day".

### Mode 1 — Enrol (Day 0, ~20 min)

1. **Verify the install** — the four `studio-setup` checks (inside a git repo, root `CLAUDE.md`/`AGENTS.md` wired, `productos/` gitignored, plan adopted if shipped). Fix what's missing; don't send the member away.
2. **Detect the stage** from evidence, not questions:

   | Signal | Read as |
   | --- | --- |
   | No app code beyond `productos/`, Define templates empty | Track A |
   | App code present, no `docs/DESIGN.md` / `docs/COPY.md`, UI reads as generated (default Tailwind/shadcn look, inconsistent spacing, marketing-voice copy) | Track B candidate |
   | App code present, no deploy config, no `docs/DEPLOY.md`, no production URL | Track C candidate |
   | Live URL reachable **or** `docs/DEPLOY.md` complete; `docs/LAUNCHES.md` rung below `payment` (or no launches at all) | Track D candidate |

   Precedence when several apply (e.g. a live app that also looks generated): **recommend the track whose win is closest to money** (D > C > B), state the reasoning in one paragraph, and let the member override. The member's answer wins; the recommendation is logged.
3. **Confirm the three things that decide the plan**: the track, the start date (default: tomorrow, so Day 1 is a full day), and how many hours per day they honestly have (`1h` / `2h` / `4h+` — the track files carry a compressed plan for `1h`).
4. **Write `docs/CHALLENGE.md`**: header (track, start/end dates, hours/day, the win bar verbatim), the 7-day plan table (day · task · skill · proof), an empty daily log, and the believers/witness line (where the daily proof gets posted — see §3).
5. **Draft the Day-0 community post** ("I'm starting the 7-day challenge, track X, my win is Y") and end by naming Day 1's literal task.

### Mode 2 — Daily check-in (Days 1–7, ~5 min of overhead)

Triggered by the member ("day 3", "check-in", "what's today"). The skill:

1. Reads `docs/CHALLENGE.md`, works out which day it is from the start date (not from how many entries exist — so missed days are visible).
2. **Confirms yesterday's proof first** — "Did it ship? Show me." A screenshot, a file that now exists, a URL, a log entry. Draft ≠ proof (same rule as `studio-launch`).
3. Logs yesterday: done / partial / missed, proof link, one-line blocker.
4. **Missed a day?** Applies the track's compression rule (drop the optional item, merge two build days, never push the ship day past Day 5) — the challenge stays 7 calendar days; it does not extend. Two consecutive missed days → shrink the win bar, don't quit (mirrors "never shame a zero").
5. Names today's **one** task, the skill to run, and the proof it produces. Then either runs that skill in the same session or hands off ("run `studio-design-design-system` now, come back when `docs/DESIGN.html` renders").
6. Drafts today's proof post for the community (≤ 5 lines, the artefact, the number, tomorrow's task).
7. Ends by stating exactly what returning tomorrow looks like.

### Mode 3 — Close (Day 7 or Day 8)

1. Checks the win bar honestly against the log — hit, partially hit, missed. A miss is logged and read, never reframed.
2. Writes the **Challenge Report** section into `docs/CHALLENGE.md`: result vs bar, what shipped each day, believers gained, the one thing that blocked most.
3. Drafts the graduation post.
4. **Routes what's next**: the exact checklist step or skill that follows this track (A → Design checklist; B → Develop step 5 build loop; C → Distribute checklist; D → growth experiments or `BONUS-Pivot-Framework.md` if the rung was missed twice). Optionally names Product Studio for members who want a custom plan (Q14).

### Voice

Same coach-at-the-moment-of-fear register as `studio-launch`: low visible bar, shipping is the achievement, silence is an entry, never shame a zero. Blunt about proof.

---

## 3. Daily accountability — the mechanics

A plugin skill cannot message anyone on its own, so accountability is two loops that reinforce each other:

1. **Inside the agent (pull):** the daily check-in above. Every session in the repo starts from `docs/CHALLENGE.md` because the wired root guidelines say so — one line added to the PRODUCTOS block in `setup/CLAUDE.md` / `setup/AGENTS.md`: *"If `docs/CHALLENGE.md` exists and is not closed, start by running the daily check-in."* This is what makes "I opened Claude Code" turn into "what day am I on" without the member remembering the skill name.
2. **In the community (push, social):** one proof post per day in a named place (Q8), drafted by the skill, posted by the member. The post is the witness — the same "cohort sees shipped things only" rule the launches use. Track files carry a `#day3/7` line format so posts are scannable in a feed.

Optional third loop, decided in Q9: a real reminder (Claude Code Routines / a `send_later`-style scheduled prompt where the member's tool supports it, or a community-side daily "post your Day N proof" thread). Recommended to leave out of v1 and let the community thread carry it.

---

## 4. Draft day plans (to be refined by your answers)

Each day: **task → skill → proof**. Times assume the `2h` plan.

**Track A — Idea → Offer → Validated**
- D1 Offer. `studio-define-leverage-finder` (no idea) or `studio-define-offer-builder` → `1-Product-Offer.md` filled.
- D2 Persona + critique. `studio-define-customer-persona`, then `studio-define-offer-review` → both files sharpened.
- D3 Price. `studio-define-pricing` → the price line. Commit a send time for D4.
- D4 **Ship.** `studio-launch` sitting one → screenshot of the live post / sent DMs.
- D5 Follow up. Reply to everyone; send the second-warmest route if silent → log entries.
- D6 Read the signal. `studio-launch` sitting two → `docs/LAUNCHES.md` with believers.
- D7 Synthesise. `studio-define-product` → `docs/PRODUCT.md`. Close. **Bar: ≥1 real reply** (stretch: a conversation).

**Track B — AI slop → Professional design**
- D1 Backfill strategy. `studio-define-from-code` + `studio-define-product` → `docs/PRODUCT.md` (skip if present).
- D2 Words. `studio-design-identity-creator` + `studio-design-ux-writing` → Brand Card, `docs/COPY.md` (with the audit fix list).
- D3 Look. Find one image you love; `studio-design-design-system` → `docs/DESIGN.md` + `DESIGN.html` screenshot.
- D4 First screen. `studio-develop-design-better` + build loop on the highest-traffic screen; `studio-develop-design-review` before commit → before/after.
- D5 Core flow. Same, onboarding-to-magic-moment screens → before/after.
- D6 Remaining screens + copy fixes from D2's list → before/after; whole-app `studio-develop-design-review`.
- D7 Show it. `studio-launch` (#2 "here's what it looks like") → live post. Close. **Bar: before/after posted publicly; stretch: one "can I try it?".**

**Track C — Prototype/local → Launched**
- D1 Backfill + baseline. `studio-define-from-code` + `studio-define-product` if missing; `studio-develop-code-review` on the working tree → known state.
- D2 Security. `studio-develop-security-audit` → `docs/SECURITY-AUDIT.md`; do the "right now" items.
- D3 Fix plan. Build loop over the audit's Fix plan → Critical/High closed.
- D4 Deploy guide. `studio-develop-golive` → `docs/DEPLOY.md`; accounts created.
- D5 **Go live.** Work `DEPLOY.md` top to bottom → live URL + smoke test as a real customer.
- D6 Invite. `studio-launch` (#3 beta invite) → sent messages.
- D7 One user. Log activations. Close. **Bar: live URL + ≥1 real person reached the magic moment.**

**Track D — First real customer**
- D1 Backfill + price. `studio-define-from-code` + `studio-define-product` if missing; `studio-define-pricing` → a price said out loud.
- D2 Checkout. Payments live, real test purchase; `studio-develop-cro-audit` on pricing/checkout → fixes list.
- D3 Channel. `studio-distribute-gtm-strategy` → one primary channel, its "Do this" list.
- D4 **Launch.** `studio-launch` (#4) → believers first, then the channel; 10 named DMs.
- D5 Ten more conversations. Founding-customer offer → log.
- D6 Close the leaners. Follow-ups, objections, the checkout link → log.
- D7 Read it. Payment or the honest read (`BONUS-Pivot-Framework.md` if the rung was missed twice). Close. **Bar: ≥1 payment.**

---

## 5. System changes (beyond the skill folder)

| File | Change |
| --- | --- |
| `README.md` | Skill count 38 → 39; "Getting started" step 1 gains the challenge as the community entry point; table of cross-phase skills. |
| `START-HERE.md` | "Starting completely from scratch?" → "Start the 7-day challenge". |
| `AGENTS.md` | Cross-phase skills sentence: three, not two; dependency-chain rule for `docs/CHALLENGE.md`. |
| `setup/CLAUDE.md`, `setup/AGENTS.md` | `CHALLENGE.md` in the canonical docs list; the "if a challenge is open, check in first" line inside the PRODUCTOS block. |
| `skills/studio-setup/SKILL.md` | Step 5: no plan → offer the challenge (before falling back to the linear checklist). |
| `skills/studio-launch/SKILL.md` | Inputs: read `docs/CHALLENGE.md` when present (the challenge day is the send deadline). |
| Four `*-CHECKLIST.md` | One preamble line: "Doing the 7-day challenge? `docs/CHALLENGE.md` says which steps are this week's." |
| `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`, `.cursor-plugin/plugin.json`, both `marketplace.json` | Version 1.10.0; "38 skills" → "39 skills"; codex `defaultPrompt` gains "Start the 7-day challenge". |
| `CHANGELOG.md` | 1.10.0 entry in the house style. |

---

## 6. Build sequence

1. **Lock the answers** to §7 (this review).
2. **Write the four track files first** — they are the product; SKILL.md is the harness around them. Each ends with a falsifiable Day-7 bar.
3. **Write `CHALLENGE-TEMPLATE.md`** — header, plan table, daily log (date · day N · task · proof · done/partial/missed · blocker), Challenge Report.
4. **Write `SKILL.md`** — the three modes, the detection table, the compression rules, failure patterns (The Research Day, The Polish Loop, The Silent Skip, The Track Hop), "what done looks like".
5. **Wire the system** (§5).
6. **Validate:** description under 1024 chars/bytes; plugin manifests load in Claude Code (`claude plugin install ./productos`), Codex, and Cursor; the skill name passes each tool's validator (see Risk 1).
7. **Dry-run each track** against four fixture repos: an empty `git init` repo; a generated Next.js app with no design docs; a local app with no deploy config; a live app with Stripe in test mode. Walk Day 0 → Day 1 → a missed day → Day 7 in each. Fix what the detection gets wrong.
8. **Ship:** bump to 1.10.0, CHANGELOG, tag.

Estimated effort: two focused sessions for the skill + track files, one for wiring and validation, one for the four dry-runs.

---

## 7. Open questions

Answer any subset; unanswered ones take the default.

**Naming and placement**
1. **Skill name.** `studio-7-day-challenge` (default — matches the `studio-setup` / `studio-launch` cross-phase convention, and avoids a name that starts with a digit, which some plugin validators may reject) or `7-day-challenge` exactly as you wrote it? "7 day challenge" is a trigger phrase either way.
2. **Should it replace `studio-setup` as the documented first step** for public copies, or run after it? Default: the challenge runs setup's checks inline and becomes the documented first step; `studio-setup` stays for coached copies and re-runs.

**Tracks and win bars**
3. **Track A's "validated".** Is the bar one real reply (the existing Mini-Launch bar, default), one real conversation, or a signup/pre-order? A higher bar in 7 days changes Day 3–6 substantially.
4. **Track B's scope.** Produce the design system *and* rebuild the core screens in code (default), or stop at the design system + prompts and leave the rebuild to the Develop phase?
5. **Track C's "launched".** Live URL + smoke test (minimum), plus one real beta user (default), or also payments live?
6. **Track D's "customer".** A paying customer (default). For free products, does an activated user count?
7. **Track precedence.** When several tracks fit, recommend the one closest to money (default) or always ask? And should the member be allowed to pick a track the evidence says they aren't ready for (e.g. D with no live app)? Default: allow, with a logged warning.

**Accountability**
8. **Where does the daily proof post go?** Your community platform (Skool?), a specific space or a single pinned "Challenge" thread, a hashtag / `#day3/7` format? Do you want the skill to draft the post in a fixed house format?
9. **Real reminders.** Community-thread only (default), or also a scheduled prompt where the tool supports it (Claude Code Routines), or email? Push reminders are outside what a skill can guarantee across Claude Code / Codex / Cursor.
10. **Calendar days or working days?** Default: 7 consecutive calendar days, chosen start date, missed days compress the plan rather than extend it. Or would you rather allow one "pause" day?
11. **Cohorts or rolling starts?** If everyone starts on a Monday, Day 4 (the ship day) lands on Thursday for the whole group and the community thread gets a rhythm. Rolling is the default because the skill can't know the cohort calendar.
12. **Hours per day.** Should the skill offer a `1h` compressed plan (default: yes, in every track file), or assume `2h+` and say so?

**Closing and the funnel**
13. **What happens on a miss?** Default: honest report, shrink the bar, route to the next checklist step. Should there be a "run it again" option that restarts the same track with a warmer channel?
14. **Product Studio upsell at Day 7.** The README already carries the banner. Default: one line in the Challenge Report ("want a custom plan? Product Studio"). Or leave the funnel to the community and keep the skill neutral?
15. **Should the challenge write `docs/PLAN.md`** for public-copy members (so the rest of ProductOS treats it as their programme), or only `docs/CHALLENGE.md` (default — PLAN.md stays coach-authored)?

**Content and voice**
16. Do you have an existing 7-day challenge (a doc, a Skool post, a video script) whose day structure or language I should mirror? Drop it in `_private/` and I'll read it.
17. Anything the challenge must **not** do — e.g. never touch app code in Track A, never run paid tools, never post on the member's behalf?

---

## 8. Risks

1. **Leading-digit skill name.** `7-day-challenge` may fail a plugin validator the way `claude-code-build-loop` did in 1.7.1. Mitigated by Q1's default; verify in all three tools before ship regardless.
2. **Time realism for B and C.** A large or messy codebase does not become professional or live in 7 days. Mitigation: the compression rules scope B to "the core flow" and C to "reachable + one user", and Day 0 says so out loud.
3. **Detection false positives.** "Looks generated" is a judgement. Mitigation: the recommendation is always confirmed with the member and logged; the four fixture dry-runs are the test.
4. **The 48-hour ship rule vs. the day plan.** Track A's Day 4 must not slip. Compression rules never push the ship day past Day 5.
5. **Scope creep into a fifth phase.** The skill must stay an orchestrator. Rule: if a day's instructions exceed "run X, produce Y, post Z", the content belongs in the skill being run, not here.
