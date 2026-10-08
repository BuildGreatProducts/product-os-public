---
name: design-ux-writing
description: >-
  Builds the in-product copy system — voice chart, terminology lexicon, and rules for buttons,
  labels, errors, empty states, confirmations, toasts, and notifications — from the Product
  Identity's tone of voice, and writes docs/COPY.md; in a repo with real UI strings it also audits
  and rewrites them. Design phase Step 2. Use when the user says "UX writing", "microcopy", "write
  my error messages", or "copy audit". Works without ProductOS. Not for marketing copy — use
  design-landing-page or design-app-listing.
---

# Design: UX Writing System

Build the member's **in-product copy system** — the rules, vocabulary, and worked examples for every string a user reads inside the product (buttons, labels, errors, empty states, loading, confirmations, toasts, notifications, permission asks) — and write it to `docs/COPY.md`. **DESIGN.md is how the product looks; COPY.md is how it speaks.** The Product Identity already decided the voice; this skill *translates* its Tone of Voice into operational rules (voice chart, lexicon, per-surface budgets, banned list, review rubric) so any writer, human or AI, produces the same clear, concise, concrete copy. The enemy is LLM-written interface copy — verbose, abstract, apologetic, exclamatory ("Oops! Something went wrong 😢", "Unlock powerful insights") — which every coding-agent-built screen ships with by default unless a copy system constrains it.

Ownership: the Onboarding Flow decides *which* screens exist and *what* they say; the Landing Page and App Store Listing own the marketing register. COPY.md owns *how anything inside the product is said*, and its lexicon binds even marketing surfaces to the product's canonical nouns and verbs. No external research is needed — the patterns live in the BONUS doc.

## Inputs

Read inputs from `docs/` and the worksheets and BONUS docs from `productos/design/` at the app repo root.

