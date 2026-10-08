# Ship in 7 — plan: Service, digital product, or website

*The primary shape is `productized-service`, `digital-product`, or `website`. The member arrives with an idea, or partway there (an offer, a draft page, a product file, a delivery process they run by hand). Seven sessions to the shape's Live-means bar: a stranger can find it, buy or join, and receive what was promised, end to end.*

**Honest note at enrol:** there may be little or no code on this path, and that's fine — the build is a delivery system, a product file, or a set of pages. What can't be skipped is the end-to-end run on Day 7: page → checkout (or signup) → delivery, by someone who isn't the member.

## The seven sessions

| Day | Block | Skill(s) | Proof | Hours |
| --- | --- | --- | --- | --- |
| 1 | **Offer + shape** | idea: `define-offer-builder` → `define-product-shape` (if enrol didn't) → `define-customer-persona` → `define-pricing`, one sitting; partly built: `define-from-code` (or the member's own description) → `define-offer-review` → `define-pricing` | `docs/DEFINE.md` has Summary, Offer, Product Shape, Persona and Pricing filled; for a service, the fixed scope and the price line said out loud | 2.5 |
| 2 | **Identity + copy** | `design-identity-creator` → `design-ux-writing`, adapted to the shape: the page, the checkout and confirmation messages, intake and delivery emails | the Product Identity in `docs/DESIGN.md`; `docs/COPY.md` | 2 |
| 3 | **Landing page** | `design-magic-moment` (the delivery moment the buyer pays for) → `design-landing-page`, or `design-marketplace-listing` when the shape's primary surface is a marketplace (Etsy, Gumroad, a freelance catalogue); build the page with brand tokens only (a Lite design system, per the shape file) on a site builder or via the build loop | `docs/LANDING-PAGE.md` or `docs/MARKETPLACE-LISTING.md`; the page or listing running at a preview link | 3 |
| 4 | **Delivery system or product build** | service: the delivery process written as steps — intake form, the AI-assisted workflow, the deliverable template, the delivery email — and one dry-run delivery on a sample client. Digital product: version one built and packaged. Website: the pages or entries the magic moment needs. Code in play (an automation, a custom site): `develop-prd-roadmap` → `develop-build` for it | a sample deliverable, the packaged file, or the pages, saved or linked in `docs/` | 4 |
| 5 | **Checkout + gate** | a payment link or checkout (Stripe Payment Link, a merchant of record, a marketplace's own checkout, or an invoice template for a high-ticket service) wired to delivery; a real test purchase, refunded the same session. Any code of the member's own that ships (custom site, webhooks, delivery automation): `develop-security-audit` → Critical/High fixed. A website with nothing to sell yet wires its signup instead | the receipt and refund, and the delivery (or welcome) arriving; `docs/SECURITY-AUDIT.md` verdict where code ships | 2 |
| 6 | **Publish** | `develop-golive` → work `docs/DEPLOY.md`: domain, the page public, analytics, the listing live, the checkout in live mode | the public URL or listing | 2 |
| 7 | **First customer through end to end** | someone who isn't the member goes page → checkout (or signup) → intake → delivery, on the live setup; a friend's real purchase is refunded and doesn't count as a sale; fix what it finds; post the link where your customers are (stretch) | **the shape's Live-means bar passed**: the run-through, step by step, with screenshots saved to `docs/`; the post's link (stretch) | 2 |

## Notes for the composer

- **The delivery system is the product.** For a service, Day 4 is the most important session: a process the member can run again for client two without reinventing it. Keep the AI-assisted steps and the human checks named separately; the human check before delivery stays.
- **Checkout before publish, delivery behind checkout.** A page that takes money and then nothing happens is the worst first impression there is. Day 5's test purchase proves the whole chain, not just the payment.
- **No code, no audit — but say so.** A service sold through a payment link and delivered by hand ships no code of its own; the gate is Day 5's checkout-and-delivery dry run. The moment there's a custom site, webhook, or automation touching customer data, the security audit runs.
- **Marketplace-first products** (a template on a marketplace, a service on a freelance catalogue) swap Day 3's landing page for the listing; the marketplace's own checkout replaces Day 5's payment link, and Day 5 checks the payout account is set up.
- **Partly built members skip what's current** and give the freed hours to Day 4.

## Compression (a missed or short session)

Actions, in order — use the first that fits:

1. Drop Announce.
2. Merge Day 2 into Day 3: identity in a paragraph from `docs/DEFINE.md`; copy rules only for the page and the delivery email.
3. Merge Days 5–6: checkout and publish in one session on the simplest stack (a hosted page, a payment link, delivery by email).

**Constraints** (rules, not steps — no action above may break them):

- Never publish a checkout before a test purchase has reached delivery.
- Never skip the security audit when the member's own code ships.
- Never move the end-to-end run past Day 7.

## What Day 7 looks like

A stranger can find the page or listing, pay (or sign up), and receive what was promised — and someone who isn't the member has done exactly that, end to end. The announcement post is a bonus.
