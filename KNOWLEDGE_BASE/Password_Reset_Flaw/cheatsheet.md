---
vuln_type: "Password_Reset_Flaw"
file_type: "cheatsheet"
total_reports: "55"
avg_bounty: "0"
max_bounty: "0"
severity_distribution: "critical:0% high:0% medium:0% low:100%"
owasp_categories: ["A00:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["Password_Reset_Flaw", "web", "api", "A00", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---
# Password Reset Flaw Cheatsheet
## Top 5 Payloads
```javascript
<script>alert(1)</script>\n<script>alert(1)</script>\n<script>alert(1)</script>\n<script>alert(1)</script>\n<script>alert(1)</script>
```
## Attack Surfaces
- Search functionality\n- Authentication\n- Export/download
## Quick Test
1. Inject a benign token to enumerate bounds.
2. Append special control characters sequentially.
## Top 3 Bypasses
- Bypass\n- Standard framework specific encoding\n- Standard framework specific encoding
## Indicators
- Reflection appearing outside standard bounds
## Impact Template
> "This Password_Reset_Flaw vulnerability allows an attacker to subvert execution bounds, resulting in severe compromise."
## Key Files
[[README]] | [[payloads]] | [[hunting-methodology]] | [[bypasses]]
