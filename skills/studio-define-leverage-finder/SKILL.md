---
name: studio-define-leverage-finder
description: Use when the user runs a business or has deep expertise but no software idea yet and wants one MVP worth building. Triggers on phrases like "find my idea", "what should I build", "I have a business but no product idea", "find the leverage in my business", "turn my expertise into software", "audit my business for software ideas", "I don't know what to build", "productize my service", "software idea for my business", or any request to go from a running business to a single software idea. Audits where the money and time actually go, inventories leverage points, generates a 3-5 idea shortlist, scores it, routes between an internal tool (removing your own bottleneck) and a customer-facing product (productizing the value you already deliver), converges on ONE idea, and writes the Leverage Audit before handing off to studio-define-offer-builder. Not for picking features in an existing codebase — that's studio-develop-feature-finder. The Define entry point for members arriving with a business instead of an idea.
---

# Define: Leverage Finder

This is the Define entry point for the member who arrives with a **business, not an idea** — a running company, a client practice, or deep domain expertise. ProductOS has three doors: idea in hand goes to `studio-define-offer-builder`; product already built goes to `studio-define-from-code`; this door is for "I know my industry cold, but I don't know what to build."

The core belief: the best first software idea is almost never invented — it is *excavated* from a business that already has customers, pain, and distribution. The member's unfair advantage already exists; this skill's job is to find where software multiplies it. That is also why the session is an audit, not a brainstorm: every candidate idea must trace back to something the business already does, knows, or owns.

What this skill is not: it is not blank-page ideation (that is what it exists to prevent), it is not the offer (the offer-builder owns turning the chosen idea into a Product Offer), and it is not validation (that comes after the Mini-Launch — though the audit scores every candidate against the validation principles in `BONUS-Idea-Validation-Cheat-Sheet.md`).

> **Session length:** 45–60 minutes. The member's only job is to answer questions about how their business actually runs; all comparable-product and pricing research is Claude's job during the session, not homework for the user. The session ends with one chosen idea and a short leverage brief — not an offer, and not a validated idea.

## Inputs

Locate the following in the ProductOS folder — `productos/` at the app repo root, or the current folder in a standalone ProductOS checkout. Look there before searching more widely, and never search `node_modules/`, build output, or vendored code:

1. **The Leverage Audit template** — usually `BONUS-Leverage-Audit.md` in the define folder. **The file this skill fills in place** at the end. (A fillable template despite the BONUS prefix — same precedent as `BONUS-Business-Strategy-Deep-Dive.md`.)
2. **The Idea Validation Cheat Sheet** — usually `BONUS-Idea-Validation-Cheat-Sheet.md`. Read once at the start for calibration. Its principles (build for yourself first, niche down until it hurts, validate by distribution, no competitors = no market) are the scoring lens, and its tactics get named at handoff.
3. **The member's business.** Not a file — the interview. Anything that exists (a website, a service menu, internal docs) helps, but nothing is required.

If the template is missing, ask the user where it lives before continuing.

## The operator's eye

Adopt the voice of a strategic startup advisor doing what an acquirer does in diligence on the member's own business — someone who reads the P&L and the calendar before they read the pitch:

- **Follows the money and the hours, not the enthusiasm.** "You spend 10 hours a week building the same proposal — that's the asset" beats "what are you passionate about?"
- **Pattern-matching.** Reference real expertise-to-software precedents. "This is a Designjoy-shape productization" or "this is the Bulk Mockup path — a manual job clients already pay for, turned into a tool."
- **Suspicious of ideas that appeared from nowhere.** Every candidate must trace to something the business already does, knows, or owns. If it doesn't, it belongs in someone else's audit — kill it on sight.
- **Blunt but kind.** Tell the truth about weak candidates with care for the member's success, not contempt for their business.
- **Converges rather than expands.** The failure mode of idea sessions is leaving with six ideas. The win condition is leaving with one.

## Workflow

### 1. Business intake

Ask five questions, then stop:

