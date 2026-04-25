---
vuln_type: "Cache_Poisoning"
file_type: "cheatsheet"
total_reports: "17"
avg_bounty: "0"
max_bounty: "0"
severity_distribution: "critical:0% high:0% medium:0% low:100%"
owasp_categories: ["A00:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["Cache_Poisoning", "web", "api", "A00", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---
# Cache Poisoning Cheatsheet
## Top 5 Payloads
```javascript
X-Forwarded-Host: your_hackerz_site.com\nyour_hackerz_site.com\nX-Forwarded-Host\nGET /test.js?cb=1 HTTP/2
Host: design.glassdoor.com
...\n-Forwarded-Host
```
## Attack Surfaces
- Search functionality\n- Authentication\n- Export/download
## Quick Test
1. Inject a benign token to enumerate bounds.
2. Append special control characters sequentially.
## Top 3 Bypasses
- Encoding technique\n- Standard framework specific encoding\n- Standard framework specific encoding
## Indicators
- Reflection appearing outside standard bounds
## Impact Template
> "This Cache_Poisoning vulnerability allows an attacker to subvert execution bounds, resulting in severe compromise."
## Key Files
[[README]] | [[payloads]] | [[hunting-methodology]] | [[bypasses]]
