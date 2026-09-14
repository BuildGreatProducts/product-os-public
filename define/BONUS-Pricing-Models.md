# BONUS - Pricing Models

Twenty-four ways to shape a price — billing units, packaging, quantity calculations, payment timing, entry routes — followed by three chapters on setting and presenting the number. Read by `studio-define-pricing` when it fills sections 3 to 5 of your Pricing Strategy (*Pricing Model*, *Price Anchors*, *Launch Price*); useful on its own whenever a plan, unit, or discount needs designing.

Choose the business model first ([BONUS - Business Models](BONUS-Business-Models.md)), then combine only the layers your buyer needs. Freemium is an entry choice. Seats are a billing unit. Annual payment is a cadence. They can all belong to one offer, and none of them is a business model.

## Keep the layers separate

| Layer | Question | Examples |
| --- | --- | --- |
| Product / app type | What does the customer use? | Mobile app, web app, desktop utility, API |
| Business model | Who pays, and for what relationship or value? | Subscription, marketplace fee, sponsorship, software plus services |
| Billing unit | What does the price multiply by? | Account, seat, document, location, accepted outcome |
| Packaging | What is included? | Feature tiers, add-ons, bundles, capacity bands |
| Entry | How does someone start? | Upfront purchase, free tier, trial, paid pilot |
| Payment and entitlement | When do they pay and what do they keep? | Monthly, annually, one-time version licence, lifetime offer |
| Price setting / presentation | How do you choose and communicate the amount? | Value, costs, alternatives, anchoring, discounts |

## Three worked combinations

All amounts are illustrative, before tax.

| Fictional app | Business model | Pricing and entry | Distribution hypothesis |
| --- | --- | --- | --- |
| Local photo cleanup utility | One-time purchase | $49 for a defined version; demo before purchase | Search tutorials and creator demonstrations show the output |
| Supplier-document workflow | Subscription plus usage | $29/month includes 500 documents; $0.05 extra; guided trial | Targeted outreach and a real workflow demonstration reach the buyer |
| Agency client-reporting tool | White-label plus software/services | $500 setup; $30/client/month; paid pilot | Agency partnerships and case studies explain implementation and value |

These are starting hypotheses. A mobile app does not automatically need subscriptions; a B2B product does not automatically need seat pricing. The customer's outcome and the cost of delivery should drive the choice.

**Scope.** Worked examples are hypothetical, exclude tax, and are not recommended market prices. App-fit guidance and experiments are recommendations to validate. Sources support specific mechanisms and examples; they do not establish the best price for your app.

## Contents

