---
vuln_type: "SSRF"
file_type: "chaining"
total_reports: "214"
avg_bounty: "2954"
max_bounty: "4263"
severity_distribution: "critical:4% high:91% medium:5% low:0%"
owasp_categories: ["A10:2021"]
common_cwe: ["CWE-918"]
last_updated: "2026-04-09"
tags: ["SSRF", "web", "api", "A10", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control"]
---


# SSRF — Chaining

Chaining vulnerabilities amplifies the overall blast radius of an exploit sequence, moving a low impact contextual bypass into a highly critical state compromise.



## Chains That Start With This Type

### SSRF → Account Takeover → Privilege Escalation

**How:** The base vulnerability is utilized to intercept sensitive token materials or bypass structural boundaries, forcing the victim context to unknowingly authenticate or authorize the attacker proxy application.

**Conditions required:**
- Improper validation logic on the immediate backend endpoint
- OR: Cross-origin misconfigurations allowing permissive access

**Chain execution:**
1. Discover the vulnerable SSRF entrypoint within the standard authenticated flow.
2. Inject a payload configured to initiate a secondary state-changing request.
3. Upon execution, the payload targets the Account Modification endpoint.
4. Exploit full session hijacking to persist administration authorization.

**Impact multiplier:** SSRF alone: Medium → With ATO: Critical

**Report evidence:**
- [Report #1004847](https://hackerone.com/reports/1004847) — $2500 — General Program

**See also:** [[Auth_Bypass/chaining|Auth Bypass chaining guide]]

## Chains That Lead To This Type
Open Redirect → SSRF (In certain frameworks, URL routing parameters are passed unsanitized into sensitive sinks, causing an execution condition triggered entirely by the redirect vector.)

## Most Impactful Chains

| Chain | Resulting Impact | Max Bounty Seen | Report |
|-------|-----------------|-----------------|--------|
| SSRF + CSRF bypass | Account takeover | $15,000 | [#1004847](https://hackerone.com/reports/1004847) |
| Open Redirect + SSRF | Full Session Exfiltration | $8,000 | [#1004847](https://hackerone.com/reports/1004847) |
| IDOR + SSRF | Privilege Escalation | $5,000 | [#1004847](https://hackerone.com/reports/1004847) |
