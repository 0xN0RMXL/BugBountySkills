# SKILL: AI Model Extraction / Stealing
## Version: 1.0 | Domain: llm

---

## IDENTITY
Model extraction = querying an API enough to replicate the model's behavior locally. Valuable for proprietary models.

## TECHNIQUES
- **Query-based extraction** — systematically query model to build training data for a clone.
- **Side-channel** — timing differences reveal model architecture / size.
- **Logit extraction** — if API returns logprobs, extract full probability distribution → train clone.
- **Embedding theft** — API returns embedding vectors → reconstruct embedding model.
- **Hyperparameter inference** — query patterns reveal temperature, top_p, model family.

## DETECTION
- Look for excessive API usage patterns.
- Rate-limit + monitor for systematic enumeration.

## CHAIN POTENTIAL
Model extraction → understand model behavior → craft better adversarial inputs → bypass safety.

## REFERENCES
Tramèr et al. "Stealing Machine Learning Models via Prediction APIs"
