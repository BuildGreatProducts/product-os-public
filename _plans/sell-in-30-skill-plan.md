# Plan: `studio-sell-in-30`

*Working plan for a new cross-phase ProductOS skill. Lives in `_plans/` (never shipped). Sibling plan: `ship-in-7-skill-plan.md`. The system wiring, build sequence and shared daily-loop mechanics are specified there and referenced here.*

**Status:** reviewed and final. Every question is answered. The daily activity model (Q3) is settled: weeks 2–4 run the member's own growth experiments, chosen by the GTM strategy and growth experiments skills, one experiment a week with a continue/kill read at the end. Ready to build alongside Ship in 7.

---

## 1. What it is

The first-customer challenge. A member with a **live product and no paying customer** runs it in their app repo and gets a **custom 30-day plan that ends with their first payment**, one task a day, a daily in-agent check-in, a weekly Skool post at each signal read, and a close that recommends joining Product Studio and booking a call. It is the natural next step after `studio-ship-in-7` and the strongest lead-in to the coaching programme: thirty days of logged market contact is exactly the material a coach composes a custom plan from.

**The bar (decided):** one payment. Not a signup, not a friend's "I'd pay for that". **Free products are allowed (decided):** at enrol the skill asks whether the product will charge within the 30 days. Yes → the bar is a payment and pricing plus checkout go in week one. No → the bar is **one activated user**, a real person reaching the magic moment, and the price and checkout blocks drop out of the plan.

**Prerequisite (decided):** the product is reachable by customers, **or can be within the first few days**. A member one deploy away enrols with Go live as the opening blocks (the Deploy guide and Go live blocks from Ship in 7, reused). Anyone further from live is routed to `studio-ship-in-7` first.

### Where members arrive from

The skill reads the repo and `docs/LAUNCHES.md`, shows what it found, and **asks (decided: always ask)** which fits:

| Starting point | Evidence | What the 30 days are mostly spent on |
| --- | --- | --- |
| **Not yet live, one deploy away** | App code, deploy config or `docs/DEPLOY.md` in progress, no production URL | Go live in the first few days, then the standard four weeks |
| **Live, free, will charge** | Live URL, no price on the site, no payments integration | Price it, wire checkout, warm asks, then the experiment loop |
| **Live, free, staying free for now** | As above; the member says no charge in the next 30 days | Bar becomes one activated user; experiments lean on activation |
| **Live, priced, nobody has paid** | Price on the site or Stripe in place, `docs/LAUNCHES.md` rung below `payment` | Verify checkout, warm asks, then the experiment loop |
| **Live with users, no revenue** | Signups or activity, no payment | Warm asks to existing users first; a founding offer is the obvious experiment 1 |
| **Just shipped via Ship in 7** | `docs/SHIP-IN-7.md` closed this week | Announce, then the standard four weeks |

### How it fits the system

