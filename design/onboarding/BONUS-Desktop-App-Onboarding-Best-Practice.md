# BONUS - Desktop App Onboarding Best Practice

*A bonus asset for ProductOS — 12 principles, 18 tactics, and a decision tree pulled from teardowns of the highest-converting native desktop apps shipping today: Granola ($125M Series C at $1.5B valuation, from $250M a year earlier), Raycast (the Spotlight-replacement playbook), Superhuman, Arc, Linear Desktop, Notion Desktop, Figma Desktop, and the 2026 AI-desktop wave (Talat, Wispr Flow, native AI tools). Sources include Apple's permission documentation, Tauri vs Electron 2026 benchmarks, Granola's funding and product launches, and Raycast's onboarding documentation.*

---

## The Meta-Rule

> **A desktop app is an active commitment. The user downloaded, opened, granted permissions, and now keeps it in their dock. Every one of those steps had friction the web app didn't — and the user crossed each one because they expect the desktop app to be faster, more keyboard-driven, more native-feeling, and more powerful than the web equivalent. Onboarding is the act of proving each of those expectations is true, before the dock icon becomes one of the ten the user never clicks.**

Mobile sells persuasion. B2B AI sells evidence. Productized services sell reliability. Marketplaces sell liquidity. API tools sell time. Vertical SaaS sells OS replacement. Creator economy sells the audience showing up. Browser extensions sell the invisible win. **Desktop apps sell speed and depth.** The user did not download Raycast to do what Spotlight already does — they downloaded it to do *more*, faster. Granola's $1.5B valuation is built on transcribing every meeting in 90% accuracy without a bot joining the call — a thing no web app can do. **The desktop install is a vote of confidence; the onboarding either honors it or wastes it.**

---

## The Numbers That Set the Stakes

These are the 2026 benchmarks from Apple's developer documentation, the Tauri vs Electron 2026 benchmark suite, Granola's published metrics, Raycast's onboarding documentation, and the documented patterns from Superhuman, Arc, Linear, and Notion.

| Metric | Number | Source |
| --- | --- | --- |
| Granola valuation (Mar 2026) | **$1.5B** (from $250M a year earlier) | TechCrunch |
| Granola Series C round | **$125M** (led by Index Ventures) | TechCrunch |
| Granola onboarding permission requirement | **Microphone access only** | Granola docs |
| Granola time-from-signup to first recorded meeting | **<10 minutes** | Granola product teardown |
| Granola transcription accuracy on clear audio | **90–95%** | Bluedot review 2026 |
| Tauri vs Electron bundle size | **2–10 MB vs 80–200 MB** | Tauri benchmarks |
| Tauri vs Electron memory usage | **50 MB vs 120+ MB** | Tauri benchmarks |
| Tauri vs Electron app size reduction | **96% smaller** | Pkgpulse 2026 |
| Electron 34+ cold-start time (well-built apps) | **<500 ms** | Electron release notes |
| Raycast onboarding step that determines activation | **Replace Cmd+Space (Spotlight) with Raycast hotkey** | Raycast manual |
| macOS Sequoia (15) screen-recording permission reset cadence | **~Monthly + on reboot** | Apple support |
| macOS microphone permission grantable via MDM | **No** — user must grant at first use | Apple support |

The number that should change how you build: **Tauri produces apps that are 96% smaller and use 50% less RAM than Electron.** In 2026, this matters less than it did two years ago (Electron 34+ ships sub-500ms cold starts), but the user-perception story is real: a 200 MB download for a "meeting notes app" is increasingly unacceptable. The 2026 desktop-app decision (Electron vs Tauri vs native) is now part of the onboarding decision, because the install time, the disk footprint, and the first-launch speed are all onboarding events.

---

## The 12 Principles

These are the mental models that show up across every winning desktop-app teardown.

### 1. The Install Is the First Cliff

Web apps have no install. Desktop apps have a DMG download, a drag-to-Applications step, a Gatekeeper warning ("This app was downloaded from the internet — are you sure?"), and a first launch. Each step loses 5–15% of would-be users. **Code-signing, notarization, and a Mac App Store / Microsoft Store distribution are no longer nice-to-haves — they're the difference between a 60% install completion and a 90%.**

### 2. The Permission Wall Is the Second Cliff

