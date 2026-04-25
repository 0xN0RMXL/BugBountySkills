---
vuln_type: "XSS"
file_type: "cheatsheet"
total_reports: "1563"
avg_bounty: "424"
max_bounty: "3800"
severity_distribution: "critical:1% high:2% medium:97% low:0%"
owasp_categories: ["A03:2021"]
common_cwe: ["CWE-79", "CWE-80"]
last_updated: "2026-04-09"
tags: ["XSS", "web", "api", "A03", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---
# XSS Cheatsheet
## Top 5 Payloads
```javascript
document.domain\nalert(document.domain)\nalert(1)\n<img src=x onerror=\njavascript:alert(
```
## Attack Surfaces
- Search functionality\n- Authentication\n- Export/download
## Quick Test
1. Inject a benign token to enumerate bounds.
2. Append special control characters sequentially.
## Top 3 Bypasses
- Bypass\n- Encoding technique\n- Filter/WAF bypass
## Indicators
- Reflection appearing outside standard bounds
## Impact Template
> "This XSS vulnerability allows an attacker to subvert execution bounds, resulting in severe compromise."
## Key Files
[[README]] | [[payloads]] | [[hunting-methodology]] | [[bypasses]]
