---
vuln_type: "CORS_Misconfiguration"
file_type: "cheatsheet"
total_reports: "18"
avg_bounty: "0"
max_bounty: "0"
severity_distribution: "critical:0% high:0% medium:0% low:100%"
owasp_categories: ["A00:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["CORS_Misconfiguration", "web", "api", "A00", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---
# CORS Misconfiguration Cheatsheet
## Top 5 Payloads
```javascript
<?xml version="1.0"?>
<!DOCTYPE cross-domain-policy ...\nGET /wp-json HTTP/1.1
Host: █████████
Connection: cl...\nGET /██████████ HTTP/1.1
Host: █████
Accept: */*
Acc...\nHTTP/1.1 200 OK
Cache-Control: max-age=0,must-revali...\n<script>alert(1)</script>
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
> "This CORS_Misconfiguration vulnerability allows an attacker to subvert execution bounds, resulting in severe compromise."
## Key Files
[[README]] | [[payloads]] | [[hunting-methodology]] | [[bypasses]]
