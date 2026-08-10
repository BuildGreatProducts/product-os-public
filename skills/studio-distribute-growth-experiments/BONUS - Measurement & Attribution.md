# BONUS - Measurement & Attribution

*A bonus asset for ProductOS — how to actually measure whether a channel is working, so every pass threshold is a real number instead of a guess.*

Every skill in the Distribute phase runs on numbers — "50 signups from this post," cost-per-acquisition, your north star. This doc is the connective tissue underneath all of them: the minimum setup that lets you read those numbers, attribute each one to the right channel, and know what's genuinely working before you scale it. Set it up once, before you run your first experiment. It takes about 30 minutes.

> **The meta-rule:** You can only scale what you can measure, and you can only measure what you tag. An untracked link is a win you'll never be able to repeat. Tag every link, instrument the magic moment, and ask every customer how they found you.

---

## The metric that matters

Every channel feeds the same funnel. Measure as far down it as you can — the closer to revenue, the more the number counts:

**Reach → Click → Signup → Activated → Paid**

| Stage | What it means | How much it counts |
| --- | --- | --- |
| Reach | Views, impressions, opens | ½ — vanity unless it converts |
| Click | A tagged click to your product | ★★ — proves the hook works |
| Signup | An account or trial | ★★★ — a real lead |
| Activated | Reached the magic moment (`productos/distribute/2. Growth Experiments.md` → `productos/design/2. Magic Moment.md`) | ★★★★ — predicts retention |
| Paid | A card swipe | ★★★★★ — the only number that never lies |

Every experiment's **Pass =** threshold should sit as far down this funnel as you can measure. "100K views" is a ½ result; "20 paying users from one community in 30 days" is a ★★★★★ one. Reach is a leading indicator — useful, but never the finish line.

---

## The 30-minute measurement stack

The minimum a non-technical founder needs to run the whole phase. You do not need more than this until volume justifies it.

| Layer | Tool (free option) | What it tells you |
| --- | --- | --- |
| Web analytics | GA4 or Plausible | Traffic, and which channel/UTM sent it |
| Product analytics | PostHog (generous free tier) | Whether users reach the magic moment (activation) |
| Payment data | Stripe / RevenueCat dashboard | Real revenue — the signal that survives every other test |
| Self-reported attribution | A "How did you hear about us?" question at signup | What UTMs miss (word of mouth, "saw your TikTok then googled you") |
| The results log | `productos/distribute/3. Growth Experiments Tracker.md` | What worked, what didn't, what you decided |

That's it. Five layers, all free to start, enough to run every experiment in the phase.

---

## UTMs — the one habit that makes attribution possible

A UTM is a tag you add to the end of a link so your analytics can tell *which channel, which post, which experiment* drove the result. Without them, all your traffic looks the same and no result is repeatable. Tag **every** link you post, send, or run an ad with.

The five parameters:

| Parameter | What it answers | Example |
| --- | --- | --- |
| `utm_source` | Which platform? | `reddit`, `tiktok`, `youtube` |
| `utm_medium` | What kind of channel? | `community`, `short-form`, `outreach`, `ads` |
| `utm_campaign` | Which experiment? | `quitvaping-demo`, `ltd-launch` |
| `utm_content` | Which variation? | `hook-v1`, `story-post` |
| `utm_term` | (ads/search) the keyword | `quit-vaping-app` |

**Example:** deep-link to the feature, never the homepage, and tag it —

`yoursite.com/record?utm_source=reddit&utm_medium=community&utm_campaign=quitvaping-demo&utm_content=story-post-v1`

Now a signup from that link shows up in your analytics tagged to the exact post, so when one hook wins you know *which one* to do more of. Keep a simple naming convention (lowercase, hyphens, consistent source names) in a sheet so your data stays clean. A free UTM builder generates these in seconds.

---

## Attribution — keep it cheap and honest

Attribution is just answering "what made this customer show up?" Two cheap tools cover almost everything a first-time founder needs:

1. **UTMs** for everything you control (links you post and send).
2. **A "How did you hear about us?" question** at signup for everything you *don't* — word of mouth, a podcast mention, "I saw you on TikTok then searched." This self-reported answer is the single highest-leverage attribution tool at this stage, because it catches the dark-social traffic UTMs can't see.