macOS permissions (accessibility, microphone, screen recording, full disk access) are the highest-friction onboarding events in any desktop app. Each prompt loses users. macOS Sequoia (15) introduced *monthly* permission resets for screen recording — so users have to re-approve apps they've already approved. **Permission requests must be staged: ask only for what's needed at the moment of need, with a clear in-app explainer before macOS shows the dialog.**

### 3. The First Keyboard Shortcut Is the Activation Event

Raycast's onboarding is, literally, replacing the default Spotlight hotkey (Cmd+Space) with Raycast's hotkey. **If the user does this, they're active. If they don't, they've installed an app they will never open.** The same pattern applies in subtler ways: Superhuman's keyboard-first inbox; Linear Desktop's Cmd+K command bar; Arc's Cmd+T command palette. **The keyboard shortcut isn't a feature — it's the activation event.**

### 4. Native Speed Is the Whole Pitch

Users download a desktop app because the web app feels slow. The first launch must feel faster than the web equivalent — sub-500ms cold start (Electron 34+ benchmark), instant keyboard response, no progress spinners. Granola opens in under a second. Raycast launches with the hotkey instantly. **If the desktop app feels slower than the web app, the user uninstalls within a week.**

### 5. The Menu Bar Is the New Notification Center

Mac menu-bar apps (Granola, Raycast in some modes, Cleanshot, Bartender) live in the top-right of the screen forever. **Onboarding must teach the user that the app is in the menu bar, what the icon means, and how to invoke it.** A menu-bar app that the user can't find again after closing the main window is a dead app.

### 6. Auto-Launch on Login Is the Retention Setting

A desktop app that opens only when the user remembers to open it gets used twice and forgotten. **Auto-launch on login is the retention setting.** Granola, Raycast, Notion, Slack, Linear, Superhuman, 1Password — every winning desktop app prompts to auto-launch on login in the onboarding flow. The prompt is part of the activation funnel, not a setting buried in preferences.

### 7. Cross-Platform Or Mac-First (Not Windows-First)

The 2026 prosumer / power-user desktop market is overwhelmingly Mac. Granola launched Mac-only and only added Windows later. Raycast was Mac-only for years. Arc launched Mac-only. **For prosumer / power-user products, Mac-first is the default. Windows is the secondary or expansion launch, not the lead.** This inverts the historical enterprise software pattern.

### 8. The Electron-vs-Tauri-vs-Native Decision Is an Onboarding Decision

A 2 MB Tauri app feels lighter than a 200 MB Electron app. A native Swift app feels more "Mac" than either. But the cost: three platforms × the engineering of three codebases. **In 2026 the practical winners are: Tauri for size-conscious products with small teams (Granola Mac-only), Electron for breadth-first products (Notion, Linear, Figma), native for highest-touch consumer (Arc, Superhuman desktop).**

### 9. The Update Cadence Is Part of the Product

Desktop apps that don't auto-update bit-rot. Users on stale versions hit bugs the team fixed three months ago. Sparkle (Mac), Squirrel (Electron), and Tauri's updater are the standard solutions. **Auto-update must be on by default, silent, and incremental.** The 2026 desktop app ships at least once a month.

### 10. The Web Companion Is the Cross-Surface Anchor

Granola desktop syncs to Granola web. Linear desktop is essentially a wrapper around Linear web. Notion desktop opens to the same workspace as Notion web. **The desktop app is one surface in a multi-surface product — the user expects state to sync across desktop, web, and mobile.** If the desktop app is the only surface, the user feels stuck on Mac.

### 11. The Companion Mobile App Is the Lock-In

Power-user products without a mobile app feel incomplete. The desktop user expects to glance at the same data on their phone — a Granola meeting summary, a Linear issue, a Superhuman email, a Raycast clipboard. **The mobile companion is the second activation funnel, and the cross-device user is functionally locked in.**

### 12. The AI-Desktop Wave Is Microphone-First

The 2026 inflection in desktop apps: AI-powered productivity tools that listen to meetings (Granola), watch the screen (Wispr Flow for dictation, Talat for local AI), and take action. **The defining permission for the AI-desktop wave is microphone access — and the differentiating product decision is whether transcription happens locally (Talat's privacy moat) or in the cloud (Granola's speed moat).** Onboarding must surface this decision clearly.

---

## The Decision Tree — Which Onboarding Pattern Should You Build?

Start at the top. Stop at the first "yes."

