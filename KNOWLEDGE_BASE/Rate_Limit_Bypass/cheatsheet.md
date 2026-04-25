---
vuln_type: "Rate_Limit_Bypass"
file_type: "cheatsheet"
total_reports: "184"
avg_bounty: "200"
max_bounty: "200"
severity_distribution: "critical:1% high:1% medium:3% low:95%"
owasp_categories: ["A00:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["Rate_Limit_Bypass", "web", "api", "A00", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---
# Rate Limit Bypass Cheatsheet
## Top 5 Payloads
```javascript
POST /emailformdata/v1/amp-lists?projectId= HTTP/1.1...\nmy case I chose !23Qweasdzxc as the password.\n~$ python tor.py -t username -p passwordlist.txt\nPUT /emitrani.txt HTTP/1.1
Host: ratelimited.me
Cont...\nPOST /auth/post_login HTTP/1.1
Host: ctf.hacker101.c...
```
## Attack Surfaces
- Search functionality\n- Authentication\n- Export/download
## Quick Test
1. Inject a benign token to enumerate bounds.
2. Append special control characters sequentially.
## Top 3 Bypasses
- Bypass\n- Circumvention\n- Encoding technique
## Indicators
- Reflection appearing outside standard bounds
## Impact Template
> "This Rate_Limit_Bypass vulnerability allows an attacker to subvert execution bounds, resulting in severe compromise."
## Key Files
[[README]] | [[payloads]] | [[hunting-methodology]] | [[bypasses]]
