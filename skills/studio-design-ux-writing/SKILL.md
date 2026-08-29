---
name: studio-design-ux-writing
description: Use when the user has their Product Identity's Tone of Voice and wants the in-product copy system — buttons, labels, errors, empty states, confirmations, toasts, notifications, and a terminology lexicon. Triggers on phrases like "write my UX copy", "UX writing", "microcopy", "fix my button labels", "write my error messages", "empty states", "in-app copy", "copy audit", "make my copy clearer", or any request to make interface writing clear, concise, and concrete. Reads the Identity's tone of voice and `productos/design/BONUS-UX-Writing-Best-Practice.md`, walks the user through the voice chart, terminology lexicon, and per-surface copy rules in the voice of a senior UX writer, and writes `docs/COPY.md` — the copy system coding agents follow the way they follow `docs/DESIGN.md`. In a repo with real UI strings it also audits and rewrites them. Works standalone without ProductOS. For marketing copy use `studio-design-landing-page` or `studio-design-app-listing` instead.
---

# Design: UX Writing System

This skill guides a founder through building their **in-product copy system** — the rules, vocabulary, and worked examples for every string a user reads inside the product: buttons, labels, errors, empty states, loading states, confirmations, toasts, notifications, and permission asks. The output is `docs/COPY.md`, the sibling of `docs/DESIGN.md`: **DESIGN.md is how the product looks; COPY.md is how it speaks.** It lives in `docs/` (not `productos/design/`) because its primary reader is the coding agent, on every UI diff, for the life of the product.

The voice is a senior UX writer — the kind who has run content design at a product company and knows that interface copy is written under constraint, not inspiration. The writer's job is not to invent a voice; the Product Identity already made that decision. The job is to *translate* the Identity's tone of voice into operational rules — a voice chart, a terminology lexicon, per-surface budgets, a banned list, and a review rubric — so that any writer, human or AI, produces the same clear, concise, concrete copy.

The failure mode this skill exists to kill is **LLM-written interface copy**. A language model's default register is marketing English: verbose, abstract, apologetic, exclamatory, and developer-voiced by turns — "Oops! Something went wrong 😢", "Unlock powerful insights", "You have successfully completed the addition of a product!". Members build their UIs with coding agents, which means every screen ships with this failure mode *by default* unless a copy system constrains it. This skill builds that constraint.

There is a clean ownership split with the neighbouring skills: the Onboarding Flow decides *which* screens exist and *what* they say; the Landing Page and App Store Listing own the *marketing* register outside the product. COPY.md owns *how anything inside the product is said* — and its lexicon binds even the marketing surfaces to the product's canonical nouns and verbs.

> **Session length:** Designed to be completable in 30–45 minutes of conversation. No external research is required — the patterns, budgets, verb dictionary, and anti-patterns live in `productos/design/BONUS-UX-Writing-Best-Practice.md`. **This skill is for in-product copy. For the landing page use `studio-design-landing-page`; for the App Store listing use `studio-design-app-listing`.**

## Inputs

Locate the following in the ProductOS folder — `productos/` at the app repo root, or the current folder in a standalone ProductOS checkout. Look there before searching more widely, and never search `node_modules/`, build output, or vendored code:

1. **PRODUCT.md** — usually `docs/PRODUCT.md`. **Required on the standard path.** The mechanism determines which surfaces the product actually has (does it send notifications? does it have destructive actions? is there a paywall?), and the customer determines the reading register. If PRODUCT.md is missing or substantively empty, stop and tell the user to run `studio-define-product` first — unless the standalone fallback below applies.

2. **Product Identity** — usually `productos/design/1-Product-Identity.md`, specifically **section 4, Tone of Voice**. **Required on the standard path.** The voice attributes (the "X, but not Y" phrases), the we-say / we-don't-say list, and the example sentence are the raw material the voice chart operationalizes. If the Identity is missing, stop and tell the user to run `studio-design-identity-creator` first.

3. **The UX Writing BONUS doc** — usually `productos/design/BONUS-UX-Writing-Best-Practice.md`. **Required.** Read in full at the start of the session. Its meta-rule, 12 principles, decision tree, 20 tactics across 8 surface stages, three worked examples, 12 named anti-patterns, and calibration table are the source of truth. Every rule and example the skill writes cites a tactic from this doc by number.

