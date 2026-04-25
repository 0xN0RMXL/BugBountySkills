# SKILL: iOS URL Scheme Attacks
## Version: 1.0 | Domain: mobile

---

## IDENTITY
Custom URL schemes (`target://`) can be hijacked by malicious apps (no verification unlike Universal Links).

## EXPLOITATION
```
target://login?token=ATTACKER_TOKEN
target://oauth/callback?code=STOLEN_CODE
target://settings?debug=1
```

### URL scheme hijacking
Register same scheme in malicious app → iOS may route to attacker's app (first-installed wins for non-Universal Links).

### Universal Link bypass
If app also has Universal Links but URL scheme is not disabled, bypass the verified domain check by using the custom scheme.

## REFERENCES
OWASP MASTG
