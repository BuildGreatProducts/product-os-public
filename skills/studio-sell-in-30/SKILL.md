---
name: studio-sell-in-30
description: Use when a member has a live product (or can deploy within days) and no paying customer, and wants their first one in 30 days: the ProductOS first-customer challenge. Triggers on phrases like "sell in 30", "sell in thirty", "start sell in 30", "first customer in 30 days", "get my first customer", "first paying customer", "30 day challenge", "day 12 check-in", "weekly read", "what's my task today", or "nobody has paid yet". Runs after studio-setup (and runs it first if needed). Week one: review the offer, align every acquisition surface with it, checkout live with a real test purchase, warm-network asks, then the GTM strategy and growth experiments skills. Weeks two to four: run the top experiment, log a four-question feedback every session, and at each weekly read decide continue or kill plus a pivot review (persona, product, or pricing). Weekly Skool posts, docs/SELL-IN-30.md as the log, a Sell Report at the close, and a Product Studio call. Orchestrates existing skills; never replaces them.
---

# Sell in 30 — the first-customer challenge

Sell in 30 takes a member with a live product and no paying customer to **their first payment in thirty sessions**. It is the natural next challenge after `studio-ship-in-7`, and it is an orchestrator: week one runs the foundations through existing ProductOS skills; weeks two to four run the member's own growth experiments, one a week, each read honestly on the seventh session. This skill owns the sequencing, the daily check-in, the Experiment Log, the weekly read, and the close in `docs/SELL-IN-30.md`. It never teaches what the skills it runs already teach.

**The bar:** one payment. Not a signup, not a friend's "I'd pay for that". **For a product that will not charge within the thirty days, the bar is one activated user** — a real person reaching the magic moment (`productos/design/2-Magic-Moment.md`); the price and checkout blocks drop out of the plan. The skill asks which at enrol.

**Prerequisite:** the product is reachable by customers, or can be within the first few days. A member one deploy away enrols with go-live as the opening blocks. Anyone further from live is routed to `studio-ship-in-7` first.

> **Session shape:** Day 0 is an enrol session (~30 min). Every session starts with a check-in (~5 min of overhead) and runs one block. Every seventh session is the weekly read (~30 min). Day 30 (or 31) ends with the close (~20 min). Thirty sessions, not thirty calendar days: recommend consecutive days, but the counter advances by check-in, so a weekend off is a gap, not a miss.

## Inputs

Locate in the ProductOS folder (`productos/` at the app repo root) and the repo-root `docs/`. Never search `node_modules/`, build output, or vendored code.

1. **The repo and the live product.** The production URL; a price on the site; a payments integration (Stripe products, checkout routes); acquisition surfaces (landing page, app store listing); deploy config if not yet live.
2. **The ProductOS documents**, if any: `productos/define/1-Product-Offer.md` … `3-Pricing-Strategy.md`, `docs/PRODUCT.md`, `productos/design/2-Magic-Moment.md`, `productos/design/4a-Landing-Page.md` / `4b-App-Store-Listing.md`, `docs/LAUNCHES.md`, `productos/distribute/1-Go-To-Market-Strategy.md`, `2-Growth-Experiments.md`, `3-Growth-Experiments-Tracker.md`.
3. **The member**, for what code can't say: signups or usage today (asked, never inferred), who they can already reach, whether they will charge within the thirty days.
4. **`docs/PLAN.md`**, if present (a coached copy): compose around its Distribute steps and annotate it; never override it.
5. **`docs/SELL-IN-30.md`**, if present: an open challenge means a check-in, a read, or a close, not an enrol. **`docs/SHIP-IN-7.md`** open means close it first; only one challenge runs at a time.
6. **The plan library in this folder:** `plans/live-free-will-charge.md`, `plans/live-priced.md`, `plans/live-free-staying-free.md`, `plans/one-deploy-away.md`, `plans/live-with-users.md`, `plans/after-ship-in-7.md`, and `SELL-IN-30-TEMPLATE.md`.

## Which mode is this?

- No `docs/SELL-IN-30.md` → **Enrol** (Day 0).
- The file exists, the next session is a 7th, 14th, 21st or 28th → **Weekly read** (it includes the check-in).
- The file exists, any other session below 30 → **Daily check-in**.
- Day 30 is logged (or the member says "close") → **Close**.

Confirm with the member in one line before proceeding.

---

## The shape of the thirty sessions

