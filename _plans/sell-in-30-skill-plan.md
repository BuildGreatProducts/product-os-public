# Plan: `studio-sell-in-30`

*Working plan for a new cross-phase ProductOS skill. Lives in `_plans/` (never shipped). Sibling plan: `ship-in-7-skill-plan.md`. The system wiring, build sequence and shared daily-loop mechanics are specified there and referenced here.*

**Status:** draft for review. Decisions already taken in review are marked **(decided)**; everything else carries a recommended default.

---

## 1. What it is

The first-customer challenge. A member with a **live product and no paying customer** runs it in their app repo and gets a **custom 30-day plan that ends with their first payment**, one task a day, a daily Skool post, weekly signal reads, and a close that recommends joining Product Studio and booking a call. It is the natural next step after `studio-ship-in-7` and the strongest lead-in to the coaching programme: thirty days of logged market contact is exactly the material a coach composes a custom plan from.

**The bar (decided):** one payment. Not a signup, not an activated user, not a friend's "I'd pay for that". For a free product, the plan puts a price on it in week one.

**Prerequisite:** the product is reachable by customers. If it isn't, the skill says so and routes to `studio-ship-in-7` first (Q1).

### Where members arrive from

The skill reads the repo and `docs/LAUNCHES.md`, shows what it found, and **asks (decided: always ask)** which fits:

| Starting point | Evidence | What the 30 days are mostly spent on |
| --- | --- | --- |
| **Live, free, never asked for money** | Live URL, no price on the site, no payments integration | Price it, wire checkout, then launch to believers and one channel |
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

- **Days 1–5:** one block a day. Outreach days carry a **conversation quota** (default five new real conversations a day from Day 8 on; Q3).
- **Day 6:** follow-ups only. Every open thread gets a reply; the checkout link goes to anyone who leaned in.
- **Day 7 (7, 14, 21, 28): the weekly read.** `studio-launch` sitting two, applied to the week: log every response including silence, warm/cold labelled, ladder rung reached, believers added, the next week's rung named. On the second consecutive missed rung, `productos/define/BONUS-Pivot-Framework.md` is read and one variable (product, persona, or price) is chosen for the following week. The read is also the weekly Skool post.

### Block library

| Block | Skill(s) / action | Produces | Proof |
| --- | --- | --- | --- |
| Setup check | `studio-setup` | wired repo | file diff |
| Define backfill | `studio-define-from-code` → `studio-define-product` | `docs/PRODUCT.md` | file exists |
| Price it | `studio-define-pricing` | one launch price, the price line | price said out loud in the log |
| Checkout live | payments switched to live via the payments section of `studio-develop-golive`, a real test purchase | a working checkout link | test-purchase receipt |
| Believers backfill | create `docs/LAUNCHES.md`; everyone who ever responded, with source and status | the believers list | file exists |
| Channel | `studio-distribute-gtm-strategy` | `1-Go-To-Market-Strategy.md`, one primary channel with its "Do this" list | file exists |
| **Launch #4** | `studio-launch` sitting one | believers messaged first, then the channel; 10 named DMs | live post / sent-folder screenshot |
| Conversations | daily quota through the channel and DMs; every reply answered same day | log entries | count vs quota, in the log |
| Conversion path | `studio-develop-cro-audit` on landing, pricing, checkout → fixes via the build loop | prioritised fixes, top three shipped | before/after |
| Activation | `studio-distribute-activation-retention-audit` → fix the top leak | users reach the magic moment | one activation logged |
| Founding offer | a time-boxed founding-customer offer built from the pricing anchors (limited seats, a price that rises on a date, a guarantee from the Product Offer) | the offer message | sent to every warm lead |
| Second push | `studio-launch` resend: rewritten hook or price toggled, through the next-warmest route | resent | screenshot |
| Experiment | `studio-distribute-growth-experiments` | one experiment running, with a pass bar | tracker entry |
| Weekly read | `studio-launch` sitting two, applied to the week | `docs/LAUNCHES.md` updated | the read, posted |
| Close | the Sell Report + the recommendation | `docs/SELL-IN-30.md` complete | graduation post |

### Composition rules

