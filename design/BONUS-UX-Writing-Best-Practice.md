# BONUS - UX Writing Best Practice

*A bonus asset for ProductOS — 12 principles, 20 tactics, and a decision tree distilled from the canonical interface writing guides: Apple's Human Interface Guidelines, Google's Material Design writing guidance, the Microsoft Writing Style Guide, Shopify Polaris, the Mailchimp Content Style Guide, Atlassian's message-design foundations, GOV.UK's content design standards, Nielsen Norman Group's research on errors, links, and forms, Torrey Podmajersky's* Strategic Writing for UX*, and Kinneret Yifrah's* Microcopy: The Complete Guide*.*

---

## The Meta-Rule

> **Every in-product string exists to help a busy person mid-task take their next action. The reader is not browsing — they are doing something, and your words are in the way of it. So the priority order is fixed: clear beats concise, concise beats consistent, consistent beats voice, and voice beats wit — and you only get to spend the next level down once the level above is satisfied. The best interface copy is the copy nobody notices, because they never had to stop and read it twice.**

Landing pages sell the next click. Onboarding sells activation. **In-product copy sells nothing — it gets a person through their task and out of your text as fast as possible.** GOV.UK, which runs the most heavily tested interface prose in the world, puts it flatly: if people do not notice your copy, you're probably doing it right. This is also why LLM-drafted interface copy fails by default: a language model's prior is marketing English — the most *likely* next word, which is almost never the most *specific* one. Everything in this document is a constraint you can apply mechanically to force specificity back in.

---

## The Numbers That Set the Stakes

These are the tested numbers behind the rules — from NN/g's reading studies, GOV.UK's content research, Shopify's Polaris guidelines, and cross-platform notification limits.

| Metric | Number | Source |
| --- | --- | --- |
| Share of words users actually read on a screen | **20–28%** | NN/g |
| Sentence length at which comprehension starts to fail | **25 words** — check and split anything longer | GOV.UK |
| Reading level ceiling for interface copy | **US grade 7** (Shopify) / **age 9** (GOV.UK — even for specialist audiences) | Shopify Polaris, GOV.UK |
| Common words an average reader recognizes by shape (no decoding) | **~5,000** — why "help" beats "assist" for every reader, including experts | GOV.UK |
| Button label budget | **1–3 words, ≤ ~25 characters** | Polaris, cross-platform |
| Text expansion in German/Finnish localization | **+100–200%** — long English labels break translated layouts | Industry localization standard |
| Push notification title visible before truncation | **~25–50 characters** | iOS/Android platform limits |
| Push notification body visible in collapsed view | **~80–120 characters** | iOS/Android platform limits |
| Sentences in a message body before it stops being read | **2** | Atlassian |
| Exclamation marks per flow | **1, maximum — and never in an error** | Polaris, GOV.UK |

The two numbers that should change how you write: **users read 20–28% of your words** — so the first two words of every string carry most of its meaning — and **reading age 9 is the target even for expert audiences**, because specialists prefer plain language too; they're just as busy as everyone else.

---

## The 12 Principles

These are the mental models that show up across every canonical guide.

### 1. Clear, Then Concise, Then Consistent — In That Order

Clarity is the only non-negotiable. Cut words until the meaning would break, and no further — approach every string like Jenga: what's the most you can remove before it falls apart? But never buy brevity with ambiguity: "Remove?" is shorter than "Remove photo?" and worse. When clarity and brevity conflict, clarity wins; when brevity and voice conflict, brevity wins.

### 2. Front-Load the Message

Users read a fifth to a quarter of the words on a screen, scanning down the left edge. The first two words of every string — heading, link, notification, error — must carry its meaning. "To remove a photo from this album, drag it to the trash" leads with the user's objective; "Drag a photo to the trash to remove it from this album" makes them read to the end to learn why they'd bother. Objective first, action second.

### 3. Write for a Reader in the Middle of a Task

Interface copy is read under load — the user is holding their task in their head while your words interrupt it. Grade-7 reading level. One idea per sentence. Sentences of 25 words or fewer. Short common words: "help" not "assist", "about" not "approximately", "buy" not "purchase", "turn on" not "enable". If you have to explain how the interface works, fix the interface, not the copy.

### 4. Buttons Say What They Do

