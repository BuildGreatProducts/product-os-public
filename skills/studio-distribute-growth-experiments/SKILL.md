---
name: studio-distribute-growth-experiments
description: Use after the user has a go-to-market plan (or live channels) and wants to systematically improve and scale them. Triggers on phrases like "growth experiments", "growth plan", "growth backlog", "what should I test", "how do I scale this channel", "marketing experiments", "improve my channel", "A/B test ideas", "growth loop", or "optimize my funnel". Reads the Go-To-Market Strategy doc (or, in a repo without ProductOS, the codebase plus a couple of questions) for the chosen channels, researches current tactics and competitor distribution for the niche, then designs product-specific experiments and writes a simple execution list — 1–3 experiments running now, each with concrete steps and a number-plus-date pass bar, plus an ordered up-next queue — and seeds a running results tracker. Prioritization (effort/impact, quick wins first) happens in the session; only the instructions land in the file. Works with ProductOS in the repo (productos/ at the app repo root) or standalone in a repo without it.
---

# Distribute: Growth Experiments

This skill turns the channels a user has already chosen into a **prioritized backlog of growth experiments** — small, falsifiable bets that make a working channel work harder — plus a **running tracker** where results and learnings accumulate. It reads the Go-To-Market Strategy (the chosen channels and their pass thresholds), researches what's working right now in the niche, and walks the user through selecting, designing, and scheduling a tight cycle of experiments for one focus channel at a time.

The goal is not to produce a list of generic growth tips. It is to produce **specific, falsifiable bets**: each experiment names what changes, what's expected to move, the number that means it worked, and the simple steps to run it this week. "Make better videos" is noise. "Five hook variations leading with the customer's pain, one a day; a winner clears 50% three-second retention" is an experiment. The whole value of this skill is the distance between those two sentences.

This is the loop that runs *after* the first 30 days. `productos/distribute/1. Go-To-Market Strategy.md` picks the channels and gets the user started; this skill is the repeatable engine for month two and beyond — hypothesis, run small, measure against a threshold, decide (double down / iterate / kill), and log. The most common ways it fails are chasing vanity metrics, running too many experiments at once, designing experiments with no threshold, writing them too generic to act on, and never logging results so nothing compounds. The workflow below is built to prevent all five.

> **Session length:** Designed to be completable in 45–60 minutes. **All tactic research is Claude's job during the session** — finding what's working now in the niche and tearing down how competitors currently distribute. The user reacts and supplies the baseline number, the tools/analytics they have, and their weekly time budget. The skill plans **one focus channel's** cycle (one to three experiments) per run, not all channels at once.

## Inputs

This skill needs **channel context** (which channels the user is running and what "working" means for each), **product context** (so experiments are specific), an **output target**, and the **experiments playbook**. Channel and product context come one of two ways depending on where the skill runs — the rest of the workflow is identical.

### Channel context — Path A (standard): ProductOS in the repo — `productos/` at the app repo root, or the current folder in a standalone ProductOS checkout

1. **The Go-To-Market Strategy** — usually `productos/distribute/1. Go-To-Market Strategy.md`. The **primary** input: the ranked channels, their starter plans, and their pass thresholds. The focus channel defaults to the GTM doc's **primary** channel. If this file doesn't exist, the user hasn't picked channels yet — offer to run `studio-distribute-gtm-strategy` first, or establish the channels via the Path B questions.
2. **The product summary** — usually `docs/PRODUCT.md` (or the Define docs). Provides the customer, their language, the magic moment, and the north star, so experiment hypotheses are product-specific and metrics ladder to the right number.

### Channel context — Path B (standalone fallback): a repo without ProductOS

When there's no ProductOS work — the skill runs inside a normal app repo — read the **codebase** for product context (README, manifests, landing/marketing copy, pricing config, routes/features) exactly as the GTM skill does. Then ask the user the few things code can't reveal:

- **Which channels are you running now**, and which one do you want to focus on?
- **The baseline** — the current number for the metric this channel should move (signups/week, trials, installs, cost-per-acquisition).
- **Tools & analytics** — what can you actually measure with (analytics, UTMs, ad dashboards)?
- **Time budget** — hours a week you can spend running experiments.

Ask only what the repo didn't answer, one at a time.

### Output target (both paths)

