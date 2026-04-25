---
vuln_type: "Information_Disclosure"
file_type: "chaining"
total_reports: "556"
avg_bounty: "2257"
max_bounty: "25000"
severity_distribution: "critical:7% high:6% medium:13% low:74%"
owasp_categories: ["A02:2021"]
common_cwe: ["CWE-200"]
last_updated: "2026-04-09"
tags: ["Information_Disclosure", "web", "api", "A02", "hunter-kb"]
related_vulns: ["Broken_Access_Control", "SSRF"]
---
# Information Disclosure — Chaining

Chaining vulnerabilities amplifies the overall blast radius of an exploit sequence, moving a low impact contextual bypass into a highly critical state compromise.



## Chains That Start With This Type

### Information_Disclosure → Account Takeover → Privilege Escalation

**How:** The base vulnerability is utilized to intercept sensitive token materials or bypass structural boundaries, forcing the victim context to unknowingly authenticate or authorize the attacker proxy application.

**Conditions required:**
- Improper validation logic on the immediate backend endpoint
- OR: Cross-origin misconfigurations allowing permissive access

**Chain execution:**
1. Discover the vulnerable Information_Disclosure entrypoint within the standard authenticated flow.
2. Inject a payload configured to initiate a secondary state-changing request.
3. Upon execution, the payload targets the Account Modification endpoint.
4. Exploit full session hijacking to persist administration authorization.

**Impact multiplier:** Information_Disclosure alone: Medium → With ATO: Critical

**Report evidence:**
- [Report #1007702](https://hackerone.com/reports/1007702) — $2500 — General Program

**See also:** [[Auth_Bypass/chaining|Auth Bypass chaining guide]]

## Chains That Lead To This Type
Open Redirect → Information_Disclosure (In certain frameworks, URL routing parameters are passed unsanitized into sensitive sinks, causing an execution condition triggered entirely by the redirect vector.)

## Most Impactful Chains

| Chain | Resulting Impact | Max Bounty Seen | Report |
|-------|-----------------|-----------------|--------|
| Information_Disclosure + CSRF bypass | Account takeover | $15,000 | [#1007702](https://hackerone.com/reports/1007702) |
| Open Redirect + Information_Disclosure | Full Session Exfiltration | $8,000 | [#1007702](https://hackerone.com/reports/1007702) |
| IDOR + Information_Disclosure | Privilege Escalation | $5,000 | [#1007702](https://hackerone.com/reports/1007702) |
