---
vuln_type: "Open_Redirect"
file_type: "cheatsheet"
total_reports: "198"
avg_bounty: "800"
max_bounty: "800"
severity_distribution: "critical:1% high:0% medium:3% low:96%"
owasp_categories: ["A03:2021"]
common_cwe: ["CWE-601"]
last_updated: "2026-04-09"
tags: ["Open_Redirect", "web", "api", "A03", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---
# Open Redirect Cheatsheet
## Top 5 Payloads
```javascript
url=http://\nnext=//\nurl=https://\nnext=http://\nurl=//
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
> "This Open_Redirect vulnerability allows an attacker to subvert execution bounds, resulting in severe compromise."
## Key Files
[[README]] | [[payloads]] | [[hunting-methodology]] | [[bypasses]]
