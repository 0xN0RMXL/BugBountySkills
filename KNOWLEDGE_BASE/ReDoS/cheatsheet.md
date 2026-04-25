---
vuln_type: "ReDoS"
file_type: "cheatsheet"
total_reports: "29"
avg_bounty: "384"
max_bounty: "541"
severity_distribution: "critical:0% high:3% medium:8% low:89%"
owasp_categories: ["A00:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["ReDoS", "web", "api", "A00", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---
# ReDoS Cheatsheet
## Top 5 Payloads
```javascript
([A-Z:a-z0-9_]+)\.([a-z0-9_]+)(\s*\(\s*[a-z0-9_.,\s]...\ndef rfc2822(date)
      if /\A\s*
          (?:(?:Mo...\ndef scrub_attribute(node, attr_node)
        attr_na...\n<script>alert(1)</script>\n<script>alert(1)</script>
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
> "This ReDoS vulnerability allows an attacker to subvert execution bounds, resulting in severe compromise."
## Key Files
[[README]] | [[payloads]] | [[hunting-methodology]] | [[bypasses]]
