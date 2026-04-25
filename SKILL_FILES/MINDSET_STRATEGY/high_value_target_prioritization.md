# SKILL: High-Value Target Prioritization
## Version: 1.0 | Domain: mindset

---

## ENDPOINTS THAT PAY MOST
- Authentication / authorization endpoints
- Payment / billing
- Admin panels
- File upload / file processing
- API integrations (OAuth callbacks, webhooks)
- Email / SMS sending
- Internal admin / debug endpoints accidentally exposed
- GraphQL / REST endpoints with rich query language
- Endpoints handling other users' data (DM, comments, sharing)

## PARAMETERS WORTH FUZZING
- `id`, `user`, `account`, `org`, `tenant`
- `redirect`, `next`, `return`, `callback`, `url`
- `file`, `path`, `template`, `view`
- `cmd`, `exec`, `eval`, `script`
- `query`, `search`, `q`, `filter`
- `email`, `username`, `name`
- `role`, `permission`, `is_admin`, `verified`
- `_method`, `_csrf`, `_token`
- `format`, `output`, `type`

## QUERY-STRING MINING
- Use Param Miner (Burp), Arjun, x8 to find hidden params.
- Try every interesting param against every endpoint.

## RESPONSE PATTERNS THAT INDICATE BUG-RICHNESS
- Stack traces in error responses
- Verbose error messages (e.g., "User with ID 123 not found")
- Backend service names in headers (X-Powered-By, X-Backend)
- Long `Set-Cookie` lists
- Exposed `/api/swagger.json`, `/openapi.json`, `/graphql` (introspection on)
- Endpoints returning 500 on edge cases

## REFERENCES
zseanos-methodology.pdf, Bug Hunters Methodology Day 2
