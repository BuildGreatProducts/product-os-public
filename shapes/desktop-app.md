# Shape: Desktop app

*Slug: `desktop-app` · Family: Apps with a screen*

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

An application the customer installs on their Mac, Windows, or Linux computer: menu-bar utilities, AI meeting recorders, writing and code editors, local-model tools. It runs with deep access to the machine (files, microphone, screen, other apps), which is both the value and the trust hurdle. Typically built with Electron, Tauri, or native Swift/C#. It's distributed directly (a signed download from the member's site, with licence keys) and/or through a store (Mac App Store, Microsoft Store) or a subscription catalogue such as Setapp.

## Live means

A signed (and on macOS, notarized) installer downloads from the member's public site or store listing, installs on a clean machine without security warnings blocking it, and a smoke test passes as a real customer: install, grant the permissions, reach the magic moment — and the auto-updater finds a newer build when one is published.

## First sale means

A real customer (warm network counts; the member's own test purchase doesn't) buys a licence or subscription and it unlocks the app: through a checkout with licence keys (Paddle, Lemon Squeezy, Gumroad, or Stripe with a licensing service such as Keygen), through Mac App Store / Microsoft Store in-app purchase, or — for Setapp — the first usage-based payout that reflects real users.

## Define notes

- **Persona:** desktop buyers are often professionals using the tool for hours a day (the editor, the recorder) or people with one repeated annoyance (the utility). Name their operating system — a Mac-only persona is a legitimate, smaller launch.
- **Pricing models:** one-time licence with paid major upgrades (common for utilities), annual licence with a year of updates, subscription (for AI-heavy apps with running costs), or a free tier with a Pro unlock. Lifetime deals suit desktop utilities well on launch platforms.
- **Who pays:** the individual by card, or a team via volume licences. Direct sale via a merchant of record keeps margin and handles VAT; store sale trades margin for trust and one-click purchase.

### Fees — last reviewed October 2026 (re-verify before quoting)

- The Mac App Store uses the same commission structure as the iOS App Store (30% standard, 15% under the Small Business Program) and requires the $99/year Apple Developer Program — which direct macOS distribution also needs, for signing and notarization.
- The Microsoft Store has allowed non-game apps to use their own commerce with no Store fee, and has made individual developer registration low-cost or free — check the current terms.
- Setapp pays developers a share of subscription revenue based on usage, not per sale — check its current revenue-share terms.

## Design route

| Step | Mode | How it adapts |
| --- | --- | --- |
| 1 — Identity | Full | The name check includes the app's bundle name and the download domain. The icon must read at menu-bar and dock sizes. |
| 2 — UX Writing | Full | Menus, keyboard-shortcut labels, permission explanations, update notes, licence-activation errors. |
| 3 — Design System | Full | Follow platform conventions (macOS / Windows) where they matter: menus, window chrome, system fonts, light and dark. |
| 4 — Design Prompts | Full | The main window and the first-run permissions screen; for a menu-bar app, the popover. |
| 5 — Magic Moment | Full | Often the first automatic result (the first transcript, the first file processed) — it may happen while the user isn't looking. |
| 6 — Onboarding | Full | Uses `BONUS-Desktop-App-Onboarding-Best-Practice.md`: download → install → OS permission grants (accessibility, screen recording, microphone) with explanations → first result. |
| 7 — Acquisition surface | Full | `design-landing-page` is the primary surface — a download page with the price. Add `design-marketplace-listing` for each store or catalogue used (Mac App Store, Microsoft Store, Setapp). `design-app-listing` is for iOS/Android only. |

## Develop route

