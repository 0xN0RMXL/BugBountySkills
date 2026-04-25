# SKILL: WAF Bypass — All Techniques

## Version: 1.0 | Domain: web | Trigger: `WEB MODE` + (waf bypass — all techniques) or pasted request matching this class

---

## IDENTITY IN THIS SKILL
WAF is a signature engine. I outflank by encoding, fragmentation, parameter pollution, HTTP/2 differential, body-size oversized, request smuggling, and origin discovery.

---

## DETECTION
Identify WAF (wafw00f, headers, cookies, block-page fingerprint). Each WAF has known bypass tier.

## EXPLOITATION
(see SEC: WAF tiers below)

## PAYLOADS (real, copy-paste, grouped)
(see PAYLOADS/waf_bypass_payloads.md)

## BYPASS TECHNIQUES
### Encoding
- URL: `%3C` `%253C` `%2525...`
- HTML entity: `&lt;` `&#x3c;` `&#60;`
- Unicode: `\u003c` `\x3c`
- UTF-7: `+ADw-`
- UTF-16 BOM
- HTTP/0.9 throwback (WAF doesn't parse)

### Fragmentation
- HTTP Parameter Pollution: `?q=harm&q=<svg>`
- Body chunking — split payload across chunks
- Multipart MIME variants

### Headers
- `Transfer-Encoding: chunked` smuggling
- HTTP/2 lone-pseudo
- Trailing whitespace in header name (WAF normalizes, server doesn't)

### Origin discovery (best long-term bypass)
- Find origin IP behind WAF (cert SAN match on Shodan / favicon hash / SecurityTrails historical A) → hit origin directly.

### Method
- `GET → POST` swap if WAF only inspects GET
- `OPTIONS` / `TRACE` / WebDAV methods

### Timing
- Slow drip — submit one byte per second
- Connection reuse abuse

### Body size
- WAF inspects first N bytes; pad with junk before payload (AWS WAF default 8KB)

### Case
- `<ScRiPt>`, `SeLeCt`

### Whitespace
- `%09 %0a %0b %0c %0d %a0` between tokens

### Comments
- SQL: `/**/`
- HTML: `<!---->`

## CHAIN POTENTIAL
Bypass WAF → land XSS / SQLi / RCE in upstream that didn't expect to be reached.

## TOOLS
wafw00f, Hackvertor (Burp), nowafpls

## COMMANDS
```bash
wafw00f https://target
nowafpls   # Burp ext: appends junk to bypass body inspection size
```

## EDGE CASES / NOT-A-BUG TRAPS
Vendor patches happen daily. Always start with origin discovery — fundamental win.

## TRIAGE ANGLE (per platform)
Show WAF block, then your bypassed payload landing.

## SEVERITY & CVSS
Same as the underlying bug.

## REFERENCES
Bypassing Cloudflare WAF in Bug Bounty Programs (uploaded) • PortSwigger WAF research
