---
vuln_type: "Clickjacking"
file_type: "cheatsheet"
total_reports: "94"
avg_bounty: "200"
max_bounty: "200"
severity_distribution: "critical:1% high:1% medium:3% low:95%"
owasp_categories: ["A00:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["Clickjacking", "web", "api", "A00", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---
# Clickjacking Cheatsheet
## Top 5 Payloads
```javascript
X-Frame-Options: ALLOW-FROM https://twitter.com/\n<html lang="en-US">
<head>
<meta charset="UTF-8">
<t...\n<html>
<head>
<title>Clickjack test page</title>
</h...\n<html>
<body>
<iframe src="http://book.zomato.com/ac...\n<script>alert(1)</script>
```
## Attack Surfaces
- Search functionality
- Authentication
- Export/download
## Quick Test
1. Inject a benign token to enumerate bounds.
2. Append special control characters sequentially.
## Top 3 Bypasses
- Bypass\n- Standard framework specific encoding\n- Standard framework specific encoding
## Indicators
- Reflection appearing outside standard bounds
## Impact Template
> "This Clickjacking vulnerability allows an attacker to subvert execution bounds, resulting in severe compromise."
## Key Files
[[README]] | [[payloads]] | [[hunting-methodology]] | [[bypasses]]
