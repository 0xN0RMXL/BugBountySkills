# SKILL: API Versioning Attacks
## Version: 1.0 | Domain: api

---

## IDENTITY
Old API versions often lack security fixes, rate limits, and auth enforcement applied to the latest version.

## DETECTION
```bash
for v in v0 v1 v2 v3 v4 v5 beta internal legacy old dev staging test; do
  curl -sk -o /dev/null -w "$v: %{http_code}\n" "https://target/api/$v/users"
done
```

Also check: `Accept: application/vnd.api.v1+json` header-based versioning.

## EXPLOITATION
- `/api/v1/users` returns all users (no pagination, no auth) while `/api/v3/users` has proper pagination + auth.
- `/api/v2/password/reset` has no rate limit.
- `/api/v1/upload` accepts any file type while v3 restricts.

## CHAIN POTENTIAL
Old version → data dump / authz bypass → ATO.

## SEVERITY
Depends on the gap (7.0–9.0).

## REFERENCES
OWASP API Top 10 — API9 Improper Inventory Management