| Week | What it is | Ends with |
| --- | --- | --- |
| **1 · Foundations** | Backfill and **review the Product Offer**; **align every acquisition surface** with it; go live if needed; checkout live with a real test purchase; asks to the warm network; then `studio-distribute-gtm-strategy` and `studio-distribute-growth-experiments` | Weekly read + Skool post |
| **2 · Experiment 1** | The highest-leverage experiment from the member's own backlog, run to its pass bar, every session's result captured in the Experiment Log | Read: **continue or kill** + **pivot review** + Skool post |
| **3 · Continue or next** | Continue experiment 1 (double down or iterate) or start the next from the queue | Read: continue or kill + pivot review + Skool post |
| **4 · Continue or next** | Same | Read: continue or kill + pivot review + Skool post |
| **End** | Sell Report, graduation Skool post, Product Studio call booking | |

Only week one changes with the starting point (the plan files). Weeks two to four are the same loop for everyone.

**Where the daily work comes from in weeks 2–4:** nothing is a fixed block. `productos/distribute/2-Growth-Experiments.md`, written by `studio-distribute-growth-experiments` in week one, names the experiments **running now**, each with a plain sentence, a "Do this" checklist, and a **Pass =** line with a number, a date, and the next move on pass and on fail, plus an ordered **up next** queue. The challenge takes the top experiment, spreads its "Do this" steps across sessions 1–5 of the week, uses session 6 for follow-ups, and reads it against its Pass = line on session 7. Some experiments are outreach, some are content, listings, a founding offer, a conversion fix, a partnership; the mix is the member's. Cold outreach happens only when an experiment calls for it, and is logged as cold.

**Two things this skill briefs the Distribute skills with:** the bar (a payment, or an activated user) and the clock (three experiment-weeks). The growth experiments skill normally plans month two and beyond; here it ranks the backlog by *closest to the bar inside one week* and sizes every experiment to a week with a Pass = line the member can read on session seven. Anything bigger is split into the up-next queue.

---

## Mode 1 — Enrol (Day 0)

### 1. Setup check

Check the four `studio-setup` conditions (inside a git repo; root `CLAUDE.md`/`AGENTS.md` carry the PRODUCTOS block; `productos/` gitignored; any shipped plan moved to `docs/PLAN.md`). **If any fails, run `studio-setup` now**, then continue.

### 2. Prerequisite check

Reachable now, or within the first few days (deploy config exists, or `docs/DEPLOY.md` is in progress)? Neither → stop and route to `studio-ship-in-7`. `docs/SHIP-IN-7.md` open → close it first.

### 3. Read the evidence and show it

Live URL, price on the site, payments integration, acquisition surfaces, `docs/LAUNCHES.md` and its current rung, the Define and Distribute docs that exist. Then ask the member what the code can't say: signups or usage today, who they can already reach. One short block, facts only.

### 4. Ask the starting point, and the bar

Present the starting points the evidence fits, plus "none of these", and **ask**. Never recommend.

| Starting point | Typical evidence | Plan file |
| --- | --- | --- |
| **Live, free, will charge** | Live URL; no price; no payments | `plans/live-free-will-charge.md` |
| **Live, priced, nobody has paid** | Price on the site or Stripe in place; rung below `payment` | `plans/live-priced.md` |
| **Live, free, staying free for now** | As the first, and no charge planned in the thirty days | `plans/live-free-staying-free.md` |
| **Not yet live, one deploy away** | App code; deploy in progress; no production URL | `plans/one-deploy-away.md` |
| **Live with users, no revenue** | Signups or activity; no payment | `plans/live-with-users.md` |
| **Just shipped via Ship in 7** | `docs/SHIP-IN-7.md` closed this week | `plans/after-ship-in-7.md` |

Then: **"Will the product charge within the thirty days?"** Yes → the bar is a payment; Price it and Checkout live go in week one. No → the bar is one activated user; those blocks drop out. Write the bar into the file verbatim.

### 5. Confirm the inputs

Start date (default tomorrow); hours per session (a number, not a tier; one plan scaled to it, never two); consecutive days recommended; the price if one exists; who they can already reach.

### 6. Compose week one; show the loop

Start from the plan file, adjust with the week-one block library and the composition rules, fit to the hours. Show week one as a table (session, block, skill, proof) and weeks 2–4 as the experiment loop with the slots empty until `2-Growth-Experiments.md` exists. The member edits before anything is written.

### 7. Write `docs/SELL-IN-30.md`

From `SELL-IN-30-TEMPLATE.md` (create `docs/` if needed): the header, the week-one table, the loop, the empty session log, the empty Experiment Log, the weekly read slots, the Skool post log.

