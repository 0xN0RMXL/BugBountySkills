---
vuln_type: "GraphQL"
file_type: "readme"
total_reports: "62"
avg_bounty: "0"
max_bounty: "0"
severity_distribution: "critical:0% high:0% medium:0% low:100%"
owasp_categories: ["A00:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["GraphQL", "web", "api", "A00", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---


# GraphQL — Complete Hunter's Reference

GraphQL represents a critical security oversight in implementing graphql paradigms. Attackers exploit gaps in input validation, output encoding, or authorization to manipulate application state, accessing data or capabilities designated for other security boundaries.

> [!NOTE] Corpus Statistics
> **Total reports analyzed:** 62
> **Average bounty:** $0
> **Highest bounty on record:** $0 — [Report #1000567](https://hackerone.com/reports/1000567) if 62 > 0 else 'N/A'
> **Dominant severity:** Low (100% of reports)
> **Most affected industry:** ecommerce (25% of reports)
> **OWASP category:** A00:2021 — Vulnerability
> **Most common CWE:** CWE-000 (Improper Handling)

## Quick Navigation

| File | What's Inside |
|------|--------------|
| [[theory\|Theory]] | All variants, root causes, how it works at code level |
| [[attack-scenarios\|Attack Scenarios]] | 6 distinct scenarios with step-by-step instructions |
| [[payloads\|Payloads]] | Complete payload library — 5 payloads |
| [[hunting-methodology\|Hunting Methodology]] | 6-phase step-by-step hunting workflow |
| [[tools\|Tools]] | 1 tools with exact commands |
| [[bypasses\|Bypasses]] | 2 bypass techniques for WAFs, filters, CSP |
| [[chaining\|Chaining]] | 3+ chain patterns with other vulnerabilities |
| [[reports-index\|Reports Index]] | All 62 reports sorted by bounty |
| [[cheatsheet\|Cheatsheet]] | One-page quick reference for active hunts |

## Why This Matters (Hunter's Perspective)

This vulnerability is incredibly prevalent across modern web architectures. Despite modern web frameworks offering out-of-the-box protections, it consistently manifests due to business logic complexities, edge-case API routing, and third-party integrations taking over rendering or processing flows. The statistical corpus shows 62 reports, making it one of the most prolific findings available for a modern bug hunter.

What separates a $100 finding from a $10,000 payload is business impact. The programs paying the highest bounties (like HackerOne and others in the ecommerce industry) evaluate findings not just on technical reproducibility, but on what an attacker can achieve. A payload simply proving execution is often valued far less than one extracting session cookies, bypassing CSRF protections to commandeer accounts, or achieving horizontal privilege escalation against enterprise tenants.

It is harder to find than beginners expect because basic scanning tools only test naive context. Most tools fail to understand single-page application router states, DOM-based sinks that only trigger upon user interaction, or WAF evasions requiring parameter pollution and exotic encodings. Mastering this area requires understanding the application exactly as the developer did, navigating the architectural nuances, and locating the specific context where validation logic breaks down.
## Top 10 Reports Hall of Fame

| Rank | ID | Program | Severity | Bounty | Sub-type | Summary |
|------|----|---------|----------|--------|----------|---------|
| 1 | [Report #1000567](https://hackerone.com/reports/1000567) | CS Money | Low | N/A | General | ReDoS at wiki.cs.money graphQL... |
| 2 | [Report #1023669](https://hackerone.com/reports/1023669) | Shopify | Low | N/A | General | Staff with no permissions can... |
| 3 | [Report #1044869](https://hackerone.com/reports/1044869) | Shopify | Low | N/A | General | Staff with no permissions could... |
| 4 | [Report #1084892](https://hackerone.com/reports/1084892) | Shopify | Low | N/A | General | [h1-2102] [Plus] User with Store... |
| 5 | [Report #1084904](https://hackerone.com/reports/1084904) | Shopify | Low | N/A | General | [h1-2102] [Plus] User with Store... |
| 6 | [Report #1102652](https://hackerone.com/reports/1102652) | Shopify | Low | N/A | General | ... |
| 7 | [Report #1132803](https://hackerone.com/reports/1132803) | On | Low | N/A | General | Graphql introspection is enabled and... |
| 8 | [Report #1138668](https://hackerone.com/reports/1138668) | HackerOne | Low | N/A | General | The possibility of disrupting the... |
| 9 | [Report #1192460](https://hackerone.com/reports/1192460) | GitLab | Low | N/A | General | A deactivated user can access data... |
| 10 | [Report #1276992](https://hackerone.com/reports/1276992) | HackerOne | Low | N/A | General | Disclosure handle private program... |

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
