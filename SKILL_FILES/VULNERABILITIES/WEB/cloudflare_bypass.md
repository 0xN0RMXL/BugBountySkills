# SKILL: Cloudflare Bypass — Origin IP + WAF

## Version: 1.0 | Domain: web | Trigger: `WEB MODE` + (cloudflare bypass — origin ip + waf) or pasted request matching this class

---

## IDENTITY IN THIS SKILL
Two angles: find origin IP (best, total bypass) or beat the WAF rules (fragile).

---

## DETECTION
`Server: cloudflare`, `cf-ray`, cookies `__cf_bm`, `__cfuid`.

## EXPLOITATION
### Origin discovery
1. SecurityTrails historical A records for the apex.
2. Cert SAN match on Shodan/Censys outside CF ranges (`ssl:"target.com" -country:US -org:cloudflare`).
3. Favicon hash match outside CF ranges.
4. MX records (mail server often sits next to web origin).
5. `dnsdumpster`, `viewdns reverse-IP`.
6. Subdomain hosting on third-party PaaS that doesn't use CF (e.g., Heroku) often shares same backend cluster IP block.
7. SSRF on the target itself reveals internal IP via error pages.
8. `ssl-cert-grabber-by-asn` (find cert hosted on AWS/GCP IP that was once target's).

### Once IP is found
Add `Host:` header override:
```bash
curl -sk --resolve target.com:443:<ORIGIN_IP> https://target.com/
```
or
```bash
curl -sk -H "Host: target.com" https://<ORIGIN_IP>/
```

### Cloudflare WAF rule bypass (when you can't find origin)
- HTML5 events not in default ruleset (`<svg/onload>`, `<details ontoggle>`)
- Inline event payload split via newline
- Fragmentation across body
- Multipart with file body containing payload + Content-Type confusion
- HTTP/2 smuggling
- 0x0c null byte / unicode whitespace in payload
- Empty body POST with payload in header (X-Forwarded-For SQLi etc.)
- WebSocket upgrade then send arbitrary content

## PAYLOADS (real, copy-paste, grouped)
(see PAYLOADS/waf_bypass_payloads.md)

## BYPASS TECHNIQUES
(see exploitation)

## CHAIN POTENTIAL
Origin IP discovery → bypass all WAF rules globally for this engagement.

## TOOLS
CloudFail, ip-locator, cloudflare-resolver, fav-up

## COMMANDS
```bash
python3 CloudFail.py -t target.com
fav-up -u target.com
```

## EDGE CASES / NOT-A-BUG TRAPS
Some targets force connection through CF via mTLS — origin won't accept direct.

## TRIAGE ANGLE (per platform)
Show direct origin response with target content.

## SEVERITY & CVSS
Same as underlying bug + fact that WAF was bypassed.

## REFERENCES
Bypassing Cloudflare WAF in Bug Bounty Programs (uploaded) • Christian Haschek's articles
