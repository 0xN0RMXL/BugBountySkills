# SKILL: API Authorization Bypass (BOLA/BFLA)
## Version: 1.0 | Domain: api | Trigger: API MODE + authz

---

## IDENTITY
Authorization flaws are the #1 API vulnerability. BOLA (Broken Object-Level Auth) = horizontal IDOR. BFLA (Broken Function-Level Auth) = vertical privilege escalation.

## DETECTION
1. Identify every endpoint with an ID parameter.
2. Log in as User A, note their IDs. Replay requests with User B's IDs.
3. For BFLA: identify admin-only endpoints (via docs/JS/introspection). Call them as regular user.

## EXPLOITATION
```http
# BOLA
GET /api/v1/orders/12345       # own order
GET /api/v1/orders/12346       # other user's order → if 200 = BOLA

# BFLA
GET /api/v1/admin/users        # admin-only
DELETE /api/v1/users/other_id  # destructive admin action
POST /api/v1/users/promote     # role escalation
PATCH /api/v1/settings/global  # tenant-wide config
```

### UUID prediction
- UUIDv1 contains timestamp + MAC → predict adjacent UUIDs.
- UUIDv4 is random — but often leaked in other responses or error messages.

### Parameter pollution for authz bypass
```http
GET /api/orders?user_id=victim_id&user_id=attacker_id
```

## PAYLOADS
(behavioral — ID substitution)

## BYPASS TECHNIQUES
- Wrap ID in array: `{"id": ["victim_id"]}`.
- Nested object: `{"user": {"id": "victim_id"}}`.
- GraphQL alias batching to enumerate.
- JSON vs form body (different parsers → different authz).

## CHAIN POTENTIAL
BOLA → mass PII dump. BFLA → admin → tenant takeover.

## TOOLS
Autorize (Burp), AuthMatrix, custom Burp macros.

## SEVERITY
BOLA: 7.5–8.5. BFLA: 9.0+.

## REFERENCES
OWASP API Top 10 — API1 BOLA, API5 BFLA
