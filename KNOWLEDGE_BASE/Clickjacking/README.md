---
vuln_type: "Clickjacking"
file_type: "readme"
total_reports: "94"
avg_bounty: "200"
max_bounty: "200"
severity_distribution: "critical:1% high:1% medium:3% low:95%"
owasp_categories: ["A00:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["Clickjacking", "web", "api", "A00", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---


# Clickjacking — Complete Hunter's Reference

Clickjacking represents a critical security oversight in implementing clickjacking paradigms. Attackers exploit gaps in input validation, output encoding, or authorization to manipulate application state, accessing data or capabilities designated for other security boundaries.

> [!NOTE] Corpus Statistics
> **Total reports analyzed:** 94
> **Average bounty:** $200
> **Highest bounty on record:** $200 — [Report #2119892](https://hackerone.com/reports/2119892) if 94 > 0 else 'N/A'
> **Dominant severity:** Low (95% of reports)
> **Most affected industry:** saas (8% of reports)
> **OWASP category:** A00:2021 — Vulnerability
> **Most common CWE:** CWE-000 (Improper Handling)

## Quick Navigation

| File | What's Inside |
|------|--------------|
| [[theory\|Theory]] | All variants, root causes, how it works at code level |
| [[attack-scenarios\|Attack Scenarios]] | 6 distinct scenarios with step-by-step instructions |
| [[payloads\|Payloads]] | Complete payload library — 4 payloads |
| [[hunting-methodology\|Hunting Methodology]] | 6-phase step-by-step hunting workflow |
| [[tools\|Tools]] | 1 tools with exact commands |
| [[bypasses\|Bypasses]] | 1 bypass techniques for WAFs, filters, CSP |
| [[chaining\|Chaining]] | 3+ chain patterns with other vulnerabilities |
| [[reports-index\|Reports Index]] | All 94 reports sorted by bounty |
| [[cheatsheet\|Cheatsheet]] | One-page quick reference for active hunts |

## Why This Matters (Hunter's Perspective)

This vulnerability is incredibly prevalent across modern web architectures. Despite modern web frameworks offering out-of-the-box protections, it consistently manifests due to business logic complexities, edge-case API routing, and third-party integrations taking over rendering or processing flows. The statistical corpus shows 94 reports, making it one of the most prolific findings available for a modern bug hunter.

What separates a $100 finding from a $10,000 payload is business impact. The programs paying the highest bounties (like Yelp and others in the saas industry) evaluate findings not just on technical reproducibility, but on what an attacker can achieve. A payload simply proving execution is often valued far less than one extracting session cookies, bypassing CSRF protections to commandeer accounts, or achieving horizontal privilege escalation against enterprise tenants.

It is harder to find than beginners expect because basic scanning tools only test naive context. Most tools fail to understand single-page application router states, DOM-based sinks that only trigger upon user interaction, or WAF evasions requiring parameter pollution and exotic encodings. Mastering this area requires understanding the application exactly as the developer did, navigating the architectural nuances, and locating the specific context where validation logic breaks down.
## Top 10 Reports Hall of Fame

| Rank | ID | Program | Severity | Bounty | Sub-type | Summary |
|------|----|---------|----------|--------|----------|---------|
| 1 | [Report #2119892](https://hackerone.com/reports/2119892) | pixiv | Low | $200 | General | clickjacing can lead to account takeover |
| 2 | [Report #3287060](https://hackerone.com/reports/3287060) | WakaTime | Critical | N/A | General | Double Clickjacking Attack on... |
| 3 | [Report #2964441](https://hackerone.com/reports/2964441) | Top Echelon Software | High | N/A | General | Clickjacking in main... |
| 4 | [Report #1031525](https://hackerone.com/reports/1031525) | Rocket.Chat | Medium | N/A | General | User Impersonation through... |
| 5 | [Report #338569](https://hackerone.com/reports/338569) | Eternal | Medium | N/A | General | Clickjacking: Delete Account,... |
| 6 | [Report #1039805](https://hackerone.com/reports/1039805) | Nextcloud | Low | N/A | General | Clickjacking URLS |
| 7 | [Report #108056](https://hackerone.com/reports/108056) | HackerOne | Low | N/A | General | HackerOne is still prone to... |
| 8 | [Report #1176104](https://hackerone.com/reports/1176104) | Sifchain | Low | N/A | General | Clickjacking misconfiguration bug |
| 9 | [Report #1185949](https://hackerone.com/reports/1185949) | Sifchain | Low | N/A | General | Clickjacking Vulnerability in... |
| 10 | [Report #1188639](https://hackerone.com/reports/1188639) | Sifchain | Low | N/A | General | Vulnerable for clickjacking attack |

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
