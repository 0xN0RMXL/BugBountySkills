---
vuln_type: "Path_Traversal"
file_type: "cheatsheet"
total_reports: "166"
avg_bounty: "3000"
max_bounty: "6000"
severity_distribution: "critical:6% high:7% medium:86% low:1%"
owasp_categories: ["A01:2021"]
common_cwe: ["CWE-22"]
last_updated: "2026-04-09"
tags: ["Path_Traversal", "web", "api", "A01", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---
# Path Traversal Cheatsheet
## Top 5 Payloads
```javascript
/etc/hosts\n/etc/passwd\n/etc/shadow\n<script>alert(1)</script>\n<script>alert(1)</script>
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
> "This Path_Traversal vulnerability allows an attacker to subvert execution bounds, resulting in severe compromise."
## Key Files
[[README]] | [[payloads]] | [[hunting-methodology]] | [[bypasses]]
