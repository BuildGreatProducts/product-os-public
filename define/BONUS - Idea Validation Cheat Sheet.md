# The Idea Validation Cheat Sheet

*A bonus asset for ProductOS — 15 tactics, 8 principles, and a decision tree pulled from 400 founder interviews.*

---

## The Meta-Rule

> **Validation is a swipe of a stranger's card, a calendar booking, or a referral inside a closed community. It is never a thumbs-up from your friends, or a "that's cool!" reply.**

Every tactic in this guide exists to manufacture one of those three signals as cheaply as possible — before you write a line of code you can't unwrite.

---

## The 8 Principles

These are the mental models that show up across every winning founder in the dataset. Internalize these and most validation decisions answer themselves.

### 1. No Competitors = No Market

Healthy competition with revenue is a signal demand is real. If nobody else is making money in the space, you are either too early or the market doesn't exist. Don't be the first to educate users on the problem.

### 2. Build For Yourself First

The strongest validation is being a daily user of your own product. If you keep using it after the novelty wears off, the workflow is real. You also become the world's foremost expert on your customer — because you are the customer.

### 3. Talk to Real Users

Pipe customer support to your DMs. Run onboarding 1-on-1. The "shy developer in the cave" is the single biggest failure mode in the dataset. Founders who reply within 10 minutes win retention.

### 4. Pre-Sale Before Pre-Build

Real money or hard calendar commitments are 10x more reliable than waitlists. Free users will ghost. Paying users complain — which is exactly what you want. Put a buy button up before you finish the product.

### 5. Niche Down Until It Hurts

The most successful first apps solve one specific problem for one specific tiny audience: "combat-sport weight cutting", "Christian phone blocker", "Notion form builder", "voice-note cleaner". The narrower the niche, the higher the conversion and the more brutal the validation signal.

### 6. Validate by Distribution, Not by Idea

An idea is only as good as your access to its audience. Before you fall in love with a concept, name the specific subreddit, Discord, Facebook group, or TikTok niche where you'll get your first 100 users. If you can't name the channel, the idea won't validate regardless of how clever it is.

### 7. Speed of Iteration Beats Perfection

Fast builders fail 90% of the time but iterate through 10+ ideas a year. Slow builders fail 90% of the time but only get one shot. Speed multiplies your odds of finding the winner.

### 8. Don't Test With Your Friends

Friends, family, and your existing audience will encourage you out of love, not market truth. Validation only counts when it comes from strangers in your ICP who have no relationship with you. If your only fans are people who know your name, you haven't validated yet.

---

## The Decision Tree — Which Test Should You Run?

Start at the top. Stop at the first "yes."

**Do you already use a clunky workaround for this problem daily?**→ Skip ahead. Use **#13 Be-Your-Own-Customer** + **#5 Buy Button Test** in parallel.

**Can you name 2+ apps in this category each doing $50K+ MRR?**→ Run **#1 Sensor Tower Revenue Scan** to confirm. If yes, jump to a Tier 2 tactic.

**Is your audience a tightly-defined community under 100K people?**→ Run **#10 Niche Sub-Community Smoke Test**. Forums, Discord, hashtags only.

**Is it event-driven, social, or scheduled?**→ Run **#7 Commitment-Metric Pre-Sale**. Don't write code without N confirmations.

**Is it visually demonstrable in under a minute?**→ Run **#6 Fake-Real TikTok Validation** + **#3 Show-Don't-Tell Reddit Demo Post**.

**Is your audience hidden or hard to reach?**→ Run **#11 Closed-Ecosystem Insider Network**. One contact, then referrals.

**Is the value mostly "saves me hours of manual work"?**→ Run **#12 Concierge MVP** before building automation.

**Do you have any audience at all (even 500 followers)?**→ Run **#14 Beta-Tester Audience Drip** in parallel with whichever public test you pick.

**None of the above and you're stuck?**→ Run **#2 Reddit Pain Mining Dig** first to find the angle, then re-run this tree.

---

## The 15 Tactics

Organized by effort tier. Start at the top of the list, only escalate if the cheap signal looks promising.

