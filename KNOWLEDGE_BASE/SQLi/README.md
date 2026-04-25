---
vuln_type: "SQLi"
file_type: "readme"
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


# SQLi — Complete Hunter's Reference

SQL Injection represents a failure to separate code from data in database queries. It occurs when untrusted input continuously concatenates into dynamic SQL statements instead of using parameterized bindings, allowing an attacker to manipulate the query structure, exfiltrate data, or even achieve RCE.

> [!NOTE] Corpus Statistics
> **Total reports analyzed:** 187
> **Average bounty:** $1,625
> **Highest bounty on record:** $4,263 — [Report #2646493](https://hackerone.com/reports/2646493) if 187 > 0 else 'N/A'
> **Dominant severity:** High (89% of reports)
> **Most affected industry:** gov (5% of reports)
> **OWASP category:** A03:2021 — Vulnerability
> **Most common CWE:** CWE-89 (Improper Handling)

## Quick Navigation

| File | What's Inside |
|------|--------------|
| [[theory\|Theory]] | All variants, root causes, how it works at code level |
| [[attack-scenarios\|Attack Scenarios]] | 13 distinct scenarios with step-by-step instructions |
| [[payloads\|Payloads]] | Complete payload library — 16 payloads |
| [[hunting-methodology\|Hunting Methodology]] | 6-phase step-by-step hunting workflow |
| [[tools\|Tools]] | 5 tools with exact commands |
| [[bypasses\|Bypasses]] | 2 bypass techniques for WAFs, filters, CSP |
| [[chaining\|Chaining]] | 3+ chain patterns with other vulnerabilities |
| [[reports-index\|Reports Index]] | All 187 reports sorted by bounty |
| [[cheatsheet\|Cheatsheet]] | One-page quick reference for active hunts |

## Why This Matters (Hunter's Perspective)

This vulnerability is incredibly prevalent across modern web architectures. Despite modern web frameworks offering out-of-the-box protections, it consistently manifests due to business logic complexities, edge-case API routing, and third-party integrations taking over rendering or processing flows. The statistical corpus shows 187 reports, making it one of the most prolific findings available for a modern bug hunter.

What separates a $100 finding from a $10,000 payload is business impact. The programs paying the highest bounties (like U.S. Dept Of Defense and others in the gov industry) evaluate findings not just on technical reproducibility, but on what an attacker can achieve. A payload simply proving execution is often valued far less than one extracting session cookies, bypassing CSRF protections to commandeer accounts, or achieving horizontal privilege escalation against enterprise tenants.

It is harder to find than beginners expect because basic scanning tools only test naive context. Most tools fail to understand single-page application router states, DOM-based sinks that only trigger upon user interaction, or WAF evasions requiring parameter pollution and exotic encodings. Mastering this area requires understanding the application exactly as the developer did, navigating the architectural nuances, and locating the specific context where validation logic breaks down.

 This vulnerability class represents a critical breakdown in software architecture.

## Top 10 Reports Hall of Fame

| Rank | ID | Program | Severity | Bounty | Sub-type | Summary |
|------|----|---------|----------|--------|----------|---------|
| 1 | [Report #2646493](https://hackerone.com/reports/2646493) | Internet Bug Bounty | Critical | $4,263 | NoSQL Injection | CVE-2024-42005:... |
| 2 | [Report #3078856](https://hackerone.com/reports/3078856) | Internet Bug Bounty | Low | $505 | General | Apache Airflow Sql... |
| 3 | [Report #2882887](https://hackerone.com/reports/2882887) | Internet Bug Bounty | High | $108 | NoSQL Injection | CVE-2024-53908: Django... |
| 4 | [Report #1436751](https://hackerone.com/reports/1436751) | Acronis | Critical | N/A | General | SQL injection in... |
| 5 | [Report #2588426](https://hackerone.com/reports/2588426) | Django | Critical | N/A | Error-based SQLi | SQL injection in JSONField KeyTransform |
| 6 | [Report #2597543](https://hackerone.com/reports/2597543) | U.S. Dept Of Defense | Critical | N/A | Blind Boolean SQLi | Blind Sql Injection in... |
| 7 | [Report #2633959](https://hackerone.com/reports/2633959) | corporate.admyntec.co.za | Critical | N/A | Second-order SQLi | SQL injection in URL path leads... |
| 8 | [Report #2737595](https://hackerone.com/reports/2737595) | U.S. Dept Of Defense | Critical | N/A | Blind Boolean SQLi | SQL Injection |
| 9 | [Report #2759243](https://hackerone.com/reports/2759243) | U.S. Dept Of Defense | Critical | N/A | Blind Boolean SQLi | Time-based blind SQL... |
| 10 | [Report #2830573](https://hackerone.com/reports/2830573) | IBM | Critical | N/A | General | SQL injection identified on IBM endpoint. |

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
