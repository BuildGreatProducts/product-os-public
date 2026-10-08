# Marketplace Listing

*This is a worksheet for the `design-marketplace-listing` skill. The skill reads `docs/DEFINE.md` (Offer, Product Shape, Pricing Strategy), the Product Identity in `docs/DESIGN.md`, `docs/COPY.md` if present, and `docs/MAGIC-MOMENT.md`, picks the stores, marketplaces, registries, and directories the product's shape needs, and writes the filled version to `docs/MARKETPLACE-LISTING.md` using the structure below — one **Listing** section per store, primary store first. For the App Store and Google Play, use the `design-app-listing` skill (worksheet: `4b-App-Store-Listing.md`); for the product's own website, use `design-landing-page` (worksheet: `4a-Landing-Page.md`). This file itself is never filled in.*

---

## Summary

[Two sentences: the product shape, the listings this file covers (primary first), and the one-line pitch that leads every listing.]

## The Magic Moment we're promising

> [One sentence from `docs/MAGIC-MOMENT.md`.]

**One-line pitch:** "[the pitch, as it appears in the primary store's results list]"
**First visual:** [what the first screenshot or demo shows — the magic moment in the host]

## Listings in this file

| Store | Why this store | Priority | Facts verified |
| --- | --- | --- | --- |
| [store name] | [primary acquisition surface / secondary shape / reach] | [primary / secondary] | [date checked, or "unverified"] |

---

## Listing — [Store name]

*Repeat this section for every store in the table above. Skip a field the store doesn't have and say so in one line.*

### Name

- **Copy:** "[exact name as it appears in the store]"
- **Character count:** [exact / limit]
- **Identifier:** [package name, plugin ID, namespace, or slug — and its availability check]
- **Naming rules checked:** [the store's restrictions, e.g. no host trademarks]
- **Reference:** Tactic #1

> Good: "Clause — contract review for freelancers" — brand plus the job, inside the limit, the buyer's search term present
> Bad: "Clause AI Pro" — no job, no search term; or "ChatGPT Contract Helper" — borrows a host trademark the store bars

### One-line pitch

- **Copy:** "[exact summary / short description]"
- **Character count:** [exact / limit]
- **Primary keyword:** "[keyword]"
- **Reference:** Tactic #2

> Good: "Flags the clauses that cost freelancers money — before you sign." — who, outcome, under the limit
> Bad: "An AI-powered assistant that helps with all your legal needs." — no customer, no outcome, category-default words

### Icon

- **Direction:** [the mark, colours from `docs/DESIGN.md`, treatment]
- **Spec:** [size, format, padding the store requires]
- **Small-size test:** [how it reads at the store's smallest rendered size]
- **Reference:** Tactic #3

### Description

- **Opening lines (visible before truncation):** "[exact copy]"
- **Body:** [exact copy in the store's supported formatting — what it does, who it's for, how it works, what it accesses, pricing, support]
- **Character count:** [exact / limit]
- **Reference:** Tactics #4–5

> Good: the first two lines stand alone as the pitch; sections the store renders; product nouns match `docs/COPY.md`
> Bad: a pasted landing page truncated mid-sentence; Markdown the store shows as raw symbols

### Category, tags, and keywords

- **Category:** [from the store's fixed list — and why buyers browse there]
- **Tags / keywords:** [each term once — count / limit]
- **Reference:** Tactic #7

### Visual assets brief

- **Visual 1 — the magic moment:** [what it shows, in the host] · Caption: "[exact caption]" · Spec: [size]
- **Visual 2 — the mechanism:** [what it shows] · Caption: "[exact caption]" · Spec: [size]
- **Visual 3 — the proof or result:** [what it shows] · Caption: "[exact caption]" · Spec: [size]
- **Additional visuals:** [up to the store's limit — or "none"]
- **Promo tile / banner / video:** [spec and direction — or "not used by this store"]
- **Reference:** Tactic #6

> Good: the extension's panel open on a real web page, caption "Every risky clause, highlighted"
> Bad: the logo on a gradient; a stock photo of a laptop

### Install and first-run instructions

- **Install action:** "[exact install command, button text, or duplicate link — per host if several]"
- **First thing to do:** "[the first prompt, command, or action — matching `docs/ONBOARDING.md`]"
- **What they should see:** [the expected first output]
- **If it doesn't work:** "[one troubleshooting line]"
- **Tested on a clean setup:** [date / host — or "to test before submission"]
- **Reference:** Tactic #8

> Good: `/plugin install clause@clause-tools`, then "Try: review contracts/acme.pdf" — tested last release
> Bad: "Install the usual way and configure as needed."

### Access and data statement

- **Reads:** [what it can read]
- **Writes:** [what it can change]
- **Sends:** [what leaves the user's machine or account, and where]
- **Permission justifications:** [one line per permission or scope]
- **Reference:** Tactic #9

### Pricing display

- **How this store shows price:** [native price field / free listing with external payment / plan tiers]
- **Copy:** "[exact pricing line(s) — mirroring `docs/DEFINE.md` → Pricing Strategy]"
- **Store fee:** [the store's cut and how the price accounts for it]
- **Reference:** Tactic #10

### Proof and support

- **Proof:** [real ratings, installs, testimonials — or `[none yet — omit]`]
- **Support:** [link and response commitment]
- **Reference:** Tactic #11

### Review and policy checklist

- [ ] [store policy item — e.g. privacy policy URL live]
- [ ] [store policy item — e.g. each permission justified in the store's form]
- [ ] [store policy item — e.g. test account with sample data for reviewers]
- [ ] [store policy item — e.g. demo video uploaded]
- **Expected review time:** [from the store's docs — dated]
- **Reference:** Tactic #12 and the store's section of `productos/design/BONUS-Marketplace-Listing-Best-Practice.md`

---

## Cross-listing consistency

- **Same promise everywhere:** [the pitch, adapted to each store's limit]
- **Differences by store:** [what changes per store and why — reader, limits, formatting]
- **Shared assets:** [which visuals are reused, resized, or store-specific]

## Anti-patterns avoided

[3–5 bullets from the BONUS doc — which anti-patterns these listings deliberately avoid and why.]

## Refresh cadence

Recommended next refresh: [the next release, or 60–90 days]. First experiment: [the first visual or the one-line pitch, where the store supports it]. Refresh trigger: [listing-view-to-install rate below [N]% for [duration], or a rejected update].

## Sources

- Reference: `productos/design/BONUS-Marketplace-Listing-Best-Practice.md` ([store sections used])
- Store facts: [official doc URLs checked, with dates — or "unverified"]
- Tone of voice: `docs/DESIGN.md` → Product Identity
- Magic moment: `docs/MAGIC-MOMENT.md`
- Product context and pricing: `docs/DEFINE.md`
- Lexicon (if available): `docs/COPY.md`
