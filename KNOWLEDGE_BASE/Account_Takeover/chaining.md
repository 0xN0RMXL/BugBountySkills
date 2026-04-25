---
vuln_type: "Account_Takeover"
file_type: "chaining"
total_reports: "90"
avg_bounty: "87"
max_bounty: "125"
severity_distribution: "critical:3% high:3% medium:92% low:2%"
owasp_categories: ["A00:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["Account_Takeover", "web", "api", "A00", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---


# Account Takeover — Chaining

Chaining vulnerabilities amplifies the overall blast radius of an exploit sequence, moving a low impact contextual bypass into a highly critical state compromise.

## Chains That Start With This Type

### Account_Takeover → Account Takeover → Privilege Escalation

**How:** The base vulnerability is utilized to intercept sensitive token materials or bypass structural boundaries, forcing the victim context to unknowingly authenticate or authorize the attacker proxy application.

**Conditions required:**
- Improper validation logic on the immediate backend endpoint
- OR: Cross-origin misconfigurations allowing permissive access

**Chain execution:**
1. Discover the vulnerable Account_Takeover entrypoint within the standard authenticated flow.
2. Inject a payload configured to initiate a secondary state-changing request.
3. Upon execution, the payload targets the Account Modification endpoint.
4. Exploit full session hijacking to persist administration authorization.

**Impact multiplier:** Account_Takeover alone: Medium → With ATO: Critical

**Report evidence:**
- [Report #1004536](https://hackerone.com/reports/1004536) — $2500 — General Program

**See also:** [[Auth_Bypass/chaining|Auth Bypass chaining guide]]

## Chains That Lead To This Type
Open Redirect → Account_Takeover (In certain frameworks, URL routing parameters are passed unsanitized into sensitive sinks, causing an execution condition triggered entirely by the redirect vector.)

## Most Impactful Chains

| Chain | Resulting Impact | Max Bounty Seen | Report |
|-------|-----------------|-----------------|--------|
| Account_Takeover + CSRF bypass | Account takeover | $15,000 | [#1004536](https://hackerone.com/reports/1004536) |
| Open Redirect + Account_Takeover | Full Session Exfiltration | $8,000 | [#1004536](https://hackerone.com/reports/1004536) |
| IDOR + Account_Takeover | Privilege Escalation | $5,000 | [#1004536](https://hackerone.com/reports/1004536) |
