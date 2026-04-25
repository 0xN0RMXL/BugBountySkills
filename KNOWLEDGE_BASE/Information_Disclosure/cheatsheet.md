---
vuln_type: "Information_Disclosure"
file_type: "cheatsheet"
total_reports: "556"
avg_bounty: "2257"
max_bounty: "25000"
severity_distribution: "critical:7% high:6% medium:13% low:74%"
owasp_categories: ["A02:2021"]
common_cwe: ["CWE-200"]
last_updated: "2026-04-09"
tags: ["Information_Disclosure", "web", "api", "A02", "hunter-kb"]
related_vulns: ["Broken_Access_Control", "SSRF"]
---
# Information Disclosure Cheatsheet
## Top 5 Payloads
```javascript
stack trace\nphpinfo()\n.htaccess\ndebug mode\nsecret =
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
> "This Information_Disclosure vulnerability allows an attacker to subvert execution bounds, resulting in severe compromise."
## Key Files
[[README]] | [[payloads]] | [[hunting-methodology]] | [[bypasses]]
