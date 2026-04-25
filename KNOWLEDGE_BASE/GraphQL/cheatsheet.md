---
vuln_type: "GraphQL"
file_type: "cheatsheet"
total_reports: "62"
avg_bounty: "0"
max_bounty: "0"
severity_distribution: "critical:0% high:0% medium:0% low:100%"
owasp_categories: ["A00:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["GraphQL", "web", "api", "A00", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---
# GraphQL Cheatsheet
## Top 5 Payloads
```javascript
query {
  user(username:"<victim>"){
    email
    u...\nPOST /graphql HTTP/1.1
Host: hackerone.com
Connectio...\ndef resolve(id:)
        snippet = authorized_find!(...\nmodule Mutations
  module Metrics
    module Dashboa...\nquery { user(username:"<victim>"){ email username } }
```
## Attack Surfaces
- Search functionality\n- Authentication\n- API endpoint
## Quick Test
1. Inject a benign token to enumerate bounds.
2. Append special control characters sequentially.
## Top 3 Bypasses
- Bypass\n- Circumvention\n- Standard framework specific encoding
## Indicators
- Reflection appearing outside standard bounds
## Impact Template
> "This GraphQL vulnerability allows an attacker to subvert execution bounds, resulting in severe compromise."
## Key Files
[[README]] | [[payloads]] | [[hunting-methodology]] | [[bypasses]]
