---
name: define-customer-persona
description: >-
  Builds an evidence-backed Customer Persona from the Product Offer, with live market research and
  section-by-section critique, and writes the Customer Persona section of docs/DEFINE.md. Use after
  the offer is drafted, when the user says "build my customer persona", "who is my ideal customer",
  "create an ICP", or "target customer profile". Requires the Product Offer section of
  docs/DEFINE.md. Not for critiquing the offer — use define-offer-review; not for extracting a
  persona from an existing product — use define-from-code.
---

# Define: Customer Persona

Turn the member's **Product Offer** into a sharp, evidence-backed **Customer Persona** by walking the worksheet section by section — researching the customer, proposing hypotheses, and critiquing weak answers against the worksheet's own Good/Bad criteria. The goal is a real, recognizable human with specific tools, communities, prices, and frustrations, not a fuzzy demographic ("millennial founders") or an aspirational caricature ("tech-savvy decision-maker"). Treat the member as a peer working through a hard problem, not a form to fill in — and push back when answers are weak: collapsing into agreement is the worst outcome.

## Inputs

Read inputs from `docs/` and the worksheets from `productos/define/` at the app repo root.

1. **`## 1. Product Offer`** (and `## Summary`) in `docs/DEFINE.md` — **required**. If it is missing, a placeholder, or vague ("our customer is small businesses"), stop and point the member to `define-offer-builder` (or `define-offer-review` to tighten it). A persona built on a fuzzy offer inherits the fuzziness, and the session turns into re-deriving the offer.
2. **`2-Customer-Persona.md`** — the worksheet's section structure, prompts, and `> Good/Bad` criteria. Read it; never write to it.
3. **`BONUS-Customer-Persona-Examples.md`** — read once at the start to calibrate what "good" looks like across business models. Calibration, never a template to copy — the member's persona must be their own.

If any of these files are missing, ask the member where they live before continuing.

## Workflow

The session is designed for 45–75 minutes. **All research is Claude's job during the session** — named tools, subreddits, anchor prices, verbatim pain language. The member's job is to confirm or correct the research-backed proposals and approve the write.

### 1. Absorb the offer and form a working hypothesis

Read the Product Offer end-to-end and extract the Customer, Pain, Outcome, Mechanism (often hints at where the customer hangs out and what tools they use), and Guarantee and Proof (hints at price sensitivity and trust signals).

Form a working hypothesis of the persona's role, context, and likely business model (vertical B2B SaaS, indie tool, productized service, consumer subscription, dev tool, marketplace, etc.). State it back in 2–3 sentences and get it confirmed or corrected **before** researching — a 30-second check saves a wrong-direction research detour.

### 2. Research the customer

The persona names specific tools, communities, prices, podcasts, and people — facts that come from the world, not the member's head. Use web search and any connected research tools to investigate:

- **Role and context** — typical job title, team size, day-to-day workflow, where the role sits in an org or household.
- **Named tools** — 3–5 specific apps already in their stack, not "productivity tools".
- **Communities** — named subreddits, Discord servers, Slack groups, Facebook groups, not "social media".
- **Trusted voices** — named newsletters, podcasts, and practitioners, not "influencers".
- **Anchor products and pricing** — what they already pay for, and the prices they consider normal / expensive / cheap.
- **Pains in their own words** — verbatim complaints from forums, reviews, or podcast episodes; evidence for Triggers and Pains & Frustrations.

Collect 8–12 concrete data points before walking the framework, noting which came from research and which still need the member's validation (this feeds the sources entry).

If web search isn't available, say so, ask the member for comparables, and mark those claims unverified.

### 3. Walk the persona, section by section

Go through the worksheet in order: **Header → 1 Identity → 2 Problem Context → 3 Behaviors & Habits → 4 Tools & Tech Fluency → 5 Job-to-be-Done → 6 Triggers → 7 Current Alternatives → 8 Pains & Frustrations → 9 Decision Criteria & Objections → 10 Willingness to Pay → 11 Watering Holes → 12 Anti-Persona.** One section at a time by default; if the member explicitly asks to batch, oblige, but warn that quality usually drops and offer a second pass on the diagnostic sections (Header, 2, 8, 10, 12).

For each section:

