---
vuln_type: "HTTP_Request_Smuggling"
file_type: "readme"
total_reports: "105"
avg_bounty: "0"
max_bounty: "0"
severity_distribution: "critical:0% high:2% medium:7% low:91%"
owasp_categories: ["A00:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["HTTP_Request_Smuggling", "web", "api", "A00", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---


# HTTP Request Smuggling — Complete Hunter's Reference

HTTP Request Smuggling represents a critical security oversight in implementing http request smuggling paradigms. Attackers exploit gaps in input validation, output encoding, or authorization to manipulate application state, accessing data or capabilities designated for other security boundaries.

> [!NOTE] Corpus Statistics
> **Total reports analyzed:** 105
> **Average bounty:** $0
> **Highest bounty on record:** $0 — [Report #3479984](https://hackerone.com/reports/3479984) if 105 > 0 else 'N/A'
> **Dominant severity:** Low (91% of reports)
> **Most affected industry:** infra (5% of reports)
> **OWASP category:** A00:2021 — Vulnerability
> **Most common CWE:** CWE-000 (Improper Handling)

## Quick Navigation

| File | What's Inside |
|------|--------------|
| [[theory\|Theory]] | All variants, root causes, how it works at code level |
| [[attack-scenarios\|Attack Scenarios]] | 6 distinct scenarios with step-by-step instructions |
| [[payloads\|Payloads]] | Complete payload library — 12 payloads |
| [[hunting-methodology\|Hunting Methodology]] | 6-phase step-by-step hunting workflow |
| [[tools\|Tools]] | 4 tools with exact commands |
| [[bypasses\|Bypasses]] | 3 bypass techniques for WAFs, filters, CSP |
| [[chaining\|Chaining]] | 3+ chain patterns with other vulnerabilities |
| [[reports-index\|Reports Index]] | All 105 reports sorted by bounty |
| [[cheatsheet\|Cheatsheet]] | One-page quick reference for active hunts |

## Why This Matters (Hunter's Perspective)

This vulnerability is incredibly prevalent across modern web architectures. Despite modern web frameworks offering out-of-the-box protections, it consistently manifests due to business logic complexities, edge-case API routing, and third-party integrations taking over rendering or processing flows. The statistical corpus shows 105 reports, making it one of the most prolific findings available for a modern bug hunter.

What separates a $100 finding from a $10,000 payload is business impact. The programs paying the highest bounties (like Node.js and others in the infra industry) evaluate findings not just on technical reproducibility, but on what an attacker can achieve. A payload simply proving execution is often valued far less than one extracting session cookies, bypassing CSRF protections to commandeer accounts, or achieving horizontal privilege escalation against enterprise tenants.

It is harder to find than beginners expect because basic scanning tools only test naive context. Most tools fail to understand single-page application router states, DOM-based sinks that only trigger upon user interaction, or WAF evasions requiring parameter pollution and exotic encodings. Mastering this area requires understanding the application exactly as the developer did, navigating the architectural nuances, and locating the specific context where validation logic breaks down.
## Top 10 Reports Hall of Fame

| Rank | ID | Program | Severity | Bounty | Sub-type | Summary |
|------|----|---------|----------|--------|----------|---------|
| 1 | [Report #3479984](https://hackerone.com/reports/3479984) | curl | Critical | N/A | General | CRLF Injection / Protocol Smuggling in... |
| 2 | [Report #1623672](https://hackerone.com/reports/1623672) | Enjin | High | N/A | General | Host header injection leads to... |
| 3 | [Report #2861797](https://hackerone.com/reports/2861797) | curl | High | N/A | General | curl mishandles `%0c%0b` sequences in... |
| 4 | [Report #3514263](https://hackerone.com/reports/3514263) | curl | High | N/A | General | libcurl: Improper Authentication State... |
| 5 | [Report #2054283](https://hackerone.com/reports/2054283) | Node.js | Medium | N/A | General | Improper HTTP header block... |
| 6 | [Report #2627221](https://hackerone.com/reports/2627221) | RubyGems | Medium | N/A | General | Host Header Attac |
| 7 | [Report #2864859](https://hackerone.com/reports/2864859) | curl | Medium | N/A | General | -H with space prefix leads to previous... |
| 8 | [Report #3235428](https://hackerone.com/reports/3235428) | curl | Medium | N/A | General | CRLF injection in libcurl's SMTP... |
| 9 | [Report #3484506](https://hackerone.com/reports/3484506) | curl | Medium | N/A | General | CRLF Injection in Gopher Protocol... |
| 10 | [Report #1002188](https://hackerone.com/reports/1002188) | Node.js | Low | N/A | General | Potential HTTP Request Smuggling in... |

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
