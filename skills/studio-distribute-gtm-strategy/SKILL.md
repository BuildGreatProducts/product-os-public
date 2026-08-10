---
name: studio-distribute-gtm-strategy
description: Use when the user wants a concrete go-to-market plan to get a product's first users — which distribution channels to use and exactly how to start each. Triggers on phrases like "go-to-market strategy", "GTM plan", "distribution plan", "how do I get users", "which channels should I use", "where do I distribute this", "marketing plan for my app", "first 100 users", "launch plan", or "pick my channels". Standard path: reads docs/PRODUCT.md or the Define docs from the ProductOS folder (productos/ at the app repo root). Standalone fallback: in a repo without ProductOS it reads the codebase for product context and asks qualifying questions to fill the gaps. Then it researches the actual named channels and competitor distribution for the niche, walks the user through choosing three ranked channels, and builds a simple, product-specific, step-by-step starter plan for each — producing a filled-in Go-To-Market Strategy document. Especially useful in a ProductOS Distribute workflow, but works standalone in any repo.
---

# Distribute: Go-To-Market Strategy

This skill turns a defined product into a **Go-To-Market Strategy** — a ranked pick of three distribution channels and, for each, a simple, specific, step-by-step plan to get started. It reads the Define work (ideally the synthesized `PRODUCT.md`) — or, in a repo without ProductOS, the codebase itself — then researches the *actual* places this product's customers already gather and how competitors in the category distribute, and walks the user through selecting channels and turning each into a concrete first-week runbook.

The goal is not to list channels. The goal is to make every step **so specific to this product that it could not have been written for any other.** "Post on Reddit" is worthless; "post your note-from-voice demo in r/therapists (220k) framed as 'I built this because writing progress notes after every session was eating my evenings'" is a plan. The difference between those two sentences is the entire value of this skill. A channel is only useful once it names the exact place, the exact first move in the customer's own words, and the exact number that means it's working.

The most common ways a first go-to-market fails are picking too many channels, picking the channel the *founder* enjoys instead of the one the *customer* is on, and writing a plan so generic it gives no actual instruction. This skill exists to prevent all three: it forces exactly three ranked channels with one crowned primary, anchors every pick to evidence of where the customer already is, and rewrites any step that would read the same for a different product.

> **Session length:** Designed to be completable in 45–60 minutes of conversation. **All channel research is Claude's job during the session** — finding the named subreddits/Discords/hashtags/keywords/creators/marketplaces and the competitor-distribution teardown. The user reacts and supplies founder context (audience, budget, what they'll actually do); they do not go off and research channels. The skill identifies and fully plans **all three** channels — not just the primary — so the user (often with a coach in a 1:1 review) can decide where to start, with a real plan waiting for whichever channel they choose. When run in a repo without ProductOS, the skill first reads the codebase for product context and asks a few qualifying questions — the customer, where they gather, and the price — to stand in for the Define docs before the channel research begins.

## Inputs

