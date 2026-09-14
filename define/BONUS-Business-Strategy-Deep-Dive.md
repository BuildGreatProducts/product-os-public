# BONUS — Business Strategy Deep Dive

An **optional** worksheet for the economics behind your price, filled in by `studio-define-business-strategy`. Your `3-Pricing-Strategy.md` owns the business model, the pricing model, and the price. This deep dive adds the three things that make them survivable: what each customer costs you to serve, why a clone doesn't kill you in six months, and the one number to watch. Most people don't need it in the first weeks. Run it when the money questions get real: before spending on paid channels in Distribute, when revenue starts arriving, or when an investor or co-founder asks how the model works. Keep each answer to 1-2 sentences; the cost table in section 1 is the exception.

---

## 1. Cost & Margin

*What does each paying customer cost you to serve — and does the price in your Pricing Strategy survive your heaviest customer?*

> Good: per-customer variable cost under 30% of revenue at expected use and still positive at heavy use, hard usage caps per plan, fixed costs covered by current MRR
> Bad: unbounded AI costs, fixed costs growing faster than revenue, you can't recite your cost-per-customer from memory, a "cost floor" copied from the Pricing Strategy and never revisited

**Cost breakdown:**

```
Variable per-customer cost  =  AI API tokens (including failed attempts)
                            +  per-customer storage
                            +  payment / platform fees (~3%, or 15–30% via an app store)
                            +  email / auth services
                            +  human support or review time
```

```
Fixed monthly cost  =  hosting (Vercel / Supabase / fly.io)
                    +  tools (RevenueCat, Linear, etc.)
                    +  your time (or contractors)
```

Planning figures for each line are in the delivery-cost cheat sheet in `BONUS-Pricing-Models.md` (chapter 25). **Gross margin** = (revenue − variable cost) ÷ revenue. For SaaS the healthy floor is \~70%. For AI apps, anything under 50% means you're funding the user's foundation-model bill.

**Three customers, one billing period** — the average hides the account that loses money:

| Per customer, same period | Low use | Expected use | Heavy use |
| --- | --- | --- | --- |
| Price received after discounts / refunds | | | |
| Payment / platform costs | | | |
| Hosting / AI / storage / other delivery | | | |
| Human delivery and support | | | |
| **Contribution** before acquisition and overhead | | | |

**Your answer:**

---

## 2. Unfair Advantage

*Why can't a vibe-coded clone kill you in 6 months?*

> Good: a moat that compounds with time and use — distribution density, niche expertise, audience, switching costs, or counter-positioning
> Bad: "I built it first", "our AI is smarter", "we have better UX", "our team"

**Common unfair advantages:**

| Advantage type | What it looks like in the data |
| --- | --- |
| Distribution density | You own a channel (subreddit, creator network, App Store keyword cluster) |
| Niche expertise | You're the customer — insider knowledge competitors can't fake |
| Audience / brand | Built before launch; followers don't churn |
| Switching costs | Data lock-in, integrations, workflow embeddedness |
| Cross-product portfolio | Same buyer, multiple SKUs (Barn2's 19 plugins, Kaching's 5 apps) |
| Open-source community | Contributor flywheel (Papermark, others) |
| Counter-positioning | A model incumbents can't copy without cannibalizing themselves |

**Your answer:**

---

## 3. North Star Metric

*What's the one number that, if it goes up, means everything else is working?*

> Good: one metric, written down, with a 90-day target — a leading indicator of revenue you know off the top of your head
> Bad: three north stars, vanity metrics (signups, downloads, followers), targets with no deadline

**Common north stars by business model:**

| Business model | Likely north star |
| --- | --- |
| Subscription SaaS | MRR |
| Mobile app | Trial-to-paid conversion rate |
| Lifetime deal / one-time | Weekly buyers |
| Consumer app w/ retention | Weekly active payers |
| Usage-based / credits | Paid units consumed per month |
| Marketplace | GMV |
| Software + services / productized service | Active retainers |

**Your answer:**
