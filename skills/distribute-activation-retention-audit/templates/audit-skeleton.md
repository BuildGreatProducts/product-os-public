# Audit skeleton — docs/ACTIVATION-RETENTION-AUDIT.md

Use this structure at step 7. Keep prose tight; tables over paragraphs. Effort is `S` / `M` / `L`; Impact is `L` / `M` / `H`.

```
# Activation & Retention Audit

*Drafted: [Month Year]. Product type: [type]. Framework: [framework]. Retention model: [daily/weekly/occasional]. Magic moment: [event].*

## Summary
[Three sentences: total findings, P0/P1 count, the single biggest leak and its headline fix.]

## Top 5 fixes ranked by effort × impact
1. **[Finding]** — `[location]` — P[X], Effort [S/M/L], Impact [L/M/H]. [One-sentence fix.]
2. … 3. … 4. … 5. …

## The activation funnel as-built
[The steps from signup to magic moment, friction flagged. Name the step count and the drop points.]

---
## A. Time-to-Value & the Activation Path
| # | Finding | Location | Sev | Effort | Impact | Fix |
| --- | --- | --- | --- | --- | --- | --- |
| A1 | … | `[file]:[line]` | P0 | S | H | … |
## B. Signup Gating & Friction Walls
## C. Empty States & First-Run Guidance
## D. Onboarding Flow Friction
[same table structure for B–D]

## The retention loop as-built
[What brings users back — or "nothing currently does."]

## E. Re-engagement Channels
## F. The Return Loop & Stored Value
## G. Churn & Win-Back Surfaces
## H. Activation & Retention Instrumentation
[same table structure for E–H]

---
## Cross-cutting quick wins
[the 5, with specific findings]

## Strategy-code drift (if ProductOS docs present)
[where documented magic moment / onboarding ≠ shipped code]

## Fix prompt (paste into your coding agent)
> Fix the following activation and retention leaks in this codebase. For each, the file and the change:
> 1. [P0 finding] — `[file:line]` — [the change].
> 2. …
> Work through them top to bottom; after each, confirm the activation event fires and is tracked.

## Verification next steps
- [ ] Confirm the magic-moment event fires and is tracked in analytics
- [ ] Measure Day 1 / Day 7 retention as a baseline
- [ ] Send a test through each lifecycle email / push trigger
- [ ] Re-run this audit in 30 days to measure the lift

## Sources & calibration
[benchmarks used, each with its source + workspace docs referenced if present]
```
