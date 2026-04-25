---
vuln_type: "Business_Logic"
file_type: "cheatsheet"
total_reports: "65"
avg_bounty: "932"
max_bounty: "2000"
severity_distribution: "critical:13% high:23% medium:20% low:44%"
owasp_categories: ["A00:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["Business_Logic", "web", "api", "A00", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---
# Business Logic Cheatsheet
## Top 5 Payloads
```javascript
.domain.com "20241107 01:02:03"
.sub.domain.com "unl...\ncurl ldap://localhost:1388
curl: result.c:930: try_r...\nFree Shipping Promo Code (pick one):
United ████: ██...\n<script>alert(1)</script>\n<script>alert(1)</script>
```
## Attack Surfaces
- Search functionality\n- Authentication\n- Export/download
## Quick Test
1. Inject a benign token to enumerate bounds.
2. Append special control characters sequentially.
## Top 3 Bypasses
- Race condition\n- Bypass\n- Encoding technique
## Indicators
- Reflection appearing outside standard bounds
## Impact Template
> "This Business_Logic vulnerability allows an attacker to subvert execution bounds, resulting in severe compromise."
## Key Files
[[README]] | [[payloads]] | [[hunting-methodology]] | [[bypasses]]
