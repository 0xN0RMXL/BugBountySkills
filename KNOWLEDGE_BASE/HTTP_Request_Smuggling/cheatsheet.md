---
vuln_type: "HTTP_Request_Smuggling"
file_type: "cheatsheet"
total_reports: "105"
avg_bounty: "0"
max_bounty: "0"
severity_distribution: "critical:0% high:2% medium:7% low:91%"
owasp_categories: ["A00:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["HTTP_Request_Smuggling", "web", "api", "A00", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---
# HTTP Request Smuggling Cheatsheet
## Top 5 Payloads
```javascript
https://engineeringblog.yelp.com/xxcrlftest%0d%0aSet...\nGET / HTTP/1.1
Host: localhost:5000
Content-Length :...\nrequire 'net/http'
http = Net::HTTP.new('192.168.30....\nGET / HTTP/1.1
Transfer-Encoding: chunked
 , identit...\nrequire 'net/http'

http = Net::HTTP.new('127.0.0.1'...
```
## Attack Surfaces
- Search functionality\n- Authentication\n- Export/download
## Quick Test
1. Inject a benign token to enumerate bounds.
2. Append special control characters sequentially.
## Top 3 Bypasses
- Encoding technique\n- Bypass\n- Filter/WAF bypass
## Indicators
- Reflection appearing outside standard bounds
## Impact Template
> "This HTTP_Request_Smuggling vulnerability allows an attacker to subvert execution bounds, resulting in severe compromise."
## Key Files
[[README]] | [[payloads]] | [[hunting-methodology]] | [[bypasses]]
