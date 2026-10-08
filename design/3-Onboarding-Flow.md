# Onboarding Flow

*This is a worksheet for the `design-onboarding-flow` skill. The skill reads `docs/DEFINE.md`, the Product Identity in `docs/DESIGN.md`, and `docs/MAGIC-MOMENT.md`, auto-selects the appropriate best-practice reference from `productos/design/onboarding/`, designs the onboarding flow that engineers the user toward the magic moment, and writes the filled version to `docs/ONBOARDING.md` using the structure below. Screen shapes (web app, mobile app, desktop app, browser extension, website) get a screen-by-screen flow and a companion clickable HTML wireframe at `docs/ONBOARDING-WIREFRAME.html`. Every other shape gets a step-by-step flow — install → configure → first command → first output; purchase → download → first use; booking → intake → kickoff → first delivery — using the same block with **Step** in place of **Screen** and **Medium** in place of **Wireframe**. This file itself is never filled in.*

---

## Summary

[Two sentences: product shape and funnel shape (e.g., "Goal-First Quiz Funnel from Mobile Onboarding"; "Install-to-First-Output from Agent Extension Onboarding"), total screen or step count, estimated time-to-magic-moment, the named magic-moment screen or step number.]

## The magic moment we're engineering toward

> [One sentence from `docs/MAGIC-MOMENT.md`'s recommended primary.]

**Position:** Screen (or Step) [N] of [total].
**Time-to-aha target:** [from Magic Moment doc].
**Success metric:** [from Magic Moment doc].

---

## The flow

*One block per screen — or per step for screenless shapes. A step's "screen" is whatever the customer is looking at: a terminal, a chat, an inbox, a file, a call.*

> Good (step): "Step 2 — First command" · Medium: terminal, one line to paste, a three-line success message that names the next command · Drop-off risk: the command fails on Windows — mitigation: a tested PowerShell variant beside it
> Bad (step): "Step 2 — Setup" · Medium: "the docs" · Drop-off risk: "user might get confused"

### Screen 1 — [Name]

- **Goal:** [one sentence]
- **User action:** [tap/type/wait — or the command run, message sent, file opened, form returned]
- **What this screen proves:** [one sentence — what the user now believes about the product after this screen or step]
- **Copy:**
  - Headline: "[exact headline — or, for a step, the first words the customer meets: the command, the agent's first reply, the email subject]"
  - Sub: "[exact sub — or the success / follow-up line]"
  - CTA: "[exact CTA text — or the next action the step names]"
- **Wireframe:** [2–3 line description — for a step, label this **Medium** and describe the terminal, chat, email, file, or call and what's in it]
- **Drop-off risk:** [named risk]
- **Reference:** [BONUS doc + tactic number]

### Screen 2 — [Name]

- **Goal:** [one sentence]
- **User action:** [tap/type/wait — or the command run, message sent, file opened, form returned]
- **What this screen proves:** [one sentence — what the user now believes about the product after this screen or step]
- **Copy:**
  - Headline: "[exact headline — or, for a step, the first words the customer meets: the command, the agent's first reply, the email subject]"
  - Sub: "[exact sub — or the success / follow-up line]"
  - CTA: "[exact CTA text — or the next action the step names]"
- **Wireframe:** [2–3 line description — for a step, label this **Medium** and describe the terminal, chat, email, file, or call and what's in it]
- **Drop-off risk:** [named risk]
- **Reference:** [BONUS doc + tactic number]

### Screen [N] — [Magic moment screen name] ★

- **Goal:** [one sentence]
- **User action:** [tap/type/wait — or the command run, message sent, file opened, form returned]
- **What this screen proves:** [one sentence — what the user now believes about the product after this screen or step]
- **Copy:**
  - Headline: "[exact headline — or, for a step, the first words the customer meets: the command, the agent's first reply, the email subject]"
  - Sub: "[exact sub — or the success / follow-up line]"
  - CTA: "[exact CTA text — or the next action the step names]"
- **Wireframe:** [2–3 line description — for a step, label this **Medium** and describe the terminal, chat, email, file, or call and what's in it]
- **Drop-off risk:** [named risk]
- **Reference:** [BONUS doc + tactic number]
- **Magic moment:** This is where the user hits [the activation event].

[Additional screens or steps follow the same structure as needed]

---

## Anti-patterns avoided

[3–5 bullet list of anti-patterns from the relevant BONUS doc that this flow specifically avoids and why.]

## Success metric

[From Magic Moment doc, plus 1–2 supporting funnel metrics worth instrumenting — e.g., screen-by-screen or step-by-step drop-off, completion rate to magic moment, signup conversion, install-to-first-run rate, purchase-to-first-open rate.]

## Wireframe

A clickable HTML wireframe is at `docs/ONBOARDING-WIREFRAME.html` — open in any browser and click through to feel the flow. [Step flows: name the transcript mock if one was built, or "No wireframe — walk the steps for real: run the install on a clean machine, buy the product, book yourself."]

## Sources

- Reference: `productos/design/onboarding/BONUS-[X]-Onboarding-Best-Practice.md` ([selected pattern])
- Tone of voice: `docs/DESIGN.md` → Product Identity
- Magic moment: `docs/MAGIC-MOMENT.md`
- Product context: `docs/DEFINE.md`
