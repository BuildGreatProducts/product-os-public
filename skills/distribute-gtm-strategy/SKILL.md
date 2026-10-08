---
name: distribute-gtm-strategy
description: >-
  Picks three ranked distribution channels for a product's first users — researching named
  communities, competitors' distribution, and the niche — and writes docs/GO-TO-MARKET.md with a
  step-by-step starter plan for each, one of them the product shape's native store or directory.
  Reads docs/DEFINE.md, or the codebase plus a few questions when ProductOS isn't installed. Use
  when the user asks for a "go-to-market plan", "how do I get users", "which channels should I
  use", or "first 100 users". Not for experiments on channels already running — use
  distribute-growth-experiments; not for deploying — use develop-golive.
---

# Distribute: Go-To-Market Strategy

Turn a defined product into `docs/GO-TO-MARKET.md`: three ranked distribution channels, one crowned primary, and for each a step-by-step starter plan so specific to this product that it could not have been written for any other. "Post on Reddit" is worthless; "post your note-from-voice demo in r/therapists (220k) framed as 'I built this because writing progress notes after every session was eating my evenings'" is a plan. Every channel names the exact place, the exact first move in the customer's own words, and the exact number that means it's working.

## Inputs

> **Inside a challenge:** if `docs/SELL-IN-30.md` is open, read its header first. The bar (a payment, or an activated user) and the clock (three experiment-weeks after this one) shape the choice: the primary channel is the one that can reach the bar inside that window, its "Do this" list is what the member runs this week, and the second and third channels stay written but don't start until after the challenge.

The skill needs **product context**, an **output target**, and the **channel playbook**. Product context comes one of two ways; the rest of the workflow is identical either way.

**Detect the path first.** If a ProductOS folder exists (`productos/` at the repo root, or the current folder is itself a ProductOS checkout), you're on Path A. Only if there's no ProductOS anywhere are you on Path B.

### Product context — Path A (standard): ProductOS in the repo

Read `docs/DEFINE.md` at the app repo root, first and in full:

