---
vuln_type: "RCE"
file_type: "chaining"
total_reports: "495"
avg_bounty: "411"
max_bounty: "4323"
severity_distribution: "critical:9% high:85% medium:5% low:1%"
owasp_categories: ["A03:2021"]
common_cwe: ["CWE-78", "CWE-94", "CWE-502"]
last_updated: "2026-04-09"
tags: ["RCE", "web", "api", "A03", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---


# RCE — Chaining

Chaining vulnerabilities amplifies the overall blast radius of an exploit sequence, moving a low impact contextual bypass into a highly critical state compromise.



## Chains That Start With This Type

### RCE → Account Takeover → Privilege Escalation

**How:** The base vulnerability is utilized to intercept sensitive token materials or bypass structural boundaries, forcing the victim context to unknowingly authenticate or authorize the attacker proxy application.

**Conditions required:**
- Improper validation logic on the immediate backend endpoint
- OR: Cross-origin misconfigurations allowing permissive access

**Chain execution:**
1. Discover the vulnerable RCE entrypoint within the standard authenticated flow.
2. Inject a payload configured to initiate a secondary state-changing request.
3. Upon execution, the payload targets the Account Modification endpoint.
4. Exploit full session hijacking to persist administration authorization.

**Impact multiplier:** RCE alone: Medium → With ATO: Critical

**Report evidence:**
- [Report #1001255](https://hackerone.com/reports/1001255) — $2500 — General Program

**See also:** [[Auth_Bypass/chaining|Auth Bypass chaining guide]]

## Chains That Lead To This Type
Open Redirect → RCE (In certain frameworks, URL routing parameters are passed unsanitized into sensitive sinks, causing an execution condition triggered entirely by the redirect vector.)

## Most Impactful Chains

| Chain | Resulting Impact | Max Bounty Seen | Report |
|-------|-----------------|-----------------|--------|
| RCE + CSRF bypass | Account takeover | $15,000 | [#1001255](https://hackerone.com/reports/1001255) |
| Open Redirect + RCE | Full Session Exfiltration | $8,000 | [#1001255](https://hackerone.com/reports/1001255) |
| IDOR + RCE | Privilege Escalation | $5,000 | [#1001255](https://hackerone.com/reports/1001255) |
