---
vuln_type: "Clickjacking"
file_type: "chaining"
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


# Clickjacking — Chaining

Chaining vulnerabilities amplifies the overall blast radius of an exploit sequence, moving a low impact contextual bypass into a highly critical state compromise.



## Chains That Start With This Type

### Clickjacking → Account Takeover → Privilege Escalation

**How:** The base vulnerability is utilized to intercept sensitive token materials or bypass structural boundaries, forcing the victim context to unknowingly authenticate or authorize the attacker proxy application.

**Conditions required:**
- Improper validation logic on the immediate backend endpoint
- OR: Cross-origin misconfigurations allowing permissive access

**Chain execution:**
1. Discover the vulnerable Clickjacking entrypoint within the standard authenticated flow.
2. Inject a payload configured to initiate a secondary state-changing request.
3. Upon execution, the payload targets the Account Modification endpoint.
4. Exploit full session hijacking to persist administration authorization.

**Impact multiplier:** Clickjacking alone: Medium → With ATO: Critical

**Report evidence:**
- [Report #1031525](https://hackerone.com/reports/1031525) — $2500 — General Program

**See also:** [[Auth_Bypass/chaining|Auth Bypass chaining guide]]

## Chains That Lead To This Type
Open Redirect → Clickjacking (In certain frameworks, URL routing parameters are passed unsanitized into sensitive sinks, causing an execution condition triggered entirely by the redirect vector.)

## Most Impactful Chains

| Chain | Resulting Impact | Max Bounty Seen | Report |
|-------|-----------------|-----------------|--------|
| Clickjacking + CSRF bypass | Account takeover | $15,000 | [#1031525](https://hackerone.com/reports/1031525) |
| Open Redirect + Clickjacking | Full Session Exfiltration | $8,000 | [#1031525](https://hackerone.com/reports/1031525) |
| IDOR + Clickjacking | Privilege Escalation | $5,000 | [#1031525](https://hackerone.com/reports/1031525) |
