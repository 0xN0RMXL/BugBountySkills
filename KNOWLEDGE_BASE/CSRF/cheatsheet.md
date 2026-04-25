---
vuln_type: "CSRF"
file_type: "cheatsheet"
total_reports: "289"
avg_bounty: "350"
max_bounty: "500"
severity_distribution: "critical:1% high:2% medium:4% low:93%"
owasp_categories: ["A04:2021"]
common_cwe: ["CWE-352"]
last_updated: "2026-04-09"
tags: ["CSRF", "web", "api", "A04", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---
# CSRF Cheatsheet
## Top 5 Payloads
```javascript
token\nToken\n<form action=\nSameSite\n<form  action=
```
## Attack Surfaces
- Search functionality\n- Authentication\n- Export/download
## Quick Test
1. Inject a benign token to enumerate bounds.
2. Append special control characters sequentially.
## Top 3 Bypasses
- Bypass\n- Encoding technique\n- Parameter pollution
## Indicators
- Reflection appearing outside standard bounds
## Impact Template
> "This CSRF vulnerability allows an attacker to subvert execution bounds, resulting in severe compromise."
## Key Files
[[README]] | [[payloads]] | [[hunting-methodology]] | [[bypasses]]
