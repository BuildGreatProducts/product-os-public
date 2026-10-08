---
name: develop-agent-evals
description: >-
  Writes docs/EVALS.md, the test suite for an AI-native product: for each core job, three or more
  scenarios (the request, input files, a checkable rubric), a baseline run without the product,
  runs across small, mid, and large models, and an observe-refine-re-run loop. Develop Step 1b.
  Use when the user says "write evals", "test my skill", "will agents use my MCP server right", or
  "is my assistant good enough". Reads docs/PRD.md and the product shape. Not for unit tests of app
  code — use develop-build or build-loop.
---

# Develop: Agent Evals

An AI product's quality lives in what a model does with it — whether a skill fires and follows its steps, whether an agent picks the right tool with valid arguments, whether an assistant stays in scope across turns. Code tests can't see that. `docs/EVALS.md` defines "good" as scenarios with checkable rubrics before the build, so build tasks verify against it and every refinement is measured rather than guessed.

**When it runs:** Develop Step 1b — Full for `agent-skill`, `agent-plugin`, `mcp-server`, and `chat-assistant`; optional for any product whose core is an AI output (an AI feature inside a web app, an AI-run productized service). After `develop-prd-roadmap`, before `develop-build`; the roadmap's eval tasks re-run it during the build, and it re-runs whenever the product, the prompts, or the target models change.

## Inputs

1. **`docs/PRD.md`** — required. Core jobs come from its P0 functional requirements and user stories, plus the shape sections (Skill Structure and Description & Triggering; Tools, Resources & Prompts; Conversation Design and Guardrails). Missing → run `develop-prd-roadmap` first. Outside ProductOS, ask the member for the core jobs instead.
2. **The shape** — `docs/DEFINE.md` → `## Product Shape` → `### Primary Shape`. Read the matching section of [references/by-shape.md](references/by-shape.md) before writing scenarios — it holds what to test, rubric examples, and common failures per shape.
3. **The persona** — `docs/DEFINE.md` → `## 2. Customer Persona`, for requests in the customer's own words.
4. **`docs/MAGIC-MOMENT.md`** — the job whose scenarios matter most.
5. **An existing `docs/EVALS.md`** — resume: keep its scenarios and run log; add, never silently rewrite. Never delete a scenario that has caught a failure.

## Workflow

### 1. Name the core jobs

List the 2–6 jobs the product must do, from the P0 requirements — each as one line: *"Given {situation}, the product {does what}."* Confirm the list with the member.

### 2. Write the scenarios

At least three per job:

- **Typical** — the request as the persona would phrase it, with inputs as they'd really arrive.
- **Hard** — messy or incomplete input, ambiguity, an unusual or long case.
- **Boundary** — something the product must decline, redirect, or not fire on (for a skill, a near-miss request that must not trigger it).

Each scenario has an ID (`J1-S1`), the request verbatim, its context (input files saved in `docs/evals/<ID>/`, or the account state, prior turns, and other tools present, described precisely enough to reproduce), and **expected behaviours as a rubric**: 3–7 items, each pass/fail from reading the transcript or output — *"asks for the date range before querying"*, *"calls `search_contacts` before `update_contact`"*, *"writes `report.md` with the four headings"* — never *"is high quality"*. Mark the must-pass items. Requests never name the product's skills, tools, or internal vocabulary; customers don't.

Write every scenario before running anything, using [templates/evals.md](templates/evals.md) for the shape of the file. Have the member approve the jobs and skim the scenarios.

### 3. Pick the model set

The models customers will actually run it on — e.g. the small, mid, and large model from each target host. Record exact model names and the date. A product locked to one model (a Custom GPT) uses that one, and re-runs when the platform changes it.

### 4. Run the baseline — without the product

Run each scenario on the mid model with nothing installed: no skill, plugin, server, or system prompt — the plain model, or however the customer does the job today. Grade it and log it. The baseline shows what the product must add; a scenario the plain model already passes tests nothing — make it harder, unless it's there to guard against a regression. If the product isn't built yet, run the baseline now; product runs happen during the build's Evals & tuning phase.

### 5. Run, observe, refine, re-run

**Run** each scenario in a fresh session per model, with the product installed exactly as a customer would install it, the request pasted verbatim, and no hints. For skills and plugins this is the **"Claude A writes, Claude B tests"** method: this session (A) writes and refines the product; a clean instance (B) that has only the product installed receives the request. In Claude Code, run B as a fresh subagent with the model set; in other tools, the member opens a fresh chat per model and pastes back the transcript.

**Observe** how it failed, not just whether: didn't trigger, read the wrong reference, skipped a step, picked the wrong tool, sent a bad argument, invented a fact, drifted out of scope. Grade each rubric item pass/fail with a quoted line of evidence.

**Refine** the product — description, instructions, references, tool descriptions and schemas, system prompt — aimed at the observed failure. One change at a time where possible. Fix the cause, not the scenario: no instructions that only make sense for one test.

**Re-run** the failed scenarios, then every scenario for that job to catch regressions. Log every run.

**The pass bar:** every must-pass item passes on the mid and large models in every scenario; small-model failures are fixed or recorded under Known limits; no boundary scenario misfires. The PRD's success criteria and the roadmap's `Verify:` lines point at this bar.

### 6. Write `docs/EVALS.md`

Write (or update) the file in the template's shape: header, model set, how to run, pass bar, scenarios by job with their baselines, the triggering table for skills and plugins, the run log, and known limits.

## Verify before delivering

- [ ] Every P0 core job has at least three scenarios — typical, hard, and boundary — and the shape's checks from `references/by-shape.md` are covered.
- [ ] Every rubric item is pass/fail from the transcript or output; must-pass items are marked.
- [ ] Requests are in the persona's words and never name the product's internals.
- [ ] Input files exist in `docs/evals/`, or the context is reproducible from its description.
- [ ] The model set is recorded with names and a date.
- [ ] Every scenario has a logged baseline; the run log records date, version or commit, model, and score.
- [ ] Nothing was tuned to a single scenario.

**Next step:** `develop-build` — the roadmap's eval tasks run these scenarios as the product is built.
