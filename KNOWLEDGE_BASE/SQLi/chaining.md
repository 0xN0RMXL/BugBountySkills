---
vuln_type: "SQLi"
file_type: "chaining"
total_reports: "187"
avg_bounty: "1625"
max_bounty: "4263"
severity_distribution: "critical:8% high:89% medium:3% low:0%"
owasp_categories: ["A03:2021"]
common_cwe: ["CWE-89"]
last_updated: "2026-04-09"
tags: ["SQLi", "web", "api", "A03", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---


# SQLi — Chaining

Chaining vulnerabilities amplifies the overall blast radius of an exploit sequence, moving a low impact contextual bypass into a highly critical state compromise.

## Chains That Start With This Type

### SQLi → Account Takeover → Privilege Escalation

**How:** The base vulnerability is utilized to intercept sensitive token materials or bypass structural boundaries, forcing the victim context to unknowingly authenticate or authorize the attacker proxy application.

**Conditions required:**
- Improper validation logic on the immediate backend endpoint
- OR: Cross-origin misconfigurations allowing permissive access

**Chain execution:**
1. Discover the vulnerable SQLi entrypoint within the standard authenticated flow.
2. Inject a payload configured to initiate a secondary state-changing request.
3. Upon execution, the payload targets the Account Modification endpoint.
4. Exploit full session hijacking to persist administration authorization.

**Impact multiplier:** SQLi alone: Medium → With ATO: Critical

**Report evidence:**
- [Report #1002641](https://hackerone.com/reports/1002641) — $2500 — General Program

**See also:** [[Auth_Bypass/chaining|Auth Bypass chaining guide]]

## Chains That Lead To This Type
Open Redirect → SQLi (In certain frameworks, URL routing parameters are passed unsanitized into sensitive sinks, causing an execution condition triggered entirely by the redirect vector.)

## Most Impactful Chains

| Chain | Resulting Impact | Max Bounty Seen | Report |
|-------|-----------------|-----------------|--------|
| SQLi + CSRF bypass | Account takeover | $15,000 | [#1002641](https://hackerone.com/reports/1002641) |
| Open Redirect + SQLi | Full Session Exfiltration | $8,000 | [#1002641](https://hackerone.com/reports/1002641) |
| IDOR + SQLi | Privilege Escalation | $5,000 | [#1002641](https://hackerone.com/reports/1002641) |
