# SKILL: LLM Denial of Service
## Version: 1.0 | Domain: llm

---

## TECHNIQUES
- **Prompt flooding** — send max-length input → consume tokens/GPU.
- **Recursive generation** — prompt that causes model to loop (e.g., "repeat the following 1000 times").
- **Resource exhaustion via tool calls** — prompt model to call expensive tools repeatedly.
- **Context window exhaustion** — fill context with junk, leaving no room for useful output.
- **Regex / parsing DoS** — if input goes through regex pre-processing, ReDoS payloads.
- **Batch API abuse** — submit thousands of concurrent requests.

## CHAIN POTENTIAL
DoS → financial cost (pay-per-token APIs) → budget exhaustion.

## REFERENCES
OWASP LLM Top 10 — LLM04 Model Denial of Service
