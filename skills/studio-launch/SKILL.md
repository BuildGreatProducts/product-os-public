---
name: studio-launch
description: >-
  Use at each phase's launch moment — the recurring ritual that puts the product in front of real potential customers and logs the signal. Four launches, one ladder: the Mini-Launch (Define — win: one reply), "here's what it looks like" (Design — win: one signup or "can I try it?"), the beta invite (Develop — win: one activated user), the public launch (Distribute — win: first payment). Triggers on phrases like "mini-launch", "mini launch", "relaunch", "launch post", "beta invite", "get my first signal", "put my offer in front of people", "write my launch post", "draft my DM", "ship the ask", "invite my believers", "message the people who replied", or any request to draft, ship, and log an outreach moment based on the ProductOS documents. Reads docs/LAUNCHES.md (and docs/PLAN.md's launches-remaining, when present) to know which launch this is, drafts 2–3 message variants in the persona's language, ships within 48 hours, then logs every response and grows the believers list. Closes each phase.
---

# Launch

This skill runs ProductOS's recurring launch ritual — the same motion at four moments across the program, each climbing one rung of the **signal ladder**:

| # | Launch | Phase | What ships | The win (pass bar) |
| --- | --- | --- | --- | --- |
| 1 | **Mini-Launch** | Define | The offer, in the persona's words | One reply |
| 2 | **"Here's what it looks like"** | Design | The landing-page draft, identity, or magic-moment mockup | One "can I try it?" or signup |
| 3 | **The beta invite** | Develop | The working MVP, into believers' hands | One activated user (reaches the magic moment) |
| 4 | **The public launch** | Distribute | The live product, announced on the primary channel | First payment |

The mechanics never change — that's the point. **Draft from your docs → ship within 48 hours → share a screenshot of the live post or sent message with your cohort → log every response.** (In the Product Studio, "your cohort" is your programme group; working solo, share it with an accountability partner or post it publicly — any witness keeps the bar honest.) By launch #4 the user isn't nervously shipping their first ask; they're a founder who launches routinely, to an audience that has watched the product grow since it was a paragraph.

Two threads carry between launches:

1. **The believers list.** Everyone who ever responds gets a name on the list in `docs/LAUNCHES.md`. Launch #1's replier is launch #2's preview reader, launch #3's beta user, and launch #4's first customer and testimonial. Every launch goes to the believers *first*, then to the wider channel — warm before cold, always.
2. **The same channel, by default.** Relaunches return to the thread that worked — same community, same feed, ideally the same literal thread ("update on the thing I posted about in March…"). Attention compounds only if it accumulates in one place. Pick a new channel only if the last one was silent after a full send and one rewrite.

And one rule keeps the ladder honest: **each rung is a target that triggers a conversation, not a gate.** Missing a rung once means rewrite and resend. Missing the same rung twice is a signal worth respecting — open `productos/define/BONUS - Pivot Framework.md`, and if the user is in a cohort, this is the moment to talk to their coach. Nobody stalls out of the program for missing a rung; they course-correct because of it.

> **Session shape:** Every launch is two sittings. **Sitting one (20–30 min): arm and ship** — route, draft, commit a send time inside 48 hours. **Sitting two: log and read** — confirm proof, log every response, read the signal, name the next rung. Do not let sitting one end without a committed send time, and do not let "one more polish pass" move it.

## First: which launch is this?

Read **`docs/LAUNCHES.md`**. If it doesn't exist, this is **launch #1 — the Mini-Launch** (see its dedicated worksheet below). If it exists, the number of completed entries tells you which relaunch this is; the believers list and previous entries tell you who to contact and where. Confirm with the user — they may be re-running a launch that missed its rung, which is a resend, not a new entry.

**One exception:** if **`docs/PLAN.md`** exists (the programme plan, shipped with coached copies of ProductOS), its *Launches remaining* section overrides the count — a member with an existing product may have earned rungs before joining, so their first ProductOS launch might be #2, #3, or #4. In that case, create `docs/LAUNCHES.md` now and backfill it: the signal they already have as dated entries, everyone who has ever responded onto the believers list, then run the launch the plan names next.

## Inputs

Locate in the ProductOS folder (`productos/` at the app repo root, or the current folder in a standalone checkout) and the repo-root `docs/`. Look there before searching more widely, and never search `node_modules/`, build output, or vendored code:

