---
name: develop-cro-audit
description: >-
  Audits a built product's code for conversion — forms, CTAs, Core Web Vitals, analytics, mobile,
  paywall placement, trust signals — and writes a prioritized fix list to docs/CRO-AUDIT.md. Use
  when the user asks for a "CRO audit", "why aren't users converting", or "what's hurting my signup
  rate". Works standalone or with ProductOS docs. Not for users who sign up but never activate or
  return — use distribute-activation-retention-audit; not for writing landing page copy — use
  design-landing-page.
---

# Develop: Conversion Rate Optimization Audit

This skill runs in the **app repo** — the repository that contains `productos/` — and produces a prioritized **conversion rate optimization audit** of the current code. The output is `docs/CRO-AUDIT.md` (creating `docs/` if needed): a scored breakdown of conversion-relevant surfaces — performance, forms, CTAs, trust signals, paywall placement, analytics tracking, mobile experience, and onboarding — with each issue tagged by severity, location in the codebase, and the fix.

**Shapes:** runs in full for the screen shapes (`web-app`, `mobile-app`, `desktop-app`, `browser-extension`) and a `website`; for every other shape, audit only the conversion surfaces it has — its landing page, listing, booking page, or checkout.

## Inputs

Read inputs from `docs/` and the reference docs from `productos/design/` at the app repo root. In a repo without ProductOS, the optional docs are simply absent — proceed standalone.

1. **The product codebase** — **required**. The skill runs in the repository root and scans the source files.
2. **`docs/DEFINE.md`** — **recommended**. Its Summary and Offer give the product type and customer; its Pricing Strategy gives the business model — which drives which audit areas matter most. If absent, ask one question: *"What kind of product is this — mobile app / B2B SaaS / marketplace / API or developer tool / landing page / browser extension / productized service portal? And what's the primary conversion event you care about — signup, free-trial start, paid conversion, first transaction, first AI output?"*
3. **The relevant BONUS reference** — optional:
   - `productos/design/BONUS-Web-Landing-Page-Best-Practice.md` for web/desktop conversion patterns
   - `productos/design/BONUS-App-Store-Listing-Best-Practice.md` for mobile listing context
   - `productos/design/onboarding/BONUS-[Type]-Onboarding-Best-Practice.md` for in-product activation
4. **`docs/MAGIC-MOMENT.md` and the `## Product Identity` section of `docs/DESIGN.md`** — optional. The activation event the audit measures against, and the tone applied to copy critiques.
5. **`docs/COPY.md`** — optional. When present, copy critiques audit against its review rubric and lexicon — not just the Identity's tone words — and error-message findings cite its error anatomy.

## The auditor's voice

A senior CRO consultant doing a technical code review — surfacing what's bleeding conversion, not reassuring.

- **Honest about severity.** A 3-second LCP is a P0; a missing alt tag is a P3. Don't conflate them, and don't pad the report.
- **Specific to the file.** Never "the signup form has too many fields." Always "`src/components/SignupForm.tsx:42–67` has 8 required fields; the benchmark is 1–2."
- **Effort × impact aware.** A 4-hour fix that lifts conversion 6% (P1, effort S) beats a 40-hour fix that lifts it 8% (P2, effort L).
- **Reference-anchored.** Every benchmark cited comes from the ProductOS BONUS docs (if present) or [references/benchmarks.md](references/benchmarks.md), with its source.
- **Code-review tone.** The member is a developer or technical founder; give findings they can implement, not marketing bullets they have to translate.

## Workflow

### 1. Detect the product type and framework

Detect the framework and platform from the repo's manifests and config before scanning, so the file-structure heuristics apply. Cross-reference the product type in `docs/DEFINE.md` if present; otherwise ask (Inputs, item 2).

State the setup back: *"Detected: [framework] for [product type]. Auditing against the [BONUS reference] pattern, primary conversion event: [event]. Confirm or correct."*

### 2. Scan all eleven audit areas

Read [references/audit-areas.md](references/audit-areas.md) for the eleven areas (A–K) and the code patterns to scan for in each, and [references/benchmarks.md](references/benchmarks.md) for the thresholds and figures findings cite. Walk every area in order and scan before drafting any findings — a partial audit produces a misleading priority order. Honor the product type: mark an area N/A with a one-line reason rather than auditing a paywall on an open-source dev tool or a pricing page on a commission-only marketplace.

For Core Web Vitals (area A): if a browser or PageSpeed tool is connected, measure LCP, INP, and CLS; otherwise estimate from code and say so in the report.

### 3. Score and prioritize each finding

For every issue, capture:

