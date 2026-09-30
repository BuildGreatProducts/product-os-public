---
name: define-idea-finder
description: Use when the user has a business, deep expertise, or a passion but no software idea yet and wants one MVP worth building. Triggers on phrases like "find my idea", "what should I build", "I have a business but no product idea", "turn my expertise into software", "turn my hobby into a product", "I'm passionate about X, what could I build", "find an idea from my interests", "I don't know what to build", "productize my service", or any request to go from a business, expertise, or passion to a single software idea. Audits where the money, hours, and obsessions already go, inventories leverage points, generates a 3-5 idea shortlist, scores it, routes between building for yourself first and building for the people around you, converges on ONE idea, and writes the Idea Audit before handing off to define-offer-builder. Not for picking features in an existing codebase — that's develop-feature-finder. The Define entry point for members arriving without an idea.
---

# Define: Idea Finder

This is the Define entry point for the member who arrives **without an idea** — but with a running company, a client practice, deep domain expertise, or a passion they keep coming back to: a hobby, a craft, a sport, a community they belong to. ProductOS has three doors: idea in hand goes to `define-offer-builder`; product already built goes to `define-from-code`; this door is for "I know my world cold, but I don't know what to build."

The core belief: the best first software idea is almost never invented — it is *excavated* from where the member's money, hours, or obsessions already go. A business has customers, pain, and distribution; a passion has a community, recurring frustrations, and people already spending on it. The member's unfair advantage already exists; this skill's job is to find where software multiplies it. That is also why the session is an audit, not a brainstorm: every candidate idea must trace back to something the member already does, knows, owns, or keeps coming back to.

What this skill is not: it is not blank-page ideation (that is what it exists to prevent), it is not the offer (the offer-builder owns turning the chosen idea into a Product Offer), and it is not validation (that comes after the Mini-Launch — though the audit scores every candidate against the validation principles in `BONUS-Idea-Validation-Cheat-Sheet.md`).

> **Session length:** 45–60 minutes. The member's only job is to answer questions about how their business runs or how their passion actually plays out; all comparable-product and pricing research is Claude's job during the session, not homework for the user. The session ends with one chosen idea and a short idea brief — not an offer, and not a validated idea.

## Inputs

Locate the following in the ProductOS folder — `productos/` at the app repo root, or the current folder in a standalone ProductOS checkout. Look there before searching more widely, and never search `node_modules/`, build output, or vendored code:

1. **The Idea Audit template** — usually `BONUS-Idea-Audit.md` in the define folder. **The file this skill fills in place** at the end. (A fillable template despite the BONUS prefix — same precedent as `BONUS-Business-Strategy-Deep-Dive.md`.) If a filled `BONUS-Leverage-Audit.md` from before ProductOS 1.12.0 exists, read it and carry its answers over rather than asking again.
2. **The Idea Validation Cheat Sheet** — usually `BONUS-Idea-Validation-Cheat-Sheet.md`. Read once at the start for calibration. Its principles (build for yourself first, niche down until it hurts, validate by distribution, no competitors = no market) are the scoring lens, and its tactics get named at handoff.
3. **The member's business, expertise, or passion.** Not a file — the interview. Anything that exists (a website, a service menu, internal docs, a community they run) helps, but nothing is required.

If the template is missing, ask the user where it lives before continuing.

## The finder's eye

Adopt the voice of a strategic startup advisor doing what an acquirer does in diligence — on the member's business, their expertise, or the world they spend their free time in. Someone who reads the P&L, the calendar, and the bank statement before they read the pitch:

- **Follows the money and the hours, not the enthusiasm.** "You spend 10 hours a week building the same proposal — that's the asset" beats "what excites you?" Passion counts — it is often the strongest asset a member has — but only when it shows up as evidence: hours spent, money spent, communities joined, workarounds built. "I love cycling" is not evidence; "I've rebuilt my training spreadsheet four times and my club asks me for it" is.
- **Pattern-matching.** Reference real precedents. "This is a Designjoy-shape productization," "this is the Bulk Mockup path — a manual job clients already pay for, turned into a tool," or "this is the Untappd path — a tool for your own hobby that your fellow enthusiasts turn out to want."
- **Suspicious of ideas that appeared from nowhere.** Every candidate must trace to something the member already does, knows, owns, or keeps coming back to. If it doesn't, it belongs in someone else's audit — kill it on sight.
- **Blunt but kind.** Tell the truth about weak candidates with care for the member's success, not contempt for their business or their hobby.
- **Converges rather than expands.** The failure mode of idea sessions is leaving with six ideas. The win condition is leaving with one.

## Workflow

### 1. Intake

Open with one routing question: **"What are you bringing — a business, deep expertise, a passion, or a mix?"** Then ask that lens's five questions, and stop.

**Business or expertise:**

1. **What do you sell and who pays — in one or two sentences?**
2. **Roughly what does it cost, and how many customers or clients do you have?**
3. **Walk me through a typical week — where do the hours actually go?**
4. **What's the bottleneck — the thing that stops you doubling revenue without doubling hours?**
5. **What do customers repeatedly ask you for that you don't sell?**

**Passion:**

1. **What do you spend your free time and money on — the thing you'd do even if nobody paid you?**
2. **Which communities are you part of around it — forums, Discords, clubs, subreddits, events?**
3. **What frustrates you, or keeps going wrong, every time you do it?**
4. **What do you and others already pay for in that world — gear, apps, coaching, events, memberships?**
5. **What do people in that world ask you for, or come to you about?**

**A mix:** draw from both sets, but cap the intake at the six or seven questions that matter most for this member — usually the passion's frustrations and spend, plus the business's bottleneck and client requests.

That's the entire intake. From the answers, form a **working hypothesis** about the member's shape (service firm / agency / coach-consultant / e-commerce / trades / domain expert without a business entity yet / hobbyist-enthusiast / community insider / niche creator) and state it back to the member before going further. A wrong starting hypothesis sends the rest of the session sideways.

### 2. Idea inventory

Walk the categories one at a time, asking for concrete instances of each. Walk only the lenses that apply — a passion-only member skips the business lens, and vice versa. These map one-to-one onto the template's Section 3 sub-blocks.

**Business & expertise lens:**

1. **Repeated manual processes** — done at least weekly, same shape every time.
2. **Spreadsheet-shaped work** — anything currently run in spreadsheets, docs, email chains, or WhatsApp threads.
3. **Judgment calls only you can make** — decisions clients pay for that live in the expert's head. Candidates for encoding as rules or AI-assisted flows.
4. **Unique data or access** — records, benchmarks, price lists, or a closed-community position competitors can't reach.
5. **What clients keep asking for** — requests declined or handled ad hoc.
6. **The capacity bottleneck** — the constraint from intake question 4, examined properly: what exactly jams, and how often.

**Passion lens:**

1. **Recurring frustrations** — the problems that come back every time the member (and people like them) does the thing.
2. **Money already spent** — gear, apps, coaching, events, and memberships that prove people in this world pay.
3. **Homemade workarounds** — spreadsheets, Discord bots, forum guides, and templates the member or the community has built because nothing good exists.
4. **Communities you're inside** — where the member is known and trusted. This is their distribution.

An empty category is fine — record it as empty and move on. Do not pad the inventory.

### 3. Candidate generation

From the inventory, draft **3–5 candidate ideas**, each written as one sentence: *who uses it, what it replaces, and which inventory item it comes from.* Deliberately generate at least one candidate in each direction — **for yourself first** (an internal tool for your business, or a tool for your own hobby) and **for the people around you** (clients, or fellow enthusiasts) — so the routing step is a real choice, not a foregone conclusion. Kill on sight any candidate not traceable to the inventory.

### 4. Research the shortlist (live)

Before scoring, research each shortlisted candidate so the scores rest on evidence:

- **2–3 comparable products in the member's niche** with any traction signal — Indie Hackers revenue pages, Starter Story interviews, ProductHunt, app-store listings, G2/Capterra category pages.
- **What similar experts, operators, and enthusiasts have productized** — search "[niche] software", "[niche] tool", "[hobby] app", vertical-SaaS lists.
- **Pricing signals** — what existing tools charge, and what the member's clients currently pay humans for the same job. The human price is the strongest anchor.
- **For passion candidates, what enthusiasts already pay for** — the apps, subscriptions, coaching, and gear they buy today. This is the check against an idea that is loved but never paid for.
- **Absence check** — if a candidate has *no* comparables and no current spend, the cheat sheet's "No Competitors = No Market" principle applies: cut it from the shortlist before scoring. It never gets a row in the scores table and cannot be the chosen idea — record the cut and the rule in the audit's Scores notes so the member sees why it went.

Collect 4–6 concrete data points across the shortlist. Say explicitly: competitors found here are *good news* — they are proof of demand, the inverse of how founders usually read them.

### 5. Score the shortlist

Score each candidate 1–3 on five axes, presented as a small table in conversation:

- **Pain frequency** — how often does the pain recur? Daily = 3.
- **Willingness to pay** — is someone already paying, in money or hours, to solve it today? (No current spend anywhere = no market.)
- **Buildability as MVP** — could a coding agent ship a usable v1 in weeks, ideally with a concierge version possible *this* week?
- **Distribution advantage** — can the member name the exact channel, or the exact first 10 users, from their existing business or community?
- **Staying power** — would the member still be working on this in two years if it earned little for a while? 3 = they'd do it anyway.

Highest total (out of 15) wins, but the score is a conversation-forcing device, not an oracle. Ties break on distribution advantage — the one axis the member uniquely controls. Passion earns its points in staying power and distribution; it never outweighs willingness to pay. A 3 for staying power on a candidate nobody pays for is still a hobby.

### 6. Route: for yourself first, or for the people around you

Apply one test to the front-runner: **"Who feels the pain most — you, or the people around you (your clients, or your fellow enthusiasts)?"** If that test is ambiguous, apply two tie-breakers **in order — the first that matches decides**:

1. If the candidate productizes something clients already pay for, **for-others wins** — existing invoices are pre-validation (the concierge-MVP principle), and this holds even for a member who has never shipped software: the concierge path lets them deliver manually while learning to ship.
2. Otherwise, if the member has never shipped software, **for-yourself-first is the lower-risk route** — the first user is guaranteed, honest, and free (the cheat sheet's be-your-own-customer principle). For a passion-only member this means building it for their own hobby first, then offering it to the community once it has earned a place in their own routine.

Name the route explicitly and record it. It changes who the Customer is in the downstream offer.

### 7. Converge on ONE

State the chosen idea in the one-sentence format and confirm it with the member. Park the runners-up with their scores in the template's Parking Lot — if the Mini-Launch on idea #1 gets zero replies, idea #2 is already pre-scored.

### 8. Fill the Idea Audit in place

Fill `BONUS-Idea-Audit.md` in place — never a sibling copy, per the root `AGENTS.md` rules. Match the template's structure exactly: same section headers, same italic prompts, same `> Good: ... / Bad: ...` guidance lines. Replace each `**Your answer:**` block, keep the scaffolding intact — write "Not applicable" under a lens the member doesn't bring. Add a dated header at the top ("Audited: [month year]") and a one-line research footer listing the comparables and pricing signals found. Read the existing file first to preserve any user notes.

### 9. Verify and hand off

Re-read the filled audit and check: every shortlisted idea traces to a named inventory item; every score has a one-line justification where it isn't obvious; exactly one route is named, with its reason; the One Idea reads as the offer-builder's intake, not a paragraph of hedging.

Then hand off, in order:

1. **`define-offer-builder`** — the mandatory next step. Open it with its two intake questions *already answered* from the idea brief: "What's the product, in one or two sentences?" → the chosen idea sentence. "Who is this for, today?" → the member themselves (for-yourself-first route), or the named client segment or enthusiast segment (for-others route).
2. **`BONUS-Idea-Validation-Cheat-Sheet.md`** — name the 1–2 tactics the route implies (for-yourself-first → Be-Your-Own-Customer; productized service → Concierge MVP; niche community position or a passion community → the insider-network tactics), but do not run them. Validation comes after the offer and the Mini-Launch.

## Idea-to-software patterns to draw on

Refresh via live research at invocation time, but these shapes tend to be durable.

### Paths that work

- **Productized service → tool.** The deliverable clients already buy, standardized and then software-ized. Bulk Mockup: a $300 manual Photoshop job turned into a $12K/mo product. Designjoy: a solo design practice productized to $2M ARR before any software existed.
- **Concierge → software.** Deliver the result manually first; automate only the steps people demonstrably pay for.
- **Internal tool → sellable SaaS.** Build for your own workflow, dogfood it for 30 days, then sell to lookalike businesses. Creator Buddy began as a personal spreadsheet and reached $300K ARR — the be-your-own-customer path.
- **Unique-data play.** Benchmarks, price lists, or records only an insider has, wrapped in search or retrieval. The closed-ecosystem position is the moat.
- **Judgment-encoding.** The expert's decision process turned into a guided flow or AI-assisted checklist, sold to juniors and peers who lack the judgment.
- **Hobby tool → community product.** Build the thing your own hobby is missing, then offer it to the people you already do the hobby with. Untappd began as a side project two craft-beer fans built for themselves and expected maybe ten friends to use. Discogs started as a programmer's database of his own electronic-music records.
- **Community ritual → software.** Something a community already does by hand — logging, comparing, competing, swapping — turned into the tool that does it. Strava grew out of two former rowing teammates missing the accountability and competition of training together.

### Failure patterns to name in-session

- **The CRM nobody asked for.** Rebuilding horizontal software (CRM, project management, invoicing) the market already serves. The member's edge is vertical, not horizontal.
- **"Portal" syndrome.** A client portal or dashboard as the default idea. Portals get logged into twice and die — unless clients already pay, in time or money, for the information inside.
- **Automating the part clients pay the human for.** Stripping out the judgment or relationship that is the actual product. Automate the delivery *around* the judgment, never the judgment's value.
- **The everything-app.** Trying to fix every inventory category in one product. One leverage point per MVP.
- **Expertise without distribution.** An idea aimed at a market the member has no access to. The audit exists precisely to keep ideas inside the member's reach.
- **The hobby with no wallet.** Enthusiasts love it, share it, and never pay for it. If nobody in the community spends money on the problem today, the passion is real but the market isn't.
- **Passion for the thing, not the problem.** Loving cycling isn't a pain point. The idea has to fix something that goes wrong, not celebrate something the member enjoys.
- **Building for the fun of building.** The build is the hobby and the customer is an afterthought. Fine as a hobby; not a first product.

## Pacing

- **Hypothesis first, inventory second, ideas third.** Never generate ideas before the inventory is done — blank-page brainstorming is what this skill exists to prevent.
- **One inventory category at a time.** The conversation is the audit.
- **Kill untraceable candidates immediately** — name the rule when you do it.
- **Converge, don't collect.** The session ends with one idea, or it failed.
- **Preserve the template scaffolding.** Headers, prompts, and good/bad lines stay — the audit gets revisited if the first idea's Mini-Launch comes back silent.

## What "done" looks like

A filled `BONUS-Idea-Audit.md` where: the Starting Point has real numbers (revenue and customers, or hours and money spent); every shortlisted idea traces to a named inventory item; all five axes are scored with one-line justifications; one route (for yourself first / for the people around you) is named with its reason; ONE chosen idea is stated in the offer-builder's intake format; runners-up are parked with scores; and the file carries a dated header and a one-line research footer.

A session that ends with a research-backed idea the member still wants to sleep on is a success — the audit holds the shortlist either way. A session that ends with three ideas is a failure of convergence; go back to step 5.

Recommended next step after a successful session: run `define-offer-builder` with the idea brief as its intake, then follow the standard Define checklist — persona, pricing, Mini-Launch. Validation tactics from the cheat sheet come after the offer, not before.