- **`productos/distribute/2. Growth Experiments.md`** — the execution list: the metric header, Running now (1–3 experiments), and the ordered Up next queue. On the standard path it exists as a template — **rewrite it in place**. On the standalone fallback, create it fresh with the same structure at `docs/growth-experiments.md`.
- **`productos/distribute/3. Growth Experiments Tracker.md`** — the running results log. **Seed it** with this cycle's planned experiments as pending rows so the user only has to fill in results. In a codebase, create `docs/growth-experiments-tracker.md`.

### Experiments playbook (both paths)

Four reference docs ship **inside this skill's folder**, so they're available in both paths. Read them at the start:

- **`BONUS - Growth Experiments Library.md` (in this skill's folder)** — the **primary** playbook: the method (the loop, effort/impact prioritization, cadence, what counts as a result), the card format, and a few named experiments per channel with real examples. Every experiment you propose should be a tailored version of one from here (or built in the same shape).
- **`BONUS - Measurement & Attribution.md` (in this skill's folder)** — how to measure each experiment's result and attribute it to the right channel, so every pass threshold is a real, readable number. Name a measurement method for every threshold before the experiment runs.
- **`BONUS - Distribution Channels.md` (in this skill's folder)** and **`BONUS - AI Distribution Tools.md` (in this skill's folder)** — channel logic and the tool to run each.

The same files also live in `productos/distribute/`; prefer the user's copies if customized. The bundled copies guarantee the skill has its playbook when run standalone.

## Workflow

### 1. Absorb context and set the focus

Read the GTM doc (or establish channels via Path B) plus the product context. Pick the **focus channel** — default to the GTM primary, unless the user names another. Then nail down the **baseline and target**: the one metric this channel should move, the number today, and a realistic target with a date. The metric must ladder to the north star — signups, trials, paying users, booked calls, cost-per-acquisition — never views or followers. State the focus + baseline back to the user before researching.

### 2. Research what's working now (always)

The library gives the *shape* of each experiment; research makes each one *specific and current*. Use web search and any connected tools to:

- **Find live tactics** for the focus channel in this exact niche — the hooks, formats, keywords, offers, posting cadences, and angles that are working right now (these decay fast, so don't rely on the library's examples alone).
- **Tear down competitor distribution** — take 3–5 competitors and look at what they're currently doing on this channel: their best-performing content, their listings, their landing pages, their offers. This shows both what works and what's already saturated.

Bring back concrete, named specifics to seed the experiment designs.

### 3. Build and prioritize the backlog

From the library's experiments for the focus channel (plus anything the research surfaced), draft a backlog of candidates **tailored to this product**. Rate each on **Effort** (Low/Med/High) and **Impact** (Low/Med/High) and order them: ⭐ quick wins first (high impact, low effort), then big bets one at a time, filler only when blocked, skip the high-effort/low-impact. Walk the user through the ranking; never let a high-effort/low-impact experiment rise to the top. **The ratings are session material, not output** — the file gets only the resulting order (Up next), never the effort/impact columns or the priority guide.

### 4. Design this cycle's experiments (the cards)

Pick the top **one to three** to run now. For each, write the full card and hold it to the specificity test — if a step would read the same for a different product, rewrite it:

- **One plain sentence** — what we're testing and why it should move the metric, in the customer's own language (this is the hypothesis, without the framework wrapper).
- **Do this** — 2–4 concrete, sequential steps to start it this week, so plain the user can follow them without guessing (this is the part students act on).
- **Pass =** — a **number + a date** that ladders to the north star, followed in the same line by the specific next move on pass and the specific next move on fail (this is the decision rule, stated as instructions).

### 5. Write the worksheet and seed the tracker

**On the standard path, rewrite `productos/distribute/2. Growth Experiments.md` in place**; on the standalone fallback, create `docs/growth-experiments.md` with the identical structure. Match the template exactly: the two header lines (**Moving** — metric, baseline, target, date; **Rhythm** — max concurrent, review day, tracker pointer), **Running now** (1–3 experiment blocks: the plain sentence, the "Do this" checklist, the Pass = line), and **Up next** (the remaining candidates as an ordered one-line list). Read the existing file first to preserve any notes.

**The output rule — the document is execution-only.** No effort/impact ratings, no priority guide, no backlog table, no `> Good/Bad` examples, no decision-rule boilerplate — only this member's specific experiments and the order to run them. All method lives in this skill and the BONUS library; if a sentence teaches instead of instructs, cut it. Scale/kill outcomes are recorded in the Tracker, never duplicated here.

Then **seed `productos/distribute/3. Growth Experiments Tracker.md`** (or `docs/growth-experiments-tracker.md`): add this cycle's experiments as rows with their pass thresholds filled in and the result/learning/decision columns left blank, so the user just records outcomes as they finish. Don't overwrite existing log rows — append.

Date the title line, and fill the one-line *Based on:* footer naming the inputs and research used — no separate summary or Sources section; the two header lines are the summary.

### 6. Verify before delivering

Re-read both files and check:

- Is there **one focus channel** and **no more than three** experiments this cycle?
- Does every experiment have a **hypothesis**, a **number-plus-date pass threshold**, and **simple next steps** the user could start tomorrow?
- Is every experiment specific to **this** product — would it read differently for another?
- Is **Up next** ordered quick-wins-first (from the session's ratings), with no high-effort/low-impact experiment near the top — and no ratings, tables, or guidance text anywhere in the file?
- Does every metric ladder to the **north star**, not a vanity number?
- Is the tracker **seeded** with this cycle's experiments as pending rows?

Deliver both files via `computer://` links and a one-paragraph summary: the focus channel, the first experiment to run this week, and the number that means it worked.

## Failure patterns to look for

Name them when you see them — naming compounds learning:

- **The Vanity Experiment.** The "win" is views, likes, or followers. Redesign until the pass threshold is revenue-shaped (signups, trials, paying users, booked calls, cost-per-acquisition).
- **Too Many in Flight.** More than three experiments, or more than one channel, at once. You can't read which change moved the number. Cap it at three on one channel.
- **The Thresholdless Test.** An experiment with no number and no date. That's an activity, not an experiment. Force "Pass = X by Y."
- **The Generic Experiment.** Steps that fit any product — "post more," "improve SEO," "run ads." Rewrite until each step could only be this product's, in this customer's words.
- **The Big-Bet-First Trap.** Reaching for a high-effort experiment while quick wins sit untouched. Clear the high-impact/low-effort wins first, every time.
- **The Unlogged Result.** Running experiments but never recording outcomes, so nothing compounds. The tracker is not optional — it's the asset that makes the next cycle smarter.
- **Optimizing a Dead Channel.** Pouring experiments into a channel that fundamentally isn't reaching buyers. If the channel can't clear its threshold after honest reps, the problem is channel choice — return to `productos/distribute/1. Go-To-Market Strategy.md`, don't keep experimenting.

## Tone and pacing

- **Conversational, not a form.** The user is deciding how to spend the next two weeks; treat them like a peer, ask one question at a time.
- **Do the research so they don't have to.** Current tactics and competitor teardowns are Claude's job in-session.
- **Push back on vague and on greedy.** A generic experiment and a five-experiment cycle are both failures — name the pattern and sharpen.
- **Force the number and the next step.** Every experiment needs a pass threshold and next steps a non-technical founder could start tomorrow.
- **One focus channel per cycle.** Resist planning all channels at once; depth beats breadth.

## What "done" looks like

A filled `productos/distribute/2. Growth Experiments.md` (or `docs/growth-experiments.md`) and a seeded `productos/distribute/3. Growth Experiments Tracker.md` where:

- The **Moving** line names one channel, one north-star-linked metric, the current number, and a target with a date; the **Rhythm** line caps concurrent experiments and sets the review day.
- **Running now** holds one to three experiments, each a plain sentence + a "Do this" checklist startable this week + a Pass = line with a number, a date, and the specific moves on pass and fail.
- **Up next** is an ordered one-line-each queue — quick wins first, no ratings shown.
- The **Tracker** is seeded with this cycle's experiments as pending rows; scale/kill outcomes live there, not in the experiments file.
- **Nothing in the file teaches** — no frameworks, tables, or calibration examples. A reader could start experiment 1 tomorrow from this file alone; the title line is dated and the *Based on:* footer names the inputs.

A plan the user can act on **this week** — run the top experiment, hit or miss its threshold, log the result. Anything vaguer is a draft; name the gap and sharpen it.

Recommended next step after a successful session: run the cycle's quick win first, log every result in the Tracker, and re-run this skill each cycle. When the focus channel hits its target and plateaus, return to `productos/distribute/1. Go-To-Market Strategy.md` and bring the next channel online.
