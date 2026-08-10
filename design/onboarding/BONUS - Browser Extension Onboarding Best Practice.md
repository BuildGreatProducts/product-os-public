# BONUS - Browser Extension Onboarding Best Practice

*A bonus asset for ProductOS — 12 principles, 18 tactics, and a decision tree pulled from teardowns of the highest-converting browser extensions shipping today: Grammarly (the default writing-assistant pattern), Loom (Atlassian's video extension), Honey, 1Password, Superhuman web extension, and the 2026 AI-extension wave — Perplexity Comet/Companion, Claude for Chrome (Anthropic research preview), HARPA AI, Complexity for Perplexity, and Scribe. Sources include Chrome for Developers' best practices, ExtensionBooster's 2026 ranking research, and the Chrome Web Store algorithm analysis.*

---

## The Meta-Rule

> **A browser extension is an invisible product. The user installs it, the icon disappears into a menu, and either the extension proves it works by silently completing the user's actual task — saving a password, fixing a typo, finding a coupon, summarizing a page — or it gets uninstalled by Sunday. Onboarding is the brief window between install and the first invisible win, and every screen, permission, and pin-to-toolbar prompt either accelerates or kills that window.**

Mobile sells persuasion. B2B AI sells evidence. Productized services sell reliability. Marketplaces sell liquidity. API tools sell time. Vertical SaaS sells OS replacement. Creator economy sells the audience showing up. **Browser extensions sell the invisible win.** 86% of users decide within the first few minutes whether to keep an extension. Poor onboarding causes 80% abandonment. **The first 5 minutes are the entire product evaluation — and they happen inside someone else's product (the browser), with permission dialogs you don't control, and an icon you have to fight to get pinned.**

---

## The Numbers That Set the Stakes

These are the 2026 benchmarks from Chrome for Developers' best-practices guide, ExtensionBooster's 2026 ranking research, MoldStud's Chrome Web Store analysis, and the documented patterns from Grammarly, Loom, Honey, and the AI extension wave.

| Metric | Number | Source |
| --- | --- | --- |
| % of users who decide to keep an extension within the first few minutes | **86%** | ExtensionBooster 2026 |
| Abandonment rate from poor onboarding | **80%** | ExtensionBooster 2026 |
| Retention lift from personalized onboarding | **+65%** | MoldStud research |
| Information retention lift from personalized tutorials | **+50%** | MoldStud research |
| Retention lift from responding to user reviews within 48 hours | **+50%** | Chrome Web Store best practices |
| % of users who expect a developer response within 24 hours | **85%** | Chrome Web Store data |
| Effective "rate this extension" prompt trigger | **After 5+ uses of the core feature** | Chrome Web Store best practices |
| Grammarly's minimum text-field height to activate | **38 pixels** | Grammarly support docs |
| HARPA AI free-tier command budget | **100 commands total** | HARPA pricing |
| Chrome 2026 in-progress feature flag for first-run onboarding | **`#first-run-desktop`** | Google blog |
| Loom permission requested on install | **"Read and change all your data on the websites you visit"** | Atlassian support |
| % of extensions whose Web Store rank correlates with review velocity | **Heavily weighted** (more than absolute star rating) | Chrome algorithm analysis |

The number that should change how you build: **86% of users decide within the first few minutes.** This is a tighter time budget than mobile apps (where the budget is 30+ seconds before first wow) and B2B SaaS (where it's 15 minutes). The browser extension has *minutes* — sometimes seconds — before the user either pins it to the toolbar or forgets it exists. Every onboarding screen that fires in those minutes must be load-bearing.

---

## The 12 Principles

These are the mental models that show up across every winning browser-extension teardown.

### 1. The Pin to Toolbar Is the Real Activation

A Chrome extension that's not pinned to the toolbar is, for most users, functionally invisible. It lives behind the puzzle-piece menu, opens in three clicks instead of one, and gets forgotten within a week. **The pin-to-toolbar prompt is the activation event — and 2026 best practice is to prompt for it in the first 30 seconds of install, with a screenshot showing exactly where the icon will appear.**

### 2. The Permission Dialog Is the Cliff

The Chrome permission dialog ("Read and change all your data on the websites you visit") is the single largest drop-off point in any browser extension's funnel. The user sees scary-sounding permissions, hesitates, and either declines or doesn't return. **Pre-permission screens — explaining the permission *before* Chrome shows the modal — are now standard, lifting opt-in rates dramatically.** Same pattern as iOS ATT modals: explain the value before the OS asks the question.

### 3. The First Invisible Win Beats the Onboarding Tutorial

Grammarly's tutorial is the act of typing a sentence and seeing the underline. Honey's tutorial is the moment a coupon code auto-fills at checkout. 1Password's tutorial is the autofill suggestion on a known login. **The "wow moment" must happen during actual web usage, not during a guided tour.** Extensions that try to teach via tour fail; extensions that demonstrate via behavior win.

### 4. Reviews Are the Web Store Algorithm

The Chrome Web Store ranking algorithm weights review *velocity* and *recency* far more than absolute star rating. An extension with a 4.2 rating receiving 100 reviews per week outranks a 4.5-rated extension receiving 5 reviews per week. **Engineer the review prompt as a primary onboarding outcome — fire it after the user has experienced ≥5 successful uses of the core feature, never sooner.**

### 5. The Icon Is the Product's Voice

Once the extension is installed, the developer's only persistent communication surface is the toolbar icon — its color (active vs. dormant), its badge (number of items, alerts), and its tooltip. Grammarly's red underline appears in the icon when it has suggestions. Loom's icon changes when recording is available. 1Password's icon counts pending fills. **Design the icon as a real-time status surface, not a static logo.**

### 6. Cross-Browser Is the New Cross-Platform

In 2026, an extension that ships only on Chrome misses Firefox, Edge, Safari, Arc, Brave, and the new AI-native browsers (Perplexity Comet, Dia). The webextension API standard means most extensions can ship across all of them with minor manifest tweaks. **Single-browser extensions concede 30–40% of the addressable market.**

### 7. The Extension Is a Side Door for the Real Product

Grammarly's extension is the acquisition surface for Grammarly's web editor, mobile app, and enterprise plan. Loom's extension is the acquisition surface for Loom's web app. 1Password's extension is the acquisition surface for the desktop password vault. **The extension is rarely the full product — it's the always-on entry point that drives the user into the deeper product where retention and monetization happen.**

### 8. Manifest V3 Is the Operating Floor

As of 2024, Manifest V3 is the only acceptable extension manifest version for the Chrome Web Store. V2 extensions are deprecated and removed. **Anything new must ship in V3, with the constraints on background workers, content security policy, and remote code execution that V3 enforces.** This is not a choice — it's the platform.

### 9. The AI-Era Extension Is an Agent Surface

The 2026 inflection: the browser extension is now the primary surface for in-browser AI agents. Perplexity's Companion summarizes the current page. Claude for Chrome (research preview) sees and interacts with the page. HARPA AI runs across GPT-5.4, Claude 4.6, DeepSeek, Gemini 3.1. The extension is no longer a "small utility" — it's the chat surface, the agent surface, the AI runtime inside someone else's browser. **Onboarding for AI extensions is dominated by trust signals (sandboxing disclosure, what-the-AI-sees indicators) and the free-tier command budget.**

### 10. Cold Install Vs. Web-Driven Install

The fastest-growing extensions in 2026 are installed not from the Chrome Web Store browse experience but from the *web product* — the user lands on grammarly.com, gets prompted to install the extension, accepts the install in-context, and is back on the web product 30 seconds later. **Web-driven install converts at 3–5x the rate of cold Web Store browsing.** The Web Store is a discovery surface, but the web product is the acquisition engine.

### 11. The Free Tier Is the Trial

There is no "trial" in a browser extension — the install IS the trial. Free-tier limits (HARPA's 100 commands, Grammarly's basic suggestions vs. premium tone analysis, Loom's 25-video cap) are the conversion mechanic. **The free tier must be useful enough to keep using and limited enough to push toward upgrade — the boundary is the entire pricing strategy.**

### 12. The Uninstall Is the Survey

Chrome doesn't tell you who uninstalled or why — but the extension can fire an uninstall URL on removal, which loads a final web page. Top extensions use this to fire a one-question exit survey or a "we're sad to see you go — try premium for 30 days" offer. **The uninstall URL is the only feedback mechanism Chrome gives you. Use it.**

---

## The Decision Tree — Which Onboarding Pattern Should You Build?

Start at the top. Stop at the first "yes."

**Is your extension a passive utility that improves something the user is already doing (Grammarly typing, Honey checkout, password autofill)?**
→ Run **#1 The Silent Activation Funnel.** Install → permission grant → demonstrate value in the user's *next natural action* (typing, checkout, login). No tutorial.

**Is your extension an active utility the user invokes (screenshot, screen recording, save-for-later)?**
→ Run **#2 The First-Action Funnel.** Install → pin to toolbar → first invocation tutorial → save / record / share within 5 minutes.

**Is your extension an AI agent that summarizes / acts on the current page (Perplexity Companion, Claude for Chrome, HARPA)?**
→ Run **#3 The Page-Aware Agent Funnel.** Install → permission grant with trust disclosure → first AI command on the user's current page → free-tier command budget visibility.

**Is your extension a productivity / power-tool replacement (Arc command bar, Raycast for browser, vimium)?**
→ Run **#4 The Keyboard-Shortcut Funnel.** Install → set up custom hotkey → first command run within 60 seconds → command-history-based discovery.

**Is your extension an enterprise / security / compliance tool (1Password business, screen DLP, etc.)?**
→ Run **#5 The Admin-Push Funnel.** IT admin deploys via MDM → user lands with extension pre-installed → SSO sign-in → first protected action.

**None of the above and you're stuck?**
→ Default to **#1 Silent Activation Funnel** if the value is passive (always-on detection), or **#2 First-Action Funnel** if the value is invoked. The trees diverge sharply on this dimension.

---

## The 18 Tactics

Organized by stage. Build top-to-bottom.

---

### Stage 1 — The Install Page (the first 30 seconds)

#### 1. The Pre-Permission Screen

**Why:** Chrome's permission dialog ("Read and change all your data on the websites you visit") sounds terrifying to a non-developer. Before triggering Chrome's modal, show a pre-permission screen explaining *why* the extension needs each permission, with plain-English language ("So we can autofill your password on the login page you visit"). Pre-permission screens lift permission opt-in rates dramatically — same pattern as iOS ATT.

**Pass threshold:** Pre-permission explainer screen fires before the Chrome permission modal on the developer-hosted install page.

#### 2. The Web-Driven Install Path

**Why:** Web-driven installs (user clicks "Install" on yourbrand.com, gets routed through Chrome Web Store, returns to the web product) convert at 3–5x the rate of cold Web Store browsing. The web product is the marketing surface; the Web Store is just the install gate. **Engineer the install flow to bounce the user back to your web product with state preserved, not to dump them into the Web Store browse experience.**

**Pass threshold:** Install flow originating on the web product redirects the user back to the same page after install completes, with installation status detected.

#### 3. The Chrome Web Store Listing

**Why:** The Chrome Web Store listing is the developer's only Web Store marketing surface. Screenshots, a demo video, the description, the privacy policy — these are the assets the Web Store algorithm and the user evaluate. **Top extensions ship at least 5 annotated screenshots, a 30-second demo video, a description that opens with the problem the extension solves (not the brand name), and a publicly verified developer.**

**Pass threshold:** Chrome Web Store listing includes ≥5 screenshots, an embedded demo video, a problem-first description, and a verified developer badge.

---

### Stage 2 — The Post-Install Tab (the first 60 seconds)

#### 4. The Pin-To-Toolbar Prompt

**Why:** Within 30 seconds of install, the developer must redirect the user to a "Welcome — pin us to your toolbar" tab. The tab includes a screenshot showing exactly where the puzzle-piece icon is, exactly where the pushpin icon is, and a 3-second video demonstrating the pin action. **An unpinned extension is a forgotten extension.**

**Pass threshold:** Post-install tab fires within 5 seconds of install completion. Includes a visual or video showing the pin-to-toolbar action.

#### 5. The Sign-In or "Skip" Flow

**Why:** Many extensions require sign-in (Grammarly, Loom, 1Password, Honey, Perplexity, Claude). The post-install tab should include SSO sign-in (Google, Microsoft, Apple, GitHub) above email/password. "Skip and try without an account" is offered as a fallback for trial-style extensions but is the lower-conversion path.

**Pass threshold:** SSO sign-in available above email/password on the post-install tab. Skip path documented and measured separately.

#### 6. The First-Use Demonstration

**Why:** The post-install tab should not be a guided tour — it should be a *demonstration*. Grammarly opens to a text area pre-filled with a sentence containing a typo, so the user sees the underline immediately. Honey opens with a fake checkout page where a coupon auto-applies. Loom opens with a "Record your first Loom" CTA. **The first wow happens in the post-install tab, not in the user's real browsing.**

**Pass threshold:** Post-install tab includes an interactive demo where the user experiences the extension's core action within 60 seconds.

---

### Stage 3 — The First Real Web Action (the next 5 minutes)

#### 7. The Silent Detection

**Why:** Grammarly activates only when the user types in a text area ≥38 pixels tall. Honey activates only on checkout pages it recognizes. 1Password's autofill triggers only on known login pages. **The extension must detect the user's natural action and react silently — never injecting UI when no relevant context is present.**

**Pass threshold:** Extension's primary activation is triggered by detected page context (text field, checkout, login, etc.), not by global insertion of UI.

#### 8. The First-Action Wow

**Why:** The first time the user encounters the extension during their normal browsing — Grammarly's underline on their first typo, Honey's coupon code on their first checkout, 1Password's autofill suggestion on their first login — that is the activation event. **Engineer the early-life experience to maximize the probability of this moment happening within 24 hours.** Pre-populate context (Grammarly opens to a demo sentence; Honey shows a fake checkout) to manufacture the moment if natural usage hasn't yet produced it.

**Pass threshold:** Median time to first organic activation event is under 24 hours. Below the threshold = activation-trigger experiment.

#### 9. The Trust Disclosure (AI Extensions)

**Why:** AI-era extensions (Perplexity Comet/Companion, Claude for Chrome, HARPA, Complexity) take an enormous leap of trust: the user is letting an AI see every page they browse. **The trust disclosure must be specific (what data leaves the browser, what doesn't, sandboxing model, retention policy), upfront (in the pre-permission screen), and re-affirmed in the post-install tab.** Without trust, AI extensions get installed and immediately uninstalled.

**Pass threshold:** AI extensions include a dedicated "what we see and what we don't" page linked from the pre-permission screen and the post-install tab.

---

### Stage 4 — The Free Tier and Upgrade (week 1)

#### 10. The Visible Free-Tier Counter

**Why:** Extensions that gate features by usage (HARPA's 100 commands, Loom's 25 videos, Grammarly's premium suggestions) must show the counter visibly: in the popup, on the toolbar badge, in the post-install tab. **Hidden counters are surprise paywalls — visible counters are progress indicators that drive engagement and upgrade.**

**Pass threshold:** Free-tier usage counter visible from the toolbar icon and the in-extension popup. Surfaced before the user hits the limit.

#### 11. The Behavioral Upgrade Prompt

**Why:** Upgrade prompts fired at specific behaviors — completing 5 successful auto-fills (1Password), recording the 25th Loom, applying the 3rd auto-coupon (Honey), running the 75th AI command (HARPA) — convert dramatically better than time-based prompts. **The user has now seen enough value to know what the upgrade is worth.** Same pattern as B2B AI SaaS PQL routing.

**Pass threshold:** Upgrade prompts fire on behavioral triggers (uses, milestones, limits) rather than on calendar days. Conversion measured per trigger.

#### 12. The Rate-This-Extension Trigger

**Why:** The Chrome Web Store algorithm weights review velocity and recency heavily — an extension getting fresh 5-star reviews ranks higher than a static 4.5-star extension. The native "rate this extension" prompt should fire only after the user has experienced ≥5 successful core uses — never on first install, never in the post-install tab. Premature review prompts produce low ratings and ranking penalties.

**Pass threshold:** Review prompt fires after ≥5 successful core uses. Average rating on prompts measured.

---

### Stage 5 — Cross-Browser and Ecosystem (week 2+)

#### 13. The Multi-Browser Manifest

**Why:** Chrome alone is ~65% of desktop browser share. The rest — Firefox, Edge, Safari, Arc, Brave, Opera, Perplexity Comet, Dia — is the other 35%. WebExtension API standards mean most extensions ship cross-browser with minor manifest tweaks. **Single-browser extensions concede a third of the market.**

**Pass threshold:** Extension ships on ≥3 browsers (Chrome + Firefox + Safari minimum). Edge and Arc are bonus territory.

#### 14. The Companion-Web-App Path

**Why:** Grammarly's web editor, Loom's web library, 1Password's web vault, Perplexity's web app — every major extension has a companion web product where retention, deeper features, and monetization compound. **The extension is a side door; the web product is the house.** Onboarding must surface the web companion early — "see all your saved Looms," "edit on the web for more controls," "access your full vault."

**Pass threshold:** Companion web product surfaced in the post-install tab and in the extension popup. Click-through rate to web app tracked.

#### 15. The Cross-Device Continuity

**Why:** Loom's recordings sync to web and mobile. 1Password's vault syncs across desktop and mobile apps. Grammarly's suggestions sync to mobile keyboard. **The extension is the entry surface; cross-device continuity is the retention loop.** The user who has the extension on Chrome, the mobile app on iPhone, and the desktop app on Mac is functionally locked in.

**Pass threshold:** Extension data syncs to at least one additional surface (web app, mobile app, or desktop app). Cross-device usage measured.

---

### Stage 6 — The Long Game (month 2+)

#### 16. The Update Cadence as Web Store Signal

**Why:** The Chrome Web Store algorithm rewards extensions that ship updates. Stale extensions (no updates in 90+ days) drop in ranking regardless of star rating. **Ship monthly minor updates with patch notes visible in the Web Store listing.** This is the same pattern as marketplaces — freshness as a ranking signal.

**Pass threshold:** Updates shipped monthly with public patch notes. Web Store ranking trend measured.

#### 17. The Review-Response Discipline

**Why:** Responding to user reviews within 48 hours produces a 50% retention lift. 85% of users expect a developer response within 24 hours. **Reviews are not just signal — they are a conversational surface.** Top extensions assign a person to respond to every Web Store review, treating it as customer support, not as reputation management.

**Pass threshold:** Public response to every Web Store review within 48 hours. Response rate measured.

#### 18. The Uninstall URL

**Why:** Chrome doesn't tell you who uninstalled or why — but you can register an uninstall URL that opens when the user removes the extension. Use it to fire a one-question exit survey ("Why did you uninstall?"), a save-attempt offer ("Try Premium free for 30 days"), or a thank-you page. **The uninstall URL is the only feedback mechanism Chrome gives you, and most extensions ignore it.**

**Pass threshold:** Uninstall URL registered with an exit survey and a save-attempt offer. Survey responses tracked.

---

## Worked Example 1 — The Grammarly Funnel Reconstructed

This is the Grammarly browser-extension flow as documented across Grammarly's support center and the demand-sage Chrome extension guide. Grammarly is the canonical reference for passive-utility browser extensions — install once, run forever, deepen value through the web editor and the premium tier.

| Step | Pattern | Why It Works |
| --- | --- | --- |
| 1. Install from grammarly.com (web-driven) | Web-driven install | 3–5x conversion vs. cold Web Store |
| 2. Pre-permission screen explains why each permission is needed | Pre-permission screen | Lifts opt-in rates |
| 3. Post-install tab with pin-to-toolbar instructions + sign-in | Pin-to-toolbar prompt | Engineer the activation event |
| 4. Sign in with Google / email | SSO above email | Faster account creation |
| 5. Demo text field with a typo, underline fires immediately | First-use demonstration | Wow inside the post-install tab |
| 6. Silent activation on text areas ≥38px in user's normal browsing | Silent detection | Reacts to natural action, not global injection |
| 7. Red underline on real typos, expansion popup with the fix | First-action wow | The product proves itself |
| 8. Premium-tier prompt after the user accepts ≥10 free suggestions | Behavioral upgrade prompt | Aha-moment-driven conversion |
| 9. Companion web editor for longer-form work | Companion web app path | Deeper retention surface |
| 10. Mobile keyboard syncs with web extension | Cross-device continuity | Lock-in loop |
| 11. Monthly Web Store updates with patch notes | Update cadence as signal | Ranking stays high |

**Result:** Grammarly is the second-most-installed extension on Chrome by an order of magnitude. The passive-utility model is the reference playbook for any extension where the user's natural action triggers value.

---

## Worked Example 2 — The Loom Funnel Reconstructed

This is the Loom browser-extension flow as documented across the Atlassian Loom support center. Loom's challenge is the "Read and change all your data" permission shock — the extension needs near-total page access to record any context the user wants. The onboarding has to defuse this shock and produce a recorded first video within 5 minutes.

| Step | Pattern | Why It Works |
| --- | --- | --- |
| 1. Install from loom.com (web-driven) | Web-driven install | 3–5x conversion |
| 2. Detailed pre-permission explainer page ("Why we need this access") | Pre-permission screen | Permission opt-in lift |
| 3. Post-install tab with pin-to-toolbar prompt + sign-in | Pin-to-toolbar | Activation event |
| 4. SSO with Google / Microsoft | SSO above email | Frictionless |
| 5. Demo Loom recording ("Record a 30-second Loom now") | First-action funnel | Active utility, first invocation |
| 6. Recorded Loom auto-uploads to Loom web | Companion web app path | Deeper surface |
| 7. Pre-formatted share links on every recording | Built-in distribution | Each share = potential install |
| 8. Free tier capped at 25 videos | Visible free-tier counter | Upgrade lever |
| 9. Upgrade prompt at video 23 | Behavioral upgrade prompt | At the boundary, not on a timer |
| 10. Mobile app for viewing + commenting | Cross-device continuity | Retention compounds |
| 11. Atlassian-integrated workspace expansion | Ecosystem expansion | Path to team / enterprise plans |

**Result:** Loom became the default async-video product through a permission-shock funnel that converts at scale via the web-driven install path and the share-loop acquisition mechanic. Acquired by Atlassian in 2023.

---

## Worked Example 3 — The 2026 AI Extension Wave (Perplexity / Claude for Chrome / HARPA)

The 2026 inflection: AI-agent extensions that summarize the current page, take actions on the web, and run multiple models inside one extension. HARPA AI offers 100 free command runs as the entry point; Claude for Chrome (research preview) sees and interacts with pages; Perplexity's Companion is the algorithmic search-replace surface inside Chrome.

| Step | Pattern | Why It Works |
| --- | --- | --- |
| 1. Install from perplexity.ai / anthropic.com / harpa.ai | Web-driven install | 3–5x vs. cold |
| 2. Pre-permission with trust disclosure (what AI sees, what it doesn't) | Trust disclosure | Critical for AI extensions |
| 3. Sandboxing model explained ("Runs in your browser, not on our servers") | Trust disclosure | Privacy positioning |
| 4. Pin-to-toolbar prompt | Pin-to-toolbar | Activation event |
| 5. SSO sign-in (Perplexity, Anthropic, Google) | SSO above email | Frictionless |
| 6. First command demo on the post-install tab ("Summarize this page") | Page-aware agent funnel | Wow on demo |
| 7. Free-tier command counter visible in popup | Visible free-tier counter | Usage as funnel |
| 8. First real-page summarize when user visits a long article | First-action wow | The product proves itself |
| 9. Multi-model selector inside the popup (GPT-5.4, Claude 4.6, Gemini 3.1) | Multi-model UX | Differentiator vs. single-model extensions |
| 10. Web companion (Perplexity.ai search, Claude.ai chat) | Companion web app | Deeper retention surface |
| 11. Upgrade prompt at ~75 commands used (out of 100) | Behavioral upgrade prompt | Before the cliff, not at it |

**Result:** AI extensions are the fastest-growing category on the Chrome Web Store in 2026. The leaders won by collapsing the install-to-first-AI-action loop to under 90 seconds while solving the AI-trust disclosure problem cleanly.

---

## Anti-Patterns — What Kills Browser Extension Onboarding

### The Permission Shock With No Explainer

Triggering Chrome's permission modal without a pre-permission screen. The user reads "Read and change all your data" and clicks Decline. **Pre-permission explainer screen, always.**

### The Unpinned Icon

Failing to prompt for pin-to-toolbar in the first 30 seconds. The icon hides behind the puzzle-piece menu, the user forgets the extension exists, uninstalls within a week. **Pin-to-toolbar prompt is the activation event.**

### The 20-Step Onboarding Tour

A multi-screen guided tour after install. Users decide in minutes — a 20-step tour wastes their entire decision window. **First-use demonstration in the post-install tab, not a guided tutorial.**

### The Global UI Injection

An extension that injects UI on every page regardless of context — sidebar, floating button, overlay. Users perceive it as malware-adjacent. **Silent detection. React only to relevant context.**

### The Premature Review Prompt

Asking for a Web Store review in the post-install tab or on day 1. The user has nothing to review. Low ratings cause Web Store ranking penalties. **Trigger reviews after ≥5 successful uses.**

### The Single-Browser Extension

Shipping only on Chrome and ignoring Firefox, Edge, Safari, Arc, and the AI-native browsers. Concedes 30–40% of the addressable market. **Multi-browser default.**

### The Hidden Free-Tier Counter

Free-tier limits that the user discovers only when they hit them. Surprise paywalls produce uninstalls. **Visible counter from day 1.**

### The Manifest V2 Holdout

Still shipping a V2 manifest. Chrome will remove the extension. **V3 only.**

### The Stale Extension

No updates in 6+ months. Web Store algorithm drops the ranking; users assume the extension is abandoned. **Monthly updates with public patch notes.**

### The Ignored Reviews

Web Store reviews left unanswered. Users see a 4.1-star extension with 150 unanswered complaints and infer the developer doesn't care. **Respond to every review within 48 hours.**

### The Uninstall Black Box

No uninstall URL registered, no exit survey, no save-attempt. Every uninstall is lost feedback. **Register the uninstall URL.**

### The AI Extension Without Trust Disclosure

An AI-agent extension that requests page-content access without explaining what data leaves the browser and what doesn't. Users install once, uninstall in 24 hours when they realize they don't understand the data model. **Explicit trust disclosure for any AI extension.**

---

## Calibration — What Good Looks Like

If your browser-extension onboarding is performing well, these are the marks to hit.

| Metric | Floor | Good | Best-in-class |
| --- | --- | --- | --- |
| Install-page → Web Store install | 8% | 18% | 35%+ |
| Install → permission granted | 60% | 80% | 95%+ |
| Install → pinned to toolbar | 25% | 50% | 75%+ |
| Install → first successful core use | 30% | 60% | 85%+ |
| Time to first successful core use | 24 hrs | 1 hr | <5 min |
| Day-7 retention (extension still installed and active) | 35% | 55% | 75%+ |
| Day-30 retention | 18% | 35% | 55%+ |
| Free → paid conversion (AI / utility extensions) | 2% | 6% | 15%+ |
| Chrome Web Store rating | 4.0 | 4.4 | 4.7+ |
| Review response rate (within 48 hrs) | 30% | 70% | 95%+ |
| Cross-browser installs as % of total | 0% | 15% | 35%+ |

If you are below the floor on pinned-to-toolbar or day-7 retention, the fix is almost never the feature set — it is the post-install tab, the pin-to-toolbar prompt, or the first-use demonstration. Re-read principles #1, #3, and #5.

---

## The Browser-Extension Operating Model

Four functions running continuously:

**1. Web Store algorithm management.** Update cadence, review velocity, screenshots, description, and category-keyword optimization are all monitored and tuned monthly. The Web Store is your primary discovery surface.

**2. Permission opt-in optimization.** Every permission grant is a conversion event. A/B test pre-permission screens, copy, and timing.

**3. Cross-browser parity.** Manifest changes are tested across Chrome, Firefox, Safari, Edge, Arc, Brave, and Perplexity Comet. Ship-everywhere-or-ship-nowhere is the 2026 default.

**4. Review-response discipline.** Every Web Store review responded to within 48 hours by a real human. Reviews are not reputation — they are customer support and algorithmic signal.

---

## Closing — The One Mental Model That Beats Everything

> **A browser extension lives or dies in the first 5 minutes after install. The user just gave you permission to see their entire browsing — and either you're invisible-and-useful (Grammarly, 1Password, Honey) or you're invasive-and-pointless. Your only job is to engineer the moment they go "oh, that's actually nice" — the underline, the autofill, the coupon, the summary — to happen during their actual browsing, not your tutorial. If it does, they pin you. If it doesn't, they uninstall by Sunday.**

Grammarly works because the underline appears the first time the user types a real sentence. Honey works because the coupon code applies at the first real checkout. 1Password works because autofill appears the first time the user lands on a known login. The AI extensions of 2026 are now solving the same problem: summarize the page the user is reading, before they ask for it, with a trust disclosure that doesn't terrify them.

The browser extension is the most constrained surface in software — six pixels of icon, one permission dialog, one shot at the post-install tab. Get those three right and the extension compounds for years. Get them wrong and you're invisible by next Sunday.

---

*Sources & teardowns this guide draws from: Chrome for Developers' Best Practices guide; ExtensionBooster's "15 Best Practices to Build a Browser Extension That Users Love (2026 Guide)"; MoldStud's Chrome extension review and onboarding research; the Grammarly browser-extension support center; the Atlassian Loom Chrome-extension permission documentation; 1Password's browser permissions guide; Honey's extension help articles; the 2026 AI extension landscape coverage from Pickaxe, DataCamp, and CIO Dive; the Perplexity Companion / Comet documentation; and the Claude for Chrome research preview announcement.*