Every button label is a promise about what happens on click. The formula is **{verb} + {noun}**: "Create invoice", "View shipping settings", "Activate Apple Pay". Generic labels — OK, Submit, Continue, Yes, Get Started as an entry point — force the user to read the surrounding text to know what they're agreeing to, and NN/g's testing shows they act on the button alone. One-word labels are fine only when immediate context supplies the noun (Done, Cancel, Save inside a titled modal).

### 5. One Name Per Thing, Everywhere

A product has a vocabulary: its nouns (what things are called) and verbs (what you do to them). Every synonym you introduce reads as a new feature. If the menu says "Remove photo" and the dialog asks "Delete photo?", the user now believes there are two operations and wonders which one they triggered. Build the lexicon once, then obey it in every string, every screen, every notification — and know the real distinctions: *delete* destroys, *remove* takes out of a list and is recoverable.

### 6. Errors Are Instructions, Not Apologies

An error message has exactly three jobs: say what happened, say why (or which item), and say what to do next — with the fix stated as a specific imperative: "Choose a password with at least 8 characters", not "That password is too short." No blame ("Wrong password", never "You entered the wrong password"), no drama words (invalid, illegal, fatal, forbidden), no error codes the user can't use, and no "sorry" in routine validation — apology inflates severity. Save one sincere apology for the outage you actually caused.

### 7. Empty States Are Onboarding, Not Dead Ends

An empty screen is a moment of maximum uncertainty: is it broken, or is there nothing here yet? The empty state answers in one breath — why it's empty, and the one action that fills it. "Add your first product and see how it looks in your store. [Add product]" A motivational poster with no next action ("Your journey starts here!") is a dead end wearing a smile.

### 8. Confirmations State the Consequence and Put Verbs on the Buttons

"Are you sure?" is a question the user cannot answer, because it doesn't say what happens next. The pattern is: title = "{Verb} {noun}?" ("Delete 2 collections?"), body = the consequence in one line ("This can't be undone."), and buttons that echo the verb — [Cancel] [Delete], [Keep editing] [Discard], [Stay] [Leave page]. Never Yes/No/OK on a consequential action: the button label must be readable on its own, because that's how it will be read.

### 9. The Interface Is Not a Person

The product doesn't plead ("please"), doesn't gush ("Awesome! 🎉"), doesn't take credit ("We did it!"), and doesn't hover ("You successfully added a product"). It states results ("Product saved") and gets out of the way. Celebrate the user's genuine milestones — first launch, first sale — briefly and by crediting *them*. Thank users only when they did something for you, like sending feedback. Routine competence is not an achievement; congratulating someone for saving a file is patronizing.

### 10. Tone Bends to the Situation; Voice Never Changes

Voice is who the product is; tone is how it reads the room. You never know a user's emotional state — but you always know the *situation*: an everyday task wants invisible copy, a simple error wants calm specifics, a serious failure wants direct facts and a single apology if you caused it, a true milestone wants one brief line of genuine credit. Apple's watch demonstrates the range: fall detection speaks in flat declaratives; a Move-streak record gets one light congratulatory line. Same voice, opposite tones — and the stressed user always gets the plainest register.

### 11. The Mechanical Layer Is Fixed

Beneath any brand voice sits a non-negotiable layer of mechanics: sentence case everywhere; no terminal periods on titles, labels, or buttons; active voice; second person ("you") — first person ("my") only for ownership and consent, never mixed in one phrase; present tense ("Message sent", not "Message has been sent"); numerals, not words ("3 messages"); positive framing ("Use only letters", not "Don't use numbers or symbols"). These are not style preferences — each one is a tested comprehension gain. Voice lives in word choice and rhythm *inside* these rules, never instead of them.

### 12. Copy Is a System, Not a String

The unit of quality is not the sentence — it's the system. A perfect error message that uses a noun no other screen uses is a defect. Write every string *from* the lexicon and the voice chart, review every screen *against* the rubric, and treat the copy guide as a living document that grows a row every time the product grows a concept.

---

## The Decision Tree — Which Kind of String Am I Writing?

Start at the top. Stop at the first "yes."

**Is it a control the user clicks, taps, or fills in — a button, link, label, field?**
→ Stage 1 (buttons & CTAs) or Stage 2 (labels, nav & forms). The {verb} + {noun} rules govern.

**Is it a screen or region with nothing in it, or something still arriving?**
→ Stage 3 (empty states) or Stage 4 (loading & progress). Reason + next action; name the wait.

**Did something go wrong?**
→ Stage 5 (errors & validation). Three parts: what happened, why, what to do next.

