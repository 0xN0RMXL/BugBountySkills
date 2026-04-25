---
vuln_type: "RCE"
file_type: "cheatsheet"
total_reports: "495"
avg_bounty: "411"
max_bounty: "4323"
severity_distribution: "critical:9% high:85% medium:5% low:1%"
owasp_categories: ["A03:2021"]
common_cwe: ["CWE-78", "CWE-94", "CWE-502"]
last_updated: "2026-04-09"
tags: ["RCE", "web", "api", "A03", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---
# RCE Cheatsheet
## Top 5 Payloads
```javascript
`curl\n`Curl\n`CURL\n`
curl\nchild_process
```
## Attack Surfaces
- Search functionality\n- Authentication\n- Export/download
## Quick Test
1. Inject a benign token to enumerate bounds.
2. Append special control characters sequentially.
## Top 3 Bypasses
- Bypass\n- Encoding technique\n- Race condition
## Indicators
- Reflection appearing outside standard bounds
## Impact Template
> "This RCE vulnerability allows an attacker to subvert execution bounds, resulting in severe compromise."
## Key Files
[[README]] | [[payloads]] | [[hunting-methodology]] | [[bypasses]]
