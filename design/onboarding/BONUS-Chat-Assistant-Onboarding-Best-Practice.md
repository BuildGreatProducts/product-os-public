# BONUS - Chat Assistant Onboarding Best Practice

*A bonus asset for ProductOS — principles, a decision tree, and staged tactics for onboarding a chat assistant: an assistant people talk to in a chat surface — a custom GPT or other assistant-store listing, a Claude Project shared with clients, a Slack, Teams, or Discord bot, a WhatsApp or Telegram assistant, or a chat embedded on a site. The patterns hold across hosts; host specifics live in the store listing (`design-marketplace-listing`), not here.*

---

## Contents

- [The Meta-Rule](#the-meta-rule)
- [The 10 Principles](#the-10-principles)
- [The Decision Tree — Which Onboarding Pattern Should You Build?](#the-decision-tree--which-onboarding-pattern-should-you-build)
- [The 12 Tactics](#the-12-tactics)
- [Worked Example — A Contract-Review Assistant](#worked-example--a-contract-review-assistant)
- [Anti-Patterns — What Kills Chat Assistant Onboarding](#anti-patterns--what-kills-chat-assistant-onboarding)
- [Calibration — What Good Looks Like](#calibration--what-good-looks-like)
- [Closing — The One Mental Model That Beats Everything](#closing--the-one-mental-model-that-beats-everything)

---

## The Meta-Rule

> **In a chat assistant, the conversation is the onboarding. There are no screens to guide anyone — the first message has to do the work of a welcome screen, a tutorial, and a proof of value at once. Within the first two exchanges the user decides whether this assistant is better than the general assistant they already have. If the first answer could have come from that general assistant, there is no second conversation.**

Everything in this doc serves one goal: get to an answer that is unmistakably specific to the user's situation in as few turns as possible, then give them a reason to come back.

---

## The 10 Principles

### 1. Beat the General Assistant on Turn One

The competitor isn't another niche assistant — it's the general-purpose assistant one tab away. Specialist knowledge, the user's own context, or a structured output the general one doesn't produce must show up in the very first substantive answer.

### 2. The Greeting Sets the Scope

A good greeting says who it's for, what it does, and gives one example of what to ask — in a few lines. It is a scope statement, not a welcome speech. Users who know what an assistant is for ask better first questions, and better first questions produce better first answers.

### 3. Starters Are the Onboarding Buttons

Conversation starters (or suggested prompts, quick replies, slash commands) are the only buttons a chat assistant has. Each one should be a core use case, written in the user's own words, that reliably produces the magic moment.

### 4. Ask Once, in the Flow

Context-gathering quizzes before the first answer feel like a form in disguise. Ask at most one question before giving value — unless personalization *is* the product, in which case ask the two or three questions that change the answer most, then deliver.

### 5. Show, Then Explain

Don't describe capabilities; demonstrate one. An assistant that answers the first question well and then mentions one adjacent thing it can do teaches more than a capabilities list.

### 6. Scope Boundaries Redirect

Every assistant has things it shouldn't do. When a request is out of scope, say what it can do instead, in the brand's voice — a redirect, not a wall. Refusals are onboarding surfaces too.

### 7. Be Honest About Memory and Data

Users don't know what an assistant remembers between conversations, or what happens to what they share. Say it plainly, once, early: what's kept, what isn't, who sees it.

### 8. The Host Shapes the Flow

A DM in a messaging app, a channel in a team workspace, and an assistant-store listing are different contexts: group conversations need brevity and explicit invocation; one-to-one chats can be warmer and longer; workspace bots answer to an admin who installed them. Design for the host the customer is in.

### 9. Design the Hand-Off

Some conversations need a human, a paid tier, or a different tool. The moment the assistant hands off — to a booking link, an upgrade, a support person — is a designed moment with its own copy, not an apology.

### 10. Return Is Earned, Not Nagged

Chat assistants are easy to forget. Earn the return with a useful follow-up the user opted into — a reminder, a digest, a "send me this weekly" — never unsolicited messages.

---

## The Decision Tree — Which Onboarding Pattern Should You Build?

Start at the top. Stop at the first "yes."

**Does it live in an assistant store or directory where users find and open it themselves?**
→ Run **#1 Starter-Led.** Profile that names the job → 3–4 starters → first specific answer → suggested follow-ups.

**Does it live in a team workspace (Slack, Teams, Discord) installed by an admin?**
→ Run **#2 Install and Introduce.** Admin installs → the bot sends the installer a short intro with one try-it command → first answer in a real channel → invite teammates to use it.

**Does it live in a consumer messaging app (WhatsApp, Telegram, SMS)?**
→ Run **#3 First-Message Funnel.** A link or QR code opens the chat with a pre-filled first message → opt-in → one question → first personalized answer.

**Does it need the user's own data (documents, accounts, a knowledge base) to be useful?**
→ Run **#4 Connect, Prove, Ask.** Connect the source → the assistant proves it read it by summarizing one real item → the user asks their first question.

**Is it a paid assistant with free turns?**
→ Run **#5 Free Turns, Then Paywall.** A few genuinely useful answers free → the paywall appears at the moment of value, naming what the user gets next.

**None of the above and you're stuck?**
→ Default to **#1 Starter-Led.** Starters make the first question easy and the first answer predictable.

---

## The 12 Tactics

Organized by stage. Build top to bottom.

---

### Stage 1 — Before the First Message

#### 1. The Profile That Names the Job

**Why:** The name, avatar, and one-line description are what users see before they open the chat. Name the job and the user ("Contract review for freelance designers"), not the technology ("AI-powered legal assistant").

**Pass threshold:** A stranger can say who it's for and what it does from the profile alone.

#### 2. Starters That Show Range

**Why:** Starters double as a capability tour. Each should map to a different core use case, be written as the user would type it, and work every time.

**Pass threshold:** 3–4 starters (or the host's limit), each a distinct use case, each producing a strong answer in testing.

#### 3. The Data Line

**Why:** Users hesitate to paste real documents or connect accounts without knowing where the data goes. One plain sentence — in the profile, the first message, or both — removes that hesitation.

**Pass threshold:** What's stored, for how long, and who can see it is stated before the user shares anything sensitive.

---

### Stage 2 — The First Exchange

#### 4. The Short Greeting

**Why:** Long greetings get skipped, and in group channels they're noise. Scope, one example, one invitation.

**Pass threshold:** The greeting fits in a few short lines (under about 40 words) and ends with a question or an example to try.

#### 5. One Question Before Value

**Why:** Each question before the first useful answer costs patience. Ask the single question that most changes the answer, or none — infer the rest from what the user says.

**Pass threshold:** At most one question before the first substantive answer (two or three only when personalization is the product).

#### 6. The Specific First Answer

**Why:** The first answer is the magic moment. It uses the user's details, applies the specialist knowledge or format the assistant exists for, and is visibly different from a generic answer.

**Pass threshold:** The first answer references the user's own input and contains something a general assistant wouldn't have produced without heavy prompting.

---

### Stage 3 — Turns Two to Five

#### 7. Suggested Follow-Ups

**Why:** After the first answer, users often don't know what to ask next. One to three specific follow-ups keep the conversation moving toward deeper value.

**Pass threshold:** Every early answer ends with at least one concrete next question or action.

#### 8. The Capability Reveal

**Why:** Users discover features by stumbling on them. Once, early, the assistant mentions one adjacent thing it can do that this user is likely to need.

**Pass threshold:** One unprompted, relevant capability mention within the first five turns — not a list.

#### 9. The Graceful Redirect

**Why:** Out-of-scope requests are inevitable. A refusal that says "I can't help with that" ends the conversation; one that says what it can do instead keeps it.

**Pass threshold:** Every out-of-scope response names an in-scope alternative, in the brand's voice, without lecturing.

---

### Stage 4 — The Return

#### 10. The Memory Statement

**Why:** Users who don't know whether the assistant remembers them either repeat themselves or assume it does and get burned. Say what carries over.

**Pass threshold:** The first session tells the user what the assistant will remember next time (or that it won't).

#### 11. The Opt-In Follow-Up

**Why:** A scheduled digest, a reminder, or a "check back with me after the meeting" gives a reason to return — when the user asked for it.

**Pass threshold:** At least one opt-in return trigger offered after the magic moment; no unsolicited messages.

#### 12. The Designed Hand-Off

**Why:** Upgrades, human escalation, and booking links are where assistants make money or keep trust. The hand-off names what happens next and why.

**Pass threshold:** Every hand-off message says where the user is going, what they'll get there, and what happens to the conversation so far.

---

## Worked Example — A Contract-Review Assistant

*A composite example to illustrate the patterns — not a real product.*

An assistant for freelance designers that reviews client contracts, listed in an assistant store (Pattern #1). The profile reads "Contract review for freelance designers — finds the clauses that cost you money." Starters: *"Review this contract before I sign"*, *"Is this kill fee normal?"*, *"Rewrite this clause in my favor"*, *"What should my payment terms be?"*. The greeting: *"Paste a contract or a clause. I'll flag what's risky for a freelancer and suggest wording you can send back. Nothing you paste is used to train models."* The user pastes a contract; the assistant asks one question — "Is this a fixed-fee or hourly project?" — then returns the three riskiest clauses, each with the plain-language risk and a rewritten version. It ends: *"Want a polite email to send these changes to the client?"* When asked for tax advice, it redirects: *"Tax is outside what I cover — I can check the payment and invoicing clauses that affect when you get paid."*

---

## Anti-Patterns — What Kills Chat Assistant Onboarding

### The Wall-of-Text Greeting

A greeting that lists every capability, the backstory, and a disclaimer. Users scroll past it and type something generic. **Scope, one example, one invitation.**

### The Intake Interrogation

Five questions before any value. Users feel processed and leave. **One question, then an answer.**

### The Generic First Answer

An answer indistinguishable from the general assistant's. The user concludes the specialist adds nothing. **Use their details and the specialist edge on turn one.**

### The Dead End

An answer with no next step. The conversation stops and doesn't restart. **End early answers with a follow-up.**

### The Wall Refusal

"I'm sorry, I can't help with that." No alternative, no voice. **Redirect to what it can do.**

### The Persona Overload

Jokes, catchphrases, and character before help. Charm that delays the answer reads as filler. **Voice shows in word choice; help comes first.**

### The Unsolicited Ping

Proactive messages the user never asked for. In messaging apps this gets the assistant muted or reported. **Opt-in only.**

### The Hidden Limit

A free tier that ends mid-answer without warning. **Say the limit upfront and paywall at a natural break, naming what's next.**

### The Claimed Capability

An assistant that says it can do things it can't (browse, remember, send) because the system prompt never said otherwise. **The system prompt lists what it can't do as clearly as what it can.**

---

## Calibration — What Good Looks Like

*ProductOS design targets — not measured industry benchmarks. Replace them with your own numbers once you have conversation data.*

| Measure | Floor | Good | Best |
| --- | --- | --- | --- |
| Turns to first specific, useful answer | 4 | 2 | 1 |
| Questions asked before first value | 3 | 1 | 0–1 |
| Greeting length | 80 words | 40 words | 25 words |
| Starters that produce a strong answer in testing | half | all | all, tested every prompt change |
| Conversations that reach a second user message | a third | half | most |
| Users who return for a second conversation within a week | your baseline | rising | rising after each prompt change |

If users drop after the first exchange, the fix is almost always the first answer's specificity or the greeting's scope — not more features. Re-read principles #1 and #2.

---

## Closing — The One Mental Model That Beats Everything

> **Imagine the user pasting the same first message into the general assistant they already use. Your first answer has to be visibly better — more specific, more useful, more theirs. If it isn't, nothing else in the flow matters; if it is, the rest is keeping the conversation going.**

The best chat assistants feel like talking to someone who already knows the job. One clear scope, one great first answer, one reason to come back.