**Is the user about to do something consequential that needs their consent?**
→ Stage 6 (confirmations & destructive actions). "{Verb} {noun}?" + consequence + verb-labeled buttons.

**Did something succeed, or does the product want the user's attention?**
→ Stage 7 (success, toasts, notifications & permissions). Quiet acknowledgment; front-loaded asks.

**None of the above — you're naming a concept, writing a setting, or reviewing a screen?**
→ Stage 8 (the long game). The lexicon and the rubric govern.

---

## The 20 Tactics

Organized by surface. Every tactic carries a pass threshold you can check mechanically.

---

### Stage 1 — Buttons & CTAs

#### 1. The {Verb} {Noun} Button

**Why:** Users act on the button label alone — eye-tracking shows they routinely skip the copy above it. A label that names its own action ("Update bank account") survives being read in isolation; "OK", "Submit", and "Yes" do not. Strong verb first, object second, sentence case, no articles, no punctuation.

> Bad: "Let's do it!" · Good: "Send" *(Apple)*
> Bad: "Try Apple Pay" · Good: "Activate Apple Pay" *(Polaris)*
> Bad: "Settings" · Good: "View shipping settings" *(Polaris)*
> Bad: "Add a menu item" · Good: "Add menu item" *(Polaris)*

**Pass threshold:** Every button starts with a verb or is one of the universal one-worders (Done, Close, Cancel, OK-for-information-only, Save) inside a context that supplies the noun. No button reads "Submit", "Yes", or "No" on a consequential action.

#### 2. The Verb Dictionary

**Why:** Verbs carry precise meanings users learn across products. Using the wrong one creates false expectations. The canonical distinctions (Polaris):

- **Create** = make from scratch ("Create order") · **Add** = bring something existing in ("Add product")
- **Save** = writes now · **Done** = deferred save, applied when the parent saves
- **Edit** = change contents · **Manage** = a hub of several actions
- **Change** = replace with something else · **Switch** = swap between accounts, modes, locations
- **Select** = pick from a closed list · **Choose** = an open-ended, subjective decision
- **View** = a CTA that navigates · **see** = conversational prose only
- **Export / Import** = format conversion · **Download / Upload** = same-format copy
- **OK** = acknowledge information only · **Accept** = legal terms only · **Cancel** = the escape hatch · **Close** = view-only surfaces
- **Delete** = destroy · **Remove** = take out of a list, recoverable

**Pass threshold:** Every verb in the product matches this table's meaning, and each concept uses exactly one verb everywhere.

#### 3. The Character Budget

**Why:** English is the shortest major language. German and Finnish translations run +100–200% longer, and a 30-character English label becomes a broken layout. Budgets: buttons 1–3 words, ≤ ~25 characters; field labels 1–3 words; toasts 2–5 words. Short labels are not a style choice — they're a survival requirement for every layout the copy will ever live in.

**Pass threshold:** No button over 25 characters; no field label over 3 words.

---

### Stage 2 — Labels, Nav Nouns & Forms

#### 4. The Visible Label

**Why:** Placeholder text is not a label. It vanishes on focus — the moment the user needs it most — breaks short-term memory mid-form, and is invisible to many screen readers (NN/g: "Placeholders in Form Fields Are Harmful"). Every field keeps a visible label outside the field. Placeholders, if used at all, show a format example only: "name@example.com".

**Pass threshold:** Zero fields where the placeholder is the only label. Zero placeholders containing instructions the user must remember.

#### 5. The Bare-Noun Label

**Why:** Labels, headings, and nav items are scan targets, not sentences. Sentence case; no articles ("Create collection", not "Create a collection"); no colons ("Share with", not "Share with:"); no terminal periods; front-loaded keyword. Mark the exception, not the rule: append "(optional)" to optional fields rather than starring required ones. Help text only where research shows it's needed — and never as a preamble: "Total cost", not "This is the total cost".

> Bad: "Buy New Domain" · Good: "Buy new domain" *(Polaris)*

**Pass threshold:** All labels sentence case, article-free, punctuation-free. Optional fields marked "(optional)".

#### 6. The Descriptive Link

**Why:** Screen readers read links out of context, and sighted users scan them the same way. NN/g's 4Ss: **specific** (says what's on the other side), **sincere** (the expectation is instantly met), **substantial** (meaningful in isolation), **succinct** (the first two words carry it). "Click here" and bare "Learn more" fail all four.

