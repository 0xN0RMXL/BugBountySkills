# SKILL: LLM Supply Chain Attacks
## Version: 1.0 | Domain: llm

---

## IDENTITY
LLM supply chain: model weights, training data, fine-tuning datasets, plugins, embeddings, vector DBs, model hosting infra.

## ATTACK VECTORS
- **Malicious model weights** — Hugging Face model with backdoor (triggers on specific input).
- **Poisoned fine-tuning data** — RLHF data manipulated to make model compliant to jailbreaks.
- **Dependency confusion** — `pip install transformers-evil` (typosquat).
- **Serialized model exploit** — `pickle.load` on model file → RCE.
- **Plugin marketplace** — malicious plugin approved; exfils data on first use.

## DETECTION
- Verify model checksums against official releases.
- Scan for pickle/joblib deserialization in model loading code.
- Audit plugin permissions and OAuth scopes.

## REFERENCES
OWASP LLM Top 10 — LLM05 Supply Chain Vulnerabilities
