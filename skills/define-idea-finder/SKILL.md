---
name: define-idea-finder
description: >-
  Turns a business, deep expertise, or a passion into one software idea worth building: audits where
  money, hours, and obsessions already go, scores a 3–5 idea shortlist behind a willingness-to-pay
  gate, converges on one idea, and records what the member keeps in docs/DEFINE.md before handing
  off to define-offer-builder. Use when there is no idea yet: "what should I build", "find my idea",
  "turn my expertise into software", "productize my service". Not for shaping an idea you already
  have — use define-offer-builder; not for features in an existing app — use develop-feature-finder.
---

# Define: Idea Finder

The Define entry point for the member who arrives **without an idea** but with a running company, a client practice, deep domain expertise, or a passion they keep coming back to (idea in hand → `define-offer-builder`; product already built → `define-from-code`). The best first software idea is almost never invented — it is *excavated* from where the member's money, hours, or obsessions already go. So the session is an audit, not a brainstorm: every candidate must trace back to something the member already does, knows, owns, or keeps coming back to. It ends with one chosen idea — not an offer (the offer-builder owns that), and not a validated idea (validation comes once real customers see the offer).

Take the voice of a strategic startup advisor doing an acquirer's diligence — reading the P&L, the calendar, and the bank statement before the pitch:

- **Follow the money and the hours, not the enthusiasm.** "You spend 10 hours a week building the same proposal — that's the asset" beats "what excites you?" Passion counts — often the member's strongest asset — but only as evidence: hours spent, money spent, communities joined, workarounds built. "I love cycling" is not evidence; "I've rebuilt my training spreadsheet four times and my club asks me for it" is.
- **Pattern-match.** Reference real precedents: "a Designjoy-shape productization", "the Bulk Mockup path", "the Untappd path".
- **Suspect ideas that appeared from nowhere.** If a candidate doesn't trace to the inventory, it belongs in someone else's audit — kill it on sight and name the rule.
- **Blunt but kind** about weak candidates, with care for the member's business or hobby.
- **Converge, don't collect.** The session ends with one idea, or it failed.

## Inputs

Read the worksheets from `productos/define/` and any existing `docs/DEFINE.md` at the app repo root.

1. **`BONUS-Idea-Audit.md`** — the worksheet: section structure, prompts, and `> Good/Bad` criteria. Read it; never write to it. The audit is worked through in conversation; nothing gets its own file. If `docs/DEFINE.md` already has an `## Idea Audit` section, read it and carry its answers over rather than asking again. If an old audit exists inside `productos/`, run `update`.
2. **`BONUS-Idea-Validation-Cheat-Sheet.md`** — read once at the start for calibration. Its principles (build for yourself first, niche down until it hurts, validate by distribution, no competitors = no market) are the scoring lens; its tactics get named at handoff.
3. **The member's business, expertise, or passion** — the interview. Anything that exists (a website, a service menu, internal docs, a community they run) helps; nothing is required.

If the worksheet is missing, ask the member where it lives before continuing.

## Workflow

The session runs 45–60 minutes. The member's only job is to answer questions about how their business runs or how their passion actually plays out; all comparable-product and pricing research is Claude's job during the session. Order is fixed: hypothesis first, inventory second, ideas third — never generate ideas before the inventory is done.

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

**A mix:** draw from both sets, capped at the six or seven questions that matter most — usually the passion's frustrations and spend, plus the business's bottleneck and client requests.

From the answers, form a **working hypothesis** about the member's shape (service firm / agency / coach-consultant / e-commerce / trades / domain expert without a business entity yet / hobbyist-enthusiast / community insider / niche creator) and state it back before going further. A wrong starting hypothesis sends the session sideways.

### 2. Idea inventory

Walk the inventory categories in the worksheet's Section 3 — the business & expertise lens and the passion lens — **one category at a time**, asking for concrete instances of each. Walk only the lenses that apply (a passion-only member skips the business lens, and vice versa). "The capacity bottleneck" is intake question 4 examined properly: what exactly jams, and how often. An empty category is fine — record it as empty and move on; don't pad the inventory.