> Bad: "Want to learn more about dropshipping? Click here." · Good: "Get started with the [Ultimate Guide to Dropshipping]." *(Polaris)*

**Pass threshold:** No link labeled "here", "click here", or bare "Learn more". In-sentence links wrap only the words that describe the destination.

---

### Stage 3 — Empty States

#### 7. The Three Empty States

**Why:** "Empty" means three different things, and each needs different copy. **First-run** (never used): educate and invite — this is the one surface where personality and full sentences earn their place: "Secure your account with two-step authentication." **User-cleared** (task done): acknowledge briefly — "All caught up." **No-results** (search or filter came back empty): state it and offer the loosening move — "No products match 'winter'. Try a shorter search." Writing first-run copy on a no-results state ("Add your first product!" when the user has 400 products filtered out) reads as broken.

**Pass threshold:** Each empty surface is classified as one of the three states and its copy matches the state.

#### 8. Reason + One CTA

**Why:** An empty state's anatomy is fixed: title of a few words (may invite the first action), body of 1–2 sentences (why it's empty + what to do), and exactly one primary CTA of 1–2 words that completes the thought. Two CTAs split the user's first step; zero CTAs is a dead end. The more often a state recurs, the plainer the copy — the joke that charmed on day one grates on day ninety.

> Bad: "Your journey starts here!" · Good: "Add your first product and see how it looks in your store. [Add product]" *(Polaris)*

**Pass threshold:** Every empty state names its reason and carries exactly one CTA. No crucial information lives only in an empty state.

---

### Stage 4 — Loading & Progress

#### 9. The Named Wait

**Why:** A spinner with no words is a broken promise; a spinner with jargon is worse. Name the wait in the user's terms, present progressive, and set the expectation if it's long: "Preparing video…", not "Buffering…"; "Your phone is contacting us. This can take up to 5 minutes.", not a paragraph about servers. Never explain the mechanism — users need to know what's happening to *them*, not to your infrastructure.

> Bad: "Buffering…" · Good: "Preparing video…" *(Material)*

**Pass threshold:** Every wait over a beat has a user-world label; waits over ~10 seconds state a duration or show progress.

---

### Stage 5 — Errors & Validation

#### 10. The Three-Part Error

**Why:** Every error answers three questions in order — what happened, why (or which item), what to do next — with the fix as a specific imperative carrying real numbers, limits, or the user's own data. The title states the effect on the user in 3–4 words; the body is 1–2 sentences; the CTA is a one-click fix wherever possible.

> Bad: "Invalid ID" · Good: "You need an ID that looks like this: someone@example.com" *(Microsoft)*
> Bad: "That password is too short" · Good: "Choose a password with at least 8 characters" *(Apple)*
> Bad: "Invalid bank account. Your payout was not deposited. [Next]" · Good: "Couldn't deposit payout — The bank account we have on file was closed. Update your details, and we'll retry automatically. [Update bank account]" *(Polaris)*

**Pass threshold:** Every error names its fix. Zero errors consisting only of a problem statement. Banned words nowhere present: invalid, illegal, forbidden, bad request, fatal, oops, uh-oh, raw error codes.

#### 11. The Blame-Free Sentence

**Why:** Errors describe the problem, never the user's failure — "you" as the subject of a mistake reads as scolding and adds zero information. Strip the accusation and the message gets shorter *and* kinder.

> Bad: "You have entered the wrong password" · Good: "Wrong password" *(GOV.UK)*

**Pass threshold:** No error sentence has "you" as the subject of a verb of failure (entered wrong, forgot, failed to).

#### 12. Errors as Tasks

**Why:** When several things fail at once, an error count is useless — the user needs a to-do list. Frame the summary as the tasks that reach the goal, each linked to its field, with the inline message repeated next to each field. Preserve everything the user typed; making people retype is the cardinal sin of validation.

> Bad: "There are 2 errors on this page" · Good: "To save this product, make 2 changes: Enter title · Add weight" *(Polaris)*

**Pass threshold:** Multi-error summaries are phrased as tasks toward the user's goal. User input survives every validation round-trip.

#### 13. The Apology Budget

**Why:** "Sorry" is a currency — spend it on routine validation and it's worthless when the outage comes. No "sorry" in field validation, no "please" making required steps sound optional, no humor (it goes stale on the fifth encounter and reads as mockery under stress). One sincere apology, once, for a serious failure the product caused: "Sorry, there is a technical problem. Please try again in a few moments." (GOV.UK). That's the entire budget.