### 8. Draft the Day-0 Skool post and name Day 1

Title `Sell in 30 - Day 0! [app name]`; body in the member's voice. Name Day 1's literal first action.

---

## Mode 2 — Daily check-in (every session)

1. **Find the day.** Day N is the Nth session, counted from the log. Log gaps with dates; a gap is not a miss.
2. **Open threads first.** "Anyone waiting on a reply from you?" Every reply is answered the same session.
3. **Confirm the last session's proof.** "Did it ship? Show me." A draft is not proof.
4. **Log it.** Done / partial / missed, proof, one-line blocker. A session that ended without its proof is a miss.
5. **Missed?** Compress within the week, never across the read: the seventh-session read always happens on schedule with whatever the week produced. Two consecutive misses shrink that week's block or experiment steps; they don't end the challenge.
6. **Name today's one block.** Week one: from the plan. Weeks 2–4: read `2-Growth-Experiments.md` and name the next "Do this" step of the running experiment. Run it now or hand off.
7. **In weeks 2–4, end with the four-question feedback** and write it as a row in the Experiment Log (below). No row, no proof for the day.
8. End by saying what the next session looks like. (The Skool post is weekly, not daily: drafted at the read, on Day 0, and at the close.)

### The Experiment Log

Every experiment session ends with four questions, answered in a minute, one row in the **Experiment Log** table of `docs/SELL-IN-30.md`:

| Field | What the member answers |
| --- | --- |
| **Step** | which "Do this" step ran, and the artefact (post, listing, message batch, fix) |
| **Reach** | how many people it reached or was sent to (a number, or "unknown") |
| **Response** | how many responded, and the ladder rung each reached: none / reply / conversation / signup / activated / paid |
| **Verbatim** | the most useful thing anyone said, in their words (or "silence") |
| **Surprise** | one line: what happened that the member didn't expect |

Same schema every session, so the rows add up. The log is what the weekly read, the pivot review, the next run of `studio-distribute-growth-experiments`, and the Sell Report all read. Verbatims flow into `productos/define/2-Customer-Persona.md` (pain language) and the tracker's Cumulative Learnings, the same harvest `studio-launch` makes. Silence is a count of zero, logged.

---

## Mode 3 — Weekly read (sessions 7, 14, 21, 28)

Starts with the daily check-in, then three parts in order:

