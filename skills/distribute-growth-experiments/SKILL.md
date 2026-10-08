---
name: distribute-growth-experiments
description: >-
  Designs 1–3 product-specific growth experiments for the channels already chosen, each with
  concrete steps and a number-plus-date pass bar, plus an ordered queue; writes
  docs/GROWTH-EXPERIMENTS.md and seeds the results tracker docs/GROWTH-TRACKER.md. Use after a
  go-to-market plan exists, when the user asks "what should I test", "growth experiments", or
  "improve my channel". Not for choosing channels — use distribute-gtm-strategy; not for scaling
  proven winners — use distribute-scale-automate.
---

# Distribute: Growth Experiments

Turn the channels the member already chose into a prioritized cycle of growth experiments — small, falsifiable bets that make a working channel work harder — written to `docs/GROWTH-EXPERIMENTS.md`, with results logged in `docs/GROWTH-TRACKER.md`. "Make better videos" is noise. "Five hook variations leading with the customer's pain, one a day; a winner clears 50% three-second retention" is an experiment. Every experiment names what changes, what's expected to move, the number that means it worked, and the simple steps to run it this week. It's the repeatable engine for month two and beyond, after `docs/GO-TO-MARKET.md` gets the member started. Plan **one focus channel's** cycle (one to three experiments) per run, not all channels at once.

## Inputs

> **Inside a challenge:** if `docs/SELL-IN-30.md` is open, read its header and Experiment Log first. The bar (a payment, or an activated user) and the clock (three experiment-weeks) override the month-two framing: rank the backlog by *closest to the bar inside one week*, size every experiment to one week with a Pass = line the member can read on the week's seventh session, split anything bigger into the up-next queue, and treat the Experiment Log's rows and verbatims as the baseline. In challenge mode **Running now holds exactly one experiment**, the top-ranked; every other candidate goes to Up next, so the week runs one experiment and the seventh-session read decides on one.

The skill needs **channel context**, **product context** (so experiments are specific), an **output target**, and the **experiments playbook**. Channel and product context come one of two ways; the rest of the workflow is identical.

### Channel context — Path A (standard): ProductOS in the repo — `productos/` at the app repo root, or the current folder in a standalone ProductOS checkout

1. **The Go-To-Market Strategy** — `docs/GO-TO-MARKET.md`. The **primary** input: the ranked channels, their starter plans, and their pass thresholds. The focus channel defaults to its **primary** channel. If this file doesn't exist, the member hasn't picked channels yet — offer to run `distribute-gtm-strategy` first, or establish the channels via the Path B questions.
2. **The product context** — `docs/DEFINE.md` (the Summary, the Offer's Customer, the Persona's language, and Business Strategy → North Star when filled) and `docs/MAGIC-MOMENT.md` if it exists — so hypotheses are product-specific and metrics ladder to the right number.

### Channel context — Path B (standalone fallback): a repo without ProductOS

Read the **codebase** for product context (README, manifests, landing/marketing copy, pricing config, routes/features). Then ask only what the repo didn't answer, one question at a time:

- **Which channels are you running now**, and which one do you want to focus on?
- **The baseline** — the current number for the metric this channel should move (signups/week, trials, installs, cost-per-acquisition).
- **Tools & analytics** — what can you actually measure with (analytics, UTMs, ad dashboards)?
- **Time budget** — hours a week you can spend running experiments.

### Output target (both paths)

Both files land in the repo-root `docs/` folder (create it if needed). Never write answers back into `productos/`.

- **`docs/GROWTH-EXPERIMENTS.md`** — the execution list: the metric header, Running now (1–3 experiments), and the ordered Up next queue. On Path A the worksheet `productos/distribute/2-Growth-Experiments.md` gives its structure; on Path B, use the structure in step 5.
- **`docs/GROWTH-TRACKER.md`** — the running results log, structured like the worksheet `productos/distribute/3-Growth-Experiments-Tracker.md`: the log table (Date · Experiment · Channel · Pass threshold · Result · Pass? · Learning · Decision, newest first), then Cumulative Learnings. On Path B, use that structure. Two columns take fixed values, because `distribute-scale-automate` gates on them: **Pass?** is `Pass` or `Fail`; **Decision** is `double down`, `iterate`, or `kill`.

