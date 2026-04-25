---
vuln_type: "Type_Confusion"
file_type: "readme"
total_reports: "50"
avg_bounty: "0"
max_bounty: "0"
severity_distribution: "critical:0% high:0% medium:0% low:100%"
owasp_categories: ["A00:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["Type_Confusion", "web", "api", "A00", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---


# Type Confusion — Complete Hunter's Reference

Type Confusion represents a critical security oversight in implementing type confusion paradigms. Attackers exploit gaps in input validation, output encoding, or authorization to manipulate application state, accessing data or capabilities designated for other security boundaries.

> [!NOTE] Corpus Statistics
> **Total reports analyzed:** 50
> **Average bounty:** $0
> **Highest bounty on record:** $0 — [Report #108682](https://hackerone.com/reports/108682) if 50 > 0 else 'N/A'
> **Dominant severity:** Low (100% of reports)
> **Most affected industry:** ecommerce (2% of reports)
> **OWASP category:** A00:2021 — Vulnerability
> **Most common CWE:** CWE-000 (Improper Handling)

## Quick Navigation

| File | What's Inside |
|------|--------------|
| [[theory\|Theory]] | All variants, root causes, how it works at code level |
| [[attack-scenarios\|Attack Scenarios]] | 6 distinct scenarios with step-by-step instructions |
| [[payloads\|Payloads]] | Complete payload library — 0 payloads |
| [[hunting-methodology\|Hunting Methodology]] | 6-phase step-by-step hunting workflow |
| [[tools\|Tools]] | 1 tools with exact commands |
| [[bypasses\|Bypasses]] | 1 bypass techniques for WAFs, filters, CSP |
| [[chaining\|Chaining]] | 3+ chain patterns with other vulnerabilities |
| [[reports-index\|Reports Index]] | All 50 reports sorted by bounty |
| [[cheatsheet\|Cheatsheet]] | One-page quick reference for active hunts |

## Why This Matters (Hunter's Perspective)

This vulnerability is incredibly prevalent across modern web architectures. Despite modern web frameworks offering out-of-the-box protections, it consistently manifests due to business logic complexities, edge-case API routing, and third-party integrations taking over rendering or processing flows. The statistical corpus shows 50 reports, making it one of the most prolific findings available for a modern bug hunter.

What separates a $100 finding from a $10,000 payload is business impact. The programs paying the highest bounties (like Node.js third-party modules and others in the ecommerce industry) evaluate findings not just on technical reproducibility, but on what an attacker can achieve. A payload simply proving execution is often valued far less than one extracting session cookies, bypassing CSRF protections to commandeer accounts, or achieving horizontal privilege escalation against enterprise tenants.

It is harder to find than beginners expect because basic scanning tools only test naive context. Most tools fail to understand single-page application router states, DOM-based sinks that only trigger upon user interaction, or WAF evasions requiring parameter pollution and exotic encodings. Mastering this area requires understanding the application exactly as the developer did, navigating the architectural nuances, and locating the specific context where validation logic breaks down.

 This vulnerability class represents a critical breakdown in software architecture.

## Top 10 Reports Hall of Fame

| Rank | ID | Program | Severity | Bounty | Sub-type | Summary |
|------|----|---------|----------|--------|----------|---------|
| 1 | [Report #108682](https://hackerone.com/reports/108682) | Internet Bug Bounty | Low | N/A | General | Type Confusion... |
| 2 | [Report #114339](https://hackerone.com/reports/114339) | Internet Bug Bounty | Low | N/A | General | Type Confusion in WDDX... |
| 3 | [Report #116773](https://hackerone.com/reports/116773) | Internet Bug Bounty | Low | N/A | General | Type Confusion... |
| 4 | [Report #1431042](https://hackerone.com/reports/1431042) | Node.js | Low | N/A | General | Prototype pollution via... |
| 5 | [Report #159943](https://hackerone.com/reports/159943) | Internet Bug Bounty | Low | N/A | General | Create an Unexpected... |
| 6 | [Report #181871](https://hackerone.com/reports/181871) | shopify-scripts | Low | N/A | General | DoS: type confusion in... |
| 7 | [Report #198733](https://hackerone.com/reports/198733) | Internet Bug Bounty | Low | N/A | General | Type Confusion in... |
| 8 | [Report #2271095](https://hackerone.com/reports/2271095) | Internet Bug Bounty | Low | N/A | General | ASAR Integrity bypass... |
| 9 | [Report #310439](https://hackerone.com/reports/310439) | Node.js third-party modul | Low | N/A | General | Prototype... |
| 10 | [Report #310443](https://hackerone.com/reports/310443) | Node.js third-party modul | Low | N/A | General | Prototype... |

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
