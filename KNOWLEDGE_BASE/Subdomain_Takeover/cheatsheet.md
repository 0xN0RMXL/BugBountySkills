---
vuln_type: "Subdomain_Takeover"
file_type: "cheatsheet"
total_reports: "165"
avg_bounty: "0"
max_bounty: "0"
severity_distribution: "critical:0% high:2% medium:2% low:96%"
owasp_categories: ["A00:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["Subdomain_Takeover", "web", "api", "A00", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---
# Subdomain Takeover Cheatsheet
## Top 5 Payloads
```javascript
$ host odoo-staging.exness.io
odoo-staging.exness.io...\n$ dig test.www.midigator.com
[snipped]
;; ANSWER... ...\n`
404 Not Found

    Code: NoSuchBucket
    Message:...\n216.58.203.243    moderator.ubnt.com
216.58.203.243 ...\n216.58.203.243 moderator.ubnt.com 216.58.203.243 ghs...
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
> "This Subdomain_Takeover vulnerability allows an attacker to subvert execution bounds, resulting in severe compromise."
## Key Files
[[README]] | [[payloads]] | [[hunting-methodology]] | [[bypasses]]
