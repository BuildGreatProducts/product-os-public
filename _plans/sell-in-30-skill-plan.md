# Plan: `studio-sell-in-30`

*Working plan for a new cross-phase ProductOS skill. Lives in `_plans/` (never shipped). Sibling plan: `ship-in-7-skill-plan.md`. The system wiring, build sequence and shared daily-loop mechanics are specified there and referenced here.*

**Status:** reviewed, one item tabled. Every question is answered except the daily activity model (Q3), which is **tabled pending your amends**: the daily work should be defined by the go-to-market strategy's "Do this" list for the chosen channel, not by a fixed outreach quota. Cold outreach (Q8) is deferred with it.

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
| **Live, free, will charge** | Live URL, no price on the site, no payments integration | Price it, wire checkout, then launch to believers and one channel |
| **Live, free, staying free for now** | As above; the member says no charge in the next 30 days | Bar becomes one activated user: activation audit, launch, get real people to the magic moment |
| **Live, priced, nobody has paid** | Price on the site or Stripe in place, `docs/LAUNCHES.md` rung below `payment` | Fix the conversion path, then launch and run twenty conversations |
| **Live with users, no revenue** | Signups or activity, no payment | Activation and conversion audits, a founding offer to the people already using it |
| **Just shipped via Ship in 7** | `docs/SHIP-IN-7.md` closed this week | Announce, then the standard four weeks |

### How it fits the system