1. **Launch #4 ships by Day 5.** Nothing before it may slip it: if Define backfill or Checkout live runs long, Channel compresses to "the one place your believers already are".
2. **Checkout works before anyone is asked for money.** A real test purchase is Day 2's proof on every path, or Day 3 at the latest.
3. **Twenty real conversations before any pivot.** The pivot framework's own rule (fewer than ten demo posts is a patience problem) is enforced by the quota: the read on Day 14 may not choose a pivot variable unless the quota was met.
4. **One variable per week.** After a missed rung, the following week changes product, persona, or price, never two.
5. **Warm before cold, always.** Believers get every message first. Cold outreach starts only when the warm list is exhausted, and is logged as cold.
6. **A payment before Day 30 does not end the challenge (Q4).** It is logged, celebrated, the customer is asked for the testimonial, and the remaining days go to customers two and three with the same loop. Momentum is the Product Studio conversation.
7. **Hours/day** scale the quota and the fix blocks: `1h` halves the quota and drops Experiment; `4h+` doubles it and brings Activation into week two.

### Worked examples (ship in the skill as `plans/`)

**Live, free, never asked for money** · W1: D1 Define backfill + Price it · D2 Checkout live · D3 Believers backfill · D4 Channel · D5 **Launch #4** · D6 follow-ups · D7 read. W2: D8–D12 Conversations (quota) + Conversion path fixes · D13 follow-ups · D14 read. W3: D15 Founding offer · D16–D19 Conversations + Activation · D20 Second push · D21 read. W4: D22 Experiment · D23–D27 Conversations · D28 read · D29 Sell Report · D30 Close.

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
  plans/live-free.md
  plans/live-priced.md    worked examples the composer starts from
  plans/live-with-users.md
  plans/after-ship-in-7.md
  SELL-IN-30-TEMPLATE.md  the docs/SELL-IN-30.md skeleton
