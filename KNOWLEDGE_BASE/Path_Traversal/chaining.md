---
vuln_type: "Path_Traversal"
file_type: "chaining"
total_reports: "166"
avg_bounty: "3000"
max_bounty: "6000"
severity_distribution: "critical:6% high:7% medium:86% low:1%"
owasp_categories: ["A01:2021"]
common_cwe: ["CWE-22"]
last_updated: "2026-04-09"
tags: ["Path_Traversal", "web", "api", "A01", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---


# Path Traversal — Chaining

Chaining vulnerabilities amplifies the overall blast radius of an exploit sequence, moving a low impact contextual bypass into a highly critical state compromise.



## Chains That Start With This Type

### Path_Traversal → Account Takeover → Privilege Escalation

**How:** The base vulnerability is utilized to intercept sensitive token materials or bypass structural boundaries, forcing the victim context to unknowingly authenticate or authorize the attacker proxy application.

**Conditions required:**
- Improper validation logic on the immediate backend endpoint
- OR: Cross-origin misconfigurations allowing permissive access

**Chain execution:**
1. Discover the vulnerable Path_Traversal entrypoint within the standard authenticated flow.
2. Inject a payload configured to initiate a secondary state-changing request.
3. Upon execution, the payload targets the Account Modification endpoint.
4. Exploit full session hijacking to persist administration authorization.

**Impact multiplier:** Path_Traversal alone: Medium → With ATO: Critical

**Report evidence:**
- [Report #1007799](https://hackerone.com/reports/1007799) — $2500 — General Program

**See also:** [[Auth_Bypass/chaining|Auth Bypass chaining guide]]

## Chains That Lead To This Type
Open Redirect → Path_Traversal (In certain frameworks, URL routing parameters are passed unsanitized into sensitive sinks, causing an execution condition triggered entirely by the redirect vector.)

## Most Impactful Chains

| Chain | Resulting Impact | Max Bounty Seen | Report |
|-------|-----------------|-----------------|--------|
| Path_Traversal + CSRF bypass | Account takeover | $15,000 | [#1007799](https://hackerone.com/reports/1007799) |
| Open Redirect + Path_Traversal | Full Session Exfiltration | $8,000 | [#1007799](https://hackerone.com/reports/1007799) |
| IDOR + Path_Traversal | Privilege Escalation | $5,000 | [#1007799](https://hackerone.com/reports/1007799) |
