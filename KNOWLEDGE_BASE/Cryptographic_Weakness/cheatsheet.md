---
vuln_type: "Cryptographic_Weakness"
file_type: "cheatsheet"
total_reports: "172"
avg_bounty: "573"
max_bounty: "2162"
severity_distribution: "critical:7% high:10% medium:20% low:63%"
owasp_categories: ["A02:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["Cryptographic_Weakness", "web", "api", "A02", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---
# Cryptographic Weakness Cheatsheet
## Top 5 Payloads
```javascript
//set private key to 2
dh.setPrivateKey(Buffer.from(...\npublic function return_handler() {
		@ob_clean();
		...\n<?php
$to = "VICTIM@example.com";
$subject = "Passwo...\nif ( sha1( $attempted_password_plaintext ) === $vali...\nnli@nlistation:~$ dig mycrypto.com txt

; <<>> DiG 9...
```
## Attack Surfaces
- Search functionality\n- Authentication\n- Export/download
## Quick Test
1. Inject a benign token to enumerate bounds.
2. Append special control characters sequentially.
## Top 3 Bypasses
- Bypass\n- Filter/WAF bypass\n- Encoding technique
## Indicators
- Reflection appearing outside standard bounds
## Impact Template
> "This Cryptographic_Weakness vulnerability allows an attacker to subvert execution bounds, resulting in severe compromise."
## Key Files
[[README]] | [[payloads]] | [[hunting-methodology]] | [[bypasses]]