### Experiments playbook (both paths)

Four reference docs live in ProductOS's `distribute/` folder, two levels up from this skill's folder (`../../distribute/`) — the same files whether ProductOS sits in the repo as `productos/` or is installed as a plugin. Read only the parts named here — the full set is long:

- **[BONUS-Growth-Experiments-Library.md](../../distribute/BONUS-Growth-Experiments-Library.md)** — the **primary** playbook. At step 1, read *The method* and *How to read a card*; once the focus channel is set, read only that channel's numbered section. Every experiment you propose is a tailored version of one from there (or built in the same shape).
- **[BONUS-Measurement-and-Attribution.md](../../distribute/BONUS-Measurement-and-Attribution.md)** — read it when writing the Pass = lines (step 4): name a measurement method for every threshold before the experiment runs, so each result is a real, readable number.
- **[BONUS-Distribution-Channels.md](../../distribute/BONUS-Distribution-Channels.md)** and **[BONUS-AI-Distribution-Tools.md](../../distribute/BONUS-AI-Distribution-Tools.md)** — channel logic and the tool to run each; read only the focus channel's section, when you need it.

## Workflow

### 1. Absorb context and set the focus

Read the GTM doc (or establish channels via Path B) plus the product context. Pick the **focus channel** — default to the GTM primary, unless the member names another. Then nail down the **baseline and target**: the one metric this channel should move, the number today, and a realistic target with a date. The metric must ladder to the north star — signups, trials, paying users, booked calls, cost-per-acquisition — never views or followers. State the focus + baseline back to the member before researching.

### 2. Research what's working (always)

The library gives the *shape* of each experiment; research makes each one *specific and current*. All tactic research is your job in the session — the member supplies the baseline, their tools, and their time. Use web search and any connected tools to:

- **Find live tactics** for the focus channel in this exact niche — the hooks, formats, keywords, offers, posting cadences, and angles working now (these decay fast, so don't rely on the library's examples alone).
- **Tear down competitor distribution** — take 3–5 competitors and look at what they're currently doing on this channel: their best-performing content, their listings, their landing pages, their offers. This shows both what works and what's already saturated.

If web search isn't available, say so, ask the member for the competitors and examples they know, and mark those claims unverified. Bring back concrete, named specifics to seed the experiment designs.

### 3. Build and prioritize the backlog

From the library's experiments for the focus channel (plus anything the research surfaced), draft a backlog of candidates **tailored to this product**. Rate each on **Effort** (Low/Med/High) and **Impact** (Low/Med/High) and order them: ⭐ quick wins first (high impact, low effort), then big bets one at a time, filler only when blocked, skip the high-effort/low-impact. Walk the member through the ranking one question at a time; never let a high-effort/low-impact experiment rise to the top, and push back on a cycle of more than three. **The ratings are session material, not output** — the file gets only the resulting order (Up next), never the effort/impact columns or the priority guide.

### 4. Design this cycle's experiments (the cards)

Pick the top **one to three** to run now. For each, write the card and hold it to the specificity test — if a step would read the same for a different product, rewrite it:

- **One plain sentence** — what we're testing and why it should move the metric, in the customer's own language (the hypothesis, without the framework wrapper).
- **Do this** — 2–4 concrete, sequential steps to start it this week, so plain the member can follow them without guessing (this is the part the member acts on).
- **Pass =** — a **number + a date** that ladders to the north star, followed in the same line by the specific next move on pass and the specific next move on fail (the decision rule, stated as instructions). Name how the number will be measured.

### 5. Write the worksheet and seed the tracker

