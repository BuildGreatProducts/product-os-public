# CRO audit report template

The structure of `docs/CRO-AUDIT.md`. Tables, not paragraphs — the whole document reads in 5–8 minutes for a developer skimming for fixes. An area that doesn't apply to the product type keeps its heading with one line: "N/A — [reason]."

```
# Conversion Rate Optimization Audit

*Drafted: [Month Year]. Product type: [type]. Framework: [framework]. Primary conversion event: [event].*

## Summary

[Three sentences: how many total findings, top P0/P1 count, the single highest-impact recommendation.]

## Top 5 fixes ranked by effort × impact

1. **[Finding]** — [location] — Severity P[X], Effort [S/M/L], Est. impact [%]. [One-sentence fix.]
2. ...
3. ...
4. ...
5. ...

---

## A. Performance & Core Web Vitals

**Current state ([measured with <tool> | estimated from code]):**
- LCP: [value or estimate based on hero / images / fonts]
- INP: [value or estimate based on JS-heavy interactive surfaces]
- CLS: [value or estimate based on image dimensions, font swap, dynamic content]

**Findings:**

| # | Finding | Location | Sev | Effort | Est. Impact | Fix |
| --- | --- | --- | --- | --- | --- | --- |
| A1 | [finding] | `[file]:[line]` | P0 | S | ~X% | [fix] |
| A2 | ... | ... | ... | ... | ... | ... |

---

## B. Above-the-Fold Hero & CTA
[same structure]

## C. Signup / Form Conversion
[same structure]

## D. Trust Signals & Social Proof
[same structure]

## E. Pricing Page Surface
[same structure]

## F. Mobile Responsiveness & Touch Targets
[same structure]

## G. Paywall & Subscription Surfaces
[same structure, mobile / subscription products only]

## H. Analytics & Conversion Tracking
[same structure]

## I. A/B Testing Infrastructure
[same structure]

## J. Onboarding & First-Session Activation
[same structure]

## K. SEO & Discoverability
[same structure]

---

## Cross-cutting quick wins

[bullet list of the 5 quick-win categories with specific findings]

## Strategy-code drift (if ProductOS docs present)

[Findings where documented strategy ≠ shipped code.]

## Verification next steps

- [ ] Re-measure LCP, INP, CLS using PageSpeed Insights and field data (CrUX)
- [ ] Confirm primary conversion event fires correctly in analytics
- [ ] Re-test on actual mobile devices, not just responsive emulator
- [ ] Take screenshots of the fix locations to confirm changes shipped

## Sources & calibration

- Industry benchmarks: [each benchmark cited above, with its source and year]
- Workspace docs referenced (if present): `docs/DEFINE.md`, `docs/DESIGN.md` (Product Identity), `docs/MAGIC-MOMENT.md`, `docs/ONBOARDING.md`, `docs/LANDING-PAGE.md`, `productos/design/BONUS-[X]-Best-Practice.md`
```