---

### Tier 1 — Desk Research (1 hour or less)

#### 1. Sensor Tower Revenue Scan

**Time:** 1 hour · **Signal:** Strong · **Cost:** Free

Open the App Store. Find the top 20 apps in your category. Run each through Sensor Tower (or similar) for revenue estimates. If multiple competitors are clearing $100K+ MRR on the same core problem, the market is proven. Identify a niche slice they're underserving and build for that.

**Pass threshold:** Two or more apps doing $50K+ MRR on the same core problem.

**Best for:** Mobile app niches and SaaS categories where competitor revenue is publicly estimable.

> **Real example — Mal Baron, Prayer Lock, $20K/month**Found existing $50K+/month prayer-blocker apps via Sensor Tower, then built a better version of the proven winner.

> **Real example — Devin, Supergrow, $230K/year**Studied three top LinkedIn-content competitors with revenue, identified the weak core flow, built a 1% better version.

---

### Tier 2 — Light Lift (1 day)

#### 2. Reddit Pain Mining Dig

**Time:** 1 day · **Signal:** Medium · **Cost:** Free

Map 10-20 niche subreddits where your ICP hangs out (use map-of-reddit.com to expand from one seed). Run a `site:reddit.com "how do I"` or `site:reddit.com "I hate"` query for your target. Paste 5-20 entire threads into Claude/ChatGPT and ask it to extract repeated pain points with quotes. The vocabulary your users use becomes your landing-page copy.

**Pass threshold:** Same specific complaint expressed by 5+ unrelated users across multiple threads, with emotional language.

**Best for:** Any B2C or prosumer product where the target audience vents online.

> **Real example — Steph France, Gold Mining Framework**Used Google `site:reddit.com` search, pasted threads into Claude, generated pain-point list and a landing page in under an hour.

> **Real example — Ovnish, Save Wise, $25K/month**Lurked in credit-card and Rakuten Facebook groups for weeks before posting; copied users' exact vocabulary into product positioning.

---

#### 3. Show-Don't-Tell Reddit Demo Post

**Time:** 1 day · **Signal:** Medium · **Cost:** Free

Record a 30-second screen recording of a single feature. Post it in a relevant subreddit framed as: *"I built this for myself because X frustrated me. Free for 30 days. Looking for feedback."* Wrap in a personal story. Deep-link to the feature with a UTM, never the homepage. Repeat one new subreddit per day for 2 weeks.

**Pass threshold:** One post hits 100+ upvotes with positive comments and drives 50+ trial signups.

**Best for:** B2C or prosumer apps where the value can be shown in under a minute.

> **Real example — Roman, Goji Berry AI, $30K MRR**Reddit story posts with screenshots and proof generated 11M impressions and the first 100 customers.

> **Real example — Aayush, Elephas, $150K/year**Posted a Super Brain feature video to niche subreddits framed as a personal problem; feedback shaped the core feature.

---

#### 4. Halfday Build & Ship

**Time:** 1 day · **Signal:** Strong · **Cost:** Free

Block one day. Build the simplest possible version of a tool in a domain you already know. Slap a real price on it. Tweet it the moment it works. The signal is whether strangers organically pay or beg for access on day one.

**Pass threshold:** First unexpected paying customer within 24-48 hours of posting.

**Best for:** Builders who already have a small audience or can credibly post in 5-10 niche communities the same day.

> **Real example — Louis Pereira, Audio Pen, $15K/month**Built MVP in 12 hours during a hackathon, posted on Twitter, got Stripe notifications from beta testers before the day ended.

> **Real example — Julien Nahum, Note Forms, $37K/month**Spent 6 days on a Notion form MVP, spammed Notion communities, watched signups become a viral loop.

---

#### 5. Buy Button Test

**Time:** 1 day · **Signal:** Strong · **Cost:** Free

Skip the waitlist. Put a real $X/month Stripe checkout on your landing page from day one — even before the product fully works. Drive a tiny amount of relevant traffic (one Reddit post, one Twitter share) and measure whether anyone clicks Buy. A click is 10x stronger signal than an email signup.

