---
vuln_type: "API_Security"
file_type: "cheatsheet"
total_reports: "409"
avg_bounty: "1022"
max_bounty: "2162"
severity_distribution: "critical:0% high:2% medium:3% low:95%"
owasp_categories: ["A00:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["API_Security", "web", "api", "A00", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---
# API Security Cheatsheet
## Top 5 Payloads
```javascript
-consumer_key\nhttps://████████/rest/api/2/user/picker?query=\ncurl -u "RANDOM1:RANDOM2" -X PROPFIND https://server...\n/ocs/v2.php/apps/spreed/api/v1/chat/$token/share\n://████████/███/?#/
```
## Attack Surfaces
- Search functionality\n- Authentication\n- API endpoint
## Quick Test
1. Inject a benign token to enumerate bounds.
2. Append special control characters sequentially.
## Top 3 Bypasses
- Bypass\n- Null byte technique\n- Filter/WAF bypass
## Indicators
- Reflection appearing outside standard bounds
## Impact Template
> "This API_Security vulnerability allows an attacker to subvert execution bounds, resulting in severe compromise."
## Key Files
[[README]] | [[payloads]] | [[hunting-methodology]] | [[bypasses]]