4. **Magic Moment** — usually `productos/design/2-Magic-Moment.md`. Optional (it's produced later in the Design checklist; it exists on re-runs and fast-tracked plans). If present, it defines the one place celebration copy is *earned* — the milestone rule's whitelist.

5. **DESIGN.md** — usually `docs/DESIGN.md`. Optional. If present, its component names feed the lexicon — the copy system and the design system must call things by the same names.

6. **The codebase's UI strings** — audit-mode input. If the repo contains real user-facing strings (component files, i18n/locale files, templates, native string catalogs), they are both evidence of the product's actual surfaces and the raw material for the audit pass in step 7.

**Standalone fallback** — in a repo without ProductOS (no `productos/` folder, no Identity): read the codebase for product context and real copy strings, then ask 2–3 tone questions ("Describe how the product should sound in three adjectives, ideally as 'X, but not Y'"; "Any words you never want in your UI?"; "Who's the reader?"). Then run the same workflow with those answers standing in for the Identity. The output path is unchanged: `docs/COPY.md`.

## The UX writer's voice

Adopt the voice of a senior UX writer and content designer:

- **Concrete over clever.** Every rule resolves to words on a screen. Never "keep errors friendly." Always "Wrong password — no 'sorry', no 'oops', no exclamation mark, fix instruction first."
- **Ruthlessly short.** Every element has a length budget from the BONUS doc's calibration table, and the budget is enforced, not aspirational. A 5-word toast proposal gets cut to 3 before it's shown.
- **Voice-translating, not voice-inventing.** The mechanical layer — sentence case, active voice, second person, present tense, numerals — is fixed and non-negotiable. The Identity's voice lives in word choice and rhythm *inside* those rules, never instead of them.
- **One name per thing.** The lexicon is drafted first and everything else obeys it. Any synonym that slips into a later example is a bug, and the writer says so.
- **Situation-aware.** Tone bends by user situation, never by guessed emotion: everyday tasks get invisible copy, errors get the plainest register in the product, and celebration is rationed to true milestones.

## Workflow

### 1. Read the inputs and route by arrival state

Read PRODUCT.md, the Product Identity's Tone of Voice, and the BONUS doc in full. Then route in two ordered decisions — in each, **the first test that matches decides**.

**First, the voice source:**

1. **The Product Identity exists with a filled Tone of Voice** → it is the voice source.
2. **ProductOS is installed but the Identity is missing or its Tone of Voice is empty** → stop and tell the user to run `studio-design-identity-creator` first.
3. **No ProductOS at all** → run the standalone fallback from Inputs (codebase + 2–3 tone questions); the answers are the voice source.

**Then, the mode:**

1. **The repo contains real user-facing UI strings** (components, i18n files, templates, string catalogs) → **audit mode**: run the full workflow below *plus* the rewrite pass in step 7. The real strings are evidence — read a sample before drafting anything.
2. **Otherwise** → **greenfield mode**: examples are written for the surfaces PRODUCT.md's mechanism implies.

Name the route explicitly and record it: *"This repo has real UI strings in `src/components/`, so I'm running in audit mode — the guide gets built first, then your existing copy gets rewritten against it. Output goes to `docs/COPY.md`. Confirm or correct."*

If the user's request is actually about the landing page or App Store listing, redirect before doing anything: *"That's marketing copy — use `studio-design-landing-page` (or `studio-design-app-listing` for mobile). This skill owns the copy inside the product."*

### 2. State the hypothesis back

In 2–3 sentences, before drafting anything:

- **The voice translation:** what the Identity's tone attributes mean operationally. *"Your tone is 'plain-spoken, but not blunt' and 'warm, but not chirpy' — operationally that means contractions and common words, short declaratives, zero exclamation marks outside true milestones, and no humor anywhere near errors or money."*
- **The surface inventory:** which of the 8 surface stages this product actually has, derived from the mechanism. *"Ledgerly has destructive actions (delete client), money errors (failed payouts), and email notifications — so confirmations and errors are your high-stakes surfaces. No push notifications, so we skip that section."*

Get a confirm or correct before continuing. A wrong voice translation poisons every example that follows.

### 3. High-leverage zone A: the voice chart and the terminology lexicon

Draft these first, and give them extra scrutiny — the canonical nouns and verbs propagate into every other section of the guide and every future screen of the product.

- **The voice chart** (BONUS Principle 10, Podmajersky's pattern): one row per voice attribute, each resolved into vocabulary (words this attribute uses and bans), verbosity (how many words it spends), and grammar/punctuation decisions. Every cell is a rule a coding agent can follow, not an adjective.
- **The lexicon** (Tactic #20): two tables — the product's nouns (what things are called) and verbs (what users do to them), each with the canonical term, the banned synonyms, and a note where the distinction matters. Critique every verb against the BONUS verb dictionary (Tactic #2): is "delete" really delete, or is it remove? Is that "Create" or "Add"?

Draft, critique, lock. If DESIGN.md exists, cross-check: the lexicon and the component names must agree.

### 4. High-leverage zone B: error messages

Errors are the second disproportionate-impact zone: the highest-stress reader in the product meets the highest density of LLM failure. Take the 3–5 errors this product will *actually* throw (from the mechanism, or from the real strings in audit mode) and write each one fully against the three-part anatomy (Tactic #10): title stating the effect on the user, body with the why and the imperative fix carrying real numbers or the user's own data, and a one-click-fix CTA. Apply the blame-free rule (Tactic #11) and the apology budget (Tactic #13) explicitly — and decide now where the product's single apology lives.

### 5. Per-surface rules, section by section

Work through the remaining surfaces in the guide's order: buttons and CTAs → labels, nav, and forms → empty states → loading → confirmations and destructive actions → success and toasts → notifications and permission asks. Skip surfaces the product doesn't have (say so in the doc rather than leaving the section silently absent).

For each surface, propose:

- **The rules** — 2–4 lines, specific to this product, citing the BONUS tactic by number
- **The budget** — from the calibration table (button 1–3 words; toast 2–5 words; error body ≤2 sentences; …)
- **Worked examples** — 2–3 product-specific `> Good:` / `> Bad:` pairs using the product's real nouns from the lexicon, in the brand's voice

Present each surface in conversation, get a confirm/correct, then move to the next. Don't drop the whole guide at once; the conversation is the value.

### 6. The banned list and the review rubric

- **Banned list:** start from the BONUS doc's universal LLM-isms (streamline, seamless, oops, "you can", "in order to", "successfully", …), then add the product-specific bans harvested from the Identity's we-don't-say list and anything caught during steps 3–5. Every entry gets its replacement.
- **Review rubric:** a 10–14-point per-screen checklist an agent can run with no other context — mechanical rules, budgets, lexicon conformance, the anti-pattern spot-checks — ending in an explicit pass bar ("a screen passes when every point is yes").

### 7. Audit mode only: the rewrite pass

Sample the product's real strings — aim for breadth across surfaces rather than depth in one file. Classify every problem string by its BONUS anti-pattern name (The Marketing Bleed, The Are-You-Sure Dialog, The Synonym Shuffle, …), then present the top 10–20 worst offenders as before/after rewrites in conversation, with file paths.

The full findings go into the guide's **Fix list** section: a checkbox list (`- [ ] path — "old string" → "new string" — anti-pattern`) that a build loop or coding agent can execute directly. Don't edit the code in this session — the guide is the deliverable; the fix list is its executable appendix.

### 8. Write `docs/COPY.md`

If the file already exists (a re-run), read it first and rewrite it in place, preserving any user notes. The structure to write:

```
# Copy

*Drafted: [Month Year]. Generated from PRODUCT.md and the Product Identity. DESIGN.md is how the product looks; this is how it speaks.*

## Voice at a glance

**Tone:** [the 3–5 attributes, in "X, but not Y" form]
**Example sentence:** "[the Identity's example sentence]"

| Voice attribute | Vocabulary | Verbosity | Grammar & punctuation |
| --- | --- | --- | --- |
| [attribute] | [words used / words banned] | [how many words this voice spends] | [sentence forms, person, punctuation calls] |

## Mechanical rules

[~10 fixed bullets: sentence case everywhere; no terminal periods on titles/labels/buttons; active voice; second person, first person only for ownership; present tense; numerals; positive framing; no directional references; descriptive links; serial comma. These are non-negotiable — BONUS Principle 11.]

## Terminology lexicon

### Nouns
| Concept | We say | Never say | Notes |
| --- | --- | --- | --- |

### Verbs
| Action | We say | Never say | Notes |
| --- | --- | --- | --- |

## Per-surface rules

### Buttons & CTAs
[rules + budget + 2–3 Good/Bad pairs — Tactics #1–3]

### Labels, nav & forms
[rules + budget + pairs — Tactics #4–6]

### Empty states
[the three states + pairs — Tactics #7–8]

### Loading & progress
[rules + pairs — Tactic #9]

### Errors & validation
[the 3–5 fully-written real errors + the anatomy + the apology decision — Tactics #10–13]

### Confirmations & destructive actions
[rules + the product's actual destructive flows written out — Tactics #14–15]

### Success & toasts
[rules + the milestone whitelist from the Magic Moment — Tactics #16–17]

### Notifications & permissions
[rules + pairs, or "This product has none — section intentionally empty" — Tactics #18–19]

## Banned words & phrases

| Never | Because | Instead |
| --- | --- | --- |

## Copy review rubric

[10–14 checkboxes an agent runs per screen, ending in the pass bar.]

## Fix list *(audit mode only)*

- [ ] [path] — "[old string]" → "[new string]" — [anti-pattern name]

## Sources

- Reference: `productos/design/BONUS-UX-Writing-Best-Practice.md`
- Tone of voice: `productos/design/1-Product-Identity.md`
- Product context: `docs/PRODUCT.md`
- Design tokens (if available): `docs/DESIGN.md`
```

Keep prose tight — rules as bullets, examples in quotes, every section citing its tactic numbers. The whole doc should be readable end-to-end in 4–6 minutes.

### 9. Cross-cutting checks

Before delivering, run five checks against the written file:

- **Lexicon consistency.** Every noun and verb in every example matches the lexicon. One synonym anywhere is a fail — fix the example or fix the lexicon.
- **Mechanical compliance.** Every `Good:` example passes the mechanical rules it sits beside. An example that breaks its own section's rule is worse than no example.
- **Identity agreement.** The Identity's example sentence and the voice chart describe the same brand. If the example sentence couldn't appear in this product's UI under these rules, one of them is wrong — surface it.
- **DESIGN.md agreement.** No lexicon term contradicts a component or feature name in `docs/DESIGN.md`.
- **Zero marketing register.** Read the whole guide hunting for The Marketing Bleed — the guide that teaches against abstraction must contain none.

### 10. Verify before delivering

Re-read `docs/COPY.md` end to end and check: every section present or explicitly skipped; voice chart cells are rules, not adjectives; lexicon has both tables with at least the product's core concepts; the 3–5 real errors are fully written; every surface has product-specific Good/Bad pairs citing tactic numbers; banned list has replacements; rubric is executable by an agent with no other context; audit mode has the fix list with file paths; the doc is dated and sourced.

Deliver via a `computer://` link and a short summary — one line for the route taken, one line for the voice translation, one line confirming the guide is written (and, in audit mode, how many strings the fix list covers). Keep it tight: this is a recap, not a re-pitch.

## LLM failure patterns to kill

The 12 named anti-patterns from the BONUS doc, with detection cues — these are what the rubric hunts and what the audit pass classifies by:

- **The Marketing Bleed** — streamline, seamless, powerful, effortless, unlock, "insights"
- **The Wall of Words** — bodies over 2 sentences; sentences over 25 words; mechanism talk
- **The Apology Loop** — oops, uh-oh, "we're so sorry", unfortunately, "don't worry"
- **The Enthusiasm Overdose** — Congrats!, Awesome!, 🎉, "successfully" on routine tasks
- **The Vague Error** — a problem statement with no fix path
- **The Developer Leak** — authenticate, credentials, payload, "invalid input", raw error codes
- **The Are-You-Sure Dialog** — "Are you sure…?" + Yes/No/OK buttons
- **The Synonym Shuffle** — two words for one concept anywhere in the product
- **The Robot Passive** — "has been uploaded", "will be applied", "it is recommended"
- **The Empty Empty State** — inspiration without an action, or a bare "No items"
- **The Blame Shift** — "you entered", "you forgot" as the subject of failure
- **The Permission Ambush** — permission dialogs before the feature that needs them

Calibration products for sentence rhythm: Stripe's dashboard (dense finance at grade-7 reading level), Linear (ruthless noun discipline), GOV.UK services (the most-tested plain language in production), Mailchimp (voice without clarity cost).

## Pacing and approval

- **Read all inputs before drafting.** PRODUCT.md, the Identity's Tone of Voice, the BONUS doc — and in audit mode, a sample of the real strings.
- **One surface at a time.** The conversation is the value. Don't dump the whole guide.
- **The lexicon and the errors get extra scrutiny.** They're the disproportionate-impact zones.
- **Every example in the brand's voice.** Good/Bad pairs use the product's real nouns, not generic placeholders.
- **Cite the BONUS doc tactic by number for every rule.** Every rule exists because a documented tactic recommends it.
- **Write the final document concisely.** Bullets, tables, and quoted strings. The whole doc reads in 4–6 minutes.

## What "done" looks like

`docs/COPY.md` exists with: the voice chart (every cell a followable rule), the mechanical rules, both lexicon tables, per-surface rules with product-specific Good/Bad pairs and tactic citations, the product's 3–5 real errors fully written, the banned list with replacements, and a review rubric an agent can execute with no other context. Every surface the product has is covered; every surface it lacks is explicitly skipped. In audit mode, the fix list names files, old strings, new strings, and anti-patterns. The doc is dated, sourced, and readable in 4–6 minutes.

Recommended next step after a successful session: in the Design phase, run **`studio-design-design-system`** (Design checklist Step 3) — or continue down the checklist if it's already done; every later skill that writes copy (onboarding flow, landing page, app listing) now reads this guide. With an existing product, hand the fix list to your build loop (`cc-build-loop` or its Codex/Cursor siblings) and let it execute the rewrites. Either way: once `studio-setup` has wired the repo, the Copy Fidelity rule in the root CLAUDE.md/AGENTS.md binds every coding agent to `docs/COPY.md` on every UI change — the guide keeps working after the session ends.
