---
name: distribute-scale-automate
description: >-
  Takes only proven winners from docs/GROWTH-TRACKER.md (passed and marked double down), plans how
  to amplify each and automate it with specific tools, MCPs, and scheduled tasks sequenced
  Now/Next/Later, and writes docs/SCALE.md. Checks activation first. Use when the user asks to
  "scale what works", "what should I automate", or for an "automation roadmap". Not for designing
  new experiments — use distribute-growth-experiments.
---

# Distribute: Scale & Automate

Read the Growth Experiments Tracker, take only the experiments that *proved* they work, and turn each into a plan to **double down** — do *more* of it (volume, spend, reach) and do it *better* (the next experiment that lifts it further) — and to **automate** it (clip-and-schedule pipelines, enrichment-and-sequence loops, scheduled tasks, templates, eventually delegation), so output grows without the member's hours growing with it. The output is `docs/SCALE.md`.

The evidence gate is non-negotiable: **only scale and automate what the tracker has proven.** Guard against scaling a hunch, automating a process before it works, and automating away the human touch that made it work (the member's voice, real community presence, a personal first line) — and keep a guardrail metric on every automation so throughput never quietly costs conversion. Plan the **top few winners**, not every line in the tracker.

## Inputs

The skill needs the **proven winners**, **product context** (so automations are specific), an **output target**, and the **automation playbook**. Winners come one of two ways; the rest is identical.

### Winners — Path A (standard): ProductOS in the repo — `productos/` at the app repo root, or the current folder in a standalone ProductOS checkout

1. **The Growth Experiments Tracker** — `docs/GROWTH-TRACKER.md`. The **primary** input. Read the log for rows whose **Pass?** is `Pass` and whose **Decision** is `double down`, and the **Cumulative Learnings**. These are the only candidates for scaling and automation.
2. **Context:** `docs/GROWTH-EXPERIMENTS.md` (the rhythm and up-next queue) and `docs/GO-TO-MARKET.md` (the channels). Plus `docs/DEFINE.md` for the customer (Offer and Persona) and the north star (Business Strategy, when filled), and `docs/MAGIC-MOMENT.md` for the magic moment. Read the primary shape slug from `docs/DEFINE.md` → `## Product Shape` → `### Primary Shape`, and the `## Distribute notes` of its shape file (`productos/shapes/<slug>.md`, or `../../shapes/<slug>.md` from this skill's folder) when a winner is on the shape's native store, marketplace, or registry. No Product Shape section → treat it as `web-app` unless the codebase says otherwise.

### Winners — Path B (standalone fallback): a repo without ProductOS

Read the codebase for product context, then **ask the member what's already working**: which channel/tactic is reliably producing results, the number that proves it, and the manual steps they run today. Establish the same thing the tracker would supply — a short list of *proven* winners with real numbers — before building the roadmap. Don't scale anything the member can't put a number on.

### Output target (both paths)

`docs/SCALE.md` at the app repo root (create `docs/` if needed). On Path A the worksheet `productos/distribute/4-Scale-and-Automation-Roadmap.md` gives the structure — read it, never write to it. On Path B, use the same six sections. Match the headers exactly: **1. What's Working → 2. Double Down → 3. Automate → 4. The Roadmap → 5. Guardrails → 6. Next.**

### Automation playbook (both paths)

Three reference docs live in ProductOS's `distribute/` folder, two levels up from this skill's folder (`../../distribute/`) — the same files whether ProductOS sits in the repo as `productos/` or is installed as a plugin. Don't read them whole — grep for each winner's channel and read only that section:

- **[BONUS-Growth-Experiments-Library.md](../../distribute/BONUS-Growth-Experiments-Library.md)** — the **primary** automation reference: each channel section's **"Recommended tools & plugins"** block names the tools, MCPs/plugins, and scheduled tasks that automate that channel's work, and its experiments supply the "do better" move.
- **[BONUS-AI-Distribution-Tools.md](../../distribute/BONUS-AI-Distribution-Tools.md)** — the tool stack for that channel.
- **[BONUS-Distribution-Channels.md](../../distribute/BONUS-Distribution-Channels.md)** — channel context for each winner.

## Workflow

### 1. Absorb the tracker and gate to proven winners

**Activation gate first** (DISTRIBUTE-CHECKLIST: "Before you scale"). Check for `docs/ACTIVATION-RETENTION-AUDIT.md`. If it doesn't exist, or it lists P0 findings that aren't fixed yet, say so before planning anything: scaling traffic into a product that doesn't activate wastes it. Recommend running `distribute-activation-retention-audit` (or fixing the open P0s) first, and continue only if the member chooses to.

Read the tracker (or, on Path B, establish winners by asking). Pull every experiment marked `Pass` + `double down`, plus the cumulative learnings that explain *why* each works. List them back to the member as the candidate winners, with their numbers. Anything not proven — iterated, killed, or never thresholded — does not pass the gate; push back when the member wants to automate a hunch. If nothing has been proven yet, say so and route the member back to `distribute-growth-experiments`; there is nothing to scale.

Ask the member, one question at a time, for what the tracker can't supply: their weekly time budget, their tooling/automation budget, and whether they're open to delegation.

### 2. For each winner, find the scale lever and the automation path

For each proven winner, work out the **scale lever** (what "more" looks like — more posts, more spend, more sends, wider reach) and the **automation path** (which tools, MCPs/plugins, and scheduled tasks collapse the manual steps). Pull the automation path from the winner's channel section in the Library (the "Recommended tools & plugins" line) and the tools doc. Note where the work genuinely needs a human. **A winner on the shape's native channel** scales differently from a content channel: *more* is more surfaces (the same product listed in the adjacent stores, registries, or agent marketplaces the shape file names; listings for the next search terms; localized listings), and *automated* is the plumbing around the listing (the in-product review prompt after the first successful output, store-console reports on a schedule, release notes published with every version so the listing stays fresh). Replying to reviews stays human.

### 3. Double down — define do-more and do-better

For each winner, write both moves — never let "do more" stand alone:

- **Do more** — the scale lever with a **target number** ("1/day → 3/day," "$50/day → $200/day at the same cost-per-acquisition," "50 sends/week → 200"). Scaling is only safe while the result holds, so tie it to the metric.
- **Do better** — the next experiment that lifts the win further, drawn from the same channel in the Library. This links back to `docs/GROWTH-EXPERIMENTS.md`: doing better never stops, even once doing more is automated.

### 4. Automate — map manual to automated, with a human-in-the-loop

For each winning process, write the **manual steps today**, then the **automated version** — named tools, MCPs/plugins, scheduled tasks, and SOP/templates. Check which connectors are installed first; for any the plan names that aren't, give a manual fallback. Say out loud the **one step to keep human** (the part that works *because* it's human — the hook-writing, the member's voice, the authentic reply) and why. Place the process on the **maturity ladder** — Manual → Templated → Assisted → Automated → Delegated — and name the next rung. Delegation is the top rung: once a process is documented and assisted, it can be handed to a VA or contractor.

### 5. Sequence the roadmap, set guardrails, write the file

Order the automations into **Now / Next / Later**, rated by effort and impact — ship the highest-leverage, lowest-effort one first, and automate one process well before starting the next: one finished automation beats three half-built ones. Then write the **guardrails**: the "don't automate (yet)" list (the unproven, the human-magic), the **one metric** that proves automation is lifting results (not just throughput — watch conversion/quality, not only volume), and a **stop rule** if that metric drops after an automation ships.

Write `docs/SCALE.md` using the worksheet's structure (the same structure on Path B), without the worksheet's `> Good/Bad` lines and italic prompts. If it already exists, read it first, preserve the member's edits, show a diff, and get approval before overwriting. Add a short **summary** at the top (the top winners being scaled and the first automation to ship), a **dated header**, and an **evidence footer** citing the tracker rows the roadmap is built on.

### 6. Verify before delivering

Re-read the roadmap against the failure patterns below:

- [ ] Every winner in **What's Working** is **proven** in the tracker (`Pass` + `double down`), with a real number and why it works — not a hunch.
- [ ] Every winner has both a **do-more (with a target)** and a **do-better**.
- [ ] Every automation maps manual → automated with **specific tools/MCPs/scheduled tasks** (with a manual fallback for any connector that isn't installed), a **keep-human** step, and a maturity rung.
- [ ] The roadmap is sequenced **Now/Next/Later, quick wins first**, one process at a time.
- [ ] **Guardrails** name what not to automate, the **metric to watch**, and a **stop rule**.
- [ ] A summary sits at the top; the file is dated and cites the tracker rows it's built on. Anything that scales a hunch or automates the human-magic is a draft — name it and fix it.

Give the member the file path and a one-paragraph summary: the top winner being scaled, the first automation to ship this week, and the metric to watch. Next step: ship the "Now" automation, hold the guardrail metric for a cycle, then re-run as new winners land in the tracker and as each automation earns its next rung.

## Failure patterns

Name them when you see them:

- **Scaling the Unproven.** Pouring more time or money into something the tracker never proved. The gate is absolute: `Pass` + `double down`, with a number, or it doesn't get scaled.
- **Automating the Magic Away.** Automating the part that works *because* it's human — the member's voice, real community replies, a personal first line. Keep that human; automate the plumbing around it.
- **Premature Scale.** Cranking spend or volume before the unit economics support it. "Do more" is only safe while the result metric holds at the higher level.
- **The Tool Hoard.** Buying ten tools instead of automating the one bottleneck step. Automate the step that actually costs the most time, with the fewest tools that do it.
- **More Without Better.** Scaling a mediocre win instead of sharpening it first. Pair every "do more" with a "do better."
- **No Guardrail Metric.** Throughput goes up while conversion quietly goes down. Every automation needs a metric that watches quality, and a stop rule.
- **Automating Out of the Loop.** Removing yourself so completely that you lose the customer signal that drove the wins. Keep a window onto real users.
