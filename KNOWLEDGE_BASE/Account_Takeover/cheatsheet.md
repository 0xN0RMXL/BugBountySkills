---
vuln_type: "Account_Takeover"
file_type: "cheatsheet"
total_reports: "90"
avg_bounty: "87"
max_bounty: "125"
severity_distribution: "critical:3% high:3% medium:92% low:2%"
owasp_categories: ["A00:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["Account_Takeover", "web", "api", "A00", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---
# Account Takeover Cheatsheet
## Top 5 Payloads
```javascript
2020-03-20 08:12:15 - main - <br>Module: change pass...\nPOST /__852585b6003eba25.nsf/forgotpassword.html?Ope...\n<script>alert(1)</script>\n<script>alert(1)</script>\n<script>alert(1)</script>
```
## Attack Surfaces
- Search functionality\n- Authentication\n- User profile/settings
## Quick Test
1. Inject a benign token to enumerate bounds.
2. Append special control characters sequentially.
## Top 3 Bypasses
- Bypass\n- Standard framework specific encoding\n- Standard framework specific encoding
## Indicators
- Reflection appearing outside standard bounds
## Impact Template
> "This Account_Takeover vulnerability allows an attacker to subvert execution bounds, resulting in severe compromise."
## Key Files
[[README]] | [[payloads]] | [[hunting-methodology]] | [[bypasses]]
