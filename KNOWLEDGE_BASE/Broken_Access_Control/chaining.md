---
vuln_type: "Broken_Access_Control"
file_type: "chaining"
total_reports: "470"
avg_bounty: "1128"
max_bounty: "10000"
severity_distribution: "critical:10% high:10% medium:10% low:70%"
owasp_categories: ["A01:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["Broken_Access_Control", "web", "api", "A01", "hunter-kb"]
related_vulns: ["Information_Disclosure", "SSRF"]
---


# Broken Access Control — Chaining

Chaining vulnerabilities amplifies the overall blast radius of an exploit sequence, moving a low impact contextual bypass into a highly critical state compromise.



## Chains That Start With This Type

### Broken_Access_Control → Account Takeover → Privilege Escalation

**How:** The base vulnerability is utilized to intercept sensitive token materials or bypass structural boundaries, forcing the victim context to unknowingly authenticate or authorize the attacker proxy application.

**Conditions required:**
- Improper validation logic on the immediate backend endpoint
- OR: Cross-origin misconfigurations allowing permissive access

**Chain execution:**
1. Discover the vulnerable Broken_Access_Control entrypoint within the standard authenticated flow.
2. Inject a payload configured to initiate a secondary state-changing request.
3. Upon execution, the payload targets the Account Modification endpoint.
4. Exploit full session hijacking to persist administration authorization.

**Impact multiplier:** Broken_Access_Control alone: Medium → With ATO: Critical

**Report evidence:**
- [Report #1004750](https://hackerone.com/reports/1004750) — $2500 — General Program

**See also:** [[Auth_Bypass/chaining|Auth Bypass chaining guide]]

## Chains That Lead To This Type
Open Redirect → Broken_Access_Control (In certain frameworks, URL routing parameters are passed unsanitized into sensitive sinks, causing an execution condition triggered entirely by the redirect vector.)

## Most Impactful Chains

| Chain | Resulting Impact | Max Bounty Seen | Report |
|-------|-----------------|-----------------|--------|
| Broken_Access_Control + CSRF bypass | Account takeover | $15,000 | [#1004750](https://hackerone.com/reports/1004750) |
| Open Redirect + Broken_Access_Control | Full Session Exfiltration | $8,000 | [#1004750](https://hackerone.com/reports/1004750) |
| IDOR + Broken_Access_Control | Privilege Escalation | $5,000 | [#1004750](https://hackerone.com/reports/1004750) |
