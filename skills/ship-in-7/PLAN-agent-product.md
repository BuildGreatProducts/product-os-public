# Ship in 7 — plan: Agent product

*The primary shape is `agent-skill`, `agent-plugin`, `mcp-server`, or `chat-assistant`. The member arrives with an idea, or with a working build (a skill folder, a plugin manifest, server code, an assistant's instructions) that only runs in their own setup. Seven sessions to the shape's Live-means bar: a stranger installs or connects it from a public link and gets the first successful output on the first try.*

**Honest note at enrol:** official directories (Anthropic's plugin directory, the Cursor Marketplace, ChatGPT's app directory, the GPT Store) review submissions on their own clock, which may not fit inside the week. Unless the shape file's Live means says otherwise, the bar is met by a public install path the member controls — their own plugin marketplace repo, a public skill repo, an MCP Registry entry and hosted endpoint, a shareable assistant link — and the official listing is submitted and logged as pending. Say so before writing the plan.

## The seven sessions

| Day | Block | Skill(s) | Proof | Hours |
| --- | --- | --- | --- | --- |
| 1 | **Define + shape** | idea: `define-offer-builder` → `define-customer-persona` → `define-pricing`, one sitting; existing build: `define-from-code` → `define-offer-review`. Then confirm `## Product Shape` (run `define-product-shape` if enrol didn't) | `docs/DEFINE.md` has Summary, Offer, Product Shape, Persona and Pricing filled; the offer read out loud | 2.5 |
| 2 | **Identity + copy** | `design-identity-creator` → `design-ux-writing`, adapted to the shape: command and skill names, the skill or tool descriptions, first-run and error messages | the Product Identity in `docs/DESIGN.md`; `docs/COPY.md` with the naming and description rules | 2 |
| 3 | **Magic moment, PRD + evals** | `design-magic-moment` (the first successful output) → `develop-prd-roadmap`, MVP scoped to that one job (existing build: its existing-codebase mode, a gap roadmap) → `develop-agent-evals` | `docs/PRD.md`, `docs/ROADMAP.md` with one phase; `docs/EVALS.md` with at least three scenarios and pass criteria | 2.5 |
| 4 | **Build** | `develop-build` (or `build-loop` task by task), running the evals after each task | the first successful output from a clean install, as a transcript or screenshot saved to `docs/` | 4 |
| 5 | **Evals pass + quality gate** | run every scenario in `docs/EVALS.md` and fix until they pass; `develop-code-review` → `develop-security-audit` (bundled scripts and hooks, tool scopes, secrets, untrusted input and prompt injection, OAuth for a remote server) → Critical/High fixed | eval results logged in `docs/EVALS.md`, all passing; `docs/SECURITY-AUDIT.md` verdict; Critical/High ticked | 2.5 |
| 6 | **Listing + publish** | `design-marketplace-listing` → `develop-golive` (the shape's publish path: repo, marketplace entry, registry, hosted endpoint, store submission) → work `docs/DEPLOY.md` | `docs/MARKETPLACE-LISTING.md`; the public install command, listing, or registry URL; official-directory submissions confirmed | 2.5 |
| 7 | **A stranger installs it** | someone who isn't the member installs or connects it from the public link, in a clean session on their own machine or account, and asks for the documented first output; fix what it finds; post the install link where your customers are (stretch) | **the shape's Live-means bar passed**: the stranger's transcript or screenshot; the post's link (stretch) | 2 |

## Notes for the composer

- **The evals are this plan's tests.** An agent product that works once in the member's session proves nothing; `docs/EVALS.md` is how Day 4's build and Day 5's gate know it works for anyone. For a skill, include trigger scenarios (fires when it should, stays quiet on neighbouring requests).
- **Words, not Look.** There are no screens to design. Day 2's copy work is the product's interface: names, descriptions, and messages are what the agent and the user read. The shape file's Design route says whether a Lite design system (brand tokens for listing images and a docs page) is worth adding; if it is and hours allow, add it to Day 6 before the listing.
- **The security audit still runs for instructions-only products.** A skill or assistant directs an agent with the user's permissions; a chat assistant with no backend is audited on its instructions, knowledge files, and actions — what a user could extract or trigger.
- **Existing builds skip what's current.** A working build with a current `docs/DEFINE.md` drops Day 1 to a 30-minute offer review and shape confirmation; a current `docs/PRD.md` drops Day 3 to the evals alone. Spend the freed hours on Day 5 and on testing in a second host tool or client.
- **The stranger is the bar.** A friend counts if they install from the public link on their own setup; the member's own machine never does. Paid products give the stranger a free key or private-repo invite for the test — the sale is Sell in 30's bar, not this one.

## Compression (a missed or short session)

Actions, in order — use the first that fits:

1. Drop Announce.
2. Merge Day 2 into Day 3: identity in a paragraph from `docs/DEFINE.md`; `docs/COPY.md` covering only names and descriptions.
3. Merge Day 6 into Day 5's afternoon: the listing drafted from `docs/DEFINE.md` and published on the member's own install path; official-directory submissions follow after the challenge.

**Constraints** (rules, not steps — no action above may break them):

- Never publish before the evals pass and the gate's Critical/High are fixed.
- Never count the member's own install as the stranger test.
- Never move the stranger test past Day 7.

## What Day 7 looks like

Someone who isn't the member found the public link, installed or connected it in a clean setup, asked for the one job, and got the output the listing promised — first try. The official directory listing may still be in review. The announcement post is a bonus.