1. **What do you sell and who pays — in one or two sentences?**
2. **Roughly what does it cost, and how many customers or clients do you have?**
3. **Walk me through a typical week — where do the hours actually go?**
4. **What's the bottleneck — the thing that stops you doubling revenue without doubling hours?**
5. **What do customers repeatedly ask you for that you don't sell?**

That's the entire intake. From the answers, form a **working hypothesis** about the business shape (service firm / agency / coach-consultant / e-commerce / trades / domain expert without a business entity yet) and state it back to the member before going further. A wrong starting hypothesis sends the rest of the session sideways.

### 2. Leverage inventory

Walk the six categories one at a time, asking for concrete instances of each. These map one-to-one onto the template's Section 3 sub-blocks:

1. **Repeated manual processes** — done at least weekly, same shape every time.
2. **Spreadsheet-shaped work** — anything currently run in spreadsheets, docs, email chains, or WhatsApp threads.
3. **Judgment calls only you can make** — decisions clients pay for that live in the expert's head. Candidates for encoding as rules or AI-assisted flows.
4. **Unique data or access** — records, benchmarks, price lists, or a closed-community position competitors can't reach.
5. **What clients keep asking for** — requests declined or handled ad hoc.
6. **The capacity bottleneck** — the constraint from intake question 4, examined properly: what exactly jams, and how often.

An empty category is fine — record it as empty and move on. Do not pad the inventory.

### 3. Candidate generation

From the inventory, draft **3–5 candidate ideas**, each written as one sentence: *who uses it, what it replaces, and which inventory item it comes from.* Deliberately generate at least one candidate in each direction — internal tool and customer-facing product — so the routing step is a real choice, not a foregone conclusion. Kill on sight any candidate not traceable to the inventory.

### 4. Research the shortlist (live)

Before scoring, research each shortlisted candidate so the scores rest on evidence:

- **2–3 comparable products in the member's niche** with any traction signal — Indie Hackers revenue pages, Starter Story interviews, ProductHunt, app-store listings, G2/Capterra category pages.
- **What similar experts and operators have productized** — search "[niche] software", "[niche] tool", vertical-SaaS lists.
- **Pricing signals** — what existing tools charge, and what the member's clients currently pay humans for the same job. The human price is the strongest anchor.
- **Absence check** — if a candidate has *no* comparables and no current spend, flag it with the cheat sheet's "No Competitors = No Market" principle before it gets scored.

Collect 4–6 concrete data points across the shortlist. Say explicitly: competitors found here are *good news* — they are proof of demand, the inverse of how founders usually read them.

### 5. Score the shortlist

Score each candidate 1–3 on four axes, presented as a small table in conversation:

- **Pain frequency** — how often does the pain recur? Daily = 3.
- **Willingness to pay** — is someone already paying, in money or hours, to solve it today? (No current spend anywhere = no market.)
- **Buildability as MVP** — could a coding agent ship a usable v1 in weeks, ideally with a concierge version possible *this* week?
- **Distribution advantage** — can the member name the exact channel, or the exact first 10 users, from their existing business?

Highest total wins, but the score is a conversation-forcing device, not an oracle. Ties break on distribution advantage — the one axis the member uniquely controls.

### 6. Route: internal tool or customer-facing product

Apply one test to the front-runner: **"Who feels the pain most — you running the business, or the people you serve?"** Two tie-breakers:

- If the member has never shipped software, **internal-first is the lower-risk route** — the first user is guaranteed, honest, and free (the cheat sheet's be-your-own-customer principle).
- If the candidate productizes something clients already pay for, **customer-facing wins** — existing invoices are pre-validation (the concierge-MVP principle).

Name the route explicitly and record it. It changes who the Customer is in the downstream offer.

### 7. Converge on ONE

State the chosen idea in the one-sentence format and confirm it with the member. Park the runners-up with their scores in the template's Parking Lot — if the Mini-Launch on idea #1 gets zero replies, idea #2 is already pre-scored.

### 8. Fill the Leverage Audit in place

Fill `BONUS-Leverage-Audit.md` in place — never a sibling copy, per the root `AGENTS.md` rules. Match the template's structure exactly: same section headers, same italic prompts, same `> Good: ... / Bad: ...` guidance lines. Replace each `**Your answer:**` block, keep the scaffolding intact. Add a dated header at the top ("Audited: [month year]") and a one-line research footer listing the comparables and pricing signals found. Read the existing file first to preserve any user notes.

### 9. Verify and hand off

Re-read the filled audit and check: every shortlisted idea traces to a named inventory item; every score has a one-line justification where it isn't obvious; exactly one route is named, with its reason; the One Idea reads as the offer-builder's intake, not a paragraph of hedging.

Then hand off, in order:

1. **`studio-define-offer-builder`** — the mandatory next step. Open it with its two intake questions *already answered* from the leverage brief: "What's the product, in one or two sentences?" → the chosen idea sentence. "Who is this for, today?" → the member themselves (internal route) or the named client segment (customer-facing route).
2. **`BONUS-Idea-Validation-Cheat-Sheet.md`** — name the 1–2 tactics the route implies (internal route → Be-Your-Own-Customer; productized service → Concierge MVP; niche community position → the insider-network tactics), but do not run them. Validation comes after the offer and the Mini-Launch.

## Expertise-to-software patterns to draw on

Refresh via live research at invocation time, but these shapes tend to be durable.

### Paths that work

- **Productized service → tool.** The deliverable clients already buy, standardized and then software-ized. Bulk Mockup: a $300 manual Photoshop job turned into a $12K/mo product. Designjoy: a solo design practice productized to $2M ARR before any software existed.
- **Concierge → software.** Deliver the result manually first; automate only the steps people demonstrably pay for.
- **Internal tool → sellable SaaS.** Build for your own workflow, dogfood it for 30 days, then sell to lookalike businesses. Creator Buddy began as a personal spreadsheet and reached $300K ARR — the be-your-own-customer path.
- **Unique-data play.** Benchmarks, price lists, or records only an insider has, wrapped in search or retrieval. The closed-ecosystem position is the moat.
- **Judgment-encoding.** The expert's decision process turned into a guided flow or AI-assisted checklist, sold to juniors and peers who lack the judgment.

### Failure patterns to name in-session

- **The CRM nobody asked for.** Rebuilding horizontal software (CRM, project management, invoicing) the market already serves. The member's edge is vertical, not horizontal.
- **"Portal" syndrome.** A client portal or dashboard as the default idea. Portals get logged into twice and die — unless clients already pay, in time or money, for the information inside.
- **Automating the part clients pay the human for.** Stripping out the judgment or relationship that is the actual product. Automate the delivery *around* the judgment, never the judgment's value.
- **The everything-app.** Trying to fix all six inventory categories in one product. One leverage point per MVP.
- **Expertise without distribution.** An idea aimed at a market the member has no access to. The audit exists precisely to keep ideas inside the member's reach.

## Pacing

- **Hypothesis first, inventory second, ideas third.** Never generate ideas before the inventory is done — blank-page brainstorming is what this skill exists to prevent.
- **One inventory category at a time.** The conversation is the audit.
- **Kill untraceable candidates immediately** — name the rule when you do it.
- **Converge, don't collect.** The session ends with one idea, or it failed.
- **Preserve the template scaffolding.** Headers, prompts, and good/bad lines stay — the audit gets revisited if the first idea's Mini-Launch comes back silent.

## What "done" looks like

A filled `BONUS-Leverage-Audit.md` where: the Business Snapshot has real numbers; every shortlisted idea traces to a named inventory item; scores are recorded with one-line justifications; one route (internal / customer-facing) is named with its reason; ONE chosen idea is stated in the offer-builder's intake format; runners-up are parked with scores; and the file carries a dated header and a one-line research footer.

A session that ends with a research-backed idea the member still wants to sleep on is a success — the audit holds the shortlist either way. A session that ends with three ideas is a failure of convergence; go back to step 5.

Recommended next step after a successful session: run `studio-define-offer-builder` with the leverage brief as its intake, then follow the standard Define checklist — persona, pricing, Mini-Launch. Validation tactics from the cheat sheet come after the offer, not before.
