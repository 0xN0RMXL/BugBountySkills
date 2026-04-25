---
vuln_type: "CORS_Misconfiguration"
file_type: "readme"
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


# CORS Misconfiguration — Complete Hunter's Reference

CORS Misconfiguration represents a critical security oversight in implementing cors misconfiguration paradigms. Attackers exploit gaps in input validation, output encoding, or authorization to manipulate application state, accessing data or capabilities designated for other security boundaries.

> [!NOTE] Corpus Statistics
> **Total reports analyzed:** 18
> **Average bounty:** $0
> **Highest bounty on record:** $0 — [Report #1092125](https://hackerone.com/reports/1092125) if 18 > 0 else 'N/A'
> **Dominant severity:** Low (100% of reports)
> **Most affected industry:** crypto (5% of reports)
> **OWASP category:** A00:2021 — Vulnerability
> **Most common CWE:** CWE-000 (Improper Handling)

## Quick Navigation

| File | What's Inside |
|------|--------------|
| [[theory\|Theory]] | All variants, root causes, how it works at code level |
| [[attack-scenarios\|Attack Scenarios]] | 6 distinct scenarios with step-by-step instructions |
| [[payloads\|Payloads]] | Complete payload library — 4 payloads |
| [[hunting-methodology\|Hunting Methodology]] | 6-phase step-by-step hunting workflow |
| [[tools\|Tools]] | 2 tools with exact commands |
| [[bypasses\|Bypasses]] | 1 bypass techniques for WAFs, filters, CSP |
| [[chaining\|Chaining]] | 3+ chain patterns with other vulnerabilities |
| [[reports-index\|Reports Index]] | All 18 reports sorted by bounty |
| [[cheatsheet\|Cheatsheet]] | One-page quick reference for active hunts |

## Why This Matters (Hunter's Perspective)

This vulnerability is incredibly prevalent across modern web architectures. Despite modern web frameworks offering out-of-the-box protections, it consistently manifests due to business logic complexities, edge-case API routing, and third-party integrations taking over rendering or processing flows. The statistical corpus shows 18 reports, making it one of the most prolific findings available for a modern bug hunter.

What separates a $100 finding from a $10,000 payload is business impact. The programs paying the highest bounties (like U.S. Dept Of Defense and others in the crypto industry) evaluate findings not just on technical reproducibility, but on what an attacker can achieve. A payload simply proving execution is often valued far less than one extracting session cookies, bypassing CSRF protections to commandeer accounts, or achieving horizontal privilege escalation against enterprise tenants.

It is harder to find than beginners expect because basic scanning tools only test naive context. Most tools fail to understand single-page application router states, DOM-based sinks that only trigger upon user interaction, or WAF evasions requiring parameter pollution and exotic encodings. Mastering this area requires understanding the application exactly as the developer did, navigating the architectural nuances, and locating the specific context where validation logic breaks down.
## Top 10 Reports Hall of Fame

| Rank | ID | Program | Severity | Bounty | Sub-type | Summary |
|------|----|---------|----------|--------|----------|---------|
| 1 | [Report #1092125](https://hackerone.com/reports/1092125) | U.S. Dept Of Defense | Low | N/A | General | Bypassing CORS... |
| 2 | [Report #1183601](https://hackerone.com/reports/1183601) | UPchieve | Low | N/A | General | Cross-origin resource sharing... |
| 3 | [Report #1188471](https://hackerone.com/reports/1188471) | Sifchain | Low | N/A | General | CORS (Cross-Origin Resource... |
| 4 | [Report #1189363](https://hackerone.com/reports/1189363) | Sifchain | Low | N/A | General | Cross Origin Resource Sharing... |
| 5 | [Report #176308](https://hackerone.com/reports/176308) | Automattic | Low | N/A | General | Wordpress.com REST API oauth... |
| 6 | [Report #235200](https://hackerone.com/reports/235200) | Semrush | Low | N/A | General | Cross-origin resource sharing... |
| 7 | [Report #269184](https://hackerone.com/reports/269184) | Hiro | Low | N/A | General | Weak crossdomain.xml |
| 8 | [Report #288912](https://hackerone.com/reports/288912) | Semrush | Low | N/A | General | Cross-origin resource sharing |
| 9 | [Report #310579](https://hackerone.com/reports/310579) | Semrush | Low | N/A | General | CORS (Cross-Origin Resource Sharing) |
| 10 | [Report #311805](https://hackerone.com/reports/311805) | Semrush | Low | N/A | General | Cross-origin resource sharing... |

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
