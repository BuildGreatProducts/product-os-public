# Distribute — Checklist

Work top to bottom. Requires `docs/PRODUCT.md` to exist and the product to be reachable by customers. Coming here directly with an already-live product? Run the Define fast-track first — `studio-define-from-code`, then `studio-define-product` — so this phase has a real PRODUCT.md to read; it takes hours, not weeks. This phase gets the product in front of people, finds what actually works, and scales it — it's a **loop**, not a one-pass sequence.

If `docs/PLAN.md` exists (your programme plan, shipped with coached copies of ProductOS), it says where this phase starts in your sequence and which launch is next on your ladder — follow it; this checklist remains the source of truth for how each step runs.

Before you start, skim the two reference playbooks you'll lean on throughout: `BONUS-Distribution-Channels.md` (which channel to pick and how each one works) and `BONUS-AI-Distribution-Tools.md` (the software to run them). Set up `BONUS-Measurement-and-Attribution.md` before Step 3 so every result is a real number.

---

## Step 1 — Go-To-Market Strategy

- **What to do:** Run `studio-distribute-gtm-strategy`.
- **What it does:** Produces `productos/distribute/1-Go-To-Market-Strategy.md` — a one-page execution plan: your three channels in sequence order, each with a product-specific "Do this" checklist and the number that means it's working. Just instructions — the channel reasoning and playbooks stay in the skill and `BONUS-Distribution-Channels.md` / `BONUS-AI-Distribution-Tools.md`.

## Step 2 — Relaunch: the public launch

- **What to do:** Run `studio-launch` once your Go-To-Market Strategy names the primary channel. Same ritual as every launch before it: ship within 48 hours, share a screenshot of the live post with your cohort or accountability partner, log every response in `docs/LAUNCHES.md`.
- **What it does:** Announces the live product — believers first (they've been waiting for this since the mini-launch), then the primary channel from `1-Go-To-Market-Strategy.md`. **The win is the first payment** — the top rung of the signal ladder. Your longest-standing believers are also your first testimonials; ask.

## Step 3 — Growth Experiments

- **What to do:** Run `studio-distribute-growth-experiments`.
- **What it does:** Produces `productos/distribute/2-Growth-Experiments.md` — a one-page execution list: the 1–3 experiments running now, each with concrete steps and a pass bar, plus your up-next queue in order — and seeds `productos/distribute/3-Growth-Experiments-Tracker.md` with this cycle's experiments. The prioritization method stays in the skill; it draws on `BONUS-Growth-Experiments-Library.md`, `BONUS-AI-Distribution-Tools.md`, and `BONUS-Measurement-and-Attribution.md`.

## Step 4 — Run the cycle and log results

- **What to do:** Run the cycle's experiments, and log every result in `productos/distribute/3-Growth-Experiments-Tracker.md` — the number against the pass threshold, the learning, and the decision (double down / iterate / kill). Re-run `studio-distribute-growth-experiments` each cycle for the next set.
- **What it does:** Turns the plan into evidence. The tracker is a **living document**, not a one-pass step — it's where "what works" accumulates, and it's the input the scaling step reads. Set up measurement first with `BONUS-Measurement-and-Attribution.md` so every result is a real number, not a guess.

## Step 5 — Scale & Automate

- **What to do:** Once the tracker has proven winners (Pass + double down), run `studio-distribute-scale-automate`.
- **What it does:** Produces `productos/distribute/4-Scale-and-Automation-Roadmap.md` — for each proven winner, a plan to do more, do better, and automate the process up the maturity ladder, sequenced Now / Next / Later. Reads the winners from `productos/distribute/3-Growth-Experiments-Tracker.md`.
- **Before you scale:** make sure activation works — that the users a channel sends actually reach the magic moment (`productos/design/2-Magic-Moment.md`). Scaling acquisition into a product that doesn't activate just pours water into a leaky bucket. Find and fix the leaks first — run `studio-distribute-activation-retention-audit` on your codebase (and `studio-develop-cro-audit` for conversion surfaces) — before pouring on more traffic.

---

## Keep going

Distribution is a loop, not a finish line. Each cycle: run experiments (Steps 3–4), log results, scale the winners (Step 5), then come back and experiment on the next improvement — or, when a channel maxes out, bring the next one online from your `1-Go-To-Market-Strategy.md`. *Doing better* never stops, even once *doing more* is automated.
