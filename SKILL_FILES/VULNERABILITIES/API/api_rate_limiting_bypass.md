# SKILL: API Rate-Limiting Bypass
## Version: 1.0 | Domain: api

---

(See WEB/rate_limiting_bypass.md for full content — API-specific patterns below)

## API PATTERNS
- API key rate-limit per key → register multiple free keys.
- OAuth token rate-limit → rotate refresh tokens.
- GraphQL batching aliases → 100 queries in 1 HTTP request (see graphql_attacks.md).
- JSON body array → `[{"action":"transfer"}, {"action":"transfer"}, ...]` bypasses per-request limit.
- HTTP/2 multiplexing → single-packet N requests arrive simultaneously before counter increments.
- API gateway route-based limit (`/api/v1/x` limited, `/api/v1/x/` not).

## TOOLS
Turbo Intruder, fireprox, custom scripts.

## SEVERITY
Depends on chained action.