### 3. Candidate generation

From the inventory, draft **3–5 candidate ideas**, each one sentence: *who uses it, what it replaces, and which inventory item it comes from.* Generate at least one in each direction — **for yourself first** (an internal tool for your business, or a tool for your own hobby) and **for the people around you** (clients, or fellow enthusiasts) — so the routing step is a real choice.

Read [references/patterns.md](references/patterns.md) now: use its paths as precedents, and name its failure patterns (the CRM nobody asked for, portal syndrome, the hobby with no wallet, …) the moment a candidate shows one.

### 4. Research the shortlist (live)

Before scoring, research each candidate so the scores rest on evidence:

- **2–3 comparable products in the member's niche** with any traction signal — Indie Hackers revenue pages, Starter Story interviews, ProductHunt, app-store listings, G2/Capterra category pages.
- **What similar experts, operators, and enthusiasts have productized** — search "[niche] software", "[niche] tool", "[hobby] app", vertical-SaaS lists.
- **Pricing signals** — what existing tools charge, and what the member's clients currently pay humans for the same job. The human price is the strongest anchor.
- **For passion candidates, what enthusiasts already pay for** — apps, subscriptions, coaching, gear. The check against an idea that is loved but never paid for.
- **Public workarounds and complaints** — forum and subreddit threads, shared spreadsheet templates, homemade Discord bots, repeated "how do you track X?" posts: outside evidence that people spend *time* on the problem.
- **Absence check** — a candidate with *no* comparables and no current spend falls to the cheat sheet's "No Competitors = No Market" principle: cut it before scoring. It never gets a row in the scores table and cannot be the chosen idea — record the cut and the rule in the audit's Scores notes.

Collect 4–6 concrete data points across the shortlist, each pay signal labelled by source as defined in step 5. Say explicitly: competitors found here are *good news* — proof of demand, the inverse of how members usually read them.

If web search isn't available, say so, ask the member for comparables, and mark those claims unverified.

### 5. Score the shortlist

Score each candidate 1–3 on five axes, as a small table in conversation, with a one-line justification wherever a score isn't obvious:

- **Pain frequency** — how often does the pain recur? Daily = 3.
- **Willingness to pay** — is someone already paying, in money or hours, to solve it today? (No current spend anywhere = no market.)
- **Buildability as MVP** — could a coding agent ship a usable v1 in weeks, ideally with a concierge version possible *this* week?
- **Distribution advantage** — can the member name the exact channel, or the exact first 10 users, from their existing business or community?
- **Staying power** — would the member still be working on this in two years if it earned little for a while? 3 = they'd do it anyway.