```

### Frontmatter

- `name`: `studio-sell-in-30` **(decided)**.
- `description` ≤ 1024 characters and bytes. Triggers: "sell in 30", "sell in thirty", "first customer in 30 days", "get my first customer", "first paying customer", "30 day challenge", "day 12 check-in", "weekly read", "what's my task today", "nobody has paid yet".

### Mode 1 — Enrol (Day 0, ~30 min)

1. **Setup check**; run `studio-setup` if needed **(decided)**.
2. **Prerequisite check:** is the product reachable? Not live → stop and route to `studio-ship-in-7` (Q1). `docs/SHIP-IN-7.md` open → close it first.
3. **Read the evidence:** live URL, price on the site, payments integration, `docs/LAUNCHES.md` and its rung, signups or usage the member reports (asked, never inferred from code), existing Define docs.
4. **Ask the starting point (decided: always ask).**
5. **Confirm the inputs:** start date, hours per day, the price if one exists, who they can already reach (the same two routing questions launch #1 asks).
6. **Compose the four weeks** and show the plan as a table: day, block, skill, proof, quota. The member edits before it's written.
7. **Write `docs/SELL-IN-30.md`:** header (dates, hours, the bar verbatim, starting point, price line), the plan table, empty daily log, weekly read slots, Skool post log.
8. **Draft the Day-0 Skool post** and name Day 1's literal task.

### Mode 2 — Daily check-in (Days 1–30)

Identical mechanics to Ship in 7 (day from the start date; confirm yesterday's proof first; log done/partial/missed; compression on misses; name today's one block; draft the Skool post; say what tomorrow looks like), plus:

- **Quota days** log the count against the quota and every reply verbatim. Silence is a count of zero, logged.
- **Every reply is answered the same day.** The check-in starts by asking about open threads.
- **Missed days compress within the week**, never across the Day-7 read: the read always happens on schedule, with whatever the week produced. Two consecutive misses halve the quota; they don't end the challenge.

### Mode 3 — Weekly read (Days 7, 14, 21, 28)

The `studio-launch` sitting-two ritual applied to the week, written into `docs/SELL-IN-30.md` and `docs/LAUNCHES.md`, and posted to Skool. Ends by naming next week's rung and, if a rung was missed twice, the one variable that changes.

### Mode 4 — Close (Day 30, or Day 31)

1. **Check the bar honestly:** a payment, or not. Partial outcomes (a signup, a "send me the link", an activated user) are logged on the ladder and named as what they are.
2. **Write the Sell Report:** result vs bar; conversations held, warm/cold; believers gained; the rung reached each week; what the market said in its own words; the variable changed, if any; the biggest blocker. *Written to be brought to a Product Studio call as-is.*
3. **Draft the graduation Skool post.**
4. **The recommendation (decided):** join Product Studio and book a call, once, framed by outcome. Paid → "you have a customer; a custom plan is how you get the next fifty." Not yet → "thirty days of real signal is exactly what a coach turns into the plan that works." Then what to run meanwhile: the Distribute loop (`studio-distribute-growth-experiments`) or the pivot framework.

### Failure patterns (named in SKILL.md)

The Friendly Echo (warm praise read as market signal) · The Rung Leap (one reply → "validated" → a silent week of building) · The Quota Dodge (posting instead of talking to people) · The Pitch-Slap · The Silent Zero · The Discount Spiral (dropping the price every time someone hesitates) · The Fresh-Start Reflex (a new channel every week) · The Feature Excuse ("they'll pay once I add X").

---

## 4. Daily accountability

Same two loops as Ship in 7 **(decided)**: the in-agent check-in, and one **new Skool post a day** with a house-format title and a body in the member's voice.

- **Title (Q6 to approve):** `Sell in 30 · Day 12/30 — [what happened, five words]`. Weekly reads: `Sell in 30 · Week 2 read — [rung reached]`. Day 30: `Sell in 30 · Sold — first customer` or `Sell in 30 · Day 30/30 — the honest read`.
- **Body:** first person, the number (conversations today, replies, the rung), one quote from the market if there was one, tomorrow's task. On quota days the number is the post.
- **Thirty posts is deliberate (Q5):** daily accountability is the mechanism, and a community feed of members counting conversations is the culture. If it's too much, the fallback is a daily check-in with a Skool post on quota days and read days only.

---

## 5. System changes, build sequence

Specified once in `ship-in-7-skill-plan.md` §5–§6 and shared. Sell-in-30-specific additions:

- `skills/studio-distribute-gtm-strategy/SKILL.md` and `studio-distribute-growth-experiments/SKILL.md`: one line each, reading `docs/SELL-IN-30.md` when open so the plan fits the remaining days.
- `distribute/DISTRIBUTE-CHECKLIST.md`: the preamble line pointing challenge members at their open challenge file.
- Fixture repos for the dry-run: a live Next.js app with no pricing; the same with Stripe in test mode and a price page; the same with fake signups seeded; a repo with a closed `docs/SHIP-IN-7.md`.

---

## 6. Open questions

Carried forward as decided: `studio-` prefix · setup first if missing · bar is one payment · always ask the starting point · Skool: new post per day, house-format title, member's voice · Product Studio + book a call at the close.

1. **Not-live members.** Refuse and route to Ship in 7 (default), or allow enrol with "go live" as Days 1–2 for members who are one deploy away?
2. **Free products.** Always price it in week one (default, since the bar is a payment), or let a member run the challenge for a free product with an activated user as the bar? (Your earlier answer says a payment; confirming it holds when the product is currently free.)
3. **The conversation quota.** Five new real conversations a day from Day 8 (default), a weekly number, or none?
4. **Payment before Day 30.** Keep going for customers two and three (default), or close early with the report and the recommendation while the win is fresh?
5. **Post cadence.** Daily for 30 days (default), or daily check-ins with posts on quota and read days only?
6. **Skool title format.** Approve `Sell in 30 · Day N/30 — [what happened]` and `Sell in 30 · Week N read — [rung]`, or give me the pattern.
7. **The Product Studio CTA.** Same as Ship in 7 Q6: link, pitch line, and whether the graduation post carries it. For Sell in 30 the lead-in is strongest; do you want the Sell Report to double as the pre-call form (default: yes, it ends with "bring this to your call")?
8. **Cold outreach.** In scope once the warm list is exhausted (default), or keep the challenge to warm channels and the one primary channel from the GTM plan?
9. **Founding offer mechanics.** Should the skill carry a house founding-offer pattern (seat cap, price rise date, guarantee), or draft it from the member's pricing anchors each time (default)?
10. **Existing material.** A Sell in 30 doc, Skool post, or script to mirror? Drop it in `_private/`.
11. **Must-nots.** Never send messages on the member's behalf, never change live prices without confirmation, never touch production data? Anything else?

---

## 7. Risks

1. **Thirty days of daily posts is a lot of surface for drop-off.** Mitigation: the check-in is five minutes, the post is drafted, misses are posted rather than hidden, and the weekly read gives a natural re-entry.
2. **The bar is out of the member's control.** Payment depends on the market. Mitigation: the ladder records every partial rung, the read is honest, and the close's recommendation is framed for both outcomes.
3. **Price changes on a live product.** Mitigation: Checkout live and any price change are confirmed with the member, never automated; the golive payments guidance is reused, not reinvented.
4. **Cold outreach etiquette.** Community rules and platform norms. Mitigation: the launch skill's Pitch-Slap rule and "check the community's self-promotion rules" carry over; cold sends are always logged as cold.
5. **Duplicated loop mechanics with Ship in 7.** See the sibling plan's Q10.