> Bad: "Oops! Something went wrong 😢 We're so sorry!" · Good: "Something went wrong. Refresh your browser to try again." *(Polaris)*

**Pass threshold:** Zero "sorry"/"oops"/"unfortunately" in validation and routine errors. At most one apology in the whole system, attached to genuine product-caused failure.

---

### Stage 6 — Confirmations & Destructive Actions

#### 14. The {Verb} {Noun}? Dialog

**Why:** Confirm only what's hard to undo — confirming everything trains users to click through the one that matters. The title is the action as a question, the body is the consequence in one line, and "Are you sure" appears nowhere, because it asks about the user's psychology instead of stating what happens next.

> Bad: "Are you sure you want to delete Dark Blue Tee?" · Good: "Delete Dark Blue Tee? — This can't be undone." *(Polaris)*
> Bad: "Would you like to save your changes?" · Good: "Save changes?" *(Material)*

**Pass threshold:** No dialog title contains "Are you sure". Every confirmation's body states a concrete consequence. Only hard-to-undo actions get dialogs.

#### 15. Verb-Labeled Buttons

**Why:** Dialog buttons are read alone, under time pressure, by users who skipped the title. Yes/No/OK force a re-read; verbs don't. The standard pairs: deleting → [Cancel] [Delete]; discarding edits → [Keep editing] [Discard]; leaving with unsaved changes → [Stay] [Leave page]. Never "Cancel" as the escape from a dialog *about* canceling something — the collision is unresolvable. Maximum two actions per dialog.

**Pass threshold:** Both buttons of every confirmation are readable in isolation and unambiguous. Zero Yes/No pairs.

---

### Stage 7 — Success, Toasts, Notifications & Permissions

#### 16. The Quiet Toast

**Why:** Success is the expected outcome — it needs an acknowledgment, not a party. Noun + past participle, 2–5 words, present-tense grammar, no "successfully" (if it happened, it happened successfully), no exclamation mark.

> Bad: "You successfully added a product." · Good: "Product saved" *(Polaris)*
> Bad: "Message has been sent" · Good: "Message sent" *(Material)*

**Pass threshold:** Every routine success message is ≤5 words with zero celebration vocabulary.

#### 17. The Milestone Rule

**Why:** Real celebration exists — for the user's genuine milestones, briefly, crediting them. First launch, first sale, first customer: one line, their achievement, not yours. "We" claiming credit is banned; thanking users is reserved for things they did *for you*.

> Bad: "We did it! Congrats on your first sale." · Good: "You launched your store! Nice work." *(Polaris)*
> Bad: "Thank you for your application" · Good: "Application complete" *(GOV.UK)*

**Pass threshold:** Celebration copy appears only at true milestones, credits the user, and is one line. "Congrats" appears nowhere near a routine task.

#### 18. The Front-Loaded Notification

**Why:** The collapsed view is all most users see: ~25–50 title characters, ~80–120 body characters. The key noun and verb go first; context goes after the fold or nowhere. Interruptive delivery requires genuinely urgent content — a marketing message dressed as an alert torches notification permission for good. Use relative time ("today", "2h ago") over raw timestamps.

**Pass threshold:** Every notification's meaning survives truncation at 50/120 characters. Urgency of delivery matches urgency of content.

#### 19. The Contextual Permission Ask

**Why:** A permission request at app launch, before the user knows why you need it, is an ambush — and iOS/Android give you exactly one clean shot. Ask at the moment the feature needs it, lead with what the user gets, and let them postpone: "To find deals near you, allow location access" at the moment they tap "Find nearby deals" — not a launch-screen battery of system dialogs. The same applies to announcements: dismissible, with "Remind me later".

**Pass threshold:** Every permission ask is triggered by a user action that needs it and names the user benefit first. Nothing consequential is asked on first launch.

---

### Stage 8 — The Long Game

#### 20. The Lexicon and the Rubric

**Why:** Individual strings decay; systems endure. Two artifacts keep copy quality alive after the writing session ends. The **lexicon** — a table of the product's canonical nouns and verbs (Concept / We say / Never say) — grows a row every time the product grows a concept, and every new string is written from it. The **rubric** — a per-screen checklist of the mechanical rules and anti-patterns — runs at design review, the same gate that checks the design tokens. Copy that isn't reviewed against a rubric regresses to the LLM's marketing prior within weeks.