1. **The Product Offer** — `productos/define/1. Product Offer.md`. **Required.** The outcome and pitch every message is built from.
2. **The Customer Persona** — `productos/define/2. Customer Persona.md`. **Required.** The pain language the message opens with and the watering holes that decide where it ships.
3. **The Pricing Strategy** — `productos/define/3. Pricing Strategy.md`. **Required.** The price line. If empty, run `studio-define-pricing` first — it's a 20-minute session.
4. **The Launch Log** — `docs/LAUNCHES.md`, if it exists. The believers list and every previous entry. Created by this skill at the end of launch #1.
5. **The Mini-Launch worksheet** — `productos/define/4. Mini-Launch.md`. Launch #1's worksheet; the skill fills it in place (sections 1–2 in sitting one, 3–6 in sitting two).
6. **Phase payloads, per launch:** #2 reads `productos/design/4a. Landing Page.md` (or `4b. App Store Listing.md`), `productos/design/1. Product Identity.md`, and `productos/design/2. Magic Moment.md` for the "look what it looks like" material. #3 reads `docs/DEPLOY.md` (or wherever the app's URL/TestFlight link lives) and `productos/design/2. Magic Moment.md` — activation is defined there. #4 reads `productos/distribute/1. Go-To-Market Strategy.md` for the primary channel and `docs/PRODUCT.md` for the story.

## Workflow — Sitting one: arm and ship

### 1. Route the launch

**Launch #1** routes off two questions — **"Who can you already reach?"** and **"What exists of the product so far?"** — always picking the warmest channel the user actually has:

| Access | Route | The ask |
| --- | --- | --- |
| Clients / network matching the persona | **The DM Ask** | Personal message to 5–10 named people |
| A named community where the persona congregates | **The Community Post** | "I'm building X for Y because Z — does this resonate? What am I missing?" |
| An active social feed — or a half-built product with screenshots | **The Build-in-Public Post** | "Here's what I'm building and why" + screenshot |
| Any of the above, plus an hour spare | **The One-Pager** *(optional upgrade)* | One-page site + email box, shared via one of the routes above |

Half-built products are an advantage — a screenshot of something real is more credible than an idea. The zero-network user takes the Community Post, and if they can't name the community, that's a persona gap: fix the watering holes in `2. Customer Persona.md` first, and check the community's self-promotion rules. DM lists must be *named* — eight actual people, not "some old clients."

**Launches #2–4** route themselves: believers first (personal messages — they replied last time, they get the update before anyone), then the same channel as the previous launch, as a continuation of the same thread where the platform allows it. Ask only one routing question: *"Anything changed about who you can reach since last time?"*

### 2. Draft 2–3 message variants

Draft *for* the user — they edit, they don't face a blank page. Every variant, every launch:

- **Opens with the pain in the persona's verbatim language** — from `2. Customer Persona.md`, not founder-speak.
- **Shows the new thing** — launch #1 the offer, #2 the screenshot/preview link, #3 the "you can use it now" link, #4 the live product.
- **Ends with one question that invites a reply** — "Does this match your experience?" / "Can I show you?" / "Want an invite?" / "Would this be worth $X to you?"
- **Carries the price line if the user is willing** — optional but recommend it plainly: a priced message converts "sounds cool" into "I'd pay for that." By launch #4 the price isn't a line in a post — it's a checkout link. If the user declines earlier, don't relitigate; note it in the log so the signal is read accordingly.
- **References the thread, from #2 onward** — "a few months ago I posted about X — here's where it is now" is the strongest opener a relaunch has.
- **Sounds like a person.** DMs read like messages to that named individual; community posts follow the community's register.

### 3. Commit the ship time