**Pass threshold:** 1+ unsolicited paying customer (not from your network) within the first week.

**Best for:** Whenever you catch yourself collecting emails instead of revenue.

> **Real example — Aayush, Elephas, $150K/year**Says "put more buy buttons on the internet." Only learns what's real when card swipes happen, not from waitlists.

> **Real example — Praneeth, Canvas Mode, $80K in 6 months**Switched from freemium subscription to one-time paywall; the price change instantly proved willingness to pay.

---

### Tier 3 — Real Commitment (1 week)

#### 6. Fake-Real TikTok Validation

**Time:** 1 week · **Signal:** Strong · **Cost:** Free

Search TikTok for keywords related to your idea. Filter by "most liked of all time." Catalog the top 10-20 viral videos in a spreadsheet: hook, story, CTA. If users are already creating viral content about the problem (millions of views, thousands of comments), demand is proven. Then replicate the format with a simple demo of your concept.

**Pass threshold:** Existing UGC in the niche getting 1M+ likes; your replicated demo hitting 10K+ organic views with no paid promo.

**Best for:** Consumer mobile apps with visual or relatable demos — habit, health, faith, lifestyle.

> **Real example — Steven, PuffCount, $44K MRR (sold**)Spent 7 days scrolling `#quitvaping`, found a 3.7M-like video, copied the "vape-in-water" format and posted his own.

> **Real example — Mal Baron, Prayer Lock, $20K/month**Saw a competitor's GC-girl reaction format crushing; had girlfriend record 40 attempts until one format clicked.

---

#### 7. Commitment-Metric Pre-Sale

**Time:** 1 week · **Signal:** Strong · **Cost:** Free

Pick a non-monetary commitment that's almost as binding as payment (e.g. "10 confirmed event dates"). Cold-message your network and 200-300 strangers via Instagram hashtags or DMs, pitching a 2-3 sentence concept. Do not write a single line of code until that number is hit.

**Pass threshold:** 10+ people with real calendar dates or scheduled use commitments — not "sounds cool" replies.

**Best for:** Event-driven, social, or B2C apps where scheduled future use is a strong proxy for willingness to pay.

> **Real example — Brian Shin, Once, $20K/month in 83 days**DMed 300 people via wedding/birthday hashtags; required 10 confirmed event commitments before writing any code.

---

#### 8. Lifetime Deal Cash Probe

**Time:** 1 week · **Signal:** Strong · **Cost:** Platform fee

Partner with an LTD platform (AppSumo, RocketHub) or run your own 3-day LTD on Twitter. Offer tiered lifetime access at 4-5x what an annual plan would cost. The platform mails its existing buyer list. You get cash, brutal feedback, and a tight cohort of evangelists who'll review on Product Hunt.

**Pass threshold:** $10K+ in real card swipes in the deal window; 20-25 of those customers actively using weekly.

**Best for:** Productivity SaaS, Mac apps, or any tool where buyers prefer one-time payments. Especially good for founders without an audience.

> **Real example — Devin, Supergrow, $230K/year**Launched LTD via RocketHub with $79/$199/$299 tiers; made $65K in 3 days; kept 250 paying evangelists.

> **Real example — Aayush, Elephas, $150K/year**Sold Mac app exclusively as lifetime deal because Mac users expect one-time pricing; gradually raised price.

---

#### 9. Free-Tool SEO Wedge

**Time:** 1 week to build · **Signal:** Medium · **Cost:** Free

Build a single-purpose free utility in your category (screenshot tool, calculator, converter) with no signup gate and aggressive SEO targeting. Use it to capture top-of-funnel intent and feed users into the paid core product. Each free tool becomes a permanent traffic asset.

**Pass threshold:** One free tool ranking top 3 for its keyword within 3 months, converting 15-20% of visitors to signup.

**Best for:** Established SaaS with engineering bandwidth and a category full of adjacent how-to searches.

> **Real example — Joseph, Super Demo, $250K/month**Built dozens of free adjacent tools (screenshots, SOPs) with ungated access; free tools now drive 20% of all traffic.

