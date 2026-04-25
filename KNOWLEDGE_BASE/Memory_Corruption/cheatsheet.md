---
vuln_type: "Memory_Corruption"
file_type: "cheatsheet"
total_reports: "421"
avg_bounty: "3416"
max_bounty: "10000"
severity_distribution: "critical:0% high:2% medium:4% low:94%"
owasp_categories: ["A03:2021"]
common_cwe: ["CWE-119", "CWE-416"]
last_updated: "2026-04-09"
tags: ["Memory_Corruption", "web", "api", "A03", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---
# Memory Corruption Cheatsheet
## Top 5 Payloads
```javascript
class<<Proc
class P class<<Proc
class P class P t en...\nfprintf(sendmail, " %s ", message);\n$ magick -version
Version: ImageMagick 7.0.10-45 Q16...\n1798     char buf[128];
...
...
1809     cp = strchr...\n3122 static char *
3123 search_make_new(const struct...
```
## Attack Surfaces
- Search functionality\n- Authentication\n- Export/download
## Quick Test
1. Inject a benign token to enumerate bounds.
2. Append special control characters sequentially.
## Top 3 Bypasses
- Encoding technique\n- Bypass\n- Null byte technique
## Indicators
- Reflection appearing outside standard bounds
## Impact Template
> "This Memory_Corruption vulnerability allows an attacker to subvert execution bounds, resulting in severe compromise."
## Key Files
[[README]] | [[payloads]] | [[hunting-methodology]] | [[bypasses]]
