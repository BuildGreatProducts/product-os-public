---
name: continue
description: >-
  Picks up the member's ProductOS work where they left off — reads setup, any open challenge, the
  programme plan, docs/PATH.md, and docs/, tells the member in plain words where they are and what
  the next step does for them, then hands over to the skill that owns it: setup, a challenge
  check-in, product-refactor, or a phase orchestrator. Use when the member starts or returns to a
  session and says "continue", "keep going", "what's next", "where was I", or "pick up where I left
  off". Not for carrying on a task already under way in this conversation — just keep going with it.
---

# Continue — pick up where you left off

One word for the member to remember, in every session and every phase. This skill decides nothing new: it reads the state, tells the member where they are, and hands over to the skill that owns the next step. That skill reads `docs/PATH.md` or `docs/PLAN.md` and runs the step.

## Workflow

### 1. Read the state

Run `python3 productos/scripts/status.py --detail` from the app repo root (in a plugin install: `python3 <this skill's folder>/../../scripts/status.py --detail --repo .`). Without Python, read `docs/` against the "Done when" column in [ROUTING.md](../../ROUTING.md).

### 2. Find who owns the next step

The first match wins:

| The state | Hand over to |
| --- | --- |
| ProductOS isn't set up: the status script's *Setup* line shows the root guidelines not wired, `productos/` isn't in `.gitignore`, or ProductOS is standalone rather than inside a project folder | `setup` |
| A challenge is open (`docs/SHIP-IN-7.md` or `docs/SELL-IN-30.md` with `Status: Open`) | its check-in: `ship-in-7` or `sell-in-30` |
| `docs/PLAN.md` exists | `product-refactor`, which walks the plan in its own order |
| No `docs/DEFINE.md` yet | setup's question — *where would you like to start?* Find a new idea → `define-phase` (idea first); start from an idea they have → `define-phase` (new idea); start from an existing project → `product-audit`; take on a challenge → `ship-in-7`, or `sell-in-30` for a live product |
| Define isn't done | `define-phase` |
| The status script's next step is in Design, Develop, or Distribute | that phase's orchestrator: `design-phase`, `develop-phase`, or `distribute-phase` |
| Every step is done | `distribute-phase` — the growth loop keeps going |

### 3. Tell the member, in plain words

Two or three lines, with no step numbers, file names, or skill names unless they ask:

- where they are: the phase, and how much of it is done;
- what the next step does for them, in one sentence. The plain wording is in the status script's summary (`python3 productos/scripts/status.py` with no flag);
- that they can stop after any step, and "continue" picks up from there next time.

> You've defined your product and finished two of the six design steps. Next, we'll pin down the moment a customer first sees the value — the rest of the design builds toward it. Ready?

Wait for a yes, or for a different request, before handing over.

### 4. Hand over

Run the owner skill from its first step and follow its instructions. Don't run the step's own skill directly from here: the owner checks the step's needs, works in the plan's or path's mode, and records the member's decisions in `docs/PATH.md`.

## Rules

- Route only. The order lives in `docs/PLAN.md`, `docs/PATH.md`, and ROUTING.md; this skill never changes them.
- Speak plainly. Say what a step does, not what it's called. Explain a technical term in a few words the first time it comes up — [GLOSSARY.md](../../GLOSSARY.md) has the ProductOS ones.
- The member's request wins. If they asked for something specific, do that instead; "continue" is the default, not a gate.

## Verify before handing over

- [ ] The member heard where they are and what's next, in plain words.
- [ ] The owner skill is the first match in the table above, and it ran from its first step.