**Is your desktop app a power-user productivity launcher / command bar / shortcut tool (Raycast, Alfred, Hyperkey)?**
→ Run **#1 The Replace-Spotlight Funnel.** Install → replace Cmd+Space → first command run within 60 seconds → keyboard-shortcut customization.

**Is your desktop app an AI meeting-notes / dictation / agent product (Granola, Wispr Flow, Talat)?**
→ Run **#2 The Microphone-First Funnel.** Install → microphone permission (with trust disclosure) → first meeting recorded within 10 minutes → summary generated.

**Is your desktop app an inbox / messaging / communication client (Superhuman, Linear Desktop, Slack Desktop)?**
→ Run **#3 The Keyboard-First Funnel.** Install → SSO sign-in → keyboard-shortcut tutorial → first archive / send / Cmd-K within 5 minutes.

**Is your desktop app a creative / production tool (Figma Desktop, Cursor, Notion Desktop, Linear Desktop)?**
→ Run **#4 The Workspace-Sync Funnel.** Install → SSO sign-in → existing workspace opens → first edit within 5 minutes → native-only features highlighted.

**Is your desktop app a menu-bar utility (Cleanshot, Bartender, BetterTouchTool)?**
→ Run **#5 The Menu-Bar-First Funnel.** Install → menu-bar icon tutorial → first invocation from menu bar → settings panel for power features.

**Is your desktop app a native AI runtime (Talat, Ollama desktop, local Claude / GPT runners)?**
→ Run **#6 The Local-AI Funnel.** Install → model download with progress + size disclosure → first local inference → privacy / no-cloud reassurance.

**None of the above and you're stuck?**
→ Default to **#3 Keyboard-First Funnel** if your audience is power users; **#4 Workspace-Sync Funnel** if your product is collaborative.

---

## The 18 Tactics

Organized by stage. Build top-to-bottom.

---

### Stage 1 — The Download (the first 60 seconds)

#### 1. The Code-Signed, Notarized Download

**Why:** A Mac DMG that hasn't been signed and notarized triggers Gatekeeper's "This app cannot be opened" warning — and the user has to right-click → Open, type their admin password, and approve it explicitly. ~30% of users abandon at this point. **Code-signing and notarization are non-negotiable. Universal binaries (Intel + Apple Silicon) are non-negotiable. Windows code-signing certificates are non-negotiable.**

**Pass threshold:** App opens on first double-click with no Gatekeeper warning. Universal binary on macOS. Code-signed installer on Windows.

#### 2. The Mac App Store / Microsoft Store Distribution Option

**Why:** Distribution via the Mac App Store and Microsoft Store dramatically improves install completion — the OS handles the download, the install, and the trust signal. Granola, Raycast (paid tier), Superhuman, and most prosumer apps now ship via both direct download (for power-user trust) and the App Stores (for convenience). **Single-channel distribution is a 30%+ install-completion penalty.**

**Pass threshold:** App available on at least one platform store (Mac App Store, Microsoft Store, Linux package managers) in addition to direct download.

#### 3. The Delta-Update Builder

