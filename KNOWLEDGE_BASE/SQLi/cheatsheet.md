---
vuln_type: "SQLi"
file_type: "cheatsheet"
total_reports: "187"
avg_bounty: "1625"
max_bounty: "4263"
severity_distribution: "critical:8% high:89% medium:3% low:0%"
owasp_categories: ["A03:2021"]
common_cwe: ["CWE-89"]
last_updated: "2026-04-09"
tags: ["SQLi", "web", "api", "A03", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---
# SQLi Cheatsheet
## Top 5 Payloads
```javascript
sqlmap\nSQLMap\ninformation_schema\nsleep(10)\nSLEEP(15)
```
## Attack Surfaces
- Search functionality\n- Authentication\n- Export/download
## Quick Test
1. Inject a benign token to enumerate bounds.
2. Append special control characters sequentially.
## Top 3 Bypasses
- Bypass\n- Encoding technique\n- Standard framework specific encoding
## Indicators
- Reflection appearing outside standard bounds
## Impact Template
> "This SQLi vulnerability allows an attacker to subvert execution bounds, resulting in severe compromise."
## Key Files
[[README]] | [[payloads]] | [[hunting-methodology]] | [[bypasses]]
