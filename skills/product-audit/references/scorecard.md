# Product audit scorecard

Score each criterion **0–3** with cited evidence: **0** missing · **1** exists but weak · **2** solid with gaps · **3** strong. A phase's score is the average of its criteria that apply to the shape, rounded to one decimal. Criteria marked *(screen shapes)* apply to web-app, mobile-app, desktop-app, browser-extension, and website only.

## Contents

- [Define](#define)
- [Design](#design)
- [Develop](#develop)
- [Distribute](#distribute)
- [Stages](#stages)
- [Leverage by stage](#leverage-by-stage)

## Define

| Criterion | 3 looks like | 0 looks like |
| --- | --- | --- |
| Offer clarity | One sentence names a specific customer, an urgent pain, a measurable outcome, and a mechanism; the landing page or listing says the same thing | No written offer, or "AI tool for everyone" |
| Persona | A named, specific person with tools, communities, and willingness to pay | "Small businesses" |
| Pricing | A decided model and launch price, live at checkout, with a reason | Free by default, or "we'll figure it out" |
| Shape fit | The shape matches where the customer already works, with a rejected alternative | The shape was never chosen — it's whatever got built |

## Design

| Criterion | 3 looks like | 0 looks like |
| --- | --- | --- |
| Identity | Name, worldview, tone, and visual style are consistent across product, site, and listing | Default template look, inconsistent voice |
| Copy | Consistent terminology, clear errors and empty states (or, for agent shapes, clear tool names and descriptions) | Lorem ipsum, mixed terms, "Something went wrong" |
| Design system *(screen shapes)* | One token set, used consistently | Hardcoded hex values everywhere, competing styles |
| Magic moment & onboarding | A named first-value moment, reached in the first session by a guided path | The user lands on an empty screen (or an install with no first command) |
| Acquisition surface | The landing page / listing converts: clear promise, real proof, one CTA | No public page, or one that describes features, not outcomes |

## Develop

| Criterion | 3 looks like | 0 looks like |
| --- | --- | --- |
| Spec & plan | A current PRD and roadmap the code matches | No spec; the code is the only documentation |
| Code health | Clear structure, tests that pass, no dead platform shims | Untestable, generated sprawl, nothing runs locally |
| Security | A recent clean audit, secrets out of the repo, access rules enforced | Committed keys, open database rules, unprotected routes |
| Live & reliable | Live by the shape's *Live means* bar, with error tracking | Not live, or live with no idea when it breaks |
| Evals *(AI-native shapes)* | A scenario set that runs and passes | Output quality judged by eye |

## Distribute

| Criterion | 3 looks like | 0 looks like |
| --- | --- | --- |
| Channels | A chosen channel with a working playbook, including the shape's native channel | "We posted it once" |
| Experiments | Experiments with pass bars and logged results | No measured experiments |
| Activation | Most new users reach the magic moment; it's measured | Unknown — no instrumentation |
| Retention & revenue | Users return and pay; churn is measured | No returning users, no revenue |

## Stages

- **Idea** — no product yet. (Point to `define-phase`; this audit is for existing products.)
- **Prototype** — something runs, but it isn't live by the shape's bar.
- **Live, no users** — live, nobody outside the member's circle using it.
- **Users, no revenue** — people use it; nobody pays yet.
- **Revenue** — people pay.

## Leverage by stage

Order the plan so the weakest link for the stage comes first, after the hard rules:

- **Prototype** — get it live: Define fast-track → Product Shape → the Design steps a launch needs (identity, acquisition surface) → PRD (existing-codebase mode) → build → security → go-live. Ship in 7 can be the opening block when the member wants a deadline.
- **Live, no users** — distribution: Define fast-track and `distribute-gtm-strategy` in week one, in parallel; then the acquisition surface and onboarding if they score low.
- **Users, no revenue** — monetization and activation: pricing, checkout live, the activation-retention audit; Sell in 30 can be the opening block.
- **Revenue** — growth and robustness: experiments on the best channel, the security audit if stale, conversion review, then scale.

Within a stage, a score of 0–1 on a criterion the stage depends on outranks everything else.