**Why:** Desktop apps that don't auto-update bit-rot. Users on stale versions hit bugs the team fixed three months ago. Sparkle (Mac native), Squirrel (Electron), and Tauri's updater are the standard solutions. **Auto-update must be on by default, silent, and incremental (only download what's changed).** This is the operating floor for desktop apps in 2026.

**Pass threshold:** Auto-update on by default. Delta updates (not full re-downloads) on every release. Update frequency at least monthly.

---

### Stage 2 — The First Launch (the next 5 minutes)

#### 4. The Sub-Second Cold Start

**Why:** Electron 34+ ships sub-500ms cold starts for well-built apps. Tauri ships even faster. Native Swift apps are instant. **The user's first experience of the desktop app must be "this feels faster than the web."** If the first launch shows a progress bar, a splash screen, or any indication of slowness, the user has already started doubting the install was worth it.

**Pass threshold:** Cold-start to first interactive surface in under 1 second on standard hardware (M1 Mac / mid-range PC).

#### 5. The SSO-First Sign-In

**Why:** The first screen is sign-in. SSO (Google, Apple, Microsoft, GitHub) above email/password. For team / B2B desktop apps, the sign-in must SSO into the existing web workspace — the desktop app inherits the user's session, settings, and data. **A separate desktop account is a horizontal-SaaS antipattern.**

**Pass threshold:** SSO providers visible above the email field. Existing web workspace sync immediately on sign-in.

#### 6. The Staged Permission Request

**Why:** Don't ask for all permissions at install. Ask only for what you need at the moment of need: microphone when the user clicks "Record a meeting"; screen recording when they click "Capture screen"; accessibility when they enable global hotkeys. **Each permission request is a cliff — bundling them all at install loses users to permission fatigue.**

**Pass threshold:** Permissions requested individually at the moment of need. Pre-permission explainer screen before each macOS dialog.

---

### Stage 3 — The First Action (the next 5 minutes)

#### 7. The Keyboard-Shortcut Setup

**Why:** Raycast's onboarding *is* setting up the global hotkey. Linear Desktop opens directly to a Cmd-K demo. Superhuman's first user action is a keyboard shortcut, not a mouse click. **The keyboard-shortcut setup is the activation event for power-user desktop apps — and it must be the first thing the user does after sign-in, not a hidden preference.**

**Pass threshold:** Keyboard-shortcut setup happens in the first 60 seconds after sign-in. Default suggestion offered (e.g., "Cmd+Space to replace Spotlight").

#### 8. The Menu-Bar Tutorial

**Why:** Menu-bar apps (Granola, Cleanshot, Bartender, 1Password) live in the top-right of the screen. **First-launch tutorial must point to the menu bar — literally, with an arrow — and demonstrate the icon's role.** A menu-bar app the user can't find after closing the main window is uninstalled within 48 hours.

**Pass threshold:** First-launch tutorial includes a visual indicator pointing at the menu-bar icon. User taught to invoke the app from the menu bar.

#### 9. The First Action Wow

**Why:** Granola records the user's first meeting and generates a summary in <10 minutes. Raycast runs a calculator / window-management / quick-look in <60 seconds. Linear Desktop opens to the user's existing issues. **The first action must be a real action — not a tutorial, not a demo — that produces a real artifact the user can keep.**

**Pass threshold:** User performs the core action (record, send, search, generate) within 5 minutes of first launch and gets a persisted artifact.

---

### Stage 4 — Settings That Make It Default (the next 24 hours)

#### 10. The Auto-Launch-On-Login Prompt

**Why:** A desktop app that opens only when the user remembers is uninstalled within a week. **Auto-launch on login is the retention setting** — and it must be prompted in the onboarding, not buried in preferences. Raycast, Granola, Superhuman, Notion, Linear all prompt for this in the first session.

**Pass threshold:** Auto-launch-on-login prompted in the first session. Visible "we'll launch quietly in the background on login" framing.

#### 11. The "Replace the Default" Prompt

**Why:** Raycast asks to replace Spotlight (Cmd+Space). Arc asks to become the default browser. Superhuman asks to be the default mail client. **Replacing the OS default is the strongest retention move in a desktop app's first week** — once the user's muscle memory rewires, switching back is painful.

**Pass threshold:** "Replace the default [X]" prompt in the first session for apps that have an OS-default competitor. Conversion measured.

#### 12. The Existing-Data Import

**Why:** Notion Desktop opens to the user's existing workspace. Linear Desktop opens to existing issues. Granola syncs to existing meeting library. Superhuman imports from Gmail. **The desktop app must inherit the user's existing data on first launch — empty-state on desktop is a horizontal-SaaS antipattern.**

**Pass threshold:** First-launch experience shows the user's existing data (from web account, from other apps, from system data) — not an empty state.

---

### Stage 5 — Cross-Device and Web Continuity (week 1)

#### 13. The Companion Mobile App Push

**Why:** Granola's iOS app, Linear's iOS app, Superhuman's iOS app, Notion's mobile app — every winning desktop product has a mobile companion. **The desktop user who installs the mobile companion is functionally locked in** (data follows them, both surfaces show the same workspace, the product becomes ambient). The mobile push happens in the first week.

**Pass threshold:** Mobile companion prompted in the desktop onboarding (QR code, app-store link, or send-to-phone). Conversion measured.

#### 14. The Web App Anchor

**Why:** The desktop app is rarely the only surface — the web app is the canonical product, the desktop app is a power-user surface. **Show the user how to access their data on the web** (for sharing, for working on someone else's machine, for collaboration links). Linear, Notion, Figma all make web URLs first-class artifacts.

**Pass threshold:** Web URLs shareable from the desktop app. Web access link visible in the desktop UI.

#### 15. The Team / Workspace Invite

**Why:** Same as B2B AI SaaS: the second user is the contract. Linear Desktop, Notion Desktop, Granola Spaces — every desktop product with multi-user value surfaces team invites in the onboarding. **The invite happens during the activation moment, not buried in settings.**

**Pass threshold:** Team-invite surface in the first session for collaborative desktop apps. Pre-detected teammates from the user's email domain.

---

### Stage 6 — The Long Game (month 2+)

#### 16. The Power-User Feature Unlock

**Why:** Mature desktop apps reward power users with deeper features — Raycast Extensions, Granola Recipes, Linear's keyboard shortcuts, Superhuman's keyboard-shortcut cheat sheet. **The 2026 winners gradually unlock power-user surfaces as the user proves usage** — not all at once, not in the onboarding. The power-user tier is the retention loop.

**Pass threshold:** Power-user features (extensions, automations, advanced shortcuts) gradually unlocked as the user crosses usage thresholds.

#### 17. The Monthly Release Cadence

**Why:** Desktop apps that don't ship monthly bit-rot in user perception. Granola's "Recipes" launch in late 2025, "Spaces" in 2026. Raycast's near-weekly changelog. Linear's frequent updates. **Public changelog + monthly minor releases is the desktop equivalent of the API-tool weekly changelog — it's both retention and acquisition.**

**Pass threshold:** Monthly release cadence with public changelog. In-app "what's new" surfaced on update.

#### 18. The Uninstall Recovery Flow

**Why:** Mac uninstall is just "drag to trash." The app gets no signal. But many apps now register a launch-on-removal handler or fire a final ping that opens a "we're sad to see you go" web page with a one-question exit survey. **Like the browser-extension uninstall URL, this is the only feedback mechanism Mac gives you — most apps ignore it.**

**Pass threshold:** Uninstall-detection mechanism (launchctl unload, periodic check, or web-side activity timeout) triggers a recovery email or web survey within 24 hours.

---

## Worked Example 1 — The Granola Funnel Reconstructed

This is the Granola flow as documented across the Granola product teardowns, TechCrunch's $125M Series C coverage, and the Bluedot 2026 review. Granola scaled to **$1.5B valuation in roughly 12 months** by collapsing the time-from-signup to first-recorded-meeting to under 10 minutes — with only one permission (microphone) required.

| Step | Pattern | Why It Works |
| --- | --- | --- |
| 1. Download from granola.ai (Mac-only initially) | Code-signed, notarized download | Zero Gatekeeper friction |
| 2. App opens in <1 second | Sub-second cold start | Native-feel wow on launch |
| 3. SSO sign-in with Google / Apple | SSO-first | Frictionless |
| 4. Join existing team / workspace if invited | Existing-data import | No empty state |
| 5. Microphone permission requested with explainer | Staged permission request | The only critical permission |
| 6. "Record your next meeting" CTA on the home screen | First action wow | Real action, not a tutorial |
| 7. Lives in menu bar with "active recording" indicator | Menu-bar tutorial | Persistent presence |
| 8. Auto-launch on login prompted | Auto-launch-on-login | Retention setting |
| 9. Meeting transcribed with 90–95% accuracy on clear audio | Native speed | Web competitors can't match |
| 10. Notion-style notes generated post-meeting | First action wow → artifact | Persisted output, shareable |
| 11. Spaces, Recipes, Personal API added in 2026 | Power-user feature unlock | Retention compounds |
| 12. Mobile companion (added during 2026 expansion) | Mobile companion push | Cross-device lock-in |

**Result:** $1.5B valuation in March 2026, up from $250M a year earlier. $125M Series C led by Index Ventures. The microphone-first AI-desktop playbook is now the reference pattern for the 2026 AI desktop wave.

---

## Worked Example 2 — The Raycast Funnel Reconstructed

This is the Raycast flow as documented in the Raycast Manual and the wondertools review. Raycast is the canonical reference for power-user desktop apps — its activation event is literally replacing the OS default (Cmd+Space, Spotlight) with its own hotkey.

| Step | Pattern | Why It Works |
| --- | --- | --- |
| 1. Download from raycast.com | Code-signed, notarized | Zero install friction |
| 2. App opens in <1 second | Sub-second cold start | "This feels faster than Spotlight" |
| 3. First-launch onboarding immediately offers "Replace Spotlight" | Keyboard-shortcut setup | Activation event = hotkey rebind |
| 4. Replace Cmd+Space with Raycast hotkey | Replace-the-default prompt | OS muscle-memory rewiring |
| 5. First Raycast command demo in <60 sec (calculator, app launcher) | First action wow | Active utility, instant value |
| 6. Auto-launch on login prompted | Auto-launch-on-login | Retention setting |
| 7. Native macOS commands installed by default | Existing-data import | No empty state |
| 8. Settings → Extensions surface for power users | Power-user feature unlock | Gradual reveal |
| 9. Hotkeys + aliases configurable per command | Keyboard customization | Deep customization for power users |
| 10. Pro tier unlocks AI Chat, Cloud Sync, themes | Behavioral upgrade prompt | After habit forms |
| 11. iOS companion app (announced 2025) | Mobile companion push | Cross-device |
| 12. Weekly changelog with new commands and integrations | Monthly release cadence | Retention compounding |

**Result:** Raycast became the default Spotlight replacement for Mac power users. The "replace the OS default" playbook is now the reference for any desktop app competing with a built-in OS utility.

---

## Worked Example 3 — The Notion / Linear / Figma Desktop Funnel

For collaborative desktop apps (Notion Desktop, Linear Desktop, Figma Desktop), the desktop app is a power-user wrapper around the web product — same data, same workspaces, but with native shortcuts, offline support, and integration into the OS dock.

| Step | Pattern | Why It Works |
| --- | --- | --- |
| 1. Download from notion.so / linear.app / figma.com | Code-signed, notarized | Trust signal |
| 2. App opens in <1 second (Electron 34+, well-built) | Sub-second cold start | Native-feel |
| 3. SSO sign-in (or auto-detect existing web session) | SSO-first | Inherits web identity |
| 4. Existing workspace opens automatically | Existing-data import | No empty state, full workspace ready |
| 5. Keyboard-shortcut tutorial overlay (Cmd-K / Cmd-N / Cmd-/ menu) | Keyboard-shortcut setup | Activation = first command |
| 6. Native menu bar with app-specific commands | Native integration | Mac/Windows native feel |
| 7. Auto-launch on login prompted | Auto-launch-on-login | Retention setting |
| 8. Mobile companion app installation prompt | Mobile companion push | Cross-device lock-in |
| 9. Pin to dock prompt (macOS) | Dock-pin = retention | Persistent dock presence |
| 10. Offline mode tested on first session loss | Native advantage | Web competitor can't match |
| 11. Monthly release cadence with auto-update | Monthly release cadence | Always-current product |
| 12. Web companion fully synced | Web app anchor | Cross-surface continuity |

**Result:** Notion, Linear, and Figma desktop apps are the default surface for power users of those products, with the web app reserved for "I'm on someone else's machine" sessions. The desktop-as-power-user-surface pattern is the canonical reference for collaborative SaaS products.

---

## Anti-Patterns — What Kills Desktop App Onboarding

### The Unsigned DMG

A Mac DMG that triggers Gatekeeper's "cannot be opened" warning. ~30% of users abandon at this point. **Code-signing and notarization are non-negotiable.**

### The "Allow All Permissions Now" Wall

Asking for accessibility, microphone, screen recording, and full disk access in the first launch, before the user has any context for why. Each permission is a cliff; bundling them all is permission fatigue. **Stage permissions by feature.**

### The Slow Cold Start

A first launch that takes 5+ seconds. The user's brain immediately thinks "this is slower than the web." Death sentence. **Sub-second cold start, always.**

### The Hidden Keyboard Shortcuts

A power-user desktop app with great keyboard shortcuts that aren't surfaced in the onboarding. Users mouse around for a week, decide it's "not faster than the web," and uninstall. **Teach shortcuts in the first 5 minutes, with overlays and cheat sheets.**

### The Menu-Bar App With No Tutorial

A menu-bar utility that closes its main window after first launch and the user can't find it again. **Always include an explicit "look at the menu bar" tutorial.**

### The Login Without SSO

Email/password as the only sign-in option. Especially fatal for desktop apps where SSO inherits the web session. **SSO first, always.**

### The Forgotten Auto-Launch

Never prompting the user to auto-launch on login. The user opens the app twice, forgets it exists, and uninstalls within a week. **Prompt for auto-launch in the first session.**

### The Empty-State Desktop

Opening the desktop app to an empty workspace or empty home screen. The user just signed in — show them their data. **Inherit data from the web account on first launch.**

### The Manual Update

An app that requires the user to manually download a new version. The user is on version 1.2 from six months ago; the team fixed their bug in 1.5. **Auto-update on by default.**

### The Windows-First Launch

A prosumer / power-user product that launches Windows-first in 2026. The early-adopter audience is on Mac. **Mac-first for prosumer products.**

### The 200MB Electron App for a 5MB Job

Shipping a 200MB Electron bundle for an app that does one simple thing. The user's perception of "is this product worth keeping" is informed by disk footprint. **For lightweight utilities, ship Tauri (2–10MB) or native. For complex apps, optimized Electron is fine.**

### The Bit-Rotted Stale App

No updates in 6+ months. Users see "Last updated 2024-09" in the menu and conclude the app is abandoned. **Monthly release cadence with public changelog.**

---

## Calibration — What Good Looks Like

If your desktop-app onboarding is performing well, these are the marks to hit.

| Metric | Floor | Good | Best-in-class |
| --- | --- | --- | --- |
| Download → install completion | 65% | 85% | 95%+ |
| Install → first launch | 70% | 88% | 97%+ |
| First launch → sign-in completion | 75% | 90% | 97%+ |
| First launch cold-start time | 3 sec | 1 sec | <500 ms |
| Sign-in → first core action | 50% | 75% | 90%+ |
| Time from first launch to first core action | 10 min | 5 min | <2 min |
| % who set up the keyboard shortcut / replace OS default | 30% | 55% | 80%+ |
| % who enable auto-launch on login | 35% | 60% | 80%+ |
| Day-7 retention (active use) | 40% | 60% | 80%+ |
| Day-30 retention | 25% | 45% | 70%+ |
| % who install the mobile companion within 30 days | 15% | 35% | 60%+ |
| App Store rating (Mac App Store / Microsoft Store) | 4.2 | 4.6 | 4.8+ |

If you are below the floor on first-launch-to-first-action or day-7 retention, the fix is almost never the feature set — it is the permission staging, the keyboard-shortcut setup, or the auto-launch prompt. Re-read principles #2, #3, and #6.

---

## The Desktop-App Operating Model

Four functions running continuously:

**1. Cold-start performance budget.** Cold-start time is a primary KPI, treated like web Time-to-Interactive. Any regression triggers a release block.

**2. Permission opt-in analytics.** Every permission request is a conversion event. Pre-permission screens are A/B tested. Staged-vs-bundled is monitored per platform.

**3. Cross-surface synchronization.** Desktop, web, and mobile are continuously tested for state synchronization. Drift between surfaces is a P1 bug.

**4. Auto-update discipline.** Monthly release cadence with public changelog. Updates are silent, incremental, and reliable. Rollback paths exist for every release.

---

## Closing — The One Mental Model That Beats Everything

> **A desktop app is on probation for its first 7 days. The user downloaded it, opened it, granted permissions, and now keeps it in their dock — but only because they're still hoping it'll be faster, more powerful, and more native than the web app they could have just used. Your only job is to honor that hope: open in under a second, demonstrate the keyboard shortcut, render their existing data, ask for one critical permission at the moment of need, and prompt to auto-launch on login. Get those five things right and you have a permanent dock occupant. Get any one of them wrong and you have a dock graveyard.**

Granola's $1.5B valuation is the modern reference. The download is signed. The app opens in <1 second. The microphone permission has a clear explainer. The first meeting recording produces a polished summary in <10 minutes. The app lives in the menu bar. It syncs to web. It now has a mobile companion. Every box gets checked, and the user's expectation that "the desktop app is the better surface for this work" is rewarded.

Raycast did the same for power-user productivity by literally replacing the OS default. Linear, Notion, and Figma did the same for collaborative SaaS by becoming the keyboard-driven, offline-capable surface their web apps couldn't be. The desktop-app playbook in 2026 is more constrained than any other surface — and that constraint, when honored, produces the highest-retention products in software.

---

*Sources & teardowns this guide draws from: TechCrunch's "Granola raises $125M, hits $1.5B valuation" (March 2026); Bluedot's In-Depth Granola Review 2026; the Raycast Manual and wondertools review; Apple's macOS permission documentation; the Tauri vs Electron 2026 benchmark suite from Pkgpulse, Tibicle, and Tech-Insider; the Wispr Flow and Talat AI-desktop launches (TechCrunch March 2026); the Arc Browser onboarding documentation; and the comparative Electron-vs-native analysis for Notion, Linear, and Figma desktop apps.*