1. **Summary and Product Offer** — `## Summary` and `## 1. Product Offer`: who the customer is, the pain they switch for, the mechanism, and the proof (whose competitors seed the teardown in step 2).
2. **The Customer Persona** — `## 2. Customer Persona`. The single most useful input for channel selection. Its *Watering Holes* (named communities, podcasts/newsletters, trusted people) are the raw material for the picks; *Willingness to Pay* gates which channels the price can afford; *Job-to-be-Done* and *Triggers* feed search intent.
3. **The Product Shape** — `## Product Shape` → `### Primary Shape` gives the shape slug (and any `### Secondary Shapes`). Then read only the `## Distribute notes` section of that shape's file, `productos/shapes/<slug>.md` (from this skill's folder, `../../shapes/<slug>.md`): the shape's native channels and first-100-users moves. No Product Shape section (a repo from before 2.0)? Treat the product as `web-app` unless the codebase or the member clearly says otherwise, and suggest running `define-product-shape`.
4. **The Pricing Strategy** — `## 3. Pricing Strategy`. Who pays, how the business earns, the pricing model, and the launch price — the first check on whether a channel's cost can ever pay back. If the optional `## 4. Business Strategy` is filled, read it too: margin, north star, and Unfair Advantage (often itself a channel — a community, an audience, a platform niche) all sharpen the ranking.
5. **Real customer signal** — any replies, conversations, signups, or payments the member has had so far, wherever they came from (ask if they aren't written down). This is the richest distribution evidence there is, and the people behind it are themselves a channel. Start the hunt from anything that already pulled; the primary channel recommendation should explain its relationship to it.

If ProductOS is present but `docs/DEFINE.md` is missing or its Offer, Persona and Pricing sections are still placeholders, that's not Path B — say so and point the member to the Define skills (`define-offer-builder` → `define-customer-persona` → `define-pricing`), or the `define-from-code` fast-track for an existing product, first. A channel plan built on a fuzzy product targets the wrong people in the wrong places.

### Product context — Path B (standalone fallback): a repo without ProductOS

Read the **codebase itself**: the README, the package manifest, any landing-page or marketing copy, pricing configuration (Stripe products, a pricing page, RevenueCat config), the app's routes / screens / features, and any app-store or deploy metadata. Infer what the product does, its product shape (a slug from `../../shapes/SHAPES.md` — the manifest and folder layout usually say: a `.claude-plugin/` folder, an extension manifest, an `eas.json`, a published package), and its price where present.

Then **ask qualifying questions to fill what the code cannot reveal** — these decide the channels, so don't proceed on guesses. Ask only what the codebase didn't answer, one question at a time:

- **The customer** — who specifically is this for (role, context), and the core pain they switch for?
- **Where they already gather** — named communities, creators, searches, platforms (the watering holes a Persona would otherwise supply).
- **Price & willingness to pay** — if it isn't clear from the code.
- **Proven demand** — named competitors, so the competitor teardown has a starting point.

### Output target (both paths)

`docs/GO-TO-MARKET.md` at the app repo root (create `docs/` if needed). On Path A, the worksheet `productos/distribute/1-Go-To-Market-Strategy.md` defines the structure; on Path B, use the structure described in step 5.

### Channel playbook (both paths)

Two reference docs live in ProductOS's `distribute/` folder, two levels up from this skill's folder (`../../distribute/`) — the same files whether ProductOS sits in the repo as `productos/` or is installed as a plugin.

- **[BONUS-Distribution-Channels.md](../../distribute/BONUS-Distribution-Channels.md)** — at the start, read its *Pick your channel first* section (the decision tree and the fit matrix), and under *Shape-native channels* the rule, the discovery forces, and only the primary shape's block; justify every pick through them. Once the three channels are chosen (step 3), read only those three channels' sections under *The twelve channels* for their pass thresholds and pitfalls.
- **[BONUS-AI-Distribution-Tools.md](../../distribute/BONUS-AI-Distribution-Tools.md)** — at step 4, read only the sections for the three chosen channels, for the tool to run each.

## Workflow

### 1. Absorb the product and form a working hypothesis

Gather product context on Path A or Path B (see Inputs). From it, extract:

- **Product shape and buyer** — the primary shape slug (what the customer receives: a web app, a browser extension, an MCP server, a productized service…) and who buys it (consumer, prosumer, B2B). Together they're the biggest constraint on which channels can work: the shape names its **native channel** (the store, marketplace, registry, or directory where buyers of that shape already look), and the fit matrix encodes the buyer side.
- **Price band** — what the customer will pay, and therefore what a channel can afford to cost (a $9/mo app can't fund cold outreach; a $4,995/mo service shouldn't lead with TikTok).
- **Where they already gather** — the named communities, creators, searches, and platforms from the Watering Holes and validation work. This is the spine of the plan.
- **Starting position** — does DEFINE.md, the member's real customer signal, or the validation work imply an existing audience, a channel that already pulled, or a platform the product extends? Note anything that already showed life.

Form a **working channel hypothesis** in one paragraph: "Shape is X sold to [buyer] at price Y; its native channel is N; the customer already gathers at Z; the three best-fit channels look like [primary], [next], [experiment], because…" State it back and ask the member to confirm or correct **before** the deep research. A wrong starting hypothesis (e.g., leading a $9 consumer app with outreach) wastes the whole session.

### 2. Research the real channels (always — this is the core of the skill)

All channel research is your job in the session; the member reacts and supplies their own context, they don't go off and research. The value of the output is specificity, and specificity comes from research, not the member's gut. Use web search and any connected research tools to do **both** every time:

- **Map the native channel.** For the primary shape's native places (from the shape file's Distribute notes and the playbook's shape block), find what ranks there today for this niche: the top listings for the persona's search terms, their review counts, their first lines and images, and which categories or curated lists they sit in. This is the bar the member's listing has to clear.
- **Name the channels.** For each candidate channel, turn the category into named instances for *this* niche: the actual subreddits (with rough subscriber counts / activity), Discord servers, Facebook groups, TikTok/Instagram hashtags, SEO keyword clusters (with the search intent behind them), marketplaces or platforms the product could ride (App Store keyword cluster, Notion/Airtable/Shopify/Chrome/WordPress ecosystems), and the specific creators, podcasts, or newsletters the persona already follows. Pull names, not categories — "r/therapists (220k)" beats "therapy communities."
- **Tear down competitor distribution.** Take 3–5 competitors from the offer's proof and pricing anchors (or find them) and reverse-engineer how they actually get users: where they post, their SEO footprint, their Product Hunt / AppSumo history, the creators who feature them, the communities they're active in. How the proven money in the category distributes is usually the strongest single signal for what will work — and what's already saturated.

If web search isn't available, say so, ask the member for the communities and competitors they know, and mark those claims unverified. Note which data points came from research and which still need the member's confirmation.

### 3. Select and rank the three channels, conversationally

Walk the member through selection **one question at a time** — never a six-question form. Ask only the context questions the documents haven't answered, each as it becomes relevant:

- **Audience** — any following or list anywhere, and how big? (Gates social/build-in-public, referrals.)
- **Budget** — organic/time-only to start, or can they spend on ads, creators, or launch-platform fees now? (Gates ads, influencer.)
- **Execution comfort** — which will they actually sustain: on-camera short-form, community posting, cold outreach/DMs, or written/SEO content? (A channel they won't run is not a channel.)
- **Stage** — live with users yet, or pre-launch? (Gates referrals, and the timing of a launch-platform moment.)
- **Traction** — has anything already pulled, even slightly?
- **Confirm the research** — "Here are the named places I found your customers gather: […]. Which look right, and are you already active in any?"

Then propose **three ranked channels with one crowned primary**, each justified out loud through the fit matrix and decision tree: product shape, buyer, price band, where the customer is, and what the member can execute. **One of the three is the shape's native channel** unless there's a stated reason it isn't (the store bans the category, the buyers are a named list of enterprises, the member already owns a stronger channel); say the reason out loud, and name it in that channel slot's "why" sentence if it replaces the native one. The native channel is often Next rather than primary: it ranks products that already have installs and reviews, so the primary is usually the channel that sends the first users there. Crown the primary as the best intersection of *customer is there* and *member can run it well*; rank the other two as Next and Experiment. Push back on weak instincts by naming the failure pattern (below) — especially the urge to pick five channels, to lead with ads, or to choose the channel the member simply likes.

### 4. Build the per-channel step-by-step plan (the heart)

Build one channel at a time: the primary's block fully, confirm it, then Next, then Experiment. For each, draft the worksheet's starter block — five "Do this" steps plus two closing lines — and hold every step to the specificity test: **if it would read the same for a different product, rewrite it.**

1. **The exact places / keywords / creators** — named, from the research. For the native channel: the store or directory, the search terms to rank for, and the listing to write (`design-marketplace-listing`, or `design-app-listing` for the App Store / Google Play) — or improve, if `docs/MARKETPLACE-LISTING.md` / `docs/APP-LISTING.md` exists.
2. **Warm up** — how to show up before selling (lurk N days, comment, build the asset).
3. **The first move** — the exact post / email / video / listing angle, written in the customer's own pain language from the Persona, not marketing-speak.
4. **The link** — deep-link to the specific feature or magic moment, never the homepage.
5. **Cadence** — how often and for how long before judging it.

Then **Working =** — a pass threshold that is a **number + a date**, laddering up to the north star (card swipes, paying users, booked calls — not views or followers) — and **If it stalls** — the number + date that means stop and diagnose, plus the first thing to check.

Plan all three fully, so the member (often with a coach in a 1:1 review) can start wherever they choose with a real plan waiting. Channel 1 gets the most detail, but Next and Experiment each get a real, runnable block — the sequence gates when they start, not how well they're planned.

### 5. Write `docs/GO-TO-MARKET.md`

Write the plan to `docs/GO-TO-MARKET.md`. On Path A, use the worksheet `productos/distribute/1-Go-To-Market-Strategy.md` for structure only; never write answers back into `productos/`. On Path B, use the same structure: the customer line, the one-rule line, then **three channel blocks in sequence order** (start here / next / experiment), each with its one-sentence why, the five-step "Do this" checklist, "Working =", and "If it stalls" — then the short **Next** handoff and the one-line *Based on:* footer naming the inputs and research used. Date the header line, and drop the worksheet's italic intro line. If `docs/GO-TO-MARKET.md` already exists, **read it first**, preserve the member's edits, show a diff, and get approval before overwriting.

**The document is execution-only.** No frameworks, menus, ratings, tables of channel options, or `> Good/Bad` examples — only this member's specific instructions. If a sentence teaches instead of instructs, cut it. The ranking rationale, the fit-matrix argument, and the research trail stay in the conversation; only the conclusions land in the file (one "why" sentence per channel, one *Based on:* line).

### 6. Verify before delivering

Re-read the file against the Distribution Channels playbook and the failure patterns below:

- [ ] **Exactly three** channels, ranked, with **one** crowned primary marked "start here"; the other two gated on the previous channel's number.
- [ ] Every channel is a **named place**, not a category — could the member post in it tomorrow morning?
- [ ] Every step passes the specificity test — it would read differently for a different product.
- [ ] Every "Working =" is a **number + a date** that ladders to the north star, not a vanity metric; every "If it stalls" has a number + date + the first thing to check.
- [ ] The primary sits where the customer already is **and** where the member can realistically execute.
- [ ] One of the three is the primary shape's native channel, or the conversation gave a stated reason it isn't.
- [ ] The first move quotes the customer's own pain language and deep-links to the magic moment.
- [ ] The customer line says who they are and where they gather — one line, no framework language.
- [ ] The Next section hands off to `distribute-growth-experiments` in one sentence; the *Based on:* footer names the inputs, dated.
- [ ] Nothing in the file teaches — a reader could execute week one without opening any other document. Anything vaguer is a draft: say so, name the gap, and sharpen it.

Give the member the file path and a one-paragraph summary: which channel to start with, the first move this week, and what to watch. Next step: start the primary channel this week, hold its cadence until it hits (or misses) its threshold, then run `distribute-growth-experiments` on that channel.

## Failure patterns

Name them when you see them — the member will catch them earlier next time:

- **The Seven-Channel Spread.** A little of everything. Seven channels at 10% effort all fail quietly; one at 100% produces readable signal. Force three, ranked, one primary, run in sequence.
- **The Preference Channel.** Choosing the channel the member enjoys (usually a blog or building in public) over the one the customer is actually on. Comfort is not a strategy. The wrestler's app belongs in wrestling communities even if its maker would rather make a podcast.
- **The Unnamed Channel.** "Communities," "social," "SEO," "word of mouth" — categories, not channels. A channel is a named place (r/X, the Y Discord, the keyword "Z") the member can show up in tomorrow. Force the name.
- **The Generic Plan.** Steps that fit any product: "post on Reddit," "do some SEO," "make videos." This is the failure that guts the skill. Every step must be rewritable only for *this* product, in *this* customer's words.
- **The Premature-Ads Reflex.** Leading with ads (or a referral program) before an organic channel has proven the hook. Ads amplify a working funnel; they don't create one. Paid channels are an Experiment, never the primary, for a pre-revenue product.
- **The Vanity Goal.** "Working = 100k views" or "10k followers." Attention isn't revenue. Every pass threshold is a card swipe, a paying user, a booked call — a number that ladders to the north star, with a date.
- **The Skipped Store.** A product whose shape has a native store, marketplace, or registry, with no plan to rank there — an extension that's only promoted on X, an MCP server in no directory. Buyers of that shape look there first; put the native channel in the three or say why not.
- **The Competitor Copy.** Lifting a competitor's channel without checking it matches this persona and price. A channel that carries a viral consumer app won't carry a $99/mo B2B tool. Use the teardown for signal, not mimicry.
