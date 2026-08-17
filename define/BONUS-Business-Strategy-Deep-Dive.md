# BONUS — Business Strategy Deep Dive

An **optional** worksheet for defining how your app actually makes money, filled in by `studio-define-business-strategy`. Most people don't need this in the first weeks — your `3-Pricing-Strategy.md` carries you through the launch ladder. Run the deep dive when the money questions get real: before spending on paid channels in Distribute, when revenue starts arriving, or when an investor or co-founder asks how the model works. Fill in each section below in 1-2 sentences max.

---

## 1. Revenue Model

*How does the money flow from user to you?*

> Good: one primary model matched to your cost structure and category expectations
> Bad: freemium-by-default, two models in parallel, subscription on a one-shot product

**Common models — pick one:**

| Model | When it fits | Watch out for |
| --- | --- | --- |
| Recurring subscription | Continuous-value tools (SaaS, mobile apps used daily) | Needs retention work; churn kills you |
| One-time purchase | Bounded-utility tools (Mac apps, calculators, generators) | No expansion revenue; need volume |
| Lifetime deal (LTD) | New launches needing cash + evangelists fast | Cap seats and time-box; otherwise you give away future MRR |
| Bring Your Own Key (BYOK) | AI apps with heavy API costs | Smaller addressable market — power users only |
| Productized service | Outcomes that need a human in the loop | You're capacity-constrained; productize ruthlessly |
| Take-rate / marketplace | Networks with two sides | Brutal cold-start; only viable with distribution |
| Free + affiliate / ads | Directories, content sites, free tools | Slow to monetize; need huge traffic |

**Your answer:**

---

## 2. Pricing Ladder

*What are your tiers, anchors, and price points?*

> Good: 2 or 3 tiers with the middle engineered as the default, annual discounted 20–30%, tested upward at least once
> Bad: single flat price, more than 3 tiers, "Enterprise — contact us" with no anchor, pricing chosen by gut

**Common shapes — pick one:**

| Shape | Example | Used by |
| --- | --- | --- |
| Consumer mobile | Free → $9.99/mo or $59.99/yr | Most $10–50K MRR mobile apps |
| Prosumer / B2B starter | $19 / $49 / $99 monthly | Most $20–100K MRR B2B SaaS |
| Agency / team | $99 / $299 / $700 monthly | Most $100K+ MRR B2B SaaS |
| LTD launch | $79 / $199 / $299 lifetime, capped seats | LTD launches via AppSumo / RocketHub |
| BYOK / one-time | $49–149 one-time | Mac apps, desktop AI tools |

**Your answer:**

---

## 3. Cost & Margin

*What does each paying user cost you to serve?*

> Good: per-user variable cost under 30% of revenue, hard usage caps per tier, fixed costs covered by current MRR
> Bad: unbounded AI costs, fixed costs growing faster than revenue, you can't recite your cost-per-user from memory

**Cost breakdown:**

```
Variable per-user cost  =  AI API tokens
                        +  per-user storage
                        +  payment processing (~3%)
                        +  email / auth services
```

```
Fixed monthly cost  =  hosting (Vercel / Supabase / fly.io)
                    +  tools (RevenueCat, Linear, etc.)
                    +  your time (or contractors)`
```

**Gross margin** = (revenue − variable cost) ÷ revenue. For SaaS the healthy floor is \~70%. For AI apps, anything under 50% means you're funding the user's OpenAI bill.

**Your answer:**

---

## 4. Unfair Advantage

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

## 5. North Star Metric

*What's the one number that, if it goes up, means everything else is working?*

> Good: one metric, written down, with a 90-day target — a leading indicator of revenue you know off the top of your head
> Bad: three north stars, vanity metrics (signups, downloads, followers), targets with no deadline

**Common north stars by business type:**

| Business type | Likely north star |
| --- | --- |
| Subscription SaaS | MRR |
| Mobile app | Trial-to-paid conversion rate |
| LTD / one-time | Weekly buyers |
| Consumer app w/ retention | Weekly active payers |
| Marketplace | GMV |
| Productized service | Active retainers |

**Your answer:**