**Write `docs/GROWTH-EXPERIMENTS.md`** using the worksheet's structure (on Path B, this same structure): the two header lines (**Moving** — metric, baseline, target, date; **Rhythm** — max concurrent, review day, pointer to `docs/GROWTH-TRACKER.md`), **Running now** (1–3 experiment blocks: the plain sentence, the "Do this" checklist, the Pass = line), and **Up next** (the remaining candidates as an ordered one-line list); drop the worksheet's italic intro line. If the file already exists, read it first, preserve the member's edits, show a diff, and get approval before overwriting.

**The document is execution-only.** No effort/impact ratings, no priority guide, no backlog table, no `> Good/Bad` examples, no decision-rule boilerplate — only this member's specific experiments and the order to run them. If a sentence teaches instead of instructs, cut it. Scale/kill outcomes are recorded in the Tracker, never duplicated here.

Then **seed `docs/GROWTH-TRACKER.md`**: if it doesn't exist, create it from the worksheet's structure without the example rows and italic prompts; add this cycle's experiments as rows with their pass thresholds filled in and Result, Pass?, Learning and Decision left blank, so the member just records outcomes (using the fixed Pass? and Decision values above) as they finish. Don't overwrite existing log rows — append.

Date the title line, and fill the one-line *Based on:* footer naming the inputs and research used — no separate summary or Sources section; the two header lines are the summary.

### 6. Verify before delivering

Re-read both files against the failure patterns below:

- [ ] **One focus channel** and **no more than three** experiments this cycle (exactly one in challenge mode).
- [ ] The **Moving** line names one channel, one north-star-linked metric, the current number, and a target with a date; the **Rhythm** line caps concurrent experiments and sets the review day.
- [ ] Every experiment has a plain-sentence hypothesis, a "Do this" list the member could start tomorrow, and a Pass = line with a **number + date** and the specific moves on pass and fail.
- [ ] Every experiment is specific to **this** product — it would read differently for another.
- [ ] Every metric ladders to the **north star**, not a vanity number.
- [ ] **Up next** is an ordered one-line-each queue, quick wins first, with no high-effort/low-impact experiment near the top — and no ratings, tables, or guidance text anywhere in the file.
- [ ] The tracker is **seeded** with this cycle's experiments as pending rows; scale/kill outcomes live there, not in the experiments file.
- [ ] The title line is dated and the *Based on:* footer names the inputs. A reader could start experiment 1 tomorrow from this file alone; anything vaguer is a draft — name the gap and sharpen it.

Give the member both file paths and a one-paragraph summary: the focus channel, the first experiment to run this week, and the number that means it worked. Next step: run the cycle's quick win first, log every result in `docs/GROWTH-TRACKER.md`, and re-run this skill each cycle; when the focus channel hits its target and plateaus, bring the next channel from `docs/GO-TO-MARKET.md` online.

## Failure patterns

Name them when you see them — naming compounds learning:

- **The Vanity Experiment.** The "win" is views, likes, or followers. Redesign until the pass threshold is revenue-shaped (signups, trials, paying users, booked calls, cost-per-acquisition).
- **Too Many in Flight.** More than three experiments, or more than one channel, at once. You can't read which change moved the number. Cap it at three on one channel.
- **The Thresholdless Test.** An experiment with no number and no date. That's an activity, not an experiment. Force "Pass = X by Y."
- **The Generic Experiment.** Steps that fit any product — "post more," "improve SEO," "run ads." Rewrite until each step could only be this product's, in this customer's words.
- **The Big-Bet-First Trap.** Reaching for a high-effort experiment while quick wins sit untouched. Clear the high-impact/low-effort wins first, every time.
- **The Unlogged Result.** Running experiments but never recording outcomes, so nothing compounds. The tracker is not optional — it's the asset that makes the next cycle smarter.
- **Optimizing a Dead Channel.** Pouring experiments into a channel that fundamentally isn't reaching buyers. If the channel can't clear its threshold after honest reps, the problem is channel choice — return to `docs/GO-TO-MARKET.md`, don't keep experimenting.
