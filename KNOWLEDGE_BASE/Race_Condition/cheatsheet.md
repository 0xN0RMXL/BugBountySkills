---
vuln_type: "Race_Condition"
file_type: "cheatsheet"
total_reports: "66"
avg_bounty: "0"
max_bounty: "0"
severity_distribution: "critical:4% high:6% medium:6% low:84%"
owasp_categories: ["A00:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["Race_Condition", "web", "api", "A00", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---
# Race Condition Cheatsheet
## Top 5 Payloads
```javascript
if(stat(filename, &sb) == -1 || !S_ISREG(sb.st_mode)...\n:54:curl/lib/socks_gssapi.c
static gss_ctx_id_t gss_...\nPOST /graphql HTTP/1.1
Host: hackerone.com
Connectio...\nPOST /cabinet/stripeapi/v1/projects/298427/emails/fo...\n<script>alert(1)</script>
```
## Attack Surfaces
- Search functionality\n- Authentication\n- Export/download
## Quick Test
1. Inject a benign token to enumerate bounds.
2. Append special control characters sequentially.
## Top 3 Bypasses
- Race condition\n- Bypass\n- Filter/WAF bypass
## Indicators
- Reflection appearing outside standard bounds
## Impact Template
> "This Race_Condition vulnerability allows an attacker to subvert execution bounds, resulting in severe compromise."
## Key Files
[[README]] | [[payloads]] | [[hunting-methodology]] | [[bypasses]]