- **Fourth cross-phase skill.** Runs after `studio-setup` **(decided)**; Day 0 checks the setup conditions and runs `studio-setup` first if any fail.
- **Composes from the Distribute checklist and the launch ritual.** Week one is the warm half of launch #4 plus the GTM strategy and growth experiments steps; weeks 2–4 are the Distribute checklist's experiment cycle (run, log, decide) compressed to one experiment a week. Nothing new is taught; the challenge owns sequencing, the daily loop, and the log.
- **Writes `docs/SELL-IN-30.md`** (tracked, the member's). Launch entries and believers go to `docs/LAUNCHES.md` through `studio-launch`, as they already do.
- **Backfills what's missing first.** No `docs/PRODUCT.md` → `studio-define-from-code` + `studio-define-product` on Day 1 (hours, not days). No `docs/LAUNCHES.md` → create it and backfill everyone who has ever responded onto the believers list, the same move `studio-launch` makes for coached members.
- **Only one challenge open at a time.** If `docs/SHIP-IN-7.md` is open, close it first.

---

## 2. The plan composer

Same mechanism as Ship in 7: a **block library**, composed into **four 7-session weeks**, fitted to the starting point and the member's hours. The shape is fixed; only week one changes with the starting point.

### The shape of the 30 days (decided)

| Week | What it is | Ends with |
| --- | --- | --- |
| **1 · Foundations** | Backfill, deploy if needed, checkout live with a real test purchase, conversations with the warm network, then `studio-distribute-gtm-strategy` and `studio-distribute-growth-experiments` | Weekly read + Skool post |
| **2 · Experiment 1** | The highest-leverage experiment from the member's own backlog, run to its pass bar | Read: **continue or kill** + Skool post |
| **3 · Continue or next** | Continue experiment 1 (iterate or double down) or start the next from the queue | Read: continue or kill + Skool post |
| **4 · Continue or next** | Same | Read: continue or kill + Skool post |
| **End** | Sell Report, graduation Skool post, Product Studio call booking | |

**Where the daily work comes from (decided, replaces the quota):** nothing in weeks 2–4 is a fixed block. `productos/distribute/2-Growth-Experiments.md` (written by the growth experiments skill in week one) names 1–3 experiments **running now**, each with a plain sentence, a "Do this" checklist, and a **Pass =** line stating the next move on pass and on fail, plus an ordered **up next** queue. The challenge takes the top experiment, spreads its "Do this" steps across sessions 1–5 of the week, uses session 6 for follow-ups, and reads it against its Pass = line on session 7. The result and decision go into `3-Growth-Experiments-Tracker.md` the way the Distribute checklist already says they should. Some experiments are outreach, some are content, listings, a founding offer, a conversion fix, a partnership; the mix is the member's, not the skill's. Cold outreach happens only when an experiment calls for it, and is logged as cold **(resolves the deferred Q8)**.

**Two things the challenge tells the Distribute skills when it runs them:** the bar (first payment, or first activated user for a product staying free) and the clock (three experiment-weeks). The growth experiments skill ranks the backlog by *closest to that bar inside a week* and sizes each experiment to one week with a pass bar a member can actually read on day seven. Anything bigger goes to the up-next queue as two smaller experiments.

### The weekly shape (the same every week)

- **Sessions 1–5:** one block a session. In week one the blocks come from the library below; in weeks 2–4 they are the running experiment's "Do this" steps.
- **Session 6:** follow-ups only. Every open thread gets a reply; the checkout link goes to anyone who leaned in.
- **Session 7: the weekly read.** `studio-launch` sitting two applied to the week (every response logged including silence, warm/cold, rung reached, believers added), plus in weeks 2–4 the experiment's result against its Pass = line and the decision: **continue** (double down or iterate) or **kill** (next experiment from the queue starts next week). Logged in the tracker and in `docs/SELL-IN-30.md`. **The read is the weekly Skool post.**

### Block library (week one)

| Block | Skill(s) / action | Produces | Proof |
| --- | --- | --- | --- |
| Setup check | `studio-setup` | wired repo | file diff |
| Go live *(when not yet live)* | `studio-develop-golive`, then work `docs/DEPLOY.md` | live URL | smoke test as a real customer |
| Define backfill | `studio-define-from-code` → `studio-define-product` | `docs/PRODUCT.md` | file exists |
| Price it *(will charge, no price yet)* | `studio-define-pricing` | one launch price, the price line | price said out loud in the log |
| Checkout live *(will charge)* | payments switched to live via the payments section of `studio-develop-golive`, a **real test purchase** | a working checkout link | test-purchase receipt |
| Believers backfill | create `docs/LAUNCHES.md`; everyone who ever responded, with source and status | the believers list | file exists |
| Warm conversations | `studio-launch` sitting one, scoped to the warm network: believers first, then named people who match the persona, checkout link in hand | messages sent | sent-folder screenshot |
| Channel | `studio-distribute-gtm-strategy` | `1-Go-To-Market-Strategy.md`: the primary channel and its "Do this" list | file exists |
| Experiments | `studio-distribute-growth-experiments`, briefed with the bar and the clock | `2-Growth-Experiments.md` (running now + up next), tracker seeded | experiment 1 named, pass bar written |
| Weekly read | `studio-launch` sitting two, applied to the week | `docs/LAUNCHES.md`, tracker updated | the read, posted |

### Block library (weeks two to four)

| Block | Source | Proof |
| --- | --- | --- |
| Run the experiment | the running experiment's "Do this" steps, one or two a session | the step's own artefact (a post, a listing, a message batch, a shipped fix) |
| Follow-ups | every open thread | replies sent |
| Read: continue or kill | result vs the Pass = line; tracker decision | tracker row + Skool post |
| Next experiment *(after a kill)* | top of the up-next queue; re-run `studio-distribute-growth-experiments` if the queue is empty | experiment named, pass bar written |

### Composition rules

1. **Checkout works before anyone is asked for money.** A real test purchase is the proof, by session 3 of week one at the latest. For a product staying free this block drops out.
2. **Warm conversations before the strategy.** The believers and the warm network get the first ask in week one, checkout link in hand, before a channel is chosen. It needs no strategy and it's the most likely source of the first payment.
3. **Strategy and experiments close week one.** GTM strategy and growth experiments run on sessions 4–5 (one session when hours are tight), so experiment 1 is named before the week-one read.
4. **One experiment at a time.** The experiments file may list up to three running; the challenge runs the top one. A member with 4h+ a session may run two.
5. **Continue or kill is decided by the pass bar, not by mood.** Pass → continue (double down or iterate per the file's own "on pass" move). Fail → kill, log the learning, next from the queue. Two kills in a row → the read also opens `productos/define/BONUS-Pivot-Framework.md` and asks whether the problem is the channel or the offer.
6. **A payment before Day 30 does not end the challenge (decided).** It is logged, celebrated, posted (`Sell in 30 - My first customer! 🚀`), the customer is asked for the testimonial, and the remaining weeks run the next experiment for customers two and three.
7. **Hours per session scale one plan, never two** (same rule as Ship in 7).
8. **Thirty sessions, not thirty calendar days** (same rule as Ship in 7): consecutive days recommended, the counter advances by check-in, a session without its proof is a miss. Weekly reads happen every seventh session.

### Worked examples (ship in the skill as `plans/`)

Only week one differs; weeks 2–4 are the experiment loop in every example.

**Live, free, will charge** · S1 Define backfill + Price it · S2 Checkout live (test purchase) · S3 Believers backfill + Warm conversations · S4 Channel · S5 Experiments · S6 Follow-ups · S7 Read + post → W2–W4 experiment loop → S29 Sell Report · S30 Close.

**Live, priced, nobody has paid** · S1 Define backfill · S2 Checkout live (verify with a real purchase) · S3 Believers backfill + Warm conversations · S4 Channel · S5 Experiments · S6 Follow-ups · S7 Read + post → experiment loop.

**Live, free, staying free** (bar: one activated user) · S1 Define backfill · S2 Believers backfill · S3 Warm conversations (the ask is "try it", not "buy it") · S4 Channel · S5 Experiments (backlog leans on activation) · S6 Follow-ups · S7 Read + post → experiment loop.

**Not yet live, one deploy away** · S1 Go live (deploy guide) · S2 Go live (smoke test) + Define backfill · S3 Checkout live · S4 Warm conversations · S5 Channel + Experiments · S6 Follow-ups · S7 Read + post → experiment loop.

**Live with users, no revenue** · S1 Define backfill + Price it · S2 Checkout live · S3 Warm conversations to existing users first · S4 Channel · S5 Experiments (a founding offer to existing users is the obvious experiment 1) · S6 Follow-ups · S7 Read + post → experiment loop.

**Just shipped via Ship in 7** · S1 Announce (the launch post that was Ship in 7's stretch) + Believers backfill · S2 Checkout live · S3 Warm conversations · S4 Channel · S5 Experiments · S6 Follow-ups · S7 Read + post → experiment loop.

## 3. Skill design

### Files

```
skills/studio-sell-in-30/
  SKILL.md                four modes; the block library; the 30-day shape; composition rules;
                          the experiment loop; Skool post format; failure patterns
  plans/live-free-will-charge.md
  plans/live-priced.md
  plans/live-free-staying-free.md   week-one worked examples the composer starts from
  plans/one-deploy-away.md
  plans/live-with-users.md
  plans/after-ship-in-7.md
  SELL-IN-30-TEMPLATE.md  the docs/SELL-IN-30.md skeleton
```

### Frontmatter

- `name`: `studio-sell-in-30` **(decided)**.
- `description` ≤ 1024 characters and bytes. Triggers: "sell in 30", "sell in thirty", "first customer in 30 days", "get my first customer", "first paying customer", "30 day challenge", "day 12 check-in", "weekly read", "what's my task today", "nobody has paid yet".

### Mode 1 — Enrol (Day 0, ~30 min)

1. **Setup check**; run `studio-setup` if needed **(decided)**.
2. **Prerequisite check (decided):** is the product reachable, or can it be within the first few days? Neither → stop and route to `studio-ship-in-7`. `docs/SHIP-IN-7.md` open → close it first.
3. **Read the evidence:** live URL, price on the site, payments integration, `docs/LAUNCHES.md` and its rung, signups or usage the member reports (asked, never inferred from code), existing Define docs.
4. **Ask the starting point (decided: always ask)**, and **whether the product will charge within the 30 days (decided)**: that sets the bar to a payment or to an activated user.
5. **Confirm the inputs:** start date, hours per day (a number, not a tier; consecutive days recommended), the price if one exists, who they can already reach (the same two routing questions launch #1 asks).
6. **Compose week one** from the block library and show it as a table: session, block, skill, proof. Weeks 2–4 are shown as the experiment loop with the slots empty until the experiments file exists. The member edits before it's written.
7. **Write `docs/SELL-IN-30.md`:** header (dates, hours, the bar verbatim, starting point, price line), the plan table, empty daily log, weekly read slots, Skool post log.
8. **Draft the Day-0 Skool post** and name Day 1's literal task.

### Mode 2 — Daily check-in (Days 1–30)

Identical mechanics to Ship in 7 (the counter advances by check-in; confirm the last session's proof first; log done/partial/missed; compression on misses; name today's one block; say what the next session looks like), **except that the Skool post is drafted only on read days, Day 0 and Day 30 (decided)**, plus:

- **In weeks 2–4 the check-in reads `2-Growth-Experiments.md` first** and names the next "Do this" step of the running experiment as today's block. Experiment days log the step's artefact and every reply verbatim. Silence is a count of zero, logged.
- **Every reply is answered the same day.** The check-in starts by asking about open threads.
- **Missed sessions compress within the week**, never across the seventh-session read: the read always happens on schedule, with whatever the week produced. Two consecutive misses shrink that week's experiment steps; they don't end the challenge.

### Mode 3 — Weekly read (Days 7, 14, 21, 28)

The `studio-launch` sitting-two ritual applied to the week, written into `docs/SELL-IN-30.md` and `docs/LAUNCHES.md`, and posted to Skool. In weeks 2–4 it also reads the running experiment against its Pass = line, records the result and the decision (**continue or kill**) in `3-Growth-Experiments-Tracker.md`, and names next week's experiment. Two kills in a row open the Pivot Framework.

### Mode 4 — Close (Day 30, or Day 31)

1. **Check the bar honestly:** a payment (or, for a product staying free, an activated user), or not. Partial outcomes (a signup, a "send me the link") are logged on the ladder and named as what they are.
2. **Write the Sell Report (decided: the pre-call brief):** result vs bar; people reached, warm/cold; believers gained; the rung reached each week; what the market said in its own words; the variable changed, if any; the biggest blocker. Structured in the shape the coach intake expects, so a member who books a call arrives with their situation documented. Ends with one line: *bring this to your call.*
3. **Draft the graduation Skool post** (`Sell in 30 completed! Here's what I learnt`).
4. **The recommendation (decided):** join Product Studio and book a call at **buildgreatproducts.com/product-studio**, once, framed by outcome, in the closing message and the Sell Report. Paid → "you have a customer; a custom plan is how you get the next fifty." Not yet → "thirty days of real signal is exactly what a coach turns into the plan that works." The pitch line is drafted in the skill in the ProductOS voice, for you to edit. Then what to run meanwhile: the Distribute loop (`studio-distribute-growth-experiments`) or the pivot framework.

### Failure patterns (named in SKILL.md)

The Friendly Echo (warm praise read as market signal) · The Rung Leap (one reply → "validated" → a silent week of building) · The Mood Kill (killing an experiment before its pass bar because it felt slow) · The Zombie Experiment (continuing one that failed its pass bar because it felt close) · The Pitch-Slap · The Silent Zero · The Discount Spiral (dropping the price every time someone hesitates) · The Fresh-Start Reflex (a new channel every week) · The Feature Excuse ("they'll pay once I add X").

---

## 4. Daily accountability

Two loops, as in Ship in 7 **(decided)**: the in-agent check-in **every session**, and a **new Skool post at each weekly read** plus the start and the close, six posts in all **(decided: weekly, not daily)**. House-format title, body free-drafted in the member's own voice.

- **Titles (decided, your wording):**

  ```
  Sell in 30 - Day 0! [app name]
  Sell in 30 - Week 2! [rung reached, five words]   (weeks 2–4: the experiment and its continue/kill)
  Sell in 30 - My first customer! 🚀
  Sell in 30 completed! Here's what I learnt
  ```

  The first-customer post goes out the day the payment lands, whatever the week. The Week N post is the weekly read.
- **Body:** first person, the week's number (the channel's own metric, replies, the rung), one quote from the market if there was one, next week's target. Missed weeks are posted too, honestly. Zero is an entry.

---

## 5. System changes, build sequence

Specified once in `ship-in-7-skill-plan.md` §5–§6 and shared. Sell-in-30-specific additions:

- `skills/studio-distribute-gtm-strategy/SKILL.md` and `studio-distribute-growth-experiments/SKILL.md`: one line each, reading `docs/SELL-IN-30.md` when open so the plan fits the remaining days.
- `distribute/DISTRIBUTE-CHECKLIST.md`: the preamble line pointing challenge members at their open challenge file.
- Fixture repos for the dry-run: a live Next.js app with no pricing; the same with Stripe in test mode and a price page; the same with fake signups seeded; a repo with a closed `docs/SHIP-IN-7.md`.

---

## 6. Decisions and open questions

**Decided, carried from the first review:** `studio-` prefix · runs after `studio-setup`, and runs it first if missing · bar is one payment · always ask the starting point · Skool: new post per day, house-format title, member's voice · Product Studio + book a call at the close.

**Decided, carried from Ship in 7's review (apply to both skills):** Product Studio link is buildgreatproducts.com/product-studio, pitch drafted for your edit, in the closing message and report only · Skool feed only, no push reminders · sessions not calendar days, consecutive recommended · one plan scaled to hours, never two · loop mechanics duplicated in both skills · must-nots: never post on the member's behalf, never run paid tools or create accounts without them, never touch production data, and for Sell in 30 never change a live price without confirmation.

**Decided in this review:**

1. **Not-live members:** allowed to enrol when they can deploy within the first few days; otherwise routed to Ship in 7.
2. **Free products:** allowed, with one activated user as the bar when the product won't charge within the 30 days.

3. **The daily activity model (decided, your shape):** week one is foundations (backfill, deploy if needed, checkout live with a test purchase, warm-network conversations, GTM strategy, growth experiments, read + post); weeks 2–4 each run the highest-leverage experiment from the member's own backlog and end with a continue/kill read and a Skool post; the end is the Sell Report, the graduation post, and the Product Studio call booking. No fixed quota; the daily steps come from the running experiment's "Do this" list.

**Decided in the second pass:**

4. **Payment before Day 30:** keep going for customers two and three.
5. **Post cadence:** weekly, at each read, plus Day 0 and Day 30. Four 7-session weeks kept.
6. **Skool titles:** your wording, recorded in §4.
7. **The Sell Report is the pre-call brief**, ending with "bring this to your call".
8. **Cold outreach:** only when an experiment calls for it, logged as cold (resolved by Q3).
9. **Founding offer:** drafted from the member's own anchors each time, no house pattern.
10. **Existing material:** none to mirror (assumed, as for Ship in 7).

---

## 7. Risks

1. **Thirty sessions is a lot of surface for drop-off.** Mitigation: the check-in is five minutes, the weekly post is drafted, misses are posted rather than hidden, and the weekly read gives a natural re-entry.
2. **The bar is out of the member's control.** Payment depends on the market. Mitigation: the ladder records every partial rung, the read is honest, and the close's recommendation is framed for both outcomes.
3. **Price changes on a live product.** Mitigation: Checkout live and any price change are confirmed with the member, never automated; the golive payments guidance is reused, not reinvented.
4. **Cold outreach etiquette.** Community rules and platform norms. Mitigation: the launch skill's Pitch-Slap rule and "check the community's self-promotion rules" carry over; cold sends are always logged as cold.
5. **Duplicated loop mechanics with Ship in 7.** Decided: duplicated, with a CHANGELOG rule that a change to one loop is a change to both.
6. **Experiments sized wrong for a week.** A backlog item that needs a month can't be read on session 7. Mitigation: the challenge briefs the experiments skill with the clock; anything bigger is split into the up-next queue.
