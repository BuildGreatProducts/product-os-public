---
name: studio-distribute-scale-automate
description: Use after the user has run growth experiments and logged results, when they want to scale what's proven and automate it. Triggers on phrases like "scale my product", "automation roadmap", "automate what works", "double down on what works", "how do I scale this", "systematize my marketing", "make my growth scalable", "what should I automate", or "scale my growth". Reads the Growth Experiments Tracker (or, in a repo without ProductOS, asks what's already working), takes only the proven winners, and builds a roadmap that amplifies each one (do more, do better) and automates it with specific tools, MCPs/plugins, and scheduled tasks — sequenced Now/Next/Later on a manual-to-delegated maturity ladder. Produces a Scale & Automation Roadmap document. Works with ProductOS in the repo (productos/ at the app repo root) or standalone in a repo without it.
---

# Distribute: Scale & Automate

This skill is the capstone of the Distribute phase. It reads the **Growth Experiments Tracker**, takes only the experiments that *proved* they work, and turns each into a plan to **double down** (do more, do better) and **automate** (make the winning process run without more of the founder's hours). The output is a sequenced Scale & Automation Roadmap.

The two principles are the whole skill. **Double down:** a proven win is a license to do *more* of it (scale the volume, spend, or reach) and *better* (the next experiment that lifts it further). **Automate:** a manual process that works is a process worth systematizing — clip-and-schedule pipelines, enrichment-and-sequence loops, scheduled tasks, templates, and eventually delegation — so output grows without the founder's time growing with it. Scale is what happens when both run at once: you amplify the result and remove yourself from the loop.

The evidence gate is non-negotiable: **you only scale and automate what the tracker has proven.** The most expensive mistakes here are scaling a hunch, automating a process before it works, and automating away the human touch that made it work in the first place (the founder's voice, real community presence, a personal first line). This skill exists to amplify proven wins, systematize them safely, and keep a guardrail metric on every automation so throughput never quietly costs conversion.

> **Session length:** 30–45 minutes. **Claude reads the tracker and maps each winning process to its automation** using the bundled tool/plugin recipes; the user supplies their time budget, their tooling/automation budget, and whether they're open to delegation. The skill plans the **top few winners**, not every line in the tracker — depth over breadth.

## Inputs

This skill needs the **proven winners**, **product context** (so automations are specific), an **output target**, and the **automation playbook**. Winners come one of two ways depending on where the skill runs — the rest is identical.

### Winners — Path A (standard): ProductOS in the repo — `productos/` at the app repo root, or the current folder in a standalone ProductOS checkout

1. **The Growth Experiments Tracker** — usually `productos/distribute/3. Growth Experiments Tracker.md`. The **primary** input. Read the log for rows marked **Pass** with a **"double down"** decision, and the **Cumulative Learnings**. These are the only candidates for scaling and automation. If the tracker is empty or has no winners yet, stop and point the user back to `studio-distribute-growth-experiments` — there's nothing proven to scale.
2. **Context:** `productos/distribute/2. Growth Experiments.md` (the rhythm and up-next queue) and `productos/distribute/1. Go-To-Market Strategy.md` (the channels). Plus `docs/PRODUCT.md` or the Define docs for the customer, the magic moment, and the north star.

### Winners — Path B (standalone fallback): a repo without ProductOS

When there's no tracker — the skill runs in a normal app repo — read the codebase for product context, then **ask the user what's already working**: which channel/tactic is reliably producing results, the number that proves it, and the manual steps they run today. Establish the same thing the tracker would supply — a short list of *proven* winners with real numbers — before building the roadmap. Don't scale anything the user can't put a number on.

### Output target (both paths)

**`productos/distribute/4. Scale & Automation Roadmap.md`** — on the standard path this exists as a template; **rewrite it in place**. On the standalone fallback, create it fresh with the same six-section structure at `docs/scale-automation-roadmap.md`. Match the headers exactly: **1. What's Working → 2. Double Down → 3. Automate → 4. The Roadmap → 5. Guardrails → 6. Next.**

### Automation playbook (both paths)

Three reference docs ship **inside this skill's folder**, so they're available in both paths:

- **`BONUS - Growth Experiments Library.md` (in this skill's folder)** — the **primary** automation reference: each channel's **"Recommended tools & plugins"** block names the tools, MCPs/plugins, and scheduled tasks that automate that channel's work. The automated version of each winner should be built from these.
- **`BONUS - AI Distribution Tools.md` (in this skill's folder)** — the full tool stack to draw specific tools from.
- **`BONUS - Distribution Channels.md` (in this skill's folder)** — channel context for each winner.

The same files also live in `productos/distribute/`; prefer the user's copies if customized. The bundled copies guarantee the skill has its playbook when run standalone.

## Workflow

### 1. Absorb the tracker and gate to proven winners

Read the tracker (or, on Path B, establish winners by asking). Pull every experiment that **passed and earned a "double down,"** plus the cumulative learnings that explain *why* each works. List them back to the user as the candidate winners, with their numbers. Anything not proven — iterated, killed, or never thresholded — does not pass the gate. If nothing has been proven yet, say so and route the user back to the Growth Experiments skill; there is nothing to scale.

### 2. For each winner, find the scale lever and the automation path

For each proven winner, work out two things: the **scale lever** (what "more" looks like — more posts, more spend, more sends, wider reach) and the **automation path** (which tools, MCPs/plugins, and scheduled tasks collapse the manual steps). Pull the automation path straight from the winner's channel block in the **Growth Experiments Library** (the "Recommended tools & plugins" line) and the tools doc. Note where the work genuinely needs a human.

### 3. Double down — define do-more and do-better

For each winner, write both moves:

- **Do more** — the scale lever with a **target number** ("1/day → 3/day," "$50/day → $200/day at the same cost-per-acquisition," "50 sends/week → 200"). Scaling is only safe while the result holds, so tie it to the metric.
- **Do better** — the next experiment that lifts the win further, drawn from the same channel in the Library. This links back to `2. Growth Experiments`: doing better never stops, even once doing more is automated.

### 4. Automate — map manual to automated, with a human-in-the-loop

For each winning process, write the **manual steps today**, then the **automated version** — named tools, MCPs/plugins (Apollo, Notion, Figma, Claude-in-Chrome), scheduled tasks, and SOP/templates. Call out the **one step to keep human** (the part that works *because* it's human — the hook-writing, the founder's voice, the authentic reply). Place the process on the **maturity ladder** — Manual → Templated → Assisted → Automated → Delegated — and name the next rung. Delegation is the top rung: once a process is documented and assisted, it can be handed to a VA or contractor.

### 5. Sequence the roadmap and set guardrails

Order the automations into **Now / Next / Later**, rated by effort and impact — ship the highest-leverage, lowest-effort one first, and automate one process well before starting the next. Then write the **guardrails**: the "don't automate (yet)" list (the unproven, the human-magic), the **one metric** that proves automation is lifting results (not just throughput — watch conversion/quality, not only volume), and a **stop rule** if that metric drops after an automation ships.

Rewrite `productos/distribute/4. Scale & Automation Roadmap.md` in place (or create the fresh doc on Path B). Match the template structure exactly; read the existing file first to preserve notes. Add a short **summary** at the top (the top winners being scaled and the first automation to ship), a **dated header**, and an **evidence footer** citing the tracker rows the roadmap is built on.

### 6. Verify before delivering

Re-read the roadmap and check:

- Is every winner in section 1 **proven** in the tracker (Pass + double down), with a real number — not a hunch?
- Does every winner have both a **do-more (with a target)** and a **do-better**?
- Does every automation name **specific tools/MCPs/scheduled tasks** and a **keep-human** step?
- Is the roadmap sequenced **Now/Next/Later, quick wins first**, one process at a time?
- Is there a **guardrail metric and a stop rule** so automation can't silently erode results?

Deliver the file via a `computer://` link and a one-paragraph summary: the top winner being scaled, the first automation to ship this week, and the metric to watch.

## Failure patterns to look for

Name them when you see them:

- **Scaling the Unproven.** Pouring more time or money into something the tracker never proved. The gate is absolute: Pass + double-down, with a number, or it doesn't get scaled.
- **Automating the Magic Away.** Automating the part that works *because* it's human — the founder's voice, real community replies, a personal first line. Keep that human; automate the plumbing around it.
- **Premature Scale.** Cranking spend or volume before the unit economics support it. "Do more" is only safe while the result metric holds at the higher level.
- **The Tool Hoard.** Buying ten tools instead of automating the one bottleneck step. Automate the step that actually costs the most time, with the fewest tools that do it.
- **More Without Better.** Scaling a mediocre win instead of sharpening it first. Pair every "do more" with a "do better."
- **No Guardrail Metric.** Throughput goes up while conversion quietly goes down. Every automation needs a metric that watches quality, and a stop rule.
- **Automating Out of the Loop.** Removing yourself so completely that you lose the customer signal that drove the wins. Keep a window onto real users.

## Tone and pacing

- **Conversational, not a form.** The user is deciding where to remove themselves from their own business; treat it like a real operational decision.
- **Guard the evidence gate.** The most valuable thing this skill does is refuse to scale the unproven. Push back when the user wants to automate a hunch.
- **Pair more with better.** Never let "do more" stand alone — scaling a win you could still improve leaves money on the table.
- **One automation at a time.** Sequence ruthlessly; a half-built automation on three processes beats nothing finished.
- **Name the human step.** For every winner, say out loud what stays manual and why.

## What "done" looks like

A filled `productos/distribute/4. Scale & Automation Roadmap.md` (or `docs/scale-automation-roadmap.md`) where:

- **What's Working** lists only tracker-proven winners, each with its number and why it works.
- **Double Down** gives every winner a do-more (with a target) and a do-better.
- **Automate** maps each winning process from manual to automated with named tools/MCPs/scheduled tasks, a keep-human step, and a maturity rung.
- **The Roadmap** sequences automations Now/Next/Later, quick wins first.
- **Guardrails** name what not to automate, the metric to watch, and a stop rule.
- A summary sits at the top; the file is dated and cites the tracker rows it's built on.

A plan the user can act on **this week** — scale the top winner, ship the first automation, and watch the one metric that proves it's working. Anything that scales a hunch or automates the human-magic is a draft; name it and fix it.

Recommended next step after a successful session: ship the "Now" automation, hold the guardrail metric for a cycle, then re-run — both as new winners land in the tracker and as each automation earns its next rung up the maturity ladder.
