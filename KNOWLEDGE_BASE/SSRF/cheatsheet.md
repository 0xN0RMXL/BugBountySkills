---
vuln_type: "SSRF"
file_type: "cheatsheet"
total_reports: "214"
avg_bounty: "2954"
max_bounty: "4263"
severity_distribution: "critical:4% high:91% medium:5% low:0%"
owasp_categories: ["A10:2021"]
common_cwe: ["CWE-918"]
last_updated: "2026-04-09"
tags: ["SSRF", "web", "api", "A10", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control"]
---
# SSRF Cheatsheet
## Top 5 Payloads
```javascript
http://127.0.0\nlatest/meta-data\n169.254.169.254\nhttp://169.254\nurl=http://
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
> "This SSRF vulnerability allows an attacker to subvert execution bounds, resulting in severe compromise."
## Key Files
[[README]] | [[payloads]] | [[hunting-methodology]] | [[bypasses]]