> **Real example — Aayush, Elephas, $150K/year**Accidentally ranked #1 for "create OpenAI API keys" with a help article, then doubled down on long-tail SEO listicles.

---

#### 10. Niche Sub-Community Smoke Test

**Time:** 1 week · **Signal:** Medium · **Cost:** Free

Target a tiny vertical community (a sport, a hobby, a specific software's user base). Build a feature that solves one specific pain point others ignore. Get your first 100 customers by posting in their forum, Discord, or Facebook group. If the niche is hot enough, no marketing budget is needed.

**Pass threshold:** 20+ paying users from a single niche community within 30 days; app store rating above 4.7.

**Best for:** When you can name a specific community of fewer than 100K people that hangs out together online.

> **Real example — Ethan, Cut Coach, $20K/month**Built for combat-sport athletes cutting weight. Demand peaked during wrestling season as the community shared it.

> **Real example — Sam, Algrow, $14K/month**Tapped faceless-YouTuber Discords to find first 100 customers for his content-research SaaS.

> **Real example — Julien Nahum, Note Forms, $37K/month**Built form-builder specifically for Notion users; posted in Notion Reddits and Facebook groups for the first wave.

---

#### 11. Closed-Ecosystem Insider Network

**Time:** 1 week to a few weeks · **Signal:** Strong · **Cost:** Free

When your target audience can't be reached via the open web (prisons, regulated industries, private professional networks), find a single insider contact, build them the simplest possible MVP, and let word of mouth spread inside the closed system. Validate by measuring referral velocity, not landing-page signups.

**Pass threshold:** Each new customer brings 1+ referrals organically inside the ecosystem within their first month.

**Best for:** Hidden markets with closed ecosystems where standard digital marketing channels don't reach the customer.

> **Real example — Jordan, Parakeet Chat, $300K/year**Built MVP for one inmate contact; got 200 paying users in 30 days entirely through word of mouth inside prisons.

---

### Tier 4 — Ongoing Practice (build the habit, not the test)

#### 12. Concierge MVP (Done-For-You)

**Time:** Ongoing · **Signal:** Strong · **Cost:** Your time

Before building automation, manually deliver the service one customer at a time. Take their input via DM or form, do the work yourself (or with a script), and ship results back. You learn exactly which features matter and which workflow steps people actually pay for. Charge real money from day one.

**Pass threshold:** 5-10 paying customers willing to pay manually-delivered prices repeatedly, with clear retention.

**Best for:** Services-to-software paths, agency-adjacent ideas, anything where the workflow can be done by hand for early customers.

> **Real example — Vikash, Bulk Mockup, $12K/month**First Upwork client paid $300 for what was a hacked Photoshop script run manually. Productized only after confirming demand.

> **Real example — Joseph, Super Demo, $250K/month**Manually built free interactive demos for founders posting on Reddit/Indie Hackers, dropping the link inline as outreach.

---

#### 13. Be-Your-Own-Customer Test

**Time:** 30+ days · **Signal:** Medium · **Cost:** Free

Build the tool to solve a problem you personally have and use daily. Run it as your primary workflow for weeks. If you keep using it after the novelty wears off and you'd be sad if it broke, you've validated the core need. Then share your usage publicly to find others with the same itch.

**Pass threshold:** You personally use the product daily for 30+ days without it feeling like a chore, and you can name 3 specific friends with the same problem.

**Best for:** When you have hands-on experience with a problem and use a clunky workaround daily.

> **Real example — Tibo, Multiple SaaS, $700K/month combined**Insists on being the daily user of every product he ships. Says it makes him 10x more relevant to user pain.

> **Real example — Ovnish, Save Wise, $25K/month**Personally stacked credit-card points manually for years. Built the automation he wished existed for himself first.

> **Real example — Alex Finn, Creator Buddy, $300K ARR**Tracked his own tweets in spreadsheets nightly. Automated his personal workflow into a paid product.

---

#### 14. Beta-Tester Audience Drip

**Time:** Months · **Signal:** Strong · **Cost:** Free (if audience exists)

If you have even a small audience (500+ followers), open a free beta to subscribers and onboard each tester in a 1-on-1 call or DM. Use months of feedback cycles to refine before a hyped launch day. The waitlist plus visible iteration journey makes launch-day buyers feel like insiders.

**Pass threshold:** 100+ beta testers actively using; clear feature requests repeating across 10+ users; visible build-in-public engagement.

**Best for:** Founders with even a tiny following on X, LinkedIn, or YouTube who can stomach building in public.

> **Real example — Alex Finn, Creator Buddy, $300K ARR in 2 weeks**150 beta testers onboarded individually. 6-7 months of iteration. Then $100K ARR in 15 minutes on launch day.

---

#### 15. Customer-Pain Content Flywheel

**Time:** Ongoing · **Signal:** Medium · **Cost:** Free

Treat every support call, onboarding email, and YouTube comment as a content-idea source. Record loom-style answers to specific user questions and post each as an SEO-targeted YouTube video. Low-view videos (300-1000 views) compound into 5-15 customers each. Validates content angles while finding customers.

**Pass threshold:** A single problem-specific video drives 3+ paying customers within 6 months.

**Best for:** Niche prosumer or B2B tools with a teachable workflow and an existing trickle of users to mine pain from.

> **Real example — Vikash, Bulk Mockup, $12K/month**Posts narrow how-to videos solving exact customer pains. A 370-view video drove $345 MRR from 3 customers.

---

## What Counts as Validation (and What Doesn't)

| Signal | Strength | Why |
| --- | --- | --- |
| Stranger swipes a card | ★★★★★ | The only signal that survives every other test |
| Confirmed calendar booking from stranger | ★★★★★ | Hard commitment with real-world cost |
| Referral inside a closed community | ★★★★★ | Customer just put their reputation behind it |
| Repeated feature request from 10+ unrelated users | ★★★★ | They want it badly enough to articulate it |
| Organic post hits viral velocity | ★★★★ | The audience exists and is reachable |
| Lifetime deal sells out | ★★★★ | Cash up front from an audience you didn't curate |
| 100+ active beta testers daily | ★★★ | Validates usage, not pricing |
| Reddit/HN/PH upvotes | ★★ | Validates novelty, not need |
| Friends say "I'd use this!" | ★ | Validates that your friends are kind |
| Email signup on landing page | ½ | Validates curiosity at best |
| Twitter likes | 0 | Validates that the platform's algorithm liked the framing |

---

## The Most Common Validation Mistakes

**Confusing signups with revenue.** A 5,000-person waitlist with zero buy-button clicks is not a green light. Convert waitlist tactics to buy-button tactics the moment you can.

**Validating only with your audience.** Your existing followers are biased fans. Real validation has to include strangers in the ICP who don't know your name.

**Treating "no competitors" as opportunity.** It's almost always a sign nobody is paying for this problem. Find the proven money first.

**Asking instead of charging.** "Would you pay $20/mo for this?" is worthless. "Here's the buy button" is the real question.

**Building before naming the channel.** If you can't name the exact subreddit / Discord / hashtag / SEO keyword that brings your first 100 users, the idea isn't validated regardless of how clever it is.

**Spending on ads before organic works.** Ads amplify a working funnel. They don't create one. If you can't get organic conversion in the niche where users live, ads will burn cash and teach you nothing.

**Over-investing in landing-page polish.** Pre-validation polish optimizes for the wrong audience: yourself. Ship ugly, ship cheap, escalate only on signal.

---

## Final Note

Validation is not a phase you finish — it's a discipline you practice. The founders in the dataset who hit $20K+ MRR weren't smarter; they were faster to kill ideas that didn't validate and faster to escalate the ones that did. Treat every week of your build as a chance to manufacture one more piece of signal from a stranger.

The cheapest signal beats the cleverest idea. Every time.

---

*Sourced from 400+ founder interviews on the Starter Story channel. All examples paraphrased; revenue figures self-reported by founders. Compiled by telescope.design.*