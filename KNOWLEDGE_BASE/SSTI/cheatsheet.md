---
vuln_type: "SSTI"
file_type: "cheatsheet"
total_reports: "10"
avg_bounty: "0"
max_bounty: "0"
severity_distribution: "critical:0% high:0% medium:0% low:100%"
owasp_categories: ["A03:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["SSTI", "web", "api", "A03", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---
# SSTI Cheatsheet
## Top 5 Payloads
```javascript
module UJS
  class Server < Rails::Application
    r...\n<script>alert(1)</script>\n<script>alert(1)</script>\n<script>alert(1)</script>\n<script>alert(1)</script>
```
## Attack Surfaces
- Search functionality\n- Authentication\n- Export/download
## Quick Test
1. Inject a benign token to enumerate bounds.
2. Append special control characters sequentially.
## Top 3 Bypasses
- Standard framework specific encoding\n- Standard framework specific encoding\n- Standard framework specific encoding
## Indicators
- Reflection appearing outside standard bounds
## Impact Template
> "This SSTI vulnerability allows an attacker to subvert execution bounds, resulting in severe compromise."
## Key Files
[[README]] | [[payloads]] | [[hunting-methodology]] | [[bypasses]]
