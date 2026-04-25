---
vuln_type: "Information_Disclosure"
file_type: "readme"
total_reports: "556"
avg_bounty: "2257"
max_bounty: "25000"
severity_distribution: "critical:7% high:6% medium:13% low:74%"
owasp_categories: ["A02:2021"]
common_cwe: ["CWE-200"]
last_updated: "2026-04-09"
tags: ["Information_Disclosure", "web", "api", "A02", "hunter-kb"]
related_vulns: ["Broken_Access_Control", "SSRF"]
---
# Information Disclosure — Complete Hunter's Reference

Information Disclosure represents a critical security oversight in implementing information disclosure paradigms. Attackers exploit gaps in input validation, output encoding, or authorization to manipulate application state, accessing data or capabilities designated for other security boundaries.

> [!NOTE] Corpus Statistics
> **Total reports analyzed:** 556
> **Average bounty:** $2,257
> **Highest bounty on record:** $25,000 — [Report #1618347](https://hackerone.com/reports/1618347) if 556 > 0 else 'N/A'
> **Dominant severity:** Low (74% of reports)
> **Most affected industry:** saas (11% of reports)
> **OWASP category:** A02:2021 — Vulnerability
> **Most common CWE:** CWE-200 (Improper Handling)

## Quick Navigation

| File | What's Inside |
|------|--------------|
| [[theory\|Theory]] | All variants, root causes, how it works at code level |
| [[attack-scenarios\|Attack Scenarios]] | 12 distinct scenarios with step-by-step instructions |
| [[payloads\|Payloads]] | Complete payload library — 12 payloads |
| [[hunting-methodology\|Hunting Methodology]] | 6-phase step-by-step hunting workflow |
| [[tools\|Tools]] | 7 tools with exact commands |
| [[bypasses\|Bypasses]] | 3 bypass techniques for WAFs, filters, CSP |
| [[chaining\|Chaining]] | 3+ chain patterns with other vulnerabilities |
| [[reports-index\|Reports Index]] | All 556 reports sorted by bounty |
| [[cheatsheet\|Cheatsheet]] | One-page quick reference for active hunts |

## Why This Matters (Hunter's Perspective)

This vulnerability is incredibly prevalent across modern web architectures. Despite modern web frameworks offering out-of-the-box protections, it consistently manifests due to business logic complexities, edge-case API routing, and third-party integrations taking over rendering or processing flows. The statistical corpus shows 556 reports, making it one of the most prolific findings available for a modern bug hunter.

What separates a $100 finding from a $10,000 payload is business impact. The programs paying the highest bounties (like U.S. Dept Of Defense and others in the saas industry) evaluate findings not just on technical reproducibility, but on what an attacker can achieve. A payload simply proving execution is often valued far less than one extracting session cookies, bypassing CSRF protections to commandeer accounts, or achieving horizontal privilege escalation against enterprise tenants.

It is harder to find than beginners expect because basic scanning tools only test naive context. Most tools fail to understand single-page application router states, DOM-based sinks that only trigger upon user interaction, or WAF evasions requiring parameter pollution and exotic encodings. Mastering this area requires understanding the application exactly as the developer did, navigating the architectural nuances, and locating the specific context where validation logic breaks down.
## Top 10 Reports Hall of Fame

| Rank | ID | Program | Severity | Bounty | Sub-type | Summary |
|------|----|---------|----------|--------|----------|---------|
| 1 | [Report #1618347](https://hackerone.com/reports/1618347) | HackerOne | Critical | $25,000 | PII Exposure | Disclosing  PolicyPageAssetGroup... |
| 2 | [Report #1707287](https://hackerone.com/reports/1707287) | Internet Bug Bounty | Critical | $8,000 | Internal IP/Infrastructure | CVE-2022-40604: Apache... |
| 3 | [Report #2915647](https://hackerone.com/reports/2915647) | Mozilla | Critical | $6,000 | API Key/Secret Exposure | Netlify Authentication Token... |
| 4 | [Report #2505761](https://hackerone.com/reports/2505761) | GitHub | Medium | $4,000 | General | Information Leakage via Clicked Link... |
| 5 | [Report #2798380](https://hackerone.com/reports/2798380) | HackerOne | Critical | $2,500 | PII Exposure | Hackerone supports accounts... |
| 6 | [Report #2552205](https://hackerone.com/reports/2552205) | HackerOne | Medium | $2,500 | Internal IP/Infrastructure | Private draft report exposure in... |
| 7 | [Report #3082917](https://hackerone.com/reports/3082917) | Internet Bug Bounty | High | $2,162 | General | Possible Sensitive... |
| 8 | [Report #2828271](https://hackerone.com/reports/2828271) | Internet Bug Bounty | Medium | $541 | API Key/Secret Exposure | Apache Airflow:... |
| 9 | [Report #2894283](https://hackerone.com/reports/2894283) | Internet Bug Bounty | Low | $505 | API Key/Secret Exposure | netrc and redirect... |
| 10 | [Report #2401648](https://hackerone.com/reports/2401648) | Mozilla | Critical | $500 | API Key/Secret Exposure | two aws access key and secret key... |

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
