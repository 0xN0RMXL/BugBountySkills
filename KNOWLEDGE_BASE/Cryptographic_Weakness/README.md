---
vuln_type: "Cryptographic_Weakness"
file_type: "readme"
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


# Cryptographic Weakness — Complete Hunter's Reference

Cryptographic Weakness represents a critical security oversight in implementing cryptographic weakness paradigms. Attackers exploit gaps in input validation, output encoding, or authorization to manipulate application state, accessing data or capabilities designated for other security boundaries.

> [!NOTE] Corpus Statistics
> **Total reports analyzed:** 172
> **Average bounty:** $573
> **Highest bounty on record:** $2,162 — [Report #2921724](https://hackerone.com/reports/2921724) if 172 > 0 else 'N/A'
> **Dominant severity:** Low (63% of reports)
> **Most affected industry:** saas (12% of reports)
> **OWASP category:** A02:2021 — Vulnerability
> **Most common CWE:** CWE-000 (Improper Handling)

## Quick Navigation

| File | What's Inside |
|------|--------------|
| [[theory\|Theory]] | All variants, root causes, how it works at code level |
| [[attack-scenarios\|Attack Scenarios]] | 11 distinct scenarios with step-by-step instructions |
| [[payloads\|Payloads]] | Complete payload library — 5 payloads |
| [[hunting-methodology\|Hunting Methodology]] | 6-phase step-by-step hunting workflow |
| [[tools\|Tools]] | 4 tools with exact commands |
| [[bypasses\|Bypasses]] | 5 bypass techniques for WAFs, filters, CSP |
| [[chaining\|Chaining]] | 3+ chain patterns with other vulnerabilities |
| [[reports-index\|Reports Index]] | All 172 reports sorted by bounty |
| [[cheatsheet\|Cheatsheet]] | One-page quick reference for active hunts |

## Why This Matters (Hunter's Perspective)

This vulnerability is incredibly prevalent across modern web architectures. Despite modern web frameworks offering out-of-the-box protections, it consistently manifests due to business logic complexities, edge-case API routing, and third-party integrations taking over rendering or processing flows. The statistical corpus shows 172 reports, making it one of the most prolific findings available for a modern bug hunter.

What separates a $100 finding from a $10,000 payload is business impact. The programs paying the highest bounties (like curl and others in the saas industry) evaluate findings not just on technical reproducibility, but on what an attacker can achieve. A payload simply proving execution is often valued far less than one extracting session cookies, bypassing CSRF protections to commandeer accounts, or achieving horizontal privilege escalation against enterprise tenants.

It is harder to find than beginners expect because basic scanning tools only test naive context. Most tools fail to understand single-page application router states, DOM-based sinks that only trigger upon user interaction, or WAF evasions requiring parameter pollution and exotic encodings. Mastering this area requires understanding the application exactly as the developer did, navigating the architectural nuances, and locating the specific context where validation logic breaks down.
## Top 10 Reports Hall of Fame

| Rank | ID | Program | Severity | Bounty | Sub-type | Summary |
|------|----|---------|----------|--------|----------|---------|
| 1 | [Report #2921724](https://hackerone.com/reports/2921724) | xenbits.xen.org | Medium | $2,162 | General | Deadlock in x86 HVM... |
| 2 | [Report #1679734](https://hackerone.com/reports/1679734) | dovetale.com), | Medium | $800 | General | Account Takeover Vulnerability in... |
| 3 | [Report #2872502](https://hackerone.com/reports/2872502) | Internet Bug Bounty | Medium | $541 | General | Possible ReDoS... |
| 4 | [Report #2621057](https://hackerone.com/reports/2621057) | Internet Bug Bounty | Medium | $536 | TLS/SSL Issues | libcurl: freeing stack... |
| 5 | [Report #2978267](https://hackerone.com/reports/2978267) | Internet Bug Bounty | Medium | $432 | TLS/SSL Issues | TLS client... |
| 6 | [Report #2553026](https://hackerone.com/reports/2553026) | HackerOne | High | $100 | General | Domain highlighting on External... |
| 7 | [Report #3283232](https://hackerone.com/reports/3283232) | github.com | High | $11 | TLS/SSL Issues | Use After Free (that leads to... |
| 8 | [Report #3542546](https://hackerone.com/reports/3542546) | RubyGems | Critical | $2 | General | Server-side ReDoS via... |
| 9 | [Report #3150884](https://hackerone.com/reports/3150884) | curl | Critical | N/A | TLS/SSL Issues | CVE-2025-4947: QUIC certificate check... |
| 10 | [Report #3268294](https://hackerone.com/reports/3268294) | curl | Critical | N/A | General | Exposure of Private RSA Private Key in... |

## Quick-Start Hunting Checklist

- [ ] Identify all input vectors reflecting into the target application response.
- [ ] Check exactly how special characters (<, >, ", ', `, {) are handled by the server.
- [ ] Attempt out-of-band correlation by submitting external blind payloads (Burp Collaborator).
- [ ] Test the exact same parameter against different content-types or APIs.
- [ ] Attempt HTTP parameter pollution by sending duplicate keys: `?id=1&id=2`.
- [ ] Inject known bypass techniques like null bytes `%00` or URL encoding cascades.
- [ ] Determine the exact framework parsing logic vs validation logic.
- [ ] Escalate to sensitive business logical flows if any reflection/injection succeeds.
- [ ] Leverage account-specific identifiers to check cross-tenant data leakage.
- [ ] Map all unauthenticated and authenticated state boundaries.

## Related Vulnerability Types

This vulnerability frequently appears alongside or enables these types:
- [[SSTI/README|SSTI]] — Server-side template injection can escalate impact constraints
- [[Open_Redirect/README|Open Redirect]] — Often chainable to upgrade impact
- [[CSRF/README|CSRF]] — Can be combined for unauthorized execution of actions
