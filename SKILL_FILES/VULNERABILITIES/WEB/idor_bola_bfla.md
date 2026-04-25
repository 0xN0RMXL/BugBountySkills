# SKILL: IDOR / BOLA / BFLA (Insecure Direct Object Reference / Broken Object/Function Level Auth)

## Version: 1.0 | Domain: web | Trigger: `WEB MODE` + (idor / bola / bfla (insecure direct object reference / broken object/function level auth)) or pasted request matching this class

---

## IDENTITY IN THIS SKILL
The most common high-bounty class in modern APIs. I substitute IDs (numeric, UUID, hash) and observe 200 vs 403.

---

## DETECTION
1. Map all endpoints with `:id` or `userId=` style.
2. With user A's session, replace ID with user B's ID. Compare response.
3. Try: increment numeric IDs, predict UUIDs (UUIDv1 leaks MAC + time → predict), substitute admin's ID, use former IDs (deleted accounts often still resolve).
4. Method swap: `GET /api/users/123` works but `PUT /api/users/123` should be admin-only — try as user.

## EXPLOITATION
- Direct ID swap: `/api/orders/12345` → `/api/orders/12346`.
- UUID brute via timing oracle (UUIDv1) or predictable shape.
- Sequential ID in JSON body: `{"userId": 1}` → `{"userId": 2}`.
- Hidden parameter inject: `{"userId": 123, "isAdmin": true}` (mass assignment).
- Method bypass: `PUT /api/users/123/role` not exposed in UI but routed.
- Plural collection: `GET /api/users?ids=1,2,3,4,5,6,7,8,9,10`.

## PAYLOADS (real, copy-paste, grouped)
```http
GET /api/users/<other_id>          # vertical IDOR
GET /api/orders/<other_user_order> # horizontal IDOR
GET /api/users/me                  # often "me" alias works for IDs
GET /api/users/me/../<other_id>    # traversal-style
GET /api/users.json?id[]=1&id[]=2  # array param
GET /api/admin/users/<id>          # method/path confusion
PATCH /api/users/<id> {"role":"admin"}  # BFLA + mass assignment
```

## BYPASS TECHNIQUES
- 403 on numeric ID → try UUID, base64-encoded ID, hash.
- 403 on direct path → query string version.
- 403 on JSON body → form body, XML body.
- 403 on `GET` → `POST` with method override `_method=GET` or `X-HTTP-Method-Override: GET`.
- IDs encoded in JWT — re-sign or alg=none if JWT vuln present (see jwt_attacks.md).

## CHAIN POTENTIAL
IDOR → admin object access → BFLA on admin endpoint → tenant takeover.

## TOOLS
Autorize (Burp), AuthMatrix, Burp Repeater + extensions

## COMMANDS
```bash
# Burp Autorize: log in as user A, set unauthorized headers to user B's, browse — extension flags every endpoint that returns the same to both.
```

## EDGE CASES / NOT-A-BUG TRAPS
Public profile data accessible by ID is by design. Triagers look for sensitive data (PII, payment, settings).

## TRIAGE ANGLE (per platform)
Show user A obtaining user B's PII / settings / actions. Crisp screenshot.

## SEVERITY & CVSS
Horizontal: 6.5–8.5; Vertical (BFLA): 9.0+.

## REFERENCES
OWASP API Top 10 — API1 BOLA, API5 BFLA • PortSwigger IDOR