Fill the pre-ship half of the record (launch #1: sections 1–2 of `productos/define/4. Mini-Launch.md`; relaunches: a new draft entry in `docs/LAUNCHES.md`). Get a **committed send time inside 48 hours** — ideally today. The post is where perfectionism hides; name it if you see it forming. End sitting one stating exactly what returning looks like: *ship it, screenshot the live post or sent DM, share the screenshot with your cohort, come back and log what happened.*

## Workflow — Sitting two: log and read

### 4. Confirm proof

First question: **"Did it ship? Show me."** Proof is the screenshot of the **live** artifact — timestamp visible — shared with the cohort the day it shipped. Not a draft. If it didn't ship, don't scold and don't re-polish: shrink the ask (fewer DMs, warmest single channel) and get a new send time inside 24 hours.

### 5. Log every response — including silence

Who, what they said, **warm or cold** (warm = they know the user), date, and the ladder rung reached: `reply → real conversation → signup → activated user → payment`. Friend replies count but get labelled. Silence gets logged too — "0 replies, 10 DMs, 3 days" is an entry, not an absence. **Add every new responder to the believers list** with where they came from and what they said.

### 6. Read the signal and set the next rung

- **Rung hit** — the win. Say so plainly, mark it in the log, and name the next rung and roughly when it comes (the next phase's launch). Anyone who leaned in gets a follow-up action *now*: "can I try it?" is a name for the beta list; a payment question is a checkout link to send.
- **Harvest the words.** Verbatim replies go back into `2. Customer Persona.md` (pain language) and forward into `docs/PRODUCT.md`'s Proof section when it's next synthesized.
- **Rung missed** — one rewrite (different hook, toggle the price), one resend through the next-warmest route. Log the miss honestly.
- **Same rung missed twice** — stop relaunching and read `productos/define/BONUS - Pivot Framework.md`: is it the product, the persona, or the price? In a cohort, this is a coach conversation, not a private shame spiral. The ladder's job is to surface this in weeks, not months.

### 7. Update the Launch Log

Create or update **`docs/LAUNCHES.md`** (create `docs/` if needed). Structure:

```markdown
# Launch Log

**The ladder:** reply → conversation → signup → activated user → payment
**Current rung:** [highest rung reached, dated]
**Next launch:** [#N — phase — target rung]

## Believers
| Name | Source | First responded | Latest status |
| --- | --- | --- | --- |

## Launch #1 — Mini-Launch (Define) — [date]
Channel · message summary · proof link · signal summary · rung reached · pass bar met? Y/N
[one entry per launch, newest last]
```

Launch #1 additionally lives in full in `productos/define/4. Mini-Launch.md`; the log entry is its dated summary. Relaunches log here directly. This file is the program's momentum record — a coach or co-founder should read it in one minute and know exactly how much market contact the product has had.

## Failure patterns to look for

- **The Polish Loop.** Draft "nearly ready" for days. The 48-hour timebox and a committed send time are the cure.
- **The Pitch-Slap.** A community post that's an ad with a question mark. Genuine request for input, community's register, rules checked.
- **The Founder-Voice Message.** Features instead of the persona's pain language. If the first line could open a press release, rewrite it.
- **The Friendly Echo.** Only warm sends, warm praise read as market signal. Warm replies are the *win*, not the *evidence* — the label keeps it honest.
- **The Rung Leap.** One good reply → "validated!" → six weeks of silent building. The ladder exists so contact never lapses for a whole phase; the next launch is always named and dated.
- **The Silent Zero.** No replies, nothing logged, momentum lost to quiet shame. Zero is an entry. Log it, rewrite once, resend warmer.
- **The Draft-as-Proof.** Sharing the unsent draft with the cohort for feedback instead of the live artifact. The community sees shipped things only.
- **The Fresh-Start Reflex.** Relaunching to a brand-new channel while the old thread had warm believers in it. New channels are for silence, not for stage fright.

## Tone and pacing

- **Coach at the moment of fear.** Every launch is scary the first time. Keep the bar visibly low — "one reply, that's the whole win" — and treat shipping itself as the achievement.
- **Draft for them, decide with them.** Blank pages kill launches.
- **Celebrate the rung, then anchor it.** When the reply / signup / activation / payment lands, mark the moment — and in the same breath file it on the ladder and name the next rung. Momentum comes from the *next* target being visible.
- **Never shame a zero.** A shipped ask with no replies beats an unshipped perfect one, every time.

## What "done" looks like

For any single launch: the message went to believers first and the warmest channel second, in the persona's language, with one question and (ideally) a price; it shipped inside the 48-hour window; the live-artifact screenshot went to the cohort the same day; every response — including silence — is in the log, warm/cold labelled, with new believers added; and the entry in `docs/LAUNCHES.md` names the rung reached and the next target.

For the program: four dated entries, a believers list that grew at every rung, and a founder who has launched four times in 60 days — for whom the fifth launch is just what happens next.