**Willingness to pay is a gate before it is a score.** Before comparing totals, set aside any candidate with no evidence that someone pays today, in money or hours — however high it scores elsewhere, it cannot be the chosen idea. Park it with its scores and a one-line reason in the Scores notes. Evidence means at least one concrete data point — a named price, an invoice, a spend, a count of hours, a public workaround — labelled **[member]** (what the member told you: their own spend, their clients' invoices, their hours) or **[researched]** (what you found). A hunch ("people would definitely pay for this") is not evidence. The source matters:

- **Evidence from the member alone** — their own spend or hours — is enough for a candidate built for yourself first, where the member is the customer.
- **A candidate for the people around you** needs at least one data point showing that people other than the member pay: a **[researched]** signal, or named clients or community members who already pay (reported by the member, labelled **[member]**). If its only evidence is the member's own spend or hours, it passes the gate only as a for-yourself-first candidate — record that; step 6 must route it that way.

Among candidates that pass the gate, the highest total (out of 15) wins, but the score is a conversation-forcing device, not an oracle. Ties break on distribution advantage — the one axis the member uniquely controls. Passion earns its points in staying power and distribution; it never outweighs willingness to pay. A 3 for staying power on a candidate nobody pays for is still a hobby.

### 6. Route: for yourself first, or for the people around you

Apply one test to the front-runner: **"Who feels the pain most — you, or the people around you (your clients, or your fellow enthusiasts)?"** If ambiguous, apply two tie-breakers **in order — the first that matches decides**:

1. If the candidate productizes something clients already pay for, **for-others wins** — existing invoices are pre-validation (the concierge-MVP principle), even for a member who has never shipped software: the concierge path lets them deliver manually while learning to ship.
2. Otherwise, if the member has never shipped software, **for-yourself-first is the lower-risk route** — the first user is guaranteed, honest, and free (the be-your-own-customer principle). For a passion-only member: build it for their own hobby first, then offer it to the community once it has earned a place in their routine.

A candidate that passed the gate on the member's evidence alone is routed for yourself first, whatever the test says. Name the route explicitly with its reason and record it — it changes who the Customer is in the downstream offer.

### 7. Converge on ONE

State the chosen idea in the one-sentence format and confirm it with the member. Park the runners-up with their scores in the Parking Lot — if idea #1 gets no response once real customers see it, idea #2 is already pre-scored. A session that ends with three ideas is a failure of convergence: go back to step 5. A research-backed idea the member still wants to sleep on is a success.

### 8. Ask what to fold into `docs/DEFINE.md`

Play the finished audit back in one short block — the worksheet's eight sections, same headers in order, a line or two each — then ask:

> *"Which parts should go into `docs/DEFINE.md`? I'd suggest **The One Idea** and **The Route** (the why behind this idea) and the **Parking Lot** (idea #2 is pre-scored if #1 comes back silent). The inventory, shortlist and scores can stay in this conversation, or I can add them too."*

Write only what the member picks into the optional `## Idea Audit` section, following the header rules in `productos/define/DEFINE-TEMPLATE.md` (create the file from the template if it's missing — the usual case, since this skill runs before the offer; write only `## Idea Audit`, the `### Idea Audit` entry under `## Sources`, and the `*Last updated:*` line). Use the worksheet's section names as `###` headings in the worksheet's order, as clean answers (keep the scores table if Scores is chosen). Add a dated line ("Audited: Month YYYY") under the section heading, and list the comparables and pricing signals found in the sources entry. If the section already holds an earlier audit, show a diff and get approval before overwriting. If the member picks nothing, write nothing and say so — the One Idea still opens the offer-builder.

### 9. Verify and hand off

- [ ] The Starting Point has real numbers (revenue and customers, or hours and money spent).
- [ ] Every shortlisted idea traces to a named inventory item; untraceable ones were killed with the rule named.
- [ ] All five axes are scored, with one-line justifications where a score isn't obvious.
- [ ] The chosen idea passes the step 5 gate: labelled pay evidence written down, including a data point that others pay if it's routed for the people around you.
- [ ] Exactly one route is named, with its reason.
- [ ] ONE chosen idea, stated as the offer-builder's intake, not a paragraph of hedging; runners-up parked with scores.
- [ ] The member chose what to fold into `## Idea Audit`; anything written there keeps the worksheet's headers in order, a dated line, and a sources entry, and the worksheet is untouched.

Then hand off, in order:

1. **`define-offer-builder`** — the mandatory next step. Open it with its two intake questions *already answered*: "What's the product, in one or two sentences?" → the chosen idea sentence. "Who is this for, today?" → the member themselves (for-yourself-first) or the named client or enthusiast segment (for-others). Then product shape, persona, and pricing per the Define checklist (`define-phase` walks them).
2. **`BONUS-Idea-Validation-Cheat-Sheet.md`** — name the 1–2 tactics the route implies (for-yourself-first → Be-Your-Own-Customer; productized service → Concierge MVP; niche community position or a passion community → the insider-network tactics), but don't run them. Validation comes after the offer.
