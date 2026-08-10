---
name: studio-define-customer-persona
description: Use when the user has filled out their Product Offer and wants to develop a sharp, evidence-backed Customer Persona. Triggers on phrases like "build a customer persona", "define my customer", "fill in the customer persona", "who is my ideal customer", "create an ICP", "target customer profile", "persona for my product", or any request to translate a product offer into a customer persona document. Reads the user's Product Offer, researches the target market online, then walks them section by section through the Customer Persona framework — proposing hypotheses, critiquing vague answers, and producing a filled-in customer persona document. Especially appropriate inside a ProductOS-style "Define" workflow where a Product Offer markdown file already exists and a Customer Persona template is waiting to be filled in.
---

# Define: Customer Persona

This skill turns a filled-in **Product Offer** into a sharp, evidence-backed **Customer Persona** by guiding the user, section by section, through the persona framework — researching the target customer, proposing hypotheses, critiquing weak answers against the framework's own "good vs bad" criteria, and producing a finished persona document.

The goal is not to fill in 12 sections quickly. The goal is to make the user a stranger to their own product for an hour — to force them to describe a real, recognizable human with specific tools, communities, prices, and frustrations, rather than a fuzzy demographic ("millennial founders") or an aspirational caricature ("tech-savvy decision-maker"). A sharp persona is the foundation of everything downstream — positioning, copy, growth channels, pricing — so the time spent here pays back many times over.

> **Session length:** Designed to be completable in 45–75 minutes of conversation. **All research is Claude's job during the session** — named tools, subreddits, anchor prices, verbatim pain language. The user's job is to talk through their idea, confirm or correct Claude's research-backed proposals for each section, and approve the rewrite at the end. A research-backed draft with some sections tagged for live validation is a *successful* output of this skill — customer interviews are a normal next phase, not a precondition for being done.

## Inputs

Before starting, locate three files in the ProductOS folder — `productos/` at the app repo root, or the current folder in a standalone ProductOS checkout. Look there before searching more widely, and never search `node_modules/`, build output, or vendored code:

1. **The Product Offer** — usually `1. Product Offer.md`. This is the **required** input. If sections are blank or vague ("our customer is small businesses"), stop and ask the user to tighten the offer before proceeding. A persona built on a fuzzy offer inherits the fuzziness, and you will spend the whole conversation re-deriving the offer instead of building the persona.
2. **The Customer Persona template** — usually `2. Customer Persona.md`. This defines the exact output structure to follow, **and it is also the file the skill rewrites in place** at the end (see step 5).
3. **The Customer Persona examples** — usually `BONUS - Customer Persona Examples.md`. Read this once at the start to internalize what "good" looks like across business models (B2B SaaS, agent-native app, AI-enabled service, consumer subscription, developer tool). Use them as **calibration**, never as templates to copy from — the user's persona must be their own.

If any of these files are missing, ask the user where they live before continuing.

## Workflow

### 1. Absorb the offer and form a working hypothesis

Read the Product Offer end-to-end. Extract:

- The customer description (section 1)
- The current pain (section 2)
- The outcome (section 3)
- The mechanism (section 4) — often hints at where the customer hangs out and what tools they already use
- The guarantee and proof (sections 5, 6) — hint at price sensitivity and trust signals

From this, form a working hypothesis of the persona's role, context, and likely business model (vertical B2B SaaS, indie tool, productized service, consumer subscription, dev tool, marketplace, etc.). State this hypothesis back to the user in 2–3 sentences and ask them to confirm or correct it **before** doing research. A wrong starting hypothesis wastes the entire research budget.

### 2. Research the customer

Spend real effort here. The persona's job is to name specific tools, communities, prices, podcasts, and people — and those facts come from the world, not the user's head. Use web search and any connected research tools to investigate:

- **Role and context** — typical job title, team size, day-to-day workflow, where this role sits in an org or a household
- **Named tools** — what is already in their stack (3–5 specific app names, not "productivity tools")
- **Communities** — subreddits, Discord servers, Slack groups, Facebook groups they actually gather in (find names, not categories like "social media")
- **Trusted voices** — newsletters, podcasts, and individual practitioners they follow (find named people, not "influencers")
- **Anchor products and pricing** — what existing tools they already pay for, and the price points they consider normal / expensive / cheap
- **Pains in their own words** — pull verbatim complaints from forums, reviews, or recent podcast episodes; these become evidence for sections 6 (Triggers) and 8 (Pains & Frustrations)

Collect 8–12 concrete data points before walking the user through the framework. Note explicitly which points came from research and which still need user validation — this matters when you write the sources section later.

### 3. Walk the user through the persona, section by section

Go through the template in order: **Header → 1 Identity → 2 Problem Context → 3 Behaviors & Habits → 4 Tools & Tech Fluency → 5 Job-to-be-Done → 6 Triggers → 7 Current Alternatives → 8 Pains & Frustrations → 9 Decision Criteria & Objections → 10 Willingness to Pay → 11 Watering Holes → 12 Anti-Persona.**

For each section:

1. **Propose a hypothesis** based on the offer + research. Be specific — not "they're frustrated" but "they're tense around Sunday 9pm after the kids are in bed, with a glass of wine and a stack of receipts."
2. **Ask 1–3 targeted questions** to confirm, refine, or reject the hypothesis. Don't ask open-ended "tell me about your customer" questions — ask "is this the moment the problem hurts, or is it actually Monday morning when the bookkeeper emails?"
3. **Critique weak answers.** Each section in the template has explicit "good" and "bad" criteria — quote them when the user's answer drifts into the "bad" column. Common offenders: "all the time", "various", "tech-savvy", "depends", "I'd have to ask", "anyone who isn't our customer", "Twitter", "industry events".
4. **Recommend a sharper version**, drawing on the BONUS examples and on research. For instance, instead of "they use spreadsheets" → "Maria maintains a parallel Google Sheet because Dentrix's aging report doesn't match the bank deposits."
5. **Do the best you can in the session.** If the user can confirm or correct from memory, great. If they can't, accept Claude's research-backed best guess and tag it `[research-backed; confirm in next 5 customer interviews]` — then continue. A research-backed draft tagged for validation is more useful than either a fake answer or a session that stalls. The conversation continues; the goal is to leave the session with an actionable persona, not a perfect one.

### 4. Sections that deserve extra scrutiny

A handful of sections are disproportionately diagnostic — if these are weak, the whole persona is weak:

- **Header tagline.** Must name *the job* and *the obstacle* in one sentence. If the tagline is just a demographic ("busy moms with babies"), it is not done.
- **Problem Context (section 2).** Push for a specific moment, place, device, and mood. "On their phone" is not a context; "3:17am one-handed on his iPhone with a baby on his chest" is.
- **Pains & Frustrations (section 8).** Each pain should be specific enough that *one design decision* could fix it. "It's clunky" is not a pain; "I have to maintain a parallel Google Sheet to cross-check the PMS's aging report against the bank" is.
- **Willingness to Pay (section 10).** Push for real numbers and named anchor products. If the user can't name three competitors with prices, they don't yet know the price ceiling — say so.
- **Anti-Persona (section 12).** The strongest test of understanding. A real anti-persona is a *recognizable lookalike* with a *reason they'd churn* and a *gating signal that filters them out at signup*. If the user can't draft one from memory, Claude proposes a recognizable anti-persona from research + offer; the user revises after live customer contact. Tag the section for validation rather than blocking the session.

### 5. Rewrite the Customer Persona file in place

Output: **rewrite `2. Customer Persona.md` in place** with the filled-in answers. Do not create a new file — the user wants the persona document to be the canonical, living version, not a sibling draft.

Match the template's structure exactly: same headers, same section order, same instructional prompts (keep the *italic* prompt lines and the `> Good: ... / Bad: ...` guidance intact — they remain useful when the user revisits the doc in three months). Replace each `**Your answer:**` (or equivalent blank field) with the filled-in answer.

At the top of the rewritten file, add:

- The persona's role-based **name** and **tagline**
- A **dated header** — e.g., "Drafted: May 2026"
- A short **evidence footer** — e.g., "Based on: 1 user-provided product offer, 4 web research passes (Reddit, G2, podcast transcripts), 0 customer interviews. Recommended next step: 5 customer interviews to validate sections 2, 6, 8, 10."

At the bottom of the rewritten file, add a **Sources** section listing the URLs, communities, and posts that backed the research — so the user can re-verify and re-research later. Personas decay; sources let you re-date them.

Because this overwrites the template, **read the existing file first** to preserve any user notes or modifications they have already made to it, and surface any conflicts to the user before writing.

### 6. Verify before delivering

Re-read the rewritten persona against the framework's "good vs bad" criteria. Specifically check:

- Does any answer contain "various", "depends", "all the time", "tech-savvy", "it depends", or "anyone who isn't our customer"? If so, fix or explicitly flag for the user.
- Can a stranger, reading only the persona, recognize this person in a coffee shop? If not, push for more specificity before delivering.
- Is the anti-persona recognizable enough to act on? If not, flag the section for live validation rather than treating it as a failure — a research-backed anti-persona to be sharpened with interview evidence is a normal output.
- Is the persona **dated**? Personas decay; an undated persona is a future fight with the team about "who's the customer again?"

Deliver the rewritten file via a `computer://` link and a one-paragraph summary of what is solid and what still needs validation.

## Tone and pacing

- **Conversational, not robotic.** The user is doing real thinking; treat them like a peer working through a hard problem, not a form to fill in.
- **Push back when answers are weak.** The user invoked this skill to be rigorous; collapsing into agreement is the worst possible outcome. Quote the framework's "bad" criteria and propose a sharper version every time the answer drifts.
- **One section at a time by default.** Don't dump all 12 sections at once. The point is the conversation. If the user explicitly asks to batch, oblige — but warn that quality usually drops, and offer to do a second pass on the diagnostic sections (Header, 2, 8, 10, 12).
- **Confirm the hypothesis before researching deeply.** Research takes time and tokens. A 30-second hypothesis check saves a 10-minute wrong-direction research detour.

## What "done" looks like

A rewritten persona file that:

- Names a specific role with a specific moment, place, mood, and device
- Lists **named** tools, communities, podcasts, and people — no categories like "social media" or "industry leaders"
- Has real numbers — frequencies, prices, satisfaction scores, dollar costs
- Includes verbatim pain language where possible
- Has an anti-persona sharp enough to inform a signup-gating rule
- Is dated and sourced

A research-backed persona with some sections tagged for live validation is a *successful* session output, not a failure. The goal is a persona the user can act on this week — write landing-page copy, pick growth channels, draft an interview script. Validation (5+ customer interviews, sharpening the tagged sections) is a normal next phase that happens after the session, not a precondition for the persona being useful.

Recommended next step after a successful session: live with the draft for 2–3 days, then book 3–5 short customer conversations to sharpen the tagged sections, and re-run this skill once the new evidence is in.
