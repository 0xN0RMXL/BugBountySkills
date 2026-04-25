---
vuln_type: "Insecure_Deserialization"
file_type: "cheatsheet"
total_reports: "16"
avg_bounty: "0"
max_bounty: "0"
severity_distribution: "critical:0% high:6% medium:94% low:0%"
owasp_categories: ["A00:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["Insecure_Deserialization", "web", "api", "A00", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---
# Insecure Deserialization Cheatsheet
## Top 5 Payloads
```javascript
https://github.com/php/php-src/blob/master/ext/wddx/...\nhttp://git.php.net/?p=php-src.git;a=commit;h=780daee...\n<script>alert(1)</script>\n<script>alert(1)</script>\n<script>alert(1)</script>
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
> "This Insecure_Deserialization vulnerability allows an attacker to subvert execution bounds, resulting in severe compromise."
## Key Files
[[README]] | [[payloads]] | [[hunting-methodology]] | [[bypasses]]
