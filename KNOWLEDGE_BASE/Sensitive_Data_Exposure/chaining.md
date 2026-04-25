---
vuln_type: "Sensitive_Data_Exposure"
file_type: "chaining"
total_reports: "234"
avg_bounty: "1877"
max_bounty: "15000"
severity_distribution: "critical:3% high:8% medium:15% low:74%"
owasp_categories: ["A02:2021"]
common_cwe: ["CWE-200"]
last_updated: "2026-04-09"
tags: ["Sensitive_Data_Exposure", "web", "api", "A02", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---


# Sensitive Data Exposure — Chaining

Chaining vulnerabilities amplifies the overall blast radius of an exploit sequence, moving a low impact contextual bypass into a highly critical state compromise.

## Chains That Start With This Type

### Sensitive_Data_Exposure → Account Takeover → Privilege Escalation

**How:** The base vulnerability is utilized to intercept sensitive token materials or bypass structural boundaries, forcing the victim context to unknowingly authenticate or authorize the attacker proxy application.

**Conditions required:**
- Improper validation logic on the immediate backend endpoint
- OR: Cross-origin misconfigurations allowing permissive access

**Chain execution:**
1. Discover the vulnerable Sensitive_Data_Exposure entrypoint within the standard authenticated flow.
2. Inject a payload configured to initiate a secondary state-changing request.
3. Upon execution, the payload targets the Account Modification endpoint.
4. Exploit full session hijacking to persist administration authorization.

**Impact multiplier:** Sensitive_Data_Exposure alone: Medium → With ATO: Critical

**Report evidence:**
- [Report #1003007](https://hackerone.com/reports/1003007) — $2500 — General Program

**See also:** [[Auth_Bypass/chaining|Auth Bypass chaining guide]]

## Chains That Lead To This Type
Open Redirect → Sensitive_Data_Exposure (In certain frameworks, URL routing parameters are passed unsanitized into sensitive sinks, causing an execution condition triggered entirely by the redirect vector.)

## Most Impactful Chains

| Chain | Resulting Impact | Max Bounty Seen | Report |
|-------|-----------------|-----------------|--------|
| Sensitive_Data_Exposure + CSRF bypass | Account takeover | $15,000 | [#1003007](https://hackerone.com/reports/1003007) |
| Open Redirect + Sensitive_Data_Exposure | Full Session Exfiltration | $8,000 | [#1003007](https://hackerone.com/reports/1003007) |
| IDOR + Sensitive_Data_Exposure | Privilege Escalation | $5,000 | [#1003007](https://hackerone.com/reports/1003007) |