1. [Flat rate / per account](#pricing-01-flat-rate-per-account)
2. [Per seat / licensed user](#pricing-02-per-seat)
3. [Per active user](#pricing-03-active-user)
4. [Metered usage / pay as you go](#pricing-04-metered-usage)
5. [Prepaid credits / credit burndown](#pricing-05-prepaid-credits)
6. [Fixed transaction fee / percentage take rate](#pricing-06-transaction-percentage-fees)
7. [Feature-based tiers / good-better-best](#pricing-07-feature-tiers)
8. [Volume pricing](#pricing-08-volume-pricing)
9. [Graduated / marginal tier pricing](#pricing-09-graduated-pricing)
10. [Block / package / stairstep pricing](#pricing-10-block-stairstep-pricing)
11. [Add-ons / modular pricing / bundles](#pricing-11-add-ons-bundles)
12. [Hybrid / base fee plus usage or overage](#pricing-12-hybrid-base-plus-overage)
13. [Per resource / project / location / device](#pricing-13-per-resource-location)
14. [Custom quotes / commitments / minimums](#pricing-14-custom-contracts-minimums)
15. [One-time / perpetual / lifetime / paid upgrades](#pricing-15-one-time-lifetime-paid-upgrades)
16. [Monthly / annual / instalments / fixed-term access](#pricing-16-billing-cadence)
17. [CPM / CPC / CPA / fixed sponsorship](#pricing-17-advertising-sponsorship-rates)
18. [Per lead / qualified referral / affiliate commission](#pricing-18-lead-referral-pricing)
19. [Hourly / project / retainer pricing](#pricing-19-services-project-retainer)
20. [Per outcome / success fee / gainshare](#pricing-20-per-outcome-gainshare)
21. [Paid pilot / paid trial / discovery project](#pricing-21-paid-pilots)
22. [Pay what you want / voluntary support](#pricing-22-pay-what-you-want)
23. [Free entry / freemium](#pricing-23-free-entry-freemium)
24. [Free trial / reverse trial / demo](#pricing-24-free-trial-reverse-trial)

### Price setting and presentation

25. [Setting your price: value, cost, and alternatives](#strategy-01-setting-your-price)
26. [Anchoring, “popcorn pricing,” and plan presentation](#strategy-02-anchoring-popcorn-and-packaging)
27. [Discounts, retention, and guarantees](#strategy-03-discounts-retention-and-guarantees)

---

<a id="pricing-01-flat-rate-per-account"></a>

## 1. Flat rate / per account

**Layer:** Billing unit

**How it works:** Charge a fixed amount for one person, account, or workspace during an agreed period. You can offer one flat plan or several feature packages. Define whether a workspace includes multiple users.

**Best-fit apps:** Simple consumer utilities and small-team apps where account costs do not vary dramatically. Less suitable when a handful of accounts can generate enormous compute or support costs.

**Worked example:** A fictional planning app charges $25 per workspace per month for up to five collaborators. Ten paid workspaces generate $250 before costs; adding a sixth collaborator needs a clearly stated rule.

**What works and what to avoid:** Sell the outcome in one sentence. Explain included use and any cap at checkout. Monitor the heaviest accounts; averages can hide loss-making customers. If cost varies strongly, add a meaningful limit or a metered component instead of an ambiguous 'unlimited' promise.

**First experiment and metrics:** Test whether prospects can state their expected bill without asking you. Measure conversion, contribution per account, and support questions about limits.

**Further reading:** Stripe lists flat-rate pricing as a supported recurring structure. [Stripe pricing models](https://docs.stripe.com/products-prices/pricing-models).

---

<a id="pricing-02-per-seat"></a>

## 2. Per seat / licensed user

**Layer:** Billing unit

**How it works:** Charge for each person entitled to use the product, usually monthly or annually. This is licensed access, not necessarily measured activity. Define guests, viewers, admins, minimum seats, and mid-period changes.

**Best-fit apps:** Collaboration, CRM, project management, and professional software where more users generally create more value. Weak fit for automation whose value rises while the number of operators falls.

**Worked example:** A fictional CRM costs $12 per seat per month. Eight paid seats cost $96. If the owner and a read-only guest are exempt, explicitly show that they are not part of the eight.

**What works and what to avoid:** Make seat ownership and invitations clear before billing. Charging for every invited guest can discourage collaboration. Account sharing may signal poor unit fit rather than just misuse. A workspace minimum can cover account-level costs, but should be obvious.

**First experiment and metrics:** Run a sample team through the bill: full users, guests, departing staff, and new hires. Track seat expansion, seats actually used, and objections to adding colleagues.

**Further reading:** Stripe distinguishes a seat as a user licence. [Stripe pricing models](https://docs.stripe.com/products-prices/pricing-models).

---

<a id="pricing-03-active-user"></a>

## 3. Per active user

**Layer:** Billing unit

**How it works:** Bill only for people who meet a stated activity rule in the period, or credit unused licensed time. Activity-based pricing requires an operational definition: an event, time window, and treatment of inactivity.

**Best-fit apps:** Large collaboration groups with many occasional users. It can reduce fear of inviting colleagues, but adds billing variability and event-tracking complexity.

**Worked example:** A fictional app charges $10 per monthly active editor. There are 100 registered accounts, but 35 edit during the month: $350. Logging in without editing does not count in this example.

**What works and what to avoid:** Use a billable action customers recognise and show the counted users. Avoid obscure activity rules or background events that unexpectedly trigger charges. Budget predictability may still require a cap or agreed maximum.

**First experiment and metrics:** Ask an administrator to reconcile the invoice to the activity report. Measure billed-user disputes, collaboration growth, and margin after supporting inactive accounts.

**Further reading:** Slack's fair-billing policy illustrates inactivity credits and reactivation charges; its specific rules should not be assumed for other apps. [Slack Fair Billing Policy](https://slack.com/help/articles/218915077-Slacks-Fair-Billing-Policy).

---

<a id="pricing-04-metered-usage"></a>

## 4. Metered usage / pay as you go

**Layer:** Billing unit

**How it works:** Multiply measured consumption by a unit rate. Choose the customer-facing unit and specify whether failed work, retries, storage duration, or partial jobs count. Billing can occur after use; prepayment changes collection timing.

**Best-fit apps:** APIs, transcription, document processing, and infrastructure with variable workloads. A useful unit tracks customer value without exposing every internal implementation detail.

**Worked example:** A fictional transcription tool charges $0.04 per audio minute. A 250-minute workload costs $10. State whether fractional minutes are rounded and whether failed jobs are excluded.

**What works and what to avoid:** Provide live consumption, estimated bills, alerts, and a customer-controlled spending limit where feasible. Track internal cost separately from the billing unit. A successful export may require several expensive attempts.

**First experiment and metrics:** Reconcile a sample invoice with source events. Test zero use, duplicate events, retries, and a heavy workload. Measure unit contribution and how accurately customers predict their spend.

**Further reading:** Stripe's usage documentation describes several metered billing structures. [Stripe usage billing](https://docs.stripe.com/billing/usage-based).

---

<a id="pricing-05-prepaid-credits"></a>

## 5. Prepaid credits / credit burndown

**Layer:** Prepayment and billing unit

**How it works:** Customers purchase a balance and consume it later. Credits may map one-to-one to jobs or use different rates for different operations. A subscription can also issue an allowance of credits.

**Best-fit apps:** Occasional AI generation, exports, processing tasks, and consumables. Useful when buyers prefer spending control over a recurring commitment.

**Worked example:** A fictional $24 pack contains 120 credits. A standard job uses two credits, so the pack funds 60 standard jobs at $0.40 each. Premium jobs using six credits would reduce the number to 20.

**What works and what to avoid:** Show both credits and understandable job equivalents. State expiry, rollover, transferability, failed-job refunds, and top-up behaviour. Treat unused balances as a delivery commitment in planning; cash already collected can still fund future expensive work.

**First experiment and metrics:** Stress-test full redemption at the most expensive allowed mix. Track repeat purchase, unused balances, support questions, and contribution per redeemed pack.

**Further reading:** Credit burndown is one structure documented by Stripe. [Stripe usage billing](https://docs.stripe.com/billing/usage-based).

---

<a id="pricing-06-transaction-percentage-fees"></a>

## 6. Fixed transaction fee / percentage take rate

**Layer:** Billing unit

**How it works:** Charge a fixed amount per completed transaction, a percentage of its value, or both. Define the fee base: gross order value, value excluding tax, or another agreed amount. Specify who pays.

**Best-fit apps:** Marketplaces and payments-enabled software. A percentage grows with transaction size; a fixed component can help cover per-transaction work on small orders.

**Worked example:** A fictional platform charges 5% plus $0.30. A $40 eligible transaction produces $2.30 in platform fees before payment expenses and other direct costs. A refund needs an explicit fee-reversal rule.

**What works and what to avoid:** Keep the total visible before commitment. Model small and large orders separately. Sellers may leave if the fee exceeds the ongoing value of matching, trust, or operations. Platform fee revenue is not the full order value.

**First experiment and metrics:** Track effective take rate, contribution per completed order, disputes, and repeat transactions. Test fee comprehension with both sides of the marketplace.

**Further reading:** Stripe describes marketplace payment infrastructure and platform fee collection. [Stripe marketplaces](https://stripe.com/connect/marketplaces).

---

<a id="pricing-07-feature-tiers"></a>

## 7. Feature-based tiers / good-better-best

**Layer:** Packaging

**How it works:** Group capabilities into plans aimed at distinct needs. Feature tiers are different from quantity pricing bands. You can combine a feature plan with per-seat or metered billing.

**Best-fit apps:** Products with meaningful differences between individual, team, and organisational workflows. Less useful when all customers need the same outcome and the tiers exist only to create three columns.

**Worked example:** A fictional analytics app offers Solo at $19, Team at $49 with collaboration, and Business at $149 with governance. Prices are monthly examples, not recommended benchmarks.

**What works and what to avoid:** Give each plan a specific buyer and complete outcome. Put upgrade triggers near the need for the extra value. Avoid arbitrary limits that make the entry product fail its own promise. Three plans are a design option, not a universal conversion rule.

**First experiment and metrics:** Ask prospects to select a plan and explain why. Watch confusion, plan switching, paid feature adoption, and contribution by tier—not just how many select the highlighted option.

**Further reading:** GitLab's named packages illustrate feature segmentation alongside other pricing dimensions. [GitLab pricing](https://about.gitlab.com/pricing/).

---

<a id="pricing-08-volume-pricing"></a>

## 8. Volume pricing

**Layer:** Quantity calculation

**How it works:** Determine the price band from total quantity, then apply that band's unit rate to every unit. It offers bulk rates but can create a downward jump in total price at a boundary.

**Best-fit apps:** Large orders or usage commitments where a lower all-units rate is commercially justified and customers can understand the threshold.

**Worked example:** Illustrative rates: 1–100 units at $1 each; 101–200 at $0.80 each. For 150 units, the bill is 150 × $0.80 = $120. For 101 units it is $80.80, which is less than $100 for 100 units.

**What works and what to avoid:** Check every boundary before launch. A lower total for higher use may be intentional, but it can encourage odd buying behaviour. Ensure the new rate still covers all delivered units and clearly distinguish this from graduated pricing.

**First experiment and metrics:** Calculate bills immediately below, at, and above every threshold. Test whether customers predict the result correctly and whether discounts improve total contribution.

**Further reading:** Stripe documents the all-units calculation and potential decreases in total cost. [Stripe tiered pricing](https://docs.stripe.com/subscriptions/pricing-models/tiered-pricing).

---

<a id="pricing-09-graduated-pricing"></a>

## 9. Graduated / marginal tier pricing

**Layer:** Quantity calculation

**How it works:** Charge each band of units at its own rate, then add the bands. Only the units above a threshold receive the next rate. This avoids the all-units repricing of volume pricing.

**Best-fit apps:** Usage-heavy tools where you want quantity discounts while maintaining a smoother total bill as consumption rises.

**Worked example:** Using the same fictional bands as the volume section: the first 100 units cost $1 each; the next 50 cost $0.80 each. A 150-unit bill is $100 + $40 = $140. Volume pricing would have charged $120.

**What works and what to avoid:** Label the bands with examples rather than only 'tiered pricing'. Customers often assume the lowest displayed rate applies to all use. Include fixed charges separately and verify rounding rules.

**First experiment and metrics:** Ask a customer to calculate a two-band bill. Review whether heavy-user contribution remains healthy and whether estimates match invoices.

**Further reading:** Stripe describes summing the cost of units within each band. [Stripe graduated pricing](https://docs.stripe.com/subscriptions/pricing-models/tiered-pricing#graduated-pricing).

---

<a id="pricing-10-block-stairstep-pricing"></a>

## 10. Block / package / stairstep pricing

**Layer:** Quantity calculation

**How it works:** Sell capacity in discrete blocks, or charge a flat amount for a quantity range. A block can be an allowance consumed over time; a capacity band can instead measure how much the customer may hold at once.

**Best-fit apps:** Contact databases, monitoring targets, batch-processing packs, and products whose customers prefer predictable bands to fine-grained metering.

**Worked example:** A fictional monitor costs $20/month for each block of 10 monitored sites. Eleven sites require two blocks, costing $40. A separate stairstep design might charge $20 for 1–10 sites and $35 for 11–25.

**What works and what to avoid:** Explain whether crossing a boundary upgrades automatically, blocks new use, or asks for approval. Large jumps can feel punitive for one extra item. Offer a sensible top-up if it matches your economics.

**First experiment and metrics:** Test quantities 0, 1, 10, 11, and the largest allowed range. Measure upgrade friction and unused purchased capacity.

**Further reading:** Stripe supports tier flat amounts; the examples here are original packaging designs rather than copies of its rate table. [Stripe tiered pricing](https://docs.stripe.com/subscriptions/pricing-models/tiered-pricing).

---

<a id="pricing-11-add-ons-bundles"></a>

## 11. Add-ons / modular pricing / bundles

**Layer:** Packaging

**How it works:** An add-on is an optional separate capability; a bundle packages several items together. Either can be purchased once or recurrently. Specify whether the base product is required.

**Best-fit apps:** Creative packs, integrations, specialist workflows, education modules, and audiences with different combinations of needs.

**Worked example:** A fictional base app costs $20/month; reporting adds $10 and scheduling adds $8. A $32 bundle saves $6 against the $38 combined standalone prices. Keep the comparison based on real available offers.

**What works and what to avoid:** Create an offer for each module and a coherent reason for the bundle. Avoid charging extra for a step essential to the base promise. Selling a bundle cheaply can reduce contribution if many buyers would have paid separately.

**First experiment and metrics:** Measure attachment rate, incremental contribution, adoption, and refunds. Test one relevant in-product recommendation before building a large catalogue.

**Further reading:** Apple's overview distinguishes optional additional purchases and warns against undermining the base experience. [Apple business models](https://developer.apple.com/app-store/business-models/).

---

<a id="pricing-12-hybrid-base-plus-overage"></a>

## 12. Hybrid / base fee plus usage or overage

**Layer:** Combined pricing

**How it works:** Combine a recurring access charge with a variable component. The base may include an allowance; usage above it is charged separately. Another hybrid combines seats with outcomes.

**Best-fit apps:** AI apps and automation products with account-level value but materially variable running costs. It can balance a predictable starting bill with paid expansion.

**Worked example:** A fictional document app costs $29/month including 500 documents, then $0.05 per extra document. At 800 documents the bill is $29 + 300 × $0.05 = $44. Below 500 it remains $29.

**What works and what to avoid:** Show what the base funds and when extra charges start. Avoid stacking so many units that the buyer cannot estimate a bill. Set notifications and a choice of top-up, overage, or pause.

**First experiment and metrics:** Compare low, ordinary, and high-use accounts. Track contribution at each level, overage disputes, and whether customers avoid valuable use because of uncertainty.

**Further reading:** Fixed fee plus overage is included in Stripe's usage structures. [Stripe usage billing](https://docs.stripe.com/billing/usage-based).

---

<a id="pricing-13-per-resource-location"></a>

## 13. Per resource / project / location / device

**Layer:** Billing unit

**How it works:** Charge for a countable asset other than a user: locations, projects, monitored sites, devices, client accounts, or managed properties. The unit should expand as customer value expands.

**Best-fit apps:** Vertical software, monitoring, property operations, agency tools, and embedded products where seat count poorly represents value.

**Worked example:** A fictional booking tool costs $39 per location per month with unlimited staff. Three locations cost $117. State whether a temporary pop-up or archived location counts.

**What works and what to avoid:** Choose one stable unit customers already manage. Charging per project can encourage deletion and discourage history; an archived-project policy helps. Avoid charging for resources that produce no ongoing value.

**First experiment and metrics:** Ask customers whether the unit reflects their growth. Check contribution per resource and whether unusually large resources require a separate usage cap.

**Further reading:** This is an extension of unit-based pricing: Stripe separates products and prices, while the business defines the commercial unit. [Stripe pricing overview](https://docs.stripe.com/products-prices/pricing-models).

---

<a id="pricing-14-custom-contracts-minimums"></a>

## 14. Custom quotes / commitments / minimums

**Layer:** Commercial terms

**How it works:** Negotiate a price and scope, often with a minimum spend, committed volume, contract period, or implementation fee. Custom quoting is not a reason to leave the billing unit undefined.

**Best-fit apps:** Enterprise, white-label, complex integrations, and large variable-volume accounts where delivery and buying requirements differ materially.

**Worked example:** A fictional contract has a $6,000 annual platform minimum including 100,000 events. Additional events cost $0.03 each. At 120,000 events, total charges are $6,600 before any separately agreed services.

**What works and what to avoid:** Standardise your quote structure and exceptions. State usage measurement, service boundaries, payment dates, renewal, and volume shortfalls. A long commitment may improve planning but can require concessions or intensive support.

**First experiment and metrics:** Track sales effort, delivery obligations, realised contribution, renewal, and concentration. Test whether a scoped pilot can remove uncertainty before negotiating a large contract.

**Further reading:** GitLab and Metabase show organisational packaging and sales-assisted offers. [GitLab pricing](https://about.gitlab.com/pricing/) and [Metabase Enterprise](https://www.metabase.com/product/enterprise).

---

<a id="pricing-15-one-time-lifetime-paid-upgrades"></a>

## 15. One-time / perpetual / lifetime / paid upgrades

**Layer:** Entitlement and payment timing

**How it works:** A single payment may buy a fixed deliverable, continuing use of a specified version, or ongoing access under a lifetime promise. These entitlements differ. Paid upgrades charge separately for a later version or new capability.

**Best-fit apps:** Offline tools and durable utilities suit perpetual licences. Hosted apps require careful long-term cost modelling. Paid upgrades suit meaningful new releases customers can choose to purchase.

**Worked example:** A fictional $89 licence includes version 1 and twelve months of updates. It continues working afterwards; version 2 is an optional $39 upgrade. This is not the same promise as all future versions and hosting forever.

**What works and what to avoid:** Write the entitlement in plain language before purchase. Include support, devices, updates, and hosting. Do not use a limited cost forecast to imply a lifetime obligation ends at that forecast horizon.

**First experiment and metrics:** Stress-test future support and delivery for each sales cohort. Measure net proceeds, refunds, cost to serve, and voluntary upgrade uptake.

**Further reading:** AppSumo supports several deal structures, so the marketplace name alone does not specify the entitlement. [AppSumo seller FAQ](https://sell.appsumo.com/).

---

<a id="pricing-16-billing-cadence"></a>

## 16. Monthly / annual / instalments / fixed-term access

**Layer:** Payment timing

**How it works:** Billing frequency and commitment length are separate choices. Annual prepayment collects cash upfront; an annual contract paid monthly still carries an annual commitment. Instalments split a fixed purchase and do not automatically make it a subscription.

**Best-fit apps:** Monthly options lower initial commitment; annual options fit proven ongoing value and budget planning. Fixed-term access can fit seasons, programmes, or bounded learning periods.

**Worked example:** A fictional app is $20 monthly or $192 prepaid annually. The annual effective rate is $16/month; saving versus twelve monthly payments is $48, or 20%. The amount due now is $192.

**What works and what to avoid:** Show the total due and renewal terms beside any monthly equivalent. Annual discounts reduce revenue from customers who would have paid the full monthly rate. Strong cash collection is not proof of future renewal.

**First experiment and metrics:** Compare retained contribution by billing cohort, refunds, and first annual renewal. Do not compare one-month churn directly with annual subscribers who cannot yet reach renewal.

**Further reading:** Apple distinguishes renewable and non-renewing access periods. [Apple purchase types](https://developer.apple.com/app-store/business-models/).

---

<a id="pricing-17-advertising-sponsorship-rates"></a>

## 17. CPM / CPC / CPA / fixed sponsorship

**Layer:** Advertiser billing unit

**How it works:** CPM charges per thousand impressions; CPC per click; CPA per agreed action. A fixed sponsorship sells a defined placement or period. The app user and paying advertiser are usually different people.

**Best-fit apps:** Audience apps, niche media, discovery tools, and games. Direct sponsorship can suit focused audiences even when there is insufficient volume for significant display-ad revenue.

**Worked example:** Illustrative: 80,000 billable impressions at $5 CPM = $400. Alternatively, 200 valid clicks at $2 CPC = $400. These are separate scenarios, not charges to add together unless the agreement says so.

**What works and what to avoid:** Define valid traffic, placement, reporting, attribution, and make-goods for missed delivery. A stronger rate is useless if ad load damages retention. Network gross advertiser spend may differ from your net receipts.

**First experiment and metrics:** Track net yield, invalid traffic adjustments, sponsor renewals, user retention, and selling time. Test a small relevant placement before redesigning the app around ads.

**Further reading:** Apple recognises advertising-funded apps; this section expands the billing units used to operationalise that family. [Apple business models](https://developer.apple.com/app-store/business-models/).

---

<a id="pricing-18-lead-referral-pricing"></a>

## 18. Per lead / qualified referral / affiliate commission

**Layer:** Partner billing unit

**How it works:** Charge for an accepted lead, a defined qualification event, or a tracked purchase. A percentage commission and recurring revenue share are possible; eligibility and attribution determine the actual payout.

**Best-fit apps:** Matching and comparison tools where the provider can evaluate downstream quality. The useful unit is an accepted action, not a raw email address.

**Worked example:** A fictional provider pays $25 per accepted lead. You send 60 leads, but 12 are duplicates and 8 fall outside the criteria: 40 × $25 = $1,000. Price acquisition against the acceptance rate.

**What works and what to avoid:** Agree duplicates, geography, intent, consent to contact, approval time, reversals, and reporting. If you pay affiliates for selling your own app, that is an acquisition cost rather than this revenue model.

**First experiment and metrics:** Track accepted earnings per visitor, rejected leads, payout timing, and partner retention. Pilot a few leads with manual feedback before scaling acquisition.

**Further reading:** Shopify's referral programme illustrates payment conditional on qualified conversions. [Shopify Affiliates](https://www.shopify.com/affiliates).

---

<a id="pricing-19-services-project-retainer"></a>

## 19. Hourly / project / retainer pricing

**Layer:** Service billing

**How it works:** Hourly pricing charges time; project pricing charges a scoped deliverable; retainers pay for defined ongoing access, capacity, or work. Combine them with software fees when the offer contains both human and product delivery.

**Best-fit apps:** Consulting-led apps, implementation, migration, and managed automation. Fixed projects work best with repeatable scope; uncertain exploration may need a paid discovery stage.

**Worked example:** Illustrative: 15 hours at $80 = $1,200 revenue. A $1,800 fixed package taking the same time earns more before costs, but unexpected rework can remove that difference. A retainer needs an explicit capacity boundary.

**What works and what to avoid:** Count founder hours, meetings, revisions, and support. Specify inputs the customer must supply and what constitutes completion. Unlimited retainers can sell more work than one builder can deliver.

**First experiment and metrics:** Track effective revenue per delivery hour, contribution per project, rework, and capacity. Pilot a fixed package only after learning how long delivery actually takes.

**Further reading:** Metabase offers specialist services alongside software. [Metabase professional services](https://www.metabase.com/product/professional-services).

---

<a id="pricing-20-per-outcome-gainshare"></a>

## 20. Per outcome / success fee / gainshare

**Layer:** Result-based billing

**How it works:** Charge per accepted result, a fixed success fee, or a share of an agreed gain. Unlike value-based price setting, payment depends on the measured event. Gainshare needs a baseline and attribution method.

**Best-fit apps:** Repeatable workflows with verifiable success and a supplier able to control enough of delivery. Poor fit when external factors overwhelm the app's contribution.

**Worked example:** Illustrative: $4 for each of 75 accepted resolutions = $300. A different agreement paying 10% of verified $5,000 incremental savings yields $500. Never treat all observed savings as incremental without a defensible baseline.

**What works and what to avoid:** Define qualifying results, measurement window, reversals, disputes, and customer responsibilities. Include failed attempts in cost. Consider a base fee when substantial delivery work is unavoidable regardless of outcomes.

**First experiment and metrics:** Score the same sample independently with the customer. Track agreement, disputes, accepted-result cost, and value after payment.

**Further reading:** Intercom's detailed outcome definitions show why a billing result needs operational rules. [Fin outcomes](https://www.intercom.com/help/en/articles/8205718-fin-ai-agent-outcomes).

---

<a id="pricing-21-paid-pilots"></a>

## 21. Paid pilot / paid trial / discovery project

**Layer:** Entry strategy

**How it works:** Sell a limited evaluation with a defined problem, scope, duration, and success criteria. A pilot establishes whether a larger deployment is justified. The pilot fee may or may not be credited against the next contract.

**Best-fit apps:** B2B products requiring setup, migration, custom data, or stakeholder buy-in. Less suitable for a simple low-price utility that should demonstrate itself immediately.

**Worked example:** A fictional $500 two-week pilot covers one workflow and one team. Success means an agreed result on a test set, followed by a scheduled go/no-go decision. Further implementation is a separate offer.

**What works and what to avoid:** Name the decision-maker before starting. Avoid open-ended custom work presented as a trial. Specify access and data arrangements after the pilot, and make any fee credit explicit.

**First experiment and metrics:** Track completion, achieved criteria, delivery cost, and conversion into a sustainable contract. A paid pilot validates some willingness to pay, not necessarily demand for a repeatable software product.

**Further reading:** Enterprise implementation needs are illustrated by [Metabase Enterprise](https://www.metabase.com/product/enterprise). The pilot structure above is a proposed experiment, not a claim about Metabase's process.

---

<a id="pricing-22-pay-what-you-want"></a>

## 22. Pay what you want / voluntary support

**Layer:** Price discretion

**How it works:** Let the buyer choose a payment, optionally above a stated minimum. Pure voluntary support does not require payment for access. Suggested amounts can make the choice easier without becoming mandatory prices.

**Best-fit apps:** Community projects, public-interest tools, creator resources, and experiments with an engaged audience. Uncertain fit for compute-heavy products where each free user creates a material cost.

**Worked example:** A fictional download has 200 users; 20 contribute an average $8, yielding $160 before costs. A $5 minimum would be a paid offer with optional extra support, changing the entry experience.

**What works and what to avoid:** Explain what funding supports and keep benefits manageable. A high average payment from a small number of supporters can hide concentration. Do not forecast all users as donors.

**First experiment and metrics:** Track payer share, median and average contribution, repeat support, funding concentration, and full serving cost. Test suggested amounts with a clear funding purpose.

**Further reading:** GitHub Sponsors supports one-time and recurring voluntary payments in tiers. [GitHub Sponsors](https://docs.github.com/en/sponsors/getting-started-with-github-sponsors/about-github-sponsors).

---

<a id="pricing-23-free-entry-freemium"></a>

## 23. Free entry / freemium

**Layer:** Entry strategy

**How it works:** Freemium provides a continuing free tier and an optional paid upgrade. It describes access, not the full revenue model. A completely free companion app monetised through another business is a different arrangement.

**Best-fit apps:** Self-serve products with low free-user costs, broad distribution, and a natural upgrade need such as collaboration, capacity, or a specialist workflow.

**Worked example:** A fictional app has 1,000 free users costing $0.20 each monthly. Twenty paid users at $20 bring $400, leaving $200 before paid-user costs, acquisition, and overhead. A large free audience can therefore be expensive.

**What works and what to avoid:** Deliver real value in the free tier while preserving a meaningful paid outcome. Place the upgrade at an authentic need. Avoid requiring expensive human onboarding for unlimited free accounts.

**First experiment and metrics:** Track free-user cost, activation, retained paid conversion, and contribution across the whole cohort. Test a capped free path against a demo or limited trial.

**Further reading:** Apple describes freemium access with optional purchases. This doc treats it as an entry layer so it can be combined with different revenue models. [Apple business models](https://developer.apple.com/app-store/business-models/).

---

<a id="pricing-24-free-trial-reverse-trial"></a>

## 24. Free trial / reverse trial / demo

**Layer:** Entry strategy

**How it works:** A free trial grants temporary access. A reverse trial starts with premium access and later falls back to a free tier. A demo or sandbox shows value without full product access. Card-required and no-card trials create different friction and billing expectations.

**Best-fit apps:** Products whose useful result can be experienced within a bounded evaluation. Longer setup may call for a guided or paid pilot instead.

**Worked example:** A fictional tool gives premium access for 14 days, then falls back to a free allowance unless the user upgrades. A separate card-required design could auto-convert, but must communicate the charge and cancellation route.

**What works and what to avoid:** Match duration to time-to-value rather than copying a competitor. Build onboarding around one meaningful success. State what happens to features, data, and payment when the trial ends. Trial signups alone do not validate pricing.

**First experiment and metrics:** Track activation before expiry, retained paid conversion, delivery cost, and refunds. Compare entry routes on contribution and customer quality, not just signup rate.

**Further reading:** Stripe documents trial behaviour, including payment collection and trial-end handling. [Stripe subscription trials](https://docs.stripe.com/billing/subscriptions/trials).

---

<a id="strategy-01-setting-your-price"></a>

## 25. Setting your price: value, cost, and alternatives

A common shortcut is to reverse-engineer price from the outcome. Start there if you like, but treat “a $1,000 outcome can justify $100” as a hypothesis. There is no universal rule that customers will pay 10% of estimated value. They consider credibility, urgency, alternatives, effort, risk, and available budget.

### Three ways to inform a price

| Approach | Question | Useful for | Limitation |
| --- | --- | --- | --- |
| Value-based | What is this result worth to this buyer? | Finding a defensible price range and segment | Claimed value is not automatically realised or payable |
| Cost-informed / cost-plus | What must we charge to deliver sustainably? | Identifying an economic floor and costly segments | Customers do not owe you your desired margin |
| Competitor / alternative-informed | What does the buyer pay or do today? | Understanding expectations and switching choices | A competitor may have different costs, customers, or economics |

These are price-setting approaches. They do not determine whether you charge per seat, monthly, or per outcome.

### Build a value estimate the buyer can recognise

Start with your Product Offer: customer, pain, outcome, mechanism, proof, and guarantee. Identify who uses the app and who controls the budget. Then estimate one of these:

- Time released: hours saved × a relevant labour value, adjusted for whether that time can actually be redeployed.
- Additional contribution: extra sales × contribution per sale, rather than treating all extra revenue as profit.
- Avoided cost: a specific expense the buyer can actually remove.
- Reduced risk: a credible change in expected loss, with uncertainty stated.
- Personal value: convenience, enjoyment, progress, or confidence; ask about tradeoffs rather than forcing a fictional financial return.

Illustrative: a workflow saves five hours a month valued at $30/hour. That suggests $150 of potential monthly time value. If only half the time can be put to useful work, the practical value might be closer to $75. A $25 price is worth testing; the calculation does not prove customers will buy.

### Check delivery economics

For a planning model, calculate:

**Contribution = net sales after discounts/refunds − direct delivery costs − payment/channel costs.**

Include hosting, AI inference, failed attempts, storage, customer support, and human review where relevant. Keep acquisition and fixed overhead visible separately. A positive contribution is necessary but does not mean the business is profitable.

Illustrative: $25 price less $7 direct service costs and $1.50 transaction costs leaves $16.50 before acquisition and overhead. At $49.50 acquisition cost, payback requires three such paid months if costs and payments stay constant. Cancellations can prevent recovery.

For subscriptions, prefer observed cohort contribution over a confident lifetime-value estimate from a few weeks of data. For lifetime offers, test multiple years and heavy usage.

### Delivery-cost cheat sheet

Use these to build a cost floor before you have measured anything. Every figure is an order of magnitude to plan with, marked `[working assumption]` in your Pricing Strategy until real invoices replace it. **Verify each at time of use** — platform fees and model prices change.

| Cost | Planning figure | Applies to | Source to re-check |
| --- | --- | --- | --- |
| Card processing | ~3% + a fixed few cents per transaction | Every direct sale | [Stripe pricing](https://stripe.com/pricing) |
| App-store commission | 15–30% of the sale | iOS / Android in-app purchases and subscriptions | [Apple](https://developer.apple.com/app-store/small-business-program/), [Google Play](https://support.google.com/googleplay/android-developer/answer/112622) |
| Creator marketplace fee | ~10% all-in | One-time sales through Gumroad, Lemon Squeezy, and similar | [Gumroad pricing](https://gumroad.com/pricing) |
| Deal-site revenue share | Often ~70/30 in the marketplace's favour at the entry tier | Lifetime-deal launches (AppSumo and similar) | [AppSumo seller FAQ](https://sell.appsumo.com/) |
| AI inference, small model | fractions of a cent per typical job | Classification, extraction, short generation | Your model provider's price list |
| AI inference, frontier model | cents to tens of cents per typical job; more for long documents, images, or agents | Drafting, analysis, multi-step agents | Your model provider's price list |
| Storage | a few cents per GB-month | Uploads, generated media, history | Your cloud provider's price list |
| Transactional email / auth | fractions of a cent per message; often free at low volume | Every account | Provider price list |
| Human review or support | your hourly planning rate × minutes per job or account | Services, outcome billing, high-touch onboarding | Your own calendar |

Two rules when you use it. Cost the **heavy** customer, not the average — the average hides the account that loses money. And count failed attempts: a successful export that takes three expensive tries costs three tries.

### Research willingness to pay

Ask what customers do today, what it costs, what triggers urgency, and what evidence they need. Then present a concrete offer at a concrete price. “Would you use this?” gives weaker evidence than a purchase, deposit, or paid pilot.

With low traffic, compare a small number of similar qualified sales conversations and document the reasons. Treat results as directional. With enough suitable traffic, a controlled price experiment can compare retained contribution. Changing price, packaging, audience, and onboarding together makes the result hard to interpret.

### Segment before you average

Picture the same app for three buyers. A personal hobbyist, a freelancer, and an operations team may value identical features differently because the outcome has different stakes. Pick a segment before averaging their willingness to pay.

For billing mechanics, see [Stripe's pricing model overview](https://docs.stripe.com/products-prices/pricing-models). The valuation process and numbers above are original planning guidance, not a pricing formula endorsed by Stripe.

---

<a id="strategy-02-anchoring-popcorn-and-packaging"></a>

## 26. Anchoring, “popcorn pricing,” and plan presentation

These are presentation tactics, not standalone app business models. They can affect how buyers compare offers, but they cannot establish product-market fit or make an unsuitable plan valuable.

### Anchoring

An initial number or comparison can influence later judgements. The classic research on judgement under uncertainty describes anchoring and adjustment; it is not evidence that displaying a high SaaS price guarantees higher conversion. [Tversky and Kahneman, 1974](https://doi.org/10.1126/science.185.4157.1124).

For an app, a credible comparison might be the customer's existing process cost, a genuinely available higher-capability plan, or a clearly explained annual total. Use a comparison that helps the buyer evaluate the same outcome.

Illustrative: “Your current process requires six staff-hours a month” can be useful if verified with that customer. An invented $999 “normal price” that nobody pays is not useful evidence of value.

### “Popcorn pricing”

Use this as an accessible teaching analogy: small, medium, and large choices can make the extra value of a higher option seem attractive. It can illustrate incremental upselling, anchoring, or a decoy depending on the exact choices.

A medium popcorn at $6.50 and large at $7 may encourage an upgrade. But if the large costs more, it does not strictly dominate the medium on both price and quantity. Do not label every three-size menu a scientific decoy effect.

A clearer hypothetical decoy example:

| Plan | Monthly price | Included exports |
| --- | --- | --- |
| Starter | $10 | 20 |
| Comparison option | $20 | 40 |
| Pro | $20 | 60 |

Pro dominates the comparison option on these two attributes: same price, more exports. The original attraction-effect research found that an asymmetrically dominated option could change choices within studied sets. It does not supply a universal conversion uplift for app pricing. [Huber, Payne, and Puto, 1982](https://doi.org/10.1086/208899).

Use the example to explain comparison effects. For a real product, prefer meaningful plans that serve distinct customers rather than manufacturing a useless choice.

### A better practical tier exercise

Design three possible packages, then remove any without a real buyer:

- Individual: accomplish the core task alone.
- Team: accomplish it together with shared workflows.
- Organisation: manage access, reporting, and governance.

One or two clear plans may be better than three. Show the full charge, included limits, and billing period. If you label a plan “most popular,” base that on actual purchase data. Otherwise use a suitability label such as “For teams.”

### Test the whole result

Measure comprehension, paid conversion, contribution, refunds, and continued use. Moving buyers into a higher tier is not a success if they immediately regret it or incur costs that exceed the extra revenue.

Put a confusing pricing page beside a clear outcome-based comparison and ask a prospect to explain who each plan serves before you discuss which one is highlighted.

---

<a id="strategy-03-discounts-retention-and-guarantees"></a>

## 27. Discounts, retention, and guarantees

Subscription advice leans heavily on rewards, discounts, progress, goals, streaks, and showing value back to users. Treat those as support for a useful product. They are not substitutes for the continuing outcome.

### Discounts need a specific job

A discount might encourage an annual commitment, support an eligible group, reward a referral, or run a bounded launch experiment. State eligibility, duration, renewal price, and whether it combines with other offers.

Illustrative: $20/month becomes $16 after a 20% discount. If direct costs remain $6, contribution falls from $14 to $10—approximately 29%. You need 40% more equally costly paying customers to recover the original contribution total: $14 ÷ $10 = 1.4. A 20% revenue discount can therefore cost more than 20% of contribution.

Stripe supports percentage and fixed-amount discounts with rules for applying them. Product strategy still needs to determine why the discount exists. [Stripe coupons and promotion codes](https://docs.stripe.com/billing/subscriptions/coupons).

### Retention should reveal delivered value

Useful approaches include:

- Progress summaries tied to the customer's goal.
- Reports of work completed, money recovered, or time saved with credible measurement.
- Reminders at the moment the task recurs.
- Pausing or downgrading when the customer's need is temporarily lower.
- Better onboarding when customers never reached the initial outcome.

Streaks and rewards should reinforce useful behaviour. A user can maintain a streak without achieving the reason they bought the app. Historical data can improve the experience, but difficult export or cancellation does not demonstrate satisfaction.

### Use a guarantee to reduce a specific risk

Connect the guarantee to the Product Offer's proof and mechanism. Define what is promised, what the customer must do, the timeframe, how a claim is evaluated, and the remedy you can actually provide.

A scoped example is an offer to refund a paid setup if the agreed import cannot be completed using supported inputs. “Guaranteed business growth” is much harder to substantiate because many conditions are outside your control.

A money-back guarantee is a remedy, not an outcome-billing model. A fixed-price purchase with a guarantee remains fixed-price unless the payment calculation itself depends on results.

### Avoid hiding the underlying problem

A cancellation discount may keep an account temporarily while reducing revenue. Compare retained contribution after the offer expires, not just immediate “saved cancellations.” Record whether customers were leaving because of price, low use, missing capability, or completed need.

For a first experiment, choose one segment and one change. Example: send an accurate monthly value summary to active users who do not recognise the benefit. Decide in advance which repeat-use and renewal measures will determine whether it helped.