This skill needs three things: **product context** (what the product is, who it's for, how it makes money), an **output target** (where the strategy gets written), and the **channel playbook** (how to choose and run channels). Product context is gathered one of two ways — the standard path reads the ProductOS folder (`productos/` at the app repo root, or the current folder in a standalone ProductOS checkout); the fallback covers a repo with no ProductOS at all — but the rest of the workflow is identical either way.

### Product context — Path A (standard): ProductOS in the repo

Locate the Define work in the ProductOS folder — `productos/` at the app repo root (or the current folder in a standalone ProductOS checkout):

1. **The product summary** — usually `docs/PRODUCT.md`. The **preferred** input: an 8-section plain-English summary of the whole strategy. If it exists, read it first and in full. If not, fall back to the Define docs directly (below).
2. **The Customer Persona** — usually `productos/define/2. Customer Persona.md`. The single most useful input for channel selection. Section 11 *Watering Holes* (named communities, podcasts/newsletters, trusted people) is the raw material for the picks; section 10 *Willingness to Pay* gates which channels the price can afford; sections 5–6 (*Job-to-be-Done*, *Triggers*) feed search intent.
3. **The Pricing Strategy** — usually `productos/define/3. Pricing Strategy.md`. The launch price and billing shape — the first check on whether a channel's cost can ever pay back. If the user has done the optional deep dive (`productos/define/BONUS - Business Strategy Deep Dive.md`), read it too: margin, north star, and Unfair Advantage (often itself a channel — a community, an audience, a platform niche) all sharpen the channel ranking.
4. **The Launch Log** — `docs/LAUNCHES.md` (and `productos/define/4. Mini-Launch.md`). The four launches so far are the richest distribution evidence in the project: which channel produced replies, signups, activated users, or payments — and the believers list, which is itself a channel. Start the hunt from anything that already pulled; the primary channel recommendation should almost always explain its relationship to the thread the launches built.

If there's no ProductOS folder anywhere, you're on Path B. If ProductOS is present but the docs are still full of `**Your answer:**` placeholders, that's not Path B — say so and point them to `studio-define-product` (or the `studio-define-from-code` fast-track) first — a channel plan built on a fuzzy product targets the wrong people in the wrong places.

### Product context — Path B (standalone fallback): a repo without ProductOS

When there's no ProductOS folder in the repo at all, read the **codebase itself** for context. Look at the README, the package manifest (`package.json`, `pyproject.toml`, etc.), any landing-page or marketing copy in the repo, pricing configuration (Stripe products, a pricing page, RevenueCat config), the app's routes / screens / features, and any app-store or deploy metadata. From these, infer what the product does, its business shape, and its price where present.

Then **ask the user qualifying questions to fill what the code cannot reveal** — these decide the channels, so don't proceed on guesses:

- **The customer** — who specifically is this for (role, context), and the core pain they switch for?
- **Where they already gather** — named communities, creators, searches, platforms (the watering holes a Persona would otherwise supply).
- **Price & willingness to pay** — if it isn't clear from the code.
- **Proven demand** — named competitors, so the competitor teardown has a starting point.

Ask only what the codebase didn't already answer, and keep it conversational — one question at a time, the same way step 3 handles founder context.

### Output target (both paths)

**The Go-To-Market Strategy template** — `productos/distribute/1. Go-To-Market Strategy.md`. On the standard path this exists, defines the exact output structure, *and is the file the skill rewrites in place* (see step 5). On the standalone fallback it won't exist — create the plan fresh with the same structure (customer line, three sequenced channel blocks, Next), at `docs/go-to-market-strategy.md` (or the repo root if there's no `docs/` folder).

### Channel playbook (both paths)

Two reference docs ship **inside this skill's folder**, so they're available in both paths. Read them in full at the start, and justify every channel pick through the decision tree and fit matrix:

- **`BONUS - Distribution Channels.md` (in this skill's folder)** — the meta-rule (go where they already are), a decision tree mapping product shape to a starting channel, a channel-vs-business-type fit matrix, and the twelve channels each with a pass threshold and pitfalls.
- **`BONUS - AI Distribution Tools.md` (in this skill's folder)** — the specific tool to run each channel.

The same two files also live in `productos/distribute/`; if the user has customized those project copies, prefer them. The bundled copies guarantee the skill always has its playbook when run standalone.

## Workflow

### 1. Absorb the product and form a working hypothesis

**First, detect the context.** If a ProductOS folder exists — `productos/` at the repo root, or the current folder is itself a ProductOS checkout — you're on Path A; read `docs/PRODUCT.md` or the Define docs end to end, plus the Persona's Watering Holes. Only if there's no ProductOS anywhere are you on Path B; read the repo for product context (README, manifests, landing/marketing copy, pricing config, routes/features) and ask the qualifying questions from Inputs to establish the customer, their watering holes, price, and proven demand. Either way, the goal of this step is identical: enough product context to form a channel hypothesis.

From whichever source, extract:

- **Business shape** — B2C consumer app, prosumer tool, B2B SaaS, indie/Mac app, marketplace, dev tool, productized service. The shape is the biggest constraint on which channels can work (the fit matrix encodes this).
- **Price band** — what the customer will pay, and therefore what a channel can afford to cost (a $9/mo app can't fund cold outreach; a $4,995/mo service shouldn't lead with TikTok).
- **Where they already gather** — the named communities, creators, searches, and platforms from the Watering Holes and validation work. This is the spine of the plan.
- **Founder starting position** — does PRODUCT.md or the validation doc imply an existing audience, a channel that already pulled, or a platform the product extends? Note anything that already showed life.

From this, form a **working channel hypothesis** in one paragraph: "Business shape is X at price Y; the customer already gathers at Z; the three best-fit channels look like [primary], [next], [experiment], because…" State it back to the user and ask them to confirm or correct **before** you do the deep research. A wrong starting hypothesis (e.g., leading a $9 consumer app with outreach) wastes the whole session.

### 2. Research the real channels (always — this is the core of the skill)

Spend real, focused effort here. The entire value of the output is specificity, and specificity comes from research, not from the user's gut. Use web search and any connected research tools to do **both** of these every time:

- **Name the channels.** For each candidate channel, turn the category into named instances for *this* niche: the actual subreddits (with rough subscriber counts / activity), Discord servers, Facebook groups, TikTok/Instagram hashtags, SEO keyword clusters (with the search intent behind them), marketplaces or platforms the product could ride (App Store keyword cluster, Notion/Airtable/Shopify/Chrome/WordPress ecosystems), and the specific creators, podcasts, or newsletters the persona already follows. Pull names, not categories — "r/therapists (220k)" beats "therapy communities."
- **Tear down competitor distribution.** Take 3–5 competitors from the offer's proof and pricing anchors (or find them) and reverse-engineer how they actually get users: where they post, their SEO footprint, their Product Hunt / AppSumo history, the creators who feature them, the communities they're active in. How the proven money in the category distributes is usually the strongest single signal for what will work — and what's already saturated.

Collect concrete, named data points before walking the user through selection. Note which came from research and which still need the user's confirmation.

### 3. Select and rank the three channels, conversationally

Walk the user through selection **one question at a time** — do not dump a six-question form. Weave in only the founder-context questions the documents haven't already answered, asking each as it becomes relevant:

- **Audience** — do they already have any following or list anywhere, and how big? (Gates social/build-in-public, referrals.)
- **Budget** — organic/time-only to start, or can they spend on ads, creators, or launch-platform fees now? (Gates ads, influencer.)
- **Execution comfort** — which will they actually sustain: on-camera short-form, community posting, cold outreach/DMs, or written/SEO content? (A channel they won't run is not a channel.)
- **Stage** — is the product live with users yet, or pre-launch? (Gates referrals, and the timing of a launch-platform moment.)
- **Traction** — has anything already pulled, even slightly?
- **Confirm the research** — "Here are the named places I found your customers gather: […]. Which look right, and are you already active in any?"

Then propose **three ranked channels with one crowned primary**, each justified out loud through the fit matrix and decision tree: business shape, price band, where the customer is, and what the founder can execute. Crown the primary as the one with the best intersection of *customer is there* and *founder can run it well*. Rank the other two as Next and Experiment. Critique weak instincts using the failure patterns below — especially the urge to pick five channels, to lead with ads, or to choose the channel the founder simply likes.

### 4. Build the per-channel step-by-step plan (the heart)

For each of the three channels, draft the starter block from the template — the five "Do this" steps plus its two closing lines — and hold every step to the specificity test: **if it would read the same for a different product, rewrite it.**

1. **The exact places / keywords / creators** — named, from the research.
2. **Warm up** — how to show up before selling (lurk N days, comment, build the asset).
3. **The first move** — the exact post / email / video / listing angle, written in the customer's own pain language pulled from the Persona, not in marketing-speak.
4. **The link** — deep-link to the specific feature or magic moment, never the homepage.
5. **Cadence** — how often and for how long before judging it.

Then the block's two closing lines: **Working =** — a pass threshold that is a **number + a date**, laddering up to the north star (card swipes, paying users, booked calls — not views or followers) — and **If it stalls** — the number + date that means stop and diagnose, plus the first thing to check.

Plan all three fully. Channel 1 gets the most detail, but the next and experiment channels each get a real, runnable block — the sequence gates when they start, not how well they're planned.

### 5. Rewrite the Go-To-Market Strategy file in place

Output depends on the path. **On the standard path, rewrite `productos/distribute/1. Go-To-Market Strategy.md` in place** with the filled-in answers — do not create a sibling draft; the user wants this to be the canonical, living plan. **On the standalone fallback, where that template doesn't exist, create the plan fresh** with the identical structure, at `docs/go-to-market-strategy.md` (or the repo root if there's no `docs/` folder).

Match the template's structure exactly: the customer line, the one-rule line, then **three channel blocks in sequence order** (start here / next / experiment), each with its one-sentence why, the five-step "Do this" checklist, "Working =", and "If it stalls" — then the short **Next** handoff and the one-line *Based on:* footer naming the inputs and research used. Date the header line. Because this overwrites the template, **read the existing file first** to preserve any notes the user already added, and surface conflicts before writing.

**The output rule — the document is execution-only.** The finished file contains no frameworks, menus, ratings, tables of channel options, or `> Good/Bad` examples — only this member's specific instructions. All reasoning happens in the session; all guidance lives in this skill and the BONUS docs. If a sentence teaches instead of instructs, cut it. The full channel ranking rationale, the fit-matrix argument, and the research trail are discussed in conversation — only the conclusions land in the file (one "why" sentence per channel, one *Based on:* line at the bottom).

### 6. Verify before delivering

Re-read the rewritten strategy against the Distribution Channels playbook and the failure patterns below. Specifically check:

- Are there **exactly three** channels, ranked, with **one** crowned primary — not five, not an un-prioritized pile?
- Is every channel a **named place**, not a category? Could the user post in it tomorrow morning?
- Does every step in the plan pass the specificity test — would it read differently for a different product?
- Is every "Working =" a **number + a date** that ladders to the north star — not a vanity metric?
- Does the primary sit where the customer already is **and** where the founder can realistically execute?
- Does the first move quote the customer's own pain language and deep-link to the magic moment?

Deliver the rewritten file via a `computer://` link and a one-paragraph summary: which channel to start with, the first move this week, and what to watch.

## Failure patterns to look for

Name them when you see them — naming compounds learning, and the user will catch them earlier next time:

- **The Seven-Channel Spread.** Picking a little of everything. Seven channels at 10% effort all fail quietly; one at 100% produces readable signal. Force three, ranked, one primary, run in sequence.
- **The Founder-Preference Channel.** Choosing the channel the founder enjoys (usually writing a blog or building in public) over the one the customer is actually on. Comfort is not a strategy. The wrestler's app belongs in wrestling communities even if the founder would rather make a podcast.
- **The Unnamed Channel.** "Communities," "social," "SEO," "word of mouth" — categories, not channels. A channel is a named place (r/X, the Y Discord, the keyword "Z") the user can show up in tomorrow. Force the name.
- **The Generic Plan.** Steps that fit any product: "post on Reddit," "do some SEO," "make videos." This is the failure that guts the skill. Every step must be rewritable only for *this* product, in *this* customer's words.
- **The Premature-Ads Reflex.** Leading with ads (or a referral program) before an organic channel has proven the hook. Ads amplify a working funnel; they don't create one. Paid channels are an Experiment, never the primary, for a pre-revenue product.
- **The Vanity Goal.** "Working = 100k views" or "10k followers." Attention isn't revenue. Every pass threshold must be a card swipe, a paying user, a booked call — a number that ladders to the north star, with a date.
- **The Competitor Copy.** Lifting a competitor's channel without checking it matches this persona and price. A channel that works for a $1M/mo viral consumer app won't carry a $99/mo B2B tool. Use the teardown for signal, not for mimicry.

## Tone and pacing

- **Conversational, not a form.** The user is deciding how to spend the next 30 days of their life; treat them like a peer, ask one question at a time, and react to their answers.
- **Do the research so they don't have to.** Naming the channels and tearing down competitors is Claude's job in-session. Don't hand the user homework you could do live.
- **Push back on generic and on greed.** The two worst outcomes are a plan that's too vague to act on and a plan with five channels. Both deserve a name-the-pattern correction and a sharper rewrite.
- **Confirm the hypothesis before deep research.** A 30-second check that the working channel hypothesis is right saves a long detour researching the wrong channels.
- **One channel at a time when building the plan.** Build the primary's block fully, confirm it, then move to Next, then Experiment.
- **Force the named place and the number.** Don't accept "communities" or "lots of signups." Make every channel a name and every goal a number with a date.

## What "done" looks like

A completed Go-To-Market Strategy document — the rewritten `productos/distribute/1. Go-To-Market Strategy.md` on the standard path, or a fresh `docs/go-to-market-strategy.md` in a repo without ProductOS — where:

- The customer line says who they are and where they already gather — one line, no framework language.
- Exactly **three channel blocks in sequence order**, one marked "start here", the others gated on the previous channel's number.
- Every "Do this" step is specific enough that it could only be this product's plan — named places, the first move in the customer's words, a deep link to the magic moment. Every block ends in "Working =" (a number + date) and "If it stalls" (a number + date + first thing to check).
- The Next section hands off to the Growth Experiments skill in one sentence; the *Based on:* footer names the inputs, dated.
- **Nothing in the file teaches** — no menus, ratings, frameworks, or calibration examples. A reader could execute week one without opening any other document.

A plan the user can act on **this week** — show up in a named place, make a specific first move, and know the number that means it's working. Anything vaguer is a draft; say so, name the gap, and sharpen it.

Recommended next step after a successful session: start the primary channel this week, hold to its cadence until it hits (or misses) its threshold, then run the **Growth Experiments** skill on that channel to turn the starter plan into repeatable, optimized experiments.
