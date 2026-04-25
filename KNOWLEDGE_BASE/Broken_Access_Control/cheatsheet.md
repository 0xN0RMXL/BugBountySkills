---
vuln_type: "Broken_Access_Control"
file_type: "cheatsheet"
total_reports: "470"
avg_bounty: "1128"
max_bounty: "10000"
severity_distribution: "critical:10% high:10% medium:10% low:70%"
owasp_categories: ["A01:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["Broken_Access_Control", "web", "api", "A01", "hunter-kb"]
related_vulns: ["Information_Disclosure", "SSRF"]
---
# Broken Access Control Cheatsheet
## Top 5 Payloads
```javascript
://hackers.upchieve.org/\n`
POST /graphql HTTP/2
Host: hackerone.com
Cookie: y...\n{"operationName":"LockReport","variables":{"product_...\nPOST /AJAXUtilities.aspx HTTP/1.1
Host: ████████
Con...\ncurl --insecure https://52.90.28.77:30920/reddit --h...
```
## Attack Surfaces
- Search functionality\n- Authentication\n- Admin/management
## Quick Test
1. Inject a benign token to enumerate bounds.
2. Append special control characters sequentially.
## Top 3 Bypasses
- Bypass\n- Filter/WAF bypass\n- Circumvention
## Indicators
- Reflection appearing outside standard bounds
## Impact Template
> "This Broken_Access_Control vulnerability allows an attacker to subvert execution bounds, resulting in severe compromise."
## Key Files
[[README]] | [[payloads]] | [[hunting-methodology]] | [[bypasses]]