**Pass threshold:** The lexicon exists, is dated, and every UI diff is checked against it. The rubric runs on every screen that ships.

---

## Worked Example 1 — The Destructive Delete Flow

A member's product ("Ledgerly", tone: "plain-spoken, but not blunt") lets users delete a client and all their invoices.

**Menu item:** `Delete client` — verb dictionary: *delete*, because the data is destroyed, not removed to an archive (Tactic #2).
**Dialog title:** `Delete Maria Chen and 34 invoices?` — {Verb} {noun}?, names the real scope with a numeral (Tactic #14, Principle 11).
**Dialog body:** `This deletes all invoices and payment history. It can't be undone.` — consequence, two short sentences, no "Are you sure" (Tactic #14).
**Buttons:** `[Cancel] [Delete client]` — verb-labeled, readable alone (Tactic #15).
**Toast after:** `Client deleted` — quiet, 2 words (Tactic #16).

What the LLM drafted before the rules: *"Are you sure you want to permanently delete this client? This action cannot be reversed and all associated data will be lost forever! [Yes] [No]"* — an Are-You-Sure Dialog with a Yes/No pair, an exclamation mark in a destructive flow, and no named scope.

## Worked Example 2 — The Error-and-Recovery Flow

Same product. A payout fails because the connected bank account was closed.

**Banner title:** `Couldn't send payout` — 3 words, effect on the user (Tactic #10).
**Banner body:** `The bank account ending in 4821 was closed. Add a new account and we'll retry automatically.` — why with the user's own data, then the imperative fix (Tactic #10).
**CTA:** `[Add bank account]` — one-click fix, {verb} {noun} (Tactic #1).
**What's absent:** "sorry" (routine failure, not product-caused — Tactic #13), "invalid", any error code, any "we're having trouble" hedge.

## Worked Example 3 — The First-Run Empty State + Permission Ask

A mobile habit tracker ("Stride", tone: "warm, but not chirpy") on first open.

**Empty state title:** `Track your first habit` — invites the action, 4 words (Tactic #8).
**Body:** `Pick one thing you want to do daily. Stride reminds you at the time you choose.` — why + what happens next, grade-5 words (Tactic #7).
**CTA:** `[Add habit]` (Tactic #1).
**Permission ask** — fired only after the user sets a reminder time, not at launch: `To remind you at 7:00, allow notifications.` — benefit first, triggered in context (Tactic #19).

What the LLM drafted before the rules: *"Welcome to Stride! 🎉 Your journey to a better you starts here. Enable notifications to unlock the full experience!"* — Enthusiasm Overdose, Marketing Bleed, a Permission Ambush, and no next action.

---

## Anti-Patterns — What Kills In-Product Copy

The twelve named failures. Most are the default output of an LLM asked to "write the copy" — which is exactly why they're named: so a review can point at one and everyone knows the fix.

### The Marketing Bleed

Landing-page vocabulary leaking into the interface: streamline, seamless, powerful, effortless, unlock, elevate, supercharge, empower, "insights". **Detect:** any abstraction where a concrete noun should be. **Fix:** name the object and the action — "Streamline your workflow with powerful insights" → "See which pages get the most visits."

### The Wall of Words

Bodies over 2 sentences, sentences over 25 words, restating the title in the body, explaining the mechanism ("Your phone needs to communicate with our servers to…"). **Fix:** what happened + what to do next; delete everything about how the system works.

### The Apology Loop

"Oops!", "Uh-oh", "We're so sorry, but…", "Unfortunately", "Don't worry!". **Fix:** neutral statement + fix path. The apology budget is one, for outages you caused.

### The Enthusiasm Overdose

"Congrats!", "Awesome!", "You're all set! 🎉", "successfully" — for routine chores. **Fix:** "Product saved". Celebration only at true user milestones, crediting the user.

### The Vague Error

"Something went wrong" with no recovery path, or a problem statement with no fix. **Fix:** the three-part anatomy — and if you genuinely don't know the cause, say so and still give the recovery move: "Something went wrong. Refresh your browser to try again."

### The Developer Leak

authenticate, credentials, payload, instantiate, sync conflict, "invalid input", raw error codes, "buffering". **Fix:** the user's words for the user's world — "Wrong password", "Preparing video…".

### The Are-You-Sure Dialog

"Are you sure you want to…?" + [Yes] [No] [OK]. **Fix:** "{Verb} {noun}?" + one-line consequence + verb-labeled buttons.

### The Synonym Shuffle

delete/remove/erase for one operation; edit/modify/change for another; "workspace" on one screen, "project" on the next. **Detect:** two words for one concept anywhere in the product. **Fix:** the lexicon decides; everything else conforms.

### The Robot Passive

"Your file has been uploaded", "The changes will be applied", "It is recommended that…". **Fix:** active voice, present tense, the doer as the subject — "File uploaded", "Changes apply when you save."

### The Empty Empty State

An inspirational line with no action, or a bare "No items". **Fix:** why it's empty + exactly one CTA — and match the copy to which of the three empty states it is.

### The Blame Shift

"You entered an invalid email", "You forgot to add a title". **Fix:** describe the problem, not the person — "Enter an email like name@example.com", "Enter title".

### The Permission Ambush

A launch-screen wall of system permission dialogs before the app has shown any value. **Fix:** ask in context, benefit first, postponable.

Also on the detection list, below the level of a named pattern: hedges ("you can", "simply", "just", "feel free to", "it's recommended"), redundancies ("in order to" → "to", "at this time" → delete, "please be aware that" → delete), generic primary CTAs ("Get Started", "Learn More", "Submit"), placeholder-as-label, directional references ("the button below", "the menu on the left"), and overpromising ("double your sales", "never worry again" → verifiable specifics only).

---

## Calibration — What Good Looks Like

The per-surface budgets in one table — this is the spec the rubric checks against:

| Surface | Budget | Shape |
| --- | --- | --- |
| Button / CTA | 1–3 words, ≤25 chars | {Verb} {noun}, sentence case, no punctuation |
| Field label | 1–3 words | Bare noun, no colon, "(optional)" marks the exception |
| Heading | 3–8 words | Sentence case, front-loaded, no period |
| Error title | 3–4 words | Effect on the user |
| Error body | 1–2 sentences, ≤25 words each | What / why / imperative fix with real numbers |
| Confirmation | 1-line title + 1-line body | "{Verb} {noun}?" + consequence + 2 verb buttons |
| Toast | 2–5 words | Noun + past participle |
| Tooltip | ≤10 words | Supplementary info only — never required instructions |
| Placeholder | 2–5 words | Format example only, never the label |
| Settings description | 1 sentence | What happens when **on** |
| Push notification | ~50-char title, ~120-char body | Key noun + verb first |
| Empty state | ≤6-word title + 1–2 sentences + 1 CTA | Why empty + next action |
| Reading level | Grade 7 / age 9 | Everywhere, including expert products |

**Calibration products** — interfaces worth stealing sentence rhythms from: **Stripe's dashboard** (dense finance rendered at grade-7 reading level; error states that always name the fix), **Linear** (ruthless noun discipline — nothing is ever called two things), **GOV.UK services** (the most usability-tested plain language in production anywhere), and **Mailchimp** (the canonical voice-vs-tone discipline: personality that never costs clarity — note their button title-casing is the one convention *not* to copy). And the deliberate conflict resolutions this document has already made for you: sentence case wins everywhere; Apple's no-"we" rule wins for product UI; the apology budget is one.

---

## The UX Writing Operating Model

1. **The lexicon is law and alive.** Every new feature adds its nouns and verbs to the lexicon *before* the strings are written. A concept that can't get a one-word name isn't ready to ship.
2. **The rubric runs at design review.** The same gate that checks tokens against `docs/DESIGN.md` checks strings against `docs/COPY.md` — every screen, every diff that touches user-facing text.
3. **Errors get written with the feature, not after it.** The error states are part of the spec: for every action, write the failure string when you write the success string.
4. **Recurring copy gets plainer over time.** Anything a user sees daily loses its personality allowance; anything seen once (first-run, milestones) keeps it.
5. **The banned list grows.** Every time review catches a new LLM-ism, it goes on the list — the cheapest possible prevention for its next thousand occurrences.

---

## Closing — The One Mental Model That Beats Everything

> **Write what a competent, busy colleague would say if they were standing next to the user, walking them through the task — then cut half the words. If a string wouldn't survive being spoken aloud across a desk ("You have successfully completed the addition of a product!"), it doesn't belong on a screen. And when in doubt, remember what the copy is for: the user came to do something. Help them do it, and get out of the sentence.**