- **Area** (A–K)
- **Finding** — one sentence
- **Location** — file path + line number(s) where applicable
- **Severity** — P0 / P1 / P2 / P3
- **Effort** — S (<4 hrs) / M (1–2 days) / L (>2 days)
- **Estimated impact** — % conversion lift if a benchmark documents it; otherwise a relative scale
- **Fix** — one specific paragraph with the code-level change

**Severity rubric:**
- **P0** — bleeding conversion daily; fix this week (e.g., LCP >4s, signup form with 8+ fields, no mobile viewport tag)
- **P1** — meaningful conversion loss; fix this month (e.g., missing above-fold social proof, generic CTA copy, no analytics tracking)
- **P2** — moderate optimization opportunity; fix this quarter (e.g., no per-tier testimonials on pricing, missing favicon variants)
- **P3** — minor; fix when convenient (e.g., missing `llms.txt`, missing alt text on decorative images)

### 4. Run the cross-cutting quick wins check

Beyond A–K, check five categories that almost always have at least one finding:

1. **The one-form-field-too-many.** Most signup forms have a field that could be removed or deferred. Name it.
2. **The CTA that doesn't match its destination.** "Get a demo" linking to a 10-field demo form is a click-to-bounce. Audit CTA → landing-page match.
3. **The "modern" sans-serif nobody can read at 14px.** Inter Display at 13px body is fashionable and illegible. Flag.
4. **The dark mode that wasn't tested.** If a dark mode toggle exists, check both modes for any element that becomes invisible in one — screenshot both if a browser tool is connected; otherwise compare the color tokens for each theme in code and say so.
5. **The cookie banner blocking the hero.** If it covers >30% of the above-fold area on first load, it's killing conversion before the visitor reads anything.

### 5. Cross-reference against ProductOS docs (if present)

If `docs/DEFINE.md`, `docs/MAGIC-MOMENT.md`, `docs/ONBOARDING.md`, or `docs/LANDING-PAGE.md` exist, check:

- Does the shipped onboarding match the documented flow in `ONBOARDING.md`?
- Does the landing page hero copy match the spec in `LANDING-PAGE.md`?
- Does the activation event in `MAGIC-MOMENT.md` actually fire — and is it tracked in analytics?
- Does product copy match the Identity's tone — and, when `docs/COPY.md` exists, pass its review rubric (lexicon, budgets, banned words)?

Discrepancies between documented strategy and shipped code are P1 findings — the strategy work was done, but the code drifted from it.

### 6. Walk the member through the findings

The conversation about the findings is the point of this skill, not just the file at the end. Present them in three checkpoints, confirming and refining at each before moving on:

1. **The headline** — the Top 5 fixes by effort × impact, plus every P0 and P1 grouped by area. Get confirmation or extra context (a known constraint, a fix already in flight).
2. **The rest** — P2/P3 findings by area (and any N/A areas with their reasons), the quick wins, and any strategy-code drift.
3. **Approve to write** — confirm the final ranking before writing the file.

### 7. Write to `docs/CRO-AUDIT.md`

Read [templates/cro-audit-report.md](templates/cro-audit-report.md) and write the approved report in that structure (`mkdir -p docs` if needed). Cite every benchmark with its source.

### 8. Verify before delivering

- [ ] Every audit area A–K is covered with a findings table, or marked N/A with a reason.
- [ ] Every finding has area, severity, effort, estimated impact, a specific fix, and a file path + line number(s) where applicable — "the signup form" is a vibe; `src/components/SignupForm.tsx:42–67` is a fix.
- [ ] Severities are honest — no missing alt tag as P0, no 5-second LCP as P3.
- [ ] The Top 5 fixes are sorted by effort × impact, not severity alone, and sit at the top.
- [ ] The audit honors the product type — no paywall finding for an open-source dev tool, no SEO finding for a browser extension, no App Store finding for B2B SaaS.
- [ ] Cross-cutting quick wins are listed.
- [ ] If ProductOS docs are present, strategy-code drift has its own section.
- [ ] Core Web Vitals say whether they were measured or estimated from code.
- [ ] Every benchmark cited carries its source; the verification next steps are specific, not generic.
- [ ] The document reads in 5–8 minutes — tables, not paragraphs.

Deliver the file path and a tight summary — total findings, P0 count, top 3 fixes by name. The doc is the deliverable.

**Next step:** implement the Top 5 (P0s and S/M effort first), instrument missing analytics events, take a baseline measurement (PageSpeed Insights, analytics funnel, paywall conversion rate), and re-run this skill in 30 days to measure the lift.
