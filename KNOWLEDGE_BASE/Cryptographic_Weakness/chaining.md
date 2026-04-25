---
vuln_type: "Cryptographic_Weakness"
file_type: "chaining"
total_reports: "172"
avg_bounty: "573"
max_bounty: "2162"
severity_distribution: "critical:7% high:10% medium:20% low:63%"
owasp_categories: ["A02:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["Cryptographic_Weakness", "web", "api", "A02", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---


# Cryptographic Weakness — Chaining

Chaining vulnerabilities amplifies the overall blast radius of an exploit sequence, moving a low impact contextual bypass into a highly critical state compromise.

## Chains That Start With This Type

### Cryptographic_Weakness → Account Takeover → Privilege Escalation

**How:** The base vulnerability is utilized to intercept sensitive token materials or bypass structural boundaries, forcing the victim context to unknowingly authenticate or authorize the attacker proxy application.

**Conditions required:**
- Improper validation logic on the immediate backend endpoint
- OR: Cross-origin misconfigurations allowing permissive access

**Chain execution:**
1. Discover the vulnerable Cryptographic_Weakness entrypoint within the standard authenticated flow.
2. Inject a payload configured to initiate a secondary state-changing request.
3. Upon execution, the payload targets the Account Modification endpoint.
4. Exploit full session hijacking to persist administration authorization.

**Impact multiplier:** Cryptographic_Weakness alone: Medium → With ATO: Critical

**Report evidence:**
- [Report #1048457](https://hackerone.com/reports/1048457) — $2500 — General Program

**See also:** [[Auth_Bypass/chaining|Auth Bypass chaining guide]]

## Chains That Lead To This Type
Open Redirect → Cryptographic_Weakness (In certain frameworks, URL routing parameters are passed unsanitized into sensitive sinks, causing an execution condition triggered entirely by the redirect vector.)

## Most Impactful Chains

| Chain | Resulting Impact | Max Bounty Seen | Report |
|-------|-----------------|-----------------|--------|
| Cryptographic_Weakness + CSRF bypass | Account takeover | $15,000 | [#1048457](https://hackerone.com/reports/1048457) |
| Open Redirect + Cryptographic_Weakness | Full Session Exfiltration | $8,000 | [#1048457](https://hackerone.com/reports/1048457) |
| IDOR + Cryptographic_Weakness | Privilege Escalation | $5,000 | [#1048457](https://hackerone.com/reports/1048457) |
