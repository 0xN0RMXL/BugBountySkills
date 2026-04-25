---
vuln_type: "Account_Takeover"
file_type: "readme"
total_reports: "90"
avg_bounty: "87"
max_bounty: "125"
severity_distribution: "critical:3% high:3% medium:92% low:2%"
owasp_categories: ["A00:2021"]
common_cwe: ["CWE-000"]
last_updated: "2026-04-09"
tags: ["Account_Takeover", "web", "api", "A00", "hunter-kb"]
related_vulns: ["Information_Disclosure", "Broken_Access_Control", "SSRF"]
---


# Account Takeover — Complete Hunter's Reference

Account Takeover represents a critical security oversight in implementing account takeover paradigms. Attackers exploit gaps in input validation, output encoding, or authorization to manipulate application state, accessing data or capabilities designated for other security boundaries.

> [!NOTE] Corpus Statistics
> **Total reports analyzed:** 90
> **Average bounty:** $87
> **Highest bounty on record:** $125 — [Report #1387366](https://hackerone.com/reports/1387366) if 90 > 0 else 'N/A'
> **Dominant severity:** Medium (91% of reports)
> **Most affected industry:** ecommerce (8% of reports)
> **OWASP category:** A00:2021 — Vulnerability
> **Most common CWE:** CWE-000 (Improper Handling)

## Quick Navigation

| File | What's Inside |
|------|--------------|
| [[theory\|Theory]] | All variants, root causes, how it works at code level |
| [[attack-scenarios\|Attack Scenarios]] | 6 distinct scenarios with step-by-step instructions |
| [[payloads\|Payloads]] | Complete payload library — 2 payloads |
| [[hunting-methodology\|Hunting Methodology]] | 6-phase step-by-step hunting workflow |
| [[tools\|Tools]] | 2 tools with exact commands |
| [[bypasses\|Bypasses]] | 1 bypass techniques for WAFs, filters, CSP |
| [[chaining\|Chaining]] | 3+ chain patterns with other vulnerabilities |
| [[reports-index\|Reports Index]] | All 90 reports sorted by bounty |
| [[cheatsheet\|Cheatsheet]] | One-page quick reference for active hunts |

## Why This Matters (Hunter's Perspective)

This vulnerability is incredibly prevalent across modern web architectures. Despite modern web frameworks offering out-of-the-box protections, it consistently manifests due to business logic complexities, edge-case API routing, and third-party integrations taking over rendering or processing flows. The statistical corpus shows 90 reports, making it one of the most prolific findings available for a modern bug hunter.

What separates a $100 finding from a $10,000 payload is business impact. The programs paying the highest bounties (like U.S. Dept Of Defense and others in the ecommerce industry) evaluate findings not just on technical reproducibility, but on what an attacker can achieve. A payload simply proving execution is often valued far less than one extracting session cookies, bypassing CSRF protections to commandeer accounts, or achieving horizontal privilege escalation against enterprise tenants.

It is harder to find than beginners expect because basic scanning tools only test naive context. Most tools fail to understand single-page application router states, DOM-based sinks that only trigger upon user interaction, or WAF evasions requiring parameter pollution and exotic encodings. Mastering this area requires understanding the application exactly as the developer did, navigating the architectural nuances, and locating the specific context where validation logic breaks down.

## Top 10 Reports Hall of Fame

| Rank | ID | Program | Severity | Bounty | Sub-type | Summary |
|------|----|---------|----------|--------|----------|---------|
| 1 | [Report #1387366](https://hackerone.com/reports/1387366) | Kubernetes | Critical | $125 | General | elections.k8s.io uses weak... |
| 2 | [Report #3062299](https://hackerone.com/reports/3062299) | Hiro | Medium | $50 | General | Logout Bypass Vulnerability in Hiro.so |
| 3 | [Report #3378635](https://hackerone.com/reports/3378635) | lemlist | Critical | N/A | General | Unauthorized Password Reset Allows... |
| 4 | [Report #3479203](https://hackerone.com/reports/3479203) | curl | Critical | N/A | General | HTTP/3 Protocol Smuggling and Header... |
| 5 | [Report #2928785](https://hackerone.com/reports/2928785) | U.S. Dept Of Defense | High | N/A | General | ASP.NET Application... |
| 6 | [Report #3161827](https://hackerone.com/reports/3161827) | Shopify | High | N/A | General | Session Persistence Designed to... |
| 7 | [Report #3295652](https://hackerone.com/reports/3295652) | curl | High | N/A | General | Insecure WebSocket Usage in curl... |
| 8 | [Report #1004536](https://hackerone.com/reports/1004536) | Weblate | Medium | N/A | General | Reset password cookie leads to... |
| 9 | [Report #1046630](https://hackerone.com/reports/1046630) | Logitech | Medium | N/A | General | One Click Account takeover using... |
| 10 | [Report #1058015](https://hackerone.com/reports/1058015) | U.S. Dept Of Defense | Medium | N/A | General | Full account takeover... |

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