| Step | Mode | How it adapts |
| --- | --- | --- |
| 0 — Migrate | Skip | Prompt-to-app platforms don't produce desktop apps; Skip unless a web app is being wrapped from one. |
| 1 — PRD & Roadmap | Full | Framework, target OSes, and distribution channel (direct vs store) are decided here — store sandboxing rules shape the architecture. |
| 1b — Evals | Optional | Run it when the magic moment is an AI output (a transcript summary, a rewrite, a code suggestion). |
| 2 — Verify setup | Full | Turn on version history (git) if it isn't on yet — the build saves its work there at every phase — and check the guidelines `setup` wired. Runs first in Develop. |
| 3 — Build | Full | The roadmap must include signing, notarization, the installer, and the auto-update pipeline as tasks — not afterthoughts. |
| 4 — Build loop | Full | Each release is a versioned, signed build with release notes the updater shows. |
| 5 — Code review | Full | For changes made outside the build skills. |
| 6 — Design changes | Full | Review in light and dark mode and at the smallest supported window size. |
| 7 — Conversion review | Adapted | Landing page → download → install → permissions → activation → trial-to-paid or licence purchase. The permissions step is where most installs die. |
| 8 — Security audit | Full | Plus desktop specifics: no secret keys in the binary, licence-check bypass, update-channel integrity (signed updates over HTTPS), local file and IPC exposure. |
| 9 — Go live | Adapted | Signed builds and an update feed rather than a single deploy (below). |

### What the PRD must cover

- **Platforms and framework:** macOS / Windows / Linux at launch, minimum OS versions, Electron vs Tauri vs native, architectures (Apple silicon and Intel, x64 and ARM).
- **Distribution:** direct download, store(s), or both — and the sandbox and API restrictions each store imposes.
- **Permissions:** every OS permission, when it's requested, and the in-app explanation before the system prompt.
- **Licensing and payments:** licence key format and activation, offline grace period, device limits, trial handling, and the backend that validates them.
- **Updates:** update framework (Sparkle on macOS, the framework's own updater elsewhere), the release feed, and how a broken release is rolled back.
- **Backend and AI:** what runs locally vs on the server, and a proxy for every paid API so no key ships in the app.

### Go live

Production backend and licence service live → code-signing set up (🧑 the member: Apple Developer ID; a Windows signing certificate or Microsoft's managed signing service) → builds signed, and notarized for macOS → installers and the update feed hosted (a CDN, GitHub Releases, or the framework's update server) → download page live with checkout → store submissions if used → smoke test on a clean machine of each OS. `develop-golive` writes this as `docs/DEPLOY.md`.

#### Review and policy — last reviewed October 2026 (re-verify before quoting)

- macOS Gatekeeper blocks apps that aren't signed with a Developer ID and notarized by Apple; recent macOS versions removed the easy override, so an unsigned build is effectively unshippable.
- Windows SmartScreen warns on installers without an established signing reputation; signing reduces the warning, and reputation builds with downloads. Check Microsoft's current signing options.
- The Mac App Store requires the App Sandbox, which blocks many utility patterns (system-wide accessibility control, some screen-capture approaches) — check before choosing the store as the channel. App Review applies, as on iOS.

## Distribute notes

**Native channels:** the member's own download page plus search (people search "[task] app for Mac"), Mac and Windows communities and newsletters, launch platforms (Product Hunt, Hacker News), lifetime-deal platforms for utilities, Setapp's catalogue, the Mac App Store / Microsoft Store search, and "best Mac apps for X" roundups and YouTube setup videos.

**First users:**

1. Give 20 warm-network users a free licence in exchange for a 15-minute screen-share of their install — the permissions step will show its friction.
2. Post a 30-second screen recording of the magic moment in the communities where the persona works (design, dev, podcasting, research).
3. Pitch the five newsletters or YouTubers who publish "apps I use" roundups for this persona.
4. Run a time-boxed launch discount or lifetime deal on Product Hunt day to convert the spike into paying users.

**Activation and retention:** *activated* = an install completes the permission grants and produces the first result (the magic-moment event, sent to the member's analytics with consent). *Returned* = the app is opened, or its background job produces a result, on at least three days in week 2. Track the download → first launch → permissions-granted funnel; desktop installs leak most before first launch.

## Watch-outs

- **Signing left to launch week.** Developer ID enrollment, certificates, and notarization take time and accounts only the member can create. Do them in the first build phase.
- **Permissions without explanation.** A raw OS prompt for screen recording loses the user. Explain the why on the app's own screen first.
- **Shipping without an updater.** The first bug fix can't reach anyone who already installed. The update pipeline ships in v1.
- **The sandbox surprise.** Choosing the Mac App Store after building features the sandbox forbids. Decide the channel in the PRD.
- **Cross-platform by default.** Building Mac, Windows, and Linux at once triples testing; launch on the persona's OS first.
