---
vuln_type: "CORS_Misconfiguration"
file_type: "chaining"
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


# CORS Misconfiguration — Chaining

Chaining vulnerabilities amplifies the overall blast radius of an exploit sequence, moving a low impact contextual bypass into a highly critical state compromise.



## Chains That Start With This Type

### CORS_Misconfiguration → Account Takeover → Privilege Escalation

**How:** The base vulnerability is utilized to intercept sensitive token materials or bypass structural boundaries, forcing the victim context to unknowingly authenticate or authorize the attacker proxy application.

**Conditions required:**
- Improper validation logic on the immediate backend endpoint
- OR: Cross-origin misconfigurations allowing permissive access

**Chain execution:**
1. Discover the vulnerable CORS_Misconfiguration entrypoint within the standard authenticated flow.
2. Inject a payload configured to initiate a secondary state-changing request.
3. Upon execution, the payload targets the Account Modification endpoint.
4. Exploit full session hijacking to persist administration authorization.

**Impact multiplier:** CORS_Misconfiguration alone: Medium → With ATO: Critical

**Report evidence:**
- [Report #1092125](https://hackerone.com/reports/1092125) — $2500 — General Program

**See also:** [[Auth_Bypass/chaining|Auth Bypass chaining guide]]

## Chains That Lead To This Type
Open Redirect → CORS_Misconfiguration (In certain frameworks, URL routing parameters are passed unsanitized into sensitive sinks, causing an execution condition triggered entirely by the redirect vector.)

## Most Impactful Chains

| Chain | Resulting Impact | Max Bounty Seen | Report |
|-------|-----------------|-----------------|--------|
| CORS_Misconfiguration + CSRF bypass | Account takeover | $15,000 | [#1092125](https://hackerone.com/reports/1092125) |
| Open Redirect + CORS_Misconfiguration | Full Session Exfiltration | $8,000 | [#1092125](https://hackerone.com/reports/1092125) |
| IDOR + CORS_Misconfiguration | Privilege Escalation | $5,000 | [#1092125](https://hackerone.com/reports/1092125) |