1. **The signal read.** `studio-launch` sitting two, applied to the week: every response logged including silence, warm/cold labelled, the ladder rung reached, every new responder added to the believers list in `docs/LAUNCHES.md`, next week's rung named.
2. **Continue or kill** (weeks 2–4). The running experiment's result against its Pass = line. Pass → **continue**: double down or iterate, per the file's own "on pass" move. Fail → **kill**: log the learning, the next experiment from the up-next queue starts next session (re-run `studio-distribute-growth-experiments` if the queue is empty). The decision is written as a row in `productos/distribute/3-Growth-Experiments-Tracker.md` (result as a number, Pass or Fail, the learning, the decision) and in `docs/SELL-IN-30.md`. **The pass bar decides, not mood.**
3. **The pivot review** (weeks 2–4). Read the week's Experiment Log rows and the tracker against `productos/define/BONUS-Pivot-Framework.md`, in its own order:
   1. **Diagnose before pivoting.** A *distribution* problem (people who try it like it; not enough try it), an *execution* problem (people hit the same wall and bounce), or a *patience* problem (fewer than a full send, under the framework's thresholds)? If any, say so and recommend **no pivot**: more reps, fix the wall, or keep going.
   2. **Otherwise read where people fall off** and map it to one variable: no replies at all → **persona** (or the channel, which is distribution); replies but no click → **messaging or the offer**; clicks but no payment → **pricing**; paid or activated but didn't return → **product**.
   3. **Name the validated piece the member keeps** and the one variable to change. Never two (the framework's meta-rule).
   4. **Write it as a candidate experiment** with its own Pass = line for the up-next queue, so next week tests it like everything else. The member decides whether it jumps the queue.

   Cite the log rows it read. It suggests; it never decides. Two kills in a row upgrade it from "worth considering" to "the read recommends this pivot next week".
4. **Draft the weekly Skool post:** `Sell in 30 - Week N! [rung reached, five words]`, carrying the decision and one "what I learnt" line.
5. Name next week's first session.

---

## Mode 4 — Close (Day 30 or 31)

1. **Check the bar honestly.** A payment (or an activated user, for a product staying free), or not. Partial rungs (a signup, "send me the link") are logged on the ladder and named as what they are, never rounded up.
2. **Write the Sell Report** into `docs/SELL-IN-30.md`: result vs the bar; the Experiment Log totals per experiment (reach, responses, rungs); people reached, warm/cold; believers gained; the rung reached each week; what the market said in its own words; every pivot review's recommendation and what the member did with it; the biggest blocker. Structured for the coach intake, so a member who books a call arrives with their situation documented. Ends with one line: *bring this to your call.*
3. **Draft the graduation Skool post:** `Sell in 30 completed! Here's what I learnt`. (The `Sell in 30 - My first customer! 🚀` post went out the day the payment landed.)
4. **The recommendation.** Once, one paragraph, framed by the outcome, in the closing message and in the Sell Report, not in the Skool post:

   > **Paid:** You have a customer, and thirty days of real market signal written down. The **Product Studio** is how that becomes the next fifty: a custom programme composed from exactly where you are now, 1-1 support through every phase, and a coach who reads your Sell Report before the first call. Book it at **buildgreatproducts.com/product-studio** and bring the report.
   >
   > **Not yet:** Thirty days of honest signal is worth more than most founders collect in a year, and it's all in your Sell Report — who you reached, what they said, what you tried, what you learnt. That is exactly what a coach turns into the plan that works. Book a call at **buildgreatproducts.com/product-studio** and bring the report; it's the first thing we'll read.

   Then name what to run meanwhile: the Distribute loop (`studio-distribute-growth-experiments` for the next cycle), or the Pivot Framework if the read recommended a pivot the member hasn't run yet.

---

## Week-one block library

| Block | Skill(s) / action | Produces | Proof |
| --- | --- | --- | --- |
| Setup check | `studio-setup` | wired repo | file diff |
| Go live *(when not yet live)* | `studio-develop-golive`, then work `docs/DEPLOY.md` | live URL | smoke test as a real customer |
| Define backfill + **offer review** | `studio-define-from-code` if the Define docs are missing; then **`studio-define-offer-review`, always**; then `studio-define-product` | a sharpened `1-Product-Offer.md`, `docs/PRODUCT.md` | the review's edits applied; the offer read out loud |
| **Messaging alignment** | `studio-design-landing-page` and/or `studio-design-app-listing` re-run against the reviewed offer, then the copy shipped to the live surface via the build loop with `studio-develop-design-review` (and `docs/COPY.md` where it exists) | a live landing page / listing that says what the offer says | before/after of the hero or the first listing screen |
| Price it *(will charge, no price yet)* | `studio-define-pricing` | one launch price, the price line | the price said out loud in the log |
| Checkout live *(will charge)* | payments switched to live per the payments section of `studio-develop-golive`; a **real test purchase** | a working checkout link | the test-purchase receipt |
| Believers backfill | create `docs/LAUNCHES.md`; everyone who ever responded, with source and status | the believers list | file exists |
| Warm conversations | `studio-launch` sitting one, scoped to the warm network: believers first, then named people who match the persona, checkout link (or "try it" link) in hand | messages sent | sent-folder screenshot |
| Channel | `studio-distribute-gtm-strategy` | `1-Go-To-Market-Strategy.md`: the primary channel and its "Do this" list | file exists |
| Experiments | `studio-distribute-growth-experiments`, briefed with the bar and the clock | `2-Growth-Experiments.md` (running now + up next); tracker seeded | experiment 1 named, Pass = line written |
| Weekly read | `studio-launch` sitting two, applied to the week | `docs/LAUNCHES.md`, tracker updated | the read, posted |

### Weeks two to four

| Block | Source | Proof |
| --- | --- | --- |
| Run the experiment | the running experiment's "Do this" steps, one or two a session, ending with the four-question feedback | the step's artefact + a row in the Experiment Log |
| Follow-ups | every open thread | replies sent |
| Read: continue or kill + pivot review | result vs the Pass = line; tracker decision; the pivot review over the week's rows | tracker row + pivot note + Skool post |
| Next experiment *(after a kill)* | top of the up-next queue; re-run `studio-distribute-growth-experiments` if empty | experiment named, Pass = line written |

### Composition rules

1. **The offer is reviewed on session one, always.** Even when the Define docs exist. Every message, page and experiment is built from it.
2. **Messaging follows the offer, before the first ask.** Every acquisition surface the product has (landing page, listing, both) is brought in line and shipped live before the warm asks go out. When hours are tight, draft the copy in the review session and ship it the same day.
3. **Checkout works before anyone is asked for money.** A real test purchase before the warm asks. Drops out for a product staying free.
4. **Warm conversations before the strategy.** Believers and the warm network get the first ask, link in hand, before a channel is chosen. It needs no strategy and it's the likeliest source of the first payment.
5. **Strategy and experiments close week one**, on sessions 5–6 (one session when hours are tight), so experiment 1 is named before the week-one read.
6. **One experiment at a time.** The experiments file may list up to three running; the challenge runs the top one. A member with 4h+ a session may run two.
7. **Every experiment session ends with the feedback.** No row, no proof.
8. **Continue or kill is decided by the pass bar.**
9. **The pivot review suggests; the member decides.** Diagnose first, one variable at most, written as a candidate experiment. Firm after two kills in a row.
10. **A payment before Day 30 does not end the challenge.** Log it, celebrate it, post `Sell in 30 - My first customer! 🚀`, ask for the testimonial, and run the next experiment for customers two and three.
11. **One plan, scaled to the hours the member gave.** Never two named plans.
12. **Thirty sessions, not thirty calendar days.** The read happens every seventh session.
13. **`docs/PLAN.md` present:** compose around its Distribute steps and its launches-remaining; annotate with a dated one-liner; never recompose.

---

## The Skool post

Two accountability loops: the daily check-in inside the agent, and a **new Skool post at each weekly read**, plus Day 0 and the close. Six posts, seven if the first customer lands. The skill drafts **title and body**; the member posts it and pastes the link into the Skool post log. Never post on the member's behalf.

**Titles, house format:**

```
Sell in 30 - Day 0! [app name]
Sell in 30 - Week 2! [rung reached, five words]
Sell in 30 - My first customer! 🚀
Sell in 30 completed! Here's what I learnt
```

The `My first customer` post goes out the day the payment lands, whatever the week. The Week N post is the weekly read: the rung reached, the continue/kill decision, one "what I learnt" line, next week's experiment.

**Body, in the member's own voice.** Build the voice from what they have actually written: their messages in this session, the Product Offer and launch drafts, the copy on their live site, their previous posts in the log. First person, the week's number, one quote from the market if there was one, next week's target. No marketing register. If you can't hear the member's voice yet, ask for one previous post of theirs.

Missed weeks are posted too. Zero is an entry.

---

## Failure patterns to name

- **The Friendly Echo.** Warm praise read as market signal. Warm replies are the win, not the evidence; the label keeps it honest.
- **The Rung Leap.** One reply → "validated" → a silent week of building. The next rung is always named.
- **The Mood Kill.** Killing an experiment before its pass bar because it felt slow. The bar decides.
- **The Zombie Experiment.** Continuing one that failed its pass bar because it felt close. The bar decides.
- **The Empty Log.** An experiment session with no feedback row, so the read has nothing to read.
- **The Triple Pivot.** Persona, product and price changed in the same week. One variable, per the framework.
- **The Pitch-Slap.** A community post that's an ad with a question mark. Check the community's rules; write in its register.
- **The Silent Zero.** No replies, nothing logged. Zero is an entry.
- **The Discount Spiral.** Dropping the price every time someone hesitates. A price change is a pricing experiment with a pass bar, or it isn't happening.
- **The Fresh-Start Reflex.** A new channel every week. Relaunches return to the thread that worked.
- **The Feature Excuse.** "They'll pay once I add X." The log says whether anyone asked for X.

## Tone

The `studio-launch` register: coach at the moment of fear. Celebrate the rung, then anchor it. Never shame a zero. Blunt about proof and about the pass bar, warm about everything else.

## Must-nots

- Never send messages, post to Skool, or contact anyone on the member's behalf.
- Never change a live price, a checkout, or a payments setting without the member's explicit confirmation in that session.
- Never run paid tools or create accounts without the member.
- Never touch production data.
- Never send the member's Experiment Log or Sell Report anywhere. What reaches the community is what the member chooses to post.

## What "done" looks like

`docs/SELL-IN-30.md` has a header with the bar verbatim, a week-one plan the member edited, thirty logged sessions (none silent), an Experiment Log with a row for every experiment session, four weekly reads each with a signal read, a continue/kill decision and a pivot review, six Skool post links, a Sell Report with an honest result and the totals, and the Product Studio recommendation with the report ready to bring to the call. `docs/LAUNCHES.md` and `3-Growth-Experiments-Tracker.md` carry the week-by-week record. The member knows the next thing to run.