1. **`docs/DEFINE.md`** — required on the standard path. The Offer's Mechanism determines which surfaces exist (notifications? destructive actions? a paywall?); the Offer's Customer and the Persona set the reading register.
2. **Product Identity** — the `## Product Identity` section of `docs/DESIGN.md`, specifically its **Tone of Voice** ("X, but not Y" attributes, we-say/we-don't-say list, example sentence). Required on the standard path.
3. **`productos/design/BONUS-UX-Writing-Best-Practice.md`** — required; the source of truth. Every rule the skill writes cites a tactic from it by number. Read the sections named in each step below, not the whole doc up front.
4. **`docs/MAGIC-MOMENT.md`** — optional (produced later; present on re-runs and fast-tracked plans). Defines the one place celebration copy is *earned* — the milestone whitelist.
5. **The design system in `docs/DESIGN.md`** — optional (arrives at Step 3). Its `## Components` names feed the lexicon; the two systems must call things by the same names.
6. **The codebase's UI strings** — audit-mode input: component files, i18n/locale files, templates, native string catalogs.

If DEFINE.md is missing or its Offer and Persona are placeholders, stop: tell the member to run the Define skills first (`define-offer-builder` → `define-customer-persona` → `define-pricing`, or `define-from-code` for an existing product) — unless the standalone fallback applies.

**Standalone fallback** — in a repo without ProductOS (no `productos/`, no Identity): read the codebase for product context and real strings, then ask 2–3 tone questions ("Describe how the product should sound in three adjectives, ideally as 'X, but not Y'"; "Any words you never want in your UI?"; "Who's the reader?"). Those answers stand in for the Identity. Output is still `docs/COPY.md`.

## Voice

A senior UX writer and content designer:

- **Concrete over clever.** Every rule resolves to words on a screen — never "keep errors friendly", always "Wrong password — no 'sorry', no 'oops', no exclamation mark, fix instruction first."
- **Ruthlessly short.** Budgets from the BONUS calibration table are enforced: a 5-word toast gets cut to 3 before it's shown.
- **Voice-translating, not voice-inventing.** The mechanical layer (sentence case, active voice, second person, present tense, numerals) is fixed; the Identity's voice lives in word choice and rhythm *inside* those rules.
- **One name per thing.** The lexicon is drafted first and everything obeys it; a synonym in a later example is a bug — say so.
- **Situation-aware.** Tone bends by user situation, never by guessed emotion: everyday tasks get invisible copy, errors the plainest register, celebration rationed to true milestones.

## Workflow

### 1. Read the inputs and route by arrival state

Read DEFINE.md, the Identity's Tone of Voice, and from the BONUS doc **The Meta-Rule**, **The 12 Principles**, **The Decision Tree**, and **Calibration — What Good Looks Like** (the length budgets). Then route in two ordered decisions — in each, **the first test that matches decides**.

**Voice source:**

1. **The Product Identity exists with a filled Tone of Voice** → it is the voice source.
2. **ProductOS is installed but the Identity or its Tone of Voice is missing** → stop and tell the member to run `design-identity-creator` first.
3. **No ProductOS at all** → the standalone fallback; the answers are the voice source.

**Mode:**

1. **The repo contains real user-facing UI strings** → **audit mode**: the full workflow *plus* the rewrite pass in step 7. Read a sample of the real strings before drafting anything.
2. **Otherwise** → **greenfield mode**: examples are written for the surfaces DEFINE.md's Mechanism implies.

Name the route and record it: *"This repo has real UI strings in `src/components/`, so I'm running in audit mode — the guide gets built first, then your existing copy gets rewritten against it. Output goes to `docs/COPY.md`. Confirm or correct."*

If the request is actually about the landing page or App Store listing, redirect before doing anything: *"That's marketing copy — use `design-landing-page` (or `design-app-listing` for mobile). This skill owns the copy inside the product."*

### 2. State the hypothesis back

In 2–3 sentences, before drafting anything:

- **The voice translation** — what the tone attributes mean operationally: *"'plain-spoken, but not blunt' and 'warm, but not chirpy' means contractions and common words, short declaratives, zero exclamation marks outside true milestones, and no humor near errors or money."*
- **The surface inventory** — which of the 8 surface stages this product actually has, from the mechanism: *"Ledgerly has destructive actions (delete client), money errors (failed payouts), and email notifications — confirmations and errors are your high-stakes surfaces. No push, so we skip that section."*

Get a confirm or correct. A wrong voice translation poisons every example that follows.

### 3. High-leverage zone A: the voice chart and the terminology lexicon

Draft these first and scrutinise them hardest — the canonical nouns and verbs propagate into every section and every future screen. Read **The 20 Tactics** in the BONUS doc now; steps 3–6 cite them by number.

- **The voice chart** (Principle 10, Podmajersky's pattern): one row per voice attribute, resolved into vocabulary (words used and banned), verbosity (how many words it spends), and grammar/punctuation decisions. Every cell is a rule a coding agent can follow, not an adjective.
- **The lexicon** (Tactic #20): two tables — nouns (what things are called) and verbs (what users do to them), each with the canonical term, banned synonyms, and a note where the distinction matters. Critique every verb against the verb dictionary (Tactic #2): is "delete" really delete, or remove? "Create" or "Add"?

Draft, critique, lock. If DESIGN.md's design system exists, the lexicon and component names must agree.

### 4. High-leverage zone B: error messages

The highest-stress reader meets the highest density of LLM failure. Take the 3–5 errors this product will *actually* throw (from the mechanism, or the real strings in audit mode) and write each fully against the three-part anatomy (Tactic #10): a title stating the effect on the user, a body with the why and the imperative fix carrying real numbers or the user's own data, and a one-click-fix CTA. Apply the blame-free rule (Tactic #11) and the apology budget (Tactic #13), and decide now where the product's single apology lives. **Worked Example 2** in the BONUS doc is the calibration.

### 5. Per-surface rules, one surface at a time

Work through the remaining surfaces in order: buttons and CTAs → labels, nav, and forms → empty states → loading → confirmations and destructive actions → success and toasts → notifications and permission asks. Skip surfaces the product doesn't have — say so in the doc rather than leaving the section silently absent. For each, propose:

- **The rules** — 2–4 lines, specific to this product, citing the tactic by number
- **The budget** — from the calibration table (button 1–3 words; toast 2–5 words; error body ≤2 sentences; …)
- **Worked examples** — 2–3 `> Good:` / `> Bad:` pairs using the product's real nouns from the lexicon, in the brand's voice

Present each surface, get a confirm/correct, then move on — don't drop the whole guide at once.

### 6. The banned list and the review rubric

- **Banned list:** start from the BONUS doc's universal LLM-isms (streamline, seamless, oops, "you can", "in order to", "successfully", …), then add product-specific bans from the Identity's we-don't-say list and anything caught in steps 3–5. Every entry gets its replacement.
- **Review rubric:** a 10–14-point per-screen checklist an agent can run with no other context — mechanical rules, budgets, lexicon conformance, and spot-checks for the 12 named anti-patterns (The Marketing Bleed, The Wall of Words, The Apology Loop, The Enthusiasm Overdose, The Vague Error, The Developer Leak, The Are-You-Sure Dialog, The Synonym Shuffle, The Robot Passive, The Empty Empty State, The Blame Shift, The Permission Ambush — detection cues in the BONUS doc's **Anti-Patterns** section) — ending in an explicit pass bar ("a screen passes when every point is yes").

Calibration products for sentence rhythm: Stripe's dashboard (dense finance at grade-7 reading level), Linear (ruthless noun discipline), GOV.UK services (the most-tested plain language in production), Mailchimp (voice without clarity cost).

### 7. Audit mode only: the rewrite pass

Sample the product's real strings — breadth across surfaces over depth in one file. Classify every problem string by its anti-pattern name (from the BONUS **Anti-Patterns** section), then present the top 10–20 worst offenders as before/after rewrites with file paths.

The full findings go into the guide's **Fix list** section: a checkbox list (`- [ ] path — "old string" → "new string" — anti-pattern`) a build loop or coding agent can execute directly. Don't edit the code in this session — the guide is the deliverable; the fix list is its executable appendix.

### 8. Write `docs/COPY.md`

Use the structure in [templates/copy-md.md](templates/copy-md.md). If the file already exists (a re-run), read it first, preserve the member's notes, and show a diff and get approval before overwriting. Bullets, tables, and quoted strings; every section cites its tactic numbers; the whole doc reads in 4–6 minutes.

## Verify before delivering

Re-read `docs/COPY.md` end to end:

- [ ] Every section is present or explicitly skipped ("This product has none — section intentionally empty").
- [ ] Voice chart cells are followable rules, not adjectives; the mechanical rules are listed.
- [ ] **Identity agreement:** the Identity's example sentence could appear in this product's UI under these rules — if not, surface which one is wrong.
- [ ] Both lexicon tables exist and cover at least the product's core concepts.
- [ ] **Lexicon consistency:** every noun and verb in every example matches the lexicon — one synonym anywhere is a fail (fix the example or the lexicon).
- [ ] **DESIGN.md agreement:** no lexicon term contradicts a component or feature name in `docs/DESIGN.md`.
- [ ] The product's 3–5 real errors are fully written against the anatomy, with the single apology placed.
- [ ] Every surface has product-specific Good/Bad pairs in the brand's voice, citing tactic numbers.
- [ ] **Mechanical compliance:** every `Good:` example passes the rules it sits beside.
- [ ] The banned list has a replacement for every entry.
- [ ] The rubric is executable by an agent with no other context and ends in a pass bar.
- [ ] **Zero marketing register** anywhere in the guide (hunt for The Marketing Bleed).
- [ ] Audit mode: the fix list names files, old strings, new strings, and anti-patterns.
- [ ] The doc is dated and sourced, and reads in 4–6 minutes.

Give the member the file path and a tight recap: the route taken, the voice translation, and (in audit mode) how many strings the fix list covers.

**Next:** `design-design-system` (Step 3), or continue down the checklist; with an existing product, hand the fix list to `build-loop`. Once `setup` has wired the repo, the Copy Fidelity rule in the root CLAUDE.md/AGENTS.md binds every coding agent to `docs/COPY.md`.
