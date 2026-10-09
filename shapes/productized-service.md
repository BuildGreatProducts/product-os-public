# Shape: Productized service

*Slug: `productized-service` · Family: Other*

## Contents

- [What it is](#what-it-is)
- [Live means](#live-means)
- [First sale means](#first-sale-means)
- [Define notes](#define-notes)
- [Design route](#design-route)
- [Develop route](#develop-route)
  - [What the PRD must cover](#what-the-prd-must-cover)
  - [Go live](#go-live)
- [Distribute notes](#distribute-notes)
- [Watch-outs](#watch-outs)

## What it is

A fixed-scope outcome delivered for a fixed price, with AI doing much of the work behind the scenes: AI-assisted bookkeeping, done-for-you SEO content, a monthly design subscription, a 48-hour pitch-deck rewrite. The customer pays for the result, not for a tool they operate — so the "product" is the offer, the delivery process (the SOP), and the tooling that makes it fast and consistent. It lives on a sales page with a booking or checkout link, and delivery runs through the member's own stack (forms, AI workflows, a shared folder or client portal). It's the classic first step of a sequenced product: deliver by hand with AI help, learn what clients pay for, then turn the proven process into a `web-app`.

## Live means

A booking or checkout page is live on a public URL with the price and scope stated, and one real client has been delivered the outcome end to end through the documented process — intake, delivery, QA, handover — on the real tooling, not a one-off favour.

## First sale means

A real client (warm network counts; a pilot paid in kind doesn't) pays the stated price — through a Stripe Payment Link or Checkout on the sales page, a paid invoice (Stripe Invoicing or the member's accounting tool), the first charge of a monthly retainer, or a marketplace order (Upwork, Fiverr, Contra) whose funds are released to the member.

## Define notes

- **Persona:** someone who would rather pay than do it — usually time-poor and able to name what the outcome is worth (a founder, a small-business owner, a marketing lead). Their alternative is a freelancer or agency, not software; the persona must say why fixed scope and speed beat both.
- **Pricing models:** fixed price per deliverable ("one deck, 48 hours, $X"); monthly subscription with a capacity limit ("unlimited requests, one at a time"); tiered packages; a paid diagnostic that leads into the main package. Price on the outcome's value, not on hours — AI makes hours a bad anchor.
- **Who pays:** the business owner or budget holder, usually by card for small packages and by invoice for larger ones. Upfront payment (or a deposit) is standard; don't start work on credit.
- **Margin:** delivery hours × the member's rate + AI and tool costs per client must leave margin at the fixed price. Track hours per delivery from client one.

### Fees — last reviewed October 2026 (re-verify before quoting)

- Card processing on payment links and invoices is a percentage plus a fixed fee per charge — check the provider's current pricing.
- Freelance marketplaces charge a service fee on the member's earnings (Fiverr's seller fee was 20% at the last review; Upwork's freelancer fee varies by contract) — check the current figure before pricing a listing there.

## Design route

| Step | Mode | How it adapts |
| --- | --- | --- |
| 1 — Identity | Full | A service brand sells trust; the name, worldview, and contrarian belief carry the sales page. The name check covers the domain and marketplace profile names. |
| 2 — UX Writing | Adapted | `docs/COPY.md` covers client-facing writing instead of UI: intake form questions, the welcome and kickoff emails, status updates, delivery notes, revision requests, and the offboarding/upsell message. |
| 3 — Design System | Lite | Brand tokens for the sales page, proposals, and deliverables (reports, decks, docs) so every client touchpoint looks like one business. |
| 4 — Design Prompts | Skip | No product screens. Optional when a client portal is built. |
| 5 — Magic Moment | Adapted | The moment the client receives the first deliverable and sees it's done better or faster than they expected — named with its timing ("first draft in their inbox within 48 hours"). |
| 6 — Onboarding | Adapted | Uses `BONUS-Productized-Service-Onboarding-Best-Practice.md`: payment → welcome email → intake form → kickoff (call or async) → first deliverable. `docs/ONBOARDING.md` is the client journey; the wireframe is optional (intake form and portal only). |
| 7 — Acquisition surface | Full | `design-landing-page` — the sales page with scope, price, process, examples, and the booking or checkout button. `design-marketplace-listing` is Optional, for marketplace service listings (Upwork Project Catalog, Fiverr gigs, Contra). |

## Develop route

| Step | Mode | How it adapts |
| --- | --- | --- |
| 0 — Migrate | Skip | Not applicable. |
| 1 — PRD & Roadmap | Adapted | The PRD becomes the delivery spec (below); the roadmap builds the delivery engine — sales page, checkout, intake, AI workflows, templates, QA — in the order the first client needs them. |
| 1b — Evals | Optional | Run it on the AI steps of delivery (the first-draft generator, the categoriser) so output quality before human QA is measured, not felt. |
| 2 — Verify setup | Full / Skip | Full when the roadmap builds code (a custom sales page, intake, automations, prompt workflows): turn on version history (git) first in Develop. Skip when the whole delivery stack is no-code tools; offer version history for the SOP, prompts, and templates if the member wants drafts kept. |
| 3 — Build | Adapted | `develop-build` builds what's code (sales page, intake, automations, prompt workflows); the rest is set up in no-code tools and checked off the same roadmap. |
| 4 — Build loop | Optional | Automate the delivery steps that repeat once several clients have been through them — this loop is where the sequence to `web-app` begins. |
| 5 — Code review | Optional | Only for custom code (automations, the sales site, scripts). |
| 6 — Design changes | Optional | For the sales page and deliverable templates. |
| 7 — Conversion review | Adapted | Traffic → sales page → booking or checkout → paid → intake completed. Runs on the sales page and the booking flow. |
| 8 — Security audit | Full / Skip | Full when the service runs custom code, a client portal, or stores client data or credentials (account logins, financial records, customer lists) in systems the member built. Skip when delivery runs entirely on established SaaS tools — then the go-live checklist covers client-data handling (access, storage, deletion). |
| 9 — Go live | Adapted | Sales page, payments, and the delivery stack live (below). |

### What the PRD must cover

- **The scope:** exactly what's delivered, in what format, by when, how many revisions — and what's out of scope.
- **The delivery SOP:** each step from payment to handover, who or what does it (the member, an AI workflow, a contractor), and how long it takes.
- **Intake:** the questions and files needed before work starts, and where they land.
- **Tooling:** the AI models and prompts used per step, the automation platform or code, where client files live, how the client receives deliverables.
- **QA:** the checklist every deliverable passes before it's sent, including checks on AI output.
- **Client data:** what's collected, where it's stored, who can access it, how long it's kept.
- **Capacity:** how many clients the member can serve at once, and what happens when it's full (waitlist, price rise).

### Go live

Sales page live on the member's domain → Stripe Payment Link, Checkout, or invoice template set up in live mode → booking link (Cal.com, Calendly) connected → intake form and welcome email automated → delivery workspace and QA checklist ready → a terms-of-service or simple service agreement linked at checkout → the first real client taken through every step. `develop-golive` writes this as `docs/DEPLOY.md`; live when one real client has received the outcome end to end.

#### Review and policy — last reviewed October 2026 (re-verify before quoting)

- Freelance marketplaces review new profiles and service listings and restrict taking clients off-platform — check their current terms before using them as a funnel to the member's own checkout.
- Services that touch regulated work (bookkeeping, tax, legal, health) may need disclaimers, licences, or professional insurance depending on jurisdiction — check before taking the first client.

## Distribute notes

**Native channels:** the warm network and referrals (the strongest channel for services), direct outreach to a tight list, LinkedIn and X content showing before/after work, communities where the persona asks for recommendations, partnerships with adjacent service providers, and freelance marketplaces for the first reviews.

**First users:**

1. Message 20 people in the warm network who match the persona with the fixed offer and price — not "let me know if you need anything".
2. Deliver the first one or two at a founding-client price in exchange for a testimonial and a case study.
3. Publish one before/after example a week from real deliverables (with permission).
4. Ask every delivered client for one introduction at the handover, when satisfaction peaks.
5. Partner with one adjacent provider who serves the same client a step earlier or later.

**Activation and retention:** *activated* = a paid client completes intake and receives the first deliverable on time. *Returned* = the client buys again or renews within 60 days (for subscriptions, the second monthly charge succeeds). Also track hours per delivery — falling hours at the same quality is the signal the process is ready to become software.

## Watch-outs

- **Scope creep.** "Fixed scope" erodes one favour at a time. Write the scope and revision limit into the checkout page and the agreement.
- **Custom work in disguise.** If every client needs a different process, it's consulting, not a productized service. Narrow the offer until the SOP is the same each time.
- **Hiding the AI badly.** Clients care about the outcome, but an undisclosed AI deliverable with obvious AI errors destroys trust. QA every AI output; decide openly how AI use is described.
- **Underpricing on hours.** AI makes delivery fast; pricing on time saved for the member instead of value to the client leaves most of the margin on the table.
- **Never sequencing.** If the plan says "move to web-app after N clients", hold the member to the trigger — and don't build the app before the trigger fires.
