# SKILL: Burp Suite Automation
## Version: 1.0 | Domain: automation

---

## ESSENTIAL EXTENSIONS
- Autorize (authz testing)
- Param Miner (hidden params + cache poisoning)
- HTTP Request Smuggler (PortSwigger)
- Active Scan++
- Backslash Powered Scanner
- Turbo Intruder (race conditions, fast brute)
- JSON Web Tokens (jwt manipulation)
- AuthMatrix
- DOM Invader (built-in)
- Hackvertor (encoding chains)
- BurpJSLinkFinder
- JS Miner
- BApp Param Auth Test
- Burp Bounty (custom rules)
- Software Vulnerability Scanner
- 403 Bypasser
- Logger++

## BURP REST API (PRO)
```bash
# Burp listens on http://127.0.0.1:1337 (config in User options → Misc)
# Trigger active scan
curl -X POST 'http://127.0.0.1:1337/v0.1/scan' -d '{"urls":["https://target.com"]}' -H 'Content-Type: application/json'
```

## SESSION HANDLING RULES
- Auto-relogin macros for long-running scans
- CSRF token refresh
- Header injection (e.g., custom auth)

## INTRUDER PRESETS
- Cluster bomb for credential stuffing
- Sniper for single-param fuzz
- Pitchfork for paired wordlists

## TURBO INTRUDER TEMPLATES
- race-single-packet-attack
- examples/many-requests
- ssrf-mass-test

## REFERENCES
PortSwigger Burp docs, BApp store
