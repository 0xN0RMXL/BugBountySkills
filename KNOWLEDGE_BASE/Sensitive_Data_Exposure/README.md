---
vuln_type: "Sensitive_Data_Exposure"
file_type: "readme"
total_reports: "234"
avg_bounty: "1877"
max_bounty: "15000"
severity_distribution: "critical:3% high:8% medium:15% low:74%"
owasp_categories: ["A02:2021"]
common_cwe: ["CWE-200"]
last_updated: "2026-04-09"
tags: ["Sensitive_Data_Exposure", "web", "api", "A02", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---


# Sensitive Data Exposure — Complete Hunter's Reference

Sensitive Data Exposure represents a critical security oversight in implementing sensitive data exposure paradigms. Attackers exploit gaps in input validation, output encoding, or authorization to manipulate application state, accessing data or capabilities designated for other security boundaries.

> [!NOTE] Corpus Statistics
> **Total reports analyzed:** 234
> **Average bounty:** $1,877
> **Highest bounty on record:** $15,000 — [Report #3018307](https://hackerone.com/reports/3018307) if 234 > 0 else 'N/A'
> **Dominant severity:** Low (74% of reports)
> **Most affected industry:** saas (17% of reports)
> **OWASP category:** A02:2021 — Vulnerability
> **Most common CWE:** CWE-200 (Improper Handling)

## Quick Navigation

| File | What's Inside |
|------|--------------|
| [[theory\|Theory]] | All variants, root causes, how it works at code level |
| [[attack-scenarios\|Attack Scenarios]] | 6 distinct scenarios with step-by-step instructions |
| [[payloads\|Payloads]] | Complete payload library — 12 payloads |
| [[hunting-methodology\|Hunting Methodology]] | 6-phase step-by-step hunting workflow |
| [[tools\|Tools]] | 3 tools with exact commands |
| [[bypasses\|Bypasses]] | 2 bypass techniques for WAFs, filters, CSP |
| [[chaining\|Chaining]] | 3+ chain patterns with other vulnerabilities |
| [[reports-index\|Reports Index]] | All 234 reports sorted by bounty |
| [[cheatsheet\|Cheatsheet]] | One-page quick reference for active hunts |

## Why This Matters (Hunter's Perspective)

This vulnerability is incredibly prevalent across modern web architectures. Despite modern web frameworks offering out-of-the-box protections, it consistently manifests due to business logic complexities, edge-case API routing, and third-party integrations taking over rendering or processing flows. The statistical corpus shows 234 reports, making it one of the most prolific findings available for a modern bug hunter.

What separates a $100 finding from a $10,000 payload is business impact. The programs paying the highest bounties (like Nextcloud and others in the saas industry) evaluate findings not just on technical reproducibility, but on what an attacker can achieve. A payload simply proving execution is often valued far less than one extracting session cookies, bypassing CSRF protections to commandeer accounts, or achieving horizontal privilege escalation against enterprise tenants.

It is harder to find than beginners expect because basic scanning tools only test naive context. Most tools fail to understand single-page application router states, DOM-based sinks that only trigger upon user interaction, or WAF evasions requiring parameter pollution and exotic encodings. Mastering this area requires understanding the application exactly as the developer did, navigating the architectural nuances, and locating the specific context where validation logic breaks down.

 This vulnerability class represents a critical breakdown in software architecture.

## Top 10 Reports Hall of Fame

| Rank | ID | Program | Severity | Bounty | Sub-type | Summary |
|------|----|---------|----------|--------|----------|---------|
| 1 | [Report #3018307](https://hackerone.com/reports/3018307) | Cosmos | Critical | $15,000 | General | Groups module can halt chain when... |
| 2 | [Report #2105808](https://hackerone.com/reports/2105808) | Rootstock Labs | High | $5,000 | General | DOS of RSKJ server |
| 3 | [Report #2520679](https://hackerone.com/reports/2520679) | Internet Bug Bounty | High | $4,920 | General | Possible DoS... |
| 4 | [Report #2591681](https://hackerone.com/reports/2591681) | Internet Bug Bounty | Medium | $2,142 | General | CVE-2024-38875:... |
| 5 | [Report #2644244](https://hackerone.com/reports/2644244) | Internet Bug Bounty | Medium | $2,142 | General | CVE-2024-41989:... |
| 6 | [Report #2930811](https://hackerone.com/reports/2930811) | Cosmos | Critical | $2,000 | General | Attacker can use any non-enabled... |
| 7 | [Report #2939077](https://hackerone.com/reports/2939077) | Internet Bug Bounty | Medium | $541 | General | CVE-2024-56374... |
| 8 | [Report #1848940](https://hackerone.com/reports/1848940) | Shopify | Low | $500 | General | URL Path Manipulation Enables Cache... |
| 9 | [Report #2622671](https://hackerone.com/reports/2622671) | Internet Bug Bounty | Medium | $497 | General | Unbounded memory growth... |
| 10 | [Report #1003007](https://hackerone.com/reports/1003007) | Acronis | High | $250 | General | Local Privilege Escalation via... |

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
