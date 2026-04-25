---
vuln_type: "Hardcoded_Credentials"
file_type: "cheatsheet"
total_reports: "39"
avg_bounty: "0"
max_bounty: "0"
severity_distribution: "critical:0% high:0% medium:0% low:100%"
owasp_categories: ["A00:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["Hardcoded_Credentials", "web", "api", "A00", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---
# Hardcoded Credentials Cheatsheet
## Top 5 Payloads
```javascript
password=admin
username=admin\npassword=admin username=admin\n<script>alert(1)</script>\n<script>alert(1)</script>\n<script>alert(1)</script>
```
## Attack Surfaces
- Search functionality\n- Authentication\n- Export/download
## Quick Test
1. Inject a benign token to enumerate bounds.
2. Append special control characters sequentially.
## Top 3 Bypasses
- Bypass\n- Case variation\n- Standard framework specific encoding
## Indicators
- Reflection appearing outside standard bounds
## Impact Template
> "This Hardcoded_Credentials vulnerability allows an attacker to subvert execution bounds, resulting in severe compromise."
## Key Files
[[README]] | [[payloads]] | [[hunting-methodology]] | [[bypasses]]
