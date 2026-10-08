# Evals by shape

What to test, rubric examples, how to run, and the usual fixes for each AI-native shape. Read only the section for the product's primary shape (and any secondary shape the MVP ships).

## Contents

- [agent-skill and agent-plugin](#agent-skill-and-agent-plugin)
- [mcp-server](#mcp-server)
- [chat-assistant](#chat-assistant)
- [AI outputs in any other shape](#ai-outputs-in-any-other-shape)

## agent-skill and agent-plugin

Two things are tested separately: **triggering** (does the right skill load for the request) and **task quality** (once loaded, does it do the job well).

**Triggering**

- Write at least three should-trigger requests per skill, phrased the way different customers would — including ones that describe the problem without naming the task.
- Write at least as many should-not-trigger requests: near misses (same topic, different job) and the jobs of neighbouring skills the customer is likely to have installed.
- Grade from the transcript: did this skill load, and did any other skill load instead? Run every request on every model in the set — small models are the most sensitive to a weak description.
- The fix is almost always the description: what it does, when to use it, 3–5 trigger phrases in the customer's words, and a "Not for X — use Y" line that separates it from its neighbours.

**Task quality** — rubric examples:

- "Reads `references/pricing-models.md` before recommending a price" (the right reference, at the right step).
- "Runs `scripts/validate.py` instead of checking the file by eye" (scripts used for deterministic work).
- "Asks one question at a time and waits" (follows the workflow's pacing).
- "Writes `docs/REPORT.md` with the template's five headings" (output shape).
- "Stops and names the missing input when `data.csv` is absent" (failure behaviour).

**Plugins, in addition:** each command handles missing and malformed arguments; each hook fires on the right event only, finishes within its time budget, and fails safe (a failing hook never blocks or corrupts the user's work); bundled components don't collide with each other; the plugin installs cleanly from its marketplace in a fresh environment.

**Running — "Claude A writes, Claude B tests":** A (the authoring session) never grades its own run. B is a clean instance with only the product installed — in Claude Code, a fresh subagent per scenario with the model set; elsewhere, a fresh chat. A reads B's full transcript: which files B opened, in what order, what it skipped, where it hesitated. Those observations, not the final output alone, drive the refinement.

**Usual failures → fixes:**

- Small models skip steps buried in a long body → shorter body, numbered steps, detail moved to references with an explicit "read when".
- The agent reads every reference up front → a sharper "read when" line per reference.
- The agent improvises what a script should do → name the script at the step that needs it, with its exact command.
- Large models over-deliver (extra sections, unrequested files) → state the output's exact shape and what not to add.

## mcp-server

Agents meet the server through tool names, descriptions, and schemas — test what an agent does with them.

**What to test:**

- **Tool selection** — given the request and every tool listed (plus any other servers the customer likely runs), the agent calls the right tool first and makes no needless calls.
- **Arguments** — valid against the schema; IDs, dates, and enums in the right format; values taken from earlier tool results rather than invented.
- **Multi-step jobs** — chains of calls (search → read → update) completed in a sensible order.
- **Errors are actionable** — provoke them on purpose (a bad ID, missing permission, rate limit, an empty result) and check that the error text leads the agent to the right next step instead of a retry loop or a guess.
- **Response size** — results fit in context; the agent uses pagination or filters for large sets.
- **Destructive tools** — the agent confirms with the user before deleting, sending, or paying.

**Rubric examples:** "calls `find_customer` before `create_invoice`", "passes `due_date` as YYYY-MM-DD", "after the `not_found` error, searches by email instead of retrying the same ID", "asks the user before calling `delete_project`".

**Running:** connect the server to at least two real clients the PRD names (a chat app and a coding agent, say) — hosts differ in how they present tools. A schema inspector catches broken schemas but is not an eval; only an agent run shows whether the tools get used well.

**Usual failures → fixes:** overlapping tools confuse selection → merge or rename them so each has one clear job; vague descriptions → say when to use the tool and when not to; free-text fields → enums and field descriptions with examples; bare error codes → messages that say what to do next.

## chat-assistant

Conversations, not single requests, are the unit of test.

**What to test:**

- **Multi-turn flows** — scripted conversations of 3–8 user turns per core job, including the user giving information late, changing their mind, and asking follow-ups. Grade the whole conversation.
- **Staying in scope** — out-of-scope requests get a brief decline and a redirect; in-scope requests that merely look borderline get answered (include these — over-refusal is a failure too).
- **Refusals** — harmful or policy-breaking requests are refused in the assistant's voice, without lecturing.
- **Knowledge** — questions the knowledge answers are answered from it; questions it doesn't cover get "I don't know" plus a next step, never an invented answer.
- **Actions** — the right action with the right parameters, and a confirmation before anything with side effects.
- **Instruction attacks** — user messages or retrieved content that try to override the system prompt or extract it.
- **Tone** — matches `docs/COPY.md`'s voice chart.

**Rubric examples:** "asks for the booking date before checking availability", "declines the tax-advice question and points to an accountant", "says the policy doesn't cover pets instead of guessing", "keeps the system prompt private when asked to print it".

**Running:** run on the real platform (the GPT, the Slack app, the bot), not only through the raw model API — platform wrappers change behaviour. Paste each user turn in order, in a fresh conversation per scenario.

**Usual failures → fixes:** drifts out of scope late in long conversations → restate the scope and the decline pattern in the system prompt's closing lines; invents answers → an explicit "when knowledge has no answer" rule with the exact fallback; over-refuses → examples of in-scope requests that look borderline.

## AI outputs in any other shape

For an AI feature inside an app, a service, or a digital product (a report generator, a classifier, a drafting step in a delivery SOP):

- Build a golden set — at least three inputs per output type: typical, hard, and edge — with the rubric each output must meet.
- Re-run the whole set after every prompt, model, or pipeline change; a change that fixes one case and breaks another is a regression.
- A model can grade outputs against the rubric, but only with explicit pass/fail items, and the member spot-checks its grades on a sample each run.