> Good: UTMs on every link + a one-line "how did you hear" question, reconciled weekly
> Bad: a multi-touch attribution model before you have 100 customers, or no tagging at all

Don't over-engineer it. First-touch (what first brought them) is enough to decide where to spend more. Multi-touch models are a problem for a much later stage — building one now is procrastination dressed up as rigour.

---

## Measuring each channel

What to actually watch for each of the twelve channels (full channel detail in [BONUS - Distribution Channels](BONUS%20-%20Distribution%20Channels.md)):

| Channel | The number that matters | How to read it |
| --- | --- | --- |
| Short-form content | 3-sec retention → profile/link clicks → tagged signups | Native analytics + a UTM'd link in bio |
| Long-form content | Watch-time / reads → tagged signups | YouTube analytics, Search Console for ranked videos |
| Communities | Tagged signups per post | One UTM per community; upvotes are a proxy, not the metric |
| Search (SEO & GEO) | Impressions → clicks → rank; AI-answer mentions | Google Search Console; ask the AI engines your query for GEO |
| Platform ecosystems | Listing views → installs; rating & reviews | The store/marketplace's own analytics |
| Launch platforms | Launch-day tagged traffic → signups; backlinks | UTM the launch link; watch the 48-hour spike |
| Outreach | Reply rate → booking rate → close rate | Your sending tool's dashboard (Apollo, Instantly, Lemlist) |
| Influencer / creator | Installs per creator → cost-per-install | A unique code/link per creator |
| Partnerships | Tagged signups per partner | A unique UTM or code per partner |
| Email & lifecycle | Open & click rate → tagged clicks → conversions and reactivations | Your ESP's dashboard (Loops, Beehiiv, Klaviyo) + UTM'd deep links |
| Referrals & affiliates | Referred signups; viral coefficient | Referral codes/links; the affiliate platform's dashboard |
| Ads | Cost-per-acquisition (and downstream retention) | Native ad dashboards + UTM into your analytics to confirm the click actually converts and stays |

For **ads especially**, never trust the ad platform's conversion count alone — UTM the traffic into your own analytics and confirm those clicks activate and pay. Platforms over-report their own results.

---

## Tie it back to your experiments

Every **Pass =** line in `productos/distribute/2. Growth Experiments.md` needs a measurement method named *before* you run it. If you can't measure the threshold, the experiment is unfalsifiable — pick a threshold you can actually read. And every result you log in `productos/distribute/3. Growth Experiments Tracker.md` should be a measured number, because `productos/distribute/4. Scale & Automation Roadmap.md` scales straight from that tracker: feed it guesses and you'll automate a guess.

---

## Common measurement mistakes

- **The Untagged Link.** No UTM means no attribution — the result is real but unrepeatable, because you can't tell what drove it. Tag everything.
- **The Vanity Metric.** Measuring reach, likes, or followers instead of signups, activation, and revenue. Track the funnel, not the applause.
- **Attribution Obsession.** Building a multi-touch model before you have a hundred customers. A "how did you hear" question outperforms it for a fraction of the effort.
- **Measuring Everything.** Fifty dashboards nobody reads. Watch the five-stage funnel and the one north-star number; ignore the rest.
- **The Homepage Link.** Sending tagged traffic to the homepage instead of the magic moment, so a click means almost nothing. Deep-link.
- **Scaling on Guesses.** The Scale phase reads the tracker. If the tracker's numbers were never measured, the roadmap pours fuel on something you only *think* works.

---

## The minimum to start today

If you do nothing else: install **GA4 or Plausible**, save a **UTM template** you reuse for every link, add a **"How did you hear about us?"** question to signup, and watch **Stripe**. Log results in `productos/distribute/3. Growth Experiments Tracker.md`. That's enough to read every experiment in this phase honestly — escalate to product analytics and richer attribution only once your volume earns it.

---

*Compiled June 2026 by telescope.design. Tool names and free tiers change — verify current options before committing. Pair with [BONUS - Growth Experiments Library](BONUS%20-%20Growth%20Experiments%20Library.md) to plan experiments and `productos/distribute/3. Growth Experiments Tracker.md` to log what you measure.*
