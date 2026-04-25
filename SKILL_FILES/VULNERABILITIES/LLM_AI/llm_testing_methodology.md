# SKILL: LLM Security Testing Methodology
## Version: 1.0 | Domain: llm

---

## CHECKLIST
- [ ] **System prompt extraction** — try 10+ techniques to extract system prompt.
- [ ] **Direct prompt injection** — override system behavior via user input.
- [ ] **Indirect prompt injection** — if LLM reads external data (web, email, docs).
- [ ] **Jailbreaking** — DAN, role-play, encoding, multi-turn escalation.
- [ ] **Data exfiltration** — markdown image rendering, link injection, tool abuse.
- [ ] **Tool/plugin abuse** — SSRF, SQLi, email send, file write via tools.
- [ ] **RAG poisoning** — if shared knowledge base exists.
- [ ] **Authorization bypass** — can user A see user B's conversations?
- [ ] **Rate limiting** — can you exhaust tokens/budget?
- [ ] **Output handling** — does frontend render LLM output as HTML? (XSS via LLM)
- [ ] **Training data extraction** — can you make model regurgitate training data?
- [ ] **Model confusion** — multi-model systems: trick routing layer.

## TOOLS
- Garak (LLM vulnerability scanner)
- promptfoo (prompt testing framework)
- rebuff (prompt injection detection testing)
- Custom scripts with OpenAI/Anthropic/local model APIs

## REPORTING
- Show exact prompt + response.
- Demonstrate real-world impact (data leak, unauthorized action, financial cost).
- Note which model version and temperature.

## REFERENCES
OWASP LLM Top 10 • AI Village resources • Anthropic red-teaming guidelines