- **Fourth cross-phase skill.** Runs after `studio-setup` **(decided)**; Day 0 checks the setup conditions and runs `studio-setup` first if any fail.
- **Composes from the Distribute checklist and the launch ritual.** Launch #4 (the public launch, win: first payment) is the spine; the Distribute steps and the two audits supply the rest. Nothing new is taught; the challenge owns sequencing, the daily loop, and the log.
- **Writes `docs/SELL-IN-30.md`** (tracked, the member's). Launch entries and believers go to `docs/LAUNCHES.md` through `studio-launch`, as they already do.
- **Backfills what's missing first.** No `docs/PRODUCT.md` → `studio-define-from-code` + `studio-define-product` on Day 1 (hours, not days). No `docs/LAUNCHES.md` → create it and backfill everyone who has ever responded onto the believers list, the same move `studio-launch` makes for coached members.
- **Only one challenge open at a time.** If `docs/SHIP-IN-7.md` is open, close it first.

---

## 2. The plan composer

Same mechanism as Ship in 7: a **block library**, composed into **four weeks with a fixed weekly shape**, fitted to the starting point and the member's hours.

### The weekly shape (the same every week)

- **Days 1–5:** one block a day. **Tabled (Q3):** the earlier draft gave outreach days a fixed conversation quota. Your direction is that the daily activity should be **defined by the go-to-market strategy skill**, not by a quota: once `1-Go-To-Market-Strategy.md` exists, the channel's own "Do this" checklist and its "Working =" number become the daily blocks and the weekly pass bar. Some channels are outreach; others are content, community, listings, or partnerships. The plan below still shows "Conversations" as a placeholder block until you send amends.
- **Day 6:** follow-ups only. Every open thread gets a reply; the checkout link goes to anyone who leaned in.
- **Day 7 (7, 14, 21, 28): the weekly read.** `studio-launch` sitting two, applied to the week: log every response including silence, warm/cold labelled, ladder rung reached, believers added, the next week's rung named. On the second consecutive missed rung, `productos/define/BONUS-Pivot-Framework.md` is read and one variable (product, persona, or price) is chosen for the following week. **The read is the weekly Skool post (decided: four 7-session weeks, one post per read).**

### Block library

| Block | Skill(s) / action | Produces | Proof |
| --- | --- | --- | --- |
| Setup check | `studio-setup` | wired repo | file diff |
| Go live *(when not yet live)* | `studio-develop-golive`, then work `docs/DEPLOY.md` | live URL | smoke test as a real customer |
| Define backfill | `studio-define-from-code` → `studio-define-product` | `docs/PRODUCT.md` | file exists |
| Price it | `studio-define-pricing` | one launch price, the price line | price said out loud in the log |
| Checkout live | payments switched to live via the payments section of `studio-develop-golive`, a real test purchase | a working checkout link | test-purchase receipt |
| Believers backfill | create `docs/LAUNCHES.md`; everyone who ever responded, with source and status | the believers list | file exists |
| Channel | `studio-distribute-gtm-strategy` | `1-Go-To-Market-Strategy.md`, one primary channel with its "Do this" list | file exists |
| **Launch #4** | `studio-launch` sitting one | believers messaged first, then the channel; 10 named DMs | live post / sent-folder screenshot |
| Channel work *(placeholder, Q3 tabled)* | the GTM strategy's "Do this" list for the primary channel, one item a day; every reply answered same day | log entries | the channel's own "Working =" number, in the log |
| Conversion path | `studio-develop-cro-audit` on landing, pricing, checkout → fixes via the build loop | prioritised fixes, top three shipped | before/after |
| Activation | `studio-distribute-activation-retention-audit` → fix the top leak | users reach the magic moment | one activation logged |
| Founding offer | a time-boxed founding-customer offer **drafted from the member's own pricing anchors and Product Offer each time (decided: no house pattern)** | the offer message | sent to every warm lead |
| Second push | `studio-launch` resend: rewritten hook or price toggled, through the next-warmest route | resent | screenshot |
| Experiment | `studio-distribute-growth-experiments` | one experiment running, with a pass bar | tracker entry |
| Weekly read | `studio-launch` sitting two, applied to the week | `docs/LAUNCHES.md` updated | the read, posted |
| Close | the Sell Report + the recommendation | `docs/SELL-IN-30.md` complete | graduation post |

### Composition rules

1. **Launch #4 ships by Day 5.** Nothing before it may slip it: if Define backfill or Checkout live runs long, Channel compresses to "the one place your believers already are".
2. **Checkout works before anyone is asked for money.** A real test purchase is Day 2's proof on every path, or Day 3 at the latest.
3. **A full send before any pivot (Q3 tabled: wording depends on the daily activity model).** The pivot framework's own rule (fewer than ten demo posts is a patience problem) still applies: the Day-14 read may not choose a pivot variable unless the channel's "Do this" list was actually worked through.
4. **One variable per week.** After a missed rung, the following week changes product, persona, or price, never two.
5. **Warm before cold, always.** Believers get every message first. Cold outreach starts only when the warm list is exhausted, and is logged as cold.
6. **A payment before Day 30 does not end the challenge (decided).** It is logged, celebrated, posted (`Sell in 30 - My first customer! 🚀`), the customer is asked for the testimonial, and the remaining days go to customers two and three with the same loop. Momentum is the Product Studio conversation.
7. **Hours per day scale one plan, never two** (same rule as Ship in 7): the composer fits the channel work and the fix blocks to the hours the member gives and recommends more where it changes the outcome.
8. **Thirty sessions, not thirty calendar days** (same rule as Ship in 7): consecutive days recommended, the counter advances by check-in, a session without its proof is a miss. Weekly reads happen every seventh session.

### Worked examples (ship in the skill as `plans/`)

*(Days marked "Channel work" are the placeholder for the tabled Q3; they will be replaced by the GTM strategy's "Do this" items once the activity model is agreed.)*

**Not yet live, one deploy away** · W1: D1 Go live (deploy guide) · D2 Go live (smoke test) · D3 Define backfill + Price it · D4 Checkout live + Channel · D5 **Launch #4** · D6 follow-ups · D7 read. W2–W4 as the free-will-charge example.

**Live, free, will charge** · W1: D1 Define backfill + Price it · D2 Checkout live · D3 Believers backfill · D4 Channel · D5 **Launch #4** · D6 follow-ups · D7 read. W2: D8–D12 Channel work + Conversion path fixes · D13 follow-ups · D14 read. W3: D15 Founding offer · D16–D19 Channel work + Activation · D20 Second push · D21 read. W4: D22 Experiment · D23–D27 Channel work · D28 read · D29 Sell Report · D30 Close.

**Live, free, staying free** (bar: one activated user) · W1: D1 Define backfill · D2 Activation (who reaches the magic moment today, fix the top leak) · D3 Believers backfill · D4 Channel · D5 **Launch #4** · D6–D7 as above. W2–W4 as above with Conversion path replaced by Activation work and no Founding offer.

**Live, priced, nobody has paid** · W1: D1 Define backfill · D2 Checkout live (verify with a real purchase) · D3 Conversion path · D4 Channel + Believers backfill · D5 **Launch #4** · D6–D7 as above. W2–W4 as above, with Activation in W2 if there are signups.

**Live with users, no revenue** · W1: D1 Define backfill + Price it · D2 Checkout live · D3 Activation (who reaches the magic moment today) · D4 Founding offer drafted for existing users · D5 **Launch #4 to existing users first** · D6–D7 as above. W2 leads with the Conversion path; W3 with Channel and cold outreach.

**Just shipped via Ship in 7** · W1 opens with Announce (the launch post that was Ship in 7's stretch) as D1, then the standard shape.

---

## 3. Skill design

### Files

```
skills/studio-sell-in-30/
  SKILL.md                three modes; the block library; weekly shape; composition rules;
                          Skool post format; failure patterns
  plans/one-deploy-away.md
  plans/live-free-will-charge.md
  plans/live-free-staying-free.md   worked examples the composer starts from
  plans/live-priced.md
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
6. **Compose the four weeks** and show the plan as a table: day, block, skill, proof, quota. The member edits before it's written.
7. **Write `docs/SELL-IN-30.md`:** header (dates, hours, the bar verbatim, starting point, price line), the plan table, empty daily log, weekly read slots, Skool post log.
8. **Draft the Day-0 Skool post** and name Day 1's literal task.

### Mode 2 — Daily check-in (Days 1–30)

Identical mechanics to Ship in 7 (the counter advances by check-in; confirm the last session's proof first; log done/partial/missed; compression on misses; name today's one block; say what the next session looks like), **except that the Skool post is drafted only on read days, Day 0 and Day 30 (decided)**, plus:

- **Channel-work days** log the channel's own number and every reply verbatim. Silence is a count of zero, logged. *(Exact shape follows the tabled Q3.)*
- **Every reply is answered the same day.** The check-in starts by asking about open threads.
- **Missed sessions compress within the week**, never across the seventh-session read: the read always happens on schedule, with whatever the week produced. Two consecutive misses shrink that week's channel work; they don't end the challenge.

### Mode 3 — Weekly read (Days 7, 14, 21, 28)

The `studio-launch` sitting-two ritual applied to the week, written into `docs/SELL-IN-30.md` and `docs/LAUNCHES.md`, and posted to Skool. Ends by naming next week's rung and, if a rung was missed twice, the one variable that changes.

### Mode 4 — Close (Day 30, or Day 31)

1. **Check the bar honestly:** a payment (or, for a product staying free, an activated user), or not. Partial outcomes (a signup, a "send me the link") are logged on the ladder and named as what they are.
2. **Write the Sell Report (decided: the pre-call brief):** result vs bar; people reached, warm/cold; believers gained; the rung reached each week; what the market said in its own words; the variable changed, if any; the biggest blocker. Structured in the shape the coach intake expects, so a member who books a call arrives with their situation documented. Ends with one line: *bring this to your call.*
3. **Draft the graduation Skool post** (`Sell in 30 completed! Here's what I learnt`).
4. **The recommendation (decided):** join Product Studio and book a call at **buildgreatproducts.com/product-studio**, once, framed by outcome, in the closing message and the Sell Report. Paid → "you have a customer; a custom plan is how you get the next fifty." Not yet → "thirty days of real signal is exactly what a coach turns into the plan that works." The pitch line is drafted in the skill in the ProductOS voice, for you to edit. Then what to run meanwhile: the Distribute loop (`studio-distribute-growth-experiments`) or the pivot framework.

### Failure patterns (named in SKILL.md)

The Friendly Echo (warm praise read as market signal) · The Rung Leap (one reply → "validated" → a silent week of building) · The Quota Dodge (posting instead of talking to people) · The Pitch-Slap · The Silent Zero · The Discount Spiral (dropping the price every time someone hesitates) · The Fresh-Start Reflex (a new channel every week) · The Feature Excuse ("they'll pay once I add X").

---

## 4. Daily accountability

Two loops, as in Ship in 7 **(decided)**: the in-agent check-in **every session**, and a **new Skool post at each weekly read** plus the start and the close, six posts in all **(decided: weekly, not daily)**. House-format title, body free-drafted in the member's own voice.

- **Titles (decided, your wording):**

  ```
  Sell in 30 - Day 0! [app name]
  Sell in 30 - Week 2! [rung reached, five words]
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

**Tabled, pending your amends after reviewing this plan:**

3. **The daily activity model.** Not a fixed outreach quota. The go-to-market strategy skill defines what the daily work is for the chosen channel (outreach, content, community, listings, partnerships), and its "Working =" number is the weekly pass bar. Send amends and I'll rewrite §2 around them.

**Decided in the second pass:**

4. **Payment before Day 30:** keep going for customers two and three.
5. **Post cadence:** weekly, at each read, plus Day 0 and Day 30. Four 7-session weeks kept.
6. **Skool titles:** your wording, recorded in §4.
7. **The Sell Report is the pre-call brief**, ending with "bring this to your call".
8. **Cold outreach:** deferred; depends on the daily activity model (Q3).
9. **Founding offer:** drafted from the member's own anchors each time, no house pattern.
10. **Existing material:** none to mirror (assumed, as for Ship in 7).

---

## 7. Risks

1. **Thirty sessions is a lot of surface for drop-off.** Mitigation: the check-in is five minutes, the weekly post is drafted, misses are posted rather than hidden, and the weekly read gives a natural re-entry.
2. **The bar is out of the member's control.** Payment depends on the market. Mitigation: the ladder records every partial rung, the read is honest, and the close's recommendation is framed for both outcomes.
3. **Price changes on a live product.** Mitigation: Checkout live and any price change are confirmed with the member, never automated; the golive payments guidance is reused, not reinvented.
4. **Cold outreach etiquette.** Community rules and platform norms. Mitigation: the launch skill's Pitch-Slap rule and "check the community's self-promotion rules" carry over; cold sends are always logged as cold.
5. **Duplicated loop mechanics with Ship in 7.** Decided: duplicated, with a CHANGELOG rule that a change to one loop is a change to both.
6. **The daily activity model is unresolved (Q3).** Until it is, the worked examples carry a placeholder and the skill can't be written. Blocking for Sell in 30 only; Ship in 7 can be built now.
