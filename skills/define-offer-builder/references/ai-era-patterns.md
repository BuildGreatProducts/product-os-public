# AI-era offer patterns

> **Last reviewed October 2026 — refresh via live research before relying on any of it.** The AI space moves quickly: the underlying shapes tend to be durable, but named products, prices, valuations, and revenue figures date fast. Re-verify any figure with a web search before quoting it to the member, and cite the source you found next to it.

## Contents

- [Customer wedges that are working](#customer-wedges-that-are-working)
- [Wedges that struggle](#wedges-that-struggle)
- [Mechanism patterns that signal real moat](#mechanism-patterns-that-signal-real-moat)
- [Guarantee patterns for AI buyer fears](#guarantee-patterns-for-ai-buyer-fears)
- [AI-specific failure modes to flag](#ai-specific-failure-modes-to-flag)
- [Calibration examples (AI-era offers in the wild)](#calibration-examples-ai-era-offers-in-the-wild)

## Customer wedges that are working

- **Vertical AI for regulated professionals** — legal (Harvey-shape), medical scribing, tax & accounting, compliance. Highest ceiling; defended by workflow depth + regulatory posture.
- **AI coding/dev tools** — Cursor, Lovable, Bolt.new shape. The biggest breakouts of 2025–2026; defended by editor integration and multi-model routing.
- **Prosumer creator tools with a sharp visual demo** — HeadshotPro, PhotoAI, Submagic shape. Distribution via TikTok/X; defended by audience + fine-tuned models.
- **Job-to-be-done agents** — Granola (meeting notes), Fin (support resolutions), AI SDR/outbound, code review agents. Defended by workflow integration and outcome-based pricing.
- **"Boring back office" agents** — invoice/AP, audit, compliance docs. Outperforms flashy consumer wrappers; defended by integration depth.

## Wedges that struggle

- Horizontal "AI assistant for everyone" — gets eaten by ChatGPT / Claude / Gemini.
- Thin wrappers on a single prompt — replaced by the next foundation-model UI release.
- Consumer chat without a defended channel — saturated.
- Generic productivity wrappers competing with native foundation-model features.

## Mechanism patterns that signal real moat

"AI-powered" or "uses <the latest model>" is a feature label every wrapper claims, not a mechanism. Credible AI-era mechanisms layer at least one of:

- Proprietary data + RAG (retrieval-augmented generation) over it.
- Vertical fine-tuning.
- Multi-model routing — so a model deprecation is a config change, not a rebuild.
- Deterministic + probabilistic hybrids — rules wrapped around LLM calls for accuracy-critical work.
- Agentic loops with checkpointing.
- Integration depth into the customer's workflow.
- Audience / distribution as moat.

## Guarantee patterns for AI buyer fears

The fears: hallucination tax, model deprecation, regulatory exposure (HIPAA / GDPR / SOC2), unbounded cost. Guarantees that name one explicitly:

- Outcome-based pricing — e.g. Fin's $0.99 per resolved ticket.
- BYOK (bring your own key) with no markup.
- Named compliance posture in the SLA.
- Soft caps with overage transparency.
- Replay / audit logs.

## AI-specific failure modes to flag

- **Foundation-model absorption** — Jasper-shape risk. The next model release eats the feature.
- **Model deprecation churn** — products without a routing abstraction take engineering hits every quarter (in 2026 alone OpenAI retired GPT-4o, 4.1, 4.1-mini, o4-mini and the Assistants API).
- **Hallucination tax** — survivors invest in verification UX, confidence scoring, human-in-the-loop checkpoints.
- **Regulatory exposure** — HIPAA / GDPR / SOC2 / PII. Healthcare/legal/tax wrappers without compliance posture stall at procurement.
- **ARR trust collapse** — the AI category is already credibility-shaky; founders who misreport revenue or capabilities get punished faster than in traditional SaaS.

## Calibration examples (AI-era offers in the wild)

Use when the member's offer needs a calibration anchor and the pre-AI examples in `BONUS-Product-Offer-Examples.md` don't fit. Proof figures are as publicly reported up to October 2026; their original sources weren't recorded, so re-verify each with a web search (and note the source) before quoting it.

- **Cursor.** Customer: working engineers. Pain: context-switching out of the editor to LLMs. Outcome: AI in the IDE. Mechanism: deep editor integration + multi-model routing. Proof: reported ~$2B ARR, ~$50B valuation talks.
- **Granola.** Customer: people in back-to-back meetings. Pain: bot note-takers are intrusive. Outcome: raw notes made awesome. Mechanism: no-bot capture + MCP integrations. Proof: reported $1.5B valuation, $125M raise.
- **Harvey.** Customer: lawyers at large firms. Pain: associate-hour-intensive doc work. Outcome: agents that draft, review, research. Mechanism: vertical legal RAG + workflow depth + compliance posture. Proof: reported 1,300 firms, ~100K lawyers, ~$190M ARR.
- **Fin (Intercom).** Customer: support teams. Outcome: deflected tickets. Mechanism: agent on top of helpdesk. Guarantee: pay only on successful resolution ($0.99). Proof: reported 8,000 companies, ~2M resolutions/week.
- **HeadshotPro.** Customer: knowledge workers needing a LinkedIn photo. Outcome: pro headshots without a studio. Mechanism: fine-tuned image models + delivery UX. Proof: $3.6M ARR per the founder's public revenue dashboard, solo.
