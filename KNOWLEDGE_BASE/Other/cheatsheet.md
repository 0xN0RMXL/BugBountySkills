---
vuln_type: "Other"
file_type: "cheatsheet"
total_reports: "3258"
avg_bounty: "1465"
max_bounty: "12500"
severity_distribution: "critical:0% high:0% medium:3% low:97%"
owasp_categories: ["A00:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["Other", "web", "api", "A00", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---
# Other Cheatsheet
## Top 5 Payloads
```javascript
User-agent: *
Disallow: /s3cr3t-ar3a
Flag: flag{4810...\nIn Scope Domain - **hackyholidays.h1ctf.com**\nhttp://www.grouplogic.com/ADMIN/store/index.cfm\nJSON.parse()\n/data/data/com.owncloud.android/*
```
## Attack Surfaces
- Search functionality\n- Authentication\n- Export/download
## Quick Test
1. Inject a benign token to enumerate bounds.
2. Append special control characters sequentially.
## Top 3 Bypasses
- Bypass\n- Encoding technique\n- Filter/WAF bypass
## Indicators
- Reflection appearing outside standard bounds
## Impact Template
> "This Other vulnerability allows an attacker to subvert execution bounds, resulting in severe compromise."
## Key Files
[[README]] | [[payloads]] | [[hunting-methodology]] | [[bypasses]]