1. **Propose a hypothesis** from the offer + research. Be specific — not "they're frustrated" but "they're tense around Sunday 9pm after the kids are in bed, with a glass of wine and a stack of receipts."
2. **Ask 1–3 targeted questions** to confirm, refine, or reject it — not "tell me about your customer" but "is this the moment the problem hurts, or is it actually Monday morning when the bookkeeper emails?"
3. **Critique weak answers.** Quote the worksheet's "bad" criteria when an answer drifts. Common offenders: "all the time", "various", "tech-savvy", "depends" / "it depends", "I'd have to ask", "anyone who isn't our customer", "Twitter", "industry events".
4. **Recommend a sharper version**, drawing on the examples and research: instead of "they use spreadsheets" → "Maria maintains a parallel Google Sheet because Dentrix's aging report doesn't match the bank deposits."
5. **Do the best you can in the session.** If the member can't confirm from memory, accept the research-backed best guess, tag it `[research-backed; confirm in next 5 customer interviews]`, and continue. A research-backed draft tagged for validation is a successful output — more useful than a fake answer or a stalled session; customer interviews are a normal next phase, not a precondition for being done.

### 4. Sections that deserve extra scrutiny

If these are weak, the whole persona is weak:

- **Header tagline.** Names *the job* and *the obstacle* in one sentence. A demographic ("busy moms with babies") is not done.
- **Problem Context (2).** A specific moment, place, device, and mood. "On their phone" is not a context; "3:17am one-handed on his iPhone with a baby on his chest" is.
- **Pains & Frustrations (8).** Each pain specific enough that *one design decision* could fix it. "It's clunky" is not a pain; "I have to maintain a parallel Google Sheet to cross-check the PMS's aging report against the bank" is.
- **Willingness to Pay (10).** Real numbers and named anchor products. If the member can't name three competitors with prices, they don't yet know the price ceiling — say so.
- **Anti-Persona (12).** The strongest test of understanding: a *recognizable lookalike* with a *reason they'd churn* and a *gating signal that filters them out at signup*. If the member can't draft one from memory, propose one from research + offer and tag it for validation rather than blocking the session.

### 5. Write the Customer Persona section of `docs/DEFINE.md`

Write to `docs/DEFINE.md` following the header rules in `productos/define/DEFINE-TEMPLATE.md` (create it from the template only if the member pointed you to an offer held elsewhere; write only `## 2. Customer Persona`, the `### Customer Persona` entry under `## Sources`, and the `*Last updated:*` line). If the section is already filled, show the member a diff and get approval before overwriting, surfacing any conflicts with their own edits. If it carries `define-from-code`'s italic *Extracted draft* line, remove that line once the member approves the rewrite.

- One `###` heading per worksheet section, same names and order (`### Header`, `### Identity` … `### Anti-Persona`), as clean answers. Keep the worksheet's field labels (**Persona:**, **Tagline:**) where they carry the answer, and keep any tables. `### Header` carries the persona's role-based **name** and **tagline**.
- Keep validation tags on the sections they apply to, and end the section with one short evidence line — e.g. "Based on: the Product Offer, 4 web research passes (Reddit, G2, podcast transcripts), 0 customer interviews. Recommended next step: 5 customer interviews to validate Problem Context, Triggers, Pains, Willingness to Pay."
- The `### Customer Persona` sources entry lists the URLs, communities, and posts behind the research — personas decay, and sources let the member re-date them.

Spell out acronyms (ICP, JTBD, MRR) on first use — `docs/DEFINE.md` is the document the member shares.

### 6. Verify before delivering

- [ ] No answer contains the vague offenders listed in step 3.3 — fix them or explicitly flag them for the member.
- [ ] A stranger reading only the persona could recognize this person in a coffee shop: a specific role with a specific moment, place, mood, and device.
- [ ] Tools, communities, podcasts, and people are **named** — no categories like "social media" or "industry leaders".
- [ ] Real numbers — frequencies, prices, satisfaction scores, dollar costs — and verbatim pain language where possible.
- [ ] The anti-persona is sharp enough to inform a signup-gating rule; if not, it's tagged for live validation (a normal output, not a failure).
- [ ] The `*Last updated:*` line is current and the sources entry is filled — an undated persona is a future fight about "who's the customer again?"
- [ ] `2-Customer-Persona.md` is untouched.

Give the member the file path (`docs/DEFINE.md`) and a one-paragraph summary of what is solid and what still needs validation.

**Next:** `define-pricing` fills `## 3. Pricing Strategy` (or `define-product-shape` first, if `## Product Shape` is still empty); alongside it, book 3–5 short customer conversations to sharpen the tagged sections and re-run this skill with the new evidence.
