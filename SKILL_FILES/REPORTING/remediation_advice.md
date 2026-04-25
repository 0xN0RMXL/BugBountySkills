# SKILL: Remediation Advice
## Version: 1.0 | Domain: reporting

---

## RULE
Specific. Actionable. Library-pinned. Reference upstream docs.

## TEMPLATES — by class

### XSS
- Encode user output for the correct context (HTML body, attribute, JS string, URL).
- Use the framework's auto-escape (`html/template` in Go, `Twig`, `Jinja2` autoescape, React JSX text nodes).
- For rich text: sanitize with DOMPurify v3 (config: ALLOWED_TAGS=['b','i','a',...] without `script/iframe/object/embed`).
- CSP with `script-src 'self' 'nonce-{random}'` and `object-src 'none'` and `base-uri 'self'`.

### SQLi
- Parameterized queries / prepared statements.
- ORM with bound params (Sequelize `:`, SQLAlchemy `:x`, Hibernate `?`, Eloquent ::raw avoided).
- Stored procedures with parameters (not concat).
- Allow-list for ORDER BY / LIMIT (numeric only).

### IDOR
- `req.user.id == resource.owner_id` check on every read/write.
- Indirect references (UUIDs scoped to user) instead of integer IDs.
- Permission middleware that runs on every controller method.

### SSRF
- Strict allow-list of domains.
- DNS rebinding mitigation: resolve once, validate, use IP for the request.
- Block private IP ranges: 10/8, 172.16/12, 192.168/16, 127/8, 169.254/16, ::1, fc00::/7, fe80::/10.
- IMDSv2 enforced (httpPutResponseHopLimit=1, RequireToken=true).

### CSRF
- SameSite=Strict / Lax (Lax + state-change-on-GET = re-evaluate)
- Double-submit token bound to session
- Custom header (X-CSRF-Token) checked server-side

### Auth bypass
- Cite specific code path.
- Verify session ID is regenerated on login.
- Lock account after N failed attempts (with reasonable threshold).

### Subdomain takeover
- Remove dangling CNAME entries.
- Use AWS Route53 alias to S3 bucket only, not bare CNAME.
- Monitor with subdomain takeover scanner in CI.

### JWT
- Use library that validates `alg` against allow-list (`HS256` or `RS256` only).
- Reject `none`, reject mismatched alg vs key type.
- Use `kid` only with strict path validation.
- Use `aud`, `iss`, `nbf`, `exp` validation.
- Rotate signing keys; revocation list / short TTL.

## REFERENCES
OWASP Cheat Sheet Series, NIST 800-63B (auth)
